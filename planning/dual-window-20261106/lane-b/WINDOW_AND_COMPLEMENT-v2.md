# Actual finite dual windows, exact S-complement and uniform variation control

DRAFT v2 (v1 preserved; explicit general A2 dependence), new research after the verified physical-sieve release. The accepted dual-unit lemma is an input; this note proves its actual finite-window assembly, exact complement representation, and derivative-free variation bounds. It does NOT prove the remaining combined signed target. Every source/output here is new and outside canonical, UI, build, release and index paths.

## 1. Exact original conventions

Read the physical-sieve POST_RELEASE_HANDOFF (SHA256 2e193a69decd3b70921728dbcb5e3aca91fc7588125353d8382ef81e804b6076), DUAL_UNIT_K_LEMMA-v3 (abeee9010e2b500565ce857f930650c277999fecc2d6cc64b59e9b0ab1973744), the primitive-Poisson DRAFT-v8 (cba96d347cd880cdead3a330ce5e39969b1950c049df1750f6444ce68a0d4ff7), and required scope addendum (5f576c22742d894536c7e8a843d29e3117be9c1e3534d5a5415aa8e130b80b11).

The actual scope is ONLY the remaining original unweighted two-pivot block v3=v4=v5=v6=O, u0 literal unit/S-supported, with no good-prime support. All extra good frozen factors would require their primal inclusion-exclusion; adding them merely to T is insufficient. Keep original good squarefree annular IDEALS m,n (D<=Nm,Nn<=2D), coprime m,n and q=mn, all actual SF v2 in [A2,2A2), and the original sharp v1 interval/capacity. Distinct ideals with the same norm remain separate. Set

    c_m=A_U(m) nu(m) (u0/m)_6 W(Nm/D),
    A_U(m)=sum_{ab|m,(a,b)=1,Na,Nb<=U}mu(a)mu(b),
    a=ceil(A1), b=b(v2)=min(ceil(2A1)-1,floor(H/(Nu0 Nv2^2))).

W is ONE fixed possibly complex column profile. No A_U factorization or replacement is made. Every original mu(q) sign is already present in c_m conjugate(c_n) when the high-window identity is used; there is no extra mu(q). If b<a, G_v2=0 and the entire row fibre is empty.

Use the bounded nodal interpolant G=G_v2 fixed in the accepted v3, with the specific nondecreasing step 0<=sigma<=1. Its support is in [1/2,5/2], amplitude<=1, and it matches every original integer-norm boundary exactly. Its higher derivatives need NOT be uniform. Keep ell|v2 only when Nell<=b and fix K=K_ell=sqrt(b/Nell)>=1 BEFORE S-removal. No k beyond K is added; unit/nonunit dual components depend on that convention.

For each fixed source column-class pair and exact finite row-ray character rho, let h_rho be its full Fourier coefficient. Let eta be the ACTUAL primitive ray character inducing rho chi_m conjugate(chi_n), f its primitive conductor and F=Nf. Its good conductor is q; its S part and primitive root eps(eta) remain. The ray modulus is supported on the original S. Put

    T=S union supp(q v2 ell)=S union supp(q v2),
    C=3/(4pi^2), x_e=A1/(Nell Ne F), e|P_S,
    K_T(X;K)=sum_{Nk<=K,(k,T)=1}
                 mu(k) eta(k)^2/(Nk)^2 dotG(X/(Nk)^2),
    E_T=product_{p notin T}(1-eta(p)^2/(Np)^2),
    g0=C^(-1/2)integral G,
    M1=integral u|G(u)|du, Mhalf=integral sqrt(u)|G(u)|du.

The square eta(k)^2, generally cubic at good primes, is NOT replaced by 1. Keep the complete T even after any power-conductor drop. Primitive values eta(h) at S are NOT values of the original forbidden raw symbol there.

Write the outer factor with no hidden signs as

    B(m,n,v2,ell,e,rho)
     =c_m conjugate(c_n) R_m(v2^2) conjugate(R_n(v2^2))
       *mu(ell)mu(e)h_rho eta(ell)eta(e)eps(eta)
       *A1/(Nell Ne sqrt(F)).                               (1.1)

The full ORIGINAL numerator P_D=D*S1^AA is the finite outer sum of (1.1) times

    W_eta(x_e;K)=sum_{y integral nonzero}conjugate(eta(y))
                                          K_T(x_e Ny;K).     (1.2)

All primitive characters in (1.2) vanish at their conductor primes. This is the accepted exact Poisson representation, with the original k cutoff. For each fixed D the full dual sum converges rapidly after evaluating dotG; its constants can depend on the actual higher derivatives. No uniform tail is inferred from that fact.

## 2. Good and S-completed finite windows

For Y>=1 define actual IDEAL sums

    A_eta^S(Y)=sum_{z good,Nz<=Y}conjugate(eta(z)),
    A_eta(Y)=sum_{Ny<=Y}conjugate(eta(y)),
    W_good(Y;x)=sum_{z good,Nz<=Y}conjugate(eta(z))K_T(x Nz;K).

The accepted pointwise k lemma, summed only in its CERTIFICATION ERROR, gives

    W_good(Y;x)=g0 E_T A_eta^S(Y)+Err_good,

    |Err_good|<=8|g0|Y/K
          +min{(16/3)C^(-3/2)x M1 Y^2,
                 12C^(-1)sqrt(x) Mhalf Y^(3/2)}.             (2.1)

Indeed #ideals<=2Y, sum_{Nz<=Y}Nz<=2Y^2 and sum sqrt(Nz)<=2Y^(3/2). The signed complex mean, character and Euler factor stay in the main term. This does not center any orientation vector.

Every nonzero integral ideal has the UNIQUE factorization y=h z, with h supported on S and z good. For the S-COMPLETE finite window define

    W_all(Y;x)=sum_{h S-supported,Nh<=Y}conjugate(eta(h))
                         W_good(Y/Nh; x Nh).

A subwindow with Y/Nh<1 is empty. Its exact main and error are

    W_all(Y;x)=g0 E_T A_eta(Y)+Err_all,                       (2.2)

with the SAME bound (2.1). This follows by counting the unique full ideal y directly, not taking a separate coarse bound for each h. Thus no artificial log(H) or S-volume factor is introduced. All nontrivial S-supported dual phases and their zeros remain through eta(h).

For the exact finite cutoff 1<=Y<Z, the S-complete complement is

    R(Y,Z;x)=sum_{h S-supported,Nh<=Z}conjugate(eta(h))
          sum_{z good,Y<Nh Nz<=Z}conjugate(eta(z))K_T(x Nh Nz;K).
                                                                  (2.3)

Then (1.2)=W_all(Y;x)+lim_{Z->infinity}R(Y,Z;x), in the transform-evaluation order specified above. Alternatively, retaining ONLY the good window W_good leaves BOTH h=O,z>Y and EVERY h!=O component in the complement. It is wrong to call that latter complement just z>Y or to replace primitive S values by raw ones.

## 3. The complete signed low-frequency model

Substituting (2.2) into the actual outer sum gives a coherent model P_low(Y) and an error certificate. The finite Euler/truncated-divisor structure can be assembled BEFORE any per-conductor absolute value.

The primitive eta,F,h_rho and E_T are independent of ell,e (ell changes the finite cutoff and its errors, not the completed Euler main). Define

    E_S(1,eta)=sum_{e|P_S}mu(e)eta(e)/Ne
             =product_{p in S}(1-eta(p)/Np),
    Q_{v2,b}(eta)=sum_{ell|v2,Nell<=b}mu(ell)eta(ell)/Nell.   (3.1)

The model is exactly

    P_low(Y)=sum_{(m,n)=1,v2,rho}
       c_m conjugate(c_n)R_m(v2^2)conjugate(R_n(v2^2))
        *h_rho eps(eta) A1/sqrt(F)
        *g0(v2) E_T(2,eta^2) E_S(1,eta)
        *Q_{v2,b}(eta) A_eta(Y).                            (3.2)

All class pairs, finite ray coefficients and actual v2 remain. This preserves mu(ell)/mu(e) in their exact finite sums, all original coefficients/complex W, primitive root/local phases, orientation means and raw zeros. E_T is not a universal scalar. If Nv2<=b, Q is the finite product over p|v2 of (1-eta(p)/Np); otherwise its upper restriction is essential. A sufficient nonempty-fibre condition for this completion is A1>=2A2; no such condition is silently imposed in general.

## 4. Exact error certificate for the actual outer sum

Let L_c=sum_m|c_m|. Let R_ray bound the sum_rho|h_rho| uniformly in the finite original class data and v2 (it is fixed; the number of finite ray characters is a crude bound). Put

    S_j=sum_{e|P_S}(Ne)^(-j),
    J_j=sum_{v2 actual, b>=a}sum_{ell|v2,Nell<=b}(Nell)^(-j).

Using the quadratic-moment option in (2.1), |g0|<=2C^(-1/2), M1<=3, K>=sqrt(A1/Nell), F>=D^2, and ONLY an error triangle gives

    |Err_outer(Y)|
      <=16 C^(-1/2) R_ray S_1 L_c^2/D
                   *sqrt(A1) Y J_(1/2)
        +16 C^(-3/2) R_ray S_2 L_c^2/D^3
                   *A1^2 Y^2 J_2.                         (4.1)

There is no conductorwise absolute value in (3.2), only in its certified error. Positively enlarging zero prefactors or the m,n support in this ERROR bound is explicit. Actual deleted sets and phases in the prediction remain unchanged.

The original assignment bound |A_U(m)|<=3^omega(m), ideal counting and the divisor bound imply, for every epsilon>0,

    L_c^2 << B_W^2 D^(2+epsilon),
    J_j << A2(DA2)^epsilon for j>=0,

so

    |Err_outer(Y)| <<_(S,ray,nu,epsilon) B_W^2 (D A2)^epsilon
         [ D A2 sqrt(A1) Y +(A1^2 A2/D)Y^2 ].              (4.2)

This is a new finite-window approximation-error bound, NOT a bound on the signed model plus complement. The AU coefficient bound is uniform in U; no rough-coefficient +/-1 formula is used.

If a row fibre is nonempty, A1 A2^2<=H/Nu0. With H=D^(3/4), A1,A2>=1, it follows that the error is at most target numerator scale D H (up to epsilon/profile constants) for Y<=sqrt(H)=D^(3/8): the first term is <=D sqrt(H)Y and the second <=D^(-1)H^2Y^2<=D^(-1)H^3. This leaves (3.2) and the exact complement to estimate; it is not itself the desired h1 estimate.

For orientation-triangle comparison ONLY, (3.2) has bound <<B_W^2(D A2)^epsilon D A1 A2 Y using |E_T|<=zeta_K(2), bounded finite S/ray factors, and |A_eta(Y)|<=2Y. At Y=D^(3/8), that crude model has numerator power 17/8 pure and 47/24 mixed, both above target 7/4. Thus the available triangle does not finish this route. These are failed-upper-bound powers, never lower bounds on the actual signed model.

## 5. Uniform Bessel/Stieltjes variation without higher derivatives

For the actual G=sigma_left sigma_right, one edge is nondecreasing and the other nonincreasing, both between 0 and 1. Therefore

    V_0(G)=integral|dG|<=2,
    V_alpha(G)=integral u^alpha|dG(u)|<=2(5/2)^alpha (alpha>=0).
                                                                  (5.1)

This stays uniform even at the exact sharp-capacity endpoint or a single permitted integer norm node. No claim about bounded higher derivative seminorms is made.

The recurrence d/du[sqrt(u)J1(2sqrt(Xu/C))]=sqrt(X/C)J0(2sqrt(Xu/C)) and compact support give the EXACT Stieltjes identity, for X>0,

    dotG(X)=-X^(-1/2)integral sqrt(u)J1(2sqrt(Xu/C))dG(u).    (5.2)

For real t>0, the angular-average formula implies

    |J1(t)|<=min{t/2,2/pi,6/(pi sqrt(t))}.                  (5.3)

For the third bound when t>=1, put phi=t^(-1/2). The stationary neighborhoods of angles 0,pi,2pi have total length 4phi, contributing at most 2phi/pi. On each intervening interval integrate exp(i t cos(theta)) cos(theta) by parts using cos(theta)/sin(theta)=cot(theta). The two intervals contribute at most 4cot(phi)/(pi t)<=4/(pi t phi). Sum to get 6/(pi sqrt(t)). For t<1, t/2 suffices. This elementary proof avoids an unpinned asymptotic constant.

Let

    A_G=C^(-1/2)integral|G|,
    B_G=(6/(pi sqrt(2))) C^(1/4)V_(1/4)(G),
    D_G=(2/pi)V_(1/2)(G).

Then, uniformly in A1 and the capacity position,

    |dotG(X)|<=min{A_G,D_G X^(-1/2),B_G X^(-3/4)}.          (5.4)

All constants depend only on the displayed amplitude/variation/support and the fixed field. For each actual G the higher-derivative bounds give still faster eventual decay, but those constants can grow with A1; they are not part of (5.4).

The finite actual k kernel obeys, for X>=1,

    |K_T(X;K)|
       <=min{4A_G,4B_G sqrt(K)X^(-3/4),
                        4(A_G+B_G)X^(-1/2)}.                (5.5)

The first two options hold for every X>0. Proof: zeta_K(2)<=4 and sum_{Nk<=K}(Nk)^(-1/2)<=4sqrt(K). For the last option split at Nk=sqrt(X), use the Bessel bound below and the amplitude bound above that threshold, with tail sum (Nk)^(-2)<=4/sqrt(X). This is a genuine uniform high-mode bound on the FINITE k kernel. It uses no cancellation of mu(k) and no arithmetic conductor hypothesis.

## 6. Exact finite complement before any conductor absolute value

For each fixed outer component and finite Y<Z, substitute (5.2) in (2.3). Because all sums are finite,

    R(Y,Z;x)=-x^(-1/2)integral sqrt(u)
       sum_{Nk<=K,(k,T)=1}mu(k)eta(k)^2/Nk
       sum_{Y<Ny<=Z}conjugate(eta(y))/sqrt(Ny)
            J1(2sqrt(x Ny u/C)/Nk) dG(u).                   (6.1)

The y sum is the exact S-complete primitive sum; equivalently split y=h z with the precise inequalities in (2.3). Good z is never confused with an S-supported h.

In the ACTUAL numerator, the prefactor has the useful exact simplification

    A1/(Nell Ne sqrt(F)) *x_e^(-1/2)
          =sqrt(A1/(Nell Ne)).                              (6.2)

Thus the conductor dependence is in the primitive root/character, deleted set and Bessel phase, not an overlooked amplitude factor. Equation (6.2) is an identity, not a power saving.

Define the coherent finite integrand J_v2(u;Y,Z) by summing INSIDE it all actual coprime m,n, all class/rho components, ell|v2 with Nell<=b, e|P_S and k<=K_ell, using

    c_m conjugate(c_n)R_m(v2^2)conjugate(R_n(v2^2))
      *mu(ell)mu(e)h_rho eta(ell)eta(e)eps(eta)
      *sqrt(A1/(Nell Ne))
      *mu(k)eta(k)^2/Nk
      *sum_{Y<Ny<=Z}conjugate(eta(y))/sqrt(Ny)
           J1(2sqrt(A1 u Ny/(C Nell Ne F))/Nk).              (6.3)

Every equal-norm fibre, root number, original coefficient and sign remains. The exact signed numerator complement is

    P_tail(Y,Z)=-sum_{v2}integral sqrt(u)J_v2(u;Y,Z)dG_v2(u). (6.4)

A legal mean-retaining variation bound is therefore

    |P_tail(Y,Z)|
       <=sum_{v2} V_(1/2)(G_v2)
                      sup_{u in[1/2,5/2]}|J_v2(u;Y,Z)|.     (6.5)

There is still NO per-conductor absolute Cauchy in (6.3)--(6.5). The finite ell/e/rho/k signs are combined before the variation bound. This identifies the actual joint Bessel-character estimate needed, rather than a generic positive tail. One can preserve even the v2 cancellation by leaving (6.4) as a single signed measure pairing; no such stronger bound is assumed.

The full complement is lim_{Z->infinity}P_tail(Y,Z), with finite integrals performed FIRST. A uniform bound on the finite integrands or justified limiting operator would be needed before moving an infinite series inside the Stieltjes integral. BV alone does not authorize that exchange.

## 7. Exact failed step and surviving result

The derivative-free bound (5.5) yields only, for example,

    |R(Y,Z;x)|<=32 B_G sqrt(K)x^(-3/4) Z^(1/4),              (7.1)

because sum_{Ny<=Z}(Ny)^(-3/4)<=8 Z^(1/4). It grows with Z and hence does not control the full infinite complement. The exponent-3/4 majorant is not absolutely summable over ideals (the Eisenstein lattice has linear ideal count; an inscribed rectangle gives A_K(X)>=X/18 for X>=12). This says the PARTICULAR uniform BV majorant cannot justify the infinite absolute interchange; it does NOT say the actual fixed-D smooth Poisson sum diverges.

The exact missing bounds are a signed estimate for the low model (3.2) TOGETHER WITH the coherent Bessel complement (6.4), or a sufficient bound on (6.3) uniform in Z with the actual capacity/primitive-conductor/Euler data. The available independent character/operator comparisons after per-conductor absolute values do not supply that signed estimate. No variance-only centering or zero-frequency deletion is allowed.

What survives as NEW proved work: actual good and S-complete window approximation (2.1)--(2.2), full signed root/Euler low model (3.2), uniform complete-outer error certificate (4.1), sharp-row BV and finite-k high-mode bounds (5.1)--(5.5), and exact coherent finite-complement representation (6.1)--(6.5). The attempt to finish the whole joint estimate by the derivative-free tail bound FAILS at (7.1). Root's separate higher-derivative/sharp-scale tail analysis is not assumed here and is not duplicated.

All nonunit and S-supported modes, the original common complex W, full union/ray/SF/capacity masks, original AU and every mean remain. No whole-kernel nonvanishing, lower bound, target-power saving, fixed-W counterexample, new sieve theorem, Lean or GRH claim is made. No old controls/tables, build, browser, dependency/auth or publication operation is part of this lane.
