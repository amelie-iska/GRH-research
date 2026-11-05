#!/usr/bin/env python3
"""Exact original-symbol commutator budgets; stdlib, independent ring/field code."""
import argparse, hashlib, json, sys
from collections import Counter
from fractions import Fraction as F
from itertools import product
from math import isqrt
from pathlib import Path
sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parents[3]
ONE=(1,0); ZERO=(0,0)
def mul(x,y):
 a,b=x;c,d=y
 return a*c-b*d,a*d+b*c-b*d

def add(x,y):return x[0]+y[0],x[1]+y[1]
def conj(x):return x[0]-x[1],-x[1]
def norm(x):return x[0]*x[0]-x[0]*x[1]+x[1]*x[1]
def real(x):return F(2*x[0]-x[1],2)
def power(x,n):
 out=ONE
 while n:
  if n&1:out=mul(out,x)
  x=mul(x,x);n//=2
 return out
UNITS=tuple(power((1,1),i) for i in range(6))
def divexact(x,y):
 d=norm(y);a,b=mul(x,conj(y))
 return (a//d,b//d) if a%d==b%d==0 else None

def prime(n):return n>1 and all(n%d for d in range(2,isqrt(n)+1))
def elements(B):
 k=2*isqrt(B)+2
 return sorted(((a,b) for a in range(-k,k+1) for b in range(-k,k+1) if 0<norm((a,b))<=B),key=lambda x:(norm(x),x))
def ideals(B):return [g for g in elements(B) if g[0]%3==1 and g[1]%3==0 and norm(g)%2 and norm(g)%3]
def fact(g,ps):
 fs=[];v=g
 for p in ps:
  e=0
  while (q:=divexact(v,p)) is not None:v=q;e+=1
  if e:fs.append((p,e))
 assert v==ONE,(g,v)
 return fs

def universe(B):
 gs=ideals(B)
 ps=[g for g in gs if prime(norm(g)) or (g[1]==0 and prime(abs(g[0])) and abs(g[0])%3==2)]
 fs={g:fact(g,ps) for g in gs}
 return gs,ps,fs

def moebius(fs):return 0 if any(e>1 for p,e in fs) else (-1)**len(fs)
def factorpairs(fs,U):
 ps=[p for p,e in fs];out=[]
 for bits in product([0,1],repeat=len(ps)):
  a=b=ONE
  for p,i in zip(ps,bits):
   if i:a=mul(a,p)
   else:b=mul(b,p)
  if norm(a)>U and norm(b)>U:out.append((a,b))
 return out

def local(pi,u):
 q=norm(pi)
 if pi[1]:
  w=(-pi[0]*pow(pi[1],-1,q))%q
  z=(u[0]+u[1]*w)%q
  if not z:return None
  y=pow(z,(q-1)//6,q);roots=[pow((1+w)%q,j,q) for j in range(6)]
 else:
  p=abs(pi[0]);z=(u[0]%p,u[1]%p)
  if z==ZERO:return None
  def mp(a,b):return tuple(t%p for t in mul(a,b))
  def pp(a,n):
   y=ONE
   while n:
    if n&1:y=mp(y,a)
    a=mp(a,a);n//=2
   return y
  y=pp(z,(q-1)//6);roots=[pp((1,1),j) for j in range(6)]
 assert len(set(roots))==6
 return roots.index(y)

def symbol(fs,u):
 e=0
 for p,k in fs:
  x=local(p,u)
  if x is None:return ZERO
  e+=k*x
 return UNITS[e%6]

# Exact Q-linear combinations of sqrt(squarefree positive integers).
def clean(a):return {d:F(c) for d,c in a.items() if c}
def radd(a,b):
 c=dict(a)
 for d,v in b.items():c[d]=c.get(d,F(0))+v
 return clean(c)
def rscale(c,a):return clean({d:c*v for d,v in a.items()})
def root(n):
 n=F(n)
 if not n:return {}
 assert n>0
 a,b=n.numerator,n.denominator;v=a*b;c=1;d=1;p=2
 while p*p<=v:
  k=0
  while v%p==0:v//=p;k+=1
  c*=p**(k//2)
  if k%2:d*=p
  p+=1
 d*=v
 return {d:F(c,b)}
def rmul(a,b):
 out={}
 for d,c in a.items():
  for e,f in b.items():out=radd(out,rscale(c*f,root(d*e)))
 return out

def rrat(n):return {1:F(n)} if n else {}
def rstr(a):return {str(d):str(c) for d,c in sorted(a.items())}
def interval(a):
 den=10**35;lo=hi=F(0)
 for d,c in a.items():
  k=isqrt(d*den*den);l=F(k,den);h=l if k*k==d*den*den else F(k+1,den)
  if c>=0:lo+=c*l;hi+=c*h
  else:lo+=c*h;hi+=c*l
 return lo,hi

def nonnegative(a):
 if not a:return True
 return interval(a)[0]>=0

def moments_case(D,U,gs,fs):
 cols=[g for g in gs if D<=norm(g)<=2*D and moebius(fs[g])]
 rs=[];dyadic=Counter();quads=0
 for g in cols:
  fps=factorpairs(fs[g],U);rs.append(len(fps))
  for (a,b),(c,d) in product(fps,repeat=2):
   common=[p for p,e in fs[g] if divexact(a,p) is not None and divexact(c,p) is not None]
   gg=ONE
   for p in common:gg=mul(gg,p)
   h=divexact(a,gg);k=divexact(c,gg);ell=divexact(b,k)
   assert ell is not None and mul(h,ell)==d and mul(mul(gg,h),mul(k,ell))==g
   assert all(norm(z)<=F(2*D,U) for z in [a,b,c,d])
   M=max(norm(h),norm(k));j=M.bit_length()-1
   assert norm(gg)*M<=F(2*D,U) and norm(ell)*M<=F(2*D,U)
   dyadic[j]+=1;quads+=1
 assert quads==sum(r*r for r in rs)
 return dict(D=D,U=U,columns=len(cols),r_histogram=dict(sorted(Counter(rs).items())),sum_r=sum(rs),sum_r_squared=quads,quadruple_dyadic_counts=dict(sorted(dyadic.items())))

def gram_case(name,D,U,cols,fs,rows,nu_num=ONE,weights=None):
 r=[len(factorpairs(fs[g],U)) for g in cols]
 mu=[moebius(fs[g]) for g in cols]
 if weights is None:weights={norm(g):(F((norm(g)-D)*(2*D-norm(g)),D*D),F(0)) for g in cols}
 v=[mul((mu[i],0),mul(symbol(fs[g],nu_num),weights[norm(g)])) for i,g in enumerate(cols)]
 table=[[symbol(fs[g],u) for g in cols] for u in rows]
 G=[]
 for i in range(len(cols)):
  row=[]
  for j in range(len(cols)):
   z=ZERO
   for a in table:z=add(z,mul(a[i],conj(a[j])))
   row.append(z)
  G.append(row)
 assert all(G[j][i]==conj(G[i][j]) for i,j in product(range(len(cols)),repeat=2))
 classes=[((norm(g)-1)//6)%6 for g in cols]
 for i,g in enumerate(cols):
  assert symbol(fs[g],UNITS[1])==UNITS[classes[i]]
 unit_vanish=0;cross_level=0;raw_zeros=sum(z==ZERO for a in table for z in a)
 cov=F(0);EA=EC=EM=F(0);QS={};DC={};B={}
 for i,j in product(range(len(cols)),repeat=2):
  if classes[i]!=classes[j]:assert G[i][j]==ZERO;unit_vanish+=1
  if r[i]!=r[j] and G[i][j]!=ZERO:cross_level+=1
  z=real(mul(mul(v[i],conj(v[j])),G[i][j]))/D
  cov+=r[i]*z;EA+=(r[i]-1)*(r[j]-1)*z;EC+=r[i]*r[j]*z;EM+=z
  sr=root(r[i]*r[j]);delta=radd(rrat(r[i]+r[j]),rscale(-2,sr))
  QS=radd(QS,rscale(z,sr));DC=radd(DC,rscale(z,delta))
  B=radd(B,rscale(F(1,2*D),rmul(delta,root(norm(v[i])*norm(v[j])*norm(G[i][j])))))
 assert EA==EC+EM-2*cov
 assert radd(QS,rscale(F(1,2),DC))==rrat(cov)
 assert nonnegative(radd(radd(rrat(cov),rscale(-1,QS)),B))
 trace=sum(G[i][i][0] for i in range(len(cols)))
 # Gershgorin with integer upper enclosures of the exact complex moduli.
 schur=max(sum((lambda n:isqrt(n)+(isqrt(n)**2<n))(norm(z)) for z in row) for row in G)
 Lambda=min(trace,schur)
 M=[sum(F(r[i]**j)*norm(v[i]) for i in range(len(cols))) for j in range(3)]
 vb=rscale(F(-Lambda,2*D),radd(root(M[0]*M[2]),rrat(-M[1])))
 assert nonnegative(radd(rrat(cov),rscale(-1,vb)))
 lo,hi=interval(B)
 return dict(name=name,D=D,U=U,rows=len(rows),columns=len(cols),nu_numerator=nu_num,r_histogram=dict(sorted(Counter(r).items())),raw_zero_entries=raw_zeros,phase_values=len(rows)*len(cols),unit_class_vanishing_pairs=unit_vanish,nonzero_cross_level_pairs=cross_level,Gram_psd_upper_bound=Lambda,real_covariance=str(cov),energy_A=str(EA),energy_C=str(EC),energy_mu=str(EM),weighted_moments=[str(t) for t in M],positive_S_energy=rstr(QS),double_commutator_quadratic=rstr(DC),Schur_budget=rstr(B),Schur_budget_interval=[str(lo),str(hi)],vector_specific_lower_budget=rstr(vb))

def exponents():
 total=sat=0
 for xs in product(range(13),repeat=6):
  cost=sum((j+1)*x for j,x in enumerate(xs))
  if cost>12:continue
  m=max(xs[:2]);rr=sum(xs);slack=12-3*(rr-m)
  branch=(xs[0]-xs[1] if xs[0]>=xs[1] else 2*(xs[1]-xs[0]))+xs[3]+2*xs[4]+3*xs[5]
  assert slack==12-cost+branch and slack>=0
  eq=slack==0
  assert eq==(cost==12 and xs[0]==xs[1] and xs[3:]==(0,0,0))
  total+=1;sat+=eq
 return dict(grid_denominator=12,admissible_cases=total,saturating_cases=sat,saturation='A1=A2, A1*A3=H^(1/3), A4=A5=A6=1; not only A3=1')

def main(out):
 if out.exists():raise FileExistsError('Preserve existing evidence')
 gs,ps,fs=universe(10000)
 moment=[]
 for D,U in [(128,7),(128,11),(400,11),(400,17),(400,20),(1024,18),(1024,32),(5000,40),(5000,70)]:
  assert 2*D<=7*U*U and U*U<=D
  moment.append(moments_case(D,U,gs,fs))
 small=[p for p in ps if 7<=norm(p)<14]
 rows=[mul(e,mul(a,power(b,2))) for a,b in product(small,repeat=2) if a!=b for e in UNITS]
 assert len(rows)==72
 fixtures=[]
 oldcols=[g for g in gs if norm(g) in [439,475] and moebius(fs[g])]
 for x in [1,4,8,10]:
  fixtures.append(gram_case('accepted_smooth_four_column_x'+str(x),400,17,oldcols,fs,rows,weights={439:(F(x),F(0)),475:(F(1),F(0))}))
 assert fixtures[-1]['real_covariance']=='-27/25'
 broad=[g for g in gs if 400<=norm(g)<=800 and moebius(fs[g])]
 for U,nu in [(11,ONE),(17,(2,0)),(20,ONE)]:
  fixtures.append(gram_case('all_annular_columns_B7',400,U,broad,fs,rows,nu))
 # Three genuine factor-count levels, including irrational sqrt(6), in one smooth norm profile.
 pp=next(norm(p) for p in ps if 5000<norm(p)<10000 and norm(p)%36==1)
 selected=[g for g in gs if norm(g) in [pp,5977,8281] and moebius(fs[g])]
 row19=[p for p in ps if norm(p)==19];row31=[p for p in ps if norm(p)==31]
 rr=[mul(e,mul(a,power(b,2))) for a,b in product(row19,row31) for e in UNITS]
 weights={q:(F(1+(q%5),3),F(q%3,4)) for q in [pp,5977,8281]}
 fixtures.append(gram_case('three_count_levels_complex_common_profile',5000,40,selected,fs,rr,(2,0),weights))
 assert set(map(int,fixtures[-1]['r_histogram']))=={0,2,6}
 sources=[Path(__file__),ROOT/'papers/signed-bilinear-core.tex',ROOT/'papers/signed-bilinear-details.tex',ROOT/'research/signed-cutoff-covariance.md',ROOT/'planning/weighted-moment-20261105/frontier/CENTERING_AND_SIGNED_TARGET.md']
 report=dict(passed=True,seed='none; exact enumeration',implementation='Independent stdlib Eisenstein ring, ideal factorization and residue-field exponentiation; exact rational radical arithmetic; no project helper imports.',moment_cases=moment,Gram_cases=fixtures,near_saturating_exponent_grid=exponents(),source_sha256={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in sources},scope='Finite diagnostics of new covariance budgets and ideal moment bookkeeping; not proof of a new analytic saving, BT_sigma, energy lower bound, Lean or GRH.')
 out.mkdir(parents=True)
 (out/'exact-budget.json').write_text(json.dumps(report,indent=2)+'\n')
 print(json.dumps(dict(passed=True,moment_cases=len(moment),Gram_cases=len(fixtures),phase_values=sum(x['phase_values'] for x in fixtures),raw_zero_entries=sum(x['raw_zero_entries'] for x in fixtures),exponent_grid=report['near_saturating_exponent_grid'],output=str(out/'exact-budget.json')),indent=2))
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--output',type=Path,required=True);main(p.parse_args().output)
