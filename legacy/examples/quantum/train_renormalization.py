#!/usr/bin/env python3
"""Train three nontrivial finite QNN architectures, then evaluate held-out data.

Fixed synthetic physics data, CPU only, seed 20261103. Qubit simulation and
parameter-shift differentiation are explicit NumPy, independently reproducible.
Framework adapters are separate; this script never installs packages.
"""
from pathlib import Path
import json, platform
import numpy as np
from surface_models import ansatz,graph_hamiltonian,reduced_keep,encoded_patch,patch_features,effective_ising
ROOT=Path(__file__).resolve().parents[2]
SEED=20261103
rng=np.random.default_rng(SEED)

def adam(params,grad,m,v,step,rate):
    m=.9*m+.1*grad; v=.999*v+.001*grad*grad
    params-=rate*(m/(1-.9**step))/(np.sqrt(v/(1-.999**step))+1e-8)
    return params,m,v

def pooling_scores(t,states,edges,projector):
    return abs(states@ansatz(t,4,edges).T)**2@projector

def pooling():
    edges=[(0,1),(1,2),(2,3),(3,0)]
    hs=np.linspace(.15,2.4,36)
    states=[]; energies=[]
    for h in hs:
        ev,vec=np.linalg.eigh(graph_hamiltonian(4,edges,float(h)))
        states.append(vec[:,0]); energies.append(float(ev[0]))
    states=np.array(states)
    train=np.array([i for i in range(len(hs)) if i%4!=0]); test=np.array([i for i in range(len(hs)) if i%4==0])
    theta=rng.normal(0,.2,16); m=np.zeros_like(theta);v=m.copy()
    # P_discard=|00><00| on the two discarded qubits.
    projector=np.array([1 if j%4==0 else 0 for j in range(16)])
    def scores(t): return pooling_scores(t,states,edges,projector)
    curve=[]
    for step in range(121):
        score=scores(theta);curve.append(dict(epoch=step,train=float(1-score[train].mean()),test=float(1-score[test].mean())))
        if step==120: break
        grad=np.empty_like(theta)
        for j in range(len(theta)):
            delta=np.zeros_like(theta);delta[j]=np.pi/2
            grad[j]=-(scores(theta+delta)[train]-scores(theta-delta)[train]).mean()/2
        theta,m,v=adam(theta,grad,m,v,step+1,.035)
    U=ansatz(theta,4,edges)
    checks=[];examples=[]
    for j in test:
        s=U@states[j];rho=reduced_keep(s,4,2)
        checks.append(dict(trace=float(np.trace(rho).real),min_eigenvalue=float(np.linalg.eigvalsh(rho).min())))
        examples.append(dict(h=float(hs[j]),discard_probability=float(1-scores(theta)[j]),kept_density=[[[float(z.real),float(z.imag)] for z in row] for row in rho]))
    assert all(abs(c['trace']-1)<1e-10 and c['min_eigenvalue']>-1e-10 for c in checks)
    return dict(name='Four-qubit QCNN compression',backend='NumPy statevector; framework adapter not executed',qubits=4,parameters=16,epochs=120,train_size=len(train),test_size=len(test),architecture='two local Ry/Rz layers, ring CZ, CNOT(0,2), CNOT(1,3), discard qubits 2,3',objective='1 minus probability of discarded qubits in 00; state compression, not exact Wilson RG',theta=theta.tolist(),curve=curve,examples=examples,checks=checks)

def convolution():
    pairs=rng.uniform(.05,1.7,(120,2)); states=np.array([encoded_patch(x) for x in pairs])
    targets=effective_ising(pairs[:,0],pairs[:,1])
    train=np.arange(90);test=np.arange(90,120)
    theta=rng.normal(0,.3,8);head=np.array([0.,0.,0.,.2]);params=np.r_[theta,head];m=np.zeros_like(params);v=m.copy()
    def evaluate(p):
        F=patch_features(p[:8],states);return F@p[8:11]+p[11],F
    curve=[]
    for step in range(181):
        pred,F=evaluate(params);err=pred-targets
        curve.append(dict(epoch=step,train=float(np.mean(err[train]**2)),test=float(np.mean(err[test]**2))))
        if step==180:break
        grad=np.zeros_like(params)
        for j in range(8):
            delta=np.zeros(8);delta[j]=np.pi/2
            derivative=(patch_features(params[:8]+delta,states)-patch_features(params[:8]-delta,states))/2
            grad[j]=2*np.mean(err[train]*(derivative@params[8:11])[train])
        grad[8:11]=2*np.mean(err[train,None]*F[train],axis=0);grad[11]=2*err[train].mean()
        params,m,v=adam(params,grad,m,v,step+1,.03)
    pred,_=evaluate(params)
    baseline=float(np.mean((targets[test]-targets[train].mean())**2))
    # Central finite differences test the actual loss gradient at final parameters.
    eps=1e-6;F=patch_features(params[:8],states);err=F@params[8:11]+params[11]-targets
    delta=np.zeros(8);delta[0]=np.pi/2
    analytic=2*np.mean(err[train]*(((patch_features(params[:8]+delta,states)-patch_features(params[:8]-delta,states))/2)@params[8:11])[train])
    d=np.zeros(12);d[0]=eps
    numeric=(np.mean((evaluate(params+d)[0][train]-targets[train])**2)-np.mean((evaluate(params-d)[0][train]-targets[train])**2))/(2*eps)
    assert abs(analytic-numeric)<1e-7
    return dict(name='Shared quantum graph convolution',backend='NumPy statevector; framework adapter not executed',qubits=2,parameters=12,epochs=180,train_size=90,test_size=30,architecture='Ry(K1), Ry(K2), shared two-layer circuit, three Pauli features, affine regression head',objective='regress exact Ising decimation atanh(tanh K1 tanh K2)',theta=params[:8].tolist(),head=params[8:].tolist(),curve=curve,constant_test_baseline=baseline,gradient_error=float(abs(analytic-numeric)),examples=[dict(k1=float(pairs[i,0]),k2=float(pairs[i,1]),exact=float(targets[i]),prediction=float(pred[i])) for i in test])

def attention():
    """Learn star-to-triangle Ising coupling data with quantum-feature attention."""
    couplings=rng.uniform(.1,1.5,(100,3));pairs=[(0,1),(1,2),(2,0)]
    states=np.array([[encoded_patch(k[[i,j]]) for i,j in pairs] for k in couplings])
    spins=np.array([[1 if b&(1<<q) else -1 for q in range(3)] for b in range(8)])
    logw=np.log(2*np.cosh(couplings@spins.T))
    targets=logw@np.array([spins[:,i]*spins[:,j] for i,j in pairs]).T/8
    train=np.arange(75);test=np.arange(75,100)
    p=np.r_[rng.normal(0,.2,8),rng.normal(0,.1,3),np.zeros(7)]
    m=np.zeros_like(p);v=m.copy();curve=[]
    def predict(t):
        F=patch_features(t[:8],states.reshape(-1,4)).reshape(-1,3,3)
        logits=F@t[8:11];logits-=logits.max(axis=1,keepdims=True)
        weights=np.exp(logits);weights/=weights.sum(axis=1,keepdims=True)
        context=(weights[:,:,None]*F).sum(axis=1)
        return F@t[11:14]+(context@t[14:17]+t[17])[:,None],weights
    def loss(t):return float(np.mean((predict(t)[0][train]-targets[train])**2))
    # End-to-end central differences differentiate the nonlinear attention head.
    eps=1e-5
    for step in range(121):
        pred,weights=predict(p);curve.append(dict(epoch=step,train=loss(p),test=float(np.mean((pred[test]-targets[test])**2))))
        if step==120:break
        grad=np.empty_like(p)
        for j in range(len(p)):
            d=np.zeros_like(p);d[j]=eps;grad[j]=(loss(p+d)-loss(p-d))/(2*eps)
        p,m,v=adam(p,grad,m,v,step+1,.025)
    pred,weights=predict(p)
    return dict(name='Quantum-feature graph attention',backend='NumPy statevector; framework adapter not executed',qubits=2,parameters=18,epochs=120,train_size=75,test_size=25,architecture='three shared two-qubit patch encoders, softmax quantum-feature scores, context aggregation and shared affine coupling readout',objective='learn exact zero-field star-to-triangle Ising decimation; central-difference Adam',theta=p.tolist(),curve=curve,constant_test_baseline=float(np.mean((targets[test]-targets[train].mean(axis=0))**2)),examples=[dict(couplings=couplings[i].tolist(),exact=targets[i].tolist(),prediction=pred[i].tolist(),attention=weights[i].tolist()) for i in test])

def main():
    out=dict(seed=SEED,python=platform.python_version(),numpy=np.__version__,scope='finite synthetic models; no hardware or GRH certification',models=[pooling(),convolution(),attention()])
    for folder in [ROOT/'outputs/experiments/renormalization',ROOT/'web/data']:
        folder.mkdir(parents=True,exist_ok=True);(folder/'training.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({m['name']:dict(first=m['curve'][0],last=m['curve'][-1]) for m in out['models']},indent=2))
if __name__=='__main__':main()
