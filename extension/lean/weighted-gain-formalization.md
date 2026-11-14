# Weighted gain formalization

The weighted gain continuation adds **six public theorem declarations** in
`WeightedGainContracts.lean`. The current strict extension check verifies
**121 declarations across seven source files**, with no warnings, complete
printed theorem types and only the disclosed foundational dependencies
`propext`, `Classical.choice`, and `Quot.sound`. Definitions and two private
algebraic helper lemmas are elaborated with the module but are not counted as
additional public results.

## Mathematical contract

The statements use a finite index type and an ordered field. They therefore
apply to exact rational data and to real gain bounds. For positive weights,
the two conditions

\[
  \forall i,\quad (Gw)_i/w_i\le q,
  \qquad
  \forall i,\quad (Gw)_i\le q w_i
\]

are equivalent. The same weight vector remains feasible at every larger rate.
These are the two formally checked components of
`prop:weighted-gain-feasibility`; a representation of an LP solver or its
optimization semantics is not part of these proofs.

The central matrix-action result assumes nonnegative gains, positive weights,
the componentwise gain certificate, and the actual entrywise domination
`|A i j| ≤ G i j`. From `|x i| ≤ r * w i`, it proves

\[
  |(Ax)_i|\le qr w_i.
\]

The proof starts from the actual signed finite sum defining `A *ᵥ x` and uses
the absolute-value triangle inequality and monotonicity of multiplication by
nonnegative gains. It does not assume the desired output bound. A separate
general comparison theorem supports block errors whenever their next-step
values have independently been bounded by the nonnegative gain matrix.

For time-varying matrices, let every `G_n` be nonnegative and satisfy
`G_n w ≤ q w`, and suppose `|A_n,ij| ≤ G_n,ij`. Given

\[
\begin{aligned}
u_{n+1}&=A_nu_n+e_n,\\
|u_{0,i}|&\le r_0w_i,\qquad |e_{n,i}|\le\delta_n w_i,
\end{aligned}
\]

with nonnegative `q`, `r₀`, and every `δ n`, the checked theorem proves

\[
  |u_{n,i}|\le
  \left(q^n r_0+\sum_{k=0}^{n-1}q^{n-1-k}\delta_k\right)w_i.
\]

The definition uses the natural-number exponent `n - (k + 1)`; inside the
sum, `k < n`. The private recurrence proof checks the exponent bookkeeping
and the last residual's exponent zero. No commutativity of the matrices is
assumed. Setting the residual radii to zero gives the unforced power bound.
The generic block-error theorem proves the same envelope from the explicit
one-step block comparison hypothesis.

The nondividing propagation theorems have valid weaker hypotheses than a
norm statement and do not require positive weights. Positive weights are
required to interpret the coordinate inequalities in the weighted maximum
norm. No new bundled norm or fixed-point construction is defined in Lean.
Strict contraction additionally requires `q < 1`. Feasibility at `q ≥ 1`
remains a legitimate gain bound and is not labeled strict contraction.

## Proof and implementation boundaries

The exact Python certificate and serialized integer witness replay have their
own implementation tests. The Lean theorems do not verify those programs,
their input parser, JSON handling, or the fact that a particular runtime
object was converted to the intended rational value. Rejecting floats and
nonfinite values is an implementation obligation, even though the
mathematical statements contain no floating-point arithmetic.

A gain envelope for a nonlinear update must hold over the claimed domain;
sampled Jacobians alone do not establish it. The domain's invariance, a
nonlinear fixed point, continuous-time differentiability/projectability,
quantum channel structure, hardware controllability, continuum fluid
regularity, arithmetic spectral identification, a continuum mass gap, and
cryptographic security are not supplied by this finite component.

The new declaration map assigns the first two results to
`prop:weighted-gain-feasibility` and the four propagation results to
`thm:weighted-gain-propagation`. All six mapping entries retain
`whole_manuscript_formalization_claim: false`.

## Reproduction and evidence

Run the following from the repository root with existing copies of the
pinned toolchain and dependency checkout:

```sh
python extension/lean/verify_all.py \
  --toolchain /absolute/path/to/lean-4.24.0-linux \
  --mathlib /absolute/path/to/mathlib4-v4.24.0
```

The driver checks Lean revision
`797c613eb9b6d4ec95db23e3e00af9ac6657f24b`, mathlib revision
`f897ebcf72cd16f89ab4577d0c826cd14afaafc7`, clean tracked dependency sources,
the registered Lake targets, and source/configuration stability. It requires
successful elaboration with warnings treated as errors, exact printed type
coverage and complete foundational axiom reports. It performs no downloads.
Compiled imports and the specified compiler remain in the trusted environment;
this is not a rebuild of the entire dependency graph from source.

| Evidence | SHA-256 |
|---|---|
| `WeightedGainContracts.lean` | `3115e1bdf4ec4479e563cf9386b6b57ee9c4a7ae1e475ac00bcda77427a6753d` |
| `final-verification/WeightedGainContracts.log` | `79be90d4807d1eb48df1f6478c3a2004db7cc0d90093f0af0c45a45225c0ffad` |
| `final-verification/verification.json` | `465cb1eceeb51316595b205d1e9cd532cf4705d62c4c767de8c879247f2443a1` |

The preceding 115-declaration verification is preserved in published commit
`ae44abba256f29f477c2348fbf15497f305ac1e2`, at the same manifest path. That
historical manifest's SHA-256 is
`0e22a8acbc9e9076a63af813d2f719cd64e27d30256f6f37c4950d77ac0868c8`.
Its result is not relabeled as a check of the new module. The independently
versioned inherited-package evidence and the separate upstream Lean 4.34
development retain their distinct scopes.
