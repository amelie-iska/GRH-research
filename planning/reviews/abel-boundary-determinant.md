# Independent review: an Abel-summed arithmetic rank-one Fredholm model

Date: 2026-11-03. Read-only mathematical review by `surface_completion_audit`. The final variant below uses dyadic weights, as requested after the initial logarithmic-weight proposal. No shared source, manuscript, Lean file, environment or existing output was changed. This report is a new generated artifact.

## Result and scope

The dyadic construction is correct. It gives an explicit holomorphic trace-class rank-one family on one fixed Hilbert space whose Fredholm determinant is the nonprincipal Dirichlet L-function on Re(s)>0. Both the full-range truncations and actual finite Galerkin compressions converge in trace norm, with explicit compact-uniform estimates. Their determinants are exactly the Abel-corrected Dirichlet partial sums, with the claimed sharp elementary tail bound. Multiplication of the summation coefficients by a nonzero completion factor gives the completed determinant with a specific fixed subtraction described below.

The proposed fixed-metric symmetry obstruction is also correct. No single positive inner product on the fixed space can make every member of this rank-one family symmetric along a vertical line Re(s)=sigma>0, including the critical line. The proof uses genuinely different coefficient functionals, not assumed zero locations. This obstruction survives multiplication by a nonvanishing scalar completion factor.

The result supplies an arithmetic determinant and determinant-compatible approximation; it does not supply a self-adjoint spectral pencil or locate zeros. It rules out one fixed-metric symmetrization of this specific fixed-range family, not other realizations, enlargements, nonlinear pencils, or parameter-dependent transformations. No novelty claim is assessed or made.

## 1. Assumptions and dyadic weights

Let chi be a nonprincipal Dirichlet character modulo q, primitive or imprimitive. Put

`A_n=sum_(k=1)^n chi(k)`.

Complete-period character sums vanish. Consequently A_n is periodic and bounded; choose `B>=sup_n |A_n|`. Also `A_1=chi(1)=1`, an essential normalization for the determinant formula, so u below is nonzero. The principal character is excluded: its partial sums grow linearly and the displayed u generally is not square summable. The arithmetic domain for this construction is the strict half-plane

`H_+={s in C: Re(s)>0}`.

For `2^k<=n<2^(k+1)`, define `ell_n=k+1`, `w_n=sqrt(n) ell_n`. In particular `w_1=1`. Work on the fixed standard Hilbert space `H=ell^2(N_{>=1},C)` and set

`u_n=A_n/w_n`,

`delta_n(s)=n^(-s)-(n+1)^(-s)`, `v_n(s)=w_n delta_n(s)`.

All powers of positive integers use their real logarithms, so each scalar coefficient is entire in s. There is no branch choice depending on n or s.

In a dyadic block,

`sum_(n=2^k)^(2^(k+1)-1) 1/n <= 1`.

Therefore

`||u||_2^2 <= B^2 sum_(k>=0) (k+1)^(-2) <= 2 B^2`.

For `N=2^J-1`, J>=1, the tail additionally satisfies

`||(I-P_N)u||_2^2 <= B^2 sum_(k>=J)(k+1)^(-2) <= B^2/J`.

These are unconditional arithmetic estimates, with no GRH or cancellation bound stronger than bounded complete-period sums.

## 2. Square summability, explicit v tails, and holomorphy

For s=sigma+it with sigma>0,

`delta_n(s)=s integral_n^(n+1) x^(-s-1) dx`,

hence `|delta_n(s)| <= |s| n^(-sigma-1)`. The sign is positive: integrating x^(-s-1) gives `(n^(-s)-(n+1)^(-s))/s`.

Fix any compact set Q contained in H_+, and choose `sigma_0>0`, M with `Re(s)>=sigma_0` and `|s|<=M` on Q. Put `r=2^(-2 sigma_0)`, so 0<r<1. A dyadic block has

`sum_(2^k<=n<2^(k+1)) |v_n(s)|^2 <= M^2 (k+1)^2 r^k`.

Indeed `w_n^2 |delta_n|^2 <= M^2 (k+1)^2 n^(-2 sigma_0-1)`, and the block has 2^k terms. Thus v(s) lies in ell^2 and, uniformly on Q,

`||v(s)||_2 <= V_Q := M sqrt((1+r)/(1-r)^3)`.

For N=2^J-1, the exact geometric-series evaluation gives

`||v(s)-P_N v(s)||_2^2 <= tau_J^2`,

`tau_J^2 = M^2 r^J [ (J+1)^2/(1-r) + 2(J+1)r/(1-r)^2 + r(1+r)/(1-r)^3 ]`.

To verify the closed form, write k=J+m and expand `(m+J+1)^2`; use the three geometric sums of 1, m and m^2. No eventual monotonicity condition or unspecified large-N threshold is needed. This corrects the main presentational weakness of the original logarithmic-weight tail estimate.

Each finite-coordinate map `P_N v(s)` is an ell^2-valued holomorphic map. The displayed uniform tails on every compact subset show that these maps converge locally uniformly in the Hilbert norm. The Banach-valued Weierstrass theorem (or Cauchy integral formula applied to these finite-coordinate maps and passed to the uniform norm limit) proves that v is holomorphic on H_+.

## 3. The functional must be complex linear, not conjugate linear

Define the bounded complex-linear functional

`phi_s(x)=sum_(n>=1) v_n(s) x_n - x_1`.

The series is absolutely convergent by Cauchy–Schwarz. The coefficient pairing has **no conjugate**: using the usual Hermitian inner product with v in the first slot would conjugate the coefficients and generally destroy holomorphy. The coefficient map from ell^2 to its complex-linear dual given by this bilinear pairing is a complex-linear isometry; its Riesz representing vector, under a linear-in-second-slot inner-product convention, is the conjugate coefficient vector.

Thus phi_s is holomorphic as a dual-valued map and `||phi_s||<=||v(s)||+1`. Define

`K_s x = phi_s(x) u`.

This is trace class of rank at most one and depends holomorphically on s in trace norm. A rank-one operator `u tensor phi` has trace `phi(u)`, trace norm `||u|| ||phi||`, and Fredholm determinant `det_F(I+u tensor phi)=1+phi(u)`. These formulas can be proved directly on its finite-dimensional range (or from the exterior-power determinant, whose terms above degree one vanish). General analytic Fredholm theory is therefore unnecessary for this particular determinant calculation. For standard surrounding theory, see Taylor's [analytic Fredholm note](https://mtaylor.web.unc.edu/wp-content/uploads/sites/16915/2018/04/fred.pdf), especially its finite-rank trace-class reduction on pp.3–4; that source is context, not a substitute for these explicit formulas.

## 4. Exact Abel identity and arithmetic determinant

For N>=1, finite telescoping gives

`sum_(n=1)^N A_n delta_n(s) = S_N(s)-A_N(N+1)^(-s) =: T_N(s)`,

where `S_N(s)=sum_(n=1)^N chi(n)n^(-s)`.

To see the endpoint sign, the coefficient of n^(-s) at an interior n is `A_n-A_(n-1)=chi(n)`, and the terminal leftover is `-A_N(N+1)^(-s)`. Bounded A_n and sigma>0 imply the endpoint tends to zero. Also `sum A_n delta_n(s)` converges absolutely in this half-plane by the integral estimate. It follows that

`L(s,chi)=sum_(n>=1) A_n delta_n(s)` on H_+.

Equivalently, one first establishes this on Re(s)>1 and extends by the proved holomorphic equality. The conventional L-function and its nonprincipal analytic continuation are described in [DLMF 25.15](https://dlmf.nist.gov/25.15). The construction here does not purport to establish the full-plane continuation by its Hilbert-space norm estimates.

Since `u_1=A_1=1`,

`1+phi_s(u)=1+sum_n A_n delta_n(s)-1=L(s,chi)`.

Hence the exact arithmetic determinant identity is

`det_F(I+K_s)=L(s,chi)` for Re(s)>0.

The initial subtraction is essential. For an arbitrary bounded-partial-sum sequence with first term a_1 rather than 1, the same unadjusted subtraction would give `1+L-a_1`; the Dirichlet normalization is what makes the present formula correct.

The nonzero eigenvalue of K_s, when it is nonzero, is `phi_s(u)=L(s,chi)-1`; the rest of the spectrum is zero. At an L-zero, I+K_s annihilates u. Thus this is a genuine operator encoding defined from character coefficients without inputting unknown zeros, but it is still a nonlinear analytic family whose single potentially nonzero eigenvalue contains the original L-value. It is not a fixed Hilbert–Polya operator with its independent spectrum already identified.

## 5. Full-range truncations and finite Galerkin compressions

Put

`phi_(s,N)(x)=sum_(n<=N) v_n(s)x_n-x_1`,

`K_(s,N)=u tensor phi_(s,N)`.

Then

`det_F(I+K_(s,N))=T_N(s)`.

There is the exact trace-norm identity

`||K_s-K_(s,N)||_1 = ||u||_2 ||v(s)-P_Nv(s)||_2`.

Consequently the full-range truncations converge locally uniformly in trace norm. Although each has finite rank, its range is the same potentially infinite-support vector u; it is not itself supported on the first N coordinates.

The actual Galerkin compression is instead

`G_(s,N)=P_N K_s P_N = (P_Nu) tensor phi_(s,N)`.

Since phi_(s,N) only uses the first N coordinates, `phi_(s,N)(P_Nu)=phi_(s,N)(u)`. Its determinant is therefore the **same** T_N. For dyadic cutoffs N=2^J-1,

`||K_s-G_(s,N)||_1 <= ||u-P_Nu|| ||phi_s|| + ||P_Nu|| ||phi_s-phi_(s,N)||`

`<= (B/sqrt(J))(V_Q+1) + sqrt(2) B tau_J`, uniformly on Q.

Both terms tend to zero. The u-tail bound makes the general Galerkin operator rate slower than the full-range one, even though their scalar determinants coincide exactly. This is a valid contrast with the earlier shift-boundary approximation: there the escaping boundary remained large in trace norm, whereas here both finite-rank differences have quantitative norm bounds tending to zero.

Let `W_N=diag(w_1,...,w_N)`. On the finite coordinate space, the similarity has the precise orientation

`W_N (I+G_(s,N)) W_N^(-1) = I + A^(N) tensor (delta^(N)(s)-e_1)`.

Here A^(N) is the column `(A_1,...,A_N)` and the second factor is the linear row functional. Therefore the finite arithmetic matrix can be written with no weight radicals. This is a finite-dimensional similarity only: the infinite diagonal map with entries w_n is unbounded on ell^2, and no bounded global conjugacy or preserved infinite Hilbert metric follows from it.

## 6. Determinant error and period cutoffs

The exact remainder is

`L(s,chi)-T_N(s)=sum_(n>N) A_n delta_n(s)`.

Use the integral representation before estimating the sum:

`|L-T_N| <= B |s| integral_(N+1)^infinity x^(-sigma-1) dx`

`= (B |s|/sigma)(N+1)^(-sigma)`.

The lower endpoint is N+1, not N. On the fixed compact Q this is at most `(BM/sigma_0)(N+1)^(-sigma_0)`. If N is a multiple of the character modulus, then A_N=0 and `T_N=S_N` exactly. Dyadic cutoffs and full-period cutoffs are different sequences, but both are valid; general N convergence follows directly or by comparison with the preceding dyadic cutoff.

Unlike finite nowhere-vanishing Euler products, these additive arithmetic determinants can have zeros. Thus this route legitimately avoids the previous Hurwitz/Rouché obstruction to zero-free approximants. It does not give a theorem that their zeros lie on any particular line.

## 7. Completion factors: the exact correction

Let g be holomorphic and nonvanishing on H_+. Define

`phi_s^g(x)=g(s) sum_n v_n(s)x_n - x_1`, `K_s^g=u tensor phi_s^g`.

Then `det_F(I+K_s^g)=g(s)L(s,chi)`. The subtraction stays fixed. Multiplying the **entire original functional** by g would instead give `1+g(s)(L(s,chi)-1)`, which is not the desired completion.

All tail arguments persist with `sup_Q |g|` multiplying the v-tail bound; in the Galerkin bound replace `V_Q+1` by `(sup_Q|g|)V_Q+1`. The scalar determinant error is bounded by `sup_Q|g|` times the preceding Abel error.

For a primitive nonprincipal character of conductor f and parity a in {0,1}, the usual completion factor can be taken as

`g(s)=(f/pi)^((s+a)/2) Gamma((s+a)/2)`.

It is holomorphic and nonzero on H_+ for both parities. Gamma's poles and absence of zeros are stated in [DLMF 5.2](https://dlmf.nist.gov/5.2). Primitive conductor and parity are separate arithmetic data; imprimitive characters retain extra finite Euler factors and should not be assigned an unqualified primitive functional equation merely from this determinant representation. The principal case needs its own pole-subtracted construction.

## 8. Fixed-metric symmetry obstruction on every vertical line

Let h be any fixed positive Hermitian inner product on the underlying vector space H, with the full operators under consideration defined on that space. It need not be equivalent to the original standard norm for the following algebraic implication. Use the convention that h is linear in its second argument.

For nonzero u, a rank-one map `Kx=phi(x)u` symmetric with respect to h satisfies

`phi(x) = [phi(u)/h(u,u)] h(u,x)`, with `phi(u)` real.

Indeed symmetry with one argument equal to u gives this formula, and symmetry on u itself makes phi(u) real. In particular if phi(u)=0, symmetry forces phi=0. Thus every symmetric rank-one operator with the same range contained in span(u) must use a functional proportional to one fixed linear functional h(u,·). This conclusion is algebraic and does not assume that the metric already diagonalizes the family.

Fix sigma>0 and a real t!=0. For n>=2, the coefficients of phi_(sigma+it) and phi_sigma are exactly v_n(sigma+it) and v_n(sigma). The first-coordinate subtraction plays no role. The denominator is nonzero since `delta_n(sigma)>0`. As n tends to infinity,

`v_n(sigma+it)/v_n(sigma) = ((sigma+it)/sigma) n^(-it) (1+O_(sigma,t)(1/n))`.

This follows by expanding `1-(1+1/n)^(-s)=s/n+O_s(n^(-2))`; the weights cancel identically.

This ratio cannot be constant. Along integer subsequences obtained by rounding `exp(2 pi m/|t|)` and `exp((2 pi m+pi)/|t|)`, the relative rounding error tends to zero and n^(-it) tends respectively to +1 and -1. The ratio therefore has two distinct limits, plus and minus `(sigma+it)/sigma`. Consequently these two coefficient functionals are not proportional.

It follows that no single positive inner product can make all `K_(sigma+it)` symmetric for real t. In particular the proposed uniform symmetry on Re(s)=1/2 is impossible. The same proof works for the completed family: multiplication of n>=2 coefficients by nonzero g(s) changes the ratio by a nonzero scalar independent of n, so it cannot remove the two different subsequential limits.

A separate finite check is also correct: the 2-by-2 coefficient minor at n=2,3 and real parameters s=1,2 is

`v_2(1)v_3(2)-v_3(1)v_2(2) = -w_2 w_3/288 != 0`.

The unweighted minor is `7/864-5/432=-1/288`. This alone disproves a uniform fixed metric over the whole half-plane; the asymptotic vertical-line argument is what establishes the stronger critical-line-specific claim. Do not use the real-parameter minor alone as if its parameters belonged to the critical line.

The obstruction does not imply that no particular single K_s can be symmetrized, and does not exclude an enlarged space, an independent fixed operator/pencil, parameter-dependent metric, or other determinant-preserving representation. Those are different constructions with further obligations. In particular a nonlinear rank-one determinant identity by itself is not a zero-location theorem.

## 9. Independent checks and remaining limits

Using exact Fraction arithmetic and the existing read-only matrix routines, I checked:

- 192 exact Abel truncation identities for chi modulo 4, parameters s=1,2,3 and N=1,...,64; 48 full-period equalities T_N=S_N.
- 21 actual finite-matrix determinant identities for the weight-free conjugated rank-one matrices at s=1,2,3 and N=1,...,7.
- 15 paired exact partial u/v dyadic-tail bounds at s=1,2,3 and J=1,...,5. These check finite partial tails against the proved infinite bounds and do not replace the proof of the infinite sums.
- The unweighted coefficient minor exactly equals -1/288.
- 64 numerical beta(1)=pi/4 remainder samples obeyed the elementary error bound. These floating-point samples were only diagnostics; no proof claim rests on them.

Finite v norm squares and functional norm squares are rational at integer real s with dyadic weights. For rational-valued characters such as the tested quadratic chi modulo 4, the finite u norm squares are rational too. For a general complex character, |A_n|^2 may lie in a nontrivial real cyclotomic field; it should not be called rational without an additional character restriction.

The earlier logarithmic choice `w_n=sqrt(n) log(n+1)` is mathematically valid too. Its integral tail bound needs an eventual monotonicity threshold (N>=8 suffices uniformly for the stated positive compact exponent), and its first-coordinate subtraction is `w_1 x_1`, since w_1 is not one. The final dyadic variant avoids these presentational issues and gives simpler exact estimates.

No new Lean file was read or compiled in this pass; root was independently developing that layer. The construction has now discharged an elementary arithmetic determinant/trace-norm-convergence task on H_+, while exposing a rigorous failure of one fixed-metric symmetry strategy. The unresolved research task is a determinant-preserving positive spectral realization of this same arithmetic function, with the required all-zero comparison and completed-function scope, not merely another encoding of its scalar values.

## Final artifact review: arithmetic note, Lean and exact checker

Independently read all of `research/abel-boundary-determinant.md` (117 lines), `lean-analytic/AbelBoundary.lean` (131 lines), and `scripts/check_abel_boundary.py` (114 lines). This includes the new every-cutoff raw endpoint operator, which was not in the earlier version of this review. No shared artifacts were changed.

### Raw endpoint correction is exact and converges in the required norm

The revised functional is

`phi_(s,N)^raw = J(P_Nv(s))-e_1*+A_N(N+1)^(-s)e_1*`.

Since u_1=1, its rank-one determinant is `1+phi_(s,N)^raw(u)=T_N+A_N(N+1)^(-s)=S_N` at **every N**. The endpoint is linear in A_N, with no character conjugation or extra sign. The full-range operator difference has the bound

`||K_s-K_(s,N)^raw||_1 <= ||u|| [||v-P_Nv|| + |A_N| (N+1)^(-Re(s))]`.

On a compact with lower real bound sigma_0 this adds at most `sqrt(2) B^2 (N+1)^(-sigma_0)` to the previous corrected-sum trace bound. The actual Galerkin raw operator has range P_Nu, and its endpoint difference is bounded by the same quantity because `||P_Nu||<=sqrt(2)B`. Its determinant is unchanged, since the functional only reads coordinates through N. The finite weighted similarity and raw matrix in note lines 45–50 have the correct orientation and coefficients.

For completion, the raw functional

`g(s)[J(P_Nv(s))+A_N(N+1)^(-s)e_1*]-e_1*`

has determinant exactly `g(s)S_N(s)`. The fixed subtraction remains outside the g multiplier. Uniform compact bounds multiply the v and endpoint tails by sup|g|; the projection-of-u term also uses the correctly completed functional norm. The note accurately distinguishes the nonlinear arithmetic family from a fixed operator with independent real spectrum.

The critical-height no-fixed-positive-metric argument is unchanged and correct. The finite real-axis minor is expressly distinguished from that stronger vertical-line proof. No broad statement excluding all other determinant representations is made.

### One compact-set hypothesis needed explicit wording

In the snapshot read, note line 19 said “For a compact K in Re s>0 fix sigma_0>0 and M>=sup_K |s|”, without explicitly requiring `sigma_0<=inf_(s in K) Re(s)`. The subsequent bounds need that lower-real-part condition. I sent this literal omission to root for correction; it is an easily specified hypothesis rather than a failure of the construction. This review's estimates always include the condition explicitly.

### Independent Lean compilation and literal scope

Independently compiled `AbelBoundary.lean` in the pinned Lean 4.24.0/mathlib environment with `-DwarningAsError=true`; exit zero. All ten declarations printed their types and only the standard foundation dependencies `propext`, `Classical.choice`, `Quot.sound`; no `sorryAx` appeared.

The formalized declarations are: exact finite Abel summation with its endpoint, the universal finite rank-one matrix determinant, an actual infinite `HasSum` for the squared geometric majorant, genuine continuous rank-one maps on an arbitrary complex inner-product space, their action on u and square identity, their exact **operator-norm** difference, the symmetry-imposed functional formula, the nonzero boundary eigenvalue for a nonzero symmetric rank-one map, the proportionality relation for two symmetric fixed-range maps, and the exact rational kernel minor. Counting these gives ten because the continuous rank-one definition is not an additional theorem declaration.

The generic finite Abel statement is zero-indexed: take c(k)=chi(k+1) and f(k)=(k+1)^(-s) to recover the manuscript's one-indexed formula. The geometric `HasSum` is valid for real r with norm below one, in particular the positive dyadic r used here. The operator-norm identity is genuinely about continuous linear maps, not a coordinate placeholder, but does **not** on its own formalize the trace-norm identity. The latter uses the rank-one singular-value calculation proved in prose.

The file does not construct the particular u and v as mathlib ell^2 vectors, prove their dyadic bounds in Lean, formalize trace-class holomorphy or Fredholm determinants, or prove the vertical asymptotic/subsequence obstruction. The note explicitly states these boundaries. The proof of the proportionality obstruction in the actual arithmetic setting still needs the nonzero coefficient and nonproportionality arguments supplied in its prose; the generic Lean relation alone is not a zero-location result.

### Exact checker run without overwriting its shared output

The checker exposes a single run() with a hardcoded output path. I parsed it in memory, removed only the final fixed-path assignment/write/print statements, and returned its already-computed report instead. All original arithmetic assertions and loops executed; no shared output writer ran and no source was modified.

Passed counts: 216 actual finite rank-one matrix determinants, 108 finite Abel identities, 42 finite dyadic kernel-tail bounds, 36 finite dyadic u-tail bounds, and 36 geometric-tail decomposition pairs. The characters modulo 3 and 4 have bounded partial sums of modulus at most one; the tests separately check period endpoints. The exact Gaussian determinant routine correctly updates the remaining submatrix and pivot signs. Its unused lower-column entries need not be explicitly zeroed for the returned determinant calculation.

The kernel/u-tail diagnostics test finite tails through coordinate 1023 against the proved infinite upper bounds; they do not assert that a finite check proves convergence of the infinite series. The u-tail loop is repeated for each exponent although u is independent of exponent; the reported count is the actual number of assertions, not 36 distinct mathematical u-tail situations. The finite matrices include both corrected and raw endpoint cases for every tested N.

The inherited chi modulo 3 certificate is transferred by an exact function identity: S_6=S_5=1-2^(-s)+4^(-s)-5^(-s), and A_6=0 makes T_6=S_6. I inspected the corresponding existing theorem `finite-offline` in `papers/core.tex` (its displayed function and certified disk). The new checker does not recompute that Rouché certificate; it checks exactly the coefficient identity needed to reuse it. Thus the statement that an off-line zero persists at cutoff N=6 is sound as an inheritance claim and is explicitly not extrapolated to all later approximants.

No substantive construction or proof error was found in these artifacts. Article additions were not yet present when this focused pass began and are not silently included in this coverage statement.

Snapshot hashes for reproducibility:

- `research/abel-boundary-determinant.md`: 11733 bytes, 117 lines, SHA-256 `3bc96415e091fd718b786a276710fadd6267aeaa9f08a9ed71c9bac2a20d024a`.
- `lean-analytic/AbelBoundary.lean`: 5750 bytes, 131 lines, SHA-256 `dfcc86209e66181be877f0359b38b5a23a5e0f894b94d433829b5d58f5125ce2`.
- `scripts/check_abel_boundary.py`: 5162 bytes, 114 lines, SHA-256 `760a99c6a279d4e4b6201c81e486afdcb06d6bdb8e3dc718bc468358a0957f8f`.

## Article additions: Abel theorem, metric obstruction and Appendix G

After the new article text appeared, independently read `papers/resolutions-core.tex` lines 215–265 (the full Abel-boundary theorem/proof, completion and common-metric proposition), the updated closure discussion at line 278 and verification disclosure at line 293, and the entire new `papers/resolutions-details.tex` Appendix G, lines 290–373. All displayed identities, estimates and proof implications match the independently reviewed construction.

The core theorem gives the correct coefficient-linear functional and raw endpoint term. Its Galerkin proof uses the full limiting functional in the u-tail difference and the truncated functional only in the second difference; the stated error is a legitimate bound. Appendix G supplies the exact geometric tail, its index power, both trace-norm rates, the finite matrix similarity with its unbounded infinite-diagonal caveat, primitive/imprimitive completion scope and the critical-height subsequence proof. The inherited off-line certificate is confined to its exact N=6 finite function and is not generalized to later truncations. The conditional positive-pencil closure remains a separate theorem whose positive-pencil hypothesis is not silently discharged by this rank-one realization.

The formal/prose boundaries remain precise: Lean verifies the finite summation identity, matrix determinant, genuine continuous rank-one operator components and scalar HasSum; the arithmetic ell^2 construction, trace class, Fredholm determinant, trace-norm holomorphy and critical-height asymptotic remain full prose arguments. The verification text does not claim otherwise.

Three small literal clarifications were communicated during this pass:

1. The research note's compact parameter sigma_0 must satisfy `0<sigma_0<=inf_Q Re(s)`. Root reported applying this correction.
2. All approximant/Galerkin statements should specify N>=1. At N=0 the full-range functional -e_1* has determinant S_0=0, but the zero-dimensional Galerkin determinant is 1. The note now explicitly restricts positive cutoffs; the core theorem's phrase “every N” was also flagged for the same qualification.
3. The primitive completion paragraph should explicitly call q the conductor, since the article previously used q as the size of a finite field. “Primitive chi of conductor q and parity a” resolves this notation without changing the formula.

These are statement-precision issues, not counterexamples within the intended domain. No substantive theorem error was identified. I also independently checked [DLMF 2.10.9](https://dlmf.nist.gov/2.10#E9); it is indeed the cited finite summation-by-parts formula with the correct endpoint sign. Bornemann's complete paper and its projection theorem were not independently reread in this focused pass; this construction's rank-one determinant continuity is independently explicit and does not depend on that unreviewed full source.

Article snapshot hashes for this added coverage:

- `papers/resolutions-core.tex`: 34730 bytes, 293 lines, SHA-256 `46ed135ba156687de0e0f1c6e66588793b465888e5220a0790901828b2451fa7`.
- `papers/resolutions-details.tex`: 48539 bytes, 373 lines, SHA-256 `e3e274646f9a5a113a66ef0557692681d0adcda609046dbdc95c3cd0b4b4cf15`.

Final clarification verification: independently reread the corrected note line 19 (explicit positive lower real bound), core line 228 (every integer N>=1), and core line 249 (primitive character of conductor q). All three precision findings are resolved. There are no outstanding substantive or literal-scope findings from this artifact/article pass.

Final corrected hashes:
- `research/abel-boundary-determinant.md`: 11773 bytes, SHA-256 `5032c8a6df8907743a83eb437e8587b41196b18816321f4382e946c00397b5c7`.
- `papers/resolutions-core.tex`: 34757 bytes, SHA-256 `f75b417d1dd3ab29b131a160c164b3356bd2115aa134f3c314a2a8da50dd3d4c`.
- `papers/resolutions-details.tex`: 49050 bytes, SHA-256 `ca1e909ac53a4315cdd2c07e124bd8e8a891d755c43f3000578fa8c28f3bd01d`.

Last insertion checked: Appendix G now starts with the elementary complete-period character-sum proof (final line 291). A unit b with chi(b)!=1 exists for a nonprincipal character, multiplication permutes the residues and forces the total sum to vanish, and finite-group character values are roots of unity. The resulting |A_n|<=q bound is correct. Also independently reread the explicit J>=1 clause at final line 294 and N>=1 in the note. This adds two lines before the previously reviewed Appendix G body; all that body remains covered.
Final Appendix G snapshot: 49050 bytes, 375 lines, SHA-256 `ca1e909ac53a4315cdd2c07e124bd8e8a891d755c43f3000578fa8c28f3bd01d`.
