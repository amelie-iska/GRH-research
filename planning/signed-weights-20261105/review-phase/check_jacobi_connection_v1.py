#!/usr/bin/env python3
"""Fresh exact Jacobi/partial-two-pivot controls; never runs old Gauss tables."""
from pathlib import Path
from itertools import product
from math import isqrt
from collections import Counter
import json,hashlib,time
ROOT=Path(__file__).resolve().parents[3]
OUT=ROOT/'outputs/checks/2026-11-05-signed-weights/review-phase'
PH=((1,0),(1,1),(0,1),(-1,0),(-1,-1),(0,-1))
def add(x,y):return x[0]+y[0],x[1]+y[1]
def mul(x,y):return x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0]-x[1]*y[1]
def conj(x):return x[0]-x[1],-x[1]
def neg(x):return -x[0],-x[1]
def norm(x):return x[0]*x[0]-x[0]*x[1]+x[1]*x[1]
def quotient(x,y):
 a,b=mul(x,conj(y));q=norm(y)
 return (a//q,b//q) if a%q==b%q==0 else None
def total(xs):
 a=(0,0)
 for x in xs:a=add(a,x)
 return a
class Field:
 def __init__(self,beta):
  self.beta=beta;self.Q=norm(beta);self.inert=beta[1]==0;self.p=isqrt(self.Q) if self.inert else self.Q
  assert self.p>=5 and all(self.p%d for d in range(2,isqrt(self.p)+1))
  self.root=None if self.inert else (-beta[0]*pow(beta[1],-1,self.p))%self.p
  if self.root is not None:assert (self.root*self.root+self.root+1)%self.p==0
  self.xs=list(product(range(self.p),repeat=2)) if self.inert else [(i,0) for i in range(self.p)]
  self.zero=(0,0);self.one=(1,0)
  self.phases={self.embed(z):i for i,z in enumerate(PH)};assert len(self.phases)==6
  self.chi={x:(None if x==self.zero else self.phases[self.power(x,(self.Q-1)//6)]) for x in self.xs}
 def embed(self,z):
  if self.inert:return z[0]%self.p,z[1]%self.p
  return (z[0]+z[1]*self.root)%self.p,0
 def add(self,x,y):return self.embed(add(x,y))
 def mul(self,x,y):return self.embed(mul(x,y))
 def power(self,x,n):
  y=self.one
  while n:
   if n%2:y=self.mul(y,x)
   x=self.mul(x,x);n//=2
  return y
 def complement(self,x):return self.add(self.one,neg(x))
 def J(self,orientation=1):
  return total(PH[(orientation*(self.chi[x]+2*self.chi[self.complement(x)]))%6] for x in self.xs if self.chi[x] is not None and self.chi[self.complement(x)] is not None)
 def pairing(self,x,beta):
  # Tr((c+dω)/(δβ))=(-b*c+a*d)/Nβ. The prime-field exponent is multiplied by p.
  a,b=beta;c,d=x;div=self.Q//self.p;num=-b*c+a*d
  assert num%div==0
  return (num//div)%self.p
 def tau(self,j,beta=None,k=(1,0),orientation=1):
  beta=self.beta if beta is None else beta;h=[(0,0) for _ in range(self.p)]
  for x in self.xs:
   e=self.chi[x]
   if e is None:continue
   v=PH[(orientation*j*e)%6];idx=self.pairing(self.mul(k,x),beta)
   h[idx]=add(h[idx],v)
  return tuple(h)
 def prod_hist(self,a,b):
  h=[(0,0) for _ in range(self.p)]
  for i,x in enumerate(a):
   for j,y in enumerate(b):h[(i+j)%self.p]=add(h[(i+j)%self.p],mul(x,y))
  return tuple(h)
 def scale_hist(self,z,a):return tuple(mul(z,x) for x in a)
 def equal_hist(self,a,b):
  # For prime p !=3, Φp remains irreducible over Q(ω); a degree<p cyclic difference vanishes iff all coefficients agree.
  dif=[add(x,neg(y)) for x,y in zip(a,b)];return len(set(dif))==1

def main():
 start=time.monotonic();assertions=0;fields=[Field(g) for g in [(1,3),(-2,-3),(1,6),(-5,-6),(-5,0),(-11,0)]];reports=[]
 for F in fields:
  j=F.J();unit=quotient(j,F.beta);assert norm(j)==F.Q and unit in PH;assertions+=2
  assert F.J(-1)==conj(j);assertions+=1
  red=F.embed(j);assert red==F.zero;assertions+=1
  s=(F.Q-1)//6
  polynomial_sum=F.zero
  for x in F.xs:polynomial_sum=F.add(polynomial_sum,F.mul(F.power(x,s),F.power(F.complement(x),2*s)))
  assert polynomial_sum==F.zero and 3*s<F.Q-1;assertions+=1
  gen_cases=[]
  for u in PH:
   beta=mul(u,F.beta);ue=F.chi[F.embed(u)];assert ue is not None
   for orientation in (1,-1):
    tj={k:F.tau(k,beta,orientation=orientation) for k in (1,2,3)}
    assert F.equal_hist(F.prod_hist(tj[1],tj[2]),F.scale_hist(F.J(orientation),tj[3]));assertions+=1
    for k in (1,2,3):
     assert F.equal_hist(tj[k],F.scale_hist(PH[(orientation*k*ue)%6],F.tau(k,orientation=orientation)));assertions+=1
    # Fresh mixed two-pivot frequencies, including a forbidden zero frequency.
    for k1,k2 in [(F.embed((2,0)),F.embed((1,1))),(F.zero,F.one),(F.one,F.zero)]:
     lhs=F.prod_hist(F.tau(1,beta,k1,orientation),F.tau(2,beta,k2,orientation))
     if k1==F.zero or k2==F.zero:rhs=tuple((0,0) for _ in range(F.p))
     else:
      e=-orientation*(F.chi[k1]+2*F.chi[k2]);rhs=F.scale_hist(mul(PH[e%6],F.J(orientation)),tj[3])
     assert F.equal_hist(lhs,rhs);assertions+=1
   gen_cases.append({'generator':beta,'unit':u,'character_unit_exponent':ue})
  wrong=add(j,(2,0));assert wrong!=j and norm(wrong)!=F.Q;assertions+=1
  reports.append({'primary_generator':F.beta,'field_order':F.Q,'characteristic':F.p,'inert':F.inert,'omega_residue':F.root,'jacobi_chi_chi2':j,'quotient_by_generator':unit,'norm':norm(j),'reduction_mod_original_prime':red,'conjugate_value':conj(j),'wrong_endpoint_restoration':wrong,'wrong_endpoint_norm':norm(wrong),'generator_cases':gen_cases})
 assert fields[1].J()==conj(fields[0].J());assert fields[3].J()==conj(fields[2].J());assertions+=2
 composites=[]
 for ids in [(0,1),(2,3),(2,4),(0,2,4)]:
  fs=[fields[i] for i in ids];Q=1;beta=(1,0)
  for F in fs:Q*=F.Q;beta=mul(beta,F.beta)
  orientations=[]
  for signs in product((1,-1),repeat=len(fs)):
   lhs=(0,0);active=0
   for xs in product(*(F.xs for F in fs)):
    exponent=0;allowed=True
    for F,x,eps in zip(fs,xs,signs):
     cx=F.chi[x];cy=F.chi[F.complement(x)]
     if cx is None or cy is None:allowed=False;break
     exponent+=eps*(cx+2*cy)
    if allowed:lhs=add(lhs,PH[exponent%6]);active+=1
   jr=(1,0);jt=(1,0);r=(1,0);t=(1,0)
   for F,eps in zip(fs,signs):
    if eps==1:jr=mul(jr,F.J());r=mul(r,F.beta)
    else:jt=mul(jt,F.J());t=mul(t,F.beta)
   expected=mul(jr,conj(jt));assert lhs==expected and norm(lhs)==Q;assertions+=2
   assert quotient(jr,r) in PH and quotient(jt,t) in PH;assertions+=2
   assert active==__import__('math').prod(F.Q-2 for F in fs);assertions+=1
   orientations.append({'signs':signs,'r_generator':r,'t_generator':t,'J_q_direct':lhs,'j_r':jr,'j_t':jt,'active_summands':active,'raw_zero_summands':Q-active})
  composites.append({'factor_generators':[F.beta for F in fs],'q_generator':beta,'Q':Q,'rational_norm_squarefree':all(Q%(p*p) for p in range(2,isqrt(Q)+1)),'orientations':orientations})
 srcs=['papers/joint-gauss-core.tex','papers/joint-gauss-details.tex','papers/theta-jacobi-core.tex','research/reciprocity-period.md','scripts/check_reciprocity_period.py','planning/joint-dual-20261105/research/HANDOFF-v1.md']
 pins={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in srcs}
 report={'passed':True,'scope':'Fresh exact χ6/χ6² Jacobi ideal/orientation/CRT and two-pivot full-period controls only; no signed estimate, new phase theorem, Lean or GRH conclusion. Old991 and reciprocity-period scripts were not imported or run.','assertions':assertions,'local_fields':reports,'composites':composites,'sources_sha256':pins,'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'elapsed_seconds':round(time.monotonic()-start,3),'exact_representation':'Z[ω] integer pairs; Gauss polynomials in Z[ω][ζ_p] with exact Φp relation; no complex floating arithmetic or simulation.','no_randomness':True}
 output=OUT/'exact-jacobi-controls-v1.json';output.parent.mkdir(parents=True,exist_ok=True)
 with output.open('x') as f:json.dump(report,f,indent=2);f.write('\n')
 print(json.dumps({'passed':True,'assertions':assertions,'local_fields':len(fields),'composite_cases':len(composites),'output':str(output),'sha256':hashlib.sha256(output.read_bytes()).hexdigest(),'local_j':[(x['primary_generator'],x['jacobi_chi_chi2']) for x in reports],'elapsed_seconds':report['elapsed_seconds']},indent=2))
if __name__=='__main__':main()
