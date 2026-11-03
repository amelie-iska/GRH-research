# Finite Gauss and common-prime correlation arithmetic

## Result and source boundary

The genuine finite correlation formulas in the pinned September source7055–7247 pass the independent arithmetic audit. The local finite-FIELD kernel, including its principal zero extension, is now proved for actual mathlib `MulChar F C` on every finite field. The nonprincipal Gauss norm-squared identity is also kernel-checked. Prime-power lifting, full-modulus Fourier normalization and the common-factor CRT bookkeeping are derived below in prose. No counterexample to the genuine formulas was found.

There is an essential off-locus limitation, not a newly discovered error in that source: the principal genuine field kernel at a=b=k=0 is(P−1)^2, whereas its artificial extension is stipulated to be zero. For F7 this is36>7. Lean verifies the actual F7 sum, so the genuine bound |L|<=P cannot be extended to all residual pairs. The source explicitly restricts its identity to coprime residuals and defines an artificial kernel elsewhere. That distinction must survive subsequent Poisson or positive-support enlargements.

Pinned input: math/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex, blob268c4e3206d460c617d3d2129742a72b831b3def at math commit4eaee87548250b2682affda7d05d947c05554bae. Labels: lem:prime-power-fourier, lem:full-correlation, lem:complete-support-correlation. Actual characters and additive pairing retain the source's original zero extensions. The arithmetic identification of the unit-phase ratio with the fixed reciprocity bicharacter, and the global theta/reflection/Gram/moment estimates, are NOT formalized or certified merely by these finite identities.

Formal primary reference: pinned mathlib commitf897ebcf72cd16f89ab4577d0c826cd14afaafc7, NumberTheory/JacobiSum/Basic.lean (`jacobiSum_nontrivial_inv`, `jacobiSum_one_one`), NumberTheory/GaussSum.lean (`gaussSum_mul_gaussSum_eq_card`), and NumberTheory/MulChar/Lemmas.lean (`star_eq_inv`). The exact Jacobi file was also checked at its public commit URL. These are classical identities, not a novelty or GRH claim.

## A genuine finite-field theorem

Let k be a finite field of size P, and let A:k->C be a multiplicative character EXTENDED BY ZERO AT ZERO, including when principal. Define

    K_A(a,b;k0)=sum_(x,y in k, a x−b y=k0) A(x) conjugate(A(y)).

For a,b both nonzero,

    K_A(a,b;k0)=A(b/a) times
      P−1, if k0=0;
      −1, if k0≠0 and A is nonprincipal;
      P−2, if k0≠0 and A is principal.

If exactly one of a,b is zero, the value is(P−1)1_(A principal)1_(k0≠0). If both vanish, the value is(P−1)^2 at k0=0 for principal A, and zero in all other cases. The last case is excluded by the genuine coprime-residual application, but is indispensable when comparing it with an artificial extension.

Here is a proof retaining all zero values. First,

    C_A(h)=sum_y A(y+h) conjugate(A(y))
      =P−1 if h=0;
      =−1 if h≠0,A nonprincipal;
      =P−2 if h≠0,A principal.

At h=0, A(y)conjugate(A(y)) is the trivial zero-extended character, whose sum is P−1. For h≠0, replace y by h t; the factor A(h)conjugate(A(h)) is1. At h=1, replace t by−t and write the result as

    A^(-1)(−1) J(A^(-1),A).

For nonprincipal A, the Jacobi sum is−A^(-1)(−1), so the product is−1; A^(-1)(−1)^2=1. In the principal case the phase is1 and J(1,1)=P−2. These are the pinned formal Jacobi identities. In particular the proof does not assume the desired autocorrelation formula or omit the points0 and−1 without their zeros.

When a,b≠0, the equation determines x=(k0+b y)/a. Factor A(b/a) out and apply C_A(k0/b). When b=0,a≠0, x=k0/a is fixed; the remaining character sum is0 for a nonprincipal A and P−1 for principal A. If k0=0 the fixed factor is zero. The case a=0 follows by swapping x,y and conjugating with k0 changed to−k0. If both vanish, the unrestricted double sum is|sum A|² when k0=0 and empty otherwise. This proves the complete case split.

FiniteCorrelation.lean proves the autocorrelation, the solved congruence and both-unit formula, the a-unit/b-zero case, unrestricted both-zero factorization/principal corner and its F7 specialization. The symmetric a-zero case follows in prose by the displayed swap/conjugation. These are actual finite fields and characters, not an abstract proposition whose desired conclusion is assumed.

## Prime-power common factors

At a good prime p, put P=Np and c=v_p(C)>=1. For the common kernel take A=chi_p^c on the residue FIELD O/(p). The character has order six before taking this power, so A is principal exactly when6 divides c. A principal character remains zero at0; it is not the constant function1.

On the genuine residual locus(n1,n2)=1, at least one coefficient is a unit at p. Every solution of

    n2 x−n1 y=k0 modulo p

has exactly P^(c−1) lifts to a solution modulo p^c: at each successive level one variable is free and the unit coefficient determines the other. The character values depend only on reduction modulo p, so the factor is EXACTLY P^(c−1), without an extra factor for a residual modulus that also contains p. Consequently the finite-field formula gives all the source's L_(p^c) cases with a=n2,b=n1, including exactly one vanishing coefficient. Its absolute value is at most P^c.

CRT factors the congruence itself over the prime powers of C, so there is no missing additive CRT phase in L_C. Their product satisfies |L_C|<=N(C) on the genuine locus. The artificial extension sets the local value to0 when both residual coefficients meet p; it has the same bound and is periodic modulo rad(C) in each residual column. It agrees with the genuine kernel only where the source asserts that identity. For instance C=p^6 and n1=n2=k0=0 modulo p^6 produce a MUCH larger genuine sum of two principal unit indicators; that is outside the coprime-residual locus and outside the asserted bound.

## Prime-power Gauss normalization

Choose the fixed primary generator pi of the ideal p. For n>=1 and G(p^n,k0)=P^(−n/2) sum_(x mod p^n) chi_p(x)^n e(k0 x/pi^n), decompose x=x0+pi y. The pairing is primitive at good p, since the fixed excluded set contains the different. The y-sum is P^(n−1) if p^(n−1) divides k0, and0 otherwise. In the former case the remaining factor is

    P^(n/2−1) sum_(x0 mod p) chi_p(x0)^n e(k1 x0/pi),
    k0=pi^(n−1) k1.

For nonprincipal A=chi_p^n and nontrivial additive psi, the finite Gauss sum satisfies

    |g(A,psi)|²=P.

This is proved in Lean by conjugating the Gauss sum, using the actual inverse multiplicative/additive characters, and applying the formal Gauss product identity. Over a field a nontrivial additive character is primitive. At trivial additive phase, the nonprincipal character sum is0. Therefore for6 not dividing n,

    |G(p^n,k0)|=P^((n−1)/2)1_(v_p(k0)=n−1).

For6 dividing n, the inner unit sum is P−1 if k1=0 modulo p, and−1 otherwise. The latter is also proved as an actual finite-field Gauss sum in Lean. Hence

    G(p^n,k0)=P^(n/2)1_(p^n divides k0)
                 −P^(n/2−1)1_(p^(n−1) divides k0).

The finite-field norm and principal inner sum are formalized. The quotient-ring lift and the source's exact primitive trace-pairing identification remain prose. In particular numerical field diagnostics are not presented as a formal proof for all Eisenstein prime powers.

## Full correlation, CRT phase and exact support

Expanding the two normalized Gauss sums in the source Fourier formula contributes1/(N(u)N(v)). Additive orthogonality over O/(uv) contributes exactly N(uv)=N(u)N(v). Thus it gives precisely the congruence-sum F(u,v;j), including when u,v share primes. At j=0, a nonzero summand has x,y units modulo u,v. Reducing modulo each modulus gives u|v and v|u, hence u=v for the chosen primary generators. The surviving value is phi(u). Principal local character powers do not remove these unit restrictions.

Put C=gcd(u,v), u=Cn1,v=Cn2 with coprime residuals. If C does not divide j the sum is empty. For j=Ck, reduction modulo n1,n2 extracts

    chi_(n1)(k) conjugate(chi_(n2)(−k)) times
    Phi(n1,n2), where Phi=chi_(n2)(n1)/chi_(n1)(n2).

Every inverted symbol is a unit. At a prime occurring in C and one residual, the congruence uniquely determines the longer-modulus variable once the shorter variable is fixed; no lift is lost or duplicated. CRT then leaves exactly L_C. The source identifies Phi with its fixed reciprocity factor R(n1,n2). We verify the orientation of that ratio, but do not claim to have re-proved the earlier global reciprocity theorem or its finite ray-table implementation.

Similarly, with u=Da,v=Eb,(a,b)=1 and(ab,DE)=1, solving at residual primes and changing x'=b x modulo D,y'=a y modulo E leaves the phase

    [chi_E(a)/chi_a(E)] [chi_b(D)/chi_D(b)] [chi_b(a)/chi_a(b)].

This is R(a,E) conjugate(R(b,D)) R(a,b) under the same identification. All the inverted symbols are units by the stated hypotheses. Off that locus, only the STIPULATED artificial extension plus the COMPLETE Mobius divisor sum is used; individual divisor terms do not turn newly shared primes into genuine D,E common support. These restrictions remain required in the later Gram proof.

## Exact diagnostics and verification limits

The checker uses actual Eisenstein residue fields at primary primes1+3omega (norm7),4+3omega (norm13), and−5 (inert norm25). The inert model is F5[omega]/(omega²+omega+1), NOT F5. Its sixth roots are reductions of1+omega; the character is obtained from x^((P−1)/6). The checker evaluates all coefficient pairs, right sides and powers1..6:108990 cases, with an independent raw double-sum pass through all2058norm7 cases. Integer sixth-root coordinates make every result exact.

It also evaluates24actual common-kernel prime-power lift cases and12full correlations with u=pi^(c+1),v=pi^c at c=1,2,6, using Hensel embeddings for the split Eisenstein primepi=1+3omega. Six full common-factor correlations use C=1+3omega and residuals4+3omega and−2+3omega, with the CRT root on the common prime squared and both residual primes. They check the unit-phase ratio and cases where original zero extensions vanish. These finite tests complement universal Lean field proofs; they do not certify the analytic Gram, reflected-energy or moment estimates.

The pinned Jacobi/Gauss module cache was added from public mathlib artifacts without upgrading, cleaning or changing the manifest. All prior caches and outputs remain preserved. Failed elaboration probes are kept locally apart from the final passing logs.

## Next concrete obligation

Independently audit the quantitative Gram periodic-Poisson step in source8345–8560, now using the genuine/artificial kernel distinction just established. Check the complete Mobius insertion, frozen common support, column coefficient independence, nonzero Fourier shells and exceptional sixth-power frequency count. A finite field identity does not prove those global bounds. If the source's R-phase periodicity is invoked, list that additional reciprocity input explicitly and check its fixed conductor separately. Outer-row/final common-signal assembly, the spectral arithmetic bridge and every full GRH scope remain unresolved.
