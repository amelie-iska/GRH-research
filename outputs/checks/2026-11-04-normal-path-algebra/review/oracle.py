#!/usr/bin/env python3
"""Independent exact finite diagnostics; no production-code imports.

Coordinates (factor,row,column,degree) represent actual polynomial pairs.
Constructs every tested image using only generator products, then checks
normal-coordinate multiplication and reconstruction in Q,F2,F3,F5.
No finite sample is represented as the unbounded proof.
"""
from collections import defaultdict
from fractions import Fraction as F
from pathlib import Path
import json
import random


def clean(a, modulus=None):
    if modulus:
        a = {c: value % modulus for c, value in a.items()}
    return {c: value for c, value in a.items() if value}


def add(a, b, modulus=None):
    out = defaultdict(int, a)
    for c, value in b.items():
        out[c] += value
    return clean(out, modulus)


def scale(scalar, a, modulus=None):
    return clean({c: scalar*v for c, v in a.items()}, modulus)


def mul(a, b, modulus=None):
    out = defaultdict(int)
    for (branch, i, j, q), value in a.items():
        for (other, r, s, d), coefficient in b.items():
            if branch == other and j == r:
                out[branch, i, s, q+d] += value*coefficient
    return clean(out, modulus)


def stationary(i):
    return {(0, i, i, 0): 1, (1, i, i, 0): 1}


ONE = {c: value for i in range(5) for c, value in stationary(i).items()}


def power(a, exponent):
    out = ONE
    while exponent:
        if exponent % 2:
            out = mul(out, a)
        a = mul(a, a)
        exponent //= 2
    return out


def arrow(branch, start):
    return {(branch, (start-1) % 5, start, int(start == 0)): 1}


def walk(branch, count, start):
    out, current = stationary(start), start
    for _ in range(count):
        out = mul(arrow(branch, current), out)
        current = (current-1) % 5
    return out


def short(branch, i, j):
    return walk(branch, j-i if i < j else 5+j-i, j)


def admissible(key):
    b, i, j, q = key
    return b in (0, 1) and i in range(5) and j in range(5) and q >= 0 and (i < j or q > 0)


def normal_image(key):
    if key[0] == 'e':
        return stationary(key[1])
    assert admissible(key)
    return {key: 1}


def reconstruct(pair, modulus=None):
    """Reject missing basis coordinates before reconstructing, not project away."""
    coefficients = {}
    for i in range(5):
        left, right = pair.get((0, i, i, 0), 0), pair.get((1, i, i, 0), 0)
        assert left == right
        if left:
            coefficients['e', i] = left
    for key, value in pair.items():
        b, i, j, q = key
        if q == 0 and i == j:
            continue
        assert admissible(key), ('forbidden coordinate', key)
        coefficients[key] = value
    expanded = {}
    for key, value in coefficients.items():
        expanded = add(expanded, scale(value, normal_image(key), modulus), modulus)
    assert expanded == clean(pair, modulus)
    return coefficients


def expected_product(x, y):
    if x[0] == 'e' and y[0] == 'e':
        return normal_image(x) if x == y else {}
    if x[0] == 'e':
        return normal_image(y) if x[1] == y[1] else {}
    if y[0] == 'e':
        return normal_image(x) if x[2] == y[1] else {}
    b, i, j, q = x
    c, r, s, d = y
    if b != c or j != r:
        return {}
    key = b, i, s, q+d
    assert admissible(key)
    return normal_image(key)


def main():
    degrees = [0, 1, 2, 3, 7, 31, 1000003]
    keys = [('e', i) for i in range(5)] + [
        (b, i, j, q) for b in range(2) for i in range(5) for j in range(5)
        for q in degrees if admissible((b, i, j, q))]
    membership = 0
    for key in keys:
        if key[0] == 'e':
            continue
        b, i, j, q = key
        q0 = 0 if i < j else 1
        assert q >= q0
        actual = mul(power(short(b, i, i), q-q0), short(b, i, j))
        assert actual == normal_image(key)
        assert reconstruct(actual) == {key: 1}
        membership += 1
    product_count = 0
    for x in keys:
        for y in keys:
            actual = mul(normal_image(x), normal_image(y))
            assert actual == expected_product(x, y)
            reconstruct(actual)
            product_count += 1
    # Actual randomly generated polynomial expressions, retaining all factors.
    # Addition/scaling/multiplication are independent polynomial pair operations.
    rng = random.Random(20261104)
    generators = [stationary(i) for i in range(5)] + [arrow(b, i) for b in range(2) for i in range(5)]
    expressions = 0
    for modulus in (None, 2, 3, 5):
        for trial in range(100):
            expression = {}
            for term in range(30):
                monomial = ONE
                for factor in range(rng.randrange(12)):
                    monomial = mul(rng.choice(generators), monomial, modulus)
                scalar = F(rng.randrange(-10, 11), rng.randrange(1, 8)) if modulus is None else rng.randrange(modulus)
                expression = add(expression, scale(scalar, monomial, modulus), modulus)
            coefficients = reconstruct(expression, modulus)
            # Every recovered positive support is an actual generated monomial.
            assert all(k[0] == 'e' or admissible(k) for k in coefficients)
            expressions += 1
    rejections = 0
    for invalid in [{(0, i, i, 0): 1} for i in range(5)] + [{(b, i, j, 0): 1} for b in range(2) for i in range(5) for j in range(i)]:
        try:
            reconstruct(invalid)
        except AssertionError:
            rejections += 1
        else:
            raise AssertionError('forbidden coordinate was accepted')
    result = dict(passed=True, seed=20261104, normal_keys=len(keys),
                  positive_generator_product_constructions=membership,
                  maximum_degree=max(degrees), product_comparisons=product_count,
                  exact_generated_expression_reconstructions=expressions,
                  fields=['Q', 'F2', 'F3', 'F5'], invalid_pairs_rejected=rejections,
                  scope='Independent finite diagnostics only; no production imports. Universal membership/span/bijection require literal Lean verification.')
    Path(__file__).with_name('oracle.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
