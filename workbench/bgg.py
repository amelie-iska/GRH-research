"""Exact finite BGG-related reference computations, not a full category-O package.

Keep a genuine finite sl2 quotient separate from an arbitrary Verma cutoff.
The exterior differential is a linear/Koszul component, not an identification
of exterior-module BGG correspondence with highest-weight category O.
"""
from __future__ import annotations
import argparse,itertools,json
from fractions import Fraction
from pathlib import Path


def scalar(x):
    if type(x) not in (int,Fraction):raise ValueError('Exact integer/Fraction required')
    return Fraction(x)

def zero(n):return [[Fraction(0) for _ in range(n)] for _ in range(n)]
def identity(n):return [[Fraction(i==j) for j in range(n)] for i in range(n)]
def add(a,b):return [[x+y for x,y in zip(r,s)] for r,s in zip(a,b)]
def scale(c,a):return [[c*x for x in r] for r in a]
def multiply(a,b):
    n=len(a)
    if n==0 or len(b)!=n or any(len(r)!=n for r in a+b):raise ValueError('Equal square matrices required')
    return [[sum((a[i][k]*b[k][j] for k in range(n)),Fraction(0)) for j in range(n)] for i in range(n)]
def commutator(a,b):return add(multiply(a,b),scale(-1,multiply(b,a)))
def nonzero(a):return [[i,j,str(x)] for i,r in enumerate(a) for j,x in enumerate(r) if x]


def sl2(lam,cutoff):
    lam=scalar(lam)
    if type(cutoff)is not int or not 1<=cutoff<=32:raise ValueError('Cutoff must be an integer in [1,32]')
    e,f,h=zero(cutoff),zero(cutoff),zero(cutoff)
    for i in range(cutoff):
        h[i][i]=lam-2*i
        if i:e[i-1][i]=i*(lam-i+1)
        if i+1<cutoff:f[i+1][i]=1
    return e,f,h


def sl2_defects(lam,cutoff):
    e,f,h=sl2(lam,cutoff)
    return {'ef_minus_h':nonzero(add(commutator(e,f),scale(-1,h))),
            'he_minus_2e':nonzero(add(commutator(h,e),scale(-2,e))),
            'hf_plus_2f':nonzero(add(commutator(h,f),scale(2,f))),
            'twice_casimir_defect':nonzero(add(add(scale(2,add(multiply(e,f),multiply(f,e))),multiply(h,h)),scale(-scalar(lam)*(scalar(lam)+2),identity(cutoff))))}


def exterior_generators(m):
    if type(m)is not int or not 1<=m<=5:raise ValueError('Exterior dimension must be in [1,5]')
    n=1<<m;ops=[]
    for j in range(m):
        a=zero(n)
        for mask in range(n):
            if not(mask&(1<<j)):
                a[mask|(1<<j)][mask]=(-1)**((mask&((1<<j)-1)).bit_count())
        ops.append(a)
    return ops


def differential(xs):
    xs=[scalar(x) for x in xs];ops=exterior_generators(len(xs));d=zero(len(ops[0]))
    for x,a in zip(xs,ops):d=add(d,scale(x,a))
    return d


def contracting_homotopy(xs):
    xs=[scalar(x) for x in xs];m=len(xs);exterior_generators(m)
    j=next((j for j,x in enumerate(xs) if x),None)
    if j is None:raise ValueError('Zero differential has no contracting homotopy')
    h=zero(1<<m)
    for mask in range(1<<m):
        if mask&(1<<j):h[mask^(1<<j)][mask]=Fraction((-1)**((mask&((1<<j)-1)).bit_count()),1)/xs[j]
    return h


def report():
    quotients=[{'highest_weight':n,'dimension':n+1,'defects':sl2_defects(n,n+1)} for n in range(9)]
    cutoffs=[{'highest_weight':2,'cutoff':k,'predicted_top_defect':k*(k-3),'defects':sl2_defects(2,k)} for k in (2,3,4,8)]
    x=[2,3,-1];d=differential(x);h=contracting_homotopy(x)
    return {'schema':'grh.bgg-finite.v1','finite_quotients':quotients,'verma_cutoffs':cutoffs,
      'exterior':{'coefficients':x,'dimension':8,'d_squared_zero':not nonzero(multiply(d,d)),'homotopy_identity':add(multiply(d,h),multiply(h,d))==identity(8)},
      'scope':'Exact rational finite examples. General Verma/BGG/category-O claims have written arguments and attributed sources. No trained BGG head or category-O reconstruction from physical data is reported.'}

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',type=Path);a=p.parse_args();text=json.dumps(report(),indent=2)
    if a.output:a.output.write_text(text+'\n')
    else:print(text)
