# Continuation checkpoint: exact weighted-gain certificates

Recorded 13 November 2026 (Pacific). This checkpoint preserves the next bounded
implementation iteration before changing the released research artifacts.

## Published baseline

GitHub `main` and all three inspected working clones are clean at
`ae44abba256f29f477c2348fbf15497f305ac1e2`. The published research payload is
`4b9adb4f9c598e7d01b8ca15ed502e169b83ab13`; the live Pages branch is
`4d6341b5a8bf072c20525868255f43eb238438c1`. There were no unpublished source
changes when this continuation started. The prior release evidence is in
`planning/continuation-20261113/PUBLICATION_STATUS.json`.

The new work is checkpointed on `research/continuation-20261113-b`. Intermediate
checkpoints are work in progress; the live release remains identified by the
commits above until a newly verified release is published.

## Concrete correctness finding

The existing `weighted_gain_certificate` routine documents an exact rational
check of `G w <= q w`, but does not enforce its scalar input domain. It accepts
floating-point and infinite values. A scalar test with `G = [[1.01]]`, the
smallest positive binary64 weight and `q = 0.99` returns true after both products
round to the same subnormal value. Exact rational arithmetic on those same
binary values rejects the inequality. An infinite weight is also accepted.

These are invalid-input acceptance defects, not counterexamples to the
rational weighted-gain proposition. The reproducible pre-correction record is
`weighted-gain-before.json`. Existing valid rational examples remain separate
from these negative observations.

## Iterative implementation plan

1. **Exact executable contract.** Enforce built-in integer/Fraction inputs,
   reject floating, nonfinite and Boolean scalars, preserve the existing valid
   rational API, and retain exact row residuals in a replayable certificate.
   Independently check rational inequalities using integer cross-products.
   Validate malformed, tampered and arithmetic-boundary cases.
2. **Formal weighted-gain theorem.** Add a pinned Lean module for positive-weight
   row inequalities, monotonicity of feasibility, signed matrix-action bounds,
   and time-varying propagation under a common gain envelope. Add forced-error
   convolution only if its exact hypotheses and proof are completed. Relate
   each checked declaration to `prop:weighted-gain-feasibility`; do not imply
   optimizer correctness or that a proposed gain matrix bounds every Jacobian.
3. **Source access and upstream evidence.** Attempt legitimate primary-source
   retrieval for the six documented full-text gaps and a reproducible original
   video transcript record. Preserve unsuccessful access observations. Inspect
   existing pinned upstream Lean cache artifacts offline before considering
   any further bounded download; no new upstream verification is claimed yet.
4. **Integrate and verify.** Update the mathematical and implementation notes,
   exact declaration maps and affected source-hashed records. Run the targeted
   numerical and formal checks, then rebuild affected PDFs and release assets.
   Preserve older evidence as explicitly dated snapshots.
5. **Publish and synchronize.** Push reviewable checkpoints periodically. Move
   `main` only after the new release gates pass, deploy the combined Pages site,
   verify served hashes and affected controls, and fast-forward the authorized
   clones without overwriting unrelated work.

## Acceptance and scope

The exact checker must reject the reproduced invalid-input false positives and
tampered witnesses. The Lean proof must derive its output estimate from finite
sum and absolute-value inequalities, rather than assume the desired conclusion.
Fresh exact types, axiom inventories and warning-free compiler output are
required. Finite gain certificates do not establish continuum estimates, GRH,
Yang-Mills mass gap, quantum advantage or cryptographic protocol security.

Private authentication material and machine identifiers are excluded from this
checkpoint. No credential contents were needed for the read-only baseline
inspection. Public source and artifact exclusions remain in effect.
