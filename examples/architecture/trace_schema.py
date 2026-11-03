"""Inspectable numerical DAGs for the book's architecture laboratory.

No training, network access or file writes occur on import. Complex tensors use
separate real/imaginary arrays so shape always means mathematical tensor shape.
"""
from pathlib import Path
import hashlib
import json
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
SCHEMA_VERSION = 1


def source(path):
    path = Path(path)
    if not path.is_absolute():
        path = ROOT / path
    return {"path": str(path.relative_to(ROOT)),
            "sha256": hashlib.sha256(path.read_bytes()).hexdigest()}


def tensor(value, axes=None):
    a = np.asarray(value)
    if not np.all(np.isfinite(a)):
        raise ValueError("Trace tensors must be finite; export masks separately")
    if axes is None:
        axes = [f"axis_{i}" for i in range(a.ndim)]
    if len(axes) != a.ndim:
        raise ValueError("Axis labels do not match tensor rank")
    result = {"shape": list(a.shape), "axes": list(axes)}
    if np.iscomplexobj(a):
        result.update(dtype="complex128", real=a.real.tolist(), imag=a.imag.tolist())
    else:
        result.update(dtype=str(a.dtype), values=a.tolist())
    return result


def array(t):
    if "real" in t:
        return np.asarray(t["real"]) + 1j * np.asarray(t["imag"])
    return np.asarray(t["values"])


class Trace:
    def __init__(self, identity, title, category, provenance, conventions):
        self.data = dict(schema_version=SCHEMA_VERSION, id=identity, title=title,
                         category=category, provenance=provenance,
                         conventions=conventions, nodes=[], checks={})

    def add(self, identity, value, formula, inputs=(), axes=None, **metadata):
        if identity in {n["id"] for n in self.data["nodes"]}:
            raise ValueError("Duplicate node " + identity)
        known = {n["id"] for n in self.data["nodes"]}
        if not set(inputs) <= known:
            raise ValueError("Node inputs must precede their output")
        self.data["nodes"].append(dict(id=identity, inputs=list(inputs),
            formula=formula, tensor=tensor(value, axes), **metadata))
        return identity

    def check(self, name, error, tolerance=1e-9):
        error = float(error)
        if not np.isfinite(error) or error > tolerance or error < 0:
            raise AssertionError(f"{name}: error {error} exceeds {tolerance}")
        self.data["checks"][name] = {"error": error, "tolerance": tolerance}

    def finish(self):
        validate(self.data)
        return self.data


def validate(data):
    if data["schema_version"] != SCHEMA_VERSION:
        raise ValueError("Unknown schema version")
    if data["provenance"]["kind"] not in {"trained-checkpoint-replay", "fixed-weight-reference"}:
        raise ValueError("Explicit numerical provenance is required")
    seen = set()
    for n in data["nodes"]:
        if n["id"] in seen or not set(n["inputs"]) <= seen:
            raise ValueError("Trace is not a topologically ordered DAG")
        seen.add(n["id"])
        a = array(n["tensor"])
        if list(a.shape) != n["tensor"]["shape"] or not np.all(np.isfinite(a)):
            raise ValueError("Invalid numerical tensor")
        if a.ndim != len(n["tensor"]["axes"]):
            raise ValueError("Invalid tensor axes")
    if not data["nodes"] or not data["checks"]:
        raise ValueError("Trace requires numerical data and checked evidence")
    for c in data["checks"].values():
        if not 0 <= c["error"] <= c["tolerance"]:
            raise ValueError("Failed trace check")
    json.dumps(data, allow_nan=False)
