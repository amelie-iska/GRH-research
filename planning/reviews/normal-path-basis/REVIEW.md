# Independent review: unbounded normal path-image independence

Reviewer `/root/branch_extension_review`, 2026-11-03. This is the next P4
formalization slice for the actual infinite polynomial genus-two dessin
algebra. The production agent owns Lean, paper and checker edits; this
reviewer writes only this report and artifacts under
`outputs/checks/2026-11-03-normal-path-basis/review/`.

## Mathematical argument and actual scope

Write B=Mat5(k[t])×Mat5(k[t]) over a field k. Its algebra generators are
the shared stationary idempotents `(Eii,Eii)` and the two independent
branch arrows with entry `t` on the wrap from0 to4 and entry1 on the
other decrements. Matrices act on column vectors: the rightmost factor
acts first. Thus a walk beginning at j and ending at i has image
`t^q Eij` in its chosen branch when its positive length is

\[
\ell=5q+j-i.
\]

The exact normal index set consists of five stationary indices and all
tuples `(branch,i,j,q)` with q natural and `i<j OR q>0`. This admissibility
condition is essential. When q=0 only strictly upper entries occur; a
diagonal constant belongs to the shared stationary index, not two
independent branch indices. For q>0 every entry is allowed. Omitting the
admissibility condition would introduce a false claim about stationary
constants or entries not arising from directed positive paths.

For a stationary key r, take the coefficient of t0 in entry(r,r) of the
first matrix factor. For a positive key `(b,i,j,q)`, take the coefficient
of tq in entry(i,j) of factor b. These selectors are k-linear and
biorthogonal to the stated images. Different branches, entries and
degrees cannot collide; a positive key cannot be a diagonal constant by
admissibility. The first-factor stationary selector vanishes on the
second branch automatically and on every admissible first-branch
positive image. Every positive selector vanishes on stationary images.

Apply a key's selector to an arbitrary finite linear combination that
vanishes: its coefficient equals zero. This establishes linear
independence and injectivity of the linear-combination map on *all*
finitely supported functions on this infinite key set. There is no
degree or length bound in this argument. It uses no signs, division,
averaging, roots of unity or characteristic restriction: characteristic2
works. A nontrivial scalar field is needed, as provided by `[Field k]`.

The length formula is genuinely positive on the admissible indices.
If q=0, i<j gives positivity. If q>0, then5q+j≥5>i, since i≤4. This
also justifies using natural subtraction without accidentally admitting
truncated-subtraction solutions. Conversely, for any positive integer
length and initial vertex j, its endpoint is i=(j−ell)mod5. The integer
q=(ell−j+i)/5 is a nonnegative integer, and `i<j OR q>0` follows. Counting
wraps in the decrement walk gives exactly q occurrences of its wrap
arrow, hence the monomial image. These facts identify the index set with
the positive directed walks without imposing a finite cutoff.

For an admissible key carrying a proof witness, the witness is a
proposition, not extra path data. Lean's proof irrelevance must identify
indices with the same branch, endpoints and degree but different proofs;
a separate spurious copy of a basis vector for each witness would be
incorrect.

The algebra already defined in the project is the generated subalgebra
A⊂B. Independence in B does not alone prove that a purported family has
been constructed in A: each displayed monomial must additionally be
identified with the image of its genuine walk, or its subalgebra
membership established. Nor does independence prove spanning, the
abstract path-quotient ring equivalence, the pullback characterization,
completion, full category equivalences, almost-split universality or the
arithmetic determinant bridge. These are separate formalization
boundaries even when corresponding prose proofs are present.

## Independent diagnostic checks

The reviewer oracle uses only standard-library Python, no production
imports. It multiplies walks by decrementing the current column vertex
and counting wrap factors, then compares the resulting monomial with
the claimed endpoint/degree image. It separately evaluates all proposed
selectors and finite linear combinations in rational and prime fields.
Seed20261103 is fixed and reported.

`review/oracle.py`, `review/oracle.json` and `review/oracle.log` record:

- 520 admissible positive path images and5 stationary images, including
  degrees1000 and lengths through5004;
- 275,625 biorthogonal selector pairs;
- 200 finitely supported combinations over Q,F2,F3,F5;
- 1,015 independent endpoint/turn reconstructions.

All checks pass. These finite diagnostics support convention and
characteristic checks; they are not a proof of the unbounded claim. The
universal coefficient-selector derivation above and the actual Lean
theorem types must carry that claim.

## Formal snapshot

**Accepted for the explicitly bounded formal scope.** I independently
compiled the final `lean-analytic/BranchExtension.lean` using the pinned
Lean4.24/mathlib environment with `-DwarningAsError=true`: exit0, no
warnings or errors. The mathlib HEAD is the recorded
`f897ebcf72cd16f89ab4577d0c826cd14afaafc7`, and its manifest matches
`lean-analytic/mathlib-manifest.json`. No dependencies were installed,
upgraded or downloaded. The focused file prints29 theorem types and
dependency reports:21 pre-existing declarations plus8 new declarations.

I read the literal new types and proofs:

1. `slot_ext` identifies proof-carrying slots from their row, column and
   degree, correctly using proof irrelevance. Its dependency report is
   axiom-free.
2. `positive_length`, `length_equation`, and `same_start_length` prove
   positivity, rearrangement of natural subtraction, and uniqueness of
   endpoint/degree from a fixed start and length. These depend only on
   `propext` and `Quot.sound`.
3. `selector_vector` proves the actual biorthogonality formula for every
   two keys, with `[Field k]` and no degree bound.
4. `coefficient_recovery` quantifies over an arbitrary `Key →₀ k`, not a
   preset finite family or bounded polynomial degree. Its conclusion is
   selector recovery from actual `Finsupp.linearCombination`.
5. `normal_vectors_independent` asserts actual `LinearIndependent k`
   for the displayed polynomial-pair family.
6. `normal_form_injective` asserts actual injectivity of the same
   `Finsupp.linearCombination` map.

The latter four reports use only `propext`, `Classical.choice` and
`Quot.sound`. There is no `sorryAx`, admission, project-specific axiom,
quotient-isomorphism hypothesis, spanning hypothesis or hidden arithmetic
premise. In particular the degree is genuinely an unrestricted natural
number. `Ambient` is the actual pair of polynomial matrix spaces; the
new family is deliberately not falsely typed as an already-proved basis
of the generated subalgebra.

The focused compilation and literal type/dependency output are retained
in `review/lean-focused.log`. `review/snapshot.json` records all hashes
and eight individual dependency reports. Final Lean source SHA-256:
`8b56c73a4960ec9a7c6d03e1aca3be24b93a0a1c491812c6e352687f265c7160`.

## Production diagnostic replay and exposition

I separately read and ran
`examples/relations/check_normal_paths.py`, directing output to the
reviewer-owned `review/production-exact.json` to preserve the original
generated evidence. It passes:

- 475 normal keys, including degree1,000,003 and length5,000,019;
- 225,625 selector pairs;
- 1,030 direct arrow-by-arrow checks;
- 15,625 product comparisons, including noncomposable and mixed-zero
  cases;
- 200 exact finite expansions over Q,F2,F3,F5;
- 17 invalid-slot rejections.

Its multiplication respects the rightmost-first column convention,
including stationary factors and branch-zero products. These are finite
diagnostics; the unbounded independence claim comes from the formal
theorems, not from testing a large degree. Checker source SHA-256:
`1680aa056d7edce17598d6a74df950e837d0d90ac97d702833395c4ab46c705d`.

I read the final new theorem/proof in `papers/branch-extension-core.tex`
and the complete new coefficient-selector subsection of
`papers/branch-extension-details.tex`. The prose matches the actual Lean
scope, including admissibility, stationary/positive separation,
finite support, characteristic independence and proof-witness
irrelevance. Its concrete examples are correct: the length12 path from4
to2 gives `t²E24`, the length4 path from3 to4 gives `tE43`, and their
rightmost-first product is `t³E23` of length16. Changing the second path
to the other branch makes the product zero. The text explicitly retains
generated-algebra membership, spanning and the quotient algebra
equivalence as separate formalization obligations.

Reviewed prose hashes:

- Core: `bcf4bf8f7bb170cda307887e138558076957868db4662bf7e6e92d3ef7f01750`
- Details: `a0e6cf9c6fbde41c59c3375d354883dc52ea72474109d6b4f966809382e87821`

No mathematical blocker remains for integrating this slice. I did not
rerun the entire analytic suite or build/visually inspect PDFs; those are
the production agent's integration checks. The result formalizes the
unbounded normal-image faithfulness component. It does not complete the
path-quotient algebra/category construction, almost-split universal
property, formal completion, or GRH proof.
