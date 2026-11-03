# Quantitative Gram: normalized periodic cancellation

Status: proved general periodic-Poisson estimate in prose and nine kernel-checked finite Fourier/dyadic components; conditional reconstruction of the September Gram bound. No GRH or new zero-free half-plane is established. The arithmetic pairing, reciprocity-period identification and initial scalar/Poisson representation are explicit source inputs, not hypotheses silently discharged by Fourier algebra.

Source: math at4eaee87548250b2682affda7d05d947c05554bae, preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex, blob268c4e3206d460c617d3d2129742a72b831b3def, lines8345–8560 (prop:probe-gram and eq:gram-periodic-poisson). The finite correlation input is audited separately in research/finite-correlation.md. No source file was changed.

## Precise cancellation lemma

Let O=Z[omega] in C with its fixed Euclidean embedding and covolume v. Let r be a nonzero Eisenstein integer, q=|r|², and a:O²→C periodic modulo r in each coordinate. Assume |a|<=M and its COMPLETE mean modulo r is0. Let W be smooth, supported on two fixed annuli 0<c<=|z_j|<=C, with a fixed collection of derivatives bounded by K. For every N>0 and A>2,

    |sum_(m in O²) a(m) W(m/sqrt(N))|
       <<_(A,c,C) K M N² min(1,(q/N)^A).                 (1)

A finite number of derivatives, depending on A, suffices. Constants are uniform in r,N and its angle, since principal Eisenstein ideals are rotations/scalings of one fixed lattice. Smooth families with seminorm K=(1+|nu|)^J R^(-B) inherit that prefactor; choose all derivative orders before the corresponding height/external-tail orders. This is a genuine analytic lemma for arbitrary bounded periodic coefficients, independent of any L-function or zero assertion.

Here is the normalization, including the period volume. The finite Fourier coefficients are

    a_hat(psi)=q^(-2) sum_(x mod r in both columns) a(x) conjugate(psi(x)).

There are q² residue pairs, so |a_hat|<=M, not M q². The trivial coefficient is0. Finite Fourier inversion and ordinary lattice Poisson give one dual-lattice sum

    N²/v² sum_(xi in (rO)^{*2}) a_hat(psi_(-xi)) W_hat(sqrt(N)xi),   (2)

with a harmless sign depending on the Fourier convention. The character is restricted to O²; indexing all dual frequencies already combines its residue representative with the ordinary Poisson translate. Do not add another sum over q² representatives or multiply (2) by q². The xi=0 term vanishes. In fact every frequency restricting to the trivial character has coefficient0.

For N>=q, the dual spacing is a fixed constant times q^(-1/2). Smooth compact support gives |W_hat(z)|<<K(1+|z|)^(-2A). Since 2A>4,

    sum_(xi !=0) (1+sqrt(N)|xi|)^(-2A) << (q/N)^A.

This proves (1) in this range, including N comparable to q. For N<q use the original lattice sum. Nonempty support requires N>=c0>0: each coordinate m_j is a nonzero lattice point. The number of pairs is O((1+N)²)=O(N²) in that range. Below c0 the sum is empty. This proves the other branch with no period loss.

Annularity is a sufficient hypothesis, not an aesthetic choice. A generic claim with unrestricted Schwartz W and a(0)W(0)!=0 fails as N tends to0. Take a(m)=(-1)^(first integer coordinate of m1), a mean-zero coefficient modulo2, and a smooth bump equal to1 at0 supported in a small ball. Only the origin remains for small N, giving1 instead of O(N²). The source profiles have the required fixed annuli; this is a counterexample to dropping a hypothesis, not to the source's actual estimate. Other suitable vanishing/decay conditions could replace annularity.

## Exact arithmetic inputs and zero masks

The source column has the normalization

    A_m=Y'^(-3/2) sum_s c_sigma(s) W1(q_s/Y')
                            (q_s/Y')^(-1+i nu) g_chi_s(s,-m).

In expanding its squared norm, write s_i=C n_i with coprime residuals. The row Poisson factor Q/(q_s1 q_s2) and the complete Fourier correlation factor q_s1 q_s2 cancel, leaving Q/Y'^3. This uses the actual finite correlation and the source pairing; it is not inferred from a model Gauss sum.

Retain the artificial common kernel L_C from the source: |L_C|<=q_C, period rad(C) in each column, and value0 if a prime of C meets both residual columns. Insert the COMPLETE Mobius divisor sum for residual coprimality before applying a triangle inequality. Then n_i=d m_i have no remaining coprimality restriction. Terms with (d,Ck)!=1 vanish: at C-primes use the artificial common zero, and at k-primes use the ORIGINAL character zero masks. A sixth power character is still zero on nonunits. An individual Mobius term cannot replace the artificial common kernel by the genuine off-locus congruence sum.

Assume the earlier fixed reciprocity theorem identifies the remaining ray/bicharacter factors with a period dividing a fixed ideal l_fixed, independent of C,d,k. Then a joint period is

    r=lcm(l_fixed,rad(C),rad(k)),   q_r <<fixed q_C q_k.

The norm/phase identity and this EXACT fixed modulus remain an arithmetic input to the application. A nonexceptional k has a prime p outside C l_fixed with exponent e not divisible by6. After CRT, every other factor is independent of the m1 residue at p, while the remaining factor is a nonprincipal chi_p(m1)^e. Since d is a unit at p, multiplication by d permutes that field. Its complete mean is0 even when the other residues and m2 couple arbitrarily. Thus the entire joint mean vanishes. The universal finite character/mean statements in GramPoisson.lean verify this last algebraic inference, not the earlier source-specific CRT/reciprocity identification.

## Shells and the nonexceptional estimate

Retain the source range Z>=2, 1<=Q,Y'<=Z^K0 for a FIXED K0, together with its prescribed support ranges. This polynomial-range hypothesis is needed when logarithmic or divisor losses are absorbed into Z^epsilon; the assertion is not uniform over unrestricted independent Q,Y',Z. Write P=Y'^2/Q>=1. Use dyadic shells R>=1 with q_C q_k/P comparable to R, the first shell also including q_C q_k/P<=2. Fix dyadic q_C comparable to C0, q_d comparable to D0, and set

    N=Y'/(C0 D0),  K_R=RP/C0,  q_r << RP.

The joint smooth weight has seminorm <<(1+|nu|)^J R^(-B), for any desired fixed B after sufficient fixed derivative orders. Applying (1), its two-column sum is bounded by

    (1+|nu|)^J R^(-B) C0 N² min(1,(RP/N)^A).       (3)

If a k-shell is nonempty, K_R has a fixed positive lower bound; ideal/lattice counting gives O(K_R) k-values and O(C0), O(D0) common/divisor values. Multiplying (3) by these counts and Q/Y'^3 gives EXACTLY

    (Q/Y') (RP/(C0D0)) min(1,(RP C0D0/Y')^A)       (4)

before the displayed smooth seminorm. The identity is kernel-checked in gram_nonexceptional_accounting. Units/fixed ray multiplicities only change constants.

For Lambda=Y'/(RP), put C0=2^i,D0=2^j. The remaining positive sum is

    S_A(Lambda)=sum_(i,j>=0)2^(-i-j) min(1,(2^(i+j)/Lambda)^A)
              =sum_(n>=0)(n+1)2^(-n) min(1,(2^n/Lambda)^A).

Take A>=2. If Lambda<1, this is4. Otherwise choose L>=0 with2^L<=Lambda<2^(L+1). The finite head is bounded by

    Lambda^(-2) sum_(n=0..L)(n+1)2^n
       =[L 2^(L+1)+1]/Lambda² <=2(L+1)/Lambda,

and the exact tail is

    sum_(n=L+1..infinity)(n+1)2^(-n)=(L+3)2^(-L)<2(L+3)/Lambda.

Thus S_A(Lambda)<=4(L+2)/Lambda (with a harmless strict/weak endpoint adjustment), and S_A(Lambda)<<(1+log(2+Lambda))/Lambda throughout Lambda>0. At the exact threshold and A=2,

    S_2(2^L)=3(L+1)2^(-L)+4^(-L).

The finite head, infinite tail and total4 are Lean statements using actual real sums/tsums. The grouping by n=i+j, comparison of min powers and full infinite inequality are prose, not claimed as a fully formalized Poisson theorem. R summation with B>2, and the allowed subpower logarithmic loss, give the nonexceptional Gram contribution

    (1+|nu|)^J (Q/Y') (P²/Y') Z^epsilon.          (5)

For Lambda<1 the same bound follows from S=4<=4/Lambda.

## Sixth-power exceptional frequencies

If k is exceptional, (k)=a1^6 e, where e has exponents0..5 and is supported on C l_fixed. There are at most a fixed factor times6^omega(C) possibilities for e, bounded by q_C^epsilon for every fixed epsilon>0. For each e, counting a1 gives O(K_R^(1/6)); if the scale is subunit the actual shell is empty or K_R is bounded below. The artificial/original zero masks can only reduce this count. Hence the exceptional k count is

    <<epsilon K_R^(1/6) q_C^epsilon.

Use the trivial two-column estimate C0 N² rather than a nonexistent zero mean. Multiplying the C,d,k counts, before the outer Q/Y'^3, gives

    Y'^2 (RP)^(1/6) C0^(-1/6+epsilon) D0^(-1).

Choose epsilon<1/6 FIRST; both positive dyadic sums converge. Summing R using a sufficient B leaves

    (1+|nu|)^J (Q/Y') P^(1/6) Z^epsilon.         (6)

At k=0, the exact correlation diagonal forces s1=s2 (residual n1=n2=1), and the column annulus/phi bound gives O(Q/Y'). Combining this, (5) and (6) reconstructs

    sum_(q_m<<Q)|A_m|²
      << (1+|nu|)^J (Q/Y') [1+P^(1/6)+P²/Y'] Z^epsilon.

No counterexample, extra period-square factor or N comparable to q_r defect was found. The reviewer independently rederived these factors. This conditional closure narrows the remaining audit to the actual arithmetic phase/period mapping and upstream representation, rather than leaving an unspecified Poisson loss.

## Verification, limits and next claim

GramPoisson.lean has nine new declarations: finite normalized Fourier norm and zero mode, two nonprincipal independent-coordinate means, exact finite head/infinite total/infinite tail, head inequality and exact nonexceptional scale cancellation. All use actual finite groups/fields or real sums; none assumes a GRH-equivalent positivity property. The analytic suite now has88 declarations. The lattice Poisson theorem, smooth seminorm estimates, ideal counts and full source coefficient identification remain prose or explicit source inputs.

scripts/check_gram_poisson.py makes deterministic exact-rational diagnostics for the dyadic series (including the closed infinite tail), finite normalized Fourier coefficients, nonprincipal coordinate cancellation and scale accounting. Its samples do not prove uniform analytic bounds. The generic nonannular obstruction is mathematical, not numerical. No dependencies or toolchain pins changed. Existing failed elaboration probes are retained locally apart from final verified logs.

Next: audit the source's EXACT fixed reciprocity/ray period used here, beginning at647–734 and761–1095. Derive a modulus independent of C,d,k from the pinned earlier reciprocity statement and map all primary generators, bad primes, ray coefficients and zero masks into it; either certify the identification or isolate a counterexample. Do not count this generic Fourier lemma as the missing arithmetic bridge. The general reflected identity, moments, outer rows, final assembly, spectral determinant construction, intended Dirichlet/Hecke/Dedekind scopes and Artin holomorphy remain unresolved as recorded in planning/OPEN_OBLIGATIONS.md.
