#!/usr/bin/env python3
"""A reproducible, deliberately non-CMB spherical Gaussian search experiment.

This is a small mathematical illustration of fixed-template matched filtering
and calibration of a full scan.  It does not load observations, estimate a CMB
power spectrum, simulate a CCC crossover, or detect a past-aeon message.

Run: python extension/review/cosmology/synthetic_search.py
Requires NumPy; no SciPy or external data is used.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import platform
import time
from pathlib import Path

import numpy as np


SEED = 20261113
N_POINTS = 96
CALIBRATION_DRAWS = 4095
VALIDATION_DRAWS = 2048
WIDTHS_RAD = (0.18, 0.30, 0.45)
CORRELATION_LENGTH = 0.35
INDEPENDENT_NOISE_SD = 0.20


def normal_upper_tail(value: float) -> float:
    return 0.5 * math.erfc(value / math.sqrt(2.0))


def fibonacci_sphere(n: int) -> np.ndarray:
    index = np.arange(n, dtype=np.float64)
    z = 1.0 - 2.0 * (index + 0.5) / n
    phi = index * math.pi * (3.0 - math.sqrt(5.0))
    radius = np.sqrt(1.0 - z * z)
    return np.column_stack((radius * np.cos(phi), radius * np.sin(phi), z))


def run(site_output: Path | None = None) -> dict:
    started = time.perf_counter()
    rng = np.random.default_rng(SEED)
    points = fibonacci_sphere(N_POINTS)
    dots = np.clip(points @ points.T, -1.0, 1.0)
    covariance = np.exp((dots - 1.0) / CORRELATION_LENGTH**2)
    covariance += INDEPENDENT_NOISE_SD**2 * np.eye(N_POINTS)
    lower = np.linalg.cholesky(covariance)
    angular_distances = np.arccos(dots)

    # Column order: center 0 / widths 0,1,2, then center 1 / widths 0,1,2, ...
    labels = []
    columns = []
    for center in range(N_POINTS):
        for width in WIDTHS_RAD:
            template = np.exp(-0.5 * (angular_distances[:, center] / width) ** 2)
            template -= template.mean()
            columns.append(template)
            labels.append({"center_index": center, "width_rad": width})
    templates = np.column_stack(columns)
    precision_templates = np.linalg.solve(covariance, templates)
    norms = np.sqrt(np.sum(templates * precision_templates, axis=0))
    filters = precision_templates / norms
    unit_variances = np.sum(filters * (covariance @ filters), axis=0)
    normalization_error = float(np.max(np.abs(unit_variances - 1.0)))
    if normalization_error > 1e-11:
        raise AssertionError(f"Filter variance error: {normalization_error}")

    # The seed and every experiment below were fixed before inspecting outputs.
    base_sky = lower @ rng.standard_normal(N_POINTS)
    calibration_skies = rng.standard_normal((CALIBRATION_DRAWS, N_POINTS)) @ lower.T
    calibration_maxima = np.max(calibration_skies @ filters, axis=1)
    sorted_maxima = np.sort(calibration_maxima)

    def global_p(statistic: float) -> tuple[float, int]:
        exceedances = int(CALIBRATION_DRAWS - np.searchsorted(sorted_maxima, statistic, side="left"))
        return (1.0 + exceedances) / (CALIBRATION_DRAWS + 1.0), exceedances

    injected_index = 1  # center 0, width 0.30 radians, declared in advance
    records = []
    for snr in (0.0, 1.0, 3.0, 5.0):
        sky = base_sky + snr * templates[:, injected_index] / norms[injected_index]
        scores = sky @ filters
        selected = int(np.argmax(scores))
        score = float(scores[selected])
        p, exceedances = global_p(score)
        records.append({
            "injected_matched_snr": snr,
            "injection_template_index": injected_index,
            "injection_template": labels[injected_index],
            "fixed_injection_template_score": float(scores[injected_index]),
            "fixed_injection_template_one_sided_p": normal_upper_tail(float(scores[injected_index])),
            "selected_template_index": selected,
            "selected_template": labels[selected],
            "scan_maximum": score,
            "selected_template_uncorrected_one_sided_p": normal_upper_tail(score),
            "global_rank_p": p,
            "calibration_exceedances": exceedances,
        })

    validation_skies = rng.standard_normal((VALIDATION_DRAWS, N_POINTS)) @ lower.T
    validation_maxima = np.max(validation_skies @ filters, axis=1)
    validation_counts = CALIBRATION_DRAWS - np.searchsorted(sorted_maxima, validation_maxima, side="left")
    validation_p = (1.0 + validation_counts) / (CALIBRATION_DRAWS + 1.0)
    rejected = int(np.sum(validation_p <= 0.05))

    # A separate quadratic-form calculation checks a genuine ring statistic.
    ring_mask = (angular_distances[:, 0] >= 1.0) & (angular_distances[:, 0] <= 1.4)
    ring_count = int(np.sum(ring_mask))
    if ring_count < 2:
        raise AssertionError("The declared ring needs at least two samples.")
    weights = ring_mask.astype(float) / ring_count
    matrix = np.diag(weights) - np.outer(weights, weights)
    ac = matrix @ covariance
    predicted_mean = float(np.trace(ac))
    predicted_variance = float(2.0 * np.trace(ac @ ac))
    ring_samples = np.einsum("bi,ij,bj->b", calibration_skies, matrix, calibration_skies)

    # Independent deterministic identities, not a broad statistical test suite.
    baseline_score = records[0]["fixed_injection_template_score"]
    snr_identity_error = max(abs(record["fixed_injection_template_score"] - baseline_score
                                 - record["injected_matched_snr"]) for record in records)
    if snr_identity_error > 1e-11:
        raise AssertionError(f"SNR normalization error: {snr_identity_error}")
    minimum_eigenvalue = float(np.linalg.eigvalsh(covariance)[0])
    if minimum_eigenvalue < INDEPENDENT_NOISE_SD**2 - 1e-12:
        raise AssertionError("The analytic covariance lower bound failed numerically.")

    result = {
        "schema": "ccc-synthetic-spherical-search-v1",
        "status": "completed",
        "evidence_scope": "Synthetic Gaussian mathematics demonstration; no observational CMB or CCC detection claim.",
        "seed": SEED,
        "random_generator": "NumPy default_rng / PCG64",
        "python": platform.python_version(),
        "numpy": np.__version__,
        "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "configuration": {
            "points": N_POINTS,
            "sampling": "deterministic Fibonacci sphere",
            "correlation_length_parameter": CORRELATION_LENGTH,
            "independent_noise_sd": INDEPENDENT_NOISE_SD,
            "covariance": "exp((dot(n_i,n_j)-1)/ell^2) + noise_sd^2 * delta_ij",
            "template": "exp(-angular_distance^2/(2*width_rad^2)), minus its discrete mean",
            "template_widths_rad": WIDTHS_RAD,
            "template_count": len(labels),
            "scan": "maximum positive normalized matched-filter score over every declared template",
            "calibration_draws": CALIBRATION_DRAWS,
            "validation_draws": VALIDATION_DRAWS,
            "rank_p_formula": "(1 + number of calibration maxima >= observed maximum)/(B + 1)",
            "rank_p_resolution": 1.0 / (CALIBRATION_DRAWS + 1),
        },
        "experiments": records,
        "independent_null_validation": {
            "nominal_threshold": 0.05,
            "rejections": rejected,
            "draws": VALIDATION_DRAWS,
            "observed_rejection_fraction": rejected / VALIDATION_DRAWS,
            "interpretation": "A finite-run diagnostic conditional on this one calibration sample; not a proof of exact 5% calibration.",
        },
        "ring_variance": {
            "center_index": 0,
            "inner_radius_rad": 1.0,
            "outer_radius_rad": 1.4,
            "samples_in_ring": ring_count,
            "predicted_mean": predicted_mean,
            "predicted_variance": predicted_variance,
            "monte_carlo_mean": float(np.mean(ring_samples)),
            "monte_carlo_variance_ddof_1": float(np.var(ring_samples, ddof=1)),
            "monte_carlo_draws": CALIBRATION_DRAWS,
        },
        "deterministic_checks": {
            "maximum_filter_variance_error": normalization_error,
            "maximum_injected_snr_identity_error": snr_identity_error,
            "covariance_minimum_eigenvalue": minimum_eigenvalue,
            "covariance_analytic_lower_bound": INDEPENDENT_NOISE_SD**2,
            "passed": True,
        },
        "wall_seconds": time.perf_counter() - started,
    }
    if site_output is not None:
        # The browser recomputes the identical declared statistic. It does not
        # generate new calibration samples or change the null covariance.
        catalog = {
            "points": points.tolist(),
            "base_sky": base_sky.tolist(),
            "labels": labels,
            "normalized_injection_templates": (templates / norms).T.tolist(),
            "filter_weights": filters.T.tolist(),
            "calibration_maxima_sorted": sorted_maxima.tolist(),
        }
        canonical = json.dumps(catalog, separators=(",", ":"), allow_nan=False)
        payload = {
            "schema": "ccc-synthetic-browser-v1",
            "scope": "Synthetic fixed-covariance Gaussian model; no observational data.",
            "catalog_sha256": hashlib.sha256(canonical.encode()).hexdigest(),
            "benchmark": result,
            **catalog,
        }
        site_output.parent.mkdir(parents=True, exist_ok=True)
        site_output.write_text(json.dumps(payload, separators=(",", ":"), allow_nan=False) + "\n", encoding="utf-8")
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path(__file__).with_name("synthetic-results.json"))
    parser.add_argument("--site-output", type=Path, help="Optionally export the exact fixed catalog and calibration for the browser companion.")
    args = parser.parse_args()
    result = run(args.site_output)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"output": str(args.output), "checks": result["deterministic_checks"],
                      "experiments": result["experiments"], "validation": result["independent_null_validation"]}, indent=2))


if __name__ == "__main__":
    main()
