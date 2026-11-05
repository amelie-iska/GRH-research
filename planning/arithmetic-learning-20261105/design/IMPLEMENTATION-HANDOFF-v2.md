# Exact arithmetic readout implementation handoff

All new code and runs are remote on iska-linux-vscode. Completed implementation:
`examples/arithmetic_learning/{learn.py,test_learning.py,README.md}`.

Accepted immutable run: `outputs/experiments/2026-11-05-arithmetic-learning-v2/`.
Evidence: `outputs/checks/2026-11-05-arithmetic-learning/implementation/{cli-v2.txt,focused-replay-v2.txt,binding-v2.txt,cli-contracts-v2.json}`.

Full15-column activated original family at norms7507,7519,8281,10507 uses one
specified common four-bump smooth profile, zero at every other integer norm.
This improves the preliminary design's selected-eight-column scope: the actual
fixture is now ALL active good squarefree ideal columns for its profile.
There are95(h,q) offdiagonal blocks,65 h1 blocks,210 trained orientations,
225 Gram entries per row case and4530 raw column zeros per row case.
All2262 literal rows and the separately labelled2148 guaranteed nonprincipal
subset retain literal units/S powers as applicable and every original zero.
Principal nu is the implemented scope.

Four exact tau=1e-12 runs accepted: all-literal real53 updates, all-literal
complex55, guaranteed-subset real53, guaranteed-subset complex55, totaling216
executed preconditioned metric-GD updates. All complete rational states,
losses, signed CC/CM predictions and squared certificates are saved.
Every case also has50 actual ordinary real-coordinate GD updates, explicitly
budget-limited with no requested-error certificate. All three final requested
squared certificates(CC,CM,uniform full-vector) are<=tau^2.
All cases contain64 nonzero negative-mu(q) C-C target orientations.

11 focused tests pass with no skips, including independent finite-field
exponentiation for31668 local symbols and independent doubled Q(sqrt(-3))
reconstruction of450 Gram targets, correct metric/gradient and full-loss
normalization, sparse histogram/orientation checks, literal units/raw common
zeros, complex W conjugation, signed q, imaginary targets, scalar-only
cancellation, stale source rejection and all metric trajectory replay.
CLI existing-output and zero-tau refusals pass; zero-tau creates no directory.
Input/source/artifact SHA256 binding passes before/after the run and on replay.
Tests that mutate protected source/output bytes were not run: stale-byte
refusal is tested with an in-memory altered reader, without file mutation.

For UI integration, each case JSON contains `feature_predictions` with actual
learned/target finite-feature values at selected phase tuples, plus all
`metric_GD.states` and exact signed output certificates. `input.json` is36MB;
extract a compact UI payload rather than bundling that full provenance table.
The four case files contain long exact ordinary trajectories(4MB/17MB each).
No dense6^omega(q) group is enumerated; full phase loss is evaluated EXACTLY
by finite Parseval, and all orientation targets are supervised, including
zero observable weights. This is executed Fourier coefficient learning,
not a sampled loss or upstream quantum-model training.

The first v1 attempt completed its first case but failed a CLI `flush` keyword
placement. Its partial input/case and cli-v1.txt are preserved unchanged.
The corrected complete accepted run uses fresh v2 outputs.

No production/pin/history/dependency/auth/GPU/Lean/publication changes.
Fixed-finite-instance arbitrary-rational-request termination does not provide
all-conductor/range/runtime uniformity, generalization, a new analytic saving,
PSD/positive arithmetic determinant, zero location or GRH.

Frozen hashes:

Run manifest: `1eb22dfdadaf4a92e6b6231b7edd2fbfab0e68e0751237ce45e7a11bdb6dc3b4`

Input: `61a43821bdba19b5ca353042e216b2107977e60211e959cd1d2e65cf1acb2ed6`

- `examples/arithmetic_learning/README.md`: `f3cb62eab1c19d05f061af90f8289dc0f8ed3b8015d5e202243892f1293fd24f`
- `examples/arithmetic_learning/learn.py`: `5c53724df205e017533c20229fe981ce70cde615eeefb7077e73be401dbbdd2e`
- `examples/arithmetic_learning/test_learning.py`: `e8c777a86a840a3d223423d235fbbc4b2adb0d0918d9126ce8f785dcd1c95cdf`
- `scripts/check_finite_correlation.py`: `5f8da7467f93071fc19b4a1a1e8c415a880a95305d847cce9a42c386d1f3d3e8`
- `scripts/check_mobius_split.py`: `a3f1d3d89acafc187d6ca6851f370712b2544c92802b4d95dc5187e18a770638`
- `scripts/check_reciprocity_period.py`: `34eef99b491f6b8d64b55b39c3a42400c6df3d0e1ddf5ba8494bc01f300e8925`
