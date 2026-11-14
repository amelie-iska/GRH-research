#!/usr/bin/env python3
"""Reproduce the monograph's finite examples, without external services.

All elliptic-curve examples are deliberately tiny educational groups. Exact
integer checks are distinguished from floating-point visualization checks.
This file is not a cryptographic implementation or a security experiment.
"""
from __future__ import annotations

# These proof checks must not be silently removed by optimized Python.
if not __debug__:
    raise RuntimeError("Verification requires assertions; run without -O or PYTHONOPTIMIZE")

import argparse
import cmath
import hashlib
import itertools
import json
import math
from pathlib import Path


P_MOD, A_CURVE, B_CURVE = 17, 2, 2
Point = tuple[int, int] | None


def ec_add(p: Point, q: Point) -> Point:
    if p is None:
        return q
    if q is None:
        return p
    x, y = p
    xx, yy = q
    if x == xx and (y + yy) % P_MOD == 0:
        return None
    if p == q:
        slope = (3 * x * x + A_CURVE) * pow(2 * y, -1, P_MOD) % P_MOD
    else:
        slope = (yy - y) * pow(xx - x, -1, P_MOD) % P_MOD
    xxx = (slope * slope - x - xx) % P_MOD
    yyy = (slope * (x - xxx) - y) % P_MOD
    return xxx, yyy


def scalar_mul(k: int, p: Point) -> Point:
    result = None
    for _ in range(k):
        result = ec_add(result, p)
    return result


def show_point(p: Point):
    return "O" if p is None else list(p)


def check_curve() -> dict:
    finite_points = [(x, y) for x in range(P_MOD) for y in range(P_MOD)
                     if (y * y - x ** 3 - A_CURVE * x - B_CURVE) % P_MOD == 0]
    points = [None] + finite_points
    p = (5, 1)
    multiples = [scalar_mul(k, p) for k in range(19)]
    assert len(points) == 19 and set(multiples) == set(points)
    assert scalar_mul(19, p) is None
    assert all(scalar_mul(k, p) is not None for k in range(1, 19))
    for x, y in itertools.product(points, repeat=2):
        assert ec_add(x, y) in points
        assert ec_add(x, y) == ec_add(y, x)
    # Exhaustion is meaningful here: all 6,859 triples, including O and
    # exceptional vertical/tangent cases, are checked with exact modular ints.
    for x, y, z in itertools.product(points, repeat=3):
        assert ec_add(ec_add(x, y), z) == ec_add(x, ec_add(y, z))
    for d in range(19):
        q = scalar_mul(d, p)
        kernel = {(a, b) for a in range(19) for b in range(19)
                  if ec_add(scalar_mul(a, p), scalar_mul(b, q)) is None}
        assert kernel == {((-d * t) % 19, t) for t in range(19)}
    return {
        "field_modulus": 17, "a": 2, "b": 2, "group_order": 19,
        "generator": [5, 1], "generator_order": 19,
        "multiples": [{"k": k, "point": show_point(v)}
                      for k, v in enumerate(multiples)],
        "associativity_triples_checked": len(points) ** 3,
        "hidden_kernel_secrets_checked": 19,
        "arithmetic": "exact integer modular arithmetic",
    }


def check_fourier(q=7, d=3) -> dict:
    support = []
    maximum_error = 0.0
    total = 0.0
    for u in range(q):
        for v in range(q):
            amplitude = sum(cmath.exp(2j * math.pi * ((v - d * u) * t) / q)
                            for t in range(q)) / (q * math.sqrt(q))
            probability = abs(amplitude) ** 2
            predicted = 1 / q if (v - d * u) % q == 0 else 0
            maximum_error = max(maximum_error, abs(probability - predicted))
            total += probability
            if predicted:
                support.append({"u": u, "v": v, "probability_exact": f"1/{q}"})
    assert maximum_error < 1e-12 and abs(total - 1) < 1e-12
    return {"q": q, "secret": d, "support": support,
            "nonzero_u_success_exact": f"{q-1}/{q}",
            "max_float_probability_error": maximum_error,
            "probability_sum": total,
            "status": "floating-point check of a separately proved exact character identity"}


def matmul(a, b):
    return [[sum(x * y for x, y in zip(row, col)) for col in zip(*b)] for row in a]


def transpose(a):
    return [list(v) for v in zip(*a)]


def plus(a, b):
    return [[x + y for x, y in zip(u, v)] for u, v in zip(a, b)]


def check_order_hodge() -> dict:
    rows = []
    for t in range(-10, 11):
        a = [[0, 0], [1, t]]
        b = [[t, 0], [-1, 0]]
        assert matmul(b, a) == [[0, 0], [0, 0]]
        delta = plus(matmul(a, transpose(a)), matmul(transpose(b), b))
        assert delta == [[1 + t*t, 0], [0, 1 + t*t]]
        rows.append({"t": t, "hodge_diagonal": 1 + t*t})
    return {"parameter_checks": rows,
            "status": "exact examples; the polynomial identity is proved in the paper"}


def check_cone() -> dict:
    max_cone_error = max_norm_error = 0.0
    count = 0
    for i in range(41):
        for j in range(41):
            alpha, beta = 2 * math.pi * i / 41, 2 * math.pi * j / 41
            u = [math.cos(alpha) / math.sqrt(2), math.sin(alpha) / math.sqrt(2)]
            v = [math.cos(beta) / math.sqrt(2), math.sin(beta) / math.sqrt(2)]
            x = [(u[k] + v[k]) / math.sqrt(2) for k in range(2)]
            y = [(u[k] - v[k]) / math.sqrt(2) for k in range(2)]
            max_cone_error = max(max_cone_error, abs(sum(x[k]*y[k] for k in range(2))))
            max_norm_error = max(max_norm_error, abs(sum(z*z for z in x+y) - 1))
            count += 1
    assert max_cone_error < 1e-12 and max_norm_error < 1e-12
    return {"samples": count, "max_composition_residual": max_cone_error,
            "max_unit_sphere_residual": max_norm_error,
            "coordinates": "(x1,x2,y1,y2) in R^4; xy=0; squared norm=1",
            "status": "floating-point check of an explicit torus-link parameterization"}


def check_noise() -> dict:
    modulus = 97
    a = [[3, 7], [12, 5], [8, 11]]
    s, e, r, e1, e2, mu = [2, -1], [1, -1, 0], [1, 0, 1], [0, 1], -1, 48
    b = [sum(x*y for x, y in zip(row, s)) + err for row, err in zip(a, e)]
    u = [sum(a[i][j]*r[i] for i in range(3)) + e1[j] for j in range(2)]
    v = sum(bi*ri for bi, ri in zip(b, r)) + e2 + mu
    decoded_value = (v - sum(si*ui for si, ui in zip(s, u))) % modulus
    residual = sum(ei*ri for ei, ri in zip(e, r)) + e2 - sum(si*ei for si, ei in zip(s, e1))
    assert decoded_value == (mu + residual) % modulus
    bound = max(map(abs, e))*sum(map(abs, r)) + abs(e2) + sum(map(abs, s))*max(map(abs, e1))
    assert abs(residual) <= bound
    return {"modulus": modulus, "encoded_message": mu,
            "integer_residual": residual, "integer_bound": bound,
            "received_residue": decoded_value,
            "status": "exact educational correctness calculation; no security claim"}


def check_gauge() -> dict:
    angles = [0.2, -0.8, 1.1, 0.6]
    sites = [0.3, -1.4, 2.0, 0.5]
    edges = [cmath.exp(1j*x) for x in angles]
    gauge = [cmath.exp(1j*x) for x in sites]
    transformed = [gauge[i]*edges[i]*gauge[(i+1) % 4].conjugate() for i in range(4)]
    holonomy = math.prod(edges)
    transformed_holonomy = math.prod(transformed)
    residual = abs(holonomy - transformed_holonomy)
    assert residual < 1e-12
    return {"group": "U(1)", "plaquettes": 1, "gauge_invariance_residual": residual,
            "status": "floating-point finite gauge-identity illustration, not continuum Yang-Mills"}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path,
                        default=Path(__file__).resolve().parents[1] / "verification/examples.json")
    args = parser.parse_args()
    result = {
        "schema": 1,
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "elliptic_curve": check_curve(), "fourier": check_fourier(),
        "periodic_order": check_order_hodge(), "cone_link": check_cone(),
        "noise": check_noise(), "gauge": check_gauge(), "passed": True,
        "scope": "finite educational checks; no proof of a general cryptographic or quantum-field theorem",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"passed": result["passed"], "output": str(args.output),
                      "exact_ECC_associativity_triples": result["elliptic_curve"]["associativity_triples_checked"],
                      "finite_Fourier_support": result["fourier"]["support"]}, indent=2))


if __name__ == "__main__":
    main()
