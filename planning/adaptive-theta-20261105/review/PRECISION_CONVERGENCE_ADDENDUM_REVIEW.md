# Independent review of the growing-order primitive bound

The added paragraph in papers/adaptive-theta-details.tex is accepted. It closes
the dependence of interval roundoff on an exponential Taylor order that grows
with precision. The producer, accepted numerical certificates, exact checks and
other three scientific TeX files are unchanged. The previous acceptance receipt
remains preserved; final-acceptance-v2.json binds the revised four-file proof set.

Write e=2^-p and delta=2^(-p-16), p>=32. For a real interval product, its exact
width is at most m(X)d(Y)+m(Y)d(X); outward rounding adds at most2e. Summing
the four real products in complex multiplication gives magnitude error at most4e
and total coordinate-width error at most8e. Integer division adds at most2e to
magnitude and4e to total width. Since the term divisor j is at least1, these give
the paragraph's conservative recurrences m_j<=a*m_(j-1)+6e and
d_j<=a*d_(j-1)+m_(j-1)*d(W)+12e.

Exact halving followed by outward integer division gives
m(W)<=1/2+2e<3/5 and d(W)<=2^-k*d(Z)+4e. The geometric recurrence yields
m_j<=a^j+6e/(1-a)<=a^j+15e. Every rectangle has d(W)<=2m(W)<6/5.
Consequently the accumulated input-width contribution is bounded by
(1-a)^-2*d(W)<=25*d(W)/4; accumulated local error is at most
H*e*(15*d(W)+12)/(1-a)<=75H*e. These are the stated constants.

For the unrounded reduced-argument bound A<=1/2, the Taylor remainder is at
most2^(-H). Taking H=p+18 certainly makes it at most delta, so the first
accepted H is no larger. Adding the symmetric rounded remainder increases
total width by at most4(delta+e). Thus the pre-squaring width is
O(d(Z)+p*2^-p), even though H grows. The magnitude is less than3: the geometric
term sum is at most5/2, and15(p+19)2^-p+2(delta+e)<1/2 for p>=32.
The latter inequality follows at p=32 and decreases thereafter. Product width
bounds give d(X^2)<=2m(X)d(X)+8e. Bounded inputs imply a uniformly bounded
number of halvings/squarings; the magnitudes and error multipliers over that
finite number are bounded, so the final width tends to zero.

The alternating atan bracket has width at most delta, then at most delta+2e
under endpoint rounding. Exact integer Machin weights16 and4 give
20delta+40e without another rounding term. Each reduced logarithm has width
at most delta+2e; the exact integer range multiplier k gives
(1+abs(k))(delta+2e). These match the source's per-series tolerance rather
than assuming an incorrectly weighted global delta budget.

This is an informal explicit convergence proof within the previously accepted
primitive/runtime model. It adds no runtime or memory bound, proof-assistant
formalization, conductor uniformity, zero-location or GRH result. No additional
execution of unchanged sample/optimizer programs is needed for this proof-only
strengthening. All previous exact and secondary diagnostic receipts remain
bound unchanged in the new receipt.
