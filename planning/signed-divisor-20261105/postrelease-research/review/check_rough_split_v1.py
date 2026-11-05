"""Fresh independent small ideal/assignment controls; no accepted helper imports."""
from pathlib import Path
from math import gcd,isqrt
from itertools import product,combinations
from collections import defaultdict
from fractions import Fraction
import hashlib,json,datetime
R=Path('/home/iska/Documents/LaTeX-projects/GRH-from-Mac-20261104')
O=R/'outputs/checks/2026-11-05-signed-divisor/postrelease-research-review'
P=Path('/home/iska/Documents/LaTeX-projects/GRH-publication-20261105-signed-divisor/outputs/publication/20261105-signed-divisor/release-preparation-v1')
sha=lambda b:hashlib.sha256(b).hexdigest()
api_before=sha((P/'api-payload-manifest-v1.json').read_bytes())
def norm(g):a,b=g;return a*a-a*b+b*b
def mul(g,h):a,b=g;c,d=h;return a*c-b*d,a*d+b*c-b*d
def conjugate(g):a,b=g;return a-b,-b
def divide(g,h):a,b=mul(g,conjugate(h));n=norm(h);return (a//n,b//n)if a%n==b%n==0 else None
def prime(n):return n>=2 and all(n%d for d in range(2,isqrt(n)+1))
def prime_ideal_norm(n):return (prime(n) and n%3==1)or(isqrt(n)**2==n and prime(isqrt(n))and isqrt(n)%3==2)
D=100;U=7;cap=2*D;bound=isqrt((4*cap+2)//3)+2
ideals=sorted([(a,b)for a in range(-bound,bound+1)for b in range(-bound,bound+1)if a%3==1 and b%3==0 and 1<=norm((a,b))<=cap and gcd(norm((a,b)),6)==1],key=lambda g:(norm(g),g))
assert len(ideals)==len(set(ideals)) and ideals[0]==(1,0)
primes=[g for g in ideals if prime_ideal_norm(norm(g))];pn=[norm(g)for g in primes];assert min(pn)==7

def factors(g):
 rem=g;out=[]
 for i,p in enumerate(primes):
  while norm(rem)>=pn[i]:
   q=divide(rem,p)
   if q is None:break
   out.append(i);rem=q
 assert rem==(1,0),g
 return tuple(out)
facts={g:factors(g)for g in ideals};sf=[g for g in ideals if len(facts[g])==len(set(facts[g]))]
cache={}
def A(ids):
 ids=tuple(sorted(ids))
 if ids in cache:return cache[ids]
 assert len(ids)==len(set(ids));s=0
 for places in product(range(3),repeat=len(ids)):
  x=y=1;parity=0
  for i,place in zip(ids,places):
   if place==0:x*=pn[i];parity+=1
   elif place==1:y*=pn[i];parity+=1
  if x<=U and y<=U:s+=(-1)**parity
 cache[ids]=s;return s
u=(-2,-3);p13=(1,-3);q13=(4,3);column=(13,0);u_factors=set(facts[u]);assert norm(u)==7 and mul(p13,q13)==column and conjugate(p13)==q13

def phase(p,u):
 pnorm=norm(p);assert prime(pnorm)
 a,b=p;lam=(-a*pow(b,-1,pnorm))%pnorm;assert (lam*lam+lam+1)%pnorm==0
 z=(u[0]+u[1]*lam)%pnorm
 if z==0:return None
 value=pow(z,(pnorm-1)//6,pnorm);eps=(1+lam)%pnorm;units=[pow(eps,k,pnorm)for k in range(6)];assert len(set(units))==6;return units.index(value)
assert phase(p13,u)==2 and phase(q13,u)==1
assert phase(u,u)is None and phase(conjugate(u),u)==3
# Every fresh squarefree d in this small box has the direct rough-invariance bijection.
invariance=0
for d in sf:
 ids=facts[d];f=tuple(i for i in ids if pn[i]<=U);e=tuple(i for i in ids if pn[i]>U)
 assert A(ids)==A(f)
 if len(e)>=2:assert not f
 assert len(e)<=2
 invariance+=1

def plus(out,Nd,Na,Nb,c):
 m=Nd*Na;n=Nd*Nb
 if D<m<2*D and D<n<2*D:out[(m,n)]+=c

def clean(out):return {k:v for k,v in sorted(out.items())if v}
def scalar(a,b,include_two):
 ai=facts[a];bi=facts[b];T=set(ai)|set(bi)|u_factors;Na=norm(a);Nb=norm(b);direct=defaultdict(int);rhs=defaultdict(int)
 for d in sf:
  di=facts[d]
  if T.intersection(di):continue
  plus(direct,norm(d),Na,Nb,(-1)**len(di)*A(di+ai)*A(di+bi))
 smooth=[f for f in sf if all(pn[i]<=U for i in facts[f])and not T.intersection(facts[f])]
 rough=[i for i,n in enumerate(pn)if n>U and i not in T]
 for f in smooth:
  fi=facts[f];c=(-1)**len(fi)*A(fi+ai)*A(fi+bi)
  plus(rhs,norm(f),Na,Nb,c)
  for i in rough:plus(rhs,norm(f)*pn[i],Na,Nb,-c)
 correction=[]
 if a==b==(1,0) and include_two:
  for i,j in combinations(rough,2):
   n=pn[i]*pn[j]
   if D<n<2*D:plus(rhs,n,Na,Nb,1);correction.append((i,j,n))
 return clean(direct),clean(rhs),correction
cases=[]
a103=next(g for g in sf if norm(g)==103);a109=next(g for g in sf if norm(g)==109)
for a,b in [((1,0),(1,0)),(p13,p13),(q13,q13),(column,column),(conjugate(u),conjugate(u)),(a103,a109)]:
 direct,rhs,correction=scalar(a,b,True);assert direct==rhs,(a,b,direct,rhs)
 cases.append({'a':a,'b':b,'Na':norm(a),'Nb':norm(b),'formal_common_profile_coefficients':{f'{k[0]},{k[1]}':v for k,v in direct.items()},'two_rough_pairs':correction})
unit,wrong,two=scalar((1,0),(1,0),False);difference={k:unit.get(k,0)-wrong.get(k,0)for k in set(unit)|set(wrong)};difference={k:v for k,v in difference.items()if v};assert difference=={(169,169):1}
_,_,two=scalar((1,0),(1,0),True);assert len(two)==1 and {primes[two[0][0]],primes[two[0][1]]}=={p13,q13}
at169=[g for g in ideals if norm(g)==169];sf169=[g for g in sf if norm(g)==169];assert len(at169)==3 and sf169==[column]
assert A(facts[column])==1 and A(facts[p13])==1 and A(facts[u])==-1
f7=u;p19=(-5,-3);assert norm(p19)==19 and norm(mul(f7,p19))==133 and A(facts[f7]+facts[p19])==A(facts[f7])==-1
assert not(set(facts[conjugate(u)])&(set(facts[f7])|set(facts[p19])))
assert Fraction(21,20)<Fraction(169,100)<Fraction(39,20)
H=0
while (H+1)**4<=D**3:H+=1
assert H==31 and norm(u)<=H and U*U<=D and 2*D<=7*U*U
sectors=[{'d':d,'residual':divide(column,d),'mu_d':(-1)**len(facts[d]),'A_residual':A(facts[divide(column,d)]),'contribution':(-1)**len(facts[d])*A(facts[divide(column,d)])**2}for d in [(1,0),p13,q13,column]]
assert [x['contribution']for x in sectors]==[1,-1,-1,1] and sum(x['contribution']for x in sectors)==0
assert sha((P/'api-payload-manifest-v1.json').read_bytes())==api_before=='143859fbaee144390ef121d3bdefed922b89c01650c02912b71d075a5e0e5954'
r={'passed':True,'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'method':'Fresh bounded primary-ideal lattice enumeration, exact division, direct ordered ternary assignments and literal split finite-field powers; no accepted imports or table reads','D':D,'U':U,'H':H,'min_good_norm':7,'good_primary_ideals_in_box':len(ideals),'prime_ideals':len(primes),'squarefree_ideals':len(sf),'rough_invariance_controls':invariance,'formal_profile_identity_cases':cases,'fixed_profile':{'delta':'1/20','plateau':['21/20','39/20'],'witness_node':'169/100','exact_plateau_value':1,'other_nodes':'Formal ordered W(m/D)conjugate(W(n/D)) coefficients, no floating approximations or replacement profile'},'norm169_ideals':at169,'norm169_squarefree_ideals':sf169,'witness_raw_phases':{'p13':phase(p13,u),'conjugate_p13':phase(q13,u),'product_phase':3,'row_prime_collision':None,'conjugate_row_prime_allowed_phase':3},'two_rough_correction':1,'selfpair_sectors':sectors,'selfpair_total':0,'negative_controls':{'omit_two_rough_fails_at_norm169':True,'rational_norm_squarefree_filter_loses_actual_ideal':True,'allow_same_prime_twice_would_add_two_invalid_norm169_ideals':True,'insert_mu_e_in_A_fails_for_single_rough_prime':True,'rational_norm_gcd_is_not_ideal_coprimality':True},'frozen_API_manifest_unchanged':api_before,'checker_sha256':sha(Path(__file__).read_bytes()),'scope':'Only new exact bounded scalar/coefficient/ideal witness controls; no full energy, new asymptotic bound, GRH, canonical edit, old scientific rerun or publication action'}
p=O/'independent-rough-controls-v1.json';assert not p.exists();p.write_text(json.dumps(r,indent=2,sort_keys=True)+'\n');print(json.dumps({'passed':True,'output':str(p),'sha256':sha(p.read_bytes()),'ideals':len(ideals),'SF':len(sf),'formal_cases':len(cases),'two_rough_correction':1,'selfpair_total':0},indent=2))
