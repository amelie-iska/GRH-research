#!/usr/bin/env python3
"""Bind laboratory contracts to fresh compiler-printed theorem types and sources.

Run after the formal and runtime sources are frozen. This does not compile Lean
or promote a numerical check to a theorem. It refuses stale compiler evidence.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
COMMON_RUNTIME = ["extension/site/exact-rational.js", "extension/site/certificate-bridge.js",
                  "extension/site/certificate-bridge-ui.js", "extension/code/verify_lab_certificate.py"]
CONTRACTS = {
    "hodge-family-v1": {
        "lab_url": "https://amelie-iska.github.io/GRH-research/index.html#hodge",
        "theorems": [("BridgeTheorems", "ResearchBridge.hodge_family_diagonal"),
                     ("LaboratoryContracts", "LaboratoryContracts.hodge_family_certificate"),
                     ("LaboratoryContracts", "LaboratoryContracts.hodge_family_kernel")],
        "runtime": ["extension/site/app.js", "extension/site/math.js"],
        "scope": "Exact rational Hodge-family diagonal, coercivity, positive-gap boundary and kernel equation; rendering and dimension reporting are separate finite computations."},
    "quadratic-cover-v1": {
        "lab_url": "https://amelie-iska.github.io/GRH-research/fluids.html#toral-cover",
        "theorems": [("FluidInterfaces", "FluidInterfaces.renormalization_power_determinant"),
                     ("LaboratoryContracts", "LaboratoryContracts.quadratic_cover_certificate")],
        "runtime": ["extension/site/fluids.js", "extension/site/fluid-core.js"],
        "scope": "Integer determinant identity and positivity for J powers. Exact point arithmetic is replayed; topological covering/fibre claims and trigonometric drawing are not newly kernel-checked here."},
    "weighted-gain-v1": {
        "lab_url": "https://amelie-iska.github.io/GRH-research/fluids.html#gain-title",
        "theorems": [("WeightedGainContracts", "WeightedGainContracts.row_ratio_iff"),
                     ("WeightedGainContracts", "WeightedGainContracts.matrix_action_weighted_bound")],
        "runtime": ["extension/site/fluids.js"],
        "scope": "Exact inequalities for the supplied nonnegative two-block gain matrix, positive weights and rate. Domain-valid domination of a physical update is an additional hypothesis."},
    "cosmology-calibration-v1": {
        "lab_url": "https://amelie-iska.github.io/GRH-research/cosmology.html#calibration-contract",
        "theorems": [("CosmologyCalibration", "CosmologyCalibration.scan_even_moment_threshold"),
                     ("CosmologyCalibration", "CosmologyCalibration.scan_uniform_even_moment_bound"),
                     ("CosmologyCalibration", "CosmologyCalibration.rank_fraction_bounds"),
                     ("CosmologyCalibration", "CosmologyCalibration.rank_fraction_threshold_iff")],
        "runtime": ["extension/site/cosmology-calibration-core.js", "extension/site/cosmology.js", "extension/site/cosmology-calibration-ui.js", "extension/code/cosmology_certificate.py",
                    "extension/site/data/cosmology-synthetic.json", "extension/site/data/cosmology-moment-model.json",
                    "extension/site/data/cosmology-noise-factor.json"],
        "scope": "Exact finite-score/rank arithmetic on stored binary64 constants, plus a probability bound conditional on measurable integrable scores and their true even-moment bounds. The ideal Gaussian law, Gaussian moment identity, PRNG law and physical observation model are separate obligations."},
}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build(root: Path = ROOT) -> dict:
    evidence = json.loads((root / "extension/lean/final-verification/verification.json").read_text())
    if evidence.get("status") != "verified" or not evidence.get("configuration_unchanged_during_check"):
        raise ValueError("A successful unchanged-configuration Lean verification record is required")
    modules = {module["module"]: module for module in evidence["modules"]}
    contracts = {}
    for contract, definition in CONTRACTS.items():
        theorems = []
        for module_name, name in definition["theorems"]:
            module = modules[module_name]
            if module["status"] != "verified" or module["exit_code"] or module["warning_count"] or not module["source_unchanged_during_check"]:
                raise ValueError(f"Unverified module: {module_name}")
            if digest(root / module["source"]) != module["source_sha256"]:
                raise ValueError(f"Source changed after compilation: {module_name}")
            printed = module["kernel_printed_types"][name]
            if not printed.startswith(name):
                raise ValueError(f"Printed declaration name mismatch: {name}")
            theorems.append({"module": module_name, "source": module["source"], "source_sha256": module["source_sha256"],
                             "source_url": "https://github.com/amelie-iska/GRH-research/blob/main/" + module["source"],
                             "name": name, "printed_type": printed, "type_sha256": hashlib.sha256(printed.encode()).hexdigest(),
                             "axioms": module["axioms_per_declaration"][name]})
        contracts[contract] = {"binding_schema": "grh-lab-source-type-binding-v1", "lean_version": evidence["lean_version"],
                               "lean_binary_sha256": evidence["lean_binary_sha256"], "mathlib_commit": evidence["mathlib_commit"],
                               "theorems": theorems,
                               "runtime_sources": {rel: digest(root / rel) for rel in COMMON_RUNTIME + definition["runtime"]},
                               "lab_url": definition["lab_url"],
                               "scope": definition["scope"]}
    return {"schema": "grh-lab-contract-registry-v1", "status": "verified",
            "meaning": "Bindings identify compiler-printed interfaces and reviewed sources; importing a certificate performs exact replay, not Lean kernel execution.",
            "contracts": contracts}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT / "extension/site/data/certificate-contracts.json")
    args = parser.parse_args()
    result = build()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"status": "bound", "contracts": list(result["contracts"]), "output": str(args.output), "sha256": digest(args.output)}))


if __name__ == "__main__":
    main()
