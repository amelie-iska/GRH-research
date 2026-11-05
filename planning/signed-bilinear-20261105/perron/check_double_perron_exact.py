#!/usr/bin/env python3
"""Exact finite original-family Euler and sharp-endpoint controls; stdlib only.

Not an analytic contour, infinite moment, zero-location or GRH certificate.
Existing arithmetic source is imported read-only; no stochastic input.
"""
import sys
sys.dont_write_bytecode = True
from pathlib import Path
from fractions import Fraction as Q
from itertools import product
import argparse
import hashlib
import json

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "scripts"))
from check_mobius_split import universe, quotient
from check_reciprocity_period import emul, norm, prime_symbol, power

ZERO = (Q(0), Q(0))
ONE = (Q(1), Q(0))
PHASES = ((1, 0), (1, 1), (0, 1), (-1, 0), (-1, -1), (0, -1))


def add(a, b):
    return (a[0] + b[0], a[1] + b[1])


def sub(a, b):
    return (a[0] - b[0], a[1] - b[1])


def scale(a, c):
    return (a[0] * c, a[1] * c)


def inv(a):
    n = norm(a)
    if not n:
        raise ZeroDivisionError("Zero algebraic denominator")
    return ((a[0] - a[1]) / n, -a[1] / n)


def mul(a, b):
    return emul(a, b)


def total(items):
    ans = ZERO
    for item in items:
        ans = add(ans, item)
    return ans


def prod(items):
    ans = ONE
    for item in items:
        ans = mul(ans, item)
    return ans


def monomials(values):
    out = [ONE]
    for m in range(1, 1 << len(values)):
        low = m & -m
        out.append(mul(out[m ^ low], values[low.bit_length() - 1]))
    return out


def run():
    _, _, _, candidates = universe(32)
    primes = [p for p in candidates if norm(p) in (7, 13, 25)]
    assert len(primes) == 5
    assert sorted(map(norm, primes)) == [7, 7, 13, 13, 25]
    full = (1 << len(primes)) - 1
    norms = [1]
    for m in range(1, full + 1):
        low = m & -m
        norms.append(norms[m ^ low] * norm(primes[low.bit_length() - 1]))
    mu = [(-1) ** m.bit_count() for m in range(full + 1)]
    pairs = [(a, b) for a in range(full + 1) for b in range(full + 1) if not a & b]
    rows = [(1, 0), (1, 1), (2, 0), primes[0], power(primes[0], 3),
            power(primes[0], 6), emul(power(primes[0], 6), primes[-1]),
            emul(primes[0], power(primes[2], 2))]
    counts = dict(local_identity=0, global_Euler_identity=0,
                  G_absolute_series_algebra=0, coordinate_slice_identity=0,
                  weighted_cutoff_coefficient_identity=0, original_zero_checks=0,
                  omitted_R_negative_controls=0, overlap_square_negative_controls=0,
                  halfweight_endpoint_negative_controls=0,
                  halfinteger_exact_endpoint=0)
    cutoffs = [Q(1), Q(7), Q(15, 2), Q(13), Q(25), Q(norms[-1])]
    for u, fixed_twist, sigma in product(rows, [False, True], [1, 2]):
        q = []
        deleted = []
        for p in primes:
            e = prime_symbol(p, u)
            deleted.append(e is None)
            if e is None:
                q.append(ZERO)
            else:
                if fixed_twist:
                    e = (e + prime_symbol(p, (2, 0))) % 6
                q.append(scale(tuple(map(Q, PHASES[e])), Q(1, norm(p) ** sigma)))
        t = [mul(v, inv(add(ONE, v))) for v in q]
        qm = monomials(q)
        tm = monomials(t)
        F0 = prod(add(ONE, v) for v in q)
        for m in range(full + 1):
            if any(deleted[j] and m >> j & 1 for j in range(len(primes))):
                assert qm[m] == tm[m] == ZERO
                counts["original_zero_checks"] += 1
        for z, w in [(0, 0), (0, 1), (1, 0), (1, 2), (2, 1)]:
            alpha = [Q(1, norm(p) ** z) for p in primes]
            beta = [Q(1, norm(p) ** w) for p in primes]
            E = []
            R = []
            main = []
            for j, v in enumerate(q):
                ap, bp = alpha[j], beta[j]
                ep = sub(sub(add(ONE, v), scale(v, ap)), scale(v, bp))
                da, db = sub(ONE, scale(v, ap)), sub(ONE, scale(v, bp))
                correction = scale(mul(v, v), (1 - ap) * (1 - bp))
                assert mul(sub(ONE, v), ep) == sub(mul(da, db), correction)
                rp = sub(ONE, mul(correction, inv(mul(da, db))))
                mp = mul(mul(da, db), inv(sub(ONE, v)))
                assert ep == mul(mp, rp)
                assert ep == mul(add(ONE, v), sub(sub(ONE, scale(t[j], ap)), scale(t[j], bp)))
                E.append(ep)
                R.append(rp)
                main.append(mp)
                counts["local_identity"] += 1
            euler = prod(E)
            direct = total(scale(mul(qm[a | b],
                prod(add(ONE, q[j]) for j in range(len(primes)) if not (a | b) >> j & 1)),
                Q(mu[a] * mu[b], norms[a] ** z * norms[b] ** w)) for a, b in pairs)
            gseries = total(scale(tm[a | b], Q(mu[a] * mu[b],
                                                norms[a] ** z * norms[b] ** w))
                            for a, b in pairs)
            assert euler == direct == mul(prod(main), prod(R)) == mul(F0, gseries)
            counts["global_Euler_identity"] += 1
            counts["G_absolute_series_algebra"] += 1
            counts["omitted_R_negative_controls"] += euler != prod(main)
            if z == 0 or w == 0:
                assert prod(R) == ONE
                shift = w if z == 0 else z
                expected = prod(sub(ONE, scale(q[j], Q(1, norm(p) ** shift)))
                                for j, p in enumerate(primes))
                assert euler == expected
                counts["coordinate_slice_identity"] += 1
        for U in cutoffs:
            beta_U = [sum(mu[a] * mu[b] for a, b in pairs if (a | b) == m
                          and norms[a] <= U and norms[b] <= U)
                      for m in range(full + 1)]
            A_U = [sum(beta_U[d] for d in range(full + 1) if not d & ~m)
                   for m in range(full + 1)]
            j_direct = total(scale(mul(qm[d], prod(add(ONE, q[j])
                             for j in range(len(primes)) if not d >> j & 1)), beta_U[d])
                             for d in range(full + 1))
            j_coeff = total(scale(qm[m], A_U[m]) for m in range(full + 1))
            j_B = mul(F0, total(scale(tm[a | b], mu[a] * mu[b]) for a, b in pairs
                                     if norms[a] <= U and norms[b] <= U))
            assert j_direct == j_coeff == j_B
            counts["weighted_cutoff_coefficient_identity"] += 1
            M = total(scale(tm[a], mu[a]) for a in range(full + 1) if norms[a] <= U)
            counts["overlap_square_negative_controls"] += j_B != mul(F0, mul(M, M))
            V = Q(U.numerator // U.denominator) + Q(1, 2)
            assert all((n <= U) == (n < V) for n in norms)
            counts["halfinteger_exact_endpoint"] += len(norms)
            def h(n):
                return Q(1) if n < U else Q(1, 2) if n == U else Q(0)
            half = total(scale(tm[a | b], mu[a] * mu[b] * h(norms[a]) * h(norms[b]))
                         for a, b in pairs)
            fix = total(scale(tm[a | b], mu[a] * mu[b] * (
                Q(1, 2) * (norms[a] == U) * h(norms[b])
                + Q(1, 2) * h(norms[a]) * (norms[b] == U)
                + Q(1, 4) * (norms[a] == U) * (norms[b] == U))) for a, b in pairs)
            assert j_B == mul(F0, add(half, fix))
            counts["halfweight_endpoint_negative_controls"] += j_B != mul(F0, half)
    # Exact actual equal-norm two-prime endpoint, not abstract equal integers.
    i, j = [i for i, p in enumerate(primes) if norm(p) == 7]
    assert i != j and not (1 << i) & (1 << j)
    assert norms[1 << i] == norms[1 << j] == 7
    # On this allowed pair the naive double half weight is 1/4, inclusive is 1.
    assert Q(1, 2) ** 2 + Q(1, 4) + Q(1, 4) + Q(1, 4) == 1
    # Sixth-power conductor drop cannot restore an original forbidden prime.
    u6 = power(primes[0], 6)
    assert prime_symbol(primes[0], u6) is None
    assert quotient(u6, primes[0]) is not None
    assert sub(ONE, (Q(1, norm(primes[0])), Q(0))) != ONE
    # Exact sufficient-domain and U-exponent bookkeeping, not analytic proof.
    regions = []
    for sigma, x, y in [(Q(3, 5), Q(2, 5) + Q(1, 100), Q(2, 5) + Q(1, 100)),
                        (Q(3, 5), -Q(1, 25), -Q(1, 25)),
                        (Q(3, 5), -Q(1, 5), -Q(1, 5)),
                        (Q(2), -Q(5, 2), Q(1))]:
        kappa = 2 * sigma + min(x, 0) + min(y, 0)
        omega = sigma + x > 0 and sigma + y > 0 and kappa > 1
        safe = sigma + x > 1 and sigma + y > 1
        regions.append(dict(sigma=str(sigma), x=str(x), y=str(y),
                            correction_region=omega, absolute_reciprocal_region=safe))
    assert regions[0]["correction_region"] and regions[0]["absolute_reciprocal_region"]
    assert regions[1]["correction_region"] and not regions[1]["absolute_reciprocal_region"]
    assert not regions[2]["correction_region"] and not regions[3]["correction_region"]
    for name in ["omitted_R_negative_controls", "overlap_square_negative_controls",
                 "halfweight_endpoint_negative_controls", "original_zero_checks"]:
        assert counts[name] > 0
    files = [Path(__file__), ROOT / "scripts/check_mobius_split.py",
             ROOT / "scripts/check_reciprocity_period.py",
             Path(__file__).with_name("DOUBLE_PERRON.md"),
             ROOT / "papers/masked-moment-core.tex",
             ROOT / "papers/masked-moment-details.tex",
             ROOT / "papers/weighted-cutoff-core.tex",
             ROOT / "papers/weighted-cutoff-details.tex",
             ROOT / "outputs/checks/2026-11-05-weighted-moment/review/independent-acceptance-v2.json"]
    return dict(passed=True, deterministic=True, arithmetic="Fraction and exact Eisenstein pairs; no seed",
                prime_ideals=[dict(generator=list(p), norm=norm(p)) for p in primes],
                finite_support=32, literal_rows=len(rows), fixed_nu_diagnostics=["principal", "raw sextic twist of 2"],
                counts=counts, equal_norm_endpoint_control=True, sixth_power_sentinel_control=True,
                rational_domain_controls=regions,
                source_sha256={str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest() for p in files},
                no_new_analytic_saving=True, no_new_Lean=True, no_GRH_claim=True,
                scope="Finite original-mask Euler/cutoff algebra and negative controls only; not analytic convergence, contour shifting, reciprocal bounds or zero location.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists():
        raise FileExistsError("Preserve prior evidence; choose a fresh report path")
    report = run()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({k: v for k, v in report.items() if k != "source_sha256"}, indent=2))
