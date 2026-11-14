#!/usr/bin/env python3
"""Authentic cuQuantum experiments on the authorized workstation.

No mocked backend or CPU fallback is used in a result labelled GPU. Dense
amplitudes (cuStateVec) and relative Pauli frames (cuStabilizer) are reported
separately. Run only one GPU experiment process at a time.
"""
from __future__ import annotations
import argparse
import gc
import hashlib
import importlib.metadata
import itertools
import json
import math
from pathlib import Path
import platform
import subprocess
import time
import traceback

import numpy as np
import cupy as cp
import cuquantum
from cuquantum import ComputeType, cudaDataType
from cuquantum.bindings import custatevec as csv

HERE = Path(__file__).resolve().parent
GIB = 1024 ** 3
RESERVE = 2 * GIB


def package_version(name):
    try: return importlib.metadata.version(name)
    except importlib.metadata.PackageNotFoundError: return None


def environment():
    props = cp.cuda.runtime.getDeviceProperties(0)
    name = props['name'].decode() if isinstance(props['name'], bytes) else props['name']
    free, total = cp.cuda.runtime.memGetInfo()
    return {'gpu': name, 'free_bytes_before': free, 'total_bytes': total,
            'driver_version': cp.cuda.runtime.driverGetVersion(),
            'runtime_version': cp.cuda.runtime.runtimeGetVersion(),
            'python': platform.python_version(),
            'packages': {p: package_version(p) for p in
                         ['cuquantum-python-cu12','cupy-cuda12x','custatevec-cu12',
                          'custabilizer-cu12','cutensornet-cu12','stim','numpy']},
            'reserve_bytes': RESERVE,
            'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}


class StateVector:
    def __init__(self, n, precision='complex64'):
        self.n = int(n)
        self.dtype = np.dtype(precision)
        self.nbytes = (1 << self.n) * self.dtype.itemsize
        free, total = cp.cuda.runtime.memGetInfo()
        if self.nbytes > free - RESERVE:
            raise MemoryError(f'{n}-qubit state needs {self.nbytes} bytes; '
                              f'only {free-RESERVE} bytes available after reserve')
        self.data_type = (cudaDataType.CUDA_C_32F if precision == 'complex64'
                          else cudaDataType.CUDA_C_64F)
        self.compute_type = (ComputeType.COMPUTE_32F if precision == 'complex64'
                             else ComputeType.COMPUTE_64F)
        self.handle = csv.create()
        self.sv = cp.zeros(1 << self.n, dtype=self.dtype)
        self.sv[:1].set(np.array([1], dtype=self.dtype))
        self.workspace = None
        self.workspace_bytes = 0
        self.matrices = []
        self.gates_applied = 0

    def gate(self, gate):
        op = gate.get('gate', gate.get('op', gate.get('name', ''))).upper()
        target = gate.get('target', gate.get('qubits', [None])[-1])
        control = gate.get('control')
        if control is None and op in ('CX','CNOT','CZ'):
            control = gate['qubits'][0]
        theta = float(gate.get('angle', 0))
        if op == 'H': m = np.array([[1,1],[1,-1]]) / math.sqrt(2)
        elif op in ('X','CX','CNOT'): m = [[0,1],[1,0]]
        elif op in ('Z','CZ'): m = [[1,0],[0,-1]]
        elif op == 'RY':
            c,s = math.cos(theta/2),math.sin(theta/2)
            m = [[c,-s],[s,c]]
        elif op == 'RZ': m = [[np.exp(-.5j*theta),0],[0,np.exp(.5j*theta)]]
        else: raise ValueError(f'Unsupported gate {op}')
        m = np.ascontiguousarray(m, dtype=self.dtype)
        self.matrices.append(m)
        controls = [] if control is None else [int(control)]
        size = csv.apply_matrix_get_workspace_size(
            self.handle, self.data_type, self.n, m.ctypes.data, self.data_type,
            csv.MatrixLayout.ROW, 0, 1, len(controls), self.compute_type)
        if size > self.workspace_bytes:
            free, _ = cp.cuda.runtime.memGetInfo()
            if size > free - RESERVE:
                raise MemoryError('Gate workspace would consume the reserved GPU memory')
            self.workspace = cp.cuda.alloc(size)
            self.workspace_bytes = size
        csv.apply_matrix(self.handle, self.sv.data.ptr, self.data_type, self.n,
                         m.ctypes.data, self.data_type, csv.MatrixLayout.ROW, 0,
                         [int(target)], 1, controls, [1]*len(controls), len(controls),
                         self.compute_type,
                         0 if self.workspace is None else self.workspace.ptr,
                         self.workspace_bytes)
        self.gates_applied += 1

    def circuit(self, gates):
        for gate in gates: self.gate(gate)

    def expectations(self, supports, paulis):
        out = np.empty(len(supports), dtype=np.float64)
        operators = [[getattr(csv.Pauli, p)]*len(s) for s,p in zip(supports,paulis)]
        csv.compute_expectations_on_pauli_basis(
            self.handle, self.sv.data.ptr, self.data_type, self.n,
            out.ctypes.data, operators, len(supports), supports,
            [len(s) for s in supports])
        cp.cuda.runtime.deviceSynchronize()
        return out

    def norm2(self): return float(self.expectations([[0]], ['I'])[0])

    def close(self):
        cp.cuda.runtime.deviceSynchronize()
        csv.destroy(self.handle)
        self.sv = None
        self.workspace = None
        self.matrices.clear()
        gc.collect()
        cp.get_default_memory_pool().free_all_blocks()


def supports(case, name):
    return [v if isinstance(v,list) else v['qubits'] for v in case[name]]


def case_file(name):
    return json.loads((HERE/'cases'/f'{name}.json').read_text())


def smoke():
    st=StateVector(2)
    try:
        st.circuit([{'gate':'H','target':0},{'gate':'CX','control':0,'target':1}])
        result=st.sv.get()
        expected=np.array([1,0,0,1])/math.sqrt(2)
        assert np.max(np.abs(result-expected)) < 2e-6
        paulis=st.expectations([[0,1],[0,1]],['X','Z'])
        assert np.max(np.abs(paulis-1)) < 2e-6
        return {'passed':True,'n':2,'amplitudes':[[float(z.real),float(z.imag)] for z in result],
                'XX_ZZ':paulis.tolist(),'norm2':st.norm2()}
    finally: st.close()


def dense_case(name, ancilla=False):
    case=case_file(name)
    x,z=supports(case,'x_checks'),supports(case,'z_checks')
    n=case['n']+int(ancilla)
    st=StateVector(n)
    start=time.perf_counter()
    try:
        st.circuit(case['prepare_circuit'])
        cp.cuda.runtime.deviceSynchronize()
        preparation_seconds=time.perf_counter()-start
        baseline=st.expectations(x+z,['X']*len(x)+['Z']*len(z))
        assert np.max(np.abs(baseline-1)) < 2e-5
        norm=st.norm2()
        assert abs(norm-1) < 2e-5
        error_edge=z[0][0]
        st.gate({'gate':'X','target':error_edge})
        error_expectations=st.expectations(x+z,['X']*len(x)+['Z']*len(z))
        predicted=np.array([1]*len(x)+[-1 if error_edge in s else 1 for s in z])
        assert np.max(np.abs(error_expectations-predicted)) < 2e-5
        ancilla_z=None
        if ancilla:
            for q in z[0]:st.gate({'gate':'CX','control':q,'target':case['n']})
            ancilla_z=float(st.expectations([[case['n']]],['Z'])[0])
            assert abs(ancilla_z+1) < 2e-5
        cp.cuda.runtime.deviceSynchronize()
        return {'case':name,'backend':'NVIDIA cuStateVec','representation':'dense complex64 state vector',
                'data_qubits':case['n'],'ancillas':int(ancilla),'total_qubits':n,
                'state_bytes':st.nbytes,'workspace_bytes':st.workspace_bytes,
                'preparation_gates':len(case['prepare_circuit']),
                'gates_applied':st.gates_applied,'preparation_seconds':preparation_seconds,
                'total_wall_seconds':time.perf_counter()-start,'norm2':norm,
                'all_stabilizer_expectations_before_error':baseline.tolist(),
                'injected_X_edge':error_edge,'after_error':error_expectations.tolist(),
                'predicted_after_error':predicted.tolist(),'syndrome_ancilla_Z':ancilla_z,
                'max_stabilizer_error':float(np.max(np.abs(baseline-1))),
                'passed':True}
    finally:st.close()


def qnn(steps=24, rate=.2):
    case=case_file('torus3x3')
    patch=supports(case,'x_checks')[0]
    assert len(patch)==4
    st=StateVector(case['n'])
    st.circuit(case['prepare_circuit'])
    cp.cuda.runtime.deviceSynchronize()
    base=st.sv.copy()
    train=np.array([[1,1,1,1],[-1,1,1,1],[-1,-1,1,1],[1,-1,1,1]],dtype=float)
    target=np.prod(train,axis=1)
    theta=np.array([.65,-.4,.5,-.6],dtype=float)
    initial=theta.copy()
    history=[]
    start=time.perf_counter()

    def predict(signs,params):
        cp.cuda.runtime.memcpyAsync(st.sv.data.ptr,base.data.ptr,st.nbytes,
                                   cp.cuda.runtime.memcpyDeviceToDevice,0)
        for q,sign,value in zip(patch,signs,params):
            st.gate({'gate':'RY','target':q,'angle':float(sign*math.pi/2+value)})
        for q in patch[1:]:st.gate({'gate':'CX','control':q,'target':patch[0]})
        return float(st.expectations([[patch[0]]],['Z'])[0])

    try:
        max_analytic_error=0.0
        for step in range(steps+1):
            predictions=np.array([predict(s,theta) for s in train])
            analytic=np.prod(train,axis=1)*np.prod(np.cos(theta))
            max_analytic_error=max(max_analytic_error,float(np.max(np.abs(predictions-analytic))))
            loss=float(np.mean((predictions-target)**2))
            history.append({'step':step,'loss':loss,'theta':theta.tolist(),
                            'predictions':predictions.tolist()})
            if step==steps:break
            grad=np.zeros(4)
            for j in range(4):
                plus,minus=theta.copy(),theta.copy()
                plus[j]+=math.pi/2;minus[j]-=math.pi/2
                derivatives=np.array([(predict(s,plus)-predict(s,minus))/2 for s in train])
                grad[j]=np.mean(2*(predictions-target)*derivatives)
            theta-=rate*grad
        truth=[]
        train_set={tuple(int(x) for x in s) for s in train}
        for signs in itertools.product([-1,1],repeat=4):
            pred=predict(signs,theta);truth.append({'signs':list(signs),
                'target':math.prod(signs),'prediction':pred,'used_in_training':signs in train_set})
        assert max_analytic_error < 2e-5
        assert history[-1]['loss'] < history[0]['loss']
        assert all((r['prediction']>0)==(r['target']>0) for r in truth)
        return {'backend':'NVIDIA cuStateVec','total_qubits':case['n'],'patch_qubits':patch,
                'model':'four-parameter surface-local variational stabilizer correlator',
                'initial_theta':initial.tolist(),'final_theta':theta.tolist(),
                'learning_rate':rate,'steps':steps,'history':history,'truth_table':truth,
                'training_samples':4,'held_out_inputs':12,
                'max_analytic_prediction_error':max_analytic_error,
                'wall_seconds':time.perf_counter()-start,'passed':True,
                'claim_limit':'Complete tiny synthetic truth table; no claimed quantum advantage or benchmark validation'}
    finally:
        base=None
        st.close()


def extraction_text(n,x,z):
    ax=list(range(n,n+len(x)))
    az=list(range(n+len(x),n+len(x)+len(z)))
    lines=['R '+' '.join(map(str,ax+az)),'H '+' '.join(map(str,ax))]
    for j in range(max(map(len,x))):
        pairs=[(a,s[j]) for a,s in zip(ax,x) if j<len(s)]
        lines.append('CX '+' '.join(str(q) for pair in pairs for q in pair))
    lines.append('H '+' '.join(map(str,ax)))
    lines.append('M '+' '.join(map(str,ax)))
    for j in range(max(map(len,z))):
        pairs=[(s[j],a) for a,s in zip(az,z) if j<len(s)]
        lines.append('CX '+' '.join(str(q) for pair in pairs for q in pair))
    lines.append('M '+' '.join(map(str,az)))
    return '\n'.join(lines)+'\n'


def frame_case(name=None,lattice_size=None,shots=32768,noise=.001):
    from cuquantum.stabilizer import Circuit,FrameSimulator
    if lattice_size is not None:
        from surface_codes import torus_checks
        x,z=torus_checks(lattice_size,lattice_size)
        n=2*lattice_size*lattice_size
        label=f'torus{lattice_size}x{lattice_size}'
        genus=1
    else:
        case=case_file(name);x,z=supports(case,'x_checks'),supports(case,'z_checks')
        n=case['n'];label=name;genus=case['genus']
    n_anc=len(x)+len(z);total=n+n_anc
    stride=((shots+31)//32)*4
    estimated=(2*total+n_anc)*stride
    free,_=cp.cuda.runtime.memGetInfo()
    # Allow 25 percent overhead beyond the explicit bit tables, plus a
    # fixed 2GiB reserve for the desktop and other users of the device.
    if estimated*1.25 > free-RESERVE:
        return {'case':label,'status':'skipped_memory_budget','data_qubits':n,
                'total_qubits':total,'shots':shots,'bit_table_bytes':estimated,
                'free_bytes':free,'required_budget_with_overhead':int(estimated*1.25+RESERVE)}
    start=time.perf_counter()
    sim=FrameSimulator(num_qubits=total,num_paulis=shots,num_measurements=n_anc,
                       randomize_measurements=False,seed=20261113,package='cupy')
    targets=' '.join(map(str,range(n)))
    noise_circuit=Circuit(f'X_ERROR({noise}) {targets}\nZ_ERROR({noise}) {targets}\n')
    measure_circuit=Circuit(extraction_text(n,x,z))
    cp.cuda.runtime.deviceSynchronize()
    setup_seconds=time.perf_counter()-start
    started=time.perf_counter()
    sim.apply(noise_circuit)
    sim.apply(measure_circuit)
    cp.cuda.runtime.deviceSynchronize()
    run_seconds=time.perf_counter()-started
    xb,zb=sim.get_pauli_xz_bits(bit_packed=True)
    measured=sim.get_measurement_bits(bit_packed=True)
    errors=0
    events=0
    lut=cp.asarray([int(i).bit_count() for i in range(256)],dtype=cp.uint8)
    for offset,rows,frames in [(0,x,zb),(len(x),z,xb)]:
        for first in range(0,len(rows),512):
            block=rows[first:first+512]
            expected=cp.zeros((len(block),stride),dtype=cp.uint8)
            for j in range(max(map(len,block))):
                # All standard grid checks have weight four. Ragged supports
                # in higher genus are handled without padding a fake qubit.
                valid=[i for i,s in enumerate(block) if j<len(s)]
                indices=cp.asarray([block[i][j] for i in valid],dtype=cp.int64)
                vi=cp.asarray(valid,dtype=cp.int64)
                expected[vi] ^= frames[indices]
            actual=measured[offset+first:offset+first+len(block)]
            errors+=int(cp.count_nonzero(expected != actual).get())
            events+=int(cp.sum(lut[actual],dtype=cp.uint64).get())
    assert errors==0, f'{errors} syndrome bytes disagree with exact sparse GF(2) propagation'
    out={'case':label,'genus':genus,'backend':'NVIDIA cuStabilizer',
         'representation':'Pauli-error frames relative to a known encoded stabilizer reference',
         'data_qubits':n,'ancilla_qubits':n_anc,'total_qubits':total,'shots':shots,
         'noise_model':{'independent_X_probability':noise,'independent_Z_probability':noise},
         'bit_table_bytes':estimated,'setup_seconds':setup_seconds,'simulation_seconds':run_seconds,
         'total_wall_seconds':time.perf_counter()-start,'syndrome_events':events,
         'syndrome_rate':events/(n_anc*shots),'all_syndrome_bytes_checked':n_anc*stride,
         'syndrome_byte_mismatches':errors,'passed':True,
         'claim_limit':'No full amplitude vector and no non-Clifford variational simulation in this backend'}
    del sim,noise_circuit,measure_circuit,xb,zb,measured,lut,expected,actual
    gc.collect();cp.get_default_memory_pool().free_all_blocks()
    return out


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--mode',choices=['smoke','states','qnn','frames','all'],default='smoke')
    p.add_argument('--output',type=Path,default=HERE/'results/gpu-results.json')
    p.add_argument('--max-frame-lattice',type=int,default=512)
    args=p.parse_args()
    result={'environment':environment(),'mode':args.mode,'experiments':[],
            'utc_started':time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime())}
    args.output.parent.mkdir(parents=True,exist_ok=True)
    def record(name,fn):
        print(f'Running {name}',flush=True)
        try:
            value=fn();result['experiments'].append({'name':name,**value})
            print(json.dumps({k:v for k,v in value.items() if k in
                  ['passed','case','total_qubits','data_qubits','simulation_seconds','status','wall_seconds']}),flush=True)
        except Exception as e:
            result['experiments'].append({'name':name,'passed':False,'error':str(e),
                                          'traceback':traceback.format_exc()})
            args.output.write_text(json.dumps(result,indent=2)+'\n')
            raise
        args.output.write_text(json.dumps(result,indent=2)+'\n')
    record('bell_smoke',smoke)
    if args.mode in ('states','all'):
        record('toric_18_dense',lambda:dense_case('torus3x3'))
        record('toric_30_dense',lambda:dense_case('torus3x5'))
        record('toric_30_plus_ancilla_31_dense',lambda:dense_case('torus3x5',True))
    if args.mode in ('qnn','all'):record('surface_local_qnn_18',qnn)
    if args.mode in ('frames','all'):
        record('genus2_frames',lambda:frame_case(name='genus2_3x3',shots=32768))
        for size in [32,128,512,1024]:
            if size <= args.max_frame_lattice:
                record(f'torus_{size}_frames',lambda size=size:frame_case(lattice_size=size,shots=32768))
    result['utc_finished']=time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime())
    result['passed']=all(r.get('passed',False) or r.get('status')=='skipped_memory_budget'
                         for r in result['experiments'])
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(f'Wrote {args.output}',flush=True)


if __name__=='__main__':main()
