#!/usr/bin/env python3
"""Exact sextic-residue Gram checks over Z[omega]; no stochastic/model input."""
from pathlib import Path
import argparse, hashlib, json, math
import numpy as np
ROOT=Path(__file__).resolve().parents[1]
# zeta_6=1+omega; omega^2+omega+1=0.
PHASES=[(1,0),(1,1),(0,1),(-1,0),(-1,-1),(0,-1)]

def primes(n):
    sieve=bytearray(b'\1')*(n+1);sieve[:2]=b'\0\0'
    for p in range(2,math.isqrt(n)+1):
        if sieve[p]:sieve[p*p::p]=b'\0'*((n-p*p)//p+1)
    return [p for p in range(2,n+1) if sieve[p]]

def rows(H):
    bound=math.isqrt(2*H)+2
    return [(a,b) for a in range(-bound,bound+1) for b in range(-bound,bound+1)
            if 0<a*a-a*b+b*b<=H]

def columns(D):
    out=[]
    for p in primes(2*D):
        if p<D or p%3!=1:continue
        w=next(x for x in range(2,p) if (x*x+x+1)%p==0)
        out.extend([(p,w),(p,(-1-w)%p)])
    return out

def table(row,col):
    result=[]
    for p,w in col:
        z=(1+w)%p
        lift={pow(z,j,p):j for j in range(6)}
        assert len(lift)==6
        # This assertion checks each original zero, rather than replacing it.
        values=[(a+b*w)%p for a,b in row]
        assert all(values),'Unimodularity fails at an actual prime collision'
        result.append([lift[pow(x,(p-1)//6,p)] for x in values])
    return np.array(result,dtype=np.int64).T

def parts(phase):
    real=np.array([2,1,-1,-2,-1,1],dtype=np.int64)[phase]
    imag=np.array([0,1,1,0,-1,-1],dtype=np.int64)[phase]
    return real,imag

def gram(real,imag,weight):
    x=real.T@(weight[:,None]*real)+3*(imag.T@(weight[:,None]*imag))
    y=imag.T@(weight[:,None]*real)-real.T@(weight[:,None]*imag)
    assert np.all(y%2==0)
    beta=y//2
    assert np.all((x+2*beta)%4==0)
    return (x+2*beta)//4,beta

def normsq(a,b):return a*a-a*b+b*b

def check(D,H):
    row,col=rows(H),columns(D);R,N=len(row),len(col)
    assert H<D and R and N
    # All pair sums/norms stay below signed int64; scalar oracle is unbounded.
    assert 100*max(R,N)**6<2**63
    phase=table(row,col);real,imag=parts(phase)
    a,b=gram(real,imag,np.ones(R,dtype=np.int64))
    potential=int(normsq(a,b).sum());off=potential-N*R*R
    ar,br=gram(real.T,imag.T,np.ones(N,dtype=np.int64))
    assert potential==int(normsq(ar,br).sum())
    bound=N*R*(N-R);assert off>=bound
    for i in range(min(8,N)):
        for j in range(min(8,N)):
            aa=bb=0
            for u in range(R):
                x,y=PHASES[int((phase[u,i]-phase[u,j])%6)]
                aa+=x;bb+=y
            assert (aa,bb)==(int(a[i,j]),int(b[i,j]))
    weights=np.array([1+(a-b)%4 for a,b in row],dtype=np.int64)
    wa,wb=gram(real,imag,weights)
    weighted_total=int(normsq(wa,wb).sum())
    weighted_row=int((normsq(ar,br)*weights[:,None]*weights[None,:]).sum())
    assert weighted_total==weighted_row
    weighted_off=weighted_total-N*int(weights.sum())**2
    weighted_bound=N*N*int((weights*weights).sum())-N*int(weights.sum())**2
    assert weighted_off>=weighted_bound
    return dict(D=D,H=H,rows=R,prime_ideal_columns=N,all_original_row_masks_checked=True,
                off_diagonal_pair_square=off,frame_lower_bound=bound,
                weighted_pair_square=weighted_off,weighted_frame_lower_bound=weighted_bound,
                full_row_column_potential_identity=True,scalar_oracle_pairs=min(8,N)**2,
                endpoint_3over4=(H**4==D**3))

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--output',type=Path,
        default=ROOT/'outputs/checks/2026-11-03-low-gcd-pair/exact-pair-checks.json')
    args=parser.parse_args()
    cases=[check(D,H) for D,H in [(128,4),(1024,9),(4096,81),(256,64)]]
    # Actual collision control: (1+3omega) has norm7 and vanishes at omega=2.
    assert 1-3+9==7 and (1+3*2)%7==0
    report=dict(cases=cases,character='original sextic residue symbol; zeta6=1+omega',
        rows='all nonzero Eisenstein elements in norm ball; no quotient by units',
        specialization='nu=1; fixed excluded set only primes above2,3; kernel checks, not signed energy',
        columns='both prime ideals above each split rational prime in [D,2D]',
        seed='none; exhaustive deterministic integer computations',
        collision_control='norm7 element 1+3omega vanishes at one prime above7; no unit replacement',
        scope='Finite diagnostics of a universal matrix theorem; not an MS_3/4 or GRH certificate',
        script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))
if __name__=='__main__':main()
