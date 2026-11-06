# A sharp one-row consequence of the admissible theta functional equation

Research-only v1, 6 November 2026. This NEW derivation keeps level, height, endpoint and fixed-twist costs explicit. It proves an away-from-3 one-row angular theorem from pinned unconditional theta functional equations; it does NOT supply the unmatched higher-3-primary finite-twist/local-vector interface of the ACTUAL complete family. Noncubic finite character alone is not used to assert absence of a pole. Full actual signed13/12/global9/8/GRH stay unchanged.

Primary: Dunn--Radziwill, Bias in cubic Gauss sums: Patterson's conjecture, arXiv2109.07463v3 (14 May2024), DOI10.4007/annals.2024.200.3.3. PDFdf888f8527b3647a3428d6677a3e3070aab7439f79f737f3e894218fb64cfef0; extracted text636da1119ebebdcab6756e9258554af06a42d67baf0c47026c73e960de2f4767. Use UNCONDITIONAL Section5 theta statements, NOT the GRH-conditional prime theorems. Existing primary caches remain private/local; this note redistributes no source body.

## 1. Exact admissible finite twist and cube completion

Work over O=Z[omega], lambda=1+2omega, with the SOURCE additive pairing and multiplicative primary1mod3 generators. Let r be a good squarefree primary ideal, R=Nr. Fix a primitive finite character kappa of conductor F with (F,3r)=1. Put M=F*r and psi=kappa*psi_r, where psi_r is the primitive cubic twist of the orientation used in DR Proposition5.2. The coarse result below also holds for the other cubic orientation. All constants may depend on F,kappa and a fixed integer ell!=0, never on R,T or height. The source gtilde(c) has magnitude at most1 and its literal SF-zero convention.

Define
 R_psi(s)=sum_(c primary) gtilde(c)psi(c)Theta_ell(c)/(Nc)^s,
 E_psi(s)=L^(M)(3s-1/2,kappa^3 Theta_(3ell)) R_psi(s).
Here L^(M) retains the prescribed finite deleted Euler factors, and Theta_j(c)=(alpha_c/|alpha_c|)^j. Nothing is divided out at a raw zero. Both primitive twists are unramified above3 in this section.

The coefficient support in DR(5.7),(5.17) is mu=lambda^-3*c*d^3, c SF, with tau(mu)=3^(5/2)gtilde(c)|d|. Thus, initially Re(s)>1, its ACTUAL theta series satisfies EXACTLY
 D_psi(s)=3^(5/2+3s) i^ell psi(lambda) E_psi(s).         (1)
Indeed psi(d^3)=kappa(d)^3*1_((d,r)=1), while the angular factor contributes Theta_(3ell)(d). This is ordinary coefficientwise cube completion, not an assertion that a noncubic twist has the cubic-only zeta factor. The factor L is generally nontrivial and must be retained.

Since psi is primitive modulo M, its finite additive Fourier transform is supported on units. DR Proposition5.1 applies to D_psi. For ell!=0 its COMPLETED transform is ENTIRE, with the stated two-Gamma functional equation and dual finite transform. This is the reason poles are absent here: the proved angular theta statement for an admissible twist, not the phrase 'kappa^3 is nonprincipal'. For ell=0 one must retain the actual residue proportional to the dual finite transform at zero from DR(5.46),(5.47); this note asserts no pole-free theorem in that case.

For a fixed finite but imprimitive character away3, first pass to its genuine primitive component and keep the finitely many EXTRA raw fixed-prime deletions exactly, or make a finite fixed-type decomposition. Moving r primes lying in the fixed finite conductor support are split off in finitely many q0 cases and absorbed into the fixed family, not divided out of psi(r). This costs fixed-data constants only. It does NOT resolve ramification above3.

## 2. Dual absolute series: two honest level costs

The theta functional equation is a finite combination of the fixed cusp series F1*,F19*,F10* with the finite Kloosterman transform psitilde. Its factor is (NM)^(-2s), up to fixed phases and constants. Stirling for the TWO source Gamma factors gives, on sigma=-eta with 0<eta<1/12,
 Gamma-ratio <<_(ell,eta) (1+|t|)^(2+4eta).             (2)
All finite-order/vertical-growth conditions for Phragmen--Lindelof come from the same theta Mellin representation.

It is essential to bound the dual SERIES, not infer a conductor power from the pointwise transform alone. The tau/tau1/tau2 formulas DR(5.7),(5.13),(5.14) have finitely many ramified branches and coefficients bounded by fixed lambda-powers times |d| at mu=lambda^L*c*d^3, c SF. Consequently their ABSOLUTE Dirichlet series converge uniformly at u=1+eta:
 sum_c (Nc)^(-u) sum_d (Nd)^(1/2-3u) <infinity,
with a convergent lambda geometric factor. This holds for every cusp in the fixed dual combination.

Coarse version, requiring no evaluation of the moving-r local matrix: from the exact transform DR(5.69), Parseval and Cauchy,
 ||psitilde||infinity <= sum_(a modM)|hatpsi(a)|
 <=(NM)^(1/2)(sum|hatpsi(a)|^2)^(1/2)
 <=(NM)^(3/2)||psi||infinity.                           (3)
Thus the dual ABSOLUTE series is O_fixed(R^(3/2)), and (1),(2) give the honest left-bound exponent a=3/2.

Refined version for the source cubic orientation: the moving-r part of the finite transform is exactly the source Gauss factor g(r), magnitude sqrt R, times the Ramanujan sum c_r of its argument. With fixed kappa away3 the fixed-F part has finitely many CRT additive variants (r modulo F) and a fixed bounded transform matrix. The dual series has no further moving-level power. To check that claim independently, put u=1+eta. At a good p|r, theta coefficients have exponent j+3k, j in{0,1}, k>=0, magnitude (Np)^(k/2), while |c_p| is1 at exponent0 and Np-1 at positive exponents. The local absolute factor is bounded by
 1+(Np-1)[(Np)^(-u)+sum_(k>=1)(Np)^(k(1/2-3u))
                                      (1+(Np)^(-u))].   (4)
It is O_eta(1) UNIFORMLY in p. Its product is C_eta^omega(r)<<_(epsilon,eta)R^epsilon, with the finitely many small primes absorbed in the constant. Outside r the original absolutely convergent theta series remains. Fixed-F changes cost constants. Thus the refined dual ABSOLUTE series is O_fixed,epsilon(R^(1/2+epsilon)), giving a=1/2. This explains both the Gauss normalization and the weighted Ramanujan mass; a bare supremum bound would not give the refined exponent.

The general primitive-away3 functional equation plus (3) already proves the COARSE theorem without a refined local calculation. The REFINED statement uses the moving Ramanujan evaluation in DR(5.70) and its fixed-away3 CRT extension, which is separately authored/reviewed in lane-a; no higher-3-primary extension is inferred here.

## 3. Completed convexity, with reciprocal factors handled safely

For either a=3/2 (coarse) or a=1/2 (refined), the bounds just proved and the absolutely convergent right line imply
 |E_psi(1+eta+it)| <<_fixed,eta 1,
 |E_psi(-eta+it)| <<_fixed,eta,epsilon
           R^(a+O(eta)+epsilon)(1+|t|)^(2+O(eta)).
Phragmen--Lindelof applied to the ENTIRE COMPLETED-NUMERATOR series E gives, on 1/2+eta<=sigma<=1+eta after reallocating epsilon,
 |E_psi(sigma+it)| <<_fixed,ell,epsilon
       (R(2+|t|))^epsilon
       R^(a(1-sigma))(1+|t|)^(2(1-sigma)).              (5)
This derivation NEVER applies a pole-free convexity strip to R_psi below1/2. The reciprocal L(3s-1/2,...) could have poles there.

Only AFTER (5), on sigma>=1/2+eta, divide by the actual Euler product L^(M): its argument has real part>=1+3eta, so its inverse is bounded by absolutely convergent positive Euler products, uniformly in r. There is no zero-free hypothesis or contour through unknown zeros. Hence (5) also bounds R_psi on this SAFE right half-strip. Constants deteriorate as eta tends to zero; the theorem uses an allocated epsilon, not a claim on the boundary sigma=1/2 itself.

## 4. Exact sharp one-row intervals and endpoint cost

Let I be ANY interval inside[T,2T], including its chosen open/closed endpoints, and count every distinct ideal in a repeated norm fibre. Let W be ONE fixed complex C1 profile on[1,2]. Put
 V1(W)=||W||infinity+integral_1^2 |W'(x)| dx.
For T>=1 define
 F_source(T;r,I)=sum_(c primary,Nc in I)
  gtilde(c)psi(c)Theta_ell(c) W(Nc/T)/sqrt(Nc).

Replace norm endpoints by half-integers selecting the exact same integers. The coefficient of an integer norm is divisor-bounded, since ideal multiplicity is at most a divisor function and |gtilde psi Theta|<=1. Truncated Perron at height H>=1 on Re(s)=1+eta therefore has unnormalized error
 O_epsilon(T^epsilon[1+T/H log(2T)]).                    (6)
Equal-norm fibres are counted whole; no half-value at a tie is introduced. An interval is a difference of two prefixes.

Shift ONLY through the pole-free safe strip to sigma=1/2+eta. By (5) its vertical integral costs
 O_epsilon((RT)^epsilon T^(1/2) R^(a/2) H).
The horizontal segments are at most T/H, up to allocated powers, provided R^a H^2<=T. If T>=R^a choose
 H=(T/R^a)^(1/4);
then both vertical and endpoint/horizontal terms are
 O_epsilon((RT)^epsilon T^(3/4) R^(a/4)).               (7)
The small1 in(6) is covered; exact bounded T is handled directly. If T<R^a use the elementary O(T) count instead; it is no larger than the right side of(7). Partial summation of the SAME fixed W(x)/sqrt(x) yields the uniform sharp bound
 |F_source(T;r,I)| <<_fixed,ell,epsilon
 V1(W)(RT)^epsilon min[sqrt T,T^(1/4)R^(a/4)].          (8)

Thus the coarse admissible-away3 theorem is H(alpha,beta)=(3/4,3/8);
the refined source-cubic-away3 theorem is H(3/4,1/8).
Both are actual sharp one-row theorems in their DECLARED source family, not full-family actual theorems. Endpoint phases or weights with growing derivatives are not inserted into a smooth theorem at polynomial height. The Mellin transform is not applied at a fictitious pole-free inverse-L boundary.

## 5. Conditional actual full-deletion and low-prefix assembly

Now assume an ACTUAL fixed component is legitimately matched to the corresponding theorem (8), including its inverse-different normalization, finite kappa, angular sign, raw fixed-prime zeros and any required ramified local vector. This condition is proved for the admitted away3 source family, NOT for all actual finite-order nu/source components with higher3-primary ramification.

Use the REQUIRED root WHOLE_PREFIX_LOCALIZATION-v1:
Np,Nr<=Z=D^(1/8), Nd<=D^(1/32), Nk<=min(K,D^(1/32)).
The source actual row is the accepted
 F_psi(T;t;Q,I), T=D/(Np Nd), t=p*d*k,
 Q=rad_good(p*r*d*k*s*w).
Its exact deletion opening uses h|rad(Q),(h,t)=1 and the literal factor(Nh)^(-1/2), with scale T/Nh and SF frequency h*t. Thus
 (Nh)^(-1/2)(T/Nh)^(1/4)N(ht)^beta
   =T^(1/4)(Nt)^beta (Nh)^(beta-3/4).                  (9)
For beta=1/8 or3/8 that exponent is NEGATIVE, and the finite divisor sum costs D^epsilon. Keep all zeros and phases in the identity before this triangle. This is not a heuristic 'deletions are free': (9) explicitly pays the scale/frequency factors.

The opposite-prefix raw mask gives h|rad_good(r*s*w), so
 Nh<<ZV=D^(3/16), N(ht)<<D^(3/8),
 T/Nh>>D^(21/32).
The actual parameters satisfy the optimized-height regime for both admitted a, but (8) is uniform even outside it. The original S divisor e_S is not h, and no k/s or w/s mask is imposed.

The original ONCE normalization is A1/[D Nd sqrt(Np Nr)]. Applying (8),(9) to the left residual column, then summing actual prefix coefficients by their pointwise D^epsilon bound, gives
 C_left <<V1(W)D^epsilon D^(1/4)
          (Nd)^(beta-1/4)(Nk)^beta
          Z^(beta+1/4).                               (10)
The right column is still bounded elementarily by
 B D^epsilon sqrt(D/Nd), including its harmonic prefix count.
Therefore the remaining low-d/short-k model, after ONLY the stated positive sums, is
 <<B V1(W)(DXA1)^epsilon A1 V D^(-1/4)
      Z^(beta+1/4)
      sum_(Nd<=R0)(Nd)^(beta-7/4)
      sum_(Nk<=min(K,J0))(Nk)^(beta-2).                 (11)
Both sums converge uniformly for the two beta values: beta<3/4 and beta<1 respectively. The exact finite original sums are not replaced in the identity by Euler values. Actual s is counted by O(V) only last; all finite source/rho/e_S/w masses stay fixed, and common rho(d)^2/Gamma squares/general finite-S chi(d)psi(d) are not set to one.

At A1V~D^(13/16), Z=D^(1/8), (11) has normalized power
 19/32+beta/8 =41/64 (coarse),39/64 (refined).            (12)
The same auxiliary equal-norm correction is O(B^2 A1V D^(-1+epsilon)), as in the governing notes; no norm-inequality mask is factored. Conjugate ideals stay distinct. The actual leading g0 may vanish and is never divided out. The accepted exact-discrete bridge already has target-sized errors; it is not rerun here.

These powers are CONDITIONAL for the full actual fixed-family kernel: the admitted away3 source theorem does not prove that every actual component has the required local/finite matching. In particular fixed finite-order nu may have arbitrarily high but fixed3-primary conductor; it need not have order dividing6. The angular index is actual+1/-1 and is not canceled by finite-order nu, but that fact alone does not manufacture a theta FE for the ramified3 twist.

## 6. Exact surviving result and failed step

Proved survivor: completed-convexity plus exact endpoint analysis gives(8) in the admitted primitive-away3 angular family, with explicit dual-series and profile costs. Equation(11) is a rigorous CONDITIONAL transfer to the actual localized model, retaining all original masks and normalization.

The failed full-family step is invoking the good-modulus theta equation for a finite kappa ramified above3. In DR's exact twist it is psi(lambda^4 mu); putting a character of lambda-power conductor into that formula can make it zero on the very support used for cube completion. A fixed-conductor assertion, finite Fourier expansion, noncubic label or nonzero angular index is not a proof of the missing local translate-vector identity and its dual absolute bounds. Such a ramified completion must be constructed and matched explicitly before any full actual exponent improvement is claimed.

No GRH, desired zeros/positivity, Artin holomorphy, unknown fixed-twist mean or determinant premise is used. Whole signed13/12/global unsigned9/8, other original frequency/short/principal scopes, determinant/zero-location and actual analytic/categoryLean/GRH obligations remain OPEN. No old controls, primary fetches, canonical/book/UI/artifact/index/auth/environment/dependency/Lean/MCP/publication action occurs.
