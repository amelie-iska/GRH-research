"""Fresh independent exact unit/sixth-power-row/selected h1 checks. No project imports."""
from pathlib import Path
from itertools import product
from fractions import Fraction as F
from functools import lru_cache
import json,math
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'outputs/checks/2026-11-05-signed-profile/review-design'
D=400;U=20;X=80
norm=lambda z:z[0]*z[0]-z[0]*z[1]+z[1]*z[1]
def mul(z,w):
 a,b=z;c,d=w;return a*c-b*d,a*d+b*c-b*d
def power(z,n):
 out=(1,0)
 while n:
  if n&1:out=mul(out,z)
  z=mul(z,z);n//=2
 return out
units=[power((1,1),j) for j in range(6)]
canonical=lambda z:min(mul(z,e) for e in units)
def prime(p):return p>=2 and all(p%d for d in range(2,math.isqrt(p)+1))
ps=[]
for p in range(5,2*D+1):
 if not prime(p):continue
 if p%3==1:
  roots=[x for x in range(p) if (x*x+x+1)%p==0]
  ps.extend([((p,i),p,root) for i,root in enumerate(roots)])
 elif p*p<=2*D:ps.append(((p,0),p*p,None))
columns=[(1,())]
for key,n,root in ps:columns.extend((a*n,fs+((key,n,root),)) for a,fs in tuple(columns) if a*n<2*D)
columns=[(n,fs) for n,fs in columns if D<n<2*D]
def actual_A(fs):
 total=0
 for bits in product(range(3),repeat=len(fs)):
  a=b=1;s=1
  for bit,(key,n,root) in zip(bits,fs):
   if bit==1:a*=n;s=-s
   if bit==2:b*=n;s=-s
  if a<=U and b<=U:total+=s
 return total
@lru_cache(None)
def local_phase(key,q,root,z):
 p=key[0]
 if root is not None:
  residue=(z[0]+z[1]*root)%p
  if not residue:return None
  zeta=(1+root)%p;value=pow(residue,(q-1)//6,p);return [pow(zeta,j,p) for j in range(6)].index(value)
 def fp_mul(a,b):return tuple(v%p for v in mul(a,b))
 def fp_power(a,n):
  out=(1,0)
  while n:
   if n&1:out=fp_mul(out,a)
   a=fp_mul(a,a);n//=2
  return out
 residue=(z[0]%p,z[1]%p)
 if residue==(0,0):return None
 value=fp_power(residue,(q-1)//6);return [fp_power((1,1),j) for j in range(6)].index(value)
phase_checks=0
for n,fs in columns:
 exponent=sum(local_phase(key,q,root,(1,1)) for key,q,root in fs)%6
 assert exponent==((n-1)//6)%6
 phase_checks+=1
assert local_phase((7,0),7,2,(1,1))==1
assert all((j%6)!=0 for j in range(1,6))
vset={canonical((a,b)) for a in range(-20,21) for b in range(-20,21) if 0<norm((a,b))<=X and math.gcd(norm((a,b)),6)==1}
vs=sorted(z for z in vset if F(X,2)<=norm(z)<=X)
assert len([z for z in vs if norm(z)==49])==3,'Arbitrary v includes both prime squares and split product'
rows=[];total_h1=F(0);total_energy=F(0);triples=0;raw_checks=0
for beta in vs:
 u=mul((1,1),power(beta,6));assert norm(u)==norm(beta)**6
 values=[];supports=[]
 for n,fs in columns:
  phases=[local_phase(key,q,root,u) for key,q,root in fs];beta_phases=[local_phase(key,q,root,beta) for key,q,root in fs]
  actual=None if None in phases else sum(phases)%6
  expected=None if None in beta_phases else ((n-1)//6)%6
  assert actual==expected;raw_checks+=1
  A=actual_A(fs);assert A
  # W_N phase is conjugate(unit phase), times sign(A).
  weight_phase=(-((n-1)//6)+(0 if A>0 else 3))%6
  aligned=0 if actual is None else A*(1 if (actual+weight_phase)%6==0 else -1 if (actual+weight_phase)%6==3 else 10**9)
  assert aligned in [0,abs(A)];values.append(aligned);supports.append({key for key,q,root in fs})
 s=sum(values);energy=F(s*s,D);h1=F(0);count=0
 for i,a in enumerate(values):
  for j,b in enumerate(values):
   if a and b and supports[i].isdisjoint(supports[j]):h1+=F(a*b,D);count+=1
 assert energy>=h1>=F(count,D);total_h1+=h1;total_energy+=energy;triples+=count;rows.append(dict(v=beta,Nv=norm(beta),u=u,Nu=norm(u),energy=str(energy),selected_h1=str(h1),coprime_pairs=count))
assert len({tuple(r['u']) for r in rows})==len(rows)
# Exact local Euler factor identity, with v arbitrary rather than squarefree.
factors=[]
for q in [4,7,13,19,25,31,49,121]:
 t=F(1,q);f=(1-t)**3*(1+2*t+t/(1-t));assert f==1-5*t*t+6*t**3-2*t**4;assert f>0;factors.append(dict(q=q,value=str(f)))
report=dict(passed=True,D=D,U=U,X=X,columns=len(columns),selected_arbitrary_ideal_rows=len(rows),unit_phase_checks=phase_checks,actual_raw_sixth_power_checks=raw_checks,all_rows_norm_at_most_H=X**6,selected_h1_total=str(total_h1),selected_energy_total=str(total_energy),unweighted_coprime_triples=triples,triple_count_over_D=str(F(triples,D)),rows=rows,local_factors=factors,scope='Independent finite exact validation of raw zeta6 convention, arbitrary overlapping sixth-power masks, alignment and selected-h1 positivity; universal proof/counting asymptotic are separate.')
(OUT/'upgrade-checks.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({k:v for k,v in report.items() if k not in ['rows','local_factors']}))
