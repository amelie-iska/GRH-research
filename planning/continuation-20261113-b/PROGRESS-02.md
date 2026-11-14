# Verified weighted-gain continuation

This research-branch checkpoint follows `e82467b`. It preserves completed
source changes and their fresh evidence before the next manuscript extension.
The published `main`/Pages edition is still the earlier verified release;
PDFs and downloadable archives will be rebuilt before the next release.

## Completed in this checkpoint

- Enforced the exact integer/rational domain of the weighted-gain API before
  arithmetic. Historical subnormal and infinite-weight false positives are
  retained as negative evidence, not relabeled as rational counterexamples.
- Added canonical rational JSON witnesses and an independent integer-only
  replay checker with separate accepted, rejected and malformed outcomes.
- Passed 15 test methods, 256 seeded exact comparisons, 84 invalid-scalar
  cases, 16 evidence mutations and 21 isolated CLI cases. Existing toric
  calculations retain their prior exact outputs; their source hash is new.
- Added six Lean declarations for fixed-rate feasibility, signed matrix
  action, and time-varying gain propagation with an explicit residual sum.
  Fresh audits pass 121 extension declarations in seven modules and 368
  inherited declarations in 37 files: 489 declarations in 44 source files.
- Added the matching written theorem and exact implementation contract.
  The claim map assigns 74 declarations to parts of 27 environments and
  continues to mark zero whole composite environments fully formalized.
- Independently reread all 249 transcript entries and verified the exact
  canonical extraction in a private cache outside Git. Only its provenance
  and digest are public. The six remaining original-paper access gaps remain.

## Next bounded addition

The requested quantum--tropical fluid realization chapter will connect the
pinned ToricGT-style graph model to finite quantum channels, nonlinear
feedback dynamics, tropical envelopes and control certificates. It will
separate established source results, locally proved finite statements and
proposed mappings to engineered or natural substrates. A generative design
pipeline must pass physical and control checks before a generated material
is described as realizing a specified operator.

The independent upstream Lean 4.34 continuum build remains incomplete.
An offline cache inspection is in progress; this checkpoint does not upgrade
its status or claim stronger Navier--Stokes, GRH or mass-gap results.
