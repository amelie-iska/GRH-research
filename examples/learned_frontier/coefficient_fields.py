#!/usr/bin/env python3
"""Exact finite-field polynomial learners and reversible quantum oracles.
A discrete coefficient network is distinct from a complex-amplitude QNN.
"""
from itertools import product
from pathlib import Path
import json,argparse


def predict(w,x,p):return (w[0]+w[1]*x[0]+w[2]*x[1]+w[3]*x[0]*x[1])%p


def run():
    records=[]
    for p in [2,3,5]:
        inputs=list(product(range(p),repeat=2));target=[x*y%p for x,y in inputs]
        affine=[]
        for a,b,c in product(range(p),repeat=3):affine.append(sum((a+b*x+c*y)%p!=v for (x,y),v in zip(inputs,target)))
        assert min(affine)>0
        checked=0;winner=None
        for w in product(range(p),repeat=4):
            checked+=1
            if all(predict(w,x,p)==v for x,v in zip(inputs,target)):winner=w;break
        assert winner is not None
        permutation=[]
        for x,y,z in product(range(p),repeat=3):
            out=(z+predict(winner,(x,y),p))%p;permutation.append(p*p*x+p*y+out)
        assert sorted(permutation)==list(range(p**3))
        # U_f is the permutation unitary; inverse subtracts f and retains inputs.
        for i,j in enumerate(permutation):
            x,y,z=i//(p*p),(i//p)%p,i%p
            assert j//(p*p)==x and (j//p)%p==y and (j%p-predict(winner,(x,y),p))%p==z
        records.append(dict(field=f'F{p}',characteristic=p,training='Exact discrete coefficient search; no real gradient',network='Constant, two input lanes, one product hidden lane, affine readout modulo p',weights=list(winner),coefficient_tuples_tested=checked,complete_input_count=p*p,minimum_affine_errors=min(affine),learned_errors=0,quantum_oracle_dimension=p**3,permutation=permutation,unitary_by_permutation=True))
    return dict(passed=True,models=records,scope='Finite field polynomial networks and complex-Hilbert reversible encodings; no unital field embedding Fp→R, continuous gradient over Fp, universal wide-QNN limit or GRH conclusion')


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--output',type=Path,required=True);args=parser.parse_args();result=run();args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps([{k:v for k,v in r.items() if k!='permutation'} for r in result['models']],indent=2))
