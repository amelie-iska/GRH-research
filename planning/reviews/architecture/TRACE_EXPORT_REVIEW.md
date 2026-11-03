# Numerical architecture trace review — 2026-11-03

Independent reviewer: `/root/architecture_trace_review`. Scope: the original
NumPy trace schema/exporter, six saved quantum experiment families, and six
fixed-weight classical reference variants in `examples/architecture/`. No
training, installation, Git mutation or network/authentication was performed.
This review does not cover the still-queued interactive inspector.

## Findings and corrections

1. The initial tropical winner mask used an absolute tolerance while calling
   the selected keys maximizers. This could mark a strict near-maximum as a
   tie. The corrected mask uses equality of the computed floating-point terms
   and their maximum. These are floating-point witnesses, not proofs of
   symbolic equality.
2. Initial replacement of stable record names followed by the manifest was
   atomic only per file; a concurrent reader of an old manifest could see new
   record bytes. The corrected exporter uses content-addressed immutable
   records, checks an existing record's exact bytes, and replaces the manifest
   last. Earlier records remain intact. An interrupted export may leave
   unreferenced records but cannot invalidate the old manifest.
3. Initial numerical-DAG edges omitted several actual tensor dependencies.
   The reviewed correction now exposes Q/K projection and normalization,
   scoring/masks, aggregation, head merge, residuals, feed-forward/routing
   dependencies and tokenization weights. The final three linear readouts
   now include their respective head-weight parents, confirmed in both the
   source and every final classical trace. All DAG findings are closed.
   A topologically valid graph
   alone is not evidence that every dependency is semantically correct.

## Independent numerical checks

The approved `.tools/book-quantum-cpu/bin/python` environment was used.

- Reconstructed the circuit from each exported gate's metadata, using actual
  PennyLane `RY`, `RZ`, `CZ`, `CNOT` operations and `StatePrep`, independently of
  the small-gate NumPy application implementation. All **18** final-state
  replays passed; maximum component error **2.29e-16**. This includes the
  nine-qubit pooling case, whose four CNOT targets start at retained wire 5.
- Independently executed Strawberry Fields squeezing followed by the source
  beamsplitter and compared its **intermediate covariance**, including the
  signs of the off-diagonal blocks. Maximum error **2.22e-16**. This checks more
  than the final scalar objective, which would not detect every convention
  error.
- Compared each output coordinate of the miniature tropical context with an
  explicit scalar loop over legal keys: maximum error **0**.
- Compared causal expert slots with explicit earlier-row weighted sums,
  independently of the cumulative-sum implementation: maximum error **0**.

The final focused checker report is
`outputs/checks/2026-11-03-architecture/trace-checks.json`: **22 traces, 124
embedded trace checks and 38 independent checks passed**. It additionally
executes Cirq 1.4.1 and Qiskit 1.3.3 state replays, both photonic cases at all
three covariance stages, all-mask and exact/near-tie boundary cases,
transported-permutation attention tests, and a negative Weyl-convention test.
PennyLane 0.40.0 and Strawberry Fields 0.23.0 were used. The reviewer verified
that this report's checker/manifest hashes match the current files and that
all 22 manifest record hashes agree. The classical hidden width is now
12 = 2 times the model width, matching an allowed integer FFN multiplier.
Protected training-checkpoint hashes are unchanged before/after the checks.

The trained replay labels match the stored held-out cases. Harper cases are
correctly labelled as rational certificate probes, not held-out training rows.
The 15 principal minors are recomputed with an independent exact Leibniz
determinant. Failed PSD at an upper bracket implies the bracket is above the
least eigenvalue; the separate Rayleigh upper bound remains valid. No learned
proposal is accepted solely because a numerical spectrum appears plausible.

## Source and scope assessment

The reviewed formulas agree with the pinned ToricGT core: shifted and
L2-normalized Q/K, ordinary dot scores, max-plus aggregation for tropical
modes, per-head gating, masked softmax rows, token-axis dispatch and slot-axis
combination. The strict-prefix module retains the actual upstream rowwise
logit centering before the prefix sums. It is not silently replaced by a
different prefix-global softmax rule.

All-masked attention has zero context; projection bias may then be nonzero,
which is explicitly labelled. Padding contributes zero Soft-MoE update.
Attention allows equal reveal ranks; strict earlier-index expert slots are a
separate module convention. Neither property licenses an unstated full-model
causality or relabelling claim.

The miniature classical references are clearly marked as **fixed weights**,
not upstream trained checkpoints or executed PyTorch models. Shared layer
weights, disabled dropout/polar compression, absolute identifier metadata and
the finite carrier's loss of full surface-order structure are disclosed.
Quantum replay means the existing trained parameters are read unchanged; it
does not mean new training, quantum hardware execution or GPU simulation.

The readout-parent finding is closed and focused checks pass; this is an
acceptable **numerical data-layer milestone**. It establishes no
new theorem about infinite surface orders, full-book Lean formalization,
arithmetic determinant positivity or GRH. The architecture inspector and
larger experiments remain separate implementation obligations.
