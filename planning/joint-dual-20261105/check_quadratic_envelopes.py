"""Exact rational bookkeeping for analytic envelopes; not a proof of GL."""
from fractions import Fraction as F
from pathlib import Path
import json,hashlib,argparse

def states(budget,n=6,prefix=()):
 j=len(prefix)+1
 if j>n:yield prefix;return
 for k in range(budget//j+1):yield from states(budget-j*k,n,prefix+(k,))

def main():
 p=argparse.ArgumentParser();p.add_argument('--output',type=Path,required=True);a=p.parse_args();assert not a.output.exists();a.output.mkdir(parents=True)
 checks=0;near=0;improved=0;worst=[];grid=[]
 for values in states(18):
  x=tuple(F(v,24) for v in values);r=sum(x);m=max(x[:2]);h=F(3,4)
  old=max(r,1+r-m,F(2,3)+r-m/3);quad=max(r,1+r-x[2]);best=min(old,quad)
  assert r-m<=h/3 and r-m/3<=2*h/3 and best<=F(5,4);checks+=1
  if best<old:improved+=1
  if best==F(5,4):
   assert x[0]==x[1] and x[0]+x[2]==F(1,4) and x[3:]==(0,0,0) and x[0]>=F(1,8)
   worst.append(values);checks+=1
  eta=F(1,24)
  if r-max(m,x[2])>=h/3-eta:
   assert x[2]-m<=eta
   capacity=sum((j+1)*v for j,v in enumerate(x))
   slack=h-3*(r-m)
   assert 0<=slack<=3*eta
   assert slack==h-capacity+(x[0]-x[1] if x[0]>=x[1] else 2*(x[1]-x[0]))+x[3]+2*x[4]+3*x[5]
   checks+=3;near+=1
 for k in range(1001):
  aa=F(k,4000);bb=F(1,4)-aa;r=2*aa+bb
  old=max(r,F(5,4),F(11,12)+2*aa/3);quad=max(r,1+2*aa);best=min(old,quad)
  assert best==min(F(5,4),1+2*aa);assert (best<F(5,4))==(aa<F(1,8));checks+=2
  if k in [0,499,500,501,1000]:grid.append({'a':str(aa),'b':str(bb),'old':str(old),'quadratic':str(quad),'combined':str(best)})
 result=dict(passed=True,assertions=checks,grid_denominator=24,capacity_units=18,feasible_states=sum(1 for _ in states(18)),strictly_refined_states=improved,near_saturation_states=near,remaining_worst_states=worst,face_checkpoints=grid,checker_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),scope='Exact exponents/slack/masks bookkeeping only; external GL theorem and arithmetic phase bounds are separate.')
 (a.output/'exact-envelopes.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
