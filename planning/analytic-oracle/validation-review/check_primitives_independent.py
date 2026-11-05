from pathlib import Path
from fractions import Fraction as F
import sys,json,hashlib,itertools,random,math,time
ROOT=Path('/home/iska/Documents/LaTeX-projects/GRH-from-Mac-20261104')
sys.path.insert(0,str(ROOT/'examples/analytic_oracle'))
import dyadic as d
import mpmath as mp
mp.mp.dps=110
OUT=ROOT/'outputs/checks/2026-11-04-validated-oracle/review';OUT.mkdir(parents=True,exist_ok=True)
source=hashlib.sha256(Path(d.__file__).read_bytes()).hexdigest();count=0

def exactend(x):return [F(x.lo,d.S),F(x.hi,d.S)]
def contains_mp(x,value):return mp.mpf(x.lo)/d.S<=value<=mp.mpf(x.hi)/d.S
def m(q):return mp.mpf(q.numerator)/q.denominator
# Fresh independently enumerated exact arithmetic corners.
for lo,hi in [(-7,-3),(-3,2),(0,0),(1,9),(-1,1)]:
 for den in [1,3,11]:
  a=d.R.bounds(F(lo,den),F(hi,den))
  for bl,bh in [(-8,-2),(-2,5),(2,7)]:
   b=d.R.bounds(F(bl,7),F(bh,7))
   for x,y in itertools.product(exactend(a),exactend(b)):
    assert (a+b).contains(x+y) and (a-b).contains(x-y) and (a*b).contains(x*y);count+=3
    if not b.lo<=0<=b.hi:assert (a/b).contains(x/y);count+=1
  for den2 in [-5,-1,1,3]:
   for x in exactend(a):assert (a/den2).contains(x/den2);count+=1
assert d.R.frac(F(-1,2*d.S))==d.R(-1,0)
assert d.R.frac(F(1,2*d.S))==d.R(0,1)
for args in [(d.real(1),d.R(-1,1)),(d.real(0),0)]:
 try:args[0]/args[1]
 except ZeroDivisionError:count+=1
 else:raise AssertionError('Accepted denominator containing zero')
for x in [.1,1.0,complex(1,2)]:
 try:d.real(x)
 except (TypeError,ValueError):count+=1
 else:raise AssertionError('Accepted binary float as exact interval input')
assert contains_mp(d.pi(),mp.pi)
# Exact log/exp identities plus separately high-precision diagnostics.
logcases=[F(1,1024),F(1,2),F(3,5),F(1),F(9,8),F(2),F(15,4),F(124),F(1024)]
for x in logcases:
 l=d.log_fraction(x);assert contains_mp(l,mp.log(m(x)));z=d.exp_box(d.C(l,d.real(0)));assert z.re.contains(x) and z.im.contains(0);count+=3
expcases=[(F(0),F(0)),(F(1),F(0)),(F(-1),F(0)),(F(-70),F(0)),(F(10),F(0)),(F(0),F(7)),(F(-2),F(11,7)),(F(3,7),F(-9,4)),(F(-100000),F(1))]
for x,y in expcases:
 z=d.exp_box(d.C(d.real(x),d.real(y)));truth=mp.exp(mp.mpc(m(x),m(y)));assert contains_mp(z.re,truth.real) and contains_mp(z.im,truth.imag);count+=2
z=d.exp_box(d.C(d.real(0),d.pi()));assert z.re.contains(-1) and z.im.contains(0);count+=2
box=d.C(d.R.bounds(F(-1,3),F(2,5)),d.R.bounds(F(-3,7),F(1,4)))
z=d.exp_box(box)
for x,y in itertools.product(exactend(box.re),exactend(box.im)):
 truth=mp.exp(mp.mpc(m(x),m(y)));assert contains_mp(z.re,truth.real) and contains_mp(z.im,truth.imag);count+=2
for x in [F(0),F(-1),1.0]:
 try:d.log_fraction(x)
 except (TypeError,ValueError):count+=1
 else:raise AssertionError('Accepted invalid log domain')
assert source==hashlib.sha256(Path(d.__file__).read_bytes()).hexdigest(),'Source changed during tests'
report={'passed':True,'checks':count,'dyadic_source_sha256':source,'dyadic_bits':d.BITS,'mpmath_version':mp.__version__,'exact_arithmetic_corner_and_identity_checks':True,'mpmath_comparisons_are_diagnostics_not_interval_proofs':True}
p=OUT/('primitives-independent-'+str(time.time_ns())+'.json');p.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({'report':str(p),**report}))
