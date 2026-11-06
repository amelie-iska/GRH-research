# Finite fractional Bessel moments and the signed endpoint obstruction

Research-only candidate v1, 6 November 2026. This is a new incomplete-moment calculation inside the accepted ACTUAL principal mean. It does not estimate that mean at target size. The surviving result is an exact finite-k signed decomposition and a quantitative endpoint-necessity theorem. The earlier lattice-count, unit-mode Euler, root-law and norm comparisons are inputs, not rerun controls or new conclusions.

The current public book/release and all canonical sources are unchanged. No data, numerical control, browser, dependency, authentication, compiler or publication operation is part of this attempt.

## 1. Actual scope and exact finite signed block

Use COHERENT_SIXTH_PART_RAY_MEAN-v1 (4315f8d2), the sharpen-v1 (972192ef), aggregate-v2 (3be411e2) and current handoff (3b393db8). Thus D>1, 1<=U<=sqrt(D), original complete good SF annular columns D<=Nm<=2D, original coprime ordered pairs, actual A_U, fixed finite-order nu, one fixed possibly complex common W, fixed S/ray/literal data, fixed unit/S-supported u0 with no good support, and original UNWEIGHTED two-pivot rows remain. Put B=||W||infinity, R=A1 A2, A1,A2>=1. The primitive total character eta, its conductor norm F=Nf_S Nm Nn, its root epsilon(eta), all original raw zeros and orientation means are unchanged. Individual xi need not have finite order.

Only principal psi=bar(rho)^6 branches contribute to the retained counting mean. Nonprincipal-psi means are zero by the accepted fixed-ray orthogonality, with no branch discarded from the original representation. The formulas below can equivalently retain delta_psi in every outer coefficient.

Fix all original outer data except k: component(A,B,rho), coprime SF m,n with q=mn, actual v2, l|v2 and e|P_S, S-supported h and GOOD sixth-free r with b>V. Write B_v for the ORIGINAL pre-S upper capacity b(v2), and keep EXACTLY

 K=sqrt(B_v/Nl),  Nl<=B_v,
 b=min(2V,(X/(Nh Nr))^(1/6)),
 A=A1 Nh Nr/(Nl Ne F),
 T=S union supp(q v2),       chi(k)=eta(k)^2 on (k,T)=1.       (1.1)

K is the original natural k cutoff. It is not recomputed from L_e, e, h, r, or a later dual truncation. Empty K<1 or b<=V has no term. All ideals in k are integral SF; ideals in r are sixth-free, not necessarily SF. Physical norms are used throughout. r/s overlap remains allowed in y=h r s^6.

On this actual support eta(k^2 l e)=chi(k)eta(l e), and eta(k^2)=0 at q collisions. Hence the actual finite-k block is exactly

 B_chi(A;V,b,K,T)
   =sum_(Nk<=K,(k,T)=1) mu(k)chi(k)/(Nk)^2
                integral_V^b dotG(A t^6/(Nk)^2)dt.         (1.2)

The original (k,v2)=1, S-goodness and q raw zeros give precisely T; no k|s, (k,s)=1 or new union mask is introduced. Primitive eta(l e), including every S zero after conductor drop, remains outside (1.2). This statement needs multiplicativity of the TOTAL primitive ideal character, not a raw S-symbol substitution or a factorization of A_U or beta.

For clarity, the exact coefficient multiplying (1.2) in M_V(X)/D is

 d_tau=(1/D)c_m bar(c_n)R_m(v2^2)bar(R_n(v2^2))h_(ABrho)(v2)
       *mu(l)mu(e)eta(l e)epsilon(eta) A1/(Nl Ne sqrt(F))
       *bar(eta(h))bar(eta(r)) delta_psi kappa_S g(q).       (1.3)

Thus M_V(X)/D=sum_tau d_tau B_chi. All source components, root/column phases, l/e signs, full q density and original masks occur BEFORE any triangle. Optional original unequal-norm projection is imposed in tau before this identity. No diagonal/overlap primitive extension is used.

## 2. The fractional moment and its finite endpoints

C=C0=3/(4pi^2), and G is the ACTUAL real capacity interpolant: 0<=G<=1, supported in[1/2,B0], B0=5/2. It is not W. Define M_j=integral G(v)v^j dv, so M_0<=2. The accepted Bessel transform is

 dotG(x)=C^(-1/2)integral G(v)J0(2sqrt(xv/C))dv.

The canonical Mellin formula (cbk primitive-Poisson proof) is absolutely justified at s=1/6, within0<Re(s)<1/4. It gives the strictly specified complete moment

 H_G=integral_0^infinity dotG(x)x^(-5/6)dx
    =C^(-1/3) Gamma(1/6)/Gamma(5/6) M_(-1/6).             (2.1)

This integral is genuinely convergent, not a contour value or a zero-mode assumption. For completeness the ordinary angular splitting also gives |J0(u)|<=3u^(-1/2): stationary arcs cost4h, while on two complementary intervals the boundary plus amplitude-derivative cost is at most8/(u sin h); take h=u^(-1/2), sin h>=2h/pi. The resulting constant(2/pi+2)<3 covers u>=4; |J0|<=1 covers smaller u. Therefore

 |dotG(x)|<=(3/sqrt(2))C^(-1/4) M_(-1/4)x^(-1/4),

so the integrand at infinity is O(x^(-13/12)), uniformly without derivatives of G. Near zero the bounded transform suffices. This merely supplies convergence for the new incomplete moment; no old ray or lattice estimate is rerun.

Set, for z>0,

 L_G(z)=integral_0^z dotG(x)x^(-5/6)dx,
 U_G(z)=integral_z^infinity dotG(x)x^(-5/6)dx.

Then H_G=L_G(z)+U_G(z), exactly, and

 |L_G(z)|<=6C^(-1/2)M_0 z^(1/6),
 |U_G(z)|<=18sqrt(2)C^(-1/4)M_(-1/4)z^(-1/12).           (2.2)

Substitution x=a t^6, for a>0, retains BOTH endpoints:

 integral_V^b dotG(a t^6)dt
   =a^(-1/6)/6 [H_G-L_G(aV^6)-U_G(ab^6)].               (2.3)

This is not the complete integral unless its endpoint terms have separately been controlled. Their arguments depend on the same k, conductor, e, h, r and physical capacity as the original block.

## 3. Exact finite-k decomposition; no free Euler completion

For s>1 define ONLY the finite sum

 Q_s^T(K)=sum_(Nk<=K,(k,T)=1) mu(k)chi(k)/(Nk)^s.

Define the signed finite endpoint sum

 E_K=sum_(Nk<=K,(k,T)=1) mu(k)chi(k)/(Nk)^(5/3)
       *[L_G(A V^6/(Nk)^2)+U_G(A b^6/(Nk)^2)].            (3.1)

Equations(1.2),(2.3) give the exact identity

 B_chi=A^(-1/6)/6 [H_G Q_(5/3)^T(K)-E_K].               (3.2)

Consequently the actual principal mean has the coherent decomposition

 M_V(X)/D=F_V(X)-E_V(X),
 F_V=sum_tau d_tau A_tau^(-1/6)H_G Q_(5/3)^T(K)/6,
 E_V=sum_tau d_tau A_tau^(-1/6)E_K/6.                    (3.3)

All sums in(3.1)--(3.3) are finite in the original representation. Each d_tau remains complex and signed; no per-conductor or positive-d triangle has occurred. The fractional moment changes the artificial complete-branch k exponent from2 to5/3. It does NOT change eta(k)^2, erase T, factor any original coefficient, remove primitive S zeros or make F_V a positive energy.

The usual absolutely convergent Euler identity at5/3 is an optional bookkeeping comparison, not a new analytic input or a saving. Using the accepted elementary all-ideal count A_K(t)<=2t for t>=1 gives, for K>=1,

 |Q_(5/3)^T(K)-1/L^T(5/3,chi)|<=5K^(-2/3),
 1/5<=|1/L^T(5/3,chi)|<=5.                              (3.4)

Indeed the tail is at most(5/3)integral_K^infinity2t*t^(-8/3)dt, and the Euler lower bound is prod_p(1-Np^(-5/3))>=1/5. This is uniform for the actual varying chi and FULL T because it stays in absolute convergence. chi may be induced after squaring; L^T here is defined by its actual good Euler values, not by a claimed unchanged primitive conductor. For K<1 the finite block is empty and this comparison is not applied.

If completion is used, the extra error in F_V is retained literally:

 |F_V-F_V,infinity|
 <=sum_tau |d_tau| A_tau^(-1/6)H_G *5K_tau^(-2/3)/6.       (3.5)

The natural cutoff depends on original B_v/Nl and cannot be replaced by an arbitrarily large parameter. Formula(3.5) does not address E_V at all. No completed Euler factor is asserted to be the actual finite mean.

## 4. A signed endpoint-necessity theorem

If M_0=0, the nonnegative continuous G is zero and all these blocks vanish; no nonvanishing is inferred. Suppose G is nonzero. Put

 c_H=C^(-1/3)Gamma(1/6)/Gamma(5/6),
 K_star=6 C^(-1/6) B0^(1/6) Gamma(5/6)/Gamma(1/6).

Then H_G>=c_H B0^(-1/6)M_0>0. For any0<z_l<=z_u,

 |L_G(z_l)+U_G(z_u)-H_G|
 <=6C^(-1/2)M_0(z_u^(1/6)-z_l^(1/6)).                   (4.1)

In particular the endpoint COMBINATION has modulus at least
 H_G[1-K_star z_u^(1/6)].
It is approximately H_G, not approximately zero, when the actual upper argument is small. This is a lower bound only for that endpoint combination.

More strongly, retaining all finite mu(k)chi(k) signs in (3.1),

 |E_K-H_G Q_(5/3)^T(K)|
 <=24 C^(-1/2)M_0 A^(1/6)(b-V).                         (4.2)

To prove it, insert(4.1) term by term ONLY in the error. Its endpoint difference is exactly A^(1/6)(b-V)/(Nk)^(1/3); the resulting sum is sum(Nk)^(-2)<=zeta_K(2)<=4. The main Q_(5/3)^T(K) is still signed. Thus(4.2) is a coherent finite-k approximation to the ENDPOINT term, not a variance-only estimate.

For K>=50^(3/2), (3.4) implies |Q_(5/3)^T(K)|>=1/10. If also

 K_star (A b^6)^(1/6)<=1/80,                            (4.3)

then (4.2) gives

 |E_K-H_G Q_(5/3)^T(K)|<=H_G/20,
 |E_K|>=H_G/20.                                        (4.4)

It also shows that E_K lies within one half of the modulus of the complete signed branch H_G Q_(5/3)^T(K). These statements are uniform in the full moving q/T and actual chi, and use no growing derivative of G. They concern a single fixed outer tuple with its complete finite-k sum. They are NOT lower bounds for B_chi, M_V, a row form or any energy: (3.2) shows precisely how the two branches cancel, and every remaining d_tau can vanish or cancel with other tuples.

On original support,
 A b^6<= A1 X/(Nl Ne F)<=A1X/D^2.
Hence at the declared critical pure scales with X=D^(3/8), this upper argument tends to zero as D^(-7/8). Wherever K is sufficiently large and G is nonzero, the endpoint correction is therefore necessarily comparable with the artificial full moment, uniformly over actual column pairs. This is a conditional-on-nonempty-component statement, not an asserted existence or nonzero full-family form. Empty fibre and small K cases stay exact rather than being filled with a completed mean.

There is a second endpoint guard independent of low-argument asymptotics: as b decreases to V, the actual integral tends to zero, whereas the complete-moment branch does not acquire the factor(b-V). At b=V the two endpoint terms add to H_G exactly. Original b<=V terms must remain excluded; they cannot be populated by an artificial fractional main.

## 5. Explicit actual bounds and the norm-only failed step

The existing all-ideal count, finite natural multiplicities and original coefficient bound apply only for certification of absolute errors here. Directly from(1.2),

 |B_chi|<=4C^(-1/2)M_0(b-V).                            (5.1)

This is the old absolute finite-k interval budget written as a consequence of the new exact signed decomposition, not a new saving. Summing it with the actual d_tau and retaining all original support until the final error triangle recovers the baseline

 |M_V(X)|/D << B^2(DXA2)^epsilon R X V^(-5),             (5.2)

as already allowed by the accepted mean note. It is included to distinguish an actual upper bound from the artificial branch sizes, not claimed as a new theorem.

Let Z=X/V^6. If Z<=1 the sector is empty; otherwise the artificial complete branch in(3.3) has the explicit uniform norm certificate

 |F_V(X)|
 << B^2(DXA2)^epsilon A1^(5/6) A2 D^(1/3) Z^(5/6).      (5.3)

Here L_e/sqrt(F) times A_tau^(-1/6) has exactly the column-conductor factor F^(-1/3), k exponent5/3 and l/e exponent5/6. The two column counts and ONE final /D give D^(1/3); sum Nr^(-1/6) up to Z/Nh is O((Z/Nh)^(5/6)); the h sum is again sum_(h S-supported)1/Nh. The finite l sum costs A2^epsilon, e is fixed, and k costs at most5. No raw mask is dropped in a signed identity; overcounts enter only this certificate. This proves also

 |E_V(X)| << B^2(DXA2)^epsilon
 [A1^(5/6)A2D^(1/3)Z^(5/6)+R X V^(-5)].                (5.4)

These are upper certificates and do not assert that either actual branch has that size. At V=X^(1/6)/2, Z=64, the artificial complete-branch norm budget has pure exponent23/24, versus the accepted actual baseline13/16. The ratio of these norm budgets is (D^2/(A1X))^(1/6), which grows in the low-Bessel regime. This comparison diagnoses loss from completing the fractional moment; it is NOT an actual arithmetic lower bound or an impossibility result. No old numerical/exponent control is rerun to make it.

The tempting failed uniform step is now exact: one cannot replace the finite integrated-s kernel by its complete1/6 moment times a reciprocal Euler factor with a negligible endpoint remainder. In the actual low-argument regime (4.2)--(4.4) give the opposite signed-k endpoint behavior. Estimating F_V alone, or noting nonvanishing of a Re(s)>1 Euler product, does not estimate F_V-E_V. A further arithmetic estimate must retain their joint cancellation across the ACTUAL roots, columns, r/h, finite k/l/e and orientation means. This attempt supplies no such target-sized joint inequality.

## 6. Status

New surviving statements: the exact incomplete fractional-moment representation (2.3),(3.2),(3.3), the derivative-free endpoint bounds, and the uniform finite-signed-k endpoint-necessity estimate(4.2)--(4.4), with exact original cutoffs and full deletion union. All principal/root/orientation means remain. Whole signed13/12/global9/8, target/short/principal assembly, determinant/zero-location, Lean and GRH obligations are unchanged. This candidate requires independent adversarial review before acceptance and stays outside the frozen release, canonical sources and UI.
