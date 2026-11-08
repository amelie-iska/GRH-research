from collections import Counter
from fractions import Fraction as F
from functools import lru_cache
from hashlib import sha256
from itertools import product
import json
from math import isqrt, prod
from pathlib import Path
import sys

# The two norm-7 and two norm-13 labels are distinct conjugate prime ideals.
NORMS = (7, 7, 13, 13, 19, 31, 37, 43, 61)
SMALL = frozenset(range(4))
EMPTY = frozenset()
COUNT = Counter()


@lru_cache(None)
def norm(labels):
    return prod(NORMS[i] for i in labels)


def mu(labels):
    return (-1) ** len(labels)


@lru_cache(None)
def subsets(labels):
    indices = sorted(labels)
    return tuple(frozenset(i for i, bit in zip(indices, bits) if bit)
                 for bits in product((0, 1), repeat=len(indices)))


@lru_cache(None)
def literal_cutoff_terms(d):
    return tuple((norm(a), norm(b), mu(a)*mu(b))
                 for a in subsets(d) for b in subsets(d-a))


def cutoff(d, t1, t2):
    return sum(sign for a, b, sign in literal_cutoff_terms(d)
               if a <= t1 and b <= t2)


def capacity_step(E, t1, t2):
    return int(E <= t1) + int(E <= t2) - 1


def correction_weight(m, n, t1, t2, small):
    if norm(m) <= t1 or norm(n) <= t2:
        return 0
    return 1 - sum(norm(m) > t1*NORMS[p] for p in small & m)


def live(E, t1, t2, h_weight=1):
    return E*h_weight < 14*t1*t2


def local_checks():
    for d in subsets(frozenset(range(7))):
        E = norm(d)
        capacities = {F(1), F(7), F(13), F(E)}
        for i, m in enumerate(subsets(d)):
            if i % 7 == 0:
                capacities.update(max(F(1), norm(m)+shift)
                                  for shift in (F(-1, 3), F(0), F(1, 3)))
        for t1, t2 in product(capacities, repeat=2):
            if not live(E, t1, t2):
                continue
            direct = cutoff(d, t1, t2)
            c = 0
            for m in subsets(d):
                n = d-m
                contribution = correction_weight(m, n, t1, t2, SMALL)
                c += contribution
                if norm(m) <= t1 or norm(n) <= t2:
                    continue
                negative_primes = 1-contribution
                assert negative_primes >= 0
                if live(E, t1, t2, 2):
                    assert negative_primes == 0
                    COUNT["no_small_prime_when_h_weight_ge_two"] += 1
                if negative_primes:
                    assert E > 7*t1*t2
                    COUNT["small_prime_subtractions"] += negative_primes
                if any(norm(m) == t1*NORMS[p] for p in SMALL & m):
                    COUNT["strict_small_prime_endpoint_controls"] += 1
            assert direct == mu(d)*(capacity_step(E,t1,t2)+c)
            assert direct == cutoff(d, t2, t1)
            if not d:
                assert direct == 1 and c == 0
                COUNT["unit_controls"] += 1
            COUNT["literal_local_correction_checks"] += 1


def scalar_weight(E):
    # Synthetic smooth profile values. Exact algebra checks only.
    return F(E**6, (E+5)**4*(E+11)**4)


def factorized_scalar(delta, free, Y, caps, small):
    result = F(0)
    for selected_sides in ((), (0,), (1,), (0, 1)):
        count = 2 ** len(selected_sides)
        for d_assignment in product(range(count), repeat=len(delta)):
            fixed = [frozenset(p for p, code in zip(sorted(delta), d_assignment)
                               if code == j) for j in range(count)]
            for free_assignment in product(range(-1, count), repeat=len(free)):
                q = [frozenset(p for p, code in zip(sorted(free), free_assignment)
                               if code == j) for j in range(count)]
                cells = [fixed[j] | q[j] for j in range(count)]
                d = frozenset().union(*cells)
                E = norm(d)
                if not Y <= E < 2*Y or not all(live(E, *cap) for cap in caps):
                    continue
                j_max = max(range(count), key=lambda j: (norm(q[j]), -j))
                assert norm(q[j_max])**count >= norm(d)/norm(delta)
                assert mu(d) == mu(delta)*prod(mu(qj) for qj in q)
                factor = 1
                for side, (t1, t2) in enumerate(caps):
                    if side not in selected_sides:
                        factor *= capacity_step(E, t1, t2)
                        continue
                    bit = selected_sides.index(side)
                    m = frozenset().union(*(cells[j] for j in range(count)
                                           if j & (1 << bit)))
                    n = d-m
                    factor *= correction_weight(m, n, t1, t2, small)
                result += mu(d)*factor*scalar_weight(E)
                if factor:
                    COUNT[f"nonzero_factorized_terms_{count}_cells"] += 1
                if j_max > 0:
                    COUNT["largest_free_cell_not_first"] += 1
    return result


def fixed_intersection_checks():
    # The fixed union consists of all small labels, the forbidden row prime
    # 19, and one active label of norm 31. The free cells avoid all six.
    eligible_fixed = frozenset({0, 1, 2, 3, 5})
    free = frozenset({6, 7, 8})
    for delta in subsets(eligible_fixed):
        physical = [delta | free_part for free_part in subsets(free)]
        dyads = sorted({2**(norm(d).bit_length()-1) for d in physical})
        for Y in dyads:
            root = max(1, isqrt(Y))
            for q in (F(1), F(2), F(5, 2)):
                cap1 = max(F(1), root/q)
                cap2 = max(F(1), F(root, 2))
                caps = ((cap1, cap2), (cap2, cap1+F(1,3)))
                direct = sum((mu(d)*cutoff(d,*caps[0])*cutoff(d,*caps[1])
                              *scalar_weight(norm(d)) for d in physical
                              if Y <= norm(d) < 2*Y and
                              all(live(norm(d), *cap) for cap in caps)), F(0))
                expanded = factorized_scalar(delta, free, Y, caps, SMALL)
                assert direct == expanded, delta, Y, caps, direct, expanded
                COUNT["fixed_intersection_weighted_scalar_checks"] += 1
                if 5 in delta:
                    COUNT["fixed_active_intersection_checks"] += 1


def main():
    local_checks()
    fixed_intersection_checks()
    for key in ("small_prime_subtractions", "strict_small_prime_endpoint_controls",
                "nonzero_factorized_terms_4_cells", "largest_free_cell_not_first",
                "fixed_active_intersection_checks"):
        assert COUNT[key] > 0, key
    receipt = {
        "status": "pass",
        "scope": "exact finite local and factorized signed cutoff controls",
        "norms_by_distinct_prime_ideal_label": list(NORMS),
        "counts": dict(sorted(COUNT.items())),
        "source_sha256": {
            str(path): sha256(path.read_bytes()).hexdigest()
            for path in [Path(__file__), Path(sys.argv[2])]
        },
    }
    with Path(sys.argv[1]).open("x") as stream:
        stream.write(json.dumps(receipt, indent=2, sort_keys=True)+"\n")
    print(json.dumps(receipt["counts"], sort_keys=True))


if __name__ == "__main__":
    main()

