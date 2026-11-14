#!/usr/bin/env python3
"""Replay the finite cosmology contract with an independent exact evaluator.

This audit checks arithmetic, provenance, and finite input boundaries. The
probability theorem still requires its stated measurable/integrable moment
hypotheses; this script does not test a physical cosmological noise law.
"""
from __future__ import annotations

import argparse
from copy import deepcopy
from datetime import datetime, timezone
from fractions import Fraction
import hashlib
import json
import math
from pathlib import Path
import subprocess
import sys
import tempfile

import cosmology_certificate as independent

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_OUTPUT = ROOT / "extension/review/final-pass/cosmology-moments"
SOURCES = (
    "extension/code/cosmology_certificate.py",
    "extension/code/verify_cosmology_moments.py",
    "extension/review/cosmology/build_moment_contract.py",
    "extension/site/cosmology-calibration-core.js",
    "extension/site/exact-rational.js",
    "extension/site/data/cosmology-synthetic.json",
    "extension/site/data/cosmology-moment-model.json",
    "extension/site/data/cosmology-noise-factor.json",
)
BASE = {"alpha": "1/20", "center": "0", "order": "8",
        "snr": "3/1", "threshold": "6/1", "width": "1"}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def reject(call, name: str) -> str:
    try:
        call()
    except (ValueError, TypeError, OverflowError, KeyError) as error:
        return type(error).__name__
    raise ValueError(f"Negative control accepted: {name}")


def parameters(**changes) -> dict:
    return BASE | changes


def cases() -> tuple[list, list]:
    valid = [{"name": f"recorded-snr-{snr}", "parameters": parameters(snr=f"{snr}/1")}
             for snr in (0, 1, 3, 5)]
    valid += [{"name": f"even-moment-order-{order}",
               "parameters": parameters(order=str(order))} for order in range(1, 17)]
    valid += [
        {"name": "capped-bound-at-one", "parameters": parameters(alpha="1/1", threshold="1/1", order="1")},
        {"name": "large-derived-denominator", "parameters": parameters(threshold="100/1", order="16")},
        {"name": "eighty-digit-rational-components",
         "parameters": parameters(threshold=f"{10**79+7}/{10**79+9}", order="16")},
        {"name": "tiny-positive-threshold", "parameters": parameters(threshold=f"1/{10**79+7}", order="16")},
        {"name": "rank-floor-equality", "parameters": parameters(snr="5/1", alpha="1/4096")},
        {"name": "rank-floor-below", "parameters": parameters(snr="5/1", alpha="1/8192")},
        {"name": "last-center-largest-width", "parameters": parameters(center="95", width="2", snr="6/1")},
        {"name": "first-width-fractional-snr", "parameters": parameters(center="42", width="0", snr="1/10")},
        {"name": "middle-center", "parameters": parameters(center="47", width="1", snr="37/10")},
    ]
    envelope = Fraction(1000000000001, 1000000000000)
    boundary = 288 * envelope / 100**2
    for name, value in (("equal", boundary), ("below", boundary-Fraction(1, 10**16)),
                        ("above", boundary+Fraction(1, 10**16))):
        valid.append({"name": "risk-budget-" + name,
                      "parameters": parameters(order="1", threshold="100/1",
                                               alpha=independent.text(value))})
    invalid = [
        ("unexpected-key", BASE | {"executable": "ignored"}),
        ("missing-key", {k: v for k, v in BASE.items() if k != "alpha"}),
        ("numeric-input", parameters(alpha=0.05)),
        ("boolean-input", parameters(center=True)),
        ("noncanonical-natural", parameters(center="00")),
        ("negative-natural", parameters(center="-1")),
        ("unreduced-rational", parameters(alpha="2/40")),
        ("decimal-as-rational", parameters(alpha="0.05")),
        ("nonfinite-text", parameters(threshold="NaN")),
        ("zero-denominator", parameters(threshold="1/0")),
        ("negative-denominator", parameters(threshold="1/-2")),
        ("negative-zero", parameters(snr="-0/1")),
        ("zero-threshold", parameters(threshold="0/1")),
        ("negative-threshold", parameters(threshold="-1/1")),
        ("threshold-too-large", parameters(threshold="101/1")),
        ("zero-alpha", parameters(alpha="0/1")),
        ("negative-alpha", parameters(alpha="-1/20")),
        ("alpha-too-large", parameters(alpha="11/10")),
        ("zeroth-moment", parameters(order="0")),
        ("unsupported-moment", parameters(order="17")),
        ("last-center-overflow", parameters(center="96")),
        ("width-overflow", parameters(width="3")),
        ("negative-snr", parameters(snr="-1/10")),
        ("snr-overflow", parameters(snr="61/10")),
        ("snr-off-control-grid", parameters(snr="1/3")),
        ("eighty-one-digit-denominator", parameters(threshold=f"1/{10**80+7}")),
        ("eighty-one-digit-numerator", parameters(threshold=f"{10**80+7}/{10**80+9}")),
        ("null-object", None),
        ("array-object", []),
    ]
    return valid, [{"name": name, "parameters": value} for name, value in invalid]


NODE_REPLAY = r"""
const fs=require('node:fs'), path=require('node:path');
const root=process.cwd(), payload=JSON.parse(fs.readFileSync(0,'utf8'));
const C=require(path.join(root,'extension/site/cosmology-calibration-core.js'));
const Q=require(path.join(root,'extension/site/exact-rational.js'));
const data=JSON.parse(fs.readFileSync(path.join(root,'extension/site/data/cosmology-synthetic.json')));
const model=JSON.parse(fs.readFileSync(path.join(root,'extension/site/data/cosmology-moment-model.json')));
const valid=payload.valid.map(c=>({name:c.name,result:C.evaluate(data,model,c.parameters)}));
const invalid=payload.invalid.map(c=>{
  try { C.evaluate(data,model,c.parameters); return {name:c.name,rejected:false}; }
  catch(e) { return {name:c.name,rejected:true,error:e.name}; }
});
const binary=payload.binary.map(c=>({name:c.name,rational:Q.format(C.binary64(c.value))}));
const nonfinite=[NaN,Infinity,-Infinity].map(x=>{
  try { C.binary64(x); return false; } catch(e) { return true; }
});
process.stdout.write(JSON.stringify({valid,invalid,binary,nonfinite}));
"""


def audit(output: Path) -> dict:
    output.mkdir(parents=True, exist_ok=True)
    before = {name: digest(ROOT / name) for name in SOURCES}
    valid, invalid = cases()
    binary_values = [
        ("positive-zero", 0.0), ("negative-zero", -0.0),
        ("smallest-subnormal", math.ulp(0.0)),
        ("largest-finite", sys.float_info.max),
        ("smallest-normal", sys.float_info.min),
        ("binary-one-third", 1.0/3.0), ("binary-pi", math.pi),
        ("negative-fraction", -0.1), ("integer-valued-float", 96.0),
    ]
    payload = {"valid": valid, "invalid": invalid,
               "binary": [{"name": n, "value": v} for n, v in binary_values]}
    process = subprocess.run(["node", "-e", NODE_REPLAY], input=json.dumps(payload),
                             cwd=ROOT, text=True, capture_output=True, timeout=60)
    require(process.returncode == 0 and not process.stderr,
            f"Node exact replay failed: {process.stderr[:1000]}")
    js = json.loads(process.stdout)
    require(len(js["valid"]) == len(valid) and len(js["invalid"]) == len(invalid),
            "Node result inventory differs.")
    replayed = []
    for case, observed in zip(valid, js["valid"]):
        expected = independent.evaluate_parameters(case["parameters"])
        require(observed == {"name": case["name"], "result": expected},
                "Independent exact result mismatch: " + case["name"])
        replayed.append(case | {"result": expected})
    results = {entry["name"]: entry["result"] for entry in replayed}
    for snr, rank in ((0, "1893/4096"), (1, "741/4096"),
                      (3, "7/2048"), (5, "1/4096")):
        require(results[f"recorded-snr-{snr}"]["rank_value"] == rank,
                "Frozen benchmark rank changed.")
    require(results["capped-bound-at-one"]["within_budget"] is True
            and Fraction(results["capped-bound-at-one"]["uncapped_family_bound"]) > 1,
            "The capped probability bound must not require the stronger uncapped premise.")
    require(results["rank-floor-equality"]["rank_at_most_alpha"] is True
            and results["rank-floor-below"]["rank_at_most_alpha"] is False,
            "Exact finite rank boundary changed.")
    require(results["risk-budget-equal"]["within_budget"] is True
            and results["risk-budget-below"]["within_budget"] is False
            and results["risk-budget-above"]["within_budget"] is True,
            "Exact moment risk boundary changed.")
    rejected = []
    for case, observed in zip(invalid, js["invalid"]):
        error = reject(lambda c=case: independent.evaluate_parameters(c["parameters"]), case["name"])
        require(observed["name"] == case["name"] and observed["rejected"] is True,
                "JavaScript accepted invalid parameter: " + case["name"])
        rejected.append({"name": case["name"], "python_error": error,
                         "javascript_error": observed["error"], "rejected_by_both": True})
    for (name, value), observed in zip(binary_values, js["binary"]):
        require(observed == {"name": name, "rational": independent.text(Fraction.from_float(value))},
                "Binary64 decoding differs: " + name)
    require(js["nonfinite"] == [True, True, True], "Nonfinite coefficient accepted.")
    variance = independent.verify_variance_model()
    tampering = []
    with tempfile.TemporaryDirectory(prefix="grh-cosmology-audit-") as temporary:
        model_path = Path(temporary) / "model.json"
        original = json.loads(independent.MODEL.read_text())
        for key in ("dataset_sha256", "factor_sha256"):
            model_path.write_text(json.dumps(original | {key: "0"*64}))
            error = reject(lambda: independent.evaluate_parameters(BASE, model_path=model_path), key)
            tampering.append({"name": key, "rejected": True, "error": error})
        model_path.write_text(json.dumps(original | {"variance_upper_bound": "3/4"}))
        error = reject(lambda: independent.verify_variance_model(model_path=model_path), "understated-envelope")
        tampering.append({"name": "understated-envelope", "rejected": True, "error": error})
    after = {name: digest(ROOT / name) for name in SOURCES}
    require(before == after, "Contract sources changed during verification.")
    artifacts = {
        "cases.json": {"schema": "grh-cosmology-moment-cases-v1", "cases": replayed},
        "negative-controls.json": {"invalid_parameters": rejected, "model_tampering": tampering},
        "variance-replay.json": variance,
        "binary64-replay.json": {"cases": js["binary"], "nonfinite_rejections": 3},
    }
    for name, body in artifacts.items():
        (output / name).write_text(json.dumps(body, indent=2, sort_keys=True) + "\n")
    record = {
        "schema": "grh-cosmology-moment-audit-v1", "status": "passed",
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "python_optimized": not __debug__, "python_version": sys.version.split()[0],
        "node_version": subprocess.check_output(["node", "--version"], text=True).strip(),
        "valid_cross_language_cases": len(valid), "invalid_parameter_cases": len(invalid),
        "exact_variances_replayed": variance["exact_variances_replayed"],
        "binary64_conversion_cases": len(binary_values), "nonfinite_rejections": 3,
        "model_tamper_rejections": len(tampering),
        "sources_unchanged_during_audit": True, "source_sha256": before,
        "artifact_sha256": {name: digest(output/name) for name in artifacts},
        "scope": [
            "Independent Python Fraction and JavaScript BigInt arithmetic agree on every returned field.",
            "All 288 variances are independently reconstructed from the full finite factor columns.",
            "The exact stored binary64 constants define the finite model; transcendental kernel evaluation and physical Gaussianity are not certified.",
            "The Lean measure bound remains conditional on its measurable, integrable, and even-moment assumptions.",
            "Calibration rank values have exact finite arithmetic; no exchangeability theorem or physical detection claim is asserted.",
            "Test counts identify separate evidence classes and are not an aggregate theorem count.",
        ],
    }
    (output / "verification.json").write_text(json.dumps(record, indent=2, sort_keys=True) + "\n")
    return record


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    try:
        record = audit(args.output)
    except (ValueError, OSError, subprocess.SubprocessError) as error:
        print(json.dumps({"status": "failed", "error": str(error)}))
        return 1
    print(json.dumps({key: record[key] for key in
                     ("status", "valid_cross_language_cases", "invalid_parameter_cases",
                      "exact_variances_replayed", "python_optimized")}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
