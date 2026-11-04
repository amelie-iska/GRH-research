#!/usr/bin/env python3
"""Exact finite good-ideal Euler restoration; no infinite-series certification."""
from pathlib import Path
from fractions import Fraction as Q
from itertools import product
import json,argparse
from check_mobius_split import universe,elements,quotient,scalar_symbol
from check_reciprocity_period import prime_symbol,power,emul,norm
ROOT=Path(__file__).resolve().parents[1]
ZERO=(Q(0),Q(0));ONE=(Q(1),Q(0))
PH=[(1,0),(1,1),(0,1),(-1,0),(-1,-1),(0,-1)]
def add(a,b):return(a[0]+b[0],a[1]+b[1])
def sub(a,b):return(a[0]-b[0],a[1]-b[1])
def mul(a,b):return emul(a,b)
def inv(a):
 q=norm(a);assert q
 return((a[0]-a[1])/q,-a[1]/q)
def div(a,b):return mul(a,inv(b))
def phase(e):return ZERO if e is None else tuple(map(Q,PH[e%6]))
def text(a):return list(map(str,a))
def valuation(u,pi):
 e=0
 while (v:=quotient(u,pi)) is not None:e+=1;u=v
 return e,u

def run():
 ideals,index,_,primes=universe(128)
 chosen=[pi for pi in primes if norm(pi) in [7,13,19,25]]
 assert len(chosen)==7 and any(norm(pi)==25 for pi in chosen)
 columns=[]
 for bits in product([0,1],repeat=len(chosen)):
  f=[(pi,1) for pi,b in zip(chosen,bits) if b];n=(1,0)
  for pi,_ in f:n=emul(n,pi)
  columns.append((n,tuple(f)))
 pi=chosen[0];u3=power(pi,3);u6=power(pi,6)
 rows=elements(25)+[u3,u6,emul(u3,chosen[2])]
 ds=[(1,0),chosen[0],chosen[-1],emul(chosen[0],chosen[2])]
 cases=terms=zeros=ramdrop=sixth=0;examples=[]
 for u,d,twist,sigma in product(rows,ds,[False,True],[1,2]):
  T={p for p in chosen if quotient(u,p) is not None or quotient(d,p) is not None}
  direct=ZERO
  for n,f in columns:
   if any(quotient(d,p) is not None for p,_ in f):continue
   exponent=scalar_symbol(f,u)
   if exponent is None:zeros+=1;continue
   if twist:exponent=(exponent+scalar_symbol(f,(2,0)))%6
   direct=add(direct,mul(phase(exponent),(Q(1,norm(n)**sigma),Q(0))));terms+=1
  primitive=correction=squarefree=ONE
  for p in chosen:
   e,unit=valuation(u,p);nu=prime_symbol(p,(2,0)) if twist else 0
   assert nu is not None
   a=ZERO if e%6 else phase(nu+prime_symbol(p,unit))
   b=ZERO if e%3 else phase(2*nu+2*prime_symbol(p,unit))
   z=(Q(1,norm(p)**sigma),Q(0));az=mul(a,z);bz2=mul(b,mul(z,z))
   r=div(sub(ONE,bz2),sub(ONE,az));primitive=mul(primitive,r)
   if p in T:correction=mul(correction,div(sub(ONE,az),sub(ONE,bz2)))
   else:
    assert b==mul(a,a);squarefree=mul(squarefree,add(ONE,az))
   if e%6==3:assert a==ZERO and b!=ZERO;ramdrop+=1
   if e and e%6==0:assert a!=ZERO and b!=ZERO;sixth+=1
  assert mul(primitive,correction)==squarefree==direct
  cases+=1
  if u in [u3,u6] and d==(1,0) and not twist and sigma==1:
   e,_=valuation(u,pi);z=(Q(1,norm(pi)),Q(0));a=ZERO if e==3 else ONE;b=ONE
   r=div(sub(ONE,mul(b,mul(z,z))),sub(ONE,mul(a,z)))
   c=inv(r);assert r!=ONE and mul(r,c)==ONE
   examples.append(dict(row=list(u),row_norm=norm(u),prime=list(pi),prime_norm=norm(pi),valuation=e,primitive_ratio=text(r),mask_restoration=text(c),correct_deleted_factor=text(ONE)))
 assert len(examples)==2 and ramdrop and sixth
 return dict(passed=True,finite_prime_ideals=7,squarefree_columns=128,rows=len(rows),cases=cases,direct_nonzero_terms=terms,original_zero_encounters=zeros,quadratic_conductor_drop_encounters=ramdrop,sixth_power_mask_encounters=sixth,examples=examples,scope='Exact finite ideal/phase identities including inert primes and full original zeros. Not an infinite Hecke continuation, conductor-uniform convexity, smooth contour or signed mean-square proof.')

def main():
 p=argparse.ArgumentParser();p.add_argument('--output',type=Path,default=ROOT/'outputs/checks/2026-11-03-hecke-type-i/exact.json');a=p.parse_args();r=run();a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r,indent=2))
if __name__=='__main__':main()
