#!/usr/bin/env python3
"""Independent exact replay of the browser laboratory certificate protocol.

Uses Python integers/Fraction, never the JavaScript producer or browser results.
The CLI also checks the trusted registry against local source and compiled type
records. A successful replay is not a fresh Lean kernel execution.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import re
import sys

SCHEMA = "grh-lab-certificate-v1"
MAX_BYTES = 524288
ROOT = Path(__file__).resolve().parents[2]
REGISTRY = ROOT / "extension/site/data/certificate-contracts.json"
CONTRACTS = {"hodge-family-v1", "quadratic-cover-v1", "weighted-gain-v1", "cosmology-calibration-v1"}
PATTERN = re.compile(r"(0|-[1-9][0-9]*|[1-9][0-9]*)/([1-9][0-9]*)\Z")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def canonical(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False, allow_nan=False)


def exact_keys(value: object, names: list[str], label: str) -> None:
    require(type(value) is dict and set(value) == set(names), f"{label} has missing, unknown, or invalid fields")


def rational(text: object, label: str = "parameter") -> Fraction:
    require(type(text) is str, f"{label} must be a canonical rational string")
    match = PATTERN.fullmatch(text)
    require(match is not None, f"{label} has invalid rational syntax")
    n, d = match.groups()
    require(len(n.lstrip("-")) <= 80 and len(d) <= 80, f"{label} exceeds the 80-digit parameter limit")
    value = Fraction(int(n), int(d))
    require(show(value) == text, f"{label} is not reduced")
    return value


def show(value: Fraction | int) -> str:
    value = Fraction(value)
    return f"{value.numerator}/{value.denominator}"


def bounded(text: object, low: int, high: int, label: str) -> Fraction:
    value = rational(text, label)
    require(low <= value <= high, f"{label} is outside its domain")
    return value


def vector(value: object, label: str) -> list[Fraction]:
    require(type(value) is list and len(value) == 2, f"{label} must contain two rationals")
    return [rational(x, label) for x in value]


def parse_certificate(text: str) -> dict:
    require(type(text) is str and len(text.encode("utf-8")) <= MAX_BYTES, "certificate exceeds the 512 KiB limit")

    def pairs(items):
        out = {}
        for key, value in items:
            require(key not in out, f"duplicate JSON key: {key}")
            out[key] = value
        return out

    def no_number(_):
        raise ValueError("JSON numbers are forbidden; use canonical rational strings")

    value = json.loads(text, object_pairs_hook=pairs, parse_int=no_number, parse_float=no_number, parse_constant=no_number)
    count = 0

    def walk(item, depth=0):
        nonlocal count
        count += 1
        require(depth <= 24 and count <= 12000, "certificate exceeds the nesting or node limit")
        if type(item) is dict:
            for entry in item.values():
                walk(entry, depth + 1)
        elif type(item) is list:
            for entry in item:
                walk(entry, depth + 1)

    walk(value)
    return value


def hodge(parameters: dict) -> dict:
    exact_keys(parameters, ["epsilon"], "Hodge parameters")
    epsilon = bounded(parameters["epsilon"], 0, 1, "epsilon")
    square = epsilon * epsilon
    return {"diagonal": [show(square), "1/1"], "least_eigenvalue": show(square),
            "smallest_positive_eigenvalue": show(square) if epsilon else "1/1",
            "kernel_dimension": "0/1" if epsilon else "1/1", "euler_index": "0/1",
            "positive_gap": bool(epsilon), "coercivity_constant": show(square)}


def cover(parameters: dict) -> dict:
    exact_keys(parameters, ["power", "x", "y"], "Cover parameters")
    k = bounded(parameters["power"], 0, 3, "power")
    require(k.denominator == 1, "power must be an integer rational")
    point = [bounded(parameters[key], 0, 1, key) for key in ("x", "y")]
    require(all((v * 100).denominator == 1 for v in point), "cover point is outside the exact hundredth grid")
    matrix = [[1, 0], [0, 1]]
    for _ in range(int(k)):
        # Independent column-by-column multiplication rather than the browser's row update.
        matrix = [[sum(matrix[i][l] * ((3, 1), (1, 5))[l][j] for l in range(2)) for j in range(2)] for i in range(2)]
    determinant = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    raw = [sum((matrix[i][j] * point[j] for j in range(2)), Fraction()) for i in range(2)]
    target = [value - value.numerator // value.denominator for value in raw]
    return {"matrix": [[show(v) for v in row] for row in matrix], "determinant": show(determinant),
            "degree_nonzero": determinant != 0, "target_mod_one": [show(v) for v in target],
            "lifted_frequency": [show(v) for v in matrix[0]], "integer_degree_identity": determinant == 14 ** int(k)}


def weighted(parameters: dict) -> dict:
    exact_keys(parameters, ["matrix", "weights", "rate"], "Weighted-gain parameters")
    require(type(parameters["matrix"]) is list and len(parameters["matrix"]) == 2, "matrix must have two rows")
    matrix = [vector(row, "matrix row") for row in parameters["matrix"]]
    weights, rate = vector(parameters["weights"], "weights"), rational(parameters["rate"], "rate")
    require(rate >= 0 and all(v >= 0 for row in matrix for v in row) and all(v > 0 for v in weights),
            "matrix/rate must be nonnegative and weights strictly positive")
    left = [sum((row[j] * weights[j] for j in range(2)), Fraction()) for row in matrix]
    right = [rate * value for value in weights]
    ratios = [left[i] / weights[i] for i in range(2)]
    holding = all(left[i] <= right[i] for i in range(2))
    return {"left_sides": [show(v) for v in left], "right_sides": [show(v) for v in right],
            "slacks": [show(right[i] - left[i]) for i in range(2)], "row_ratios": [show(v) for v in ratios],
            "maximum_ratio": show(max(ratios)), "bound_holds": holding,
            "certifies_contraction_of_supplied_gain": holding and rate < 1}


def evaluate(contract: str, parameters: dict) -> dict:
    if contract == "cosmology-calibration-v1":
        from cosmology_certificate import evaluate_parameters
        return evaluate_parameters(parameters)
    functions = {"hodge-family-v1": hodge, "quadratic-cover-v1": cover, "weighted-gain-v1": weighted}
    require(contract in functions, "no independent exact evaluator is installed for this contract")
    return functions[contract](parameters)


def replay(text_or_certificate: str | dict, registry: dict, expected_contract: str | None = None) -> dict:
    certificate = parse_certificate(text_or_certificate) if type(text_or_certificate) is str else text_or_certificate
    exact_keys(certificate, ["schema", "contract", "binding", "parameters", "result"], "Certificate")
    require(certificate["schema"] == SCHEMA, "unsupported certificate schema")
    contract = certificate["contract"]
    require(type(contract) is str and contract in CONTRACTS, "unknown contract")
    require(expected_contract is None or contract == expected_contract, "certificate belongs to another laboratory")
    require(registry.get("schema") == "grh-lab-contract-registry-v1" and registry.get("status") == "verified", "trusted registry is not verified")
    require(contract in registry["contracts"], "contract missing from trusted registry")
    require(canonical(certificate["binding"]) == canonical(registry["contracts"][contract]), "stale or altered theorem/source binding")
    result = evaluate(contract, certificate["parameters"])
    require(canonical(result) == canonical(certificate["result"]), "derived results fail independent exact replay")
    return {"schema": "grh-lab-independent-replay-v1", "status": "valid-instance", "contract": contract,
            "parameters": certificate["parameters"], "result": result, "lean_kernel_executed": False}


def verify_registry_sources(registry: dict, root: Path = ROOT) -> None:
    """Check provenance using trusted local paths, never paths from an import."""
    record = json.loads((root / "extension/lean/final-verification/verification.json").read_text())
    require(record.get("status") == "verified", "local Lean verification record is not verified")
    modules = {module["module"]: module for module in record["modules"]}
    for binding in registry["contracts"].values():
        for rel, expected in binding["runtime_sources"].items():
            require(Path(rel).is_relative_to("extension") and ".." not in Path(rel).parts, "invalid trusted runtime path")
            require(hashlib.sha256((root / rel).read_bytes()).hexdigest() == expected, f"stale runtime source binding: {rel}")
        require(binding["lean_version"] == record["lean_version"] and binding["mathlib_commit"] == record["mathlib_commit"] and binding["lean_binary_sha256"] == record["lean_binary_sha256"], "stale toolchain binding")
        for theorem in binding["theorems"]:
            module = modules[theorem["module"]]
            require(module["status"] == "verified" and module["exit_code"] == 0 and module["warning_count"] == 0, "theorem module was not verified")
            require(theorem["source"] == module["source"] and theorem["source_sha256"] == module["source_sha256"], "stale theorem source binding")
            require(hashlib.sha256((root / module["source"]).read_bytes()).hexdigest() == theorem["source_sha256"], "Lean source changed after its verification")
            printed = module["kernel_printed_types"][theorem["name"]]
            require(printed == theorem["printed_type"] and hashlib.sha256(printed.encode()).hexdigest() == theorem["type_sha256"], "altered compiled theorem type")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate", help="certificate JSON path, or - for stdin")
    parser.add_argument("--registry", type=Path, default=REGISTRY)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    try:
        registry = json.loads(args.registry.read_text())
        verify_registry_sources(registry)
        if args.certificate == "-":
            text = sys.stdin.buffer.read(MAX_BYTES + 1).decode("utf-8")
        else:
            with Path(args.certificate).open("rb") as source:
                text = source.read(MAX_BYTES + 1).decode("utf-8")
        report = replay(text, registry)
        report["local_source_bindings_checked"] = True
        rendered = json.dumps(report, indent=2, ensure_ascii=False) + "\n"
        if args.output:
            args.output.write_text(rendered)
        print(rendered, end="")
        return 0
    except (ValueError, TypeError, KeyError, OSError, UnicodeError, RecursionError) as error:
        print(json.dumps({"schema": "grh-lab-independent-replay-v1", "status": "rejected", "reason": str(error), "lean_kernel_executed": False}), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
