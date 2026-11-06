# A cubic bound for the actual large short-divisor contribution

Research-only CANDIDATE v2 (v1 preserved; separate primitive S factors and reversed-tail convention explicit),6 November2026; independent all-component proof review is REQUIRED. This is an attempted genuine signed estimate inside the pure leading principal moment, not a coefficient-norm shrinkage argument. Its external arithmetic input is ONLY the already pinned physical cubic residue matrix theorem (de Faveri arXiv:2610.04045v1 Theorem1.1/Example2.2), in the exact specialization stated as cbk:cubic-norm. It proves no new deep sieve theorem or whole GRH bound.

## 1. Exact quantity and proposed bound

Retain every hypothesis of PURE_TOP_GAUSS_MOMENT_REDUCTION-v1 and INCOMPLETE_CUBIC_GAUSS_ROOT_MOMENT-v3. Only original UNWEIGHTED pure two-pivot rows A2=1,v2=O, fixed unit/S-supported u0 without good support, actual annular good SF columns, fixednu/S/ray data, fixed common complex smooth W, and all source/rho/S/root/coprime masks are considered. Optional ORIGINAL unequal-norm projection is retained throughout.

Write G_D[F,G] for formula(G) of the pure reduction, with c_m=F(m)nu(m)R_m(u0)W(Nm/D), c_n=G(n)nu(n)R_n(u0)W(Nn/D). Every other factor in(G) remains EXACT. This is a bilinear notation (conjugate-linear in G), not a primitive extension at overlapping conductors. In particular G_D[A_U,A_U] is the actual retained root moment. Its actual e/w values and primitive conductor drops remain inside each finite component. Its E_T(eta) can be used by its absolutely convergent k expansion, preserving T=S union supp(mn); no free fractional completion or endpoint deletion occurs.

For any real1<=Y<=U<=sqrtD, let A_Y be the SAME exact double short-divisor definition with both norm cutoffs Y. Put
 M(W)=(2pi)^(-1) integral_R |hat W(t)|dt,
 hat W(t)=integral_0^infinity W(x)x^(-it)dx/x,
 B=||W||infinity.
For fixed smooth W supported[1,2], M(W) is finite and can be bounded by its explicit first two logarithmic-derivative seminorms. The proposed signed estimate is

 |G_D[A_U,A_U]-G_D[A_Y,A_Y]|
   <<_(S,source/ray,nu,epsilon)
       B M(W) D^epsilon [Y^(-1/2)+D^(-1/6)].             (T)

The same bound holds for the original unequal-norm restriction. It is a bound for a SIGNED Gauss-weighted large-short-divisor contribution; no inequality |A_U|<=|A_Y| or small coefficient norm is asserted. The auxiliary small-cutoff moment stays unestimated.

## 2. All-component reduction to a column sum

For a fixed actual other column n, fixed e,w,k and source pair/rho, the accepted root/Jacobi calculation gives
 epsilon(eta)=S_(m,n,rho) Gamma(alpha_m alpha_n)
       mu(m)mu(n)vartheta(m)bar(vartheta(n))bar(G_m)G_n,
 G_m=tau_m(chi_3,m)/sqrt(Nm),
 vartheta=Psi/sqrtN,
with exact primitiveS factor S and finite quadratic phase Gamma modulo4. eta(k²),eta(e),bar eta(w) retain every primitive/raw zero. This is at actual q=mn with (m,n)=1; it is never asserted for overlapping primitive conductors.

After FINITELY MANY original source/ray/mod4 character components, the dependence on m of each fixed n,e,w,k contribution has the form
   mu(m) F(m) bar(G_m) phi(m) W(Nm/D)/sqrt(Nm),           (C)
times a bounded scalar depending on n,e,w,k and fixed data.
Here phi is a multiplicative function on good ideals with |phi|<=1, apart from a fixed finite linear combination with bounded total coefficient mass. Its factors are vartheta,nu,g, the fixed-numerator residue symbols at u0,k²,e,w and gamma_S, fixed ray characters, and raw coprimality with n. All such norm bounds are uniform in n,k; the characters may have growing conductors, but no theorem for their conductors is invoked.

Why this finite separation is legitimate is a required part of the claim. On each fixed(A,B,rho), f_S and the primitive finite theta_S are fixed. theta_S(alpha_m alpha_n) factors by multiplicativity of primary generators, and theta_q(gamma_S) splits into the two genuine column factors. The primitive factors at e and w are SEPARATE: theta_S(gamma_e) times bar(theta_S(gamma_w)), or equivalently their corresponding original primitive factors with all column corrections retained. If either primitive factor is0, it kills the whole fixed component; no quotient e/w is evaluated and no such factor is ever divided out. If nonzero, its fixed scalar remains while the good-denominator fixed-numerator symbol is multiplicative in m, including its zeros. Gamma(alpha_m alpha_n) is a function on the FIXED unit group modulo4. For fixed n expand this function, and each original source-class selector on m, in the complete finite character basis; indicators themselves are not assumed multiplicative. Primary generators multiply for coprime ideals. All resulting constants are fixed independent of D,n,k,U,Y. The mask(m,n)=1 and the SEPARATE raw collision factors for m with k and with w factor into their corresponding ideal-character zeros/ordinary multiplicative deletion factors; no k/w quotient is formed. No raw prime is restored.

Thus proving a bound UNIFORM for all phi in(C) bounds the actual fixed-n column sum. This separation is not the assertion that the full signed coprime matrix is rank one or positive.

If the original unequal-norm projection is present, first apply the estimate to the coprime full annulus and subtract the forbidden equal-norm columns at that fixed n. There are O_epsilon(D^epsilon) such m (ideal representation divisor bound at a fixed rational norm), each contributing at most B D^epsilon/sqrtD, including A_U or A_Y. Their column error is O(B D^(-1/2+epsilon)), below the bounds below. This count retains all conjugate and equal-norm ideal orientations; it does not identify them or use radial Parseval.

## 3. Retain the actual short-divisor phases before a norm

For SFm the EXACT identity is
 mu(m)A_U(m)=sum_(a b c=m,Na,Nb<=U)mu(c),
with a,b,c pairwise coprime goodSF ideals. For A_U-A_Y the assignments partition DISJOINTLY into
 (i) Na>Y,Na<=U,Nb<=U;
 (ii) Na<=Y,Y<Nb<=U.
Swap labels a,b in(ii); the same estimate applies with inner b cutoffY.

For(i), put z=bc and
 T_L(z)=sum_(b|z,Nb<=L)mu(z/b),  |T_L(z)|<=tau(z).
This coefficient depends on z and L, NOT a. All original (m,n) masks become(a,n)=1,(z,n)=1 and can be put in their respective coefficients. The same is true of all fixed-numerator raw collisions. No factorization of A_U is presumed.

The exact cubic Gauss CRT identity for coprime primary a,z is
 bar(G_(az))=bar(G_a)bar(G_z)chi_3,a(alpha_z).
Consequently the actual column in(i) is
 sum_(a goodSF,Y<Na<=U) bar(G_a)phi(a)/sqrt(Na)
   sum_(z goodSF)bar(G_z)phi(z)T_U(z)/sqrt(Nz)
                        chi_3,a(alpha_z)W(NaNz/D),       (B)
with all finite character components from(C). The cubic symbol is zero at(a,z)>1, so an encompassing SF rectangle may be used with that EXACT zero. On its nonzero support m=az is SF and every original mask is correct. Off it no primitive overlapping-conductor object is invented. For(ii) the identical formula uses T_Y.

In particular there is no unsupported smooth inner Gauss-sum estimate here: the sign mu(c) remains inside T_L and the cubic CROSS interaction a,z is retained. We apply a physical cubic matrix norm to that interaction, before any triangle in a.

## 4. Apply only the pinned physical cubic matrix theorem

On a dyad Na comparable A,Nz comparable Z, the product support of W implies Z comparable D/A. The source's accepted external specialization is
 ||(chi_3,a(alpha_z))_(a,z)||op²
  <<_epsilon (AZ)^epsilon [A+Z+(AZ)^(2/3)].               (LS3)
Both variables here are ACTUAL goodSF ideals, hence cube-free, with their primary1mod3 generators. Fixed source/ray restrictions, raw deletions and fixed-numerator twists are coefficient masks/phases, not arbitrary conductor labels. The theorem's complete encompassing SF/cube-free matrix is restricted only inside its positive norm.

Mellin inversion separates the actual common W:
 W(NaNz/D)=(2pi)^(-1)integral hatW(t)D^(-it)
                                          (Na)^(it)(Nz)^(it)dt.
The two coefficient L² norms in(B) are O_epsilon(D^epsilon), since
 sum_(Na comparable A)1/Na<<1,
 sum_(Nz comparable Z)|T_L(z)|²/Nz<<_epsilon D^epsilon.
All phi/G phases have modulus<=1, uniformly in the other column and k. Thus the signed dyadic column sum is bounded by
 M(W) D^epsilon sqrt[A+D/A+D^(2/3)].
This is a proved conditional application of the explicit external theorem(LS3), not a new proof of it or an assumption of arithmetic positivity.

Sum the O(log²(2D)) relevant dyads, with Y/2<=A<=U<=sqrtD. For every epsilon>0 distribute its loss among the ideal divisor bound, LS3 and dyadic count. The ACTUAL column tail obeys
 |sum_(m)mu(m)(A_U-A_Y)(m)bar(G_m)phi(m)W(Nm/D)/sqrtNm|
   <<_epsilon M(W)D^epsilon
                        [D^(1/3)+sqrt(D/Y)].             (COL)
The equal-norm removal error described above is smaller. This uses NO hypothetical alpha=5/6 or uniform growing-conductor Gauss first moment. It differs from the failed absolute-short-divisor method precisely by retaining chi_3,a(alpha_z) through(LS3).

## 5. Reassemble the original signed leading moment

For fixed n the estimate(COL) is uniform, including its actual coprimality and S/ray/raw data. The untouched other column has
 sum_(n annular goodSF)|A_T(n)W(Nn/D)|/sqrt(Nn)
          << B D^(1/2+epsilon), T in{U,Y}.
Only NOW take the other-column triangle. All source/rho/S/mod4 coefficient masses are fixed, w<64 and e|P_S are fixed finite, |g0| is uniformly bounded. The actual k coefficients, if E_T is opened, have absolute sum<=zeta_K(2), uniformly in their induced eta² and FULL deletion set. k twists only change the bounded coefficient phases phi, so no conductor-dependent norm constant or k^epsilon is needed. One could retain original finiteK instead; the same estimate is uniform and its old tail remains accounted for in the separate pure reduction.

The1/D in formula(G) is essential. Combining(COL) and the n count gives
 |G_D[A_U-A_Y,A_T]|
  << B M(W)D^epsilon [D^(-1/6)+Y^(-1/2)].
For a tail on the n side, conjugate the fixed-other-column scalar and reverse the two roles before the same column estimate. This changes G_n to bar(G_n), W to bar(W), and conjugates its bounded finite S/source coefficients; M(bar(W))=M(W), and the conjugate cubic matrix has the same operator norm. No assumption that a single source block is Hermitian is required. All fixed other-column phase factors stay bounded with the corresponding complete finite character expansion.
Bilinearity gives exactly
 G_D[A_U,A_U]-G_D[A_Y,A_Y]
  =G_D[A_U-A_Y,A_U]+G_D[A_Y,A_U-A_Y],
which proves(T), subject to independent verification of the all-component separation(C).

This is an ACTUAL signed tail comparison, not a claim that a Gauss average for arbitrary A_U follows from a smooth unweighted theorem. It does not replace the coefficient in the original primal/kernel definition. It bounds the entire explicitly defined difference using its exact short-divisor expansion and cubic cross phases.

## 6. Meaning at the declared pure window and remaining task

For U comparable sqrtD, X=D^(3/8), H comparable A1=D^(3/4), choose Y=D^(1/8) (or the smaller original U, in which case the tail is0). Then(T) is O(B M(W)D^(-1/16+epsilon)). Multiplying by A1X^(1/6) makes the signed LARGE-short-divisor contribution to the retained principal mean target-sized. The previously reviewed Bessel/Euler reduction errors are also target-small. The auxiliary small-short-divisor G_D[A_Y,A_Y] remains UNBOUNDED at the required size.

No coefficient-only norm bound has improved: original |A_U| can remain odd/nonzero and large, and all actual A_U entries persist in the exact difference. Y is not a new data cutoff in the primal family, a virtual column gcd, the good sixth-part s, the sixth-free indicator divisor, or original k. The comparison is scoped to the Gauss-weighted pure leading principal moment. It is distinct from the older identity-source virtual-gcd cubic comparator (cbk:cubic), which used different variables and did not estimate this actual short-divisor contribution.

The original P_top-M_top separate upper certificate at this window is still37/48>3/4. Neither(T) nor a future target estimate of the small-short moment alone removes that discrepancy or the other original sectors. Whole signed13/12/global unsigned9/8, short/principal/full assembly, independent arithmetic determinant/zero-location, analytic/categoryLean and all intended GRH scopes remain open. No actualM/energy lower bound, new primitive conductor identity or new data result follows from this comparison.

Independent all-component phase derivation to be read with this candidate: planning/root-moment-20261106/lane-a/ALL_COMPONENT_COLUMN_PHASES-v1.md SHA011b68a07eda5489b6ea8d8b7fa565e52920423f0c954ef583ea143b64609df8. It makes the source/ray/mod4 Fourier coefficient mass and the separate primitive e/w factors explicit. Its own independent gate is required, not inferred from authorship.
