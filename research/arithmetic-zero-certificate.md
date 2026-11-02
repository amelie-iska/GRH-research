# A certified off-line zero of an actual arithmetic approximant

Research heartbeat2026-11-02. Target: test the direct positive-pencil identity on a concrete arithmetic approximant rather than repeat an abstract spectral criterion.

The primitive nonprincipal character modulo3 has S5(s)=1−2^(−s)+4^(−s)−5^(−s). Exploratory deterministic double-precision Newton iteration located a possible zero near0.3372609735807354+11.027504200829364i. That floating-point search is not the certificate and is not used in the rigorous inequalities.

The exact certificate uses c=337261/10^6+i11027504/10^6 and r=1/10000. It proves |f(c)|<1e−6, |f′(c)|>1 and sup_D|f″|≤9. The disk's real parts lie in[337161,337361]/10^6, strictly inside(0,1/2). Rouché comparison with f′(c)(s−c) gives exactly one zero counted with multiplicity, hence a simple zero. The strict boundary margin is19791/200000000.

## Exact certificate mechanics

scripts/check_arithmetic_zero.py uses no floating-point operation or external package. It encloses log2,log4,log5 by60terms of 2sum_k y^(2k+1)/(2k+1), with y=(n−1)/(n+1), and the rational tail2y^121/[121(1−y²)]. Rational rounded logs ell_n have certified errors delta_n. Degree120 inclusive complex exponential sums have tail at most3^24*24^121/121!<1e−18 because |c ell_n|<24. Log perturbations cost at most2Cdelta_n, C=|Re c|+|Im c|<12. Derivative errors are at most delta_n+ell_n*exp_error. Exact Fraction comparisons establish the stated center and derivative bounds; positive real part on D and log2<1,log4,log5<2 give the second derivative bound9. Both paper editions state the theorem and the extended edition spells out every estimate.

## Scope and result

The conductor/gamma factor is holomorphic and nonvanishing on D, so the completed fifth partial sum has the same off-line zero. It therefore cannot equal a nowhere-zero holomorphic factor times the determinant of a fixed positive Hermitian pencil on this disk. This rejects a specific exact finite-level arithmetic/spectral identification. It does not refute GRH, the full L-function, arithmetic partial-sum convergence, later truncations, subsequences or modified approximants. No zero of the full L-function has been certified here.

An independent reviewer reproduced the bounds with a separate exact Fraction implementation and found no proof defect. The program certifies rational inequalities; the analytic error estimates and Rouché theorem are prose. lean-analytic/ArithmeticZeroDisk.lean verifies the actual complex disk location and rational comparison margin, not the full zero-existence inference.

## Handoff

The unmodified finite Dirichlet partial sums should not be assumed to carry the positive spectral structure term by term. A remaining route must modify the approximants and prove a uniform positive certificate, or pursue an independently arithmetic operator/mean-square argument. Next run should avoid simply rerunning this certificate or calling this finite off-line zero a GRH counterexample. Source clones, pinned tools and previous experiment records remain preserved.
