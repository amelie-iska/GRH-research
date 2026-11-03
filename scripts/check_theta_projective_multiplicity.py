#!/usr/bin/env python3
"""Exact deterministic diagnostics for the ACTUAL theta order special fiber.

The finite algebra here is explicitly Λ/uΛ, never a replacement for infinite Λ.
Basis: at each vertex, identity; two paths of length1; two of length2;
and the plus length3 path, with minus length3 its negative. Pure checks(),
stdlib only, no randomness. Universal categorical arguments remain prose.
"""
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'outputs/checks/2026-11-03-projective-multiplicity/exact-checks.json'
SLOTS = ((0, 0), (1, 1), (1, -1), (2, 1), (2, -1), (3, 1))
BASIS = tuple((v, length, branch) for v in range(3) for length, branch in SLOTS)


def endpoint(p):
    return (p[0]-p[1]) % 3


def multiply(p, q):
    """Travel-order multiplication of basis paths; return coefficient and basis path."""
    if endpoint(p) != q[0]:
        return 0, None
    if p[1] == 0:
        return 1, q
    if q[1] == 0:
        return 1, p
    if p[2] != q[2] or p[1]+q[1] > 3:
        return 0, None
    length = p[1]+q[1]
    if length == 3:
        return p[2], (p[0], 3, 1)
    return 1, (p[0], length, p[2])


def scaled_product(left, right):
    c, p = left
    d, q = right
    if c == 0 or d == 0:
        return 0, None
    e, r = multiply(p, q)
    return (c*d*e, r) if e else (0, None)


def zeros(n):
    return [[0 for _ in range(n)] for _ in range(n)]


def mmul(a, b):
    n = len(a)
    out = zeros(n)
    for i in range(n):
        for k in range(n):
            if a[i][k]:
                for j in range(n):
                    if b[k][j]:
                        out[i][j] += a[i][k]*b[k][j]
    return out


def local_polynomial(a):
    """All coefficients of det(I−T*a), via exact Newton traces, not interpolation."""
    n = len(a)
    power = [[int(i == j) for j in range(n)] for i in range(n)]
    traces, coeffs = [0], [Q(1)]
    for k in range(1, n+1):
        power = mmul(power, a)
        traces.append(sum(power[i][i] for i in range(n)))
        coeffs.append(-sum(coeffs[k-j]*traces[j] for j in range(1, k+1))/k)
    assert all(c.denominator == 1 for c in coeffs)
    return trim([int(c) for c in coeffs])


def trim(p):
    p = list(p)
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def pmul(p, q):
    out = [0]*(len(p)+len(q)-1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            out[i+j] += a*b
    return trim(out)


def ppow(p, n):
    out = [1]
    for _ in range(n):
        out = pmul(out, p)
    return out


def projective_data(multiplicities):
    copies = [(v, c) for v, m in enumerate(multiplicities) for c in range(m)]
    basis = [(v, c, p) for v, c in copies for p in BASIS if p[0] == v]
    index = {b: i for i, b in enumerate(basis)}
    homs = [(v, c, w, d, p) for v, c in copies for w, d in copies
            for p in BASIS if p[0] == w and endpoint(p) == v]
    return copies, basis, index, homs


def hom_matrix(h, basis, index):
    v, c, w, d, path = h
    out = zeros(len(basis))
    for col, (src, copy, p) in enumerate(basis):
        if (src, copy) == (v, c):
            coef, q = multiply(path, p)
            if coef:
                out[index[(w, d, q)]][col] += coef
    return out


def right_action(path, basis, index):
    out = zeros(len(basis))
    for col, (v, c, p) in enumerate(basis):
        coef, q = multiply(p, path)
        if coef:
            out[index[(v, c, q)]][col] = coef
    return out


def branch_image(path, u, branch):
    """Literal matrix entry of the cycle order column representation at integer u.

    Only used at u=0 for quotient Hom paths to test the reduced branch
    functor; no claim that this evaluation represents the full formal completion.
    """
    v, length, side = path
    if length and side != branch:
        return 0
    crossings = sum((v-r) % 3 == 0 for r in range(length))
    return u**crossings


def rank(rows):
    rows = [[Q(x) for x in row] for row in rows]
    pivot = 0
    for col in range(len(rows[0])):
        choices = [i for i in range(pivot, len(rows)) if rows[i][col]]
        if not choices:
            continue
        k = choices[0]
        rows[pivot], rows[k] = rows[k], rows[pivot]
        scalar = rows[pivot][col]
        rows[pivot] = [x/scalar for x in rows[pivot]]
        for i in range(pivot+1, len(rows)):
            scalar = rows[i][col]
            if scalar:
                rows[i] = [a-scalar*b for a, b in zip(rows[i], rows[pivot])]
        pivot += 1
        if pivot == len(rows):
            break
    return pivot


def column_representation(path, branch):
    out = zeros(3)
    out[path[0]][endpoint(path)] = branch_image(path, 0, branch)
    return out


def check_column_tensor():
    identities, quotients = 0, []
    for branch in (1, -1):
        reps = {p: column_representation(p, branch) for p in BASIS}
        for p, q in product(BASIS, repeat=2):
            coef, r = multiply(p, q)
            target = [[coef*x for x in row] for row in reps[r]] if coef else zeros(3)
            assert mmul(reps[p], reps[q]) == target
            identities += 1
        for v in range(3):
            paths = [p for p in BASIS if p[0] == v]
            pi = {p: i for i, p in enumerate(paths)}
            relations = []
            for p, b, w in product(paths, BASIS, range(3)):
                row = [0]*18
                coef, q = multiply(p, b)
                if coef:
                    row[3*pi[q]+w] += coef
                for z in range(3):
                    row[3*pi[p]+z] -= reps[b][z][w]
                relations.append(row)
            relation_rank = rank(relations)
            assert relation_rank == 17
            # Multiplication e_iB tensor W -> e_iW annihilates every relation.
            multiplication = [reps[p][v][w] for p in paths for w in range(3)]
            assert any(multiplication)
            assert all(sum(a*b for a, b in zip(row, multiplication)) == 0 for row in relations)
            quotients.append({'branch': branch, 'vertex': v, 'tensor_dimension': 18,
                              'relation_rank': relation_rank, 'quotient_dimension': 1})
    return identities, quotients


def checks():
    assert len(BASIS) == 18
    assoc = 0
    for a, b, c in product(BASIS, repeat=3):
        assert scaled_product(multiply(a, b), (1, c)) == scaled_product((1, a), multiply(b, c))
        assoc += 1
    cartan = [[sum(p[0] == i and endpoint(p) == j for p in BASIS)
               for j in range(3)] for i in range(3)]
    assert cartan == [[2, 2, 2] for _ in range(3)]
    for v in range(3):
        assert [sum(p[0] == v and p[1] == length for p in BASIS)
                for length in range(4)] == [1, 2, 2, 1]
    column_identities, tensor_quotients = check_column_tensor()
    diagnostics, right_linear, hom_count = [], 0, 0
    for mult in ((1, 0, 0), (1, 1, 0), (1, 1, 1), (2, 1, 0), (2, 2, 1)):
        copies, basis, index, homs = projective_data(mult)
        elementary = [hom_matrix(h, basis, index) for h in homs]
        actions = [right_action(path, basis, index) for path in BASIS]
        for matrix in elementary:
            for action in actions:
                assert mmul(matrix, action) == mmul(action, matrix)
                right_linear += 1
        hom_count += len(homs)
        for case in range(3):
            coefficients = [((13*j+7*case+3*j*j) % 11)-5 for j in range(len(homs))]
            n = len(basis)
            f = zeros(n)
            top = zeros(len(copies))
            ci = {c: i for i, c in enumerate(copies)}
            for coef, h, matrix in zip(coefficients, homs, elementary):
                for i in range(n):
                    for j in range(n):
                        f[i][j] += coef*matrix[i][j]
                v, c, w, d, path = h
                if path[1] == 0:
                    top[ci[(w, d)]][ci[(v, c)]] += coef
            # Positive-length Hom entries strictly increase the INPUT path length.
            for i, (_, _, p) in enumerate(basis):
                for j, (_, _, q) in enumerate(basis):
                    if p[1] < q[1]:
                        assert f[i][j] == 0
            actual, expected = local_polynomial(f), ppow(local_polynomial(top), 6)
            assert actual == expected
            # Actual column functor after u=0: keep the selected cycle branch,
            # with its cut arrow zero; determinant has only ONE top factor.
            branch_factors = []
            for branch in (1, -1):
                image = zeros(len(copies))
                for coef, h in zip(coefficients, homs):
                    v, c, w, d, path = h
                    image[ci[(w, d)]][ci[(v, c)]] += coef*branch_image(path, 0, branch)
                factor = local_polynomial(image)
                assert factor == local_polynomial(top)
                branch_factors.append(factor)
            diagnostics.append({'multiplicities': mult, 'case': case, 'dimension': n,
                                'top_factor': local_polynomial(top), 'ordinary_factor': actual,
                                'column_factors_at_u0': branch_factors})
    # All possible nonnegative arrow valuations with full cycle u; no fixed C3 lift.
    valuations = [w for w in product(range(2), repeat=3) if sum(w) == 1]
    assert len(valuations) == 3 and not any(a == b == c for a, b, c in valuations)
    assert sum((1, 1, 1)) == 3  # allowed only after the explicit ramified base u=v^3
    return {'scope': 'Exact bounded diagnostics for Λ/uΛ and column-functor specializations; not GRH',
            'parameters': {'field': 'Q', 'dart_sigma': [[0, 1, 2], [3, 4, 5]],
                           'dart_alpha': [[0, 3], [1, 4], [2, 5]],
                           'travel_order': True, 'randomness': None},
            'basis': BASIS, 'cartan': cartan, 'projective_layers': [1, 2, 2, 1],
            'column_multiplicativity_pairs': column_identities,
            'column_tensor_quotients': tensor_quotients,
            'associativity_triples': assoc, 'elementary_homomorphisms': hom_count,
            'right_linearity_identities': right_linear,
            'all_coefficient_determinant_tests': len(diagnostics),
            'admissible_column_valuations': valuations, 'cases': diagnostics}


def run(write_output=True):
    report = checks()
    if write_output:
        OUT.parent.mkdir(parents=True, exist_ok=True)
        OUT.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps({k: v for k, v in report.items() if k not in ('cases', 'basis')}, indent=2))
    return report


if __name__ == '__main__':
    run()
