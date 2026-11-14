#!/usr/bin/env python3
"""Exact known-teacher reverse mixture control and matched seed repetitions.
No claim that the teacher-based sampler is a learned or efficient method.
"""
import argparse,json,hashlib
from pathlib import Path
import torch,numpy as np
from generative import physical_teacher,spins,schedule,sample_data,metrics,train_one


@torch.no_grad()
def exact_reverse(p,count=8192,T=64,sigma=.2):
    beta,alpha,ab=schedule(T,p.device);centers=spins(2,p.device)
    # Start from the exact forward marginal, avoiding a Gaussian-prior approximation.
    x=ab[T].sqrt()*sample_data(p,count,sigma)+(1-ab[T]).sqrt()*torch.randn(count,2,device=p.device)
    for k in range(T,0,-1):
        vt=ab[k]*sigma*sigma+1-ab[k];vp=ab[k-1]*sigma*sigma+1-ab[k-1]
        mean=ab[k].sqrt()*centers
        weights=torch.softmax(p.clamp_min(1e-30).log()[None]-(x[:,None]-mean[None]).square().sum(2)/(2*vt),1)
        chosen=centers[torch.multinomial(weights,1).flatten()];previous_mean=ab[k-1].sqrt()*chosen
        posterior_mean=previous_mean+alpha[k-1].sqrt()*vp/vt*(x-alpha[k-1].sqrt()*previous_mean)
        variance=vp*beta[k-1]/vt
        x=posterior_mean+variance.sqrt()*torch.randn_like(x)
    return x


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--output',required=True,type=Path);parser.add_argument('--seed',required=True,type=int);parser.add_argument('--steps',type=int,default=2000);parser.add_argument('--device',default='cuda');args=parser.parse_args()
    if args.output.exists():raise SystemExit('Preserve prior results: choose a new output directory')
    args.output.mkdir(parents=True);p=physical_teacher(args.device)['probabilities'];torch.manual_seed(args.seed);np.random.seed(args.seed)
    control=metrics(exact_reverse(p),p);records=[]
    for objective in ['diffusion','flow']:
        for entangle in [False,True]:
            record=train_one(p,objective,entangle,args.output,args.steps,seed=args.seed);records.append(record)
            print(json.dumps({'seed':args.seed,'objective':objective,'entangle':entangle,'evaluation':record['evaluation']}),flush=True)
    result=dict(seed=args.seed,records=records,exact_teacher_reverse_control=control,source_sha256=hashlib.sha256(Path(__file__).with_name('generative.py').read_bytes()).hexdigest(),scope='Matched finite-seed repeats and known-teacher exact reverse mixture; learned DDPM oracle-epsilon control separately retains Gaussian reverse-kernel approximation')
    (args.output/'record.json').write_text(json.dumps(result,indent=2)+'\n')


if __name__=='__main__':main()
