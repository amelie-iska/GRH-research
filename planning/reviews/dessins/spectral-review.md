# Independent review: dessin Fock spectrum, Abel-family attachment and arithmetic descent

2026-11-03. Read-only adversarial review of the construction supplied in the task, checked against `research/abel-boundary-determinant.md` and the pinned Connes primary statements already cached locally. No shared manuscript, Lean, planning, source clone, environment or dependency was changed. The finite-field enumeration below was executed in memory without writing outputs.

## Verdict

The path counts, number operator, trace formulas, isometric compact-operator attachment and proposed elliptic descent counterexample are correct under the explicit hypotheses below. They give an actual Fock C*-algebra setting for the existing analytic Dirichlet family. They do not establish that the arithmetic character or Fredholm family is intrinsically reconstructed from the dessin, or that it is a module/derived/Frobenius-compatible construction.

Three qualifications should be explicit in any statement:

1. The bounded representation is of the algebraic permitted-path algebra and its concrete polynomial creation/annihilation *-algebra, not automatically of the entire J-adically completed order.
2. This is an **ungraded** spectral triple. Length parity does not supply an even spectral triple in the standard sense.
3. The compact ideal belongs to the concrete **Fock/Toeplitz** algebra. Passing to a graph/Cuntz–Krieger boundary quotient can kill that ideal, so the attached Fredholm family need not survive that quotient.

The attachment is universal at the Hilbert-space/compact-ideal level: any trace-class family on a separable Hilbert space can be inserted in the same way. This is a useful exact realization, but not by itself an arithmetic comparison theorem or a new derived functor.

## 1. Assumptions and path counts

Let Q be finite and nonempty, with E vertices and 2E arrows. Require each vertex to have exactly two incoming and two outgoing arrows, and each arrow to have exactly one permitted successor and predecessor. Paths are formal permitted paths in the quadratic monomial algebra: do not impose an additional cycle-identification, higher relation or truncation. These assumptions hold for the specified closed dessin convention; they should appear in the statement instead of being replaced by the weaker bare arrow count.

Write H=ℓ²(P), where P contains the E length-zero vertex paths and all permitted positive-length paths. There are 2E paths of every length n≥1: an initial arrow has a unique continuation. For a fixed terminal vertex e there are two paths of every positive length, because there are two arrows ending at e and each extends backwards uniquely. Thus
\[
H=\bigoplus_e H_e,\qquad
\dim H_e[0]=1,\quad \dim H_e[n]=2\ (n\ge1).
\]
Loops and coincident endpoints do not merge distinct formal paths; these multiplicities remain valid.

For left creation L_a, prepend a when the concatenation is permitted and send the vector to zero otherwise. L_a is a bounded partial isometry, with norm at most 1. Prepending preserves the terminal vertex, so each H_e reduces all creations and their adjoints. These conventions are important: a right-creation model would instead preserve initial sectors.

## 2. Number operator and spectral triple

On the precise maximal domain
\[
\mathcal D(N)=\{\xi:\sum_{p\in P}|p|^2|\xi_p|^2<\infty\},
\qquad (N\xi)_p=|p|\xi_p,
\]
N is the real diagonal multiplication operator. Its adjoint has the same domain, hence it is self-adjoint; finitely supported vectors are a core. The resolvent is diagonal with finite multiplicities and entries tending to zero, so is compact. The zero eigenspace has dimension E; every integer n≥1 has multiplicity 2E.

On finitely supported vectors,
\[
[N,L_a]=L_a,\qquad [N,L_a^*]=-L_a^*.
\]
Both creations preserve the maximal domain (shifting degree by one), and these identities extend to that domain with bounded commutators. The Leibniz rule handles every finite noncommutative polynomial in the creations, adjoints and vertex projections. This polynomial *-algebra is norm dense in the concrete C*-algebra it generates, so it gives a legitimate ungraded spectral triple.

Precisely,
\[
\operatorname{Tr}(1+N^2)^{-p/2}
=E+2E\sum_{n\ge1}(1+n^2)^{-p/2}<\infty
\quad\Longleftrightarrow\quad p>1.
\]
Thus the summability dimension is exactly 1. The triple need not be faithful after restriction to a single terminal sector; the full concrete representation is faithful by definition of its concrete algebra. The algebraic permitted-path algebra itself is faithfully represented on the full Fock space: applying a finite path combination to its appropriate vacua recovers its coefficients.

The length-parity operator Γδ_p=(-1)^|p|δ_p has ΓL_a=-L_aΓ but ΓN=NΓ. An even spectral triple would require the algebra to commute with Γ and the Dirac operator to anticommute with Γ. Therefore this Γ is not such a grading. It is harmless to call the vacuum “even under length parity,” but this is not the interval-reflection evenness required in the Connes theorems.

An additional limitation: the bounded transform F=N(1+N²)^(-1/2) differs from the identity by a compact operator. Consequently the associated ordinary odd Fredholm-module class is trivial. The triple's summability and trace formulas do not supply a nontrivial index pairing merely from this positive number operator.

## 3. Exact traces and what they determine

For t>0,
\[
\operatorname{Tr}e^{-tN}=E+2E\sum_{n\ge1}e^{-tn}
=E+\frac{2E}{e^t-1}.
\]
This is the semigroup trace of N. If “heat trace of the spectral triple” is intended to mean e^(-tN²), that is a different formula:
\[
\operatorname{Tr}e^{-tN^2}=E+2E\sum_{n\ge1}e^{-tn^2}.
\]
There is no mathematical defect in using e^(-tN), provided the operator in the exponent is stated.

Define N_+^(-s) to be zero on ker N and n^(-s) on the positive eigenspaces. On Re s>1 it is trace class and
\[
\zeta_N(s)=\operatorname{Tr}N_+^{-s}=2E\zeta(s).
\]
The equality of scalar meromorphic continuations follows from their equality on that half-plane; it is not a statement that the zeros of ζ are eigenvalues of N. The spectrum and all the displayed scalar traces depend only on E. Different dessins with the same E are unitarily equivalent as pairs (H,N), despite possibly different creation-algebra representations.

For a chosen Dirichlet character χ set χ(0)=0 on the vacuum. Then χ(N) is bounded and, for Re s>1,
\[
\operatorname{Tr}(\chi(N)N_+^{-s})=2E L(s,\chi).
\]
On one terminal sector the coefficient is 2 rather than 2E. The operator product is trace class in this half-plane, which justifies the trace. Do not claim an ordinary trace-class identity on Re s>0 merely because L has analytic continuation there. Also, χ(N) need not itself belong to the polynomial/Fock C*-algebra; bounded functional calculus of an unbounded N places it in B(H), not automatically in that smaller algebra. The twist is externally chosen arithmetic data unless an independent descent/Frobenius construction produces it.

## 4. Why the compact ideal is genuinely present

Let P_v project onto paths whose initial vertex is v. Then
\[
Q_v=P_v-\sum_{a:\,\text{initial}(a)=v}L_aL_a^*
\]
is the projection onto the length-zero vacuum δ_v. The ranges in the sum are orthogonal and exhaust all nonempty paths starting at v. Thus Q_v lies in the Fock C*-algebra.

For any permitted paths p,q ending at e,
\[
L_pQ_eL_q^*=|\delta_p\rangle\langle\delta_q|
\]
(as operators on H, supported on H_e). These are matrix units. Their norm-closed span is K(H_e), embedded by zero on the other terminal sectors. Since H_e reduces the Fock representation, multiplication on either side by any generator preserves this compact block. Hence K(H_e) is an actual closed two-sided ideal. Globally the evident compact ideal is the finite direct sum ⊕_e K(H_e); cross-sector rank-one operators are absent because the representation is block diagonal.

This proof needs the vacuum defect projections. A boundary quotient imposing the corresponding Cuntz relations kills the Q_e and the resulting compact ideal. Accordingly, say “the dessin Fock C*-algebra,” not an unspecified graph C*-algebra or Leavitt quotient.

The J-adic completion is a separate issue. Along any permitted cycle c, the series Σ_(n≥0)c^n is an element of the completed order. Its formal action on the vacuum would be Σ_(n≥0)δ_(c^n), which is not square summable; the operator series ΣL_c^n cannot converge in norm either. Thus there is no general bounded extension of this Fock representation to the completed order. Restrict to the algebraic/polynomial data unless a convergence-restricted completion is constructed.

## 5. Radial insertion of the existing Abel family

In one fixed terminal sector choose its two length-n paths p_(n,1),p_(n,2) and put
\[
\xi_n=2^{-1/2}(\delta_{p_{n,1}}+\delta_{p_{n,2}}),\quad n\ge1.
\]
Their supports are disjoint across degrees, so they are orthonormal. The map U:ℓ²({1,2,…})→H_e, Ue_n=ξ_n, is an isometry. It need not be onto; its orthogonal complement includes the vacuum and all antisymmetric degree vectors. It intertwines the positive degree operators on their natural domains.

For the existing fixed-range Abel family K_s=u⊗φ_s define
\[
\widetilde K_s=UK_sU^*=(Uu)\otimes(\varphi_s\circ U^*),
\]
with value zero on the orthogonal complement of U's range. This is rank one, hence belongs to K(H_e) and therefore to the Fock algebra. U itself does not need to belong to that algebra.

Since U*U=I,
\[
\det_F(I+\widetilde K_s)
=1+\varphi_s(U^*Uu)
=1+\varphi_s(u)=L(s,\chi)
\]
on Re s>0. The same argument gives the completed determinant with the correctly scaled coefficient functional and every previously constructed raw partial sum. The nonzero singular values of UXU* equal those of X, so
\[
\|UXU^*\|_1=\|X\|_1.
\]
Consequently all compact-uniform trace-norm convergence estimates, trace-norm holomorphy and exact raw/Galerkin determinant identities transfer unchanged. Use the matching projections UP_NU* for the transferred finite sections. A full degree-≤N projection on H_e has extra orthogonal vectors on which the inserted operator is zero, so its determinant is unchanged as well.

The common-positive-metric obstruction also transfers. If the inserted family were symmetric for one positive inner product on the common full vector space, restricting that inner product to Uℓ² and pulling it back by U would make the original family symmetric. Equivalently, all inserted functionals would have to be proportional on their fixed range, and evaluating on Ue_n gives exactly the old contradictory coefficient ratios. Changing domains or the class of admissible metric forms would require a new formulation and is not excluded indiscriminately.

What has not been proved: the inserted operators are A-linear, arise from a derived chain endomorphism/determinant line, intertwine a Frobenius/Hecke action, are canonical under dessin isomorphisms, or survive a graph boundary quotient. The finite-dimensional degree eigenspaces also allow many arbitrary choices beyond the normalized two-path sums. The construction provides a concrete home for the known scalar encoding, not an intrinsic arithmetic derivation of that encoding.

## 6. Connes hypotheses are not supplied by the vacuum

Connes–van Suijlekom, [arXiv:2511.23257v1](https://arxiv.org/abs/2511.23257v1), Theorem 6.1, p.13, assumes the operator comes from the specified real distribution on an interval and the associated quadratic form on trigonometric polynomials, with essential self-adjointness on that core, a simple isolated bottom eigenvalue and reflection-even eigenfunction. A one-dimensional vacuum eigenspace of N is insufficient. In particular, the theorem's entire function is the Fourier transform of the specified interval eigenfunction; no such identification with the Dirichlet determinant follows from the radial isometry.

Connes–Consani–Moscovici, [arXiv:2511.22755v1](https://arxiv.org/abs/2511.22755v1), Theorem 5.10, pp.23–24, concerns the restricted Weil form and its specified scaling operator, boundary normalization and quotient metric. It cannot be applied to an arbitrary simple-even-ground-state number operator. These precise hypotheses were checked in the cached primary text; no new full-paper audit is claimed here.

## 7. Exact arithmetic descent counterexample

For d≠0 over Q let
\[
E_d:y^2=x^3-d,\qquad \beta_d=x^3/d.
\]
The curve is smooth of discriminant -432d². Over C, after choosing a=d^(1/3), b=d^(1/2), the map
\[
(x_0,y_0)\mapsto(ax_0,by_0)
\]
extends to a pointed projective elliptic-curve isomorphism E_1→E_d, and β_d(ax_0,by_0)=x_0³=β_1(x_0,y_0). Thus these are isomorphic complex Belyi pairs. The map is clean: above 0 there are two ramification indices 3, above 1 three indices 2, and above ∞ one index 6. Its degree is 6; the associated clean dessin has three edges and genus 1.

At p=7 the discriminants are nonzero for d=1,2, so both have good reduction. Direct exhaustive enumeration of y for each x gives:

| d | Numbers of y-solutions for x=0,1,…,6 | #E_d(F_7), including ∞ | a_7=8-#E_d(F_7) |
| --- | --- | ---: | ---: |
| 1 | [0,1,1,0,1,0,0] | 4 | 4 |
| 2 | [0,0,0,2,0,2,2] | 7 | 1 |

This exactly matches the proposed fibers. In particular the local H¹ factors are respectively
\[
1-4T+7T^2,\qquad 1-T+7T^2.
\]
Any invariant depending only on the isomorphism class of the **complex** Belyi pair, including its abstract combinatorial quiver/order/Fock data, has the same value on the two pairs. It therefore cannot recover these distinct rational-model Frobenius factors without extra descent data. This is a standard descent obstruction, not a statement that a dessin equipped with a chosen arithmetic model and compatible Galois action can never carry such data. Keep “complex/combinatorial data alone” in the claim.

Elliptic H¹ is weight 1. In the usual unshifted variable its functional-equation center is s=1 and the local factor is 1-a_p p^(-s)+p^(1-2s). This is not the unshifted Dirichlet L scope centered at 1/2, and is not a counterexample to RH or GRH.

## Minimal acceptable claim

The closed dessin's permitted-path Fock representation has a verified dimension-one ungraded spectral triple. Its compact ideal supports an isometric insertion of the existing character-dependent Abel Fredholm family, preserving its determinant and convergence estimates. The number spectrum depends only on the edge count, and the character/family has not been derived from descent or Frobenius. The two elliptic models demonstrate precisely why an arithmetic descent datum is necessary. No complete arithmetic spectral bridge, determinant-preserving positive comparison, purity statement, or RH/GRH proof has been obtained.
