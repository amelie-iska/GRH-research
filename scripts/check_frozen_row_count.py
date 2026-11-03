"""Exact arithmetic checks; not a certification of source arithmetic moments."""
from fractions import Fraction as F
from pathlib import Path
import json

OUT = Path(__file__).resolve().parents[1] / 'outputs/checks/2026-11-02-frozen-row'

def norm2(z):
    return z[0]**2 + z[1]**2

def mul(z, w):
    return (z[0]*w[0]-z[1]*w[1], z[0]*w[1]+z[1]*w[0])

checked = 0
for delta in (F(0), F(1,50), F(79,204), F(3,4)):
    for x in (F(0), F(1,7), F(1,4), F(1,2)):
        D = 3-F(17,9)*x
        P = (2-F(8,9)*x)*(1-x)
        J = (F(5,6)-delta)*D+delta*P
        assert D >= F(37,18) and P >= F(7,9) and J > 0
        cutoff = 1+delta*P/(2*J)
        assert 1 <= cutoff < F(3,2)
        short = lambda u: 1-delta+delta*P/D*(F(3,2)-u)
        long = lambda u: 1-delta+(F(5,6)-delta)*(u-1)
        R = long(cutoff)
        assert short(cutoff) == R
        for tau in (F(1), F(5,4), F(3,2), cutoff):
            crossing = ((2-F(8,9)*x)*tau-F(5,9)*x)/D
            assert F(23,37) <= crossing <= 1
            assert F(1,3) <= tau-crossing <= F(1,2)
            inverse = lambda r: 1-delta*(x+(1-x)*r)
            plain = lambda r: 1-delta*(F(4,9)*x+(2-F(8,9)*x)*(tau-r))
            assert inverse(crossing) == plain(crossing) == short(tau)
            assert max(short(tau), long(tau)) >= R
            for r in (crossing, (crossing+1)/2):
                assert (1-r)/2 <= F(7,37)
                assert 2*r-1 >= F(9,37)
            checked += 1
        # Actual and baseline capacity agree with the frozen parameter.
        for m in (F(0), F(1,3), F(1,2)):
            z = (1-2*m)/F(9,2)
            assert 2*m+6*F(3,4)*z == 1

# No-slot crossing is independent of the physical amplitude x.
for delta in (F(1,50), F(3,4)):
    r = F(2,3)
    assert 1-delta*r == 1-2*delta*(1-r) == 1-2*delta/3

# Finite complex moments, including an empty family and the plain fourth spike.
moment_tests = 0
for size in (0, 1, 4):
    w = [(F(i+1), F(i%2)) for i in range(size)]
    p = [(F(i+2,3), F(1,5)) for i in range(size)]
    A = min(map(norm2, w), default=F(0))
    B = min(map(norm2, p), default=F(0))
    M = sum((norm2(mul(a,b)) for a,b in zip(w,p)), F(0))
    assert size*A*B <= M
    fourth = sum((norm2(mul(mul(a,a),b)) for a,b in zip(w,p)), F(0))
    assert size*A*A*B <= fourth
    moment_tests += 2

t = F(1,100000)
ell = F(1,6)+t
h = F(13,16)+3*t/2
room = F(23,336)+53*t/14
assert room == 37*ell/7-h > 0
for zeta in (F(0), room/2):
    assert ell/(h+zeta) > F(7,37)
# The supply threshold is exact; equality does not provide a fixed margin.
assert ell/(h+room) == F(7,37)
report = {
    'status': 'passed',
    'crossing_and_cutoff_samples': checked,
    'finite_complex_moment_checks': moment_tests,
    'kappa': '3/4',
    'perturbation': str(t),
    'supply_extension_room': str(room),
    'scope': 'Exact finite and rational tests; no certification of source moment or witness estimates.'
}
OUT.mkdir(parents=True, exist_ok=True)
(OUT/'certificate.json').write_text(json.dumps(report, indent=2)+'\n')
print(json.dumps(report, indent=2))
