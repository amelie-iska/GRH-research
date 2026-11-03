# Independent review: arXiv:2210.11433v1 and resolution interfaces

Review date: 3 November 2026. Reviewer scope: all 40 printed pages, every section, every displayed proof, all numbered statements and examples, and the entire printed Macaulay2 transcript. This is a mathematical review, not a machine-checked certification of the cited literature. No shared manuscript, Lean, planning file, protected source clone, or existing dataset was edited. No installation, authentication, MCP activation, or push was performed.

## 1. Version and evidence

The reviewed item is Amelie Schreiber, **Multiparameter Persistent Homology: Generic Structures and Quantum Computing**, [arXiv:2210.11433v1](https://arxiv.org/abs/2210.11433v1), submitted 20 October 2022. The arXiv record currently lists only v1; the PDF has 40 pages. The internal title-page date is 21 October 2022. All page references below are printed PDF pages, which agree with the PDF page numbers.

Fresh evidence directory:

`/Users/amelieschreiber/Documents/LaTeX-projects/GRH/research/literature/projective/arxiv-2210.11433v1-review-20261103-01/`

It contains the pinned PDF, extracted layout text, pinned source archive and extraction, and separately downloaded primary Buchsbaum–Eisenbud and Bruns PDFs. Important SHA-256 values:

- `paper.pdf`: `931fbfaf973d1e827621b8c989289c4800e9334c3f2c7c564721d7668dbc01d3`
- `source.tar`: `287a28e39427e639fd72d8406f56cfdcf1179236e59d4f777558daa67b8fdae2`

The source was consulted to distinguish actual omissions from PDF extraction problems. In particular, Theorem 5.3 really has an empty theorem environment. PDF pages 20–21 were also rendered and visually inspected.

## 2. Assessment

The paper identifies useful classical tools, especially finite presentations, Fitting ideals, varieties of complexes, exterior powers and characteristic-free straightening. It is useful as a bibliography and a source of examples. Its literal statements are **not safe as a theorem package** without corrections. The main generic-exactification account replaces Bruns's direct limit by an unsupported finite stopping assertion, the acyclicity theorem is absent, an explicit multiplier equality is false, and the standard-monomial exclusion gives a false basis even for a single1×1 matrix. Several field/commutativity/finiteness hypotheses also disappear while passing between settings.

For the present project, the usable contribution is a **conditional finite-resolution architecture**: specify a finite complex, prove its exactness with the correct hypotheses, construct its determinant line, and control specialization. This paper does not construct an arithmetic complex, a holomorphic determinant, an analytic convergence theorem, or any GRH/RH implication.

## 3. Complete coverage ledger

| Pages | Material reviewed | Result of review |
|---|---|---|
| 1–3 | Abstract; §§1.1–1.3, conventions, motivation, advertised characteristic-free scope | Survey intent is explicit. Field versus integer coefficient scope and linear reductivity need correction; no quantitative application theorem is proved. |
| 4–5 | §2, Schur modules via exterior powers, tableaux, straightening relations, Remark 2.1 | Exterior-row tableau convention is legitimate, but is conjugate to the usual symmetric-row partition convention. All later rank bounds and determinant twists must use a consistent convention. The standard-basis assertion is cited, not reproved. |
| 5–8 | Definitions 3.1–3.2; §3.2 free-resolution example, exterior minors, generic presentation claims | The displayed small complex is valid after suppressing shifts. The universal length-two claim over integers, grading signs, complementary-minor signs and classification claims have defects below. |
| 8–9 | §3.3 Grassmannian functor; Remark 3.3 | Standard locally free quotient/direct-summand Grassmannian and base change are usable. Distinguish quotient rank r from submodule rank r, or use duality explicitly; reject arbitrary non-locally-free quotients. |
| 9–13 | §4 presentation spaces, graded shifts, projective covers/tops, rank invariants | The minimal-support definition of top is inadequate; minimal differential data are not recovered by maps on tops; fixed graded compatibility is more than an isolated matrix rank condition. |
| 13–17 | Definition 4.1, Proposition 4.2, Recall 4.3, Theorems 4.4–4.5 and its complete displayed proof, Example 4.6 | Generic determinantal facts are recoverable under their actual hypotheses. The Cauchy argument proves a statement about the full symmetric algebra and omits the quotient's partition cutoff. Grassmannian is a Plücker subvariety, not all exterior projective space. |
| 17–18 | §4.3 six-dimensional representation example | Matrices commute and satisfy XY=0. Stated source/target dimensions conflict; the claimed indecomposability proof using X+Y is insufficient. No claim here that the representation itself is decomposable. |
| 18–19 | §4.4, Definition 4.7, Theorems 4.8–4.9 | Fitting invariance, arbitrary base change, and local generator tests are usable for finite presentations. In the stated Noetherian polynomial setting finite generation implies finite presentation. They do not establish exact base change of resolutions. |
| 19–20 | §5.1, Theorem 5.1 and full construction, Remark 5.2, Theorem 5.3 | Bruns existence result is genuine; construction needs a direct limit, corrected rank indexing, and cycle generators. Theorem 5.3 is empty. |
| 20–21 | §6, Examples 6.1–6.2 | Example 6.1 uses undeclared variables; displayed nonminimal format is defensible and visible in appendix. Example 6.2 equates independent minors and is false. |
| 22–25 | §§7.1–7.4, Definitions 7.1–7.2, Example 7.3, Proposition 7.4 | Coordinate equations describe a scheme of complexes with rank upper bounds. Points, fibers, exact loci, bases and orbit quotients must be separated. Scheme-functor and rank-indexing errors below. The promised proof through §8 is affected by §8's defects. |
| 25–29 | Entire §8, Definitions 8.1–8.2, Examples 8.3–8.4, Definition 8.5, Remark 8.6, Examples 8.7–8.8, Definition 8.9, Theorems 8.10–8.11, Definition 8.12, Theorems 8.13 and 8.15, Definition 8.14 | Monomial order is incompletely defined; rank cutoff is wrong; ambient polynomial alphabets are conflated. Relations in 8.10 and multiplier basis assertion in 8.11 are cited without proof and need the original universal/multiplier hypotheses. Constructibility is an imported Tchernev result, not established here. The original Tchernev full text could not be retrieved through Project Euclid's security check; no claim of independent verification of that paper. |
| 29–30 | Entire §9, Example 9.1, colored product and multitableaux | Tensor product of independent coordinate algebras is a legitimate construction, but it does not impose cross-color commutativity/relations. Indexed minor conventions require repair before using the explicit tableau as a computation. Its standardness conclusion depends on the defective §8 definitions. |
| 30–31 | Entire §10, Ising and dynamic DBSCAN proposals | Ising formula is recognizable. Arbitrary time-varying graphs do not give ordinary bifiltrations; entanglement/metric and quantum-code assertions remain proposals. |
| 31–39 | Entire §11 transcript | Exterior-power and product computations are explicitly shown; no completed exactification, grade verification, homology computation of the generic family, quantum computation, or runtime/version information is supplied. Unit in the last differential explains nonminimality. One deliberately erroneous `minors(M)` call is followed by the corrected `minors(2,M)`. |
| 39–40 | All references | Many useful originals; incomplete placeholders `[?]`, `[]`, `§??`, incomplete titles and no precise theorem attribution remain. Recent sources below supply narrower, more reliable interfaces. |

“Reviewed” does not mean every external theorem was reproved. The paper is mainly a survey: the only substantial displayed proof in the determinantal portion is Theorem 4.5's Cauchy argument; later main assertions are mostly cited or announced. The evidence above identifies which imports remain imports.

## 4. Most consequential corrections

### A. The acyclicity criterion is missing (p.20, Theorem 5.3)

Theorem 5.3 consists only of its number and citation. Neither its rank condition nor its grade/depth condition is stated. The surrounding exterior-power definitions do not imply exactness.

A safe finite-free version is as follows. Let R be a commutative Noetherian ring and

`0 → F_n --d_n→ ... → F_1 --d_1→ F_0`

be a complex of finite free R-modules, with d_i d_{i+1}=0. Define

`r_i = Σ_{j=i}^n (-1)^(j-i) rank_R(F_j)`.

Then positive-degree acyclicity is characterized by the expected ranks `rank(d_i)=r_i` and `grade_R I_{r_i}(d_i) ≥ i` for each i≥1, with the usual conventions for zero ranks and the unit ideal. Rank here is the maximal nonzero exterior power/minor rank, not merely a pointwise numerical guess. There is no requirement that d_1 be surjective; H_0 is the module being resolved. For constant-rank finite projectives, formulate locally or use the projective version.

The original primary source is [Buchsbaum–Eisenbud, *What Makes a Complex Exact?*, J. Algebra 25 (1973), pp.259–268](https://eisenbud.github.io/papers/pdfs/1973-002.pdf): criterion at pp.260–261, Theorem and Corollaries 1–2. Their module-valued version uses ranks on M and M-regular sequences, with the stated finiteness/nonzero-map conditions. I checked the actual primary statement. In a Cohen–Macaulay Noetherian setting height conditions can be used in the appropriate form; over a general ring height alone is not a replacement for grade. This criterion does not directly apply to a noncommutative path algebra or an infinite free complex.

### B. Bruns exactification is a direct-limit construction, not finite termination (pp.19–20, §5.1)

The claim that some finite stage G_m becomes acyclic is unsupported and does not reproduce Bruns. The primary [Bruns, *The Existence of Generic Free Resolutions and Related Objects*, Math. Scand.55 (1984), 33–46](https://www.home.uni-osnabrueck.de/wbruns/brunsw/pdf-article/GenFreeRes.pdf), Theorem 1 and proof at printed pp.35–36, explicitly forms a directed system S_i and takes `S = colim_i S_i`; positive homology is killed in the limit. Every prescribed finite based resolution of the format receives a compatible specialization. Bruns does not claim a finite stopping stage in that proof.

Further corrections:

- With r_k defined by the alternating sum printed above Theorem 5.1, the identity is `b_k=r_k+r_{k+1}`, not `r_k+r_{k-1}`; r_0 is generally the rank of the resolved module and need not be zero.
- Homology need not be free. Choose finitely many homology generators and cycle representatives at each Noetherian stage, not a “basis” without proof.
- The boundary equations must sum all coefficient indices. The printed lower limit `l=j`/`j=p` omits coefficients and is not a general matrix-vector multiplication formula. A related typographical defect also appears in the scanned Bruns formula; the full construction and its specialization proof determine the intended full sum.
- A countably generated generic Z-algebra is not thereby a finite type Noetherian coordinate ring.
- “Generic” means existence of specialization maps to already specified resolutions. Uniqueness is an extra universal property, not automatic. One must distinguish based resolutions from their isomorphism classes.

### C. Upper-rank complex schemes do not classify exact resolutions (pp.7–8, 19–25)

Equations `d_i d_{i+1}=0` and `(r_i+1)`-minor vanishing define complexes with rank bounds. They do not force positive homology to vanish. Setting all matrices equal to zero satisfies those equations and is nonexact whenever an internal module is nonzero. Taking a quotient by change of basis is an additional moduli problem; without it one parameterizes matrices with chosen bases.

Exactness is not preserved by arbitrary specialization of a free resolution. For example, over k[x], `0→k[x] --x→ k[x]` resolves k[x]/(x); after tensoring with k[x]/(x), its first differential is zero and H_1 is k. Sufficient replacement conditions are flat base change, the requisite Tor vanishing, or a fresh acyclicity/grade check after specialization. Derived base change retains the complex and its Tor homology; it does not erase it.

Fitting base change (Theorem 4.8) is true but logically independent of exactness preservation. Neither a universal coordinate ring nor characteristic-free straightening supplies an exactness certificate for every arithmetic specialization.

### D. Example 6.2's displayed equality is false (p.21; appendix pp.31–33)

The paper sets `(Λ³A)^t = Λ²B` for independent generic matrices A of size3×5 and B of size5×2. Their entries even have different polynomial degrees in unrelated variables. Take `A=[I_3 0]`, `B=0`: a maximal minor of A equals1 whereas every 2-minor of B equals0. This also satisfies AB=0, so adding the complex equation alone cannot salvage the stated equality.

For an exact expected-rank complex, complementary minors can be related using determinant-line identifications, signs, and the appropriate Buchsbaum–Eisenbud multiplier. They are not entrywise equal in the full polynomial ring. The appendix computes AB and the two exterior powers separately; it never establishes the equality. Exact integer counterexample checked in memory.

At p.7, the introductory example also misses a complementary-minor sign: for `d_1=[[x²,0,0],[0,x,y]]`, `d_2=(0,-y,x)^t`, the middle equation requires `[1,3]_1=-a[2]_2`, with a=x². All-plus equations fail. A general orientation convention must be fixed before writing multiplier identities.

### E. The proposed standard-monomial basis deletes allowed maximal minors (pp.27–29, Definition 8.5; Example 8.8; Definition 8.12; Theorem 8.13)

Variables in V(d) represent minors of size at most r_k (Definition 8.2). Definition 8.5 then excludes monomials divisible by a minor of size **r_k**, using V^max(d). Example 8.8 explicitly excludes a size2 minor when r_1=2. The coordinate ring of rank≤r_k matrices instead kills size **r_k+1** minors; size r_k minors are generally nonzero.

Concrete counterexample in the exact format used there: dimensions (2,5,3), ranks(2,3), maps

`X_1 = [I_2 0] : k^5→k²`,

`X_2 = [0; I_3] : k³→k^5`.

Then X_1X_2=0, the complex is split exact, and a 2-minor of X_1 equals1. This shows that maximal minors need not vanish, although nonvanishing alone does not refute an initial-ideal assertion: an initial ideal can eliminate a nonzero coordinate function. A decisive basis/initial-ideal counterexample is the single-arrow format d=(1,1), r=(1): V(d) has only x, V^max(d)={x}, so Definition8.5 permits only the monomial1. But the rank≤1 coordinate ring is k[x], the presentation map is the identity, and its kernel/initial ideal are0 rather than(x). Thus both claims fail literally. The split-complex integer check was performed in memory; the one-variable counterexample requires no numerical check.

A second distinction is needed: a polynomial algebra whose variables are **all minors** is an enlarged presentation and has relations equating a minor variable to a determinant in size1 variables, in addition to straightening/complex relations. It differs from the polynomial ring on matrix entries. Theorem 8.13 switches alphabets without specifying this presentation map or a compatible term order. A Gröbner assertion in one ring does not automatically become the same assertion in the other. Consult the original Pragacz–Weyman/Tchernev constructions rather than transplanting the displayed list unchanged.

## 5. Additional actionable defects and conditions

1. **Integer coefficient length bound (p.6, §3.2).** Over a field k, a finitely generated k[x,y]-module has projective dimension at most2. Under the paper's default K=Z this is false: `Z[x,y]/(2,x,y)` has projective dimension3, by the regular sequence(2,x,y). Generally `gl.dim Z[x_1,...,x_n]=n+1`. State a field hypothesis or the corrected bound and justify free versus projective resolutions. This matters for determinant parity and resolution format.

2. **Grading directions (p.5, Definition 3.2; p.11).** If u≤v, the structure map M_u→M_v is multiplication by `x^(v-u)`, not `x^(u-v)`. Under the conventional shift R(-u) with generator in degreeu, a degree-zero map `R(-u)→R(-v)` has coefficient degree `u-v`, not `v-u`. The worked xy example is consistent with the conventional correction, so these are genuine convention inconsistencies.

3. **Top and projective covers (p.12; pp.17–18).** The correct graded top over k[x_1,...,x_n] is `M/(x_1,...,x_n)M`; it is not just the sum of components at minimal nonzero support degrees. For `M=R⊕R(-1)` a new generator is needed in degree1 even though support already begins at degree0. A minimal free differential has entries in the homogeneous maximal ideal and induces the zero map on tops, so studying only `top(F_1)→top(F_0)` loses the relations. OverZ, torsion and nonsemisimple base coefficients require further care.

4. **Determinantal base hypotheses (pp.13–15, §4.2, Recall 4.3, Theorems 4.4–4.5).** A generic determinantal quotient over an arbitrary commutative K need not be normal or Cohen–Macaulay: for rank0 the quotient is K itself, so take nonreduced or non-CM K. Standard field or suitable base-ring hypotheses must be retained. Rational singularities require a characteristic-zero context. Orbits classified by rank are field statements, not arbitrary-ring statements: the1×1 matrices[2] and[3] overZ have equal rank and are not equivalent under units. Normality is equivalent to R1 plus S2 for a Noetherian domain; “nonsingular in codimension1” alone is insufficient. The Cohen–Macaulay determinantal case supplies the missing S2, but the general recall is overbroad.

5. **Cauchy filtration misses the determinantal quotient (pp.14–15, Theorem 4.5 and its entire proof).** The argument describes the full symmetric algebra. For rank≤r the sum must omit the partitions corresponding to minors larger thanr: in the paper's exterior-row convention this is the bound on largest row/minor size; in the usual Schur convention it is the bound on the number of parts. At rank0 the coordinate ring is K, whereas the unqualified displayed sum contains positive-degree terms. In positive characteristic this is a filtration with specified associated graded, not an automatic semisimple direct sum.

6. **Plücker embedding is not surjective onto the ambient projective space (p.15).** Gr(n,m+n) maps to decomposable lines in P(Λ^nV), cut out by Plücker relations. For Gr(2,4), `e_1∧e_2+e_3∧e_4` is not decomposable over a characteristic≠2 field. The text's one-to-one correspondence with all points of ambient exterior projective space is false. The later discussion of relations uses the correct idea.

7. **Scheme-of-points equations (pp.22–23, §7.1).** A map from K[X]/I to a K-algebra A corresponds to a map from K[X] with `I⊆ker f`, not `ker f=I`. The stronger equality discards legitimate specializations with extra relations. Spec of a coordinate ring is not its set of K-rational points. Preserve the distinction between a scheme and its A-valued points.

8. **Adjacent rank indexing, ambient space and orbit statements (pp.23–25, §§7.2–7.3).** For `d_i:F_i→F_{i-1}`, adjacent ranks at F_i obey `r_i+r_{i+1}≤b_i`. The displayed `r_i+r_{i-1}` requires an explicit opposite indexing convention to be valid. V(b,r) must be defined inside the complex scheme, or explicitly include the composition equations. An intersection of two upper-rank strata uses coordinatewise `min(r_i,r_i')`, not an arbitrary smaller sequence. GL-orbit classification by rank sequence holds for finite-dimensional vector-space complexes, not polynomial-ring matrices: multiplication by x and x² on k[x] have the same fraction-field rank and are not related by GL_1(k[x]). Likewise Hom_R(R^a,R^b) has polynomial entries if R is a polynomial ring, not merely finitely many scalar K-coordinates unless degrees/bases or a relative scheme are fixed.

9. **Naive nonzero-minor rank over nonreduced rings is not enough (pp.20,23).** For R=k[ε]/(ε²), the complex with successive1×1 differentialsε has both naive ranks1 yet their sum exceeds the internal module rank1. Use the actual grade criterion or fiberwise rank-stratification formulation; vector-space rank inequalities cannot be transferred blindly to this rank definition over all rings.

10. **Six-dimensional example's inference and dimensions (pp.17–18).** The written source has three one-dimensional summands and target four, so it is K³→K⁴, not K⁶→K⁶. The two displayed endomorphisms define an ambient six-dimensional representation, which is a different description. Connectedness of a support graph or failure of permutation block decomposition is not a proof that no simultaneous arbitrary-basis block decomposition exists. In particular X+Y can have a Jordan block decomposition even when the pair(X,Y) is indecomposable. Prove the endomorphism-ring idempotent criterion or use the correct string-module theorem. I verified XY=YX=0; I do not assert the indecomposability conclusion is false.

11. **Example 6.1 and the appendix (pp.20–21,33–38).** Correct `Z[x_1,...,x_6]` to eight variables; x_7,x_8 occur in M. The transcript has format(1,6,8,4,1), and the last differential is `(x_1,-x_2,0,1)^t`. Its unit entry permits cancellation of a contractible R→R summand. Thus this is a valid nonminimal format, not a counterexample to the standard minimal Eagon–Northcott format(1,6,8,3). The p.21 wording should say it resolves R/I, not I, when its degree0 term isR. The appendix constructs generic matrices and products but does not finish generic exactification or verify its homology/grade conditions. It is evidence of algebraic operations, not a complete resolution certificate for the universal family.

12. **Monomial order and integer coefficients (p.25, Definitions 8.1–8.2).** Multiplicative compatibility alone does not imply a well-order. Reverse the usual exponent order on k[x] to obtain an infinite descending chain. Require a global admissible well-order with1 minimal. OverZ, standard monomials do not form a Z-free basis for every quotient: `Z[x]/(2x)` has torsion. Specific monic straightening laws can give Z-free bases; the blanket field-style claim needs a field or monic/unit-leading-coefficient hypotheses. Noetherianity and Dickson's lemma also do not automatically pass to infinitely many variables or arbitrary orders.

13. **Determinant-line orientations (pp.6–7; Remark 5.2).** Canonically `Λ^kV ≅ Λ^(n-k)V* ⊗ det(V)`. Suppressing det(V) uses an orientation/trivialization; it is harmless for fixed standard free bases but is not a basis-independent natural identification of bare functors. The orientation is acknowledged later, but must be carried consistently into multipliers and determinant lines, with complementary-minor signs.

14. **Linear reductivity and numerical arithmetic (pp.2–3).** GL_n and SL_n are not linearly reductive over arbitrary characteristic or overZ; characteristic-free Schur/standard-monomial filtrations do not rely on pretending they are. Exact rational arithmetic does not itself introduce numerical rounding errors; bit complexity and approximate/p-adic precision issues should be separated.

15. **Time-varying interaction graphs need a genuine filtration (pp.30–31, §10).** If an edge exists at t_1 but disappears at t_2>t_1, the clique complex at t_1 is not contained in that at t_2. Hence arbitrary time-dependent threshold graphs are not a bifiltration under the stated ordinary product order. A monotone cumulative construction or an explicitly defined zigzag/generalized persistence setup is needed. Controlled-U parameters or energy differences are not automatically a metric, and no theorem identifies the proposed persistence construction with entanglement or a surface-code invariant. These are application proposals, not established consequences of §§2–9.

16. **Missing references and formal placeholders.** Theorem 4.4 has `[?]`; p.7 has an empty reference; Remark 8.6 and Definition 8.12 have `§??`; §7 cites another `[?]`. Many matrix-composition labels use d_2∘d_1 where the stated arrows require d_1∘d_2. Resolve these before treating the account as reproducible mathematical documentation.

## 6. Safe transfer to gentle/surface algebra resolutions

The following distinctions prevent the useful classical material from being overextended.

### Finite-dimensional gentle algebra over a field

Let A=kQ/I be a finite-dimensional gentle algebra, fix left or right modules, and use actual idempotent projectives Ae_v or e_vA. These projectives generally are not free A-modules. Build differentials from admissible paths/string maps with a declared composition convention. Verify A-linearity and d²=0, then exactness. For a finite complex the forgetful functor to k-vector spaces is exact and faithful, so underlying finite-dimensional rank checks can certify exactness; a commutative grade theorem on A is unnecessary and inapplicable.

For parameter families over a commutative Noetherian ring B, if A_B is finite projective over B, the underlying B-modules of the idempotent projectives are finite projective. One can then apply a commutative finite-projective acyclicity criterion to the underlying B-complex, locally choosing bases, or use flat/Tor conditions. The grade conditions are conditions in B, not noncommutative “minors” in the path algebra. Family flatness, dimensions and base change still need proof.

### Infinite-dimensional monomial orders and locally gentle algebras

An infinite-dimensional path algebra, completed monomial order, or infinite family of projectives is not a polynomial ring in finitely many variables. Noetherianity, Hilbert syzygy bounds, finite Gröbner termination, ordinary commutative determinants, finite rank and properness all require separate justification. A finite quiver with oriented full-relation cycles can already have modules of infinite projective dimension; gentleness alone does not make every bounded derived object perfect. The dual-numbers algebra k[ε]/(ε²) is a basic periodic-resolution warning.

One can still use a finite perfect subcategory, a proven finite-dimensional representation, a suitable finite-over-center family, or a perfect finite-dimensional RHom realization. Each is an additional hypothesis/choice, not supplied by arXiv:2210.11433.

### Determinant line interface

For a bounded complex P• of finite projective modules over a **commutative** B, the determinant is the graded invertible B-module

`det(P•)=⊗_i (det P^i)^((-1)^i)`.

It is invariant under quasi-isomorphism and compatible with derived base change. An acyclic perfect complex has the canonical acyclic trivialization; a complex resolving a perfect object defines its determinant without requiring each cohomology module to be locally free. Identifying this with determinants of individual cohomology modules requires the relevant perfectness/local-freeness hypotheses.

For A-modules, first specify a determinant realization over a commutative base (for example the finite underlying B-complex, or a perfect RHom complex). There is no ordinary top exterior-power determinant of arbitrary projective noncommutative A-modules with the same properties. If a noncommutative determinant/K-theoretic refinement is intended, name it and prove its hypotheses.

A determinant **line** is not a scalar function until a trivialization/section is supplied. Rank loci and Fitting ideals locate algebraic degeneracy, not analytic zeros of an independently specified L-function. Arithmetic encoding, holomorphy, normalization, local uniform convergence, and a zero-transport theorem remain independent obligations.

## 7. Recent primary literature with concrete uses

These are targeted leads, checked against primary records and, where indicated, primary theorem text. They are not claimed to have received the same all-page review as the target paper. Versions are pinned to avoid silently replacing titles or hypotheses. Each transfer below retains its original algebra/category restrictions.

1. **Wen Chang, *Geometric models for the algebraic hearts in the derived category of a gentle algebra*, [arXiv:2305.03998v2](https://arxiv.org/abs/2305.03998v2), 4 September 2024 (first2023), 41pages.** Highest-priority constructive source. Theorem2.16 constructs projective resolutions from zigzag curves; Proposition2.23 gives the boundary-endpoint resolution, Remark2.27 describes the infinite periodic tail at a puncture, Corollary2.28 distinguishes finite/infinite projective dimension and band projective dimension1. Theorem2.32 interprets Yoneda extensions geometrically. Use it to generate the actual idempotent-projective complex and to test perfectness before determinants. Primary theorem text inspected, not every proof. Its algebraically closed field and finite-dimensional gentle context must not be replaced by an arbitrary arithmetic order.

2. **Yu-Zhe Liu, Chao Zhang, Houjun Zhang, *Constructing projective resolution and taking cohomology for gentle algebras in the geometric model*, [arXiv:2308.07220v1](https://arxiv.org/abs/2308.07220v1), 14August2023, 29pages.** Theorems3.2/3.4 (intro Theorem1.1) use rotation; Theorem4.4 uses projective-curve truncations for cohomology. Useful as a second constructive description. Important caution: introductory wording places resolutions in per(A) even while §3 discusses an infinite-projective-dimension case. Independently impose finite projective dimension before importing a finite determinant construction; use the explicit infinite/finite distinctions in Chang's later v2. Primary relevant sections inspected.

3. **Wen Chang, Haibo Jin, Sibylle Schroll, *Recollements of partially wrapped Fukaya categories and surface cuts*, [arXiv:2206.11196v2](https://arxiv.org/abs/2206.11196v2), 3April2023 (first2022), 30pages.** Theorem2.5 supplies a partial cofibrant dg resolution for graded quadratic monomial algebras. Theorem4.1 gives a surface-cut recollement with its no-interior-marked-points condition on the generated sub-surface. Useful for decomposing resolutions and potential determinant multiplicativity via exact triangles. It does not say arbitrary geometric cuts preserve a desired heart, perfectness or a scalar determinant. Primary introduction/theorems inspected.

4. **Benjamin Dequêne, Michaël Schoonheere, *Resolving subcategories for gentle algebras I: Monogeneous resolving subcategories for gentle trees*, [arXiv:2502.20994v3](https://arxiv.org/abs/2502.20994v3), 9September2026; and *II: Resolving subcategories for gentle trees*, [arXiv:2509.10120v2](https://arxiv.org/abs/2509.10120v2), 3October2025.** PartI §3.6 treats projective covers/resolutions; Theorem1.1(=4.27) identifies the join-irreducibles of the resolving-subcategory poset in the gentle-tree setting. PartII describes resolving closures of collections. Useful for closure under syzygies/extensions in small surface models. The tree/finite-global-dimension and algebraically closed field restrictions matter. These are resolving-subcategory results, not universal finite free resolutions of arbitrary surface algebras.

5. **Fabian Lenzen, *Computing Flat-Injective Presentations of Multiparameter Persistence Modules*, [arXiv:2401.06008v4](https://arxiv.org/abs/2401.06008v4), 13November2025 (first2024).** The older v1 title was *Computing Fringe Presentations of Multigraded Persistence Modules*. Constructs an explicit quasi-isomorphism from a bounded flat n-parameter complex to its shifted Nakayama image when all homology modules are finite-dimensional; degree0 yields a flat-injective presentation for a finite-dimensional module. Useful for finite matrix representations and duality, not a claim that every persistence or surface module meets the finiteness hypothesis. Primary abstract and setup inspected.

6. **Magnus Bakke Botnan, Steffen Oppermann, Steve Oudot, *Signed Barcodes for Multi-Parameter Persistence via Rank Decompositions and Rank-Exact Resolutions*, [arXiv:2107.06800v3](https://arxiv.org/abs/2107.06800v3), 22August2024; published [Found. Comput. Math., DOI10.1007/s10208-024-09672-9](https://doi.org/10.1007/s10208-024-09672-9).** Supplies the correct distinction between ordinary projectives and projectives for a rank-exact structure. Useful if a signed Euler characteristic/rank decomposition is desired. A rank-exact resolution is relative to a specified exact structure, so its alternating terms do not automatically define the same derived object or determinant as an ordinary projective resolution.

7. **Steve Oudot, Luis Scoccola, *On the stability of multigraded Betti numbers and Hilbert functions*, [arXiv:2112.11901v4](https://arxiv.org/abs/2112.11901v4), 7February2024; [SIAM J. Appl. Algebra Geom.8(1),54–88](https://doi.org/10.1137/22M1489150).** Signed/parity-aware bottleneck stability for Betti information, plus a stability result for projective resolutions. Useful for interpreting finite-resolution numerical invariants under perturbation. It is not same-degree matching of every individual Betti number and not analytic determinant convergence. Primary record and scope inspected.

8. **Lorenzo Guerrieri, Jerzy Weyman, *Mapping resolutions of length three I*, [arXiv:2012.08358](https://arxiv.org/abs/2012.08358); published JPAA227(4)(2023),107248, [DOI10.1016/j.jpaa.2022.107248](https://doi.org/10.1016/j.jpaa.2022.107248).** Concrete generic-resolution slices/localizations in selected length-three formats, with characteristic-zero and format conditions. This is a better template for an explicit family than asserting a generic ring automatically supplies all exact specializations. Primary published introduction inspected.

9. **Lorenzo Guerrieri, Xianglong Ni, Jerzy Weyman, *Higher structure maps for free resolutions of length3 and linkage*, [arXiv:2208.05934v3](https://arxiv.org/abs/2208.05934v3), 15March2023; and *The linkage class of a grade three complete intersection*, [arXiv:2412.00399v2](https://arxiv.org/abs/2412.00399v2), 23June2026.** Higher structure maps carry data beyond differentials/minors. The latter's classification is explicitly for grade-three licci ideals in characteristic0; its §4 discusses generic rings and higher structure maps. Useful for understanding why naive matrix minors do not provide all structure. These are commutative grade-three results, not noncommutative gentle-algebra theorems. Primary introduction and scope inspected.

10. **Xianglong Ni, Jerzy Weyman, *Free resolutions constructed from bigradings on Lie algebras*, [arXiv:2304.01381v1](https://arxiv.org/abs/2304.01381v1), 3April2023.** Explicit families resolving selected Schubert-variety restrictions. The genericity/structure-theorem extension is labeled a conjecture in its abstract; do not promote it to a universal theorem. **Sara Angela Filippini, Lorenzo Guerrieri**, [*Mapping free resolutions of length three II—Module formats*, arXiv:2303.10098v2](https://arxiv.org/abs/2303.10098v2),19January2024, is a related module-format source with perfect pd3 modules over Gorenstein local/graded rings.

11. **Dennis Eriksson, Gerard Freixas i Montplet, *Deligne–Riemann–Roch and intersection bundles*, J. Éc. polytech. Math.11(2024),247–361, [DOI10.5802/jep.254](https://doi.org/10.5802/jep.254), [arXiv:2305.13129](https://arxiv.org/abs/2305.13129).** §4.5, Proposition4.14 and Definition4.16 recall the perfect-complex determinant and determinant of cohomology/base change for the stated proper-flat-finite-presentation setting. Useful for actual line-valued functoriality. Their sequel [*The Deligne–Riemann–Roch isomorphism*, arXiv:2509.05077v2](https://arxiv.org/abs/2509.05077v2),2December2025, develops the refined isomorphism. Neither gives a canonical scalar, Hilbert-space positivity or an arithmetic zero-free theorem without further input. Relevant primary §4 text and sequel abstract inspected.

Foundational references still needed: Buchsbaum–Eisenbud1973 above; Bruns1984 above; the original De Concini–Eisenbud–Procesi, De Concini–Strickland, Pragacz–Weyman and Tchernev papers for the precise straightening rings; Opper–Plamondon–Schroll's surface model, [arXiv:1801.09659](https://arxiv.org/abs/1801.09659), for the derived/perfect category conventions. The 2023 corrigendum to Baur–Coelho Simões, [DOI10.1093/imrn/rnac368](https://doi.org/10.1093/imrn/rnac368), should accompany use of their earlier module-category model.

## 8. A concrete next test that the literature supports

Choose one finite-dimensional gentle algebra from a small marked-surface dissection and one zigzag string with boundary endpoints. Use Chang's Theorem2.16/Proposition2.23 to write its actual idempotent-projective resolution, retaining degrees, left/right convention and signs. Check d²=0 and exactness on finite underlying vector spaces; identify any periodic-tail obstruction before truncation. For a declared finite parameter family over a commutative ring, state flatness/Tor or determinantal-grade conditions explicitly. Form its determinant **line**, record basis changes/trivialization and check derived base change on a specialization with a rank drop.

This finite example can establish that the proposed surface construction has a correct homological/determinant interface. It does not yet identify that determinant with an arithmetic L-function or provide an analytic limiting argument. It is preferable to claiming that the existence of a generic resolution has already closed those interfaces.

## 9. Verification and limits

- Read all40 target pages and the source for the crucial omissions/equalities.
- Visually checked target pp.20–21 and Bruns printed pp.33–36.
- Inspected actual original Buchsbaum–Eisenbud criterion pp.260–261 and Bruns Theorem1/direct-limit proof pp.35–36.
- Ran exact, dependency-free integer arithmetic in memory confirming three decisive counterexamples: Example6.2 independent-minor equality, Definition8.5 maximal-minor exclusion, and p.7 middle complementary-minor sign.
- Macaulay2 is available at `/opt/homebrew/bin/M2`, but the transcript was reviewed rather than re-executed. No claim that all historical output has been reproduced; running a modern version is unnecessary to establish the unit-entry cancellation or the counterexamples.
- No complete proof audit of every primary related paper; their role/hypotheses are individually identified above. Tchernev retrieval was blocked by a site security check; no bypass or authentication attempted.
- No shared-source mutation, dependency changes, credentials or private data access. New immutable literature copies/extractions were placed only in the fresh evidence directory authorized by the parent task; this report is the requested `/tmp` artifact.
