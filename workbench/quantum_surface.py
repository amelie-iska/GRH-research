"""Independent CPU/controller and optional genuine cuStateVec surface checks.

The controller is classical. The circuit acts on the already specified 18-qubit
CSS state, not a quantum state inferred from a cosmological signal. Existing GPU
libraries are reused without installation or changes to unrelated environments.
"""
from __future__ import annotations
import argparse,hashlib,json,math,sys,time
from pathlib import Path
import numpy as np

ROOT=Path(__file__).resolve().parents[1]
MODEL=ROOT/'extension/site/data/torus3x3.json'
DEFAULT=dict(qx=.7,qy=-.4,mode='maxplus',tau=.35,gain=.6,base=[.35,-.2,.25,-.3],signs=[1,1,1,1])


def configuration(raw):
    if type(raw)is not dict:raise ValueError('Configuration dictionary required')
    c={}
    for name,low,high in [('qx',-3,3),('qy',-3,3),('tau',.02,2),('gain',0,1)]:
        value=raw[name]
        if type(value)not in (int,float)or not math.isfinite(value)or not low<=value<=high:raise ValueError('Invalid '+name)
        c[name]=float(value)
    c['mode']=raw['mode']
    if c['mode']not in ('softmax','hard','maxplus'):raise ValueError('Unknown attention operator')
    if type(raw['base'])is not list or len(raw['base'])!=4 or any(type(x)not in(int,float)or not math.isfinite(x)or abs(x)>math.pi for x in raw['base']):raise ValueError('Four bounded angles required')
    if type(raw['signs'])is not list or len(raw['signs'])!=4 or any(type(x)is not int or x not in(-1,1)for x in raw['signs']):raise ValueError('Four exact signs required')
    c['base']=list(map(float,raw['base']));c['signs']=raw['signs'].copy();return c


def controller(model,raw):
    c=configuration(raw)
    uv=np.array([[2*math.pi*e['x']/3,2*math.pi*e['y']/3]for e in model['edges']])
    u,v=uv.T;keys=np.column_stack((np.cos(u),np.sin(v)))
    values=np.column_stack((np.sin(u),np.cos(u),np.sin(v),np.cos(v)))
    scores=(c['qx']*keys[:,0]+c['qy']*keys[:,1])/math.sqrt(2);top=float(scores.max())
    exp=np.exp((scores-top)/c['tau']);soft=exp/exp.sum()
    if c['mode']=='maxplus':output=(scores[:,None]+values).max(0)-top
    elif c['mode']=='hard':output=values[scores==top].mean(0)
    else:output=soft@values
    theta=np.array(c['base'])+c['gain']*output
    return dict(config=c,scores=scores.tolist(),output=output.tolist(),theta=theta.tolist(),analytic_expectation=float(np.prod(c['signs'])*np.cos(theta).prod()))


def circuit_gates(model,raw):
    a=controller(model,raw);patch=model['x_checks'][0]['qubits']
    return [dict(gate='RY',target=q,angle=s*math.pi/2+t)for q,s,t in zip(patch,a['config']['signs'],a['theta'])]+[dict(gate='CX',control=q,target=patch[0])for q in patch[1:]]


def apply_cpu(state,gate):
    n=state.size;indices=np.arange(n,dtype=np.uint32)
    op=gate['gate'];q=gate['target'];bit=1<<q
    if op=='CX':
        selected=indices[((indices>>gate['control'])&1).astype(bool)&((indices&bit)==0)];other=selected|bit
        a=state[selected].copy();state[selected]=state[other];state[other]=a;return
    if op not in ('H','RY'):raise ValueError('Independent CPU reference only uses H, RY, CX')
    selected=indices[(indices&bit)==0];other=selected|bit;a=state[selected].copy();b=state[other].copy()
    if op=='H':state[selected]=(a+b)/math.sqrt(2);state[other]=(a-b)/math.sqrt(2)
    else:
        c=math.cos(gate['angle']/2);s=math.sin(gate['angle']/2)
        state[selected]=c*a-s*b;state[other]=s*a+c*b


def cpu_state(model,raw=None):
    state=np.zeros(1<<model['n'],dtype=np.complex128);state[0]=1
    for gate in model['prepare_circuit']:apply_cpu(state,gate)
    if raw is not None:
        for gate in circuit_gates(model,raw):apply_cpu(state,gate)
    return state


def observable(state,support,pauli):
    indices=np.arange(state.size,dtype=np.uint32);mask=sum(1<<q for q in support)
    if pauli=='X':return float(np.vdot(state,state[indices^mask]).real)
    signs=np.ones(state.size)
    for q in support:signs*=1-2*((indices>>q)&1).astype(np.int8)
    return float(np.dot(abs(state)**2,signs))


def execute_cpu(model,raw):
    state=cpu_state(model,raw);patch=model['x_checks'][0]['qubits'];indices=np.arange(state.size,dtype=np.uint32)
    labels=sum(((indices>>q)&1)<<i for i,q in enumerate(patch));prob=np.bincount(labels,weights=abs(state)**2,minlength=16)
    x=[observable(state,c['qubits'],'X')for c in model['x_checks']];z=[observable(state,c['qubits'],'Z')for c in model['z_checks']]
    return dict(expectation=observable(state,[patch[0]],'Z'),norm2=float(np.vdot(state,state).real),probability=prob.tolist(),x_checks=x,z_checks=z,energy=-sum(x)-sum(z),controller=controller(model,raw))


def verify_gpu(model,cases):
    # Import the previously validated backend, not a CPU shim labelled GPU.
    sys.path.insert(0,str(ROOT/'extension/quantum'))
    from gpu_experiments import StateVector,environment
    import cupy as cp
    info=environment();state=StateVector(18,precision='complex128');rows=[];patch=model['x_checks'][0]['qubits']
    try:
        state.circuit(model['prepare_circuit']);cp.cuda.runtime.deviceSynchronize();prepared=state.sv.copy()
        for c in cases:
            cp.copyto(state.sv,prepared);start=time.perf_counter();state.circuit(circuit_gates(model,c));cp.cuda.runtime.deviceSynchronize()
            gpu=state.sv.get();cpu=cpu_state(model,c);error=float(np.max(abs(gpu-cpu)))
            ex=float(state.expectations([[patch[0]]],['Z'])[0]);analytic=controller(model,c)['analytic_expectation']
            if error>2e-12 or abs(ex-analytic)>2e-12:raise ValueError('GPU/CPU/analytic mismatch')
            rows.append(dict(configuration=c,amplitude_max_error=error,expectation=ex,analytic=analytic,norm2=state.norm2(),seconds=time.perf_counter()-start))
        c=cases[0];angles=controller(model,c)['theta'];grads=[]
        for j in range(4):
            values=[]
            for shift in (math.pi/2,-math.pi/2):
                gates=circuit_gates(model,c);gates[j]['angle']+=shift
                cp.copyto(state.sv,prepared);state.circuit(gates);values.append(float(state.expectations([[patch[0]]],['Z'])[0]))
            numerical=(values[0]-values[1])/2
            exact=-np.prod(c['signs'])*math.sin(angles[j])*math.prod(math.cos(t)for i,t in enumerate(angles)if i!=j)
            if abs(numerical-exact)>2e-12:raise ValueError('Parameter-shift discrepancy')
            grads.append(dict(parameter=j,parameter_shift=numerical,analytic=exact,error=abs(numerical-exact)))
        return dict(status='passed',backend='NVIDIA cuStateVec dense complex128',environment=info,rows=rows,parameter_shift=grads,scope='Actual classical GPU state-vector simulation. No hardware experiment, quantum advantage or learned physical law.')
    finally:state.close()


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--gpu',action='store_true');parser.add_argument('--output',type=Path,required=True);args=parser.parse_args()
    model=json.loads(MODEL.read_text());cases=[]
    for mode in ('maxplus','softmax','hard'):
        for gain in (0.,.6):cases.append(dict(DEFAULT,mode=mode,gain=gain))
    cases.extend([dict(DEFAULT,qx=0.,qy=0.),dict(DEFAULT,signs=[-1,1,-1,1]),dict(DEFAULT,qx=-1.2,qy=.9)])
    result=dict(schema='grh.surface-quantum-check.v1',model_sha256=hashlib.sha256(MODEL.read_bytes()).hexdigest(),script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),data_qubits=18)
    if args.gpu:result['gpu']=verify_gpu(model,cases)
    else:
        rows=[]
        for c in cases:
            row=execute_cpu(model,c);error=abs(row['expectation']-row['controller']['analytic_expectation'])
            if error>2e-12 or abs(row['norm2']-1)>2e-12:raise ValueError('CPU identity failure')
            rows.append(dict(configuration=c,result=row,error=error))
        result['cpu']=dict(status='passed',rows=rows,scope='Independent NumPy gate execution, not replacing the circuit by its analytic formula.')
    args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(result,indent=2,allow_nan=False)+'\n');print(json.dumps(result,indent=2))

if __name__=='__main__':main()
