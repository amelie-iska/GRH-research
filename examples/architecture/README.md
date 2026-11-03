# Numerical architecture traces

This is the numerical data layer for the book's
[step-through architecture inspector](http://127.0.0.1:8765/architecture.html).
It exports **22 cases, 836 numerical DAG nodes**, with shapes, semantic axes,
formulas, parameter values and provenance. The inspector adds a separately
computed adjustable forward clock/shift carrier. It has one canonical in-book
location alongside the four earlier tools.

| Family | Evidence | Exported cases |
|---|---|---:|
| Four-qubit QCNN | Saved PennyLane weights; gate/state, partial trace and held-out compression replay | 2 |
| Nine-qubit genus-four QCNN | Saved PennyLane weights; correct 5+4 pooling partition and sparse eigenstate residual | 2 |
| Shared quantum graph convolution | Saved circuit and classical head; exact Ising decimation target | 2 |
| Quantum-feature attention | Three shared feature circuits, patch softmax, context and affine output | 2 |
| Photonic pooling | Saved Strawberry Fields angle; intermediate Gaussian covariances, hbar=2 | 2 |
| ToricGT/quantum-classical Harper surrogate | Saved weights and six independently rechecked rational PSD certificates | 6 |
| TokenGT-style softmax | Fixed-weight source-audited miniature, not a trained TokenGT checkpoint | 1 |
| Tropical attention / block-ring | Two fixed-weight references with identical scores and checked max-plus reduction | 2 |
| Attention hybrid | Fixed-weight softmax layer followed by tropical-ring layer; this is a classical attention hybrid | 1 |
| ToricGT-style Soft-MoE | Fixed weights, token-axis dispatch, expert-slot processing and slot-axis combination | 1 |
| Prefix-causal Soft-MoE | Fixed weights, source-exact row centering and strict earlier-index slots | 1 |

The classical graph is one permitted three-cycle of the elliptic theta dessin
with sigma=(012)(345), alpha=(03)(14)(25), genus one and completed order rank
18 over its central DVR. The fourth node position is padding. This carrier
forgets the other branch and alpha-gluing; it is not a faithful representation
of the infinite locally gentle algebra or completed surface order. The
larger QCNN likewise acts on finite edge-labelled spin states of the genus-four
example. Photonic and local feature circuits are finite physical models.
None establishes an arithmetic L-function operator or determinant positivity.

## Reproduce and verify

Use the already approved and pinned environment; do not install or upgrade:

```sh
.tools/book-quantum-cpu/bin/python examples/architecture/export_traces.py --output outputs/experiments/architecture-traces/candidate
.tools/book-quantum-cpu/bin/python scripts/check_architecture_traces.py --directory outputs/experiments/architecture-traces/candidate
.tools/book-quantum-cpu/bin/python examples/architecture/export_traces.py
.tools/book-quantum-cpu/bin/python scripts/check_architecture_traces.py
```

All code is safe to import. No training scripts with top-level optimization
are imported. The checker runs actual gate-level PennyLane circuits, actual
Strawberry Fields intermediate covariances, and a Cirq/Qiskit two-qubit replay.
Independent scalar loops verify attention and ordinary/strict-prefix expert
routing. Masked/all-pad inputs, empty prefix, transported metadata, exact
floating ties versus near-ties, Weyl orientation and unchanged checkpoints
are checked. These are numerical program checks, not Lean theorem proofs.
The preserved legacy Strawberry Fields release emits deprecation and
disconnected-mode warnings for its valid independent squeezing preparation.

The exporter first constructs and validates every trace. Immutable
content-addressed records are then written before atomically replacing the
manifest; old records remain available to readers holding an older manifest.
Failed independent checks must prevent treating a candidate as accepted.
Do not remove previous generations or source checkpoints as cleanup.
The manifest records exact source/checkpoint hashes and the NumPy/SciPy
versions; the check report records backend versions and its own source hash.

## Interface contract

`web/data/architecture/manifest.json` lists the active records and SHA256
hashes. Each record contains:

- `provenance.kind`: `trained-checkpoint-replay` or `fixed-weight-reference`;
- `nodes`: a topologically ordered dependency DAG, with `id`, `inputs`,
  `formula`, numerical `tensor` and optional gate/wire/angle metadata;
- `tensor.shape`, `tensor.axes` and either `values`, or separate `real` and
  `imag` arrays for a complex tensor;
- `checks`: measured errors with their checked tolerances;
- explicit conventions, inputs and finite-model limitations.

Attention exports raw and normalized Q/K, scores, legal masks, softmax
weights, tropical coordinate-wise winners, block contexts with validity,
head merge, residuals, feed-forward states and readouts. Masked block entries
are stored as zero **with a separate validity mask**; these zeros must not be
included in a maximum. Tropical winner ties mean equality of computed
floating-point terms, not a symbolic equality certificate. Softmax weights
in a tropical record are comparison diagnostics, not its aggregation rule.
Padding contexts are zero; output-projection bias can make a padded residual
nonzero, so downstream pooling and expert updates retain the validity mask.

Qubit 0 is most significant. The Harper carrier uses the upstream **backward**
shift, hence VU=iUV, whereas the book's forward clock/shift example uses
UV=iVU. The photonic covariance ordering is x0,x1,p0,p1. Equal reveal-rank
attention and strict earlier-index expert slots are different rules. The
classical references share weights between their two layers only to make the
comparison inspectable. Optional upstream polar compression, optimizer
campaigns, GPU/distributed execution and physical hardware are not run.

The inspector renders these arrays with playback, dependency navigation,
perspective orbit/zoom, exact coordinate selection and category-specific
circuit, covariance, token/attention, tropical-witness and expert-slot views.
Large tensors are paged; cells are rounded and selected coordinates expose
the numerical real/imaginary values. The data and trained checkpoints stay
immutable. A corrupted record is rejected before display; failed loads retain
and label the previous valid case. The current UI is not a training interface,
full upstream campaign, complete book formalization or a proof of GRH.

Frontend verification uses the project's existing dependency-free Node and
isolated headless Chrome/CDP harness:

```sh
node scripts/check_architecture_model.mjs
python3 scripts/launch_inspector_browser.py
node scripts/check_architecture_browser.mjs
```

The launcher refuses an occupied test port and preserves its isolated profile.
The browser checker closes only that isolated test browser. It covers all 22
saved cases, live clock parameters, exact displayed coordinates, masks, zero
phase, playback/loading races, checksum rejection, orbit/depth ordering,
responsive layout and the unique in-book embedding. No browser package is
installed. Optional upstream memory/GFlowNet/persistence heads, non-Gaussian
photonic networks and NVIDIA/hardware execution remain separate obligations.
