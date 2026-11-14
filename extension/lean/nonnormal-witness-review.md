# Nonnormal Jacobian witness and current formal inventory

**13 November 2026.** This follow-up adds six exact real-matrix declarations to
`TransportContracts.lean`. The current package has **115 selected declarations
in six modules**, including 17 transport declarations. The
[current verification manifest](final-verification/verification.json) and six
raw logs record a fresh successful elaboration, zero warnings, and only the
disclosed standard Lean foundations. The earlier
`independent-verification-20261113` record checked 109 declarations before this
addition and remains a historical snapshot.

## What the witness proves

For the explicit matrix

\[
J_M=\begin{pmatrix}0&M\\0&0\end{pmatrix},
\]

the new theorems establish `J_M²=0`, `J_M(0,1)=(M,0)`, exact squared
Euclidean gain `M²` on that unit input, strict gain greater than one for
`M>1`, a zero second Jacobian-vector product on every input, and failure to
commute with the transpose for `M≠0`. The last fact confirms nonnormality.
All six declarations map to the exact component scope of manuscript label
`prop:nonnormal-jvp`.

This exhibits the mathematical defect in using repeated multiplication by
`J` as a general singular-value upper certificate: large one-step amplification
can coexist with vanishing iterated products. The formal witness does not
assume a spectral-radius characterization or prove convergence of any
numerical singular-value algorithm. Even an iterative estimate using `J*J`
needs a separate argument before it can be called a certified upper bound.

## Current evidence binding

The claim-register generator now reads the current successful six-module
manifest, rather than taking its authority from the older four-module records.
It validates the exact source and log hashes, the checker and Lake configuration
hashes, module inventory, declaration inventory, source stability, foundational
axiom inventories, and actual printed theorem types for every declaration.
Missing exact types or stale evidence stop generation.

The additional declaration map contains 33 reviewed component entries: the
16 reduction declarations and 17 transport declarations. The generator checks
each entry's source hash, current type-and-axiom log, manuscript source and
exact label, and refuses a full-manuscript-formalization claim. All 35 earlier
precise declaration mappings were compared with the previous register and
remain unchanged. The resulting register has:

| Inventory | Count |
|---|---:|
| Included TeX files | 31 |
| Named theorem/proposition/lemma/corollary/problem environments | 264 |
| Attached written proof environments | 257 |
| Local arguments | 252 |
| Specially classified conditional arguments | 5 |
| Cited external theorem environments | 6 |
| Open-problem environments | 1 |
| Verified local Lean declarations | 115 |
| Declarations mapped to precise manuscript components | 68 |
| Manuscript environments with partial formal components | 25 |
| Whole composite environments asserted fully formalized | 0 |

These counts describe a specific manuscript snapshot. Written proof presence
is not the same as independent mathematical verification, and a component map
does not formalize every assertion surrounding that component.

## Verification of the evidence gate

[The targeted gate checks](claim-register-gate-checks.json) accepted the current
115-declaration record and rejected three deliberate defects in isolated
temporary copies: a modified source with stale verification, a missing printed
type even when the log hash was updated to match, and an attempted
whole-statement formalization overclaim. The project sources and authoritative
logs were not modified by these negative checks.

Reproduce the gate check with:

```sh
python extension/lean/verify_claim_register_gate.py
```

The main proof check remains:

```sh
python extension/lean/verify_all.py \
  --toolchain /absolute/path/to/lean-4.24.0-linux \
  --mathlib /absolute/path/to/mathlib4-v4.24.0
python extension/review/build_claim_register.py
```

The first command elaborates the actual local Lean source. The second audits
the resulting evidence and inventories the manuscript; it does not run Lean.
Neither command independently checks the external continuum Navier–Stokes
formalization or proves GRH, a Yang–Mills mass gap, or cryptographic security.
