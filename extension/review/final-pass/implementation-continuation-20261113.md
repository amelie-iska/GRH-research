# Implementation continuation: verification runtime and crypto boundaries

Reviewed 13 November 2026, Pacific time. This bounded continuation changes the
evidence-producing drivers and strengthens permanent cryptography regressions.
It does not change the cryptographic primitives, mathematical statements or
historical experiment outcomes.

## Correctness issue reproduced and fixed

Before the correction, running `verify_examples.py` with `python -O` returned
exit status zero and wrote `passed: true`, including a claim of 6,859 elliptic
curve associativity checks. Python optimization had removed all 14 `assert`
statements, including the associativity comparison. The pre-correction source
SHA-256 was `a9354622110430bc30ab49222d96a5be372fbda5cd33b87052f7aab9d4e184ea`.
The [preserved pre-correction output](optimization-false-pass-before.json) is
negative evidence of that driver defect, **not a successful mathematical
validation**.

The same failure mode affected `verify_invariants.py` (13 assertions),
`verify_fluid_interfaces.py` (24) and `verify_legacy.py` (6). Each now refuses
optimized Python before imports, computations or report writes. The existing
`verify_toric_transport.py` execution guard remains; an early guard additionally
protects imports of its verifier functions.

The new [runtime regression driver](../../code/verify_verifier_runtime.py)
discovers every assertion-bearing `verify_*.py` in `extension/code`, copies each
into an isolated temporary tree, and checks five execution modes: `-O`, `-OO`,
`PYTHONOPTIMIZE=1`, `PYTHONOPTIMIZE=2`, and optimized import. Acceptance requires
a nonzero process exit, the explicit disabled-assertions diagnostic, no created
evidence files and unchanged input bytes. An empty target set is rejected. The
driver itself uses explicit conditionals rather than assertions.

All **25 subprocess cases** passed. The driver also passed all 25 cases when it
was itself invoked with `python -O`. These are the same 25 refusal scenarios
under two parent-interpreter modes, not 50 independent mathematical checks.
Source hashes are recorded in
[verification-runtime.json](../../verification/verification-runtime.json) and
[verification-runtime-optimized.json](../../verification/verification-runtime-optimized.json).

## Permanent cryptography boundary coverage

The cryptography implementation is unchanged. Its source SHA-256 remains
`54565f60dc085a9fddabc21c8f260f4611399f428d6d48a6b33772a063ad8116`.
Six test methods were added to retain boundary cases that previously existed
only as one-off audit probes:

- Both AEAD choices round-trip the actual 16 MiB maximum payload with a
  1024-byte UTF-8 context.
- Payloads one byte over the limit are rejected.
- Serialized envelopes one byte over their limit are rejected.
- Context length is measured in UTF-8 bytes, including multibyte inputs.
- Noncanonical base64 pad-bit aliases are rejected even when they decode to
  exactly the same authentication-tag bytes.
- Unpaired Unicode surrogate contexts are rejected during envelope parsing.

The suite now contains **31 test methods**, all passing with zero failures,
errors or skips, on Python 3.12.14, cryptography 50.0.0 and OpenSSL 4.0.1. The
[current report](../../crypto/verification.json) binds the actual test source
and [log](../../crypto/verification.log) hashes. It retains AES-256-GCM,
ChaCha20-Poly1305, Ed25519, ML-KEM-768 and ML-KEM-1024 coverage. Test keys and
shared secrets remain ephemeral and are not logged. This is regression
evidence, not a new security reduction, backend audit or module validation.

## Ordinary verification after correction

| Driver | Observed result |
|---|---|
| `verify_examples.py` | Pass; all 6,859 exact finite associativity comparisons now execute |
| `verify_invariants.py` | Pass; 257 bounded feasible vectors, 135 exact pencil identities, point counts 19 and 323 |
| `verify_fluid_interfaces.py` | Pass; six cochain grids and 16 circuit cases; maximum feature-gradient error approximately 2.9914e-10 |
| `verify_toric_transport.py` | Pass; 288 generic paths, 120 rectangular paths, 128 noncommuting flat cycles and 96 tropical enumeration cases, with its additional counterexamples and multiplicity tests |
| `verify_legacy.py` | Pass; 650 served assets, 15 URL-adapter cases and two DOM-setter cases |

The source-hashed finite reports and fluid browser fixtures were regenerated.
The unchanged site worker should be validated against the regenerated fixture
hash during final site integration. No historical GPU experiment was rerun.

## Reproduce this chunk

Run from the repository root using the recorded Python dependencies:

```sh
python extension/code/verify_verifier_runtime.py
python -O extension/code/verify_verifier_runtime.py --output extension/verification/verification-runtime-optimized.json
python extension/crypto/verify_crypto.py
python extension/code/verify_examples.py
python extension/code/verify_invariants.py
python extension/code/verify_fluid_interfaces.py
python extension/code/verify_toric_transport.py --output extension/review/final-pass/toric-transport-verification.json
python extension/code/verify_legacy.py
```

The legacy command additionally needs the generated legacy site bundle and
Node.js. Per-command logs use the `continuation-` prefix in this directory.
The [chunk manifest](implementation-continuation-20261113.json) records relevant
source and evidence hashes so that later integration can detect stale results.
This continuation adds no proof of unforced Navier–Stokes regularity, GRH,
continuum Yang–Mills mass gap, quantum advantage or cryptographic security.
