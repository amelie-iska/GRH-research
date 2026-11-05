"""Independent exact covariance proof checks; no attempt/project imports."""
from pathlib import Path
from fractions import Fraction as F
from math import isqrt
from collections import Counter
import hashlib,json,argparse
ROOT=Path(__file__).resolve().parents[3]
ONE=(1,0);Z=(0,0)
def times(z,t):return z[0]*t[0]-z[1]*t[1],z[0]*t[1]+z[1]*t[0]-z[1]*t[1]
def plus(z,t):return z[0]+t[0],z[1]+t[1]
def bar(z):return z[0]-z[1],-z[1]
def N(z):return z[0]**2-z[0]*z[1]+z[1]**2
def re(z):return F(2*z[0]-z[1],2)
def exp(z,n,mod=None):
 t=ONE
 while n:
  if n%2:
   t=times(t,z)
   if mod:t=tuple(x%mod for x in t)
  z=times(z,z)
  if mod:z=tuple(x%mod for x in z)
  n//=2
 return t
def quotient(z,t):
 a,b=times(z,bar(t));n=N(t)
 return (a//n,b//n) if a%n==b%n==0 else None
def isprime(n):return n>1 and all(n%d for d in range(2,isqrt(n)+1))
def enumerate_ideals(bound):
 # N(a+bw)>=(a²+b²)/2; this square encloses the full norm disk.
 L=isqrt(2*bound)+1
 return sorted(((a,b) for a in range(-L,L+1) for b in range(-L,L+1)
  if a%3==1 and b%3==0 and N((a,b))<=bound and N((a,b))>0 and N((a,b))%6 in (1,5)),key=lambda z:(N(z),z))
units=tuple(exp((1,1),i) for i in range(6))
def get_primes(gs):
 return [z for z in gs if isprime(N(z)) or (z[1]==0 and isprime(abs(z[0])) and abs(z[0])%3==2)]
def factor(z,ps):
 result=[];left=z
 for p in ps:
  if N(p)>N(left):break
  e=0
  while (q:=quotient(left,p)) is not None:left=q;e+=1
  if e:result.append((p,e))
 assert left==ONE
 return result

def local(p,z):
 q=N(p)
 if p[1]:
  root=(-p[0]*pow(p[1],-1,q))%q
  value=(z[0]+root*z[1])%q
  if value==0:return None
  power=pow(value,(q-1)//6,q)
  return [pow((1+root)%q,j,q) for j in range(6)].index(power)
 r=abs(p[0]);zz=(z[0]%r,z[1]%r)
 if zz==Z:return None
 power=exp(zz,(q-1)//6,r)
 return [exp((1,1),j,r) for j in range(6)].index(power)
def sym(factors,z):
 power=0
 for p,e in factors:
  index=local(p,z)
  if index is None:return Z
  power+=e*index
 return units[power%6]

def sqrt_decomp(n):
 if not n:return {}
 coeff=1;rad=1;p=2
 while p*p<=n:
  count=0
  while n%p==0:n//=p;count+=1
  coeff*=p**(count//2)
  if count%2:rad*=p
  p+=1
 rad*=n
 return {rad:F(coeff)}
def radical_add(total,values,scale=F(1)):
 for key,value in values.items():
  total[key]=total.get(key,F())+scale*value
  if not total[key]:del total[key]
 return total

def main(output):
 if output.exists():raise FileExistsError('Preserve earlier independent review')
 attempt=ROOT/'planning/covariance-budget-20261105/attempt'
 manifest=json.loads((attempt/'manifest-v1.json').read_text())
 hashes={}
 for name,h in manifest['source_sha256'].items():
  actual=hashlib.sha256((ROOT/name).read_bytes()).hexdigest();assert actual==h;hashes[name]=actual
 report=json.loads((ROOT/'outputs/checks/2026-11-05-covariance-budget/attempt/exact-v2/exact-budget.json').read_text())
 gs=enumerate_ideals(10000);ps=get_primes(gs);facts={z:factor(z,ps) for z in gs}
 sf=[z for z in gs if all(e==1 for p,e in facts[z])]
 mu=lambda z:(-1)**len(facts[z])
 checks=0;moment_results=[]
 for case in report['moment_cases']:
  D,U=case['D'],case['U'];cols=[m for m in sf if D<=N(m)<=2*D]
  counts=[];hist=Counter();dyad=Counter();quads=0
  candidates=[a for a in gs if U<N(a) and N(a)*U<2*D]
  for m in cols:
   fps=[]
   for a in candidates:
    b=quotient(m,a)
    if b is not None and N(b)>U:fps.append((a,b))
   r=len(fps);counts.append(r);hist[r]+=1
   for a,b in fps:
    for c,d in fps:
     g=ONE
     for p,e in facts[m]:
      if quotient(a,p) is not None and quotient(c,p) is not None:g=times(g,p)
     h=quotient(a,g);k=quotient(c,g);ell=quotient(b,k)
     assert times(h,ell)==d and times(times(g,h),times(k,ell))==m
     M=max(N(h),N(k))
     assert N(g)*M*U<2*D and N(ell)*M*U<2*D
     dyad[M.bit_length()-1]+=1;quads+=1;checks+=3
  assert len(cols)==case['columns'] and sum(counts)==case['sum_r'] and sum(r*r for r in counts)==case['sum_r_squared'];checks+=3
  assert {str(k):v for k,v in hist.items()}==case['r_histogram'];checks+=1
  assert {str(k):v for k,v in dyad.items()}==case['quadruple_dyadic_counts'];checks+=1
  moment_results.append({'D':D,'U':U,'columns':len(cols),'sum_r_squared':quads,'dyadic_ranges':len(dyad)})
 def gram_check(name,D,U,cols,rows,nu_num,weights):
  nonlocal checks
  target=next(c for c in report['Gram_cases'] if c['name']==name and c['U']==U and c['nu_numerator']==list(nu_num))
  r=[]
  for m in cols:
   r.append(sum(1 for a in gs if U<N(a) and N(a)*U<2*D and (b:=quotient(m,a)) is not None and N(b)>U))
  lambdas=[times((mu(m),0),times(sym(facts[m],nu_num),weights[N(m)])) for m in cols]
  table=[[sym(facts[m],u) for m in cols] for u in rows]
  G=[]
  for i,m in enumerate(cols):
   gg=[]
   for j,n in enumerate(cols):
    total=Z
    for row in table:total=plus(total,times(row[i],bar(row[j])))
    gg.append(total)
   G.append(gg)
  cov=F();EA=F();EC=F();EM=F();positive={};comm={};Bfix={};vanish=cross=0
  for i,m in enumerate(cols):
   assert sym(facts[m],units[1])==units[((N(m)-1)//6)%6];checks+=1
   for j,n in enumerate(cols):
    assert G[j][i]==bar(G[i][j]);checks+=1
    if N(m)%36!=N(n)%36:assert G[i][j]==Z;vanish+=1;checks+=1
    if r[i]!=r[j] and G[i][j]!=Z:cross+=1
    value=re(times(times(lambdas[i],bar(lambdas[j])),G[i][j]))/D
    cov+=r[i]*value;EA+=(r[i]-1)*(r[j]-1)*value;EC+=r[i]*r[j]*value;EM+=value
    sr=sqrt_decomp(r[i]*r[j]);delta={1:F(r[i]+r[j])} if r[i]+r[j] else {}
    radical_add(delta,sr,F(-2))
    radical_add(positive,sr,value);radical_add(comm,delta,value);radical_add(Bfix,delta,abs(value)/2)
  identity=dict(positive);radical_add(identity,comm,F(1,2))
  assert identity==({1:cov} if cov else {}) and EA==EC+EM-2*cov;checks+=2
  assert cov==F(target['real_covariance']) and EA==F(target['energy_A']) and EC==F(target['energy_C']) and EM==F(target['energy_mu']);checks+=4
  assert positive=={int(k):F(v) for k,v in target['positive_S_energy'].items()};checks+=1
  assert comm=={int(k):F(v) for k,v in target['double_commutator_quadratic'].items()};checks+=1
  assert Bfix=={int(k):F(v) for k,v in target['coefficient_adapted_budget'].items()};checks+=1
  rawzeros=sum(z==Z for row in table for z in row)
  assert vanish==target['unit_class_vanishing_pairs'] and cross==target['nonzero_cross_level_pairs'] and rawzeros==target['raw_zero_entries'];checks+=3
  moments=[sum((F(ri**j)*N(lam) for ri,lam in zip(r,lambdas)),F()) for j in range(3)]
  assert moments==[F(s) for s in target['weighted_moments']];checks+=1
  trace=sum(G[i][i][0] for i in range(len(cols)))
  ceilroot=lambda n:isqrt(n)+(isqrt(n)**2!=n)
  lam=min(trace,max(sum(ceilroot(N(z)) for z in row) for row in G))
  assert lam==target['Gram_psd_upper_bound'];checks+=1
  if lam:
   rhs=moments[1]-2*D*cov/lam
   assert rhs<=0 or moments[0]*moments[2]>=rhs*rhs;checks+=1
  return {'name':name,'columns':len(cols),'rows':len(rows),'phase_values':len(cols)*len(rows),'raw_zero_entries':rawzeros,'covariance':str(cov)}
 small=[p for p in ps if 7<=N(p)<14]
 rows=[times(e,times(a,exp(b,2))) for a in small for b in small if a!=b for e in units]
 assert len(rows)==len(set(rows))==72;checks+=1
 broad=[m for m in sf if 400<=N(m)<=800]
 weights={N(m):(F((N(m)-400)*(800-N(m)),400**2),F()) for m in broad}
 fixtures=[gram_check('all_annular_columns_B7',400,17,broad,rows,(2,0),weights)]
 four=[m for m in sf if N(m) in (439,475)]
 fixtures.append(gram_check('accepted_smooth_four_column_x10',400,17,four,rows,ONE,{439:(F(10),F()),475:(F(1),F())}))
 pp=next(N(p) for p in ps if 5000<N(p)<10000 and N(p)%36==1)
 cols=[m for m in sf if N(m) in (pp,5977,8281)]
 rows=[times(e,times(a,exp(b,2))) for a in ps if N(a)==19 for b in ps if N(b)==31 for e in units]
 weights={q:(F(1+q%5,3),F(q%3,4)) for q in (pp,5977,8281)}
 fixtures.append(gram_check('three_count_levels_complex_common_profile',5000,40,cols,rows,(2,0),weights))
 # Exact sharpness fixture: v=(3,4), R=diag(0,1), G=7P_neg, D=11.
 G=[[F(63,10),F(-21,10)],[F(-21,10),F(7,10)]];v=(F(3),F(4));rv=(F(),F(4))
 assert all(sum(G[i][k]*G[k][j] for k in range(2))==7*G[i][j] for i in range(2) for j in range(2));checks+=4
 cov=sum(v[i]*G[i][j]*rv[j] for i in range(2) for j in range(2))/11
 assert cov==F(-14,11)==-F(7,22)*(20-16);checks+=1
 # Exhaustive weighted exponent compositions, enumerated recursively.
 exponent=[]
 def walk(xs,left):
  j=len(xs)+1
  if j==7:exponent.append(tuple(xs));return
  for a in range(left//j+1):walk(xs+[a],left-j*a)
 walk([],12);saturation=[]
 for xs in exponent:
  cost=sum((j+1)*x for j,x in enumerate(xs));slack=12-3*(sum(xs)-max(xs[:2]))
  branch=(xs[0]-xs[1] if xs[0]>=xs[1] else 2*(xs[1]-xs[0]))+xs[3]+2*xs[4]+3*xs[5]
  assert slack==12-cost+branch and slack>=0;checks+=2
  if slack==0:saturation.append(xs)
 assert len(exponent)==227 and set(saturation)=={(t,t,4-t,0,0,0) for t in range(5)};checks+=2
 # Bind final review to the exact manuscript and report bytes inspected.
 for name,h in hashes.items():assert hashlib.sha256((ROOT/name).read_bytes()).hexdigest()==h
 result={'status':'passed','checks':checks,'source_sha256':hashes,'independent_checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'moment_cases':moment_results,'Gram_cases':fixtures,'sharpness_fixture_covariance':str(cov),'exponent_cases':len(exponent),'saturating_face_points':saturation,'scope':'Finite independent exact reconstruction supports informal mathematical review; no attempt imports, no Lean, no new analytic exponent or GRH.'}
 output.mkdir(parents=True)
 (output/'independent-review.json').write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps({k:result[k] for k in ('status','checks','sharpness_fixture_covariance','exponent_cases','saturating_face_points')}))
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--output',type=Path,required=True);main(p.parse_args().output)
