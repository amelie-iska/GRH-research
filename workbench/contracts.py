"""Small, exact certificate contracts. No floating-point or symbolic-code inputs.

A passing contract proves the displayed finite arithmetic proposition, not the
physical comparison inequality or statistical null assumptions that motivate it.
"""
from __future__ import annotations
import hashlib
import json
import re
from fractions import Fraction
from typing import Any

SCHEMA = "grh.workbench.certificate.v1"
MAX_DIM = 12
MAX_DIGITS = 96
SCOPES = {
    "heat": "Exact five-point stencil coefficients; not floating-point execution or a continuum PDE proof.",
    "gain": "Exact weighted comparison-matrix contraction; the model-to-matrix comparison remains an assumption.",
    "rank": "Exact finite Monte Carlo rank; probability validity additionally requires exchangeability of the complete frozen search statistic.",
    "risk": "Exact union-bound budget with a supplied null-model discrepancy allowance; individual event bounds and discrepancy are assumptions.",
    "mutation": "Exact skew-symmetric exchange-matrix and positive rational seed mutation; not a categorical or spectral equivalence certificate.",
}


def integer(value: Any, low: int, high: int, name: str = "integer") -> int:
    if type(value) is not int or not low <= value <= high:
        raise ValueError(f"{name} must be an integer in [{low}, {high}]")
    return value


def rational(value: Any) -> Fraction:
    """Only explicit integer or p/q strings; JSON numbers are never rationals."""
    if type(value) is not str or len(value) > 2 * MAX_DIGITS + 2:
        raise ValueError("Rational values must be bounded integer or p/q strings")
    if not re.fullmatch(r"-?(?:0|[1-9][0-9]*)(?:/[1-9][0-9]*)?", value):
        raise ValueError("Invalid rational syntax")
    parts = value.split("/")
    if any(len(p.lstrip("-")) > MAX_DIGITS for p in parts):
        raise ValueError("Rational exceeds digit budget")
    return Fraction(value)


def qstr(value: Fraction) -> str:
    if max(len(str(abs(value.numerator))), len(str(value.denominator))) > MAX_DIGITS:
        raise ValueError("Result exceeds rational digit budget")
    return f"{value.numerator}/{value.denominator}"


def keys(value: Any, required: set[str]) -> None:
    if type(value) is not dict or set(value) != required:
        raise ValueError("Unexpected or missing input fields")


def matrix(value: Any) -> list[list[int]]:
    if type(value) is not list or not 1 <= len(value) <= MAX_DIM:
        raise ValueError("Exchange matrix dimension outside budget")
    n = len(value)
    if any(type(row) is not list or len(row) != n for row in value):
        raise ValueError("Exchange matrix must be square")
    b = [[integer(x, -10**6, 10**6, "matrix entry") for x in row] for row in value]
    if any(b[i][j] != -b[j][i] for i in range(n) for j in range(n)):
        raise ValueError("Exchange matrix must be skew-symmetric")
    return b


def mutate(b: list[list[int]], k: int) -> list[list[int]]:
    b = matrix(b)
    k = integer(k, 0, len(b) - 1, "mutable vertex")
    positive = lambda x: max(x, 0)
    out = [[-b[i][j] if i == k or j == k else b[i][j]
            + positive(b[i][k]) * positive(b[k][j])
            - positive(-b[i][k]) * positive(-b[k][j])
            for j in range(len(b))] for i in range(len(b))]
    return matrix(out)


def seed_step(b: list[list[int]], x: list[Fraction], k: int) -> tuple[list[list[int]], list[Fraction]]:
    b = matrix(b)
    integer(k, 0, len(b) - 1)
    if len(x) != len(b) or any(type(v) is not Fraction or v <= 0 for v in x):
        raise ValueError("Positive rational seed coordinates required")
    # Bound exponent work before exponentiation, not merely its eventual output.
    if any(abs(b[i][k]) > 64 for i in range(len(b))):
        raise ValueError("Seed exponent budget exceeded")
    a, c = Fraction(1), Fraction(1)
    for i, v in enumerate(x):
        a *= v ** max(b[i][k], 0)
        c *= v ** max(-b[i][k], 0)
        qstr(a); qstr(c)
    y = x.copy()
    y[k] = (a + c) / x[k]
    qstr(y[k])
    return mutate(b, k), y


def tropical_step(b: list[list[int]], u: list[int], k: int) -> list[int]:
    b = matrix(b)
    integer(k, 0, len(b) - 1)
    if len(u) != len(b):
        raise ValueError("Tropical dimension mismatch")
    u = [integer(v, -10**6, 10**6, "valuation") for v in u]
    v = u.copy()
    v[k] = min(sum(max(b[i][k], 0) * u[i] for i in range(len(b))),
               sum(max(-b[i][k], 0) * u[i] for i in range(len(b)))) - u[k]
    return v


def gentle_check(vertices: int, arrows: list[list[int]], relations: list[list[int]]) -> dict:
    """Decide the finite-dimensional quadratic monomial gentle conditions.

    Arrows are ordered [source,target] pairs; relation [a,b] means first a then b.
    Distinct parallel arrows retain distinct indices. No derived claim is made.
    """
    integer(vertices, 1, 64, "vertices")
    if type(arrows) is not list or len(arrows) > 128 or type(relations) is not list:
        raise ValueError("Invalid quiver")
    for a in arrows:
        if type(a) is not list or len(a) != 2:
            raise ValueError("An arrow has two endpoints")
        for v in a: integer(v, 0, vertices - 1)
    rel = set()
    for r in relations:
        if type(r) is not list or len(r) != 2:
            raise ValueError("A relation has two arrow indices")
        a, b = (integer(v, 0, len(arrows) - 1) for v in r)
        if arrows[a][1] != arrows[b][0] or (a, b) in rel:
            raise ValueError("Noncomposable or duplicate relation")
        rel.add((a, b))
    degree = all(sum(a[0] == v for a in arrows) <= 2 and
                 sum(a[1] == v for a in arrows) <= 2 for v in range(vertices))
    allowed = [[] for _ in arrows]
    local = True
    for i, a in enumerate(arrows):
        succ = [j for j, b in enumerate(arrows) if a[1] == b[0]]
        pred = [j for j, b in enumerate(arrows) if b[1] == a[0]]
        allowed[i] = [j for j in succ if (i, j) not in rel]
        local &= all(count <= 1 for count in (
            sum((i,j) in rel for j in succ), len(allowed[i]),
            sum((j,i) in rel for j in pred), sum((j,i) not in rel for j in pred)))
    color = [0] * len(arrows)
    def acyclic(i: int) -> bool:
        if color[i] == 1: return False
        if color[i] == 2: return True
        color[i] = 1
        if not all(acyclic(j) for j in allowed[i]): return False
        color[i] = 2
        return True
    finite = all(acyclic(i) for i in range(len(arrows)))
    return {"degree_bound": degree, "unique_allowed_forbidden": local,
            "finite_dimensional": finite, "gentle": bool(degree and local and finite)}


def certificate(kind: str, inputs: dict) -> dict:
    if kind not in SCOPES:
        raise ValueError("Unknown contract kind")
    if kind == "heat":
        keys(inputs, {"r"})
        r = rational(inputs["r"])
        if not 0 <= r <= Fraction(1, 4):
            raise ValueError("The positive-stencil boundary is 0 <= r <= 1/4")
        normalized = {"r": qstr(r)}
        claim = {"weights": [qstr(1 - 4*r)] + [qstr(r)] * 4, "sum": "1/1"}
    elif kind == "gain":
        keys(inputs, {"matrix", "weights", "rate"})
        raw, ws = inputs["matrix"], inputs["weights"]
        if type(ws) is not list or not 1 <= len(ws) <= MAX_DIM:
            raise ValueError("Invalid weights")
        n = len(ws)
        if type(raw) is not list or len(raw) != n or any(type(row) is not list or len(row) != n for row in raw):
            raise ValueError("Gain dimension mismatch")
        g = [[rational(v) for v in row] for row in raw]
        w, q = [rational(v) for v in ws], rational(inputs["rate"])
        if any(v < 0 for row in g for v in row) or any(v <= 0 for v in w) or not 0 <= q < 1:
            raise ValueError("Nonnegative gains, positive weights and 0 <= rate < 1 required")
        slack = [q*w[i] - sum((g[i][j]*w[j] for j in range(n)), Fraction(0)) for i in range(n)]
        if any(v < 0 for v in slack): raise ValueError("Weighted gain inequality fails")
        normalized = {"matrix": [[qstr(v) for v in row] for row in g],
                      "weights": [qstr(v) for v in w], "rate": qstr(q)}
        claim = {"row_slack": [qstr(v) for v in slack]}
    elif kind == "rank":
        keys(inputs, {"draws", "exceedances"})
        n = integer(inputs["draws"], 1, 10**7, "draws")
        e = integer(inputs["exceedances"], 0, n, "exceedances")
        normalized = {"draws": n, "exceedances": e}
        claim = {"p": qstr(Fraction(e + 1, n + 1)), "resolution": qstr(Fraction(1, n + 1))}
    elif kind == "risk":
        keys(inputs, {"tests", "per_test", "drift", "alpha"})
        n = integer(inputs["tests"], 1, 10**7, "tests")
        p, d, a = (rational(inputs[k]) for k in ("per_test", "drift", "alpha"))
        if not all(0 <= v <= 1 for v in (p, d, a)): raise ValueError("Probabilities must be in [0,1]")
        total = n*p + d
        if total > a: raise ValueError("Family-wise risk budget exceeded")
        normalized = {"tests": n, "per_test": qstr(p), "drift": qstr(d), "alpha": qstr(a)}
        claim = {"upper_bound": qstr(total), "slack": qstr(a-total)}
    else:
        keys(inputs, {"matrix", "seed", "vertex"})
        b = matrix(inputs["matrix"])
        k = integer(inputs["vertex"], 0, len(b)-1)
        if type(inputs["seed"]) is not list: raise ValueError("Seed must be a list")
        x = [rational(v) for v in inputs["seed"]]
        bp, xp = seed_step(b, x, k)
        normalized = {"matrix": b, "seed": [qstr(v) for v in x], "vertex": k}
        claim = {"matrix": bp, "seed": [qstr(v) for v in xp]}
    return {"schema": SCHEMA, "kind": kind, "inputs": normalized,
            "claim": claim, "scope": SCOPES[kind]}


def canonical(value: dict) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True, allow_nan=False)


def replay(value: dict) -> dict:
    keys(value, {"schema", "kind", "inputs", "claim", "scope"})
    if value["schema"] != SCHEMA: raise ValueError("Unsupported certificate schema")
    expected = certificate(value["kind"], value["inputs"])
    if canonical(value) != canonical(expected): raise ValueError("Certificate is noncanonical or witness was altered")
    return expected


def digest(value: dict) -> str:
    replay(value)
    return hashlib.sha256(canonical(value).encode("ascii")).hexdigest()
