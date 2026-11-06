# Independent review of the incomplete cubic Gauss root moment

Reviewer: lane C. Governing source: A v3, SHA256 d857b3f0c9bd3eea83f09240737eb4faf8cc1c1064723b40273a6681b23e7c68. This is an analytic source review of an exact reduction and its failed estimate step. It does not certify a new Gauss average, a signed power saving, or a complete proof of the external sieve.

## Verdict and the bounded correction

PASS for the scope stated in v3. I read the full v2 derivation and compared the exact v2-to-v3 delta. My only finding was that the original coprime pairing must still constrain the inner c sum when the other column n is fixed. V3 now retains (c,n)=1 in (11), the outer (ab,n)=1 mask, and the original ab/k/v2 collision masks. Its illustrative hypothetical bound explicitly includes the growing other-column deletion. No formula (2)--(10), exponent, root convention, or bound was changed. V1 and v2 are preserved.

## Independent normalization checks

1. At each good prime of a squarefree modulus, the cubic character is nonprincipal, hence primitive with conductor exponent one. The finite Fourier formula for every integral frequency follows by a change of variables at unit frequencies and primitivity at nonunits. Thus g_m(z)=conj(chi_3,m(z)) G_m includes the exact zero when (m,z)>1. The cubic value at -1 is one. These statements hold for inert prime ideals and for composite ideal-squarefree moduli even when their rational norm is not squarefree.

2. The root in (3) is the root of the TOTAL type-zero character eta. It is not a root of one angular or radially twisted factor with its archimedean term suppressed. Splitting its actual conductor into the coprime S and good-q parts and applying the accepted inverse-different finite Gauss CRT gives exactly theta_S(gamma_q) theta_q(gamma_S) tau_S/sqrt(F_S). The S character need not be unit-trivial separately; the product is. This also covers the unit S conductor by its one-element convention. No extra averaging over units is justified or used. Changing a generator changes the finite factors compatibly.

3. The Gauss--Jacobi relation is used only with theta_q, theta_q^2 and theta_q^3 primitive at the exact good squarefree q. CRT for the Jacobi sum gives j(m) conj(j(n)), without an additive-generator correction. On original squarefree columns the accepted identification j(m)/sqrt(Nm)=mu(m) vartheta(m) supplies the two displayed Mobius factors. Vartheta has the stated nonzero infinity type; it is not a finite-order character and the identity is not extended to arbitrary nonsquarefree ideals.

4. With primary generators, cubic reciprocity cancels chi_3,m(alpha_n) conj(chi_3,n(alpha_m)). The normalized conjugate cubic Gauss sum is conj(G_n), because chi_3,n(-1)=1. Therefore the normalized theta_q^2 sum is G_m conj(G_n). Dividing the Gauss--Jacobi identity by this unit phase produces conj(G_m) G_n in (7). The accepted quadratic period-four evaluation applies at gamma_q with the same inverse-different pairing. There is no additional quadratic value at -1 in this calculation. For composite q this reuses the accepted Gauss evaluation, not the false identification of 1+xi_q with a composite-ring square-root count.

5. The actual row factor R_m(v2^2) contributes chi_3,m(alpha_v2), while eta(k^2) contributes chi_3,m(alpha_k) and its conjugate n factor. Their product is the frequency alpha_k alpha_v2, exactly as in (8). The primitive S scalar theta_S(alpha_k)^2 remains outside. A collision of that frequency with m or n gives the original raw zero. The separate original (k,v2)=1 condition and the cutoff Nk<=sqrt(b/Nell) remain; no relation k|w or (k,w)=1 is introduced. Primitive eta(ell e) and eta(w) values, including their S zeros, are retained, rather than divided out.

6. The ternary short-divisor expansion keeps a,b,c squarefree and pairwise coprime. Multiplication by mu(m) changes the short-divisor signs to mu(c), not to one. The conjugate cubic CRT cross in (10) is chi_3,a(alpha_b), and analogously for the other two pairs, rather than its square. Combining those crosses with the frequency factor and cubic reciprocity gives chi_3,abkv2(alpha_c) only on the already nonzero original masks. There abkv2 is indeed squarefree. V3's full other-column masks make explicit that this is an ingredient inside the original bilinear pairing, not a free column replacement.

## Check of the failed estimate step

The remaining mu(c), the growing abkv2 twist, the other-column deletion, the original class/ray data and the product profile preclude inserting an unspecified smooth-coefficient, fixed-conductor first-moment theorem. No such theorem is asserted in the note.

The illustrative exponent calculation is internally correct as a conditional diagnostic. If the explicitly hypothetical uniform unnormalized c bound were L^(5/6+epsilon), also for the fixed rescaled test x^(-1/2) W(x), then the normalization 1/sqrt(Nc) and the external 1/sqrt(Nab) give D^(1/3+epsilon) (Nab)^(-5/6). The fixed-field ideal count gives sum_(Na<=U) (Na)^(-5/6)=O(U^(1/6)); the two absolute short-divisor sums cost U^(1/3). Thus at U comparable to sqrt(D), the resulting column budget is D^(1/2+epsilon). This is neither an available theorem nor an estimate of the full coprime bilinear moment.

Expanding conj(g_m(z)) g_n(z) gives exactly the additive pairing z[y/alpha_n-x/alpha_m] in (13), with the negative sign from complex conjugation of the first exponential. The same inverse different remains. The actual finite primary k set, its Mobius and norm weights, and its capacity cutoff do not form a complete residue average modulo growing q. A bounded w window does not complete that residue ring either. The proposed free orthogonality step therefore has no justification.

## Accepted survivor and limit

The survivor is the explicit exact incomplete cubic Gauss formulation of the actual root-weighted mean, together with the precise missing uniform arithmetic input. All class/rho components, finite S factors, root phases, original A_U/common W, capacity endpoints, original coprime/optional unequal-norm support and raw zeros remain. Bounds recovered from pointwise phases or the fixed-s norm are inherited RV budgets; they are not new signed estimates.

No lower bound, impossibility theorem, actual-vector norm equivalence, automatic positivity, metaplectic input, or full-mean target follows. Even a mean-only target would leave the separate accepted 37/48 ray-count approximation budget above 3/4 in the pure critical window. Whole signed 13/12, global unsigned 9/8, determinant/zero-location and GRH status are unchanged.

## Evidence and operations

The accompanying acceptance receipt binds A's exact v3 and source-pins-v3 JSON, the preserved v2 and its literal delta, and all eight current technical input hashes. The proof review used the published local project sources for the root, Jacobi, period-four and original-mean conventions. No full third-party cache was copied. No old controls, finite tables, builds, browser sessions, installations, authentication, canonical/global metadata edits, publication actions, index changes or protected-progress mutation were performed.
