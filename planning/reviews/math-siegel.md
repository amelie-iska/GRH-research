# Read-only mathematical audit: Uniform exclusion of Landau–Siegel zeros

Source: `/tmp/grh-math-audit/siegel.tex`.

- Git blob verified: `7e41c77c252348369ca0fb99cbe389271ba6ce86`.
- SHA-256: `b011ba9c1f55ee2164292492c55e0c6d75c458eb30d4808808f9953823b8ded4`.
- Size/coverage: **all 773 lines, 31,166 bytes, read in full**, including the bibliography and proof of the interpolation lemma. No source mutation, MCP, installation, authentication, or publishing occurred. This report is the only new artifact for this subtask.

## Finding and limitations

I did **not locate a concrete fatal mathematical gap or counterexample** in this manuscript during this audit. The algebraic interpolation proof and the determinant preservation/divisibility argument survived direct scrutiny. This is substantially different from the surface-order manuscript, where numerous explicit false statements have elementary counterexamples.

This finding is **not certification of a proof of an open problem**. It is a single-auditor mathematical check, not formal verification or independent expert replication. External cited sources and current literature were not checked. In particular, I am not claiming that the claimed Landau–Siegel theorem is established in the literature, or that this audit establishes it. I give the exact proof dependencies and checks below so another auditor can attack the substantive steps rather than relying on the title or apparent plausibility.

## Exact scope versus GRH

The abstract (42–45) and main theorem (66–73) assert an absolute constant c>0 such that

`(1−β) log q ≥ c`

for every **real** zero β∈(0,1) of a primitive nonprincipal **real Dirichlet** L-function of conductor q≥3. Such characters are quadratic. The theorem targets the possible exceptional real zero near 1, uniformly in conductor.

Even if the proof were validated, this is **not GRH**. It would not locate complex Dirichlet zeros on Re(s)=1/2, would not exclude real zeros farther left than the stated logarithmic window, and would not establish the critical-line statement for general Artin, Hecke, or automorphic L-functions. No surface-order Hilbert–Pólya construction, determinant/zero identification, or arithmetic-geodesic matching is proved here. Thus it cannot close the much broader GRH gaps in the surface manuscript.

The proof supplies existence of a uniform c by contradiction. It does not provide a numerical value of c or an explicit numerical conductor threshold. The statement does not promise either, so this is a scope limitation, not a contradiction.

## Formalization evidence and limits

I also inspected the supplied conclusion file `lean_OAI_NumberTheory_SiegelZeros_Conclusions_Theorem.lean`, corresponding to upstream `Lean/OAI/NumberTheory/SiegelZeros/Conclusions/Theorem.lean`. It contains the actual theorem declaration `OAI.SiegelZeros.WeightedTorusJets.exists_absolute_real_zero_gap`, with a statement matching the primitive real-character real-zero gap. Its proof invokes `SiegelZerosAwei.W50.uniform_exclusion_of_local_isolated_bezout` and `W22.localIsolatedBezout_of_actual_regular_selection ℂ`, importing `OAI.NumberTheory.SiegelZeros.Intersection.BezoutBoundary`. The terminal wrapper itself has an `exact` proof, not a displayed `sorry`.

The separately supplied `lean_ComparatorChallenges_QuasiRiemannHypothesis.lean` contains a challenge statement with `sorry`. That is a comparator placeholder, **not the actual proof file**, and is not evidence that the actual Siegel formalization has a proof hole. It also targets a different statement (a seven-eighths zero-free region for the Riemann zeta function), not the main Siegel theorem here.

The full imported formal dependency graph has **not** been built or audited. The coordinating audit reports the upstream toolchain is Lean 4.34.1, differing from the available local Lean 4.24 core. This audit did not change or install a toolchain. Accordingly, the source declaration is evidence of an intended formalization, **not a verified kernel build or an axiom/sorry-free transitive certificate**. Verifying the theorem requires the matching upstream environment, all imports, and the actual declaration's transitive axioms, plus checking that the definitions coincide with the claimed mathematical statement.

## Dependency graph

1. A real zero with δ=(1−β)log q small forces χ(p)=1 primes to have small logarithmic mass (181–244).
2. A uniform interpolation lemma makes monomial evaluations on a projected four-dimensional integer box span all N⁴ columns (252–408); its rectangular corollary permits an anisotropic degree budget (410–432).
3. A rank-three map arising from three of the four embeddings of a biquadratic field satisfies that interpolation hypothesis (451–485).
4. Greedy weighted row selection produces a nonzero determinant whose total first-coordinate exponent S1 dominates the other two, S2 (493–549).
5. Frobenius at inert quadratic primes replaces p first-coordinate powers with one conjugate-coordinate power; the latter has lower weight when p>H (579–637).
6. This gives prime divisibility of the nonzero algebraic-integer determinant, compared against its Archimedean norm bound (554–661).
7. Choose H fixed and large, then γ fixed and large, take N=ceil(q^γ), and let δ→0 along q→∞. The resulting bound is 1≤7/8 (665–719).

## Detailed checks

### 1. Prime-bias lemma, lines 181–244

The completed-function logarithmic-derivative formula is cited at 203–215. Its sign is consistent: for real s>1 each `Re(1/(s−ρ))` is nonnegative, and retaining the β term yields an upper bound for `−L'/L`. Combining it with `−ζ'/ζ=1/(s−1)+O(1)` gives 219–220 with the stated sign.

At s=1+1/log X, terms with χ(p)=1 in the nonnegative Euler-product series contribute `2 log p/p^s ≥ (2/e)log p/p` for p≤X. Also

`1/(s−1)−1/(s−β) ≤ (1−β)(log X)²`.

Thus the claimed shortage bound is consistent. Subtracting it and the ramified-prime mass from `Σ_(p≤X) log p/p = log X+O(1)` gives the lower bound for inert primes, with a constant loss for p≤H. I found no sign reversal or uniformity failure here.

**External dependency not independently checked:** the exact Hadamard/logarithmic-derivative identity and its convergence, and the standard Mertens estimate as cited. They are standard analytic-number-theory inputs; no new arithmetic distribution theorem is smuggled in at this step as far as this reading shows.

### 2. Interpolation lemma, lines 252–408

This is the main novel algebraic input, and the part most deserving independent replication.

The assumption that the four coordinates of c span a Q-linearly independent set implies `r·c≠0` for every nonzero rational vector r. Therefore A restricts to an affine bijection from any rational affine hyperplane transverse to c onto C³ (374–380). This is enough for the face interpolation; no Diophantine lower bound on `r·c` is used.

The dimension count at 281–290 supplies a nonzero R vanishing at all integer points of 4P, because the number of polynomial coefficients exceeds the number of imposed evaluations. The proof does not need those evaluation constraints to be independent.

A nonzero R∘A cannot vanish on every point of Z⁴, so the choice of a nonvanishing lattice point m at minimum distance from the compact polytope 4P is justified. Only finitely many lattice points occur in each bounded neighborhood. By construction the minimum distance is positive.

The nearest point y defines a supporting face G of P. If P has full dimension then G is proper; if P has lower dimension, G has dimension at most three anyway. Expressing y/4 as a combination of at most four vertices of G gives a vertex u with coefficient at least 1/4, hence `y−u∈3P`.

For n off G, the translated point `y'=y+n−u` lies in 4P. The displacement toward y is `u−n`; because `h·(u−n)>0`, the displayed squared distance in 329–330 is strictly smaller for sufficiently small η. Consequently `R(A(m+n−u))=0` follows from the minimizing choice of m. I checked the sign of this inequality; it has the required direction.

The supporting face lies in a rational affine hyperplane. The three free original integer coordinates can therefore be recovered as affine functions of An on that hyperplane. The product of univariate Lagrange factors in 388–390 selects u among the face's lattice points with total degree at most 3(N−1).

Finally, translation preserves each separate degree of R, and multiplying by that Q costs at most 3(N−1) in each coordinate. The polynomial B is within the assumed rectangular budget. Off-face terms vanish by the nearest-point argument and other face terms by Lagrange interpolation, leaving `v_u R(Am)≠0`, as required.

I did not identify a missing rationality assumption, dimension-count error, or invalid nearest-point inference in this proof. In particular, the supporting hyperplane need not have a controlled coefficient height, because the subsequent determinant is formed from original monomials rather than those interpolation-polynomial coefficients.

### 3. Rectangular corollary, lines 410–432

The degrees are `T1=32 H^(2/3) U`, `T2=T3=32 H^(−1/3) U`, with U=N^(4/3). Under H≤N all Tj≥32N. Their product is 32³N⁴. The subtractive 3(N−1) costs in the interpolation lemma leave more than enough volume: the lower bound 4096N⁴ exceeds `(4N−3)^4`. The floors do not reverse the inequality because `floor(T)+1>T`.

The constant is independent of the linear map and H. No coefficient-height bound is asserted or needed in this corollary.

### 4. Field and kernel construction, lines 451–485

For a primitive nonprincipal real character, the quadratic field is Q(√d), with d squarefree and |d|≤q. Excluding d=2 avoids adjoining the same quadratic field twice. Since d≠1, the field Q(√d,√2) has degree four otherwise, including negative d.

The matrix at 471–473 has rank three. Its kernel vector `(ab,b,−a,−1)` is annihilated by all three displayed rows. Its entries are Q-linearly independent since `{1,a,b,ab}` is a basis of the biquadratic field. Thus the precise hypothesis of the interpolation lemma is met.

The finite excluded field is dealt with at the end: a hypothetical sequence with conductors tending to infinity eventually avoids it.

### 5. Weighted greedy selection and exponent bounds, lines 493–549

The row order has finite initial segments because H is a positive integer. Every row that is rejected is in the K-span of earlier retained rows. Interpolation over C implies the same rank over K because the matrix entries lie in K.

Every row in the sufficient rectangular family has weight at most 96H^(2/3)U; therefore all M retained rows occur by that weight. Hence α2,α3≤96H^(−1/3)U.

At a fixed α1 there are at most Q0=(floor(B)+1)² retained indices. Packing M first exponents with that maximum multiplicity gives the lower bound on S1. The arithmetic of the floor/remainder estimate at 537–542 is correct: its error has sign `r(Q0−r)/(2Q0)≥0`. For fixed H and sufficiently large N, M≥2Q0, yielding the stated absolute c0 and C0 and the ratio bound `S2/S1≤const/H`.

I found no dependence on q or the field hidden in these constants. H is allowed to be extremely large, but is fixed before the q→∞ limit.

### 6. Determinant-preserving prime row replacement, lines 579–637

At an odd prime not dividing 2q with `(d/p)=−1`, Euler's criterion gives the Frobenius automorphism σ or στ according to `(2/p)`. The congruence is in the actual order R=Z[a,b], and follows coefficientwise from the characteristic-p power map.

For α1=pk+r, replacing `θ^α1` by `θ^r(θ^p−g_pθ)^k` expands exactly as in 616–618. The other indices are nonnegative. Every replacement summand has smaller weight by m(p−H)>0. By the greedy property each is a K-linear combination of earlier retained rows.

Thus the simultaneous replacement matrix is lower triangular over K with unit diagonal. Its determinant is exactly one, so the determinant remains Δ. At the same time every new entry in that row is in p^kR. Factoring out these powers establishes Δ∈p^(E_p)R.

An initially suspicious issue here does **not** produce a gap: the triangular coefficients need not be integral. Determinant preservation is an identity over K, and divisibility is then obtained directly from the entries of the replacement matrix, which are integral. Lines 635–637 explicitly make this distinction correctly.

### 7. Norm and divisibility estimates, lines 554–661

The determinant lies in Z[a,b], so its field norm is a nonzero integer. If Δ∈p^E R then its norm is divisible by p^(4E). The four embeddings have the same elementary bound `|ν(θ_n)|≤8N√q`, yielding the stated Hadamard upper bound.

Summing `floor(α1/p)≥α1/p−1` over all M rows and primes up to U introduces an error bounded by `M Σ_(p≤U) log p = O(MU)`. The factor 1/4 in both norm bounds is consistent with the degree-four field. Distinct prime divisibilities combine for the single nonzero integer norm.

The comparison between log N and log U is exactly `log N=(3/4)log U`. It is the strict 3/4 coefficient, together with S2/S1 small, that creates the intended contradiction. I did not find a lost factor of four or incorrect prime-power multiplicity.

### 8. Quantifier order and limiting argument, lines 665–719

If the claimed positive infimum failed, a sequence δ→0 could be extracted with q→∞. Bounded-conductor characters cannot supply such a sequence because there are finitely many of them and each L(1,χ) is nonzero, so analyticity provides a neighborhood free of zeros near 1 for each fixed character.

The order of choices is valid as written: H fixed large first; γ fixed large second; N=ceil(q^γ); then q→∞ along δ→0. Consequently `log U/log q→4γ/3`, the δ term tends to zero, the H-dependent constant divided by log U tends to zero, and both determinant error ratios vanish using the S1 lower bound. The first two limiting contributions are at most 13/16 and less than 1/16, producing the claimed contradiction.

I did not find a diagonal-limit error in which H or γ must secretly depend on δ, nor a failure to keep the constants uniform in q.

## Recommended independent verification targets

The correct next mathematical review is independent reconstruction of the interpolation lemma and the determinant comparison, preferably by an analytic number theorist and an arithmetic-geometry/transcendence specialist. In particular:

- Prove or refute the exact interpolation statement 252–266 for all complex A satisfying the Q-independence kernel hypothesis, independently of this nearest-point proof.
- Independently reconstruct the weighted row replacement and the exact equality of determinants at 624–637.
- Check the standard analytic identity at 203–220 with the precise zero counting/completion conventions and uniform constants.
- Reproduce the norm comparison and quantifier order without relying on this report.

These are review targets, **not identified gaps**. I would not replace them with a speculative objection merely because the advertised result is major. Equally, the absence of a located error in this single pass should not be reported as a verified resolution of the Landau–Siegel problem.

## Handoff

Full source coverage was achieved for this 773-line paper. No exact fatal gap was found. The strongest supported conclusion is: the displayed proof has a coherent, self-contained algebraic core that merits independent expert checking; its claimed conclusion is much narrower than GRH and does not repair the false surface-order foundations or the missing arithmetic spectral identification in the other manuscript.
