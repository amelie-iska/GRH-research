# Final integration review: formal proofs and artifact cryptography

**Review date:** 13 November 2026, Pacific. **Integration clone:**
`/workspace/scratch/02736665cfd3/GRH-research`.

The six current finite-interface Lean modules passed fresh kernel elaboration:
**115 selected declarations, six successful modules, zero warnings, no additional
project axioms or admitted proofs in the reported declaration dependencies**.
The separate library-backed cryptographic wrapper passed **25 test methods,
zero failures, zero errors and zero skips**. No mathematical theorem or
cryptographic primitive needed modification in this pass. One evidence-test
weakness was corrected: its required assertions can no longer disappear under
optimized Python.

## Exact current verification

The command executed in the integration clone was:

```sh
python3 extension/lean/verify_all.py \
  --toolchain /workspace/scratch/70763186a94c/.tooling/lean-4.24.0-linux \
  --mathlib /workspace/scratch/70763186a94c/.tooling/mathlib4-v4.24.0
```

It exited zero at `2026-11-14T00:08:36.469870+00:00` (13 November locally).
The [current manifest](../../lean/final-verification/verification.json) binds
each source and actual output log by SHA-256, enumerates all selected theorem
names and their axiom dependencies, records the compiler, and checks that
the source remained unchanged during elaboration. Its SHA-256 at this review is
`9568040c5e2626b15876c068603a57f8536455774407f93481ed3469badfdc45`.

| Module | Selected declarations | Exit | Warnings |
|---|---:|---:|---:|
| `BridgeTheorems` | 25 | 0 | 0 |
| `QuantumInterfaces` | 7 | 0 | 0 |
| `DiagramGrammar` | 16 | 0 | 0 |
| `FluidInterfaces` | 34 | 0 | 0 |
| `ReductionContracts` | 16 | 0 | 0 |
| `TransportContracts` | 17 | 0 | 0 |
| **Total** | **115** | **all zero** | **0** |

Lean is version 4.24.0, compiler revision
`797c613eb9b6d4ec95db23e3e00af9ac6657f24b`. The clean tracked mathlib checkout
is pinned to `f897ebcf72cd16f89ab4577d0c826cd14afaafc7`. The reported axiom
dependencies are subsets of `propext`, `Classical.choice` and `Quot.sound`.
The checker appends both exact type output and an axiom report for every selected
declaration. The source/configuration/printed-type audit accepts the resulting
manifest without changing the theorem sources.

The earlier [109-declaration independent review](independent-formal-audit-20261113.md)
remains a historical review of its stated snapshot. The current transport file
adds six exact nonnormal-matrix witnesses to that snapshot. They concern the
actual matrix `[[0, M], [0, 0]]`: its square and second Jacobian-vector product
vanish, while its image of the second unit coordinate has squared length
`M^2`, which exceeds one for `M > 1`. This is an explicit obstruction to
identifying repeated Jacobian-vector multiplication with a singular-norm
certificate; it is not a general convergence theorem for every norm estimator.

This pass freshly elaborates local sources against cached compiled imports.
It does not independently rebuild the compiler or every mathlib dependency.
The inherited `lean/` and `lean-analytic/` packages, the external continuum
Navier–Stokes development, and every written manuscript proof were not
rechecked by this six-module command. Their separate evidence remains separate.

## Claim-register gate correction

The prior `verify_claim_register_gate.py` used bare Python `assert` for its
expected declaration count, rejection-message checks and the setup of the
missing-type test. `python -O` removes those statements. A passing optimized
run could therefore overstate which gate properties had actually been checked.

The script now uses explicit conditional failures, has a normal `main` entry
point, and records its own hash, the generator hash and the exact Lean manifest
hash. It checks all of the following in temporary copies:

1. The unchanged current manifest is accepted and contains 115 declarations.
2. A source-file change is rejected.
3. A verification-checker change is rejected.
4. An output-log change is rejected.
5. Removal of an exact printed theorem type is rejected even when the altered
   log's hash has been recomputed in its copied manifest.
6. A component mapping that falsely claims whole-manuscript formalization is
   rejected.

Both ordinary Python and `python -O` executed all six checks and exited zero.
The [ordinary record](../../lean/claim-register-gate-checks.json) and
[optimized record](../../lean/claim-register-gate-optimized-checks.json) preserve
the results. No repository source or verification record is mutated by the
negative probes; only the final named gate reports are written.

Hashes bind evidence to the reviewed bytes. They are not digital signatures,
and this gate does not claim to defend against an adversary who can replace
the verifier, all evidence and the trust root together. It prevents accidental
reuse of stale or incomplete records in this publication workflow.

## Artifact cryptography review

The reviewed code is [research_crypto.py](../../crypto/research_crypto.py),
SHA-256 `54565f60dc085a9fddabc21c8f260f4611399f428d6d48a6b33772a063ad8116`.
It delegates AES-256-GCM, ChaCha20-Poly1305, Ed25519, ML-KEM-768 and ML-KEM-1024
to the installed `cryptography` package. The Python layer supplies bounded
framing, strict base64/JSON parsing and the application context.

The command `python3 extension/crypto/verify_crypto.py` exited zero at
`2026-11-14T00:08:04.025648+00:00`. Its
[manifest](../../crypto/verification.json) and [test log](../../crypto/verification.log)
record Python 3.12.14, cryptography 50.0.0 and OpenSSL 4.0.1, with all 25 methods
executed. The manifest SHA-256 at this review is
`01c470bab5086236b478c91f626688bc77f7a8846f61658e0349a1bf9b5a3af4`.
The four recorded hashes for the implementation, tests, runner and requirements
match the current files. Private keys and shared secrets were ephemeral and
were not written to the report.

The fresh regressions cover both AEAD algorithms, wrong keys and contexts,
algorithm substitution, nonce/ciphertext/tag changes, strict envelope parsing,
signature changes and context framing, and both ML-KEM parameter sets including
implicit rejection. The earlier independent audit also records separately
performed payload/context boundary probes; those historical probes are not
being counted as newly executed tests here.

The API behavior agrees with the versioned primary documentation for
[authenticated encryption](https://cryptography.io/en/50.0.0/hazmat/primitives/aead/),
[Ed25519](https://cryptography.io/en/50.0.0/hazmat/primitives/asymmetric/ed25519/)
and [ML-KEM](https://cryptography.io/en/50.0.0/hazmat/primitives/asymmetric/mlkem/).
[FIPS 203](https://csrc.nist.gov/pubs/fips/203/final) specifies ML-KEM and records
its publication errata notice. These sources classify the primitives; they do
not certify this wrapper or turn the local backend into a FIPS-validated module.
The pinned version describes the executed reproduction environment. The
[library changelog](https://cryptography.io/en/stable/changelog/) now lists
50.0.2, so this audit does not label 50.0.0 the latest production release.

The existing trust boundaries remain correct: the KEM interface alone is not
an authenticated transport protocol; Ed25519 is not a post-quantum signature;
public-key identity and replay rejection need application mechanisms;
random nonces require a per-key lifecycle; and Python object disposal does not
guarantee zeroization. The selected Lean algebraic correctness lemmas do not
formalize these native cryptographic implementations or prove computational
security. No new wrapper, home-designed primitive or additional security claim
was introduced in this review.
