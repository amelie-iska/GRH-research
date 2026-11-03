# Full review: graph C*-algebra pullbacks, arXiv:1907.10260v3

2026-11-03. Alexandru Chirvasitu, Piotr M. Hajac and Mariusz Tobolski, **Non-surjective pullbacks of graph C*-algebras from non-injective pushouts of graphs**, [arXiv:1907.10260v3](https://arxiv.org/abs/1907.10260v3), revised 31 December 2019; first submitted 24 July 2019. The primary record explicitly notes that v3 reformulates the main results and corrects their proofs. DOI associated with the published work: [10.1112/blms.12389](https://doi.org/10.1112/blms.12389).

Exact artifact: `/Users/amelieschreiber/Documents/LaTeX-projects/GRH/research/literature/pullback-extension-20261103/1907.10260v3.pdf`, 17 pages, SHA-256 `9f5c3e023e4333bd20cb8305dc53fd7cbcd62555f58647a1ff0ea050e3a97436`.

Coverage: the entire 6,532-word extracted text was read, including all §§1–5, definitions, both main proofs, preliminary lemmas, all example discussions and references through p.17. Pages 13–15 were additionally rendered and inspected to check the graph/pushout examples obscured in text extraction. This is a full textual reading and focused adversarial proof review, not independent reproof of every imported uniqueness, ideal-structure or abstract pullback theorem. No shared source/manuscript/Lean/planning file was altered. The original protected source clones remain untouched.

## Verdict

The applicable results are **Theorem 3.4 and Theorem 4.3**, not a Theorem 3.9 in this pinned version. They give specific pullback and sink-extension results. They do not assert that arbitrary graph pushouts become C*-algebra pullbacks. The stated hypotheses are essential and substantially stronger than matching vertex sets or drawing a gluing square.

No fatal gap was found in the two main pullback arguments when their full hypotheses are retained. There are small wording/convention issues and a separate erroneous classical-topological analogy in §5.2, explained below. Neither is needed for a direct, separately proved dessin diagonal-fiber construction.

## 1. Graph and map conventions

All graphs have countable vertex and edge sets. “Loop” means **any nonempty closed path**, while “short loop” means a one-edge self-loop (p.3). Thus “E₁ has no loops” in Theorem 3.4 means E₁ is acyclic, not merely that its adjacency matrix has zero diagonal.

Graph C*-algebras use CK1 for all edges, the sum relation at regular vertices only, and the range inequality (Definition 2.1, p.3). Infinite emitters are allowed. A pointed positive-length path is one whose final edge is not a short loop. The term is tailored to the particular path functor and must not be replaced by “path with a chosen basepoint.”

An admissible inclusion F⊂E (Definition 3.1, p.5) has all three properties:

- H=E⁰\F⁰ is hereditary and saturated.
- F¹ consists of **all** E-edges whose range belongs to F⁰.
- No vertex emits infinitely many edges into H and finitely many but positively many into F⁰ (the excluded breaking-vertex situation).

These guarantee the genuine graph quotient C*(E)→C*(F), with the expected hereditary ideal, not an arbitrary deletion map (Proposition 3.2, p.6). The third condition is automatic for finite graphs, but the first two remain necessary.

Lemma 3.3 (p.6) uses a **functor of path categories** f:F→E. It must reflect prolongation:
`f(α) is a prefix of f(β) ⇒ α is a prefix of β`.
At each regular vertex it must restrict to a bijection of outgoing **edges**. This produces a covariant *-homomorphism f*:C*(F)→C*(E), whereas admissible graph inclusions produce the opposite-direction quotient maps. One must preserve this distinction rather than announce one unrestricted contravariant graph functor.

## 2. Theorem 3.4: exact hypotheses and proof

Theorem statement starts p.6 and continues p.7; proof pp.7–8. Let F_i⊂E_i be admissible inclusions, i=1,2. Require:

1. E₁ is acyclic. E₂ has no **short** loops at vertices of E₂⁰\F₂⁰.
2. E₁⁰=E₂⁰ and F₁⁰=F₂⁰.
3. A path functor f:E₁→E₂ is identity on vertices, reflects prolongation as above, and its image is exactly the pointed paths (with the harmless zero-length convention described below).

Then the square with top C*(E₁), bottom C*(F₂), left quotient C*(E₁)→C*(F₁), right quotient C*(E₂)→C*(F₂), and horizontal maps f*, f|* is a pullback. The horizontal maps are injective, vertical maps surjective. If the vertex set is finite, these are unital algebras/maps.

The substantive proof steps were checked:

- Prolongation reflection forces injectivity of the path functor, including vertices, and prevents a nonempty edge from mapping to a length-zero path.
- At a regular source, surjectivity onto pointed paths prevents an image edge from having a nontrivial factorization. A short loop at its starting point would force infinitely many distinct preimage edges, contradicting regularity. Hence the outgoing-edge bijection required by Lemma 3.3 is proved rather than assumed.
- The acyclic-domain uniqueness theorem gives injectivity of f*. Admissibility ensures restriction/corestriction to F_i.
- Abstract pullback recognition reduces the conclusion to ker π₂⊂f*(ker π₁). The hereditary ideals are closed spans of S_αS_β* ending in the removed vertex set. Absence of short loops at those endpoints makes these positive paths pointed, so all their factors have preimages. Vertex generators are already covered by f being identity on objects. Closure of the *-homomorphism image passes the algebraic inclusion to C*-algebras.

The role of each condition is visible here. In particular, neither acyclicity nor the ideal/path-surjectivity condition may be dropped just because all vertex projections are nonzero.

## 3. Sink extension: Lemma 4.1 and Theorem 4.3

General setup GS, p.8, takes a discrete graph X and **injective** maps X→E⁰, X→H⁰. The vertex pushout joins E and H along these named vertices, retaining all edges.

Lemma 4.1 (p.9) assumes at least one side maps X into sinks. Its algebra is not the plain amalgamated free product: one additionally quotients by the ideal generated by products of nonidentified vertex projections from the two sides. The resulting orthogonality-enforced amalgam is C*(E⊔_XH). The sink condition ensures that CK sums at glued vertices are not incorrectly duplicated. The universal-generator proof can be checked directly; an arbitrary two-sided regular-vertex gluing would fail this argument.

The second main theorem is **4.3**, p.10, proof pp.10–12. Its full setup comprises the material before and after equation (4.11), not just the short theorem-header cross-reference to assumptions before (4.6):

- The two embeddings of X land in sinks of both E₁ and E₂; X→H⁰ is injective.
- There is already a pullback square C*(E₁)→C*(E₂), C*(E₁)→A, C*(E₂)→B, A→B.
- The horizontal map φ is injective, takes vertices to vertices and edge partial isometries to **path** partial isometries, agrees on X, and sends non-X vertices to non-X vertices.
- Every path partial isometry in E₂ ending at a glued sink belongs to im φ.
- The map δ:C*(E₁)→A kills the glued vertex projections.

Extending φ by identity on C*(H), and δ and θ by zero there, gives a new pullback after attaching H. A and B need not be graph algebras.

The proof's sink geometry prevents a new cycle from alternating between E_i and H, allowing the general uniqueness theorem to prove injectivity. Lemma 4.2 identifies the extended kernels. The already-pullback condition handles the old kernel; the ending-path coverage and annihilation of gluing vertices handle the ideal generated by H. The equalities of images and kernel containment are separately checked. No step removes the ending-path condition or upgrades the construction to arbitrary self-identification of sinks.

## 4. Applicability to the actual dessin objects

The permitted-arrow-state graph of a closed dessin is a finite disjoint union of directed cycles. It is not acyclic and has no sinks. Consequently:

- It cannot simply be E₁ of Theorem 3.4.
- Its ordinary vertices cannot simply serve as the glued sinks of Theorem 4.3.
- For such a disjoint-cycle graph, hereditary vertex deletions remove entire components. An arbitrary pairing of two dart vertices is not an admissible inclusion/quotient of the required kind.
- A cycle of length >1 is itself a pointed closed path under the paper's convention. A vertex-identity acyclic path functor cannot surject onto that path. Thus the all-pointed-path hypothesis specifically obstructs a naive use of Theorem 3.4 for these cycles.
- A noninjective map identifying two sink occurrences **within one branch** does not meet the injectivity assumptions of GS merely because the vertices happen to be sinks.

There is, however, an explicit useful graph presentation of the **constrained Fock** algebra, which can be proved before invoking any pullback theorem. Use graph vertices indexed by the nonzero projections Q_a and the vacuum projections v_e. For each original arrow state a introduce two graph edges represented by
\[
S_a=L_aQ_{\tau(a)},\qquad T_a=L_av_{t(a)}.
\]
They have initial projections Q_(τ(a)) and v_(t(a)), orthogonal ranges contained in Q_a, and range sum Q_a. Thus the graph has a cycle edge a→τ(a) and an exit a→the vacuum sink at t(a). All cross-edge CK1 relations follow from the orthogonal prefix ranges and the orthogonal initial pieces. The projections sum to identity, and L_a=S_a+T_a. Hence the graph family generates the original Fock algebra. Its nonzero vertex projections and inherited gauge action give a faithful graph presentation by gauge-invariant uniqueness. This does not extend the bounded representation to all formal-order series.

This exact presentation creates genuine vacuum sinks and permits a precise investigation of sink attachments. Each proposed use of Theorem 4.3 still requires a specified original pullback and the listed path/annihilation conditions. It does not justify merging all normalization-branch sinks indiscriminately. A separately defined diagonal-fiber C*-algebra may be perfectly valid, but should be proved through its own actual *-homomorphisms rather than mislabeled as an automatic application of this source.

For the nodal interval specifically, the graph has two loop states, each with an exit to the common vacuum sink. Replacing each loop-plus-exit family by countably many edges to that sink gives an acyclic E₁; send its nth edge to loop^n followed by exit. With the quotient retaining the two loop states, this is a concrete candidate satisfying Theorem 3.4. It computes a particular AF pullback of the Fock graph algebra along the constant inclusion C²→C(T)², not an identification of that AF pullback with the original order/Fock algebra. Higher permitted cycles require another verified construction.

## 5. Small source cautions and a genuine unrelated example defect

- Definition 2.2 speaks of the final edge of a pointed path, while Theorem 3.4 describes the image of an object-preserving functor as all pointed paths. Vertices have no final edge. Read this with vertices included separately, or state the image condition only on positive-length paths. The proofs already cover the vertex images; this is a convention omission, not an obstruction to the main theorem.
- In Lemma 2.3, p.3, the phrase that S_γ* is an element of a linear basis of C*(E) should not be read as a countable Hamel basis for an infinite-dimensional C*-algebra. The dense graph *-algebra/basis result is being used to certify nonvanishing. More directly S_γ*S_γ=P_(rγ)≠0 proves this without that phrasing. The prefix criterion remains correct.
- **Section 5.2, p.13, misidentifies the usual classical coarse weighted projective line WP¹(1,2) as S²∨S².** In the standard weighted quotient the continuous map `[z₀:z₁]↦[z₀²:z₁]` is a bijection onto CP¹, hence a homeomorphism by compactness/Hausdorffness. Its coarse space is S². Collapsing an equator in S² instead gives S²∨S², whose second homology has rank two rather than one. Thus the stated classical interpretation is not valid for the usual teardrop coarse space. The graph-C*-algebra pullback in (5.5) can remain valid; the topological deformation analogy should not be imported as a theorem about classical weighted projective lines. This issue is unrelated to the proposed dessin construction.

The remaining examples illustrate the stated graph hypotheses rather than broaden them: Podleś sphere §5.1, quantum projective spaces §5.3, and multi-sink teardrop extensions §5.4. They supply no arithmetic descent, Frobenius action, purity theorem or completed-L determinant comparison.


## Addendum: the literal nodal pullback application

The following specific instance has been checked against every hypothesis. Let E₂ have loop states x,y, a vacuum sink v, loops l_x,l_y and one exit t_x:x→v, t_y:y→v. Its graph algebra is the previously proved nodal constrained Fock algebra. Let F₂ retain x,y and their loops. Let E₁ have the same three vertices, countably many edges e_(x,n):x→v and e_(y,n):y→v, n≥0, and no other edges; F₁ retains x,y with no edges. Send e_(x,n) to l_x^n t_x and similarly for y, and be identity on vertices.

The removed subset {v} is hereditary and saturated in both graphs. The retained edges are exactly those ending in the retained vertices. In E₁ the infinite emitters send zero edges outside {v}; therefore the “finitely many but not zero outside” breaking-vertex exclusion is satisfied. The path functor is injective and prefix-reflecting: two different loop^n-exit words are never prefixes of one another, and the same holds for the source single edges. Every positive pointed path in E₂ is exactly one such word. E₁ is acyclic and v has no short loop. Hence Theorem 3.4 gives
\[
C^*(E_1)\cong\mathcal T_A\times_{C(\mathbb T)^2}\mathbb C^2,
\]
with the constant-function inclusion on the second factor and the symbol quotient on the first. This is the **subalgebra of Fock operators whose two symbols are constant**, not an isomorphism of all of T_A with an AF algebra. E₁ is acyclic, so its graph algebra is AF; it has no regular vertices, giving K₀≅Z³ and K₁=0. The original nodal Fock algebra instead has K₀≅Z² and K₁≅Z. The distinction is consistent and must remain explicit.
