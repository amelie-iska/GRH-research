# Exact finite-K, all-Bessel-order joint window bound

NEW research-only v1, 6 November 2026. The preceding HANDOFF-v2 (daa59cabbc6fb81ba3a120546a26699700b3123fa0b7a17de09a93acc64630cc) and governing aggregate (9aea44feff625b4af056b703f4060f308093f7f6a4a4ee1b76e3154ad354761e) are INPUTS, not results re-audited here. In particular the j=0/window/Euler hierarchy and the positive raw Phi norm are reused accepted ingredients. This note makes a NEW joint estimate of the EXACT finite-K S-complete window by bounding each Bessel order before summing. No old arithmetic/control/exponent grid is rerun, and no canonical/build/UI/browser/auth/release/index operation occurs.

## 1. Actual window and theorem

Keep the original remaining UNWEIGHTED two-pivot family v3=v4=v5=v6=O, fixed literal u0 unit/S-supported with no good-prime support, original good SF/coprime v1,v2, full ray/S/union/raw-zero masks and capacity Nu0 Nv1 Nv2^2<=H. Additional good frozen factors require their own primal deletions/rescalings and are not included here. Fix ONE source column class C on both sides and the rho=1 component of the actual finite row-ray expansion. Other class/rho components are not claimed.

All original good SF columns in D<=Nm<=2D remain ideal-indexed; equal-norm/conjugate ideals are distinct. Use literally

    c_m=A_U(m)nu(m)R_m(u0)W(Nm/D),
    A_U(m)=sum_{ab|m,(a,b)=1,Na,Nb<=U}mu(a)mu(b),
    w_m=c_m beta_m/sqrt(Nm).

W is ONE common possibly complex fixed column profile, B_W=||W||infinity. No AU/beta multiplicativity, centering, changed coefficient, rational-norm-SF restriction or new row-weight theorem is assumed. The same-class/rho1 primitive root identity is the REUSED accepted input

    eta_mn=xi_m conjugate(xi_n), f_eta=mn,
    epsilon(eta_mn)=kappa_C beta_m conjugate(beta_n),
    |kappa_C|=|beta_m|=1,                                   (1.1)

on ORIGINAL coprime m,n in C. No general H_ROOT is used.

For actual v2 let a=ceil(A1), b=min(ceil(2A1)-1,floor(H/(Nu0 Nv2^2))). Empty b<a fibres are0. Use the accepted exact bounded nodal interpolant G_v2, supported in [1/2,B0], B0=5/2, with 0<=G<=1. Its derivative seminorms may grow with A1. For each ell|v2 with Nell<=b FIX K_ell=sqrt(b/Nell)>=1 BEFORE S-removal; empty ell terms are0. Keep e|P_S and every finite k<=K_ell. Put T=S union supp(mn v2 ell). All raw common-prime zeros are literal.

Let P_{<=Y,C,1} be the accepted primitive-Poisson numerator truncated at the TOTAL dual ideal norm Ny<=Y, including EVERY y=h z with h S-supported and z good. This is the EXACT finite-K window, for the fixed interpolation/cutoff representation, not the completed-Euler low model and not a profile approximation. The claim is, for D>1,Y>=1,A1,A2>=1,

    |P_{<=Y,C,1}|
      <<_(S,family,ray,nu,epsilon) B_W^2(D Y A2)^epsilon
          A1 A2 Phi(Y,D) I(B0 A1 Y/(C0 D^2)),               (1.2)

where

    C0=3/(4pi^2),
    Phi(Z,L)=Z+L Z^(1/6)+Z^(5/6)L^(1/3)+Z^(1/3)L^(5/6),
    I(t)=sum_{j>=0}t^j/(j!)^2, t>=0.                       (1.3)

The field constant C0 is distinguished from the source CLASS C. The implicit constant is independent of j, K_ell, all primitive h/e phases and every actual conductor. Profile dependence in this estimate is only B_W and the stated bounded/support constants of the accepted nodal row interpolant. It does not require uniformly bounded higher derivatives.

## 2. Accepted exact hierarchy, without an Euler completion

The accepted A-lane finite-K hierarchy, Eq(9) of EULER_SCHUR_AND_BESSEL_HIERARCHY-v1 (48de3f90…), gives the Bessel expansion

    dotG(X)=C0^(-1/2) sum_{j>=0}(-X/C0)^j M_j/(j!)^2,
    M_j=M_j(v2)=integral u^j G_v2(u)du,
    |M_j|<=2 B0^j.                                        (2.1)

We USE that identity and its accepted convergence, rather than re-prove it. Applied to the exact actual window, each j carries the unchanged character phase eta(k)^2, the finite weight (Nk)^(-2-2j), and the norm factors (Nm Nn)^(-j). No character is raised to a new power2+2j: only the ABSOLUTE NORM exponent changes. In particular no new primitive-conductor formula is introduced.

For the fixed parameters v2,ell,e,k,h set

    R_j(m)=(D/Nm)^j,  0<R_j(m)<=1,
    a_m^(j)=w_m R_j(m) R_m(v2^2) chi_m(ell)chi_m(k)^2
                                xi_m(e)conjugate(xi_m(h)). (2.2)

All source S values use the primitive xi_m; they are NOT the forbidden original raw symbol at S. They are unitary column phases since m is good. Original AU(da), beta_da, nu/common complex W stay unfactored after any d restriction. The (Nm Nn)^(-j) factor has supplied D^(-2j) times the two real contractions R_j. Literal zeros at k/ell/v2 remain in a_m^(j).

With y=h z, the jth term of the exact numerator is

    P_j=C0^(-1/2)kappa_C (-A1/(C0 D^2))^j A1/(j!)^2
       *sum_{v2 actual}M_j(v2)h_0(C,C;v2)
       *sum_{ell|v2,Nell<=b}mu(ell)/(Nell)^(1+j)
       *sum_{e|P_S}mu(e)/(Ne)^(1+j)
       *sum_{k good,(k,v2)=1,Nk<=K_ell}mu(k)/(Nk)^(2+2j)
       *sum_{h S-supported,Nh<=Y} T_{j,h},                  (2.3)

where all active original columns in a_m^(j) remain and

    T_{j,h}=(Nh)^j sum_{z good,Nz<=Y/Nh}(Nz)^j
                 sum_{m,n in C,(m,n)=1}
                    a_m^(j)conjugate(a_n^(j))
                              conjugate(chi_m(z))chi_n(z). (2.4)

Equation(2.3) retains mu(ell)/mu(e)/mu(k), the actual ray coefficient, kappa, beta phases, all raw zeros and complex W ONCE. The finite-k deletion of q is in the raw chi_m(k)chi_n(k) values; the displayed(k,v2)=1 and good-k restrictions complete T. No completed E_T is substituted and no omitted finite-cutoff error is being claimed small.

As in the accepted LOW proof, (2.4) uses only an AUXILIARY individual-column product extension off the original coprime support. It is not the primitive eta/root/conductor at overlaps or diagonal, and no principal Poisson term is asserted there. The original coprime mask comes first; exact gcd inversion then cancels auxiliary overlaps/self-pairs with all ideal divisors.

## 3. Uniform j-bound: weights only inside positive norms

This is the NEW step. Reuse exact ideal-gcd inversion as in the accepted LOW proof. On GOOD z the common source class factors cancel before using the raw denominator identity

    R_da(z)conjugate(R_db(z))
       =1{(d,z)=1} R_a(z)conjugate(R_b(z)).                 (3.1)

The residual a,b may overlap; each is SF and coprime to d, and each has source class C[d]^(-1). The primitive xi_a itself need NOT have order6. Its common residual-class psi row phase cancels inside each positive norm before raw sextic extraction, exactly as in accepted LOW-v4.

After gcd inversion,

    T_{j,h}=sum_d mu(d) (Nh)^j
      sum_{z good,Nz<=Y/Nh,(d,z)=1}(Nz)^j
            |sum_{a residual}a_da^(j)conjugate(R_a(z))|^2.  (3.2)

Only NOW, after a d triangle has produced positive subsequence norms, may we use

    (Nh Nz)^j<=Y^j.                                       (3.3)

There is no invalid step bounding a signed character pairing by the unweighted pairing times Y^j. There is also no arbitrary positive-row-weight large sieve: (3.3) simply dominates a bounded nonnegative weight inside a positive norm, leaving the SAME unweighted all-good-ideal rows.

The original annular pointwise bound and contraction R_j give, UNIFORMLY in j and every fixed modulation,

    sum_a|a_da^(j)|^2 <<_epsilon B_W^2 D^epsilon/Nd.         (3.4)

This is the accepted bound with an extra contraction (D/(Nd Na))^j<=1 on the original support. It assumes neither AU(da)=AU(d)AU(a) nor beta multiplicativity. Keeping primitive xi_da(e/h) as column phases is essential.

Use the accepted arbitrary-COEFFICIENT raw all-ideal Phi(Z,L) norm for ALL Z,L>=1, including its sixth-power coefficient collision mask. No Z<=L or simplified H<=D envelope is used. For1/2<=L=D/Nd<1 count the unit residual directly; L<1/2 has no column. The accepted d sums1/d,1/d^2,1/d^(4/3),1/d^(11/6) and logarithm are unchanged by j. Therefore

    |T_{j,h}|
      << B_W^2(DY)^epsilon Y^j Phi(Y/Nh,D).                 (3.5)

The implicit constant is independent of j. All actual source/S phases have been fixed as bounded column coefficients BEFORE applying this positive norm.

The subsequent S-supported h sum is also independent of j:

    sum_{h supported on S,Nh<=Y}Phi(Y/Nh,D)<<_S Phi(Y,D).    (3.6)

Its four positive exponents remain1,1/6,5/6,1/3. The factor(Nh)^j was absorbed in Y^j inside(3.2); it must NOT be left to create a false zero/negative-exponent S sum.

## 4. Summing every Bessel order with explicit dependence

All remaining auxiliary absolute weights in(2.3) are uniformly bounded in j:

    sum_{e|P_S}(Ne)^(-1-j)<=sum_{e|P_S}1/Ne,
    sum_{k good,(k,v2)=1,Nk<=K_ell}(Nk)^(-2-2j)<=zeta_K(2),
    sum_{ell|v2,Nell<=b}(Nell)^(-1-j)<=tau(v2).

These are comparisons of the actual FINITE sets; no cutoff is completed in the formula. The count/divisor bound for actual v2 costs A2(DA2)^epsilon, |h_0| is bounded by fixed finite-ray data, and |M_j(v2)|<=2B0^j. Equations(2.3)--(3.6) now yield, with ONE constant independent of j,

    |P_j| << B_W^2(D Y A2)^epsilon A1 A2 Phi(Y,D)
                      *[B0 A1 Y/(C0 D^2)]^j/(j!)^2.       (4.1)

This is an actual joint column estimate: the m,n sum was combined using its raw character norm, never completed conductor by conductor. Taking absolute values in the stated auxiliary indices/j does not delete an orientation mean or replace the original q sign by a new coefficient.

For fixed D,Y all original outer sums, finite k and the total dual window are finite, and the accepted Bessel series is absolutely convergent. The uniform bound(4.1) also sums absolutely, so termwise passage and its estimate are justified. This is NOT an interchange with the infinite dual ideal sum. Summing j proves(1.2).

For t>=0, I(t)<=exp(t) and I(t)<=exp(2sqrt(t)). Thus for any FIXED c>0,

    A1Y<=c D^2

makes the I factor an explicit constant I(B0c/C0), independent of D,A1,Y. The row profile still has growing derivatives; no fixed-smooth claim or high-tail cutoff follows from this finite-window argument. If M_0=0 the exact j=0 term vanishes, while all remaining terms are retained; no nonvanishing assumption is made.

## 5. Exact-window target range, without a low-model error term

Let R=A1A2 and Theta=H/R. When A1Y<=cD^2, division by D gives the normalized bound

    |P_{<=Y,C,1}|/D << B_W^2(DYA2)^epsilon (R/D)Phi(Y,D).   (5.1)

The four Phi terms are at most H under the sufficient conditions

    Y<=min{D Theta,Theta^6,D^(4/5)Theta^(6/5),
                       D^(1/2)Theta^3,cD^2/A1}.           (5.2)

There is NO Y<=sqrt(H) approximation-error restriction: (5.1) bounds the EXACT finite-K window, not its completed-Euler low model. All actual empty-fibre and ell cutoffs and the original capacity b(v2) were retained in its definition. Conditions(5.2) are sufficient for this norm majorant, not necessary for the actual scalar form.

For critical power bookkeeping H~D^(3/4) with fixed Nu0 and saturated A1A2^2~H:

* Mixed A1~D^(5/12),A2~D^(1/6) admits Y~D. The I argument is O(D^(-7/12)), Phi(D,D) has leading power7/6, and R/D contributes-5/12, giving normalized power3/4. Thus this REPRESENTATION-FIXED SAME-C/rho1 actual prefix is target-sized to dual norm of order D, extending the previously certified D^(3/8) window. There is no low-profile approximation error to add.
* Pure A1~D^(3/4),A2=1 still has Theta~1, so the stated norm majorant allows only bounded/subpower target windows when epsilon losses are allowed. It does not prove an actual lower bound for any longer window. At Y=D^(3/8), the exact-window bound has power13/16; the corresponding mixed power is31/48. No old exponent-control run is repeated to obtain these algebraic substitutions.

All displayed power statements are upper bounds; if an exact finite block is empty they are vacuous, not assertions of density or a lower construction. The literal physical capacity remains in b throughout, including constants and unit/S factors.

## 6. Remaining problem and scope

This proves a NEW exact all-j intermediate-window bound, not merely a recheck of the accepted unit or j=0 approximation. It exploits the accepted hierarchy together with a uniform joint positive-norm argument at EVERY order. It requires no general H_ROOT: only the reused same-C/rho1 root gauge. Arbitrary coefficients are allowed in the unweighted positive norm, while actual AU/nu/complex W and all contraction/modulation factors remain as coefficients.

It does NOT bound other class pairs/rho components or the complementary total dual norms Ny>Y. It does NOT sum the I majorant over all dual ideals; it grows and cannot certify a high tail. The separate honest high-tail and BV/Mellin routes remain distinct inputs/attempts. Full original scoped signed13/12 and global9/8 comparisons are unchanged until ALL components/ranges and principal/residue assembly are controlled. There is no energy positivity/lower bound, fixed-W obstruction, new large-sieve theorem, Lean or GRH claim. Every nonunit/S-supported mode INSIDE the stated exact window is included, and the entire outside complement remains in the full problem.
