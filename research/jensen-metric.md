# Coefficient-defined Jensen metrics: convergence and the missing positivity

Research heartbeat2026-11-02 (local date). This changes the approximation class after the certified S5 failure. Target: construct a symmetry-preserving arithmetic polynomial family and a positive metric without using unknown zeros. Result: an explicit convergence rate and coefficient-defined candidate metric; its required positivity remains unresolved. These are classical Jensen/Hermite constructions and elementary deductions, not a novelty claim or a GRH proof.

## Arithmetic family and an explicit compact error

Use the zeta xi function, xi(s)=s(s−1)pi^(−s/2)Gamma(s/2)zeta(s)/2, and define

    gamma(j)=j! xi^(2j)(1/2)/(2j)!,
    F(w)=sum_{j>=0} gamma(j)w^j/j!,
    Xi(t)=xi(1/2+it)=F(−t²).

Evenness of xi about1/2 makes F an entire function defined by its series; the square-root notation xi(1/2+sqrt(w)) is only a convenient equality and imposes no branch cut. The standard positive xi Fourier kernel gives gamma(j)>0. This accepted classical analytic input is not formalized here. Its precise convention is Romik1902.06330v3 Eq1.8–1.11: Xi(t)=integral_R Phi(u)exp(itu)du, Phi(u)=2sum_n(2pi²n⁴exp(9u/2)−3pi n²exp(5u/2))exp(−pi n²exp(2u)), and gamma(j)=j!/(2j)! integral_R u^(2j)Phi(u)du. Each summand is positive for u>=0; kernel evenness supplies positivity on the other half-line. Our gamma is1/8 of the sequence in GORZ Eq1, which uses8xi; this positive common factor does not change polynomial zeros.

Set J_d(x)=sum_{j=0}^d binom(d,j)gamma(j)x^j, Q_d(w)=J_d(w/d), P_d(t)=Q_d(−t²), d>=1. For any entire F with nonnegative gamma, not just xi, put w_dj=j!binom(d,j)/d^j for j<=d and0 otherwise. The product representation gives

    0<=w_dj<=1,
    1−w_dj <= j(j−1)/(2d).

For j<=d apply1−prod(1−a_k)<=sum a_k with a_k=k/d, k=0,...,j−1. For j>d, j(j−1)>=d(d+1)>=2d. Termwise absolute majorization therefore proves

    sup_{|w|<=R}|Q_d(w)−F(w)| <= R² F''(R)/(2d),
    sup_{|t|<=T}|P_d(t)−Xi(t)| <= T⁴ F''(T²)/(2d).

All series here converge absolutely. R=0 or T=0 gives zero error. This solves convergence for the specified family, without asserting its zeros are real.

## A metric determined entirely by coefficients

Divide J_d by its leading coefficient gamma(d) and write p(x)=x^d+a_(d−1)x^(d−1)+...+a0. Let C be multiplication by x on R[x]/(p) in basis1,x,...,x^(d−1): subdiagonal ones, last column−(a0,...,a_(d−1)). Newton sums m0=d and the Newton recurrence determine m1,...,m_(2d−2) from the coefficients. H_ij=m_(i+j) for0<=i,j<d. This is a Newton-sum Hermite matrix; it is not the moment matrix of the xi Fourier kernel. Multiplication in the quotient gives HC=C^T H, also visible from m_k=sum roots^k with multiplicity. The construction never needs root locations as input.

Hermite–Sylvester says H>=0 iff p has only real roots. H>0 iff all roots are real and simple. Strict positivity gives S=H^(1/2)(−C)H^(−1/2) real symmetric; since J_d has positive coefficients and nonzero constant term, its real roots are all strictly negative, so S>0. With

    K_d = [[0, sqrt(d S)], [sqrt(d S),0]],

the exact normalization is

    P_d(t)= (−1)^d gamma(d)/d^d * det(t I_(2d)−K_d).

Thus the arithmetic determinant/convergence bridge is explicit **conditional on proving H_d>0 for all d**, or another adequate unbounded sequence of levels. The semidefinite case still gives real zeros by the Hermite criterion, but H^(−1/2) is unavailable; do not silently use the displayed strict-metric construction there. For example gamma0=gamma1=gamma2=1 gives J2=(1+x)^2 and singular H=[[2,−2],[−2,2]].

The classical unshifted Jensen criterion makes H_d>=0 for every d equivalent to zeta RH. This is a precise restatement of the missing positivity, not an unconditional advance on RH. Known eventual hyperbolicity at each fixed degree as shift n grows does not settle the growing-degree, shift-zero family. No extension to all Dirichlet, Hecke, Dedekind or general Artin functions is supplied by this zeta-only construction.

## Attempted proof from a positive Fourier measure fails

The tempting step is to use positivity of a moment measure to infer positivity of H. It already fails at degree2. For J2=gamma0+2gamma1 x+gamma2 x², gamma2>0, put a=gamma0/gamma2,b=2gamma1/gamma2. Then

    H=[[2,−b],[−b,b²−2a]],
    HC=[[−b,b²−2a],[b²−2a,3ab−b³]],
    detH=b²−4a=4(gamma1²−gamma0gamma2)/gamma2²,
    v^T H v=2(v0−b v1/2)²+(b²−4a)v1²/2.

Positive moment Hankel matrices alone do not imply the required Turan inequality. Let a symmetric probability measure put9/10 at0 and1/20 at each of±1. It has F(w)=9/10+(1/10)cosh(sqrt(w)), gamma0=1,gamma1=1/20,gamma2=1/120. Its moment matrix[[1,1/10],[1/10,1/10]] is positive definite, but the Newton-sum metric is[[2,−12],[−12,−96]], with determinant−336 and negative value on e2.

This failure survives strictly positive smooth densities. Convolve that measure with a centered Gaussian of variance v>0. Its Fourier transform is exp(−v t²/2)[9/10+(1/10)cos t], an even entire function arising from a strictly positive even Schwartz density. Its first moments are mu2=v+1/10 and mu4=3v²+(3/5)v+1/10. The Jensen gap is exactly

    gamma1²−gamma0gamma2=(mu2/2)²−mu4/12=−7/1200

for every v. Therefore positivity, symmetry, smoothness and Gaussian decay do not supply the required Jensen metric. This is a counterexample to that general inference, not to the arithmetic xi function or RH. Arithmetic-specific inequalities stronger than ordinary moment positivity are necessary for this route.

## Verification and limits

JensenMetric.lean verifies the universal finite-product bound, real eigenvalues for an actual matrix with a positive symmetrizing metric, the actual quadratic companion/Hermite identities and positivity from its explicit discriminant inequality, and the Gaussian-mixture coefficient gap. It does not formalize the measure integrals, xi coefficients, compact-error summation, general Hermite criterion or full conditional determinant construction.

check_jensen_metric.py uses exact Fraction arithmetic for the Newton recurrence and HC symmetry. It certifies positive LDL pivots for the cosh model at degrees1through8, the negative mixture witness, the singular repeated-root example and finite checks of the coefficient bound. These are construction tests, **not actual xi coefficient enclosures** and not verification of universal positivity. Primary sources are pinned in planning/BIBLIOGRAPHY.md.

## Durable handoff

Attempt: obtain a positive spectral realization from symmetry-preserving arithmetic Jensen approximants. Surviving results: explicit compact error, root-independent coefficient metric and conditional exact determinant. Failed step: positive Fourier measure ⇒ positive Newton-sum metric, decisively refuted even for smooth positive Gaussian-mixture densities. Unresolved: arithmetic H_d>=0 for an unbounded range of unshifted degrees, an RH-equivalent condition; full formalization and non-zeta scopes remain open.

Next concrete work: derive and inspect an arithmetic expression for the first uncontrolled higher principal minor of H_d (beyond merely retesting known low degrees), with rigorous xi coefficient bounds, or switch to proving a specified short-row mean square in exponent-frontier.md. Do not infer the missing matrix positivity from the kernel's ordinary moment Hankel form or use fixed-degree/large-shift theorems to claim the needed degree-uniform result.
