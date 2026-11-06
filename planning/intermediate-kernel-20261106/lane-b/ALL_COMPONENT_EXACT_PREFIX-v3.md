# New all-component exact-prefix transport after global root normalization

NEW v3 (v1--v2 preserved) for independent review; exact positive-epsilon absorption explicit. This is a SEPARATE extension; the same-class all-j note8197418d remains unchanged. The proof below includes its needed bilinear j estimates, rather than treating that still-reviewable companion proposal as an accepted theorem. The new global primitive-root multiplication proof v2 (25ad1b4abdcaa0598e4aec079322b4a834d180e7f9409ea5eff411985ee7503c) now has BOTH independent analytic gates: lane-B f5486cb1… and lane-A069f36b1…. The old H_ROOT hypothesis is therefore not assumed without proof here. Accepted hierarchy/positive-Phi/window machinery is input, not rerun or re-audited.

## 1. Original family and exact target of this extension

Keep the complete original good SF annular IDEAL columns D<=Nm<=2D, D>1, with distinct equal-norm/conjugate ideals kept separately, original AU/nu, one common possibly complex W and

    c_m=A_U(m)nu(m)R_m(u0)W(Nm/D),
    A_U(m)=sum_{ab|m,(a,b)=1,Na,Nb<=U}mu(a)mu(b).

All means and original signs remain; there is no extra mu(mn). Fix the same original two-pivot row block as all accepted inputs: v3=v4=v5=v6=O, literal u0 unit/S-supported with no good-prime support, original SF/coprime v1,v2, literal/ray conditions and Nu0 Nv1 Nv2^2<=H. This does not silently extend to extra good frozen factors or sum all varying u0 blocks.

For each v2 use EXACT a,b,G_v2 and original finite pre-S K_ell=sqrt(b/Nell), ell|v2,Nell<=b. Empty fibres/ell terms are0. The bounded G support is[1/2,B0], B0=5/2, amplitude<=1. The field constant is C0=3/(4pi^2). Every finite e|P_S and every raw/common-prime mask remains. No derivative-uniformity assertion is made.

Partition ALL original columns by the fixed SOURCE class group Gamma. Expand every original row-ray projector in its ACTUAL fixed finite S-supported character set rho with coefficients h_ABrho(v2). Rho need not factor through Gamma. The sum over all source class pairs A,B and ALL those rho is the exact original finite ray/coprime-column form, not one selected component.

Let P_{<=Y}^{two-pivot} denote this FULL reconstructed primitive-Poisson numerator, truncated at total dual norm Ny<=Y, with EVERY y=h z (h S-supported,z good), and EVERY original finite k<=K_ell. For fixed u0 and Y>=1,

    |P_{<=Y}^{two-pivot}|
      <<_(S,family,original-ray,nu,epsilon)
          B_W^2(DYA2)^epsilon A1A2 Phi(Y,D)
                    I(B0 A1Y/(C0D^2)),                    (1.1)

where Phi(Z,L)=Z+L Z^(1/6)+Z^(5/6)L^(1/3)+Z^(1/3)L^(5/6) and I(t)=sum_j t^j/(j!)^2. This is the exact finite-K prefix, NOT a completed-Euler model and NOT an approximation plus an omitted error. All fixed S/class/ray constants are permitted in the bound; there is no uniformity over varying S or varying row-ray modulus.

The complementary Ny>Y remains unestimated at target here. Nor is any principal/residue assembly or original physical-row energy lower bound asserted.

## 2. The proved root identity and its two distinct column phases

Fix A,B,rho. In the accepted source normalization

    tilde_chi_m=xi_m psi_A, tilde_chi_n=xi_n psi_B,
    sigma=prim(rho psi_A conjugate(psi_B)), f_S=cond(sigma), F_S=Nf_S,
    eta=xi_m conjugate(xi_n) sigma,
    f_eta=m n f_S, F=F_S Nm Nn,

on ORIGINAL coprime m,n. Xi and sigma may have nonzero fixed angular/radial UNITARY types. The TOTAL eta has type(0,0), so the SAME field J0/Bessel kernel is used. Its primitive conductor, including actual S drops, is retained; this is not a Gauss sum at a physical or induced modulus.

The newly proved global law gives EXACTLY

    epsilon(eta)=kappa_ABrho u_m conjugate(v_n),
    u_m=beta_m xi_m(f_S)rho(m),
    v_n=beta_n xi_n(f_S)conjugate(rho(n)),                   (2.1)

with kappa fixed by A,B,rho and the actual fixed types. The rho values are NOT absorbed into kappa. U and V are diagonal unitaries on the actual good columns, because m,n avoid S. Values xi_m(f_S) are primitive-good-conductor values, not raw symbols at forbidden S primes.

For t=k^2 ell, the other exact phases split as

    eta(t e)=sigma(t e)xi_m(t e)conjugate(xi_n(t e)),
    conjugate(eta(hz))=conjugate(sigma(h))conjugate(sigma(z))
         *conjugate(xi_m(h))xi_n(h)conjugate(xi_m(z))xi_n(z).
                                                                  (2.2)

ALL primitive sigma(e/h) values, including0, are kept. They must not be replaced by rho(e/h) at S, even after a conductor drop. K/ell are good, so their sigma factors are unit phases; e/h may kill a term. No division by such a value occurs.

For good z, write tilde_chi_m(z)=gamma_A(z)R_m(z), with gamma_A the accepted finite reciprocity phase independent of m within A (and similarly B). Equality extends collisions as zeros. Then

    conjugate(sigma(z))conjugate(xi_m(z))xi_n(z)
          =Omega_ABrho(z)conjugate(R_m(z))R_n(z),
    Omega=conjugate(sigma(z))psi_A(z)conjugate(psi_B(z))
                             conjugate(gamma_A(z))gamma_B(z),
    |Omega(z)|=1 for good z.                                (2.3)

Equivalently Omega=conjugate(rho(z))conjugate(gamma_A(z))gamma_B(z) on good arguments. This is a fixed UNITARY ROW phase, not a new positive weight/row-family theorem. It is kept in the exact pairing and only bounded in Cauchy. One must not claim psi_A and psi_B cancel BETWEEN different classes; (2.3) is the retained correction.

## 3. Exact all-j component with every scalar zero retained

Use the accepted finite-K Bessel hierarchy. Write M_j(v2)=integral u^j G_v2(u)du, |M_j|<=2B0^j, and r_j(m)=(D/Nm)^j<=1. Define two DISTINCT column vectors

    a_m^(j)=c_m u_m/sqrt(Nm) *r_j(m)*R_m(v2^2)
                            *xi_m(k^2 ell e)conjugate(xi_m(h)), m in A,
    b_n^(j)=c_n v_n/sqrt(Nn) *r_j(n)*R_n(v2^2)
                            *xi_n(k^2 ell e)conjugate(xi_n(h)), n in B.
                                                                  (3.1)

All original AU/beta/W/nu phases remain unfactored. Xi(t e) includes the good raw k/ell collisions; v2 collisions are in R_m(v2^2). At S, xi_m(e/h) is a legitimate primitive column phase. Its modulus is1 for good m, because its conductor m is disjoint from S. Column factors u_m,v_n also have modulus1; no variable normalization cost is hidden.

The exact j component, with the original coprime mask FIRST, is

    P_j^(ABrho)=C0^(-1/2)kappa_ABrho A1/(j!)^2
                  *(-A1/(C0D^2))^j F_S^(-j-1/2)
       *sum_{v2} M_j(v2)h_ABrho(v2)
       *sum_{ell|v2,Nell<=b}mu(ell)/(Nell)^(1+j)
       *sum_{e|P_S}mu(e)/(Ne)^(1+j)
       *sum_{k good,(k,v2)=1,Nk<=K_ell}mu(k)/(Nk)^(2+2j)
       *sum_{h S-supported,Nh<=Y}
                   sigma(k^2 ell e)conjugate(sigma(h)) T_jh,       (3.2)

    T_jh=(Nh)^j sum_{z good,Nz<=Y/Nh}(Nz)^j Omega_ABrho(z)
               sum_{m in A,n in B,(m,n)=1}
                     a_m^(j)conjugate(b_n^(j))
                                 conjugate(R_m(z))R_n(z).   (3.3)

Thus eta(k)^2 has not disappeared or been replaced by1: its two xi factors are in(3.1), and sigma(k^2) is in(3.2). Only its NORM exponent is2+2j. Every mu(ell)/mu(e)/mu(k), finite ray coefficient, root phase, F_S scale and sigma zero occurs once. All original finite Kcut and e/ell restrictions remain literal. There is no completed E_T or finite-cutoff error substitution.

For any off-coprime pair, the displayed individual-column product is only an AUXILIARY extension used for gcd inversion. It is NOT the primitive character/root/conductor at a diagonal or overlapping pair. The actual coprime mask is exact before any extension; all full divisors are retained to cancel unwanted overlaps.

## 4. Different residual classes require bilinear Cauchy

Insert 1_(m,n)=1=sum_{d|m,n}mu(d) in(3.3). Put m=da,n=db; residual a,b are SF, coprime to d, but may overlap with each other. Their classes are A[d]^(-1) and B[d]^(-1), generally different. Raw multiplicativity gives

    conjugate(R_da(z))R_db(z)
         =1{(d,z)=1}conjugate(R_a(z))R_b(z).

For each d, the residual form is therefore a BILINEAR z sum with fixed row phase Omega and nonnegative weight(Nh Nz)^j1{(d,z)=1}. Cauchy in that row variable gives two weighted positive norms. ONLY INSIDE EACH may the raw(d,z) mask be dropped and

    (Nh Nz)^j<=Y^j

be applied. The product of the two square roots costs exactly Y^j, not Y^(2j). No PSD or equality of residual classes is assumed.

Each vector in(3.1) has the SAME pointwise size bound as c_m/sqrt(Nm); real r_j is an additional contraction. On the actual annular subsequence,

    sum_a|a_da^(j)|^2, sum_b|b_db^(j)|^2
            <<_epsilon B_W^2 D^epsilon/Nd,                 (4.1)

uniformly in j,k,ell,e,h,A,B,rho. Neither beta_da nor AU(da) is factored. Xi values at fixed S arguments stay as arbitrary unitary COLUMN coefficients.

Use the already accepted arbitrary-coefficient ALL-good-row raw Phi(Z,L) norm for every Z,L>=1. Residual column classes can be retained as zero coefficients. Any common primitive xi row phase is removed separately INSIDE its own positive norm before using raw finite-order R; xi is not assumed sixth-order. For1/2<=L=D/Nd<1 count the unit residual directly; below1/2 there is no column. The same accepted ideal-d sums then give

    |T_jh| << B_W^2(DY)^epsilon Y^j Phi(Y/Nh,D).             (4.2)

The implicit constant is independent of j and all fixed column modulations. This is not a per-conductor absolute completion: the whole m,n form was combined first. Different original/root classes have been handled by genuine bilinear Cauchy, not by a positive completion of the coprime matrix.

The S h sum has the SAME four positive exponents1,1/6,5/6,1/3. Scalar|sigma(h)|<=1 does not enlarge it:

    sum_{Nh<=Y,h supported on S}Phi(Y/Nh,D)<<_S Phi(Y,D).

All h outside the finite total-norm window remain absent from that prefix and present in the full outside complement. Original forbidden S raw values are never restored.

## 5. Summation and the full original prefix

The exact F_S factors satisfy F_S>=1, so F_S^(-j-1/2)<=1 only in the upper bound; their actual values remain in(3.2). The scalar|sigma(k^2 ell e)|<=1, with actual zero terms kept in the identity. E finite weights are bounded by sum1/Ne, k FINITE weights by zeta_K(2), and ell's original truncated sum by tau(v2), all uniformly in j. The number/divisor loss of actual v2 is A2(DA2)^epsilon. Consequently

    |P_j^(ABrho)|
      << B_W^2(DYA2)^epsilon A1A2 Phi(Y,D)
             *[B0 A1Y/(C0D^2)]^j/(j!)^2.                   (5.1)

The finite ray Fourier coefficients and number of source class pairs are fixed constants of the original family. Summing them and the absolutely convergent j series proves(1.1). This reconstructs ALL actual class/rho components of the original two-pivot prefix for the fixed u0, not just a same-class block. No assumption that rho factors through sourceGamma is used.

All original outer sets and Ny<=Y are finite, and the accepted finite-K Bessel hierarchy is absolutely convergent there. Thus no infinite-dual/Fubini claim is being made. A unit or sixth-power dual mode is included exactly if it is in the prefix, with its actual raw and primitive local phases; there is no centering or mean deletion.

## 6. Quantitative consequence and honest boundary

If A1Y<=cD^2 for fixed c, I is a field/c-dependent constant. The normalized exact FULL two-pivot prefix therefore has sufficient target conditions, with R=A1A2 and Theta=H/R,

    Y<=min{DTheta,Theta^6,D^(4/5)Theta^(6/5),
                         D^(1/2)Theta^3,cD^2/A1}.           (6.1)

There is NO oldY<=sqrt(H) approximation-error restriction. At critical mixed scales A1~D^(5/12), A2~D^(1/6), H~D^(3/4), the FULL original two-pivot finite prefix Ny<=constant*D is target-sized O(B_W^2 H D^epsilon), for fixed u0 and the actual original ray/S support. All I arguments there are O(D^(-7/12)). AtY=D^(3/8), its normalized pure/mixed powers are13/16 and31/48. In the pure case A2=1, the stated norm majorant still allows only bounded/subpower target windows; it proves no lower bound for larger windows.

These are finite representation-prefix bounds, not positive physical energies and not an infinite-kernel target. The original exact capacity b(v2) remains throughout; power-scale saturation is only bookkeeping, and an empty actual block gives0. There is no asserted density/lower construction.

The complement Ny>Y, including ALL nonunit/S-supported modes outside the prefix, remains part of the original kernel and is not estimated at target by this result. Full scoped13/12 and global9/8 remain current; principal/residue assembly and GRH are unchanged. The newly proved root normalization removes one TECHNICAL hypothesis and supplies explicit phase transport, not cancellation by itself. The all-j theorem(1.1) does not assume the separate BV--Mellin theorem. That theorem has now been independently accepted, and its distinct all-component transport is proved in Section7 below.

No accepted j0/window/Euler audit or old numeric control/table was rerun. There is no canonical/book/UI/build/browser/env/auth/publication/index mutation. This is a new proof requiring its own independent review, in addition to the two completed analytic gates for global root normalization.


## 7. NEW accepted-input BV--Mellin transport: all finite prefixes without I

This section adds a second result, not a new proof of A's already reviewed transform theorem. Input A is HONEST_BV_MELLIN_INTERMEDIATE-v1 (985295ddbdb03b721a68ce7a1397ca5c80b75c93df26edfc874f028be0b2cb8f), independently accepted by C ca55abb4be886113b1c518c47c816d09e296f96612f28bcec8f34dccef2b7f51. Its actual TV/Mellin L1 bound at a FIXED line0<lambda<1/2 is used unchanged. Lambda denotes the contour real part; sigma above still denotes the primitive S CHARACTER, so the two must not be confused.

For a fixed class/rho block the exact primitive-conductor factor after Mellin inversion is

    F_S^(s-1/2) * (A1/(Nell Ne))^(1-s), s=lambda+i tau.    (7.1)

It is F_S^(s-1/2), NOT its inverse. Since F_S>=1 and lambda<1/2, its modulus is<=1. The ACTUAL eta has total type(0,0), so A's same field Gamma/BV integral is applicable; no functional equation for a non-finite-order individual xi is substituted.

Use distinct coefficient vectors

    a_m(s)=c_m u_m R_m(v2^2)xi_m(k^2 ell e)bar xi_m(h)
                                                    *(Nm)^(s-1/2),
    b_n(s)=c_n v_n R_n(v2^2)xi_n(k^2 ell e)bar xi_n(h)
                                                    *(Nn)^(s-1/2).

The paired second vector is b_n(conjugate(s)) before conjugation, exactly as in the accepted Mellin convention. Scalar sigma(k^2 ell e)bar sigma(h), including its primitive e/h zeros, stays outside. The good-z row phase is the SAME Omega in(2.3). All exact finite K_ell, e/ell and raw collision masks remain, with finite k norm weight(Nk)^(-2+2s). None is completed to an Euler product.

For the dyadic band Y<NhNz<=2Y, insert exact gcd inversion and use bilinear Cauchy for the two DIFFERENT residual classes as in Section4. The weight modulus is at mostY^(-lambda), and the row phase Omega(z)(NhNz)^(-i tau) has modulus1 on good z. Those masks/weights are removed or bounded only inside the two positive norms, using their legal upper prefix2Y/Nh>=1. The left/right subsequence estimates are

    sum_a|a_da(s)|^2, sum_b|b_db(conjugate(s))|^2
                    <<B_W^2 D^(2lambda+epsilon)/Nd,        (7.2)

uniform in tau and every fixed primitive phase. No equality of source/residual classes is used across the two vectors, and no primitive xi is assumed sixth-order. Their individual common residual-class row phases are cancelled separately before raw Phi is applied.

The accepted d/Phi and positive S-h sums therefore have precisely the same bounds as A's original proof, now with the extra fixed unit row phase and distinct unit column gauges. The scalar|sigma(h)|<=1 only suppresses terms. Finite k is bounded AFTER this joint estimate by zeta_K^S(2-2lambda), lambda<1/2; this is only a positive majorant, not an Euler completion in the actual kernel. Finite ell/e weights have exponentlambda-1; their cutoffs and original scalar zeros remain before the comparison. The TV/Mellin integral and v2 count are unchanged. Sum the FIXED finite class/rho components. This proves for the FULL reconstructed original two-pivot band

    |P^(two-pivot)(Y,2Y]|/D
      <<_(lambda,data,epsilon) B_W^2(DYA2)^epsilon
           A2 A1^(1-lambda)D^(2lambda-1)Y^(-lambda)Phi(Y,D).
                                                                  (7.3)

No general unproved H_ROOT remains: its actual normalization was independently proved/gated before this extension. Neither an arbitrary row-weight theorem nor a per-conductor absolute completion is used; (7.2) is an arbitrary-COLUMN-coefficient application after genuine bilinear Cauchy.

For0<lambda<1/6 every Phi exponent minuslambda is positive. The accepted finite-dyadic summation, including a last partial band and the dual UNIT separately, is unchanged. It is legitimate for ALL fixed class pairs: at y=O the same phase/gcd/Cauchy argument uses the positive row prefix1 and retains all scalar zeros. Consequently for every FINITE X>=1,

    |P^(two-pivot)_{<=X}|/D
       <<_(lambda,data,epsilon) B_W^2(DXA2)^epsilon
           A2 A1^(1-lambda)D^(2lambda-1)X^(-lambda)Phi(X,D).
                                                                  (7.4)

For a requested FINAL loss eta0>0, choose lambda=min(1/12,eta0/4)>0 FIXED with respect to D,X,A1,A2, and use(7.4) with its positive-norm epsilon=eta0/2. Constants may depend on eta0, never through a D-dependent contour. Since A1,X>=1 and2lambda<=eta0/2,

    D^(2lambda)(A1X)^(-lambda)<=D^(eta0/2),
    (DXA2)^(eta0/2)D^(eta0/2)<=(DXA2)^eta0.

Rename the final eta0 as epsilon. This is exact positive-epsilon absorption, with no endpoint lambda=0 or lambda=1/2. Hence the FULL EXACT finite-K two-pivot prefix obeys

    |P^(two-pivot)_{<=X}|/D
         <<_(data,epsilon) B_W^2(DXA2)^epsilon
                         (A1A2/D)Phi(X,D), ALL finite X>=1. (7.5)

There is no Taylor-I, X<=sqrt(H), or low-profile approximation restriction in(7.5). The actual G, finite square-divisor cutoffs and capacity were not replaced. This is the new ALL-COMPONENT extension of the accepted same-class BV--Mellin prefix theorem, not a blanket assertion that a same-class proof automatically covers other components: equations(2.1)--(4.2),(7.1)--(7.2) supply the distinct phases, scalar zeros and bilinear step.

In particular the full original two-pivot finite prefix X~D is target-sized in the critical mixed block; the critical pure prefix has upper power11/12. At X=D^(3/8), the full actual prefix powers are13/16 pure and31/48 mixed. The four sufficient target constraints are those in(6.1) WITHOUT its last Taylor conditioncD^2/A1. They remain sufficient upper-bound conditions, not necessary conditions or lower bounds.

All these conclusions concern finite representation prefixes for the fixed original u0/ray block. The complete infinite dual kernel, any summation over all varying u0 blocks, principal/residue target assembly, physical energy lower bounds, global9/8/whole13/12 improvements, Lean and GRH are NOT concluded. The nonunit/S-supported complement outside each finite prefix remains. No mean has been centered or ideal fibre merged, no forbidden raw S value restored, and no old controls/build/publication repeated.
