#!/usr/bin/env python3
"""Exact exponents and local identities in Q(sqrt(-3)); no floating point.

The source scalar identity is an inherited input. This checker does not verify
its preceding Gauss sums, analytic contour estimates or any zero-free theorem.
"""
from fractions import Fraction as Q
from pathlib import Path
import json


class K:
    """a+b sqrt(-3), with the standard complex embedding understood in prose."""
    def __init__(self, a=0, b=0):
        self.a, self.b = Q(a), Q(b)

    def __add__(self, other):
        other = other if isinstance(other, K) else K(other)
        return K(self.a+other.a, self.b+other.b)
    __radd__ = __add__

    def __neg__(self):
        return K(-self.a, -self.b)

    def __sub__(self, other):
        return self+-other if isinstance(other, K) else self+K(-other)

    def __rsub__(self, other):
        return -self+other

    def __mul__(self, other):
        other = other if isinstance(other, K) else K(other)
        return K(self.a*other.a-3*self.b*other.b,
                 self.a*other.b+self.b*other.a)
    __rmul__ = __mul__

    def conj(self):
        return K(self.a, -self.b)

    def norm_sq(self):
        return self.a**2+3*self.b**2

    def __truediv__(self, other):
        other = other if isinstance(other, K) else K(other)
        norm = other.norm_sq()
        assert norm != 0
        product = self*other.conj()
        return K(product.a/norm, product.b/norm)

    def __rtruediv__(self, other):
        return K(other)/self

    def __pow__(self, n):
        assert isinstance(n, int) and n >= 0
        result = K(1)
        for _ in range(n):
            result = result*self
        return result

    def __eq__(self, other):
        other = other if isinstance(other, K) else K(other)
        return self.a == other.a and self.b == other.b


def run():
    x, w, z = Q(3, 4), Q(19, 20), Q(33, 200)
    good = {
        "R": 4-6*x-6*z, "Q_D_W_V": 1-x-w-6*z,
        "D_V": -x-6*z, "D_W": -x-w,
        "D_V_W": -x-w-6*z, "V_W": -w-6*z,
    }
    bad = {
        "R": good["R"], "strict_family": 1-x-w,
        "J1": -x-w, "J2": Q(3, 2)-3*x,
        "J3_first": 2-3*x-w, "J3_second": 2-4*x,
        "J4": Q(5, 2)-4*x-w, "J5": 3-6*x,
    }
    assert max(good.values()) == -Q(149, 100)
    assert max(bad.values()) == -Q(7, 10)
    assert Q(1, 4) < Q(8, 27)  # 2^(-2/3)<2/3 for the principal bound.
    assert Q(9, 16) > Q(1, 2)  # 2^(-1/2)<3/4; all denominators controlled.
    assert 4*(4+4*40) == 656 < 1024
    assert 4*(1+1+2*2) == 24 < 32
    assert Q(349999, 400000) > x

    omega = K(-Q(1, 2), Q(1, 2))
    assert omega**3 == 1
    # Primary prime elements in Z[omega]: -2-3omega and 1-3omega.
    primes = [(7, -2-3*omega), (13, 1-3*omega)]
    samples = 0
    for q, prime in primes:
        assert prime.norm_sq() == q
        alpha_bar_six = prime.conj()**6/q**3
        assert alpha_bar_six.norm_sq() == 1
        for eta in (K(1), omega, -omega):
            theta = alpha_bar_six*eta**6
            assert theta.norm_sq() == 1
            for sx in (1, 2):
                v, d, r = K(Q(1, q)), eta/q**sx, theta*K(Q(q)**(3-6*sx))
                for sw in (1, 2):
                    ww = K(Q(1, q**sw))
                    pstar = ((r*(1-Q(1, q))-d*ww*(q-1)*v)/(1-v)-d+ww*r)/(1-r)
                    residual = (r*((1-Q(1, q))/(1-v)+ww-d)
                                -d*ww*(q-1)*v/(1-v))/(1-r)
                    assert pstar+d == residual
                    raw_h = (1/(1-v)+ww/(1-ww)+pstar)*(1-v)*(1-ww)/(1-d)
                    if sw == 1:
                        h = (1-v**2)*(1-v*r-(1-v)*d)/((1-r)*(1-d))
                        a = (1-v**2)*(1-v*r-(1-v)*d)/(1-d)
                        assert raw_h == h and a == (1-r)*h
                        assert a-1 == -v**2+(1-v**2)*v*(d-r)/(1-d)
                        assert h != 0 and a != 0
                    samples += 1

    margins = {}
    for sigma in (Q(51, 100), Q(3, 4), Q(349999, 400000)):
        delta_a = min(Q(1), sigma, 6*sigma-3)
        assert delta_a > 0
        margins[str(sigma)] = {"A_tail_margin": str(delta_a)}
        if sigma > Q(2, 3):
            delta_h = min(Q(1), sigma, 6*sigma-4)
            assert delta_h > 0
            margins[str(sigma)]["H_tail_margin"] = str(delta_h)
    assert (Q(1, 2)+3)/6 == Q(7, 12)
    report = {
        "arithmetic": "exact Fraction and Q(sqrt(-3)); deterministic; no seed",
        "closed_region": {"Re_x_min": str(x), "Re_w_min": str(w), "Re_z_min": str(z)},
        "good_prime_exponents": {k: str(v) for k, v in good.items()},
        "row_ramified_exponents": {k: str(v) for k, v in bad.items()},
        "safe_constants": {"good": 1024, "row_ramified": 32},
        "exact_arithmetic_local_samples": samples,
        "prime_representatives_in_Zomega": ["-2-3omega (norm7)", "1-3omega (norm13)"],
        "tail_margins": margins,
        "scope": "Checks exponents and rational local identities, not Gauss/reciprocity derivation, infinite-product normal convergence, Hecke analytic theory, compensated contours, mean squares or GRH."
    }
    out = Path(__file__).resolve().parents[1]/"outputs/checks/2026-11-02-euler-correction/certificate.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, indent=2)+"\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    run()
