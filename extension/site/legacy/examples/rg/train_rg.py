#!/usr/bin/env python3
"""Actual full-action RG regression with PennyLane features and a classical head.

All labels are exact7-to5-spin decimation on a genus-two clean dessin.
The learner approximates ALL32 logweights, including their constant. Subsequent
RG steps are exact marginalization of that predicted action, not learned flow.
"""
from pathlib import Path
import hashlib,json,platform
import numpy as np
import pennylane as qml
from scipy.special import logsumexp
from rg_math import black_decimation,walsh,decimate,spins,classical_flow
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'outputs/experiments/actual-rg';SEED=20261103

def dataset():
    rng=np.random.default_rng(SEED)
    x=rng.uniform([.15,.15,-.6],[1.1,1.1,.6],(160,3));perm=rng.permutation(160)
    ood=rng.uniform([1.15,1.15,-.8],[1.5,1.5,.8],(40,3))
    y=np.array([black_decimation(5,p) for p in x]);yo=np.array([black_decimation(5,p) for p in ood])
    return x,y,perm[:120],perm[120:],ood,yo

DEV=qml.device('default.qubit',wires=3,shots=None)
@qml.qnode(DEV,interface=None,diff_method=None)
def circuit(theta,x):
    for q in range(3):qml.RY(x[:,q],wires=q)
    for l in range(2):
        for q in range(3):qml.RY(theta[l,q,0],wires=q);qml.RZ(theta[l,q,1],wires=q)
        for a,b in [(0,1),(1,2),(2,0)]:qml.CZ(wires=[a,b])
    return tuple(qml.expval(qml.prod(*(qml.PauliZ(q) for q in range(3) if mask>>(2-q)&1))) for mask in range(1,8))

def encode(x):return np.asarray(x)*np.array([1.5,1.5,2.])
def features(theta,x):return np.asarray(circuit(theta.reshape(2,3,2),encode(x))).T

def metrics(pred,target):
    lp=pred-logsumexp(pred,axis=1,keepdims=True);lt=target-logsumexp(target,axis=1,keepdims=True)
    pp=np.exp(lp);pt=np.exp(lt);eps=np.max(abs(pred-target),axis=1)
    return dict(logweight_mse=float(np.mean((pred-target)**2)),
        KL_target_to_prediction=float(np.mean(np.sum(pt*(lt-lp),axis=1))),
        mean_TV=float(np.mean(.5*np.abs(pp-pt).sum(1))),
        mean_abs_logZ_error=float(np.mean(abs(logsumexp(pred,axis=1)-logsumexp(target,axis=1)))),
        max_logweight_error=float(np.max(eps)),
        max_magnetization_error=float(np.max(abs((pp-pt)@spins(5)))))

def ridge(f,y):return np.linalg.solve(f.T@f+1e-5*np.eye(f.shape[1]),f.T@y)
def augmented(f):return np.c_[f,np.ones(len(f))]
def classical_features(x):
    a,b,c=x.T
    return np.c_[a,b,c,a*a,b*b,a*b,c*c,np.ones(len(x))]

def main():
    OUT.mkdir(parents=True,exist_ok=True);x,y,train,test,ood,yo=dataset()
    data=dict(seed=SEED,parameters=x.tolist(),targets=y.tolist(),train=train.tolist(),test=test.tolist(),ood_parameters=ood.tolist(),ood_targets=yo.tolist(),m=5,action_convention='V=log unnormalized Boltzmann weight; ALL32 states and constant retained')
    raw=(json.dumps(data,indent=2)+'\n').encode();path=OUT/'dataset.json'
    if path.exists():assert path.read_bytes()==raw,'Protected dataset differs; choose a new experiment directory'
    else:path.write_bytes(raw)
    mean=y[train].mean(0);scale=float(np.std(y[train]-mean));ys=(y-mean)/scale
    rng=np.random.default_rng(SEED+1);theta=rng.normal(0,.3,12)
    f=augmented(features(theta,x[train]));head=ridge(f,ys[train])
    def loss(t,h):return np.mean((augmented(features(t,x[train]))@h-ys[train])**2)
    fgrad=2*(f@head-ys[train])@head[:-1].T/(len(train)*32)
    gradient=[]
    for j in range(12):
        d=np.zeros(12);d[j]=np.pi/2
        gradient.append(np.sum(fgrad*(features(theta+d,x[train])-features(theta-d,x[train]))/2))
    check=[]
    for j in [0,5,11]:
        d=np.zeros(12);d[j]=1e-5
        numerical=(loss(theta+d,head)-loss(theta-d,head))/2e-5
        check.append(abs(numerical-gradient[j]))
    assert max(check)<1e-6
    p=np.r_[theta,head.ravel()];mom=np.zeros_like(p);var=mom.copy();curve=[]
    for epoch in range(121):
        theta=p[:12];head=p[12:].reshape(8,32)
        f=features(theta,x);fa=augmented(f);pred=(fa@head)*scale+mean
        curve.append(dict(epoch=epoch,train=float(np.mean((pred[train]-y[train])**2)),test=float(np.mean((pred[test]-y[test])**2))))
        if epoch%20==0:
            (OUT/f'checkpoint-{epoch:03d}.json').write_text(json.dumps(dict(epoch=epoch,theta=theta.tolist(),head=head.tolist(),train_loss=curve[-1]['train']),indent=2)+'\n')
            print(json.dumps(curve[-1]),flush=True)
        if epoch==120:break
        residual=fa[train]@head-ys[train]
        headgrad=2*fa[train].T@residual/(len(train)*32)
        fg=2*residual@head[:-1].T/(len(train)*32)
        tg=[]
        for j in range(12):
            d=np.zeros(12);d[j]=np.pi/2
            tg.append(np.sum(fg*(features(theta+d,x[train])-features(theta-d,x[train]))/2))
        g=np.r_[tg,headgrad.ravel()];mom=.9*mom+.1*g;var=.999*var+.001*g*g
        p-=.008*(mom/(1-.9**(epoch+1)))/(np.sqrt(var/(1-.999**(epoch+1)))+1e-8)
    theta=p[:12];head=p[12:].reshape(8,32)
    pred=augmented(features(theta,x))@head*scale+mean
    opred=augmented(features(theta,ood))@head*scale+mean
    base=ridge(classical_features(x[train]),ys[train]);bp=classical_features(x)@base*scale+mean
    bo=classical_features(ood)@base*scale+mean
    examples=[]
    for i in test[:6]:
        pf=classical_flow(5,x[i],initial=pred[i]);ef=classical_flow(5,x[i],initial=y[i]);eps=float(np.max(abs(pred[i]-y[i])))
        for a,b in zip(pf,ef):
            assert np.max(abs(np.array(a['logweights'])-b['logweights']))<=eps+1e-11
        examples.append(dict(index=int(i),parameters=x[i].tolist(),exact_logweights=y[i].tolist(),predicted_logweights=pred[i].tolist(),exact_couplings=walsh(y[i]).tolist(),predicted_couplings=walsh(pred[i]).tolist(),sup_error=eps,exact_flow=ef,predicted_flow=pf))
    result=dict(seed=SEED,name='Dessin full-action quantum RG learner',backend=f'PennyLane{qml.__version__} default.qubit CPU analytic expectations',python=platform.python_version(),
        m=5,genus=2,physical_sites=7,retained_sites=5,qubits=3,parameters=len(p),circuit_parameters=12,head_parameters=256,
        epochs=120,train_size=len(train),test_size=len(test),ood_size=len(ood),
        training_objective='MSE of all32 unnormalized coarse logweights; constant retained',
        initialization='training-only ridge warm start of classical head; joint circuit/head Adam thereafter',
        architecture='3 encoded coupling parameters -> two Ry/Rz+CZ layers -> seven PauliZ-product features -> affine32-state logweight head -> exact subsequent RG',
        theta=theta.tolist(),head=head.tolist(),target_mean=mean.tolist(),target_scale=scale,curve=curve,
        test_metrics=metrics(pred[test],y[test]),ood_metrics=metrics(opred,yo),
        classical_baseline=dict(features='seven quadratic/coupling features plus bias; same256 readout parameters, no circuit',test=metrics(bp[test],y[test]),ood=metrics(bo,yo)),
        gradient_max_error=float(max(check)),examples=examples,
        dataset_sha256=hashlib.sha256(raw).hexdigest(),
        scope='Learned finite full-action RG approximation on tied3parameter family; no uniform parameter-space accuracy, quantum advantage, physical hardware or arithmetic bridge')
    (OUT/'training.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(final=result['test_metrics'],ood=result['ood_metrics'],baseline=result['classical_baseline']['test']),indent=2),flush=True)
if __name__=='__main__':main()
