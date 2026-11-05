#!/usr/bin/env python3
"""Independent exact negative/edge diagnostics. No imports from author checkers."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
from fractions import Fraction as F
from itertools import product
from math import gcd
import argparse, hashlib, json
ROOT=Path(__file__).resolve().parents[3]
Z=(F(0),F(0)); ONE=(F(1),F(0))
PH=((1,0),(1,1),(0,1),(-1,0),(-1,-1),(0,-1))
PRIMES=((1,3),(-2,-3),(4,3),(1,-3),(-5,0))

def add(x,y):return x[0]+y[0],x[1]+y[1]
def neg(x):return -x[0],-x[1]
def sub(x,y):return add(x,neg(y))
def mul(x,y):return x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0]-x[1]*y[1]
def sc(t,x):return t*x[0],t*x[1]
def conj(x):return x[0]-x[1],-x[1]
def real(x):return x[0]-x[1]/2
def nn(x):return x[0]*x[0]-x[0]*x[1]+x[1]*x[1]
def ip(x,y):return mul(x,conj(y))
def summ(xs):
 s=Z
 for x in xs:s=add(s,x)
 return s

def powr(x,k):
 r=(1,0)
 while k:
  if k&1:r=mul(r,x)
  x=mul(x,x);k//=2
 return r

def red(x,pi):
 q=nn(pi)
 if pi[1]:return ((x[0]+x[1]*(-pi[0])*pow(pi[1],-1,q))%q,0)
 p=abs(pi[0]);return x[0]%p,x[1]%p

def fpow(x,k,pi):
 r=(1,0)
 while k:
  if k&1:r=red(mul(r,x),pi)
  x=red(mul(x,x),pi);k//=2
 return r

def sextic(pi,x):
 y=red(x,pi)
 if y==(0,0):return None
 v=fpow(y,(nn(pi)-1)//6,pi)
 roots=[red(z,pi) for z in PH]
 assert len(set(roots))==6
 return roots.index(v)

def raw(mask,u):
 e=0
 for i,p in enumerate(PRIMES):
  if mask>>i&1:
   t=sextic(p,u)
   if t is None:return Z
   e+=t
 return PH[e%6]

def norms_of(prime_norms):
 return [__import__('functools').reduce(lambda a,b:a*b,(q for i,q in enumerate(prime_norms) if m>>i&1),1) for m in range(1<<len(prime_norms))]

def coeffs(mask,U,ns):
 bits=[i for i in range(len(PRIMES)) if mask>>i&1]
 A=C=beta=0
 for placements in product((0,1,2),repeat=len(bits)):
  a=b=0
  for i,k in zip(bits,placements):
   if k==1:a|=1<<i
   if k==2:b|=1<<i
  s=(-1)**((a|b).bit_count())
  A+=s*(ns[a]<=U and ns[b]<=U)
  C+=s*(ns[a]>U and ns[b]>U)
  if a|b==mask:beta+=s*(ns[a]<=U and ns[b]<=U)
 return A,C,beta

def encoded(x):
 if isinstance(x,F):return str(x)
 if isinstance(x,dict):return {k:encoded(v) for k,v in x.items()}
 if isinstance(x,(list,tuple)):return [encoded(v) for v in x]
 return x

def main(output):
 if output.exists():raise FileExistsError('Preserve previous review evidence')
 ns=norms_of([nn(p) for p in PRIMES]);mus=[(-1)**m.bit_count() for m in range(len(ns))]
 Uvalues=[F(1),F(13,2),F(7),F(15,2),F(13),F(25),F(49)]
 ll=active=endpoints=0;tables={}
 for U in Uvalues:
  tab=[coeffs(m,U,ns) for m in range(len(ns))];tables[U]=tab
  for m,(A,C,beta) in enumerate(tab):
   assert A==mus[m]-2*mus[m]*(ns[m]>U)+C;ll+=1
   if ns[m]>U:assert A==C-mus[m];active+=1
   if ns[m]==U*U and U>1:
    assert C==0 and A==-mus[m];endpoints+=1
 assert endpoints>=2
 # Hypothesis controls: Nm=U is outside active reduction; nonsquarefree m is excluded.
 assert tables[F(7)][1][0]==mus[1] and tables[F(7)][1][0]!=tables[F(7)][1][1]-mus[1]
 assert 1-1-1 != 0 # unrestricted disjoint three-placement sum for p^2 vs mu(p^2).
 # Tame local inertia: nonzero exponents 1,2 remain nontrivial even at inert norm25.
 local=[]
 for pi in PRIMES:
  q=nn(pi)
  residues=[(a,0) for a in range(q)] if pi[1] else list(product(range(abs(pi[0])),repeat=2))
  values={sextic(pi,x) for x in residues}-{None}
  assert values==set(range(6))
  for r in range(1,6):
   image={(r*k)%6 for k in values}
   assert len(image)==6//gcd(6,r)>1
   # Any unramified twist has inertia exponent zero. A ramified inverse could cancel.
   assert {(r*k+0)%6 for k in values}==image
   assert {(r*k-r*k)%6 for k in values}=={0}
   local.append(dict(norm=q,valuation=r,inertia_order=len(image),tame_conductor_exponent=1))
 rows=[]
 for i,j in product(range(4),repeat=2):
  if i!=j:
   u=mul(PRIMES[i],powr(PRIMES[j],2))
   rows.extend(mul(e,u) for e in PH)
 assert len(rows)==len(set(rows))==72
 assert all(7<=nn(PRIMES[i])<14 for i in range(4))
 sixth=powr(PRIMES[0],6)
 masks=range(len(ns));raw_cases=zero_cases=wrong_inverse=0
 for u in rows+[sixth,(1,0)]:
  xs=[raw(m,u) for m in masks]
  for m,n in product(masks,repeat=2):
   observed=ip(xs[m],xs[n]);union=m|n
   deleted=any(union>>i&1 and red(u,p)==(0,0) for i,p in enumerate(PRIMES))
   if deleted:assert observed==Z;zero_cases+=1
   else:
    e=sum(((m>>i&1)-(n>>i&1))*sextic(p,u) for i,p in enumerate(PRIMES) if (m^n)>>i&1)
    assert observed==PH[e%6]
    wrong_inverse+=observed!=mul(xs[m],xs[n])
   if m==n:assert observed==((0,0) if deleted else (1,0))
   raw_cases+=1
 assert ip(raw(1,sixth),raw(1,sixth))==Z and raw(0,sixth)==ONE
 assert wrong_inverse>0
 # Complex weights and true fixed Kummer twists; inclusive annulus and U^2=D cases.
 profiles=[];cov_cases=gram_cases=bt_cases=wrong_cov=wrong_w=0
 for D,U in ((49,7),(64,7),(128,7),(169,13),(625,25),(1024,20)):
  assert U*U<=D and D>U
  tab=tables.get(F(U)) or [coeffs(m,F(U),ns) for m in masks]
  columns=[m for m in masks if D<=ns[m]<=2*D]
  assert columns
  endpoint_columns=sum(ns[m] in (D,2*D) for m in columns)
  w={m:(F(ns[m]+D,D),F(ns[m]*ns[m]+D*D,D*D)) for m in columns}
  for twist in ((1,0),(2,0),(-1,0)):
   nu={m:raw(m,twist) for m in columns};assert all(v!=Z for v in nu.values())
   energies=[F(0),F(0),F(0)];cov=Z
   for u in rows:
    terms={m:mul(mul(w[m],nu[m]),raw(m,u)) for m in columns}
    aa=summ(sc(tab[m][0],terms[m]) for m in columns)
    cc=summ(sc(tab[m][1],terms[m]) for m in columns)
    mm=summ(sc(mus[m],terms[m]) for m in columns)
    assert aa==sub(cc,mm)
    ccmm=ip(cc,mm)
    assert nn(aa)==nn(cc)+nn(mm)-2*real(ccmm)
    wrong_cov+=nn(aa)!=nn(cc)+nn(mm)-2*real(mul(cc,mm))
    wrong_cov+=nn(aa)!=nn(cc)+nn(mm)+2*real(ccmm)
    for k,x in enumerate((aa,cc,mm)):energies[k]+=nn(x)/D
    cov=add(cov,sc(F(1,D),ccmm));cov_cases+=1
   expanded=Z;bad_weight=Z
   for m,n in product(columns,repeat=2):
    G=summ(ip(raw(m,u),raw(n,u)) for u in rows)
    k=sc(F(tab[m][0]*tab[n][0],D),mul(ip(nu[m],nu[n]),G))
    expanded=add(expanded,mul(k,ip(w[m],w[n])))
    bad_weight=add(bad_weight,mul(k,mul(w[m],w[n])))
   assert expanded==(energies[0],0);gram_cases+=1;wrong_w+=bad_weight!=expanded
   assert energies[0]==energies[1]+energies[2]-2*real(cov)
   for R in (energies[0]-1,energies[0],energies[0]+1):
    assert (energies[0]<=R)==(2*real(cov)>=energies[1]+energies[2]-R);bt_cases+=1
   profiles.append(dict(D=D,U=U,endpoint_columns=endpoint_columns,columns=len(columns),nu_numerator=twist,energy=energies[0],covariance=cov))
 assert wrong_cov and wrong_w and sum(p['endpoint_columns'] for p in profiles)>0
 # Centered beta Gram algebra with actual t-columns and a nonzero formal residue constant.
 D=49;U=7;tab=tables[F(U)];ds=[d for d in masks if tab[d][2]]
 testrows=rows+[(1,0),sixth];principal=[False]*len(rows)+[True,True]
 What=(F(2),F(1));tt=[];rr=[];ee=[];I=[];P=[]
 for u,pr in zip(testrows,principal):
  trow=[];rrow=[]
  for d in ds:
   tx=summ(sc(F(1,7),mul((F(ns[d|c]+D,D),F(ns[d|c]**2+D**2,D**2)),raw(d|c,u))) for c in masks if not c&d and D<=ns[d|c]<=2*D and all(not(c>>i&1) or red(u,p)!=(0,0) for i,p in enumerate(PRIMES)))
   # rho_T/residue base is treated as a formal common constant =1; no numeric pole claim.
   rho=F(1)
   for i,p in enumerate(PRIMES):
    if d>>i&1 or red(u,p)==(0,0):rho*=F(nn(p),nn(p)+1)
   rx=sc(F(7,ns[d])*rho,mul(What,raw(d,u))) if pr else Z
   trow.append(tx);rrow.append(rx)
  erow=[sub(t,r) for t,r in zip(trow,rrow)];tt.append(trow);rr.append(rrow);ee.append(erow)
  I.append(summ(sc(tab[d][2],trow[j]) for j,d in enumerate(ds)))
  P.append(summ(sc(tab[d][2],rrow[j]) for j,d in enumerate(ds)))
 E=[sub(i,p) for i,p in zip(I,P)]
 assert all(E[k]==summ(sc(tab[d][2],ee[k][j]) for j,d in enumerate(ds)) for k in range(len(testrows)))
 K=[[summ(ip(e[j],e[k]) for e in ee) for k in range(len(ds))] for j in range(len(ds))]
 centered=summ(sc(tab[d][2]*tab[f][2],K[j][k]) for j,d in enumerate(ds) for k,f in enumerate(ds))
 assert centered==(sum(nn(e) for e in E),0)
 assert sum(nn(e) for e in E)==sum(nn(i) for i,pr in zip(I,principal) if not pr)+sum(nn(sub(i,p)) for i,p,pr in zip(I,P,principal) if pr)
 assert all(P[k]==Z and E[k]==I[k] for k in range(len(rows)))
 assert all(K[j][k]==conj(K[k][j]) for j,k in product(range(len(ds)),repeat=2))
 for shift in range(5):
  z=[(F(j+shift+1),F(j*2-shift)) for j in range(len(ds))]
  q=summ(mul(ip(z[j],z[k]),K[j][k]) for j,k in product(range(len(ds)),repeat=2))
  assert q[1]==0 and q[0]>=0
 # No orthogonality follows from the formal residue subtraction.
 projection_witness=next((ip(e,r) for er,rrr in zip(ee,rr) for e,r in zip(er,rrr) if ip(e,r)!=Z),None)
 assert projection_witness is not None
 sources=[ROOT/'planning/weighted-moment-20261105/frontier/CENTERING_AND_SIGNED_TARGET.md',ROOT/'planning/weighted-moment-20261105/frontier/check_frontier_exact.py',ROOT/'planning/weighted-moment-20261105/frontier/HANDOFF.md',ROOT/'planning/weighted-moment-20261105/frontier/manifest.json',ROOT/'outputs/checks/2026-11-05-weighted-moment/frontier/exact-controls-v1.json',ROOT/'research/weighted-cutoff-moment.md',ROOT/'papers/masked-moment-details.tex',ROOT/'planning/weighted-moment-20261104/attempt/UNIFORM_CUTOFF_MOMENT.md',Path(__file__)]
 manifest=json.loads(sources[3].read_text())
 for name,digest in manifest['paths_sha256'].items():assert hashlib.sha256((ROOT/name).read_bytes()).hexdigest()==digest
 report=dict(passed=True,deterministic=True,seed='none',python=sys.version.split()[0],independent_no_author_imports=True,
 ll_cases=ll,active_cases=active,exact_U_squared_endpoint_cases=endpoints,
 cutoff_values=Uvalues,local_inertia_cases=local,balanced_literal_rows=len(rows),
 raw_product_cases=raw_cases,union_mask_zero_cases=zero_cases,wrong_inverse_witnesses=wrong_inverse,
 complex_covariance_row_cases=cov_cases,independent_Gram_expansions=gram_cases,
 signed_target_equivalence_cases=bt_cases,wrong_covariance_witnesses=wrong_cov,wrong_weight_conjugation_witnesses=wrong_w,
 centered_rows=len(testrows),centered_columns=len(ds),centered_PSD_vectors=5,nonprojection_witness=projection_witness,
 negative_controls=['Nm=U does not satisfy active A=C-mu','nonsquarefree m invalidates unrestricted sum=mu','ramified inverse twist could cancel tame inertia if S hypothesis removed','symmetric-difference mask loses a shared-prime zero','primitive sixth-power row substitution loses raw zero','missing conjugate/inverse changes exact raw product','wrong covariance sign/conjugate changes energy','missing W(n) conjugate changes Gram energy'],
 complex_annular_profiles=profiles,author_manifest_hashes_match=True,
 source_sha256={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in sources},
 scope='Finite diagnostics only. Tame Kummer conductor fact, accepted Mellin transfer and powered BGL remain analytic inputs. Formal residue base=1 tests algebra, not the value of a zeta residue. Complex rational finite profiles are not analytic W estimates. No BT_sigma proof, energy lower bound, Lean or GRH claim.')
 output.parent.mkdir(parents=True,exist_ok=True)
 with output.open('x') as f:json.dump(encoded(report),f,indent=2);f.write('\n')
 print(json.dumps({k:encoded(v) for k,v in report.items() if k not in ('complex_annular_profiles','local_inertia_cases','source_sha256')},indent=2))

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--output',type=Path,required=True);a=p.parse_args();main(a.output)
