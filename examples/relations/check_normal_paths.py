#!/usr/bin/env python3
"""Exact normal-image coordinates for the infinite genus-two dessin algebra.

Sparse dictionaries store actual branch, matrix-entry and polynomial-degree
coordinates. Degrees are not expanded into dense arrays. No randomness,
training, installation or change to source data is involved.
"""
from collections import defaultdict
from fractions import Fraction
from pathlib import Path
import argparse
import json

ROOT = Path(__file__).resolve().parents[2]


def keys(degrees):
    return [(0, i, i, 0) for i in range(5)] + [
        (b, i, j, q) for b in (1, 2) for q in degrees
        for i in range(5) for j in range(5) if i < j or q > 0]


def length(key):
    b, i, j, q = key
    assert 0 <= i < 5 and 0 <= j < 5 and q >= 0
    if b == 0:
        assert i == j and q == 0
        return 0
    assert b in (1, 2) and (i < j or q > 0)
    return 5*q + j-i


def image(key):
    b, i, j, q = key
    length(key)  # Enforce the stationary/positive disjointness.
    return {(branch, i, j, q): 1 for branch in ((1, 2) if b == 0 else (b,))}


def recover_key(branch, ell, start):
    end = (start-ell) % 5
    return (branch if ell else 0, end, start, (ell-start+end)//5)


def selector(key, matrix):
    b, i, j, q = key
    return matrix.get((b or 1, i, j, q), 0)


def multiply(left, right):
    result = defaultdict(int)
    for (b, i, j, q), x in left.items():
        for (c, r, s, t), y in right.items():
            if b == c and j == r:
                result[b, i, s, q+t] += x*y
    return {key: value for key, value in result.items() if value}


def path_product(left, right):
    b, i, j, q = left
    c, r, s, t = right
    if j != r or (b and c and b != c):
        return {}
    ell = length(left)+length(right)
    return image(recover_key(b or c, ell, s))


def run():
    degrees = [0, 1, 2, 3, 4, 5, 7, 31, 1000, 1000003]
    basis = keys(degrees)
    images = [image(key) for key in basis]
    assert len(set(tuple(sorted(M.items())) for M in images)) == len(basis)
    for key in basis:
        ell = length(key)
        assert recover_key(key[0], ell, key[2]) == key
        assert bool(ell) == bool(key[0])
    for i, key in enumerate(basis):
        for j, matrix in enumerate(images):
            assert selector(key, matrix) == int(i == j)
    # Direct arrow-by-arrow replay, separate from the closed normal formula.
    walks = 0
    for b in (1, 2):
        for start in range(5):
            vertex, degree = start, 0
            for ell in range(1, 104):
                degree += int(vertex == 0)
                vertex = (vertex-1) % 5
                key = recover_key(b, ell, start)
                assert image(key) == {(b, vertex, start, degree): 1}
                walks += 1
    small = keys([0, 1, 2])
    for left in small:
        for right in small:
            assert multiply(image(left), image(right)) == path_product(left, right)
    combinations = 0
    for modulus in (None, 2, 3, 5):
        for case in range(50):
            coefficients = {}
            for n in range(19):
                key = basis[(case*17+n*53) % len(basis)]
                value = Fraction((case+3*n) % 17-8, n % 7+1) if modulus is None else (case+3*n) % modulus
                coefficients[key] = coefficients.get(key, 0)+value
            if modulus:
                coefficients = {key: value % modulus for key, value in coefficients.items()}
            matrix = defaultdict(int)
            for key, value in coefficients.items():
                for coordinate, scalar in image(key).items():
                    matrix[coordinate] += value*scalar
            for key in basis:
                actual = selector(key, matrix)
                if modulus:
                    actual %= modulus
                assert actual == coefficients.get(key, 0)
            combinations += 1
    rejected = 0
    for bad in [(1, i, j, 0) for i in range(5) for j in range(i+1)] + [(3, 0, 1, 0), (0, 0, 1, 0)]:
        try:
            length(bad)
        except AssertionError:
            rejected += 1
        else:
            raise AssertionError(('invalid normal key accepted', bad))
    return dict(passed=True, genus=2, vertices=5, degrees=degrees,
                normal_keys=len(basis), selector_pairs=len(basis)**2,
                maximum_degree=max(degrees), maximum_path_length=max(map(length, basis)),
                arrow_walk_steps=walks, product_pairs=len(small)**2,
                exact_combinations=combinations, fields=['Q', 'F2', 'F3', 'F5'],
                invalid_keys_rejected=rejected, randomness='none',
                scope='Finite exact diagnostics for unbounded definitions. Universal independence and coefficient recovery are separately Lean checked; generated-subalgebra spanning and the quotient equivalence are not inferred from these samples.')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=ROOT/'outputs/checks/2026-11-03-normal-path-basis/exact.json')
    args = parser.parse_args()
    result = run()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
