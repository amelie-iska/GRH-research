# Independent review: normal coordinates of the generated infinite algebra

Reviewer `/root/branch_extension_review`, 2026-11-04. This reviews the new
slice after baseline `a07b1c1`: actual membership of every normal image,
spanning of the generated algebra and its bijective finite normal
coordinate map. I read the entire new Lean delta and research derivation,
and independently compiled the focused file. Production files and Git
state were not edited by this reviewer; reviewer writes are confined to
this report and `outputs/checks/2026-11-04-normal-path-algebra/review/`.

## Mathematical construction and absence of circular premises

The underlying algebra A is the existing actual generated subalgebra of
Mat5(k[t])×Mat5(k[t]), over an arbitrary field. It retains both branches
and shared stationary idempotents. No abstract path quotient or its
unproved equivalence is introduced as an assumption. The prior
biorthogonal coefficient selectors prove ambient independence for the
unbounded key set; this extension supplies the previously missing actual
membership and spanning arguments.

The new recursive walk is A-valued from its definition:

\[
W_b(0,j)=e_j,\qquad
W_b(n+1,j)=W_b(n,j-1)\,a_{b,j}.
\]

Here matrices act on columns and the rightmost arrow acts first. Let
P_b(i,j) be the shortest *positive* walk from j to i: length j−i if
i<j and5+j−i otherwise. In particular P_b(i,i) is a full length-five
turn, not the stationary idempotent. The checked finite-vertex
calculation gives its image as the one-branch monomial t^dEij, with
d=0 when i<j and d=1 otherwise. Although that endpoint calculation
enumerates the fixed five vertices, the next step is an actual induction
on an unrestricted natural n:

\[
\operatorname{view}\big(P_b(i,i)^nP_b(i,j)\big)
       =t^{n+d}E_{ij}\quad\text{in branch }b.
\]

For each admissible slot `(i,j,q)`, its condition i<j or q>0 proves
q≥d. Choosing n=q−d therefore constructs a genuine A-element with
the desired image. The subtraction equality is justified before use;
there is no silently truncated exponent. No polynomial degree or path
length cutoff occurs in this membership theorem.

The normal image span is closed under multiplication. Shared stationary
images multiply by the vertex rule and select the appropriate row or
column of a positive image. Different branches and nonmatching endpoints
multiply to zero. Same-branch matching images multiply to
t^(q+r)Eil. Its output key is admissible: if q+r=0, both inputs have
degree0 and strictly upper entries, so their composite is strictly upper
by transitivity. Otherwise the summed degree is positive. This correctly
excludes an independent one-branch constant diagonal, including in
characteristic2.

Double span induction extends that multiplication rule to arbitrary
finite normal combinations. The span contains1, the sum of the five
shared stationary images, and contains every original arrow generator.
Actual `Algebra.adjoin_induction` then proves that the entire generated
algebra lies in the span. The reverse inclusion uses the constructed
membership theorem. Thus `surface_eq_normalSpan` proves equality of the
actual submodules; spanning is discharged rather than presumed.

Each normal image is then lifted into A with its proved membership.
Ambient independence transfers through the actual inclusion. The span
equality supplies surjectivity of `Finsupp.linearCombination k lift` and
independence supplies injectivity. Consequently the defined

\[
\mathrm{normalEquiv}:(\mathcal K\to_0 k)\simeq_k A
\]

is a genuine linear equivalence for every field, and its inverse
coordinates are the actual polynomial-entry coefficient selectors.
Finite support is retained; no formal infinite expansion or topology is
being assumed. No signs, division, positivity or characteristic-zero
premise occurs. Admissibility witnesses remain proof-irrelevant.

## Fresh kernel check and literal theorem scopes

Independently ran the final focused source using the existing pinned
Lean4.24/mathlib environment and `-DwarningAsError=true`: exit0, no
warnings or errors. The detailed output is `review/lean-focused.log`.
The new public reports are:

- `lifted_normal_power`: arbitrary natural powers of the actual A-valued
  walks have the stated polynomial-pair images;
- `positive_mem_surface` and `vector_mem_surface`: every admissible
  positive image and every full key image belongs to the generated
  subalgebra;
- `view_lift`: the constructed A-element has exactly the intended image;
- `lifted_vectors_independent`: actual linear independence in A;
- `vector_mul_mem_normalSpan`: all normal image products remain in the
  actual linear span;
- `surface_eq_normalSpan`: equality of the generated algebra's underlying
  submodule and normal span;
- `view_expansion`: inclusion intertwines the two actual finite linear
  combinations;
- `lifted_expansion_bijective`: the A-valued linear-combination map is
  genuinely bijective;
- `normalEquiv_symm_coefficient`: inverse normal coordinates are the
  displayed selectors evaluated on the included A-element.

All ten new reports use only `propext`, `Classical.choice` and
`Quot.sound`. There is no `sorryAx`, custom axiom, hidden membership or
spanning premise, presumed quotient equivalence, or desired arithmetic
positivity hypothesis. The complete focused file has39 public
type/dependency reports,29 pre-existing and10 new. This count concerns
this file, not all theorems in the book.

## Independent finite diagnostics

The reviewer oracle `review/oracle.py` imports only the Python standard
library, without any production module. Its sparse dictionaries represent
actual polynomial matrix pairs. It constructs shortest walk products
arrow by arrow, forms arbitrary tested powers by binary multiplication,
and compares them with the proposed positive monomial. Separate raw
matrix-pair multiplication and normal-key product rules are compared.

It passes:

- 320 constructive generator-product preimages plus5 stationary images,
  through degree1,000,003;
- 105,625 normal-image product comparisons;
- 400 generated polynomial-expression reconstructions over Q,F2,F3,F5,
  with seed20261104 and rational coefficients in the Q cases;
- 25 rejections of unmatched diagonal constants or forbidden constant
  lower entries.

Reconstruction checks every raw coordinate before expansion, so it does
not hide a bad component by projecting onto admissible ones. The original
matrix factors are retained, including the shared stationary diagonal.
Evidence is in `review/oracle.json` and `review/oracle.log`. These are
finite diagnostics of conventions and implementations; the unrestricted
membership, span and bijection claims rest on the kernel-checked proofs.

## Remaining boundary and final integration review

The result is a linear coordinate equivalence of the already-defined
generated algebra. It does not yet construct a separate concatenation
path algebra, impose its abstract mixed-zero quotient and verify an
algebra homomorphism's universal property. Nor does a k-linear equivalence
alone preserve multiplication or identify categories. A formal comparison
with that separately constructed ring, completion, order-lattice or module
categories, almost-split sequences and AR components remain separate
tasks. No arithmetic determinant or GRH result follows from the basis.

**Accepted for the stated mathematical and formal scope.** I read the
complete current tracked diff from `a07b1c1`, the new untracked research
derivation/checker/evidence, and both frozen TeX additions. The core
theorem accurately states a linear isomorphism with the actual generated
algebra. The detailed proof correctly distinguishes the length-five full
turn from the stationary path, uses the whole unit at exponent0, and
handles the degree-zero multiplication case. Its example
`P_a(2,4)=a3 a4` and `C_a(2)^2 P_a(2,4)` has image `t²E24` and length12;
the wrap example `P_a(4,0)=a0` needs no inverse or negative power. All
match the literal Lean construction. The separately constructed path
quotient and categorical boundaries remain explicit.

The two generated book chapter bodies match the reviewed papers exactly
after their single generated-comment prefix. The project-page code-source
and exact-data additions state the same scope and retain the single
canonical relation laboratory. I read these code/HTML changes; I did not
launch a browser, inspect rendered PDFs or independently rerun all book
and suite integration checks. Those remain the production agent's lane.

The new production `examples/relations/check_normal_algebra.py` was read
and independently replayed to reviewer-owned `production-exact.json` and
`production-exact.log`. It passes50 shortest arrow words,375 normal
preimages,5,625 product round trips,200 exact expansions and187 nonzero
generated products over the four stated fields. Three forbidden constant
shape controls fail reconstruction as intended. Its coordinate reader
alone can project arbitrary ambient inputs; the test explicitly checks
the full expansion round trip, so it does not falsely accept those
controls as A-elements. This evidence matches both the primary exact
JSON and the identical web dataset. The independent oracle above does
not import this production reader or multiplication code.

The one nonmathematical integration correction is **resolved**. Prior
subsections in `book/VERIFICATION.md` and `lean-analytic/README.md`
initially described the preceding350-report milestone as current and
left membership/spanning open. I inspected the corrected paragraphs:
the book now titles it a prior ambient milestone, labels178pages/350
reports as historical and points to the next section for discharge of
membership/spanning. The analytic README likewise states that they
were open then and are proved by the following construction. No theorem
or Lean source changed; the compiled hash is unchanged. The production
agent owns the final handoff and full-suite/build integration results.

`review/snapshot.json` pins the focused compiler result, all ten new
dependency reports, source hashes, matching pinned manifest, matching
paper/book bodies and replay/web data. Principal frozen hashes:

- Lean: `94f15ffe4a6b8e1c10637d6a788411eb80035f68233b9aeb13b2224c2acf4017`
- Checker: `8ef8813a51e5854166ee540ef2cd962ff58d0881c46ddaec376e8891e69faff7`
- Core TeX: `3b00bb388dd04d09f36d1197a60409bafeeccdeaae00f6f07fcb29546f64e49c`
- Detail TeX: `ceaf52c36abbead7e8310c131a686dd10001a5d73f0da915205b1d93b1ec9c76`
- Independent oracle: `9f7f8e5a0d2bcaae94368ead31e7c1f082ee758e2f98ca638b0cb313d1566b9d`

The existing mathlib HEAD is
`f897ebcf72cd16f89ab4577d0c826cd14afaafc7`; its manifest bytes still
match the project pin. No dependencies, configurations, source clones,
existing evidence or unrelated worktree changes were altered by this
reviewer. No GRH or global categorical completion is inferred.
