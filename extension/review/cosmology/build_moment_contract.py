#!/usr/bin/env python3
"""Build an exact variance envelope for an explicit finite Gaussian model.

The model is Y=L xi, with independent ideal standard-normal coordinates.
L and the exported filters are interpreted as exact binary64 constants.
The numerical Cholesky construction selects L; it is not an interval proof
about the unrounded analytic covariance kernel or a proof about a PRNG.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "extension/site/data/cosmology-synthetic.json"


def encoded(value: object) -> bytes:
    return (json.dumps(value, indent=2, sort_keys=True, allow_nan=False) + "\n").encode()


def rational(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def scaled_dyadics(rows: list[list[float]]) -> tuple[list[list[int]], int]:
    ratios = [[float(x).as_integer_ratio() for x in row] for row in rows]
    exponent = max(d.bit_length() - 1 for row in ratios for _, d in row)
    integers = [[n << (exponent - (d.bit_length() - 1)) for n, d in row] for row in ratios]
    return integers, exponent


def build(output_dir: Path) -> dict:
    raw = DATA.read_bytes()
    dataset = json.loads(raw)
    points = np.asarray(dataset["points"], dtype=np.float64)
    filters = dataset["filter_weights"]
    if points.shape != (96, 3) or len(filters) != 288 or any(len(row) != 96 for row in filters):
        raise ValueError("The exact model requires the declared 96-point/288-filter catalog.")
    config = dataset["benchmark"]["configuration"]
    covariance = np.exp((np.clip(points @ points.T, -1.0, 1.0) - 1.0)
                        / config["correlation_length_parameter"] ** 2)
    covariance += config["independent_noise_sd"] ** 2 * np.eye(96)
    lower = np.linalg.cholesky(covariance)
    if not np.isfinite(lower).all():
        raise ValueError("The generated factor is not finite.")
    factor = {
        "schema": "grh-cosmology-noise-factor-v1",
        "model": "Y = L xi; xi has independent ideal standard-normal real coordinates",
        "coefficient_interpretation": "Each hexadecimal binary64 value is an exact dyadic rational.",
        "dimension": "96",
        "factor_hex": [[float(x).hex() for x in row] for row in lower],
    }
    factor_bytes = encoded(factor)
    lint, le = scaled_dyadics(lower.tolist())
    wint, we = scaled_dyadics(filters)
    denominator = 1 << (2 * (le + we))
    variances = []
    for weights in wint:
        transformed = [sum(weights[i] * lint[i][column] for i in range(column, 96))
                       for column in range(96)]
        variances.append(Fraction(sum(x * x for x in transformed), denominator))
    maximum = max(variances)
    scale = 10 ** 12
    ceiling = -(-(maximum.numerator * scale) // maximum.denominator)
    envelope = Fraction(ceiling, scale)
    if any(v > envelope for v in variances):
        raise ArithmeticError("Outward variance envelope failed.")
    model = {
        "schema": "grh-cosmology-moment-model-v1",
        "dataset_sha256": hashlib.sha256(raw).hexdigest(),
        "factor_sha256": hashlib.sha256(factor_bytes).hexdigest(),
        "builder_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "dimension": "96", "family_size": "288", "calibration_draws": "4095",
        "variance_upper_bound": rational(envelope),
        "maximum_exact_variance": rational(maximum),
        "maximum_variance_filter": str(variances.index(maximum)),
        "filter_variances": [rational(v) for v in variances],
        "model": "The finite null is Y=L xi with the exact factor in cosmology-noise-factor.json.",
        "moment_rule": "For k>=1, each score has E|score|^(2k) <= (2k-1)!! * variance_upper_bound^k.",
        "formal_scope": "The measure-theoretic bound is proved from moment hypotheses. The ideal Gaussian law and Gaussian moment identity are external model obligations.",
        "exact_scope": "All filter variances and their outward envelope use integer dyadic arithmetic, independently replayed with Fraction arithmetic.",
        "limits": ["No probability law for the fixed PCG64 output is asserted.",
                   "No interval enclosure of the analytic covariance kernel is asserted.",
                   "No observed sky or cosmological detection is modeled.",
                   "A data-adaptive threshold or expanded search needs its own testing contract."],
        "generation": {"numpy": np.__version__, "factor_method": "numerical Cholesky; returned binary64 coefficients define the exact finite model",
                       "covariance_reconstruction_max_abs": float(np.max(np.abs(lower @ lower.T - covariance))),
                       "filter_unit_variance_max_abs": float(max(abs(v - 1) for v in variances))},
    }
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "cosmology-noise-factor.json").write_bytes(factor_bytes)
    model_bytes = encoded(model)
    (output_dir / "cosmology-moment-model.json").write_bytes(model_bytes)
    return {"status": "generated", "filters": len(variances),
            "variance_upper_bound": rational(envelope), "maximum_exact_variance": rational(maximum),
            "dataset_sha256": model["dataset_sha256"], "factor_sha256": model["factor_sha256"],
            "model_sha256": hashlib.sha256(model_bytes).hexdigest()}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, default=ROOT / "extension/site/data")
    args = parser.parse_args()
    print(json.dumps(build(args.output_dir), indent=2))


if __name__ == "__main__":
    main()
