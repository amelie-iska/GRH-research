# Schur modules and cyclic-quiver invariants for the infinite dessin algebra

Independent mathematical review, 2026-11-03. Shared project sources were read only. This report concerns finite-dimensional representations of the specified **infinite-dimensional** locally gentle algebra and, separately, continuous representations/lattices of its completion. It does not replace the algebra by a finite-dimensional gentle algebra. All calculations below are over a field of characteristic zero; analytic positivity statements use complex vector spaces.

## 1. Findings and usable scope

There is a concrete positive bridge: nonempty Young-diagram Schur functors produce actual representations of the monomial dessin algebra, natural Littlewood–Richardson maps intertwine the arrows, and the retained three-cycle stratum has a completely explicit polynomial invariant ring. The associated Schur-character Cauchy kernel is positive semidefinite under a quantitative convergence condition.

Three qualifications are essential. The empty-partition functor does not preserve the zero relations, although its scalar character is a valid constant invariant. These Schur constructions are not exact or additive and do not automatically preserve the order's fixed central power-series action. Finally, continuous finite-dimensional representations of the completed order have nilpotent cycle monodromy, on which all positive-degree ordinary trace/Schur invariants vanish. This makes semi-invariants and flags relevant, but does not furnish an arithmetic positive kernel or prove RH/GRH.

## 2. Primary sources and actual coverage

* Le Bruyn–Procesi, **Semisimple representations of quivers**, Transactions AMS 317 (1990), 585–598, [DOI](https://doi.org/10.1090/S0002-9947-1990-0958897-0). Bibliographic metadata verified. Both attempted direct AMS PDF URLs returned HTTP 403; I have **not** read the original proof in full.
* Craw–Yamagishi, **The Le Bruyn–Procesi theorem following Lusztig**, [arXiv:2312.08527v4](https://arxiv.org/abs/2312.08527v4), 14 November 2025, 13 pages. This is the verified current title/version; the earlier title ending “and Hilbert schemes” is obsolete for v4. Inspected introduction, Theorems 1.1–1.2 on p.2, Lusztig's Theorem 2.2 on p.4, framing/proof discussion on pp.4–7 and Proposition 3.2 on p.8. The bound-quiver statement supplies trace generators and the kernel from relation combinations. Its hypotheses include an algebraically closed characteristic-zero field. No assertion of full proof-by-proof review of all 13 pages is made here. [Primary PDF](https://arxiv.org/pdf/2312.08527v4).
* Etingof et al., **Introduction to Representation Theory**, author-hosted [book PDF](https://math.mit.edu/~etingof/representationtheorybook.pdf). Inspected the Young-symmetrizer, Schur–Weyl and GL-character sections, especially §§5.12–5.13, 5.17–5.18 and 5.22. These are the background references for the conventional Schur modules. This is not a full-book audit. Row/column normalizations must be specified independently; the calculation in §3 below fixes ours directly.
* Price–Stelzer–Yong, **Representations from matrix varieties, and filtered RSK**, [arXiv:2403.09938v2](https://arxiv.org/pdf/2403.09938), 6 October 2025, 38 pages. Inspected pp.1–5, including the Cauchy identity and semistandard-tableau character formula on p.2 and Remark 1.13 on p.5. Their more general matrix-variety multiplicity results require their stated Levi-stability/bicrystallinity hypotheses; I do not apply those results automatically to a gentle relation variety.
* Akin–Buchsbaum–Weyman, **Schur functors and Schur complexes**, Advances in Mathematics 44 (1982), 207–278, [DOI](https://doi.org/10.1016/0001-8708(82)90039-1). Metadata and introductory scope verified; author-hosted PDF retrieval failed, so no claim of a full direct audit. An accessible primary account of precisely relevant constructions is Jiang, **Derived Grassmannians and derived Schur functors**, [arXiv:2212.10488v3](https://arxiv.org/abs/2212.10488v3), 6 July 2023, 99 pages. Inspected §2.4, pp.24–27, particularly Definition 2.17, Theorem 2.22, Example 2.23, and Theorem 2.24; also the introduction/roadmap for derived extensions. The split-injective finite-projective acyclicity assertion is about the genuine Schur complex, with mixed terms, rather than a three-term degreewise application of a Schur functor.
* Derksen–Weyman, **Semi-invariants of quivers and saturation for Littlewood–Richardson coefficients**, JAMS 13 (2000), 467–479, [primary author PDF](https://sites.lsa.umich.edu/hderksen/wp-content/uploads/sites/614/2018/05/A.I.a.6.pdf). Inspected introduction and setup, pp.467–468. The hypothesis “without oriented cycles” is explicit on p.467. It prevents indiscriminate application of their acyclic-quiver results to the whole theta algebra; the concrete Kronecker slice below is acyclic.

The proofs of the particular theta-stratum, lattice and exactness statements below are supplied explicitly, rather than attributed to uninspected literature. No Lean declarations or project files were modified or compiled for this review. The exact computations in §10 were executed in memory, without persistent reports or bytecode.

## 3. Actual Young symmetrizers, tableaux and Schur modules

Let λ be a partition of m, let T be a numbering of its boxes, and let R_T and C_T be its row and column permutation groups. On V tensor m define the **unnormalized** operators

    R = sum_{σ in R_T} σ,
    C = sum_{τ in C_T} sign(τ) τ,
    Y_T = R C.

With the usual place-permutation action, Y_T squared equals h_λ Y_T, where h_λ is the product of hook lengths. Thus e_T=Y_T/h_λ is an idempotent, and its image is one copy of the Schur module S_λ(V). Characteristic zero ensures that h_λ is invertible. Reversing the order R,C gives an equivalent Schur construction, not generally the identical subspace. Separately averaging the row and column sums changes the quasi-idempotence scalar; one cannot use h_λ unchanged after such a normalization.

For a d-dimensional V, S_λ(V)=0 when the number of rows exceeds d. A semistandard tableau has weakly increasing rows and strictly increasing columns, with entries in {1,...,d}. Standard Schur basis vectors are indexed by these tableaux; on diagonal matrices, their monomial weights sum to the Schur polynomial s_λ. The two dimensions often confused here are

    dim Specht_λ = m! / h_λ,
    dim S_λ(C^d) = product_{(i,j) in λ} (d+j-i)/h_ij.

A single normalized Young symmetrizer extracts one Schur copy. A central symmetric-group isotypic projector extracts that copy with its Specht multiplicity; its trace on M tensor m is therefore different by that multiplicity. For λ=(2,1), d=2, the hook product is 3, the Schur dimension is 2, and the Specht dimension is 2. Our explicit calculation used Y=(I+P_12)(I-P_13), verified Y²=3Y and rank(Y)=2, and verified

    tr((M tensor M tensor M) Y/3)=det(M) tr(M).

These are actual linear maps and submodules, not a naming convention for formal symmetric functions.

## 4. Schur functors on representations of the actual infinite algebra

Write A=kQ/I, where I is generated by forbidden length-two paths of the closed dessin. For a representation X, and a **nonempty** partition λ, put

    (S_λ X)_v = S_λ(X_v),
    (S_λ X)_a = S_λ(X_a).

If ba is forbidden, functoriality and positive homogeneity give

    S_λ(X_b) S_λ(X_a) = S_λ(X_b X_a)=S_λ(0)=0.

Thus this is an actual A-module. For a module morphism f, apply S_λ at its vertex maps; naturality proves the arrow squares commute. The construction is a generally nonlinear functor on this representation category. It does not require a Hopf algebra structure on A.

The restriction to nonempty λ is real: S_empty sends every vector space to k and every linear map, including zero, to id_k. Therefore a forbidden two-arrow product becomes id_k, and this does not define an A-module. The empty partition remains legitimate in character formulas as the scalar 1. One must distinguish that invariant from an object in the zero-relation representation category.

Define the **vertexwise tensor operation** explicitly by (X tensor_pt Y)_v=X_v tensor Y_v and arrow map X_a tensor Y_a. The zero relations survive, so it stays inside this category. This is not an invocation of the usual tensor product of modules over an arbitrary algebra. Natural Littlewood–Richardson decomposition gives, for nonempty λ and μ,

    S_λ X tensor_pt S_μ X
       isomorphic to direct sum_ν (S_ν X) repeated c_{λμ}^ν times.

The isomorphism is natural in arbitrary linear maps, hence intertwines every arrow, including singular or zero arrows. Multiplicity-space bases are choices; naturality does not mean a canonically chosen basis for every multiplicity space. The scalar character identity follows by tracing, but is weaker than this representation statement. The absent empty-partition object means one should not silently declare this operation unital on the relation category.

The coefficient c_{λμ}^ν counts skew semistandard tableaux of shape ν/λ, content μ, with the usual lattice/Yamanouchi reading word (right to left within successive rows from top to bottom). Sizes must add, and terms with too many rows for the vertex dimension vanish. This is the actual LR rule, with rank restrictions, rather than an unconstrained formal sum.

## 5. The elliptic theta stratum and its exact invariants

Use H={0,...,5}, σ=(012)(345), α=(03)(14)(25), and vertices v_0={0,3}, v_1={1,4}, v_2={2,5}. The arrows a_h:[h]→[σ^-1 h] are

    a_0,a_3: v_0→v_2,
    a_2,a_5: v_2→v_1,
    a_1,a_4: v_1→v_0.

The two permitted cycles are (a_0,a_2,a_1) and (a_3,a_5,a_4); cross successors are forbidden. Setting a_3=a_5=a_4=0 defines a closed, gauge-stable subvariety Z of Rep_A(d,d,d). Its remaining matrices X_1=X_a0, X_2=X_a2, X_3=X_a1 are arbitrary, so Z=Mat_d^3. No additional relation on X_3 X_2 X_1 results. This is a representation stratum of the infinite A and a quotient to the infinite path algebra of an oriented three-cycle.

Set M=X_3 X_2 X_1 at v_0. Gauge acts on an arrow s→t by X_a↦g_t X_a g_s^-1; consequently M↦g_0 M g_0^-1. On the invariant open set where X_1 and X_2 are invertible, gauge fixes those two matrices to identities and leaves precisely conjugation of M. Every characteristic coefficient of M is nevertheless polynomial on all of Z, so no denominator is needed to extend those invariants.

Here is a complete short argument for the whole invariant ring. Trace generation for this finite quiver says every invariant is a polynomial in traces of oriented cycles. Every oriented cycle is a power of the retained three-cycle, with trace unchanged by moving its starting vertex. Thus generators are tr(M^r). Newton identities in characteristic zero reduce them to c_1(M),...,c_d(M), with c_j the elementary characteristic coefficient. Their algebraic independence follows by restricting to the section (X_1,X_2,X_3)=(I,I,M). Therefore

    k[Z]^(GL_d^3) = k[c_1(M),...,c_d(M)].

The quotient classifies semisimple orbit closures, not all nonclosed orbits or the full Jordan structure. Its Hilbert series, using total arrow degree t, is

    product_{j=1}^d (1-t^(3j))^-1.

In arrow multidegree (m_1,m_2,m_3), invariants vanish unless all three m_i equal m. In that degree a basis is χ_λ(M)=tr(S_λ M), for λ a partition of m with at most d rows. This can be seen by the Cauchy decomposition and Schur's lemma at the three vertices, or by the ordinary Schur basis in the eigenvalue invariant ring.

These statements apply directly to Z. They do not assert that the full theta representation variety has no other generators, components or relations. Its stable relation ideal can remove ambient Cauchy/LR summands. In characteristic zero, reductivity makes invariant restriction to a stable closed subvariety surjective, but the restriction kernel still matters. In this example, the first-cycle characteristic functions are explicit polynomials on the full variety and the section above shows their polynomial subalgebra remains algebraically independent there. That does not describe the full ring.

## 6. Coordinate duals and the vertex LR calculation

The space of arrow matrices is Hom(V_s,V_t)=V_t tensor V_s*. Its polynomial coordinate representation is its dual. For the conventional action (g·f)(X)=f(g^-1·X), it is therefore

    Hom(V_s,V_t)* = V_s tensor V_t*,
    Sym^m(V_s tensor V_t*)
      = direct sum_{λ partition m} S_λ(V_s) tensor S_λ(V_t)*.

For scalar diagonal gauges, a coordinate entry has source weight divided by target weight. This is the contragredient sign that is easily reversed when passing between matrix entries as numerical functions on a transformed point and the induced representation on the coordinate ring.

At a vertex, outgoing arrows contribute polynomial V factors and incoming arrows contribute dual V factors. The invariant space is the corresponding GL(V)-Hom space. Decompose each side using LR, and match identical irreducibles. Thus the genuine local contraction mechanism is LR multiplicity on the outgoing side times LR multiplicity on the incoming side, summed over the common intermediate highest weight. At one-in/one-out vertices this forces equality of the adjacent edge partitions. Applying this at all three cycle vertices yields the single partition λ described in §5.

For a relation quotient one first has this ambient decomposition, then must compute the quotient by the actual stable relation ideal in the relevant multidegree. The surviving multiplicities are not automatically the ambient ones. Recent matrix-variety filtered-RSK results likewise cannot be transplanted without their geometric hypotheses.

## 7. Explicit two-dimensional actual intertwiners

For a 2×2 matrix M write t=tr M and Δ=det M. Direct identities are

    χ_(2)(M)=t²-Δ=((tr M)²+tr(M²))/2,
    t²=χ_(2)(M)+Δ,
    χ_(3)(M)=t³-2tΔ,
    χ_(2,1)(M)=tΔ.

There is an actual natural isomorphism S_(2,1)V≅det(V) tensor V and

    V tensor Sym²V ≅ Sym³V direct sum (det(V) tensor V).

For completeness, multiplication μ:V tensor Sym²V→Sym³V has natural section

    δ(f)=(1/3) sum_i e_i tensor (partial f / partial e_i).

Its kernel is the image of the natural injection

    ι((u wedge v) tensor w)=u tensor (vw)-v tensor (uw).

Euler's identity proves μδ=id and μι=0, and dimensions give the direct sum. These definitions are basis independent and natural for all linear maps. In the ordered tensor basis

    e1⊗e1², e1⊗e1e2, e1⊗e2²,
    e2⊗e1², e2⊗e1e2, e2⊗e2²,

the six columns δ(e1³),δ(e1²e2),δ(e1e2²),δ(e2³),ι(det⊗e1),ι(det⊗e2) form

    B = [[1,0,0,0, 0, 0],
         [0,2/3,0,0, 1, 0],
         [0,0,1/3,0, 0, 1],
         [0,1/3,0,0,-1, 0],
         [0,0,2/3,0, 0,-1],
         [0,0,0,1, 0, 0]].

Its determinant is 1, and

    (A tensor Sym² A) B = B diag(Sym³ A, det(A) A).

The natural maps prove this universally; exact samples in §10 independently check the implementation, including singular A. Applied at each vertex, B supplies concrete module intertwiners for the theta stratum and for the full zero-relation representation category in positive degree.

## 8. Determinant expansions and a genuinely local positive kernel

For any complex matrix M, including singular and nondiagonalizable ones,

    det(I-zM) = sum_{r=0}^d (-z)^r tr(wedge^r M),
    det(I-zM)^-1 = sum_{m>=0} z^m tr(Sym^m M).

The second identity is formal, and converges analytically whenever |z| ||M||<1. Schur characters are polynomial class functions, so none of these formulas requires diagonalizability.

For r≥0 define

    K_r(M,N)=det(I-r M tensor conjugate(N))^-1.

For a finite family with ||M_i||≤R and rR²<1, the character Cauchy identity gives

    K_r(M,N)=sum_λ r^|λ| χ_λ(M) conjugate(χ_λ(N)).

The feature vector is (r^(|λ|/2)χ_λ(M))_λ. Its Gram matrices are positive semidefinite. This conclusion is valid for nonnormal matrices as well. A direct quantitative convergence argument uses

    |χ_λ(M)| ≤ dim(S_λ C^d) ||M||^|λ|,
    sum_{λ partition m} dim(S_λ C^d)^2
        = binomial(m+d²-1,d²-1).

Consequently the absolute tail after degree L is bounded by

    sum_{m>L} binomial(m+d²-1,d²-1) (rR²)^m,

and the whole absolute sum is at most (1-rR²)^(-d²). This also proves passage from finite feature sums to the infinite PSD kernel. Nonnegative r is an assumption; arbitrary signed weights do not give a Gram-feature proof.

This is positivity on matrix/representation feature space. No equality with a global Weil, Jensen, prime-side or completed-L-function kernel has been established. LR positivity in multiplication of characters and PSD positivity of this Cauchy kernel are different assertions, both local here.

## 9. Completion, central action and exactness: explicit limits

### Continuous finite-dimensional modules

Let the completion be with respect to the arrow ideal, and let a finite-dimensional module be continuous with the discrete topology. Some power of the arrow ideal annihilates it. Every cycle monodromy is nilpotent, so every nonempty Schur character of it vanishes. Thus the Cauchy trace kernel of §8 becomes the constant 1. One cannot silently retain the arbitrary-monodromy/invertible-arrow stratum inside this continuous finite-dimensional category.

Nevertheless ordinary affine traces do not classify these modules. In the actual theta algebra put all arrows zero except a_0=x and a_3=y from v_0 to v_2, with one-dimensional spaces at all vertices. All paths of length two act as zero. Thus these are continuous modules of the completion. For (x,y)=(1,λ), different λ give different gauge orbits (the ratio y/x is unchanged), although every cycle trace vanishes. The v_1 simple splits off; the remaining subproblem is the two-arrow Kronecker quiver. Here x,y are semi-invariants with the same point-action weight g_v2/g_v0, or the inverse weight under the coordinate-ring convention in §6. With an appropriate stability condition on the Kronecker subproblem the projective coordinate [x:y] is retained. This is a precise pencil/semi-invariant example, not a claim that ordinary polynomial invariants distinguish these nonclosed orbits. Their closures can meet the zero representation, consistently with the invariant theorem.

Positive Schur functors still preserve continuity on finite-dimensional continuous modules: sufficiently long paths become zero, and their positive Schur images are zero. What degenerates is the cycle-character information, not the existence of the module functor.

### The fixed-R lattice obstruction

For the node order take R=k[[u]] and M=R e_x direct sum R e_y, with

    x=diag(u,0), y=diag(0,u), xy=yx=0, x+y=u I.

It is an actual R-free order lattice. On Sym²_R M with basis e_x²,e_x e_y,e_y², applying the arrow maps gives

    x'=diag(u²,0,0), y'=diag(0,0,u²).

Their sum is neither uI nor u²I: it kills the mixed vector. Therefore the construction does not respect the prescribed central relation x+y=u, and even replacing the central action by u↦u² does not repair the mixed term. Over the external R this symmetric square is free, but that is not the same as a module for the original R-order with its given central action. Over k it remains a representation of the polynomial monomial algebra via x',y'. Functoriality of composition does not imply additivity on arbitrary algebra elements or compatibility with the central power-series parameter. A separate lattice construction is required.

### Failure of exactness, even for a split sequence

Let S be an actual vertex simple of the closed infinite A, with all arrows zero. The split exact sequence

    0 → S → S direct sum S → S → 0

uses first-coordinate inclusion and second-coordinate projection. Applying Sym² at its terms and maps gives

    0 → S → S direct sum S direct sum S → S → 0.

The first image is the first square; the last kernel is spanned by that square and the mixed term. Hence its middle homology is S, not zero. This explicitly refutes treating the vertexwise Schur operation as an additive/exact functor, even on split sequences.

Applying it to differentials degreewise can retain d²=0 in positive degree, but need not retain acyclicity or projectivity. Correct derived Schur constructions use mixed tensor degrees, the total differential, Koszul signs for permutations of graded factors, and suitable projective/K-flat replacements and base-ring hypotheses. In characteristic zero, appropriate Schur idempotents on the signed total tensor complex provide a familiar construction over a commutative base; one must still prove it stays in the desired order-module category. Jiang §2.4 explicitly displays the extra terms of a genuine Schur complex and its finite-projective acyclicity hypotheses. These results do not certify a naive degreewise Schur transform of the existing projective resolution.

## 10. Exact diagnostics actually executed

All calculations used Python standard-library rational arithmetic, with no random choices. They were executed in memory; no shared checker or certificate file was changed. They are finite diagnostics, supplementing rather than replacing the proofs above.

1. Took

       X1=[[1,1],[0,1]], X2=[[2,0],[0,1]], X3=[[1,0],[1,1]].

   Their monodromy is M=[[2,2],[2,3]], with t=5, Δ=2, χ_(2)=23, χ_(3)=105 and χ_(2,1)=10. Thus t χ_(2)=115=105+10.
2. For M above, N=[[1,1],[0,2]], and P=[[0,1],[-1,1]], checked the Cauchy coefficient identity for all nine ordered pairs and every degree 0 through 8: **81 exact equalities**. The left side used the Newton recurrence for the complete characters of the 4×4 Kronecker matrix; the right side summed the two-row Schur expressions det(M)^j h_(m-2j)(M). Thus the sides were not evaluated by the same expression.
3. With r=1/100, the maximum squared Frobenius norm of these three matrices is 21, so rR²≤21/100<1. Checked **all seven nonempty principal minors** of their 3×3 rational Cauchy-kernel Gram matrix; all were nonnegative and its full determinant was positive.
4. Checked a coordinate Cauchy coefficient using source weights (2,3), target dual weights (1/5,1/7): degree two equals 2281/1225 on both sides. This checks the coordinate contragredient convention explicitly.
5. Built the actual 8×8 place-permutation Young operator for shape (2,1) on (Q²) tensor three, checked Y²=3Y, rank 2, and its projected trace against the three monodromies above.
6. Constructed the displayed 6×6 intertwiner B, checked det B=1 and its intertwining identity for those three matrices plus [[0,1],[0,0]] and the zero matrix: **five exact matrix identities**, including singular cases.

No formal verification of these new general statements is claimed. The only full universal arguments asserted in this report are the elementary constructions and deductions explicitly provided above.

## 11. Concrete next results that are justified

A focused paper can safely state: positive-degree Schur module functors for this monomial infinite algebra; natural LR intertwiners for the specified vertexwise tensor operation; the exact invariant ring and Hilbert series of the retained three-cycle stratum; and the quantitative local Cauchy PSD kernel. It should state the empty-partition exception, coordinate dual convention, rank constraints, and the difference between the polynomial representation category and continuous modules/lattices of the completion.

For completed finite-dimensional modules, the explicit Kronecker slice is a more informative next test than cycle traces: compute its semi-invariant sections or chosen framed/stable quotient, retaining its pencil parameter. A general transfer of acyclic semi-invariant theorems to the cyclic relation algebra requires additional proof. For projective resolutions, formulate a genuine derived-Schur construction first and verify its central action and projective/acyclicity hypotheses; the two counterexamples in §9 must remain visible.

No arithmetic determinant comparison, global positive realization, spectral identification, or zero-location theorem follows from these representation-theoretic facts alone.
