# Design and proof handoff

The selected next extension is a requested-rational-tolerance readout on the
fixed compact |s-1/2|<=7/10, using the accepted frozen64-circle labels. It
executes exact rational GD on explicitly declared rational Fourier-midpoint
targets, certifies their perturbation from ideal-root Fourier targets, and
refuses unsupported tolerances by an exact finite-degree budget scan.

* `adaptive-readout-core-proposal.tex` and
  `adaptive-readout-details-proposal.tex`: selected implementation proof,
  matching the current simple optimization plus whole-DFT-radius budget.
* `DESIGN.md`: source/provenance inspection, full parameter/stop proof,
  optional sharper budgets and future adjustable compact/exact-endpoint
  rectangle alternatives, and a separately labelled future adaptive-theta
  parameter/precision convergence design. The initial alignment note states
  which alternatives the delivered executable does not implement.
* `check_design.py`: independent Fraction endpoint rectangle propagation and
  analytic/optimizer parameter checks; imports no production module.

Checks ran only over SSH in the existing Linux environment. The independent
check script passed1,792exact assertions. Receipt:
`outputs/checks/2026-11-05-adaptive-readout/design/design-checks.json`.
It checked accepted source hashes and frozen hash unchanged, complete node
indices, exact floor-equality refusal and strict-slack acceptance, exact
executed objective contraction9/16 and residual contraction3/4, independent
Fourier rectangle containment in both new production output sets, and
matching minimizing degrees56/56/55. At1e-15 it independently reproduces
selected degrees29/30/30 and update counts122/123/123.

The two shared TeX proposals compile as a2-page standalone preview at
`outputs/checks/2026-11-05-adaptive-readout/design/proposal-preview.pdf`.
The sole TeX warning is the preview wrapper's omitted author; no overfull or
underfull boxes were reported. Build stdout and transcript are preserved.

Exact base floors of the selected budget are approximately
7.292853591735253e-17,1.7369759965161748e-16,3.374091218773938e-16
forq3/q4/q5. The exact rational floors, not these displays, control acceptance.
They are attainability boundaries for this fixed-data majorant, not
impossibility results about polynomial approximation. The source sample
radii cannot be replaced by smaller diagnostic discrepancies.

No theta oracle rerun, general adaptive-precision implementation, new Lean
check, all-conductor proof, zero-location claim or GRH proof was performed.
No production sources, accepted data, dependency/environment, queue,
publication, authentication or GPU state were edited by this design task.
