"""Independent complete-ideal/direct-pair checker; stdlib only, no accepted-checker imports."""
from pathlib import Path
from itertools import product
from math import isqrt
from functools import lru_cache
import json,hashlib
PH=((1,0),(1,1),(0,1),(-1,0),(-1,-1),(0,-1))
ZERO=(0,0)
def add(x,y):return x[0]+y[0],x[1]+y[1]
def mul(x,y):return x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0]-x[1]*y[1]
def conj(z):return z[0]-z[1],-z[1]
def norm(z):return z[0]*z[0]-z[0]*z[1]+z[1]*z[1]
def scale(z,k):return z[0]*k,z[1]*k
def quotient(z,w):
 a,b=mul(z,conj(w));n=norm(w)
 return (a//n,b//n)if a%n==b%n==0 else None
def prime(n):return n>=2 and all(n%d for d in range(2,isqrt(n)+1))
def primary(cap):
 bound=isqrt(4*cap//3)+1
 return sorted(((a,b)for a in range(-bound,bound+1)for b in range(-bound,bound+1)if a%3==1 and b%3==0 and 0<norm((a,b))<=cap and norm((a,b))%2 and norm((a,b))%3),key=lambda g:(norm(g),g))
def ideal_universe(cap):
 gs=primary(cap);ps=[g for g in gs if prime(norm(g)) or g[1]==0 and prime(abs(g[0])) and abs(g[0])%3==2]
 def factors(g):
  out=[];rem=g
  for pi in ps:
   while (q:=quotient(rem,pi))is not None:out.append(pi);rem=q
  assert rem==(1,0),(g,rem)
  return tuple(out)
 return [(g,factors(g))for g in gs]
def divisors(fs):
 out=[]
 for bits in product((0,1),repeat=len(fs)):
  ds=tuple(p for p,b in zip(fs,bits)if b);g=(1,0)
  for p in ds:g=mul(g,p)
  out.append((g,frozenset(ds),(-1)**len(ds)))
 return out
@lru_cache(None)
def local_phase(pi,u):
 Q=norm(pi);inert=pi[1]==0;p=abs(pi[0])if inert else Q
 root=None if inert else (-pi[0]*pow(pi[1],-1,p))%p
 def embed(z):return(z[0]%p,z[1]%p)if inert else((z[0]+z[1]*root)%p,0)
 def times(x,y):return embed(mul(x,y))
 x=embed(u)
 if x==ZERO:return None
 n=(Q-1)//6;v=(1,0)
 while n:
  if n%2:v=times(v,x)
  x=times(x,x);n//=2
 roots={embed(z):i for i,z in enumerate(PH)};assert len(roots)==6
 return roots[v]
def raw(fs,u):
 es=[local_phase(p,u)for p in fs]
 return ZERO if None in es else PH[sum(es)%6]
def original_coefficients(fs,U):
 ds=divisors(fs);A=C=0
 for a,fa,ma in ds:
  for b,fb,mb in ds:
   if fa&fb:continue
   if norm(a)<=U and norm(b)<=U:A+=ma*mb
   if norm(a)>U and norm(b)>U:C+=ma*mb
 mu=(-1)**len(fs);assert A==C-mu
 return(A,C,mu)
def reconstruct(D,U,H,A1):
 allideals=ideal_universe(2*D);sf=[(g,fs)for g,fs in allideals if len(fs)==len(set(fs))]
 cols=[{'g':g,'fs':fs,'x':original_coefficients(fs,U),'divisors':divisors(fs)}for g,fs in sf if D<norm(g)<2*D]
 rows=[g for g,fs in sf if A1<=norm(g)<2*A1 and norm(g)<=H]
 assert all(norm(g)>1 for g in rows),'Principal u=1 requires a separate residue label'
 all_div={d:mu for c in cols for d,fs,mu in c['divisors']};assert(1,0)in all_div
 chars=[[raw(c['fs'],u)for c in cols]for u in rows]
 gcdcounts={};gcdvalues={}
 for c in cols:
  for e in cols:
   fs=frozenset(c['fs'])&frozenset(e['fs']);gcdcounts[fs]=gcdcounts.get(fs,0)+1
 for fs in gcdcounts:gcdvalues[fs]=[[ZERO for y in range(3)]for x in range(3)]
 Z={d:[[ZERO for y in range(3)]for x in range(3)]for d in all_div};direct=[[ZERO for y in range(3)]for x in range(3)];perrow=[]
 for u,chi in zip(rows,chars):
  F={d:[ZERO,ZERO,ZERO]for d in all_div}
  for c,ch in zip(cols,chi):
   for d,fs,mu in c['divisors']:
    for x in range(3):F[d][x]=add(F[d][x],scale(ch,c['x'][x]))
  for d,values in F.items():
   assert values[0]==add(values[1],scale(values[2],-1))
   for x in range(3):
    for y in range(3):Z[d][x][y]=add(Z[d][x][y],mul(values[x],conj(values[y])))
  pair=[[ZERO for y in range(3)]for x in range(3)]
  for i,c in enumerate(cols):
   for j,e in enumerate(cols):
    common=frozenset(c['fs'])&frozenset(e['fs']);value=mul(chi[i],conj(chi[j]))
    for x in range(3):
     for y in range(3):
      term=scale(value,c['x'][x]*e['x'][y]);gcdvalues[common][x][y]=add(gcdvalues[common][x][y],term)
      if not common:pair[x][y]=add(pair[x][y],term)
  via=[[ZERO for y in range(3)]for x in range(3)]
  for d,values in F.items():
   for x in range(3):
    for y in range(3):via[x][y]=add(via[x][y],scale(mul(values[x],conj(values[y])),all_div[d]))
  assert via==pair,(D,u,via,pair)
  for x in range(3):
   for y in range(3):direct[x][y]=add(direct[x][y],pair[x][y])
  perrow.append({'u':u,'N':norm(u),'direct_pair':pair,'divisor_pair':via,'full_AA':norm(F[(1,0)][0]),'F':[{'d':d,'values':v}for d,v in F.items()]})
 signed=[[ZERO for y in range(3)]for x in range(3)]
 for d,values in Z.items():
  for x in range(3):
   for y in range(3):signed[x][y]=add(signed[x][y],scale(values[x][y],all_div[d]));assert values[y][x]==conj(values[x][y])
  assert values[0][0]==add(add(values[1][1],scale(values[1][2],-1)),add(scale(values[2][1],-1),values[2][2])) and values[0][0][1]==0 and values[0][0][0]>=0
 assert signed==direct and signed[0][0][1]==0
 # Exhaustive incidence/self-pair check independent of the row characters.
 pair_checks=0
 for c in cols:
  dc={d for d,fs,mu in c['divisors']}
  for e in cols:
   total=sum(mu for d,fs,mu in e['divisors']if d in dc);assert total==int(set(c['fs']).isdisjoint(e['fs']));pair_checks+=1
 return{'D':D,'U':U,'H':H,'A1':A1,'columns':[{k:v for k,v in c.items()if k!='divisors'}for c in cols],'rows':rows,'raw_character_values':chars,'divisors':[{'g':d,'mu':mu,'Z':Z[d]}for d,mu in sorted(all_div.items(),key=lambda x:(norm(x[0]),x[0]))],'direct_pair':direct,'signed_divisor_pair':signed,'full_pair':Z[(1,0)],'per_row_checks':perrow,'incidence_pair_checks':pair_checks,'gcd_classes':[{'prime_generators':sorted(fs),'ordered_pair_count':gcdcounts[fs],'contribution':values}for fs,values in gcdvalues.items()],'ideal_squarefree_with_nonsquarefree_norm':[c['g']for c in cols if any(norm(c['g'])%(p*p)==0 for p in range(2,isqrt(norm(c['g']))+1))]}
# No execution at import. The final driver is attached only after the author's case schema is frozen.
