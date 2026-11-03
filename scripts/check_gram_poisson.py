"""Exact deterministic diagnostics for Gram Fourier normalization and dyadic sums.

These finite samples complement the universal Lean components and prose Poisson
proof. They do not certify the source-specific reciprocity/period identification.
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json

OUT = Path(__file__).resolve().parents[1] / 'outputs/checks/2026-11-02-gram-poisson'


def exact_series(lam, exponent):
    """Infinite sum via an exact finite head plus CLOSED infinite tail."""
    assert lam > 0 and exponent >= 2
    if lam < 1:
        return F(4), None
    level = 0
    while 2 ** (level + 1) <= lam:
        level += 1
    head = sum((F(n + 1) * F(2) ** ((exponent - 1) * n)
                for n in range(level + 1)), F(0)) / lam ** exponent
    tail = F(level + 3, 2 ** level)
    return head + tail, level


def run():
    dyads = 0
    for level in range(31):
        head = sum(F(n + 1) * 2 ** n for n in range(level + 1))
        assert head == level * 2 ** (level + 1) + 1
        # Independently check tail recurrence and tail+head for the total series.
        tail = F(level + 3, 2 ** level)
        next_tail = F(level + 4, 2 ** (level + 1))
        assert tail - next_tail == F(level + 2, 2 ** (level + 1))
        assert sum(F(n + 1, 2 ** n) for n in range(level + 1)) + tail == 4
        value, _ = exact_series(F(2) ** level, 2)
        assert value == 3 * F(level + 1, 2 ** level) + F(1, 4 ** level)
        for ratio in (F(1, 3), F(1, 2), F(1), F(5, 4), F(3, 2), F(7, 4), F(2)):
            lam = F(2) ** level * ratio
            base, cutoff = exact_series(lam, 2)
            if cutoff is not None:
                assert base <= 4 * F(cutoff + 2) / lam
                assert (cutoff * 2 ** (cutoff + 1) + 1) / lam ** 2 <= 2 * F(cutoff + 1) / lam
            for exponent in (2, 3, 4):
                value, _ = exact_series(lam, exponent)
                assert 0 < value <= base <= 4
                dyads += 1

    # The additive quotient O/(2) in TWO columns is (Z/2)^4, size16.
    # All its characters are real signs, so the normalized DFT is exact rational.
    residues = list(product(range(2), repeat=4))
    fourier = 0
    for profile in range(5):
        def coefficient(x):
            y, z, w = x[1:]
            rest = (1, 1 + y - z + w, (y-z)*(w+1), 2*y*z-w, 3-y*z*w)[profile]
            return (-1) ** x[0] * rest
        a = {x: coefficient(x) for x in residues}
        assert sum(a.values()) == 0
        bound = max(abs(v) for v in a.values())
        for freq in residues:
            raw = sum(a[x] * (-1) ** sum(s*t for s, t in zip(x, freq)) for x in residues)
            normalized = F(raw, len(residues))
            assert abs(normalized) <= bound
            if freq == (0, 0, 0, 0):
                assert normalized == 0
            if profile == 0 and freq == (1, 0, 0, 0):
                assert raw == 16 and normalized == 1
            fourier += 1

    # Genuine nonprincipal multiplicative character on F7, extended by zero.
    chi = [0] + [1 if pow(x, 3, 7) == 1 else -1 for x in range(1, 7)]
    assert sum(chi) == 0
    independent = 0
    for d in range(1, 7):
        for profile in range(5):
            def other(i, j):
                return (1, i-j, i*j-2*j, (i-j)**2, (i+1)*(j+2))[profile]
            assert sum(chi[d*x % 7] * other(i, j)
                       for x in range(7) for i in range(4) for j in range(3)) == 0
            independent += 1

    accounting = 0
    for Q, Y, R, P, C, D in product((F(1), F(3, 2), F(8)), repeat=6):
        lhs = (Q/Y**3)*(C*D*(R*P/C))*C*(Y/(C*D))**2
        rhs = (Q/Y)*(R*P/(C*D))
        assert lhs == rhs
        accounting += 1
    result = {
        'dyadic_infinite_series_cases': dyads,
        'dyadic_head_tail_levels': 31,
        'normalized_finite_fourier_cases': fourier,
        'nonprincipal_independent_coordinate_cases': independent,
        'exact_scale_accounting_cases': accounting,
        'parameters': 'levels0..30; exponents2,3,4; seven rational cutoff ratios; O/(2)^2 additive quotient; F7 quadratic character; no randomness',
        'scope': 'exact finite diagnostics and closed-tail series checks; no certification of arithmetic reciprocity, full lattice Poisson, moments or GRH'
    }
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT/'certificate.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    run()
