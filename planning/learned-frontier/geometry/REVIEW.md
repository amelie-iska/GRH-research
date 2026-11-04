# Geometry, fields and games: checked interfaces

Prepared 2026-11-04. External results are named and linked; the small propositions
proved below are original calculations for the stated models. The exact program
is `examples/learned_frontier/geometry/check_geometry.py`; its complete output is
in that directory's `outputs/exact.json`. It uses the existing pinned SymPy 1.14.0
environment, no randomness, and no new dependency. This review is an integration
handoff, not a claim to solve the arithmetic determinant or GRH problem.

## Four different meanings of a cover

Write **F₂=⟨x,y⟩** for the free group, **𝔽₂** for the two-element field,
and **F̂₂** for the profinite completion of the free group. Their roles must be
separate. Bit-valued cellular boundary matrices use 𝔽₂; deck words use F₂.
Taking coefficients in 𝔽₂ does not turn an arithmetic fundamental group into F₂.

The undirected theta graph has two vertices A,B and three edges a,b,c. Its
fundamental group is F₂, but its universal graph cover is the **3-regular** tree.
The Cayley graph of F₂ for x±¹,y±¹ is **4-regular**. Choose the a-edge as a
spanning tree and coordinates (g,A),(g,B), g∈F₂. Put edges

    a: (g,A)—(g,B),  b: (g,A)—(gx,B),  c: (g,A)—(gy,B).

Left multiplication by h on g is a deck transformation; using right multiplication
for the deck action would not preserve these voltage labels. Contracting every
a-edge recovers the Cayley graph. Conversely, splitting each Cayley vertex into
its A/B pair with these three edge types produces the theta cover. Splitting a
vertex into a connected tree and redistributing incident edges preserves
connectedness and absence of cycles, so this graph is a tree. Every vertex has
exactly one incident edge over each base edge. This also proves unique path
lifting without relying on a finite drawing.

A second concrete description takes vertices to be reduced, nonbacktracking
paths from A, with cancellation of an immediately reversed edge. The unique
reduced path is the geodesic in the tree with unit edge lengths. The n-th sphere
has 3·2ⁿ⁻¹ vertices for n≥1. The checker lifts all paths through radius eight,
gets 766 distinct vertices, checks inverse steps and five deck transformations.
These are finite diagnostics of the unbounded definition. General covering
background is [Hatcher, §1.3](https://pi.math.cornell.edu/~hatcher/AT/ATch1.pdf).

The graph is the deformation retract of a topological pair of pants. A **metric**
hyperbolic pair of pants instead has hyperbolic boundary/geodesic data; arbitrary
reduced graph paths do not automatically represent its geodesics with the same
length. Filling the faces of a dessin changes its fundamental group. For example,
the torus theta cellulation has the graph as its 1-skeleton, but attaching its face
introduces a relation. A closed genus-two surface has four generators and its
surface relation; its universal surface cover is a disk, not this tree.

## Finite support, deck-Hom and a genuine loss of full faithfulness

Here only, take the graph quiver with three arrows A→B and its path category
over Q. This is not the quiver or algebra of the theta dessin in the existing
`examples/coverings/theta_cover.py`. That older script treats an actual dessin
quotient and a cyclic grading cover; it remains unchanged and is complementary
evidence, not an implementation of the universal graph cover above.

For finite-supported representations M,N of our cover, pushdown sums the vector
spaces over each base vertex. A downstairs linear map is a finite matrix of
blocks F(h,g), source grade g and target grade h. Its degree is h g⁻¹. Arrow
equations preserve this degree: a,b,c multiply source and target grades by the
same voltage v, and (hv)(gv)⁻¹=h g⁻¹. Thus the arrow-commuting system splits by
deck degree and the Hom space is the direct sum of its homogeneous pieces.
If hN is defined by (hN)(g)=N(h⁻¹g), the degree-d piece is
Hom_cover(M,d⁻¹N). This fixes the inverse convention explicitly.

Take M=N to be the sum of two a-edge interval modules, one at grade 1 and one at
grade x. At each supported A and B put Q, let its a-arrow be the identity, and set
all b,c maps to zero, including arrows between supported vertices. Downstairs
A=B=Q², a=I₂ and b=c=0, hence End=Mat₂(Q), dimension four. Upstairs an endomorphism
cannot change its vertex, so End=Q⊕Q, dimension two. The two off-diagonal matrix
units have degrees x and x⁻¹, one dimension each. This proves 4=2+1+1 and failure
of fullness for pushdown; it does not prove failure of every covering functor.

A claimed Hom-controlled functor must specify which of these spaces it controls.
Even faithful and exact does not imply fully faithful; a direct-sum deck formula
is not an equivalence. For a derived comparison the relevant data are all
Hom(X,Y[n]), their composition, and an enhancement or explicit derived functor.
AR meshes additionally require almost-split properties in a chosen exact/module
category. A finite coefficient graph or agreement of dimensions cannot supply
those universal properties.

## Actual infinite genus-two modules, not a finite path-algebra surrogate

Work over Q with ordinary **right polynomial modules**, travel-order path
multiplication and vertices i∈Z/5. There are two arrows aᵢ,bᵢ:i→i−1, with

    aᵢ bᵢ₋₁ = bᵢ aᵢ₋₁ = 0;

pure a and pure b paths remain nonzero at every length. This is the genuinely
infinite locally gentle algebra A of the clean dessin
y²=x⁵−1, β=x⁵, with σ=(01234)(56789), α=(05)(16)(27)(38)(49).
The permutation φ=ασ⁻¹ is one 10-cycle. The contracted cellulation has V=2,E=5,F=1,
so χ=−2 and genus two. This agrees with `papers/dessin-core.tex` and the existing
branch-module scripts; no source module, order, or dataset is changed here.

Normal paths consist of idempotents and pure paths of either branch. Let
Pᵢ=eᵢA, Sᵢ=Pᵢ/PᵢJ. A simple resolution has P₀=Pᵢ and, for n≥1,

    Pₙ=Pᵢ₋ₙ ⊕ Pᵢ₋ₙ.

The summands are labelled by the two length-n words whose branches alternate.
Those indexing words are zero in A once n≥2: the differential entry is their
**last arrow**, not their zero product. To prove exactness, multiplication by an
arrow kills precisely the opposite-branch paths of positive length at its target.
Every same-branch path survives to a distinct normal path. Thus its kernel is the
ideal generated by its unique forbidden successor; there can be no cancellation.
The augmentation kernel is the direct sum aᵢA⊕bᵢA. Iteration proves exactness
in every degree, and the summands are projective. On applying Hom to a simple all
arrow entries vanish. Therefore

    dim Hom_A(Sᵢ,Sⱼ)=1 if i=j, else 0;
    dim Extⁿ_A(Sᵢ,Sⱼ)=2 if j=i−n mod 5, else 0  (n≥1).

For the left residue simple Tⱼ, dim Tor⁽ᴬ⁾ₙ(Sᵢ,Tⱼ) has the same formula.
Ungraded ordinary modules are meant; an internal grading adds the corresponding
degree shifts. Positive Ext in unbounded degrees rules out a bounded finite
projective resolution of Sᵢ. This is one reason not to apply a smooth-algebra HMS
theorem to this full algebra by inspection.

Let B have Q at 0 and 4, with a₀=1 and all remaining arrows zero. This is an
actual one-arrow branch module of A, supported at two vertices. Its normal-path
presentation is

    P₄ ⊕ P₃ --(b₀, a₀a₄)--> P₀ --> B --> 0.

The two images have disjoint normal-path supports; their sum is the entire
kernel because B retains just e₀,a₀. The next entries are a₄ on the first arm and
b₃ on the second. Continue each arm by its unique forbidden successor. The
same normal-path proof establishes this resolution in all degrees.

The full ten-arrow Hom equations give

| pair | Hom dimension |
|---|---:|
| (B,B) | 1 |
| (S₀,B) | 0 |
| (B,S₀) | 1 |
| (S₄,B) | 1 |

For Ext¹(B,B), Hom(P₀,B)=Q, Hom(P₄⊕P₃,B)=Q⊕0. The first Hom differential is
(B(b₀), B(a₄)B(a₀))=0 and the next is also zero. Hence **Ext¹_A(B,B)=Q**.
This is witnessed by a nonsplit self-extension: put Q² at 0,4, a₀=I₂,
b₀=[[0,1],[0,0]], all other arrows zero. Its invariant first-coordinate subspaces
and corresponding quotients are B; a section commuting with b₀ would have to
send a nonzero quotient vector into ker b₀ while projecting to that vector,
which is impossible. Relations hold because every next arrow out of vertex4
vanishes. Thus the branch string B is not rigid in this actual ambient category.

For any finite-dimensional right target N, let D(N)=Hom_Q(N,Q) be its left dual.
For a finite idempotent projective P, the natural pairing identifies
P⊗_A D(N) with D Hom_A(P,N). Dualizing the finite-dimensional Hom complexes is
exact, so Tor⁽ᴬ⁾ₙ(M,D(N)) ≅ D Extⁿ_A(M,N) for M=S₀ or B. In particular
Tor⁽ᴬ⁾₁(B,D(B))=Q. The program constructs the displayed projectives and arrow
differentials, checks d²=0 and computes the Hom and transposed tensor complexes
through degree12 for six source/target cases. It separately verifies all five
simple-target formulas and 250 normal-path kernel samples. These checks support
the proofs; they do not replace their unbounded normal-form argument.

No claim here identifies algebraic modules with continuous completed modules,
all lattices, or all infinite strings. No AR classification is inferred.

## Pants gluing is exact algebra; physical realization needs a metric

External theorem: oriented 2D TQFTs with finite-dimensional state space are
classified by commutative Frobenius algebras, with the usual monoidal and
isomorphism conventions. See [Abrams (1996)](https://www.math.umd.edu/~jmr/AbramsTQFT.pdf).
Our explicit example uses C=Q[t]/t², ordered basis (1,t), with ε(1)=0, ε(t)=1.
The multiplication and comultiplication matrices are

    μ = [[1,0,0,0], [0,1,1,0]],
    Δ = [[0,0], [1,0], [1,0], [0,1]].

The tensor order is (1⊗1,1⊗t,t⊗1,t⊗t). Thus Δ(1)=1⊗t+t⊗1, Δ(t)=t⊗t.
The pairing ε(ab) is [[0,1],[1,0]], determinant −1. Associativity follows from
t²=0, and coassociativity sends 1 to the sum of the three placements of one 1
among two t's, and t to t⊗t⊗t. For the Frobenius identity, on 1⊗1 all three
maps give 1⊗t+t⊗1; on 1⊗t or t⊗1 they give t⊗t; on t⊗t they give zero.
This proves Δμ=(μ⊗1)(1⊗Δ)=(1⊗μ)(Δ⊗1), including every basis case.
The checker independently verifies all these tensor equalities, both unit and
counit identities, commutativity and cocommutativity.

The handle map H=μΔ sends 1↦2t and t↦0. Consequently the closed genus-g
amplitude εHᵍη is 0,2,0,0,… for g=0,1,2,3,…; this is a literal finite tensor
contraction. In particular the genus-two gluing amplitude vanishes in this
example, rather than being a nonzero partition function inserted by assumption.

After extending scalars to C and taking the positive Euclidean Hilbert metric,
μ:C⁴→C² cannot be an isometry, Δ†Δ=diag(2,1), and Δ≠μ†. The Frobenius pairing is
nondegenerate but indefinite; it is not the physical Hilbert inner product.
The program supplies an exact heralded realization K=μ/√2 and an explicit
4×4 failure matrix L with K†K+L†L=I₄. The stacked map V=(K,L):C⁴→C²⊕C⁴ is an
isometry. After embedding that direct sum into an outcome-flagged tensor space,
it can be extended to a unitary with ancillas. Selecting the success outcome
implements K, with state-dependent success probability ||Kψ||²; normalized
postselection is not the linear map μ. Basis success probabilities are
(1/2,1/2,1/2,0). A deterministic unitary circuit is therefore a different claim.

[Segal's CFT definition (2004)](https://www.cambridge.org/core/books/abs/topology-geometry-and-quantum-field-theory/definition-of-conformal-field-theory/90BD9D5C5C8A4BD7ABE4000694D84DFA)
adds conformal geometry and analytic sewing data. Our Frobenius example has no
modulus-dependent propagator, Virasoro representation, conformal anomaly, or
integration over worldsheet moduli. An actual string amplitude needs further
worldsheet/ghost/consistency data. Similarly,
[Ryu–Takayanagi v2](https://arxiv.org/abs/hep-th/0603001v2) concerns entropy in an
AdS/CFT setting; a pants tensor graph alone does not instantiate that setting.

## CHSH: an executable game and the separate infinite-operator theorem

Uniform bits x,y are sent to two separated players; output bits u,v win when
u⊕v=xy. Put Aₓ=(−1)ᵘ, Bᵧ=(−1)ᵛ. The success probability is
1/2+〈T〉/8 with T=A₀⊗(B₀+B₁)+A₁⊗(B₀−B₁).
For deterministic ±1 outputs one of B₀+B₁, B₀−B₁ vanishes and the other is ±2.
Thus T≤2; convex combinations preserve the bound. All16 deterministic strategies
are enumerated, and the maximum classical success probability is 3/4.

Take |Φ⁺〉=(|00〉+|11〉)/√2, A₀=Z,A₁=X, B₀=(Z+X)/√2,B₁=(Z−X)/√2.
Then T=√2(Z⊗Z+X⊗X), and 〈T〉=2√2, so the quantum value is
(2+√2)/4. For any self-adjoint involutions, expansion gives
T²=4I−[A₀,A₁]⊗[B₀,B₁]. Each commutator has norm at most2, hence ||T||≤2√2.
This proves optimality, not just achievement; it is the elementary CHSH instance
of [Tsirelson's result (1980)](https://doi.org/10.1007/BF00417500).
The checker verifies the involutions, commutator identity, state expectation and
the full Bell-matrix eigenvalue multiset {−2√2,0,0,2√2} exactly.

Current external theorem, verified 2026-11-04:
[Ji–Natarajan–Vidick–Wright–Yuen, MIP*=RE v4](https://arxiv.org/abs/2001.04383v4)
is dated **16 October 2026**; the version page reports acceptance to Annals,
corrections and a link to a Lean formalization. Its theorem equates entangled
multiprover interactive-proof languages with recursively enumerable languages.
It gives undecidability for the promise of two-player entangled value1 versus
at most1/2, a strict inclusion Cqa⊊Cqc, and a negative answer to Connes embedding.
Cqa is the closure of finite-dimensional tensor-product correlations; Cqc uses
commuting operators. The unrestricted dimensions and computability quantifiers
matter. We have not run that external Lean development. CHSH achieves its optimum
on two qubits and has the same commuting optimum by the same operator bound;
this example does **not** exhibit Cqa⊊Cqc or encode the undecidable family.

## From a trained field to tropical geometry and HMS: admissible next claims

The finite-data QNTK is Kᵢⱼ=Σₐ∂ₐf(xᵢ)∂ₐf(xⱼ); this is a real positive
semidefinite Gram matrix by construction. If it is frozen under squared-loss
gradient flow, residuals obey ṙ=−Kr and r(t)=exp(−Kt)r(0). A zero eigenvalue
preserves its residual component. This elementary conditional identity does not
prove that a particular trained circuit has a frozen kernel, reaches a global
minimum, or has a field limit.

[Liu et al., QNTK v3](https://arxiv.org/abs/2111.04225v3) treats lazy/frozen
dynamics, corrections and a specified hybrid large-width Gaussian regime.
[Liu et al., wide quantum networks v3](https://arxiv.org/abs/2203.16711v3)
studies circuits with many qubits and variational parameters, with ensemble
assumptions controlling average training behavior. These are distinct width
limits, not a theorem that every finite quantum graph transformer becomes a QFT.
[Shirai et al. v2](https://arxiv.org/abs/2111.02951v2) studies tangent-kernel
behavior of deep parameterized circuits and numerical ansatz-generated data.
Gaussianity, a continuum limit, locality and interacting field dynamics require
their own scaling, convergence topology and observables.

Max/min attention can exactly implement a piecewise-linear optimization or a
tropical semiring calculation. It does not by itself tropicalize an algebraic
variety. [Zhang–Naitzat–Lim v1](https://arxiv.org/abs/1805.07091v1) supplies the
ReLU/tropical-rational-map connection; a max-plus expression still needs a stated
coefficient/exponent convention to be an algebraic tropicalization.
[Kontsevich–Soibelman math/0406564v1](https://arxiv.org/abs/math/0406564v1)
constructs non-Archimedean analytic geometry from integral-affine data and gluing,
including a K3 example, motivated by HMS/SYZ. The source does not identify
arbitrary learned real coefficients, a softmax feature map, or our dessin order
with that construction. A proposed bridge needs a valued coefficient field,
an integral-affine base, singularity/wall data and valid gluing maps. Learned
coefficients may propose such data; equations and compatibility must be checked.

External categorical theorem with precise scope:
[Lekili–Polishchuk v5](https://arxiv.org/abs/1801.06370v5) attaches a surface with
boundary, stops and line field to a homologically smooth graded gentle algebra,
with its perfect category equivalent to the specified partially wrapped Fukaya
category. To use such a result one must establish the hypotheses for the exact
algebra/category, keep grading and stops, and construct the comparison. Our
genus-two algebra has residue simples with infinite projective dimension; no
identification of its entire ordinary or completed module category with this
Fukaya category has been supplied. A module's finite path is not automatically
a geodesic, and its graph intersections are not automatically Ext groups.

Finally, an arithmetic/anabelian reconstruction needs arithmetic profinite data.
[Mochizuki's survey, introduction and Theorem1.3.4](https://www.kurims.kyoto-u.ac.jp/~motizuki/Absolute%20Anabelian%20Geometry.pdf)
distinguishes the arithmetic étale fundamental group and its map to the ground
field Galois group from the geometric kernel. The relevant reconstruction
hypotheses concern hyperbolic curves and arithmetic fields. An abstract discrete
F₂, its graph, or even its profinite completion without the arithmetic extension
does not contain all that datum. The geometric étale fundamental group of the
thrice-punctured projective line in characteristic zero is F̂₂; this does not
identify it with the full arithmetic fundamental group. A learned model can be
tested against Frobenius/ramification descent data, but no anabelian theorem
follows merely from a pants decomposition, a module Hom matrix or MIP*=RE.

## Verification and integration limits

Fresh command: `.tools/book-quantum-cpu/bin/python examples/learned_frontier/geometry/check_geometry.py`.
All four diagnostics pass. Outputs record exact parameters and all Ext/Tor
tables; no stochastic seed is needed. The existing cover and branch scripts,
environments, checkpoints and sources were read only. No MCP server, installation,
external job, authentication, GPU, git stage or push was used. No full book/web
build was run by this scoped worker. Integration must preserve the category and
coefficient distinctions above; external theorem claims remain externally sourced.
