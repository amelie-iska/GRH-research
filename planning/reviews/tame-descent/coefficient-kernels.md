# Independent review: theta-column descent, selection and equivariant coefficient kernels

Date: 2026-11-03. Read-only review of the mathematical proposal; the existing theta projective core/details were inspected for the order, branch and deck conventions. No shared files, source clones or environments were modified. The statements below are proved algebraically, not inferred from numerical tests. No claim of an independent arithmetic Frobenius construction, global L-function comparison or RH/GRH proof is made.

## 1. Conventions and the actual semilinear relation

Let k=Q(ω), ω³=1 with ω≠1, R=k[[u]], S=k[[v]], u=v³, and g(v)=ωv, with g fixing k. Index coordinates by i∈Z/3. On W=S³ let the plus arrows act by vE_(i,i−1), the minus arrows by zero and the vertex idempotents by E_ii. Thus the plus full cycle is uE_ii, so this is a central representation of the base-changed completed theta order.

Define C e_i=e_(i+1), D=diag(1,ω⁻¹,ω⁻²), and Θ=Dg. The explicit three-by-three permutation C must be distinguished from any earlier two-dimensional cellular H1 matrix also denoted C. Direct calculation gives

    Θ³=C³=1,   Θ C=ω⁻¹ C Θ.

The sign of D is correct for the stated g and C: ωD_i=D_(i−1), so Dg(vE_(i,i−1))=(vE_(i,i−1))D. Consequently Θ commutes with the fixed R-order action; C intertwines its rotation σ. Since g fixes ω, the central scalar ω also commutes with Θ. Normal forms ω^c C^a Θ^b are distinct: compare their actions on v times a vector to detect b, then coordinate permutation detects a and scalar action detects c. This gives a semilinear Heisenberg group of order 27, or a projective action of C3×C3. It is not an ordinary commuting action of those two C3 groups.

## 2. Invariants are precisely the three cut lattices

For r∈Z/3 put Θ_r=ω^rΘ and let m_i(r) be the least nonnegative residue of i−r modulo 3. Then

    L_r=W^(Θ_r)=⊕_i R v^(m_i(r))e_i.

Indeed, a coefficient of v^n in coordinate i is invariant exactly when n+r−i≡0 mod 3. Each L_r is R-free of rank three, with rank one at each vertex. In its displayed basis the i-th plus arrow has scalar 1 except at i=r, where its scalar is u: the exponent is 1+m_(i−1)(r)−m_i(r), equal to zero or three. Thus tame invariants recover the old cut columns, rather than a central-fixed rotation-equivariant rank-one column.

The correct rotation direction is

    C:L_r→L_(r+1),   Θ_(r+1) C=C Θ_r.

Each L_r is preserved by the order but not by C. Twisting Θ by one character never changes its scalar commutator with C.

The comparison S⊗_R L_r→W is diagonal in these bases with diagonal entries v^m_i(r). Its determinant is v³=u, a nonunit. It is an isomorphism generically but not integrally: its cokernel has the two nonzero pieces S/(v) and S/(v²), of total S-length three; its closed-fiber rank is one instead of three.

Terminology matters here. S/R is finite faithfully flat of rank three. Flat or fpqc descent has not failed. The ramified cover is not a Galois torsor at its closed point, and a semilinear action of its abstract deck group is not automatically a full effective fpqc descent datum. Its three distinct closed-fiber inertia characters account for this failure of the particular comparison. Invariants remain exact as R-modules by averaging, since 3 is invertible; exactness of invariants does not make that comparison an isomorphism.

## 3. Full character orbit: rotation recovered at a rank cost

Let W_big=⊕_(r=0)^2(W,Θ_r), with its blockwise order action. It has S-rank nine, and hence underlying R-rank 27. Map block r to block r+1 using C; this commutes with the blockwise descent action and has cube one. Its invariant lattice is

    N=⊕_(r=0)^2 L_r,

of R-rank nine and vertex rank three. Hence the basic projective e_iΛ maps under −⊗_Λ N to R³. An external two-dimensional arithmetic matrix M_d therefore contributes P_d³ on that basic-projective input, and P_d^9 on the regular input. Pairing the plus and minus versions to recover the branch swap doubles the basic-projective multiplicity to six.

The full character orbit does not eliminate closed-point inertia in W_big. Its base-change comparison has determinant v^9 and closed-fiber rank three rather than nine. It becomes effective only after replacing the original S-lattice by the S-span of its invariants, a genuinely different integral lattice. There is also a useful description N≅Res_(S/R)W as an R-order module: the original underlying R-module splits into the three eigenspaces of Θ. This confirms the rank-nine R cost directly.

## 4. No character repair of the fixed rank-one-per-vertex model

An S-linear automorphism commuting with the branch order action is scalar a(v)I. Vertex idempotents first force a diagonal matrix; the nonzero adjacent arrow maps force its three entries equal. Thus any g-semilinear order-compatible automorphism differs from Θ by such a scalar. This scalar change does not change its commutator with C. An order-three condition imposes an additional norm-one cocycle condition, but cannot remove that commutator.

Any S-linear invertible σ-intertwiner is b(v)C for b∈S×. For it to commute with a(v)Θ one would need g(b)=ωb. Evaluation at v=0 gives b(0)=ωb(0), impossible for a unit. More generally, even an R-linear intertwiner commuting with a chosen Θ_r would restrict to an invertible rotation intertwiner on L_r, excluded by the valuation proof below.

Multiplying C by v does produce a commuting isogeny, but it is not an integral automorphism: (vC)³=uI. On L_0 with basis (e_0,ve_1,v²e_2), its matrix is [[0,0,u],[1,0,0],[0,1,0]], with determinant u. This is not a descended order-three rotation.

## 5. The general branch valuation argument

Let L be an R-free central order lattice supported on one branch, with an invertible R-linear σ-semilinear intertwiner. All vertex pieces have the same rank r. The three arrow matrices A_i have full-cycle product uI_r, so they are invertible over K=Frac(R). Their determinant valuations are nonnegative integers with sum r. Rotation identifies successive arrow matrices up to multiplication on each side by integral invertible matrices, so those three valuations are equal. Therefore 3 divides r. This excludes rank one and rank two per vertex; the full cut orbit, of vertex rank three, is sharp.

Only the existence of an invertible intertwiner is needed, not a separate order-three coherence identity. Centrality is essential: the prescribed u of the order must act as the actual R scalar u.

## 6. Stronger theorem for every full C6-equivariant coefficient lattice

Keep the actual theta order over R, with Λ_K=M_3(K)×M_3(K), σ preserving the two branches and α exchanging them. Let W be any finite R-free central left Λ-module equipped with invertible R-linear σ- and α-semilinear intertwiners. There is no requirement that W be Λ-projective, Λ-flat, or integrally split into its branches.

The generic central projectors are

    p_±=u⁻¹ Σ_i c_i^±,   e_i p_±=c_i^±/u.

Put V_±=p_±W_K and W_±=W∩V_±. These intersections are finite R-free, Λ-stable and saturated: if a nonzero scalar multiple of w lies in V_±, then w already lies in V_±. They need not sum integrally to W. The branch rotation preserves them, and the branch swap exchanges them. Write their common per-vertex ranks as r_±. The preceding valuation argument gives 3|r_±; branch swap gives r_+=r_−. Thus, for some integer m≥0,

    rank_R(e_iW)=r_++r_−=6m,   rank_R W=18m.

Rank additivity here is generic and does not assume an integral branch decomposition. For nonzero W, m≥1. The regular left lattice W=Λ, with its natural deck action by ring automorphisms, realizes m=1, so the assertion is sharp.

This proof needs the actual branch behavior of σ and α, R-linearity of their intertwiners, finite R-freeness and the fixed central parameter. If an action moves the central parameter, or u acts by u^d, the same numerical conclusion has not been proved.

## 7. Arbitrary induced actions, not merely external tensor actions

There is a further valid strengthening. For ANY finite R-free central left Λ-module W with equal vertex ranks r, define Φ_W on bounded right-projective complexes by termwise tensoring. Let P=⊕_i(e_iΛ)^(n_i), f∈End_Λ(P), and let A_i be its top multiplicity blocks modulo the completed arrow radical. Then

    det_R(1−T Φ_W(f)) mod u
      = (∏_i det_k(1−T A_i))^r.

Proof: let B=Λ/uΛ, J=rad(B), and W_0=W/uW. Filter every summand e_iW_0 by e_i J^aW_0. An entry of f lying in the radical raises this filtration by at least one. Modulo it, an entry is a scalar at a fixed vertex. On each associated-graded vertex piece f acts as A_i tensor the identity. Summing the dimensions of these pieces gives dim_k e_iW_0=r. Triangular determinants yield the formula. The nilpotence of J, not any projectivity of W, ensures the finite filtration. This also explains why a bare Cartan-rank statement alone is insufficient without its filtration proof.

Consequently the full-C6 lattices of Section 6 yield an exponent 6m for arbitrary induced f. For a bounded projective chain endomorphism, the finite alternating ratio specializes to a (6m)-th power in k(T). Every determinant factor has constant coefficient one in T, so its special-fiber denominator remains nonzero. Cancellation does not change the divisibility of the rational divisor.

This rules out equality with a constant-in-u local quadratic P_d: its degree-at-infinity valuation is −2, which is not divisible by 6m, even if it has repeated roots. It also rules out the full local curve zeta P_d/((1−T)(1−qT)): q>1 and |a_q|≤2√q imply P_d(1)=q+1−a_q>0, so the pole at T=1 is simple. No distinct-root hypothesis for the numerator is needed.

Thus the obstruction really covers all finite R-free central coefficient kernels with the stipulated strict full symmetry, and all arbitrary actions INDUCED from finite projective order endomorphisms through that fixed kernel. It does not cover arbitrary unrelated endomorphisms of the output R-module, infinite objects, changed central actions, or alternative reduced/categorical determinant theories. Tensoring bounded projectives computes a derived functor to Perf(R) without assuming W flat over Λ; a bounded acyclic projective complex is contractible and remains so after tensoring.

## 8. Homogeneous functors and determinant-line exceptions

For a homogeneous polynomial functor of degree d with induced Θ and C, the commutator becomes ω^(−d). A nonzero object with the induced operators cannot have them commute unless 3|d. On a complex, if the commutation is imposed only up to homotopy, the difference is a nonzero scalar times an invertible map when 3∤d; it forces the identity null-homotopic. The conclusion then applies to nonzero objects of the derived category, not merely to a complex with some nonzero terms. Mixed degrees require separate central-weight sectors modulo three.

Divisibility of d does not guarantee effective coarse descent: Sym³W still has nontrivial closed-fiber inertia. Conversely, the top exterior line is a genuine exception at the group/determinant level: det D=1 and det C=1, so on ∧³_SW the actions are g and the identity. It descends effectively to an R-line. This is why the module-level obstruction must not be advertised as a blanket determinant-line obstruction.

That line is not automatically a unital Λ-module: applying ∧³ to the three rank-one vertex projectors gives zero, while ∧³I=1. Polynomial functors are not additive maps of endomorphism rings. A natural degree-d functor also sends the scalar uI to u^dI. Vertexwise Schur constructions can preserve the zero-path relations but change the full-cycle scalar to u^d, so they do not automatically remain coefficient kernels for the fixed central action. For a determinant of a mixed complex, the central commutator depends on its alternating weighted rank and can cancel; a raw degree-divisibility rule must not be applied to every determinant category.

Finally, changing from Q to k=Q(ω) is itself part of the data. A factor P_d with rational coefficients occurring once over k[[u]] becomes P_d² under the ordinary determinant after restriction of scalars to Q[[u]]. An intended rational multiplicity-one result needs its own coefficient-field descent comparison.

## Conclusion and coverage

The proposed ramified commutator and its sign are correct. The invariant lattices restore the cut; the full orbit restores rotation at vertex rank three, and full branch symmetry enforces vertex rank six. The general arbitrary-endomorphism special-fiber formula strengthens the latter to an actual obstruction for all fixed finite free full-symmetry coefficient kernels, without a flatness assumption. Neither ramification nor a character twist gives the requested original multiplicity-one descent for free. The positive determinant-line exception and the exact scope of the arbitrary-action statement must be retained. The construction of a local degree-two arithmetic carrier independently from Frobenius data remains open, as do all global arithmetic and positive spectral comparisons.

## 2026-11-03 final literal manuscript review

Read completely, without shared edits:

- `papers/theta-tame-core.tex`, lines 1–43, SHA256 `429a1261516ad3ffda779c860dccf52a3f89304bf6b51128fa3a528d3f15443e`.
- `papers/theta-tame-details.tex`, lines 1–108, SHA256 `1f51f778ddd53a742bb0431207c7c0ffd1bf586e853116820a1954ad971118e2`.

No actionable mathematical correction was found in these literal versions. In particular:

1. Core lines 2–21 and details lines 5–58 consistently use Θ=Dg, the sign ω², the fixed lattice `(e0,ve1,v²e2)`, and the nonunit comparison of determinant lines. The carrier endomorphism algebra calculation is correct: its invariant entries become R below/on the diagonal and uR above. Conjugation by C descends to conjugation by A because the basis-change conjugator is v⁻¹A and the scalar disappears. Ad(A) really preserves this hereditary order and has order three despite A not being an integral unit. These statements concern the carrier endomorphism algebra, as the text explicitly says.

2. Details lines 80–90 correctly identify each cut lattice L_j with the left column B_+e_j. The exponent identity δ_(i0)+t_(i−1,j)−t_(ij)=δ_(ij) includes the cyclic boundary i=0 and is valid. Thus the entire invariant cut orbit is the regular left B_+, not a multiplicity-one column. Pairing branches produces B_+×B_− with vertex rank six.

3. The normalization comparison in details line 92 is correct for every finite projective P and linear f. The natural map P→P⊗_ΛB is injective (P is flat/projective), becomes an isomorphism over K, and intertwines f with its extension. Both R-modules are finite free, so their generic characteristic determinants agree and injectivity R[T]→K[T] proves exact equality of ordinary characteristic polynomials over R. The alternating ratio assertion follows. This is polynomial equality, not a claim that the natural integral comparison of determinant lines is a unit; the earlier determinant-line calculation remains compatible with it.

4. Core lines 30–43 and details lines 94–106 correctly handle arbitrary finite free central kernels and arbitrary induced endomorphisms. The branch intersections need no integral direct-sum decomposition. Their generic components are spanned by those intersections, the valuation proof enforces ranks divisible by three, and branch swap doubles that rank. The radical filtration proves the arbitrary-f formula, rather than relying only on an external identity-tensor insertion. Left flatness is correctly absent. The zero-kernel case m=0 yields determinant one and also cannot equal either target.

5. The local quadratic obstruction does not require distinct roots: degree two already excludes a sixth-multiple rational power. The full zeta obstruction uses its uncancelled simple pole at T=1. The relevant local bound and q>1 are supplied in the preceding projective section. The manuscript retains the hypotheses of finite R-freeness, fixed central scalar u, invertible R-linear deck intertwiners, induced actions, and the stated k-valued base. It does not generalize the result to arbitrary unrelated R-linear arithmetic operators, twisted determinant categories or infinite analytic objects.

6. Details lines 60–77 correctly separate homogeneous/Schur group-action cancellation from coarse descent and from unital Λ-module functoriality. The stated Sym³ inertia multiplicities (4,3,3) are correct. The aI+bC commutator and the determinant of aI+bA have the displayed signs. The text does not confuse a carrier rotation intertwiner with an order-linear endomorphism or promote the failed Jacobi-plane attempt to an arithmetic descent theorem.

Coverage limitations: this pass checked all displayed mathematics and scope in these two TeX files, using the already established theta-order conventions. It did not independently reread the external Alper/root-stack sources; their use here is explicitly interpretive, and none of the determinant or invariant-lattice proofs relies on them. The bibliography entries for both cited keys exist. Lean compilation is assigned to the separate formal reviewer and was not rerun in this pass. No private push, build, authentication, MCP use, installation or shared-file mutation was performed.
