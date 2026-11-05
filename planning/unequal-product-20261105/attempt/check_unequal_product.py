#!/usr/bin/env python3
"""Exact local completion and original masked fourth/mixed moment diagnostics.

Standard library only. No author/project helper imports. Finite algebra is
checked exactly in Q(omega) and Q(omega,zeta_p); no analytic bound is tested.
"""
import argparse, hashlib, json, sys
from collections import Counter
from fractions import Fraction as F
from itertools import product
from math import isqrt
from pathlib import Path
sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parents[3]
ZERO=(0,0); ONE=(1,0)
def add(x,y):return x[0]+y[0],x[1]+y[1]
def neg(x):return -x[0],-x[1]
def mul(x,y):
 a,b=x;c,d=y
 return a*c-b*d,a*d+b*c-b*d
def conj(x):return x[0]-x[1],-x[1]
def norm(x):return x[0]*x[0]-x[0]*x[1]+x[1]*x[1]
def scale(c,x):return c*x[0],c*x[1]
def power(x,k):
 y=ONE
 while k:
  if k&1:y=mul(y,x)
  x=mul(x,x);k//=2
 return y
UNITS=tuple(power((1,1),j) for j in range(6))
def total(xs):
 z=ZERO
 for x in xs:z=add(z,x)
 return z
def quotient(x,y):
 n=norm(y);a,b=mul(x,conj(y))
 return (a//n,b//n) if a%n==b%n==0 else None
def prime(n):return n>1 and all(n%d for d in range(2,isqrt(n)+1))
def elements(B):
 k=2*isqrt(B)+2
 return [(a,b) for a in range(-k,k+1) for b in range(-k,k+1) if 0<norm((a,b))<=B]
def universe(B):
 gs=sorted([g for g in elements(B) if g[0]%3==1 and g[1]%3==0 and norm(g)%2 and norm(g)%3],key=lambda g:(norm(g),g))
 ps=[g for g in gs if prime(norm(g)) or (g[1]==0 and prime(abs(g[0])) and abs(g[0])%3==2)]
 fs={}
 for g in gs:
  z=g;ff=[]
  for p in ps:
   e=0
   while (v:=quotient(z,p)) is not None:z=v;e+=1
   if e:ff.append((p,e))
  assert z==ONE
  fs[g]=tuple(ff)
 return gs,ps,fs

class Residue:
 def __init__(self,pi):
  self.pi=pi;self.q=norm(pi)
  if pi[1]:
   assert prime(self.q)
   self.p=self.q;self.w=(-pi[0]*pow(pi[1],-1,self.p))%self.p
   self.values=tuple(range(self.p));self.zero=0;self.one=1
  else:
   self.p=abs(pi[0]);assert prime(self.p) and self.p%3==2
   self.w=None;self.values=tuple(product(range(self.p),repeat=2));self.zero=(0,0);self.one=(1,0)
  zeta=self.reduce((1,1))
  self.roots=tuple(self.pow(zeta,j) for j in range(6))
  assert len(set(self.roots))==6
 def reduce(self,z):
  if self.w is not None:return (z[0]+self.w*z[1])%self.p
  return tuple(v%self.p for v in z)
 def mult(self,x,y):
  return (x*y)%self.p if self.w is not None else tuple(v%self.p for v in mul(x,y))
 def pow(self,x,k):
  y=self.one
  while k:
   if k&1:y=self.mult(y,x)
   x=self.mult(x,x);k//=2
  return y
 def trace(self,x):
  return x%self.p if self.w is not None else (2*x[0]-x[1])%self.p
 def exponent(self,x):
  return None if x==self.zero else self.roots.index(self.pow(x,(self.q-1)//6))
 def character(self,x,k,deleted=True):
  if x==self.zero:return ZERO if deleted else ONE
  return UNITS[(self.exponent(x)*k)%6]

FIELDS={}
def field(p):
 if p not in FIELDS:FIELDS[p]=Residue(p)
 return FIELDS[p]
def local(p,u):return field(p).exponent(field(p).reduce(u))
def symbol(fs,u):
 z=ONE
 for p,k in fs:
  e=local(p,u)
  if e is None:return ZERO
  z=mul(z,UNITS[(k*e)%6])
 return z
def moebius(fs):return 0 if any(e>1 for p,e in fs) else (-1)**len(fs)
def factorpairs(fs,U):
 assert all(e==1 for p,e in fs)
 out=[]
 for bits in product((0,1),repeat=len(fs)):
  a=b=ONE
  for (p,e),bit in zip(fs,bits):
   if bit:a=mul(a,p)
   else:b=mul(b,p)
  if norm(a)>U and norm(b)>U:out.append((a,b))
 return out

def cyclo_equal(a,b):
 diff=[add(x,neg(y)) for x,y in zip(a,b)]
 return all(x==diff[-1] for x in diff)
def gauss_coeff(Fq,k,t):
 out=[ZERO]*Fq.p
 for z in Fq.values:
  if z==Fq.zero:continue
  i=Fq.trace(Fq.mult(t,z))
  out[i]=add(out[i],Fq.character(z,k))
 return out
def cyclo_norm(g):
 p=len(g);out=[ZERO]*p
 for i,x in enumerate(g):
  for j,y in enumerate(g):out[(i-j)%p]=add(out[(i-j)%p],mul(x,conj(y)))
 return out
def local_checks():
 fields=[(1,3),(4,3),(-2,3),(-5,0),(-11,0)]
 reps=[];n_assert=0;pattern_n=0
 for pi in fields:
  f=field(pi);n=f.q
  conductors={}
  for e in (-2,-1,0,1,2):
   for j in range(1,7):
    k=e*j%6
    vals={f.character(z,k) for z in f.values if z!=f.zero}
    assert (len(vals)>1)==(k!=0)
    order=6//__import__('math').gcd(k,6)
    assert len(vals)==order
    assert f.character(f.zero,k)==ZERO
    conductors[f"{e}:{j}"]={"local_order":order,"tame_conductor_exponent":int(k!=0),"zero_retained":True}
    n_assert+=3
  for bits in product((0,1),repeat=4):
   e=bits[0]+bits[1]-bits[2]-bits[3]
   internal=not(bits[0] and bits[1]) and not(bits[2] and bits[3])
   if internal:assert e in (-1,0,1)
   for j in range(1,7):
    for z in f.values:
     zz=f.pow(z,j)
     lhs=ONE
     for bit,sgn in zip(bits,(1,1,-1,-1)):
      if bit:
       v=f.character(zz,1)
       lhs=mul(lhs,v if sgn==1 else conj(v))
     rhs=f.character(z,e*j) if any(bits) else ONE
     assert lhs==rhs
     n_assert+=1
   pattern_n+=1
  gauss_n=0
  for k in range(6):
   g1=gauss_coeff(f,k,f.one)
   for t in f.values:
    g=gauss_coeff(f,k,t)
    target=[ZERO]*f.p
    if t==f.zero:
     target[0]=(n-1,0) if k==0 else ZERO
     assert cyclo_equal(g,target);n_assert+=1
    elif k==0:
     target[0]=(-1,0)
     assert cyclo_equal(g,target);n_assert+=1
    else:
     target[0]=(n,0)
     assert cyclo_equal(cyclo_norm(g),target)
     factor=conj(f.character(t,k))
     assert cyclo_equal(g,[mul(factor,v) for v in g1])
     n_assert+=2
    gauss_n+=1
  reps.append({"prime_generator":pi,"residue_norm":n,"character_conductor_table":conductors,"complete_sums_checked":gauss_n})
 return {"fields":reps,"local_membership_patterns":pattern_n,"exact_assertions":n_assert}

def reduced_character(parts,signs,u,j=1):
 L=set();es=Counter()
 for fs,s in zip(parts,signs):
  for p,k in fs:L.add(p);es[p]+=s*k
 out=ONE
 for p in L:
  e=local(p,u)
  if e is None:return ZERO
  out=mul(out,UNITS[(j*es[p]*e)%6])
 return out

def moment_case(D,U,gs,ps,fs,nu_num):
 cols=[g for g in gs if D<=norm(g)<=2*D and moebius(fs[g])]
 pairs=[(a,b,m) for m in cols for a,b in factorpairs(fs[m],U)]
 basis=[p for p in ps if 7<=norm(p)<14]
 assert len(basis)==4
 balanced=[mul(e,mul(a,power(b,2))) for a,b in product(basis,repeat=2) if a!=b for e in UNITS]
 cubic=[mul(e,power(a,3)) for a in basis for e in UNITS]
 rows=balanced+cubic
 assert len(rows)==96
 weights={}
 for m in cols:
  n=norm(m);t=F((n-D)*(2*D-n),D*D)
  weights[n]=(t,t*F(n-D,D))
 def coeff(m):return mul((moebius(fs[m]),0),mul(symbol(fs[m],nu_num),weights[norm(m)]))
 cf={m:coeff(m) for m in cols}
 counts=Counter();local_ledgers=Counter();mixed_ledgers=Counter()
 for a,b,m in pairs:
  assert set(p for p,e in fs[a]).isdisjoint(p for p,e in fs[b])
 for a,b,m in pairs:
  for c,d,n in pairs:
   L=set(p for g in (a,b,c,d) for p,e in fs[g])
   es={p:sum(s*dict(fs[g]).get(p,0) for g,s in zip((a,b,c,d),(1,1,-1,-1))) for p in L}
   assert set(es.values())<=set((-1,0,1))
   q={p for p,e in es.items() if e}
   z=L-q
   assert q==set(p for p,e in fs[m])^set(p for p,e in fs[n])
   assert z==set(p for p,e in fs[m])&set(p for p,e in fs[n])
   local_ledgers["equal_product" if m==n else "unequal_product"]+=1
   if z:local_ledgers["union_has_canceled_prime"]+=1
 for a,b,m in pairs:
  for n in cols:
   L=set(p for g in (a,b,n) for p,e in fs[g])
   es={p:sum(s*dict(fs[g]).get(p,0) for g,s in zip((a,b,n),(1,1,-1))) for p in L}
   assert set(es.values())<=set((-1,0,1))
   mixed_ledgers["equal_product" if m==n else "unequal_product"]+=1
   if any(e==0 for e in es.values()):mixed_ledgers["union_has_canceled_prime"]+=1
 energies=[ZERO,ZERO,ZERO]
 for u in rows:
  raw={m:symbol(fs[m],u) for m in cols}
  cu=total(mul(cf[m],raw[m]) for a,b,m in pairs)
  mu=total(mul(cf[m],raw[m]) for m in cols)
  ec=mul(cu,conj(cu));em=mul(mu,conj(mu));mix=mul(cu,conj(mu))
  energies=[add(v,z) for v,z in zip(energies,(ec,em,mix))]
  e_exp=m_exp=ZERO
  for a,b,m in pairs:
   for c,d,n in pairs:
    actual=mul(mul(symbol(fs[a],u),symbol(fs[b],u)),conj(mul(symbol(fs[c],u),symbol(fs[d],u))))
    red=reduced_character([fs[a],fs[b],fs[c],fs[d]],[1,1,-1,-1],u)
    assert actual==red
    if actual==ZERO:counts["raw_zero_four_column"]+=1
    e_exp=add(e_exp,mul(mul(cf[m],conj(cf[n])),red))
    counts["four_column_values"]+=1
   for n in cols:
    actual=mul(mul(symbol(fs[a],u),symbol(fs[b],u)),conj(raw[n]))
    red=reduced_character([fs[a],fs[b],fs[n]],[1,1,-1],u)
    assert actual==red
    if actual==ZERO:counts["raw_zero_mixed"]+=1
    m_exp=add(m_exp,mul(mul(cf[m],conj(cf[n])),red))
    counts["mixed_values"]+=1
  assert e_exp==ec and m_exp==mix
 # Independent exact finite divisor deletion, including rows divisible by common primes.
 for m,n in product(cols,repeat=2):
  h={p for p,e in fs[m]}&{p for p,e in fs[n]}
  L={p for p,e in fs[m]}|{p for p,e in fs[n]}
  es={p:dict(fs[m]).get(p,0)-dict(fs[n]).get(p,0) for p in L}
  for u in rows:
   primitive=ONE
   for p,e in es.items():
    if not e:continue
    v=local(p,u)
    primitive=ZERO if v is None else mul(primitive,UNITS[(v*e)%6])
   delete=0
   for bits in product((0,1),repeat=len(h)):
    chosen=[p for p,b in zip(sorted(h),bits) if b]
    if all(quotient(u,p) is not None for p in chosen):delete+=(-1)**len(chosen)
   assert mul(rawchar:=mul(symbol(fs[m],u),conj(symbol(fs[n],u))),ONE)==scale(delete,primitive)
   counts["mobius_delete_values"]+=1
 return {"D":D,"U":U,"nu_numerator":nu_num,"columns":len(cols),"ordered_long_pairs":len(pairs),"rows":len(rows),"quadruple_ledgers":dict(local_ledgers),"mixed_ledgers":dict(mixed_ledgers),"values":dict(counts),"normalized_energy_C":[str(v/D) for v in energies[0]],"normalized_energy_mu":[str(v/D) for v in energies[1]],"normalized_mixed":[str(v/D) for v in energies[2]]}

def exponent_checks():
 # Exact full saturation face at H=D^(3/4): a1=a2=t,a3=1/4-t.
 rows=[]
 for i in range(13):
  t=F(i,48);s=F(1,4)-t;R=2*t+s
  assert t>=0 and s>=0 and 3*t+3*s==F(3,4)
  assert R-t==F(1,4)
  trivial=1+R;middle=F(5,4)
  assert trivial>=middle
  # Every active j<=3 norm scale is <= D^(1/4), versus sqrt(NQ)~D.
  assert max(t,s)<=F(1,4)
  rows.append({"a1":str(t),"a2":str(t),"a3":str(s),"normalized_absolute_quadruple_bound_exponent":str(trivial),"inherited_D_R_over_M_exponent":str(middle)})
 return rows

def main():
 p=argparse.ArgumentParser();p.add_argument("--output",type=Path,required=True);args=p.parse_args()
 if args.output.exists():raise FileExistsError("Preserve prior diagnostics")
 local_report=local_checks()
 gs,ps,fs=universe(800)
 cases=[moment_case(128,7,gs,ps,fs,ONE),moment_case(128,7,gs,ps,fs,(2,0))]
 report={"passed":True,"local_complete_sums":local_report,"original_fourth_and_mixed_cases":cases,"full_A3_face":exponent_checks(),"scope":"Exact finite character/conductor/union-deletion and moment expansion identities; no asymptotic saving, analytic large-sieve theorem, Lean, or GRH claim.","source_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
 args.output.mkdir(parents=True)
 with (args.output/"exact-unequal-product.json").open("x") as f:json.dump(report,f,indent=2);f.write("\n")
 print(json.dumps({"passed":True,"local_assertions":local_report["exact_assertions"],"moment_cases":len(cases),"four_column_values":sum(c["values"]["four_column_values"] for c in cases),"mixed_values":sum(c["values"]["mixed_values"] for c in cases),"delete_values":sum(c["values"]["mobius_delete_values"] for c in cases),"raw_zeros":sum(c["values"]["raw_zero_four_column"]+c["values"]["raw_zero_mixed"] for c in cases),"face_points":len(report["full_A3_face"])}))
if __name__=="__main__":main()
