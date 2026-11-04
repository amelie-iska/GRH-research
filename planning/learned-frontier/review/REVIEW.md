# Independent integrated review, 2026-11-04

Verdict: the finite constructions, saved numerical results and new inspector
calculations are accepted within their explicit scope. The two requested
corrections and the recommended theta-ribbon clarification were applied by the
root agent and independently inspected; all are resolved. No numerical failure
or hidden GRH/quantum-advantage claim was found in the reviewed core. This review
does not declare the user's complete-book formalization request complete.

The reviewer changed only this review directory and its corresponding
`outputs/checks/2026-11-04-learned-frontier/review/` evidence directory. No
production edits, dependency installation, Torch checkpoint deserialization,
training, GPU/SSH job, MCP activation, Git staging or publication was performed.
The existing CPU NumPy/SymPy environment and Node were used.

## Inspected scope

Read `README.md`, the existing quantum CPU lock/reproduction instructions, the
new core/details manuscripts, all new bibliography entries, and
`generative.py`, `controls.py`, `state_flow.py`, `width_limits.py`,
`cuquantum_surface.py`, `export.py`, `export_state_flow.py`,
`check_generative.py`, `summarize.py`, and `plot.py`. Inspected the new lab
HTML/JS, all five manifest-linked DAGs, the surface-profile/selection mapping
changes and cell-calculation branches relative to `c2d1b9a`.

Reviewed the saved twelve hybrid run records/checkpoints, separate coherent
flow record/checkpoint, actual cuQuantum result, summary/lab JSON, and the
geometry/hardware source/review ledgers. Read the actual algebra-resolution,
Frobenius/CHSH and hardware-check implementations and freshly executed their
local checkers. Earlier worker reviews were corroborating evidence, not assumed
proof. Final PDF pagination, live browser rendering and Linux transfer are
outside this review's execution scope and require the root agent's checks.

## Fresh evidence

Reproduce from the repository root:

```sh
.tools/book-quantum-cpu/bin/python -B planning/learned-frontier/review/check_integrated.py
node planning/learned-frontier/review/check_integrated.mjs
.tools/book-quantum-cpu/bin/python -B examples/learned_frontier/geometry/check_geometry.py --output outputs/checks/2026-11-04-learned-frontier/review/geometry-fresh.json
python3 -B examples/learned_frontier/hardware/check_reference_designs.py
```

The hardware invocation without `--output` preserves all prior evidence. The
review's first run used its own new `hardware-fresh.json` output path. Evidence:

| Independent check | Result |
|---|---|
| All twelve hybrid + one coherent checkpoint SHA256 values | Match records |
| Three-seed means/sample SDs in web summary | Exact recomputation match |
| Current generative source, preserved v1 snapshot, both repeat source hashes | Identical |
| Independent 128-by-128 Pauli-Kronecker Gibbs teacher and explicit white trace | Max saved-matrix difference 2.04e-10 |
| NumPy explicit coherent gate replay at all 33 recorded times | Max density-entry difference 2.94e-7; max fidelity difference 7.34e-7 |
| Replayed coherent density normalization/positivity | Pass |
| Frozen-feature width sweep, all eight seeds/five widths | Saved values reproduced exactly |
| Five DAG schema/manifest hashes and linked implementation/checkpoint hashes | Pass |
| All five new DAGs, every cell supported by numeric explanation | 3,752 cells over 250 nodes; max discrepancy 2.80e-7 |
| Surface mapping genus | All five are genus two |
| Tree counts, depolarizing composition, tropical bound, pants field values, CHSH | Pass |
| Fresh exact geometry script | 766 tree vertices, degree-12 resolution checks, exact pants/CHSH pass |
| Fresh hardware reference script | 65,536 sums, 262,144 masked cases, scheduler/controller checks and twelve negative controls pass |

Machine-readable results are `integrated-python.json`, `integrated-node.json`,
`geometry-fresh.json`, and `hardware-fresh.json` in the review evidence directory.
These are independent CPU replays/consistency checks, not fresh training or
cuQuantum execution. Torch is absent from the existing local CPU environment;
no dependency was added to change that.

## Mathematical and physical conclusions accepted

The specified random-feature limit follows from phase integration, the Gaussian
characteristic function and a finite-set strong law. Its PSD and readout tangent
kernel claims are exact. It is separate from jointly training the finite
four-qubit hybrid networks. Neither function-space tightness nor general QNTK,
many-qubit/QFT behavior is inferred. The GP assertion needs the initialization
precision below. Classical black-spin decimation with 32 outputs and quantum
white-spin partial trace to two retained spins are correctly distinguished.

The seven-spin Hamiltonian, white partial trace and smoothed measured law agree
with code/data. The dequantization sign-flip bound is correct. The measured law
does not determine coherence; the manuscript supplies an explicit conjugation
counterexample. Both conditional fields and the exact reverse-mixture formula
follow from Gaussian conditioning. The ordinary DDPM oracle still uses an
approximate Gaussian reverse kernel and approximate terminal prior; the text
states this explicitly. The full-known-teacher reverse sampler and coherent
purification supervision are not described as sample-only learned recovery.

The canonical purification has the claimed normalization/partial trace; the
conjugated CNOT blocks cancel at time zero. Forty-eight controls and 76 replay
gates are consistent with code. The reported 0.999903 minimum fidelity is a
33-point diagnostic. The inverse depolarization counterexample correctly
excludes a universal positive inverse. No quantum processor, OOD materials
validation, complexity speedup or consistent entanglement advantage is claimed.

Travel-order right modules over `A_trav = A_col^op` resolve the apparent
left-column multiplication convention. The simple and one-arrow branch
resolutions follow in every degree from normal-path kernel descriptions, not
just the finite diagnostics. Their Ext/Tor formulas and explicit nonsplit branch
self-extension are consistent. Finite-dimensional duality applies termwise to
the stated finite-idempotent projectives. No completed-lattice, smoothness,
derived equivalence or AR-universality conclusion is silently added.

The graph-tree, Cayley-tree, punctured Belyi cover and compact-surface cover are
correctly separated. The dual-number Frobenius matrices, characteristic-two
change, closed contractions and heralded rather than unitary multiplication
are consistent. CHSH's exact optimum does not exhibit the unrestricted
tensor/commuting separation. Arithmetic profinite/anabelian data, conformal
sewing, string amplitudes, holography/HMS and the positive arithmetic determinant
remain separate obligations.

The 7/11/23-qubit cuQuantum records explicitly mark all circuits untrained. The
23-qubit case has 8,388,608 amplitudes and 447 gates and only normalization/echo
checks; independent NumPy comparison stops at eleven qubits. The measured
gate-segment timing is not asserted as an end-to-end speedup. The hardware
survey's twenty repositories, twenty-four document ranges and thirteen papers
are correctly described as focused source review. Three digital references are
not synthesized chips. Original vector figure code uses saved numeric records;
the cover figures are openly schematic.

## Precision fixes resolved after independent reinspection

1. `papers/learned-frontier-details.tex`, width subsection, initially said
   merely "Gaussian independent readout coefficients" yield covariance
   `K_m`. Require `a_r ~ N(0,1)` independently of the features, at initialization
   or before fitting. Gaussian coefficients of variance four produce covariance
   `4 K_m`; fitted coefficients generally lose the asserted distribution. This
   correction affects the GP paragraph, not the valid feature-kernel theorem.
   **Resolved:** the paragraph now explicitly specifies standard centered
   independent `N(0,1)` coefficients at initialization, independent of frozen
   features, and centered conditional Gaussian outputs.
2. `planning/learned-frontier/GPU_ENVIRONMENT.md` initially said no installation
   occurred and the environment awaited approval. This contradicts the approved
   actual environment and both resolved lockfiles. Update it to distinguish the
   preserved initial proposal/lock and setup failures from final executed status.
   **Resolved:** the document now states user approval and actual installed
   versions, names both initial/final lockfiles, records activation/header and
   metadata failures, and scopes isolated supplemental headers and GPU checks.

Recommended clarification: "the graph is a spine of a pair of pants" is true
for an appropriate ribbon embedding of the abstract theta graph. The actual
one-face genus-one theta dessin thickens to a once-punctured torus. State the
choice of ribbon structure explicitly to prevent a false identification; the
universal graph cover calculation does not depend on that choice.
**Resolved:** the manuscript now explicitly distinguishes a planar ribbon theta
spine of pants from the actual `m=3` dessin's once-punctured-torus thickening.

## Appended coefficient-field learners

Independently inspected `examples/learned_frontier/coefficient_fields.py` and the
new manuscript paragraph. Fresh standard-library execution reproduced the saved
`coefficient-fields.json` exactly; the review copy is
`coefficient-fields-fresh.json`. Fields have prime orders 2, 3, 5. Exhaustive
affine coefficient searches have minimum mismatch counts 1, 4, 16, respectively;
the four-feature polynomial learner has zero errors on all 4, 9, 25 inputs.
The verified reversible maps permute dimensions 8, 27, 125 and have explicit
subtraction inverses. Thus their complex permutation matrices are unitary.

The target product is already supplied as the `xy` feature, and exact finite
coefficient search finds its readout. This is an elementary finite algebra
example, not evidence of representation discovery, generalization or QNN
optimization; no such stronger claims appear. Its field arithmetic, input
retention and reversible basis encoding do not identify finite-field addition
with complex amplitude addition. The paragraph explicitly excludes finite-field
backpropagation and field embeddings. Accepted within that scope. No broad
numerical rerun was needed after these prose-only corrections; model/data and
the preceding numerical evidence are unchanged.

## Primary-reference verification

Fresh direct primary-page inspection confirmed the new metadata and limited
comparison claims for [Jacot--Gabriel--Hongler v4](https://arxiv.org/abs/1806.07572v4),
[Liu et al. v3](https://arxiv.org/abs/2111.04225v3),
[Quantum Flow Matching v1](https://arxiv.org/abs/2508.12413v1),
[Kontsevich--Soibelman v1](https://arxiv.org/abs/math/0406564v1), and
[Lekili--Polishchuk v5](https://arxiv.org/abs/1801.06370v5).
[MIP*=RE v4](https://arxiv.org/abs/2001.04383v4) really is dated 16 October 2026;
its correlation/Connes consequence and advertised external formalization remain
external inputs. The [Abrams author-hosted PDF](https://www.math.umd.edu/~jmr/AbramsTQFT.pdf)
and [Mochizuki introduction](https://www.kurims.kyoto-u.ac.jp/~motizuki/Absolute%20Anabelian%20Geometry.pdf)
support the Frobenius and arithmetic-field scope. This is focused metadata,
abstract/intro and hypothesis verification, not full independent reproof of those
papers. Existing Segal/RT source ledgers were inspected; no new strong theorem
from them is needed for the explicit elementary constructions here.

No new Lean claim was certified by this review. The old 360 reports cannot be
promoted to a formalization of this extension, the whole book or GRH. The
reviewed text retains that boundary.
