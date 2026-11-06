# NEW actual joint bound for the same-source-class, trivial-ray low model

NEW v4 (v1--v3 preserved; primitive infinity-type guard explicit), research only, 6 November 2026. This is a genuinely joint m,n partial bound for one precisely specified finite-window MODEL. It is not a bound on the whole primitive Poisson kernel, other class pairs/ray components, principal/residue assembly, or the global signed target. No old controls/tables or numerical experiment is rerun.

## 1. Statement and exact scope

Use the accepted WINDOW_AND_COMPLEMENT-v2 (SHA256 a4df542c9a0874fc2ca5b0dabcb39e51a59b3d1a4243f9133e50431439a37890), root acceptance 490b60fa286067ea79c8d6d51594de5ff9eb130c120eebcc8f06068823309b4d, dual-unit lemma v3 abeee901…, v8 cba96d34… with its required scope addendum5f576c22…. The actual family remains v3=v4=v5=v6=O, fixed literal u0 unit/S-supported with NO good-prime support, actual SF/coprime v1,v2 and exact capacity Nu0 Nv1 Nv2^2<=H. Keep every original annular good SF ideal column m (D<=Nm<=2D), equal-norm/conjugate ideals separately, one common possibly complex W, original nu and

    c_m=A_U(m)nu(m)R_m(u0)W(Nm/D),
    A_U(m)=sum_{ab|m,(a,b)=1,Na,Nb<=U}mu(a)mu(b).

Fix ONE SOURCE column class C and restrict both m,n to C, with the EXACT rho=1 coefficient from the full original finite row-ray expansion. Its coefficient h_0(C,C;v2) stays, bounded by its fixed finite-ray constant. This is not an assertion that the entire actual family has rho=1, or that every row-ray character factors through the source class group.

For coprime m,n in C, the inherited de Faveri Lemma3.3/v8(5.2) gives UNCONDITIONALLY

    f_eta=mn, eta=xi_m conjugate(xi_n),
    epsilon(eta)=kappa_C beta_m conjugate(beta_n),
    |kappa_C|=|beta_m|=1.                                   (1.1)

This uses only the accepted same-class/rho1 law, NOT the conditional general H_ROOT. xi_m is the source primitive good-conductor unitary Hecke character; its values at S are legitimate column phases, not original forbidden raw symbols. No angular/type-one or finite-order description of beta_m is assumed.

Let P_low,C,1(Y) be exactly this component of accepted window model(3.2), including its E_T(2,eta^2), E_S(1,eta), capacity-truncated Q_v2,b(eta), g0(v2), and all original raw prefactors. For Y>=1,

    |P_low,C,1(Y)|
      <<_(S,family,ray,nu,epsilon) B_W^2 (D Y A2)^epsilon
                                      A1 A2 Phi(Y,D),       (1.2)

where

    Phi(Z,L)=Z+L Z^(1/6)+Z^(5/6)L^(1/3)+Z^(1/3)L^(5/6).

The column profile enters only through B_W=||W||infinity. Actual higher row-interpolant derivative seminorms are not used. Empty actual row/column fibres give zero. The model's normalization is P_D=D*S1^AA; divide(1.2) by D for the normalized LOW MODEL.

## 2. Do not replace a special-vector form by an entrywise Euler bound

We prove(1.2) by an explicit ABSOLUTELY SUMMABLE diagonal expansion, not by incorrectly applying an arbitrary operator estimate to only one attractive vector. The Euler mean is expanded as

    E_T(2,eta^2)
      =sum_{k good,(k,v2)=1}mu(k)/(Nk)^2
                         chi_m(k)^2 conjugate(chi_n(k)^2).  (2.1)

The literal zeros remove every k collision with m or n; T=S union supp(mn v2 ell), ell|v2, is not shrunk to a power conductor. The k series in(2.1) is infinite because THIS MODEL contains the completed Euler product. It is absolutely convergent; its absolute weight is at most zeta_K(2) (indeed11/7 on good ideals). It is NOT a replacement of the exact finite Kcut in the full transform: that finite cutoff and its explicit error remain in the accepted window approximation.

Also use the exact finite expansions

    E_S(1,eta)=sum_{e|P_S}mu(e)eta(e)/Ne,
    Q_v2,b(eta)=sum_{ell|v2,Nell<=b}mu(ell)eta(ell)/Nell,

and the EXACT S-complete window

    A_eta(Y)=sum_{h S-supported,Nh<=Y}conjugate(eta(h))
                 sum_{z good,Nz<=Y/Nh}conjugate(eta(z)).     (2.2)

All these interchanges are legitimate: m,n,v2,ell,e,h,z sums are finite for fixed D,Y, and only the k series is infinite, with absolute exponent2. No infinite-dual/Mellin-contour Fubini is used. All means, including unit/sixth-power dual modes, stay.

Put

    w_m=c_m beta_m/sqrt(Nm),
    a_m=w_m R_m(v2^2) chi_m(ell) chi_m(k)^2
                         xi_m(e) conjugate(xi_m(h)).        (2.3)

Every original column mask/class restriction is retained in this vector, or by setting its coefficient to zero. At an S argument e,h, (2.3) uses xi_m, NOT raw R_m. For m good its primitive conductor m is disjoint from S, so these unitary factors have modulus1. The k/ell/v2 factors have modulus<=1 with their literal zeros. Original nu,u0 and complex W remain inside w_m. No beta or A_U is factored as m varies.

For the fixed v2,ell,e,k,h inner sum, (1.1) reduces the joint column form to the scalar kappa_C times

    T(a;Z)=sum_{z good,Nz<=Z}
             sum_{m,n in C,(m,n)=1}
                a_m conjugate(a_n)conjugate(chi_m(z))chi_n(z),
    Z=Y/Nh>=1.                                             (2.4)

All finite signs mu(ell),mu(e),mu(k), h_0 and weights remain outside ONCE. This reduction combines the actual m,n sum before taking any absolute value in its conductors. The bounds below take triangles in the displayed auxiliary expansions and d only; they do not complete each q separately or discard the orientation mean.

## 3. Exact gcd inversion and the raw S-mask point

Insert the ideal identity 1_(m,n)=1=sum_{d|m,n}mu(d) into(2.4), retaining EVERY ideal divisor including full divisors. Write m=da,n=db. Original squarefreeness gives a,b SF, (a,d)=(b,d)=1; a,b themselves need not be coprime after this inversion. Their norms are in [L,2L], L=D/Nd, and their common source class is C[d]^(-1).

On GOOD z the same-class source factors in chi_m(z)conjugate(chi_n(z)) cancel. In the exact raw symbols one has

    R_da(z)conjugate(R_db(z))
        =1_(d,z)=1 R_a(z)conjugate(R_b(z)).                 (3.1)

This is ordinary multiplicativity in the SF denominator with its zero sentinel, not a primitive extension at an S prime. Equivalently use the source's multiplicative family on good arguments and its common class factors. Thus

    T(a;Z)=sum_d mu(d)
        sum_{z good,Nz<=Z,(d,z)=1}
          |sum_{a residual} a_da conjugate(R_a(z))|^2.      (3.2)

The common chi_d phase contributes exactly the displayed raw (d,z) mask. Primitive xi_da(e) and xi_da(h) in the coefficient are not divided or moved into the z family. For each fixed d,e,h,k,ell,v2 they are only column modulations. The original beta_da, A_U(da), nu(da), W(Nd Na/D), class restriction and all zero masks remain UNFACTORED inside a_da.

The product kernel defined by the INDIVIDUAL column characters and factors in(2.3) is only an AUXILIARY Gram extension off the ORIGINAL (m,n)=1 support. On a diagonal or overlapping pair, it is NOT claimed to be the character/root/primitive-conductor expression for eta_mn, which could drop conductor or become principal. The coprime mask is applied FIRST and is exact. Gcd inversion is then performed on this masked form using the auxiliary product extension; all full divisors are kept so the unwanted overlaps/self-pairs cancel. Only afterward are its positive subsequence norms bounded. No diagonal eta calibration or principal Poisson/residue term has been introduced. Beta_da is a specified column phase; no multiplicativity of beta is needed. The row kernel used below is the RAW finite-order R_a, after the common source-class factors have cancelled. We do NOT assert that the primitive good-conductor xi_a itself has order6. If one instead writes the positive residual norm with xi_a(z), its fixed residual class C_a=C[d]^(-1) gives xi_a(z)=tilde_chi_a(z)/psi_Ca(z); divide out that COMMON UNITARY ROW phase first. In particular

    xi_a(s^6)=psi_Ca(s)^(-6) 1_(a,s)=1,

not simply1_(a,s)=1. The common phase cancels in the positive norm. Sixth-power extraction in(4.2) is performed only after this conversion, or directly with raw R_a. Neither a finite-order claim for xi_a nor a general root normalization is required.

We may take absolute values in the sum over d and drop(d,z)=1 ONLY INSIDE EACH POSITIVE subsequence norm in(3.2). There is no assertion that the coprime-truncated original matrix is positive or dominated in operator order by the complete energy. There is no extra mu(q): the original signed coefficients were already in a_m.

## 4. The actual subsequence norm and positive sieve

The ternary assignment bound |A_U(m)|<=3^omega(m)<<_delta D^delta on the original annulus, uniformly in U, and Nm>=D give

    |a_da|<=B_W C_delta D^delta/sqrt(D).

There are at most4L ideals with Na<=2L whenever L>=1/2. Hence for every fixed modulation in(2.3),

    sum_a |a_da|^2 <<_epsilon B_W^2 D^epsilon/Nd.            (4.1)

This is the decisive 1/Nd norm. It uses no factorization of the cutoff or root phase, and is uniform in h,e,k,ell. The primitive S factors DO NOT break the positive norm: they are fixed-z-independent unitary column factors at this stage. They are not being declared a new finite-order row family.

The accepted positive arbitrary-COEFFICIENT raw all-ideal comparison is

    sum_{z good,Nz<=Z}|sum_{a good SF,Na in[L,2L]}
                                  b_a R_a(z)|^2
       <<_epsilon (ZL)^epsilon Phi(Z,L)sum_a|b_a|^2,
       Z,L>=1.                                             (4.2)

For completeness, the arbitrary-coefficient assertion follows DIRECTLY from the accepted external Theorem1.1, rather than an AU-specific proposition. Uniquely write the GOOD ideal z=r s^6 with r sixth-power-free and s arbitrary good, with overlaps allowed. At each FIXED s the raw identity is

    R_a(r s^6)=R_a(r) 1_(a,s)=1.

Freeze that actual zero mask in b_a^(s)=b_a 1_(a,s)=1. Both r and the SF columns a are sixth-power-free, and ||b^(s)||_2<=||b||_2. Zero-extend the columns to Na<=2L and apply Theorem1.1 at physical row length Z/(Ns)^6>=1. The sixth-free bound is

    F6(T,2L)<<T+L+T^(5/6)L^(1/3)+T^(1/3)L^(5/6).

Summing Ns<=Z^(1/6) gives exactly Z sum_s(Ns)^(-6), L times the COUNT of s, Z^(5/6)L^(1/3)sum_s(Ns)^(-5), and Z^(1/3)L^(5/6)sum_s(Ns)^(-2). Ideal counting and these convergent zeta sums give Phi(Z,L), with the common (ZL)^epsilon loss. There is NO restriction Z<=L: residual L may be far smaller than Z. No simplified H<=D envelope is used. The coefficients are arbitrary; their beta/xi/nu/W phases stay as COLUMN coefficients, not a new finite-order row family or inserted row-weight theorem. Applying the same estimate to conjugated R_a is just conjugation of the whole inner sum and its coefficients. The unit/principal dual rows remain in this raw positive majorant; no original principal residue is subtracted or assembled.

For1/2<=L<1 only the UNIT residual a can survive. Direct ideal counting gives energy<=2Z sum|b_a|^2. Since Phi(Z,L)>=Z, the same needed estimate follows directly, without invoking the theorem below length1. IfL<1/2 there is no residual column. Class/cop rime restrictions on the residual support only remove coefficients and may be retained as zeros in the positive comparison.

## 5. Summing d and S-supported h with their actual exponents

Combining(3.2),(4.1),(4.2), the d triangle costs

    B_W^2(DY)^epsilon
          sum_{Nd<=2D}(Nd)^(-1)Phi(Z,D/Nd).

The four terms are explicitly

    Z sum_(Nd<=2D)1/Nd,
    D Z^(1/6) sum_d1/(Nd)^2,
    D^(1/3) Z^(5/6) sum_d1/(Nd)^(4/3),
    D^(5/6) Z^(1/3) sum_d1/(Nd)^(11/6).

The first is <=(2+2log(2D))Z by ideal count; the others have absolutely convergent ideal sums (bounded, for example, by4,8,22/5). Therefore

    |T(a;Z)| << B_W^2(DY)^epsilon Phi(Z,D).                 (5.1)

These are joint-column bounds, not a per-conductor absolute completion.

Now h was FIRST fixed as a primitive S-column phase. Sum(5.1) with Z=Y/Nh over actual Nh<=Y, then enlarge positively to all S-supported h. Every Phi exponent of Z is POSITIVE:

    sum_h Phi(Y/Nh,D)
      <=Y prod_(p in S)(1-(Np)^(-1))^(-1)
        +D Y^(1/6)prod_(p in S)(1-(Np)^(-1/6))^(-1)
        +D^(1/3)Y^(5/6)prod_(p in S)(1-(Np)^(-5/6))^(-1)
        +D^(5/6)Y^(1/3)prod_(p in S)(1-(Np)^(-1/3))^(-1)
      <<_S Phi(Y,D).                                       (5.2)

There is no zero-exponent S sum, no hidden h-dependent norm or uniform-conductor hypothesis. Do not replace Phi here by a different sixth-free formula with a flat D term.

The e weights sum to the fixed finite product sum_{e|P_S}1/Ne. The k weights sum absolutely at exponent2. The ell triangle retains the exact Nell<=b cut; it is bounded by tau(v2), and the number of actual SF v2 in its block is O(A2). The original |g0(v2)|<=2C^(-1/2), and h_0 is bounded by fixed row-ray data. Multiplying these and the outer A1 proves(1.2), with divisor/log losses included in(D Y A2)^epsilon.

## 6. New quantitative partial consequence and its boundaries

At critical H=D^(3/4), Y=D^(3/8), Phi(Y,D) has powers

    3/8, 17/16, 31/48, 23/24,

so the leading power is17/16. Dividing(1.2) by D gives

    pure A1=D^(3/4), A2=1:          power13/16,
    mixed A1=D^(5/12), A2=D^(1/6): power31/48.               (6.1)

This improves a joint LOW-MODEL comparison, not the current whole-kernel13/12. The accepted window error certificate is target-sized forY<=sqrt(H). Thus on this SAME-class/rho1 component the actual finite-window bound combines(6.1) with that error: pure remains13/16; mixed is at most the target3/4 (up to epsilon/profile factors). This is only a representation-fixed finite-window partial form, not an energy statement or a bound on the complementary modes.

For a general normalized low-model target H, put R=A1A2 and Theta=H/R. The four terms of(R/D)Phi(Y,D) are at most H under the sufficient conditions

    Y<=min{D Theta, Theta^6, D^(4/5)Theta^(6/5),
                                D^(1/2)Theta^3}.            (6.2)

For the ACTUAL window rather than just its model, assume1<=H<=D and add Y<=sqrt(H): the accepted full-outer error is bounded by B_W^2(D A2)^epsilon[D sqrt(H)Y+H^2Y^2/D]<=constant*B_W^2(D A2)^epsilon D H. Thus the critical certificate used above is not silently extended to H>D. In the saturated power bookkeeping H~A1A2^2 with fixed Nu0 (or exactlyH=A1A2^2 forNu0=1), Theta~A2 and this is the proposed min of sqrt(H),A2^6,D A2,D^(4/5)A2^(6/5),D^(1/2)A2^3. The ACTUAL capacity remains b(v2) everywhere in the proof; no equality H=A1A2^2 is imposed on arbitrary blocks.

For the pure block A2=1, the norm majorant permits only bounded/subpowerY at target power once epsilon losses are allowed. This does not prove the actual pure partial form is large or that another signed estimate cannot improve it. The mixed block permits Y=D^(3/8) within these sufficient conditions.

The proof is unconditional relative to the already accepted external Theorem1.1 family application, and uses only the inherited same-class/rho1 root gauge. It does NOT assume general H_ROOT. Unequal source classes/general rho, the entire nonunit/S-supported complement, exact full-kernel target, principal/residue assembly and GRH remain open. Original AU/common complex W, all raw/deletion/S/ray/SF/capacity masks and equal-norm fibres have been retained, and no variance-only centering is used. No numeric control/data run, code/build/env/auth/public operation belongs to this result.
