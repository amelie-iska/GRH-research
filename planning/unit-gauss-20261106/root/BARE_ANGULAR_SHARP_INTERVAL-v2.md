# Sharp inner intervals in the source bare-angular TypeI family

Research-only external-input corollary v2,6 November2026. This concerns the BARE angular coefficient in a pinned primary preprint. It does NOT yet concern the full actual inverse-different/fixed-finite-twist/deletion kernel. The distinction is a hypothesis of the result, not a missing proof step silently assumed away.

Acceptance: derive the exact sharp-interval estimate from the cited low/high-height inputs, keep norm ties and row-dependent endpoints, identify each normalization and remaining source-to-actual obstruction, independently review the argument and pin the source version. No GRH, desired positivity, contour-through-zeros or new sieve premise is used. No original book/public/Lean claim is changed.

## 1. Primary inputs and object

Use An unconditional first moment for cubic Gauss sums, September25,2026, pinned openai/math commit4eaee87548250b2682affda7d05d947c05554bae, AppendixA PropositionA.4 (A.8),(A.9), including the nonzero-angular model estimate(A.11). This is a public repository preprint used as an EXTERNAL input; no independent full reproof or Lean verification of it is claimed. The companion public metadata contains the immutable URL/hash; full paper caches stay excluded from publication.

Let G_src(c)=Nc^(-1/2) sum_(x mod alpha_c) chi_(3,c)(x) exp(2pi i Tr(x/alpha_c)), with the primary1mod3 convention and the source's squarefree-zero convention. Set theta_l(c)=(alpha_c/|alpha_c|)^l and G_l(c)=theta_l(c)G_src(c), for a FIXED nonzero integer l. Every ideal and norm-fibre multiplicity here is precisely the source family; no extra deletion at2, fixed finite Hecke character, source/ray selector or ramified additive twist is inserted.

Take X large, R*U comparable toX, 1<=R<=C X^(1/2), r in a physical dyad of norm comparable toR. Let a_r be arbitrary divisor-bounded coefficients, uniformly |a_r|<<epsilon X^epsilon. Let w_r be smooth weights on one fixed compact subinterval of(0,infinity), with each fixed derivative bounded independently ofX,r; dependence on one fixed complex profile and its finitely many seminorms is allowed. For EACH r choose an arbitrary interval I_r of integer norm values inside that support. These intervals may differ and may be empty. Define the unnormalized sum

 S_I(X,R)=sum_r a_r sum_(u good in the SOURCE sense)
             G_l(r*u) w_r(Nu/U) 1_(Nu in I_r).           (1)

All source squarefree and raw collision zeros remain in G_l(r*u). The theorem is

 |S_I(X,R)| <<_(l,epsilon,profile,C) X^(11/12+epsilon).    (2)

This is a genuine resolution of sharp r-dependent radial intervals for THIS bare source object. It is not an arbitrary coefficient theorem in u or a theorem for the actual finite psi(v) factor.

For original annular normalization, multiplying byX^(-1/2) gives X^(5/12+epsilon). In the previously stated pure critical bookkeeping A1V=D^(13/16), one such matched column against the other elementary sqrt(D) column would have power35/48, below3/4 by1/48. This last sentence is ONLY a scale implication for a hypothetical exact match; no actual model piece is asserted covered without all other phase/mask interfaces.

## 2. Exact integer endpoints and truncated Perron

Replace every real endpoint by the half-integer threshold selecting exactly the same integers. For example Nu<=B becomes Nu<floor(B)+1/2, and Nu<B uses ceil(B)-1+1/2. Open lower endpoints use the complementary prefix. Thus no ideal norm equals a threshold and no half-weight at a norm tie occurs. Empty intervals contributezero.

Write each nonempty interval as a difference of at most two prefixes, with thresholds y_r comparable toU; intervals meeting the fixed support can be clipped there before this step. Treat one prefix. Put sigma=1/log(2X) and H=X^(1/12). The classical finite Perron kernel is

 P_H(z)=(1/(2pi)) int_(-H)^H z^(sigma+it)/(sigma+it) dt.

For z!=1, direct integration of the Mellin step identity gives
|1_(z>1)-P_H(z)| << z^sigma min(1,1/(H*|log z|)).
Here z=y_r/Nu stays in a fixed compact positive range, so z^sigma is uniformly bounded. Endpoint phases y_r^(it) have absolutevalue1 and are allowed to depend onr. The small positive sigma produces bounded smooth x^(-sigma) factors and bounded coefficients y_r^sigma U^(-sigma). This has no D-power cost.

The absolute size of G_l is at most1. In the fixed quadratic ideal family the number of ideals of any integer norm n is divisor-bounded: at split/inert/ramified rational primes the elementary Euler coefficients are at most d(n), so at n<<X it isOepsilon(X^epsilon). This does NOT identify equal-norm ideals or assume radial orthogonality.

For one r the absolute Perron error is therefore
<<epsilon X^epsilon [1+ U/H*log(2U)].
To see it, order integer n by distance from the half-integer y_r; log(y_r/n) is comparable to(n-y_r)/U on this fixed support, and sum min(1,U/(H*|n-y_r|)) by integer shells. The closest shell costsO(1+U/H), the rest costsO(U/H log(2U)); every ideal in a norm fibre is counted. There areO(R) r ideals and coefficients are divisor-bounded. Total truncation error is

 <<epsilon X^epsilon (R+X/H).                            (3)

No analytic cancellation is used for this endpoint error.

## 3. Bounded heights

Inside the Perron integral, apply(A.8) at every |t|<=2 after putting y_r^(it), the bounded sigma factor and any fixed Nr-scale factor into a_r(t). Its absolute coefficient bound remains uniform. The weights x^(-sigma-it)w_r(x) have uniformly bounded fixed derivatives for these bounded t and retain a common compact support. The source-level range R<=CX^(1/2) lies inside R<<X^.51 for sufficiently largeX; boundedX is absorbed in constants.

The source D_l is G_l minus its explicit angular model. The(A.11) elementary angular discrepancy quoted in the proof ofA.4 bounds that model at most X^(1/3+epsilon)R^(1/2), hence at most X^(7/12+epsilon) here. The(A.8) difference costs X^(5/6-1/100), uniformly over these coefficients and weights. The finite |sigma+it|^(-1) integral adds only O(log(2X)); nearzero it is not bounded by1/|t| without sigma. These terms are below X^(11/12+epsilon).

This uses the nonzero angular mode l. It does not apply the disappearance of a bare theta residue to a different finite character transform.

## 4. Higher heights and row-dependent endpoint phases

Split2<=|t|<=H into dyadic blocks of sizeT. On each block |sigma+it|^(-1)<<1/T. The endpoint phase y_r^(it) can be placed outside the u sum and removed AFTER taking absolutevalues in the outer r sum. Therefore(A.9), whose left side is ALREADY an integral of the absolute inner sum weighted by |a_r|, applies exactly:

 int_(|t|~T) sum_r |a_r| |sum_u G_l(ru)(Nu)^(it)
                                            W_r(Nu/U)| dt/T
 << X^(1/2+epsilon) R^(3/4) T^(1/2).                    (4)

The sign of t and conjugation of the fixed profile do not affect this bound. The bounded sigma factor is included in W_r with uniformly bounded derivatives. Its fixed-derivative hypothesis, rather than a log-smooth assertion at polynomial height, is the one used. Since l!=0, the source's explicit residue term is absent. H=X^(1/12) is inside the stated range T<<X^(1/6+rho) of(A.9).

Crucially, the theorem integrates the modulus in t. We do NOT take an interval Schur mask to have operatornorm1, nor apply(A.8) to x^(it)w_r at polynomial t. No derivative cost is hidden in either step.

Summing the dyadic T gives

 << X^(1/2+epsilon)R^(3/4)H^(1/2).                       (5)

For R<=CX^(1/2), H=X^(1/12), this is X^(11/12+epsilon). The error X/H is the same power, and R<=X^(1/2). Combining(3)-(5) and bounded heights proves(2). The height exponent1/12 balances7/8+h/2 and1-h at h=1/12; no conjectural short-interval cancellation occurs.

## 5. Why this is still NOT the actual TypeI theorem

The actual normalized Gauss sum in the accepted book uses exp(2pi i Tr(x/(delta*alpha_c))), delta=1+2omega. Primitive change of variable x=delta*y on good c gives EXACTLY

 G_actual(c)=chi_(3,c)(delta) G_src(c),
 barG_actual(c)=bar(chi_(3,c)(delta)) barG_src(c).          (6)

The fixed S-supported numerator factor in(6) is not identically1. It is not a good squarefree level r, and it is retained in the actual fixed finite psi. The actual vartheta gauge additionally has its prescribed generator-unit correction; original nu, source/Gamma/mod4/rho and e/w primitive S factors produce fixed finite characters, with rawzeros. Formula(2) has not been proved for all those factors. A finite Fourier expansion or fixed conductor does not by itself permit inserting an arbitrary u-dependent character into(A.8),(A.9).

The full actual deletion Q also remains separate. Opening it changes levelt to d*t while keeping product(T/Nd)N(dt)=D*Nk. At the worst originalunit level Nt~D^(1/2), the stated R<<X^.51 leaves only Nd<<D^.01. At Nk=D^kappa the allowable exponent for that divisor is .01-.49*kappa. This is negative at kappa=1/32; a divisor-epsilon bound cannot cure the violation of a theorem's level hypothesis. Even before opening Q, the extreme short-k level ratio(.5+kappa)/(1+kappa) exceeds.51 when kappa>1/49.

The sharp inner interval obstruction is now resolved for the complete source bare-angular family. The actual finite-twist/ramified normalization and coupled deletion/short-k range are still open interfaces. This is not a proof that they are impossible to resolve, nor that a scalar input is necessary for the full signed assembly.

No original finiteK, common complexW, class/rho/source/primitiveS zero, fullunion/commonprime mask, ray/SF/capacity distinction or orientation mean has been dropped in an ACTUAL claimed estimate: we have explicitly restricted(1) to its source object. Whole signed13/12/global unsigned9/8 and determinant/zero-location/actual Lean/GRH obligations remain unchanged. No source/book/PDF/UI/release/index/auth/dependency/toolchain change follows from this research-only note.

