# Smooth-divisor tail localization after publication

This is a new post-publication research attempt outside the frozen 153-file release and current book. It is a corollary of the already accepted positive subsequence norm, not a new sieve, signed cancellation theorem, exponent improvement, or GRH/Lean result. The attempt to close the coherent main by a tail split fails; the surviving result localizes one part of the unresolved sum.

## Actual objects and scope

Use exactly the complete original good squarefree annulus, common complex W, A_U, fixed S/nu/literal class, and original A6=1 two-pivot row block of rma:core and sw:divisor-budget. S contains the primes above 2 and 3; U^2<=D<=7U^2/2. Let R=A1 A2, M=max(A1,A2), B=||W||infty. Rows have their original unweighted natural multiplicity, including every ray/squarefree/coprime/capacity/full-union zero. The classical bound below is NOT asserted for arbitrary row weights. A subfamily is enlarged only within a positive norm. Let F=Nf, f good squarefree U-smooth, and

G_f = sum_{actual u, (f,u)=1} |T_f(1;u)|^2.

This is the actual positive norm from K0, including A_U(fa), (a,f)=1, raw row symbols and W(FNa/D). No factorization of A_U(fa), independence, removal of an original raw zero, or replacement by a coefficient proxy is used. The smooth f is an intermediate common divisor after inversion, not the original column-pair gcd h. This distinction is essential even in the original h=1 slice.

## Surviving quantitative tail

For Y>=1 define K0^{>Y}=sum_{F>Y} mu(f) G_f, with the same original masks, and define KS^{>Y} by restricting the smooth f in the accepted clean rough-prime sum KS. Then

|K0^{>Y}|/D <<_{epsilon,nu,S,literal class}
 (HD)^epsilon B^2 [R + DR/(M Y) + D^(2/3) R/(M^(1/3) Y^(2/3))].       (1)

The statement is trivial if Y>=2D. For 1<=Y<2D, insert the existing actual-coefficient bound sw:divisor-budget with d=f and L=D/F. For L>=1 its powered part gives

G_f << (HD)^eta B^2 [LR + L^2 R/M + L^(5/3) R/M^(1/3)].

The assignment bound |A_U(fa)|<<_eta D^eta is valid uniformly for N(fa)<=2D and gives the required coefficient l2 norm. For 1/2<L<1, count the unit residual directly, exactly as in the accepted proof; no subunit-length sieve is invoked. Its O(R D^eta B^2) cost is bounded by the same expression up to an absolute constant because L>1/2. Terms with F>=2D have zero profile.

Only now take the triangle over this tail and enlarge the squarefree smooth ideals to all ideals. Elementary ideal counting yields

sum_{Y<F<2D} F^-1 << log(2D),
sum_{F>Y} F^-2 << Y^-1,
sum_{F>Y} F^(-5/3) << Y^(-2/3).

After division by D these are (1), absorbing the logarithm and assignment powers into the requested epsilon. This is an application of an existing positive upper bound; no cancellation in mu(f) has been proved.

There is an exact additional support fact:

Y>=2D/U  ==>  KS^{>Y}=0.                                      (2)

Indeed every rough prime has P>U and every residual has Na>=1, so F>Y gives F P Na>2D. This statement also holds for the explicitly restored auxiliary masks in KS; it does not identify auxiliary nonsquarefree columns with original columns.

Assume additionally R<<H (as for the original feasible two-pivot blocks). A sufficient target-size tail cutoff is

Y >= max{1, 2D/U, DR/(MH), D R^(3/2)/(M^(1/2) H^(3/2))}.       (3)

Then |K0^{>Y}-KS^{>Y}|/D << (HD)^epsilon B^2 H. The high-f contribution is part of the actual signed clean main, not an elementary coefficient diagonal alone, but its proof uses only an absolute tail bound. Hidden constants in capacities and the classical norm remain fixed; (3) is a sufficient bound, not a necessary cutoff or measured energy threshold.

## Critical remaining neighborhoods

For H=D^(3/4), the high-window U is comparable with sqrt(D). At the mixed upper-envelope witness A1=D^(5/12), A2=D^(1/6), take Y=D^(13/24), with sufficiently large fixed capacity constants. The normalized powered tail exponents are respectively

7/12, 5/8, 3/4.

At the pure witness A1=D^(3/4), A2=1, take Y=D^(5/8). They are

3/4, 3/8, 3/4.

Both cutoffs exceed the rough-prime support scale D^(1/2); thus (2) applies for sufficiently large D. The general formula (3), rather than either endpoint alone, retains neighboring capacity-feasible blocks and arbitrary relative pivot sizes. These calculations describe upper bounds; they are not actual-energy lower bounds or sharpness claims.

## Failed step and next genuine target

The remaining expression still contains ALL small smooth divisors F<=Y, all rough-prime terms, coherent orientation means, common-prime and union masks, actual A_U(fa), and one common W. In particular f=1 survives. Its inherited powered monomial upper bound still reaches D^(7/6) at both displayed neighborhoods. Moving a target-size positive tail to the error therefore supplies no improvement to the global exponent and does not produce the missing 5/12 saving.

A scalar Mertens estimate cannot be applied to the remaining G_f as if it were a norm-only smooth function: literal ideal prime supports, A_U(fa), and row deletions remain coupled. Neither the triangle tail bound nor the support identity estimates the mean-retaining finite small-f sum. The next substantive task remains an actual signed estimate of this coupled main (or its coherent prime integral) before per-f/per-conductor absolute Cauchy.

No already accepted finite tables or learned traces were rerun. The exact rational exponent check accompanying this note checks only the new localization arithmetic. All frozen publication files, indices, current production artifacts and prior records stay unchanged.
