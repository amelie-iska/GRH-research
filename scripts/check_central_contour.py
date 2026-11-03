"""Exact central-interface arithmetic; source analytic hypotheses are not certified."""
from fractions import Fraction as F
from pathlib import Path
import json
OUT = Path(__file__).resolve().parents[1] / 'outputs/checks/2026-11-02-central-contour'
geometry = 0
for a in (F(51,100),F(7,8),F(1)):
    for beta in (a,F(1)):
        for e in (F(1,10**7),F(1,1000)):
            for s in (a+16*e,beta+20*e):
                w = 1-a-6*e
                assert s >= F(51,100) and w >= -F(1,100)
                assert s+w >= 1+10*e and beta+20*e+w >= 1+14*e
                good = (-a-4*e,-F(51,25)+12*e,F(49,25)-5*a-68*e,a-F(51,25)+12*e)
                assert max(good) <= -F(51,100)
                geometry += 1
height = 0
for m in (3,4,12):
    cap = [F(i+1,3) for i in range(m)]
    for T in (F(1),F(17),F(103)):
        for sign in (-1,1):
            v = [sign*T/(2*m*(1+c)) for c in cap]
            assert abs(sum((c*x for c,x in zip(cap,v)),F(0))) <= T/2
            gamma = (3*4+1)*T
            assert abs(gamma+sum((c*x for c,x in zip(cap,v)),F(0))) <= (3*4+2)*T
            height += 1
credits = 0
for w in (F(-1,2),F(1,2)):
    A = F(1,2)-w
    Q = (F(7),F(13),F(19))
    for js in ((2,2,2),(2,3,5),(5,4,3)):
        product = F(1)
        comparison = F(1)
        for q,j in zip(Q,js):
            power = -w-(j-1)*A
            assert power == -F(1,2)-(j-2)*A <= -F(1,2)
            # Square both positive products: these exponents are integers here.
            assert (2*power).denominator == 1
            product *= q**int(2*power)
            comparison *= 1/q
        assert product <= comparison
        credits += 1

def E(sigma,a,h,ly,ell,g,d,R,delta):
    return a-sigma+h*(F(17,50)-F(1,6))-a*ly-ell/2+g+d*(R+delta/2-F(17,50))
t = F(1,100000)
identities = 0
for delta in (F(1,50),F(79,204),F(3,4)):
    a = (1+delta)/2
    for q in (F(0),delta/2):
        for R in (1-delta,F(1)):
            def exp(v,d):
                return E(F(7,8)-v/4,a,F(13,16)+3*v/2,F(23,48)-v/2,F(1,6)+v,q*(F(1,6)+v),d,R,delta)
            for d in (F(1,100),F(13,16),F(13,16)+3*t/2):
                assert exp(t,d)-exp(F(0),d) == t*(F(13,50)+delta/4+q)
                identities += 1
            assert exp(t,F(13,16)+3*t/2)-exp(F(0),F(13,16)) == t*(-F(1,4)+delta+q+3*R/2)
late = 0
for A in (F(0),F(100)):
    for saving in (F(1,10000),F(1,10)):
        cap = F(1,10**8)
        tau = min(cap,saving/(4*(A+1)))
        assert 0 < tau <= cap and A*tau <= saving/4
        B,C = F(7),F(-1,2)
        ratio = (B-C+saving/2)/tau
        N = max(0,ratio.numerator//ratio.denominator+1)
        assert B-N*tau < C-saving/2
        late += 1
report = {'status':'passed','rectangle_cases':geometry,'height_cases':height,
          'simultaneous_credit_cases':credits,'fixed_d_identity_cases':identities,
          'late_height_cases':late,'perturbation':str(t),
          'scope':'Exact finite geometry and exponent checks; no certification of scalar high identity, buffered bounds or row moments.'}
OUT.mkdir(parents=True, exist_ok=True)
(OUT/'certificate.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
