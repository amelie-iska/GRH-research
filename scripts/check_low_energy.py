"""Exact abstract-dyad/scale tests; no arithmetic moment or GRH certification."""
from fractions import Fraction as F
from pathlib import Path
import json

OUT = Path(__file__).resolve().parents[1] / 'outputs/checks/2026-11-02-low-energy'
positive = lambda x: max(F(0), x)
geometry_count = 0
dyad_count = 0
branches = {'u_equals_z': 0, 'u_at_least_v_over_2': 0}
for t in (F(0), F(1,100000), F(1,30)):
    ell = F(1,6)+t
    M = F(5,6)-t
    lx = F(17,48)-t/2
    ly = F(23,48)-t/2
    for fraction in (F(0),F(1,4),F(1,2),F(3,4),F(1)):
        d = fraction*ell
        Mr = M-2*d
        er = ell-d
        assert Mr+er-1 == -3*d
        assert 1+3*er-2*Mr == -F(1,6)+5*t+d
        assert lx-d >= F(11,80) and ly-d >= F(21,80)
        assert Mr >= F(2,5) and ly-d-F(11,48) >= F(1,30)
        loss = positive((-F(1,6)+5*t+d)/4)
        assert -d+loss/2 <= -7*d/8 <= 0
        assert lx/2+F(1,96) == F(3,16)-t/4
        geometry_count += 1
        for eps in (F(0),F(1,1000)):
            tau = eps
            for O in (F(0),Mr/3):
                for gap in (F(0),Mr/5):
                    H = Mr-O-gap
                    A = O/2
                    S = F(0)
                    for N in (F(0),A):
                        for B in (F(0),A/4):
                            for z in (F(0),er/2,er):
                                for theta in (-eps,F(0),eps):
                                    T = 2*H+2*A+2*z-1-er-theta-N-3*B
                                    for e in (F(0),-eps):
                                        if T+tau-e < 0:
                                            continue
                                        for split in (F(0),F(1,4),F(1)):
                                            v = split*(T+tau-e)
                                            lb = (1-split)*(T+tau-e)/3
                                            y = v+3*lb+e
                                            assert y <= T+tau
                                            u = min(v,z,(v+z)/3)
                                            assert u == z or u >= v/2
                                            if u == z:
                                                branches['u_equals_z'] += 1
                                            else:
                                                branches['u_at_least_v_over_2'] += 1
                                                assert u+lb+2*e/3+positive(T-y)/2 >= T/4-5*eps/12
                                            E = O/2+max(H,v+lb)-S-B+z-u-lb-2*e/3-positive(T-y)/2
                                            assert E <= Mr+loss+6*eps+2*abs(theta)+tau
                                            dyad_count += 1
# Exact boundary reason for retaining the unit-dyad offset.
eps = F(1,1000)
e = T = -eps
assert 2*e/3 == T/4-5*eps/12 < T/4
# A positive envelope does occur; it is absorbed, not falsely set to zero.
t = F(1,100000)
d = F(1,6)+t
assert positive((-F(1,6)+5*t+d)/4) == 3*t/2
# One explicit support/Gaussian/retention loss budget.
assert 8*F(1,128)+2*F(1,32)+F(1,16) == F(3,16)
assert F(3,16)+3*F(1,4) == F(15,16) < 1
report = {
    'status': 'passed',
    'geometry_cases': geometry_count,
    'feasible_abstract_dyads': dyad_count,
    'branches': branches,
    'perturbation': '1/100000',
    'scope': 'Exact rational real-exponent tests; source arithmetic energy, Gram and identities remain inputs.'
}
OUT.mkdir(parents=True, exist_ok=True)
(OUT/'certificate.json').write_text(json.dumps(report, indent=2)+'\n')
print(json.dumps(report, indent=2))
