#!/usr/bin/env python3
"""Exact original-family signed covariance counterexample; not a GRH estimate.

All four active ideal columns of norms439/475 are retained. The smooth common
profile has exact integer-norm values10/1; no transcendental sample is evaluated.
"""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
from fractions import Fraction as F
from itertools import product
import argparse,json,hashlib
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'scripts'))
from check_mobius_split import universe,elements,quotient,scalar_symbol
from check_reciprocity_period import emul,norm,power
PH=((1,0),(1,1),(0,1),(-1,0),(-1,-1),(0,-1))
ZERO=(0,0)
def plus(a,b):return(a[0]+b[0],a[1]+b[1])
def times(c,a):return(c*a[0],c*a[1])
def conj(a):return(a[0]-a[1],-a[1])
def real(a):return F(2*a[0]-a[1],2)
def inner(a,b):return emul(a,conj(b))
def total(xs):
 z=ZERO
 for x in xs:z=plus(z,x)
 return z
def phase(e):return ZERO if e is None else PH[e%6]
def strip_bad(u):
 for p in [(2,0),(1,-1)]:
  while (v:=quotient(u,p)) is not None:u=v
 return u

def run(output):
 if output.exists():raise FileExistsError('Preserve prior exact experiments')
 D,U=400,17
 assert U*U<=D and 7*U*U>=2*D
 ids,index,divs,ps=universe(800)
 # W_x(y)=x phi(4(400y-439))+phi(4(400y-475)),
 # phi(t)=exp(1-1/(1-t^2)) for |t|<1, zero otherwise.
 # Integer norms make both evaluation rules below exact, with no exp arithmetic.
 columns=[i for i,n in enumerate(ids) if n['sf'] and D<=n['q']<=2*D and n['q'] in(439,475)]
 assert len(columns)==4 and [ids[i]['q'] for i in columns]==[439,439,475,475]
 coeff={}
 for i in columns:
  beta={}
  for d in divs[i]:
   beta[d]=sum(ids[a]['mu']*ids[index[quotient(ids[d]['g'],ids[a]['g'])]]['mu'] for a in divs[d] if ids[a]['q']<=U and norm(quotient(ids[d]['g'],ids[a]['g']))<=U)
  A=sum(beta.values());C=0;r=0
  for a in divs[i]:
   rem=index[quotient(ids[i]['g'],ids[a]['g'])]
   for b in divs[rem]:
    if ids[a]['q']>U and ids[b]['q']>U:C+=ids[a]['mu']*ids[b]['mu']
   if ids[a]['q']>U and ids[rem]['q']>U:r+=1
  assert C==ids[i]['mu']*r and r%2==0 and A==C-ids[i]['mu']
  assert A==1 and C==(0 if ids[i]['q']==439 else 2)
  coeff[i]=dict(A=A,C=C,mu=ids[i]['mu'],ordered_long_factors=r)
 # Complete B_7: good squarefree ideals with norm in[7,14) are exactly these4primes.
 small=[n for n in ids if n['sf'] and 7<=n['q']<14]
 basis=[p for p in ps if 7<=norm(p)<14]
 assert len(small)==len(basis)==4 and {n['g'] for n in small}==set(basis)
 balanced=[emul(v,emul(a,power(b,2))) for a,b in product(basis,repeat=2) if a!=b for v in PH]
 assert len(balanced)==len(set(balanced))==72 and max(map(norm,balanced))==2197
 # A second guaranteed nonprincipal subset at H=floor(D^(3/4)).
 # Outside-S exponents are1or2 since7^3>89, so the character is nonprincipal.
 H=89;assert H**4<=D**3<(H+1)**4
 short=[u for u in elements(H) if norm(strip_bad(u))>1]
 assert len(short)==246
 reports={}
 for name,rows in [('balanced_B7',balanced),('outside_S_nontrivial_H89',short)]:
  raw=[[phase(scalar_symbol(ids[i]['f'],u)) for i in columns] for u in rows]
  G=[[total(inner(v[i],v[j]) for v in raw) for j in range(4)] for i in range(4)]
  R=[[real(x) for x in row] for row in G]
  assert all(G[j][i]==conj(G[i][j]) for i,j in product(range(4),repeat=2))
  observations=[]
  for x in [0,1,4,5,7,10]:
   ws=[x,x,1,1];ac=[coeff[i]['A']*w for i,w in zip(columns,ws)];cc=[coeff[i]['C']*w for i,w in zip(columns,ws)];mc=[coeff[i]['mu']*w for i,w in zip(columns,ws)]
   EA=EC=EM=0;cov=ZERO
   for v in raw:
    aa,cl,mm=[total(times(t,z) for t,z in zip(cs,v)) for cs in(ac,cc,mc)]
    assert aa==plus(cl,times(-1,mm))
    EA+=norm(aa);EC+=norm(cl);EM+=norm(mm);cov=plus(cov,inner(cl,mm))
   assert F(EA,D)==F(EC+EM,D)-2*real(cov)/D
   expansion=total(times(cc[j]*mc[k],G[j][k]) for j,k in product(range(4),repeat=2))
   assert expansion==cov
   diagonal=sum(cc[j]*mc[j]*G[j][j][0] for j in range(4));assert diagonal>=0
   observations.append(dict(profile_amplitude=x,energy_A=str(F(EA,D)),energy_C=str(F(EC,D)),energy_M=str(F(EM,D)),real_covariance=str(real(cov)/D),diagonal_covariance=str(F(diagonal,D)),off_diagonal_covariance=str((real(cov)-diagonal)/D)))
  if name=='balanced_B7':
   assert R==[[72,0,0,18],[0,72,18,0],[0,18,72,0],[18,0,0,72]]
   assert observations[-1]['real_covariance']=='-27/25'
   assert observations[-1]['energy_A']=='954/25'
   assert observations[-1]['energy_C']=='36/25' and observations[-1]['energy_M']=='864/25'
   # Real-part Gram is positive definite: (R-72I)^2=18^2I.
   T=[[R[j][k]-(72 if j==k else 0) for k in range(4)] for j in range(4)]
   assert [[sum(T[j][q]*T[q][k] for q in range(4)) for k in range(4)] for j in range(4)]==[[324 if j==k else 0 for k in range(4)] for j in range(4)]
  else:assert observations[-1]['real_covariance']=='-69/50'
  reports[name]=dict(rows=len(rows),max_row_norm=max(map(norm,rows)),raw_zero_entries=sum(z==ZERO for v in raw for z in v),Gram_Eisenstein=G,Gram_real=[[str(v) for v in row] for row in R],observations=observations,row_data=[dict(u=u,characters=v) for u,v in zip(rows,raw)])
 output.mkdir(parents=True)
 sources=[Path(__file__),ROOT/'scripts/check_mobius_split.py',ROOT/'scripts/check_reciprocity_period.py',ROOT/'scripts/check_finite_correlation.py']
 report=dict(passed=True,D=D,U=U,nu='principal',S='prime ideals above2and3',columns=[dict(generator=ids[i]['g'],norm=ids[i]['q'],factors=ids[i]['f'],**coeff[i]) for i in columns],common_smooth_profile='W_x(y)=x*phi(4*(400*y-439))+phi(4*(400*y-475)); phi(t)=exp(1-1/(1-t^2)) on abs(t)<1 and0otherwise; x=10 for counterexample',profile_supnorm=10,normalized_coefficient_l2='101/200',row_cases=reports,source_sha256={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in sources},scope='Exact finite original-ideal/raw-sextic covariance counterexample to automatic nonnegative covariance; no asymptotic BT_sigma counterexample, analytic saving, arithmetic determinant, Lean or GRH proof.')
 (output/'counterexample.json').write_text(json.dumps(report,indent=2)+'\n')
 print(json.dumps({k:v for k,v in report.items() if k!='row_cases'},indent=2))
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--output',type=Path,required=True);run(p.parse_args().output)
