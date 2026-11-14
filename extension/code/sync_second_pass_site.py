#!/usr/bin/env python3
"""Copy the checked, authored ToricGT runtime and compact data to the static site."""
from pathlib import Path
import hashlib
import json
import shutil

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "extension/quantum/toricgt"
TARGET = ROOT / "extension/site/toricgt"
FILES = {
    "reference.js": "reference.js",
    "graph-reference.js": "graph-reference.js",
    "results/browser-weights.json": "weights.json",
    "results/browser-graphs.json": "graphs.json",
    "results/browser-benchmark.json": "benchmark.json",
    "results/browser-fullforward-verification.json": "verification.json",
}
TARGET.mkdir(parents=True, exist_ok=True)
manifest = []
for source, target in FILES.items():
    a, b = SOURCE / source, TARGET / target
    shutil.copyfile(a, b)
    manifest.append({"source": str(a.relative_to(ROOT)), "target": str(b.relative_to(ROOT)),
                     "sha256": hashlib.sha256(b.read_bytes()).hexdigest()})
(TARGET / "asset-manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
print(f"Copied and hashed {len(manifest)} ToricGT runtime/data assets.")
