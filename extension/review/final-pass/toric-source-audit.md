# Final source audit: tropical quivers and the ToricGT program

**Review date:** 13 November 2026. **Disposition:** corrected quiver transport, prefix information and damping; independent repairs to logarithmic valuation and bounded-path claims in the tropical-attention reference; explicitly scoped quantum and stochastic interfaces; selected Lean declarations and exact rational regression evidence. The final continuation adds path-multiplicity stability bounds, fixed-rate feasibility, proper-scoring endpoint hypotheses, and an exact predictive-synergy counterexample. These additional arguments are written proofs with finite regressions, not newly claimed Lean declarations.

This is a targeted mathematical audit of the requested sources, not a claim that every theorem in every cited paper has been verified. The existing [quantum ToricGT review](../quantum-toricgt/review.md) remains authoritative for the earlier code review, Paper V corrections and nine-run experiment. It is not overwritten or relabeled as newly executed work.

## Repositories and coverage

Both repositories were cloned and their heads resolved:

| Repository | Reviewed revision | Actual content |
|---|---|---|
| [Tropical_Quivers_of_Archs](https://github.com/amelie-iska/Tropical_Quivers_of_Archs/tree/2b6ab79a685e2c6233fb8892e59589951feeddad) | `2b6ab79a685e2c6233fb8892e59589951feeddad` | README, one 255,186-character TeX manuscript and its PDF |
| [ToricGT-Program](https://github.com/amelie-iska/ToricGT-Program/tree/f91ba1811b5a4f70d53c7120acf8ca2a0049f85b) | `f91ba1811b5a4f70d53c7120acf8ca2a0049f85b` | Five-paper program, earlier Paper I variants, figures, bibliography PDFs, and a ToricGT gitlink |

The Program's `ToricGT` gitlink is `17960fc87f0aba147e7a886a3ebc95da92bd5263`. It was not initialized during this audit. Therefore the two newly cloned repositories do not, by themselves, establish that their architecture blueprints are a runnable model package. The separate ToricGT implementation revision audited earlier was `a5199bc989a6fb170e21220e5e87bf95bc2fc0b4`; these pins must not be conflated.

All eight available TeX manuscripts were inventoried and their section/theorem headings scanned. Full text was inspected only for the following selected material:

| Source | Material read for this pass | Boundary |
|---|---|---|
| Tropical Quivers README | Complete README | Assertions of universality/generalization were checked against the manuscript's hypotheses |
| Tropical Quivers manuscript | Introduction; contraction; tropical transformer definitions; graph universality and random-order decoding; covariant cycle/Hodge construction; GFlowNet and embedding-fluid sections; max-plus cocycle growth interpretation; block small-gain and damping sections; bibliography | Remaining case studies, every code listing, and every appendix proof are not certified |
| ToricGT II | Finite packet and persistence setup; chain-map/mapping-cone statements; invariant averages; prefix-information identity; sheaf and toric-margin definitions (selected theory block around source lines 130–450) | Forty proposed objective entries and full experiments not reproduced |
| ToricGT III | Prefix-safe retrieval definition and side-information theorem; ring reduction, streaming-memory claim and margin statement; final exact-context utility theorem and its proof | Other memory/database/deployment sections scanned by headings only |
| ToricGT IV | Theory section: equivariance, proper scoring, side information, isotonic projection, sheaf gluing, persistence, margins, KL policy optimization and ergodicity | Remaining objective catalog and application proposals not audited proof by proof |
| ToricGT V | Front matter, Part II overview and beginning of semigroup presentation | The earlier review contains its independent, more detailed selected-section audit; no claim of a fresh full reread |
| Paper I variants | Section/theorem/bibliography inventories; the pinned Toric BGG rewrite's token equivariance and fixed-cell universality block, especially the claimed uniform norm | Detailed prior implementation review is reused with its original scope; the three full variants are not newly certified |

The citation-PDF directory was enumerated and twelve numeric-arXiv PDFs extracted to text for identification. Extraction is not proof review. Three of those received additional selected-text inspection: Yun et al.'s precise theorem/metric definitions, Mohamed–Hirani–Samtaney's exterior-calculus formulation, and the tropical-attention introductory/kernel/experiment context. The final revision additionally reads the primary arXiv HTML of Tropical Attention v2, Appendix C's proof of Lemma 3.1, Lemma C.1, and Theorem C.5, producing TA-08--TA-10 below. Other PDF titles were recorded only.

## TA-01: transport direction and order

**Source:** Tropical Quivers, “Elliptic complexes on quiver cycles,” the definitions of `D0`, `T_{c,e_j}`, `D1`, and the subsequent flatness assertion.

The source's `D0` residual is `x_j − A_j x_{j−1}`. Its proposed transport back to the basepoint is the forward prefix `A_1 ... A_j`. That is generally neither correctly typed nor the transport needed to telescope.

A scalar flat-cycle counterexample suffices: `A_1=2`, `A_2=1/2`, `(x_0,x_1,x_2)=(0,1,0)`. Holonomy is the identity, but the source's prefix sum is `3/2` instead of zero.

**Repair:** use the suffix `T_j=A_k ... A_{j+1}`, identity for the last edge. Then

\[
\sum_{j=1}^k T_j(x_j-A_jx_{j-1})=x_k-A_k\cdots A_1x_0.
\]

The proof cancels adjacent terms without commuting any matrix. For a closed cycle, this is `(I−H)x_0`; full flatness makes it vanish. The new chapter gives the typed proof, while Lean proves its arbitrary-length equal-space specialization by induction. The regression includes noncommuting matrices and independently compares direct suffix summation, recursive accumulation and the endpoint formula.

## TA-02: positive Laplacians versus actual chain complexes

**Source:** same Hodge subsection.

`D0 D0* + D1* D1` is positive semidefinite for arbitrary linear maps. Its kernel is `ker D0* ∩ ker D1`. The orthogonal Hodge decomposition additionally requires `D1 D0=0`, because the cross pairing is exactly `<D1 D0 x,y>`. A curved learned connection can produce a useful positive residual operator without producing an exact cochain complex. A small floating-point residual does not establish exact cohomology.

**Repair:** the chapter proves the precise equivalence and attaches the corrected flat-holonomy condition to the quiver version. This strengthens the connection to surface cochains while preserving the separation between a finite complex and a convergent continuum discretization.

## TA-03: prefix-derived certificates add no Bayes information to the complete prefix

**Sources:** ToricGT II “Prefix-visible certificates improve optimal bits-per-byte by mutual information”; ToricGT III “Prefix-safe retrieval feature” and “Side-information limit”; ToricGT IV's oracle side-information theorem.

If `Z` is measurable from the full prefix `F`, then `σ(F,Z)=F` and `I(B;Z|F)=0`. The entropy identity is valid, but a positive-information interpretation under that same measurability hypothesis is not. The full-prefix Bayes predictor has already used all the information from which the certificate was computed.

**Repair:** distinguish the complete prefix `X` from a lossy or computationally restricted representation `S=g(X)`. A certificate `Z=f(X)` can have `I(B;Z|S)>0`, or reduce approximation/optimization error within a restricted neural predictor family. The chapter derives the full actual-predictor decomposition into conditional mutual information plus the difference of conditional KL approximation errors. Arbitrary learned-predictor gains are not bounded merely by Bayes conditional mutual information.

The exact finite example uses uniform `X∈{0,1,2,3}`, `B=Z=X mod 2`, `S=floor(X/2)`. It has zero added information beyond `X` and one bit beyond `S`. This preserves the useful deployment criterion—held-out predictive benefit after artifact/runtime accounting—without a false information-theoretic explanation.

## TA-04: positive residual damping does not repair every expansion

**Source:** Tropical Quivers, “Damped updates and contraction enforcement,” immediately following its small-gain criterion.

The bound for `(1−η)I+ηF` is `(1−η)+ηL`. When `L>1`, this bound is greater than one for every positive `η`; reducing `η` cannot turn this particular bound into a contraction certificate. `F(x)=2x` gives a concrete counterexample for the exact Lipschitz constant.

**Repair:** the chapter and Lean record the inequality and counterexample. Damping can stabilize some other maps, for example `F(x)=−2x` with `0<η<2/3`; a coarse bound is not an exact Lipschitz constant. Use a valid small-gain bound, a suitable norm, monotonicity/dissipativity hypotheses or an appropriately scoped local Jacobian analysis.

## TA-05: stochastic embedding motion needs a diffusion term when variance survives

**Source:** Tropical Quivers, “From trajectory balance to a continuity equation.”

A random increment with conditional covariance of order `Δt` does not generally converge to a deterministic continuity equation driven only by its mean. The second-order term survives and produces a Fokker–Planck operator. The new chapter gives the test-function expansion, specifies the needed moment/convergence assumptions, and identifies the scaling under which the pure continuity equation is legitimate. Exact trajectory balance alone is not a diffusion-limit theorem. The manuscript itself correctly labels its Navier–Stokes penalties as an analogy; that limitation is retained.

## TA-06: gentle zero relations cannot be modeled by arbitrary trace-preserving arrows

This is a new interface theorem derived for the extension. Two composable trace-preserving maps cannot have zero composite on a space with a trace-one state, because the composite preserves that trace. Hence a gentle-algebra relation `ba=0` cannot be interpreted by assigning trace-preserving channels to both full-space arrows.

**Operational repair:** use CP trace-nonincreasing instrument branches, explicit rejection flags, or typed amplitude maps whose ranges and kernels enforce the relations. Retain postselection probability; normalized postselection is nonlinear. The elementary trace obstruction is kernel checked in `TransportContracts.trace_preserving_composite_nonzero`. The general transport telescope also holds for channel maps acting on Hermitian discrepancies; the chapter proves the finite trace-norm error bound through the positive unital adjoint.

## TA-07: tropical and graph-universality qualifications

Finite piecewise-affine functions with arbitrary real slopes fit generalized real tropical representations; lattice toric geometry needs additional integral/rational structure. Biases give affine polyhedral complexes unless homogenized. Softmax is not an exact finite piecewise-affine function on a nontrivial open logit domain, and jointly variable dot-product queries/keys are bilinear. Exact max-reduction associativity does not make every score function tropical affine.

The graph-universality proof's invocation of ambient Lebesgue `L^p` approximation does not automatically imply approximation on a lower-dimensional tokenized graph family. The new chapter supplies a continuous shrinking-peak counterexample to that implication. A valid transfer must supply the graph-domain measure or a uniform approximation result, match the relabeling group to token symmetries, and state padding/output/detokenization conditions. Expressivity then still does not imply trainability, sample efficiency or out-of-distribution generalization.

Paper I's fixed-cell theorem separately states a uniform supremum bound while citing Yun et al. The primary source's Theorems 2 and 3 prove approximation in `L^p` for `1 ≤ p < ∞`, not that supremum statement. This does not show a uniform theorem is impossible; it identifies a missing argument and a mismatched citation. Both the norm and the domain measure must be repaired before importing the theorem.

The repository bundles version 1 of arXiv:2604.14727. Its [current version 2](https://arxiv.org/abs/2604.14727v2), dated 21 July 2026, explicitly frames its exact routing geometry in fixed-key zero-temperature terms and treats finite-temperature bounds separately. Version-sensitive distinctions should be preserved in downstream citations.

## TA-08: logarithmic coordinates are not a non-Archimedean valuation

**Source:** [Hashemi et al., arXiv:2505.17190v2, Appendix C, proof of Lemma 3.1](https://arxiv.org/html/2505.17190v2).

For the displayed positive-input definition `vλ(a)=log(a)−λ`, expansion gives `vλ(ab)=vλ(a)+vλ(b)+λ`. The source writes a minus offset even immediately after deriving the plus offset. More substantially, its claimed inequality `vλ(a+b)≤max(vλ(a),vλ(b))` fails for `a=b=1`, since `log(2)>0`. Subtracting the same constant from both sides cannot remove the additive `log 2` error. No question about signed inputs is needed for this counterexample.

**Repair:** the amendment proves the exact product formula and the log-sum-exp bound `M ≤ τ log Σ exp(z_j/τ) ≤ M+τ log m`. This is a controlled dequantization limit for `τ→0`; when the number of terms grows, `τ log m` must be controlled. Signed cancellation remains subject to the separate polynomial obstruction in the reduction chapter. The source's algorithmic experiments are distinct evidence and are not negated merely by this proof correction, but its proof package is not imported wholesale.

## TA-09: a large finite mask is not minus infinity

**Source:** the same Appendix C, Lemma C.1.

The statement that sufficiently large finite `Γ` makes the exact score `−∞` is false. The independently proved repair is a bounded-domain certificate: if an admissible score is at least `L`, excluded raw scores are at most `U`, and penalty `M>U−L`, every excluded penalized score is below the admissible maximum. On an unbounded domain an excluded value `M+1` defeats any fixed finite `M` against admissible score zero.

**Scope qualification:** the source also sets excluded value entries to literal `−∞`. If those entries really are enforced by an exact structural mask, they eliminate the candidates independently of the score penalty. The correction targets the finite-penalty inference, not a separately exactly masked maximum. All-masked outputs and any finite substitute must be defined and tested.

## TA-10: exact-length paths differ from finite Kleene closure

**Source:** the same Appendix C, Theorem C.5 and its preceding definition.

The recurrence `v_(t+1)=D⊗v_t` computes `D^t⊗v0`. It does not generally compute `⊕_(j=0)^(t−1) D^j⊗v0`, as asserted there. For the one-by-one max-plus matrix `D=[−1]`, `v0=[0]`, two pure steps give `−2`, while either the source's truncated star or the through-two-step closure gives `0`.

**Repair:** retain the previous state, `w_(t+1)=w_t⊕D⊗w_t`, to obtain `⊕_(j=0)^t D^j⊗v0`. The manuscript proves both statements by induction. The regression compares both recurrences with independently enumerated paths on 96 finite exact instances. For max-plus longest paths the cycle condition is absence of positive cycles; for min-plus shortest paths it is absence of negative cycles. These semiring conventions and the inclusive horizon are explicit.

## TA-11: a constructive relaxation certificate

The damping correction is supplemented by a sufficient condition with a complete proof. If the residual update `b=F−I` is `L_b`-Lipschitz and satisfies `<b(x)−b(y),x−y> ≤ −μ||x−y||²`, with `0<μ≤L_b`, then `I+ηb` has contraction bound `sqrt(1−2μη+L_b²η²)<1` for `0<η<2μ/L_b²`. This follows by expanding the squared difference. Single-trajectory energy dissipation does not itself establish this two-trajectory condition for a state-dependent learned closure.

## TA-12: maximal-path decay does not certify ordinary operator contraction

**Source:** Tropical Quivers, “Max-plus cocycles and tropical growth rates,” especially the interpretation following its subadditivity theorem (pinned TeX lines 1551–1595). The subadditivity of maximal path weights is not the disputed step.

Ordinary linear propagation adds contributions from different paths. For `A = a·11ᵀ` in dimension `n`, with `1/n < a < 1`, every length-`T` path has weight `a^T`, so its tropical exponent is negative. Yet `A·1 = na·1` and the induced row-sum norm of `A^T` is `(na)^T`, which grows. The exact two-dimensional witness uses `a=3/4`: maximal paths decay by `3/4`, while the linear map grows by `3/2`.

**Repair:** for chronological, possibly rectangular arrows, count admissible paths `C_T(i,j)` and retain their maximum absolute weight `W_T(i,j)`. Direct expansion proves

\[
|(A_T\cdots A_1)_{ij}|
\le (|A_T|\cdots|A_1|)_{ij}
\le C_T(i,j)W_T(i,j).
\]

Taking row sums gives a bound by `N_T m_T`, where `N_T` is the maximum number of paths ending at one final index and `m_T` is the maximum path weight. For fixed dimension `n`, `N_T≤n^T`; thus `limsup log(m_T)/T + log(n) < 0` is sufficient for exponential decay. The dense example attains this bound. Replacing `|A|` by `epsilon+|A|` increases the path bound and does not eliminate multiplicity. Signed cancellation can reduce the actual product and is not recovered from absolute values.

The implementation compares ordinary multiplication, maximum-product dynamic programming, and support counts against independent exhaustive enumeration in 72 small cases, including varying dimensions and length-zero identities. Three dense examples are checked at six horizons each. This is finite exact evidence; no infinite-horizon exponent is numerically certified and no PDE convergence is inferred.

## TA-13: the weighted-gain problem is linear only at a fixed rate

**Source:** Tropical Quivers, the weight-selection paragraph following its block small-gain condition (pinned TeX lines 3531–3562).

For `G≥0` and positive weights, the bound `max_i (Gw)_i/w_i≤q` is equivalent to `Gw≤qw`. At fixed `q`, with explicit positive lower and finite upper bounds on the weights, these are linear feasibility inequalities. If `q` is also optimized in this representation, the products `q w_i` are bilinear. It is therefore not directly the single linear program described in the source.

**Repair:** use fixed-rate feasibility and, when optimization is needed, a justified bracket and bisection. Check the returned witness exactly or with validated numerical errors. The new checker verifies witnesses without claiming to implement an optimizer. For `G=[[0,2],[1/8,0]]`, `w=[4,1]`, it checks `Gw=(1/2)w`, despite the unweighted row bound of two. Multiplying the two inequalities shows that every positive witness needs `q²≥1/4`; `q=2/5` is impossible. These statements do not make sampled local Jacobian estimates into global Lipschitz bounds.

## TA-14: proper scoring needs endpoint hypotheses

**Source:** ToricGT IV, “Cross-entropy identifies conditional property probabilities” (pinned TeX lines 351–365).

The theorem minimizes over predictions in `(0,1)` but allows the true conditional probability `eta` to equal zero or one. In those deterministic cases, `q=eta` is outside the admissible class, so an interior minimizer does not exist. Differentiating and asserting `q=eta` without checking its admissibility misses this boundary.

**Repair:** either assume `0<eta<1` almost surely or permit `[0,1]` with the conventional extended log loss. The added proposition proves uniqueness at the true conditional probability for the closed interval and proves nonattainment on the open interval for deterministic labels. Exact rational witnesses check that `q/2` always improves an interior forecast for label zero and `(1+q)/2` improves it for label one; the log-loss implication follows from monotonicity of the logarithm. Finite sigmoid logits therefore need not attain the deterministic Bayes optimum. Proper scoring alone also does not certify empirical calibration after restricted or incomplete training.

## TA-15: information synergy is not a Cech-overlap correction

**Source:** ToricGT III, “Utility decomposition under exact context selection” (pinned TeX lines 1661–1675), specifically its final additive/independent-component assertion.

Take independent fair bits `X,Y`, target `B=XOR(X,Y)`, and additive sufficient statistic `T=X+Y`. Each individual source has zero information about `B`, while `T` and the pair jointly determine one fair target bit. The sources may be stored on disjoint sheaf components, so there is no nonempty overlap whose restriction data could explain this gain.

**Repair:** retain the exact conditional information chain rule:

\[
I(B;X,Y\mid C)=I(B;X\mid C)+I(B;Y\mid X,C).
\]

Equivalently, the correction to the sum of the two individual informations is `I(X;Y|B,C)−I(X;Y|C)`. Independent sources can become dependent after conditioning on the target. The geometric overlap data alone do not determine this statistical term. Additional probabilistic factorization assumptions would be needed for a special overlap formula. If both source variables are already measurable from the complete prefix, TA-03 instead makes all added conditional information zero; the synergy example concerns a predictor retaining a smaller context.

The complete four-outcome probability table is checked with rational arithmetic, including 12 pairwise-independence equalities, deterministic recovery from `T`, and dependence conditioned on `B`. The exact zero/one-bit values follow from the verified fair and deterministic laws; no floating-point entropy is substituted for the proof.

## Primary reference connections

| Primary source | Legitimate connection | What does not follow |
|---|---|---|
| [Yun et al., 1912.10077v2](https://arxiv.org/abs/1912.10077v2) | Approximation of specified continuous sequence maps in the stated metric; selected theorem text read | Universal physical accuracy, SGD convergence, unrestricted graph-map transfer |
| [TokenGT, 2207.02505v2](https://arxiv.org/abs/2207.02505v2) | Node/edge tokenization and equivariant graph representation; existing review plus primary abstract checked | Every identifier embedding is relabeling invariant; every bounded circuit inherits its expressivity theorem |
| [Hashemi et al., 2505.17190v2](https://arxiv.org/abs/2505.17190v2) | A specified tropical-projective attention kernel and algorithmic benchmarks; selected Appendix C claims independently repaired in TA-08--TA-10 | Its proof package is imported unchanged; every maximum of learned bilinear scores is the same kernel; empirical NP-hard benchmarks settle complexity questions |
| [Su–Liu, 2604.14727v2](https://arxiv.org/abs/2604.14727v2) | Conditioned routing geometry; current primary abstract checked, bundled v1 identified | Exact finite-temperature, jointly varying-input polyhedrality without qualifications |
| [Mohamed–Hirani–Samtaney, 1508.01166v2](https://arxiv.org/abs/1508.01166v2) | Exterior-calculus formulation and DEC discretization; selected formulation read | Arbitrary learned connector complexes inherit conservation, convergence, or 3D global regularity |
| [Ring Attention, 2310.01889v4](https://arxiv.org/abs/2310.01889v4) | Reference inventory and established distinction between streaming schedule and kernel definition | Ten-million-token capability or exact full tie provenance with fixed bounded storage in this program |
| [Schreiber, 2210.11433v1](https://arxiv.org/abs/2210.11433v1) | Source inventory for multiparameter persistence and quantum-computation proposals; earlier project theory remains separately scoped | A finite chain certificate proves external semantic truth or a continuum spectral conjecture |

Other identified bundled numeric-arXiv PDFs are GraphCG `2401.17123v1`, PolarQuant `2502.02617v1`, Toric Geometry of ReLU Neural Networks `2509.05894v1`, Emergent Analogical Reasoning `2602.01992v5`, and Fulton–Sturmfels intersection theory `9403002v1`. These were identified from local PDF title material; their full proofs were not audited in this pass. The two toric-variety book PDFs and every bibliography item were not reread in full. This coverage limitation must remain visible in the final release.

## Resulting artifacts and reproduction

- [Mathematical amendment](../../manuscript/chapters/toric-transport-audit.tex)
- [Selected Lean module](../../lean/TransportContracts.lean)
- [Exact finite regression](../../code/verify_toric_transport.py)
- [Pinned kernel-check driver](../../code/verify_transport_kernel.py)
- [Rational-check record](toric-transport-verification.json)
- [Kernel record](transport-kernel-verification.json) and [actual type/axiom log](transport-kernel.log)

Run from the repository root:

```sh
python extension/code/verify_toric_transport.py --output extension/review/final-pass/toric-transport-verification.json
python extension/code/verify_transport_kernel.py --toolchain /absolute/path/to/lean-4.24.0-linux --mathlib /absolute/path/to/mathlib4-v4.24.0
```

The updated exact regression passed 288 generic equal-dimension paths, 120 genuinely rectangular typed paths, 128 flat noncommuting cycles, 16 conditional-independence equalities, and 96 tropical recurrence/enumeration comparisons. It additionally passed 72 independent path-multiplicity enumerations, 18 dense branching cases, the accepted/rejected weighted-gain witnesses, 12 XOR pairwise-independence equalities, and 32 endpoint-improvement witnesses. The source counterexamples are retained. Matrix shape checks reject ill-typed compositions rather than silently truncating vectors. The logarithmic witnesses use exact rational identities and monotonicity of log; floating-point logarithms are not presented as a formal proof.

The Lean module's recorded elaboration uses Lean 4.24.0, compiler commit `797c613eb9b6d4ec95db23e3e00af9ac6657f24b`, and mathlib `f897ebcf72cd16f89ab4577d0c826cd14afaafc7`. Its eleven declarations use only `propext`, `Quot.sound` and, for some declarations, `Classical.choice`. No `sorryAx` or new assumed axiom is present. The manifest records source/checker/log hashes and each declaration's actual dependencies. The release-wide rebuild records separately whether that unchanged source has been freshly checked again.

These checks certify the listed finite claims. The source surveys, quantum-channel interpretation, information decomposition, stochastic-limit discussion and continuum research program must not be relabeled as completely Lean formalized.
