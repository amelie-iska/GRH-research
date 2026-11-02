from fractions import Fraction as F
from pathlib import Path
m0=F(49,440640)
t=F(1,100000)
max_t=m0/5
assert t < max_t < F(1,30)
assert F(7,8)-t/4 == F(349999,400000)
assert m0-F(5,2)*max_t == m0/2
# Independent rational substitutions in the general printed high formula.
for delta in (F(0),F(1,50),F(79,204),F(3,4),F(5,6)):
 for x in (F(0),F(1,4),F(1,2)):
  alpha=F(5,6);D=3-F(17,9)*x;P=(2-F(8,9)*x)*(1-x)
  J=(alpha-delta)*D+delta*P
  R=1-delta+(alpha-delta)*delta*P/(2*J)
  q=x*delta;a=(1+delta)/2
  def general(v):
   ell=F(1,6)+v;lx=F(17,48)-v/2;ly=F(23,48)-v/2;h=F(13,16)+3*v/2
   sigma=F(7,8)-v/4
   assert lx+ly+ell==1
   assert lx/2-1+h/6 == -F(11,16)
   assert lx/2+F(1,8)/12 == F(3,16)-v/4
   return a-sigma+h*(F(17,50)-F(1,6))-a*ly-ell/2+q*ell+h*(R+delta/2-F(17,50))
  K=-F(1,4)+delta+q+F(3,2)*R
  assert general(t)-general(F(0))==t*K
  assert R<=1
  assert K<=F(5,2)
# Exact adverse witness for continuing the same envelope much further.
delta=F(79,204);x=F(1,2);alpha=F(5,6)
D=3-F(17,9)*x;P=(2-F(8,9)*x)*(1-x);J=(alpha-delta)*D+delta*P
R=1-delta+(alpha-delta)*delta*P/(2*J)
m=F(1,48)-F(2,3)*delta-x*delta/6+F(13,16)*(1-R)
K=-F(1,4)+delta+x*delta+F(3,2)*R
assert m==F(7,30672) and K==F(115819,86904)
assert m/K==F(119,694914)
# Unused rescaling suppression controls the generalized row-norm loss.
for v in (F(0),t,max_t,F(1,30)):
 for frac in (F(0),F(1,3),F(2,3),F(1)):
  ell=F(1,6)+v;d=frac*ell
  loss=max(F(0),(-F(1,6)+5*v+d)/4)
  assert -d+loss/2<=0
assert F(1,2)+5*F(6,7)/12==F(6,7)
assert 1-F(6,7)/6==F(6,7)
assert F(1,2)+5*F(3,4)/12==F(13,16)
print('All exact rational checks passed.')
print('Safe t range: 0<t<=',max_t)
print('Concrete conditional target:',F(349999,400000))
print('Central margin after perturbation:',m0-F(5,2)*t)
print('Exact unchanged-envelope adverse t:',m/K)
