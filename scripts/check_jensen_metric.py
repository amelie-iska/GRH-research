#!/usr/bin/env python3
"""Exact Newton-sum metric checks for specified rational model sequences.

These are regression witnesses for the proposed construction and failed generic
moment-positivity argument. They are not certificates for xi's coefficients.
"""
from fractions import Fraction as Q
from math import comb, factorial
from pathlib import Path
import json


def transpose(a):
    return list(map(list, zip(*a)))


def matmul(a, b):
    return [[sum((x*y for x, y in zip(row, col)), Q(0))
             for col in zip(*b)] for row in a]


def metric(gamma):
    d = len(gamma)-1
    assert d > 0 and gamma[-1] != 0
    a = [Q(comb(d, j))*gamma[j]/gamma[-1] for j in range(d+1)]
    # C is multiplication by x on R[x]/(p), basis 1,x,...,x^(d-1).
    c = [[Q(int(i == j+1)) if j < d-1 else -a[i]
          for j in range(d)] for i in range(d)]
    powers = [Q(d)]
    for k in range(1, 2*d-1):
        if k <= d:
            pk = -k*a[d-k] - sum((a[d-i]*powers[k-i]
                                   for i in range(1, k)), Q(0))
        else:
            pk = -sum((a[d-i]*powers[k-i]
                       for i in range(1, d+1)), Q(0))
        powers.append(pk)
    h = [[powers[i+j] for j in range(d)] for i in range(d)]
    hc = matmul(h, c)
    assert hc == transpose(hc)
    return c, h


def positive_ldl_pivots(a):
    """Exact Sylvester/LDL certificate; assert every pivot is positive."""
    a = [row[:] for row in a]
    pivots = []
    for k in range(len(a)):
        pivot = a[k][k]
        assert pivot > 0
        pivots.append(pivot)
        for i in range(k+1, len(a)):
            for j in range(k+1, len(a)):
                a[i][j] -= a[i][k]*a[k][j]/pivot
    return pivots


def run():
    good = {}
    # gamma(n)=n!/(2n)! is the cosh(sqrt(z)) model, not xi.
    for d in range(1, 9):
        gamma = [Q(factorial(n), factorial(2*n)) for n in range(d+1)]
        _, h = metric(gamma)
        good[str(d)] = list(map(str, positive_ldl_pivots(h)))

    bad_gamma = [Q(1), Q(1, 20), Q(1, 120)]
    c, h = metric(bad_gamma)
    assert c == [[0, -120], [1, -12]]
    assert h == [[2, -12], [-12, -96]]
    assert h[0][0]*h[1][1]-h[0][1]*h[1][0] == -336
    assert bad_gamma[1]**2-bad_gamma[0]*bad_gamma[2] == -Q(7, 1200)
    # The distinct kernel moment matrix is positive, including after smoothing.
    for variance in (Q(0), Q(1, 10), Q(1), Q(10)):
        mu2 = variance+Q(1, 10)
        mu4 = 3*variance**2+Q(3, 5)*variance+Q(1, 10)
        assert mu4-mu2**2 > 0
        assert (mu2/2)**2-mu4/12 == -Q(7, 1200)

    # Repeated roots require semidefinite treatment: H is singular for (1+x)^2.
    _, repeated = metric([Q(1), Q(1), Q(1)])
    assert repeated == [[2, -2], [-2, 2]]

    # Finite checks of the coefficient bound; its universal proof is in prose.
    for d in range(1, 65):
        for j in range(129):
            w = Q(factorial(j)*comb(d, j), d**j) if j <= d else Q(0)
            assert 0 <= w <= 1
            assert 1-w <= Q(j*(j-1), 2*d)

    report = {
        "arithmetic": "exact Fraction; deterministic; no random seed",
        "cosh_model_positive_pivots_degrees_1_to_8": good,
        "positive_moment_counterexample_gamma": list(map(str, bad_gamma)),
        "counterexample_companion": [[str(v) for v in row] for row in c],
        "counterexample_newton_hermite": [[str(v) for v in row] for row in h],
        "counterexample_determinant": "-336",
        "gaussian_smoothing_turan_gap": "-7/1200 for every variance >= 0 (algebra in Lean)",
        "repeated_root_model_metric": [[str(v) for v in row] for row in repeated],
        "coefficient_bound_finite_checks": "1<=d<=64, 0<=j<=128; universal argument in paper",
        "scope": "Model arithmetic and construction checks only. No xi coefficient enclosures or universal Jensen positivity proved. GRH remains unresolved."
    }
    out = Path(__file__).resolve().parents[1]/"outputs/checks/2026-11-02-jensen-metric/certificate.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, indent=2)+"\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    run()
