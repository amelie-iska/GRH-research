# Dessin locally gentle algebras: semi-invariants, completion and Auslander–Reiten categories

Independent read-only review, 2026-11-03, by `surface_completion_audit`. This report concerns infinite-dimensional polynomial dessin/locally gentle algebras and their completed orders. Finite-dimensional modules are test objects for those infinite algebras, not a substitution of a finite-dimensional gentle algebra for the requested object. No shared manuscript, source clone, Lean file or environment was changed.

## Conclusions and one substantive refinement

Determinants of maps between finite sums of idempotent projectives are valid semi-invariants for the stated infinite-dimensional dessin algebras. The proposed point-evaluation weight is correct. Schofield–Van den Bergh's spanning theorem itself allows oriented cycles; its characteristic-zero hypotheses, and the separate hypotheses for Hom/Ext or derived interpretations, must be retained.

The nilpotent-degeneration argument is correct: over an algebraically closed field every invariant regular function on the **reduced** fixed-dimension nilpotent representation variety is constant. This does not imply that all semi-invariants, modules, bands or orbit parameters are trivial. Completed finite-length modules have nilpotent central t; polynomial modules at nonzero central characters and complete-order lattices are different categories.

There is an important refinement to “the Ext interpretation needs pd<=1”. An actual short projective resolution is needed to identify the cokernel of Hom(f,N) with Ext¹(M,N) and to interpret the presentation Euler difference as the module's Hom–Ext Euler number. However, for **any** projective presentation f with square Hom(f,N), determinant nonvanishing already implies—and is equivalent to—Hom(M,N)=Ext¹(M,N)=0. It does not force higher Ext to vanish. Concrete dessin/node examples below distinguish these assertions.

For the completed node I can prove the actual lattice AR sequences and the proposed nonzero 3-by-3 specialization diagram. The proof uses conductor descent to classify its lattices and verifies factorization, rather than importing a finite-dimensional gentle curve theorem. General strongly locally finite quiver theorems of Bautista–Liu–Paquette and Paquette do not automatically apply to finite quivers with surviving permitted cycles or completed orders.

## 1. Exact determinant construction, weights and hypotheses

Let A=kQ/I for a finite quiver with the quadratic monomial dessin relations; A may have infinitely many paths. Use right modules and P_i=e_iA. Let

`P_0=sum_i P_i^(a_i)`, `P_1=sum_i P_i^(b_i)`, `f:P_1 -> P_0`.

For a finite-dimensional representation N with dimension vector alpha, precomposition gives

`Hom_A(f,N): Hom_A(P_0,N) -> Hom_A(P_1,N)`.

Its source and target dimensions are `sum a_i alpha_i` and `sum b_i alpha_i`. Define its determinant only when those dimensions agree. Fixed bases/trivializations determine its scalar up to the expected constant factor. The determinant belongs naturally to a determinant line before those choices.

With column-vector representation matrices and point action `N(a) -> g_target N(a) g_source^(-1)`, put `G_0=sum g_i^(a_i)` and `G_1=sum g_i^(b_i)`. Naturality gives

`Hom(f,g.N)=G_1 Hom(f,N) G_0^(-1)`.

Consequently

`c_f(g.N)=product_i det(g_i)^(b_i-a_i) c_f(N)`.

This is the proposed weight under **point evaluation**. If the coordinate-ring action is defined by `(g.c)(N)=c(g^(-1).N)`, its character is the inverse, with exponents a_i-b_i. State the convention instead of silently reversing the weight.

For polynomial A, the finite entries of f are finite sums of paths, so evaluation is polynomial on the representation variety, including its closed relation locus. For the completed algebra Lambda=hat A, an entry may be a formal path series. On a fixed nilpotent representation space of total dimension d, J^d acts by zero, so truncate every entry modulo J^d. This gives an actual polynomial function on that finite-type nilpotent representation variety. No evaluation of arbitrary formal series at a nonnilpotent matrix is authorized.

Schofield–Van den Bergh, *Semi-invariants of quivers for arbitrary dimension vectors*, arXiv:math/9907174v1 (27 July 1999), defines the projective-map determinants on p.2 and proves their characteristic-zero spanning theorem as Theorem 2.3, p.8. It does not require acyclicity there. Its Section 3 distinguishes the hereditary perpendicular interpretation and explicitly allows an infinite-dimensional cokernel, pp.10–12. [Primary PDF](https://arxiv.org/pdf/math/9907174v1). The PDF's internal 2018 date is not evidence of a new arXiv version. The published record is Indagationes Mathematicae 12 (2001), 125–138.

A useful corollary follows, with its hypotheses explicit. In algebraically closed characteristic zero, take any closed G-stable relation/nilpotence locus Y inside Rep(Q,alpha). Every semi-invariant of a fixed weight on Y lifts to one of that weight in the ambient coordinate ring: twist by the inverse character and use exactness of invariants for the linearly reductive group G=product GL(alpha_i). Restrict the preceding determinant spanning theorem. The resulting restricted determinants span the semi-invariants on Y. The path matrices descend to projective maps for A, but their injectivity need not survive the relation quotient. This is a legitimate extension to the dessin relation variety; it does not transfer hereditary homological hypotheses. The characteristic-zero reductivity input is standard; see Milne, [Reductive Groups](https://www.jmilne.org/math/CourseNotes/RG.pdf), 5.18. No characteristic-p lifting/spanning assertion is made here.

## 2. What exactly requires a short resolution

Set M=coker f. For any presentation, without assuming f injective,

`ker Hom(f,N)=Hom(M,N)`.

Write K=im f. From `0 -> K -> P_0 -> M -> 0`, projectivity of P_0 gives

`Ext¹(M,N)=Hom(K,N)/im Hom(P_0,N)`.

Precomposition with the epimorphism `P_1 -> K` embeds Hom(K,N) into Hom(P_1,N). It follows that Ext¹(M,N) injects into coker Hom(f,N). In particular, on the square locus,

`det Hom(f,N) != 0 <=> Hom(M,N)=0 <=> Hom(M,N)=Ext¹(M,N)=0`.

The first equivalence is finite-dimensional injective-implies-bijective linear algebra; the second uses the injection just proved. Therefore it would be too strong to say that every degree-zero/degree-one perpendicular nonvanishing interpretation disappears without injectivity of f.

What does fail without a short resolution is the unconditional equality

`coker Hom(f,N) = Ext¹(M,N)`

and the resulting dimension/Euler identification. If

`0 -> P_1 --f--> P_0 -> M -> 0`

is exact, then applying Hom gives the familiar four-term sequence and

`dim Hom(M,N)-dim Ext¹(M,N)=sum_i (a_i-b_i) alpha_i`,

with higher Ext zero. This remains valid when the finitely presented module M is infinite-dimensional over k. Without injectivity, the two-term **perfect complex** `[P_1 -> P_0]` is still legitimate; its negative cohomology ker f must not be silently discarded in favor of M alone.

Concrete failure of the full Euler identification occurs inside the completed node. Let

`Lambda=k[[x,y]]/(xy)`, `f=times x:Lambda -> Lambda`,

`M=Lambda/(x)`, `N=Lambda/(x,y^2)`.

Hom(f,N) is the zero map on k², so its cokernel has dimension two. The alternating x,y resolution of M gives `Ext¹(M,N)=ker(y:N->N)`, of dimension one. Also Hom(M,N) has dimension two. Thus the module's Hom-minus-Ext¹ number is one, whereas the two-term presentation dimension difference is zero.

Higher derived perpendicularity fails even on a nonvanishing semi-invariant locus. Use the closed locally gentle four-arrow dessin quiver

`a,b:0->1`, `c,d:1->0`, with permitted cycle `a c b d` and forbidden cycle `a d b c`.

Take `f:P_1 --a--> P_0`, `M=coker f`, and N of dimension (1,1) with a=1 and b=c=d=0. It satisfies all dessin relations and is nilpotent. Hom(f,N) is [1], so its determinant is one. The actual projective resolution of M follows the forbidden tail a,d,b,c,a,... . Applying Hom(-,N) gives scalar differentials

`1,0,0,0,1,0,0,0,...`.

Hence Hom(M,N)=Ext¹(M,N)=0, but Ext²(M,N)=Ext³(M,N)=k. Thus Schofield's degree<=1 perpendicular language and all-degree derived orthogonality must not be conflated outside the hereditary/pd<=1 setting. In closed locally gentle completed orders, simple resolutions themselves have nonterminating forbidden arms, so finite pd cannot be assumed merely from a finite quiver.

## 3. Nilpotent degeneration: invariant functions are constant, not all semi-invariants

Assume k algebraically closed and fix dimension vector alpha, total dimension d>0. A continuous finite-dimensional representation of the arrow-adic completion, with discrete target, kills some J^m. Its Loewy filtration

`N=F^0 >= F^1=NJ >= F^2 >= ... >= 0`

strictly descends until zero, so it already kills J^d. Choose a basis at every vertex adapted to this filtration and write its layer complements as W_i^p. Each arrow sends W_i^p into the sum of layers W_j^q with q>=p+1. The one-parameter subgroup acting as z^p on W_i^p conjugates such a component by z^(q-p). Therefore it extends at z=0 to the representation with all arrows zero.

Every orbit closure in the nilpotent locus contains that same zero-arrow representation of the fixed dimension vector. A G-invariant regular function has the same value on a point and this orbit limit. It is consequently constant on all k-points. On the **reduced** affine variety the Nullstellensatz makes it a constant regular function, not merely a pointwise constant function modulo unknown nilpotents. This argument works in any characteristic; it does not require characteristic-zero reductivity. For a nonreduced representation scheme, invariant nilpotent functions would need separate analysis.

This proves only a weight-zero statement. In the same closed four-arrow dessin above, with dimension vector (1,1), the determinant for f given by a is simply the scalar a. It is nonconstant even on the nilpotent locus: set all other arrows zero and vary a. Its point-evaluation weight is g_1/g_0. Thus nonzero-weight semi-invariants survive and can organize stability/moduli even when the affine invariant quotient is a point.

Nor do constant invariants imply trivial isomorphism classes or absence of bands. Already for the nodal algebra, on k² take x=J_2 and y=lambda J_2, where J_2 is the nonzero nilpotent Jordan block. Then xy=yx=0 and the total arrow ideal squares to zero. Different lambda give nonisomorphic modules: any simultaneous isomorphism must commute with the fixed nonzero x and preserve y=lambda x. These are mixed-word band-type parameters, not nonzero eigenvalues of an actual oriented path. Nilpotence kills the latter but does not eliminate all inverse-letter/string-band information.

## 4. Central specialization: polynomial algebra versus completion versus lattices

For a split closed completed dessin order, the common parameter t lies in its closed arrow radical. On a finite-dimensional continuous representation N, t_N is nilpotent, and

`det(t_N-lambda I)=(-lambda)^(dim_k N)`.

For any scalar lambda in k^*, t-lambda is a unit in Lambda, with inverse

`-lambda^(-1) sum_(r>=0) (t/lambda)^r`.

Thus `Lambda/(t-lambda)Lambda=0` for nonzero scalar lambda. A proposed completed finite-length representation with nonzero central eigenvalue contradicts this unit identity. No map from a Laurent-series field to its purported residue field should be substituted for this analysis.

The polynomial node A=k[x,y]/(xy), which is infinite-dimensional, behaves differently. Set t=x+y. It is free of rank two over k[t], with `A=k[t][x]/(x^2-tx)`. Thus multiplication by t-lambda is injective and gives the genuine pd<=1 presentation

`0 -> A --(t-lambda)--> A -> A/(t-lambda) -> 0`.

For finite-dimensional polynomial N, its determinant evaluates the actual characteristic polynomial of t_N. At nonzero lambda the quotient is `k[x]/(x(x-lambda))`, isomorphic to k x k. These nonzero central-character modules do not extend to the t-adic completion. In a general split closed dessin algebra, the analogous regularity can be checked through the product-of-cycle-order embedding; it should not be assumed for an arbitrary central element in an arbitrary infinite algebra.

A Lambda-lattice means a finitely generated Lambda-module which is finite free over R_0=k[[t]]. Nonzero lattices have nonnilpotent t action as R_0-modules. They are not finite-dimensional k-representations. The finite quotients M/t^nM are nilpotent representations, while their compatible inverse system retains the formal parameter. For idempotent projectives P, Hom_Lambda(P,M) is finite free over R_0, so a square map can have an R_0-valued determinant or determinant line. Its reduction at one nilpotent level and its relative/base-ring determinant are distinct constructions. A scalar formal parameter does not by itself create arithmetic Frobenius or an L-factor.

## 5. Which AR category and which primary theorem

There are three separate ambient choices.

1. Polynomial A-modules: infinite-dimensional string-algebra tools are appropriate, with their module finiteness conditions. Crawley-Boevey's author version of *Classification of modules for infinite-dimensional string algebras*, pp.1–4, Theorems 1.1–1.4, includes k[x,y]/(xy), infinite words, finitely controlled and pointwise artinian modules. [Primary author PDF](https://www.math.uni-bielefeld.de/~wcrawley/string-revised.pdf). Published TAMS 370 (2018), 3289–3313, DOI10.1090/tran/7032. The theorem is not automatically a classification of topologically complete Lambda-lattices as algebraic A-modules: those need not be finitely generated/finitely controlled or artinian over A.
2. Complete-order lattices: use the extension-closed exact category lat(Lambda) inside finitely generated modules, with R_0-split underlying short exact sequences. For finite free Lambda over a complete DVR and semisimple generic algebra, the generic-projectivity condition holds for every lattice. Auslander–Reiten's main existence equivalence, *Almost split sequences for Cohen-Macaulay-modules*, Math. Ann.277 (1987), 345–349, introduction p.345, gives an almost split sequence ending at each indecomposable nonprojective lattice; its dual uses generic injectivity. [Primary digitized statement](https://gdz.sub.uni-goettingen.de/fulltext/PPN235181684_0277/00000351?_format=xml), [DOI](https://doi.org/10.1007/BF01457367). Its general hypotheses are complete local equidimensional Gorenstein base and finite maximal-CM algebra; the actual endpoint must be projective at nonmaximal primes. Endomorphism spaces here are usually infinite-dimensional over k, though finite over R_0.
3. Finite-length Lambda-modules: these are the union of nilpotent representation categories of Lambda/J^n. Each fixed quotient is an Artin algebra with its usual AR theory. Its almost split sequence need not stay almost split after enlarging the ambient category or increasing n. No blanket existence assertion for every endpoint of the whole union is established in this report. Lattices, except zero, are not in that union, and finite-length modules, except zero, are not lattices.

Bautista–Liu–Paquette's arXiv:1109.3176v1, *Representation Theory of an Infinite Quiver* (2011; published as *Representation theory of strongly locally finite quivers*, PLMS106 (2013), 97–162), defines strongly locally finite as locally finite plus finitely many paths between each pair, p.4. Theorem2.8, pp.15–16, constructs AR sequences for finitely presented/nonprojective and finitely copresented/noninjective endpoints. [Primary PDF](https://arxiv.org/pdf/1109.3176v1). A surviving permitted cycle gives infinitely many paths at a vertex, so a closed dessin quiver fails interval finiteness. Merely saying its valency is at most two does not repair this.

Paquette, *Irreducible morphisms and locally finite dimensional representations*, arXiv:1508.04353v3 (4 January 2016), Theorem4.1 and Corollary4.2, p.10, give endpoint finite-(co)presentation criteria in modules over the stipulated Hom-finite Krull–Schmidt k-category. [Primary PDF](https://arxiv.org/pdf/1508.04353v3). The projective path category of a finite dessin with permitted cycles has infinite-dimensional Hom at cycle vertices; a completed order has the analogous Hom-finiteness failure. The theorem cannot simply be relabeled as one about all dessin lattices.

Liu–Ng–Paquette, *Almost split sequences and approximations*, arXiv:1203.5009v1 (2012), supplies the proper transfer framework: Corollary3.5, p.12, uses a Krull–Schmidt functorially finite exact subcategory; Theorem3.7, p.13, gives stable-approximation criteria under its artinian-base/Ext-finite hypotheses. [Primary PDF](https://arxiv.org/pdf/1203.5009v1). One must verify those hypotheses before transporting AR sequences. In particular an R_0-finite lattice category is not automatically a k-Hom-finite category. An AR mesh is not, by definition, a 3-by-3 diagram.

## 6. A fully proved completed nodal/dessin AR calculation

Take `Lambda=k[[x,y]]/(xy)`, `R_0=k[[t]]`, t=x+y, and let `X=(x)`, `Y=(y)` as Lambda-modules. The normalization is `B=k[[x]] x k[[y]]`; its conductor is `tB=(x) x (y)`. Define BM **inside the total quotient module**, not by an unjustified flat tensor operation.

For any lattice M, write `Mbar=BM` inside its generic module. Each branch of Mbar is free over its branch DVR, so `Mbar=k[[x]]^r x k[[y]]^s` after choosing bases. The conductor gives

`t Mbar subset M subset Mbar`.

Modulo t Mbar, M is a subspace W of `k^r x k^s`. The projections of W onto both factors are onto because BM=Mbar and Nakayama. Let U=W intersection (k^r x 0), V=W intersection (0 x k^s). The residual quotients k^r/U and k^s/V are identified by W. Choose bases for U,V and this common quotient. Under independent branch basis changes, W becomes a direct sum of pure first-branch lines, pure second-branch lines and diagonal pairs.

Lifting the decomposition yields

`M isomorphic Lambda^h directsum X^a directsum Y^b`.

A full first-branch module k[[x]] is isomorphic to X by multiplication by x; likewise for Y. Thus Lambda,X,Y are exactly the indecomposable lattice types. Their endomorphism rings Lambda,k[[x]],k[[y]] are local, so these summands really are indecomposable. This proof is elementary conductor descent for this order, rather than an imported finite-dimensional gentle classification.

Now consider

`0 -> Y --inclusion--> Lambda --times x--> X -> 0`.

It is exact since ann(x)=Y. It does not split: any map X->Lambda has image in ann(y)=X, and composing with multiplication by x gives an endomorphism of X divisible by x, never identity.

For right almost splitness, it suffices to test an arbitrary finite sum of the three indecomposables. Every Lambda->X factors through the displayed epimorphism. Hom(Y,X)=0. An endomorphism of X which is not a unit is divisible by x, and factors through `X -> Lambda --times x--> X` using the natural inclusion and an appropriate scalar. If a map from a direct sum to X has a unit X-component it is a retraction; otherwise all its components have the factorizations just given. Hence every non-retraction factors through Lambda->X.

Dually, every non-section out of Y factors through its inclusion in Lambda: Hom(Y,X)=0, maps Y->Lambda land in Y, and nonunit endomorphisms of Y are divisible by y. The same component test handles direct sums. Endomorphisms of the middle Lambda which fix its epimorphism to X, or its incoming Y, have constant term one and are units, proving minimality. This is an actual AR sequence in lat(Lambda). Swapping x and y gives

`0 -> X -> Lambda --times y--> Y -> 0`.

In particular `tau X=Y`, `tau Y=X`. The lattice AR quiver has vertices Lambda,X,Y and arrows `Y->Lambda->X` and `X->Lambda->Y`. The mesh composites are multiplication by xy or yx, hence zero. Lambda is projective, so there is no non-split AR sequence ending at Lambda. This is fully compatible with the irreducible incoming radical map from X directsum Y.

For an independent Ext check, the alternating x,y resolutions give `Ext¹(X,Y)=k`, `Ext¹(Y,X)=k` and zero self-Ext¹ for X and Y. The displayed nonsplit sequences represent their nonzero extension classes.

The node is itself a clean sphere dessin example: beta(z)=4z(1-z) has two simple points above zero, one degree-two point above one and a degree-two pole at infinity. Its black permutation is the identity on two darts and its white permutation is their transposition. The two length-one permitted cycles become the two loops x,y paired at one quiver vertex, with forbidden xy,yx. Thus this calculation stays within the requested infinite dessin/order scope.

## 7. The requested nonzero 3-by-3 exact diagram

Repeat the AR row ending at X, and use multiplication by t as all three vertical maps. Add its reduction modulo t:

```
0 -> Y       -> Lambda       --x--> X       -> 0
     | t          | t                 | t
0 -> Y       -> Lambda       --x--> X       -> 0
     |            |                   |
0 -> Y/tY    -> Lambda/tLambda   -> X/tX    -> 0
```

All nine displayed modules are nonzero. Each column is short exact because Y,Lambda,X are finite free R_0-modules. The bottom row is exact because tensoring the top row with k=R_0/(t) has no Tor contribution from its free quotient X. This is a valid difference from tensoring the infinite resolution of the nonflat simple, where extra homology was previously found.

In Lambda/tLambda, set epsilon=x, so y=-epsilon and epsilon²=0. Identify Y/tY with k using its generator y and X/tX using its generator x. Then the bottom row is

`0 -> k --(-epsilon)--> k[epsilon]/(epsilon²) --augmentation--> k -> 0`.

The minus sign follows from the chosen generator y; it may be removed by a basis change. The quotient is the special fiber of the actual infinite order and the row is derived from its genuine AR sequence. This is not a standalone finite-dimensional replacement for the order.

The diagram does not prove that every AR mesh has a three-by-three layout. General AR sequences have middle terms with variable numbers of indecomposable summands. Pullbacks, pushouts, projective covers or reduction by a regular central parameter can create 3-by-3 diagrams under their own hypotheses. Pulling an AR extension back along a projective epimorphism splits that row; being part of such a diagram is not itself an almost-split property. Likewise preservation of the displayed node row under reduction does not license arbitrary specialization of AR sequences for general orders.

## 8. Concrete next calculations and source coverage

The useful next construction is now narrow: formalize the node lattice classification, the two actual AR sequences, their maps and the t-reduction diagram, then calculate determinant lines or semi-invariants of specified projective maps in that exact setting. In parallel, enumerate balanced projective-map determinants on a fixed closed dessin representation variety, retaining their weights and higher syzygies. If an arithmetic realization is proposed, separately define its Frobenius/flow and compare its determinant; neither semi-invariants nor an AR translation supply that identity automatically.

Source coverage was focused and explicit: Schofield–Van den Bergh pp.1–3, Theorem2.3 and proof conclusion pp.8–9, and Section3 pp.10–12; BLP definitions p.4, AR endpoint construction pp.13–16 and stated category criteria p.24; Paquette introduction and Theorem4.1/Corollary4.2 on p.10; Liu–Ng–Paquette exact-category/pushout conventions and transfer results pp.10–13; Crawley-Boevey definitions and Theorems1.1–1.4 pp.1–5 plus proof structure pp.23–24; Auslander–Reiten's actual existence equivalence in the primary p.345 introduction; Milne5.18. These are not claims to have read every proof in all six papers. The nodal classification, AR factorization, three-by-three diagram, weight calculation, nilpotent degeneration and higher-Ext counterexample above are independently supplied derivations.

No shared file was edited and no software was installed. No unproved arithmetic purity, Galois realization, number-field determinant identity or GRH consequence is claimed.

## Implementation and new article review addendum

At root's explicit request, implemented only `scripts/check_dessin_diamonds.py` and its requested generated `outputs/checks/2026-11-03-dessins/diamond-checks.json`. Reused the project's standard-library Fraction matrix routines, without dependencies. API `checks()` is pure; `run(write_output=False)` returns the same report without writing. A standalone writer run and a fresh pure-import comparison with the saved JSON both passed.

The artifact constructs all nine H_3 basis representations and twelve signed maps from the independent diamond report. Its checks cover 54 closed-dessin relation identities, 72 arrow-commutation identities, four exact meshes and twelve vertexwise exactness/rank calculations. A negative control reverses one essential mesh sign and confirms that the composite becomes nonzero; the checker therefore does not mistake an unsigned square for a chain complex. The output records words, basis vertices, arrow/map nonzero entries, dimension vectors and all boundary ranks.

For the actual completed node, the checker uses its R_0-free bases (1,x),x,y and jet rings R_m=Q[t]/(t^m). It constructs x,y actions and both AR-row maps, not merely a standalone dual-number complex. Five jet levels give ten exact rows. Four nonzero 3-by-3 diagrams use the **injective** map t:R_m -> R_(m+1) and constant-term quotient to the fiber; there are twelve exact columns and thirty-two commuting squares. This avoids the false assertion that multiplication by t is injective on a single fixed truncated ring R_m. The fiber injection is correctly -epsilon under the chosen y generator. These bounded exact diagnostics do not by themselves prove the infinite lattice classification or the almost-split factorization property, which remain the independent prose proofs above.

Also independently read every line 1–251 of the newly written `papers/dessin-core.tex`. The order, explicit forbidden-chain resolutions, dual-dessin/cycle determinant, semi-invariant/nilpotent statements, node lattice AR proof and HLS quotient category correctly match the preceding reviewed results. The square-map Hom/Ext¹ nonvanishing refinement is now included, with its node and higher-Ext counterexamples. The HLS import is expressly intrinsic to the quotient-annihilator category. Other C*/Schur/arithmetic sections were read for consistency, but this pass is not a fresh primary-source audit of all their imported theorems.

Two literal precision points were sent to root: the projective formula at lines 43–45 uses the last arrow a_n, so must be restricted to n>=1 with P_0=e_iA separately (or use an endpoint convention for the empty path); and the Cauchy-kernel bound R_0^(-2) should explicitly have R_0>0, with the all-zero case treated separately if desired. Neither issue is a counterexample to the intended theorem on its proper domain. Extended dessin details were not yet present in this review snapshot.

Snapshots:

- `scripts/check_dessin_diamonds.py`: 12859 bytes, 256 lines, SHA-256 `1779c13a5e908e22c10425dffff94f2355b9729cd477230145dc9dba3fe13956`.
- `outputs/checks/2026-11-03-dessins/diamond-checks.json`: 31035 bytes, 1615 lines, SHA-256 `93bf417666eca6bd7f58b23bf7ced32a71923b51ab95532e57e76c828bca245d`.
- `papers/dessin-core.tex`: 37260 bytes, 251 lines, SHA-256 `5b59da7dabc05400abbc9a32b8769aee39cab71852a11fac01bcd20c31a54f11`.


## Final expanded-article and Lean review (2026-11-03)

Read every line 1–258 of `papers/dessin-details.tex` and every line 1–359 of `lean-analytic/DessinNodeOrder.lean`, plus all 110 lines of `lean-analytic/DessinInvariantComponents.lean`. Previously read all 251 lines of the initial core; reread the current order, resolution, invariant and lattice-AR sections to check the revised literal scopes. This pass was read-only: only this temporary report was updated; no manuscript, Lean file or shared check output was written.

The expanded cycle-order proof (details3–11) correctly maps each branch path into its matrix-corner power series, glues only paired diagonal constants and preserves positive-length independent coefficients. The conductor argument yields an actual finite torsion-free DVR module of rank sum(length(c)^2), hence freeness. In the node, the explicit coordinates a(u)+b(u)x and both annihilator identities are valid formal-series identities. The source does not infer those infinite statements solely from finite jets.

The forbidden-chain resolution (core39–54, details13–31) has actual idempotent projectives and exact kernels coefficientwise in the completion. The displayed nodal alternating maps and theta arm lists are correct. Minimality is graded in the polynomial algebra and radical-adic in the completion; the text appropriately avoids declaring the polynomial arrow ideal its ordinary Jacobson radical. Ext counts against residue simples and the row-order identity E C=I are justified, with matching internal shifts. Positive periodic syzygy tails are distinguished from a simple being periodic. The complementary-relation Ext product is forbidden-word concatenation, with the stated possible Yoneda opposite convention. This supplies a Koszul calculation, not an equivalence of all completed derived categories.

The semi-invariant Hom/Ext scope (core78–103; details37–48) matches the independent argument in this report: square Hom-map invertibility detects Hom(M,N)=0 and hence Ext1(M,N)=0 even without injectivity of f, whereas equality of the entire cokernel with Ext1 and higher Ext vanishing require the actual short projective resolution. Both explicit node and four-periodic higher-Ext counterexamples have the claimed dimensions. The positive-weight semi-invariant survives although all invariant regular functions on the reduced nilpotent representation variety are constant. Finite R-free lattices and continuous finite-length k-modules remain distinct throughout.

The actual nodal AR classification/factorization and reduction diagram (core137–152; details nodal diagram) agree with Sections6–7 of this report. All nine entries are modules arising from the order and parameter reduction; -epsilon in the bottom injection is correct for the chosen y generator. The proof establishes right/left almost-split factorization in the lattice exact category, not merely exactness or a pattern of dimensions. The classification closes the factorization argument for arbitrary finite direct sums. A projective vertex has no nonsplit AR sequence ending there.

The HLS table, travel words, basis dimensions, all twelve signed morphisms and four mesh sequences (details120–154) agree exactly with the checker. Vertexwise injectivity/surjectivity plus zero composite and dimension equality prove these are exact, and HLS's specialized hook/cohook theorem supplies the stronger intrinsic almost-split property. The quotient annihilator category is explicitly the relevant category; inflation alone does not make those sequences almost split in the full order category. The source's dimension-grid drawing is not falsely described as having short-exact rows and columns.

Literal issues found and sent to root:

1. Core's n=0 formula was corrected: P0=e_i A is now separate and the last-arrow formula is restricted to n>=1. The Cauchy bound is now r R0^2<1, which also covers R0=0 without taking its inverse.
2. Details154 originally called E=ab type(1,1). The correct type is (2,2), indispensable for the cited HLS Proposition3.12. Reread confirms this correction is present.
3. Details31 originally said the next differential vanishes precisely for a forbidden join. For the suffix comparison lift the next arrow differential generally does not vanish; it agrees with its suffix counterpart. Reread confirms the corrected paragraph now states commuting suffix differentials, standard shift signs, and the forbidden indexing-word existence condition. The Ext product conclusion remains correct.
4. Details33 initially said an arbitrary chain endomorphism acts on the determinant line. The determinant-functor action must be restricted to chain automorphisms/quasi-isomorphisms; a generic 1-zF action is instead rational on its invertibility locus. In odd degree its contribution is an inverse determinant, which is not regular at a singular endomorphism. Root has acknowledged and is qualifying this literal statement; final snapshot status must be read from the lines below.
5. Details256 calls its displayed symmetric-square convention 'scaled monomial'. The displayed matrix is exactly the ordinary monomial basis (e1^2,e1e2,e2^2) used in Lean49. The matrix is universally correct; only the basis adjective needed correction. Root has been notified.

Independent Lean verification used the existing pinned Lean4.24.0/mathlib4-v4.24.0 environment and `lake env lean -DwarningAsError=true ABSOLUTE_FILE`, without producing an olean output. Both files exited zero with no warnings. All twenty node declarations and ten invariant-component declarations printed their actual types and axioms. Only the standard foundational dependencies propext/Classical.choice/Quot.sound occur (some CK1 lemmas use fewer); no custom arithmetic axioms or sorryAx occur.

The node formalization proves statements about the genuine subring of two PowerSeries fields with equal constant coefficient, not an abstract ring with assumed annihilator axioms: diagonal injectivity; nonzero x,y; xy=yx=0; actual branch factorizations; both annihilator identities; regular parameter; surjective augmentation and its kernel/range; three alternating kernel-equals-range identities; genuine regular/product module projectivity. Its coordinate result is a bijection, not yet a packaged R-linear equivalence or a general finite-free order theorem. These limits match details249. It does not formally prove the full lattice classification or almost-split property.

The invariant file proves three CK1-collapse components, a cleared determinant change-of-bases identity with an actual inverse, symmetric-square zero/identity/composition/relation preservation, the actual degree-two trace character identity, and failure of the fixed central parameter on that explicit Schur-transformed node representation. Its square-matrix index type and matrix equalities are honest universal algebraic component statements; they do not claim a formal general semi-invariant spanning theorem, LR decomposition, analytic positivity, C* K-theory or GRH. This matches details251–256 after the harmless basis-word correction.

Other expanded C*/arithmetic/recent-source paragraphs were read for internal consistency and preservation of conditional scope, not freshly re-audited against every cited primary paper in this pass. No arithmetic determinant identity, number-field weight theorem or GRH proof is supplied or inferred by the AR/semi-invariant constructions or these thirty Lean components.

Snapshot hashes at report update:
- `papers/dessin-core.tex`: 37414 bytes, 251 lines, SHA-256 `63cfd82ed093bd6f4922297ee282104ca1111c3cf85410c803f3e4490a6973ab`.
- `papers/dessin-details.tex`: 38189 bytes, 258 lines, SHA-256 `4447a2196ec38da8c0fab67ed54a4da0f6e3cea17befd9123ad549f0821ddcc1`.
- `lean-analytic/DessinNodeOrder.lean`: 12500 bytes, 359 lines, SHA-256 `e23b7cb94dd2e6fff66afafe654a301a303a4647b1a847f90a39f9f41c43a2f7`.
- `lean-analytic/DessinInvariantComponents.lean`: 4399 bytes, 110 lines, SHA-256 `d2d7f69118c646a1c20797639fe014cc915b41aac15a3294b48bea4c56cc9cd2`.

Final reread: details33 now explicitly distinguishes automorphism/quasi-isomorphism determinant-functor action from rational 1-zF action on the invertibility locus; that correction is resolved. A fresh pure `checks()` import (with the project scripts directory on sys.path) passed and deep-equalled the preserved diamond JSON. The first isolated import omitted that module search path and failed before checks; this was an invocation-path issue, corrected without editing sources. The only remaining communicated literal issue at this reread is the harmless adjective scaled in details256.
Latest details snapshot: 38189 bytes, 258 lines, SHA-256 `7a64197a6d4e28d57b81377158eba1864beb4856bbde1cbdbf550d21b1f5811b`.
