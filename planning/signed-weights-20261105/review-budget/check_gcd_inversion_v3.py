"""Independent NEW gcd inversion controls; no author module or old tables."""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
from math import isqrt,prod
import json,hashlib,subprocess
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'outputs/checks/2026-11-05-signed-weights/review-budget'
D=40000;U=200;PS=[7,13,19,31,37,43,211,223]
zero=(F(0),F(0));one=(F(1),F(0))
def add(x,y):return(x[0]+y[0],x[1]+y[1])
def mul(x,y):return(x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0]-x[1]*y[1])
def conj(x):return(x[0]-x[1],-x[1])
def scale(c,x):return(c*x[0],c*x[1])
def power(x,n):
 y=one
 for _ in range(n):y=mul(y,x)
 return y
def total(xs):
 y=zero
 for x in xs:y=add(y,x)
 return y
EPS=(F(1),F(1));UNITS=[power(EPS,j)for j in range(6)];ws=[];pis=[]
for p in PS:
 w=next(w for w in range(p)if(w*w+w+1)%p==0);ws.append(w);r=2*isqrt(p)+2
 choices=[(F(a),F(b))for a in range(-r,r+1)for b in range(-r,r+1)if a*a-a*b+b*b==p and(a+b*w)%p==0 and a%3==1 and b%3==0];assert len(choices)==1;pis.append(choices[0])
def chi(i,u):
 p=PS[i];z=int(u[0]+u[1]*ws[i])%p
 if z==0:return zero
 v=pow(z,(p-1)//6,p);roots=[int(a+b*ws[i])%p for a,b in UNITS];assert len(set(roots))==6
 return UNITS[roots.index(v)]
def chiset(s,u):
 y=one
 for i in s:y=mul(y,chi(i,u))
 return y
def norm(s):return prod(PS[i]for i in s)
def mu(s):return(-1)**len(s)
def nu(s):return(-1)**((norm(s)-1)//2)
def A(s):
 ans=0;ss=sorted(s)
 for places in product(range(3),repeat=len(ss)):
  a=prod(PS[i]for i,t in zip(ss,places)if t==0);b=prod(PS[i]for i,t in zip(ss,places)if t==1)
  if a<=U and b<=U:ans+=(-1)**sum(t!=2 for t in places)
 return ans
def X(kind,s):return A(s)if kind=='A'else mu(s)if kind=='mu'else A(s)+mu(s)
COLS=[frozenset(s)for s in [(0,1,2,3),(0,1,2,4),(0,1,2,5),(6,7)]]
assert all(D<norm(s)<2*D for s in COLS)
# One fixed C-infinity plateau times(1+omega*y) gives these exact complex values.
def W(s):return(F(1),F(norm(s),D))
ROWS=[EPS,pis[3],power(pis[4],2),power(pis[0],2),pis[6],mul(mul(pis[0],pis[1]),pis[2])]
DIVS=sorted({frozenset(i for i,b in zip(sorted(s),mask)if b)for s in COLS for mask in product([0,1],repeat=len(s))},key=lambda s:(len(s),tuple(sorted(s))))
def coeff(kind,s):return scale(X(kind,s)*nu(s),W(s))
def direct(k,l):return total(mul(mul(coeff(k,s),conj(coeff(l,t))),mul(chiset(s,u),conj(chiset(t,u))))for u in ROWS for s in COLS for t in COLS if not s&t)
def Td(k,d,u,factor=False):return total(scale(nu(s-d)*(X(k,d)*X(k,s-d)if factor else X(k,s)),mul(W(s),chiset(s-d,u)))for s in COLS if d<=s)
def inverted(k,l,mask=True,sign=True,factor=False):
 return total(scale(mu(d)if sign else 1,mul(Td(k,d,u,factor),conj(Td(l,d,u,factor))))for d in DIVS for u in ROWS if not mask or chiset(d,u)!=zero)
vals={};checks=0
for k,l in product(['A','C','mu'],repeat=2):
 a=direct(k,l);b=inverted(k,l);assert a==b;(vals.update({k+'-'+l:[str(v/D)for v in a]}));checks+=1
for d in DIVS:
 g=total(mul(Td('A',d,u),conj(Td('A',d,u)))for u in ROWS if chiset(d,u)!=zero);assert g[1]==0 and g[0]>=0;checks+=1
assert inverted('A','A',mask=False)!=direct('A','A');checks+=1
assert inverted('A','A',sign=False)!=direct('A','A');checks+=1
assert any(Td('A',d,u,True)!=Td('A',d,u)for d in DIVS for u in ROWS);checks+=1
# Every d=m has L<1 and exactly the surviving unit c=1.
for m in COLS:
 assert F(1,2)<F(D,norm(m))<1 and sum(m<=s for s in COLS)==1;checks+=1
witness=(COLS[0],frozenset([0]));assert X('A',witness[0])!=X('A',witness[1])*X('A',witness[0]-witness[1]);checks+=1
report=dict(passed=True,assertions=checks,D=D,U=U,prime_norms=PS,prime_primary_generators=[[int(a),int(b)]for a,b in pis],column_norms=[norm(s)for s in COLS],rows=[[int(a),int(b)]for a,b in ROWS],nu='norm quadratic character modulo4; S above2,3',W='one fixed smooth plateau on[1.1,1.9] times(1+omega*y); all columns in plateau',actual_A=[A(s)for s in COLS],exact_signed_slices=vals,negative_controls=['omit raw(d,u)mask','omit mu(d)sign','factor actual X(dc) intoX(d)X(c)'],endpoint_d_over_D=[str(F(norm(s),D))for s in COLS],scope='NEW exact gcd-inversion diagnostic and boundary cases; no phase/old table rerun or analytic saving',checker_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
with(OUT/'exact-gcd-inversion-v1.json').open('x')as f:json.dump(report,f,indent=2);f.write('\n')
print(json.dumps(dict(passed=True,assertions=checks,column_norms=report['column_norms'],actual_A=report['actual_A'],negative_controls=3,endpoint_cases=4)))
