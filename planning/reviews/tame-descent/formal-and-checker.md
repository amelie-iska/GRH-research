# Balanced theta column: tame descent and formal review

Independent read-only mathematical review, 2026-11-03. Initial coverage is the supplied tame-descent construction, the independent /tmp derivation, and all162 lines of lean-analytic/ThetaTameDescent.lean. The requested paper sections were not yet present when this initial portion was saved; their literal review will be appended. Shared project sources, scripts, environments and outputs were not edited.

## 1. Mathematical verdict and coefficient conventions

The candidate constructions and their stated limitations are consistent. Work over k=Q(omega), omega³=1, omega≠1, with R=k[[u]], S=k[[v]], u=v³. The balanced plus column W=S³ has arrows vE_(i,i−1) and zero minus arrows. The full plus turns give v³E_ii=uE_ii, so this is a module for the completed order. Matrix multiplication follows travel order for a **left** module, rather than forward right-module arrow maps.

Let C epsilon_i=epsilon_(i+1), D=diag(1,omega²,omega), and g(v)=omega v with k fixed. Then Theta=Dg has order3, fixes the R scalars and commutes with each original arrow action. For a plus arrow the coefficient factor omega from g(v) cancels the consecutive D-weight ratio omega². Thus Theta is genuinely compatible with this Lambda_R action; it is not merely an action on an unrelated vector space. On the carrier rotation,

    Theta C=omega² C Theta.

The nontrivial scalar commutator is exactly the expected sign for the chosen shift direction. It is not a commuting product of the two order-three actions on the vector bundle. It does cancel after passage to conjugation on its matrix algebra.

## 2. Fixed lattice and the failed comparison

At vertex i, a coefficient v^n is invariant exactly when n=i modulo3. Hence

    U=W^Theta=R epsilon_0 + R v epsilon_1 + R v² epsilon_2.

The natural S-linear comparison S tensor_R U→W is diagonal(1,v,v²). It is injective and has determinant v³=u, with cokernel S/(v) plus S/(v²), placed in the last two coordinates. The closed-fiber matrix has rank1. Its failure to be an isomorphism is real, not an ambiguity in choice of basis.

R→S is nevertheless finite **free** of rank3, with basis1,v,v², and faithfully flat. The comparison fails because a semilinear group action across a ramified quotient is not automatically the ordinary fpqc descent datum. The factors of w³−v³ in S tensor_R S are not comaximal at v=0. Off that point they do give the usual cubic Galois cover. At the branchpoint, Theta acts on W/vW by D with nontrivial stabilizer weights, whereas a bundle pulled back from the coarse R base has trivial canonical stabilizer action on that fiber. There is no counterexample to faithfully flat descent.

Since3 is invertible and Theta is R-linear, averaging makes invariants exact on equivariant short exact sequences. Exactness does not make invariants tensor-compatible and does not turn the displayed comparison into an isomorphism.

In U's fixed basis, the arrow scalars are(u,1,1); the old hereditary cut column reappears. C maps the invariant lattice into another Theta-weight space. The compensated vC does preserve U, with matrix

    A=[[0,0,u],[1,0,0],[0,1,0]],
    A³=uI, det A=u.

This is an R-linear carrier map, not an integral automorphism. Over K=Frac(R), it is invertible and its projective class has order3, but no scalar in K can normalize its cube to1: the required equation h³u=1 violates the integer u-valuation. This is an actual lattice obstruction, not an assertion that all projective/algebra-level rotation disappears.

## 3. The descended matrix algebra and rotation

For the full carrier matrix algebra End_S(W), conjugation by Theta sends H to Dg(H)D^-1. Its invariant entries satisfy

    H_ij in v^([i−j]_3) R.

Conjugating to U's basis multiplies entry(i,j) by v^(j−i). The exponent becomes0 when i≥j and3 when i<j. Thus the invariant algebra is exactly the hereditary order B_+ with entries R on/below the diagonal and uR above it. This is a direct computation of the actual order, not a dimension analogy.

Ad_C commutes with this descent because the clock/shift commutator is scalar. In the invariant basis it is Ad_A, interpreted in M3(K). Although A is not an integral unit, it normalizes B_+ and A³=uI makes this a genuine order-three R-algebra automorphism. It is not an element of PGL3(R) acting on the same free lattice by an invertible integral matrix.

Crucially this is End_S(W), not End_Lambda(W). The rotation C and the compensated vC are generally rotation intertwiners/carrier operators, not Lambda-linear endomorphisms. Their polynomials must not be silently promoted to arithmetic endomorphisms in the ordinary Lambda-linear category.

## 4. Tensor weights and the top determinant line

On a global homogeneous tensor/Schur carrier of degree m, the induced commutator is omega^(2m). For these particular induced invertible operators on a nonzero summand, commutation requires and is equivalent to3 dividing m. It is a central-character selection rule, not a theorem about every modified lift. For mixed variance one must use net central degree.

Commutation alone does not imply that the original S bundle descends unchanged. In Sym³W the ten monomial fiber weights have multiplicities(4,3,3). Its comparison from invariants still has nonunit determinant v^9=u³. The top exterior line is a special positive exception: det D=det C=1, so its Theta action is just g and its invariant line is R vol; that line really does base change back to det_S W.

But the natural map det_R(U)→(det_S W)^Theta sends the fixed basis wedge to v³vol=u vol. Its image is uR vol and its cokernel R/(u). Both abstract lines are free rank1; it is their specified natural comparison that is noninvertible. Dropping that nonunit would lose the ramification divisor.

When comparing operators, use the **same** operator on each side of this map. det(C)=1 refers to C on the top S-line, whereas det(A)=u refers to vC on U. For vC itself both determinant actions are u, and the natural comparison intertwines them. There is no false naturality contradiction between different operators.

These global Schur operations are not automatically tensor functors on Lambda modules; no Hopf structure was specified. The actual vertexwise Sym^m of the one-dimensional vertex spaces changes arrow coefficients to v^m and the central full-cycle scalar to u^m. Vertexwise exterior³ is zero. Those operations must not be confused with the global top line of S³.

## 5. Jacobi carrier operator and its degeneration

For coefficients a,b fixed by g, the balanced carrier expression aI+bC fails to commute with Theta when b≠0. Its commutator is b(omega²−1)C Theta. This failure is independent of the earlier arithmetic trace/norm theorem.

Replacing C by vC makes the expression descend as an R-linear carrier map, but gives

    det(I−T(aI+bA))=(1−aT)³−u b³T³.

At u=0 it is(1−aT)³. This is not the original constant quadratic Jacobi factor. The compensation therefore does not preserve that claimed arithmetic characteristic polynomial. Moreover neither expression is automatically Lambda-linear, as noted in §3. This is a concrete failed elementary proposal, not a no-go for every arithmetic semilinear correspondence or determinant category.

## 6. General strict full-C6 lattice rank

The stronger candidate rank theorem is valid under its stated central-fixed, R-linear, invertible symmetry hypotheses. Let M be an R-free Lambda lattice with a strict lift of both rotation sigma and branch-swap alpha. In the generic fiber use the central branch idempotents and form the **intersections** M^±=M intersect M_K^±. Do not assume an integral direct-sum decomposition of M into branches. These intersections are finite free R lattices, preserved by sigma. Alpha exchanges their generic branch multiplicities, so both are r copies of the corresponding three-dimensional simple. At each vertex the intersection has rank r.

The three arrow matrices on a branch intersection multiply to uI_r. Their nonnegative determinant valuations therefore sum to r. The invertible sigma intertwiners between the three vertex lattices have unit determinants and conjugate these arrows cyclically, forcing their three valuations equal. Thus r=3m. Each vertex of M has total rank2r=6m, and M has total R rank18m. If M is nonzero then m≥1. No projectivity assumption is needed for this rank argument, but the branch-intersection and invertibility arguments are load bearing.

Normalization B is the sharp m=1 example: it carries the strict order automorphisms on both branches and has vertex rank6. Keeping all three tame character lattices similarly restores rotation while tripling the basic column rank; retaining both branch families restores the larger multiplicity. For a projective P, P→P tensor_Lambda B becomes an isomorphism over K. Any Lambda-linear endomorphism therefore has the same ordinary characteristic determinant before/after this full normalization, by generic conjugacy and R→K injectivity. This does not assert that the integral determinant-line comparison is an isomorphism; its conductor cokernel may be nonzero.

The rank theorem does not apply to noninvertible actions, coefficient-semilinear actions changing R, other ranks/bases after ramification, or arbitrary infinite-dimensional carriers. It does not supply a Frobenius action or prove a global spectral statement.

## 7. Independent formal compilation and literal scope

Read all162 lines of ThetaTameDescent.lean and ran a fresh independent lake env lean -DwarningAsError=true in the pinned Lean4.24.0/mathlib4.24.0 environment. It completed with exit0 and twelve standard foundational axiom reports, with no admissions/new axioms. There is also an unprinted auxiliary lemma cubic_fourth, so twelve **printed components** should be distinguished from the total declaration count including that helper. The compile emitted two informational ring-tactic fallback suggestions; these were not errors or warnings and did not affect the accepted proof terms.

The twelve printed types cover: clock/shift commutation; the exact infinite-power-series coefficient action; vanishing of forbidden invariant coefficients; the genuine threefold tame operator identity; determinant and closed fiber of the comparison matrix; cube and characteristic polynomial of the weighted rotation; the rotation-polynomial commutator and primitive-root noncommutation; clock/rotation determinants; and the exact same-operator matrix identity comparison*A=(vC)*comparison.

These are actual formal-series and matrix components, not assumed arithmetic kernels. However they do not define the separate R/S base embedding as an entire finite-free extension, package the invariant lattice equivalence, prove the full C6 lattice-rank theorem, construct the invariant hereditary algebra/Ad action, or establish categorical/arithmetical descent. The primitive-root noncommutation theorem has explicit z³=1,z≠1,b≠0 hypotheses. The weighted rotation results hold over any commutative ring. The invariant-coefficient theorem alone is a support restriction; the exact basis of all fixed vectors is supplied by the coefficientwise prose proof.

No shared files were modified or existing checker writers invoked. The literal new paper/checker pass follows below.

## 8. Literal paper review and the stronger arbitrary-kernel theorem

Read the complete papers/theta-tame-core.tex lines1–43 and papers/theta-tame-details.tex lines1–108. The explicit comparisons, matrix conventions, hereditary-order shape, determinant-line map, same-vC naturality, failure of the old H1 plane, and distinction between carrier and Lambda-linear endomorphisms all agree with §§1–7. The mathematical interpretation via a local root stack is not needed to prove any displayed matrix/module assertion. This follow-up did not independently reread the entire Alper/root-stack primary sources; their general theorems are interpretive background here, rather than hidden premises of the calculated failure of comparison.

The new rank theorem is stated with invertible R-linear intertwiners for sigma and alpha; it does not even need the stronger strict group relations. The branch-intersection proof is sound and avoids assuming an integral splitting. The generic branch idempotents are u^-1 times the respective sums of based full turns. Their actions isolate the two semisimple branch summands. Intersections with the original lattice are finite free, span those summands and are stable under the required operators. This justifies all determinant valuations in the rank argument.

The new **arbitrary coefficient-kernel determinant formula** also checks out. Let W0 be any finite R-free left kernel satisfying these hypotheses, not assumed projective or flat as a Lambda module. Each e_iW0 has rank6m. For a finite right projective P=sum_i(e_iLambda)^n_i,

    P tensor_Lambda W0 = sum_i(e_iW0)^n_i

is finite R-free. Reduce modulo u and filter by the left arrow radical J. Since J^4 is contained in uLambda, this filtration is finite. A positive-length Hom entry in e_j Lambda e_i sends e_i J^a(W0/uW0) into e_j J^(a+1)(W0/uW0). Constant entries at i are exactly the top multiplicity matrix A_i tensored with the identity on each internal vertex graded piece. The total dimension of those pieces is rank(e_iW0)=6m. Multiplying the graded determinants therefore gives

    det(1-T Phi_W0(f)) modulo u
       = [product_i det(1-TA_i)]^(6m).

This is valid for every Lambda-linear source endomorphism f, whether or not f itself is deck equivariant. No flatness or integral branch splitting has entered the argument. Bounded-projective inputs compute the derived tensor functor and its alternating ratios; denominator constant coefficients1 make specialization legitimate. The degree/pole obstructions then exclude the single arithmetic quadratic and full local curve zeta. If m=0 the output is zero and determinant1, which also cannot give those targets.

The condition that the action is induced as Phi_W0(f) is essential. The theorem does not exclude choosing an unrelated R-linear operator directly on an output vector space, nor semilinear source maps, changed coefficient/determinant categories or infinite analytic carriers. The statement and final paragraph retain these limits. W0=Lambda attains m=1, making the rank bound sharp.

The character-orbit identification is integral, not merely generic: the j-th hereditary column has basis exponents t_ij=1 for i<j and0 otherwise, so its arrow exponent delta_i0+t_(i−1,j)-t_ij is delta_ij. This matches the cut of L_j exactly. Thus the three invariant character lattices sum to B_+; both branch orbits give the full normalization B. The dimensions before/after invariants are correctly distinguished: the three-copy S orbit has rank9 over S and27 over R, while its invariant lattice has R rank9. Restoring both branches gives vertex rank6.

For every finite projective P and Lambda-linear f, P→P tensor B becomes an isomorphism over K and intertwines the extended operator. Equality of the characteristic determinants over K implies equality already over R. This recovers the old ordinary determinant, not only the external tensor example's exponent. It does not assert that the integral lattice or determinant-line comparison is an isomorphism. Also, the invariant carrier matrix order B_+ is not End_Lambda(W) or an effective Azumaya descent of the unchanged full matrix bundle: the positive statement is its actual invariant hereditary order and the descended automorphism of that order.

The coefficient field change is kept explicit. Restricting a rational characteristic polynomial from the k-valued determinant to Q takes its field norm; for a rational factor P_d this is P_d². An unqualified identification with the old rational determinant would be false, and the paper correctly avoids it.

One small local wording correction was requested and is now present at details62: vertexwise Sym^d preserves the zero relations only for d>0; Sym^0 sends zero maps to the identity. The central scalar differs from u for d>1, whereas d=1 leaves it unchanged, as the displayed formula confirms. This resolved qualification does not affect the main rank or determinant proofs.

## 9. Latest formal and finite-checker pass

Read the latest164-line ThetaTameDescent.lean after its clock-proof adjustment and compiled it again independently with warningAsError=true. It passed with exit0 and the same twelve standard reports; two informational ring-normalization suggestions remain, with no failed theorem, admission or new axiom. These twelve printed components plus the unprinted auxiliary lemma are not a formalization of the new arbitrary-kernel rank/filtration theorem. The latter is the prose proof audited in §8.

Read the final189-line scripts/check_theta_tame_descent.py. An earlier leftover orbit assertion incorrectly added an extra degree shift; the author corrected it before the final pass. Imported its pure checks() API with bytecode disabled and without invoking its report writer. The corrected final API passed:

* 99 tame-cube coefficient cases, 99 clock/shift cases and99 weighted-rotation cases;
* 297 character-orbit cases and297 matrix-entry coefficient-weight cases;
* 297 candidate arrow/input cases, of which96 execute the nonzero-input coefficient assertion within the stated degree bound; the other channels are zero/vacuous or at the cutoff;
* symmetric-power carrier weights in degrees0 through9, including Sym³ inertia multiplicities(4,3,3);
* both exact prime-seven noncommutation controls;
* 324 multiplication pairs for the actual18-dimensional normalization special-fiber representation;
* 36 explicit rotation/branch-swap intertwining identities, with the group relations checked;
* vertex ranks(6,6,6), and9 all-coefficient induced determinant cases for three projective multiplicity patterns.

The finite representation is the normalization kernel modulo u, not an assertion that Lambda/uLambda has become a new primary algebra or that its module action is faithful. Its c_i socle actions vanish, consistently with this kernel. The determinant cases are induced source Hom actions, matching the general theorem's scope. The checker corroborates a specified normalization example, not every finite free coefficient kernel. The universal arbitrary-kernel statement rests on the independently inspected valuation and radical-filtration proofs.

No shared files or existing outputs were modified by this reviewer; only this /tmp report was generated. No full220-report suite, PDF build or rendering was independently run. The independent formal rerun was the new tame module, and the exact rerun was this checker's pure API. With the local positive-degree qualification resolved, no blocking mathematical error was found in the literal construction or strengthened coefficient-kernel theorem. The proposed repair still has not recovered an independent arithmetic endomorphism or a global positive determinant for the desired completed function.
