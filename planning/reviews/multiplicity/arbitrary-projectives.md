# Arbitrary projective determinant multiplicities for the completed theta order

2026-11-03. Independent read-only adversarial proof review. No shared source, manuscript, Lean, script or output artifact was edited. The proposed sixth-power specialization is correct for **ordinary determinants of the underlying R-modules** and arbitrary Λ-linear projective endomorphisms. It is not an obstruction to every determinant functor on Perf(Λ): the branch-column derived-tensor construction below is a positive repair.

## 1. Precise ring and specialization

Work in characteristic zero, R=Q[[u]], with the actual completed elliptic-theta order Λ. Its arrow radical J satisfies Λ/J≅Q³, u∈J³, and J⁴⊂uΛ. Its three primitive vertex idempotents e_i give projectives e_iΛ of R-rank6; Λ has rank18. All tensor conventions below use right projectives and left coefficient lattices.

Put B=Λ/uΛ and r=J/uΛ. Since r is nilpotent and B/r=Q³ is semisimple, r is exactly rad(B). For each i the radical layers of e_iB have Q-dimensions
\[
1,\quad2,\quad2,\quad1.
\]
Indeed the two permitted branches give two paths in lengths1 and2; length3 gives two full turns whose sum is ue_i, leaving one independent class after reduction; all length≥4 paths are u times a positive path and vanish. The terminal-simple multiplicities are two of each of the three simples, so the special-fiber Cartan matrix is indeed all2. Only the total dimension6 and split-basic top are required for the determinant proof.

Every finitely generated projective P decomposes as ⊕_i(e_iΛ)^{n_i}. One can prove this directly: choose a basis of the Q³-top P/PJ, lift it to a map from the displayed finite sum, use Nakayama for surjectivity, split because P is projective, and apply Nakayama again to the resulting zero-top kernel. The arrow ideal is the Jacobson radical because it is topologically nilpotent, its quotient is Q³, and Λ is a complete finite R-order. Thus this decomposition is not an assumption excluding some finitely generated projectives. In particular P is R-free of rank6Σn_i.

The specialization used here is **u=0 with residue field Q**, not reduction modulo the arithmetic prime defining E_d. This distinction is essential.

## 2. Uniform formula for every Λ-linear endomorphism

Let f:P→P be any Λ-linear endomorphism. It induces block matrices
\[
\bar f_i\in M_{n_i}(\mathbb Q)
\]
on the i-th isotypic component of P/PJ. Then, as a polynomial identity,
\[
\left.\det_R(I-Tf)\right|_{u=0}
=\prod_i\det_{\mathbb Q}(I-T\bar f_i)^6.
\]
There is no diagonalizability, generic-eigenvalue, identity-tensor or minimal-complex assumption.

Proof: reduction commutes with the finite free R-determinant, giving the Q-determinant on P/uP. Lift the top matrices to the Λ-linear map g whose i-to-i block is the constant scalar matrix bar(f_i), with all other blocks zero. Then f−g has zero top, so its image lies in PJ. By Λ-linearity,
\[
(f-g)(PJ^r)\subseteq PJ^{r+1}.
\]
After reducing modulo u this says f and g induce exactly the same map on every radical-associated-graded layer. On the i-th summand of such a layer, g is bar(f_i) repeated dim_Q(e_i rad(B)^j/e_i rad(B)^(j+1)) times. The determinant of a filtration-preserving map is the product of its associated-graded determinants. Summing those layer dimensions gives6, proving the formula. This also explains why arbitrary off-diagonal/radical entries cannot supply a counterexample: they lie strictly above the relevant filtration diagonal.

Equivalently, the kernel of End_B(P/uP)→∏M_(n_i)(Q) is a nilpotent ideal that lowers this filtration. The underlying representation of that endomorphism algebra contains its i-th simple block with multiplicity6. No unproved assertion that all endomorphisms are semisimple is needed.

## 3. Bounded perfect complexes and rational specialization

For a bounded complex P^• of finitely generated projectives and a Λ-linear chain endomorphism f, define the ordinary alternating characteristic determinant by
\[
D(T)=\prod_j\det_R(I-Tf^j)^{(-1)^j}.
\]
For the odd-over-even convention, invert D; the same conclusion follows. Every polynomial factor has constant coefficient1 in T, so its u=0 reduction is nonzero. Consequently specialization is well defined in the localization
\[
S^{-1}R[T]\longrightarrow\mathbb Q(T),\qquad
S=\{a(T):a(T)\bmod u\ne0\}.
\]
One must not claim that arbitrary elements of Frac(R)(T) have a specialization; these particular determinant ratios do.

With
\[
H(T)=\prod_{j,i}\det_{\mathbb Q}(I-T\bar f_i^j)^{(-1)^j}
\]
one obtains D(T)|_(u=0)=H(T)^6. The chain-map condition is not even needed for this elementary product assertion; it matters for its derived interpretation. Contractible-pair cancellations preserve the sixth-power property. Any endomorphism of a perfect derived object can be represented on a bounded projective complex, so passing to the perfect homotopy category does not evade the ordinary-determinant conclusion.

## 4. Excluding the stated arithmetic targets

The polynomial P_d(T)=1−a_qT+qT² is nonconstant of degree2 in Q[T]. Its order at T=∞ is −2, not divisible by6. Hence it is not a sixth power in Q(T), irrespective of whether its roots are distinct. Its reciprocal is excluded in exactly the same way.

The proposed distinct-root justification needs correction for uniform prime powers. For example E_1 over F₂₅ has36 points, a₂₅=−10 and P_1(T)=(1+5T)². This was independently verified in memory by enumeration in F₅[t]/(t²−2). The degree argument works equally well for this double-root case. At a prime q>1 the roots are automatically distinct because the integer trace cannot equal ±2√q, but that argument does not cover all prime powers.

For the classical curve zeta
\[
Z(T)=\frac{P_d(T)}{(1-T)(1-qT)},
\]
use its two **uncancelled simple poles** rather than its degree. Since the elliptic curve has its rational point at infinity,
\[
P_d(1)=\#E_d(F_q)>0,\qquad
P_d(1/q)=\#E_d(F_q)/q>0.
\]
Thus T=1 and T=1/q are distinct simple poles. A sixth power in Q(T) has every valuation divisible by6, so Z and its inverse are excluded. This proves the precise obstruction to an exact unchanged identification with the ordinary perfect-chain determinant. An arbitrary T-dependent normalization or another determinant functor must be analyzed separately.

## 5. An additional generic cube, and sharpness of the specialization

Let K=Q((u)). The actual generic algebra is M₃(K)×M₃(K). Each e_iΛ_K is one3-dimensional simple row module on each branch. If N=Σn_i, any f_K is therefore represented by F_+,F_-∈M_N(K) on the branch multiplicity spaces, and
\[
\det_K(I-Tf_K)
=\bigl(\det(I-TF_+)\det(I-TF_-)\bigr)^3.
\]
Any bounded ordinary perfect-chain determinant is already a cube in K(T). P_d's order−2 at infinity and Z's simple poles exclude equality with these targets even before specialization. The sixth power at u=0 reflects the agreement of the two branch top characters.

Do not strengthen this to a global sixth power. On e_iΛ, multiplication by one branch's full turn c_+ has ordinary determinant (1−uT)³: the two generic branch eigenvalues are u and0, each repeated3. This is not a sixth power in K(T), while its reduction is1 and meets the theorem. This supplies a concrete sharpness/control example.

## 6. Positive repair: a genuine branch-column determinant functor

Choose one permitted branch projection Λ→B_+⊂M₃(R), and let W_+=R³ be the ordinary column lattice with this left action. It is a (Λ,R)-bimodule. For every i,
\[
e_i\Lambda\otimes_\Lambda W_+\cong e_iW_+\cong R.
\]
Therefore
\[
\Phi_+=-\otimes_\Lambda^{\mathbf L}W_+:
\operatorname{Perf}(\Lambda)\longrightarrow\operatorname{Perf}(R)
\]
is a valid triangulated functor. Bounded projectives compute the derived tensor, and every term maps to a finite free R-module; W_+ need not be flat or have finite projective dimension as a left Λ-module. This is an actual integral functor, not extracting a formal root of the ordinary determinant.

For P=e_iΛ⊗Q² and f=I⊗M_d, the image is R² with endomorphism M_d and determinant P_d. For **P=Λ⊗Q²**, however, the image is W_+⊗Q² of rank6 and its determinant remains P_d³. Specify the idempotent projective when claiming the multiplicity-one positive repair.

The paired functor from W_+⊕W_- sends each e_iΛ to R² and this same tensor action gives P_d². Branch selection can remove a multiplicity through a genuine new functor, while retaining its full arithmetic/deck/trace compatibility remains another obligation. The sixth-power theorem must not be advertised as excluding this possibility.

## 7. Cut and deck equivariance: exact obstruction

In W_+ write its three primitive lines as Rw_h. Each arrow acts between the corresponding lines by a nonzero scalar a_h∈R, and the product around the branch is u. Thus its three integral valuations m_h satisfy Σm_h=1. For the standard column lattice they are0,0,1.

An R-linear σ-linearization would be an invertible U satisfying U(a·w)=σ(a)·U(w). Because σ permutes the primitive idempotents, U must carry each Rw_h isomorphically to Rw_(σh), hence by a **unit** t_h. Intertwining an arrow forces
\[
a_h t_h=a_{\sigma h}t_{\tau h}.
\]
Taking valuations gives m_h=m_(σh). Transitivity of σ makes all three valuations equal, contradicting3m=1. Therefore there is no such integral σ-linearization fixing the R-parameter. The proof applies to any rank-one-per-state integral branch lattice with full-cycle actionu, not merely to a badly chosen basis at the standard cut.

The involution α exchanges the two branch representations, so W_+ alone is not α-invariant either. Pairing W_+ and W_- can restore the branch swap when the cuts are paired consistently, but does not by itself cure the σ valuation obstruction on either generic branch; σ preserves those branch factors. The paired tensor determinant is correspondingly squared.

## 8. Ramification permits a new lattice, not automatic repair of the old one

After u=v³ over R'=Q[[v]], one may choose a new branch representation on R'³ with **every** permitted arrow vE_(h,τh). A full turn acts asv³=u and cyclic coordinate permutation gives an honest σ-linearization. This is a precise positive construction after changing the base and lattice.

The mere scalar extension of the original column lattice has arrow valuations0,0,3, so it still fails the equal-valuation test. The balanced model is generically conjugate to it by a diagonal matrix with unequal powers ofv, not by a GL₃(R') matrix. For a travel cycle with standard valuations0,0,3, diagonal weights2,1,0 balance them to1,1,1. Hence describe this as **ramification plus a different integral lattice**, not as ramification automatically linearizing the same W_+.

None of these facts identifies the branch-column functor with a canonical Frobenius/Tate realization, supplies the required ramified-base arithmetic descent, or proves a global positive determinant. They isolate what the ordinary multiplicity obstruction proves and which valid categorical replacement can avoid it.


## 9. Literal new manuscript and formal-component review

Read both `papers/theta-projective-core.tex` and `papers/theta-projective-details.tex` in full after the preceding independent derivation. Their special-fiber basis, six-block argument, generic cube, rational-function specialization, derived branch functor, α witness, rotation obstruction and ramified-new-lattice construction agree with this review. No fatal mathematical defect was found.

Two local wording points were communicated. The α witness is a **corner** unit e_i+c_i⁺ (an automorphism of e_iΛ), not a global unit of Λ; the current core now explicitly says this. The core's phrase “entire local curve zeta” should be “full local curve zeta,” since the very argument uses its poles. This latter is a terminology correction, not a failure of its valuation proof. The manuscript correctly avoids confusing lack of a strict σ lattice lift with impossibility of every determinant-level rotation comparison.

The positive repair uses only bounded-projective input, exactly as needed. W₊ is in fact nonflat on all modules: it is finitely presented over the noetherian order, so flat would imply projective; finite left projectives have R-ranks divisible by6, whereas W₊ has rank3. This confirms the importance of the explicitly derived functor. The manuscript does not falsely advertise ordinary tensor exactness.

Read all five theorem types/proofs in `lean-analytic/ThetaProjectiveMultiplicity.lean`. They prove determinants and characteristic factors for actual block-triangular matrices with six equal diagonal blocks; actual power-series constant-coefficient specialization for each scalar parameter; the degree obstruction to a quadratic rational sixth power; and a genuine formal-series product-X obstruction under the residue-zero equivalences forced by a cyclic intertwiner. The order-to-block identification, projective decomposition, coefficientwise polynomial interface, derived tensor functor and deck-linearization argument remain prose. The current verification paragraph accurately states these limits. The parent's full verification log was observed but no independent new compilation is claimed.

The primary [Stacks Tag0FJ9](https://stacks.math.columbia.edu/tag/0FJ9) and [Tag0GSX](https://stacks.math.columbia.edu/tag/0GSX) citations were checked: the first treats finite-projective determinants and exact-sequence naturality; the second treats characteristic-polynomial multiplicativity under invariant filtrations. The present filtration step is ordinary finite-dimensional Q-linear algebra, so no noncommutative-local-ring variant is being assumed by that citation.
