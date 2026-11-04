#!/usr/bin/env python3
"""Independent sparse polynomial-pair normal-path diagnostics.

No production imports. Finite checks support, but do not replace, the
unbounded coefficient-selector proof reviewed in REVIEW.md.
"""
from fractions import Fraction as Q
from pathlib import Path
import json
import random


def admissible(branch, i, j, degree):
    return branch in (0, 1) and 0 <= i < 5 and 0 <= j < 5 and degree >= 0 and (i < j or degree > 0)


def monomial_path(branch, i, j, degree):
    assert admissible(branch, i, j, degree)
    length = 5*degree+j-i
    assert length > 0
    # Compute generator products in travel order; matrices act on columns.
    current, power = j, 0
    for _ in range(length):
        power += (current == 0)
        current = (current - 1) % 5
    assert current == i and power == degree
    return {(branch, current, j, power): 1}, length


def image(key):
    if key[0] == 'e':
        i = key[1]
        return {(0, i, i, 0): 1, (1, i, i, 0): 1}
    _, b, i, j, d = key
    assert admissible(b, i, j, d)
    return {(b, i, j, d): 1}


def coefficient(key, pair):
    if key[0] == 'e':
        i = key[1]
        return pair.get((0, i, i, 0), 0)
    return pair.get(tuple(key[1:]), 0)


def main():
    degrees = list(range(8)) + [10, 71, 1000]
    keys = [('e', i) for i in range(5)]
    lengths = []
    for branch in range(2):
        for i in range(5):
            for j in range(5):
                for d in degrees:
                    if admissible(branch, i, j, d):
                        key = ('p', branch, i, j, d)
                        actual, length = monomial_path(branch, i, j, d)
                        assert actual == image(key)
                        lengths.append(length)
                        keys.append(key)
    # Test the actual biorthogonal selector, including all stationary cases.
    for ki, key in enumerate(keys):
        for li, other in enumerate(keys):
            assert coefficient(key, image(other)) == (ki == li)
    rng = random.Random(20261103)
    combination_checks = 0
    for modulus in (None, 2, 3, 5):
        for _ in range(50):
            support = rng.sample(keys, 50)
            scalars = {key: rng.randrange(-7, 8) for key in support}
            actual = {}
            for key, scalar in scalars.items():
                for coordinate, value in image(key).items():
                    actual[coordinate] = actual.get(coordinate, 0)+scalar*value
            if modulus:
                actual = {coordinate: value % modulus for coordinate, value in actual.items()}
            for key in keys:
                expected = scalars.get(key, 0)
                if modulus:
                    expected %= modulus
                assert coefficient(key, actual) == expected
            combination_checks += 1
    # Reversing modular endpoint arithmetic and recovering the turn count.
    inversions = 0
    for start in range(5):
        for length in list(range(1, 201)) + [5001, 5004, 5005]:
            endpoint = (start-length) % 5
            q, rem = divmod(length-start+endpoint, 5)
            assert rem == 0 and admissible(0, endpoint, start, q)
            assert length == 5*q+start-endpoint
            inversions += 1
    result = dict(status='PASS', seed=20261103, normal_keys=len(keys),
                  walk_images=len(lengths), largest_walk_length=max(lengths),
                  selector_pairs=len(keys)**2, finite_combinations=combination_checks,
                  fields=['Q', 'F2', 'F3', 'F5'], inverse_endpoint_turn_checks=inversions,
                  caveat='Finite diagnostics only; unbounded proof is coefficientwise and must be checked separately in Lean/prose.')
    Path(__file__).with_name('oracle.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
