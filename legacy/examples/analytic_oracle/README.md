# Validated theta/Mellin targets and rational Fourier readouts

This directory implements a fixed, outward-rounded evaluation certificate for the completed primitive Dirichlet functions of conductors 3, 4 and 5. The characters, parities, primitive theta identity and root-number normalization are explicit. No hypothesis on zero locations is used.

The frozen accepted run is `outputs/experiments/2026-11-04-validated-oracle-final-v5/`. It contains 192 true circle-node enclosures, exact sample centers and radii, three rational degree-28 readouts, full component budgets and copies/hashes of the producer. Both producer files use only the Python standard library. Existing mpmath is used separately for independent diagnostic comparisons.

Run from the repository root on Linux, choosing an output directory that does not exist:

```sh
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 nice -n 15 python3 examples/analytic_oracle/theta_oracle.py --output outputs/experiments/NEW-validated-oracle
```

The program refuses to overwrite an experiment. Defaults are 64 nodes per conductor, quadrature order 12, retained n=1..11, time cutoff 128, and 224-bit dyadic rectangles. Error budgets are rounded upward to 180-bit dyadic rationals. The current truncations are fixed: this is not an arbitrary-requested-accuracy API. A stride greater than one is a sample-only diagnostic and does not emit a complete readout certificate.

For each exported model let c_n be its exact rational real/imaginary coefficient pair. The actual polynomial is

`P_q(s) = sum_{n=0}^{28} c_n * ((s - 1/2)/(6/5))**n`.

The normalization is essential. The proved compact is `abs(s-1/2) <= 7/10`. The strict certified uniform errors are below 5e-15 for each conductor. The coefficients evaluate the closed-form 180-step gradient-descent iterate from zero initialization with step 1/4; no executed optimizer-loop trace or quantum-training advantage is claimed.

`dyadic.py` encloses primitive rational arithmetic, Machin pi, range-reduced logarithms and complex exponentials. `theta_oracle.py` adds Cauchy-controlled panel integration, all omitted-tail/discard errors, exact growth constants, circle-node enclosures, DFT/GD rectangles and coefficient rounding. A complete (n,panel) contribution may be skipped only after adding its explicit whole-contribution bound; this prevents large late coefficients amplifying fixed absolute exponential roundoff.

The independent review and acceptance receipt are under `planning/analytic-oracle/validation-review/` and `outputs/checks/2026-11-04-validated-oracle/review/`. They cover 843 primitive cases, 1160 exact recurrence identities, 24 negative controls, all 192 sample and 1536 component checks, 87 coefficient enclosures and 144 boundary diagnostics. High-precision comparisons are diagnostics; the interval inclusion, analytic bounds and exact five-part budget provide the certificate. Earlier iterations and failures remain preserved.

Proof editions: `papers/validated-oracle-concise.tex` and `papers/validated-oracle-extended.tex`; compiled copies are under `outputs/papers/validated-oracle-20261104/`. The independent arithmetic moment development is documented separately in `research/validated-oracle-and-masked-moment.md`.

The implementation is not kernel-checked Lean. It does not construct a self-adjoint arithmetic determinant, force real-rooted polynomials, settle the original signed short-row/covariance problem, prove Artin holomorphy, or prove GRH. These are separate explicit research obligations.

## Requested-error extension and executed readout training

`adaptive_readout.py` reuses the immutable final-v5 labels, selects a degree
and executes exact rational GD updates for an explicitly stated midpoint
Fourier objective. Its certified perturbation from ideal-root least squares
is included in the five-term budget. The actual loop trace is saved in full.

```sh
PYTHONDONTWRITEBYTECODE=1 python3 examples/analytic_oracle/adaptive_readout.py --tolerance 1e-15 --output outputs/experiments/NEW-requested-readout
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s examples/analytic_oracle -p test_adaptive_readout.py -v
```

The final-v3 examples at1e-12/1e-15 use degrees23–30 and98–123 updates.
Requested1e-18 is refused by the fixed-data majorant. This is not an arbitrary-
accuracy theta API: sample/truncation/alias floors remain. Exact endpoints,
source pins, normalized coefficients and all updates are in the linked
[research record](../../research/requested-readout-training.md). The
[interactive replay](https://amelie-iska.github.io/GRH-research/readout.html)
uses display-only decimal projections; complete exact certificates supply
its proof. No additional dependency, Lean theorem, zero-location or GRH
claim is introduced.

## Fresh adaptive sampler and end-to-end family driver

The separate `precision.py`, `adaptive_theta.py` and `adaptive_family.py`
implement new sampling/precision/node/degree choices, retaining the old
fixed-source/API certificates unchanged. See
[full proof and reproduction](../../research/adaptive-theta-and-readouts.md).

```sh
PYTHONDONTWRITEBYTECODE=1 python3 examples/analytic_oracle/adaptive_family.py --tolerance 1e-24 --output outputs/experiments/NEW-adaptive-family
PYTHONDONTWRITEBYTECODE=1 python3 examples/analytic_oracle/adaptive_theta.py --sample-error 1e-32 --m 64 --output outputs/experiments/NEW-adaptive-samples
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s examples/analytic_oracle -p 'test_adaptive*.py' -v
```

The mathematical arbitrary-request termination statement is for fixed q = 3, 4, 5
and the stated compact/domain with unbounded resources. Extreme requests can
be computationally impractical. Output coefficients and compressed executed
trajectories remain exact; graphics are decimal projections. No new Lean,
quantum-advantage, zero-location or GRH claim.
