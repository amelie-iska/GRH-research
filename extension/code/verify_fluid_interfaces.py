#!/usr/bin/env python3
"""Independent finite checks for the fluid companion; no GPU or network needed."""
from __future__ import annotations

import datetime as dt
import hashlib
import json
import math
from pathlib import Path

import numpy as np
import scipy.linalg as sla
import sympy as sp

ROOT = Path(__file__).resolve().parents[2]
SEED = 20261113
RNG = np.random.default_rng(SEED)


def rank_mod(a: np.ndarray, prime: int = 101) -> int:
    a = np.asarray(a, dtype=np.int64).copy() % prime
    row = 0
    for col in range(a.shape[1]):
        candidates = np.flatnonzero(a[row:, col])
        if not len(candidates):
            continue
        pivot = row + int(candidates[0])
        a[[row, pivot]] = a[[pivot, row]]
        a[row] = a[row] * pow(int(a[row, col]), -1, prime) % prime
        for k in range(row + 1, a.shape[0]):
            a[k] = (a[k] - a[k, col] * a[row]) % prime
        row += 1
        if row == a.shape[0]:
            break
    return row


def cochains(length: int) -> tuple[np.ndarray, np.ndarray]:
    n = length * length
    d0, d1 = np.zeros((2 * n, n), dtype=np.int64), np.zeros((n, 2 * n), dtype=np.int64)
    vertex = lambda x, y: (y % length) * length + x % length
    for y in range(length):
        for x in range(length):
            j = vertex(x, y)
            d0[j, j], d0[j, vertex(x + 1, y)] = -1, 1
            d0[n + j, j], d0[n + j, vertex(x, y + 1)] = -1, 1
            d1[j, j] = 1
            d1[j, n + vertex(x + 1, y)] = 1
            d1[j, vertex(x, y + 1)] = -1
            d1[j, n + j] = -1
    return d0, d1


def dense_circuit(theta: list[float]) -> dict:
    identity = np.eye(2, dtype=np.complex128)
    x = np.array([[0, 1], [1, 0]], dtype=np.complex128)
    z = np.diag([1, -1])
    ry = lambda t: np.array([[math.cos(t / 2), -math.sin(t / 2)],
                             [math.sin(t / 2), math.cos(t / 2)]], dtype=np.complex128)
    rz = lambda t: np.diag(np.exp(np.array([-1j, 1j]) * t / 2))
    cx = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]], dtype=np.complex128)
    gates = [np.kron(ry(theta[0]), identity), np.kron(rz(theta[1]), identity),
             np.kron(identity, ry(theta[2])), np.kron(identity, rz(theta[3])), cx,
             np.kron(ry(0.4), identity), np.kron(identity, ry(-0.3))]
    psi = np.array([1, 0, 0, 0], dtype=np.complex128)
    for gate in gates:
        assert np.max(np.abs(gate.conj().T @ gate - np.eye(4))) < 5e-16
        psi = gate @ psi
    features = np.array([np.vdot(psi, op @ psi).real for op in
                         [np.kron(z, identity), np.kron(identity, z), np.kron(x, x)]])
    sigmoid = 1 / (1 + np.exp(-np.dot([1.4, -0.8, 0.6], features)))
    nu = 0.02 + 0.28 * sigmoid
    return {"angles": list(map(float, theta)), "amplitudes": [[float(v.real), float(v.imag)] for v in psi],
            "probabilities": (abs(psi) ** 2).tolist(), "features": features.tolist(),
            "norm": float(np.vdot(psi, psi).real), "nu": float(nu),
            "r": float(nu * 0.1 / (2 * np.pi / 16) ** 2)}


def initial(n: int, kind: str) -> np.ndarray:
    yy, xx = np.mgrid[:n, :n]
    wrap = lambda d: np.minimum(abs(d), n - abs(d))
    if kind == "point":
        p = np.zeros((n, n)); p[n // 2, n // 4] = 1
    elif kind == "stripe":
        p = 1 + 0.85 * np.cos(2 * np.pi * xx / n)
    else:
        p = np.exp(-(wrap(xx - n / 4) ** 2 + wrap(yy - n / 2) ** 2) / 2.2)
        p += 0.55 * np.exp(-(wrap(xx - 11 * n / 16) ** 2 + wrap(yy - 5 * n / 16) ** 2) / 2.2)
    return p / p.sum()


def heat(p: np.ndarray, r: float) -> np.ndarray:
    return (1 - 4 * r) * p + r * sum(np.roll(p, shift, axis) for axis in [0, 1] for shift in [-1, 1])


def entropy(p: np.ndarray) -> float:
    p = p[p > 0]
    return float(-np.dot(p, np.log2(p)))


def main() -> None:
    report: dict = {"status": "passed", "seed": SEED,
                    "checked_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
                    "representation": "CPU binary64 finite computations, symbolic identities, and exact integer/modular linear algebra"}
    grids = []
    for length in range(3, 9):
        d0, d1 = cochains(length)
        n = length * length
        assert np.count_nonzero(d1 @ d0) == 0
        assert np.count_nonzero(d0 @ np.ones(n, dtype=int)) == 0
        assert np.count_nonzero(np.ones(n, dtype=int) @ d1) == 0
        ranks = [rank_mod(d0), rank_mod(d1)]
        assert ranks == [n - 1, n - 1]
        lap = d0 @ d0.T + d1.T @ d1
        eigenvalues = sla.eigvalsh(lap.astype(float))
        assert eigenvalues.min() > -1e-12 and np.count_nonzero(abs(eigenvalues) < 1e-10) == 2
        u = RNG.normal(size=2 * n)
        energy_residual = abs(u @ lap @ u - (np.linalg.norm(d0.T @ u) ** 2 + np.linalg.norm(d1 @ u) ** 2))
        assert energy_residual < 1e-9
        grids.append({"L": length, "vertices": n, "edges": 2 * n, "faces": n,
                      "integer_composition_nonzeros": 0, "ranks": ranks, "rank_prime": 101,
                      "rank_certificate": "modular lower rank n-1 plus exact constant-vector/cosum upper rank n-1",
                      "betti": [1, 2, 1], "min_hodge_eigenvalue": float(eigenvalues.min()),
                      "hodge_nullity_numeric": 2, "quadratic_form_residual": float(energy_residual)})
    report["cochain_complexes"] = grids

    x, y, t, nu = sp.symbols("x y t nu", real=True)
    decay = sp.exp(-2 * nu * t)
    u, v = sp.sin(x) * sp.cos(y) * decay, -sp.cos(x) * sp.sin(y) * decay
    pressure = (sp.cos(2 * x) + sp.cos(2 * y)) * decay ** 2 / 4
    residuals = [sp.diff(u, x) + sp.diff(v, y),
                 sp.diff(u, t) + u * sp.diff(u, x) + v * sp.diff(u, y) + sp.diff(pressure, x) - nu * (sp.diff(u, x, 2) + sp.diff(u, y, 2)),
                 sp.diff(v, t) + u * sp.diff(v, x) + v * sp.diff(v, y) + sp.diff(pressure, y) - nu * (sp.diff(v, x, 2) + sp.diff(v, y, 2)),
                 sp.diff(v, x) - sp.diff(u, y) - 2 * sp.sin(x) * sp.sin(y) * decay]
    residuals = [sp.simplify(sp.trigsimp(expr)) for expr in residuals]
    assert residuals == [0, 0, 0, 0]
    expressions = [u, v, pressure, 2 * sp.sin(x) * sp.sin(y) * decay, decay ** 2 / 4, -nu * decay ** 2]
    evaluators = [sp.lambdify((x, y, t, nu), expr, "numpy") for expr in expressions]
    tg_fixtures = []
    for i in range(16):
        args = [float(RNG.uniform(0, 2 * np.pi)), float(RNG.uniform(0, 2 * np.pi)),
                float(RNG.uniform(0, 12)), float(RNG.uniform(0, 0.3))]
        values = [float(fn(*args)) for fn in evaluators]
        tg_fixtures.append(dict(zip(["u", "v", "pressure", "vorticity", "energyAverage", "energyDerivative"], values), args=args))
    xx, yy = np.meshgrid(np.arange(64) * 2 * np.pi / 64, np.arange(64) * 2 * np.pi / 64)
    average_errors = []
    for time, viscosity in [(0, 0), (1.5, 0.08), (7.2, 0.21)]:
        ux, vy = evaluators[0](xx, yy, time, viscosity), evaluators[1](xx, yy, time, viscosity)
        err = abs(np.mean((ux ** 2 + vy ** 2) / 2) - math.exp(-4 * viscosity * time) / 4)
        average_errors.append(float(err))
    assert max(average_errors) < 1e-15
    report["taylor_green"] = {"symbolic_divergence_momentum_curl_residuals": list(map(str, residuals)),
                               "sample_count": len(tg_fixtures), "energy_average_errors": average_errors,
                               "domain": "flat (R / 2pi Z)^2, unit density, zero force", "pressure_sign": "+(cos(2x)+cos(2y))*exp(-4nu*t)/4"}

    j = sp.Matrix([[3, 1], [1, 5]]); a = j - 4 * sp.eye(2)
    aa, bb, cc, dd = sp.symbols("a b c d", integer=True)
    matrix = lambda c, d: sp.Matrix([[c - d, d], [d, c + d]])
    assert a * a == 2 * sp.eye(2)
    assert j * j - 8 * j + 14 * sp.eye(2) == sp.zeros(2)
    assert sp.expand(matrix(aa, bb).det() - (aa ** 2 - 2 * bb ** 2)) == 0
    assert (matrix(aa, bb) * matrix(cc, dd) - matrix(aa * cc + 2 * bb * dd, aa * dd + bb * cc)).applyfunc(sp.expand) == sp.zeros(2)
    powers = [{"k": k, "matrix": np.array(j ** k).astype(np.int64).tolist(), "determinant": int((j ** k).det())} for k in range(7)]
    assert all(row["determinant"] == 14 ** row["k"] for row in powers)
    report["quadratic_order"] = {"exact_symbolic_identities": 4, "powers": powers,
                                 "limitation": "determinant identities; no independent reproduction of the full analytic singularity construction"}

    cases = [dense_circuit([0.72, -0.45, 1.1, 0.38]), dense_circuit([0, 0, 0, 0])]
    cases += [dense_circuit(RNG.uniform(-np.pi, np.pi, 4).tolist()) for _ in range(14)]
    gradient_errors, nu_gradient_errors = [], []
    for case in cases:
        theta = np.array(case["angles"])
        gradients, nu_gradients = [], []
        for k in range(4):
            direction = np.eye(4)[k]
            plus = dense_circuit((theta + np.pi / 2 * direction).tolist())
            minus = dense_circuit((theta - np.pi / 2 * direction).tolist())
            gradient = (np.array(plus["features"]) - minus["features"]) / 2
            epsilon = 1e-6
            finite_p = dense_circuit((theta + epsilon * direction).tolist())
            finite_m = dense_circuit((theta - epsilon * direction).tolist())
            finite = (np.array(finite_p["features"]) - finite_m["features"]) / (2 * epsilon)
            sigmoid = (case["nu"] - 0.02) / 0.28
            nu_gradient = 0.28 * sigmoid * (1 - sigmoid) * np.dot([1.4, -0.8, 0.6], gradient)
            gradient_errors.append(float(np.max(abs(gradient - finite))))
            nu_gradient_errors.append(float(abs(nu_gradient - (finite_p["nu"] - finite_m["nu"]) / (2 * epsilon))))
            gradients.append(gradient.tolist()); nu_gradients.append(float(nu_gradient))
        case["feature_gradients"] = gradients; case["nu_gradients"] = nu_gradients
        assert abs(case["norm"] - 1) < 2e-15 and 0 < case["r"] < 0.25
    assert max(gradient_errors) < 2e-9 and max(nu_gradient_errors) < 5e-10
    report["circuit"] = {"cases": len(cases), "gates": 7, "parameters": 4, "qubits": 2,
                          "reference": "independent NumPy dense Kronecker matrices; complex128; q0 is most significant bit",
                          "max_feature_shift_vs_finite_difference_error": max(gradient_errors),
                          "max_nu_chain_rule_error": max(nu_gradient_errors),
                          "training": "none", "hardware": "classical CPU simulation"}

    trajectories = []
    for r, count, kind in [(cases[0]["r"], 30, "peaks"), (0.12, 50, "stripe"), (0.25, 8, "point"), (0, 5, "peaks")]:
        p = initial(16, kind); last_h, last_e = entropy(p), float(np.sum((p - 1 / p.size) ** 2) / 2)
        entropy_increments, contrast_decreases, mass_errors = [], [], []
        for _ in range(count):
            p = heat(p, r)
            h, e = entropy(p), float(np.sum((p - 1 / p.size) ** 2) / 2)
            entropy_increments.append(h - last_h); contrast_decreases.append(last_e - e)
            mass_errors.append(abs(float(p.sum()) - 1)); last_h, last_e = h, e
        assert min(entropy_increments) > -1e-12 and min(contrast_decreases) > -1e-15
        assert min(p.ravel()) >= 0 and max(mass_errors) < 1e-13
        trajectories.append({"r": r, "steps": count, "kind": kind, "probabilities": p.ravel().tolist(),
                             "entropy": last_h, "contrast": last_e, "mass": float(p.sum()),
                             "min_entropy_increment": min(entropy_increments), "max_mass_error": max(mass_errors)})

    # A coherent mixed density matrix, independently checked on a 3x3 position torus.
    n = 3; dimension = n * n; r = 0.19
    unitaries = []
    for shift_x, shift_y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        shift = np.zeros((dimension, dimension), complex)
        for y0 in range(n):
            for x0 in range(n): shift[((y0 + shift_y) % n) * n + (x0 + shift_x) % n, y0 * n + x0] = 1
        assert np.array_equal(shift.conj().T @ shift, np.eye(dimension))
        unitaries.append(shift)
    kraus = [math.sqrt(1 - 4 * r) * np.eye(dimension)] + [math.sqrt(r) * shift for shift in unitaries]
    completeness = sum(k.conj().T @ k for k in kraus)
    unitality = sum(k @ k.conj().T for k in kraus)
    choi = sum(np.outer(k.ravel(order="F"), k.ravel(order="F").conj()) for k in kraus)
    mat = RNG.normal(size=(dimension, dimension)) + 1j * RNG.normal(size=(dimension, dimension))
    rho = mat @ mat.conj().T; rho /= np.trace(rho)
    evolved = sum(k @ rho @ k.conj().T for k in kraus)
    eig0, eig1 = sla.eigvalsh(rho), sla.eigvalsh(evolved)
    choi_eigen = sla.eigvalsh(choi)
    assert np.max(abs(completeness - np.eye(dimension))) < 1e-15
    assert np.max(abs(unitality - np.eye(dimension))) < 1e-15
    assert choi_eigen.min() > -1e-12 and eig1.min() > 0
    assert abs(np.trace(evolved) - 1) < 1e-14 and entropy(eig1) >= entropy(eig0) - 1e-13
    report["heat_channel"] = {"diagonal_grid": [16, 16], "trajectories": [{k: v for k, v in row.items() if k != "probabilities"} for row in trajectories],
                              "coherent_density_check_dimension": dimension, "choi_dimension": dimension ** 2,
                              "min_choi_eigenvalue": float(choi_eigen.min()),
                              "completeness_max_error": float(np.max(abs(completeness - np.eye(dimension)))),
                              "unitality_max_error": float(np.max(abs(unitality - np.eye(dimension)))),
                              "coherent_entropy_before": entropy(eig0), "coherent_entropy_after": entropy(eig1),
                              "scope": "random-unitary CPTP heat channel; not incompressible Navier-Stokes and not a GPU run"}
    tau, h = sp.symbols("tau h", positive=True)
    velocity_exponent, volume_exponent, energy_exponent = -sp.Rational(1, 2) - h, sp.Rational(3, 2) - h, sp.Rational(1, 2) - 3 * h
    assert sp.simplify(2 * velocity_exponent + volume_exponent - energy_exponent) == 0
    report["scaling"] = {"symbolic_energy_exponent_residual": "0", "h_range": [0.002, 0.009],
                         "minimum_energy_exponent": 0.5 - 3 * 0.009,
                         "scope": "scaling illustration only; not the upstream singular solution"}
    report["script_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    output = ROOT / "extension/verification/fluids-python.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, indent=2, allow_nan=False) + "\n")
    fixtures = {"schema": "fluid-reference-v1", "seed": SEED, "source": "extension/code/verify_fluid_interfaces.py",
                "script_sha256": report["script_sha256"], "cochain_complexes": grids,
                "taylor_green": tg_fixtures, "renormalization_powers": powers,
                "circuit_cases": cases, "heat_trajectories": trajectories,
                "summary": {"cochain_grids": len(grids), "symbolic_pde_residuals": [0, 0, 0, 0],
                            "circuit_cases": len(cases), "feature_gradient_error": max(gradient_errors),
                            "nu_gradient_error": max(nu_gradient_errors), "coherent_channel_dimension": dimension}}
    target = ROOT / "extension/site/data/fluids-reference.json"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(fixtures, indent=2, allow_nan=False) + "\n")
    print(json.dumps({"status": report["status"], "cochain_grids": len(grids), "circuit_cases": len(cases),
                      "feature_gradient_error": max(gradient_errors), "nu_gradient_error": max(nu_gradient_errors),
                      "coherent_entropy_gain": entropy(eig1) - entropy(eig0), "fixture_bytes": target.stat().st_size}, indent=2))


if __name__ == "__main__":
    main()
