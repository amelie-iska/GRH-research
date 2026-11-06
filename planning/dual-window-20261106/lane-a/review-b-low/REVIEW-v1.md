# Independent review of the new joint low-model estimate

PASS for NEW_LOW_MODEL_BOUND-v4.md, SHA256 de79e9639fee4b463ae16901459c3f5552434130b88daa9a8b7cfd7b61d97c5d. I read the complete v3 proof, the exact v3-to-v4 primitive-infinity-type qualification, and the accepted WINDOW_AND_COMPLEMENT-v2 definitions of the model and certified error. This review accepts a new quantitative joint bound for that precisely specified finite-window MODEL and its stated same-class actual-window consequence. It does not accept a new whole-kernel exponent.

## Exact model and root scope

Both columns are in ONE fixed source class C and the exact trivial rho component of the original finite ray expansion is used. The two-pivot family has v3=v4=v5=v6=O, u0 unit/S-supported and no hidden extra good factors. The inherited same-class/rho1 law gives F=Nm*Nn and epsilon(eta)=kappa_C beta_m conjugate(beta_n), with eta=xi_m conjugate(xi_n). No general class/rho H_ROOT is assumed. xi_m can have nontrivial fixed unitary infinity type; beta_m is not declared multiplicative, finite-order, or the earlier Jacobi Hecke character.

The stated P_low,C,1 is exactly accepted WINDOW(3.2) restricted to this component. It includes the completed E_T(2,eta^2), the finite S-removal factor E_S(1,eta), the capacity-truncated ell polynomial, g0(v2), and the S-COMPLETE dual ideal window. The original finite pre-e Kcut is not removed from the actual kernel: the accepted approximation error retains it separately. This distinction is essential.

Expanding E_T is absolutely justified at exponent2, with its full raw deletion union. Expanding e and ell is finite, and decomposing y=h*z is the unique S-supported/good split. All h<=Y are kept with their primitive phases. The displayed coefficient

    a_m=(c_m beta_m/sqrt(Nm))*R_m(v2^2)*chi_m(ell)*chi_m(k)^2
                                      *xi_m(e)*conjugate(xi_m(h))

has exactly the required product with conjugate(a_n). The k/ell/v2 zero sentinels survive, while S values use primitive xi, not forbidden original raw symbols. All signs and h0 stay once outside. g0 depends on the actual v2 capacity fibre and remains signed in the model; only its absolute uniform bound is used in this estimate. Original A_U, nu,u0 and the common complex W remain in c_m.

## Gcd inversion and primitive/raw conversion

The joint coprime mask is inserted first. The subsequent product extension to overlapping columns is auxiliary, not a primitive eta or root calibration there. Full divisor inversion then writes m=da,n=db, with a,b squarefree and coprime to d but NOT necessarily to each other. Full divisors, including d=m on self-pairs, are essential to the cancellation of the auxiliary overlaps.

On GOOD z, columns m,n of the same source class have common reciprocity/S factors, so their product kernel equals the raw R_m,R_n product. Multiplicativity in the squarefree ideal denominator, including its zero sentinel, gives

    conjugate(R_da(z))*R_db(z)
       =1_((d,z)=1) conjugate(R_a(z))*R_b(z).

This yields exactly the sum of positive residual energies with the signed mu(d) coefficients in(3.2). The residuals have common source class C[d]^-1. Primitive xi_da(e),xi_da(h), beta_da and A_U(da) remain UNFACTORED column coefficients; no multiplicativity of any of them is used. Absolute values are taken in d only after this identity, and (d,z) can be dropped only inside a positive energy. There is no order comparison between the indefinite original coprime slice and a full PSD energy.

V4 also makes the infinity guard explicit. The norm is written in RAW finite-order R_a. If instead expressed with xi_a(z), divide out the common residual-class unitary row phase psi_Ca(z)^-1 before sixth-power extraction. In particular xi_a(s^6)=psi_Ca(s)^-6 times the raw coprimality indicator, not just that indicator. The proof does not assert xi_a^6=1.

## Arbitrary-coefficient norm and sums

The actual ternary bound |A_U(m)|<=3^omega(m) is uniform in U. Since Nm>=D and the residual support has at most4D/Nd ideals, every frozen modulation satisfies sum_a|a_da|^2<=C_epsilon B_W^2 D^epsilon/Nd. The decisive 1/Nd is correct; replacing A_U(da) by an a-only cutoff would not be.

The arbitrary-coefficient ALL-good-ideal raw norm Phi(Z,L) is correctly derived directly from the already accepted external Theorem1.1 application, not inferred from an actual-vector residue-subtracted envelope. Write z=r*s^6 with r sixth-power-free and s arbitrary, overlaps allowed. At fixed s the identity R_a(r*s^6)=R_a(r)1_((a,s)=1) freezes a genuine column collision mask. The norm of that masked coefficient vector does not increase. Both remaining physical indices r and the SF a are sixth-power-free, so the pinned family theorem applies at lengths Z/(Ns)^6 and2L. Summing s gives the four terms Z, L*Z^(1/6), Z^(5/6)L^(1/3), Z^(1/3)L^(5/6), with weights -6/count/-5/-2. There is no Z<=L restriction. Conjugated R is handled by conjugating coefficients. This does not apply a generic conductor-family sieve or a weighted-row theorem.

For L in[1/2,1) only the unit residual survives and direct counting gives energy<=2Z times its coefficient norm, covered by Phi>=Z. No theorem is invoked below input length1. For L<1/2 no column survives.

After the coefficient norm, the d sums have exponents1,2,4/3,11/6. The first costs at most2+2log(2D); the other bounds4,8,22/5 follow from the accepted ideal count. Thus the joint inner form is bounded by B_W^2(DY)^epsilon Phi(Z,D). Fixing h first is valid because its primitive S factors are z-independent unitary column modulations. Every Z exponent of Phi is positive, so summing h<=Y and then enlarging the polynomial expression to the S-supported monoid gives finite fixed products at exponents1,1/6,5/6,1/3. No flat-D S sum or hidden conductor loss occurs.

Finally e has fixed finite l1 weight; k is absolutely summable at exponent2; ell stays capacity-truncated and its l1 norm is bounded by tau(v2); there are O(A2) actual v2. Together with |g0|<=2C^-1/2 and fixed finite h0, this proves

    |P_low,C,1(Y)| <= C B_W^2(DYA2)^epsilon A1*A2*Phi(Y,D).

The epsilon loss explicitly retains A2 as needed. These triangles occur in auxiliary expansions and d AFTER the coupled m,n form, not conductor-by-conductor completions or orientation centering.

## Quantitative partial consequence and boundaries

At Y=D^(3/8), Phi has exponents3/8,17/16,31/48,23/24. Dividing the numerator bound by D gives13/16 for pure(a,b)=(3/4,0) and31/48 for mixed(5/12,1/6). The accepted actual-window error is target-sized for Y<=sqrt(H) in the original critical range. Therefore this representation-fixed same-C/rho1 actual finite-window piece is bounded by13/16 in pure and by at most the target3/4 in mixed, up to the stated epsilon/profile factors. Its complementary modes and other class/ray components are not covered.

The four general sufficient model inequalities are algebraically correct with R=A1A2, Theta=H/R: Y<=D*Theta, Theta^6, D^(4/5)Theta^(6/5), D^(1/2)Theta^3. To transfer to the ACTUAL window, the additional H<=D and Y<=sqrt(H) conditions correctly control both error terms; the original exact b(v2) capacity is unchanged. Pure A2=1 gives a norm-majorant term H*Y^(1/6), so only bounded/subpower windows are certified at target power without another signed estimate. This is not a lower bound on the actual pure form.

No other finding remains. This is a genuine new partial joint estimate relative to the previously accepted pinned external sieve theorem; it neither reproves that preprint nor improves current full global9/8/scoped13/12. No H_ROOT, GRH, nonvanishing, energy lower bound, positivity/determinant bridge or principal-residue assembly follows. No numeric control, old table, compiler, build, browser, environment, auth or publication action was rerun, and no frozen source/index was edited.
