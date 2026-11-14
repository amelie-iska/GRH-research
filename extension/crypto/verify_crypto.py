#!/usr/bin/env python3
"""Run the crypto regressions and record versions, source hashes and real output."""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import io
import json
from pathlib import Path
import platform
import time
import unittest

import cryptography
from cryptography.hazmat.backends.openssl.backend import backend

import test_research_crypto


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, default=Path(__file__).resolve().parent)
    args = parser.parse_args()
    source = Path(__file__).resolve().parent
    hashes = {name: hashlib.sha256((source / name).read_bytes()).hexdigest()
              for name in ["research_crypto.py", "test_research_crypto.py", "verify_crypto.py", "requirements.txt"]}
    stream = io.StringIO()
    suite = unittest.defaultTestLoader.loadTestsFromModule(test_research_crypto)
    started = time.monotonic()
    result = unittest.TextTestRunner(stream=stream, verbosity=2).run(suite)
    output = stream.getvalue()
    report = {
        "schema_version": 1,
        "checked_at_utc": datetime.now(timezone.utc).isoformat(),
        "status": "passed" if result.wasSuccessful() and not result.skipped else "failed",
        "tests_run": result.testsRun, "failures": len(result.failures),
        "errors": len(result.errors), "skipped": len(result.skipped),
        "elapsed_seconds": time.monotonic() - started,
        "python": platform.python_version(), "cryptography": cryptography.__version__,
        "native_backend": backend.openssl_version_text(),
        "algorithms_exercised": ["AES-256-GCM", "ChaCha20-Poly1305", "Ed25519", "ML-KEM-768", "ML-KEM-1024"],
        "source_sha256": hashes,
        "log_sha256": hashlib.sha256(output.encode()).hexdigest(),
        "keys": "Generated ephemerally inside tests; no private keys, shared secrets or plaintext inputs logged.",
        "scope": "Functional and tamper-rejection regressions for library-backed wrappers. No cryptographic security reduction, Lean proof of the primitives, independent backend audit, FIPS validation, authenticated KEM protocol or quantum-advantage claim.",
    }
    args.output_dir.mkdir(parents=True, exist_ok=True)
    (args.output_dir / "verification.log").write_text(output)
    (args.output_dir / "verification.json").write_text(json.dumps(report, indent=2) + "\n")
    print(output, end="")
    print(json.dumps(report, indent=2))
    return 0 if report["status"] == "passed" else 1


if __name__ == "__main__":
    raise SystemExit(main())
