#!/usr/bin/env python3
"""Independent 80-digit scalar/spectral references for the browser diagnostics.

These are numerical references, not interval arithmetic or a PDE proof.
Run from any directory; the default output is the versioned browser fixture.
"""
from __future__ import annotations

from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path

import mpmath as mp

ROOT = Path(__file__).resolve().parents[2]
mp.mp.dps = 80


def scalar(value: mp.mpf) -> dict:
    return {"value": float(value), "decimal": mp.nstr(value, 65)}


def taylor_green(n: int, nu_text: str = "0.08", time_text: str = "1.5") -> dict:
    nu, time = mp.mpf(nu_text), mp.mpf(time_text)
    h = 2 * mp.pi / n
    a = mp.exp(-2 * nu * time)
    sinc = mp.sin(h) / h
    lap = 8 * mp.sin(h / 2) ** 2 / h**2
    sin = [mp.sin(i * h) for i in range(n)]
    cos = [mp.cos(i * h) for i in range(n)]
    sin2 = [mp.sin(2 * i * h) for i in range(n)]
    pressure_factor = (sinc - mp.sin(2 * h) / (2 * h)) * a**2 / 2
    maximum = mp.mpf("0")
    for j in range(n):
        for i in range(n):
            u, v = a * sin[i] * cos[j], -a * cos[i] * sin[j]
            rx = nu * (lap - 2) * u + pressure_factor * sin2[i]
            ry = nu * (lap - 2) * v + pressure_factor * sin2[j]
            maximum = max(maximum, abs(rx), abs(ry))
    return {
        "options": {"n": n, "nu": float(nu), "time": float(time)},
        "amplitude": scalar(a), "curl_multiplier": scalar(sinc),
        "laplacian_multiplier": scalar(lap),
        "curl_error": scalar(2 * a * (1 - sinc)),
        "laplacian_error": scalar(a * (2 - lap)),
        "pde_residual": scalar(maximum), "energy": scalar(a**2 / 4),
    }


def heat(n: int, nu_text: str = "0.08", time_text: str = "1", kx: int = 1,
         ky: int = 0, steps: int | None = None) -> dict:
    nu, time = mp.mpf(nu_text), mp.mpf(time_text)
    h = 2 * mp.pi / n
    count = max(1, int(mp.ceil(5 * nu * time / h**2))) if steps is None else steps
    rate = nu * time / (count * h**2)
    lam = 4 * (mp.sin(kx * h / 2)**2 + mp.sin(ky * h / 2)**2) / h**2
    multiplier = 1 - nu * time * lam / count
    discrete = multiplier**count
    semi = mp.exp(-nu * time * lam)
    continuum = mp.exp(-nu * time * (kx*kx + ky*ky))
    return {
        "options": {"n": n, "nu": float(nu), "time": float(time),
                    "modeX": kx, "modeY": ky, "steps": count},
        "r": scalar(rate), "discrete_eigenvalue": scalar(lam),
        "multiplier": scalar(multiplier), "discrete_amplitude": scalar(discrete),
        "semidiscrete_amplitude": scalar(semi), "continuum_amplitude": scalar(continuum),
        "spatial_error": scalar(abs(semi - continuum)),
        "time_error": scalar(abs(discrete - semi)),
        "total_error": scalar(abs(discrete - continuum)),
    }


def plaquette(n: int, curvature_text: str = "1", quadratic_text: str = "0") -> dict:
    curvature, quadratic = mp.mpf(curvature_text), mp.mpf(quadratic_text)
    h = mp.mpf(1) / n
    mean = curvature + quadratic * h**2 / 6
    flux = h**2 * mean
    density = 4 * mp.sin(flux / 2)**2 / h**4
    radius = abs(quadratic) * h**2 / 6
    midpoint = radius * (2 * abs(curvature) + radius)
    small_angle = h**4 * (abs(curvature) + radius)**4 / 12
    return {
        "options": {"n": n, "curvature": float(curvature), "quadratic": float(quadratic)},
        "flux": scalar(flux), "cell_mean": scalar(mean),
        "stable_density": scalar(density), "target_density": scalar(curvature**2),
        "error": scalar(abs(density - curvature**2)),
        "midpoint_bound": scalar(midpoint), "small_angle_bound": scalar(small_angle),
    }


def main() -> None:
    levels = [8, 16, 32, 64]
    report = {
        "schema": "finite-resolution-reference-v1",
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "reference_arithmetic": {"library": "mpmath", "version": mp.__version__, "decimal_digits": mp.mp.dps},
        "generator_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "taylor_green": [taylor_green(n) for n in levels],
        "heat_modes": [heat(n) for n in levels] + [heat(8, "0.14", "1", 3, 3, 1)],
        "u1_plaquettes": [plaquette(n) for n in [1, 2, 4, 8, 16, 32, 4096, 65536]]
            + [plaquette(n, "1", "0.7") for n in [1, 2, 4, 8, 16, 32]]
            + [plaquette(1, "8")],
        "scope": "Independent high-precision evaluations of the declared Fourier and polynomial-curvature families. Decimal strings retain errors too small to resolve by subtracting binary64 densities. Not an interval certificate, continuum limit, or arbitrary-field model validation.",
    }
    target = ROOT / "extension/site/data/finite-resolution-reference.json"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({"path": str(target.relative_to(ROOT)),
                      "sha256": hashlib.sha256(target.read_bytes()).hexdigest(),
                      "taylor_green_cases": len(report["taylor_green"]),
                      "heat_cases": len(report["heat_modes"]),
                      "plaquette_cases": len(report["u1_plaquettes"])}, indent=2))


if __name__ == "__main__":
    main()
