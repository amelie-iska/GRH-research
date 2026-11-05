# Fresh adaptive theta sampling and requested-error analytic readouts

5 November2026. The preserved fixed-label API and its certificate floors are
unchanged. New modules `precision.py`, `adaptive_theta.py`, `adaptive_family.py`
remove that fixed-data obstruction by choosing new sample parameters, root
precision, circle count and polynomial degree for the requested error.

The scope is the completed primitive quadratic Dirichlet functions of
conductors3/4/5 and |s−1/2|<=7/10. The classical primitive theta/Mellin identity
with rootnumber1 is an explicit external analytic input. No zero-location,
Artin holomorphy, desired positivity or determinant identity is assumed.

For a rational sample request eta>0, sequential exact comparisons select
retained n cutoff N, dyadic time cutoff T=2^J, and Cauchy order K. The
nonincreasing exact bound E(x)=2^(-floor(x)) majorizes exp(-x); each true
exponential is bounded separately, without assuming E is multiplicative.
Each n/time/quadrature/discard budget is <=eta/8. The actual interval
L1halfwidth must be <=eta/4, with regenerated point/root enclosures on retry.
Five bounds are rounded UP at a request-dependent dyadic scale B satisfying
5*2^-B<=eta/8; their literal sum is <=7eta/8. A chunked integer encoder/parser
avoids both giant raw-tail fractions and the interpreter's decimal digit
limit without changing global settings. Growing primitive Taylor orders are
handled by explicit width bounds O(inputwidth+p*2^-p), not a fixed-order
assumption.

For requested compact error epsilon, choose degree and circle count so each
Taylor/alias term is <=epsilon/8, and eta=epsilon*(1−7/12)/8. Regenerate the
nodes/samples until the finite Fourier rectangle-midpoint term is also
<=epsilon/8. Execute exact rational GD for the explicit Fourier-midpoint
quadratic objective until its weighted residual is <=epsilon/4. Round the
five final bounds upward with totalrounding<=epsilon/8. The printed uniform
bound is <=7epsilon/8. Termination is proved in the mathematical unbounded-
resource model; no practical runtime or memory bound for extreme requests
is claimed.

The supplied final-v2 requested1e-24 run has degree48 and88truecircle samples
per conductor. It executes196/197/197updates. Certified uniform bounds,
rounded upward for this display, are:

|q|Uniform upper bound|Updates|
|---|---:|---:|
|3|2.71418638494e-25|196|
|4|4.07127957742e-25|197|
|5|3.36042123850e-25|197|

All590updates/593vectorstates/29,057complexcoordinate states are exactly
recoverable from a shared rational target vector and per-state rational
scale extracted AFTER executing vector updates. Independent replay checks
all coordinates, state hashes, objectives, residuals and first stopping step.
The saved trajectory is the specified midpoint objective, with certified
true-root least-squares perturbation; it is not ideal-root or quantum/upstream
training. A separate192-sample64circle experiment certifies eta1e-32.

Reproduce from the repository root on Linux, using fresh output directories:

```sh
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 nice -n 15 python3 examples/analytic_oracle/adaptive_family.py --tolerance 1e-24 --output outputs/experiments/NEW-adaptive-family
PYTHONDONTWRITEBYTECODE=1 python3 examples/analytic_oracle/adaptive_theta.py --sample-error 1e-32 --m 64 --output outputs/experiments/NEW-adaptive-samples
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s examples/analytic_oracle -p 'test_adaptive*.py' -v
```

Independent scientific acceptance: outputs/checks/2026-11-05-adaptive-theta/review/.
Sampler7241checks and family8666checks include exact reconstruction, negative
controls, forced node-refining precision retry and separately labelled
high-precision diagnostics. Existing fixed producer/certificates remain
byte-identical. Failedpilot serialization, all previous versions, and the
failed firstHTML staging check remain preserved; only accepted artifacts
are promoted.

The [interactive laboratory](https://amelie-iska.github.io/GRH-research/readout.html)
separates fresh adaptive sampling from the preserved fixed-label runs. It
shows actual saved sampler parameters and numerical projections of exact
states/gradients. Decimal drawings are illustrative; linked rational
certificates are authoritative. The proof is in chapter38 and both article/
note editions. This is compact approximation of known functions: output
polynomials need not be real-rooted or arithmetic spectral determinants.
All-conductor/height extensions, analytic/category Lean and the independent
positive determinant/zero-location bridge remain open. GRH is not proved.
