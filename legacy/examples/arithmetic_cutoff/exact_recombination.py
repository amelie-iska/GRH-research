#!/usr/bin/env python3
"""Exact finite Eisenstein-ideal diagnostics for the original weighted cutoff.

This does not prove the infinite large sieve, a Hecke theorem, or GRH.
Finite prime support is stated in every output. No binary float arithmetic.
"""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
from fractions import Fraction as Q
from itertools import product
import argparse,json,hashlib
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'scripts'))
from check_mobius_split import universe,elements,quotient,scalar_symbol
from check_reciprocity_period import prime_symbol,power,emul,norm
ZERO=(Q(0),Q(0));ONE=(Q(1),Q(0))
PH=[(1,0),(1,1),(0,1),(-1,0),(-1,-1),(0,-1)]
def add(a,b):return(a[0]+b[0],a[1]+b[1])
def sub(a,b):return(a[0]-b[0],a[1]-b[1])
def mul(a,b):return emul(a,b)
def inv(a):
 n=norm(a)
 if not n:raise ZeroDivisionError('Zero algebraic denominator')
 return((a[0]-a[1])/n,-a[1]/n)
def phase(e):return ZERO if e is None else tuple(map(Q,PH[e%6]))
def total(xs):
 z=ZERO
 for x in xs:z=add(z,x)
 return z
def subsets(mask):
 x=mask
 while True:
  yield x
  if not x:return
  x=(x-1)&mask

def coefficient_tables(norms,U):
 if type(U)is not int or U<1:raise ValueError('Positive integer cutoff required')
 beta=[];coeff=[]
 for mask,N in enumerate(norms):
  count=sum(norms[a]<=U and norms[mask^a]<=U for a in subsets(mask))
  beta.append((-1)**mask.bit_count()*count)
  coeff.append(sum(beta[a] for a in subsets(mask)))
 return beta,coeff

def run(output):
 if output.exists():raise FileExistsError('Preserve existing experiments')
 _,_,_,all_primes=universe(128)
 primes=[p for p in all_primes if norm(p) in [7,13,19,25]]
 assert len(primes)==7
 norms=[];generators=[];factors=[]
 for mask in range(1<<len(primes)):
  g=(1,0);fs=[]
  for j,p in enumerate(primes):
   if mask>>j&1:g=emul(g,p);fs.append((p,1))
  generators.append(g);norms.append(norm(g));factors.append(tuple(fs))
 full=(1<<len(primes))-1;cutoffs=[1,7,20,50,500,norms[-1]]
 tables={U:coefficient_tables(norms,U) for U in cutoffs}
 coefficient_checks=0
 for U,(beta,coeff) in tables.items():
  for m in range(full+1):
   assert abs(beta[m])<=2**m.bit_count()
   assert abs(coeff[m])<=3**m.bit_count()
   if norms[m]<=U:assert coeff[m]==(-1)**m.bit_count()
   coefficient_checks+=3
 beta,coeff=tables[norms[-1]]
 assert all(beta[m]==(-2)**m.bit_count() and coeff[m]==(-1)**m.bit_count() for m in range(full+1))
 rows=elements(8)+[power(primes[0],3),power(primes[0],6),emul(power(primes[0],6),primes[-1])]
 cases=original_zero_values=naive_square_failures=0;max_abs_coeff=0
 for u,twist,sigma in product(rows,[False,True],[1,2]):
  deleted={j for j,p in enumerate(primes) if quotient(u,p) is not None}
  zp=[]
  for j,p in enumerate(primes):
   e=prime_symbol(p,u)
   if e is None:original_zero_values+=1
   elif twist:e=(e+prime_symbol(p,(2,0)))%6
   zp.append(mul(phase(e),(Q(1,norm(p)**sigma),Q(0))))
  monomials=[ONE];tmonomials=[ONE]
  for m in range(1,full+1):
   low=m&-m;j=low.bit_length()-1
   monomials.append(mul(monomials[m^low],zp[j]))
   tmonomials.append(mul(tmonomials[m^low],mul(zp[j],inv(add(ONE,zp[j])))))
  F=[]
  for d in range(full+1):
   f=ONE
   for j,z in enumerate(zp):
    if j not in deleted and not d>>j&1:f=mul(f,add(ONE,z))
   F.append(f)
  for U,(beta,coeff) in tables.items():
   direct=total(mul((Q(beta[d]),Q(0)),mul(monomials[d],F[d])) for d in range(full+1))
   recombined=total(mul((Q(coeff[m]),Q(0)),monomials[m]) for m in range(full+1))
   B=total(mul((Q(beta[d]),Q(0)),tmonomials[d]) for d in range(full+1))
   assert direct==recombined==mul(F[0],B)
   # Original zeros remain zeros even when sixth powers drop from conductor.
   assert all(monomials[d]==ZERO for d in range(full+1) if any(d>>j&1 for j in deleted))
   M=total(mul((Q((-1)**a.bit_count()),Q(0)),tmonomials[a]) for a in range(full+1) if norms[a]<=U)
   naive_square_failures+=mul(M,M)!=B
   max_abs_coeff=max(max_abs_coeff,max(map(abs,coeff)));cases+=1
  reciprocal=ONE
  for j,z in enumerate(zp):
   if j not in deleted:reciprocal=mul(reciprocal,sub(ONE,z))
  assert reciprocal==total(mul((Q((-1)**m.bit_count()),Q(0)),monomials[m]) for m in range(full+1))
 assert naive_square_failures>0 and original_zero_values>0
 # Explicit negative control: erasing the original sentinel at pi^6 is wrong.
 u6=power(primes[0],6);raw=prime_symbol(primes[0],u6);assert raw is None
 principal_replacement=(Q(1,norm(primes[0])),Q(0));assert sub(ONE,principal_replacement)!=ONE
 output.mkdir(parents=True)
 source_files=[Path(__file__),ROOT/'scripts/check_mobius_split.py',ROOT/'scripts/check_reciprocity_period.py']
 hashes={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in source_files}
 report=dict(passed=True,arithmetic='exact Fraction and Eisenstein elements; no seed',prime_ideals=[dict(generator=list(p),norm=norm(p)) for p in primes],finite_squarefree_support=128,rows=len(rows),cutoffs=cutoffs,coefficient_checks=coefficient_checks,weighted_identity_cases=cases,original_zero_values=original_zero_values,naive_non_coprime_square_counterexamples=naive_square_failures,max_abs_A_U=max_abs_coeff,sixth_power_sentinel_negative_control=True,source_sha256=hashes,scope='Finite actual Eisenstein-prime-ideal and raw sextic-symbol identities. Not infinite cutoff convergence, the large-sieve moment theorem, analytic Lean, positivity or GRH.')
 (output/'exact-recombination.json').write_text(json.dumps(report,indent=2)+'\n')
 print(json.dumps(report,indent=2))
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--output',type=Path,required=True);a=p.parse_args();run(a.output)
