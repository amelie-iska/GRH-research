# Requested-error readouts with an executed rational optimizer

5 November 2026. This extends the preserved fixed theta/Mellin certificates,
without recomputing their 192 labels or changing their accepted sources.
For each completed primitive quadratic Dirichlet function q=3,4,5, the
new standard-library producer scans degrees0–63 and accepts an exact rational
requested uniform error only when its exact five-term budget has strict slack.
Otherwise it returns the minimum computed base budget and refuses.

The actual objective is J(b)=1/2 sum_n |b_n−t_n|² for rational midpoint
Fourier targets. Every update b←3b/4+t/4 is executed using Fractions, and
every coefficient, objective value and weighted residual is saved. These are
not the ideal true-root least-squares iterates: the coefficient rectangles
bound their gradient/target perturbation explicitly. The polynomial uses
((s−1/2)/(6/5))^n on |s−1/2|<=7/10.

The final-v3 runs at requested1e-15 select degrees29,30,30 and execute
122,123,123 updates. Their certified uniform bounds, displayed approximately,
are9.0712202398e-16,9.7497570634e-16,9.7666224003e-16 (the displayed upper
bounds are rounded upward). Requested1e-12 selects degrees23,24,24 and
100,100,98 updates. Exact acceptance uses serialized rational endpoints.

The five terms are the actual optimization residual, preserved oracle
radii,64-node aliasing, analytic Taylor tail, and Fourier rectangle-to-midpoint
error. The minimum base budgets are approximately7.29e-17,1.74e-16,3.37e-16;
these are floors of this fixed-data majorant, not lower bounds on actual
approximation error. A request1e-18 is explicitly declined. Increasing the
number of updates cannot reduce fixed sampling and alias budgets. A fully
adaptive theta oracle needs new proof-preserving truncations and primitive
series/interval precision, and remains unfinished.

Reproduce on Linux from the repository root with a fresh output directory:

```sh
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 nice -n 15 python3 examples/analytic_oracle/adaptive_readout.py --tolerance 1e-15 --output outputs/experiments/NEW-requested-readout
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s examples/analytic_oracle -p test_adaptive_readout.py -v
```

Exact final evidence lives in
outputs/experiments/2026-11-05-adaptive-readout-{1e-12,1e-15}-v3/.
Earlier v1/v2 outputs and failed probes remain preserved. Independent checks
reconstruct the Fourier enclosures, replay all666 updates/18,802 coefficient
states, test strict-floor refusal and tiny positive slack, and retain the
original source/certificate hashes. Diagnostic special-function comparisons
are separately labelled; they do not supply interval inclusion.

The [interactive laboratory](https://amelie-iska.github.io/GRH-research/readout.html)
shows saved states, the quadratic loss, five budgets and complex boundary
images. Its decimal projections are illustrative; complete exact certificates
and producing snapshots are linked. The concise/extended shared proofs are
papers/adaptive-readout-{core,details}.tex.

This is a finite linear readout, not quantum training or an upstream neural
checkpoint replay. It proves no all-conductor uniformity, zero-location,
positive arithmetic determinant, full Lean formalization or GRH. The active
arithmetic covariance and determinant obligations remain separate.
