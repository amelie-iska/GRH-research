#!/usr/bin/env python3
"""Explicit local cuQuantum simulations on actual clean-dessin incidence graphs.

Run only on an approved NVIDIA GPU host. No install/fallback/cloud action.
Large circuits are untrained finite-state benchmarks, not thermal or GRH proofs.
"""
import argparse,json,time,math,platform,importlib.metadata
from pathlib import Path
import numpy as np


def circuit(m,layers=3):
    n=m+2;gates=[]
    def add(matrix,target,controls=()):gates.append((np.asarray(matrix,np.complex64),target,tuple(controls)))
    for layer in range(layers):
        for q in range(n):
            a=.23*(q+1)+.17*layer;c=math.cos(a/2);s=math.sin(a/2)
            add([[c,-s],[s,c]],n-1-q)
        for black in (0,1):
            for j in range(m):
                bit=n-1-(j+2);control=n-1-black;angle=.19*(layer+1)*(1 if black==0 else (-1)**j)
                add([[0,1],[1,0]],bit,[control])
                add(np.diag(np.exp(np.array([-.5j,.5j])*angle)),bit)
                add([[0,1],[1,0]],bit,[control])
    return gates


def numpy_apply(state,matrix,target,controls,adjoint=False):
    out=state.copy();U=matrix.conj().T if adjoint else matrix
    for i in range(len(state)):
        if i & (1<<target) or any(not(i & (1<<c)) for c in controls):continue
        j=i|(1<<target);out[i],out[j]=U@state[[i,j]]
    return out


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--output',required=True,type=Path);parser.add_argument('--m',type=int,nargs='+',default=[5,9,21]);args=parser.parse_args()
    if args.output.exists():raise SystemExit('New output file required')
    import cupy as cp
    import cuquantum
    from cuquantum.bindings import custatevec as cusv
    from cuquantum.tensornet import contract
    if cp.cuda.runtime.getDeviceCount()<1:raise SystemExit('NVIDIA device required')
    device=cp.cuda.runtime.getDeviceProperties(cp.cuda.Device().id);name=device['name'];name=name.decode() if isinstance(name,bytes) else name
    rng=np.random.default_rng(20261104);A=rng.normal(size=(64,32));B=rng.normal(size=(32,16))
    contracted=contract('ab,bc->ac',cp.asarray(A),cp.asarray(B));contraction_error=float(cp.max(cp.abs(contracted-cp.asarray(A@B))))
    assert contraction_error<1e-10
    records=[];handle=cusv.create()
    try:
        for m in args.m:
            if m<3 or m%2!=1 or m+2>25:raise ValueError('Odd dessin m; maximum25qubits in this explicit memory-bounded runner')
            n=m+2;gates=circuit(m);state=cp.zeros(2**n,dtype=cp.complex64);state[0]=1;cp.cuda.Stream.null.synchronize();start=time.perf_counter()
            def apply(matrix,target,controls,adjoint=0):
                matrix=np.ascontiguousarray(matrix);targets=np.asarray([target],np.int32);control=np.asarray(controls,np.int32)
                dtype=cuquantum.cudaDataType.CUDA_C_32F;compute=cuquantum.ComputeType.COMPUTE_32F
                size=cusv.apply_matrix_get_workspace_size(handle,dtype,n,matrix.ctypes.data,dtype,cusv.MatrixLayout.ROW,adjoint,1,len(control),compute)
                workspace=cp.cuda.memory.alloc(size) if size else None
                cusv.apply_matrix(handle,state.data.ptr,dtype,n,matrix.ctypes.data,dtype,cusv.MatrixLayout.ROW,adjoint,targets.ctypes.data,1,control.ctypes.data if len(control) else 0,0,len(control),compute,workspace.ptr if workspace else 0,size)
            for matrix,target,controls in gates:apply(matrix,target,controls)
            cp.cuda.Stream.null.synchronize();seconds=time.perf_counter()-start;norm=float(cp.vdot(state,state).real);assert abs(norm-1)<.0005
            reference_error=None
            if n<=11:
                reference=np.zeros(2**n,np.complex128);reference[0]=1
                for matrix,target,controls in gates:reference=numpy_apply(reference,matrix,target,controls)
                reference_error=float(np.max(abs(cp.asnumpy(state)-reference)));assert reference_error<2e-5
            exp=np.empty(3,np.float64)
            cusv.compute_expectations_on_pauli_basis(handle,state.data.ptr,cuquantum.cudaDataType.CUDA_C_32F,n,exp.ctypes.data,[[cusv.Pauli.Z],[cusv.Pauli.Z],[cusv.Pauli.Z,cusv.Pauli.Z]],3,[[n-1],[n-3],[n-1,n-3]],[1,1,2])
            for matrix,target,controls in reversed(gates):apply(matrix,target,controls,1)
            cp.cuda.Stream.null.synchronize();echo=float(abs(state[0])**2);assert abs(echo-1)<.001
            records.append(dict(m=m,genus=(m-1)//2,qubits=n,amplitudes=2**n,statevector_bytes=2**n*8,physical_edges=2*m,layers=3,gate_count=len(gates),gpu_seconds=seconds,norm=norm,numpy_reference_max_error=reference_error,inverse_circuit_echo=echo,expectations=dict(Z_black0=float(exp[0]),Z_white0=float(exp[1]),ZZ_black0_white0=float(exp[2])),trained=False))
            print(json.dumps(records[-1]),flush=True)
    finally:cusv.destroy(handle)
    result=dict(passed=True,seed=20261104,gpu=name,platform=platform.platform(),versions={'cuquantum':cuquantum.__version__,'cupy':cp.__version__,'numpy':np.__version__},tensornet_contraction_error=contraction_error,records=records,scope='Actual cuStateVec and cuTensorNet execution on finite clean-dessin matter circuits. Large cases checked by normalization and inverse echo; independent NumPy reference only up to11qubits. No claim of training, hardware quantum execution, infinite surface limit or GRH proof.')
    args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(result,indent=2)+'\n')


if __name__=='__main__':main()
