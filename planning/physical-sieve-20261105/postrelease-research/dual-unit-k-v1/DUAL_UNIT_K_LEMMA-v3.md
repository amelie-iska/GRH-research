# Uniform low-frequency recombination of the actual row square-divisor sum — v3

NEW postpublication step, authored after root reported Main 5d49a3e / Pages 504df4af and all 17 hosted hashes PASS. Start time: 2026-11-06 01:33:24 UTC. This note is separate from the preserved v8 failed norm-route attempt and excluded from the frozen release. It proves a component estimate with explicit errors, not a whole-kernel estimate, nonvanishing statement or target-power improvement.

## 1. Exact component and cutoff convention

Use the exact full primitive Poisson identity in `../dual-kernel-v1/DRAFT-v8.md`, SHA256 cba96d347cd880cdead3a330ce5e39969b1950c049df1750f6444ce68a0d4ff7. The primary source is de Faveri arXiv:2610.04045v1, Lemma 3.1 and transform (3.1); its PDF SHA256 is 97720b3cacccbedb9c2014520ad4d128ae23afd0a781bdeff27dab4e86b7c726. No earlier arithmetic table or inverse-L cutoff control is rerun.

Fix original coprime good SF annular columns m,n, q=mn, one actual SF second pivot v2, one divisor ell|v2, a fixed finite ray-character component rho, and an original S-removal divisor e|P_S. The ACTUAL application here is exactly the displayed remaining two-pivot pure/mixed block: v3=v4=v5=v6=O. The fixed u0 is a literal unit/S-supported factor and has NO good-prime support. Thus there is no additional (v1,v3v4v5)=1 mask hidden in u0. The fixed original ray projectors are those of v8 and have their modulus supported on the displayed S; no new good-prime ray exclusion is added. All finite ray coefficients have FIRST been expanded exactly, so the remaining k phase is multiplicative. Write eta for the primitive ray character inducing rho chi_m conjugate(chi_n), f its ACTUAL primitive conductor, F=Nf, and eps(eta) its primitive root number. The good conductor is q; its S part is retained. Never normalize a Gauss sum at a higher induced or physical modulus to a unit.

Set, as in v8,

    a=ceil(A1),
    b=b(v2)=min(ceil(2A1)-1, floor(H/(Nu0 Nv2^2))).

If b<a the entire row fibre is empty; set G=0 and its contribution is 0. For b>=a use the EXACT integer-node interpolant G=G_v2 from v8 (3.1). For the explicit amplitude constants below, FIX its auxiliary step to sigma(t)=exp(-1/t)/(exp(-1/t)+exp(-1/(1-t))) on 0<t<1, extended by 0 for t<=0 and 1 for t>=1. In particular 0<=sigma<=1 and 0<=G<=1. This fixes a concrete representative of the auxiliary row interpolant; it changes no original integer-node row weight or the common COLUMN profile W. The general complex-G moment theorem (4.2) does not need this amplitude hypothesis. If Nell>b, this ell term has no k and is 0; do not attach a nonzero Euler main term to it. Otherwise FIX the finite cutoff

    Kcut=sqrt(b/Nell) >=1.                                  (1.1)

This is the cutoff of the ORIGINAL row square-divisor expansion, before S-removal. It is not sqrt(b/(Nell Ne)). The factor e rescales the Poisson length afterward. One may remove further primal terms whose whole Poisson sums vanish, but that changes the separate dual-unit component: their unit modes need not vanish individually. This note uses exactly the pre-S-removal cutoff (1.1) and does not add any k beyond it. The approximation by an infinite Euler product below retains its full truncation error.

For the ACTUAL formula (1.3), T is exactly S union supp(q v2 ell), including the displayed original S-supported ray deletions. Here ell|v2, so its support is already included; it is displayed to make the union explicit. Do not replace T by only the primitive conductor of eta^2 after a possible power-conductor drop. The ANALYTIC k-lemma in Section 4 is uniform for any finite deletion set T, but that generality does not silently broaden the actual row identity. If extra frozen good factors v3,v4,v5 or other original good-prime row exclusions are introduced, their primal z masks must first be removed by their OWN finite inclusion-exclusion/rescalings (or by ell over the full exclusion radical). Merely adding them to the k deletion set T is insufficient. Such a broadened row identity is outside formula (1.3) here. Let h_rho denote the exact finite row-ray coefficient; it is outside the k sum. Original u0/nu/A_U/common complex W stay in c_m and conjugate(c_n). They do not depend on this ROW divisor k.

Put

    x=A1/(Nell Ne F),
    psi=eta^2,
    K_T(x,Kcut;G,eta)
       =sum_{Nk<=Kcut,(k,T)=1}
            mu(k) eta(k)^2/(Nk)^2 * dotG(x/(Nk)^2).           (1.2)

Squarefreeness of k is automatic from mu(k); it is ideal, not rational, squarefreeness. The phase is eta(k)^2, generally cubic at the good primes in this sextic setting, NOT 1. A fixed ray phase rho(k^2) is part of it. All k collisions with q and v2 are deleted, exactly as in v8.

For the GOOD dual unit (h=z=O), the fixed m,n,v2,ell,e,rho contribution to the actual numerator is LITERALLY

    c_m conjugate(c_n) R_m(v2^2) conjugate(R_n(v2^2))
      * mu(ell) mu(e) h_rho eta(ell) eta(e) eps(eta)
      * A1/(Nell Ne sqrt(F))
      * K_T(x,Kcut;G,eta).                                  (1.3)

This follows by substituting t=k^2 ell, L_e=A1/((Nk)^2 Nell Ne) in v8 (5.1). The prefactor L_e contributes (Nk)^-2; eta(t)=eta(k)^2 eta(ell). The raw second-pivot zeros, local eta(e) (possibly zero), primitive root, finite ray coefficient, mu(ell), mu(e), and all original column coefficients appear once. No sign is put in both column vectors. The formula is also valid in unequal column classes because (1.3) uses the actual primitive root number, not a same-class factorization assumed by analogy. For an inactive collision term all appropriate original zero prefactors remain zero.

## 2. The transform near zero needs moments, not derivative bounds

Let d=|D_K|=3 and C=d/(2pi)^2=3/(4pi^2). In this imaginary quadratic field the source transform is

    dotG(x)=C^(-1/2) integral_0^infinity
                      G(y) J0(2 sqrt(xy/C)) dy.              (2.1)

Indeed the Mellin transform of the angular-average kernel is

    integral_0^infinity J0(2 sqrt(u)) u^(s-1) du
         =Gamma(s)/Gamma(1-s),

initially in the safe ABSOLUTE strip 0<Re(s)<1/4. One explicit derivation uses the angular-average J0, its Laplace identity integral exp(-tu)J0(2sqrt(u))du=t^(-1)exp(-1/t), and u^(s-1)=Gamma(1-s)^(-1) integral t^(-s)exp(-tu)dt; absolute Fubini in that strip and t->1/t give the displayed Gamma ratio. Substitution into (2.1) gives exactly Ghat(1-s) Gamma(s)/Gamma(1-s) C^(s-1/2), the n=6/K=Q(omega) instance of the source's (3.1). Smooth compact support gives the same transform by Mellin inversion. No new large-sieve theorem or arithmetic hypothesis is being used.

For possibly COMPLEX G define

    M0=integral G(y)dy,               (signed/complex mean)
    Mhalf=integral sqrt(y)|G(y)|dy,
    M1=integral y|G(y)|dy,
    g0=C^(-1/2) M0=dotG(0).                                  (2.2)

The angular average definition J0(t)=(2pi)^-1 integral exp(i t cos(theta))dtheta gives

    |J0(t)-1| <= t^2/4,
    |J0(t)-1| <= |t|,                                        (2.3)

for real t. For the first inequality average 1-cos(t cos(theta))<=t^2 cos(theta)^2/2; the imaginary average vanishes and the average of cos^2 is 1/2. Consequently, for EVERY x>=0,

    |dotG(x)-g0|
      <= C^(-3/2) x M1,
    |dotG(x)-g0|
      <= 2 C^(-1) sqrt(x) Mhalf.                             (2.4)

These are absolute estimates. They remain valid if M0=0. There is no division by M0 or Ghat, no nonvanishing assertion and no derivative seminorm in the constants.

For comparison with a literal Fourier first moment, put H_G(w)=G(|w|^2) on R^2, with Fourier convention exp(-2pi i w dot xi). Then dotG(x)=(2/sqrt(d)) Hhat_G(xi) for |xi|=2 sqrt(x/d), and integral |w||H_G(w)|dw=pi Mhalf. The ordinary first-moment Fourier inequality gives the second bound in (2.4). Radial symmetry gives the sharper first bound, involving the first moment of the NORM y, M1. Thus both meanings of first moment are explicit.

For the actual nodal G_v2, 0<=G<=1 and supp(G) is contained in [1/2,5/2] when A1>=1. Hence

    |M0|<=2,  M1<=3,  Mhalf<=2 sqrt(5/2),                    (2.5)

uniformly in A1, v2 and the sharp capacity location. Its derivatives can still cost A1^j. That cost is important for high frequencies and tails in the FULL kernel, but is absent from the genuine near-zero estimate (2.4). No fixed-smooth-uniformity assertion has been invented.

## 3. Explicit ideal-count and truncation constants

Let A_K(X) count all nonzero integral ideals of O=Z[omega] with norm<=X. For X>=1, each ideal is principal with six unit associates. Since

    N(a+b omega)=(a-b/2)^2+3b^2/4,

a bounding rectangle contains at most

    (4 sqrt(X/3)+1)(2 sqrt(X)+1)

lattice points. Dividing this overcount by 6, and using sqrt(X)<=X and 1<=X, gives

    A_K(X) <= (2/sqrt(3)+1/2)X < 2X.                         (3.1)

Counting the zero lattice point in the rectangle only enlarges the bound; it is NOT an ideal being added. For 0<X<1 the ideal count is 0. Layer-cake/Stieltjes integration therefore gives

    sum_{Nk>Kcut} (Nk)^-2 <= 4/Kcut,                         (3.2)
    zeta_K(3)<=3,            zeta_K(4)<=8/3.                 (3.3)

For example sum n^-sigma =sigma integral A_K(t)t^(-sigma-1)dt <=2sigma/(sigma-1). All restricted/squarefree sums are dominated by these counts. No constant in (3.1)--(3.3) depends on the conductor, the finite deletion set, a ray class or the character.

## 4. Uniform actual-k lemma at s=2

Define the absolutely convergent DELETED Euler product

    E_T(2,eta^2)
      =sum_{(k,T)=1} mu(k) eta(k)^2/(Nk)^2
      =product_{p notin T}(1-eta(p)^2/(Np)^2).                (4.1)

The exponent 2 here is the absolutely convergent k-Dirichlet-series exponent. It is NOT a claim about the Mellin contour sigma in v8 (5.4), and is NOT a new assertion about an A_U inverse-L series. The variable T is kept in full. Equality follows first for finite prime sets and then by absolute convergence, dominated by zeta_K(2). It is valid uniformly for arbitrary finite conductor and arbitrary finite T containing its forbidden support.

For the fixed finite component (1.2),

    K_T(x,Kcut;G,eta)=g0 E_T(2,eta^2)+Err,

    |Err| <= 4 |g0|/Kcut
          +min( (8/3) C^(-3/2) x M1,
                 6 C^(-1) sqrt(x) Mhalf ).                  (4.2)

Proof: subtract g0 from each retained transform value and apply (2.4). Its sharper error is bounded by C^(-3/2) x M1 sum (Nk)^-4 <=(8/3) C^(-3/2) x M1; its first-Fourier-moment error is bounded by 2 C^(-1) sqrt(x) Mhalf sum (Nk)^-3 <=6 C^(-1) sqrt(x) Mhalf. Complete only the constant g0 sum to (4.1); its missing tail is at most |g0| times (3.2). This retains the finite-k convention exactly. All estimates are absolute and uniform in eta,T,q,v2,ell,e except through the explicit x,Kcut,moments.

For the actual nonempty nodal fibre, one convenient wholly explicit consequence is

    |Err| <= 8 C^(-1/2)/Kcut +8 C^(-3/2) x.                  (4.3)

The signed mean M0 itself must still be used in the main term. Replacing it by its absolute value changes the asserted approximation for complex G.

At the displayed critical pure block Kcut is of scale sqrt(A1) and x<=A1/D^2. In the mixed block the truncation is uniform for each actual ell with Nell<=b; in particular ell|v2 gives Kcut>=sqrt(a/Nell)>=sqrt(A1/Nell). These statements concern the explicit errors only. No power bound for the full m,n or ell sum follows just from their smallness. Full f_S and capacity constants remain in x and b, not in an unexplained implied conductor-uniform constant.

## 5. What this proves, and what it does not

The k-Mobius cancellation route DOES work for this chosen inner low-frequency component: the absolute k triangle can be replaced by a mean times (4.1) and the errors (4.2), despite growing derivatives of the exact sharp-row interpolant. The reason it works here is specific: k is a square divisor of the ROW, and the original A_U(m), nu(m), common complex W and primitive root are fixed outside its sum. This is different from a column-divisor sum with an unfactored k-dependent A_U(km).

The remaining main factor E_T(2,eta^2) is orientation-, conductor- and deletion-dependent. It is not a universal scalar and has not been removed from the m,n sum. The complete original mu(q) signs already inside c_m conjugate(c_n), mu(ell), local eta(e), finite ray coefficient, root number and all original raw collision zeros in (1.3) remain. Equal-norm prime ideals are never merged. The original physical row norm/capacity is b(v2); it has not been replaced by a conductor radical.

All NONUNIT dual modes and all S-supported dual h components remain in the full v8 identity. This lemma does not discard them, estimate them by zero or establish a lower bound after their cancellation. In particular a nodal interpolant can have nonzero integral while the allowed integer norm nodes contain no ideal at all; the complete Poisson sum then cancels, even if its isolated unit mode does not. The representation-dependent cutoff convention in Section 1 is another reason why component nonvanishing is not an energy assertion.

If M0=0, the main term in (4.2) is exactly 0, and only the error statement survives. Even a nonzero M0 would say nothing by itself about the complete row form: outer signed/class/column sums and nonunit modes may cancel. No whole-kernel nonvanishing, positive arithmetic determinant, global energy lower bound, fixed-W obstruction, target-power saving, GRH or new sieve theorem is claimed. The actual joint estimate left open by v8 remains open.
