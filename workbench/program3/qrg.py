"""A trainable hierarchical CPTP coarse grainer and a declared width limit.

Four qubits are reduced to two and one through shared two-qubit unitaries and
partial trace. Gate parameters are learned, not supplied by a target solution.
The optional classical readout is distinct from the quantum channel. Width in
random_fourier_report means independent feature circuits, not cover degree.
"""
from __future__ import annotations
import argparse,hashlib,itertools,json,math
from pathlib import Path
import numpy as np
import torch
from torch import nn

torch.set_num_threads(2)
DT=torch.float64
I=np.eye(2);X=np.array([[0.,1],[1,0]]);Z=np.diag([1.,-1.]);Y=np.array([[0,-1j],[1j,0]])


def expand_gate(matrix,wires,n):
    wires=list(wires);matrix=np.asarray(matrix,dtype=complex)
    if len(set(wires))!=len(wires)or any(type(q)is not int or not 0<=q<n for q in wires)or matrix.shape!=(1<<len(wires),)*2:raise ValueError('Gate shape/wires invalid')
    out=np.zeros((1<<n,1<<n),complex)
    for column in range(1<<n):
        local=sum(((column>>q)&1)<<i for i,q in enumerate(wires));base=column
        for q in wires:base&=~(1<<q)
        for row in range(1<<len(wires)):
            global_row=base|sum(((row>>i)&1)<<q for i,q in enumerate(wires));out[global_row,column]=matrix[row,local]
    return out


def ry(a):return np.array([[math.cos(a/2),-math.sin(a/2)],[math.sin(a/2),math.cos(a/2)]])
def cx(control,target,n):
    out=np.zeros((1<<n,1<<n))
    for i in range(1<<n):out[i^((1<<target)if i>>control&1 else 0),i]=1
    return out


def stage_unitary_np(theta,n):
    if n not in(2,4)or len(theta)!=3:raise ValueError('Declared two-level hierarchy only')
    u=np.eye(1<<n,dtype=complex)
    for keep in range(0,n,2):
        u=expand_gate(ry(theta[0]),[keep],n)@u;u=expand_gate(ry(theta[1]),[keep+1],n)@u
        u=cx(keep,keep+1,n)@u;u=expand_gate(ry(theta[2]),[keep],n)@u
    return u


def pool_kraus_np(u,n):
    keep=list(range(0,n,2));discard=list(range(1,n,2));ks=[]
    for d in range(1<<len(discard)):
        select=np.zeros((1<<len(keep),1<<n))
        for k in range(1<<len(keep)):
            col=sum(((k>>j)&1)<<q for j,q in enumerate(keep))|sum(((d>>j)&1)<<q for j,q in enumerate(discard));select[k,col]=1
        ks.append(select@u)
    return ks


def hierarchy_kraus(theta):
    t=np.asarray(theta,dtype=float)
    if t.shape!=(6,)or not np.all(np.isfinite(t)):raise ValueError('Six finite gate parameters required')
    first=pool_kraus_np(stage_unitary_np(t[:3],4),4);second=pool_kraus_np(stage_unitary_np(t[3:],2),2)
    return first,second,[b@a for a in first for b in second]


def channel(rho,kraus):return sum(k@rho@k.conj().T for k in kraus)

def partial_trace_np(rho,keep,n):
    keep=list(keep);discard=[q for q in range(n)if q not in keep];out=np.zeros((1<<len(keep),)*2,complex)
    for i,j in itertools.product(range(1<<len(keep)),repeat=2):
        for d in range(1<<len(discard)):
            a=sum(((i>>r)&1)<<q for r,q in enumerate(keep))+sum(((d>>r)&1)<<q for r,q in enumerate(discard));b=sum(((j>>r)&1)<<q for r,q in enumerate(keep))+sum(((d>>r)&1)<<q for r,q in enumerate(discard));out[i,j]+=rho[a,b]
    return out


def lifted_gates(theta):
    gates=[]
    for active,t in [([0,1,2,3],theta[:3]),([0,2],theta[3:])]:
        for i in range(0,len(active),2):
            k,d=active[i:i+2];gates.extend([{'gate':'RY','target':k,'angle':float(t[0])},{'gate':'RY','target':d,'angle':float(t[1])},{'gate':'CX','control':k,'target':d},{'gate':'RY','target':k,'angle':float(t[2])}])
    return gates


class HierarchicalQNN(nn.Module):
    def __init__(self,seed=17):
        super().__init__();g=torch.Generator().manual_seed(seed);self.theta=nn.Parameter(torch.randn(6,generator=g,dtype=DT)*.25);self.slope=nn.Parameter(torch.tensor(1.,dtype=DT));self.bias=nn.Parameter(torch.tensor(0.,dtype=DT))
        for n in (2,4):
            for q in range(n):
                # RY(theta)=cos(theta/2) I + sin(theta/2) J on the target qubit.
                self.register_buffer(f'J{n}_{q}',torch.tensor(expand_gate([[0,-1],[1,0]],[q],n).real,dtype=DT))
            self.register_buffer(f'I{n}',torch.eye(1<<n,dtype=DT))
            for q in range(0,n,2):self.register_buffer(f'C{n}_{q}',torch.tensor(cx(q,q+1,n),dtype=DT))
        self.register_buffer('Z0',torch.tensor(np.diag([1.,-1.]),dtype=DT))
    def rotation(self,t,q,n):return torch.cos(t/2)*getattr(self,f'I{n}')+torch.sin(t/2)*getattr(self,f'J{n}_{q}')
    def unitary(self,t,n):
        u=getattr(self,f'I{n}')
        for q in range(0,n,2):u=self.rotation(t[2],q,n)@getattr(self,f'C{n}_{q}')@self.rotation(t[1],q+1,n)@self.rotation(t[0],q,n)@u
        return u
    def observable(self):
        u2=self.unitary(self.theta[3:],2);o2=u2.T@torch.kron(torch.eye(2,dtype=DT),self.Z0)@u2
        # Lift the 2-qubit observable to physical qubits 0,2; discarded 1,3 are I.
        rows=[]
        for i in range(16):
            row=[]
            for j in range(16):row.append(o2[(i&1)|((i>>1)&2),(j&1)|((j>>1)&2)]if (i&10)==(j&10)else o2.new_zeros(()))
            rows.append(torch.stack(row))
        o=torch.stack(rows);u4=self.unitary(self.theta[:3],4);return u4.T@o@u4
    @staticmethod
    def states(x):
        if x.ndim!=2 or x.shape[1]!=4:raise ValueError('Four angle features required')
        x=x.to(DT);state=torch.ones((len(x),1),dtype=DT,device=x.device)
        for q in reversed(range(4)):
            one=torch.stack([torch.cos(x[:,q]/2),torch.sin(x[:,q]/2)],1);state=(state[:,:,None]*one[:,None,:]).reshape(len(x),-1)
        return state
    def expectations(self,x):
        state=self.states(x);o=self.observable();return torch.einsum('bi,ij,bj->b',state,o,state)
    def forward(self,x):return self.slope*self.expectations(x)+self.bias
    def export(self):return {'theta':self.theta.detach().numpy().tolist(),'slope':float(self.slope.detach()),'bias':float(self.bias.detach()),'parameters':8,'channel_parameters':6,'pooling':'4 -> 2 -> 1 qubits; retain 0,2 then 0; discarded outcomes not postselected'}


def frozen_predict(x,weights):
    first,second,k=hierarchy_kraus(weights['theta']);o=sum(a.conj().T@Z@a for a in k).real;x=np.asarray(x,dtype=float);state=np.ones((len(x),1))
    for q in reversed(range(4)):state=(state[:,:,None]*np.stack((np.cos(x[:,q]/2),np.sin(x[:,q]/2)),1)[:,None,:]).reshape(len(x),-1)
    return weights['slope']*np.einsum('bi,ij,bj->b',state,o,state)+weights['bias']


def thermal_states():
    records=[]
    pairs=[(0,1),(1,2),(2,3),(3,0)]
    ZZ=sum(expand_gate(np.kron(Z,Z),[a,b],4)for a,b in pairs)/4
    for i,g in enumerate(np.linspace(.2,1.8,33)):
        H=-4*ZZ-g*sum(expand_gate(X,[q],4)for q in range(4));evals,U=np.linalg.eigh(H);p=np.exp(-(evals-evals.min()));p/=p.sum();rho=(U*p)@U.conj().T
        split='test'if i%4==3 else'validation'if i%4==1 else'train'
        records.append(dict(g=float(g),split=split,rho=rho,target=float(np.trace(rho@ZZ).real)))
    return records


def train_thermal(seed=17,steps=120):
    records=thermal_states();model=HierarchicalQNN(seed);optimizer=torch.optim.Adam(model.parameters(),lr=.04)
    batches={s:(torch.tensor(np.stack([r['rho'].real for r in records if r['split']==s]),dtype=DT),torch.tensor([r['target']for r in records if r['split']==s],dtype=DT))for s in ['train','validation','test']}
    best=None;history=[]
    def predict(s):rho,y=batches[s];return model.slope*torch.einsum('bij,ji->b',rho,model.observable())+model.bias,y
    for step in range(steps+1):
        p,y=predict('train');loss=((p-y)**2).mean()
        if step%10==0 or step==steps:
            with torch.no_grad():v,t=predict('validation');vl=float(((v-t)**2).mean())
            history.append({'step':step,'train_mse':float(loss.detach()),'validation_mse':vl})
            if best is None or vl<best[0]:best=(vl,step,{k:v.detach().clone()for k,v in model.state_dict().items()})
        if step<steps:optimizer.zero_grad();loss.backward();optimizer.step()
    model.load_state_dict(best[2]);p,y=predict('test');baseline=float(batches['train'][1].mean());weights=model.export();first,second,kraus=hierarchy_kraus(weights['theta']);coarse=[]
    paulis=[I,X,Y,Z]
    for r in records:
        rho=channel(r['rho'],first);evals,U=np.linalg.eigh(rho);H=(U*(-np.log(evals)))@U.conj().T;H-=np.trace(H)/4*np.eye(4)
        coefficients={a+b:float(np.trace(np.kron(paulis['IXYZ'.index(a)],paulis['IXYZ'.index(b)])@H).real/4)for a,b in itertools.product('IXYZ',repeat=2)}
        trunc=sum(coefficients[key]*np.kron(paulis['IXYZ'.index(key[0])],paulis['IXYZ'.index(key[1])])for key in ['IX','XI','ZZ']);e,V=np.linalg.eigh(trunc);prob=np.exp(-e);prob/=prob.sum();approx=(V*prob)@V.conj().T
        coarse.append({'g':r['g'],'split':r['split'],'effective_hamiltonian_pauli':coefficients,'ising_projection_trace_distance':float(np.linalg.svd(rho-approx,compute_uv=False).sum()/2),'coarse_min_eigenvalue':float(evals.min()),'coarse_trace':float(np.trace(rho).real)})
    return dict(seed=seed,weights=weights,selected_step=best[1],history=history,test_mse=float(((p-y)**2).mean().detach()),constant_test_mse=float(((y-baseline)**2).mean()),coarse_hamiltonians=coarse,scope='Actually trained hierarchical channel on exact four-site periodic Ising Gibbs states at beta=1. Learned ZZ-observable retention; finite-size states, not an infinite-system phase-transition claim. Effective H=-log rho is exact; Ising-family truncation error is measured.')


def random_fourier_report():
    rng=np.random.default_rng(6721);x=rng.normal(size=(12,4));D=((x[:,None,:]-x[None,:,:])**2).sum(-1);exact=np.exp(-D/2);rows=[]
    for width in [16,64,256,1024,4096]:
        for seed in [3,5,7,11]:
            gen=np.random.default_rng(seed);w=gen.normal(size=(width,4));phase=gen.uniform(0,2*math.pi,width);features=math.sqrt(2)*np.cos(x@w.T+phase);kernel=features@features.T/width
            rows.append(dict(width=width,seed=seed,max_error=float(np.max(abs(kernel-exact))),frobenius_relative=float(np.linalg.norm(kernel-exact)/np.linalg.norm(exact)),minimum_eigenvalue=float(np.linalg.eigvalsh(kernel).min()),hoeffding_union_epsilon=min(4.,math.sqrt(8/width*math.log(2*len(x)**2/.05)))))
    return dict(inputs=x.tolist(),exact_kernel=exact.tolist(),rows=rows,feature='sqrt(2) times Z expectation after RY(w dot x + phase); w iid standard normal, phase uniform [0,2pi)',width='Number of independent single-qubit feature circuits, not a covering degree or simultaneous qubit count',theorem='K_M converges to exp(-||x-y||²/2). On n fixed inputs, P(max error>epsilon)<=2 n² exp(-M epsilon²/8). Readout-only kernel training is a distinct regime from training all quantum gates.')


def channel_audit(theta):
    first,second,kraus=hierarchy_kraus(theta);identity=sum(k.conj().T@k for k in kraus);rng=np.random.default_rng(477);rows=[]
    for i in range(16):
        a=rng.normal(size=(16,16))+1j*rng.normal(size=(16,16));rho=a@a.conj().T;rho/=np.trace(rho)
        u=stage_unitary_np(theta[:3],4);mid=partial_trace_np(u@rho@u.conj().T,[0,2],4);u2=stage_unitary_np(theta[3:],2);out=partial_trace_np(u2@mid@u2.conj().T,[0],2);direct=channel(rho,kraus)
        rows.append(dict(trace_error=float(abs(np.trace(out)-1)),minimum_eigenvalue=float(np.linalg.eigvalsh(out).min()),independent_partial_trace_error=float(np.max(abs(out-direct)))))
    error=float(np.max(abs(identity-np.eye(16))))
    if error>1e-12 or max(r['independent_partial_trace_error']for r in rows)>1e-12:raise ValueError('Channel audit failed')
    return dict(kraus_count=len(kraus),completeness_error=error,states=rows)


def run(output):
    output.mkdir(parents=True,exist_ok=True);runs=[train_thermal(s)for s in (17,29)];audits=[channel_audit(r['weights']['theta'])for r in runs];width=random_fourier_report();r=dict(schema='grh.learned-quantum-renormalization.v1',thermal_runs=runs,channel_audits=audits,infinite_width=width,script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    (output/'results.json').write_text(json.dumps(r,indent=2)+'\n');return r

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output',type=Path,required=True);a=p.parse_args();r=run(a.output);print(json.dumps({'runs':[{'seed':x['seed'],'test_mse':x['test_mse'],'baseline':x['constant_test_mse']}for x in r['thermal_runs']],'channel_errors':[x['completeness_error']for x in r['channel_audits']]},indent=2))
