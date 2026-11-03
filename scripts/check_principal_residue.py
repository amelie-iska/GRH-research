#!/usr/bin/env python3
"""Exact principal-multiplier, weighted-slot and exponent checks.
No prime-counting, contour theorem or GRH is certified by finite samples.
"""
from fractions import Fraction as Q
from pathlib import Path
import json
from check_euler_correction import K


def multiplier(v, d, r):
    return (1-v)*(r-d)/(d*(1-v*r-(1-v)*d))-v


def run():
    sx, sw, sz = Q(3, 4), Q(19, 20), Q(33, 200)
    gaps = [sx, 6*sz, 5*sx+6*sz-4, sw+6*sz-1]
    assert min(gaps) == Q(37, 50)
    t = Q(1, 100000)
    ell, lx, ly, h = Q(1, 6)+t, Q(17, 48)-t/2, Q(23, 48)-t/2, Q(13, 16)+3*t/2
    sigma = Q(7, 8)-t/4
    assert sigma == Q(349999, 400000) and sigma > Q(3, 4)
    assert lx+ly+ell == 1 and h == 1-lx+ell
    assert lx/2-1+h/6 == -Q(11, 16)
    allocations = {}
    for slots in (2, 8, 1024):
        # Examples of the principal interface only; row-count slot admissibility is separate.
        ell_min = ell/slots
        mu = Q(7, 10)*ell_min
        mw, mz = ly/20, h/600
        e = min(Q(1, 10000), mw/(8*(1+h)), mz/8, mu/8)
        eps = e
        assert 0 < mu < Q(37, 50)*ell_min
        assert (1+h)*e+eps < mw
        assert e+eps < mz and e+eps < mu
        allocations[str(slots)] = {"mu": str(mu), "e": str(e),
                                    "w_saving": str(mw-(1+h)*e-eps),
                                    "z_saving": str(mz-e-eps),
                                    "residue_saving": str(mu-e-eps)}

    omega = K(-Q(1, 2), Q(1, 2))
    samples = 0
    for q, prime in ((7, -2-3*omega), (13, 1-3*omega)):
        angular = prime.conj()**6/q**3
        assert angular.norm_sq() == 1
        for eta in (K(1), omega, -omega):
            for real_s in (1, 2):
                v = K(Q(1, q))
                d, r = eta/q**real_s, angular*eta**6*K(Q(q)**(3-6*real_s))
                n = 1-v*r-(1-v)*d
                b = multiplier(v, d, r)
                pstar = (1+v)*(r-d)/(1-r)
                p = 1/(1-v)+v/(1-v)+pstar
                assert b == (pstar/p)/d-v
                assert b+1 == (1-v)*(r/d-v*r-(1-v)*d)/n
                assert (b+1)/(r/d)-1 == (-v*(1-r)+(1-v)**2*d*(1-d/r))/n
                samples += 1

    for q in (4, 25, 121):
        # r=d is the exact arithmetic boundary relation at s=3/5 for inert
        # prime ideals and eta=1. The chosen d tests its universal scalar identity;
        # it is not offered as the transcendental value q^(-3/5).
        v, d = K(Q(1, q)), K(Q(1, q))
        assert multiplier(v, d, d) == -v

    weights = [Q(1, 3), Q(2, 5), Q(1, 7)]
    errors = [K(Q(1, 100)), K(0, Q(1, 200)), K(Q(1, 300), Q(1, 400))]
    delta = Q(1, 100)
    mass = sum(weights)
    assert mass > 0 and all(x >= 0 for x in weights)
    assert all(e.norm_sq() <= delta**2 for e in errors)
    rho = -sum((a*e for a, e in zip(weights, errors)), K())/mass
    slot = sum((a*(-1+e) for a, e in zip(weights, errors)), K())
    assert slot == -mass*(1+rho) and rho.norm_sq() <= delta**2
    for slots in range(9):
        product = K(1)
        for j in range(slots):
            product = product*(1+errors[j % len(errors)])
        assert (product-1).norm_sq() <= ((2**slots-1)*delta)**2

    # A positive total mass alone cannot replace nonnegative individual weights.
    signed_mass = Q(1)-Q(99, 100)
    signed_rho = -(Q(1, 100)+Q(99, 10000))/signed_mass
    assert abs(signed_rho) == Q(199, 100) > delta
    assert 3-5*Q(3, 5) == 0
    assert 4*Q(3, 5)-3 == -Q(3, 5)
    report = {
        "arithmetic": "exact Fraction and Q(sqrt(-3)); deterministic; no random seed",
        "rectangle_gaps": list(map(str, gaps)), "uniform_local_gap": "37/50",
        "target_sigma": str(sigma), "geometry_t": str(t),
        "principal_loss_allocations": allocations,
        "arithmetic_prime_phase_samples": samples,
        "boundary_relation": "r=d implies B=-1/Q; inert prime ideals at s=3/5 and eta=1 realize r=d, proved in prose and scalar identity in Lean",
        "weighted_slot_and_product_checks": "passed; nonnegative weights, plus signed-weight failure witness",
        "scope": "Exact algebra/exponents only. No fixed-ray PNT, full source Gauss identity, contour integration, energy/row-count estimates or new zero-free theorem is certified."
    }
    out = Path(__file__).resolve().parents[1]/"outputs/checks/2026-11-02-principal-residue/certificate.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, indent=2)+"\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    run()
