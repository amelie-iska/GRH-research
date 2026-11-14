# Exact formal interfaces

The current package contains **115 selected theorem declarations in six
default Lake libraries**. `ReductionContracts.lean` adds 16 declarations and
`TransportContracts.lean` adds 17 to the previous four-module, 82-declaration
snapshot. The current fresh check and complete printed types/axioms are in
[`final-verification/verification.json`](final-verification/verification.json)
and its per-module logs. The historical records below retain their original
sources and counts; they are not relabeled as checks of the new modules.

The [new declaration map](new-declarations.md) links each of the 33 additions
to its precise manuscript component and states where formal coverage stops.
No whole continuum PDE proof, complete monograph, GRH, Yang–Mills mass-gap
construction, or implemented cryptographic security theorem is claimed here.

For a fresh check without network access or environment changes, use the
existing exact toolchain and mathlib checkout:

```sh
python extension/lean/verify_all.py \
  --toolchain /absolute/path/to/lean-4.24.0-linux \
  --mathlib /absolute/path/to/mathlib4-v4.24.0
```

Run that command from the repository root. It checks the compiler revision,
clean tracked mathlib pin, all six Lake targets, current source hashes, actual
theorem types, axiom inventories and source stability during elaboration.
The fresh checker now passes `-DwarningAsError=true` to Lean and independently
rejects warning-bearing output, absent printed types and unexpected axioms.
Compiler, checker and configuration hashes must stay unchanged during the run.
Standard foundational dependencies remain disclosed. Cached compiled imports
and the named compiler are part of the trusted environment; this command is
not a from-source rebuild of the entire Lean/mathlib dependency graph.

The [final integration audit](../review/final-pass/independent-formal-crypto-final-20261113.md)
records the fresh 115-declaration run in the integration clone and the separate
25-test cryptographic wrapper run. The claim-register gate also has executable
negative checks: altered source, checker or log bytes; a missing printed type
even after the log hash is recomputed; and a falsely asserted whole-manuscript
formalization. These checks use explicit failures and remain active under
Python optimization:

```sh
python extension/lean/verify_claim_register_gate.py
python -O extension/lean/verify_claim_register_gate.py \
  --output extension/lean/claim-register-gate-optimized-checks.json
```

The ordinary and optimized records each report six checks, including acceptance
of the unchanged current manifest. These are tests of evidence handling, not
additional mathematical theorem declarations.

The [continuation review](../review/final-pass/formal-continuation-20261113.md)
records the stricter fresh run and the portability work. Its additional
[fresh-checker regression record](verifier-gate-verification/verification.json)
contains nine checks driven by five actual compiler invocations, including a
warning that Lean otherwise emits with exit zero, an admitted proof, and an
unproved project axiom. The corresponding
[optimized run](verifier-gate-optimized-verification/verification.json) keeps all
nine checks active under `python -O`. Deliberately invalid fixtures are temporary;
they are never installed as project theorem sources.

## Portable inherited-package verification

The original `lean/` arithmetic and `lean-analytic/` packages remain separate
from the six extension modules. Their public theorem/lemma inventory currently
contains **7 arithmetic and 361 analytic declarations**. This source inventory
is not itself a successful build count: consult each verification record's
`verified_declaration_count`, `blocked_module_count` and exact source hashes.
The older analytic README's 342 count describes an earlier snapshot.

Both shell entrypoints accept explicit existing toolchains on Linux or macOS:

```sh
sh scripts/check_lean.sh --toolchain /absolute/path/to/lean-4.24.0-linux
sh scripts/check_analytic.sh \
  --toolchain /absolute/path/to/lean-4.24.0-linux \
  --mathlib /absolute/path/to/mathlib4-v4.24.0
```

`GRH_LEAN_TOOLCHAIN` and `GRH_MATHLIB` provide equivalent per-command settings.
To check both packages in one invocation:

```sh
python extension/lean/verify_inherited.py \
  --toolchain /absolute/path/to/lean-4.24.0-linux \
  --mathlib /absolute/path/to/mathlib4-v4.24.0
```

The [combined inherited manifest](inherited-verification/all/verification.json)
records each public declaration's fully qualified name, actual elaborated type,
foundational axiom dependencies, source and output hashes. Private helpers are
elaborated with their containing modules but are not separately counted. The
driver verifies the compiler revision, clean tracked mathlib pin, and exact
dependency manifest. It makes no downloads and never invokes a global toolchain
installer. A missing compiled import is recorded as a dependency block rather
than presented as a failed mathematical theorem or a verified declaration.

These packages still do not supply the missing arithmetic identification for
GRH or a continuum mass-gap theorem. Their audit does not rebuild the separate
Lean 4.34.0-rc2 upstream Navier–Stokes development.

## Original module and historical verification

`BridgeTheorems.lean` contains 25 selected, typed theorem declarations for the
research extension. The file is deliberately limited to explicit elementary
interfaces. It does not formalize every theorem in the books or monograph.

The supplied build completed with exit code **0** for all 25 declarations.
`verification.log` records the actual Lean output, and `verification.json`
records the source hash, pinned dependency revision, declaration inventory, and
axiom dependencies. All printed dependencies are subsets of `propext`,
`Classical.choice`, and `Quot.sound`; none includes `sorryAx` or a project axiom.

## Reproduce with the pinned dependency

The local package uses Lean **4.24.0** and mathlib commit
`f897ebcf72cd16f89ab4577d0c826cd14afaafc7`.

From this directory, with the matching Lean toolchain installed:

```sh
lake update
lake exe cache get
lake env lean BridgeTheorems.lean
lake env lean QuantumInterfaces.lean
lake env lean DiagramGrammar.lean
lake env lean FluidInterfaces.lean
lake env lean ReductionContracts.lean
lake env lean TransportContracts.lean
```

The fresh-check driver above appends type and axiom commands for every selected
declaration, including modules without embedded audit commands. The verification
log and claim inventory are supplied separately.
An exit code of zero is required; source text alone is not a verification result.
The log must not contain `sorryAx` or project-specific unproved assumptions.
The standard Lean foundations, such as `propext`, `Quot.sound`, and
`Classical.choice`, are distinguished from an unproved mathematical claim.

An existing checkout of the same pinned mathlib commit can also provide the
environment without creating a second dependency checkout:

```sh
cd /absolute/path/to/pinned/mathlib
lake env lean /absolute/path/to/extension/lean/BridgeTheorems.lean
```

## What is formalized

| Family | Theorem content | Main hypotheses |
|---|---|---|
| Finite complexes | Image in kernel; rank bound; rank criterion for middle exactness | Linear maps over a field; zero composite; finite-dimensional middle space for dimension statements |
| Euler arithmetic | Rank terms cancel in the alternating sum | Integer dimension variables; this statement does not itself construct cohomology |
| Four-coordinate quadric | Exact perturbation expansion; tangent remainder; split quadratic coordinates; equal-radius equation | Commutative ring |
| Koszul identity | Two successive explicit maps compose to zero | Commutative ring; exactness is a stronger separate statement |
| Finite Hodge matrices | Positive semidefiniteness; quadratic energy; kernel test; characteristic determinant factorization | Real matrices; orthogonality condition for factorization |
| Small-energy family | Positive parameters with arbitrarily small energy in a fixed unit direction | Positive real tolerance |
| Integral shears | Determinant one; inverse; image and squared norm of the second basis vector | Integral matrix and real norm coordinates |
| Cyclic hidden relation | Kernel equation and collision-difference equation | `ZMod q`, including the general modulus allowed by its type |
| Linear encryption algebra | Matrix cancellation and a binary-selector noise estimate | Commutative coefficient ring for cancellation; real bounded errors for the estimate |

These proofs establish no runtime bound for a quantum algorithm, no lattice
hardness reduction, no global index theorem, and no continuum Yang–Mills
construction. Those distinctions are part of the theorem interfaces rather than
exceptions hidden in documentation.

## Additional quantum and binary-chain interfaces

`QuantumInterfaces.lean` contains **seven additional verified declarations**.
Its authentic output and independent inventory are in `quantum-verification.log`
and `quantum-verification.json`. The original 25-declaration manifest and
`BridgeTheorems.lean` hash remain unchanged. Both files are default Lake targets.
These first two files supply **32 selected declarations**. The second-pass
module below brings the total to **48**, without claiming a formalization of
the complete monograph.

The new file proves the square identities and anticommutation of actual 2-by-2
Pauli X/Z integer matrices. It defines the sign character of `ZMod 2`, proves
its multiplicativity, and derives the shift/phase commutation rule on actual
amplitude functions with values in any commutative ring. This specializes to
complex amplitudes without claiming an additional analytical Hilbert-space
theorem. For actual linear maps `d2 : C2 →ₗ[ZMod 2] C1` and
`d1 : C1 →ₗ[ZMod 2] C0` with zero composite, the resulting boundary shift and
coboundary phase commute. The proof derives their zero binary pairing from
the maps' composition; it does not assume the desired commutation as a premise.

The final theorem substitutes a separately justified Euler equation into an
integer rank formula. It does not itself prove surface classification,
cellular boundary ranks, encoded-qubit counts, or error-correction performance.
No full quantum circuit or QNN training procedure is claimed formalized.
Each new theorem has both a printed type and a printed axiom dependency list;
the successful build contains no `sorryAx` or project-specific axiom.

## Typed diagrams and transport: sixteen additional declarations

`DiagramGrammar.lean` and its `diagram-verification.log`/`.json` contain an
actually compiled typed sequential syntax, one-hole contexts, contextual
finite derivations, and explicit identity/associativity/inverse rules. The
semantics maps generators to actual linear maps. Equality of interpretation
is preserved by the verified rewrite rules and every finite derivation.

Separate declarations check finite matrix tensor interchange, tensor trace
factorization, rectangular trace cyclicity, the identity-loop dimension,
transport of complexes and exactness by actual linear equivalences, a
contracting-homotopy criterion for exactness, and the finite Hodge matrix
conjugacy identity under its displayed endpoint conditions. The middle
matrix must additionally be unitary for the manuscript's spectral reading.

All three modules are default Lake targets and all **48 declarations** were
freshly checked during the second pass. The raw outputs and source hashes
are preserved in `../review/second-pass-math-audit-core-kernel.*` and the
per-module manifests. The new source SHA-256 is
`871d34de90d99a263094f7abc4aadb51f5012d613c671b04fff43f5a0c35c1c6`.

The sequential syntax does not claim full tensor/dagger/traced graphical
coherence, channel CP/TP, measurements, QNN training, grammar completeness,
CCC, or natural-language understanding. Exact component mappings to the
manuscript appear in the mathematical claim register.

## Fluid dynamics: 34 additional declarations

`FluidInterfaces.lean` adds 34 actually checked declarations, bringing the
companion total to **82 across four default Lake targets**. The module checks
finite energy and actual coordinate derivatives, orthogonal projection,
boundary-flux continuity, Schur elimination, exact discrete memory, a forbidden
block composition, and the quadratic-order matrix used in the 2026
Navier–Stokes construction. `fluid-verification.json` and
`fluid-verification.log` preserve the successful check, exact types and source
hash; `fluid-axioms.log` preserves the axiom reports.

The module uses the same Lean 4.24.0/mathlib pin as the previous files and
introduces no project axiom or admitted placeholder. See
`../review/navier-stokes/formalization-review.md` for component scope.
It is separate from OpenAI's Lean 4.34.0-rc2 continuum development. The fresh
upstream build did not complete after dependency-cache rate limiting; the
upstream source audit is not described as a kernel verification.

## Exact reduction and transport contracts: 33 additional declarations

`ReductionContracts.lean` proves the fiber-constant factorization criterion,
uniqueness under surjectivity, exact discrete closure and trajectory
intertwining, norm lower bounds on unresolved fibers, and an arbitrary-order
signed polynomial cancellation example. The zero polynomial is treated through
the library's extended trailing-degree type, not assigned a false finite order.
The continuous-time nonlinear observation derivative is not formalized by
the discrete update statements.

`TransportContracts.lean` proves the suffix-transport telescope by induction,
closed/flat/fixed-vector consequences, a counterexample to forward-prefix
transport, damping inequalities and a real linear trace-preservation obstruction
to zero path relations. The path proof specializes the varying-space manuscript
statement to arrows acting on one module; no finite Hodge operator is thereby
turned into a continuum PDE theorem. The trace lemma does not formalize complete
positivity, instrument branches, quantum-channel trace-norm contraction or
protocol security.

Both modules are now Lake libraries and default targets. The source/type/hash
map and fresh six-module logs are the authority for the current **115** count.

Six of the transport declarations provide a concrete nonnormal-matrix witness:
`J_M = [[0,M],[0,0]]` has square zero, but maps the unit vector `(0,1)`
to `(M,0)` with squared Euclidean gain `M²`, greater than one when `M>1`.
Its second Jacobian-vector product vanishes for every input, and for `M≠0`
the matrix does not commute with its transpose. These exact algebraic facts
expose the failure of a plain `J` power probe as a general operator-norm upper
certificate. They do not claim a complete singular-value algorithm or its
numerical error analysis. The earlier independent-verification snapshot with
109 declarations remains historical; the current `final-verification` directory
contains the fresh 115-declaration run.
