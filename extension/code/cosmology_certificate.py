#!/usr/bin/env python3
"""Independent Fraction replay of the exact finite cosmology contract.

This module does not import the JavaScript producer or the variance builder.
The probability conclusion remains conditional on the explicitly named
ideal Gaussian/moment assumptions; finite calibration ranks are arithmetic.
"""
from __future__ import annotations

from fractions import Fraction
from functools import lru_cache
import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "extension/site/data/cosmology-synthetic.json"
MODEL = ROOT / "extension/site/data/cosmology-moment-model.json"
FACTOR = ROOT / "extension/site/data/cosmology-noise-factor.json"
PARAMETER_KEYS = {"alpha", "center", "order", "snr", "threshold", "width"}


def text(q: Fraction) -> str:
    return f"{q.numerator}/{q.denominator}"


def rational(value: object, *, input_limit: int = 162) -> Fraction:
    if type(value) is not str or len(value) > input_limit or not re.fullmatch(r"(0|-[1-9][0-9]*|[1-9][0-9]*)/[1-9][0-9]*", value):
        raise ValueError("Expected a canonical rational string.")
    n, d = value.split("/")
    q = Fraction(int(n), int(d))
    if text(q) != value:
        raise ValueError("Rational input is not reduced.")
    return q


def natural(value: object, low: int, high: int) -> int:
    if type(value) is not str or len(value) > 6 or not re.fullmatch(r"0|[1-9][0-9]*", value):
        raise ValueError("Expected a canonical natural string.")
    n = int(value)
    if not low <= n <= high:
        raise ValueError("Natural input outside the finite domain.")
    return n


def parse_parameters(p: dict) -> dict:
    if type(p) is not dict or set(p) != PARAMETER_KEYS:
        raise ValueError("Unexpected cosmology parameters.")
    out = {key: natural(p[key], *bounds) for key, bounds in
           {"center": (0, 95), "width": (0, 2), "order": (1, 16)}.items()}
    for key in ("alpha", "snr", "threshold"):
        out[key] = rational(p[key])
        if any(len(component.lstrip("-")) > 80 for component in p[key].split("/")):
            raise ValueError("Scalar input exceeds the 80-digit component limit.")
    if not 0 < out["alpha"] <= 1 or not 0 < out["threshold"] <= 100:
        raise ValueError("Risk budget or positive threshold outside the contract.")
    if not 0 <= out["snr"] <= 6 or (10 * out["snr"]).denominator != 1:
        raise ValueError("SNR is not a supported control value.")
    return out


def _binary(value: object) -> Fraction:
    if type(value) is not float:
        raise ValueError("Expected the stored finite binary64 catalog.")
    return Fraction.from_float(value)


def dot(a: tuple[Fraction, ...], b: tuple[Fraction, ...]) -> Fraction:
    if len(a) != len(b):
        raise ValueError("Vector dimensions differ.")
    return sum((x * y for x, y in zip(a, b)), Fraction(0))


@lru_cache(maxsize=2)
def _catalog(data_bytes: bytes, model_bytes: bytes, factor_bytes: bytes) -> tuple:
    data, model, factor = json.loads(data_bytes), json.loads(model_bytes), json.loads(factor_bytes)
    if (data.get("schema") != "ccc-synthetic-browser-v1"
            or model.get("schema") != "grh-cosmology-moment-model-v1"
            or factor.get("schema") != "grh-cosmology-noise-factor-v1"
            or model.get("dataset_sha256") != hashlib.sha256(data_bytes).hexdigest()
            or model.get("factor_sha256") != hashlib.sha256(factor_bytes).hexdigest()
            or (model.get("dimension"), model.get("family_size"), model.get("calibration_draws")) != ("96", "288", "4095")):
        raise ValueError("Finite model provenance or dimensions do not match.")
    weights = tuple(tuple(_binary(x) for x in row) for row in data["filter_weights"])
    injections = tuple(tuple(_binary(x) for x in row) for row in data["normalized_injection_templates"])
    base = tuple(_binary(x) for x in data["base_sky"])
    calibration = tuple(_binary(x) for x in data["calibration_maxima_sorted"])
    if (len(weights) != 288 or len(injections) != 288 or len(base) != 96 or len(calibration) != 4095
            or any(len(row) != 96 for row in weights + injections)
            or any(a > b for a, b in zip(calibration, calibration[1:]))):
        raise ValueError("Invalid exact finite catalog.")
    variance = rational(model["variance_upper_bound"])
    if variance <= 0:
        raise ValueError("Variance envelope must be positive.")
    return weights, injections, tuple(dot(w, base) for w in weights), calibration, variance, model, factor


@lru_cache(maxsize=32)
def _responses(weights: tuple, injection: tuple) -> tuple:
    return tuple(dot(w, injection) for w in weights)


def evaluate_parameters(p: dict, *, data_path: Path = DATA, model_path: Path = MODEL,
                        factor_path: Path = FACTOR) -> dict:
    params = parse_parameters(p)
    weights, injections, base, calibration, variance, _, _ = _catalog(
        data_path.read_bytes(), model_path.read_bytes(), factor_path.read_bytes())
    response = _responses(weights, injections[params["center"] * 3 + params["width"]])
    scores = tuple(b + params["snr"] * a for b, a in zip(base, response))
    winner = max(range(len(scores)), key=scores.__getitem__)
    maximum = scores[winner]
    count = sum(x >= maximum for x in calibration)
    rank = Fraction(count + 1, len(calibration) + 1)
    coefficient = 1
    for j in range(1, params["order"] + 1):
        coefficient *= 2 * j - 1
    moment = coefficient * variance ** params["order"]
    power = params["threshold"] ** (2 * params["order"])
    raw = len(weights) * moment / power
    bound = min(Fraction(1), raw)
    return {
        "family_size": "288", "variance_upper_bound": text(variance),
        "even_exponent": str(2 * params["order"]), "gaussian_moment_coefficient": str(coefficient),
        "moment_upper_bound": text(moment), "threshold_power": text(power),
        "uncapped_family_bound": text(raw), "family_bound": text(bound),
        "within_budget": bound <= params["alpha"],
        "exact_scan_maximum": text(maximum), "winner_index": str(winner),
        "threshold_crossed": maximum >= params["threshold"],
        "calibration_exceedances": str(count), "calibration_draws": str(len(calibration)),
        "rank_value": text(rank), "rank_floor": text(Fraction(1, len(calibration) + 1)),
        "rank_at_most_alpha": rank <= params["alpha"],
        "probability_scope": "conditional_even_moment_bound",
        "rank_scope": "exact_finite_rank_no_probability_law_asserted",
        "score_scope": "exact_real_arithmetic_on_stored_binary64_constants",
    }


def verify_variance_model(*, data_path: Path = DATA, model_path: Path = MODEL,
                          factor_path: Path = FACTOR) -> dict:
    weights, _, _, _, envelope, model, factor = _catalog(
        data_path.read_bytes(), model_path.read_bytes(), factor_path.read_bytes())
    rows = factor.get("factor_hex")
    if not isinstance(rows, list) or len(rows) != 96 or any(not isinstance(row, list) or len(row) != 96 for row in rows):
        raise ValueError("Unexpected noise-factor shape.")
    lower = tuple(tuple(Fraction.from_float(float.fromhex(x)) for x in row) for row in rows)
    columns = tuple(tuple(row[j] for row in lower) for j in range(96))
    actual = tuple(sum((dot(w, col) ** 2 for col in columns), Fraction(0)) for w in weights)
    recorded = tuple(rational(x, input_limit=1024) for x in model["filter_variances"])
    if actual != recorded or any(v > envelope for v in actual):
        raise ValueError("Independent exact variance replay failed.")
    if text(max(actual)) != model["maximum_exact_variance"]:
        raise ValueError("Recorded maximum variance is inconsistent.")
    return {"status": "passed", "exact_variances_replayed": len(actual),
            "variance_upper_bound": text(envelope), "maximum_exact_variance": text(max(actual)),
            "method": "Independent Fraction dot products against every full factor column, then exact sums of squares.",
            "scope": "Exact variance arithmetic for the declared finite factor; the ideal Gaussian law and moment identity remain model assumptions."}
