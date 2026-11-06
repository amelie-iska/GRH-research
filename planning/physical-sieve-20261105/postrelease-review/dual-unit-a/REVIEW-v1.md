# Independent acceptance of the actual row-divisor low-frequency lemma

PASS, scoped to `DUAL_UNIT_K_LEMMA-v3.md`, SHA256 `abeee9010e2b500565ce857f930650c277999fecc2d6cc64b59e9b0ab1973744`. This is new postpublication research. It accepts a uniform approximation for one explicitly defined good dual-unit component, with both transform and finite-cutoff errors retained. It supplies no estimate of the whole dual kernel, nonvanishing, energy lower bound, or improved target exponent.

I read the complete v1 argument and exact preserved v1-to-v3 changes, rederived its formulas independently, and checked it against the accepted v8 primitive Poisson identity and pinned primary transform. No previous arithmetic table, nominal-power script, build, compiler, browser or publication check was rerun.

## Actual scope and exact normalization

The actual application is the displayed remaining pure/mixed two-pivot family: v3=v4=v5=v6=O, with fixed u0 supported only at the literal unit/S data. The complete original good squarefree annular columns, original A_U(m), fixed nu, one common complex column W, exact capacity, and raw second-pivot collision zeros remain. Ray projectors have fixed S-supported modulus and are expanded before the k sum. In particular the finite Fourier coefficient h_rho here means the coefficient before substituting t=k^2 ell; rho(k^2 ell) belongs in eta(t), not in a k-dependent coefficient silently pulled outside.

For fixed columns m,n, q=mn, actual v2, ell|v2, ray component rho and e|P_S, write eta for the primitive character inducing rho chi_m conjugate(chi_n), F=Nf and epsilon for its primitive root. Every good prime of q remains ramified; no physical-modulus square-root normalization is imported. Substituting L_e=A1/((Nk)^2 Nell Ne) into primitive Poisson at the GOOD dual unit gives exactly the author's (1.3): the outer coefficient contains c_m conjugate(c_n), both raw v2 factors, mu(ell)mu(e), h_rho, eta(ell)eta(e), epsilon, and A1/(Nell Ne sqrt(F)), each once. Inside is

    sum_(Nk<=K,(k,T)=1) mu(k) eta(k)^2/(Nk)^2 * dotG(x/(Nk)^2),
    x=A1/(Nell Ne F),  T=S union supp(q v2 ell).

The phase is eta^2, ordinarily cubic at good primes in this sextic setting; replacing it by one would lose the original weight. Primitive eta(e) may be zero and is retained. The raw column coefficients do not depend on this ROW square-divisor k; this argument does not factor an A_U(km) column coefficient.

The finite representation is fixed before removing S primes: a=ceil(A1), b=min(ceil(2A1)-1,floor(H/(Nu0 Nv2^2))), K=sqrt(b/Nell). If b<a or Nell>b, the specified contribution is zero and has no attached Euler main term. Otherwise K>=1. The extra e factor does not change this pre-e cutoff. Including larger k would add primal expressions identically zero but could alter their separated unit dual modes, with other modes canceling the change. Thus this cutoff convention is necessary to define the component being approximated.

The abstract analytic result permits arbitrary finite T, but this does not add missing original row masks. Extra fixed good factors would also require their primal z masks to be removed by finite inclusion-exclusion and the accompanying phases and rescalings. The actual formula here does not include that broader family.

## Transform and explicit constants

For C=3/(4 pi^2), the source Gamma factor gives

    dotG(x)=C^(-1/2) integral G(y) J0(2 sqrt(xy/C))dy.

The normalization can be checked without an arithmetic hypothesis. In the absolute strip 0<Re(s)<1/4, combine the Laplace identity integral exp(-tu)J0(2sqrt(u))du=t^(-1)exp(-1/t) with the Laplace expression for u^(s-1). Absolute Fubini and t->1/t give Gamma(s)/Gamma(1-s). Scaling the Mellin variable yields Ghat(1-s) C^(s-1/2) Gamma(s)/Gamma(1-s), exactly the pinned source transform. Smooth compact support then identifies the two inversions. This avoids an unproved small-positive-line interchange of the full arithmetic series.

The angular definition of J0 gives |J0(t)-1|<=t^2/4 and <=|t| for real t. Therefore, with g0=C^(-1/2) integral G, M1=integral y|G(y)| and Mhalf=integral sqrt(y)|G(y)|,

    |dotG(x)-g0| <= C^(-3/2) x M1,
    |dotG(x)-g0| <= 2 C^(-1) sqrt(x) Mhalf.

These hold for every x>=0 and complex G; no division by its mean occurs. The Fourier statement also checks: for H_G(w)=G(|w|^2), dotG(x)=(2/sqrt(3)) Hhat_G(xi), |xi|=2sqrt(x/3). Its ordinary spatial first moment is pi*Mhalf, giving the second bound with precisely the displayed constant.

The v3 explicit step has 0<=step<=1. Its actual nodal G therefore satisfies 0<=G<=1 with support in [1/2,5/2], so |integral G|<=2, M1<=3 and Mhalf<=2sqrt(5/2). Derivatives can still grow like A1^j; none is needed for this near-zero estimate. The amplitude qualification is essential for these convenient constants, while the general complex-G moment estimate remains valid without it.

The ideal count is independently checked. For each b with |b|<=2sqrt(X/3), there are at most 2sqrt(X)+1 possible integers a in the norm ellipse. Dividing the resulting overcount by six unit associates, including the harmless zero-lattice-point overcount, and using sqrt(X)<=X, gives

    A_K(X) <= (2/sqrt(3)+1/2)X < 2X  (X>=1).

Consequently the strict tail sum_(Nk>K)(Nk)^(-2) is at most 4/K. Layer-cake gives zeta_K(3)<=3 and zeta_K(4)<=8/3. These estimates count ideals, including distinct ideals of the same rational norm, and do not impose rational squarefreeness.

## The approximation and its limitations

At s=2 the deleted Euler series is absolutely convergent:

    E_T(2,eta^2)=product_(p notin T)(1-eta(p)^2/(Np)^2).

Subtract g0 from each retained transform value. The first transform bound is summed with (Nk)^(-4), the second with (Nk)^(-3). Complete only the constant g0 series to the infinite Euler product. This proves exactly

    K_T = g0 E_T(2,eta^2)+Err,
    |Err| <= 4|g0|/K
       + min{ (8/3) C^(-3/2) x M1,
              6 C^(-1) sqrt(x) Mhalf }.

Using the actual nodal moment bounds gives 8 C^(-1/2)/K+8 C^(-3/2)x. The bounds are uniform in conductor, finite deletion set and character, except for the displayed x, K and moments. The signed/complex mean remains in the main term, and the truncation error remains even when the Euler factor is completed. If the mean is zero, the main term is zero; no nonvanishing statement follows.

This is an absolutely convergent Euler recombination with quantitative component errors, not a new Mertens cancellation input. E_T depends on the orientation and deletion data and stays in the m,n sum. All other dual frequencies, all S-supported h!=O pieces, outer mu(ell), finite classes, roots, and original column weights remain. The isolated unit component already permits a row-count triangle estimate; the approximation does not produce a new target power. A nonzero auxiliary integral need not correspond to a nonempty ideal norm fibre, and cannot imply nonzero full energy.

All requested scope and amplitude clarifications are present in v3. No remaining blocker was found. The v8 full-kernel failed norm route and its acceptance remain separate; the current frozen release is unchanged. Companion receipts bind exact source bytes and verify all twelve protected HEAD/index states without mutation.
