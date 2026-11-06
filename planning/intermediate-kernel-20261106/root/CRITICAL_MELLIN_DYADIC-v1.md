# Actual intermediate dyadic kernels on the critical Mellin line

Research-only root lane, 6 November 2026. NEW theorem: an actual sharp-capacity, finite-square-divisor dyadic kernel can be bounded on Re(s)=1/2 with only LOGARITHMIC interpolation and square-divisor costs. The previously accepted finite-window/Euler hierarchy and all-dual tail are INPUTS, not rerun. This is a joint same-source-class/rho=1 bound before conductorwise absolute completion; it is not the full signed target.

## 1. Exact inputs, scope and theorem

Use planning/dual-window-20261106/HANDOFF-v2.md (daa59cabbc6fb81ba3a120546a26699700b3123fa0b7a17de09a93acc64630cc), the original pre-Cauchy primitive identity DRAFT-v8 (cba96d34...) with scope addendum5f576c22..., and the accepted SHARP_ROW_DUAL_TAIL-v2 (bb2c8277...). Only the remaining original unweighted two-pivot block v3=v4=v5=v6=O, fixed u0 literal unit/S-supported with no good-prime support, is asserted. Keep every original ideal column in the annulus D<=Nm<=2D, original good/squarefree/ray/common-prime/full-union/capacity masks, actual AU, fixed nu/S and ONE common complex W. Equal-norm/conjugate ideals stay distinct.

Fix ONE source column class C and the exact rho=1 finite-ray coefficient. Only the inherited same-class root splitting is used:
 F=Nm*Nn, eps(eta)=eta_C beta_m conjugate(beta_n), eta=xi_m conjugate(xi_n).
No general H_ROOT is assumed. For each v2, a=ceil(A1), b=min(ceil(2A1)-1,floor(H/(Nu0 Nv2²))), and the original exact nodal function is
 G(y)=sigma(4(A1*y-a+1/2)) sigma(4(b+1/2-A1*y)).
Empty b<a is zero. The accepted sigmoid, not the original column W, has 0<=G<=1, support[1/2,5/2], TV(G)<=2, ||G''||1<=832 A1. For ell|v2 with Nell<=b use the ORIGINAL finite pre-S K_ell=sqrt(b/Nell); all other ell terms are zero.

For Y>=1 let P_C,1(Y,2Y] be the exact primitive-Poisson numerator restricted to ALL dual ideals y with Y<Ny<=2Y, with every S-supported h and good z (y=h*z) included. All finite k,ell,e,v2 signs and raw zeros remain; no Euler completion or low-frequency approximation is made.

For any epsilon>0,
 |P_C,1(Y,2Y]|/D
   <<_(S,family,ray,nu,epsilon)
       B_W² (D Y A2)^epsilon A2 sqrt(A1/Y) Phi(Y,D)
                    (1+log(2A1))²,                         (1.1)
 Phi(Y,D)=Y+D Y^(1/6)+Y^(5/6)D^(1/3)+Y^(1/3)D^(5/6).

The logarithms are displayed explicitly; without a stated polynomial A1/D relation they are not silently absorbed into D^epsilon. All row weights used in the classical input are the original unweighted positive comparisons. This theorem is an upper bound for an ACTUAL signed dyadic representation component; it makes no positivity, energy lower-bound or full-kernel assertion.

## 2. A new logarithmic Mellin cost for the actual interpolant

Put H(v)=exp(v/2)G(exp v), supported in [log(1/2),log(5/2)]. With Mellin convention Ghat(z)=integral G(y)y^(z-1)dy,
 Ghat(1/2-it)=integral H(v)exp(-itv)dv.
The accepted amplitude/variation/second-derivative estimates give
 ||H||1<=h0=2sqrt2,
 ||H'||1<=h1=sqrt2+2sqrt(5/2),
 ||H''||1<=h2*A1,
 h2=sqrt2/2+4sqrt(5/2)+832(5/2)^(3/2).
Indeed H'=exp(v/2)(G/2+yG') and
 H''=exp(v/2)(G/4+2yG'+y²G'').
Integrate these against dv=dy/y; every bound is a direct L1 estimate, not uniformity of higher derivatives.

Integration by parts in v, without boundary terms, gives
 |Ghat(1/2-it)|<=min{h0,h1/|t|,h2*A1/t²}.
Split |t| at1 and A1>=1. Therefore
 M(A1):=(1/(2pi))integral_R|Ghat(1/2-it)|dt
     <=[h0+h2+h1 log A1]/pi
     <<1+log(2A1).                                        (2.1)
For A1=1 the middle interval is empty. This uses the REAL A1 derivative cost only to cut off a harmonic integral; it does not erase it or claim a uniform fixed smooth profile.

In Q(omega), gamma_field(s)=C0^(s-1/2)Gamma(s)/Gamma(1-s), C0=3/(4pi²). At s=1/2+it it has EXACT modulus1, by conjugation of Gamma. Hence (2.1) is the full absolute vertical-integral cost. No Stirling-based power of A1, contour shift, pole crossing or reciprocal L-function is involved.

## 3. The exact finite dyadic Mellin kernel

For fixed k,ell,e,v2,C let L_e=A1/((Nk)² Nell Ne). Inserting Mellin inversion into the accepted primitive Poisson formula yields
 sum_h sum_(z good,Y<NhNz<=2Y) (1/(2pi i)) integral_(Re s=1/2)
   Ghat(1-s)gamma_field(s) L_e^(1-s)(Nh Nz)^(-s)
      sum_(m,n in C,(m,n)=1)
          b_m(s;e,h) conjugate(b_n(conjugate(s);e,h))
                     conjugate(chi_m(z))chi_n(z) ds,
times the exact OUTER mu(k)mu(ell)mu(e)h_0 eta_C ONCE. Here literally
 b_m(s;e,h)=c_m beta_m R_m(k² ell v2²)
               xi_m(e)conjugate(xi_m(h)) (Nm)^(s-1/2).
Primitive xi_m at S is legitimate and is not an invented raw symbol there. On good z, common same-class source factors cancel to the original raw row characters. Every k/ell/v2 collision remains a zero coefficient.

There are only finitely many h,z in a fixed dyadic window; k,ell,e,v2 are finite. The vertical integral is absolutely convergent by (2.1), so these finite interchanges are justified. The b_n argument is conjugate(s), not s. At nonzero t this is a bilinear pairing between two DIFFERENT phase-modulated vectors, not a PSD norm square.

At Re s=1/2, both vectors have the SAME pointwise magnitudes as c_m. Thus for m=da, L=D/Nd>=1/2,
 sum_a |b_da(s;e,h)|², sum_a |b_da(conjugate(s);e,h)|²
       << B_W² D^(1+epsilon)/Nd.                           (3.1)
No beta, cutoff or S phase is factored multiplicatively in d.

Insert exact gcd-Mobius inversion. For each d, use bilinear Cauchy in z after retaining its raw(d,z) mask and the lower dyadic endpoint; only INSIDE the two positive norms may this mask and the upper support be enlarged. The varying row phase (NhNz)^(-it) has modulus1. Its magnitude weight is <=Y^(-1/2).

For each h<=2Y use the positive row PREFIX Z_h=2Y/Nh>=1, NOT the lower lengthY/Nh. This avoids an unapproved row-sieve application below1. The accepted arbitrary-coefficient all-good-row Phi(Z_h,L) comparison applies; if column L<1, count the unit column directly. Exact d summation then gives
 joint kernel at fixed t,h
  << B_W² D^(1+epsilon)Y^(-1/2)Phi(2Y/Nh,D).
The constants are independent of t,k,e,h. Primitive S h/e phases are column modulations. Finite-class common row phases on good z cancel or are bounded by1 in the bilinear Cauchy; primitive xi is not assumed sixth-order.

Sum over the UNIQUE S-supported h. Each Phi monomial has a POSITIVE power of Z_h, so extending the positive monomial sum over all S-smooth h gives
 sum_h Phi(2Y/Nh,D)<<_S Phi(Y,D).
This does not restore an original forbidden S value and does not introduce a log(Y) S-volume factor.

## 4. Natural finite square-divisor cutoff: a logarithm, not zeta(1)

The remaining magnitude of L_e^(1-s) on this line is exactly
 sqrt(A1)/(Nk sqrt(Nell Ne)).
The original finite cutoff satisfies K_ell<=sqrt(2A1). Elementary ideal counting gives
 sum_(Nk<=K_ell)1/Nk<=2+2log K_ell<=2+log(2A1).             (4.1)
No infinite k-Euler series at exponent1 is introduced. In particular this proof does NOT contradict the previous disjoint absolute convergence domains for infinite k and infinite dual sums.

The finite e sum of Ne^-1/2 is a fixed S constant. The truncated ell sum of Nell^-1/2 is bounded by tau(v2), retaining its actual restriction before the error-only bound. The number of original v2 is O(A2), and its divisor loss remains (DYA2)^epsilon. Multiplying (3.1), the joint Phi bound, (2.1), (4.1), the sqrt(A1) prefactor and normalization1/D proves(1.1). Absolute values have been taken only after the actual joint m,n form and d-positive comparison, not by completing each conductor q=mn separately.

## 5. What the bound controls, and the exact failed completion

The unit dual ideal Ny=1 is deliberately NOT in a dyadic band(Y,2Y], Y>=1. It remains in the separate prefix and in the full primitive identity. This is support decomposition, not centering or deletion of a mean. Every nonunit, sixth-power and S-supported ideal in the band is retained. No original physical row has been added or removed.

For finite bands the derivative cost is logarithmic, and the k cutoff is kept exact. This is stronger than merely granting an imaginary uniformly smooth G to a nominal dual-length calculation. It does NOT give a summable whole-dual estimate: at largeY, Phi(Y,D) has termY, so the right side has a term proportional to sqrt(Y). The actual fixed-D transform still decays rapidly and has the independently accepted derivative-cost high tail. The missing bound is on the coherent intermediate/main sum, not on whether a finite Poisson representation exists.

This estimate can be combined as a MINIMUM of valid finite-block bounds with the new all-j/prefix estimate or other proved positive comparisons. Such a minimum is only a bound-monomial comparison, not measured energy or a lower bound. The current global9/8 and whole two-pivot signed13/12 remain unchanged. The theorem does not assume general H_ROOT, Artin holomorphy, GRH, desired positivity or any zero location, and supplies no new Lean/determinant conclusion.

Next actual research must exploit more of the prescribed AU/nu/fixedW arithmetic before norm-only Cauchy for the remaining intermediate range and other class/rho components. The proof above is a new actual dyadic bound and a precise limit of that uniform norm mechanism, not the missing complete signed saving.
