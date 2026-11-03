# Independent adversarial review: projective resolutions and determinant program

Reviewer: independent read-only subagent `surface_completion_audit`. Date: 2026-11-03. Project root: `/Users/amelieschreiber/Documents/LaTeX-projects/GRH`.

## Result and precise limits

The new account gives a correct explicit resolution for finite quadratic monomial quivers, correct right-module Ext/Tor counts and signed Cartan inversion, and a valid compact proof of the weighted locally gentle determinant formula. The direct completion argument is sound; it does not assume flatness of an unspecified completion. The node and central special-fiber calculations distinguish actual derived specialization from an incorrect exactness claim. Functional duality and positivity are separated correctly. The arithmetic part is explicitly conditional and does not constitute a GRH proof.

I found no counterexample to the principal resolution, signed inversion, cycle determinant, finite cohomological cancellation, positive-purity, obstruction, or closure theorems as stated. Two wording/hypothesis issues were identified and corrected during review: the closed split subclass now has explicit incidence hypotheses, and the determinant-line discussion now uses a rational trivialization on its invertibility locus. I reread both corrections and accept them. The history and mathematical reasons are retained below; there is no outstanding principal-theorem correction from this pass.

This report is an independent mathematical and code review, not a formal verification of all imported geometric/arithmetic literature. I checked every line of the two new mathematical bodies, both new Lean modules, and the finite checker. Existing external-literature review is separately recorded in `/tmp/grh-surface-II-review.md`; not every theorem of every cited reference was reread in this pass.

## Coverage and snapshot

Read in full:

- `papers/resolutions-core.tex`: lines 1–208, all sections and proofs.
- `papers/resolutions-details.tex`: lines 1–218, all appendices, proofs and implementation tasks.
- `lean-analytic/ResolutionDeterminant.lean`: lines 1–61.
- `lean-analytic/DualNumberResolution.lean`: lines 1–172.
- `scripts/check_projective_resolutions.py`: lines 1–434.
- Supporting `lean-analytic/README.md`, `lean-analytic/DEPENDENCIES.json` and `scripts/check_analytic.sh` for toolchain/scope.

Snapshot hashes recorded during review (these are snapshots, since the author was actively integrating feedback):

| File | Bytes | SHA-256 |
|---|---:|---|
| core | 25311 | `fa26940f081f4a1c02a0f3501b44a13ffa18e753e94f3b338b8689b9954ba4f4` |
| details | 30621 | `d19806c28c1b754e2c9946466961840fd3f3538cbed2968dfabebb65270df1ac` |
| ResolutionDeterminant.lean | 2675 | `0af562e374ce22245e1a032d5e6242f1976221a7cb85521a0ee6979fd0910f09` |
| DualNumberResolution.lean | 5955 | `58487840ee31a19a67e68129144b0e16b32986a558344df59e16b9c7e12bd4fa` |
| checker | 18428 | `4c3048bbcd8eae127bc244def52e38631ed6937737d5b83c387c4838c745c790` |

No shared source was changed. The checker was imported with a non-main run name, so its fixed shared output writer was not called. The independent report is the only generated artifact deliberately written by this review.

## 1. Exactness with branching: checked, including the nongentle case

Core lines 4–27 correctly assume a **quadratic monomial** ideal: a set of composable length-two paths, rather than arbitrary quadratic linear combinations. This hypothesis is essential for all path-support arguments.

For a right module, left multiplication by the last arrow sends

`e_{t(a_n)} A -> e_{t(a_{n-1})} A`

into the prefix summand, using travel-order composition. The map is right-linear. With internal shift `(M<n>)_d=M_{d-n}`, it has degree zero. The composability and shift signs are correct.

The central exactness point is not restricted to one forbidden successor. If `a` has several forbidden successors `b`, then the kernel of left multiplication by `a` is the **direct sum** of the right ideals `bA`, each supported on a distinct first arrow. A surviving path prefixed by one arrow cannot equal a surviving path prefixed by a different arrow. Accordingly, in a fixed prefix summand no cancellation between the nonzero images of distinct last arrows is possible. Once their individual kernels are identified, these are exactly the images of the next forbidden-chain summands. This proves exactness for arbitrary finite quadratic monomial quivers, regardless of branching. The locally gentle hypothesis first becomes relevant later for at-most-two arms and transition graph factorization.

The current text correctly says **graded** minimality and explicitly avoids identifying the ordinary arrow ideal of an infinite ordinary path algebra with its Jacobson radical. For example, `k[x]` has ordinary Jacobson radical zero, whereas its graded augmentation ideal is `(x)`. This previous ambiguity has been removed. The sum of the vertex simples is `A/J`, so its displayed linear resolution gives the ordinary semisimple-degree-zero Koszul property claimed here.

Independent additional finite tests specifically exercised branching beyond the four shipped gentle examples:

1. Vertices `0,1,2,3`; arrows `a:0->1`, `b:1->2`, `c:1->3`; relations `ab=ac=0`. The arrow `a` has two forbidden successors. The resolution and signed inversion checks passed: 264 square-zero and 264 exactness checks through internal degree 10, both matrix products through series degree 12. Forbidden-chain counts by degree begin `4,3,2,0,...`.
2. Vertices `0,1,2,3`; arrows `a:0->2`, `b:1->2`, `c:2->3`; relations `ac=bc=0`. The arrow `c` has two forbidden predecessors. The same checks and counts passed.

These tests supplement the support proof; they do not replace it. They should not be passed through the current cycle-factorization checker, which correctly requires partial-permutation transition graphs. Adding them to a separate resolution/series example set would improve shipped regression coverage without broadening the cycle theorem.

## 2. Right-module Ext, Tor and Euler matrix order: checked

Core lines 30–42 have the correct source/target orientation. For right modules,

`Hom_A(e_v A,S_j) = S_j e_v`,

so a forbidden chain **from i to j** indexes an Ext class in `Ext_A^n(S_i,S_j)`. A right simple tensored with the stated left simple uses `e_v A ⊗_A {}_jS`, again selecting endpoint `j`.

With `C_ij` counting paths from `i` to `j`, the Euler characteristic of the resolution of `S_i` contributes

`sum_j E_ij C_jl`,

so the direct argument gives **EC=I**, rather than a transposed or reversed matrix identity. The formal inverse is two-sided because constant terms are identity. Every fixed internal coefficient has only finitely many homological contributions (`n<=d`), so there is no illegal infinite alternating sum.

The sign is applied exactly once. `E` already includes `(-1)^n`; its inverse relation is `E(z)C(z)=I`. Details lines 43–60 exhibit the nodal double-sign failure explicitly: `C(z)E(-z)=1+4z+8z^2+...`. The complementary-relation algebra has the expected indexing words, while the opposite-quiver issue is kept separate from this numerical inversion.

Details lines 17–21 provide genuine comparison maps for Yoneda products. Removing a last arrow commutes with removing a fixed forbidden prefix. A word with a different prefix cannot acquire the designated prefix by removing only its final arrow when the remaining length is at least that prefix length. Thus both sides are zero on the other summands. The augmentation condition in degree zero is also correct. Composing the comparison lift with the suffix cocycle selects precisely the forbidden concatenation. The text acknowledges the conversion between homological and signed cochain shift conventions; no false extra Yoneda sign was identified.

## 3. Arrow-state determinant and cycle factorization: checked

Core lines 46–86 consistently use

`S_(i,a)=1_(s(a)=i)`, `T_(a,j)=1_(t(a)=j)`, `D_(a,a)=w_a`.

Thus `U+V=TSD` has the correct shapes (`m x m`) and puts the successor weight `w_b` in entry `(a,b)`. A length `r+1` path contributes `SD U^r T`, so `C=I+SD(I-U)^(-1)T` is correct.

The inverse is a formal augmentation-adic geometric series. Independent commuting variables and finite quiver ensure finite coefficients at each total degree. This is not an assertion about convergence at arbitrary numerical weights.

Sylvester gives `det C=det(I+(I-U)^(-1)TSD)`. Multiplication by `I-U` gives `I-U+TSD=I+V`, proving the ratio. Equivalently, the cleared identity holds over any commutative ring with the explicitly required inverse. There is no need to assume `U` and `V` commute.

For the component factorization it is necessary that each transition graph has at most one predecessor **and** one successor. Both are included in the locally gentle definition. Consequently the finite components are directed chains or cycles; a loop is treated explicitly. Forbidden cycles give `1-(-1)^length w(c)`. Primitive cycles are counted once modulo rotation; powers are not new components. The cancellation/critical case is naturally covered rather than excluded.

Details lines 76–92 give a legitimate two-vertex/four-arrow cancellation. Both transition cycles have length four and equal commuting product. The stated univariate matrix has determinant one since its numerator determinant is `(1-z^2)^2`; its inverse is the stated signed matrix. Infinite resolutions coexist with scalar determinant one. The script uses an isomorphic arrow labeling, with `b` and `c` interchanged relative to the manuscript. This should remain explicit in artifact documentation to avoid an apparent mismatch; it is not a mathematical discrepancy.

## 4. Completion, projective covers, node and special fiber: checked, with one hypothesis request

Details lines 23–25 prove completed exactness directly coefficient by coefficient. A completed element is a formal permitted-path sum. Prefixing an arrow injects on surviving supports, while the killed first-arrow branches are exactly the kernel. Finite outgoing arrow sets and finite direct sums at each fixed homological degree ensure that factoring off the first arrow is legitimate. Branch ideals and the displayed images are closed. No unproved completion-flatness assertion is used.

The Jacobson-radical argument is sound: for an element of the closed arrow ideal, the geometric series in `ax` inverts `1-ax` for every `a`. The semisimple quotient supplies the reverse inclusion. Vertex idempotents already lift, giving the relevant semiperfect/projective-cover setting. Applying Hom to the vertex simples again kills the maps.

The node calculations in core lines 89–107 and details lines 43–74 are correct. In the normalization description, equality of constant terms is a fiber product over `k x k`, not a nonexistent residue map from a Laurent-series field. The actual alternating rank-two simple resolution has the stated annihilators and disjoint branch supports. With `t=x+y`, the order is `k[[t]][x]/(x^2-tx)`, free of rank two over the DVR. A positive syzygy is torsion-free over this DVR, so it cannot equal the torsion simple. The unlabeled positive syzygy tail can have period one even though the ordered branch pattern alternates with period two.

Details lines 69–74 also correctly show that the branch module `Lambda/(y)` is nonperfect by an actual alternating rank-one resolution with nonzero Tor in every degree. Hereditary normalization does not transfer this finite-projective-dimension conclusion to the glued node.

The central specialization example is exact. The tensor complex over the dual numbers has `H_0=k`, `H_1=k`, and higher homology zero; the rank-one resolution of the special-fiber simple is a different complex. The independent checker recovered dimensions `(1,1,0)`. Details line 118 correctly distinguishes `H/tH` (dimension four) from the entrywise triangular image (dimension three): `t E_12` survives in the module quotient.

**Resolved hypothesis request, core line 109.** The completed path-algebra/pullback assertion is plausible and correct in the intended closed paired-incidence setting, but “closed split surface order” is not itself defined in the new account. State the combinatorial data: permitted successor is a permutation of the arrows, every original vertex has exactly the specified matched cycle incidences, the residue pairings identify those incidences, and there are no unmatched endpoints/isolated vertices unless separately handled. These assumptions are not true of every locally gentle quiver. They are what make each nonempty permitted path a unique matrix-entry coefficient and make all matching tuples reconstructible.

The revised text explicitly requires two incoming/outgoing arrows, unique permitted/forbidden successors/predecessors, two matched permitted-cycle incidences and no unmatched endpoints, resolving the scope issue. A useful explicit topology argument under those hypotheses is: if the permitted cycle lengths are bounded by `L`, then sufficiently long paths lie in arbitrarily high powers of the product uniformizers, while `t` is a positive-length central cycle sum. Since `tB` lies in the conductor and therefore in `Lambda`, inclusions of the form `J^r ⊂ t^(s+1) B ⊂ t^s Lambda` for sufficiently large `r` establish one cofinal direction; `t in J` gives the other. This would make “long permitted paths” a precise proof rather than an implicit surface-order convention.

## 5. Parameter exactness, derived geometry and imported scope

Details lines 94–123 correctly distinguish a complex (`d^2=0`) from an exact complex. The Buchsbaum–Eisenbud statement retains ranks and **grade**, not an unconditional height replacement over arbitrary Noetherian rings. Its role is limited to a commutative finite-projective realization; noncommutative arrow entries do not have the same minors theorem. The two-term `k[t] --t--> k[t]` example is a decisive and correct nonflat specialization warning. Rank-at-most-r uses (r+1)-minors. The independent-matrices example `A=[I_3 0]`, `B=0` indeed defeats an unconditional complementary-minor equality. Contractible unit entries are correctly allowed and canceled rather than labeled errors.

Details lines 125–177 distinguish derived localization, perfectness, right/right Hom from right/left tensor, line-field/endpoint data, exceptional band morphisms, and the hypotheses of imported gentle-surface models. These are proper restrictions rather than a new universal curve equivalence. The finite-dimensional models are not silently extended to arbitrary completed orders. The patching passage retains overlap isomorphisms and actual descent hypotheses. The affine Grassmannian, affine flag and Iwahori group/order distinctions are correct.

The genus counterexample from `sigma=(123)(456)` with the two stated pairings is consistent: the face permutations have one six-cycle versus three two-cycles, hence genera one versus zero with the same two length-three normalization cycles. It supports the limited claim that normalization type does not determine gluing/passport.

The abelian Weil algebra computation is also correct in characteristic zero: `d(theta g)=u g`, cohomology `k`. The separate negative-degree algebra with `d epsilon=1` is acyclic because its unit is a boundary; it cannot augment as a DG algebra to `k`. This is distinguished from the actual ordinary dual-number ring used in the module resolution.

## 6. Determinant functors and cancellation: checked, with one wording correction

Core lines 115–142 correctly limit elementary determinant lines to perfect complexes over a commutative base or a specified realization to one. The finite cohomological cancellation theorem needs only a chain endomorphism, not a Frobenius-equivariant splitting. Boundary characteristic factors cancel through the two exact sequences. Infinite periodic resolutions are explicitly excluded without further analytic structure.

The trace-log formula is valid in characteristic zero as a formal power series; its primitive-cycle interpretation does not supply an arithmetic realization. The Fredholm/regularized determinant alternatives in details lines 185–187 retain their distinct convergence and normalization demands.

**Resolved wording correction, details line 185.** An arbitrary perfect complex with endomorphism does not automatically supply a globally regular section with the alternating characteristic determinant. For example, a one-dimensional complex concentrated in an odd degree with identity endomorphism contributes `(1-u)^(-1)` to the determinant action on its determinant line; this has a pole. The determinant functor directly acts on isomorphisms, while `1-uF` is generally invertible only on a specified locus. Say that the cone/determinant construction yields the relevant **rational section or trivialization on the generic invertibility locus**, with the grading/sign convention specified. The revised text now states precisely this rational-trivialization scope and includes the odd-degree pole example. This resolves the issue; it was a local clarification, not a failure of the cancellation theorem.

## 7. Arithmetic scopes: no disguised GRH proof identified

Core lines 144–171 correctly invoke rather than derive the trace formula and Deligne purity. The geometric Frobenius convention is stated. Smooth projective curve constant cohomology has the weight-one middle factor; the open `G_m` weight-zero zero illustrates why arbitrary category/cohomology is insufficient. Weil II's formulation over finite-type morphisms over `Z` with fiberwise weights is acknowledged; the missing theorem is not misdescribed as absence of known local Artin purity.

The `F_5` elliptic benchmark is correct: affine counts `1,1,2,2,1` plus infinity give eight points, trace minus two, numerator `1+2u+5u^2`, inverse roots `-1±2i`. This finite check is explicitly not a derivation of general purity.

The alternating-duality counterexample is exact. The stronger details example `q=16`, `F=diag(2,8)` has `F^t J F=16J`, polynomial `1-10u+16u^2`, and `u=16^(-s)` zero real parts `1/4,3/4`. It has reciprocal symmetry but fails purity strictly inside the strip. Positive Hermitian similitude, on the same realization, does force the claimed modulus by the eigenvector quotient. These are different assertions, and the paper keeps them separate.

The positive-length Cartan obstruction is correct on the connected half-plane `Re(s)>0`: every finite cycle product has modulus below one, so determinant and reciprocal are holomorphic and nonzero. Multiplication by nowhere-vanishing holomorphic factors preserves this. Rouché on a small disk around an isolated zero refutes compact-uniform convergence to a nonzero holomorphic target with that zero. This applies to the stated Cartan family, not to arbitrary different approximants.

The conditional closure theorem is also correct. A positive generalized Hermitian pencil has real spectral parameter, hence zeros on the critical line after `z=-i(s-1/2)`. Compact-uniform convergence to a nonzero holomorphic limit prevents an isolated off-line zero. The paper explicitly does not construct the positive pencils for its arithmetic approximants. Taking Hermitian parts would generally alter determinants, as the text warns. The flow identity `Theta+Theta*=1` forces eigenvalues on the line only on genuine eigenvectors in the actual domains; the missing global realization, determinant/eigenvalue correspondence and positivity remain stated obligations.

The scope paragraph distinguishes primitive Dirichlet, finite-order Hecke, Dedekind and general Artin cases; it does not assume general Artin holomorphy. The concluding arithmetic claims are research tasks and conditional mechanisms, rather than established GRH.

## 8. Independent Lean and Python validation

After root confirmed readiness, I independently ran each new Lean file using the project's pinned Lean 4.24.0 and mathlib checkout, with `-DwarningAsError=true`. Both exited zero.

`ResolutionDeterminant.lean` verifies three declarations:

- General cleared rectangular determinant identity, over arbitrary commutative rings with finite matrix indices. Its inverse hypothesis is explicit: `(I-U)W=I`, and its splitting is `TSD=U+V`. It does not formalize path enumeration, formal geometric-series existence, partial-permutation cycles or the entire weighted Cartan theorem.
- Acyclic-pair characteristic determinant conjugacy/cancellation. Its square-matrix inverse condition is explicit, not an assumed equality of independent endomorphisms.
- The actual rational 2x2 alternating-duality witness, together with `2^2 != 2`. It is an elementary algebraic witness, not a full formal spectral-purity theorem.

`DualNumberResolution.lean` verifies thirteen declarations over an arbitrary field, using actual `QuadraticAlgebra k 0 0`, the regular module and the residue action pulled back along the augmentation. These include the nonzero square-zero epsilon, coordinate formula, all-degree exactness, augmentation exactness/surjectivity, projective regular terms and zero Hom boundaries. The file does not claim mathlib's categorical projective-resolution object or an abstract derived Ext identification, and the paper accurately discloses this.

Every printed theorem dependency consisted solely of `propext`, `Classical.choice` and `Quot.sound`. No `sorryAx` or fabricated GRH axiom appeared in these compilations. I did not independently rerun the entire existing Lean suite in this pass; root was separately running that suite.

The Python checker was read completely and invoked without its main writer. For each of the four examples, resolution/rank exactness checks through internal degree 10, both signed matrix products through degree 12, and three exact rational transfer/cycle determinant samples passed. Sample denominators were invertible. Totals for shipped resolution tests: 462 square-zero and 462 exactness checks (66 node, 66 dual number, 198 line, 132 critical). Signed matrix coefficient checks total 390 (26+26+234+104), and transfer samples total twelve. Specialization and period diagnostics passed. The period diagnostic compares labels directly and is not by itself a module-isomorphism formalization; the manuscript supplies the elementary branch-isomorphism argument.

My first import driver used an incorrect function name `check_specialization` after all four examples had passed; this was a driver `KeyError`, not a checker failure. The corrected call `check_specialization_and_period` passed. The two independent nongentle tests in section 1 also passed, without writing them into shared source or outputs.

## Acceptance recommendation

Accept the principal algebraic and conditional analytic results as supported by the presented proofs and focused checks. Both precise clarifications above have been applied and independently reread. Keep the universal path/cycle proofs, finite computational coverage and literal Lean theorem scopes separate. The next major research work remains a determinant-preserving arithmetic realization and positivity on that same object; no amount of additional local resolution testing alone discharges those obligations.

## Final corrected snapshot

Both requested corrections were independently reread in the final files. Final source sizes/hashes:

- `papers/resolutions-core.tex`: 25549 bytes, 208 lines, SHA-256 `bdacd1e5e74faf09297ec7ff8167f48d3c008e0e668df93e803dfebe4fdf5965`.
- `papers/resolutions-details.tex`: 33614 bytes, 224 lines, SHA-256 `84f6e6ea9fcc1b7bfb3534d32534bf22bba5a25f5c3a8aba918debeee4e07ea9`.

I also read all 24 entries in `papers/resolutions-references.tex` for consistency with the present review. No additional concrete bibliographic error was identified. The corrected Beauville–Laszlo author link and Z. Li initial are consistent with the sources previously consulted. I did not independently reverify every recent arXiv version/date or every geometric theorem locator in this pass.

## Addendum: full split completed-order comparison, final insertion

Independently read the three new paragraphs at final `papers/resolutions-details.tex` lines 159–163, beginning “Here is the coefficientwise proof”. They supply the promised constructive argument and are correct under the explicit closed split hypotheses now present in core line 109. No new substantive error was found.

The matrix orientation is consistent with travel-order multiplication: `E_(j,j+1) E_(j+1,j+2)=E_(j,j+2)`, and the wrap arrow is `x_c E_(n,1)`. The resulting order has arbitrary upper entries and lower entries divisible by `x_c`. “Generated” should be understood as a `k[[x_c]]`-order (equivalently the indicated closed algebra); the immediately following entrywise description makes the intended meaning clear. It is not merely the ordinary k-subalgebra of finite polynomials in these matrices.

The hereditary-order radical description is correct, including length-one cycles: all allowed off-diagonal entries and diagonal entries divisible by `x_c`; the quotient has one residue coordinate per cycle position. A vertex idempotent is the sum of its two position idempotents. A forbidden product switches to a different position over the same original vertex, so the matrix indices do not match. This remains valid when the paired positions lie on the same permitted cycle: they are distinct positions, not an identified matrix index.

The injectivity/surjectivity proof has the required coefficient precision. For distinct positions, the shortest oriented segment, followed by full turns, gives exactly the allowed powers in its matrix entry. For equal positions, positive paths make at least one full turn and therefore have zero constant term. The only constant constraints are precisely the paired diagonal residues. Hence matching tuples reconstruct uniquely as shared vertex constants plus independent positive-path coefficients, and there is no hidden cancellation between those coefficients. Formal length and entrywise-adic convergence agree because there are finitely many cycle lengths.

The sharper inclusion `Jhat^(L+1) ⊂ t Lambda'` is valid. For a permitted path of length at least `L+1`, remove one full turn on its cycle. The suffix is nonempty since that cycle length is at most L. Multiplication of this suffix by the central cycle sum t restores exactly that removed turn: the other incidence contribution at its original initial vertex is killed by the forbidden first join. The nonempty-suffix condition is essential; removing a full turn and leaving an empty path would generally produce both incidence contributions rather than only the desired branch. The manuscript deliberately uses L+1, so it avoids this issue. The same factorization applies coefficientwise to arbitrary elements of the closed ideal. Together with `t Lambda' ⊂ Jhat`, raising ideal inclusions gives `Jhat^((L+1)r) ⊂ t^r Lambda' ⊂ Jhat^r`, proving cofinality explicitly.

Finally, the residue-equality subalgebra contains `t product_c H_c`; its quotient inside the product is finite-dimensional over k. It is therefore finite over the common DVR and has the same generic fiber as the product. It is torsion-free, hence free, with rank `sum_c n_c^2`. Equality of cycle lengths is unnecessary. This is a split equal-characteristic construction; it does not imply mixed-characteristic or general Dedekind-base descent, as the text expressly says.

Final insertion snapshot: 33614 bytes, 224 lines, SHA-256 `84f6e6ea9fcc1b7bfb3534d32534bf22bba5a25f5c3a8aba918debeee4e07ea9`. Only these inserted paragraphs were new relative to the prior complete review; downstream line references in the earlier report shift by six lines after the insertion.
