# Explicit convergence of variable-length primitive evaluation

5 November 2026. Independent analytic addendum to the adaptive-theta design. This review writes only fresh files under planning/adaptive-theta-20261105/design/; production sources and all earlier design/verification artifacts are unchanged.

Read implementation: examples/analytic_oracle/precision.py
SHA256 897716c550e96ab667661a4fc89257e6e9fb0b3ffb0fec4b85a3597033cf20bd

Read accepted proof: papers/adaptive-theta-details.tex
SHA256 bc67cead9058c83f5b7e42541c70ec03154130980fe2dc1bb9f8babab1e07e41

## Gap and conclusion

The current prose states that primitive interval widths tend to zero, then invokes continuity through a finite expression. The exponential's Taylor length H grows with precision, so it needs a bound uniform in H rather than an induction that presumes a fixed number of primitive operations. The following elementary estimates fill that explanatory step. They establish the stronger bound O(input width+p*2^(-p)) before the bounded number of squarings, with no global complexity assertion. Inclusion of every primitive is already supplied by the outward/tail proof; this addendum concerns shrinking width.

## Rectangle operation bounds

Put e=2^(-p), delta=2^(-p-16). Let d(X) be the sum of the two full coordinate widths, and m(X) the sum of their maximum absolute endpoints. A real outward multiplication adds less than2e to full width and at most e to magnitude. There are four such real products in complex multiplication; addition/subtraction at the same dyadic scale is exact. Hence

 d(XY)<=m(X)d(Y)+m(Y)d(X)+8e,
 m(XY)<=m(X)m(Y)+4e.

For division by an exact positive integer j,

 d(X/j)<=d(X)/j+4e,
 m(X/j)<=m(X)/j+2e.

These follow directly from rounding each real endpoint down/up by at most one ulp. They are valid for rectangles even though dependency can make the product enclosure larger than the exact image. They do not assume that every point in the rectangle is a coherent product of input points.

## Reduced input and a uniform order bound

The implementation halves the exact input-rectangle magnitude until A=m(Z)/2^k<=1/2. Dividing the original dyadic rectangle by2^k gives W with

 a=m(W)<=A+2e<=1/2+2e<0.51<3/5,
 d(W)<=2^(-k)d(Z)+4e.

These hold for every p>=32. The Taylor remainder bound for the true reduced input is

 T_H=A^(H+1)/(H+1)!/(1-A/(H+2)).

Its denominator is at least3/4 and factorial at least1, so T_H<=2^(-H). Thus the first accepted H is at most p+16 (and certainly at most p+18). The small outward widening of W does not invalidate inclusion: the remainder uses the true reduced argument bounded by A, while polynomial evaluation on W contains that argument. For the width estimate, use the slightly larger a above.

## Summing all growing-order interval widths

Let T_0=1 and T_j=(T_(j-1)*W)/j be the actual outward term rectangles, with m_j=m(T_j), d_j=d(T_j). The operation bounds and j>=1 give

 m_j <= a*m_(j-1)+6e,
 d_j <= a*d_(j-1)+m_(j-1)*d(W)+12e.

Since m_0=1 and d_0=0, the first recurrence gives m_j<=a^j+15e using a<=3/5. Put S=sum_(j=0)^H d_j. Summing the second recurrence and discarding a nonnegative terminal term gives

 (1-a)S <= d(W)*[(1-a)^(-1)+15He]+12He.

Every rectangle satisfies d(W)<=2m(W)<=6/5. Therefore

 S <= d(W)/(1-a)^2 + [(15d(W)+12)/(1-a)]He
   <= (25/4)d(W)+75He.

The implementation adds all term rectangles at the same scale, so additions introduce no further rounding. The symmetric remainder expansion adds at most4(delta+e) to full L1 width: each of two coordinates is expanded on each side by ceil(delta/e)*e. This remains true when the actual tail is strictly smaller than delta.

Thus the pre-squaring width is O(d(Z)+p*e), despite growing H. Its magnitude is bounded by

 (1-a)^(-1)+15(H+1)e+2(delta+e)
 <=5/2+[15(p+19)+2+2^(-15)]2^(-p)<3

for every p>=32. The final elementary inequality is strongest at p=32 since (p+19)2^(-p) decreases thereafter.

## Squaring and the remaining primitives

For each outward square, d(X^2)<=2m(X)d(X)+8e and m(X^2)<=m(X)^2+4e. For a bounded input family Z_p with shrinking width, the halving count k is uniformly bounded. Starting from the pre-squaring bound and magnitude<3, finitely many iterations of these recurrences give final width O_k(d(Z_p)+p*e), tending to zero. The hidden constant may depend on the fixed input bound and maximum k. No bound uniform in all possible sample requests or a global bit-complexity estimate is asserted.

Arctangent and logarithm partial sums use exact Fraction arithmetic and only their final interval endpoints are converted to p-bit dyadics. Each atan interval has width at most delta+2e; multiplication by16 and-4 is exact at the dyadic scale, giving pi width<=20delta+40e. For fixed rational x=2^k v, the two reduced logarithm intervals similarly give width<=(1+abs(k))(delta+2e). These estimates tend to zero even as their exact rational series lengths grow.

Consequently the primitive convergence step is valid with variable series lengths. Induction through the genuinely finite outer theta/recurrence expression, for fixed N/J/K and a fixed exact target, now applies. Refining regenerated circle nodes is included; a fixed nondegenerate input rectangle is still outside the shrinking-input contract.

## Proposed insertion

precision-convergence-addendum.tex is a short self-contained paragraph for the existing primitive/termination proof. It changes no algorithm, certificate budget, accepted sample or frozen producer. The formulas use full coordinate widths; the output interval radius is half that quantity, so width convergence implies the required radius convergence.

## Focused exact checks

A read-only Linux check of the stated inequalities at p=32,64,128,256,512 and four exact input boxes (including zero, a half-unit input, a general complex input, and magnitude above1000) passed20 configurations and1856 exact rational inequality controls. It checked normalized magnitude/width, the growing-order bound, every term recurrence bound, their literal accumulated width, the magnitude bound and the outward-square inequality. The maximum observed Taylor order was86; no special-function reference value was used. These checks are diagnostics for the explicit operation constants; the uniform-in-p proof above supplies convergence. No output/data/dependency or production source was changed.
