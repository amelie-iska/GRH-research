# Rational cusp constants and an exact ramified angular Mellin transform

NEW research-only candidate v1,6 November2026. This derives the actual endpoint constants and a conservative transform from the KNOWN27 integral cusp expansions, not from assumed closure of an unconstructed ramified vector. It supplies a new general finite-character source interface with left cost R^(3/2+epsilon). Its source-to-ACTUAL finite-family match and normalization require independent review before any actual target statement. No current whole signed13/12/global9/8/GRH claim changes.

Primary inputs: Dunn--Radziwill2109.07463v3, Section5, theta modularity on Gamma2 with its weight-zero Kubota CHARACTER; the27 integral coset functions F_j=theta(gamma_j*w); exact constant/nonconstant expansions(5.15),(5.16), theta coefficients(5.7), and their Mellin Gamma factors(5.45). PDFdf888f8527b3647a3428d6677a3e3070aab7439f79f737f3e894218fb64cfef0; text636da1119ebebdcab6756e9258554af06a42d67baf0c47026c73e960de2f4767. No GRH-conditional prime theorem is used. K=Q(omega), O=Z[omega], lambda=1+2omega=i sqrt3, different(lambda). All project edits/checks SSH-Linux/owned paths only.

## 1. Known integral cusp data, not arbitrary new cusp assumptions

Write w=(z,v) in H3. The KNOWN source functions have
 F_j(z,v)=sigma_j v^(2/3)+F_j^*(z,v),
where sigma_j=sigma=3^(5/2)/2 for j<=9 and0 for j>=10.
The nonconstant terms have the stated discrete lambda^-4 O Fourier support and K_(1/3) Bessel expansion. Their angular derivatives decay exponentially as v tends to infinity; the absolute Dirichlet series of every fixed cusp coefficient family converges at real part>1, as already checked from the explicit tau/tau1/tau2 formulas. No unknown state is assigned this expansion.

For a rational translate a=A/C in K, choose A,C in O coprime, C!=0. This includes integral a by C=1. Since O is Euclidean, choose B,D with AD-BC=1, and set
 gamma_a=[[A,B],[C,D]] in SL2(O).
Choose its actual left coset gamma_a=delta_a*gamma_j, delta_a in Gamma2. The multiplier chi(delta_a) is the KNOWN Kubota value, a fixed modulus-one scalar independent of w; it is not an arbitrary phase nor a primitive S-Hecke value. No scalar is divided out. Different Bezout/coset choices give the same function by source automorphy.

Define U(x)=[[1,x],[0,1]] and W_C=[[0,-1/C],[C,0]]. EXACTLY,
 gamma_a^(-1) U(a)=U(-D/C) W_(-C).                      (1)
Indeed the matrix on the left is [[D,1/C],[-C,0]]. Therefore
 theta(U(a)w)=chi(delta_a) F_j(U(-D/C) W_(-C)w).         (2)
This is a genuine construction using known integral cosets, valid at full z,v; it is not inversion-of-a-translate by inspection.

## 2. Exact constants and what angular derivatives kill

The H3 action on the right has
 z'=-D/C - bar z/[C^2(|z|^2+v^2)],
 v'=v/[NC(|z|^2+v^2)].                                (3)
Hence at z=0, v'=1/(NC*v). Its pulled-back constant is exactly
 chi(delta_a)sigma_j (NC)^(-2/3)
               v^(2/3)(|z|^2+v^2)^(-2/3).             (4)
It is RADIAL in z. Pure partial_z^m or partial_barz^m at z=0 kills it for every m>=1. This is a verified property of(4), not a declaration that nonzero angular order eliminates poles in an unconstructed state.

At v small, the remaining derivatives are polynomial factors in v^(-1) times exp(-c/(NC*v)), because the known nonconstant cusp support is discrete with a positive shortest frequency. At v large the original theta translate has constant sigma v^(2/3), also z-independent and killed. Thus for each fixed rational a, the pure nonzero-angular derivative is exponentially small at BOTH ends.

For ell=0 the small-v constant DOES NOT disappear:
 theta(a,v)=c_a v^(-2/3)+exponentially small terms,
 c_a=chi(delta_a)sigma_j (NC)^(-2/3).                   (5)
For a finite combination H=sum_a c(a)theta(z+a,v), put
 C_infinity=sigma sum_a c(a),
 C_zero=sum_a c(a)chi(delta_a)sigma_(j(a))(NC_a)^(-2/3).
The regularized weight-v^(2s-2) Mellin transform has endpoint poles
 Res_(s=1/6)=-C_infinity/2,
 Res_(s=5/6)= C_zero/2.                                (6)
If the finite coefficient projector has sum c(a)=0, as below, only the second may remain. No assumption that a finite noncubic character forces C_zero=0 is made.

## 3. Exact nonzero-angular Mellin identity

For ell>0 let D_ell=(2pi i)^(-ell)partial_z^ell; for ell<0 use (2pi i)^(-|ell|)partial_barz^|ell|. Evaluating at z=0 and using(3), pure derivatives act through ONLY the opposite complex coordinate:
 D_ell[theta(z+a,v)]_(z=0)
 =chi(delta_a)(-1)^|ell| barC^(-2ell) v^(-2ell)
       D_(-ell)[F_j(z',v')]_(z'=-D/C), ell>0.           (7)
For ell<0 the corresponding C-conjugated formula is used. At formal barz=0, z' is constant, v' is constant and barz' is affine in z, so higher pure derivatives create NO hidden radial terms or lower angular orders.

Let
 Lambda_a(s,ell)=integral_0^infinity
     D_ell[theta(z+a,v)]_(z=0) v^(2s+|ell|-2) dv .
For ell!=0 it converges for EVERY complex s and defines an ENTIRE function by the endpoint bounds in Section2. Substitute y=1/(NC*v) in(7). The exact result, for either angular sign, is
 Lambda_a(s,ell)
 =chi(delta_a)(-1)^|ell|(C/barC)^ell (NC)^(1-2s)
                  Lambda_(j,-D/C)(1-s,-ell).           (8)
The dual Mellin is that of the KNOWN cusp F_j at the specified translate. Notice the essential exponent1-2s, NOT -2s. This factor includes the Jacobian and the v-weight. Its angular phase(C/barC)^ell has modulus one and is retained.

At Re(1-s)>1, the dual expression equals the usual source two-Gamma product times
 sum_mu d_j(-mu)e(Tr(-mu D/C))
                (mu/|mu|)^(-ell)/(Nmu)^(1-s).
Its ABSOLUTE norm is the fixed cusp coefficient norm, independent of D/C since every translate phase is unitary. No fixed/unknown translated cusp is assigned a norm by fiat: these are exactly the original d_j in the known27 expansions.

This proves the angular pole statement and the per-translate functional identity BEFORE any ramified finite-state closure claim. It does not prove a refined moving sqrtR norm.

## 4. The actual integral index and the primary branch

Fix a finite denominator character kappa on the PRIMARY SECTION, with arbitrary finite order. Separate its lambda part kappa_lambda (possibly trivial) and its away-lambda part kappa_0. Any needed fixed raw prime exclusions remain in the finite modulus and its imprimitive zero extension. Finite source/ray/Gamma product characters are treated componentwise; their total Fourier mass remains a fixed constant. A finite primary-section character may be extended to the fixed finite unit group; the result below depends only on its original primary values. No order-dividing-six assumption is made.

Take f>=2 containing the lambda conductor and define on O/lambda^f
 f_lambda(x)=kappa_lambda(x)*1_(x congruent1 modlambda^2),
with value zero at nonunits. This function is NOT replaced by kappa_lambda(lambda) or evaluated at lambda^4*mu.

On theta's entire support lambda^3*mu is integral. The projector f_lambda(lambda^3*mu) selects EXACTLY
 mu=lambda^-3*c*d^3, c,d congruent1mod3, c squarefree,
the source subset S. To check this from(5.7): every other valuation sector gives lambda|lambda^3*mu and is killed; the minus branch has lambda^3*mu congruent-1mod3 and is killed; the plus branch is1mod3. The source actual theta coefficient there is3^(5/2)gtilde(c)|d|. No unit-state parity argument is silently substituted for this primary selector.

Let t be the actual good squarefree cubic frequency and R=Nt, and let
 psi(x)=kappa_0(x)*overline(chi_(3,t)(x))
on the literal modulus M=F*t, F the fixed away-lambda modulus. This definition remains valid if t meets F, or psi is imprimitive. It does NOT evaluate or divide by kappa(t). The product modulus is only a valid period here, not a claim about primitive conductor. It retains all original fixed/moving zeros.

Define H_(kappa,t) by replacing the theta coefficient tau(mu) with
 tau(mu) f_lambda(lambda^3*mu) psi(lambda^3*mu).
The infinite constant is zero since f_lambda(0)=0. Initially Re(s)>1, coefficientwise cube completion gives
 D_H(s,ell)=3^(5/2+3s)i^ell
    L^(lambda*F*t)(3s-1/2,kappa^3 Theta_(3ell))
                 R_(kappa,t,ell)(s),                  (9)
where
 R_(kappa,t,ell)(s)=sum_(c primary SF)
   gtilde(c)kappa(c)overline(chi_(3,t)(c))
                Theta_ell(c)/(Nc)^s .
Here kappa includes every literal fixed-prime zero. In(9), the cube variable is prime to lambda,F,t and its character is EXACTLY kappa(d)^3 Theta_(3ell)(d). Conductor drop never restores a deleted prime. There is NO kappa(lambda) factor: the correct argument was lambda^3*mu=c*d^3. Source angleTheta_ell(lambda^-3)=i^ell supplies the displayed unit. The L factor is generally twisted, not assumed to be zeta.

## 5. Finite translates and a conservative moving-level bound

The perfect lambda trace pairing gives normalized Fourier coefficients b_h of f_lambda with
 sum|b_h|<=3^(f/2), and translations a_h=h*lambda^(2-f).
For the AWAY modulus M, use the primitive additive pairing e(Tr(xu/alpha_M)). It is perfect since(M,lambda)=1. For ANY psi bounded by1, not necessarily primitive, normalized finite Fourier inversion has coefficients q_u satisfying
 sum_(u modM)|q_u|<=sqrt(NM).                           (10)
This is Parseval and Cauchy, not unit Fourier-support or an implicit conductor reduction.

Consequently the exact function H_(kappa,t) is
 H_(kappa,t)(z,v)
 =sum_(h,u) b_h q_u theta(z+a_h+lambda^3*u/alpha_M,v).    (11)
All raw zeros are reconstructed by the FULL finite sum. Its total coefficient mass is O_fixed(sqrt R). Each translate is rational. After reducing its fraction to A/C, its denominator divides a fixed lambda-power times M, so
 1<=NC<=C_fixed R.                                    (12)
The integral cusp reduction(1)-(8) applies to EACH term, including zero/integral shifts. Thus the angular completed numerator in(9) is ENTIRE for ell!=0, including ramified kappa, because its actual finite sum of angular Mellins is entire. This is NOT inferred from noncubic kappa.

On s=-eta+i tau, apply(8), the known cusp absolute norm at1+eta and the source two-Gamma Stirling quotient. The total is bounded explicitly by
 (1+|tau|)^(2+4eta)
   sum_(h,u)|b_h q_u| (NC_(h,u))^(1+2eta)
 <<_fixed,ell,eta R^(3/2+2eta)(1+|tau|)^(2+4eta).       (13)
Fixed powers from3^(5/2+3s) do not alter R. This is an adequate COARSE left-side moving norm. No unproved Ramanujan cancellation, metaplectic multiplier evaluation, local primitive S root division or refined R^(1/2+epsilon) claim is used. The actual multiplier in every summand remains chi(delta_(h,u)); only its known unit magnitude is used AFTER writing the exact identity.

Equation(13) uses known cusp series term by term; it does not pretend that arbitrary rational translates are a closed finite vector with an unproved coefficient theorem. If a fixed-state matrix is desired, root/lane-A's separate rational identity can collect these exact terms. It is not a premise of(13).

## 6. Quantitative interface and still-required actual matching review

The right line of the cube-completed numerator is absolutely bounded, by the same theta/cube coefficient formulas, uniformly in t. With(13) and entire-ness, the ALREADY PROVED completed-convexity/sharp-Perron argument in twisted-gauss lane-c applies with left cost a=3/2. It is not rerun as a new experiment:
 |F_source(T;t,I)| <<_(fixedkappa,ell,epsilon)
 V1(W)(T Nt)^epsilon min[sqrt T,T^(1/4)(Nt)^(3/8)].     (14)
This now has an explicit ramified coefficient realization; it is not the old away3 theorem relabelled. Division by the actual L factor occurs ONLY where Re(3s-1/2)>1. No unknown zero or GRH premise is inserted. For ell=0 the actual residue(6) must instead be retained; this note makes no pole-free version of(14) then.

Applying(14) to the ACTUAL fixed family still requires the independent exact phase-family check: after removing the genuine angular ell=+1/-1, EVERY remaining own-column factor must be one of the fixed finite denominator characters/functions described above; all original nu/source/rho/ray/Gamma/e/w and primitive-S zeros must be in that finite family or kept as their actual outer coefficients. No densityg is present in the governing DIRECT model. The original nu is fixed finite-order, not assumed to have order dividing6; arbitrary infinity-type nu is a separate scope.

If that check passes, the previous exact full-deletion/prefix transfer with alpha3/4,beta3/8 gives the scoped pure localized BOTH-TypeI normalized power41/64. That is a CONSEQUENCE requiring independent gates, not an automatic current whole signed estimate. The complete signed/global scopes, all other components/assembly, independent determinant/zero-location bridges, separate arithmetic scopes, actual analytic/categoryLean and GRH remain OPEN. Current whole signed13/12/global9/8 and public333-page release are not changed by this candidate.

No accepted tail, convexity, finite table, source build, browser/auth/publication or old control is rerun. The new mathematics is(1)-(13): actual rational cusp constants/poles, exact nonzero-angular Mellin, correct integral-index primary projector/completion, and the conservative finite-translate bound.
