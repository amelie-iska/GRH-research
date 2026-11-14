# Proof boundary

`FiniteContracts.lean` uses only Std and integer arithmetic. The exporter accepts
canonical, bounded JSON, independently replays it in Python, then inserts only
validated integers into fixed Lean templates. Each generated theorem is a `by
decide` proof of the displayed Boolean predicate. `native_decide` is not used.
The property proved is the finite predicate, not correctness of the Python or
JavaScript programs. Numerical and physical hypotheses remain outside it.

`CosmologyRisk.lean` has four measure-theoretic results: a finite union bound,
a rejection-event subset bound, a model-discrepancy allowance, and an allocated
family-wise budget. They apply to measures and therefore to probability measures.
No independence is needed. Event-level calibration and a bound on the change in
the null measure are hypotheses, not empirical facts manufactured by the proof.
The Monte Carlo rank formula is checked arithmetically; this does not formalize
its exchangeability theorem or validate CMB noise, masks, beams or foregrounds.

Pinned compiler: Lean 4.24.0, commit
`797c613eb9b6d4ec95db23e3e00af9ac6657f24b`.
Pinned mathlib: `f897ebcf72cd16f89ab4577d0c826cd14afaafc7`.

For the measure module, run `lake env lean /absolute/path/CosmologyRisk.lean`
from a mathlib checkout at that pin. The four declarations compiled without
warnings on Iska; their printed dependencies were only `propext`,
`Classical.choice`, and `Quot.sound`. Detailed final receipts are retained in
the workbench verification checkpoint rather than changing historical audits.

The HTTP verifier binds only to loopback, rejects cross-origin requests,
limits bodies to 64 KiB and permits one bounded kernel subprocess at a time.
No uploaded Lean is executed. Static paths cannot escape the two public asset
roots. It is opt-in, not an internet-facing proof server. Receipts bind the
certificate, generated source, exporter, contracts, template and compiler hashes;
they are local observations, not cryptographically signed attestations.
