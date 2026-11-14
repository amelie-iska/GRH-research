#!/usr/bin/env python3
"""Specified quantum random-feature width limit and full-action RG readout fits.

This is a frozen-feature/readout-only limit, not the asymptotic theorem of the
finite trainable4qubit diffusion networks. No install or training on import.
"""
from pathlib import Path
import sys,json,argparse,math
import numpy as np
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'examples/rg'))
from rg_math import black_decimation


def run():
    seed=20261104;rng=np.random.default_rng(seed);x=rng.uniform(-.7,.7,(128,3));train=x[:96];test=x[96:]
    y=np.array([black_decimation(5,p) for p in x]);mean=y[:96].mean(0);center=y-mean
    squared=((x[:,None]-x[None])**2).sum(2);exact=np.exp(-squared/2);lam=1e-5
    exact_prediction=exact[96:,:96]@np.linalg.solve(exact[:96,:96]+lam*np.eye(96),center[:96])+mean
    rows=[]
    for width in [16,64,256,1024,4096]:
        errors=[];tests=[]
        for replica in range(8):
            g=np.random.default_rng(seed+replica);w=g.normal(size=(width,3));phase=g.uniform(0,2*np.pi,width)
            phi=np.sqrt(2)*np.cos(x@w.T+phase);gram=phi@phi.T/width
            assert np.linalg.eigvalsh(gram).min()>-1e-10
            pred=gram[96:,:96]@np.linalg.solve(gram[:96,:96]+lam*np.eye(96),center[:96])+mean
            errors.append(float(np.linalg.norm(gram-exact)/np.linalg.norm(exact)));tests.append(float(np.mean((pred-y[96:])**2)))
        rows.append(dict(width=width,replicas=8,kernel_relative_Frobenius_mean=float(np.mean(errors)),kernel_relative_Frobenius_std=float(np.std(errors,ddof=1)),RG_full_action_test_MSE_mean=float(np.mean(tests)),RG_full_action_test_MSE_std=float(np.std(tests,ddof=1))))
    assert rows[-1]['kernel_relative_Frobenius_mean']<rows[0]['kernel_relative_Frobenius_mean']
    tropical=[];scores=np.array([-.3,.2,1.])
    for tau in [1.,.5,.2,.1,.03]:
        maximum=float(scores.max());soft=maximum+tau*math.log(float(np.exp((scores-maximum)/tau).sum()));gap=soft-maximum
        assert -1e-12<=gap<=tau*math.log(len(scores))+1e-12
        tropical.append(dict(tau=tau,maximum=maximum,logsumexp=soft,gap=gap,upper_bound=tau*math.log(len(scores))))
    return dict(passed=True,seed=seed,train_count=96,test_count=32,full_action_outputs=32,ridge=lam,
                feature='sqrt(2)<Z> for RY(w dot x+b)|0>; w standard Gaussian,b uniform phase',
                exact_kernel='exp(-||x-y||^2/2)',readout_only=True,rows=rows,
                exact_kernel_RG_test_MSE=float(np.mean((exact_prediction-y[96:])**2)),tropical=tropical,
                valuation_examples=[dict(field='Q',f='1+T',g='-1+T',val_f=0,val_g=0,val_sum=1,sum='2T'),dict(field='F2',f='1+T',g='1+T',val_f=0,val_g=0,val_sum='infinity',sum='0')],
                scope='Specified frozen random-feature/readout experiment and elementary tropical limits; no universal trained-QNN infinite-width limit, HMS functor, arithmetic positivity or GRH proof')


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--output',required=True,type=Path);args=parser.parse_args();r=run();args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r,indent=2))
