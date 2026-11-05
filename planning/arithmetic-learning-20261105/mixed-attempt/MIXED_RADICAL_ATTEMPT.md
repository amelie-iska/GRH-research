# Radical conductor route: ordinary large sieve gives a quantitative partial

Date: 5 November 2026. Fresh independent P7 attempt in the original Linux research checkout. This is a mathematical application refinement with a self-contained ordinary large-sieve proof, not a new BGL theorem, a Lean theorem, an actual-energy lower bound, or a GRH result. No production integration or publication is authorized by this note.

## Result and precise scope

Keep the original squarefree good ideal columns `D <= Nm <= 2D`, all literal sextic zeros, all finite S/ray data, and arbitrary fixed coefficients b_m. For an outside-S row write

    u = u0 r1 r2^2 r3^3 r4^4 r5^5 r6^6.

The first five factors are pairwise-coprime squarefree ideals with primary generators; r6 is arbitrary and may overlap them. On a dyadic block put A_j <= Nr_j < 2A_j, R = product A_j, M = max(A1,A2), Q = A1 A2 A3 A4 A5 = R/A6, and product A_j^j <= H. The actual sharp capacity, coprimality, squarefree, and ray restrictions select a subset of a positive row sum.

The new applicable block bound is

    Lambda_A <= C_(S,eps) (HD)^eps A6 {D + Q^2}.

The coefficient norm sum_m |b_m|^2 multiplies the right side. It is not replaced by one. In particular this bound covers nonsquarefree rational norms of ideal columns. Fixed literal unit/S row factors and frozen r6 act through their original bounded column multipliers.

Combined with the accepted powered-BGL block estimate, this yields the all-row envelope

    sum_(0<Nu<=H) |I_u|^2
      <<_(nu,S,eps) (HD)^eps {H + D H^(1/6) + (DH)^(2/3)} ||b||_2^2

when b_m denotes an arbitrary length-D sequence, with I_u = sum_m b_m chi_m(u). For the project's normalized actual b_m = D^(-1/2) A_U(m) nu(m) W(Nm/D), the existing divisor-norm estimate absorbs ||b||_2^2 into (HD)^eps ||W||_infty^2, uniformly under U>=1, U^2<=D. The accepted principal-residue bound is D H^(1/6) log^4(2U) ||W||_infty^2. Therefore the same envelope applies to the original residue-subtracted E_u after taking smaller internal epsilons.

At H=D^(3/4), this costs D^(7/6+eps), improving the previous D^(5/4+eps) envelope by D^(1/12). The remaining excess above H is D^(5/12), so the original requested signed energy estimate remains unproved.

More specifically, on the entire old saturation face A1=A2=A, A3=B, A4=A5=A6=1, AB=H^(1/3), one has Q=A^2 B = A H^(1/3) <= H^(2/3). At H=D^(3/4), Q^2<=D, so this entire face costs O(D^(1+eps)); this includes the previously surviving sector B<=A. This is an upper bound for raw Gram energy, not a measurement or a lower bound. It does not use signed cancellation of A_U.

## Why the proposed direct BGL radical substitution is unjustified

The primitive mixed character attached to the pair (a,b) is chi_(ab^2), and its outside-S conductor is indeed ab. A conductor count alone does not make it the Fisher--Friedberg character chi_(ab). In fixed canonical reciprocity classes, put c=ab, d=a'b' with the four factors coprime, and define Psi_(a,b)=chi_a chi_b^2. The quotient of the two proposed reciprocal values, after the fixed original ray phase, is

    Psi_(a,b)(a'b') / Psi_(a',b')(ab) = chi_b(a') / chi_a(b').

This variable factor is not removed by the original fixed S/ray partition: fixing b and b' while varying a' in one fixed original ray class leaves the nontrivial outside-S character chi_b(a') varying. Thus GL Definition 1(2) has not been verified for radical labels. No theorem for arbitrary primitive conductor families is silently imported. The ordinary all-character estimate below needs no reciprocity between family labels and conductor labels and is valid for arbitrary subsets of primitive characters.

## An elementary ordinary multiplicative large sieve over the Eisenstein integers

Let O=Z[omega], omega^2+omega+1=0, and delta=1+2omega. There is a constant C_O such that for Q,D>=1 and arbitrary coefficients c_alpha supported on a subset of O with |alpha|^2<=C0 D,

    sum_(Nf<=Q) sum_(chi primitive modulo f)
       |sum_alpha c_alpha chi(alpha)|^2
      <= C_(O,C0) (D+Q^2) sum_alpha |c_alpha|^2.                 (LS)

The sums may be restricted to unit-trivial characters, as required for trivial-infinity-type Hecke characters. Modulus1 and its principal character may be included; it gives the single frequency0. The argument below proves (LS), so no external number-field large-sieve theorem is left implicit.

1. **Reduced fractions and spacing.** O has class number one, so choose one generator f of each conductor ideal f. The primitive additive character is e_f(x)=exp(2 pi i Tr(x/(delta f))). For distinct reduced fractions x/f and y/g modulo O, their difference modulo O has the form (xg-yf-kfg)/(fg). Its numerator is a nonzero Eisenstein integer and has complex modulus at least1; |fg|=(Nf Ng)^(1/2)<=Q. Thus their distance in the fixed complex torus is at least c_O/Q. Equality modulo O between two reduced fractions forces equal denominator ideals (the denominator ideal of a reduced fraction is intrinsic), followed by the same residue numerator. Multiplication by the fixed codifferent factor1/delta changes only constants.

2. **The two-dimensional additive inequality.** For a delta0-separated set of points t_r in a fixed two-dimensional torus and lattice coefficients supported on a disk of radius O(sqrt D),

       sum_r |sum_alpha c_alpha exp(2 pi i Tr(alpha t_r))|^2
         <<_O (D+delta0^(-2)) sum_alpha |c_alpha|^2.            (ALS)

   Here is a complete analytic proof route. Identify O and its dual with Z^2 by fixed linear maps. The support lies in a box |n_i|<=N with N comparable to max(1,sqrt D). To prove the dual inequality, majorize that box indicator by C exp(-pi ||n||^2/N^2), expand the square, and apply the two-dimensional Gaussian Poisson formula. The resulting nonnegative kernel is C N^2 sum_(k in Z^2) exp(-c N^2 ||t_r-t_s+k||^2). The lifted point set is separated by c' delta0 after taking delta0 smaller than a fixed torus constant. Disjoint disks of radius c' delta0/3 give a packing count O(1+(L/delta0)^2) in any disk of radius L. Summing annuli, or integrating this count against the Gaussian, bounds every absolute kernel row sum by C {N^2+delta0^(-2)}. Schur's inequality proves the dual estimate, and finite-dimensional Hilbert-space duality proves (ALS). All constants depend only on the fixed lattice/support factor; the number of frequencies is absent from them.

3. **Gauss expansion and character orthogonality.** For a primitive multiplicative character chi modulo f, extended by zero at nonunits, its primitive Gauss sum has |tau_f(chi)|^2=Nf and

       chi(alpha) = tau_f(bar chi)^(-1)
          sum_(x mod f)^* bar chi(x) e_f(alpha x)

   for every alpha, including nonunits. The latter vanish by primitivity; no conductor-drop value replaces them. Write S(x/f)=sum_alpha c_alpha e_f(alpha x). Summing squared Gauss expansions over the primitive characters and then enlarging to all multiplicative characters gives, by orthogonality,

       sum_(chi primitive mod f) |sum_alpha c_alpha chi(alpha)|^2
         <= phi(f)/Nf sum_(x mod f)^* |S(x/f)|^2
         <= sum_(x mod f)^* |S(x/f)|^2.

   Now sum over Nf<=Q and apply (ALS) with the reduced-fraction separation in step1. This proves (LS).

4. **Ideal columns.** Every ideal m of O has a generator alpha_m with |alpha_m|^2=Nm. Choose exactly one such generator for each column; the map from ideals to these elements is injective. A finite-order Hecke character with trivial infinite type on this class-number-one field is a unit-trivial multiplicative residue character, and its ideal value equals its value on alpha_m. If the residue character descended to a proper divisor of its conductor, unit-triviality would descend too, contradicting primitive Hecke conductor minimality. Hence it is among the primitive characters used in (LS). The resulting ideal-column estimate is independent of the chosen generators and imposes no condition on rational squarefreeness of Nm.

## Transfer to the actual raw sextic block

Freeze r6, the literal unit, and the S-supported row factor. For m prime to S put

    c_m = b_m chi_m(u0) 1_(m,r6)=1.

Then ||c||_2<=||b||_2. In particular chi_m(r6^6)=1_(m,r6)=1 is kept, including permitted overlaps between r6 and any of r1,...,r5. No coprimality with r6 is added.

Let v be the product of the chosen primary generators r_j^j, 1<=j<=5. Every outside-S valuation of v lies in {1,...,5}. Its literal Kummer character kappa_v, made primitive, has trivial infinity type and conductor f_v between q and c_S q, where q=r1 r2 r3 r4 r5 and c_S is fixed. This is exactly the conductor statement in BGL Lemma2.1 plus the already established finite S-unit comparison for literal generators. The conductor has every outside-S prime of q. Thus, for all good column ideals m,

    kappa_v(m) = chi_m(v)

including their equal zero at (m,q)>1. The primitive Kummer convention is safe here because no valuation6 occurs in v. The sixth-power zeros have already been retained in c_m.

If one prefers the project's canonical theta notation, kappa_v=eta_v theta_(r1 r2^2 r3^3 r4^4 r5^5) as primitive characters, eta_v ranges over the fixed finite S-supported comparison set, and conductors are still <=c_S q. Unlike the BGL transfer, (LS) accepts all of these primitive characters together: no row-dependent phase is absorbed into c_m.

For a fixed primitive character, its outside-S conductor determines q. There are at most 5^omega(q) ways to assign each prime of q to one of r1,...,r5, before any original restrictions. This is at most C_eta (Nq)^eta, by the same finite-small-prime argument as the accepted divisor bound. This safe multiplicity estimate suffices; no classification of arbitrary Hecke families is needed. All characters in the block have Nf_v<=C_S Q (dyadic factors contribute only a fixed factor2^5). Enlarge the positive row sum to this primitive-character set, pay the subpower multiplicity, and apply (LS). Finally count O(A6) possibilities for the arbitrary frozen r6. This proves the announced block bound. Original row restrictions only shrink the positive sum.

On the three-factor face, the map from (r1,r2,r3) to the primitive character is even injective: its local tame inertia orders6,3,2 respectively identify the three factors. The more conservative multiplicity estimate works uniformly without this extra observation.

## Combining the block estimates without a false cancellation

The accepted BGL estimate is

    Lambda_A << (HD)^eps {R + DS + T},
    S=R/M, T=D^(2/3) R/M^(1/3).

The new one is A6 D + R^2/A6. The exact capacity identities imply

    R<=H, A6<=H^(1/6), RS=R^2/M<=H,
    T<=(DH)^(2/3).

For completeness, taking x_j=log A_j, C=sum j x_j, r=sum x_j, m=max(x1,x2), the third inequality is C>=2r-m. When m=x1 its slack is x3+2x4+3x5+4x6; when m=x2 add x2-x1. The last follows from 2C+m-3r = (m-x1)+x2+3x3+5x4+7x5+9x6>=0. These are universal monomial comparisons, not numerical fits.

For nonnegative quantities,

    min(R+DS+T, A6 D+R^2/A6)
      <= R+T+A6 D+min(DS,R^2/A6).

Since R^2/A6<=H^2/S^2,

    min(DS,H^2/S^2) <= (DH)^(2/3).

Indeed, split at S=(H^2/D)^(1/3); on either side the appropriate monomial is bounded by (DH)^(2/3). Hence every block is bounded by

    C (HD)^eps {H + D H^(1/6) + (DH)^(2/3)} ||b||_2^2.

Sum the logarithmically many dyadic blocks with smaller internal epsilons. For S-supported literal row ideals b, use the actual reduced capacity H/Nb and sum geometric factors (Nb)^(-1), (Nb)^(-1/6), (Nb)^(-2/3). All converge because S is finite. Literal unit multiplicity is at most6. This proves the all-literal-row bound above, including units and arbitrary sixth-power rows.

At H=D^(3/4), the old/new combined envelope still reaches exponent7/6 at

    A1=D^(5/12), A2=D^(1/6), A3=A4=A5=A6=1.

Here A1 A2^2=D^(3/4), DS=D^(7/6), and Q^2=D^(7/6); T has exponent10/9 and is smaller. This identifies the next upper-envelope obstruction. It is not an energy lower bound or a reason the actual signed coefficients cannot cancel. Including the accepted quadratic pivot does not change this witness because A3=1.

## Evidence, prerequisites, and boundaries

Primary sources are the existing pinned BGL arXiv:1112.1650v1 (Lemma2.1, Section3) and GL arXiv:1112.1642v2 (Definition1). No new download or external source publication was performed. Their exact paths/hashes and all read production inputs are bound in source-pins-v1.json. The ordinary sieve above is derived rather than asserted from these papers.

The focused stdlib checker verifies new rational capacity/envelope bookkeeping, exact sixth-order Gauss magnitude and all-character domination on small split residue fields, and reduced Eisenstein fraction uniqueness. It does not replace the Gaussian Poisson argument, prove an infinite arithmetic bound by enumeration, or check Lean. Independent review is recorded separately in REVIEW.md. No production bytes, queue claim, prior checks, protected index, compiler state, dependencies, models, datasets, or releases are changed.

The new estimate improves the prior unsigned envelope but still does not prove the target signed mean square, a type-II minus type-I covariance bound, short/principal reassembly at the target size, a positive arithmetic determinant comparison, zero location, or GRH. It uses no finite learning and makes no generalization claim.
