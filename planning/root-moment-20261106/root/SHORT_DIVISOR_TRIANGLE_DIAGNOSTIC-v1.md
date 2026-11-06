# Why absolute short-divisor opening loses a proposed column Gauss gain

Research-only method diagnostic v1, 6 November2026. This note records an attempted analytic use of column Gauss cancellation and its exact failed step. It does NOT assert a new cubic-Gauss first-moment theorem, an actual-family lower bound, or a bound on the principal mean. The uniform input below is deliberately HYPOTHETICAL, including its growing conductor and all raw masks. It cannot be silently imported from a fixed smooth-coefficient theorem.

## 1. Start with the actual coefficient, not arbitrary learned weights

Retain the actual annular good SF ideal columns, A_U, fixed complex common W, and all source/ray/root/gauge conditions of cbk:coefficients. In the pure principal-root attempt let f_m denote any one ACTUAL column phase obtained after legitimate root/gauge transport. This may contain the original fixed nu,u0 phase, a primitive cubic Gauss factor, ray character, fixed S factor and fixed dual-twist values, including collision zeros. Its exact definition must be proved from the actual kernel before invoking any estimate for it. We do not assert that the full coprime two-column form factors into this one-column expression.

The scalar column subproblem is
 C_D(f)=sum_(m goodSF,D<=Nm<=2D) A_U(m) f_m W(Nm/D)/sqrt(Nm).
No coefficient replacement is made here. The exact finite identity gives
 C_D(f)=sum_(r,s goodSF,(r,s)=1,Nr,Ns<=U)mu(r)mu(s)
   sum_(t goodSF,(t,rs)=1,D<=NrNsNt<=2D)
                 f_(rst) W(NrNsNt/D)/sqrt(NrNsNt).        (1)
r,s,t are pairwise coprime in(1), and all original column phases and zeros remain in f_(rst). This is an opening of A_U only, not an extra assumption that f is multiplicative or that Gauss sums are arbitrary reciprocal labels.

Since U^2<=D, L=D/(NrNs)>=1. Thus no fictitious small-length decay or automatic zero at L<1 is used.

## 2. Give the proposed method an explicitly stronger hypothetical input

Fix0<=alpha<1. Suppose, solely to test this route, that for EVERY actual r,s and EVERY inner phase/mask arising in(1), every partial interval inside[L,2L] satisfies
 |sum_(t in that interval,goodSF,(t,rs)=1) f_(rst)|
       <=C_alpha (D NrNs)^eps L^alpha.                   (H_alpha)
Uniformity in the growing rs-dependent conductor, all primitive/S/ray/source/root twists and the full common-prime mask is part of this assumption. No such input is proved or claimed available here. Even identifying the correct metaplectic twisted family does not prove(H_alpha).

Partial summation with the ACTUAL common W gives
 |inner(r,s)| <=C_alpha M1(W) D^(-1/2) (D NrNs)^eps
                                      (D/(NrNs))^alpha,  (2)
where one may take M1(W)=||W||infinity+integral_1^2|W'(x)|dx.
The extra derivative of x^(-1/2) costs only another fixed multiple of ||W||infinity on[1,2]. This uniform partial-interval hypothesis is essential; an estimate of the final unweighted sum alone is insufficient for arbitrary fixed smooth W.

Now take the ABSOLUTE TRIANGLE in r,s. The elementary ideal count implies
 sum_(Na<=U)(Na)^(-alpha) <<_(alpha,K) U^(1-alpha)
for0<=alpha<1. Consequently
 |C_D(f)| <<_(alpha,fixed data,eps)
  M1(W) D^(alpha-1/2+eps) U^(2(1-alpha)).                 (3)
The original r/s coprimality can be overcounted only after this absolute step. All source masks in(1) were retained until the bound; none is silently filled back into a signed identity.

## 3. The exact failed step in the high window

The actual high window includes U^2 comparable to D (in particular2D/7<=U^2<=D). Write U=c sqrt(D), c bounded above and below. The power of D in(3) is
 alpha-1/2+(1-alpha)=1/2
for EVERY0<=alpha<1. Thus even the extraordinarily strong alpha=0 version of(H_alpha) would give only D^(1/2+eps) after this triangle. The near-boundary r,s norms comparable to U leave actual t lengths comparable to1; individual smooth t estimates cannot supply the missing cancellation among these many signed r,s terms.

For U=D^u the displayed upper certificate has exponent
 p(alpha,u)=alpha-1/2+2u(1-alpha).
For example alpha5/6 is an ILLUSTRATIVE HYPOTHETICAL exponent, not an asserted theorem for this shifted family; it gives p=1/3+u/3. At u1/2 its certificate is again1/2. No numerical family or asymptotic fit is used to state this algebra.

The endpoint alpha=1 instead costs D^(1/2+eps)(1+log U)^2 and supplies no gain. We do not extrapolate the alpha-dependent constant through1.

This is a failure of the proposed proof strategy after giving it a generous hypothetical smooth-input bound, not a lower bound on C_D(f) and not an impossibility theorem for its actual arithmetic cancellation. Formula(3) may be far from sharp because the outer mu(r)mu(s) signs were discarded. A bilinear/trilinear estimate retaining these actual signs, residual overlaps, growing twists and common-prime masks BEFORE that triangle could do better; it is not supplied here.

## 4. Connection and limits

The pure top-band reduction leaves the exact signed Gauss-column moment G_D in PURE_TOP_GAUSS_MOMENT_REDUCTION-v1. At the declared critical X=D^(3/8) it asks for a D^(-1/16) improvement of that actual normalized principal moment. Replacing A_U by a smooth or bounded arbitrary coefficient and invoking an unweighted Gauss average is invalid. Equation(3) shows why merely opening both short divisors and applying smooth inner estimates separately does not repair this.

The coprime h1 two-column slice remains indefinite; it is NOT simply |C_D(f)|^2. In the auxiliary unrestricted rank-one case only, a D^(-1/16) normalized square/D improvement would correspond to column exponent<=15/32. The triangle certificate1/2 fails even that simpler sufficient test. Neither the auxiliary test nor a one-column target is asserted necessary for the actual G_D or the final signed assembly.

No external Gauss-average theorem has been invoked, no zero-free strip or GRH/Artin holomorphy has been assumed, and no new signed exponent is proved. The actual two-column root/cubic-k moment (and its joint discrete-s discrepancy), with fixedW and original A_U, remains open. Do not repackage this failed scalar route as a new determinant/zero-location bridge or an actual-energy obstruction.
