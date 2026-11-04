# Independent linear-relations and branch-filtration review

Reviewer `/root/linear_relations_review`, 2026-11-03. This is an adversarial
mathematical review of the proposed construction and the original 2053
manuscript lines1097–1307. Source manuscripts, production code, Git state,
environments and configuration were not changed. Only this report and
reviewer-owned evidence under `outputs/checks/2026-11-03-linear-relations/review/`
were written. Final implementation/Lean snapshot review will be recorded below
when the integrating worker supplies the files.

Read the project README, existing pinned Lean check script/toolchain manifest,
original source slice, and the existing exact-scope review
`planning/reviews/pullbacks/string-fukaya-scope.md`. The cached primary
Crawley–Boevey1308.6410v2 PDF remains SHA-256
`d998acee987998ec11c69ca73d10279c2174abe1c08e75090068eba34415ab74`.
This review does not claim a new full25-page audit of its proof. Its existing
focused source record identifies definitions, Theorems1.1–1.4, completion
remarks and tail criteria. The new finite branch claims below are proved
directly and do not depend on an unrestricted infinite-module classification.

## Decisive corrections to the source

For a linear map T:V→V, its graph is all pairs (v,Tv), including vectors
sent to zero. The source's displayed f on k³ has graph basis
(e1,e2),(e2,e3),(e3,0), not just its first two pairs. The inverse-shift g has
basis (e1,0),(e2,e1),(e3,e2). Graph(f²) has basis
(e1,e3),(e2,0),(e3,0). Graph(gf²) has basis
(e1,e2),(e2,0),(e3,0). All these graph subspaces have dimension3, irrespective
of the maps' ranks. Omitting the zero-output pairs changes the relation's
domain and is not a harmless visualization simplification.

The displayed definition κ(C)=⋃Cⁿ(0) gives κ(Graph T)=0 for every linear T.
The ordinary stable kernel is instead ⋃ker(Tⁿ), equivalently the zero orbit
under the inverse relation. A subspace of V must not be listed as pairs in
V×V. With the source's exact matrices,

- gf=diag(1,1,0): stable kernel k e3 and stable image k e1⊕k e2;
- fg=diag(0,1,1): stable kernel k e1 and stable image k e2⊕k e3.

Thus even after interpreting κ as the ordinary stable kernel, the source's
gf/fg kernel entries are reversed. For f and g the ordinary stable kernel
is V and stable image0; the outgoing zero-orbit κ remains0.

Fitting decomposition requires finite length, here finite-dimensional V.
Multiplication by t on k[t] is injective, not surjective, has stable kernel0
and stable image⋂tⁿk[t]=0, yet V≠0. The naive finite-dimensional decomposition
cannot be asserted for arbitrary infinite-dimensional modules or lattices.
General multivalued-relation regular parts require their own definitions and
hypotheses; graph Fitting alone does not prove them.

The source's blanket string rigidity claim is false. The explicit length
m−1 a-chain below has a nonsplit self-extension. A band parameter λ=1 is
allowed: excluding it from k* has no mathematical justification. Finite words
also require composability, avoidance of inverse zero-relations, and
identification with inverse words; bands require primitive cyclic admissible
words whose powers remain admissible and coefficient data. The source's
ordinary strings do not classify all completed-order modules. Its definitions
of an abelian category as a quiver with an additive object set are incorrect:
additivity is on Hom groups, with bilinear composition and biproducts; abelian
categories further have kernels/cokernels and the usual image/coimage property.

## Actual higher-genus branch construction

Take the polynomial dessin algebra A_m, m odd5 or9, with two arrows
 a_i,b_i:i→i−1 modulo m and forbidden cross-branch length-two products.
This is an actual infinite-dimensional locally gentle algebra; the m5 case
is the specified genus-two clean dessin and m9 is genus four. It is not
replaced by a finite-dimensional algebra.

In finite-dimensional representations impose b_i=0 and make a_i invertible
for i=1,…,m−1. After identifying all vertex spaces using these invertible
maps, the representation is N_m(V,T), with each vertex space V, a_0=T and
all other a_i=identity. A morphism has one common component h because the
identity arrows connect all vertices; its remaining condition is hT=Sh.
Consequently this full subcategory is equivalent to finite-dimensional
k[t]-modules. The inverse identifications are choices of normal form; the
monodromy equivalence itself uses canonical transport after selecting the
base vertex. Kernels and cokernels preserve the invertibility of the
specified arrows, so the subcategory is abelian and its inclusion is exact.
None of this asserts that it equals the whole A_m module category.

The central sum of full permitted turns acts as T on each vertex. A nilpotent
T gives a continuous action of the arrow-adic completion: all sufficiently
long paths act as zero, so every formal series acts by a finite sum. This is
a finite central-torsion module, not a DVR-free lattice. Conversely on a
Jordan block J_r(λ) with λ≠0, (u−λ)^r acts as zero while u−λ is a unit in
k[[u]]. A nonzero unital module over the completed order cannot have this
property, even if continuity is dropped. Thus these ordinary polynomial
bands do not extend to the u-adic completed order. This is an actual change
of category, not a reason to forbid λ=1 in the polynomial category.

For Jordan blocks over a field containing the displayed eigenvalues,
Hom(J_r(λ),J_s(μ)) has dimension min(r,s) when λ=μ and0 otherwise.
The same Hom result holds for the actual A_m modules by the full equivalence.
End(J_r(λ))=k[t]/((t−λ)^r) is local, proving indecomposability. In the
nilpotent case these are finite strings running along the a-cycle repeatedly
with the endpoint broken at a_0. In particular N_m(J_1(0)) is a length m−1
string, and N_m(J_2(0)) gives its nonsplit self-extension. An A_m splitting
would be a k[t]-splitting by the Hom calculation; no such section exists.
Thus Ext¹ of that string with itself is nonzero. No assertion about all
ambient higher Ext groups follows from the full abelian inclusion.

## Functorial Fitting statement and categorical lemma

For finite-dimensional (V,T), choose N beyond stabilization. Set
K=ker(T^N), I=im(T^N). The equality ker(T^(2N))=ker(T^N) shows K∩I=0;
rank-nullity gives K⊕I=V. Both are invariant, T|K is nilpotent and T|I is
bijective. An intertwiner hT=Sh transports both the stable kernels and stable
images. The decomposition is therefore functorial, despite noncanonical
choices of bases and Jordan vectors. It yields the nilpotent/invertible
parts on the actual branch subcategory. For d_r=dim ker(T^r), d_0=0,
2d_r−d_(r−1)−d_(r+1) counts zero-eigenvalue blocks of exact size r.
It does not recover nonzero eigenvalue/Jordan data without the corresponding
(T−λ) filtrations.

The abstract source classification lemma survives after correcting its
categorical vocabulary and γ's direction. Let the ambient/source categories
be additive with finite biproducts, F_i and S_i additive, F_iS_i≅identity,
F_iS_j≅0 for i≠j, the family F_i objectwise locally finite and jointly
reflecting isomorphisms, and γ_i,M:S_iF_iM→M with F_iγ_i,M invertible.
For the finite set of nonzero F_iM, the biproduct of these γ maps is sent by
every F_j to an isomorphism, including indices outside that set, where both
objects are zero. Hence ⊕S_iF_iM→M is an isomorphism. A nonzero indecomposable
M therefore comes from exactly one nonzero component. Conversely a
biproduct decomposition of S_iX with X nonzero indecomposable has one summand
annihilated by every F_j; applying joint reflection to0→that summand makes
it zero. Applying F_i gives uniqueness of i and X. Nonzero qualification is
essential. Exactness and naturality of γ are not needed for this argument.
The stated assumptions alone should not be advertised as a full equivalence
of categories or as a theorem about all completed-order module categories.

## Determinant and spectral boundary

Let L be the branch transport on V^m. Its m-th power is diagonal with T in
every block. Block elimination, or the usual companion-matrix identity,
gives det(I−zL)=det(I−z^mT). The identity includes singular T. For J_r(λ)
it is (1−λz^m)^r; nilpotent blocks contribute1. This is a genuine finite
monodromy invariant and is compatible with direct-sum factorization.
For λ=2 its zeros have radius2^(−1/m), so a cyclic string/band construction
does not force unit-circle zeros. Functional-equation centers, positive
self-adjoint realizations and arithmetic L-identification remain separate.
The mere existence of an invariant determinant does not supply relations
among semi-invariant generators or a Hilbert–Pólya/GRH proof.

## Topology and covering qualifications

For this particular saturated closed A_m, every admissible letter has two
admissible successors: continue on its branch/orientation, or switch to the
other branch in opposite orientation. Its one-sided admissible-word space,
as a closed subspace of the finite-alphabet product, is compact, totally
disconnected and has no isolated points. Thus it is a Cantor space itself,
not a Cantor set with a supposed countable exceptional set removed. This
argument must not be generalized to arbitrary gentle quivers, whose
languages may have isolated or eventually forced paths. An infinite
admissible word cannot terminate or contain a forbidden relation.

The underlying graph's universal cover is a tree, but the algebra cover
retains the lifted zero-relations; a bare path category of the tree forgets
them. Descent requires compatible equivariant/local-system data, not simply
a periodic picture. A band parameter is a scalar or Laurent coefficient
monodromy, not a temporal period or a derived equivalence. Existing precise
Fukaya/perfect/finite-support/completion distinctions remain necessary.

## Independent executed exact oracle

Executed reviewer-owned `oracle.py` with the existing approved CPU environment,
without importing the new production code or changing source artifacts.
The result in `oracle.json` and `oracle.log` passes:

- full graph bases and reversed gf/fg kernel correction;
-24 exact m5/m9, Jordan-size1–4 and λ0/1/2 transport/characteristic identities;
-125 exact intertwiner-kernel dimensions across sizes1–5 and equal/unequal eigenvalues;
- mixed nilpotent/invertible Fitting direct sum and exact block counts;
- inconsistency of the linear equations for a splitting of the nilpotent self-extension.

All calculations use exact symbolic/integer linear algebra. They corroborate
the direct proofs, not a general classification or an arithmetic zero theorem.
No substantive mathematical blocker is present in the proposed scoped
construction. Final literal manuscript/theorem-type checks remain pending.

## Focused fresh primary relation reading

Additionally read Section4 pp7–10 of the pinned CB1308.6410v2 cached text:
Definitions4.1/4.3, Lemmas4.2/4.4/4.5, statement and initial construction of
Splitting Lemma4.6. The proof of4.2 uses stabilization in finite dimension;
the proof of4.5 uses both symmetric relation identities to establish a
well-defined invertible quotient map. These confirm that the genuine general
regular quotient is C^sharp/C^flat, with
C^sharp=C''∩(C^−1)'',
C^flat=(C''∩(C^−1)')+(C'∩(C^−1)''). Here C'=⋃Cⁿ0 and C'' consists of
vectors admitting a compatible backwards chain. One only has
C''⊆⋂CⁿV without finite-dimensionality; Lemma4.2 gives equality in finite
dimension. Lemma4.6 asserts splitting when C^sharp/C^flat is finite-dimensional.
This is a precise external relation result, not something the current
finite-graph Lean file proves. A chapter paragraph using these definitions
and named theorem scopes would correctly connect the elementary Fitting
construction to the source's intended functorial-filtration method.

## Literal implementation and formal review

Read all of `papers/relations-core.tex`, `papers/relations-details.tex`,
`examples/relations/check_relations.py` and `lean-analytic/LinearRelations.lean`.
The normal-form transport p_i=a_1…a_i and T=p_(m−1)a_0 has the correct
left-representation composition order. The Hom equations, exactness argument,
completion criterion, field qualifications, mixed example, corrected source
table, indecomposable-classification lemma, self-extension and determinant
row elimination are valid as stated. The chapter correctly disclaims
whole-module classification, general derived full faithfulness, arithmetic
identification and full categorical Lean verification.

Independently ran the final Lean file with the existing pinned Lean4.24.0 /
mathlib environment and warnings treated as errors: exit0. Its11 printed
types and axiom reports use only propext, Quot.sound and Classical.choice
as applicable. The actual IsCompl statement proves finite-dimensional
Fitting at exponent finrank(V), not an assumed desired decomposition.
The graph, inverse/compose, semiconjugacy and ker/range membership statements
use actual Submodule/LinearMap objects. Unit-power annihilation is universal
module algebra, not a custom completed-order axiom. The file does not package
the entire dessin category, Jordan classification, general relation splitting,
abstract functor proposition, determinant proof or any GRH result. Formal
source SHA-256:
`db7b07d8164a2498de3a2f3321b7d7411eea90e20ddf19c9975a13fc074987bf`.

Independently replayed the production exact checker, redirecting both its
OUT destination and web-data write to reviewer-owned artifacts. It passes
all8 actual m5/m9 module cases,10 full quiver Hom equation cases, source
corrections, mixed Fitting and nonsplit extension. The independently written
oracle above additionally checks24 characteristic identities and125 Hom
cases. The exact letter test correctly retains composability, direct and
inverse forbidden pairs and inverse cancellation. No caches, dependencies,
shared exported data or training outputs were changed by reviewer execution.

One precision suggestion was sent to the integrating worker: CB Lemma4.5's
regular-quotient automorphism needs no finite-dimensionality hypothesis;
Lemma4.6's splitting does need finite-dimensional C^sharp/C^flat. The
reviewed text already points to the correct quotient, but separating those
two clauses prevents an ambiguous reading of their different scopes.
This does not affect the finite Fitting or branch construction. Snapshot
hashes and raw logs are under the reviewer evidence directory. Browser,
visual, final generated-output and full-suite integration gates remain
with the integrating worker.

### Precision correction verified

The final relation paragraph now explicitly states that the automorphism
holds for an arbitrary relation and that only splitting additionally requires
finite-dimensionality of the quotient. Reread that corrected paragraph;
no outstanding review finding remains. Updated details SHA-256:
`431637508f0360c61276b7654b2a038f538d57cbd84f4a730d30aeb47da08046`.
