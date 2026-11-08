from collections import Counter
from fractions import Fraction as F
from functools import lru_cache
from hashlib import sha256
from itertools import product
import json
from math import prod
from pathlib import Path
import sys

NORMS = (7, 7, 13, 13, 19, 31, 43)
ORIENTATIONS = (1, -1, 1, -1, 1, 1, 1)
LABELS = frozenset(range(len(NORMS)))
COUNTS = Counter()


@lru_cache(None)
def norm(labels):
    return prod(NORMS[i] for i in labels)


def mu(labels):
    return (-1) ** len(labels)


@lru_cache(None)
def subsets(labels):
    ordered = sorted(labels)
    return tuple(frozenset(i for i, bit in zip(ordered, bits) if bit)
                 for bits in product((0, 1), repeat=len(ordered)))


def residue_table(q, orientation):
    generator = next(g for g in range(2, q)
                     if len({pow(g, j, q) for j in range(q-1)}) == q-1)
    root = pow(generator, (q-1)//6, q)
    index = {pow(root, i, q): i*orientation % 6 for i in range(6)}
    return tuple([None] + [index[pow(v, (q-1)//6, q)] for v in range(1, q)])


TABLES = tuple(map(residue_table, NORMS, ORIENTATIONS))
ROWS = tuple(
    tuple((s*(i+2)+s//(i+1)) % q for i, q in enumerate(NORMS))
    for s in range(18)
) + ((1,) * len(NORMS),)


def phase(powers, row):
    value = 0
    for ideal, exponent in powers:
        for p in ideal:
            root = TABLES[p][row[p]]
            if root is None:
                return None
            value += exponent * root
    return value % 6


def weight(y):
    if not 1 < y < 2:
        return (F(0), F(0))
    base = (y-1)**2*(2-y)**2
    return (base, base*(y-F(1,2)))


def update(acc, root, sign, profile):
    if root is None or profile == (0, 0):
        return
    acc[root, 0] += sign*profile[0]
    acc[root, 1] += sign*profile[1]


def array_value(d, m, n, U, D, row):
    E = norm(d)
    l1, l2 = F(U, norm(m)), F(U, norm(n))
    candidates = subsets(LABELS-d)
    left = tuple(z for z in candidates if l1 < norm(z) <= U)
    right = tuple(z for z in candidates if l2 < norm(z) <= U)
    direct, shortened = Counter(), Counter()
    if any(not row[i] for i in d):
        COUNTS["raw_d_mask_controls"] += 1
        return direct, shortened
    for a, b in product(left, right):
        x, y = norm(a), norm(b)
        assert E*x*y > U**2
        if not a & b:
            for c in subsets(LABELS - d - a - b):
                argument = F(E*x*y*norm(c), D)
                profile = weight(argument)
                if profile == (0, 0):
                    if c:
                        COUNTS["nonunit_primal_zero_controls"] += 1
                    continue
                assert not c
                COUNTS["live_unit_primal_terms"] += 1
                if a and b and a != b and x == y:
                    COUNTS["equal_norm_distinct_cutoff_terms"] += 1
                if l1 < 1 or l2 < 1:
                    COUNTS["live_subunit_terms"] += 1
                update(direct, phase(((a, 1), (b, 1), (c, 1)), row),
                       mu(d)*mu(a)*mu(b)*mu(c), profile)
        if x >= 7*l1 or y >= 7*l2:
            assert weight(F(E*x*y, D)) == (0, 0)
            COUNTS["independent_upper_cap_controls"] += 1
            continue
        profile = weight(F(E*x*y, D))
        if profile == (0, 0):
            continue
        for w in subsets(a & b):
            aa, bb = a-w, b-w
            assert not (aa | bb) & w
            assert l1/norm(w) < norm(aa) <= F(U, norm(w))
            assert l2/norm(w) < norm(bb) <= F(U, norm(w))
            assert norm(w)**2*norm(aa)*norm(bb) == x*y
            grouped_root = phase(((w, 2), (aa, 1), (bb, 1)), row)
            assert grouped_root == phase(((a, 1), (b, 1)), row)
            assert mu(a)*mu(b) == mu(aa)*mu(bb)
            update(shortened, grouped_root, mu(d)*mu(w)*mu(aa)*mu(bb), profile)
            COUNTS["shortened_raw_phase_checks"] += 1
            if w and grouped_root is None:
                COUNTS["nonunit_shortening_raw_zero_controls"] += 1
    return direct, shortened


def exact_arrays():
    for U, ratio in product((13, 19, 31, 37, 49), (F(1), F(5, 2), F(7, 2))):
        D = int(U*U*ratio)
        assert U**2 <= D <= F(7, 2)*U**2
        for d in subsets(LABELS):
            if not 1 < norm(d) < 2*D:
                continue
            for m in subsets(d):
                n = d-m
                if not m or not n:
                    continue
                for row in ROWS:
                    direct, expanded = array_value(d, m, n, U, D, row)
                    assert all(direct[key] == expanded[key] for key in direct.keys() | expanded.keys())
                    COUNTS["complete_unit_array_comparisons"] += 1


def exponent_controls():
    peak, tail_peak = F(0), F(0)
    for l1, l2 in product((F(i, 192) for i in range(97)), repeat=2):
        excess = (max(F(0), l1/3-F(1,8)) + max(F(0), l2/3-F(1,8)))/2
        power = F(3,4)+excess
        peak = max(peak, power)
        assert power <= F(19,24)
        if l1+l2 <= F(7,8):
            assert power <= F(37,48)
            tail_peak = max(tail_peak, power)
        if max(l1, l2) <= F(3,8):
            assert power == F(3,4)
            COUNTS["balanced_exponent_controls"] += 1
        COUNTS["dyadic_exponent_controls"] += 1
    assert peak == F(19,24) and tail_peak == F(37,48)
    for D, E, E1, R in product((97, 512, 10000), (1, 7, 49), (1, 3, 4), (1, 31, 625)):
        T2 = F(D, E*E1*R)
        assert T2*min(F(1), 1/T2) <= 1
        COUNTS["pointwise_equality_scalar_controls"] += 1


def main():
    exact_arrays()
    exponent_controls()
    for witness in ("live_unit_primal_terms", "equal_norm_distinct_cutoff_terms",
                    "live_subunit_terms", "shortened_raw_phase_checks",
                    "nonunit_shortening_raw_zero_controls", "raw_d_mask_controls"):
        assert COUNTS[witness] > 0, witness
    report = {
        "status": "pass",
        "scope": "fresh finite ideal/residue/projector checks and exact exponent arithmetic",
        "counts": dict(sorted(COUNTS.items())),
        "norms_by_prime_ideal_label": list(NORMS),
        "source_sha256": {
            str(path): sha256(path.read_bytes()).hexdigest()
            for path in [Path(__file__), Path(sys.argv[2])]
        },
    }
    with Path(sys.argv[1]).open("x") as stream:
        stream.write(json.dumps(report, indent=2, sort_keys=True)+"\n")
    print(json.dumps(report["counts"], sort_keys=True))


if __name__ == "__main__":
    main()

