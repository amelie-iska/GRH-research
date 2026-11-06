# What a uniform prime-error squarefunction power would imply

Research-only conditional input audit, 5 November 2026. This is not a new zero-free theorem or a proof of the signed target. It identifies additional analytic content in one proposed sufficient scalar-error certificate. The actual coupled signed estimate may avoid this certificate altogether.

## Objects and exact hypothesis

Let K=Q(sqrt(-3)), O_K its Eisenstein order of integers, and S a fixed finite set of prime IDEALS. Count every prime ideal, including inert rational-square norms and distinct conjugate ideals of the same norm:
 pi_K^S(x)=#{p notin S:Np<=x}.
Set Li_2(x)=integral_2^x du/log u and E_S(x)=pi_K^S(x)-Li_2(x).
Changing the logarithmic integral normalization by a fixed constant does not affect the conclusion below for 0<alpha<1/2.

Define the logarithmic dyadic squarefunction
 d2(T)^2=integral_T^(2T) |E_S(t)|^2 t^(-3) dt.
Assume, EXPLICITLY HYPOTHETICALLY, that for every epsilon>0 there is a finite C_(epsilon,K,S) with
 d2(T)<=C_(epsilon,K,S) T^(-alpha+epsilon)
for ALL sufficiently large real T, where 0<alpha<1/2 is fixed. A finite range, finite table, selected sequence of T, or unknown conductor-dependent constants is not this hypothesis.

We use the standard meromorphic continuation and Euler product of zeta_K, not any zero-location assertion. In this specific field zeta_K(s)=zeta(s)L(s,chi_-3); the prerequisite is ordinary Riemann/primitive-Dirichlet continuation. No general Artin holomorphy, positivity, GRH, custom Lean axiom or new formalization is used.

## Lemma

The stated hypothetical squarefunction power implies
 zeta_K(s) != 0 whenever Re(s)>max(1-alpha,1/2), s!=1.          (1)

The point s=1 is the usual pole. In the current alpha-range max(1-alpha,1/2)=1-alpha. This is a STRICT zero-free region, not a statement about its boundary. Finite S deletion creates no zero with positive real part and is not a change to a varying-conductor family.

### Proof of the Mellin step

For Re(s)>1 set
 F_S(s)=integral_2^infty E_S(t)t^(-s-1)dt.
On [T,2T], with sigma=Re(s), Cauchy--Schwarz gives
 integral_T^(2T)|E_S(t)|t^(-sigma-1)dt
 <= d2(T) [integral_T^(2T)t^(1-2sigma)dt]^(1/2)
 <= C_sigma d2(T)T^(1-sigma).
The formula remains finite at sigma=1 by its logarithmic limit. Given a compact subset of sigma>1-alpha, choose epsilon less than its distance to the boundary. The dyadic bound is then a summable geometric series. It also remains summable after any fixed number of log(t) factors. Thus the SAME Mellin integral converges normally and defines a holomorphic F_S in sigma>1-alpha, with holomorphic derivatives. Its bounded initial interval is entire. No contour is shifted through zeros.

### Prime and prime-power steps

For sigma>1 the prime-ideal zeta sum P_S(s)=sum_(p notin S) (Np)^(-s) satisfies
 P_S(s)=s integral_2^infty pi_K^S(t)t^(-s-1)dt
       =L0(s)+s F_S(s),
where L0(s)=integral_2^infty t^(-s)/log(t)dt. Here Li_2(2)=0 and pi_K^S(2)=0 in this field; there is no omitted boundary atom. Direct differentiation gives
 L0'(s)=-2^(1-s)/(s-1).
We do not assert a single-valued continuation of L0 across s=1. Its derivative is the explicitly displayed meromorphic function, which suffices:
 -P_S'(s)=2^(1-s)/(s-1)-(s F_S(s))'.                          (2)

Let zeta_K^S(s)=zeta_K(s) product_(p in S)(1-(Np)^(-s)).
For sigma>1 its logarithmic derivative obeys
 -(zeta_K^S)'/zeta_K^S(s)=-P_S'(s)+H_S(s),
 H_S(s)=sum_(p notin S) sum_(k>=2) log(Np)(Np)^(-ks).          (3)
The higher-prime-power series is normally convergent in sigma>1/2: on compact subregions bound its geometric tail by a constant times sum_p log(Np)(Np)^(-2sigma), and dominate by the corresponding absolutely convergent ideal series. This includes inert prime ideals; they are not dropped as though only rational split primes existed.

Equations (2)--(3) give a meromorphic continuation of the logarithmic derivative into sigma>max(1-alpha,1/2), with its ONLY possible pole at s=1. The standard continuation of zeta_K^S and the identity theorem identify this with its actual logarithmic derivative. A zero at any other point would create a pole with nonzero integer residue, impossible there. Each omitted finite Euler factor can vanish only on sigma=0, so zeta_K and zeta_K^S have the same zeros in this region. This proves (1). A hypothetical exceptional real zero is not discarded: it too would be excluded if it lay in this strict region.

## Application to the proposed certificate, not to the actual target

The common-column signed-incidence route studies the ACTUAL joint f quadratic form and a prime-discrepancy Stieltjes error before taking a per-f triangle. The inherited positive operator majorant, not a measured energy lower bound, has critical exponents:
 pure A1=D^(3/4),A2=1: 5/6;
 mixed A1=D^(5/12),A2=D^(1/6): 7/9.
The target exponent is3/4 and U is comparable to D^(1/2). Independent scalar-error inputs of the following sizes would neutralize those dominant monomials (up to the stated arbitrarily small epsilon powers):
 pure d2(U) of size U^(-1/6+epsilon);
 mixed d2(U) of size U^(-1/18+epsilon).
Their ALL-SCALE versions would therefore imply, respectively,
 zeta_K zero-free in Re(s)>5/6;
 zeta_K zero-free in Re(s)>17/18.

These implications DO NOT prove such scalar estimates, exclude actual zeros, or show that either input is necessary for the true signed main. The row operator upper monomial may be very loose, and the coupled signed prime error may cancel without any independent power bound for d2. Endpoint E_S(U)Q(U) is also part of the exact Abel formula; a mean-square assumption alone has not bounded that pointwise term.

The pinned fixed-field PIT/zero-free input currently supplies no asserted fixed-strip power of this form. Its subpower discrepancy majorant cannot simply be renamed as one. The conclusion is a precise failed-input diagnosis for the scalar/squarefunction route: the required extra independent prime-error certificate carries zero-free content not furnished by the existing hypotheses. The next task is a genuinely coupled mean-retaining estimate exploiting the ACTUAL f/row/column/profile weights, or an honestly justified additional analytic theorem. Existing global7/6 and missing5/12 saving, all scope-specific determinant/zero-location obligations and actual analytic/category Lean remain open.
