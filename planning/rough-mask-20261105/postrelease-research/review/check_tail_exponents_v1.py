"""Fresh rational localization arithmetic only; no old experiment imports or reruns."""
from fractions import Fraction as Q
from pathlib import Path
import json
H=Q(3,4)
rows=[]
for name,a,b,expectedY in [('mixed',Q(5,12),Q(1,6),Q(13,24)),('pure',Q(3,4),Q(0),Q(5,8))]:
 r=a+b;m=max(a,b)
 required=[Q(0),Q(1,2),Q(1)+r-m-H,Q(1)+Q(3,2)*r-Q(1,2)*m-Q(3,2)*H]
 y=max(required);assert y==expectedY
 tail=[r,Q(1)+r-m-y,Q(2,3)+r-m/Q(3)-Q(2,3)*y]
 uncut=[r,Q(1)+r-m,Q(2,3)+r-m/Q(3)]
 assert all(x<=H for x in tail) and y>Q(1,2) and max(uncut)==Q(7,6)
 assert a+2*b<=H
 rows.append(dict(case=name,a=str(a),b=str(b),R=str(r),M=str(m),Y=str(y),required=[str(x)for x in required],tail=[str(x)for x in tail],uncut=[str(x)for x in uncut],capacity_exponent=str(a+2*b)))
# Verify the sufficient-cutoff identities throughout a rational feasible triangle.
# This is algebraic bookkeeping, not a finite energy experiment or analytic proof.
count=0
for ia in range(37):
 for ib in range(19):
  a=Q(ia,48);b=Q(ib,48)
  if a+2*b>H:continue
  r=a+b;m=max(a,b);y=max(Q(0),Q(1,2),1+r-m-H,1+Q(3,2)*r-Q(1,2)*m-Q(3,2)*H)
  assert r<=H and 1+r-m-y<=H and Q(2,3)+r-m/Q(3)-Q(2,3)*y<=H
  count+=1
print(json.dumps(dict(passed=True,cases=rows,feasible_rational_points_checked=count,scope='Independent exact exponent algebra only; no claimed necessity, measured energy, saving, or analytic theorem from this grid'),sort_keys=True,indent=2))
