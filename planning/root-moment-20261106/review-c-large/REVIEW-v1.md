# Independent adversarial review: actual large short-divisor cubic tail

Reviewer: lane C. Governing sources are root LARGE_SHORT_DIVISOR_CUBIC_BOUND-v2.md, SHA256 ed8b92c48812ada0dfe92c2bd7e314d8f4432b1952011da72236d4959f14aef7, and A ALL_COMPONENT_COLUMN_PHASES-v1.md, SHA256 011b68a07eda5489b6ea8d8b7fa565e52920423f0c954ef583ea143b64609df8. Both were read in full. I also read the preserved root v1 and its exact v1-to-v2 delta, the accepted incomplete-Gauss v3, the actual pure G_D definition, and the accepted physical cubic input in cbk:cubic-norm.

## Verdict and exact scope

PASS for the stated pure leading principal-moment cutoff comparison, conditional on the already accepted external physical cubic sieve theorem. In particular, for the SAME original G_D and 1<=Y<=U<=sqrt(D),

 |G_D[A_U,A_U]-G_D[A_Y,A_Y]|
   << B M(W) D^epsilon (Y^(-1/2)+D^(-1/6)).

This is a scoped signed Gauss-weighted tail estimate. It is not a smaller norm for A_U, a theorem for arbitrary primitive conductor labels, a new deep sieve, a full h1 estimate or a whole-kernel improvement. The pure unweighted A2=1 hypotheses, fixed S/ray/nu/u0, complete original good-SF annulus, common fixed complex W and all other original kernel factors are indispensable here. The optional original unequal-norm projection is covered by a separate fibre count, not by pretending that indicator is multiplicative.

## 1. Actual all-component coefficient package

I checked the good-q/S separation against accepted incomplete-Gauss v3 and the canonical root conventions. At fixed source pair A,B,rho and fixed other column n, the TOTAL type-zero eta root has its primitive finite S factor, the period-four Gamma(alpha_m alpha_n), and the exact mu(m)mu(n) vartheta(m)conj(vartheta(n)) conj(G_m)G_n factors. No angular or radial normalization of a constituent is discarded.

The m-dependent part of theta_S(alpha_m alpha_n) is multiplicative through the canonical primary section. The q-character value at gamma_S and the original fixed numerator values at u0,k,e,w are multiplicative in the denominator m, including raw zeros. The good density g and nu are bounded multiplicative factors. The original (m,n)=1 mask is multiplicative and splits as the two masks (a,n)=1 and (z,n)=1 on m=az. The q masks from k and w similarly remain separate raw zero factors. No k/w or e/w quotient, k|w, or artificial (k,w)=1 condition is formed.

Root v2 correctly keeps theta_S(gamma_e) and conj(theta_S(gamma_w)) SEPARATELY. A zero of either primitive S factor kills the component and is not divided out. The finite S conductor/drop is fixed on the selected source/rho component. Chosen integral generators of S-supported e,w need not be primary; total type-zero unit-triviality gives the actual combined value.

The source class selector and Gamma need not be multiplicative as written. Their finite Fourier expansions repair this exactly: the class-indicator coefficient l1 mass is one, and the Gamma expansion on the fixed group (O/4)^times has l1 mass at most sqrt(12), by normalized Parseval and Cauchy. For fixed n, multiplication by alpha_n permutes that finite group. Therefore the expansion costs a fixed mass uniformly in n and k. Off-class formulas are auxiliary coefficient extensions only; summing the indicator expansion restores the actual class. No primitive character/root is asserted off its original source component.

After this expansion, the relevant column fits the theorem for ANY bounded multiplicative lambda. The potentially growing twists and n-dependent masks are in arbitrary coefficient vectors of the SAME physical cubic matrix; no growing-conductor theorem is being assumed. This is the essential all-class check, rather than an inference from a same-class/rho=1 formula.

## 2. Exact signed tail grouping

On original squarefree m, the accepted ternary identity is

 mu(m) A_T(m) = sum_(abc=m,Na,Nb<=T) mu(c),

with all three ideals squarefree, good and pairwise coprime. The difference of the two square cutoff boxes is exactly the DISJOINT union
 Y<Na<=U, Nb<=U
and
 Na<=Y, Y<Nb<=U.
Swapping a and b in the second term leaves its sign and Gauss factors unchanged. With z=bc, its two coefficients are respectively T_U(z) and T_Y(z), where
 T_L(z)=sum_(b|z,Nb<=L) mu(z/b).
They are independent of a. Thus A's single grouped expression contains T_U+T_Y; the root proof's two separate sums are equivalent and do not omit the second box.

The exact conjugate Gauss CRT formula for coprime primary a,z is
 conj(G_az)=conj(G_a)conj(G_z) chi_3,a(alpha_z).
This follows from the two cubic cross factors and primary reciprocity; the conjugate cross is chi_3, not its square. Multiplicativity of lambda then gives the claimed a-by-z matrix. On an encompassing SF rectangle a shared prime makes that cubic entry ZERO. Consequently the encompassing rectangle encodes, rather than relaxes, the requirement that original m=az be SF. All n/k/w deletions split in the lambda diagonals. The objects at overlap are raw matrix zeros, not primitive roots of overlapping conductors.

The coefficient estimate |T_U+T_Y|<=2 tau(z) suffices. It bounds a genuinely derived z coefficient; it does not posit multiplicativity or pointwise shrinkage of A_U. The residual mu(c) is retained in the exact identity before the norm estimate. The final bound does not separately claim cancellation of that Mobius sign.

## 3. Physical cubic norm and the actual profile

For Na on a dyad A and Nz on a relevant dyad Z, the original W support permits Z comparable to D/A. Both indices are actual good SF ideals and hence cube-free. The matrix chi_3,a(alpha_z), or its transpose/conjugate, is the primary physical cubic family already covered by the pinned external Theorem 1.1/Example 2.2 and cbk:cubic-norm. Its squared norm is bounded by (AZ)^epsilon [A+Z+(AZ)^(2/3)]. This is an external arithmetic input, not a proof of that preprint theorem here.

The coefficient l2 norms are bounded by D^epsilon: ideal counting gives sum_(a~A)1/Na=O(1), and the divisor bound gives sum_(z~Z)|T_U+T_Y|^2/Nz<<D^epsilon. Arbitrary bounded lambda and unit Gauss phases, including all growing raw deletions, are allowed by this arbitrary-coefficient norm. No factor depending on Nk or the conductor of lambda enters.

For the Fourier convention in root v2, the Mellin inversion is exactly
 W(Na Nz/D)=(2pi)^(-1) integral hatW(t) D^(-it) (Na)^it (Nz)^it dt.
The three powers are unitary on the integration line. Hence this LINEAR column sum costs M(W) once, not M(W)^2, and no derivative of the sharp capacity G enters. Smooth compact support of the actual common W gives finite M(W); its logarithmic derivative seminorms can bound it. The bound is not supnorm-uniform in a varying W.

Bilinear matrix Cauchy, which requires no PSD claim, now bounds each dyad by
 M(W) D^epsilon sqrt(A+D/A+D^(2/3)).
Summing the finitely many relevant dyads, with A>=Y/2 and A<=U<=sqrt(D), gives
 M(W) D^epsilon [sqrt(U)+sqrt(D/Y)+D^(1/3)].
The sqrt(U) term is absorbed by D^(1/3). Real cutoffs, partial dyads and ties are exact coefficient indicators. If Y=U the tail is empty; the bound still holds. This proves the stated uniform linear column-tail lemma for arbitrary bounded multiplicative lambda.

## 4. Original pair support, reassembly and normalization

A literal unequal-norm exclusion is not multiplicative in m. For fixed rational norm Nn, the ideal count is at most the integer divisor function: split prime exponents give at most exponent+1 choices, inert exponents at most one and ramified exponents one. Thus there are O_epsilon(D^epsilon) ideals of that norm, with all conjugate orientations distinct. The original coprime restriction can only reduce this count. The original short-divisor coefficients satisfy |A_U|+|A_Y|<<D^epsilon. Subtracting that fibre costs O(B D^(-1/2+epsilon)) in the column sum. It is harmless after the same other-column triangle and is smaller than the displayed bound. No radial Parseval or artificial class identification is used.

For the untouched column, the actual complete-annulus count gives
 sum_n |A_T(n) W(Nn/D)|/sqrt(Nn) << B D^(1/2+epsilon),
uniformly for T=U,Y. Only at this point is its triangle taken. The exact G_D definition has the once-only 1/D and the two 1/sqrt(Nm),1/sqrt(Nn) weights already used above. Its g0, kappa_S, fixed class/rho and S factors, w<64 and e|P_S have fixed total mass. Opening E_T(eta) at exponent 2 is legitimate: its k series is absolutely convergent, the column lemma is uniform in the k-induced bounded coefficient, and sum_k (Nk)^(-2) is finite. The full T=S union supp(mn) deletion remains through the raw factors. No Nk^epsilon has been introduced and no exponent-5/3 or endpoint completion is being used.

This yields
 |G_D[A_U-A_Y,A_T]|
 << B M(W) D^epsilon [D^(-1/6)+Y^(-1/2)].
For the n-side tail, complex-conjugating the scalar expression changes G_n into conj(G_n), W into conj(W), and all finite coefficients into their conjugates. The conjugate cubic matrix has the same norm, and M(conj(W))=M(W). This proves the reversed estimate without assuming a source block is Hermitian.

Finally, conjugate bilinearity gives EXACTLY
 G_D[A_U,A_U]-G_D[A_Y,A_Y]
 =G_D[A_U-A_Y,A_U]+G_D[A_Y,A_U-A_Y].
The two estimates prove the proposed comparison with every original mask still present.

## 5. Scope, novelty and unresolved arithmetic

This is a genuine scoped bound for the actual signed large-short-divisor contribution to the stated Gauss-weighted leading moment. It retains the cubic cross interaction through the physical sieve before the distinguished short-divisor triangle. It is not the old identity-source virtual-column-gcd comparator: these a,z are the exact ternary short-divisor grouping inside an original column, and original coprime m,n remain throughout. It is nevertheless an application of an accepted external norm theorem, not a new sieve or a Mobius-sign theorem.

At U comparable to sqrt(D), X=D^(3/8) and Y=D^(1/8), the moment difference is O(B M(W) D^(-1/16+epsilon)). Multiplication by the ORIGINAL A1 X^(1/6), with A1 comparable to D^(3/4), makes this tail target-sized. If U<Y, choosing Y=U makes the tail identically zero and says nothing new about the remaining moment.

The auxiliary small-cutoff moment G_D[A_Y,A_Y] is still unestimated. Its constant short-divisor term has not been removed. The separate accepted P_top-M_top certificate still has power 37/48>3/4; it is an upper certificate, not an actual lower bound. There is no new full band/prefix or whole signed 13/12/global unsigned 9/8 improvement, no necessary actual-vector norm condition, and no GRH/determinant/zero-location/Lean conclusion. The prior inherited UB01 actual fixed-s band bound is not superseded by a whole-family claim here.

No old controls, finite tables, arithmetic runs, builds, browsers, dependency or authentication actions were used in this review. Only exact source reads, source hash binding and newly owned review records were performed. All old versions and frozen release/canonical/index data remain untouched.
