# Diagonal-fiber gluing and the positive graph model

Independent mathematical review, 2026-11-03. This reviews the proposed construction supplied in the task and its subsequent graph/IBN additions. Shared project files were read only. The arguments below use the already fixed closed dessin conventions: darts H, involution alpha, permitted successor tau=sigma^-1, edge set H/alpha, and travel-order multiplication. C* algebras and the polynomial embedding are over C. No arithmetic comparison or GRH conclusion is asserted.

## Verdict

The proposed diagonal-fiber algebra, its split extension and K groups are correct. The specified polynomial embedding is faithful and generates the entire diagonal-fiber algebra as a C* algebra. The off-diagonal generation step admits an explicit uniform approximation, supplied below. The construction cannot extend to the full formal order, even as a unital algebra homomorphism; rescaling the generators does not remove this obstruction.

The additional positive graph identification of the existing constrained Fock algebra is also correct. It is a graph algebra for the enlarged state-and-sink graph G_alpha, not the original gentle quiver. Its graph K-theory reproduces the previously derived unsigned-incidence groups. This Fock algebra and the diagonal-fiber algebra are distinct; their K0 groups already separate them in every connected closed case.

## 1. The actual C* pullback

Let c range over the tau cycles, of lengths ell_c, and let E be the number of alpha edges. Define

    D_H = { (f_c) in product_c C(T,M_ell_c(C)) :
             f_c(1)=diag(lambda_[h])_(h in c)
             for one lambda in C^E }.

The boundary condition is closed under sums, products and adjoints, so D_H is a closed unital C* subalgebra. Evaluation at 1 followed by reading the paired diagonal values is a surjective * homomorphism q:D_H→C^E. A * homomorphic section is the constant diagonal function

    s(lambda)_c(z)=diag(lambda_[h])_(h in c).

Thus the following sequence is genuinely split in C* algebras:

    0 → I → D_H → C^E → 0,
    I = direct sum_c C_0(T minus {1},M_ell_c(C)).

Equivalently, first use the diagonal-fiber algebras D_ell={f:f(1) is diagonal}, whose diagonal evaluation maps are multiplicative, then pull back their finite-dimensional diagonal residues along the paired-state inclusion C^E→C^H. This distinction from extracting diagonals of arbitrary matrices is essential.

Since T minus {1} is an open interval, stability and suspension give K0(I)=0 and K1(I)=Z^C, where C is the number of tau cycles. The split six-term sequence therefore gives

    K0(D_H)=Z^E,       K1(D_H)=Z^C.

The K0 basis is represented by the constant paired projections p_e=s(standard coordinate e). A primitive K1 generator for branch c is the unitary equal to I+(z−1)E_hh on that branch and the identity on every other branch, for one h in c. It belongs to D_H because its value at 1 is the global identity. The branch scalar unitary z I_ell represents ell times this primitive generator; that multiplicity should not be forgotten if later normalizations use a central loop.

These K groups use standard C* K-theory stability, suspension and split exactness. No claim of a new proof of Bott periodicity is made. The six-term exact sequence is standard background, for example [Rordam–Larsen–Laustsen, Chapter 12](https://www.cambridge.org/core/books/abs/an-introduction-to-ktheory-for-calgebras/sixterm-exact-sequence/50CD0F5F9B23447FC9B4CFF2C2716AB9).

## 2. Why raw diagonal extraction is not an algebra map

For ell>1, any * homomorphism from M_ell(C(T)) to a commutative C* algebra is zero, whether or not unitality is assumed. Indeed, with u_ij the images of the constant matrix units, commutativity gives

    u_ii=u_ij u_ji=u_ji u_ij=u_jj.

The different diagonal matrix units are orthogonal, so each common projection is zero. Their sum is the image of the identity, which is zero, forcing the whole homomorphism to vanish.

Direct diagonal extraction at 1 fails multiplicativity already on E_12,E_21: each has zero diagonal, but their product has nonzero diagonal E_11. Restricting the domain to D_ell repairs precisely this defect because all boundary values are diagonal before multiplication.

The ell>1 hypothesis must remain explicit. A length-one factor is C(T) and has nonzero characters. A product containing such factors can have commutative quotients through those factors; the preceding obstruction is not a blanket assertion that every product normalization has no commutative quotient.

## 3. The polynomial representation

Use the final requested choice

    g(z)=|1−z|^2/4=(2−z−conjugate(z))/4.

It is continuous, lies in [0,1], vanishes exactly at 1, and is positive elsewhere. Pick one cut arrow in each cycle. Send the vertex idempotent e_[h] to the sum of the two corresponding state-diagonal projections. Send a_h to g(z)E_(h,tau h) on its branch, multiplied by z if it is the chosen cut arrow, and zero on all other branches.

These assignments satisfy the idempotent/source/target identities. For a forbidden pair a_h a_(alpha tau h), the middle matrix indices differ because alpha has no fixed points; if the arrows lie in different branches their product is zero componentwise. Thus all forbidden products vanish. The images of arrows vanish at 1, while the vertex images have exactly the paired diagonal residue, so the assignments land in D_H and define a unital algebra homomorphism rho:A_C→D_H.

Travel-order paths correspond to matrix multiplication E_hj E_jk=E_hk. This is the algebra convention; one should not simultaneously reinterpret those same matrices as forward column-vector arrow maps without reversing the representation convention.

The full permitted cycle based at h has image

    b_h = w_c(z) E_hh,        w_c(z)=g(z)^ell_c z.

Every full turn meets the cut exactly once. All arrow images have norm at most one with the chosen g.

## 4. Diagonal ideal generation by nonunital functional calculus

The map w_c:T→C is injective. It is zero only at 1. At a nonzero value, w_c(z)/|w_c(z)|=z, so equality of values forces equality of points. Compactness makes it a homeomorphism onto its image.

The normal element b_h is supported on only one state/branch. Its spectrum is w_c(T), containing 0. For any f in C(T) with f(1)=0, define F on w_c(T) by F(w_c(z))=f(z). It is continuous and satisfies F(0)=0. Functional calculus therefore gives

    F(b_h)=f(z)E_hh

on branch c and zero on the other states/branches. This uses the **nonunital** generated algebra, or equivalently functions with F(0)=0 in the ambient unital functional calculus. It does not incorrectly assert that E_hh itself belongs to D_H. In general E_hh violates the paired boundary condition.

Thus the generated algebra already contains every diagonal corner C_0(T minus {1})E_hh. Continuous functional calculus is the standard normal-element theorem; an accessible primary exposition is Shapiro's [MAT520 notes, Theorems 8.39–8.40, p.89 of the PDF](https://web.math.princeton.edu/~shapiro/PDFs/teaching/MAT520_fall_2025/MAT520_Lecture_Notes.pdf). Only that background, not the proposed gluing construction, is being imported from the notes.

## 5. Complete off-diagonal generation with an explicit approximation

Take states h,j in the same cycle, h≠j. The directed path of length r in {1,...,ell−1} from h to j has image

    v_hj(z)=g(z)^r z^kappa E_hj,

where kappa is 0 or 1 according to whether the path crosses the cut. This scalar is nonzero at every z≠1.

For an arbitrary continuous f with f(1)=0 and epsilon>0, the diagonal function

    d_epsilon(z)=f(z) z^(−kappa)/(g(z)^r+epsilon) E_hh

is continuous, vanishes at 1 and therefore belongs to the generated algebra by §4. Multiplication gives

    d_epsilon v_hj = f(z) g(z)^r/(g(z)^r+epsilon) E_hj.

This converges uniformly to f(z)E_hj. To prove uniformity, first choose a neighborhood U of 1 on which |f| is arbitrarily small. On the compact complement, g^r has a positive minimum and the factor epsilon/(g^r+epsilon) tends uniformly to zero. On U that factor is at most one. This proves the required estimate without treating an unbounded inverse of g as an algebra element.

All matrix corners of each ideal component are consequently contained in C*(rho(A)). Their finite direct sum is I. The constant paired projections supply s(C^E). Every element of D_H decomposes as an element of I plus its constant paired boundary value. Hence

    C*(rho(A)) = D_H.

For ell=1, §4 already proves the entire ideal assertion and no off-diagonal argument is needed. The phase z on one cut arrow is important: omitting it makes g^ell real and can identify z with conjugate(z), so it does not supply the same functional-calculus separation.

## 6. Faithfulness of rho on the polynomial path algebra

Suppose a finite normal-form path sum maps to zero. Evaluation at 1 first forces every length-zero vertex coefficient to vanish. Fix a branch and an entry E_hj. For h≠j, all permitted words contributing to that entry have lengths r+n ell with the same shortest prefix. Their entry is

    g(z)^r z^kappa P(w_c(z))

for a finite polynomial P whose coefficients are exactly the corresponding path coefficients. Off 1 the prefactor is nonzero, and w_c(T minus {1}) is infinite. Thus P is identically zero, so all these coefficients vanish. For a diagonal entry, the positive paths are the positive full powers and give a polynomial in w_c with zero constant term; the identical argument applies. This covers every state/entry and proves injectivity.

No infinite-series rearrangement is used. The conclusion is an embedding of the complex polynomial algebra with a specified C* realization. It does not identify D_H with an abstract universal C* envelope for unconstrained generators, or with an arrow-adic completion.

## 7. Strong obstruction to extending to all formal series

For any positive cycle c_h, the element 1−lambda c_h is a unit of the formal completion Lambda for every scalar lambda: its inverse is the formal geometric series. Choose z0≠1 and lambda=1/w_c(z0). The matrix value

    rho(1−lambda c_h)(z0)=I−E_hh

is singular. Thus the polynomial embedding cannot extend to a unital algebra homomorphism Lambda→D_H at all. This is stronger than a failure of norm convergence or continuity.

For the final normalized g an especially simple witness is z0=−1: g(−1)=1 and w_c(−1)=−1. Therefore 1+c_h is a formal unit but its matrix image is singular at −1. Rescaling g to have norm at most one does not fix the obstruction.

Conversely, norm greater than one by itself does **not** show that I−rho(c_h) is noninvertible. In fact w_c(T) does not contain the positive scalar 1, because a nonzero positive value would require z=1, where w_c is zero. Thus that particular I−rho(c_h) is invertible even for the earlier unscaled g=|1−z|. The formal-unit witness must choose lambda appropriately, or use the explicit normalized 1+c_h example above.

## 8. Positive graph identification of the existing Fock algebra

Let Q_h=L_h L_h* be the state projections and v_e the vacuum projections in the existing constrained Fock model. Define a finite graph G_alpha with state vertices h in H and sink vertices e in H/alpha. Its edges are

    s_h : h→tau h,          t_h : h→[tau h].

Represent them by

    S_h=L_h Q_(tau h),       T_h=L_h v_[tau h].

The initial projections are respectively Q_(tau h) and v_[tau h]. Their ranges are orthogonal and sum to Q_h, since L_h*L_h=Q_(tau h)+v_[tau h]. All state/vacuum vertex projections are mutually orthogonal and nonzero. Edges with different sources have orthogonal ranges; the two same-source edges have orthogonal initial pieces, so the full graph CK relations hold.

The length gauge multiplies S_h and T_h by the circle parameter and fixes all vertices. They generate the old Fock algebra because L_h=S_h+T_h and P_e=v_e+sum_(source h=e)Q_h; conversely every displayed generator is in that old algebra. Gauge-invariant uniqueness therefore gives

    C*(G_alpha) isomorphic to T_A.

The relevant primary theorem explicitly allows row-finite graphs with sinks and requires nonzero vertex projections plus the equivariant gauge action: [Bates–Pask–Raeburn–Szymanski, Theorem 2.1, printed p.311/physical p.5](https://nyjm.albany.edu/j/2000/6-14p.pdf). These hypotheses are verified here. This identification does not revive the invalid graph construction on the original gentle quiver Q. Its graph edges are S_h,T_h, while each original L_h is their sum and has a different initial projection.

Removing the sink ideal leaves the permitted-state cycles. The sink ideal is the same terminal-sector compact ideal already established by matrix units; this gives the previous Fock extension within a standard graph-algebra framework.

## 9. Direct graph K-map and incidence elimination

The graph K-map, with one column for each regular state h and no columns for sinks, is

    d: Z^H → Z^H direct sum Z^E,
    d(e_h)=e_h−e_(tau h)−e_[tau h].

The overall negative convention gives the same kernel/cokernel. The standard graph formula with sinks gives K1=ker d and K0=coker d; see [Drinen–Tomforde, Theorem 3.1, p.8](https://arxiv.org/pdf/math/0103036). Only this theorem/its stated sink matrix convention, not every proof in that paper, was checked for this review.

Write D(e_h)=e_h−e_(tau h) and R(e_h)=e_[tau h]. The kernel of D consists of constant coefficients on each cycle, and its cokernel is freely generated by the cycles. On ker D, R is the unsigned incidence map B:Z^C→Z^E. Thus ker d is ker B. Projection onto coker D gives the exact sequence

    0 → coker B → coker d → Z^C → 0.

Indeed an element whose state part is a D-image can have that state part eliminated by subtracting d(x); the remaining sink vector is determined modulo R(ker D). The free final group splits abstractly. Hence

    K0(T_A) isomorphic to Z^C direct sum coker B,
    K1(T_A) isomorphic to ker B.

This independently reproduces the previous incidence-index calculation. It introduces no spurious sink relations or extra renewed quotient generators.

## 10. Scope, IBN and information retained

D_H and T_A are different constructions. Their ideals are respectively a matrix-valued suspended circle-puncture ideal and terminal-sector compact operators. Their K0 groups separate them for every connected closed dessin: D_H has Z^E; the Fock algebra has Z^(E+1) in the bipartite case, or Z^E plus Z/2 otherwise. They must not be silently identified with each other or with the formal completed order.

The paired boundary data retain alpha incidence, but the **unmarked** D_H is not automatically a reconstruction of the ribbon embedding or genus. Permuting the states inside each matrix factor conjugates its boundary diagonal labels. The two theta dessins have isomorphic unmarked D_H, since their branch lengths and incidence graph agree, while their cyclic embeddings differ. Marked arrows/rotation data contain additional information. No universal reconstruction or arithmetic claim follows from the algebra alone.

The requested IBN statements are correct. A unital ring with a nonzero finite-dimensional k-algebra quotient has invariant basis number: an isomorphism of finite free modules descends to that quotient, where k-dimensions force equal ranks. Both A and Lambda have a vertex-simple quotient k. The permitted-state Leavitt algebra is a finite direct sum of matrix Laurent algebras and has a unital quotient M_ell(k), by choosing one cycle factor and evaluating its Laurent coordinate at 1. The Leavitt algebra of G_alpha first quotients out the sinks/exits, giving that permitted-state algebra, then has the same finite matrix quotient. All have IBN. D_H also has its nonzero finite quotient C^E.

This is not a statement that every Leavitt path algebra has IBN, or that IBN implies stable/direct finiteness. In particular the state-and-sink graph has cycle exits and the Fock model has proper isometries, consistently with IBN. The zero algebra obtained by incorrectly imposing gentle relations on the original CK1 graph is not a witness for any of these positive IBN assertions.

## 11. Checks and coverage

No shared source, checker, Lean, planning or output file was edited for this task. In-memory exact rational checks used the existing eight explicit dessins at z=−1, where the final g equals 1. They verified 44 forbidden products and 11 exact full-cycle images −E_hh, together with singularity of I+rho(c_h). These finite checks supplement the general proofs above; they do not certify C* generation or K-theory by sampling.

The functional-calculus and graph uniqueness/K-map primary statements cited above were checked at their stated pages. The split-exact K computation uses standard suspension/stability dependencies. No full-text audit of all cited books or graph-algebra papers, no new formal proof, and no RH/GRH result is claimed.

## 12. Literal manuscript and ten-statement formal review

Follow-up review, 2026-11-03. Read all 37 lines of papers/dessin-gluing-core.tex, all 80 lines of papers/dessin-gluing-details.tex, and all 129 lines of lean-analytic/DessinPullbackComponents.lean as supplied. No shared edits were made. The node AF application's primary hypotheses were checked directly against the immutable cached arXiv:1907.10260v3 text, Definitions 2.1–2.2 and 3.1, Lemma 3.3, Theorem 3.4 and its proof on pp.5–8, plus the setup preceding Theorem 4.3. The source is Chirvasitu–Hajac–Tobolski, *Non-surjective pullbacks of graph C*-algebras from non-injective pushouts of graphs*, v3 dated 31 December 2019.

### One concrete wording correction

Core line37 calls D_H a “chosen norm completion of the polynomial algebra.” The actual theorem at line32 correctly says that the polynomial image **generates with its adjoints**. Those statements are not interchangeable. The ordinary norm closure of rho(A) need not contain those adjoints and need not equal D_H. Replace the line37 phrase with “the C* algebra generated by this faithful polynomial representation and its adjoints,” or “the norm completion of its generated *-algebra.”

The node is an explicit counterexample to the stronger reading. On either length-one branch, with the final g,

    w(z)=g(z)z=(2z-z^2-1)/4.

Every polynomial path image in that branch is a polynomial in w, and hence has only nonnegative Fourier modes in z. Uniform limits preserve the vanishing of each negative Fourier coefficient. But conjugate(w) has nonzero coefficients at z^-1 and z^-2. It therefore does not belong to the ordinary uniform closure of the polynomial image, while it certainly belongs to C*(rho(A))=D_H. This is a terminology correction to the prose, not a failure of the proved generation/faithfulness theorem.

### Actual nodal AF application: pass

Core lines12–17/details20–34 apply the source theorem to an actual, suitable pair of graphs. E2 is the two state loops, each with an exit to the common vacuum sink b. E1 has the same three objects and countably many parallel edges from each source to b, with no other edges. Its map sends edge n to s^n t. This is not an ordinary edge-to-edge graph map; it is exactly the path functor allowed by the cited theorem.

The removed set {b} is hereditary. It is saturated in E2 because each remaining regular vertex retains its loop, and saturated in E1 because its sources are infinite emitters rather than regular vertices. The retained subgraph contains all edges ending at retained objects. For the source's additional infinite-emitter condition, E1 emits infinitely many arrows into {b} but **zero**, not a positive finite number, outside; this is allowed by Definition3.1(A3). E2 has only finite emitters, so that condition is automatic.

Distinct s^n t images are prefix incomparable: at the first unequal step one path exits and the other still loops. Identity-object prefixes agree with identity-object prefixes in the domain. The positive pointed paths of E2 are precisely these loop-powers followed by an exit; vertices are retained separately in the object-preserving functor. E1 is acyclic, and b has no short loop. Thus all hypotheses of Theorem3.4 are met, including the ones that allow countably many edges rather than requiring row finiteness.

The resulting restricted-symbol algebra is exactly

    {T in T_A : pi(T) is in the constant C^2 inside C(T)^2}.

This can also be seen directly in the old Fock representation. The s^n t operators map the common vacuum to all finite paths in the two arms. Together with their adjoints they generate the whole terminal compact ideal, while the two source projections lift the two constant quotient coordinates. Thus the constants-symbol preimage is generated by precisely the proposed E1 family.

The graph is acyclic, so its C* algebra is AF. Its two sources are infinite emitters and its third vertex is a sink, hence it has no regular vertices. The graph K-map therefore has zero columns and three rows: K0=Z^3 and K1=0. No finite-emitter CK2 relation has been incorrectly imposed at the infinite emitters. It is a subalgebra of T_A, not T_A itself and not the formal order. No novelty theorem is claimed beyond this explicit application of the existing source.

The warning against copying it to longer permitted cycles is also sound. A closed cycle of length greater than one has final edge which is not a short loop, so it is pointed in the source's definition. An object-preserving functor from an acyclic E1 cannot cover that positive closed path. The extra injection/annihilation/path-coverage assumptions for the sink-extension theorem remain expressly stated.

### Remaining operator statements: pass

The positive graph model, graph integer map, diagonal-fiber split extension, K groups, faithful polynomial embedding, nonunital functional calculus, explicit epsilon approximation and singular formal-unit witness agree with §§1–10 of this report. Details lines48–58 keep the shortest-path cut factor and the possible zero coefficient for diagonal positive paths, so there is no hidden independence assumption. The branch unitary's factor-ell K1 class and the unmarked theta-isomorphism caveat are retained. The IBN proof uses a unital finite-dimensional representation, not faithfulness or a mistaken generalization about all Leavitt algebras. The ordinary complex Leavitt algebra of G_alpha is correctly associated to the split graph generators, not the unsplit original arrows.

Details line37 implicitly needs two distinct matrix indices, equivalently ell>1; the core line20 says this explicitly. Repeating “for ell>1” in that details paragraph would improve local clarity, but the surrounding claim is already properly scoped by the core. Length-one C(T) blocks do have characters.

The additional string-finiteness/smooth-quotient discussion at details69–80 was fully read. The formal-branch endomorphism argument, the finite-generation obstruction using invertibility of 1-u, and the alternating Ext counterexample are internally consistent. I did not independently audit the entire Crawley–Boevey or Lekili–Polishchuk primary proofs in this follow-up; those source applications retain their separate specialist-review dependency.

### Ten actual Lean types: independently compiled

Ran the existing pinned environment's lake env lean -DwarningAsError=true on DessinPullbackComponents.lean. It completed with exit0. All ten printed theorem types and axiom reports were inspected; there are no sorry/admit declarations or newly introduced axioms. Dependencies are standard Lean foundations.

The actual scope is five 2-by-2 matrix-unit identities; a concrete diagonal-extraction nonmultiplicativity witness; impossibility of a **unital** homomorphism from the two-state matrix ring to a nontrivial commutative ring; multiplication of actual diagonal matrices; surjectivity of a generic equal-image subring projection supplied with a compatible section; and one implication identifying its zero fiber. In particular pullback_zero_fiber asserts that second component zero implies first-component image zero. It does not by itself package a kernel isomorphism or an entire exact C* sequence. The manuscript must retain the distinction between these generic algebraic components and the prose proofs of actual continuous-function C* gluing, functional calculus, AF identification and K-theory.

The old §§1–11 remain applicable. The sole requested manuscript correction from this literal pass is the ordinary norm-completion phrase above; no new false mathematical theorem was found in the operator pullback or nodal AF application.
