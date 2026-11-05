"""Fresh exact h1 fixed-profile/mean diagnostic; no author arithmetic imports."""
from pathlib import Path
from fractions import Fraction
from itertools import product
from math import isqrt
import hashlib,json
ROOT=Path(__file__).resolve().parents[3];HERE=Path(__file__).resolve().parent;OUT=ROOT/'outputs/checks/2026-11-05-signed-weights/joint-budget/fixed-profile-h1-v1.json'
assert not OUT.exists(),'Preserve all evidence';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
freeze=json.loads((HERE/'source-freeze-v1.json').read_text());assert sha(Path(__file__))==freeze['checker_sha256'];assert all(sha(ROOT/p)==h for p,h in freeze['source_sha256'].items())
def mul(z,w):a,b=z;c,d=w;return a*c-b*d,a*d+b*c-b*d
def power(z,k):
 a=(1,0)
 for _ in range(k):a=mul(a,z)
 return a
def norm(z):a,b=z;return a*a-a*b+b*b
z=(1,1);phase=[power(z,k) for k in range(6)]
def add(a,b):return a[0]+b[0],a[1]+b[1]
def conjugate(a):return a[0]-a[1],-a[1]
def scale(a,k):return a[0]*k,a[1]*k
def factors(n):
 f={};d=2
 while d*d<=n:
  while n%d==0:f[d]=f.get(d,0)+1;n//=d
  d+=1
 if n>1:f[n]=f.get(n,0)+1
 return f
def sf(z):
 for p,e in factors(norm(z)).items():
  if p in [2,3]:return False
  if p%3==2:
   if e!=2:return False
  elif e>2 or e==2 and not(z[0]%p==0 and z[1]%p==0):return False
 return True
def roots(p):return[t for t in range(p)if(t*t+t+1)%p==0]
def cp(a,b):
 for p in set(factors(norm(a)))&set(factors(norm(b))):
  if p%3==2:return False
  if any((a[0]+a[1]*t)%p==0 and(b[0]+b[1]*t)%p==0 for t in roots(p)):return False
 return True
# Unique good ideal generator1mod3. Complete tiny enumeration, not an old fixture.
ideals=sorted([(a,b)for a in range(-20,21)for b in range(-20,21)if a%3==1 and b%3==0 and 1<=norm((a,b))<74 and sf((a,b))],key=lambda a:(norm(a),a))
assert len(ideals)==len(set(ideals));D=60000;U=244;H=isqrt(isqrt(D**3));assert H==3833
ps=[37,43,61,307,313];assert all(factors(p)=={p:1}and p%3==1 for p in ps);lambdas={p:min(roots(p))for p in ps}
prod=lambda v:__import__('functools').reduce(lambda a,b:a*b,v,1)
def ru(v):
 n=prod(v);ds=[prod(v[i]for i in range(len(v))if mask>>i&1)for mask in range(1<<len(v))];return sum(d>U and n>U*d for d in ds)
def au(v):
 # Original ternary placements, not the high-window formula.
 result=0
 for choices in product(range(3),repeat=len(v)):
  a=prod(p for p,k in zip(v,choices)if k==1);b=prod(p for p,k in zip(v,choices)if k==2)
  if a<=U and b<=U:result+=(-1)**sum(k!=0 for k in choices)
 return result
def chi(u,v,drop_zeros=False):
 e=0
 for p in v:
  t=lambdas[p];val=(u[0]+u[1]*t)%p
  if not val:
   if drop_zeros:continue
   return None
  a=pow(val,(p-1)//6,p);epsilon=(1+t)%p;e+=next(k for k in range(6)if pow(epsilon,k,p)==a)
 return e%6
orient=[]
for mask in range(1<<len(ps)):
 m=[p for i,p in enumerate(ps)if mask>>i&1];n=[p for i,p in enumerate(ps)if not(mask>>i&1)]
 if D<=prod(m)<=2*D and D<=prod(n)<=2*D:
  A,B=au(m),au(n);r,s=ru(m),ru(n);assert A==(-1)**len(m)*(r-1)and B==(-1)**len(n)*(s-1)
  orient.append(dict(m=prod(m),n=prod(n),m_primes=m,n_primes=n,r_m=r,r_n=s,A_m=A,A_n=B,a=(r-1)*(s-1)))
assert len(orient)==2 and {(v['m'],v['n'])for v in orient}=={(97051,96091),(96091,97051)};assert all(v['A_m']==v['A_n']==1 and v['a']==-1 for v in orient)
blocks=[]
for A,B in [(13,13),(37,7)]:
 rows=[dict(v1=v,v2=w,u=mul(v,power(w,2)),N=norm(v)*norm(w)**2)for v in ideals for w in ideals if A<=norm(v)<2*A and B<=norm(w)<2*B and cp(v,w)and norm(v)*norm(w)**2<=H]
 assert rows and len({tuple(x['u'])for x in rows})==len(rows)
 gammas=[];wrong=[];rawzeros=0
 for o in orient:
  g=(0,0);bad=(0,0)
  for row in rows:
   a,b=chi(row['u'],o['m_primes']),chi(row['u'],o['n_primes'])
   if a is None or b is None:rawzeros+=1
   else:g=add(g,phase[(a-b)%6])
   a,b=chi(row['u'],o['m_primes'],True),chi(row['u'],o['n_primes'],True);bad=add(bad,phase[(a-b)%6])
  gammas.append(g);wrong.append(bad)
 assert gammas[1]==conjugate(gammas[0])
 mean=(Fraction(gammas[0][0]+gammas[1][0],2),Fraction(gammas[0][1]+gammas[1][1],2));centered=[(Fraction(a)-mean[0],Fraction(b)-mean[1])for a,b in gammas]
 signed=scale(add(*gammas),1);centered_pairing=(sum(-v[0]for v in centered)*-1,sum(-v[1]for v in centered)*-1);assert centered_pairing==(0,0)
 blocks.append({'A1':A,'A2':B,'all_rows_in_actual_block':rows,'literal_unit':1,'capacity_H':H,'row_count':len(rows),'Gamma_omega':gammas,'Gamma_mean_omega':[str(x)for x in mean],'mu_q':-1,'a_per_orientation':-1,'actual_AA_pairing_before_D':signed,'centered_only_pairing_before_D':[str(x)for x in centered_pairing],'actual_h1_over_D_omega':[str(Fraction(x,D))for x in signed],'wrong_restored_zero_Gamma_omega':wrong,'raw_zero_pair_evaluations':rawzeros,'scope':'Complete two-variable block for this fixed literal unit and fresh selected q; not the full q sum or an asymptotic experiment.'})
assert blocks[0]['row_count']==6 and blocks[1]['row_count']==20
assert any(any(x for x in b['actual_AA_pairing_before_D'])for b in blocks)
assert blocks[1]['raw_zero_pair_evaluations']>0 and blocks[1]['Gamma_omega']!=blocks[1]['wrong_restored_zero_Gamma_omega']
# Exponents of the proved gcd-Mobius budget.
def budget(a,b):
 R=a+b;M=max(a,b);x=[R,1+R-M,Fraction(2,3)+R-M/3];y=[Fraction(1),2*R];return {'R':str(R),'BGL_terms':list(map(str,x)),'ordinary_terms':list(map(str,y)),'minimum':str(min(max(x),max(y))),'required_cancellation_to_H':str(min(max(x),max(y))-Fraction(3,4))}
endpoints={'mixed':budget(Fraction(5,12),Fraction(1,6)),'pure':budget(Fraction(3,4),Fraction(0))};assert all(v['minimum']=='7/6'and v['required_cancellation_to_H']=='5/12'for v in endpoints.values())
record={'passed':True,'D':D,'U':U,'H':H,'fixed_common_profile':'W(y)=s(8(y-1))*s(8(2-y)), s(t)=exp(-1/t)/(exp(-1/t)+exp(-1/(1-t))) on0<t<1, extended0/1. Fixed support[1,2], plateau[9/8,15/8]; W=1 at both selected norm nodes.','q_prime_ideals':'(p,omega-lambda_p) with the explicitly stored roots; all good split ideals','lambdas':lambdas,'q_norm':prod(ps),'orientations':orient,'blocks':blocks,'endpoint_exponents':endpoints,'checker_sha256':sha(Path(__file__)),'source_freeze_sha256':sha(HERE/'source-freeze-v1.json'),'no_author_arithmetic_imports':True,'limitations':['fresh exact identities only','selected q, not full annulus family','fixed small finite row blocks, not asymptotic endpoint evidence','no new exponent or GRH claim']}
OUT.write_text(json.dumps(record,indent=2)+'\n');print(json.dumps({'passed':True,'receipt':str(OUT.relative_to(ROOT)),'sha256':sha(OUT),'blocks':[{'rows':x['row_count'],'Gamma':x['Gamma_omega'],'h1':x['actual_h1_over_D_omega'],'zeros':x['raw_zero_pair_evaluations']}for x in blocks]}))
