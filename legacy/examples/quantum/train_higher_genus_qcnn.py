#!/usr/bin/env python3
"""Nine-qubit pooling on edge labels of the genus-four m=9 dessin.

Finite TFIM on the permitted quiver cycle, not a faithful surface-order action.
Sparse numerical eigenstate labels for an explicit finite Hamiltonian and a real PennyLane gate simulation.
"""
from pathlib import Path
import json
import numpy as np
from scipy.sparse import csr_matrix,diags
from scipy.sparse.linalg import eigsh
import pennylane as qml
ROOT=Path(__file__).resolve().parents[2];seed=20261105;rng=np.random.default_rng(seed)
def main():
 n=9;keep=5;d=2**n;hs=np.linspace(.2,1.9,12);indices=np.arange(d)
 bits=np.array([1-2*((indices>>(n-1-q))&1) for q in range(n)])
 zz=-sum(bits[q]*bits[(q+1)%n] for q in range(n))
 rows=np.tile(indices,n);cols=np.concatenate([indices^(1<<(n-1-q)) for q in range(n)])
 sx=csr_matrix((np.ones(n*d),(rows,cols)),shape=(d,d));states=[];residuals=[];energies=[]
 for h in hs:
  H=diags(zz)-h*sx
  val,vec=eigsh(H,k=1,which='SA',tol=1e-12,v0=np.ones(d)/np.sqrt(d))
  state=vec[:,0];states.append(state);energies.append(float(val[0]));residuals.append(float(np.linalg.norm(H@state-val[0]*state)))
 states=np.asarray(states);assert max(residuals)<1e-8
 train=np.array([i for i in range(12) if i%4]);test=np.array([i for i in range(12) if not i%4])
 dev=qml.device('default.qubit',wires=n,shots=None)
 @qml.qnode(dev,interface=None,diff_method=None)
 def scores(theta):
  qml.StatePrep(states,wires=range(n));theta=theta.reshape(2,n,2)
  for layer in range(2):
   for q in range(n):qml.RY(theta[layer,q,0],wires=q);qml.RZ(theta[layer,q,1],wires=q)
   for q in range(n):qml.CZ(wires=[q,(q+1)%n])
  for q in range(n-keep):qml.CNOT(wires=[q,keep+q])
  return qml.expval(qml.Projector([0]*(n-keep),wires=range(keep,n)))
 p=rng.normal(0,.12,4*n);m=np.zeros_like(p);v=m.copy();curve=[]
 for epoch in range(51):
  score=np.asarray(scores(p));curve.append(dict(epoch=epoch,train=float(1-score[train].mean()),test=float(1-score[test].mean())))
  if epoch==50:break
  g=np.empty_like(p)
  for j in range(len(p)):
   delta=np.zeros_like(p);delta[j]=np.pi/2;g[j]=-np.mean((np.asarray(scores(p+delta))-np.asarray(scores(p-delta)))[train])/2
  m=.9*m+.1*g;v=.999*v+.001*g*g;p-=.035*(m/(1-.9**(epoch+1)))/(np.sqrt(v/(1-.999**(epoch+1)))+1e-8)
 final=np.asarray(scores(p))
 out=dict(seed=seed,name='Genus-four nine-qubit QCNN',backend='PennyLane default.qubit CPU; sparse finite Hamiltonian eigensolver',qubits=n,parameters=len(p),epochs=50,train_size=len(train),test_size=len(test),architecture='two local Ry/Rz layers on nine edge qubits, cycle CZ, four CNOT pooling gates, trace out four qubits',objective='compress finite TFIM ground states on the permitted 9-cycle of the genus-four dessin; not a full order representation',theta=p.tolist(),curve=curve,hamiltonian_residual_max=max(residuals),genus=4,order_rank=162,examples=[dict(h=float(hs[i]),ground_energy=energies[i],discard_probability=float(1-final[i]),hamiltonian_residual=residuals[i]) for i in test])
 pth=ROOT/'outputs/experiments/higher-genus-qcnn';pth.mkdir(parents=True,exist_ok=True);(pth/'training.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps(dict(first=curve[0],last=curve[-1],residual=max(residuals)),indent=2))

if __name__=='__main__':main()
