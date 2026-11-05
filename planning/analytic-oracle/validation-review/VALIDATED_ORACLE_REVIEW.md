# Independent validated-oracle and finite-readout review

2026-11-04, entirely on iska-linux-vscode. Root production paths were read
but never edited by this reviewer. Review/check artifacts only were written
under the explicitly assigned validation-review and output/review paths.
No new dependencies, authentication, GPU/model jobs, existing-source changes
or Mac writes. Existing remote mpmath1.4.1 was used only for diagnostics.

## Verdict

The frozen final-v5 producer and supplied finite certificates are accepted
within their stated scope: primitive quadratic completed Dirichlet functions
q3/q4/q5, exact enclosed64-circle nodes, degree28 exact-rational midpoint
polynomials on |s−1/2|<=7/10, and strict uniform bound5e-15. The classical
primitive theta/Mellin identity is an explicit external analytic theorem.
No zero-location, arithmetic determinant identification, general conductor
uniformity, arbitrary-requested-tolerance implementation or new Lean proof
is inferred. The optimizer value is a closed-form exact GD iterate, not an
executed180-update training trace.

Final producer source hashes checked against saved source copies:
- dyadic.py:82e995ae9f67395980cec3f06bf493931de0413c7ce024562283882c01425170
- theta_oracle.py:c50857831de0fc5faa6829cf539c7d31dc32958b76412c27689235aeba95d2c1

The companion PRIMITIVE_ENCLOSURE_REVIEW.md gives the reviewed exact
Machin/log/exp formulas, outward integer rounding, Cauchy coefficient
recurrence, safe per-panel discard and final error-ball construction.
The standalone core/details text agrees with these formulas. The requested
self-contained U16/n0=8 growth formula is now included and independently
checked in its own section, with k2 for odd and k1 for even characters,
proving M<4/10/6. No required mathematical or self-containment correction
remains in the reviewed producer or standalone proof.

## Bugs/precision issues found and resolved

1. Negative quadrature order K could make the remainder majorant negative.
   The producer now rejects negative/noninteger K and asserts nonnegative
   radii/error pieces. Malformed readout dimensions/orders are also rejected.
2. Un-typed lru_cache could bypass a type guard: after caching log(Fraction(1)),
   log(1.0) returned the cached result. All relevant caches are now typed,
   and explicit cross-type primed-cache negative controls pass.
3. The old reported global bound was below the sum of individually rounded
   reported components by2–3ulp. The final producer rounds each component
   first and then sums those exact components; final data verify the printed
   inequality literally. The old raw computation was still conservative,
   but serialization needed this correction for direct auditability.
4. Provenance snapshots were previously read only at experiment end. The
   final run captures source at entry and checks it unchanged before emission.
   Final-v5 snapshot hashes match the independently inspected live sources.
5. Tiny exponentials can amplify fixed absolute rounding through large late
   Taylor coefficients. A correctly proved per-(n,panel) whole-contribution
   bound permits omission below2^-90, with every such error added explicitly.
   It precedes recurrence evaluation and follows a parameter-domain check.

All earlier pilots/failure probes remain preserved. The actual certificate
path uses exact integers/Fractions and outward dyadic intervals. Float fields
are display summaries; they are not proof endpoints or target oracles.

## Independent checks executed

-843 primitive checks: independently enumerated exact interval endpoint
 arithmetic, negative division, invalid inputs; exp(log x)=x and exp(i*pi)=−1
 enclosures; high-precision pi/log/exp diagnostic containment.
-1160 exact rational complex coefficient identities: the scaled recurrence
 versus an independent generalized-binomial/exponential convolution,
 40parameter cases through degree28.
-24 negative controls: primed-cache float aliases, conductor/order/domain
 violations, malformed circle and readout dimensions/steps.
-Final-v5 all192 circle nodes and completed-function values compared against
 independent110-digit Gamma/Hurwitz-Dirichlet evaluations. Every target is
 inside its certified complex disk; every node lies in its recorded rectangle.
-All1536 sample component checks pass. Bare quadrature-box halfwidths are
 reconstructed exactly; n/time/quadrature/discard pieces are nonnegative;
 final sample radii dominate their exact sum with only the documented
 outward dyadic rounding. No error term is silently discarded.
-All87 coefficient rectangles contain independently computed110-digit
 Fourier/GD coefficients. Exact oracle, alias, Taylor and coefficient-rounding
 component calculations agree with their exported upper bounds.
-All144 compact-boundary numerical polynomial comparisons stay inside the
 global certificates. These comparisons are diagnostics, not a proof of the
 uniform theorem; the Cauchy/Fourier error derivation supplies that theorem.

Final exact global bounds (decimal displays only):
q3:1.7850692874475243e-15
q4:4.454049465469766e-15
q5:2.905620215391504e-15
Each exact serialized rational is strictly below5e-15.
Max observed sample-reference discrepancy:7.774454644802258e-27.
Max observed compact-boundary discrepancies:1.90e-23,3.31e-23,3.19e-23.
Observed errors must not replace the larger certified uniform bounds.

Evidence:
outputs/checks/2026-11-04-validated-oracle/review/
  primitives-independent-1793812501863728623.json
  recurrence-independent-1793812412600535543.json
  guards-independent-1793812785271473933.json
  full-dataset-independent-1793812841478379102.json

## Remaining limits

The fixed N11/T128 analytic tails impose a floor; changing an accuracy
request needs new proof-preserving truncation/precision choices. The code is
not kernel-checked Lean and trusts the usual Python integer/rational runtime
plus the separately reviewed analytic arguments. General Artin holomorphy,
Weil positivity and unknown zero locations are nowhere assumed. The actual
positive arithmetic determinant bridge and original signed low-gcd estimates
remain independent open research obligations.

## Final editorial clarification: normalized polynomial basis

The stored Fourier/readout coefficients are coefficients in the normalized
basis, not raw powers of s-1/2. Precisely, with rho=6/5 and each stored exact
rational complex midpoint denoted btilde_n, the certified exported object is

P_q(s) = sum_{n=0}^{28} btilde_n ((s-1/2)/(6/5))^n.

This is required: the DFT produces b_n approximately equal to a_n rho^n,
while every compact-disk coefficient error is weighted by (R/rho)^n.
Using raw powers without dividing the coefficients by rho^n would specify
a different polynomial and would not inherit this certificate. Alternatively,
raw-basis coefficients may be explicitly converted to btilde_n/rho^n.
Clarifying the manuscript definition and outward-rounding its display table
are editorial changes only. The final-v5 certificate bytes have SHA256
85e3bed76ad4067084ab5f8413b7159e4c5169e5d7cef0469d36164e82dfbca8;
the validated source hashes and all exact serialized rational certificates
remain unchanged. Table entries used as upper bounds must be rounded upward,
while diagnostic displays may be marked approximate. No experiment rerun is
necessary for these clarifications.

## Objective normalization and the exact gradient-descent recurrence

The specified objective L(b)=(1/128) sum_{j=0}^{63}|(A b)_j-y_j|^2,
A_{jn}=zeta_j^n, 0<=n<=28, is one-half of the mean squared complex
residual. Identify C^29 with R^58 with its usual Euclidean metric.
For a complex perturbation h, its real differential is

D L(b)[h] = (1/64) Re <A h, A b-y>
            = Re <h, b-b*> ,

because A* A=64 I and b*=(A* y)/64. Consequently the Euclidean real
coordinate gradient is represented by the complex vector b-b*.
Step size 1/4 therefore gives b^{k+1}=(3/4)b^k+(1/4)b* and, from b^0=0,
b^k=(1-(3/4)^k)b*. This proves the precise recurrence whose closed form
the producer evaluates. Complex Wirtinger derivatives alone use a different
factor convention; the explicit real-Euclidean statement removes that
ambiguity. Exact roots and degree28<64 supply the orthogonality. This
prose clarification leaves final-v5 and its source snapshots unchanged.
