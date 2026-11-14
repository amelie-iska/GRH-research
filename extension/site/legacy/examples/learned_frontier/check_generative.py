#!/usr/bin/env python3
"""Independent dense circuit and physics/oracle checks; no training/import installs."""
import argparse,json,math
from pathlib import Path
import numpy as np
import torch
from generative import QuantumFeatures, physical_teacher, oracle_field, spins, metrics


def literal_circuit(angles,theta,entangle):
    n=len(angles);state=np.zeros(2**n,complex);state[0]=1
    for layer in range(len(theta)):
        for q in range(n):
            a=angles[q]+theta[layer,q,0];p=.37*angles[q]+theta[layer,q,1]
            ry=np.array([[np.cos(a/2),-np.sin(a/2)],[np.sin(a/2),np.cos(a/2)]])
            rz=np.diag(np.exp(np.array([-.5j,.5j])*p));full=np.array([[1]],complex)
            for r in range(n):full=np.kron(full,rz@ry if r==q else np.eye(2))
            state=full@state
        if entangle:
            for q in range(n):
                output=np.zeros_like(state)
                for index,value in enumerate(state):
                    target=index^((((index>>(n-1-q))&1))<<(n-1-(q+1)%n))
                    output[target]=value
                state=output
    return np.array([sum(abs(state[i])**2*(-1)**((i&mask).bit_count()) for i in range(2**n)) for mask in range(1,2**n)])


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--device',choices=['cpu','cuda'],default='cpu');parser.add_argument('--output',required=True,type=Path);args=parser.parse_args()
    torch.manual_seed(20261104);rng=np.random.default_rng(20261104);device=torch.device(args.device)
    teacher=physical_teacher(device);p=teacher['probabilities'];rho=np.array(teacher['reduced_density'])
    assert np.linalg.eigvalsh(rho).min()>0 and abs(np.trace(rho)-1)<1e-10
    assert np.linalg.norm(rho-np.diag(np.diag(rho)))>.01
    I=np.eye(4)/4;a,b=.31,.72
    D=lambda R,t:math.exp(-t)*R+(1-math.exp(-t))*I
    semigroup_error=float(np.linalg.norm(D(D(rho,a),b)-D(rho,a+b)));assert semigroup_error<1e-12
    # Same measured Z distribution, different actual quantum density matrix.
    Z=np.diag([1,1,-1,-1]);other=Z@rho@Z
    assert np.allclose(np.diag(other),np.diag(rho)) and np.linalg.norm(other-rho)>.01
    errors=[];gradient_errors=[]
    for entangle in [False,True]:
        model=QuantumFeatures(entangle=entangle).to(device);theta=model.theta.detach().cpu().numpy().copy()
        angles=torch.tensor(rng.normal(size=(3,4)),dtype=torch.float32,device=device,requires_grad=True)
        actual=model(angles);reference=np.stack([literal_circuit(row,theta,entangle) for row in angles.detach().cpu().numpy()])
        error=float(np.max(abs(actual.detach().cpu().numpy()-reference)));assert error<3e-6,error;errors.append(error)
        actual.square().sum().backward();gradient=float(angles.grad[1,2]);h=.002
        aa=angles.detach().clone();aa[1,2]+=h;bb=angles.detach().clone();bb[1,2]-=h
        finite=float(((model(aa).square().sum()-model(bb).square().sum())/(2*h)).detach())
        assert abs(gradient-finite)<.006,(gradient,finite);gradient_errors.append(abs(gradient-finite))
    # Finite differences of an independently written Gaussian-mixture log density.
    x=np.array([[.2,-.5],[1.2,.8],[-.9,.3]]);centers=np.array([[1,1],[1,-1],[-1,1],[-1,-1]])
    prob=p.cpu().numpy().astype(float);t=np.array([.17,.41,.83]);sigma=.2
    score_errors=[]
    for objective in ['diffusion','flow']:
        xt=torch.tensor(x,dtype=torch.float64,device=device);tt=torch.tensor(t,dtype=torch.float64,device=device)
        actual=oracle_field(xt,tt,p,objective).cpu().numpy()
        for j in range(len(x)):
            if objective=='flow':
                tau=t[j];variance=(1-tau)**2+tau*tau*sigma*sigma;mean=tau*centers
            else:
                from generative import schedule
                _,_,ab=schedule(64,device);aval=float(ab[round(t[j]*64)]);variance=aval*sigma*sigma+1-aval;mean=math.sqrt(aval)*centers
            def logdensity(y):
                v=np.log(prob)-np.sum((y-mean)**2,1)/(2*variance);mx=v.max();return mx+np.log(np.exp(v-mx).sum())
            h=1e-5;score=np.array([(logdensity(x[j]+np.eye(2)[q]*h)-logdensity(x[j]-np.eye(2)[q]*h))/(2*h) for q in range(2)])
            if objective=='diffusion':reference=-math.sqrt(1-aval)*score
            else:
                # From score and xt=t*s+noise, infer posterior E[s] then E[v|xt].
                mean_s=(x[j]+variance*score)/tau
                reference=mean_s+(tau*sigma*sigma-(1-tau))/variance*(x[j]-tau*mean_s)
            err=float(np.max(abs(actual[j]-reference)));assert err<2e-6,(objective,err);score_errors.append(err)
    # Regression for the prior CUDA Long-matmul error: exact bit-index encoding.
    result=metrics(spins(2,device).repeat(64,1),p);assert result['histogram']==[.25]*4
    report=dict(passed=True,device=args.device,teacher_min_eigenvalue=teacher['minimum_density_eigenvalue'],
                teacher_coherence_norm=teacher['offdiagonal_norm'],channel_semigroup_error=semigroup_error,
                literal_numpy_circuit_errors=errors,autograd_finite_difference_errors=gradient_errors,
                oracle_finite_difference_errors=score_errors,bit_index_regression=True,
                measured_distribution_not_tomography=True,seed=20261104)
    args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))


if __name__=='__main__':main()
