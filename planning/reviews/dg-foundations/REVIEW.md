# Independent DG-foundations review — 2026-11-03

Reviewer: `/root/persistence_tool_review`. Read the original2053 source
chapter at lines1308–1478, the existing dessin/resolution conventions in
`papers/dessin-core.tex`, and the proposed P4 corrections. The subsequent
actual-file review covers `book/chapters/dg-foundations.tex`,
`papers/dg-core.tex`, `lean-analytic/NodalDG.lean`,
`examples/dg/check_nodal_dg.py`, `web/dg-model.mjs`, `web/dg.mjs`,
the HTML interface and its existing Node checker. Only this report was written.

The proposed five corrections are sound with the hypotheses below. No
arithmetic determinant, positivity or GRH conclusion follows from them.

## 1. The differential dε=1 contracts everything

Use Z-cohomological degrees, |ε|=-1, d of degree+1, and a unital DG algebra
with the graded Leibniz rule. For a left DG module M, put h(m)=εm. Then
d_M h(m)=m-εd_M(m), so d_M h+h d_M=id. Thus every unital left DG module
is acyclic, including the algebra itself; H*(A)=0, not k. For right DG
modules the corresponding formula on homogeneous elements of degree n is
h(m)=(-1)^n mε. The contraction is at least k-linear; do not infer
graded A-linearity for multiplication by ε in a general noncentral DGA.
Here the exterior example is graded commutative, so that extra property
can also be checked. There is no unital DG map to a nonzero field k in
degree0: its image would give d(0)=1. No characteristic restriction is
needed for the displayed contraction; impose ε²=0 explicitly, including
in characteristic2. The source exterior algebra example also needs V
placed in negative degree to justify its nonpositive grading.

## 2. A genuine nodal Koszul DG model

For a field k let P=k[ξ,η], C^0=P, C^-1=Pε, and all other degrees zero.
Let ε²=0, ε commute with degree0 coefficients, and d(aε)=aξη, d(P)=0.
The centrality of ξη makes the graded derivation compatible with ε²=0.
Since multiplication by ξη is injective in P, H^-1(C)=0 and
H^0(C)=P/(ξη). The projection ε↦0 and P→P/(ξη) is an actual DGA
quasi-isomorphism. This establishes formality of this model; it does not
produce a mysterious higher product on its degree0 cohomology.

The coefficientwise completed construction uses P-hat=k[[ξ,η]], not a
Hilbert/operator-norm completion. Multiplication by ξη remains injective
by coefficient shifting. The projection to the branch pullback
Λ={(f(ξ),g(η)):f(0)=g(0)} sends F to (F(ξ,0),F(0,η)). Its kernel is
(ξη), and it is onto: a pair with common constant c lifts to f+g-c.
The topology and the continuity of the differential/projection should be
stated if continuous modules or completed tensor products are used. The
ordinary algebraic quasi-isomorphism result must not silently be promoted
to every possible topological derived category.

This is a genuine infinite nodal dessin example, not a general two-term
model for every glued noncommutative surface order. General monomial
relations have overlaps; gluing DG models, coherently lifting clocks and
comparing their module categories require additional constructions.

## 3. Rescaling and the embedded base DVR

For a specified constant q in k×, ξ↦qξ, η↦q^-1η and ε↦ε preserve ξη,
the products and the differential. The inverse uses q^-1, so this is a
continuous automorphism of the completed DGA as well as a polynomial DG
automorphism. It fixes k pointwise. In Λ the element u=ξ+η corresponds
to the branch pair (ξ,η), and the embedded k[[u]] consists of
(f(ξ),f(η)). Its image qξ+q^-1η belongs to this subring only if the
linear coefficient on both branches agrees, namely q=q^-1. Conversely,
when q²=1 it is qu, so the entire base subring is preserved. This proves
setwise preservation iff q²=1. The automorphism is pointwise k[[u]]-linear
iff q=1. For q=-1 in characteristic different from2 it is base-semilinear
with u↦-u, not base-linear. In characteristic2, q²=1 already forces q=1
over a field. Do not conflate these three notions of compatibility.

## 4. Ext endpoints: distinguish the two theta dessins

Keep the project's right-module and travel-order path convention, residue
simples S_i, and the existing exact forbidden-word resolution. For the
elliptic theta, the vertices are {0,3},{1,4},{2,5}, indexed0,1,2. Every
arrow moves i→i-1 modulo3; each of the two initial arrows has exactly one
forbidden successor. Thus for n>0 there are two forbidden indexing words,
both ending at i-n. The residue-simple Hom differentials vanish, giving
dim Ext^n(S_i,S_j)=2 if j=i-n mod3 and0 otherwise. In degree0 use δ_ij.
In particular self Ext1=Ext2=0 and self Ext3 has dimension2. For graded
Ext, retain the matching internal shifts; for completed orders, specify
the residue-simple category and the already proved formal-series
resolution rather than invoking an unspecified finite module category.

The original2053 paragraph explicitly names the spherical double3 example.
Replacing its numerical skeleton with elliptic theta must be labelled as
a change of input. For the spherical pairing {0,3},{1,5},{2,4}, forbidden
successors have two-cycles. For n>0 even, Ext^n(S_i,S_i) has dimension2
and the other entries vanish; for n odd, each j≠i has dimension1 and the
self entry vanishes. Thus self Ext1 is false in both models, while the
spherical self Ext2 is nonzero. The absence of loops alone already rules
out the asserted two-dimensional self Ext1. Independently iterating the
two actual dart permutations confirmed these endpoint formulas through
degree12 for both examples; this finite check supplements the universal
unique-successor argument, not a replacement proof of exactness.

## 5. Minimal models and necessary categorical boundaries

An isomorphism H0(A)≅Λ is not a DGA quasi-isomorphism. A quasi-isomorphism
is an actual chain/algebra map inducing isomorphisms in every degree. For
example Λ⊗ exterior(ζ), |ζ|=-1, d=0 has H0=Λ and H^-1=Λ, so cannot be
quasi-isomorphic to Λ in degree0. Either require and construct an actual
quasi-isomorphism to Λ, or explicitly retain its extra derived cohomology.

For uncurved Z-graded A∞ conventions, m_n has degree2-n and a minimal
model has m1=0. An ordinary algebra concentrated in degree0 therefore has
all m_n=0 for n>2, by degree alone. RHom(S,S), computed from an actual
suitable projective/K-projective resolution, is a different DGA and may
have cohomology in many degrees. Do not conflate these two minimal models.
Over a field, transfer may use a splitting of complexes; in a completed
topological category a continuous splitting and compatible completed
operations must be supplied rather than assumed.

There is a stronger caution in the present polynomial theta examples.
Their already proved linear projective resolutions make the quadratic
monomial algebras Koszul. For the direct sum of vertex simples, Ext has
cohomological/internal degrees on the diagonal. A transfer respecting
the internal grading has m_n of internal degree0. Comparing the output
cohomological degree sum(p_i)+2-n with internal degree sum(p_i) forces
n=2 for a nonzero operation. Consequently these examples admit a model
with no higher m_n. A nonzero intrinsic m3 is not supplied by the quiver
or by this Ext skeleton. A corresponding topological assertion for a
completed order needs its own category/transfer hypotheses.

In any minimal A∞ algebra, m2 is already strictly associative. m3 is not
a failure of that associativity; it is higher homotopy data, dependent on
model coordinates, related to suitable Massey products modulo choices.
No equality between m3 and physical curvature follows without a defined
observable and a proved comparison theorem.

The remaining original-chapter interfaces also need precise statements:
Ginzburg/Fukaya enhancements are not interchangeable merely because H0
looks related; Hochschild theory uses the graded enveloping algebra and
derived tensor/Hom (with k-flatness or derived base tensor as appropriate);
a homotopy-coherent poset diagram needs all coherence data, not arbitrary
pairwise homotopies. Existing corrected unitary-logarithm material should
be retained: a bounded Borel logarithm exists for a unitary, a continuous
logarithm need not; a singular nilpotent has no matrix logarithm at all.
None of these operations alone constructs the arithmetic spectral bridge.

## Actual implementation and added results

The actual chapter correctly distinguishes the two theta dessins and their
endpoint-sensitive Ext tables. The cohomological sign formulas, ordinary
versus completed rings, formal normal form, semilinearity/DVR distinction,
and internal-grading obstruction to higher operations agree with the reviewed
mathematics. The field hypothesis has now been made explicit in both the
chapter and the shared nodal proposition, as needed by the domain/DVR proof.

The new elementary interfaces are valid. Since A is commutative,
HH0(A)=A/[A,A]=A. With complex coefficients and self-adjoint ξ,η, origin
evaluation is a normalized positive functional: its squared GNS seminorm is
the squared absolute value of the constant coefficient. Its null ideal is
(ξ,η), so the completed GNS space is only C. Its negative is an invariant
trace and fails positivity at1. For complex q the algebraic rescaling still
preserves origin evaluation, but is not a *-automorphism for this declared
involution unless q is real. Consequently the arbitrary unit-circle phases
in the finite visualization are not intrinsic *-automorphisms of this order.

F_(a,b)=ξ^aη^b K is an actual DG submodule because the multiplier is central,
degree0 and closed; the reversed coordinatewise index order makes its maps
literal inclusions. Monomial divisibility proves the stated intersection
formula. The finite boxes are instead subcomplexes of k-vector spaces and
generally fail closure under the coefficient/action ring. Localizing to make
ξη invertible gives d(ε/(ξη))=1 and contracts the underlying complex, so it
does not preserve the nonzero nodal cohomology.

One necessary categorical qualifier was raised during review: for arbitrary
noncentral ε, the homotopy h(m)=εm is only k-linear. The general proposition
must say that the underlying k-complex is contractible, hence the DG module
is acyclic; it cannot assert a B-linear contraction for every module.
For example B=End(C) for C=(k→id k), with commutator differential, contains
the contraction ε with d_Bε=1. Its tautological module C has no nonzero
degree−1 graded B-linear endomorphism: commuting with the degree projections
forces such a map to vanish. The actual graded-commutative exterior example
does admit the stronger contraction. This issue does not invalidate any
checked Lean identity. Both semantic conditions are now resolved in the
actual source: core/book explicitly contract the underlying k-complex, the
proof distinguishes k-linearity from graded B-linearity, and the book adds
the End(C) counterexample over the actual infinite nodal A. The even-degree
projection argument remains valid over A; independent exact matrix checks
verify D H+H D=1 and H P0-P0 H=H for its two rank-one terms. The declared-*
paragraph now explicitly proves that for nonreal q a unitary implementing
U X U*=q X with X self-adjoint forces (q-conjugate(q))X=0, hence X=0,
and likewise for η. It carefully limits this obstruction to the stipulated
involution and does not exclude different adjoint conventions. This is the
correct hypothesis and scope for the stated obstruction.

## Independent executable/formal checks

Independently compiled `NodalDG.lean` with the existing pinned Lean4.24.0
and mathlib environment and `-DwarningAsError=true`: exit0,20 printed
theorems, dependencies confined to the standard foundational axioms
propext/Classical.choice/Quot.sound (some use fewer). Source SHA-256 is
`87a814c73605cd1dd37b156202f0b7d6c0a8dea8e387392d34aa1d4f615e1d83`.
The carrier really is QuadraticAlgebra S0 0, with actual even/odd embeddings,
the signed Leibniz identity and explicit linear differential/homotopy.
The ambient nodal sequence uses actual MvPolynomial(Fin2)k and its principal
ideal quotient. Domain/nonzero hypotheses in the general injectivity lemma
are discharged for the actual product of polynomial variables. The general
clock theorem explicitly assumes a coefficient-ring automorphism fixing f;
it does not claim a kernel-checked construction of the actual q-substitution.
The formal scope appropriately excludes categorical Z-grading, completed
topology, DG-module equivalences, general module contractions, Ext tables,
HH/GNS and A∞ transfer.

The existing Node checker passed12 window cases and26 theta matrices.
Independent additional checks cover all27 windows allowed by the model API
(N=0 through8, three modes) and135 inclusions between them. Every differential
target lies in its target box, targets are distinct, weights i-j agree at
both ends, and all asserted ranks and homology dimensions agree with the
explicit basis counts. All window inclusions preserve both chain layers and
the arrows. Independent symbolic calculations reproduced the sign-Leibniz
and homotopy identities and64 quotient normal forms. A separately assembled
dart-transition matrix computation B T^(n−1) E, including the degree0
identity, agrees with all234 stored theta dimension entries. These checks
ran in memory and wrote no new outputs; they complement the infinite proofs.

Acceptance: no algebraic, numerical, formal-check or semantic blocker remains
in the reviewed components. Both requested wording corrections are resolved.
Browser/visual, build and repository-integrity checks belong to the integrating
worker and were not repeated by this reviewer. No claim of full DG/A∞
formalization, arithmetic comparison or GRH is made here.
