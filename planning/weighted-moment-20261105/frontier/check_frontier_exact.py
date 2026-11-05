#!/usr/bin/env python3
"""Deterministic exact algebra diagnostics; not an analytic moment proof."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
from fractions import Fraction as F
from itertools import product
import argparse,json,hashlib
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'scripts'))
from check_mobius_split import universe,quotient
from check_reciprocity_period import emul,norm,prime,prime_symbol,power,symbol
PH=((1,0),(1,1),(0,1),(-1,0),(-1,-1),(0,-1))
ZERO=(F(0),F(0))
def add(x,y):return (x[0]+y[0],x[1]+y[1])
def sub(x,y):return (x[0]-y[0],x[1]-y[1])
def scale(c,x):return (c*x[0],c*x[1])
def conjugate(x):return (x[0]-x[1],-x[1])
def real(x):return x[0]-x[1]/2
def inner(x,y):return emul(x,conjugate(y))
def phase(e):return ZERO if e is None else tuple(map(F,PH[e%6]))
def total(xs):
 r=ZERO
 for x in xs:r=add(r,x)
 return r
def subsets(m):
 q=m
 while True:
  yield q
  if not q:return
  q=(q-1)&m

def main(output):
 if output.exists():raise FileExistsError('Preserve prior diagnostic output')
 _,_,_,primegens=universe(128)
 primes=[p for p in primegens if norm(p) in (7,13,19,25)]
 assert len(primes)==7
 ns=[];factors=[]
 for mask in range(128):
  fs=[(p,1) for i,p in enumerate(primes) if mask>>i&1]
  factors.append(fs)
  n=1
  for p,_ in fs:n*=norm(p)
  ns.append(n)
 cutoffs=(1,2,7,13,20,50,500,1000)
 tables={};coefficient_cases=active_cases=0
 for U in cutoffs:
  A=[];C=[]
  for mask in range(128):
   low=long=0
   for a in subsets(mask):
    for b in subsets(mask^a):
     sg=(-1)**(a.bit_count()+b.bit_count())
     if ns[a]<=U and ns[b]<=U:low+=sg
     if ns[a]>U and ns[b]>U:long+=sg
   mu=(-1)**mask.bit_count()
   assert low==mu-2*mu*(ns[mask]>U)+long
   if ns[mask]>U:assert low==long-mu;active_cases+=1
   A.append(low);C.append(long);coefficient_cases+=1
  tables[U]=(A,C)
 # Exact literal nonprincipal rows: distinct prime ideals at exponents 1 and 2.
 base=primes[:4]
 assert set(map(norm,base))=={7,13}
 rows=[]
 for i,j in product(range(4),repeat=2):
  if i==j:continue
  z=emul(base[i],power(base[j],2))
  assert quotient(z,base[i]) is not None and quotient(z,base[j]) is not None
  for unit in PH:rows.append(emul(unit,z))
 assert len(rows)==len(set(rows))==72
 sixth=power(primes[0],6)
 raw_table=[[phase(symbol(fs,u)) for fs in factors] for u in rows+[sixth]]
 # Product conductor drops at common primes; union zero mask does not drop.
 gram_products=shared_zero_cases=0
 for ri,u in enumerate(rows+[sixth]):
  for m,n in product(range(32),repeat=2):
   raw=inner(raw_table[ri][m],raw_table[ri][n])
   union=m|n
   if any(union>>i&1 and prime_symbol(p,u) is None for i,p in enumerate(primes)):
    assert raw==ZERO;shared_zero_cases+=1
   else:
    e=0
    for i,p in enumerate(primes):
     z=prime_symbol(p,u)
     if m>>i&1 and not n>>i&1:e+=z
     if n>>i&1 and not m>>i&1:e-=z
    assert raw==phase(e)
   gram_products+=1
 # Explicit sixth-power sentinel: primitive oscillation may cancel; raw zero stays.
 single=1
 assert prime_symbol(primes[0],sixth) is None
 assert raw_table[-1][single]==ZERO
 assert inner(raw_table[-1][single],raw_table[-1][single])==ZERO
 # Actual long-long-minus-Mobius covariance on all 72 guaranteed nonprincipal rows.
 cov_cases=0;nonzero_LL=0;masked_entries=0
 parameters=[]
 for D,U in ((64,7),(128,7),(512,7),(1024,20),(4096,50)):
  assert U*U<=D
  columns=[m for m in range(128) if D<ns[m]<2*D]
  assert columns and all(ns[m]>U for m in columns)
  A,C=tables[U]
  weights={m:F((ns[m]-D)*(2*D-ns[m]),D*D)**2 for m in columns}
  nonzero_LL+=sum(C[m]!=0 for m in columns)
  for twist in ((1,0),(2,0)):
   nu={m:phase(symbol(factors[m],twist)) for m in columns}
   assert all(nu[m]!=ZERO for m in columns)
   energyA=energyC=energyM=F(0);cov=ZERO
   for ri,u in enumerate(rows):
    terms={m:scale(weights[m],emul(nu[m],raw_table[ri][m])) for m in columns}
    masked_entries+=sum(raw_table[ri][m]==ZERO for m in columns)
    a=total(scale(A[m],terms[m]) for m in columns)
    c=total(scale(C[m],terms[m]) for m in columns)
    mu=total(scale((-1)**m.bit_count(),terms[m]) for m in columns)
    assert a==sub(c,mu)
    assert norm(a)==norm(c)+norm(mu)-2*real(inner(c,mu))
    energyA+=norm(a)/D;energyC+=norm(c)/D;energyM+=norm(mu)/D
    cov=add(cov,scale(F(1,D),inner(c,mu)));cov_cases+=1
   assert energyA==energyC+energyM-2*real(cov)
   # Independent expansion of the ACTUAL signed Gram quadratic form.
   expanded=ZERO
   for m,n in product(columns,repeat=2):
    G=total(inner(raw_table[ri][m],raw_table[ri][n]) for ri in range(len(rows)))
    coeff=scale(F(A[m]*A[n],D)*weights[m]*weights[n],inner(nu[m],nu[n]))
    expanded=add(expanded,emul(coeff,G))
   assert expanded==(energyA,F(0))
   parameters.append(dict(D=D,U=U,columns=len(columns),nu_numerator=list(twist)))
 assert nonzero_LL and masked_entries
 # Actual prime columns above every row norm are never deleted by the gcd mask.
 u0=emul(base[0],power(base[2],2));H=norm(u0)
 prime_columns=[]
 for a in range(1,75):
  for b in range(1,a):
   p=(a,b);q=norm(p)
   if 2048<=q<=4096 and prime(q):
    if q not in {norm(z) for z in prime_columns}:prime_columns.append(p)
    if len(prime_columns)==6:break
  if len(prime_columns)==6:break
 assert len(prime_columns)==6 and all(norm(p)>H for p in prime_columns)
 prime_values=[phase(prime_symbol(p,u0)) for p in prime_columns]
 assert all(x!=ZERO for x in prime_values)
 # U=20: the only admissible placements for a prime above 2048 are a=b=1.
 assert all(norm(p)>20 for p in prime_columns)
 aligned=total(inner(x,x) for x in prime_values)
 assert aligned==(F(6),F(0)) and norm(aligned)==36
 report=dict(passed=True,seed='none; exhaustive deterministic exact arithmetic',
  prime_ideal_generators=[list(x) for x in primes],prime_ideal_norms=list(map(norm,primes)),
  finite_squarefree_support=128,coefficient_LL_cases=coefficient_cases,
  active_A_equals_C_minus_mu_cases=active_cases,nonprincipal_literal_rows=72,
  exact_raw_union_mask_product_cases=gram_products,shared_zero_cases=shared_zero_cases,
  covariance_row_cases=cov_cases,independent_Gram_expansions=len(parameters),
  nonzero_long_long_active_columns=nonzero_LL,retained_masked_covariance_entries=masked_entries,
  parameters=parameters,prime_mask_example=dict(row=list(u0),row_norm=H,
   columns=[dict(generator=list(p),norm=norm(p)) for p in prime_columns],
   all_masks_equal_one=True,actual_A_U_prime=1,U=20,
   aligned_arbitrary_coefficient_norm_squared=6,aligned_row_amplitude_squared=36),
  sixth_power_shared_prime_sentinel_preserved=True,
  source_sha256={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest()
   for p in [Path(__file__),ROOT/'scripts/check_mobius_split.py',ROOT/'scripts/check_reciprocity_period.py']},
  scope='Exact finite disjoint-convolution, raw symbol masks, Gram and LL-minus-Mobius covariance identities. Rational finite annular profile. No analytic BT_sigma bound, energy lower asymptotic, new Lean theorem, determinant positivity or GRH claim.')
 output.parent.mkdir(parents=True,exist_ok=True)
 with output.open('x') as f:json.dump(report,f,indent=2);f.write('\n')
 print(json.dumps(report,indent=2))

if __name__=='__main__':
 parser=argparse.ArgumentParser();parser.add_argument('--output',type=Path,required=True)
 main(parser.parse_args().output)
