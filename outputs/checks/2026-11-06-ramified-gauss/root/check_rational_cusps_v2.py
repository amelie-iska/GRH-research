#!/usr/bin/env python3
"""New exact Eisenstein rational-cusp/group controls; not an FE or GRH checker."""
from pathlib import Path
from fractions import Fraction as F
from collections import deque
import itertools,json,hashlib
ROOT=Path('/home/iska/Documents/LaTeX-projects/GRH-from-Mac-20261104')
OUT=ROOT/'outputs/checks/2026-11-06-ramified-gauss/root/finite-cusp-v2'
OUT.mkdir(exist_ok=False)
Z=(0,0);O=(1,0);W=(0,1);LAM=(1,2)
def add(x,y):return(x[0]+y[0],x[1]+y[1])
def neg(x):return(-x[0],-x[1])
def sub(x,y):return add(x,neg(y))
def mul(x,y):return(x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0]-x[1]*y[1])
def norm(x):return x[0]*x[0]-x[0]*x[1]+x[1]*x[1]
def inv(x):
 n=norm(x);assert n
 return(F(x[0]-x[1],n),F(-x[1],n))
def div(x,y):return mul(x,inv(y))
def exact(x,y):
 v=div(x,y);assert all(a.denominator==1 for a in v),(x,y,v)
 return tuple(int(a) for a in v)
def power(x,n):
 a=O
 for _ in range(n):a=mul(a,x)
 return a
def canonical(x,m):
 v=div(x,m);q=tuple(a.numerator//a.denominator for a in v)
 return sub(x,mul(m,q))
def divrem(a,b):
 v=div(a,b);f=[x.numerator//x.denominator for x in v]
 qs=itertools.product(range(f[0]-1,f[0]+3),range(f[1]-1,f[1]+3))
 q=min(qs,key=lambda u:(norm(sub(a,mul(b,u))),u))
 rem=sub(a,mul(b,q));assert norm(rem)<norm(b)
 return q,rem
def egcd(a,b):
 x,y=O,Z
 while b!=Z:
  q,c=divrem(a,b);a,b=b,c;x,y=y,sub(x,mul(q,y))
 return a,x
def inverse_mod(a,m):
 if norm(m)==1:return Z
 g,x=egcd(a,m);assert norm(g)==1,(a,m,g)
 return canonical(mul(x,inv(g)),m)
def residues(m):
 n=int(norm(m));out={}
 for a in range(n):
  for b in range(n):
   v=canonical((a,b),m);out[v]=None
 assert len(out)==n,(m,len(out),n)
 return sorted(out)
I=(O,Z,Z,O)
P=(W,Z,Z,mul(W,W));T=(O,O,Z,O);E=(Z,neg(O),O,Z)
def mm(a,b):
 return(add(mul(a[0],b[0]),mul(a[1],b[2])),
        add(mul(a[0],b[1]),mul(a[1],b[3])),
        add(mul(a[2],b[0]),mul(a[3],b[2])),
        add(mul(a[2],b[1]),mul(a[3],b[3])))
def det(a):return sub(mul(a[0],a[3]),mul(a[1],a[2]))
def mi(a):assert det(a)==O;return(a[3],neg(a[1]),neg(a[2]),a[0])
def mod(a):return tuple((int(v[0])%3,int(v[1])%3) for v in a)
def U(x):return(O,x,Z,O)
def DIAG(x):return(x,Z,Z,inv(x))
def FR(x):return(Z,neg(inv(x)),x,Z)
def bfs(gens):
 lifts={mod(I):I};todo=deque([mod(I)])
 while todo:
  k=todo.popleft()
  for g in gens:
   v=mm(lifts[k],g);key=mod(v)
   if key not in lifts:lifts[key]=v;todo.append(key)
 return lifts
G=bfs([P,T,E]);H=bfs([T,E])
elts=list(itertools.product(range(3),repeat=2))
ALL={m for m in itertools.product(elts,repeat=4) if mod((det(m),Z,Z,O))[0]==O}
assert len(ALL)==648 and set(G)==ALL and len(H)==24
assert all(all(z[1]==0 for z in k) for k in H)
cosets={};reps=[]
for k in G:
 if k in cosets:continue
 j=len(reps);rep=G[k];reps.append(rep)
 c={mod(mm(h,k)) for h in H}
 assert len(c)==24 and not any(a in cosets for a in c)
 for a in c:cosets[a]=j
assert len(reps)==27 and len(cosets)==648
raw=[];count=0;fixed=0;wrong=0;denlower=0
levels=[O,(-2,-3),(1,-3),(-2,3)]
for f in [2,3,4]:
 B=f-2;q=power(LAM,B)
 for r in levels:
  for hh in residues(power(LAM,f)):
   for dd in residues(r):
    n=sub(mul(hh,r),mul(power(LAM,B+4),dd));den=mul(q,r)
    g,_=egcd(n,den);A=exact(n,g);C=exact(den,g)
    D=inverse_mod(A,C);b=exact(sub(mul(A,D),O),C)
    gamma=(A,b,C,D);assert det(gamma)==O
    frac=div(A,C);rhs=mm(mm(gamma,U(neg(div(D,C)))),mi(FR(C)))
    assert rhs==U(frac)
    j=cosets[mod(gamma)];gg=mm(gamma,mi(reps[j]));sig=H[mod(gg)]
    gamma0=mm(mi(sig),gg);assert mod(gamma0)==mod(I)
    assert norm(C)<=norm(den);denlower+=int(norm(C)<norm(den))
    unit_d=norm(egcd(dd,r)[0])==1
    affine=None
    if unit_d:
     c0=exact(C,r);bb=canonical(mul(D,inverse_mod(r,mul((9,0),c0))),mul((9,0),c0))
     cc=exact(sub(D,mul(bb,r)),mul((9,0),c0))
     base=mm(mm(gamma,U(neg(div(bb,c0)))),DIAG(inv(c0)))
     moving=neg(div(mul((9,0),mul(mul(c0,c0),cc)),r))
     correct=mm(base,U(moving));target=mm(U(frac),FR(r));assert correct==target
     bad=mm(base,U(neg(div(mul((9,0),cc),r))))
     wrong+=int(bad!=target);fixed+=1
     affine=[c0,bb,cc]
    raw.append([f,r,hh,dd,A,C,D,j,affine]);count+=1
def encode_exact_integer(v):
 assert isinstance(v,F) and v.denominator==1,repr(v)
 return v.numerator
data=OUT/'cases-v1.json';data.write_text(json.dumps(raw,separators=(',',':'),default=encode_exact_integer)+'\n')
summary=dict(passed=True,scope='NEW exact Z[omega] finite cusp geometry controls only. No Kubota symbol numerics, theta coefficients, analytic FE, original annular-family energies, training or Lean inferred.',material=dict(ring='Z[omega], omega^2+omega+1=0',lambda_value=LAM,ramified_f=[2,3,4],levels=levels,all_h_and_d_residues=True,randomness='none'),SL2_Omod3=648,integer_subgroup_mod3=24,left_cosets=27,rational_cases=count,unit_d_fixed_affine_cases=fixed,denominator_strict_reductions=denlower,wrong_diagonal_order_negative_controls=wrong,cases_sha256=hashlib.sha256(data.read_bytes()).hexdigest(),producer_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),own_coset_basis=[list(x) for x in reps],coset_numbering='Computed BFS basis, NOT Patterson j numbering; each matches a published state up to its actual fixed Kubota unit. No constant term is assigned numerically.',phase_policy='Exact phase remains chi(gamma0) from the pinned Kubota Jacobi formula. It is never set to1; geometry check does not evaluate it.')
assert wrong>0 and denlower>0
(OUT/'checks-v1.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps({k:summary[k] for k in ['passed','SL2_Omod3','integer_subgroup_mod3','left_cosets','rational_cases','unit_d_fixed_affine_cases','denominator_strict_reductions','wrong_diagonal_order_negative_controls']}))
