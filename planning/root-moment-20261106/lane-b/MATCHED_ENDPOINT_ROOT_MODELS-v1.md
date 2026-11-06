# Matched-endpoint root moments with a real-axis truncation certificate

Research-only candidate v1, 6 November2026. This is a quantitative reduction of the ACTUAL retained mean to its finite signed root moments. It is not a bound of those moments at the arithmetic target. The exact infinite Bessel hierarchy is already accepted; it is NOT claimed new here. New content is its matched-endpoint finite model for M_V, a real-axis factorial remainder WITHOUT an exponential I-majorant, and the target-small zeroth-model error on the declared pure low-Bessel scales. The leading root/column mean is retained and remains the missing arithmetic estimate.

No canonical, global ledger, source index, book, UI, release or environment file is edited. No old control, finite dataset, numerical exponent script, browser, build, dependency, auth or Lean operation is run.

## 1. Governing actual mean and notation

Read principal-mean HANDOFF-v1 (2b923adf), accepted aggregate-v2 (bbe4a216) and the accepted finite-endpoint note e23311fa. Keep all of their hypotheses: D>1,1<=U<=sqrt(D), original COMPLETE good SF ideal annulus D<=Nm<=2D, original coprime ordered m,n, actual A_U, fixed finite-order nu, one fixed possibly complex COMMON W, fixed S/ray/literal data, and fixed unit/S-supported u0 with no good support. Only original UNWEIGHTED two-pivot rows are asserted. A1,A2>=1, R=A1A2. No selected-column replacement, extra good frozen factor or arbitrary row weight is introduced.

Let tau fix every original outer parameter except k: all source pairs/rho with delta_(bar rho^6)=1, original m,n, actual v2,l,e, every S-supported h and GOOD sixth-free r. All primitive S zeros and total primitive eta/root/conductor are retained. Set

 F=Nf_S Nm Nn,  B_v=the ORIGINAL pre-S capacity endpoint b(v2),
 K_l=sqrt(B_v/Nl), Nl<=B_v,
 b_tau=min(2V,(X/(Nh Nr))^(1/6)),
 A_tau=A1 Nh Nr/(Nl Ne F),
 T_tau=S union supp(mn*v2),  chi_tau(k)=eta(k)^2.          (1.1)

Only b_tau>V contributes; an empty natural K_l<1 contributes0. A_tau is a scalar, NOT pivotA1. Physical Nr, not radical/conductor norm, is used; r may have valuations2..5. r/s overlap in y=h r s^6 stays allowed. The separate sixth-free indicator divisor a from the companion compensation note has deletion S union supp(mn), but it is not used here and must not be confused with original k or T_tau.

For real s>1 keep the actual FINITE signed coefficient

 Q_s^(T_tau)(K_l)
 =sum_(k SF,Nk<=K_l,(k,T_tau)=1) mu(k)chi_tau(k)/(Nk)^s.   (1.2)

The character stays eta(k)^2 for EVERY s. No new power/order/conductor is assigned when the norm exponent changes. Squaring or conductor drop restores no deleted prime; (k,v2)=1 and q raw zeros stay in the complete union. No Euler completion or k|s condition is used.

Use EXACTLY the normalized coefficient from the accepted endpoint note:

 d_tau=(1/D)c_m bar(c_n)R_m(v2^2)bar(R_n(v2^2))h_(ABrho)(v2)
  *mu(l)mu(e)eta(l e)epsilon(eta) A1/(Nl Ne sqrt(F))
  *bar(eta(h))bar(eta(r))delta_(bar rho^6) kappa_S g(mn).  (1.3)

Here c_m is the actual A_U(m)nu(m)R_m(u0)W(Nm/D). In particular no extra mu(mn) is inserted and neither A_U nor a root gauge is factored. eta(l e) at S is its ACTUAL primitive value, possibly0. All row/source/rho/capacity restrictions are in tau and h_(ABrho); every complex orientation/equal-norm mean remains. Optional original Nm!=Nn projection is imposed before this definition.

The accepted exact signed identity is

 mathcalM_V(X):=M_V(X)/D=sum_tau d_tau B_tau,
 B_tau=sum_(k as in1.2)mu(k)chi_tau(k)/(Nk)^2
                 integral_V^(b_tau) dotG_v2(A_tau t^6/(Nk)^2)dt. (1.4)

It is the ACTUAL F_V-E_V, already recombined. No fractional complete moment appears below. The real capacity G_v2 satisfies0<=G<=1, support[1/2,B0],B0=5/2, and is distinct from possibly complex column W. Put C=C0=3/(4pi^2) and M_j(v2)=integral G_v2(v)v^j dv; M_j<=B0^j M_0<=2B0^j.

## 2. A real-axis remainder, stronger than an absolute series tail

For every z>=0 and integer J>=0,

 |J0(2sqrt(z))-sum_(j=0)^J(-z)^j/(j!)^2|
                   <=z^(J+1)/((J+1)!)^2.                (2.1)

Proof: use J0(2sqrt(z))=(2pi)^(-1)integral cos(2sqrt(z)cos(theta))dtheta. Taylor's real-variable remainder through degree2J+1 is bounded by |2sqrt(z)cos(theta)|^(2J+2)/(2J+2)!. The angular moment is (2J+2)!/[4^(J+1)((J+1)!)^2], giving(2.1). The lower moments give precisely the displayed Bessel polynomial. This is an absolute REAL-AXIS remainder for every z, not a sign assertion about the error and not a complex-frequency bound.

Integrating(2.1) against the actual nonnegative G gives

 dotG(x)=C^(-1/2)sum_(j=0)^J(-x/C)^j M_j/(j!)^2+R_J(x),
 |R_J(x)|<=C^(-1/2)M_(J+1)(x/C)^(J+1)/((J+1)!)^2.       (2.2)

No growing derivative of the sharp nodal G occurs. The accepted hierarchy48de3f90/8197418d supplies the same infinite identity; the point here is the explicit finite REAL remainder without a factor I(B0x/C) or an exponential tail. This improvement controls model error, not arithmetic cancellation.

## 3. Exact finite signed root moments with BOTH endpoints

Define the actual matched endpoint moment

 W_j(V,b)=(b^(6j+1)-V^(6j+1))/(6j+1)=integral_V^b t^(6j)dt.

The order-J finite root model is

 L_(V,J)(X)=C^(-1/2)sum_(j=0)^J (-1)^j/[C^j(j!)^2]
       *sum_tau d_tau M_j(v2) A_tau^j W_j(V,b_tau)
                           Q_(2+2j)^(T_tau)(K_l).         (3.1)

All k sums and every outer set are FINITE. In particular W_j is not replaced by b^(6j+1)/(6j+1), an infinite moment, or a free lower endpoint. All signed/root/column means remain inside the inner sum in(3.1), before any conductor or positive-d triangle. This is not a PSD form.

The literal per-tau remainder is

 |B_tau-B_(tau,J)|
 <= C^(-1/2) M_(J+1)(v2) (A_tau/C)^(J+1)
    *W_(J+1)(V,b_tau)/((J+1)!)^2
    *sum_(k as in1.2)(Nk)^(-4-2J).                       (3.2)

Proof: apply the finite real Taylor identity BEFORE integrating t and summing the actual signed k coefficients; then take a triangle only for its certified remainder. The exponent4+2J is the original2 plus2(J+1), while chi remains eta^2. There is no infinite-height, infinite-dual or Euler interchange.

In particular the true leading joint root moment is explicitly

 L_(V,0)(X)=C^(-1/2)sum_tau d_tau M_0(v2)
                      (b_tau-V)Q_2^(T_tau)(K_l).          (3.3)

Unlike the fractional complete branch with Q_(5/3), (3.3) carries the actual interval length and does vanish at an empty interval. It includes ALL h/r modes and all roots/classes/rho, not merely the good dual unit. Nonzero G or Q2 yields no lower bound for this joint sum: d_tau can be0 or cancel and the other modes remain.

## 4. Actual global error certificate, uniform in model order

Set Lambda=A1 X/D^2 and Omega=B0 Lambda/C. On every original support point and V<=t<=b_tau,

 A_tau t^6<= A1 X/(Nl Ne F)<=Lambda.

The accepted all-ideal count gives sum(Nk)^(-4-2J)<=zeta_K(4+2J)<=8/3, uniformly in J and every moving deletion/character/conductor. Together with M_(J+1)<=B0^(J+1)M0 and W_(J+1)<= (b_tau-V)b_tau^(6J+6), (3.2) yields

 |B_tau-B_(tau,J)|
 <=(8/3) C^(-1/2)M0(v2)(b_tau-V)
                     *Omega^(J+1)/((J+1)!)^2.            (4.1)

This holds for every Omega>=0, not only when Omega<1. It is an upper error certificate, not an estimate of the signed polynomial itself.

Taking the triangle only AFTER retaining the joint model (3.1), the actual mean obeys

 |mathcalM_V(X)-L_(V,J)(X)|
 <<_(S,ray,epsilon) B^2(DXA2)^epsilon R X V^(-5)
                     *Omega^(J+1)/((J+1)!)^2.            (4.2)

The implicit constant is independent of J, the natural finite K, all primitive/local roots, and derivatives of G. To check it rather than promote a theorem to arbitrary row weights: use only actual |A_U|<=D^epsilon for the ERROR; the two complete annular column counts are O(D^2); A1/(D sqrt(F))<=A1/D^2 in(1.3); l/e/k have their original finite supports; l costs A2^epsilon, e fixed and v2 costs O(A2). Finally b_tau>V gives NhNr<X/V^6, and sum_h#r<=O_S(X/V^6) by sum_h1/Nh. Since b_tau-V<=V, this supplies R X/V^5. The same certification is valid after original unequal-norm projection. No arithmetic character norm or arbitrary row-weight extension is invoked, and no sign is removed from (3.1).

The bound (4.2) is beyond the earlier necessity estimate E_K≈H_GQ5/3: it approximates the ACTUAL recombined M, with both endpoints, by signed finite root moments. The previous exact hierarchy is an input; (4.2) is a model-reduction error, not a claimed new whole or principal-mean saving.

## 5. The zeroth model and the exact missing estimate

At J=0, (4.2) states

 |M_V(X)/D-L_(V,0)(X)|
 << B^2(DXA2)^epsilon R A1 D^(-2) X^2 V^(-5).             (5.1)

At the top V=X^(1/6)/2, X>=64,

 |M_top(X)/D-L_(V,0)(X)|
 << B^2(DXA2)^epsilon R A1 D^(-2) X^(7/6).               (5.2)

The harmless fixed B0/C and2^5 factors are in the constant. Here X/V^6=64, so(3.3) is the actual finite-frequency root moment, retaining nonunit S modes, full finite signed Q2, physical norms and original column/root data. It is not a completed Euler/zero-frequency replacement.

At pure A1=R=D^(3/4),X=D^(3/8), the existing absolute main budget is D^(13/16); the NEW zeroth-model ERROR has power -1/16 (up to the stated epsilon). Thus the actual mean is reduced, to target-small error, to the explicit genuine joint root moment(3.3). Nothing here bounds that moment by D^(3/4). The same reasoning makes the order-J error smaller by further powers of Lambda when Lambda is small, but extra model terms are still genuine signed root moments requiring arithmetic control.

For general declared parameters, a sufficient condition for this error ALONE to be at most the target scale H is

            R A1 D^(-2) X^2 V^(-5)<=H,                  (5.3)

up to the explicit subpower factor. This is not a target theorem for M or the original kernel. Under such a condition, a target bound for(3.3) would transfer to M. Conversely a target bound for M gives the same bound for(3.3) with the explicit additive error. This is the precise reduced arithmetic task, not a variance-only deletion of its mean.

Two separate comparisons prevent a false advance:

* The inherited fixed-s F6 and actual-band bound already control P_V, and the accepted mean comparison controls M with bound(R/D)V F6(X/V^6,D) plus its ray-count error. On mixed top bands the inherited actual-P certificate already reaches X<=D^(3/2); deriving a target-small polynomial-model error in that same range is not a new actual-sector improvement.
* Even if(3.3) were bounded at the pure target, the accepted P_V-M_V lattice/ray ERROR at the declared pure X=D^(3/8) has power37/48>3/4. The new Bessel model error -1/16 does not replace or cancel that different error. An actual P target still needs a joint treatment of it or another stronger argument, as well as the other original sectors. Whole signed13/12/global9/8 do not change.

The attempted signed step is therefore sharply located. Lambda occurs only in the certified higher-order remainder; it does NOT multiply the genuine leading moment. Replacing finite Q2/roots/d_tau by their norms simply recovers the finished R X/V5 main budget and loses the cancellation being sought. Known bounded diagonal/root/Schur transports and the old norm theorem supply no asserted power saving for(3.3). The finite mu(k) remains coupled to the same moving column characters and original K/union; there is no independent scalar cancellation factor to insert. A new arithmetic estimate of(3.3), or of the exact polynomial moments jointly, is still missing. This is a failed target route with a precise quantitative reduction, not an impossibility or an actual lower bound.

## 6. Scope and acceptance status

New survivor proposed for independent review: matched-endpoint actual root models (3.1),(3.3), global real-axis truncation certificate(4.2), and target-small leading reduction(5.2) on the declared pure scales. The exact infinite Taylor identity is inherited; no new sieve, Euler cancellation or whole power is claimed. All AU/commoncomplexW/fullunion/rawzeros/primitiveS/ray/source/capacity/orientation means remain. Empty K/G/endpoint cases remain exactly zero. No good frozen extras, arbitrary row weights, PSD or actual M/energy lower bound are asserted. Canonical/release/index/Lean/determinant/zero-location/GRH scopes remain unchanged.
