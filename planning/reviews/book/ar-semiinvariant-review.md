# AR meshes, determinant multiplicativity and semi-invariant syzygies

Independent read-only review, 2026-11-03. All algebra examples below are actual modules, lattice categories or explicitly specified quotient-annihilator strata of the existing infinite dessin algebras/completed orders. No shared manuscript, planning, Lean, source clone or environment was modified. Throughout take k algebraically closed of characteristic zero; the elementary module and determinant calculations themselves often need less.

## Results

1. A blanket identification “AR mesh = polynomial semi-invariant relation” is false. An actual Chebyshev quotient has an AR mesh whose presentation determinant is a free polynomial generator, with no algebraic relation at all.
2. The actual completed nodal lattice AR sequences do give relative R-characteristic determinant multiplicativity for compatible endomorphisms. This is a determinant-functor statement over R, not a Schofield product theorem for the nonperfect endpoints.
3. The usual presentation-determinant product theorem has a precise short-resolution and square-matrix hypothesis; it is proved below by horseshoe block matrices. The displayed HLS object E=ab already has infinite projective dimension in its intrinsic quotient category, so those hypotheses cannot be assumed throughout the diamond.
4. A genuine nontrivial Plücker relation exists on an explicitly framed nilpotent elliptic-square stratum of the actual completed order. The framing is essential: its six minors are not all semi-invariants for the full unframed vertex group. An unframed Chebyshev stratum also has an explicit generator relation ab=0, arising from its defining zero relation rather than from an automatic mesh algorithm.

## 1. Read scope and prior inputs

Read the relevant determinant, derived-scope and nodal/Chebyshev AR sections in `papers/dessin-core.tex` (especially 75–102 and 137–164) and `papers/dessin-details.tex` (1–48 and 91–159). Consulted the existing independent reports `/tmp/grh-dessin-semiinvariant-ar-review.md`, `/tmp/grh-dessin-schur-invariants-review.md` and `/tmp/grh-dessin-diamond-review.md`; this report does not repeat their full audits of Ringel or Huang–Lin–Su.

The HLS input remains arXiv:2110.02777v2, Proposition 3.12 and its exact intrinsic quotient category, as pinned in the prior diamond review. The completed nodal classification and two actual almost-split lattice sequences have already been proved directly in the shared papers. No claim that the HLS quotient is extension closed or has the ambient order's AR theory is made here.

Rechecked the primary setup of Schofield–Van den Bergh, arXiv:math/9907174v1, PDF pp.1–2, especially its determinant definition. [Primary PDF](https://arxiv.org/pdf/math/9907174v1). It constructs polynomial functions from suitable square projective maps; its spanning theorem is not a claim that AR meshes present all polynomial relations. Its characteristic-zero and separate homological hypotheses remain in force. No new assertion of full source-paper reading is made in this pass.

All new specific claims below have direct proofs. No numerical experiment or Lean compilation was needed.

## 2. A decisive actual-dessin counterexample

Use the infinite Chebyshev algebra/order Λ_3 already specified in the papers: vertices 1,2,3, loops l,r at the endpoints, opposite arrows a_i,b_i, and relations l²,r²,a_ib_i,b_ia_i. Quotient by the closed ideal killing vertex 3, the loops and b_1, retaining only a=a_1:1→2. The quotient is

    B=k(1→2).

It kills J² and is therefore a genuine finite continuous quotient of the completed order. Its finite module category is the full quotient-annihilator subcategory of Λ_3-mod, not a replacement for the infinite primary algebra.

In column-representation conventions let S_1=(k→0), S_2=(0→k) and E=(k --1→ k). These are all its indecomposables: any linear map decomposes, after source/target bases, into rank-one identity blocks and zero blocks. The sequence

    0→S_2 --i→ E --p→ S_1→0

is almost split. It is nonsplit because Hom(S_1,E)=0. For right almost splitness, a non-retraction from a finite sum of the three indecomposables to S_1 has zero components from S_1 and S_2 and its E components factor through p. Dually, nonsections from S_2 factor through i. End(E)=k proves minimality. Also S_2=P_2 and E=P_1 are projective B-modules, so this same AR sequence is the length-one projective resolution of S_1.

Now fix the actual representation stratum with dimension vector (1,1,0), b_1=l=r=0 and remaining arrow coordinate z. Its base group is GL_1×GL_1, acting by z↦g_2 z g_1⁻¹. The presentation determinant from P_2→P_1 is exactly

    c_(S_1)(N)=z.

Its semi-invariant ring is k[z], graded by that character. It has no polynomial relation among this generator. Nevertheless the mesh equation p∘i=0 holds identically, including at the representation z=1. Thus an AR mesh can give a nonzero, algebraically independent determinant generator rather than a syzygy among generators.

The AR assertion is intrinsic to B-mod. In the ambient Λ_3 category it fails: the module L supported at vertex 1 with space k² and l=J_2 has a nonsplit epimorphism to S_1. Every map L→E is zero, since E(a)=1 but L(a)=0 forces its vertex-1 component to vanish. This epimorphism therefore does not factor through E→S_1. One cannot promote this quotient mesh to the ambient lattice/finite-length AR category.

The quotient projectives are not Λ-projectives. On the original order, the path a still gives a valid two-term projective-presentation determinant restricting to z, but its cokernel need not be S_1 and its kernel cannot be silently removed. This is exactly the distinction between presentation determinants and module resolutions established in the existing papers.

## 3. What determinant multiplicativity actually proves

### 3a. Short projective resolutions and square evaluation

Let A be any algebra in the discussion. Suppose

    0→M′→M→M″→0

is exact and M′,M″ have length-one resolutions by finite projectives. The horseshoe construction gives a resolution for M with P_j=P′_j⊕P″_j and differential

    d=[[d′,ξ],[0,d″]].

A direct proof is to lift P″_0→M″ through M, form the surjection P′_0⊕P″_0→M, and identify its kernel through the split sequence 0→P′_1→ker→P″_1→0. For a fixed representation N, if EACH of Hom(d′,N) and Hom(d″,N) is square, applying Hom(-,N) gives a block triangular square matrix. Therefore

    c_M(N)=c_(M′)(N)c_(M″)(N),

up to the fixed sign/unit resulting from basis and ordering conventions. It is a multiplicative identity, not automatically an additive Plücker-type syzygy. The individual square conditions are essential: knowing only that the total presentation is square does not define the two factors.

In the A_2 AR example at dimension (1,1), S_1 has Euler value zero but P_1 and P_2 each have Euler value one. Their Hom presentations are rectangular. Therefore that AR sequence does not even meet the hypotheses for a product of three individual Schofield determinants.

Nor do the HLS diamonds automatically meet the finite-pd hypothesis. For H_3 with forward orientation, e_1H_3e_1=k[l]/(l²). Applying e_1 is exact and takes indecomposable projectives to free modules over this ring: P_1 gives the regular ring, P_2 and P_3 give zero. The displayed E=ab has e_1E=k with l=0. This k has the infinite periodic l-resolution over the dual numbers; applying Hom(-,k) gives Ext^j(k,k)=k in every degree. Hence pd_(H_3)(E)=∞. A finite projective resolution over H_3 would restrict to a finite free resolution of that k, a contradiction. Thus one cannot apply a pd≤1 module theorem uniformly to the four pictured diamond meshes. Their finite projective presentations still define two-term perfect complexes, with their other cohomology retained.

### 3b. A genuine nodal AR determinant identity over R

Let Λ=k[[x,y]]/(xy), u=x+y and R=k[[u]]. Keep the actual almost-split sequence

    0→Y=(y)→Λ --×x→ X=(x)→0.

All terms are R-free, of ranks 1,2,1, so the sequence splits over R and has the canonical determinant-line isomorphism det_RΛ≅det_RY⊗det_RX. For any compatible endomorphism triple, triangular matrices give

    det_R(1−TF_Λ)=det_R(1−TF_Y)det_R(1−TF_X).

This can be calculated for EVERY Λ-linear endomorphism of Λ. Write it as multiplication by f=a(u)+b(u)x. It acts on Y by a and on X by a+ub. In the R-basis (y,1) of Λ, its matrix is

    [[a,−b],[0,a+ub]].

Hence the identity is explicitly `(1−Ta)(1−T(a+ub))`. No arithmetic operator has been manufactured: f is independently specified. The same identity holds after the exact u-specialization diagram already in the papers. In particular vertical multiplication by u gives u²=u·u.

The endpoints X,Y are not Λ-perfect. They have the nonterminating alternating x,y resolutions. Applying Hom_Λ(-,Y) to this AR row gives a map Hom(Λ,Y)→Hom(Y,Y) identified with multiplication by u between R-lines; its cokernel is Ext¹(X,Y)=k. Thus un-derived Hom is not exact on this AR sequence. The relative R determinant identity is valid because these lattices are perfect after forgetting to R; it must not be sold as a consequence of a nonexistent short Λ-projective resolution. An exact triangle in D^b(Λ) becomes determinant-admissible after that specified forgetful functor, or after any other separately proved functor to a suitable perfect category.

### 3c. Actual-node ordinary semi-invariants can all be trivial

On a reduced fixed-dimension continuous finite-length representation variety of this one-vertex node, the full group is GL_d. Its scalar center acts trivially by conjugation. Every character is det^m, so a nonzero semi-invariant forces λ^(dm)=1 for all λ∈k*, and therefore m=0. All such semi-invariants are ordinary invariants. The nilpotent-filtration one-parameter degeneration in the existing paper makes every invariant constant. Consequently this ordinary semi-invariant ring is just k.

This coexists with the nontrivial lattice AR quiver above. It is a particularly direct warning that lattice AR data alone cannot guarantee interesting generators on a different finite-length representation variety. Flags, framed actions and relative R determinants are possible precisely because they change the target data.

## 4. Genuine polynomial relations, with the exact category stated

### 4a. Unframed Chebyshev relation

Instead retain both arrows a:1→2 and b:2→1, kill all other vertices/arrows, and impose the inherited ab=ba=0. On the reduced dimension-(1,1,0) stratum the coordinates are scalars a,b and the coordinate ring is

    k[a,b]/(ab).

The vertex torus gives a and b opposite weights, so both are genuine ordinary semi-invariants and `ab=0` is a genuine nontrivial generator relation. The modules kill J² and extend continuously to Λ_3. This polynomial relation follows directly from the inherited gentle zero relation. An AR drawing can be compatible with it, but the drawing alone is not a theorem identifying the ideal of relations of the semi-invariant ring.

### 4b. Framed elliptic-square Plücker relation

Use the actual elliptic-square order with two forward arrows a,b:0→1 and two reverse arrows. Fix V_0=k² with a chosen basis, V_1=k², set both reverse maps to zero, and let X=N(a), Y=N(b) be arbitrary. These modules kill J² and are genuine continuous representations of the full completed order. Form the four columns

    Z=[x_1,x_2,y_1,y_2]∈Mat_(2×4),   p_ij=det(z_i,z_j).

Under the FRAMED group H=GL(V_1), each p_ij has character det(H). The three-term identity is

    p_12 p_34 − p_13 p_24 + p_14 p_23=0.

Proof: on the dense open p_12≠0 use z_1,z_2 as a basis and expand z_3,z_4. The determinant expansion gives the formula; polynomial continuation proves it for all matrices. It is nontrivial: with X=I and Y=[[1,1],[1,2]], its three product terms are 1,−1,−2, yielding 1−(−1)−2=0. More strongly the subalgebra generated by the six minors has precisely this relation. Every nonzero skew coordinate vector satisfying this Pfaffian equation is decomposable and is represented by two rows of a matrix Z; on each patch p_ij≠0 this follows by solving the other two columns as above. The irreducible quadric equation therefore cuts out the image cone and is its prime ideal of relations.

The exact-sequence origin is explicit on the rank-two locus: `0→ker Z→k⁴ --Z→k²→0`. Its exterior determinant-line comparison expresses the complementary kernel minors by the p_ij, and decomposability supplies the same Plücker equation. This is an exterior identity from an exact diagram; it is not an assertion that this sequence is almost split. The polynomial identity extends to the lower-rank boundary, where that short exact sequence no longer has a rank-two target image.

The framing qualification is indispensable. Under the full original group GL(V_0)×GL(V_1), the mixed p_ij generally mix rather than transform by a character. For example X=I,Y=[[0,0],[1,0]] has p_13=1; swapping the source basis makes p_13 zero. It therefore cannot be a full-group semi-invariant. The ordinary full-group coefficients of det(X+tY), namely p_12, p_14−p_23 and p_34, are semi-invariants; the framed six-generator Plücker presentation must not be claimed as their unframed presentation. Similarly the mixed minors use the specified source framing, not an unqualified path-matrix presentation in the original module category.

## 5. Consequence for the proposed derived/arithmetic program

A mesh is an equation among compositions of fixed module morphisms. A semi-invariant syzygy is an identity among regular functions on a specified representation/diagram parameter space. To pass from one to the other, one needs a universal equivariant family, determinant-admissible resolutions or complexes, controlled ranks, and an explicit polynomial determinant construction. Cauchy–Binet/exterior identities can then yield real syzygies; almost splitness alone does not supply those prerequisites or identify all generators/relations.

The existing nodal exact diagram therefore supports a valid relative determinant functor, and the framed square supports a valid Plücker model. Neither gives descent-aware Frobenius actions, the conductor and archimedean comparison with a completed L-function, or positive spectral realization. The previously proved full-deck finite-free multiplicity obstructions and the absence of a GRH proof are unaffected. A useful next implementation would formalize the A_2 mesh/free-generator counterexample, the nodal compatible-endomorphism product, and the framed Plücker relation as three separate statements with their actual categories, rather than asserting one general mesh-to-syzygy theorem.
