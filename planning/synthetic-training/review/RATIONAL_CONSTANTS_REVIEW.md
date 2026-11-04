# Exact rational learning constants: independent review

Reviewed2026-11-04: `certify_learning_constants.py`, preserved v1--v4
`rational-constants.json` outputs, v4 source snapshot, final web copy and the
new final subsection of `holomorphic-learning-details.tex`. Only review
files/evidence were written; no remote job, credentials, dependency, production
source, model repository or prior certificate was changed by this reviewer.

Verdict: **accepted on final v4**. The inequalities, all exact output fractions,
integer growth bounds and declared certification boundary are correct. One
floating-parity API loophole was discovered during review and fixed; it never
affected the saved main-path rational values. All requested fixes are resolved.

## Why the rational bound is valid

Let `d=pi/q` and `delta=3/q`. Since `0<delta<d`, lowering the Gaussian
exponent increases every positive Mellin-integral majorant. The integer k
and `Q_k` are the same previously reviewed disk-growth bound, for center1/2
and radius12/5.

For positive rational x and integer L>=1, binomial coefficients satisfy
`choose(L,j)/L^j <= 1/j!`. Thus `(1+x/L)^L <= exp(x)` and
`exp(-x) <= U_L(x)=(1+x/L)^(-L) < 1`. Its evaluation uses only rational
operations. This proves the manuscript's elementary majorant without
transcendental rounding in the certificate.

For odd parity, `n exp(-delta*n^2/2)` is bounded by
`1/sqrt(delta*e) <= 1/sqrt(delta)`. The rational
`C1=(1+1/delta)/2` is at least `1/sqrt(delta)` by AM--GM;
equivalently `delta*C1^2-1=(delta-1)^2/(4*delta)>=0`.
For even parity, C0=1 suffices.

Split `exp(-delta*n^2)` into two halves and use the C bound on one half.
The remaining Gaussian tail, together with decreasing positive Q, is bounded
by

`C Q(delta*n0^2) exp(-delta*n0^2/2) / (1-exp(-delta*n0))`.

Replacing its positive numerator exponential with U increases it. Replacing
the geometric ratio with U also increases it, because
`0<exp(-delta*n0)<=U(delta*n0)<1`; the new denominator remains positive and
is smaller. This proves exactly the displayed rational tail. It does not
require U to preserve exponential multiplication or Gaussian semigroup laws.
Adding the finite positive prefix and both Mellin terms proves the claimed
rational `Mhat` bound.

For conductors3,4,5 with parities1,1,0, `n0=8,L=16`, exact reconstruction
confirms strict upper bounds `Mhat<4, Mhat<10, Mhat<6` and exact integer
ceilings4,10,6. Aliasing and Taylor expressions use the tighter exact Mhat
fractions; the prose now correctly permits Mhat or its integer upper bounds.
The rational radii and fixed64 samples make these expressions exact rational
certificate terms. The oracle term remains conditional on eta=10^-12 and
does not certify eta itself.

## API and provenance corrections resolved

Initially `growth(3,1.0)` passed the parity-membership test and returned a float
because `n**1.0` contaminated the prefix. Main only called integer parities,
so v1--v3 stored values remained valid. Final source requires actual integer
types for conductor, parity and cutoff, and Fraction-positive exponential
arguments. The floating-parity negative control now rejects as intended.

Final v4 explicitly records center real1/2, imaginary0 and the normalized
completed Dirichlet target. It includes `generation_source.py` and a matching
SHA256. The web JSON is byte-identical to v4. All prior numeric Mhat and model
terms remain unchanged, while the earlier versions remain preserved.

## Fresh independent exact checks

Reproduce:

```sh
python3 -B planning/synthetic-training/review/check_rational_constants.py
```

The checker independently rebuilds Q using its integration-by-parts coefficient
recurrence and U as a positive rational power. It verifies normalized
numerator/denominator pairs for all three growth/construction records and all
twelve model rows' alias, Taylor and assumed-eta terms. It also confirms the
strict integer bounds, exact source snapshot hash, byte-identical web copy and
unchanged numerical records across preserved v1--v3.

Twelve negative-domain controls pass: zero/negative/floating exponential x;
zero/negative/floating L; too-small/floating conductor; invalid/floating parity;
and zero/floating cutoff. Evidence is
`outputs/checks/2026-11-04-synthetic-training/review/rational-constants-review.json`.
Display floats are checked only for correspondence with the stored fractions;
they are explicitly excluded from the certificate arithmetic.

## Certification boundary

This step certifies growth, Gaussian-tail majorants and the resulting analytic
alias/Taylor constants under the previously stated primitive-nonprincipal
theta/Mellin identity. It does **not** certify the complex contour sample
evaluations, their eta, floating FFT/GD coefficient rounding or a complete
four-term end-to-end evaluation budget. The high-precision learning demo is
still unvalidated numerics. No new Lean declaration, all-conductor efficiency
theorem, arithmetic positivity, determinant identification or GRH claim is
introduced. The final manuscript and JSON retain these limits correctly.
