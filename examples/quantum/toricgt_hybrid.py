#!/usr/bin/env python3
"""Train a finite ToricGT/Weyl hybrid surrogate; certify rational test bounds.

Imports the pinned upstream toric_algebra.py directly, without modifying or
importing the full language-model package. The quantum features are simulated
by PennyLane. Exact rational principal minors accept/repair spectral proposals.
This is a finite Harper model, not a claimed arithmetic L-function operator.
"""
from pathlib import Path
import sys,importlib.util,json
from fractions import Fraction as Q
from itertools import combinations
import numpy as np
import pennylane as qml
from surface_models import ansatz,encoded_patch
ROOT=Path(__file__).resolve().parents[2]
file=ROOT/'external/ToricGT/src/toricgt/toric_algebra.py'
spec=importlib.util.spec_from_file_location('pinned_toricgt_algebra',file);upstream=importlib.util.module_from_spec(spec);sys.modules[spec.name]=upstream;spec.loader.exec_module(upstream)
U,V=upstream.RotationAlgebraApproximant(.25,max_denominator=4).generators()
assert U.shape==(4,4) and np.linalg.norm(V@U-1j*U@V)<1e-12
dev=qml.device('default.qubit',wires=2,shots=None)
@qml.qnode(dev,interface=None,diff_method=None)
def circuit(theta,states):
 qml.StatePrep(states,wires=[0,1]);qml.QubitUnitary(ansatz(theta,2,[(0,1)]),wires=[0,1])
 return qml.expval(qml.PauliZ(0)),qml.expval(qml.PauliZ(1)),qml.expval(qml.PauliZ(0)@qml.PauliZ(1))

def determinant(A):
 A=[list(row) for row in A];out=Q(1);n=len(A)
 for i in range(n):
  j=next((j for j in range(i,n) if A[j][i]),None)
  if j is None:return Q(0)
  if i!=j:A[i],A[j]=A[j],A[i];out=-out
  pivot=A[i][i];out*=pivot
  for j in range(i+1,n):
   ratio=A[j][i]/pivot
   for k in range(i+1,n):A[j][k]-=ratio*A[i][k]
 return out

def exact_h(lam):
 return [[Q([2,0,-2,0][i]) if i==j else lam if (i-j)%4 in [1,3] else Q(0) for j in range(4)] for i in range(4)]

def minors(h,E):
 shifted=[[h[i][j]-(E if i==j else 0) for j in range(4)] for i in range(4)]
 return [determinant([[shifted[i][j] for j in ix] for i in ix]) for size in range(1,5) for ix in combinations(range(4),size)]

def certify(lam,proposal):
 if lam<0:raise ValueError("The stated Gershgorin bound requires lambda >= 0")
 h=exact_h(lam);trial=Q(int(np.floor(proposal*256)),256)
 values=minors(h,trial);accepted=all(x>=0 for x in values)
 lo=-2-2*lam # Gershgorin lower bound, independently valid.
 assert all(x>=0 for x in minors(h,lo))
 if accepted:lo=max(lo,trial)
 hi=Q(-2) # Rayleigh quotient at basis vector 2.
 # The learned trial is checked, not silently trusted. Exact bisection repairs it.
 if not accepted and trial<hi:hi=trial
 for _ in range(16):
  mid=(lo+hi)/2
  if all(x>=0 for x in minors(h,mid)):lo=mid
  else:hi=mid
 vals=minors(h,lo);assert all(x>=0 for x in vals)
 return dict(lambda_rational=str(lam),learned_proposal=proposal,rational_trial=str(trial),proposal_accepted=accepted,certified_lower=str(lo),certified_upper_bracket=str(hi),principal_minors=[str(x) for x in vals],scope='exact rational PSD certificate for lower bound; bracket upper follows failed PSD or Rayleigh bound')

def main():
 seed=20261104;rng=np.random.default_rng(seed);lam=rng.uniform(.1,1.8,100)
 states=np.array([encoded_patch([x,.7*x*x]) for x in lam])
 targets=np.array([np.linalg.eigvalsh(U+U.conj().T+x*(V+V.conj().T))[0]/6 for x in lam])
 train=np.arange(75);test=np.arange(75,100);p=np.r_[rng.normal(0,.2,8),np.zeros(4)];m=np.zeros_like(p);v=m.copy();curve=[]
 def features(t):return np.asarray(circuit(t,states)).T
 for epoch in range(161):
  F=features(p[:8]);pred=F@p[8:11]+p[11];err=pred-targets
  curve.append(dict(epoch=epoch,train=float(np.mean(err[train]**2)),test=float(np.mean(err[test]**2))))
  if epoch==160:break
  g=np.zeros_like(p)
  for j in range(8):
   d=np.zeros(8);d[j]=np.pi/2;dF=(features(p[:8]+d)-features(p[:8]-d))/2
   g[j]=2*np.mean(err[train]*(dF@p[8:11])[train])
  g[8:11]=2*np.mean(err[train,None]*F[train],axis=0);g[11]=2*err[train].mean()
  m=.9*m+.1*g;v=.999*v+.001*g*g;p-=.025*(m/(1-.9**(epoch+1)))/(np.sqrt(v/(1-.999**(epoch+1)))+1e-8)
 cert=[]
 for x in [Q(1,4),Q(1,2),Q(3,4),Q(1),Q(5,4),Q(3,2)]:
  state=np.array([encoded_patch([float(x),.7*float(x*x)])]);f=np.asarray(circuit(p[:8],state)).reshape(3)
  cert.append(certify(x,float((f@p[8:11]+p[11])*6)))
 out=dict(seed=seed,name='Hybrid ToricGT spectral surrogate',backend='PennyLane default.qubit CPU + pinned ToricGT Weyl matrices + exact Fraction certificates',qubits=2,parameters=12,epochs=160,train_size=75,test_size=25,architecture='ToricGT rational Weyl carrier, two-qubit feature circuit, classical affine readout, exact rational principal-minor verifier',objective='predict normalized lowest Harper eigenvalue; exact verifier accepts or repairs lower-bound proposals',theta=p.tolist(),curve=curve,constant_test_baseline=float(np.mean((targets[test]-targets[train].mean())**2)),examples=cert,upstream_commit=json.loads((ROOT/'book/toricgt-pins.json').read_text())[0]['commit'])
 path=ROOT/'outputs/experiments/toricgt-hybrid';path.mkdir(parents=True,exist_ok=True);(path/'training.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps(dict(first=curve[0],last=curve[-1],certificates=len(cert)),indent=2))
if __name__=='__main__':main()
