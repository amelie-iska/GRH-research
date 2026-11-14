# Research companion

This static companion presents the research monograph, executable finite models,
source reviews, and verification evidence. Its publication destination is the
existing [amelie-iska/GRH-Research repository](https://github.com/amelie-iska/GRH-Research).
The Pages release combines this companion with the inherited project material;
publication and machine synchronization are recorded separately from local validation.

The new laboratories use local JavaScript, styles, and data; they require no
package installation or CDN. The inherited pages under [legacy/](legacy/index.html)
retain their separately documented dependencies.

## Read and run

- [Research atlas](index.html).
- [Compiled monograph: 341 pages](downloads/paper.pdf).
- [Standalone fluid supplement: 90 pages](downloads/fluid-extension.pdf).
- [Compact research source archive](downloads/source.zip).
- [Lean companion archive](downloads/lean4.zip).

From this directory, run:

```sh
python3 -m http.server 8000
```

Open <http://localhost:8000/>. Use an HTTP server for the worker and JSON assets;
opening the HTML directly through a file URL is insufficient. This address is
for local development, not a claim of a public deployment.

The PDF hashes, source snapshots, compiler results, and warning counts are in
the [monograph build record](verification/pdf-build.json) and
[fluid supplement build record](verification/fluid-build-verification.json).
Earlier rendered-page reviews are retained as historical records for the
[main manuscript](verification/main-fluid-pdf-visual-qa.json) and
[fluid supplement](verification/fluid-pdf-visual-qa.json); their hashes identify
the editions they inspected. Current build freshness is checked independently.
The download directory contains generated release artifacts and is excluded
from the compact source archive to prevent recursive packaging.

## Pages and implementation files

| Page | Implementation and data | Mathematical purpose |
|---|---|---|
| [Research atlas](index.html) | [math.js](math.js), [app.js](app.js), [styles.css](styles.css) | Six laboratories for finite elliptic-curve arithmetic, Fourier sampling, complex rank loci, Hodge spectra, torus geometry, and a finite gauge example |
| [Surface circuits](quantum.html) | [quantum-core.js](quantum-core.js), [quantum-worker.js](quantum-worker.js), [quantum.js](quantum.js), [surface cases](data/surface-cases.json) | An actual 18-qubit state-vector circuit, editable errors and gates, and a four-angle variational circuit |
| [Exact algebra](algebra.html) | [algebra.js](algebra.js), [design record](ALGEBRA-DESIGN.md) | BigInt Plücker minors, Schur tableaux, gentle-module decompositions, and matching-semigroup relations |
| [Quantum ToricGT](learning.html) | [learning.js](learning.js), [exported weights](toricgt/weights.json), [benchmarks](toricgt/benchmark.json), [verification](toricgt/verification.json) | Full browser inference for the exported trained graph model with live circuit parameters and exact path comparisons |
| [Diagrams and languages](languages.html) | [grammar-core.js](grammar-core.js), [languages.js](languages.js) | Typed circuit rewrites, finite denotational checks, and constructive neural-language examples |
| [Cyclic cosmology](cosmology.html) | [cosmology.js](cosmology.js), [synthetic sky data](data/cosmology-synthetic.json) | Calibrated template searches on explicitly synthetic data |
| [Fluid laboratory](fluids.html) | [fluid-core.js](fluid-core.js), [fluids.js](fluids.js), [fluids.css](fluids.css), [independent reference data](data/fluids-reference.json) | Exact flow, integer toral coverings, a parameterized quantum circuit, a finite heat channel, and concentration scales |

The original interface remains accessible at [legacy/index.html](legacy/index.html).
The new page designs document the distinction between display geometry and the
mathematical structures being computed. For example, the embedded torus and its
flat period metric differ, and a four-dimensional viewing transform does not
change the original coordinates used to test a complex equation.

## The fluid extension

The fluid page evaluates a Taylor–Green manufactured solution, enumerates complete
fibres of the integer toral covering, executes a two-qubit complex-amplitude
circuit, and uses its measured features to parameterize a separate finite heat
channel. The circuit and position registers are distinct systems. The circuit
is untrained and simulated classically. The concentration panel evaluates
scaling formulas; it does not numerically reproduce the released singular flow.

The corresponding research supplement develops microscopic reductions, collision
invariants, entropy and moment equations, exact hidden-state memory, the quadratic
order behind the covering, compatible finite complexes, and constrained learned
closures. Its circuit-repair section supplies exact equality encodings and
contraction-normalized dilations with their success probabilities. Those finite
repairs do not establish a complete quantum-fluid algorithm or an end-to-end
speedup.

The September 2026 Navier–Stokes release concerns smooth **externally forced
breakdown from rest**, including positive viscosity and bounded kinetic energy,
in the whole-space and periodic settings. Its forced theorem is not an unforced
positive-viscosity theorem. The [release review](verification/navier-stokes/release-review.md)
records the exact scope, the full 166-page paper reading, and the analytic
interfaces explained by this project.

The pinned upstream solution has a 609-module local import closure. Its source
audit was completed; the separate fresh upstream build stopped at missing
dependency artifacts after rate-limited cache downloads. The
[current build-attempt record](verification/final-pass/upstream-build-current.json)
preserves that incomplete status. Successful local companion checks do not
substitute for the upstream continuum kernel or Comparator checks.

## Current proof and source evidence

The [claim register](verification/claim-register.md) inventories
**269 named environments**, including
257 local arguments,
5 conditional arguments,
6 cited external results, and
1 open problem. It records
**262 attached written proofs**. Presence of
a written argument does not certify its correctness. The selected external
statements in prose retain their distinct source and proof-scope classifications.

The [current selected Lean record](verification/lean-current/verification.json)
contains **115 kernel-checked declarations in 6 modules**.
The [formal type map](verification/formal-type-map.md) maps
**68 declarations** to
precise components of **25
manuscript environments**. No complete composite manuscript environment is
marked fully formalized. The source hashes, exact printed types, actual axiom
dependencies and module logs accompany the record and the recursive Lean archive.

The selected checks use Lean 4.24.0 and the pinned mathlib revision. Their
foundational dependencies are limited to `propext`, `Classical.choice` and
`Quot.sound`. They trust cached compiled imports; they do not independently
rebuild every dependency or formalize the entire monograph. The four-module,
82-declaration manifests retained elsewhere are historical evidence.

The library-backed cryptographic implementation has
**31 passing test methods** in its
[current regression record](verification/crypto/verification.json). Those tests
exercise the implemented interfaces and malformed-input rejection. They do not
prove computational security or certify a deployment.

The [release summary](verification/release-summary.json) binds these displayed
counts and the two PDF records to their source hashes. The separate upstream
Navier–Stokes check remains **incomplete**, as recorded in the
[current build status](verification/final-pass/upstream-build-current.json).
Local finite-interface certificates do not establish that continuum theorem.

The [review ledger](verification/review-ledger.md) retains historical audits at
their original scope. Fluid sources have separate
[microscopic](verification/navier-stokes/microscopic-source-review.md),
[Farhat](verification/navier-stokes/farhat-review.md), and
[quantum-algorithm](verification/navier-stokes/quantum-algorithms-review.md)
records. They distinguish full-text reading, selected passages, image inspection
and inaccessible originals. The prior 249-segment video transcript review lacks
a retained executor-local transcript export and content hash. The nine current
Farhat decks contain 627 PDF pages including overlays; they are replacements
for unavailable historical filenames, not a claim of identical editions.

## Numerical verification and browser inspection

The finite checks are separate from Lean proofs and from rendered browser
inspection. Run the applicable Node checks from this directory:

```sh
node verify-math.cjs
node verify-quantum.cjs
node verify-quantum-worker.cjs
node verify-algebra.cjs
node verify-grammar.cjs
node verify-cosmology.cjs
node verify-fluids.cjs
```

The fluid reference generator is `extension/code/verify_fluid_interfaces.py` in
the repository or source archive. It independently uses exact integer and modular
linear algebra, symbolic differentiation, and dense complex matrices. The
[Python results](verification/fluids-python.json) and
[Node comparison](verification/fluids-node.json) retain the exact scope and
floating-point discrepancies. The latter covers 16 circuit cases, 64 feature
gradient cases, and 8,865 complete-fibre points. These finite checks do not prove
continuum convergence or quantum advantage.

The [fluid browser record](verification/fluids-browser-qa.json) covers observed
flow, covering, circuit, heat, and scaling interactions, plus a narrow viewport.
It is not a claim that every parameter state was visually inspected. Separate
records cover the other pages. The atlas exposes its actual state through
`window.ResearchCompanion.getReport()`; URL state is validated and constrained
to supported controls.

## Quantum and cosmology interpretation

The live surface worker allocates the 18-qubit case. Larger toric and higher-genus
views use combinatorial records and separately reported GPU experiments. The
[GPU data](data/gpu-results.json) distinguish dense complex64 state vectors from
Pauli-error frames. A large error-frame experiment is not a comparably sized
dense state-vector simulation or execution on quantum hardware.

The [QNN record](data/qnn-training.json) and nine quantum ToricGT runs are actual
classical GPU simulations with their recorded datasets, checkpoints, and
comparisons. They establish trainability in those experiments. The new fluid
circuit has a separate scope and supplies no trained fluid ToricGT result.

Cosmology examples use synthetic skies and calibrated searches. No observed CMB
or decoded cosmological message is presented. The Yang–Mills status likewise
retains the distinction between the reviewed construction results and the
unresolved mass gap; the companion does not assert a proof of that conjecture.

## Publication bundle

The public verification directory contains authored reviews, exact type maps,
source hashes, reproduction scripts, and execution logs. Uploaded books, complete
OCR texts, downloaded third-party papers, and private authentication material are
excluded. The copied reproduction scripts are supplied for inspection; execute
their original repository paths from the source archive so their documented
relative paths remain valid.

Keep the download PDFs, build records, claim register, type map, and local
verification logs from the same release snapshot. Preserve the original research
history when updating the existing GitHub repository. Website publication and
the repository push are checked independently; neither is inferred from a local
preview or a documentation update.
