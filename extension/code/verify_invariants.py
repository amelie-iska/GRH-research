#!/usr/bin/env python3
"""Exact independent checks for the gentle-algebra and zeta chapters.

No external dependencies. These finite checks supplement the unbounded proofs
in the manuscript; they do not claim a general theorem from a finite search.
"""
from __future__ import annotations

# Refuse before imports or report writes when Python has disabled the checks.
if not __debug__:
    raise RuntimeError("Verification requires assertions; run without -O or PYTHONOPTIMIZE")

from collections import Counter
from fractions import Fraction
import hashlib
import itertools
import json
from pathlib import Path

NAMES = ["X1", "X2", "Y1", "Y2", "Z1", "Z2", "B1", "B2"]
SUPPORTS = [
    [0, 4], [5, 9], [0, 3, 8, 5], [4, 1, 6, 9],
    [1, 7, 3], [6, 2, 8], [1, 6, 8, 3], [2, 7],
]
GENERATORS = [[int(i in support) for i in range(10)] for support in SUPPORTS]


def in_semigroup(u):
    a1, a2, a3, a4, a5, b1, b2, b3, b4, b5 = u
    return (min(u) >= 0 and a1+a2 == a4+a5 and b1+b2 == b4+b5
            and a2+a3 == b2+b3 and a3+a4 == b3+b4)


def expand(coeffs):
    return [sum(c*g[i] for c, g in zip(coeffs, GENERATORS)) for i in range(10)]


def decompose(u):
    """Constructive proof in (G18), using only nonnegative subtraction."""
    assert in_semigroup(u)
    residual = list(u)
    result = [0]*8

    def remove(index, multiplicity):
        assert multiplicity >= 0
        result[index] += multiplicity
        for i, value in enumerate(GENERATORS[index]):
            residual[i] -= multiplicity*value
        assert in_semigroup(residual)

    d = residual[0]-residual[4]
    remove(2 if d >= 0 else 3, abs(d))
    assert residual[0] == residual[4] and residual[5] == residual[9]
    assert residual[1] == residual[3] and residual[6] == residual[8]
    remove(0, residual[0])
    remove(1, residual[5])
    remove(6, min(residual[1], residual[6]))
    if residual[1] > 0:
        remove(4, residual[1])
    elif residual[6] > 0:
        remove(5, residual[6])
    remove(7, residual[2])
    assert residual == [0]*10 and expand(result) == list(u)
    return result


def rational_rank(matrix):
    m = [[Fraction(v) for v in row] for row in matrix]
    row = 0
    for col in range(len(m[0])):
        pivot = next((i for i in range(row, len(m)) if m[i][col]), None)
        if pivot is None:
            continue
        m[row], m[pivot] = m[pivot], m[row]
        scale = m[row][col]
        m[row] = [v/scale for v in m[row]]
        for i in range(len(m)):
            if i != row:
                scale = m[i][col]
                m[i] = [a-scale*b for a, b in zip(m[i], m[row])]
        row += 1
        if row == len(m):
            break
    return row


def determinant(matrix):
    m = [[Fraction(v) for v in row] for row in matrix]
    det = Fraction(1)
    for col in range(len(m)):
        pivot = next((i for i in range(col, len(m)) if m[i][col]), None)
        if pivot is None:
            return Fraction(0)
        if pivot != col:
            m[col], m[pivot] = m[pivot], m[col]
            det = -det
        scale = m[col][col]
        det *= scale
        for i in range(col+1, len(m)):
            factor = m[i][col]/scale
            for j in range(col+1, len(m)):
                m[i][j] -= factor*m[col][j]
    return det


def verify_matching():
    relations = [
        [-1, -1, 1, 1, 0, 0, -1, 0],
        [0, 0, 0, 0, 1, 1, -1, -1],
    ]
    assert all(expand(r) == [0]*10 for r in relations)
    # The printed B2 in the first arXiv-v1 relation fails exact substitution.
    printed_relation = [-1, -1, 1, 1, 0, 0, 0, -1]
    assert expand(printed_relation) != [0]*10
    exponent_matrix = list(map(list, zip(*GENERATORS)))
    assert rational_rank(exponent_matrix) == 6
    count = 0
    for u in itertools.product(range(3), repeat=10):
        if in_semigroup(u):
            decompose(u)
            count += 1
    # Much larger exponents check the constructive path, without exhaustive claims.
    for k in range(1, 101):
        coefficients = [(k*(j+3)**2+17*j) % 10007 for j in range(8)]
        decompose(expand(coefficients))
    return {
        "bounded_coordinate_range": [0, 2],
        "candidate_vectors": 3**10,
        "all_feasible_vectors_decomposed": count,
        "large_constructed_vectors": 100,
        "exponent_matrix_rank": 6,
        "integer_kernel_basis": relations,
        "correct_relations": ["Y1*Y2=B1*X1*X2", "Z1*Z2=B1*B2"],
        "arxiv_v1_printed_first_relation_fails": True,
        "generators": dict(zip(NAMES, GENERATORS)),
        "proof_scope": "General generation, defining ideal and normality proved in chapter; finite checks supplement them."
    }


def verify_pencil():
    checked = 0
    # Includes singular A, so the numeric checks do not assume the dense chart.
    for k in range(-7, 8):
        A = [[k, 2], [3, k+1]]
        B = [[1-k, k*k], [2*k, -3]]
        for lam in range(-4, 5):
            block = [[A[0][0], A[0][1], -1, 0],
                     [A[1][0], A[1][1], 0, -1],
                     [B[0][0], B[0][1], -lam, 0],
                     [B[1][0], B[1][1], 0, -lam]]
            target = [[B[i][j]-lam*A[i][j] for j in range(2)] for i in range(2)]
            assert determinant(block) == determinant(target)
            checked += 1
    return {"exact_block_determinants_checked": checked,
            "identity": "det([[A,-I],[B,-lambda*I]])=det(B-lambda*A)"}


def verify_zeta():
    p = 17
    assert pow(3, (p-1)//2, p) == p-1  # u^2-3 is irreducible.
    def add(a, b):
        return ((a[0]+b[0]) % p, (a[1]+b[1]) % p)
    def mul(a, b):
        return ((a[0]*b[0]+3*a[1]*b[1]) % p,
                (a[0]*b[1]+a[1]*b[0]) % p)
    elements = list(itertools.product(range(p), repeat=2))
    square_counts = Counter(mul(y, y) for y in elements)
    n2 = 1 + sum(square_counts[add(add(mul(mul(x,x),x), mul((2,0),x)),(2,0))]
                 for x in elements)
    n1 = 1+sum((y*y-x*x*x-2*x-2) % p == 0
               for x in range(p) for y in range(p))
    assert n1 == 19 and n2 == 323
    a = p+1-n1
    assert n2 == p*p+1-(a*a-2*p)
    return {
        "curve": "y^2=x^3+2*x+2", "q": p, "N1": n1, "N2": n2,
        "extension_field": "F17[u]/(u^2-3)",
        "quadratic_nonresidue_check": pow(3,8,17),
        "numerator_coefficients_ascending": [1,-a,p],
        "arithmetic": "exact integer pairs modulo 17",
        "scope": "Point counts checked directly; the general zeta theorem remains an external theorem."
    }


def main():
    result = {"matching": verify_matching(), "schofield": verify_pencil(),
              "elliptic_zeta": verify_zeta(), "passed": True,
              "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    output = Path(__file__).resolve().parents[1]/"verification/invariants.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({"passed": True, "bounded_solutions": result["matching"]["all_feasible_vectors_decomposed"],
                      "pencil_checks": result["schofield"]["exact_block_determinants_checked"],
                      "N1": result["elliptic_zeta"]["N1"], "N2": result["elliptic_zeta"]["N2"]}))


if __name__ == "__main__":
    main()

