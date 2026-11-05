"""Fresh exact diagnostics for the new gauged coefficient identities only.
Does not invoke old accepted cutoffs/Gauss/period tables or claim analytic saving.
"""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
import json,hashlib
R=Path(__file__).resolve().parents[3]
def clean(p):return {k:v for k,v in p.items() if v}
def add(*ps):
 z={}
 for p in ps:
  for k,v in p.items():z[k]=z.get(k,0)+v
 return clean(z)
def mul(p,q):
 z={}
 for k,v in p.items():
  for l,w in q.items():
   t=tuple(a+b for a,b in zip(k,l));z[t]=z.get(t,0)+v*w
 return clean(z)
N=3;one={(0,)*N:1};x={(1,0,0):1};a={(0,1,0):1};b={(0,0,1):1}
neg=lambda p:{k:-v for k,v in p.items()}
factor=add(one,mul(x,add(a,b,neg(one))))
num=mul(mul(factor,add(one,neg(mul(x,a)))),add(one,neg(mul(x,b))))
rhs=add(one,neg(x),mul(mul(x,x),add(a,b,neg(mul(a,a)),neg(mul(b,b)),neg(mul(a,b)))),mul(mul(mul(x,x),x),mul(mul(a,b),add(a,b,neg(one)))))
assert num==rhs
checks=1;cases=[]
prime_norms=[[],[7],[25],[7,7],[7,13],[7,7,13],[7,13,19,31]]
for ns in prime_norms:
 for U in [1,2,6,7,13,24,25,50,100,244]:
  A=B=0;series=F(0);numU=F(0);xs=[F((-1)**i,i+4) for i in range(len(ns))]
  for places in product(range(3),repeat=len(ns)):
   na=nb=1;sgn_ab=sgn_c=1;assigned=[]
   for i,(norm,t) in enumerate(zip(ns,places)):
    if t==0:na*=norm;sgn_ab*=-1;assigned.append(i)
    elif t==1:nb*=norm;sgn_ab*=-1;assigned.append(i)
    else:sgn_c*=-1
   if na<=U and nb<=U:
    A+=sgn_ab;B+=sgn_c
  assert (-1)**len(ns)*A==B;checks+=1
  # Each ideal support S is an actual squarefree column of these distinct primes.
  for subset in product([False,True],repeat=len(ns)):
   col=[i for i,t in enumerate(subset) if t];BU=0
   for places in product(range(3),repeat=len(col)):
    na=nb=1;sc=1
    for i,t in zip(col,places):
     if t==0:na*=ns[i]
     elif t==1:nb*=ns[i]
     else:sc*=-1
    if na<=U and nb<=U:BU+=sc
   term=F(BU)
   for i in col:term*=xs[i]
   series+=term
  L_inverse=F(1)
  for z in xs:L_inverse*=1-z
  for places in product(range(3),repeat=len(ns)):
   na=nb=1;term=F(1)
   for i,(norm,t) in enumerate(zip(ns,places)):
    if t==0:na*=norm;term*=xs[i]/(1-xs[i])
    elif t==1:nb*=norm;term*=xs[i]/(1-xs[i])
   if na<=U and nb<=U:numU+=term
  assert series==L_inverse*numU;checks+=1
  if U==1:assert numU==1 and series==L_inverse;checks+=1
  cases.append({'distinct_prime_ideal_norms':ns,'U':U,'mu_times_A':B,'finite_series':str(series),'finite_numerator':str(numU)})
# New opposite signs and coordinate slices, checked as exact rational identities.
negative_controls=0
for z in [F(1,7),F(-1,11),F(1,19)]:
 for al,be in [(F(1),F(1)),(F(1),F(1,3)),(F(1,2),F(1,5)),(F(0),F(0))]:
  direct=1+z*(al+be-1)
  H=direct*(1-z*al)*(1-z*be)/(1-z)
  assert direct==(1-z)/((1-z*al)*(1-z*be))*H;checks+=1
  assert H==1+(z*z*(al+be-al*al-be*be-al*be)+z**3*al*be*(al+be-1))/(1-z);checks+=1
  if al==be==1:assert H==1-z*z;checks+=1
  if al==1:assert H==1-(z*be)**2;checks+=1
  wrong=1+z*(1-al-be)
  if wrong!=direct:negative_controls+=1
assert negative_controls>=3
report={'passed':True,'exact_grouped_controls':checks,'negative_opposite_sign_controls':negative_controls,'finite_support_cases':cases,'new_source_sha256':{str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest() for p in [Path(__file__),Path(__file__).with_name('GAUGED_MELLIN_BARRIER-v2.md')]},'scope':'Exact local algebra and finite-cutoff coefficient diagnostics; analytic normal convergence proved separately. No original-row/kernel bound, critical-strip reciprocal estimate, Lean or GRH claim.'}
out=R/'outputs/checks/2026-11-05-signed-weights/root/gauged-euler-v1.json';assert not out.exists();out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({k:v for k,v in report.items() if k!='finite_support_cases'}))
