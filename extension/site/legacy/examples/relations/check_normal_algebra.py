#!/usr/bin/env python3
"""Construct actual arrow products, then recover finite normal coordinates.

All degrees are sparse, including million-degree powers. Deterministic exact
checks complement the unbounded Lean membership/span/bijection proof; they
are not a formal path-quotient or GRH certificate.
"""
from collections import defaultdict
from fractions import Fraction
from pathlib import Path
import argparse
import json
from check_normal_paths import keys, image, multiply, length, selector

ROOT = Path(__file__).resolve().parents[2]


def add(left, right):
    out = defaultdict(int, left)
    for coordinate, value in right.items():
        out[coordinate] += value
    return {coordinate: value for coordinate, value in out.items() if value}


def stationary(i):
    return {(b, i, i, 0): 1 for b in (1, 2)}


def arrow(b, j):
    return {(b, (j-1) % 5, j, int(j == 0)): 1}


def short_walk(b, i, j):
    steps = j-i if i < j else 5+j-i
    current, out = j, stationary(j)
    for _ in range(steps):
        out = multiply(arrow(b, current), out)
        current = (current-1) % 5
    assert current == i
    return out


def power(base, exponent):
    assert exponent >= 0
    out = {coordinate: 1 for b in (1, 2) for i in range(5)
           for coordinate in [(b, i, i, 0)]}
    while exponent:
        if exponent & 1:
            out = multiply(out, base)
        base = multiply(base, base)
        exponent //= 2
    return out


def witness(key):
    b, i, j, q = key
    if b == 0:
        return stationary(i)
    delta = int(i >= j)
    assert q >= delta
    return multiply(power(short_walk(b, i, i), q-delta), short_walk(b, i, j))


def normal_coordinates(matrix):
    """Read coefficients without assuming that the input is in the algebra."""
    coefficients = {}
    for i in range(5):
        value = matrix.get((1, i, i, 0), 0)
        if value:
            coefficients[0, i, i, 0] = value
    for (b, i, j, q), value in matrix.items():
        if (i < j or q > 0) and value:
            coefficients[b, i, j, q] = value
    return coefficients


def expand(coefficients):
    out = {}
    for key, value in coefficients.items():
        out = add(out, {coordinate: value*v for coordinate, v in witness(key).items()})
    return out


def reduce_field(matrix, modulus):
    return {key: (value % modulus if modulus else value)
            for key, value in matrix.items() if (value % modulus if modulus else value)}


def run():
    degrees = [0, 1, 2, 3, 7, 31, 1000, 1000003]
    basis = keys(degrees)
    for key in basis:
        assert witness(key) == image(key)
    for b in (1, 2):
        for i in range(5):
            for j in range(5):
                assert short_walk(b, i, j) == image((b, i, j, int(i >= j)))
    product_cases = 0
    for left in keys([0, 1]):
        for right in keys([0, 1]):
            product = multiply(witness(left), witness(right))
            assert expand(normal_coordinates(product)) == product
            product_cases += 1
    cases, nonzero_products = 0, 0
    for modulus in (None, 2, 3, 5):
        for case in range(50):
            coefficients = {}
            for n in range(13):
                key = basis[(case*19+n*43) % len(basis)]
                value = Fraction((case+n*5) % 19-9, n % 7+1) if modulus is None else (case+n*5) % modulus
                coefficients[key] = coefficients.get(key, 0)+value
            coefficients = reduce_field(coefficients, modulus)
            matrix = reduce_field(expand(coefficients), modulus)
            assert reduce_field(normal_coordinates(matrix), modulus) == coefficients
            for key in basis:
                actual = selector(key, matrix)
                assert (actual % modulus if modulus else actual) == coefficients.get(key, 0)
            right = add(short_walk(1, (case+2) % 5, case % 5), stationary(case % 5))
            product = reduce_field(multiply(matrix, right), modulus)
            assert reduce_field(expand(normal_coordinates(product)), modulus) == product
            nonzero_products += bool(product)
            cases += 1
    # These ambient matrices fail the pullback/upper-constant shape and cannot
    # be reconstructed as an A element by the normal expansion.
    controls = [{(1, 0, 0, 0): 1}, {(1, 4, 0, 0): 1}, {(2, 1, 1, 0): 1}]
    for matrix in controls:
        assert expand(normal_coordinates(matrix)) != matrix
    return dict(passed=True, genus=2, vertices=5, coefficient_fields=['Q', 'F2', 'F3', 'F5'],
                shortest_arrow_words=50, normal_preimages=len(basis),
                maximum_degree=max(degrees), maximum_path_length=max(map(length, basis)),
                product_roundtrips=product_cases, exact_expansions=cases,
                nonzero_generated_product_examples=nonzero_products,
                ambient_nonmembership_controls=len(controls), randomness='none',
                scope='Finite exact replay of actual arrow words and compressed arbitrary-degree cycle powers. Unbounded membership, normal span equality and actual A-valued bijectivity are separately Lean checked; no path-quotient universal property or GRH inference.')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=ROOT/'outputs/checks/2026-11-04-normal-path-algebra/exact.json')
    args = parser.parse_args()
    result = run()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
