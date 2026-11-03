# Full review of Surface II and a rigorous route from resolutions to arithmetic determinants

## 1. Exact artifact, coverage, and limits

The reviewed work is Amelie Schreiber, **Surface Algebras and Surface Orders II: Affine Bundles on Curves**, [arXiv:1812.00621v1](https://arxiv.org/abs/1812.00621v1), submitted 3 December 2018. The arXiv record lists only v1. The downloaded PDF has 26 pages, an internal date of 27 November 2024, and the same arXiv v1 identifier. Its PDF metadata also records compilation on that date; this is not evidence of a separately numbered arXiv revision.

Downloaded artifact:

`/Users/amelieschreiber/Documents/LaTeX-projects/GRH/research/literature/projective/surface-II-1812.00621v1-20261103-9af2d671.pdf`

Size: 294818 bytes. SHA-256: `5f2e498421e3121b6b18ba68d6309a1f6a6e3545b1bc451856b34d5a2555e7aa`.

I read **all 26 pages**, covering every section, definition, example, displayed construction, conjectural discussion, explanatory argument, footnote, and bibliography. Text was read in page groups 1–5, 6–10, 11–15, 16–20, 21–26. I additionally rendered and visually checked pages 9, 17, 18, 21, 23, and 24 to verify diagrams and formulas that extraction could distort. All page references below are printed PDF page numbers, which agree with PDF page indices plus one.

This is a full reading of the target paper, not a full reproof of all references it invokes. The external literature review is focused: exact relevant statements and hypotheses were checked, rather than claiming full readings of SGA, Weil II, BBD, or modern Langlands papers. No source clone, shared manuscript, planning file, Lean source, environment, or existing dataset was edited. Only new literature/review artifacts were created.

## 2. Overall mathematical assessment

The paper is best used as a source of geometric and representation-theoretic proposals, with some standard local constructions that can be made precise. Its final global gluing and representation-correspondence assertions are not established by the displayed constructions. Several intermediate identifications fail by elementary counterexamples. These failures do not refute the classical Lusztig/Magyar results or the possibility of a corrected surface-order theory.

The useful components are local hereditary orders, nodal residue gluing, periodic lattice descriptions, and nilpotent cyclic-quiver geometry. A rigorous projective-resolution program can build on those components after correcting the category and finiteness assumptions. No argument in this paper supplies arithmetic Frobenius traces, a global number-field purity theorem, a completed Dirichlet L-function determinant, or GRH.

The absence of numbered theorems, expressly discussed on p.3, is not itself a mathematical objection. The objections below concern actual statements and missing constructions.

## 3. Coverage ledger for all sections

| Section and pages | Audit outcome and usable interface |
|---|---|
| §1, pp.1–4 | Finite covering/monodromy data are useful, but puncture count, deck groups and field extensions require the distinctions in §4 below. No categorical Langlands theorem is specified. |
| §2, pp.4–10 | The nodal algebra is useful. Literal inverses and group-algebra quotients destroy the proposed algebra; the commutative-algebra pictures also need grading and module-category corrections. Conjecture 2.4 is not a theorem. |
| §3, pp.10–11 | The finite GL/Borel setup is standard. The loop subsection is not developed into an analytic or algebraic comparison theorem. |
| §4, p.11 | Completed local rings and fraction fields are appropriate formal objects; their spectra are not analytic disks. |
| §5, pp.11–12 | The quadratic monomial/path-algebra definition provides a combinatorial starting point. Formal completion, ordinary path algebra, and finite-dimensional quotient must remain distinct. |
| §6, pp.12–15 | Local vertex orders and residue fiber products are recoverable. A common center/base and precise gluing maps are needed. Heredity of the normalization does not imply finite projective dimension after gluing. |
| §7, pp.15–18 | The lattice quotient model is useful after fixing full-rank periodic chains, residue-field dimensions, and Iwahori/unit-group distinctions. |
| §8, pp.18–20 | Periodic permutation methods apply. Affine versus extended affine Weyl groups and formal versus smooth loops must be separated. |
| §9, pp.21–22 | The asserted global bundles and induced fiber products lack a descent diagram and local-triviality proof. The displayed nodal square has an incorrect ideal. |
| §10, pp.22–23 | The nilpotent-matrix construction has a correct classical version. It does not classify arbitrary representations or give an arithmetic trace formula. |
| §11, pp.23–25 | Cyclic-quiver geometry must use nilpotent cyclic compositions, correct ambient dimension, and the invertible resolvent/lattice construction. Global seam compatibility remains unproved. |
| §12 and references, pp.25–26 | Future moduli work is proposed; the needed equivalence, Frobenius realization and determinant/purity comparison are not proved here. |

## 4. Exact false identifications and corrections

### 4.1 Two removed points give one generator, not two

At pp.2–3 and again p.22, the specified base is P1(C) minus {0,1}. This is biholomorphic to C*, with fundamental group Z. A free group on two generators requires P1 minus **three** points, normally {0,1,∞}. A plane minus {0,1} has that same three-puncture compactification, but is a different written space. The distinction changes the covering group and cannot be ignored in a monodromy construction.

For a connected covering classified by H⊂π1(Y), the deck group is N(H)/H, whereas its transitive monodromy group is π1(Y)/core(H). They coincide as π1(Y)/H when H is normal, i.e. for a regular/Galois cover. For instance a transitive degree-three action with monodromy S3 can have trivial deck group. Thus a general cover cannot be treated as a Galois extension with monodromy equal to its automorphism group. Field automorphisms do match deck transformations of the corresponding finite complex-function-field cover, but need not have order equal to its degree.

### 4.2 The literal group-algebra quotient is zero

At p.6, and in the chain on p.22, x and y are treated as free-group generators while xy and yx are killed. In any unital group algebra, xy is a unit. An ideal containing xy contains `(xy)^−1(xy)=1`, so the quotient is the zero ring.

By contrast `k⟨x,y⟩/(xy,yx)` with **noninvertible** arrows is the nonzero nodal algebra `k[x,y]/(xy)`. The path category of the Cayley graph has many vertex idempotents and is not the one-object group algebra. A path/category/orbit construction can be defined, but it does not justify identifying these algebras.

Formal inverse letters in string-module combinatorics describe orientation; they do not make the underlying arrow operators invertible. This correction is essential when converting string walks into projective resolutions.

### 4.3 Localizing a node does not make both branches invertible

The p.9 construction tries to retain xy=0 while making x and y invertible. In a nonzero unital ring this is impossible: multiply by x^−1y^−1 to get 1=0. Also `C((x))/(x)=0`, because x is a unit; it is not C. Consequently the displayed residue maps from Laurent-series fields cannot be the residue maps used for nodal gluing.

The correct normalization of `A=C[[x,y]]/(xy)` is

`B=C[[x]] × C[[y]]`,

and its total quotient ring is `C((x)) × C((y))`. The image of x in that product is `(x,0)` and of y is `(0,y)`; neither is a unit. Their sum is a non-zero-divisor. The conductor square is

`A ≅ B ×_(C×C) C`,

where the map C→C×C is diagonal and B→C×C evaluates each branch at its origin. Equivalently, A consists of pairs of power series with the same constant term. This is a genuine fiber product, with no evaluation of a Laurent-series field at zero.

The p.21 square uses the ideal `(x,y)` in its upper-left ring. That quotient is C and is not this fiber product; the nodal construction needs `(xy)`.

### 4.4 Formal spectra, analytic disks, and smooth loops are different

`Spec C((t))` has one point because C((t)) is a field. It is not a punctured analytic disk, and cannot literally deformation retract to a circle. The formal disk is modeled by `Spf C[[t]]`; algebraic/formal patching and analytic disk patching have separate formulations.

Likewise C((t)) contains arbitrary formal coefficients. The series `∑ n! t^n` is a legitimate formal power series but diverges on every nonzero complex disk. Substituting t=exp(iθ) does not define a smooth loop. Thus the identifications at pp.9–10 and p.18 between formal Laurent loops and all smooth circle-valued loops are not literal isomorphisms. Laurent-polynomial loops embed in appropriate analytic loop groups; their formal and smooth completions must be specified separately.

Tensor products such as `g⊗_C S1` and `Z/nZ⊗_C C((t))` on pp.9–10,18–20 are not defined in the stated categories: a circle or finite cyclic group is not a C-vector space. Replace them by a function algebra, a loop space, or a complex representation, with an actual comparison map.

### 4.5 Local Galois automorphisms must fix the base parameter

For `C((t^(1/n)))/C((t))`, the cyclic automorphism sends the **root** `t^(1/n)` to `ζ_n t^(1/n)` and fixes t. Sending t itself to ζ_n t generally moves the base field pointwise, so it is not that relative Galois automorphism. See pp.2 and 10.

In characteristic zero with algebraically closed constant field, the algebraic closure is the directed union of Puiseux fields; it is not their topological completion. The associated absolute Galois group is the inverse limit of the finite cyclic groups. These are a direct-limit field and an inverse-limit group, not the same construction. Neither local procyclic groups nor their direct products determine global geometric monodromy without generators, relations and gluing maps. They also do not provide arithmetic Frobenius elements over Q.

### 4.6 Some §2 representation statements need narrower categories

The module `m^n` in C[x,y] is infinite dimensional over C, whereas `Sym^n(C²)` has dimension n+1. The correct graded statement is `m^n/m^(n+1) ≅ Sym^n(C²)`. A general R-linear map R→R is multiplication by an arbitrary polynomial, e.g. 1+x, rather than one lattice path; paths give a monomial basis of such maps.

Finite-dimensional sl2(C)-modules form a semisimple category. Modules over the node include nontrivial self-extensions of its residue field, for example x acting by a nonzero 2×2 nilpotent Jordan block and y by zero. These full categories cannot be equivalent. A genuine Gel'fand–Ponomarev/Harish-Chandra comparison needs its particular category, block, parameters and relations; it is not obtained just by the displayed matrices on pp.4–8.

The vertices of the free-group Cayley graph are countable; Cantor space is uncountable. The graph's boundary of ends is a Cantor space, not the vertex set itself. After an initial letter, an unrestricted reduced F2 word has three legal next letters, not two. Additional string relations can restrict letters, but then one is coding a different constrained path language.

### 4.7 Iwahori orders are not Laurent Borel subalgebras

For n=2 the hereditary vertex order in the paper is

`H=[[R,tR],[R,R]]`, with R=k[[t]].

Its generic fiber is all M2(k((t))), of dimension four over k((t)); a triangular Borel Lie algebra has dimension three. Therefore `H` is not `b[[t]]` with generic fiber `b((t))`, as used on pp.21–22. It is an Iwahori **order** whose reduction has a triangular form; its **unit group** is an Iwahori subgroup. The order also contains nonunits and zero.

The inclusion at p.16 from M2(k((t))) into M2(k[[t]]) is backwards. The valid inclusion goes from integral matrices to Laurent matrices.

### 4.8 Full affine flags require full-rank periodic lattices

A full affine lattice chain is, with one consistent convention,

`L0 ⊃ L1 ⊃ ... ⊃ Ln=tL0`, with `dim_k(Li/Li+1)=1`.

Every Li has rank n over k[[t]]. A rank-one submodule Re1 in Fn for n>1 is not such a full-rank lattice; `Li/Li+1` is a residue-field vector space, not an F-vector space. This fixes the incompatible chain and dimension statements on p.17.

The homogeneous-space formulas must remain

`Gr=GLn(F)/GLn(R)`,
`Fl_aff=GLn(F)/I`,
`GLn(R)/I ≅ GLn(k)/B`.

The last quotient is the finite flag variety; it is not the whole affine flag variety as asserted at p.18. The topological basis of Laurent powers is not an ordinary Hamel basis, and an R-lattice is not closed under arbitrary F-scalars. Magyar explicitly uses the relevant topological sense in [§1.1, pp.1–2](https://arxiv.org/pdf/math/0210151v1).

### 4.9 Affine and extended affine Weyl groups must be separated

The sum condition on p.18 is the binomial coefficient `(n+1 choose 2)`; visual review confirms this, despite misleading plain-text extraction. That condition is not an error.

With it, however, translations have total exponent zero: the affine group is `Sn ⋉ {a∈Z^n:Σa_i=0}`. The extended group for GLn is `Sn ⋉ Z^n`. They are conflated in the p.19 decomposition.

A finite n-cycle permutation matrix has nth power I, whereas the twisted shift has nth power tI. The latter lies naturally in the extended affine picture and normalizes the Iwahori order by conjugation; it is not the image of that finite cycle under an unchanged group embedding. Moreover, left multiplication by the normalizer is generally semilinear for the induced conjugation automorphism, not automatically a homomorphism of left H-modules.

### 4.10 Nilpotent cyclic representations are not only zero-composition representations

For a two-cycle with dimensions (2,2), take A1=I2 and A2=J2, a nonzero nilpotent Jordan block. Both cyclic compositions are nilpotent, so this is a nilpotent cyclic-quiver representation; neither composition is zero. The product-equals-zero condition on p.24 is strictly stronger. It describes a circular-complex type subvariety, not every nilpotent cyclic representation.

Also distinguish h, the number of quiver vertices, from N=Σd_i, the total ambient dimension. Arbitrary dimension vectors do not allow identifying both numbers with a ramification index.

The zero representation maps to a zero block matrix, which is not in GL_N(F). The correct invertible construction uses a finite nilpotent resolvent, of the form `t^(N−1)(1−M_tilde)^−1`, then acts on a periodic lattice chain. Magyar's exposition itself has an informal GL label on an intermediate block-matrix display, but its subsequent resolvent is the operative construction; the zero-block issue is a correction to that intermediate label, not a refutation of Lusztig's theorem.

The precise classical statement concerns open opposite-Schubert loci (in general a union) attached to nilpotent cyclic data, not a classification of every module of a glued surface order. [Magyar, §2.2, pp.9–12](https://arxiv.org/pdf/math/0210151v1).

## 5. The bundle and Langlands gaps, stated precisely

### 5.1 A tensor product of a coefficient algebra with O_X is not the missing descent construction

One can define a constant quasicoherent O_X-module `A⊗_C O_X`. If A is infinite dimensional, this is not a finite-rank vector bundle. A flag ind-scheme is not a vector space to which that tensor notation applies literally. A constant flag-family can instead be defined as `X×Fl` in a suitable ind-scheme category.

A constant seam equation over C gives another constant subfamily. To obtain a nontrivial family, specify charts, transition morphisms, their cocycle, representability and local triviality. Gluing a node in the **center** changes the local curve geometry to a singular nodal curve; it is not automatically a subbundle on the original smooth curve. The pp.21–25 discussion does not resolve these alternatives.

GL_n, as a functor on commutative rings, preserves an actual fiber-product ring diagram of a fixed matrix size. Quotients by Borel/Iwahori subgroups need not preserve arbitrary fiber products. In particular, pulling back groups or corner rings does not by itself produce a fiber-product identification of their homogeneous spaces. The needed quotient maps, compatible subgroups, possible torsor obstructions, and functor-of-points equivalence must be proved.

### 5.2 There is a rigorous replacement: formal patching

[Beauville–Laszlo, *Un lemme de descente*, C. R. Acad. Sci. Paris 320 (1995), 335–340; author preprint, theorem on PDF pp.1–2](https://math.univ-cotedazur.fr/~beauvill/pubs/descente.pdf) gives the relevant interface. For a ring A and a non-zero-divisor f, projective finite modules can be patched from A[1/f] and the f-adic completion, together with an isomorphism on the punctured completion. On a curve this supplies the missing transition data between the complement of a point and its formal neighborhood.

This explains how loop-group transition matrices and affine Grassmannians describe modifications of bundles on a curve. It does not identify the formal disk with a topological disk or prove that arbitrary diagonal seam equations give the desired global moduli functor.

### 5.3 What a geometric Langlands theorem would additionally require

A local Schubert embedding is not a global categorical Langlands equivalence. One must specify the reductive group and its dual, the curve, the automorphic category on Bun_G, the local-system/connection stack on the spectral side, support and singular-support conditions, Hecke correspondences, the functor, and the properties claimed for it.

The relevant classical geometric Satake statement concerns a tensor category of equivariant perverse sheaves on an affine Grassmannian and representations of the dual reductive group; it does not assert that every loop-algebra module is an individual Schubert variety. See [Mirković–Vilonen, arXiv:math/0401222](https://arxiv.org/abs/math/0401222). A modern primary comparison point is [Gaitsgory–Raskin, arXiv:2405.03599](https://arxiv.org/abs/2405.03599), which states its characteristic-zero de Rham/Betti functor and categorical setting explicitly.

Surface II does not define and verify these ingredients. Its proposed representation/geometry picture should be formulated as a narrower theorem or conjectural program. Even a valid characteristic-zero geometric Langlands result would not by itself prove an arithmetic number-field L-function zero theorem.

## 6. What genuinely carries into projective resolutions

### 6.1 A correct local algebra and its projectives

The nodal fiber product, local hereditary matrix orders over complete DVRs, and residue identifications can be used to define explicit complete algebras and their vertex/edge projectives. Work over a specified central ring or coherent sheaf of orders. With heterogeneous local centers, prove finite generation and torsion-freeness over that center rather than silently treating every component as an order over one common field.

The standard twisted shift S with top-right entry t satisfies S^n=tI and conjugates the displayed lower-Iwahori order to itself. That is a valid calculation in the chosen convention. It describes a normalizer action on projective types; it does not make t a unit inside the integral order or turn S into an untwisted finite-order automorphism.

### 6.2 Normalization does not preserve the required finite projective dimension

Here is a complete test case. Let `A=k[[x,y]]/(xy)` and `M=A/(y)`. Then

`... → A --y→ A --x→ A --y→ A → M → 0`

is a minimal infinite free resolution: the last quotient has kernel (y), `ann(y)=(x)` and `ann(x)=(y)`. All differentials lie in the maximal ideal. Tensoring with k makes every differential zero, giving `Tor_i^A(M,k)≅k` for all i≥0. Therefore `pd_A(M)=∞`.

The normalization `k[[x]]×k[[y]]` has hereditary factors, but the glued node has infinite global dimension. The module M is finitely generated and maximal Cohen–Macaulay, yet is not a perfect A-complex. Thus the local hereditary property cannot justify a finite projective resolution of every glued representation.

This example is also a constructive entry point to matrix factorizations: over the regular ring k[[x,y]], the pair (x,y) factors xy and produces the alternating resolution after quotienting. [Eisenbud, *Homological algebra on a complete intersection*, Trans. AMS 260 (1980), 35–64, especially §§5–6](https://www.ams.org/tran/1980-260-01/S0002-9947-1980-0570778-7/S0002-9947-1980-0570778-7.pdf) provides the general hypersurface-periodicity framework.

### 6.3 Use Perf and derived gluing honestly

A finite determinant line is naturally attached to a **perfect** complex, not to an arbitrary unbounded projective resolution. A resolution truncation generally has a boundary syzygy; dropping it changes the derived object. Periodicity can give rational generating functions, but does not make an infinite complex perfect or automatically justify a Fredholm regularization.

For a conductor square, begin with actual projective patching data or a derived descent theorem. Ordinary tensor products can miss Tor at the singular seam. An exact resolution, including maps and compositions, is a useful object to verify in Lean or exact arithmetic; its relation to Frobenius still needs a separate realization.

For a finite locally gentle quiver, weighted path and Cartan determinants can also be computed directly using the permitted/forbidden arrow-transition matrices. This yields a formal cycle-generating identity. Its commuting arrow weights, augmentation topology, and cycle conventions must be stated. Such an identity is valid algebraic bookkeeping, not an arithmetic L-function identification or a purity theorem.

## 7. Determinant functors: the correct homological statement

For a bounded complex P of finite projective modules over a commutative ring R, its determinant line is

`det(P)=⊗_i(det P^i)^((-1)^i)`.

This is compatible with quasi-isomorphisms and exact triangles with the appropriate coherent signs. A determinant **line** is not yet a preferred scalar function: one needs an endomorphism and/or a trivialization. Over a field E, for a finite-dimensional complex with a chain endomorphism F, define

`det(1−tF | P)=∏_i det(1−tF | P^i)^((-1)^i)`.

Adapted bases to boundaries and cycles show that boundary factors cancel in adjacent degrees, giving

`det(1−tF | P)=∏_i det(1−tF | H^i(P))^((-1)^i)`.

The commutation `Fd=dF` is essential. For noncommutative surface orders, an ordinary scalar determinant requires a specified realization over a commutative coefficient field/ring; one cannot apply exterior-power notation to arbitrary noncommutative projectives without additional structure.

Primary references:

- [Knudsen–Mumford, *The projectivity of the moduli space of stable curves I*, Math. Scand. 39 (1976), 19–55](https://doi.org/10.7146/math.scand.a-11642).
- [Deligne, *Le déterminant de la cohomologie*, Contemporary Mathematics 67 (1987), 93–177; author publication record](https://publications.ias.edu/book/export/html/404).
- [Breuning, *Determinant functors on triangulated categories*, arXiv:math/0610435](https://arxiv.org/abs/math/0610435), for the modern categorical extension.

These theorems supply invariance and additivity after the correct hypotheses are met. They do not identify a determinant with ζ or prove spectral positivity.

## 8. The real arithmetic model: finite-field trace formula and weights

### 8.1 Hypotheses and exact determinant orientation

Let X be separated of finite type over F_q, let ℓ differ from the characteristic, and let F be an appropriate constructible ℓ-adic Weil sheaf. Use Frobenius conventions so that H²(P1,Qℓ) has eigenvalue q. Then

`L(X,F,t)=∏_(x closed) det(1−t^(deg x) Fr_x | F_x)^−1`

is identified with

`∏_i det(1−t Fr_q | H_c^i(X_bar,F))^((-1)^(i+1))`.

Equivalently it is the inverse determinant of `1−tFr` on the compactly supported cohomology complex. This is an equality with an Euler product in its initial convergence/formal-series region and a rational cohomological continuation. It is not a claim of local uniform convergence of raw finite Euler products through zeros.

The classical primary statement is in Deligne's *Cohomologie étale (SGA 4½)*, LNM 569 (1977), Rapport, §3, Theorems 3.1–3.2. For an original-source formulation see also [Deligne, *La conjecture de Weil I*, §1, equations (1.5.1)–(1.5.4), pp.275–276](https://www.numdam.org/item/PMIHES_1974__43__273_0.pdf). A precise modern derived formulation is [Stacks Project, §64.20, Theorems 64.20.1, 64.20.2, 64.20.4](https://stacks.math.columbia.edu/tag/03UY): with finite coefficients and finite Tor-amplitude, RΓ_c is perfect; with Qℓ coefficients one gets the alternating cohomology determinants.

### 8.2 Purity is additional arithmetic content, not a consequence of a resolution

For a smooth projective X/F_q, Deligne's theorem gives Frobenius eigenvalues on H^i whose complex absolute values are q^(i/2). The exact primary statement is [Weil I, Theorem (1.6), p.276](https://www.numdam.org/item/PMIHES_1974__43__273_0.pdf). The general mixed-sheaf and weight formalism is developed in [*La conjecture de Weil II*, Publ. Math. IHÉS 52 (1980), 137–252](https://numdam.org/articles/10.1007/BF02684780/).

A useful precision is that Weil II Theorem (3.3.1), printed p.204 (downloaded PDF p.69), is stated for morphisms of finite-type schemes over Z: its weights are measured through closed-point Frobenius data. It is not accurate to describe all of Deligne's weight formalism as confined to schemes over one finite field. Corollaries (3.3.4)–(3.3.6), printed p.206 (PDF p.71), give the finite-field consequences: compact-support weights at most w+i, ordinary weights at least w+i for a smooth scheme and lisse input, and purity of the image H_c^i→H^i for lisse pure weight-w input. The global number-field determinant and zero-location conclusion still do not follow. These precise pages were independently read in the downloaded primary paper.

For a smooth projective geometrically connected curve C,

`Z(C,t)=det(1−tFr | H¹)/((1−t)(1−qt))`.

The numerator's zeros have modulus q^(−1/2). Substituting t=q^(−s) gives Re(s)=1/2. Here all three ingredients are present: the right arithmetic trace identity, the correct cohomological degree, and purity in that degree.

Do not generalize this conclusion to every finite-field variety. For example

`#G_m(F_(q^r))=q^r−1`, so `Z(G_m,t)=(1−t)/(1−qt)`.

Its zero is t=1, of weight zero, reflecting the missing boundary. For singular or open Schubert loci one must track mixed weights and, where appropriate, intersection complexes. Purity of intersection complexes and proper direct-image/decomposition statements belong to [Beilinson–Bernstein–Deligne–Gabber, *Faisceaux pervers*, Astérisque 100](https://www.numdam.org/issue/AST_1982__100__1_0.pdf), not to the bare existence of a quiver resolution.

### 8.3 An explicit positive finite-field benchmark

Take the smooth elliptic curve `E: y²=x³−x` over F5. Direct counting gives eight points, including infinity, hence Frobenius trace `5+1−8=−2`. Its curve zeta numerator is

`1+2t+5t²`,

with reciprocal roots `α=−1±2i`, each of absolute value sqrt(5). Thus

`Z(E,t)=(1+2t+5t²)/((1−t)(1−5t))`

has its numerator zeros at `t=(−1±2i)/5`, on the required circle. This is a concrete arithmetic determinant with a real coefficient system and a verified weight statement for the example. It is the zeta function of a curve over a finite field, not a Dirichlet L-function over Q. It is a useful acceptance-test target for a derived/Frobenius implementation.

## 9. Modern derived and noncommutative zeta work: useful but scoped

[Tabuada, *Noncommutative Weil conjecture*, arXiv:1808.00950v7](https://arxiv.org/abs/1808.00950v7), and the [2022 accepted manuscript](https://wrap.warwick.ac.uk/164151/1/WRAP-noncommutative-weil-conjecture-Tabuada-2022.pdf), treat smooth proper dg categories over finite fields, with topological-periodic/cyclotomic Frobenius realizations. This is a genuine modern bridge from noncommutative categories to arithmetic zeta/weight questions, with specified hypotheses and proved classes of examples.

A complete nodal local ring is infinite dimensional over the ground field, so its Perf category is not automatically proper over that field. A singular finite-dimensional quotient need not be homologically smooth. Neither property follows just from being gentle or having a hereditary normalization. One must verify the hypotheses for the actual dg category before using that framework.

For arithmetic schemes over Spec Z, [Lichtenbaum's Weil-étale proposal for number rings](https://arxiv.org/abs/math/0503604) and [Flach–Morin, *On the Weil-étale topos of regular arithmetic schemes*, arXiv:1010.3833](https://arxiv.org/abs/1010.3833) relate cohomology and special values/orders of vanishing, under stated conditions. Such special-value and determinant-line statements are not all-zero-location theorems. [Deninger, *Arithmetic Geometry and Analysis on Foliated Spaces*, arXiv:math/0505354](https://arxiv.org/abs/math/0505354) explicitly presents conjectural cohomological/dynamical interfaces and regularized determinants; it must not be cited as a completed number-field purity theory.

## 10. What is still missing over number fields

For a finite-image Artin representation ρ, unramified local Frobenius eigenvalues are already roots of unity. This weight-zero local fact is unconditional. Yet it does not imply that the complex Artin or Dirichlet L-function has all zeros on its critical line. Therefore assigning unitary matrices to local arrows or proving local weight zero cannot be the missing global theorem.

Over F_q there is a single geometric Frobenius and a common variable t=q^(−s); its action on finite-dimensional global cohomology produces the numerator and denominator. Over Spec Z the rational primes have different norms, and no such finite-dimensional global Frobenius construction is supplied by a complex nodal curve or by diagonal gluing.

A number-field continuation of this program needs, at minimum:

1. A specified arithmetic realization functor from the chosen algebra/resolution category to coefficient systems carrying actual Galois/Frobenius data, including ramification and archimedean terms.
2. A global trace/determinant identity identifying that realization with the **particular completed** L-function, with the right inverse orientation and regularization.
3. A finiteness/perfectness or analytic determinant theorem for that global object, independently verified for the actual family.
4. A global polarization/positivity/weight statement strong enough to force the zero-bearing spectral piece to the critical line, rather than merely bounding eigenvalues at each finite prime.
5. A comparison theorem proving that projective syzygies, Schubert geometry, or a proposed Hilbert-space operator preserve this exact arithmetic determinant.

There is no universally established object called the missing number-field weight theorem that can simply be imported here. These are research obligations. A valid geometric Langlands theorem or Deligne purity for reductions does not discharge them automatically. Any version that already assumes a self-adjoint realization whose determinant is Λ is again a conditional Hilbert–Pólya criterion.

## 11. A concrete continuation plan with mathematical acceptance criteria

1. **Repair the local category.** Fix a finite quadratic monomial quiver, its completion, central ring, and residue conductor diagram. Keep formal inverse string letters separate from units. Verify maps and syzygies exactly.
2. **Work a nodal example completely.** Use A=k[[x,y]]/(xy), its normalization, conductor square, projective covers, and the explicit alternating resolution. Record which modules are perfect and which require a singularity/matrix-factorization category.
3. **Prove a genuine gluing theorem.** Define a functor of patching data and prove equivalence by Beauville–Laszlo or an appropriate conductor/projective-patching result. Only then form lattice/flag moduli with compatible quotient data. Do not infer it from a picture of diagonal entries.
4. **Use the correct cyclic-quiver theorem.** Keep h and Σd_i distinct, require nilpotency, use the resolvent/lattice map, and determine the exact opposite Schubert loci and rank conditions. Prove seam compatibility as an additional theorem.
5. **Create a finite-field realization first.** Use a finite-presentation model over F_q, a genuine Weil sheaf or smooth proper dg category, and compact-support/IC cohomology with Frobenius. Verify determinant signs and compare with explicit point counts such as the elliptic example.
6. **Separate an arithmetic bridge from a weight bridge.** State each as its own theorem or open obligation. A formal Cartan determinant is a useful invariant to compare, but is not automatically the cohomological L-function.
7. **Return to number fields only after the bridge is explicit.** Check gamma factors, conductor, inertia, determinant orientation, and compact-uniform or regularized determinant control. Raw finite Euler products remain zero free in Re(s)>0, so they cannot converge locally uniformly through L zeros under nonvanishing normalizations; global cohomological determinants are a different approximation mechanism.

This program can yield real local homological and finite-field results without claiming a fabricated GRH proof.

## 12. Verification statement

Completed: full target-paper reading; six visual formula checks; direct enumeration of the seven affine F5 points plus infinity in the elliptic example; exact version/size/hash record; elementary counterexamples and corrected definitions; the explicit nodal infinite resolution; focused primary-source checking for patching, cyclic-quiver geometry, determinant functors, finite-field trace/purity, modern dg zeta work, and the scope of number-field cohomological proposals. External source papers were not all read cover to cover, and no claim of independent certification of their complete proofs is made.

No shared paper/planning/Lean files or source clones were edited by this subtask. The report identifies recoverable mathematics and missing hypotheses; it does not claim a full geometric Langlands equivalence or GRH.
