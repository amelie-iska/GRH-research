# Independent review: genuine infinite dessin algebra and nonsplit branch extension

Reviewer `/root/branch_extension_review`, 2026-11-03. The assignment is an
adversarial review of the new P4 categorical/formal construction, not a new
audit of all historical manuscripts. Read the current relation construction
in `papers/relations-core.tex` and `papers/relations-details.tex`, its existing
independent review, project README, local fixed Lean script/toolchain and the
current source-expansion handoff. Original sources, production files, Git,
environments and configuration were not changed. Only this report and
reviewer-owned artifacts under
`outputs/checks/2026-11-03-branch-extension/review/` were written.

## The polynomial algebra is genuinely the infinite dessin algebra

Use coefficient field k, vertices0,…,4, arrows a_i,b_i:i→i−1 modulo5 and
the mixed length-two zero-relations. Represent paths in their direction of
travel on column vectors, so the rightmost arrow acts first. Put

- e_i=(E_ii,E_ii);
- a_i=(w_i E_(i−1,i),0), b_i=(0,w_i E_(i−1,i));
- w_0=t and w_i=1 for i=1,…,4.

These generators satisfy orthogonal idempotents, sum_i e_i=1, all endpoint
relations and exactly the required mixed products. A nonzero positive-length
path stays on one branch. For a path starting at j, ending at i, of length
ell, write ell=j−i+5q. Its image is t^q E_ij in that branch. For i<j,
q≥0; for i>j, q≥1; for positive-length i=j, q≥1. Conversely each monomial
with these conditions occurs exactly once. The trivial path e_i supplies
the shared diagonal constant term. Thus the monomial path basis is sent to
independent polynomial-pair coordinates: different branches/entries/powers
cannot cancel, and the diagonal constants cannot be canceled by a positive
path. This proves injectivity of kQ/(mixed zero), not merely that the
relations hold in a finite representation.

Its image is exactly H×_(k^5)H, where H consists of polynomial matrices
upper triangular modulo t, and the maps H→k^5 are the diagonal constant
terms. The map on H is multiplicative: in a product's diagonal entry each
off-diagonal cross term has at least one strictly lower-triangular factor,
whose constant term vanishes. Every off-diagonal allowed monomial and
every positive diagonal power occurs on its own branch; shared diagonal
constants are furnished by the e_i. Hence this pullback description and
the generated-subalgebra description coincide. This is an actual infinite
polynomial algebra, not Mat5(k) or a finite arrow quotient.

For instance a1 a2 a3 a4 a0=(tE00,0). Its positive powers are independent.
Summing all five full turns on each of the two branches gives u=(tI,tI),
the central scalar polynomial parameter. The diagonal polynomial map
k[t]→A5 is injective, so A5 is infinite-dimensional over k. Its rank over
that central polynomial ring is50; the finite residue matching does not
change that rank. The u-adic completion is a distinct completed-order
object and should not be silently substituted for the polynomial algebra.

The geometry is the clean dessin on the complex compact curve y²=x5−1,
beta=x5, of genus2. The same monomial quiver presentation can then be
formed over an arbitrary coefficient field k. No characteristic restriction
is needed for the algebraic extension below; this does not assert that the
same displayed hyperelliptic map is a smooth genus-two dessin in every
positive characteristic.

## Actual modules and exactness

Let D=k[epsilon]/epsilon², with basis1,epsilon. On M1=k^5 the first matrix
branch acts by t↦0. On M2=D^5 it acts by t↦epsilon. The second branch
is killed, but the original ambient algebra still retains both branches.
These are unital representations of the actual infinite polynomial
algebra, because entrywise polynomial evaluation is a ring homomorphism
and ordinary matrix multiplication acts on column vectors.

Define i:M1→M2 coordinatewise by x↦epsilon*x=(0,x), and p:M2→M1 by
constant coefficient (x,y)↦x. For any polynomial P,
P(epsilon)=P(0)+P'(0)epsilon (the coefficient-of-t formula is valid in all
characteristics). Therefore P(epsilon)epsilon*x=epsilon P(0)x, and
p(P(epsilon)d)=P(0)p(d). Summing matrix entries proves both maps A-linear
for every algebra element, not just for the arrow generators. Addition,
injectivity of i, surjectivity of p and ker p=im i are coordinatewise.
The sequence is consequently a genuine short exact sequence in Mod(A5).
It is split as a sequence of k-vector spaces, which does not make it split
as a sequence of A5-modules.

The nonzero wrap arrow a0 acts as zero on M1. On M2 its output coordinate4
is epsilon times input coordinate0. If an A-linear section s of p existed,
p(s(e0))=e0 would make the constant term of (s(e0))_0 equal1. Hence the
coordinate4 of a0*s(e0) would equal epsilon, which is nonzero over any
field. But A-linearity gives a0*s(e0)=s(a0*e0)=s(0)=0. Contradiction.
This proof uses only1≠0, so characteristic2 causes no exception.

With the coefficient order(1,epsilon), multiplication by epsilon sends
the first basis vector to the second, exactly J2(0). Thus these modules
are N5(J1(0)) and N5(J2(0)) in the existing branch convention. The former
is the directed string of length4, while the middle term is the string of
length9. The nonsplit extension is a nonzero Ext1 class in the ambient
module category; no assumption of a derived fully faithful branch functor
is required. Both are finite u-torsion (uM1=0,u²M2=0), hence extend
continuously to the completion; neither is a nonzero DVR-free order lattice.

## Independent exact checks

`review/oracle.py` imports no production code or nonstandard dependency.
It uses sparse polynomial-pair matrices and exact rational/modular
arithmetic. It checks generator endpoint/zero relations,400 distinct normal
paths through length40, the actual full-turn and central parameter, and
300 whole-polynomial module-map checks on elements involving both branches
and powers through t8. It also assembles full generator-compatible Hom and
putative-section linear systems independently.

Over Q,F2,F3,F5, the section coefficient matrix has rank49 and its augmented
matrix rank50, proving finite equations inconsistent. The same independent
systems give End(M1) dimension1, End(M2) dimension2 and Hom(M1,M2) dimension1.
These finite checks corroborate the general arguments above; they do not
replace the full path-basis proof or prove the infinite assertion merely
by testing400 paths. Output and method are recorded in `review/oracle.json`.

No mathematical blocker was found in the proposed construction. Literal
production Lean/source review and a fresh independent compilation will be
recorded below when the root supplies the settled files. General AR
factorization/component classification, derived/HMS equivalences and the
arithmetic positive determinant/GRH bridge are not established by this
short exact module sequence.

## Final literal Lean and production replay

Read the entire final `lean-analytic/BranchExtension.lean`, including all
21 printed public theorem types and axiom dependencies. Independently ran
the focused file in the existing pinned Lean4.24/mathlib environment with
`-DwarningAsError=true`: exit0. All21 reports use only standard foundations
(propext, Classical.choice, Quot.sound); no error, admission dependency or
project-specific axiom occurs. Source SHA-256:
`1eed799b72a9e817c992128821f9e0a8643ae6fbb38e535e8bf6dc6e02437944`.

The literal type `A k` is the actual generated subalgebra of
Mat5(k[t])×Mat5(k[t]), retaining both polynomial branches and unbounded
degrees. The infinite-dimensionality result is not assumed: an actual
polynomial aeval map at the permitted turn has its full polynomial recovered
by the first(0,0) entry, proving injectivity; Module.Finite.of_injective and
Polynomial.not_finite then yield `¬Module.Finite k (A k)`. This avoids any
inference of infinity from finitely many tested powers.

The two actions are actual ring homomorphisms and Module instances on
k^5 and (QuadraticAlgebra k 0 0)^5. The inclusion/projection records prove
A-linearity for every A element using the coefficient evaluation formulas.
Injectivity, surjectivity, zero composite and range=kernel are actual module
map statements. `project_surjective` correctly uses a set-theoretic lift
only; it does not assert that constant lifting is A-linear. The no-section
theorem quantifies over all actual A-linear maps and assumes only the
section identity inside the contradiction argument. No nonsplitting,
desired positivity or finite representation predicate appears as a premise.

This fully checks the stated short-exact/nonsplit module construction over
the concrete infinite algebra. It does not package the path-quotient
isomorphism or H-pullback equality in Lean, an Ext/Yoneda object, a ModuleCat
short-complex adapter, all module classifications, almost-split universal
factorization or any arithmetic spectral bridge. Those distinctions in the
final TeX are correct. The normal-form identification itself was checked
directly in the prose review above.

Read the entire production `examples/relations/check_extension.py` and
replayed it with bytecode writes disabled and `--output` redirected to
reviewer-owned `production-replay.json`. It passes405 stationary/positive
normal paths,7225 path products,30 distinct loop powers,80 whole-polynomial
action samples through degree8 and all section systems over Q,F2,F3,F5.
Its flat coordinate order is all real/constant coordinates then all
infinitesimal coordinates; our independent oracle interleaves each pair.
These are merely permuted descriptions of the same module action. The
production flag `all_element_module_maps` refers to the separate general
Lean result; the numerical checker itself checks the stated finite sample,
as its header/scope explicitly says. No finite sample alone is accepted as
the infinite module-map proof.

Read both new TeX fragments in full. The normal path signs, multiplication
convention, cyclic monomial identification, polynomial recovery,
coefficient actions, short exactness and no-section proof match the formal
objects and direct mathematical review. No substantive mathematical or
code blocker remains. Two small wording refinements were suggested to root:
explicitly call the geometric dessin complex before permitting arbitrary
coefficient fields, and use “constant coefficient” instead of “real part”
for the dual-number coordinates over arbitrary fields. These do not change
the mathematics; their final wording can be checked independently of Lean.

Snapshots and raw evidence: `review/reviewed-snapshots.json`, `review/lean.log`,
`review/production-replay.{json,log}` and the independent oracle artifacts.
The integrating worker retains responsibility for full-suite, visual/browser,
generated-output, privacy and staged-push checks.

### Precision wording verified

The final core now explicitly says “complex genus-two clean dessin” and
the no-section proof uses “constant coefficient”; the detail paragraph also
uses “coordinate-zero constant coefficient.” Reread these edits; both
precision suggestions are resolved. No outstanding review finding remains.
Updated source hashes are in `review/reviewed-snapshots-final.json`.
