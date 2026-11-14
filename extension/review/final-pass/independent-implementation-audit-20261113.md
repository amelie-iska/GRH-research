# Independent implementation and source audit

**Date:** 13 November 2026. **Scope:** the artifact cryptography wrapper, its test driver, the exact toric transport regression, and selected mathematical claims in the pinned Tropical Quivers and ToricGT sources. This is a second inspection with fresh execution, not a certification of the complete repositories or of their external dependencies.

## Findings and disposition

| Finding | Evidence | Disposition |
|---|---|---|
| Cryptography wrapper behavior matches its documented finite API contracts on the exercised inputs | Fresh 25-method run; additional size-boundary and serialization probes below | No implementation change to `research_crypto.py` was required |
| Exact toric regression could report success while Python optimization removed its assertions | Before correction, `python -O extension/code/verify_toric_transport.py` exited zero and printed `status: passed` | Corrected: `run_checks` now explicitly refuses optimized execution before producing a report |
| The upstream JVP-only power iteration is incorrectly described as a singular-norm estimator and stability certificate | Exact nilpotent counterexample below, checked against the actual pinned source | Added a regression witness and documented the mathematical correction; upstream source remains unchanged |
| Earlier suffix-transport, damping, information and finite-mask corrections are substantively supported | Actual source sections inspected and independent finite computations rerun | Retained with their original scope; they do not imply a continuum theorem |

## Cryptographic implementation

The inspected implementation is [`research_crypto.py`](../../crypto/research_crypto.py). The source SHA-256 at this inspection is `54565f60dc085a9fddabc21c8f260f4611399f428d6d48a6b33772a063ad8116`.

The wrapper uses a 32-byte key and a newly sampled 96-bit nonce for each AEAD encryption. The version, algorithm and public application context are authenticated. The recipient independently supplies its expected algorithm and context. A changed envelope cannot choose a different algorithm implicitly. Decryption delegates tag verification to the native library and returns bytes only after that operation succeeds. Duplicate and unknown JSON fields, invalid version types, noncanonical base64, and invalid nonce/ciphertext lengths are rejected. The signature format has a distinct domain prefix and an explicit context length, avoiding concatenation ambiguity. The ML-KEM interface delegates encapsulation and decapsulation to the maintained backend rather than inventing a lattice cryptosystem.

The fresh execution of

```sh
python extension/crypto/verify_crypto.py
```

completed **25 test methods, zero failures, zero errors, zero skips** on Python 3.12.14, `cryptography` 50.0.0 and OpenSSL 4.0.1. The updated [`verification.json`](../../crypto/verification.json) and [`verification.log`](../../crypto/verification.log) record the actual run, source hashes, versions and named cases. Both ML-KEM-768 and ML-KEM-1024 executed. These results are finite functional and rejection checks, not an independent review of the backend's cryptographic implementation.

Additional independent probes exercised both AEAD choices at the actual **16 MiB payload boundary** with a **1024-byte context**, and verified round trips. They also verified rejection of a payload one byte above its limit, a UTF-8 context exceeding 1024 encoded bytes, and an envelope above the 24 MiB serialized limit. A noncanonical base64 pad-bit alias that decoded to exactly the same tag bytes was rejected. These were targeted boundary probes in this audit, separate from the permanent 25-method suite.

No new cryptographic security theorem follows from these tests. The documentation correctly retains the following boundaries:

- Random nonces have a quantified collision probability; sampling alone does not implement a persistent uniqueness guarantee or distributed key-use quota.
- Replay prevention requires receiver state. Context binding alone does not reject a second acceptance of valid old bytes.
- Public-key identity must be authenticated separately. An ephemeral test signature is not an archival author identity.
- Correctly sized invalid ML-KEM ciphertexts use implicit rejection; a returned shared secret is not a ciphertext-validity signal.
- ML-KEM is a KEM, not a complete authenticated transport protocol. Ed25519 is a classical signature algorithm.
- Python object disposal does not certify secret-memory zeroization. No FIPS module-validation or side-channel assurance is established.
- Neither GRH, a finite Hodge gap, the fluid model, nor a Lean arithmetic cancellation lemma supplies a security reduction for this wrapper.

The relevant primary APIs were checked against the versioned [AEAD documentation](https://cryptography.io/en/50.0.0/hazmat/primitives/aead/) and [ML-KEM documentation](https://cryptography.io/en/50.0.0/hazmat/primitives/asymmetric/mlkem/). [NIST FIPS 203](https://csrc.nist.gov/pubs/fips/203/final) provides the algorithm standard, including its publication update notice. These references support the algorithm/API classification; they do not certify this application.

## Verification must refuse disabled assertions

The toric regression uses Python `assert` to check the exact identities. In ordinary execution those checks ran successfully. However, `python -O` removes assertions during compilation. Before this correction, optimized execution returned zero and produced a successful report without performing those checks.

The guard now present at the start of `run_checks` raises `RuntimeError` when `__debug__` is false. A fresh optimized invocation exited **1** with the reason `Verification requires assertions; run without -O or PYTHONOPTIMIZE`. Ordinary execution still passed. This is a correction to the evidence-producing driver, not to the transport theorem.

Fresh ordinary execution reproduced:

| Check family | Instances |
|---|---:|
| Generic equal-dimension paths | 288 |
| Varying-dimension rectangular paths | 120 |
| Noncommuting flat cycles | 128 |
| Conditional-independence equalities | 16 |
| Tropical recurrence against independent path enumeration | 96 |

The source still records exact counterexamples to forward-prefix transport, positive damping of an expanding map, unbounded finite masks, and an incorrect path-horizon formula. A new exact JVP counterexample is included as described next. The final published regression JSON must be regenerated from the corrected source so that its source hash agrees.

## New source correction: JVP iteration is not singular-norm certification

The clean local source checkout resolves to [Tropical_Quivers_of_Archs at `2b6ab79a685e2c6233fb8892e59589951feeddad`](https://github.com/amelie-iska/Tropical_Quivers_of_Archs/tree/2b6ab79a685e2c6233fb8892e59589951feeddad). Its manuscript section **“Jacobian spectral radius estimation via JVPs”**, immediately after **“Damped updates and contraction enforcement”**, repeatedly applies

\[
u=Jv,\qquad v=u/\|u\|,
\]

and labels the result an estimate of the largest singular value. Its accompanying prose then treats this estimate as a norm bound relevant to stability. Repeated multiplication by `J` is not power iteration on `J*J`. For a general nonnormal Jacobian, the two operations differ materially.

Take the real matrix

\[
J=\begin{pmatrix}0&10\\0&0\end{pmatrix}.
\]

Then `J²=0`, so its spectral radius is zero. For a unit vector `x=(x₁,x₂)`, `||Jx||₂=10|x₂|≤10`, with equality at `e₂`; thus its operator norm is exactly **10**. Starting the displayed iteration at `e₂` produces `10e₁`, then zero. The source code's epsilon-stabilized normalization subsequently keeps the iterate at zero. It can therefore report zero for an operator whose singular norm is 10. The same matrix has

\[
J^T J=\operatorname{diag}(0,100),
\]

which identifies the correct singular direction. These equalities are now checked using rational arithmetic in [`verify_toric_transport.py`](../../code/verify_toric_transport.py).

**Correction:** a singular-norm power iteration must apply `J*J`, which can be computed by a JVP followed by the corresponding VJP, at a fixed state and with the correct inner product. Convergence requires its own hypotheses and stopping analysis. For a unit test direction, the sampled norm `||Jv||` is a lower bound on the true operator norm. A finite iteration by itself is not a certified upper bound and cannot prove contraction merely because the returned estimate is below one. A certified analytic upper bound, an appropriately rigorous numerical enclosure, or another justified stability criterion is needed. Pointwise local Jacobian evidence is also not a global Lipschitz certificate on the whole state domain.

This distinction does not rule out stable nonnormal systems or useful empirical diagnostics. It prevents an estimator from being assigned a proof contract it does not satisfy. No additional Lean theorem is claimed for this new witness.

## Source comparison and mathematical scope

The second clean local source checkout resolves to [ToricGT-Program at `f91ba1811b5a4f70d53c7120acf8ca2a0049f85b`](https://github.com/amelie-iska/ToricGT-Program/tree/f91ba1811b5a4f70d53c7120acf8ca2a0049f85b). The inspected original material includes the quiver-cycle coboundary formula, positive damping claim, JVP code and prose, stochastic embedding-fluid passage, and prefix-side-information statements. The corresponding amendment sections in [`toric-transport-audit.tex`](../../manuscript/chapters/toric-transport-audit.tex) were checked for the direction of composition, the relevant hypotheses and what the conclusions actually establish.

The suffix telescope is correctly typed for varying vector-space dimensions and does not require invertible or commuting arrows. Orthogonal exact/coexact Hodge components require the actual complex relation. A certificate computed from a complete prefix adds zero conditional information beyond that same prefix, although it can help a restricted predictor or a lossy representation. A stochastic small-step limit retains a diffusion term when its second conditional moment survives. Trace-preserving channels cannot represent a zero composite on normalized states, so the gentle-algebra quantum interpretation needs the stated instrument/typed-amplitude qualifications.

These are useful finite and conditional interfaces. They do not prove mesh-uniform continuum convergence, create an arithmetic spectral realization proving GRH, establish the Yang–Mills mass gap, turn a finite simulated circuit into quantum computational advantage, or strengthen the released forced Navier–Stokes result into an unforced regularity theorem. The reviewed cryptography chapter states those distinctions correctly.

This audit did not rerun the historical GPU training, review every bibliography item, or independently reprove every theorem in the two source repositories. The detailed earlier [source audit](toric-source-audit.md) retains its own coverage ledger. The current report adds a fresh implementation check, a concrete validation-driver fix and one additional mathematical source correction.
