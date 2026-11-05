#!/usr/bin/env python3
"""Independent ideal-factor and direct finite-field audit of the NEW20-row diagnostic."""
from pathlib import Path
from itertools import product,combinations
from fractions import Fraction
from math import isqrt,prod
from collections import Counter
import json,hashlib
R=Path(__file__).resolve().parents[3];P=Path(__file__).resolve().parent;O=R/'outputs/checks/2026-11-05-signed-weights/review-diagnostic';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
pins=json.loads((P/'input-pins-v1.json').read_text());assert all(sha(R/p)==h for p,h in pins.items())
report=json.loads((R/'outputs/checks/2026-11-05-signed-weights/joint-budget/fixed-profile-h1-v1.json').read_text());assert report['passed']
PH=((1,0),(1,1),(0,1),(-1,0),(-1,-1),(0,-1))
def add(x,y):return x[0]+y[0],x[1]+y[1]
def mul(x,y):return x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0]-x[1]*y[1]
def norm(z):return z[0]**2-z[0]*z[1]+z[1]**2
def conj(z):return z[0]-z[1],-z[1]
def quotient(x,y):
 a,b=mul(x,conj(y));n=norm(y)
 return (a//n,b//n) if a%n==b%n==0 else None
def power(z,k):
 out=(1,0)
 while k:
  if k%2:out=mul(out,z)
  z=mul(z,z);k//=2
 return out
def prime(n):return n>=2 and all(n%d for d in range(2,isqrt(n)+1))
def primary(cap):
 # N(a+bω)>=3a²/4 and >=3b²/4, so this rectangle is provably exhaustive.
 B=isqrt((4*cap)//3)+1
 return sorted(((a,b) for a in range(-B,B+1) for b in range(-B,B+1) if a%3==1 and b%3==0 and 0<norm((a,b))<=cap and norm((a,b))%2 and norm((a,b))%3),key=lambda z:(norm(z),z))
primegens=[g for g in primary(313) if prime(norm(g)) or g[1]==0 and prime(abs(g[0])) and abs(g[0])%3==2]
def factor(g):
 rem=g;fs=[]
 for pi in primegens:
  while (v:=quotient(rem,pi)) is not None:fs.append(pi);rem=v
 assert rem==(1,0),(g,rem)
 return tuple(fs)
small=[(g,factor(g)) for g in primary(73)];sf=[g for g,fs in small if len(fs)==len(set(fs))]
D=60000;U=244;H=3833;assert H**4<=D**3<(H+1)**4 and 2*D<=7*U*U and U*U<=D
v1s=[g for g in sf if 37<=norm(g)<74];v2s=[g for g in sf if 7<=norm(g)<14]
rows=[];rejections=Counter()
for v,w in product(v1s,v2s):
 f1,f2=factor(v),factor(w)
 if set(f1)&set(f2):rejections['not_coprime']+=1;continue
 n=norm(v)*norm(w)**2
 if n>H:rejections['over_capacity']+=1;continue
 u=mul(v,power(w,2));assert norm(u)==n
 rows.append((v,w,u,n))
assert len(v1s)==11 and len(v2s)==4 and len(rows)==20
block=report['blocks'][1];claimed={(tuple(x['v1']),tuple(x['v2']),tuple(x['u']),x['N']) for x in block['all_rows_in_actual_block']};assert set(rows)==claimed and len({r[2] for r in rows})==20
qprimes=[]
for p in [37,43,61,307,313]:
 assert prime(p) and p%3==1
 roots=[x for x in range(p) if (x*x+x+1)%p==0];root=min(roots)
 assert root==report['lambdas'][str(p)]
 candidates=[g for g in primegens if norm(g)==p and (g[0]+g[1]*root)%p==0];assert len(candidates)==1
 qprimes.append({'norm':p,'root':root,'generator':candidates[0],'conjugate_root':max(roots)})
Q=prod(p['norm'] for p in qprimes);assert Q==report['q_norm']
orient=[]
for mask in range(1<<len(qprimes)):
 ids=[i for i in range(len(qprimes)) if mask>>i&1];other=[i for i in range(len(qprimes)) if not mask>>i&1];nm=prod(qprimes[i]['norm'] for i in ids);nn=Q//nm
 if D<=nm<=2*D and D<=nn<=2*D:orient.append((ids,other,nm,nn))
assert len(orient)==2 and [(a[2],a[3]) for a in orient]==[(97051,96091),(96091,97051)]
# Direct original ordered small-small and long-long divisor convolution. No high-window formula is assumed.
def coefficient(ids):
 fs=[qprimes[i]['generator'] for i in ids];divs=[]
 for mask in range(1<<len(fs)):
  s=frozenset(i for i in range(len(fs)) if mask>>i&1);divs.append((s,prod(norm(fs[i]) for i in s),(-1)**len(s)))
 A=C=0
 for da,na,ma in divs:
  for db,nb,mb in divs:
   if da&db:continue
   if na<=U and nb<=U:A+=ma*mb
   if na>U and nb>U:C+=ma*mb
 r=sum(na>U and prod(norm(f) for f in fs)//na>U for _,na,_ in divs);mu=(-1)**len(fs)
 assert A==C-mu and C==mu*r and A==mu*(r-1)
 return {'N':prod(norm(f) for f in fs),'A':A,'C':C,'mu':mu,'r_U':r,'generator':__import__('functools').reduce(mul,fs,(1,0))}
columns={n:coefficient(ids) for ids,other,n,nn in orient};assert columns[97051]['r_U']==0 and columns[96091]['r_U']==2
assert all(v['A']==1 for v in columns.values());assert (-1)**len(qprimes)==-1
# Exact field powers with epsilon=1+omega, retaining the raw zero at each selected ideal.
def raw(u,p,root):
 residue=(u[0]+u[1]*root)%p
 if residue==0:return None
 v=pow(residue,(p-1)//6,p);eps=(1+root)%p
 exponents=[e for e in range(6) if pow(eps,e,p)==v];assert len(exponents)==1
 return exponents[0]
phase_rows=[];Gamma=[(0,0),(0,0)];wrong=[(0,0),(0,0)];zeros=0
for v,w,u,n in rows:
 local=[raw(u,p['norm'],p['root']) for p in qprimes];qs=[p['norm'] for p,e in zip(qprimes,local) if e is None]
 # Independent nonprincipal certificate: exponent1 at the first-factor prime AND an explicit surviving raw Frobenius value !=1.
 fs1=factor(v);fs2=factor(w);assert fs1 and set(fs1).isdisjoint(fs2) and all(fs1.count(pi)==1 for pi in fs1)
 witness=None
 for pi in primegens:
  p=norm(pi)
  if p>100 or not prime(p):continue
  root=(-pi[0]*pow(pi[1],-1,p))%p;e=raw(u,p,root)
  if e not in (None,0):witness={'prime_generator':pi,'norm':p,'root':root,'raw_exponent':e};break
 assert witness is not None
 for j,(ids,other,nm,nn) in enumerate(orient):
  if any(e is None for e in local):zeros+=1;value=None
  else:
   e=(sum(local[i] for i in ids)-sum(local[i] for i in other))%6;value=PH[e];Gamma[j]=add(Gamma[j],value)
  ew=(sum(local[i] or 0 for i in ids)-sum(local[i] or 0 for i in other))%6;wrong[j]=add(wrong[j],PH[ew])
 phase_rows.append({'v1':v,'v2':w,'u':u,'N':n,'v1_prime_factors':fs1,'v2_prime_factors':fs2,'q_raw_exponents':local,'raw_collision_prime_norms':qs,'nonprincipal_witness':witness})
assert zeros==12 and Gamma==[(-4,-2),(-2,2)] and wrong==[(-6,-1),(-5,1)]
assert [list(g) for g in Gamma]==block['Gamma_omega'] and [list(g) for g in wrong]==block['wrong_restored_zero_Gamma_omega']
mean=(Fraction(sum(g[0] for g in Gamma),2),Fraction(sum(g[1] for g in Gamma),2));assert mean==(Fraction(-3),Fraction(0))
centered=[(Fraction(g[0])-mean[0],Fraction(g[1])-mean[1]) for g in Gamma];assert (sum(v[0] for v in centered),sum(v[1] for v in centered))==(0,0)
parts={}
for X,Y in [('C','C'),('C','mu'),('mu','C'),('mu','mu'),('A','A')]:
 total=(0,0)
 for j,(ids,other,nm,nn) in enumerate(orient):
  m=columns[nm];n=columns[nn];weight=m[X]*n[Y];total=add(total,(weight*Gamma[j][0],weight*Gamma[j][1]))
 parts[X+'_'+Y]=total
assert parts=={'C_C':(0,0),'C_mu':(4,-4),'mu_C':(8,4),'mu_mu':(6,0),'A_A':(-6,0)}
AA=(Fraction(parts['A_A'][0],D),Fraction(parts['A_A'][1],D));assert AA==(Fraction(-1,10000),0)
# A single fixed smooth profile: selected rational nodes lie strictly within its constant-one plateau.
profile_nodes={str(n):{'y':str(Fraction(n,D)),'left_plateau_margin':str(Fraction(n,D)-Fraction(9,8)),'right_plateau_margin':str(Fraction(15,8)-Fraction(n,D))} for n in columns};assert all(Fraction(9,8)<Fraction(n,D)<Fraction(15,8) for n in columns)
assert all(sha(R/p)==h for p,h in pins.items())
result={'passed':True,'scope':'Independent finite reconstruction of blocks[1] actual20-row selected-q diagnostic ONLY; no old700/fixtures imported or run, no full-family/asymptotic claim.','parameters':{'D':D,'U':U,'H':H,'A1':37,'A2':7,'nu':1,'literal_unit':1,'fixed_other_ideal_factors':[1,1,1,1]},'complete_ideal_enumeration':{'v1_candidates':v1s,'v2_candidates':v2s,'candidate_pairs':len(v1s)*len(v2s),'rejections':dict(rejections),'rows':len(rows),'coordinate_completeness':'N(a+bω)>=3a²/4 and>=3b²/4; finite enumeration bounds use this inequality.'},'selected_q':{'Q':Q,'prime_ideals':qprimes,'complete_annular_orientations':orient},'columns':columns,'all20_rows':phase_rows,'all20_nonprincipal':True,'row_value_methods':'Prime-ideal valuations from independent exact factorization; explicit nontrivial raw Frobenius witness for every row; selected-q symbols from finite-field powers with literal epsilon embedding.','Gamma_omega':Gamma,'Gamma_mean_omega':[str(x) for x in mean],'raw_zero_orientation_row_pairs':zeros,'raw_zero_rows':zeros//2,'wrong_restored_zero_Gamma_omega':wrong,'signed_components_before_D':parts,'actual_h1_AA_omega':[str(x) for x in AA],'centered_only_omega':['0','0'],'fixed_profile_nodes':profile_nodes,'fixed_profile_validity':'The displayed smoothstep formula has no D parameter; it is C∞ on positive reals, supported[1,2], identically1 on[9/8,15/8]. This agrees with the source profile class. Other norm nodes/columns generally remain active.','input_sha256':pins,'checker_sha256':sha(Path(__file__)),'limitations':['One selected q and one literal unit class, not the full q/h1/energy family.','Negative off-diagonal selected-q value is not negative row energy.','Finite block sizes do not prove asymptotic endpoint behavior, an obstruction to the fixed-W target, or an exponent saving.','This review does not audit the separate analytic budget in ACTUAL_SIGNED_BUDGET-v1.md.']}
output=O/'independent-diagnostic-v1.json'
with output.open('x') as f:json.dump(result,f,indent=2);f.write('\n')
print(json.dumps({'passed':True,'rows':len(rows),'all_nonprincipal':True,'Gamma':Gamma,'mean':list(map(str,mean)),'rawzero_pairs':zeros,'AA':list(map(str,AA)),'output':str(output),'sha256':sha(output)},indent=2))
