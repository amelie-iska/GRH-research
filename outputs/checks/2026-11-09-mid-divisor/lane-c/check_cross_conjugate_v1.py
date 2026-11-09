from fractions import Fraction as F
from hashlib import sha256
from itertools import product
import json
from math import prod
from pathlib import Path


PROOF = Path("planning/mid-divisor-20261109/lane-c/CROSS_CONJUGATE_CUTOFF-v1.md")
OUT = Path("outputs/checks/2026-11-09-mid-divisor/lane-c/cross-conjugate-check-v1.json")
DIGEST = "68ec0ada633f984cb5cfe665436e4abcef00896e255e187bbd995b28b5d57ab4"
assert sha256(PROOF.read_bytes()).hexdigest() == DIGEST
assert all(byte >= 32 or byte in {9, 10} for byte in PROOF.read_bytes())

# Distinct ideals above split 7,13,19 and one inert ideal above 5.
NORMS = (7, 7, 13, 13, 19, 19, 25)
CONJUGATE = (1, 0, 3, 2, 5, 4, 6)
SIZE = 1 << len(NORMS)
MASK = SIZE - 1
SUB = [[sub for sub in range(SIZE) if sub & mask == sub] for mask in range(SIZE)]
NORM = [prod(p for i, p in enumerate(NORMS) if (mask >> i) & 1) for mask in range(SIZE)]
MU = [(-1) ** mask.bit_count() for mask in range(SIZE)]
BAR = [sum(1 << CONJUGATE[i] for i in range(len(NORMS)) if (mask >> i) & 1)
       for mask in range(SIZE)]
SPLIT_PAIRS = (3, 12, 48)
ROWS = ((0, 1, 2, 3, 4, 5, 0), (1, None, 2, 4, 5, 1, 3),
        (None, 3, 1, None, 2, 5, 4))


def phase(*factors):
    values = []
    for row in ROWS:
        roots = [row[i] for mask in factors for i in range(len(row)) if (mask >> i) & 1]
        values.append(None if None in roots else sum(roots) % 6)
    return tuple(values)


def record(hist, exponents, weight):
    for row, exponent in enumerate(exponents):
        if exponent is not None:
            hist[row][exponent] += weight


def rational_node(total, d):
    return (total - d) * (2 * d - total) if d < total < 2 * d else 0


def ideal_content(mask):
    return prod(NORMS[(pair & -pair).bit_length() - 1] for pair in SPLIT_PAIRS if mask & pair == pair)


direct_terms = 0
expanded_terms = 0
nonunit_overlap_content_one = 0
nontrivial_projectors = [0, 0, 0]
joint_jk = 0
rational_and_other_projectors = 0
witness_unequal_conjugate = 0
fixtures = 0
for allowed, m, n, u, dyad in (
        (MASK, 31, 37, 2200, 4),
        (MASK, 31, 37, 3600, 8),
        (MASK, 31, 37, 20000, 64),
        (MASK ^ 32, 31, 37, 5500, 4),
        (MASK ^ 3, 7, 31, 3100, 8),
        (MASK, 37, 41, 2500, 1),
        (MASK, 31, 37, 9000, 16),
        (MASK, 31, 37, 5000, 4),
        (MASK, 31, 37, 8000, 4),
        (MASK, 31, 37, 10000, 4),
):
    e, d = m * n, u * u
    orig = [[0] * 6 for _ in ROWS]
    regrouped = [[0] * 6 for _ in ROWS]
    for a, b in product(SUB[allowed], repeat=2):
        if a & b:
            continue
        ell = a & BAR[b]
        na, nb, r = NORM[a], NORM[b], NORM[ell]
        if not (dyad <= r < 2 * dyad and u < m * na and u < n * nb and na <= u and nb <= u):
            continue
        weight = rational_node(e * na * nb, d)
        if not weight:
            continue
        assert m * na < 7 * u and n * nb < 7 * u
        record(orig, phase(a, b), MU[a] * MU[b] * weight)
        direct_terms += 1
        if r > 1 and ideal_content(a) == ideal_content(b) == 1:
            nonunit_overlap_content_one += 1

    for lam in SUB[allowed]:
        if lam & 64 or BAR[lam] != lam:
            continue
        r = ideal_content(lam)
        if not dyad <= r < 2 * dyad:
            continue
        orientation_count = 2 ** (lam.bit_count() // 2)
        assert orientation_count == sum(1 for ell in SUB[lam] if ell | BAR[ell] == lam and not ell & BAR[ell])
        for x, y in product(SUB[allowed], SUB[allowed ^ lam]):
            na, nb = r * NORM[x], r * NORM[y]
            if not (u < m * na and u < n * nb and na <= u and nb <= u and m * na < 7 * u and n * nb < 7 * u):
                continue
            for j, k, v in product(SUB[x & y], SUB[x & BAR[y]], SUB[x & lam]):
                b_fixed = j | BAR[k]
                a_base = j | k
                assert not v & a_base
                a_fixed = v | a_base
                assert a_fixed & x == a_fixed and b_fixed & y == b_fixed
                X, Y = x ^ a_fixed, y ^ b_fixed
                assert not X & a_fixed and not Y & b_fixed
                assert not Y & lam
                Z = lam | Y
                assert NORM[Z] == r * r * NORM[Y]
                assert na == r * NORM[a_fixed] * NORM[X] and nb == r * NORM[b_fixed] * NORM[Y]
                assert e * na * nb == e * NORM[a_fixed] * NORM[b_fixed] * NORM[X] * NORM[Z]
                assert r % ideal_content(v | BAR[v]) == 0
                actual = phase(lam, x, y)
                assert actual == phase(a_fixed, b_fixed, X, Z)
                sign = MU[j] * MU[k] * MU[v] * MU[x] * MU[y]
                weight = rational_node(e * NORM[a_fixed] * NORM[b_fixed] * NORM[X] * NORM[Z], d)
                if not weight:
                    continue
                record(regrouped, actual, sign * orientation_count * weight)
                expanded_terms += 1
                for i, factor in enumerate((j, k, v)):
                    nontrivial_projectors[i] += bool(factor)
                joint_jk += bool(j & k)
                rational_and_other_projectors += bool(v and (j or k))
                witness_unequal_conjugate += bool(k and k != BAR[k])
    assert orig == regrouped
    fixtures += 1
assert nonunit_overlap_content_one > 0
assert all(nontrivial_projectors) and witness_unequal_conjugate > 0


def delta(x):
    return max(F(0), x - F(3, 4), x / 3 - F(1, 8), 5 * x / 6 - F(1, 2))


ordinary_cells = 0
joint_cells = 0
monotone_cells = 0
for a, b in product(range(65), repeat=2):
    e = F(a + b, 128)
    if e < F(1, 6):
        continue
    short, long = sorted((F(1, 2) - F(a, 128), F(1, 2) - F(b, 128)))

    def ordinary(eta):
        return (-eta + delta(max(F(0), long - eta)) + delta(short + eta)
                - max(F(0), e - F(1, 4))) / 2

    assert ordinary(F(1, 32)) <= 0
    above = ordinary(F(1, 32))
    for q in range(5, 17):
        value = ordinary(F(q, 128))
        assert value <= above
        above = value
        monotone_cells += 1
    if e >= F(1, 4):
        eta = max(F(0), F(1, 32) - 3 * (e - F(1, 4)) / 4)
        assert ordinary(eta) <= 0
        ordinary_cells += 1
    else:
        eta = max(F(0), F(1, 4) + e / 2 - short) / 4
        assert eta <= F(1, 32)
        assert min(short + eta, long - eta) >= F(1, 4) + e / 2 - 3 * eta
        assert -eta / 2 + max(F(0), F(1, 4) + e / 2 - min(short + eta, long - eta)) / 6 <= 0
        joint_cells += 1

receipt = {
    "passed": True,
    "scope": "Fresh formal six-root/raw-zero and signed projector control at actual split/inert norm labels, rational profile nodes, and exact exponent arithmetic. No analytic sieve inference from the fixtures.",
    "proof_sha256": DIGEST,
    "script_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
    "fixtures": fixtures,
    "direct_terms": direct_terms,
    "expanded_terms": expanded_terms,
    "nonunit_overlap_with_both_individual_contents_one": nonunit_overlap_content_one,
    "nontrivial_projector_terms": dict(zip(("j", "k", "v"), nontrivial_projectors, strict=True)),
    "joint_jk_terms": joint_jk,
    "rational_and_other_projector_terms": rational_and_other_projectors,
    "unequal_conjugate_k_terms": witness_unequal_conjugate,
    "ordinary_exponent_cells": ordinary_cells,
    "joint_exponent_cells": joint_cells,
    "monotonicity_cells": monotone_cells,
}
with OUT.open("x", encoding="utf-8") as stream:
    json.dump(receipt, stream, sort_keys=True, indent=2)
    stream.write("\n")
print(json.dumps(receipt, sort_keys=True))
