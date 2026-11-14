"""Genuine cuStateVec verification of emitted arithmetic and learned RG gates.

No CPU fallback is called GPU. Dense ECC cases are p=7 at 16 and 22 logical
qubits; p=13 retains exhaustive basis checks. The finite compiler's full resource
cost is recorded. No gate-synthesis, routing or error-correction cost is hidden.
"""
from __future__ import annotations
import argparse,hashlib,json,math,sys,time
from pathlib import Path
import numpy as np
import cupy as cp
from cuquantum import ComputeType,cudaDataType
from cuquantum.bindings import custatevec as csv
from .ecc import execute_words
from .quantum_reference import hierarchy_kraus,channel,lifted_gates,partial_trace_np

ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'extension/quantum'))
from gpu_experiments import environment

class Dense:
 def __init__(self,n):
  if type(n)is not int or not 1<=n<=22:raise ValueError('Dense audit is bounded at 22 qubits')
  free,_=cp.cuda.runtime.memGetInfo();required=(1<<n)*16
  if free-required<2*1024**3:raise MemoryError('Respect 2 GiB reserve')
  self.n=n;self.h=csv.create();self.state=cp.zeros(1<<n,dtype=cp.complex128);self.workspace=None;self.workspace_size=0
  self.X=np.ascontiguousarray([[0,1],[1,0]],dtype=np.complex128)
 def gate(self,g):
  op=g['gate'];controls=g.get('controls',[])
  if op=='CX'and not controls:controls=[g['control']]
  t=g['target']
  if op in('X','CX','CCX'):matrix=self.X
  elif op=='RY':
   c=math.cos(g['angle']/2);s=math.sin(g['angle']/2);matrix=np.ascontiguousarray([[c,-s],[s,c]],dtype=np.complex128)
  else:raise ValueError('Unsupported emitted gate')
  if len(set(controls+[t]))!=len(controls)+1 or any(not 0<=q<self.n for q in controls+[t]):raise ValueError('Invalid wires')
  size=csv.apply_matrix_get_workspace_size(self.h,cudaDataType.CUDA_C_64F,self.n,matrix.ctypes.data,cudaDataType.CUDA_C_64F,csv.MatrixLayout.ROW,0,1,len(controls),ComputeType.COMPUTE_64F)
  if size>self.workspace_size:self.workspace=cp.cuda.alloc(size);self.workspace_size=size
  csv.apply_matrix(self.h,self.state.data.ptr,cudaDataType.CUDA_C_64F,self.n,matrix.ctypes.data,cudaDataType.CUDA_C_64F,csv.MatrixLayout.ROW,0,[t],1,controls,[1]*len(controls),len(controls),ComputeType.COMPUTE_64F,0 if self.workspace is None else self.workspace.ptr,self.workspace_size)
  if op=='RY':cp.cuda.runtime.deviceSynchronize()
 def close(self):
  cp.cuda.runtime.deviceSynchronize();csv.destroy(self.h);self.state=None;self.workspace=None;cp.get_default_memory_pool().free_all_blocks()


def independent_count(c):
 counts={'X':0,'CX':0,'CCX':0};ends=[0]*c['qubits']
 for gate in c['gates']:
  controls=gate['controls'];expected={0:'X',1:'CX',2:'CCX'}.get(len(controls))
  if gate['gate']!=expected:raise ValueError('Invalid primitive declaration')
  counts[expected]+=1;wires=controls+[gate['target']];layer=1+max(ends[w]for w in wires)
  for w in wires:ends[w]=layer
 return dict(gates={k:v for k,v in counts.items()if v},total_gates=sum(counts.values()),depth_all_to_all=max(ends))


def audit(eccdir,qrgfile,output):
 record=dict(schema='grh.program3-gpu.v1',environment=environment(),ecc=[],hierarchy=[],source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
 for path in sorted(eccdir.glob('ecc-*.json')):
  c=json.loads(path.read_text());counts=independent_count(c)
  if any(counts[k]!=c['resources'][k]for k in counts):raise ValueError('Independent recount mismatch')
  row=dict(file=path.name,circuit_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),independent_counts=counts)
  if c['curve']['p']!=7:row['dense_gpu']='not_run; exhaustive basis checks in ECC report';record['ecc'].append(row);continue
  n=c['qubits'];s=len(c['scalar_wires']);w=c['encoding']['point_bits'];N=1<<(s+w);rng=np.random.default_rng(514)
  psi=rng.normal(size=N)+1j*rng.normal(size=N);psi/=np.linalg.norm(psi);start=time.perf_counter();st=Dense(n)
  try:
   st.state[:N].set(psi)
   for g in c['gates']:st.gate(g)
   cp.cuda.runtime.deviceSynchronize();out=st.state.get();mapping=execute_words(c['gates'],np.arange(N,dtype=np.uint64));expected=np.zeros_like(out);expected[mapping]=psi
   error=float(np.max(abs(out-expected)));dirty=float(np.sum(abs(out[N:])**2));norm=float(np.vdot(out,out).real)
   if error>1e-12 or dirty>1e-14 or abs(norm-1)>1e-12:raise ValueError('Coherent arithmetic/cleanup mismatch')
   row.update(dense_gpu='passed',qubits=n,full_state_amplitudes=len(out),coherent_input_terms=N,max_amplitude_error=error,dirty_ancilla_probability=dirty,norm2=norm,wall_seconds=time.perf_counter()-start)
  finally:st.close()
  record['ecc'].append(row)
 q=json.loads(qrgfile.read_text())
 for r in q['thermal_runs']:
  for i,x in enumerate([[.2,.4,.6,.8],[-.7,.3,1.1,-.2],[0.,0.,0.,0.]]):
   theta=r['weights']['theta'];st=Dense(4)
   try:
    psi=np.ones(1,complex)
    for a in reversed(x):psi=np.kron(psi,[math.cos(a/2),math.sin(a/2)])
    st.state.set(psi)
    for g in lifted_gates(theta):st.gate(g)
    cp.cuda.runtime.deviceSynchronize();evolved=st.state.get();rho=partial_trace_np(np.outer(evolved,evolved.conj()),[0],4)
    _,_,ks=hierarchy_kraus(theta);reference=channel(np.outer(psi,psi.conj()),ks);err=float(np.max(abs(rho-reference)))
    if err>1e-12:raise ValueError('GPU circuit/Kraus mismatch')
    record['hierarchy'].append(dict(seed=r['seed'],input=i,channel_output_real=rho.real.tolist(),gpu_kraus_error=err,qubits=4,actual_gate_count=len(lifted_gates(theta))))
   finally:st.close()
 record['scope']='Actual classical GPU simulation of emitted reversible and trained quantum circuits; not hardware, error-corrected physical costs or large-curve extrapolation.'
 output.parent.mkdir(parents=True,exist_ok=True);output.write_text(json.dumps(record,indent=2)+'\n');return record

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--ecc',type=Path,required=True);p.add_argument('--qrg',type=Path,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args();print(json.dumps(audit(a.ecc,a.qrg,a.output),indent=2))
