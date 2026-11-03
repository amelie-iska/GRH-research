# Euler-correction extension and its shifted Hecke factor

Research heartbeat2026-11-02 (local date). The attempted claim is the specific missing local Euler-correction extension in exponent-frontier.md section3e. This rotates away from the failed generic Jensen moment-positivity argument.

Input: the explicit scalar local factors in the immutable September manuscript, math/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex, blob `268c4e3206d460c617d3d2129742a72b831b3def` at source commit `4eaee87548250b2682affda7d05d947c05554bae`. Focused rereading covered3845–4206,5480–5548 and8645–8775. All deductions below inherit the displayed scalar identity; this run does not independently certify its earlier Gauss-sum/reciprocity derivation or either manuscript's main zero-free theorem.

## A larger three-variable region

Write Q=Np>=2, V=Q^(−6z), R=a_p²Q^(4−6x−6z), W=chi_p(u)Q^(−w), D=eta(p)conj(chi_p(u))Q^(−x). Unit phases have norm1; at p|u the zero extension makes W=D=0, while W_loc retains its unit phase. The six J_j are precisely the displayed table in the input. Primes in the fixed excluded/conductor set S are omitted; “row-ramified” below refers to p|u, not new conductor factors in S.

For p not dividing u, let E=P_p*+D. The j=0 formula simplifies exactly to

    E=[R((1−Q^(−1))/(1−V)+W−D)−DW(Q−1)V/(1−V)]/(1−R).

The correction defect is

    H_p−1=[D(V+W−VW)−VW+(1−V)(1−W)E]/(1−D).

In the closed region Re x>=3/4, Re w>=19/20, Re z>=33/200, the following exponents are valid upper bounds:

| Term | exponent of Q |
| --- | --- |
| R | −149/100 |
| QDWV | −169/100 |
| DV | −174/100 |
| DW | −17/10 |
| DVW | −269/100 |
| VW | −194/100 |

All of |R|,|V|,|D|,|W| are at most3/4, so denominator reciprocals are at most4. The formulas give |E|<=40Q^(−149/100) and |H_p−1|<=656Q^(−149/100), hence safely1024Q^(−149/100).

At p|u, direct cancellation gives

    H_p−1=[R(1−Q^(−1))−eta(p)(Q−1)Q^(−x−w)V^(1_{j<=1})+(1−V)J_j]/(1−R).

The middle term has exponent at most−7/10. The respective J-table exponents are−17/10 (j1),−3/4 (j2),−6/5 and−1 (j3),−29/20 (j4), and−3/2 (j5). Thus every case gives |H_p−1|<=24Q^(−7/10), safely32Q^(−7/10).

This establishes normal convergence and holomorphy of the explicit correction product on a neighborhood of the entire closed region, with upper bound O_epsilon(q_u^epsilon). For example the open neighborhood Re x>74/100, Re w>94/100, Re z>31/200 retains exponents−137/100 for good primes and−68/100 for row primes, with the same denominator control. The finitely many primes dividing u obey the divisor-product bound. No nonvanishing of these row factors is inferred from an upper bound.

The source's finite selected-tuple formula for the compensated correction also extends holomorphically to this neighborhood: each selected G_p uses only the same nonzero denominators1−V,1−R,1−D; the unselected product converges normally. This does not prove the quantitative principal-error or contour estimates for that compensated expression.

## Principal simplification

At u=1,w=1,z=1/6, put v=Q^(−1), d=eta(p)Q^(−s), theta_p=alpha(p)^(−6)eta(p)^6, r=theta_p Q^(3−6s). Here alpha(p)=p/|p|, not a finite-order phase. The exact scalar simplification is

    P_p*=(1+v)(r−d)/(1−r),
    H_p=(1−v²)[1−vr−(1−v)d]/[(1−r)(1−d)].

For Re s>1/2, |r|<1, |d|<1, 0<v<1, and

    |vr+(1−v)d| < v+(1−v)=1.

Consequently every individual principal factor is nonzero already there. This alone does not prove convergence of their product. For each fixed sigma0>2/3,

    |H_p−1| <=12[Q^(−2)+Q^(−sigma0−1)+Q^(3−6sigma0)]

uniformly on Re s>=sigma0 and in all phases. Indeed subtracting1 gives numerator

    −v²+r(1−v+v³)+d(v+v²−v³)−rd.

For sigma0>2/3, |r|<1/2, |d|<2/3, so the denominator reciprocal is less than6 and the numerator is at most v²+2|r|+2v|d|. Hence H_eta converges normally and is nonzero on Re s>2/3. Large-prime deletion gives uniform closeness to1 on each fixed closed half-plane inside that region, not uniformly as sigma0 tends to2/3.

For a quantitative tail, the norm-Euclidean Eisenstein ring is a PID. Its norm a²−ab+b² is at least(a²+b²)/2, so counting generators in a square gives A_F(X)<=25X for X>=1. Therefore

    sum_{Np>P0} (Np)^(−1−delta)
       <=50 P0^(−delta)/(1−2^(−delta)), delta>0.

Use delta=min(1,sigma0,6sigma0−4). If the total local defect sum is at most1/4, the product differs from1 by at most exp(1/4)−1<1/3. The cutoff may be fixed uniformly in target phases for this fixed sigma0. In particular the desired sigma_t=349999/400000 is covered by the larger three-variable region. This resolves this local analytic sub-obligation conditional on the source's scalar identity, without establishing the other perturbation hypotheses.

## The extra Hecke factor and a limitation on iteration

Define

    A_p=(1−r)H_p=(1−v²)[1−vr−(1−v)d]/(1−d).

Its exact defect is

    A_p−1=−v²+(1−v²)v(d−r)/(1−d).

For every fixed sigma0>1/2 this is O_sigma0(Q^(−2)+Q^(−sigma0−1)+Q^(2−6sigma0)). Each exponent is strictly below−1. Thus A=product A_p is holomorphic and nonzero on Re s>1/2. In absolute Euler convergence,

    H_eta(s)=A(s)L_F^S(6s−3,theta), Re s>2/3,
    theta(ideal a)=alpha(a)^(−6)eta(a)^6.

The sixth power removes the choice of unit generator; theta has nontrivial angular factor alpha^(−6). It is an infinite-order Hecke character, outside the finite-order-only target family in the source. We use the angular factor description to avoid opposing infinity-type sign conventions.

For the following stronger obstruction, explicitly import classical Hecke analytic theory: the primitive completion for this character is an entire function of order 1, has gamma factor Gamma(s+3) times a nonzero exponential, obeys the functional equation with the conjugate character and the complex-conjugation identity, and has its usual nonvanishing Euler product for Re s>1. These are external analytic inputs, not Lean-checked results or GRH assumptions. Tate's original thesis sections4.4–4.5 supports the continuation/functional equation framework; the pure angular special case eta=1 is also recorded in White2208.02309v1 Theorem 2. That latter theorem alone is not cited as a proof of order 1 or of arbitrary finite-conductor twists.

Here is the deduction from the listed data. A finite zero set would, by Hadamard factorization for entire order-one functions, make the completion exp(as+b)P(s). Along positive real sigma its logarithmic absolute value would then be O(sigma)+O(log sigma). But Stirling and L(sigma,theta)->1 give sigma log sigma+O(sigma), a contradiction. Hence there are nontrivial completed zeros. Euler nonvanishing and the functional equation put them in0<=Re rho<=1; the functional equation together with conjugation reflects rho to1−conj(rho) for the same character. Select one with Re rho>=1/2. Gamma and deleted Euler factors are nonzero there, so L_F^S(rho,theta)=0.

The analytic continuation A(s)L_F^S(6s−3,theta) therefore has a zero at s=(rho+3)/6, with Re s>=7/12 and Re s<=2/3. Since A is nonzero, no cancellation occurs. Increasing the finite deletion set cannot remove this zero. Consequently the **unchanged correction** cannot meet the common-signal requirement of nonvanishing on Re s>sigma0 for any sigma0<7/12. This is a limitation of this particular correction/probe and criterion, not a counterexample to RH/GRH or the claimed7/8 source result. Removing the extra factor would change the analytic signal and require a new proof of its estimates.

## Verification, evidence and next task

EulerCorrection.lean verifies the exact complex scalar identities, convex local nonvanishing, actual complex infinite-product nonvanishing and error with explicit summability assumptions, and shifted zero transport. It does not verify the arithmetic Gauss identities, exponent-to-prime summation, multivariable normal convergence or classical Hecke completion/zero-existence theory. The exact Python checker verifies all valuation exponents, constants and local identities at actual Eisenstein prime representatives of norms7and13, using Q(sqrt(-3)) arithmetic. These finite checks are not full analytic certification.

Independent adversarial review checked the region extension, all five row valuations, constants, open neighborhoods, principal simplification, A factorization and classical-data-dependent barrier. Both article editions contain the new results. Prior data, source clones and pinned environments remain unchanged; the one additional mathlib import uses only public cache artifacts for the existing pinned version.

Next concrete task: prove the quantitative compensated principal-residue approximation on the perturbed line sigma_t (source6173–6306 and9050–9100), with all slot losses and height orders explicit, or verify the general energy/mean-square input. The corrected Euler product alone does not supply those inequalities. Any later plan to reach1/2 must replace or account for the shifted theta factor rather than assume its zeros disappear.
