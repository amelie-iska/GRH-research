#!/usr/bin/env python3
"""Independently replay an exact finite weighted-gain witness.

The schema is produced by verify_toric_transport.weighted_gain_witness, but
this checker imports neither that producer nor Fraction. It uses integer
numerators, positive denominators, gcd and cross multiplication throughout.
All validation uses explicit conditions and remains active under -O/-OO.

CLI exit codes: 0 = a verified holding bound (including rates >= 1);
2 = a well-formed, accurately recorded witness whose bound does not hold;
1 = malformed, inconsistent or unreadable evidence. The contraction flag
concerns only the supplied finite matrix and requires a holding rate < 1.
Applying it to another update needs a separately proved gain envelope and
appropriate domain. This is neither an optimizer nor an authenticity check.

JSON rationals are reduced {numerator: decimal-string, denominator:
positive-decimal-string} objects. The CLI accepts at most 8 MiB and each
integer component at most 4096 decimal digits; these are parser resource
limits, not mathematical bounds on the boolean feasibility API.
"""
from __future__ import annotations

import argparse
import json
from math import gcd
from pathlib import Path
import re


MAX_WITNESS_BYTES = 8 * 1024 * 1024
MAX_INTEGER_DIGITS = 4096
FIELDS = {
    "schema_version", "kind", "gain", "weights", "rate", "row_lhs",
    "row_rhs", "row_slack", "row_bounds", "weighted_bound", "bound_holds",
    "certifies_contraction",
}
INTEGER = re.compile(r"(?:0|-?[1-9][0-9]*)")
POSITIVE_INTEGER = re.compile(r"[1-9][0-9]*")


def _fields(value, expected, label):
    if type(value) is not dict or any(type(key) is not str for key in value):
        raise ValueError(f"{label} must be an object with string keys")
    if set(value) != expected:
        raise ValueError(f"{label} has missing or unknown fields")


def _rational(value, label):
    _fields(value, {"numerator", "denominator"}, label)
    numerator, denominator = value["numerator"], value["denominator"]
    if type(numerator) is not str or type(denominator) is not str:
        raise ValueError(f"{label} components must be decimal strings")
    if (len(numerator.lstrip("-")) > MAX_INTEGER_DIGITS
            or len(denominator) > MAX_INTEGER_DIGITS):
        raise ValueError(f"{label} exceeds the integer parser limit")
    if not INTEGER.fullmatch(numerator) or not POSITIVE_INTEGER.fullmatch(denominator):
        raise ValueError(f"{label} is not a canonical signed/positive integer pair")
    n, d = int(numerator), int(denominator)
    if gcd(n, d) != 1:
        raise ValueError(f"{label} must be reduced with a positive denominator")
    return n, d


def _vector(value, size, label):
    if type(value) is not list or len(value) != size:
        raise ValueError(f"{label} must be a list matching the matrix dimension")
    return [_rational(item, f"{label}[{i}]") for i, item in enumerate(value)]


def _reduce(numerator, denominator):
    divisor = gcd(numerator, denominator)
    return numerator // divisor, denominator // divisor


def _add(left, right):
    return _reduce(left[0] * right[1] + right[0] * left[1],
                   left[1] * right[1])


def _multiply(left, right):
    return _reduce(left[0] * right[0], left[1] * right[1])


def _equal(left, right):
    return left[0] * right[1] == right[0] * left[1]


def _less_equal(left, right):
    return left[0] * right[1] <= right[0] * left[1]


def replay_weighted_gain_witness(witness):
    """Recompute every field; return a summary or raise ValueError.

    A correctly recorded negative feasibility result is valid evidence of
    rejection and returns status 'rejected'. A falsely recorded result raises
    ValueError. The summary never treats an unsuccessful bound as certified.
    """
    _fields(witness, FIELDS, "witness")
    if type(witness["schema_version"]) is not int or witness["schema_version"] != 1:
        raise ValueError("Unsupported witness schema version")
    if type(witness["kind"]) is not str or witness["kind"] != "weighted-gain":
        raise ValueError("Unsupported witness kind")
    raw_gain = witness["gain"]
    if type(raw_gain) is not list or not raw_gain:
        raise ValueError("gain must be a nonempty square matrix")
    size = len(raw_gain)
    gain = [_vector(row, size, f"gain[{i}]") for i, row in enumerate(raw_gain)]
    weights = _vector(witness["weights"], size, "weights")
    rate = _rational(witness["rate"], "rate")
    if any(value[0] < 0 for row in gain for value in row) or rate[0] < 0:
        raise ValueError("Gains and rate must be nonnegative")
    if any(weight[0] <= 0 for weight in weights):
        raise ValueError("Weights must be strictly positive")
    recorded = {name: _vector(witness[name], size, name)
                for name in ("row_lhs", "row_rhs", "row_slack", "row_bounds")}
    recorded_bound = _rational(witness["weighted_bound"], "weighted_bound")
    for name in ("bound_holds", "certifies_contraction"):
        if type(witness[name]) is not bool:
            raise ValueError(f"{name} must be a JSON boolean")

    holds, maximum = True, (0, 1)
    for i, row in enumerate(gain):
        lhs = (0, 1)
        for coefficient, weight in zip(row, weights):
            lhs = _add(lhs, _multiply(coefficient, weight))
        rhs = _multiply(rate, weights[i])
        slack = _add(rhs, (-lhs[0], lhs[1]))
        ratio = _reduce(lhs[0] * weights[i][1], lhs[1] * weights[i][0])
        expected = {"row_lhs": lhs, "row_rhs": rhs,
                    "row_slack": slack, "row_bounds": ratio}
        for name, value in expected.items():
            if not _equal(recorded[name][i], value):
                raise ValueError(f"{name}[{i}] does not match the exact inputs")
        holds = holds and _less_equal(lhs, rhs)
        if _less_equal(maximum, ratio):
            maximum = ratio

    contraction = holds and _less_equal(rate, (1, 1)) and not _equal(rate, (1, 1))
    if not _equal(recorded_bound, maximum):
        raise ValueError("weighted_bound is not the maximum exact row ratio")
    if witness["bound_holds"] != holds:
        raise ValueError("bound_holds disagrees with the exact inequalities")
    if witness["certifies_contraction"] != contraction:
        raise ValueError("certifies_contraction requires a holding bound and rate < 1")
    return {
        "status": "certified" if holds else "rejected",
        "dimension": size,
        "bound_holds": holds,
        "certifies_contraction": contraction,
        "weighted_bound": dict(witness["weighted_bound"]),
        "rate": dict(witness["rate"]),
        "arithmetic": "integer gcd and cross multiplication",
        "scope": "Exact bound for the supplied finite matrix; no optimization, "
                 "model gain-envelope, continuum or authenticity claim.",
    }


def _unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("Duplicate JSON object key")
        result[key] = value
    return result


def _reject_inexact_json(token):
    raise ValueError("JSON floats/nonfinite values are not exact rational pairs")


def load_weighted_gain_witness(payload):
    """Decode UTF-8 JSON while rejecting duplicate keys and float syntax."""
    if type(payload) is str:
        payload = payload.encode("utf-8")
    if type(payload) is not bytes:
        raise ValueError("Witness JSON must be UTF-8 bytes or a string")
    if len(payload) > MAX_WITNESS_BYTES:
        raise ValueError("Witness JSON exceeds the 8 MiB parser limit")
    return json.loads(payload.decode("utf-8"), object_pairs_hook=_unique_object,
                      parse_float=_reject_inexact_json, parse_constant=_reject_inexact_json)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("witness", type=Path)
    args = parser.parse_args()
    try:
        with args.witness.open("rb") as stream:
            payload = stream.read(MAX_WITNESS_BYTES + 1)
        report = replay_weighted_gain_witness(load_weighted_gain_witness(payload))
    except (OSError, ValueError, TypeError, UnicodeError, RecursionError) as error:
        print(json.dumps({"status": "invalid", "error": str(error)}))
        return 1
    print(json.dumps(report, indent=2))
    return 0 if report["bound_holds"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
