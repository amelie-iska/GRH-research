from fractions import Fraction as F
from pathlib import Path
import json,math,time
ROOT=Path('/home/iska/Documents/LaTeX-projects/GRH-from-Mac-20261104')
Z=(F(),F());ONE=(F(1),F())
def add(a,b):return a[0]+b[0],a[1]+b[1]
def neg(a):return -a[0],-a[1]
def sub(a,b):return add(a,neg(b))
def mul(a,b):return a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0]
def scale(a,x):return a[0]*x,a[1]*x
def const(x):return F(x),F()
checks=0
for p in [const(0),const(1),const(-2),(F(1,3),F(2,7)),(F(-4,5),F(-2,3))]:
 for lm in [F(0),F(3,5),F(22,7),F(1240)]:
  for u in [F(1,9),F(1,15)]:
   J=28;rec=[ONE];prev=Z;current=ONE
   for j in range(J):
    nxt=scale(sub(scale(mul(sub(p,const(lm+j)),current),u),scale(prev,lm*u*u)),F(1,j+1));rec.append(nxt);prev,current=current,nxt
   binomial=[ONE]
   for j in range(1,J+1):binomial.append(scale(mul(binomial[-1],sub(p,const(j-1))),F(1,j)))
   for j in range(J+1):
    convolution=Z
    for k in range(j+1):convolution=add(convolution,scale(binomial[j-k],(-lm*u)**k/F(math.factorial(k))*u**(j-k)))
    assert rec[j]==convolution;(checks:=checks+1)
report={'passed':True,'checks':checks,'cases':40,'maximum_degree':28,'method':'Exact Fraction complex coefficient recurrence versus independent generalized-binomial/exponential convolution','scope':'Finite exact algebra checks supplement the general coefficient-comparison proof'}
out=ROOT/'outputs/checks/2026-11-04-validated-oracle/review';out.mkdir(parents=True,exist_ok=True);p=out/('recurrence-independent-'+str(time.time_ns())+'.json');p.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({'report':str(p),**report}))
