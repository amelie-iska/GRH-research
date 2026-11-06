# Honest BV--Mellin bounds for actual finite dual bands and prefixes

DRAFT v1 for independent review, 6 November 2026. New research only. This proves a proposed ACTUAL finite-window estimate using the exact sharp-capacity transform; it is not the earlier completed-Euler low model or its approximation error. The current full global9/8 and whole scoped signed13/12 bounds are unchanged.

## 1. Exact scope and input norm

Use the current handoff HANDOFF-v2.md (daa59cabbc6fb81ba3a120546a26699700b3123fa0b7a17de09a93acc64630cc), accepted v8 primitive Poisson identity (cba96d347cd880cdead3a330ce5e39969b1950c049df1750f6444ce68a0d4ff7), required two-pivot scope addendum5f576c22..., and bounded nodal interpolant from dual-unit v3abeee901.... The arbitrary-coefficient raw all-good-ideal norm is the accepted NEW_LOW_MODEL_BOUND-v4(4.2), derived there from the pinned de Faveri arXiv:2610.04045v1 Theorem1.1 on the actual family. These are reused inputs, not new audits.

Work over O=Z[omega], fixed original S/ray/source-family choices, fixed nu and ONE common possibly complex column W supported in[1,2]. D>1, A1,A2>=1. The columns are the COMPLETE original good squarefree ideal annulus D<=Nm<=2D, with distinct ideals kept as distinct coordinates, including conjugate/equal-norm ideals. The actual coefficient is

    c_m=A_U(m)nu(m)R_m(u0)W(Nm/D),
    A_U(m)=sum_(ab|m,(a,b)=1,Na,Nb<=U)mu(a)mu(b).

The original cutoff U is not rescaled or factored. The row family is ONLY the remaining two-pivot family v3=v4=v5=v6=O; u0 is a fixed literal unit/S-supported factor with no good-prime support. Original v1,v2 are squarefree/coprime with the actual dyadic restrictions and Nu0*Nv1*Nv2^2<=H. Extra good frozen factors require their own primal deletion/rescaling; that extension is not made here.

Fix ONE source class C on BOTH original columns and the EXACT rho=1 component of the finite row-ray expansion. Its scalar h0(C,C;v2) is retained and uniformly bounded by the fixed ray data. On original coprime columns the INHERITED same-class law gives

    eta_mn=xi_m conjugate(xi_n), F=Nm*Nn,
    epsilon(eta_mn)=kappa_C beta_m conjugate(beta_n).

No general class/rho H_ROOT is assumed. Primitive good-conductor xi_m may have nontrivial fixed unitary infinity type. Its S values below are column phases, not forbidden original raw symbols.

For fixed actual v2, let a=ceil(A1), b=min(ceil(2A1)-1,floor(H/(Nu0*Nv2^2))). If b<a this fibre is zero. For ell|v2 with Nell<=b keep EXACTLY K_ell=sqrt(b/Nell)>=1 BEFORE S removal. Other ell terms are zero. Let e|P_S be the finite original S-removal divisor. No k cutoff is completed or changed.

The actual row interpolant is

    G_v2(y)=step(4(A1*y-a+1/2))*step(4(b+1/2-A1*y)),

with the fixed bounded nondecreasing smooth step from accepted v3. It has compact support in[1/2,5/2], 0<=G<=1 and TV(G)<=2, uniformly in all capacity endpoints. It matches the original integer-norm row values exactly. It is not W. Higher derivatives can grow with A1 and will NOT be used here.

Write Phi(Z,L)=Z+L Z^(1/6)+Z^(5/6)L^(1/3)+Z^(1/3)L^(5/6). The accepted RAW norm is

    sum_(z good,Nz<=Z)|sum_(a SF good,Na in[L,2L]) u_a R_a(z)|^2
       <<_epsilon (ZL)^epsilon Phi(Z,L)sum_a|u_a|^2, Z,L>=1.  (LS)

It is an arbitrary-COLUMN-coefficient comparison, with all-ideal dual rows and physical ideal norms. It is not a residue-subtracted actual-vector bound, a generic primitive-conductor theorem, or an inserted weighted-row theorem. It follows by z=r*s^6 extraction with the actual collision mask on columns, with overlaps allowed. For1/2<=L<1 only the residual unit survives and the needed norm follows directly from ideal counting. No L<1 sieve is used. There is NO condition Z<=L.

## 2. Proposed quantitative results

Define P_C,1(Y,2Y] as the actual primitive-Poisson numerator with total dual IDEAL norm Y<Ny<=2Y, all S-supported factors included, with the original finite k cutoffs and the exact G. It is this representation-fixed part of P_D=D*S1AA, not a physical positive row energy. Define P_C,1(<=X) similarly by Ny<=X.

For every FIXED 0<sigma<1/2, every epsilon>0 and Y>=1,

    |P_C,1(Y,2Y]|/D
      <<_(sigma,epsilon,S,family,ray,nu)
        B_W^2 (DYA2)^epsilon A2 A1^(1-sigma)
                   D^(2sigma-1) Y^(-sigma) Phi(Y,D).          (1)

The same bound holds for any last partial interval (Y,X] with Y<X<=2Y. Constants depend on sigma, and are not asserted uniform as sigma tends to0 or1/2.

For FIXED 0<sigma<1/6, summing dyadic bands and retaining the dual UNIT separately gives, for every finite X>=1,

    |P_C,1(<=X)|/D
      <<_(sigma,epsilon,S,family,ray,nu)
        B_W^2 (DXA2)^epsilon A2 A1^(1-sigma)
                   D^(2sigma-1) X^(-sigma) Phi(X,D).          (2)

Consequently, for every eta>0 there is a constant depending only on eta and the stated fixed data such that

    |P_C,1(<=X)|/D
      <<_eta B_W^2(DXA2)^eta (A1*A2/D) Phi(X,D), X>=1.        (3)

This ACTUAL prefix estimate has NO low-model approximation condition X<=sqrt(H) and no Taylor entire-function factor. It never uses the contour sigma=0. All source and finite-cutoff hypotheses above remain in force.

## 3. Uniform Mellin integral of the exact BV profile

Put C0=3/(4*pi^2). The exact imaginary-quadratic source transform is

    dotG(X)=1/(2*pi*i) integral_(Re s=sigma)
          Ghat(1-s) gamma_K(s) X^(-s) ds,
    gamma_K(s)=C0^(s-1/2) Gamma(s)/Gamma(1-s).                (4)

Here the ACTUAL eta has trivial total infinity type; no functional equation for an individual non-finite-order xi_m is substituted. Define

    J_sigma=(1/(2*pi)) integral_R |gamma_K(s)|/|1-s| dt,
    s=sigma+i*t.

For fixed0<sigma<1/2, J_sigma is finite. Vertical Stirling gives

    |Gamma(s)/Gamma(1-s)|=|t|^(2sigma-1)(1+O_sigma(1/|t|)),

and the integrand is O_sigma((1+|t|)^(2sigma-2)); on bounded t the line avoids every pole. C0^(sigma-1/2) is the fixed field/discriminant factor. This uses only the classical Gamma-function asymptotic, not an arithmetic or zero-free hypothesis.

Integration by parts in the ordinary Mellin integral gives EXACTLY

    Ghat(1-s)=-(1/(1-s)) integral y^(1-s) dG(y).

There is no endpoint term. With B0=5/2,

    |Ghat(1-s)|<=2 B0^(1-sigma)/|1-s|,
    (1/(2*pi)) integral_R |Ghat(1-s)gamma_K(s)|dt
                       <=2 B0^(1-sigma) J_sigma.             (5)

Thus the required L1 norm is uniform in A1,v2,H and sharp-capacity location. It is the PRODUCT in(5) that is integrable; we do not assert a uniform L1 norm for Ghat alone. No higher derivative, nonzero mean, or division by Ghat is needed. Sigma stays strictly positive, so no Gamma pole is crossed and no dual-unit/residue term is discarded.

## 4. Exact finite Mellin expression and bilinear coefficient convention

For fixed v2,ell,e,k,h and s=sigma+i*t set

    b_m(s)=c_m beta_m R_m(v2^2) chi_m(ell)chi_m(k)^2
                    *xi_m(e)conjugate(xi_m(h))*(Nm)^(s-1/2). (6)

Only good source/raw symbols are used at ell,k; primitive xi values are used at S-supported e,h. All raw collision zeros remain. The coefficients c_m include the original common complex W. On the original coprime support, inserting(4) gives the exact finite expression: outer coefficients mu(ell)mu(e)h0 kappa_C, the factor

    Ghat(1-s)gamma_K(s)*(A1/(Nell*Ne))^(1-s),

the finite k sum with weight mu(k)/(Nk)^(2-2s), and the remaining sum

    sum_(h S-supported,Nh<=2Y)
     sum_(z good,Y<Nh*Nz<=2Y) (Nh*Nz)^(-s)
       sum_(m,n in C,(m,n)=1)
         b_m(s)conjugate(b_n(conjugate(s)))
                                  conjugate(chi_m(z))chi_n(z). (7)

K=K_ell is finite, and (k,Sv2)=1; collisions with m,n are in(6). Every sign occurs once. In particular the ell/e weights are (Nell*Ne)^(s-1), not their zero-frequency low-model weights. No completed Euler factor is inserted.

The second vector is b(conjugate(s)), not b(s). The product norm power is (Nm*Nn)^(s-1/2), so(7) is NOT a positive energy at nonreal s. All sums except the vertical integral are finite. The exact source Mellin identity may first be used at finite D,Y;(5) and the subsequent bounds justify its absolute integral uniformly in the displayed parameters.

## 5. Joint gcd inversion, Cauchy and actual subsequence norms

As in the accepted LOW proof, first keep the original coprime mask, then use an AUXILIARY individual-column product extension to perform exact ideal Mobius inversion. On an overlapping/self-pair this extension is not its actual primitive eta or root number. Full divisors are retained; their signed sum removes all those overlaps.

Write m=da,n=db, L=D/Nd. Residuals a,b are SF and coprime to d, but may overlap each other. They have the same residual source class C[d]^-1. On GOOD z, source multiplicativity with its raw zero gives the common chi_d factor and exact mask1_((d,z)=1). Primitive beta_da, A_U(da), nu(da), W(Nd*Na/D) and xi_da(e/h) remain UNFACTORED inside the two coefficient vectors. No index multiplicativity of beta or of primitive xi at S is used.

For each fixed h,d,k,ell,e,t, the inner sum has form

    sum_(z in actual window,(d,z)=1) (Nh*Nz)^(-s)
                          F_d(s,z)conjugate(F_d(conjugate(s),z)).

Since total Ny=Nh*Nz>Y, Cauchy gives at most

    Y^(-sigma) [sum_(Nz<=Z_h)|F_d(s,z)|^2]^(1/2)
                   [sum_(Nz<=Z_h)|F_d(conjugate(s),z)|^2]^(1/2),
    Z_h=2Y/Nh>=1  (Nh<=2Y).                                 (8)

The (d,z) and dyadic-window masks are enlarged ONLY within these positive norms. The complex row phase has modulus one. This is bilinear Cauchy, not a claim that(7) is positive.

The choice Z_h=2Y/Nh is important: for Nh>Y the good row can be the unit, but Z_h>=1. No below1 row-length sieve is invoked and no S-supported component is dropped. For residual columns L in[1/2,1), direct unit-column counting applies as in(LS).

The actual ternary bound |A_U(m)|<=3^omega(m)<<_delta D^delta and original Nm in[D,2D] imply, uniformly in t and every frozen modulation,

    sum_a |b_da(s)|^2,
    sum_a |b_da(conjugate(s))|^2
                    <<_epsilon B_W^2 D^(2sigma+epsilon)/Nd. (9)

Both norms have the same magnitude, despite their different Mellin phases. This is an ORIGINAL-annulus estimate, not A_U(a) at a changed cutoff. The common residual-class row phase converts the good-z kernel to the raw finite-order R_a norm before invoking(LS). Primitive xi_a itself is not assumed to have sixth order.

Apply(LS) to both norms in(8), then take the absolute d triangle. Exactly the same ideal-divisor sums as before give

    sum_(Nd<=2D) (Nd)^(-1) Phi(Z_h,D/Nd)
                         <<_epsilon D^epsilon Phi(Z_h,D),

from exponents1,2,4/3,11/6; the first is logarithmic. Therefore the joint m,n,h,d contribution is at most

    B_W^2(DY)^epsilon D^(2sigma)Y^(-sigma)
                      *sum_(h S-supported,Nh<=2Y)Phi(2Y/Nh,D).

Every Y exponent of Phi is positive, so the S-supported sum is bounded by a fixed S constant times Phi(Y,D), using the geometric products at exponents1,1/6,5/6,1/3. The primitive h values have already remained in the coefficient vectors; their norms are uniformly unitary. This is not a flat-D S sum or a new row family of order6.

## 6. Completing the dyadic estimate without changing the finite kernel

The exact finite k sum is bounded only AFTER the preceding joint estimate:

    sum_(Nk<=K,(k,Sv2)=1)|mu(k)|(Nk)^(-2+2sigma)
                                     <=zeta_K^S(2-2sigma)<infinity. (10)

This is a positive majorant; it does NOT complete the actual finite k expression to an Euler product. Its constant depends on sigma, and it is not asserted at sigma=1/2. The full union q/v2/S zeros are still the exact zeros of(6).

The e sum costs the fixed finite sum(N e)^(sigma-1). The ell sum keeps Nell<=b and is bounded by tau(v2) since sigma<1. Counting actual v2 costs O(A2); its divisor loss is retained in(DYA2)^epsilon. The outer amplitude from(7) is A1^(1-sigma), and normalization is exactly1/D. Finally use(5). These steps give(1), with no hidden A1 derivative power, no per-conductor completion, and no principal/residue assembly.

No additional cancellation of the signs mu(k) or of the prescribed A_U vector was found. The gain is a valid JOINT column bound and a uniform transform estimate for the actual sharp profile, not a new scalar-Mertens input or a positivity argument.

## 7. Prefixes, positive epsilon and actual intermediate control

The dual UNIT Ny=1 is retained separately. The same Mellin calculation with h=z=O and row prefix1 gives(1) with Y=1, Phi(1,D); alternatively its elementary bounded-Bessel estimate is available. It is not the zero ideal or a principal original row being dropped.

For0<sigma<1/6, every exponent alpha-sigma, alpha in{1,1/6,5/6,1/3}, is positive. Dyadically sum(1), allowing the last partial band, and add that unit term. Geometric sums are bounded by constants depending on sigma times X^(-sigma)Phi(X,D). This proves(2); all limits here are FINITE prefixes.

Given final eta>0, choose for example sigma=min(1/12,eta/4)>0, fixed independently of D,X,A1,A2. Invoke(2) with epsilon=eta/2. Because A1,X>=1,

    D^(2sigma) A1^(-sigma)X^(-sigma)<=D^(eta/2).

This proves(3), absorbing into(DXA2)^eta. The constant can grow as eta tends to0, as usual; it has no dependence on D through sigma. There is never a contour at sigma=0, no residue discarded, and no assertion of uniform constants at an endpoint.

For the original critical scales H=D^(3/4), with fixed feasible capacity constants suppressed, the ACTUAL normalized prefix powers from(3) are:

    prefix X=D^(3/8):  pure13/16, mixed31/48;
    prefix X=D:        pure11/12, mixed3/4.                  (11)

Here pure means(A1,A2)=(D^(3/4),1), mixed means(D^(5/12),D^(1/6)), always in the same-C/rho1 component. At X=D, Phi(D,D)<<D^(7/6). The mixed prefix is target-sized up to epsilon, not merely its low-model prediction plus an error; the pure prefix is still above target. These are honest finite-window estimates for the exact sharp-row representation. They are NOT current full-slice exponents or bounds on an original physical energy.

More generally let R=A1A2, Theta=H/R. Sufficient prefix-target conditions are

    X<=min{D*Theta,Theta^6,D^(4/5)Theta^(6/5),D^(1/2)Theta^3}. (12)

These are the four termwise comparisons of(R/D)Phi(X,D) with H. Unlike the earlier model-plus-error route, no X<=sqrt(H) approximation restriction is needed. Original nonempty capacity and fixed u0 bound A2 and X polynomially in D,H under(12), so epsilon factors can be renamed in(DH)^epsilon. Conditions are sufficient, never necessary. In the saturated pure block this norm certificate still permits only bounded/subpower target prefixes; it does not prove the actual pure form is large.

## 8. Precise open step and comparisons

The estimate is unconditional RELATIVE TO the already accepted pinned external sieve application and same-class root input. It does not adopt the proposed general H_ROOT or extend to unequal classes/general rho. Such an extension needs a separately proved exact root normalization and all finite gauges, not a generic family substitution.

All dual ideals, including S-supported factors and nonunit modes in the finite window, remain; no mean or equal-norm fibre is centered or merged. Finite k/capacity conventions are exact. The proof does not use high profile derivatives. The separate critical-half endpoint/logarithmic argument belongs to the root lane and is not claimed here.

The new norm bound grows with X through Phi and therefore gives no uniform estimate as X tends to infinity. In particular the high/intermediate complement beyond the certified mixed prefix and the other finite components still need a joint signed estimate. A small bound for the full original signed slice cannot be assigned to each of its dual windows by positivity; those windows may cancel. Conversely a target-sized prefix does not bound the full slice or provide a lower bound.

There is no contradiction with the earlier no-overlap absolute Mellin warning: the dual norm window HERE is finite. We never interchange the full infinite ideal Dirichlet sum on this small-positive contour. Actual fixed-D transform tails may be certified separately with their true derivative costs; those tails are not removed by(1)--(3).

Thus the surviving new result is the actual BV--Mellin dyadic/prefix estimate and its same-C/rho1 mixed intermediate control. No extra signed gain closes the full kernel. No principal/short assembly, determinant/zero-location bridge, positive energy lower bound, new sieve theorem, analytic/category Lean result or GRH conclusion follows. Current full global9/8 and scoped whole signed13/12 remain. No old controls/data, compiler, build, dependency, environment, auth, publication or frozen index was changed.
