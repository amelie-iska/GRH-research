# Independent review: honest BV--Mellin finite dual bands and prefixes

Verdict: PASS for the exact same-source-class/rho=1, original unweighted two-pivot theorem in planning/intermediate-kernel-20261106/lane-a/HONEST_BV_MELLIN_INTERMEDIATE-v1.md (SHA256 985295ddbdb03b721a68ce7a1397ca5c80b75c93df26edfc874f028be0b2cb8f). This is a new independent analytic proof read, not an execution or reuse of author controls. The actual all-component root normalization is a separate C result and is NOT needed or silently inserted here.

## 1. BV profile and gamma-factor integrability

The actual capacity interpolant G is smooth, compactly supported in[1/2,5/2], bounded by1, and TV(G)<=2. Its growing higher derivatives are irrelevant to this argument. Ordinary Mellin integration by parts gives the exact sign and denominator

 Ghat(1-s)=-(1-s)^(-1) integral y^(1-s)dG(y).

There is no boundary term. Since sigma<1 and y<=5/2, its absolute value is at most 2(5/2)^(1-sigma)/|1-s|. The complex column W is not being declared BV with this seminorm; it remains the original coefficient, and G is the separate row-capacity profile.

For s=sigma+it, the numerator and denominator in Gamma(s)/Gamma(1-s) have the same exponential Stirling factor. Their absolute-power ratio is |t|^(2sigma-1)(1+O_sigma(1/|t|)). Division by |1-s| therefore leaves O_sigma(|t|^(2sigma-2)), integrable at infinity precisely in the stated range sigma<1/2. On bounded t the line 0<sigma<1/2 avoids the gamma poles and |1-s| is bounded away from zero. The positive field factor C0^(sigma-1/2) is constant. Thus the product Ghat(1-s)gamma_K(s), not Ghat alone, has the claimed uniform vertical L1 bound, independent of A1 and all capacity endpoints.

The argument does not place the contour at sigma=0. At that endpoint Gamma(s) has a pole; the proof may not erase a mean/residue by taking that contour. Every positive sigma is fixed before the physical parameters, and constants may depend on it. Nor does the theorem assert uniformity as sigma tends to1/2, where both this vertical integral and the k majorant become critical. For each finite set of original parameters G is smooth, so the exact source transform can be represented on any such strictly positive line without crossing a pole. The uniform BV bound is then applied to that exact finite expression.

## 2. Exact amplitude, coefficient pairing and raw zeros

In the primitive formula, F=NmNn and the prefactor is L_e/sqrt(F). Mellin separation gives

 L_e^(1-s)(Ny)^(-s)(NmNn)^(s-1/2).

Consequently the second coefficient vector in the linear-first form is b(conjugate(s)), followed by complex conjugation. It is not b(s), and the form is not a PSD norm square for nonreal s. The two correct vectors nevertheless have identical pointwise magnitudes. On the ORIGINAL annulus Nm in[D,2D],

 |(Nm)^(s-1/2)|^2=(Nm)^(2sigma-1),
 sum_{a:da original}|b_da(s)|^2
    <<_epsilon B_W^2 D^(2sigma+epsilon)/Nd,

with the same bound at conjugate(s). This comes from the original coefficient AU(da), bounded by 3^omega(da), and O(D/Nd) residual columns. No cutoff rescaling to AU(a), multiplicativity of beta, or multiplicativity of primitive xi at S is used.

The e,h values of xi_da are fixed primitive column phases, legitimate because their conductor is good and disjoint from S. They do not restore forbidden original raw values. The literal raw factors at k,ell,v2 retain every collision zero. Original common W, nu, u0, class/ray and capacity restrictions remain. The finite scalar h0 and all mu signs occur once outside, rather than being squared into the two columns.

Mellin factorization here is exact with the ORIGINAL finite K_ell; it is not a completed-Euler approximation. For a fixed finite dual band, m,n,h,z,k,ell,e,v2 are all finite sums. The uniform integrable vertical majorant just established justifies the finite exchanges. It makes no assertion about an infinite full-dual Dirichlet interchange.

## 3. The joint positive comparison and the divisor budget

The original (m,n)=1 support is imposed first. Off that support the individual-column product used for ideal Mobius inversion is an auxiliary extension, not the physical primitive root/conductor at shared-prime pairs. Full divisors including d=m are retained so that self-pairs and all overlaps cancel exactly.

For m=da,n=db, the source raw multiplicativity on GOOD z gives the common chi_d factor, with its raw mask (d,z)=1. The residual class is C[d]^(-1), so any source psi row factor is common and unitary and cancels before using the raw R_a norm. Primitive xi_a is not being asserted sixth-order. AU(da), beta_da, the e/h phases and every original coefficient mask remain unfactored in the coefficient subsequence. Residual a,b may overlap each other; no unwanted residual coprime restriction is inserted.

For fixed h and d, the actual band has Y<NhNz<=2Y. After extracting the complex phase, its magnitude is at most Y^(-sigma). Bilinear row Cauchy then bounds it by that factor times the geometric mean of TWO positive prefix norms. Only in those norms are the window and (d,z) mask enlarged. The prefix is Z_h=2Y/Nh>=1 for every retained Nh<=2Y, including the possible z=unit when Nh>Y. This avoids a false sieve invocation at the lower length Y/Nh<1.

The accepted unweighted arbitrary-COEFFICIENT all-good-ideal bound (LS) is exactly available, as independently explained in accepted NEW_LOW_MODEL_BOUND-v4(4.2): write z=r*s^6 uniquely, freeze the actual coefficient mask (a,s)=1, apply the external sixth-power-free norm with physical row length Z/(Ns)^6, and sum s. The exponents6,5,2 converge and the L term uses the finite count O(Z^(1/6)), yielding Phi(Z,L) for every Z,L>=1. There is no condition Z<=L. This is a positive unweighted-row theorem, not an arbitrary weighted-row extension. When 1/2<=L<1 only the unit residual survives, with direct row norm O(Z); when L<1/2 no residual column survives.

Applying this norm to both subsequences and taking the absolute d triangle gives

 sum_{Nd<=2D}(Nd)^(-1)Phi(Z_h,D/Nd)
   =Z_h sum1/Nd
    +D Z_h^(1/6)sum1/(Nd)^2
    +D^(1/3)Z_h^(5/6)sum1/(Nd)^(4/3)
    +D^(5/6)Z_h^(1/3)sum1/(Nd)^(11/6).

The first sum is logarithmic and the other three converge. This produces D^(2sigma)Y^(-sigma)Phi(Z_h,D), up to the displayed arbitrary epsilon, and not an extra factor D or an illicit 1/L sieve. The S-supported splitting y=h*z is unique. Every power of Z_h in Phi is positive, so summing h uses fixed geometric products at exponents1,1/6,5/6,1/3. There is no extra flat S-volume log(Y). Unitary h phases stay in the coefficients until their positive norm bound; no S component has been removed.

## 4. Finite square-divisor sum and normalization

The amplitude is A1^(1-sigma)/(Nell Ne)^(1-sigma), while the ORIGINAL finite square-divisor weight has magnitude (Nk)^(-2+2sigma). For 0<sigma<1/2, its positive upper bound by zeta_K^S(2-2sigma) is valid and finite. This is only a majorant AFTER the joint bound. The exact signed finite k expression is never replaced by an infinite Euler factor. Its common-prime, v2 and S zeros remain in the identity.

The finite e sum is a fixed S constant. The ell restriction Nell<=b remains until its upper bound by tau(v2), using sigma<1. The actual v2 count is O(A2) with the standard A2^epsilon divisor loss. The last normalization is ONCE 1/D. Thus I obtain exactly the dyadic estimate (1):

 B_W^2(DYA2)^epsilon A2 A1^(1-sigma)
                  D^(2sigma-1)Y^(-sigma)Phi(Y,D).

The same proof covers a last partial band (Y,X] with X<=2Y, since its support is contained in the same prefix and it has the same lower bound Y. There is no hidden growing derivative seminorm of G in the constant.

## 5. Prefixes, the unit dual ideal and the epsilon consequence

The unit Ny=1 is a separate term, not part of the dyadic bands. Its exact Mellin expression with h=z=O has the same bound with Y=1 and Phi(1,D), or can be bounded directly by the elementary bounded-Bessel estimate. It is retained, not called a zero ideal or subtracted as a principal physical row.

For fixed 0<sigma<1/6, all four exponents alpha-sigma for alpha=1,1/6,5/6,1/3 are positive. The finite geometric dyadic sums are bounded by constants depending on sigma times X^(alpha-sigma). These same positive powers dominate the unit bound for X>=1. This proves (2). At sigma=1/6 one term would instead produce a logarithm; that endpoint is correctly excluded.

For any requested eta>0 choose the FIXED sigma=min(1/12,eta/4)>0 and invoke (2) with epsilon=eta/2. Then

 D^(2sigma)A1^(-sigma)X^(-sigma)<=D^(eta/2)

because A1,X>=1. This yields (3) with an allowed eta-dependent constant, without using sigma=0 or choosing sigma as a D-dependent fitted parameter. No principal residue is lost in this epsilon relabelling.

I independently recomputed the displayed powers. At X=D^(3/8), the dominant Phi exponent is17/16; subtracting1/4 for the pure R/D gives13/16, and subtracting5/12 for the mixed block gives31/48. At X=D, Phi has power7/6, giving11/12 pure and3/4 mixed. These are upper-bound exponents for finite representation prefixes, with feasible fixed capacity constants suppressed; they are not actual arithmetic energy measurements or global exponents.

Writing Theta=H/(A1A2), the four termwise target conditions are precisely X<=DTheta, Theta^6, D^(4/5)Theta^(6/5), D^(1/2)Theta^3. Nonempty original capacity gives A1A2^2<=H up to the fixed literal factor, so A2 and any X satisfying these sufficient conditions are polynomially bounded in D,H. The positive epsilon may therefore be relabelled in (DH)^epsilon. For a saturated pure block Theta is bounded, so this norm mechanism still only certifies bounded/subpower target prefixes; that is not an actual-error lower bound.

## 6. Verdict and remaining boundary

All claims (1)--(3) and their finite-prefix interpretation pass in the stated domain. The root's separate critical-half logarithmic argument is not implicitly used at an endpoint here. Conversely this BV estimate does not estimate the whole infinite dual sum: Phi grows with X and the complementary intermediate/high window needs its own signed argument or a separate valid tail certificate. A target-sized mixed prefix is not a target-sized full slice, and no positivity can assign a bound on the full signed slice to each of its windows.

The unchanged whole-slice13/12 and global9/8 are the correct scope statements. No new external sieve, arbitrary weighted operator theorem, general class/rho assembly, energy lower bound, positivity, GRH/determinant or Lean conclusion follows. All twelve protected HEAD/index states remain unchanged. This reviewer ran no author controls, numerical fixtures, builds, publication or browser operations.
