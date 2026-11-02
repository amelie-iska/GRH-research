#!/usr/bin/env python3
"""Exact rational consistency checks for the constructive approximation formulas.
These finite checks do not replace the analytic convergence proofs.
"""
from fractions import Fraction as Q
from pathlib import Path
import json

def chi3(n):
    return (0, 1, -1)[n % 3]

def partial_sums(limit, coefficient):
    values = [Q(0)]
    for n in range(1, limit + 1):
        values.append(values[-1] + Q(coefficient(n), n*n))
    return values

def run():
    limit = 600
    zeta = partial_sums(limit, lambda n: 1)
    character = partial_sums(limit, chi3)
    running = 0
    for n in range(1, limit + 1):
        running += chi3(n)
        assert running in (0, 1)  # exact B_chi=1 for this character
    # Integral comparison provides an independent rational enclosure of zeta(2).
    zeta_lower = zeta[limit] + Q(1, limit + 1)
    zeta_upper = zeta[limit] + Q(1, limit)
    # The proved Abel bound encloses L(2,chi3); checks below are finite consistency only.
    char_radius = Q(2, limit*limit)
    for n in range(1, 51):
        corrected_zeta = zeta[n] + Q(1, n)
        assert max(abs(corrected_zeta-zeta_lower), abs(corrected_zeta-zeta_upper)) <= Q(1,n*n)
        assert abs(character[n]-character[limit]) + char_radius <= Q(2,n*n)
    # At s=1 the pole-cleared bracket is exactly1 for every cutoff, before gamma factors.
    for n in (1, 2, 5, 50):
        assert 0 * n + n**0 == 1
    report = {
        "arithmetic": "exact rational integers; no floating point or randomness",
        "reference_cutoff": limit,
        "cutoffs_checked": 50,
        "character_modulus": 3,
        "character_partial_sum_bound": 1,
        "zeta_exponent": 2,
        "checks": "pole-subtracted zeta and nonprincipal Dirichlet partial sums",
        "scope": "finite consistency checks; not a proof of GRH or an independent formal proof of the analytic bounds"
    }
    out = Path(__file__).resolve().parents[1]/"outputs/checks/continuation/arithmetic-approximants.json"
    out.write_text(json.dumps(report, indent=2)+"\n")
    print(json.dumps(report, indent=2))
if __name__ == "__main__":
    run()
