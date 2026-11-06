# Independent review: finite-cutoff Schur transfer

PASS for the exact root note FINITE_CUTOFF_SCHUR-v1.md, SHA256 f07d6228b1e192c07553f6af38c5ce8371c975f48a4dd691c419923c9e973d43. This is an independent analytic proof review, not author-test execution or a repeat of an older Perron/large-sieve audit. No findings remain for its stated finite-matrix domain. It is not an acceptance of a separate cubic arithmetic norm or signed saving.

The domain is important: X>=2, 1<=U<=X, FINITE distinct ideal index sets with individual norms<=X, and an arbitrary complex operator K which is already zero off coprime squarefree products of norm<=X. All additional masks remain in K. On that supported set alone H_da=H_d H_a. There is no asserted coefficient factorization AU(da)=AU(d)AU(a), no primitive beta factorization, no non-SF extension and no positivity assumption.

For the one-variable Perron integral I_T, the two oscillatory tails each contribute at most2/(T|logx|) before division by2pi and multiplication byx^c. Thus the stated bound2x^c/(pi T|logx|) is correct. The full integral is exact Fourier inversion away fromx=1, requiring no contour shift or L-function input. The HALF-INTEGER U#=floorU+1/2 is separated from every positive integer Nr by at least1/2. Since max(U#,Nr)<=X+1/2, |log(U#/Nr)|>=1/(2X+1)>=1/(3X). Also(U#/Nr)^c<=e for c=1/log4X. Hence the error is at most(6e/pi)X/T<6X/T. The selected6 constant is safe. The indicator is exactlyNr<=U even at integerU; no boundary half-weight occurs.

T>=8X gives e_T<=3/4. Therefore2e_T+e_T^2<=(2+3/4)6X/T=16.5X/T<18X/T. The expanded ternary product has exactly3^omega(da) disjoint ordered divisor assignments. Equation(5)'s finite-height error and all signs in its finite integral are correct.

The diagonal-integral step is a true operator estimate: each integrand is diag(H_d) K diag(H_a) with an ordinary right diagonal; it need not be Hermitian. Its two diagonal norms cost G_IJ. The factor(U#)^(2c)<=e^2 and each normalized absolute vertical integral is asinh(T/c)/pi. Thus e^2 L_T^2 G_IJ is correct. Masks are preserved by these actual diagonal operations.

Crucially, the residual is NOT bounded by max-entry times||K||. The independent Frobenius argument is valid for rectangular complex matrices:

    ||R circ K||op <= ||R circ K||F
       <= max|R| ||K||F
       <= max|R| sqrt(min(#I,#J)) ||K||op.

The stated accepted fixed-field count<=2X gives18sqrt2 X^(3/2)G_IJ/T, smaller than32 X^(3/2)G_IJ/T. Empty matrices are handled before taking maxima. Thus explicit theorem(1) passes for every finiteT>=8X. T=(4X)^4 is legal, L_T=O(log4X), and splitting the finitely many small prime ideals proves each3^omega bound with constants depending on epsilon. Using delta=epsilon/2 yields G_IJ=O_epsilon(X^epsilon). No efficient Perron-evaluation runtime is inferred.

For the profile transfer, F(v)=W(e^v) is compactly supported in[0,log2], C2, and has zero boundary data for the two integrations by parts. F''(v)=xW'(x)+x^2W''(x). Splitting the Fourier integral at|t|=1 gives J(W)<=(||F||1+||F''||1)/pi and the displayed log2 supnorm formula. Fourier inversion is absolute. Each multiplier(NdNa/D)^it is two unitary norm diagonals and a scalar. The resulting Schur bound is J(W)||K|| for complex W, with D>0 arbitrary. Composition with the AU multiplier is legal and retains every original zero. Applying the transferred norm to a Gram/energy twice costs its SQUARE. No varying-profile supnorm-only bound is asserted.

The theorem correctly leaves the actual cubic/root splitting, mu(d) cancellation, finite-ray transport, full signed estimate, principal/energy/determinant/zero-location assembly and GRH unproved. It repairs one exact row-dependent AU obstacle at subpower/log cost; it does not solve those independent arithmetic tasks. No source, canonical/book/UI/build/browser/dependency/auth/publication/index changes or controls were used in this review.
