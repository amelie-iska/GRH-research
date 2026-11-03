# Final review: theta Jacobi arithmetic and the cellular carrier

2026-11-03. Full textual adversarial review of `papers/theta-jacobi-core.tex` and `papers/theta-jacobi-details.tex`, including their subsequently added inert-prime obstruction, together with all sixteen current theorem types/proofs in `lean-analytic/ThetaJacobi.lean`. No shared source, manuscript, Lean, checker or output artifact was edited in this review.

## Result and corrections

The uniform Jacobi factorization, actual theta cellular Gram form, split-case arithmetic matrix, rational chain lift, determinant cancellation and Kummer compatibility up to rational chain homotopy are correct. The new real two-dimensional obstruction at inert primes is also correct and appropriately restricted. No full GRH theorem, full order-derived Frobenius functor, or canonical integral comparison is asserted.

Three potentially misleading points were corrected during the review and have been checked in the current files:

- The base coefficients in the Kummer comparison are now explicitly j=A₁+B₁ω, distinct from π_d=A_d+B_dω. This avoids inadvertently twisting π_d a second time.
- The order-insertion tests now explicitly use the characteristic-zero order Λ_Q over Q[[u]], rational residue simples and Q², distinct from the finite field used for character sums. Determinants P_d^18/P_d^6 are characteristic-zero polynomial identities; reduction of determinant q modulo p would be singular.
- The global discussion fixes a rational d and claims only the absolute convergence region supplied by the local bound, rather than claiming its sharpness without extra prime-distribution input.

For complete clarity, introduce the CM cellular matrix and its chain lift with the explicit words **“In the split case q≡1 mod3”**. The symbol π_d is only defined in that case, and the later inert-prime obstruction correctly explains why the same real CM carrier cannot cover all primes. This is a scope clarification, not a failed split-case argument.

The complex inert replacement is valid as a one-field local model. No extension-power compatibility follows from independently choosing i√q K for each q; for example (i√p K)³=−i p^(3/2)K. If extension functoriality is later claimed, define the higher maps as powers of a fixed Frobenius rather than choosing the phase independently. The current draft calls it a local model and does not assert such compatibility.

## 1. Uniform arithmetic signs and hypotheses

The cube-fiber count is valid including zero because the first term in 1+ρ+ρ̄ is the literal constant one. The square-fiber count gives a_q=−Σ_xη(x³−d), and t=du gives the exact factor ρ(d)η(−d)J. Thus j=−η(−1)J and λ_d=η(d)ρ(d) have the correct signs/orientation. Replacing ρ by its inverse conjugates the entire pair, preserving the unordered roots.

The Gauss norm proof uses a nontrivial additive character and a nontrivial multiplicative character. The product identity requires ρη nontrivial; coprime orders 3 and 2 establish that condition. Taking three Gauss norms proves |J|²=q without presuming an arithmetic positivity theorem. All arguments hold for prime powers. The q≡2 cube bijection gives trace zero; the text properly excludes characteristics2,3 and d=0 and does not claim trace zero at every extension of an inert residue characteristic.

The F₇ values j=3+2ω and π₂=−1−3ω give traces4,1 and norm7. The F₁₃ value j=−1−4ω is a useful sign-sensitive control. Weil's cited printed pp.499–502 contain the relevant Gauss/Jacobi method with the finite-field hypotheses; the signed two-character normalization is proved directly rather than identified silently with Weil's different homogeneous notation. The general elliptic H¹ trace/determinant theorem is named as the remaining classical comparison input. Neither full cohomological trace theory nor global analytic continuation is being called elementary here.

## 2. The actual theta plane and its fixed positive Gram form

The cellular differential is ∂₁=[−1 −1 −1;1 1 1], with ∂₂=0 because every edge occurs once in each orientation in the face boundary. Its H₁ is exactly the sum-zero plane. The inclusion of the basis b₀=e₀−e₁, b₁=e₁−e₂ is
\[
B=\begin{pmatrix}1&0\\-1&1\\0&-1\end{pmatrix},\qquad
B^tB=\begin{pmatrix}2&-1\\-1&2\end{pmatrix}=G.
\]
The edge rotation P sends b₀↦b₁ and b₁↦−b₀−b₁, giving the literal C matrix in the manuscript. The deck involution exchanges the two vertices and reverses each oriented edge, so its H₁ action is −I. The two permutations commute, preserve both successor permutations and therefore induce the stated algebra/resolution relabelings. Those relabelings are semilinear/twisted-module maps; they are not silently claimed to be fixed-module Λ-linear maps.

For π_d=A_d+B_dω, M_d=A_dI+B_dC is consequently an actual action on this cellular plane. Its polynomial is 1−(2A_d−B_d)T+(A_d²−A_dB_d+B_d²)T². The norm identity gives determinantq. The Euclidean-edge form is positive by the displayed sum of three squares, and M_dᵀGM_d=qG follows from multiplication of the Eisenstein norm. The statement is scaled unitarity, not self-adjointness.

## 3. Chain lift and exact determinant cancellation

F₁=A I+B P acts by M_d on the sum-zero plane and by γ=A+B on the edge-sum line. The specified rational F₀ acts as1 on the vertex-sum line and γ on v₋−v₊. Hence F₀∂₁=∂₁F₁. Since ∂₂=0, the chosen F₂=q is a valid chain action and induces q on H₂. No continuous complex-surface Frobenius map is asserted.

The extra γ factors in det(I−TF₁) and det(I−TF₀) coincide exactly. The quotient is the **odd-over-even** determinant ratio, P_d/((1−T)(1−qT)); the alternating product with exponents(−1)^i is its inverse. The text explicitly retains that sign distinction, including cancellation as a formal rational identity at apparent intermediate singularities.

## 4. Kummer normalization and homotopy

The displayed curve-morphism identity φ⁻¹F_dφ=h_dF₁ follows directly by raising the coordinates ax,by to the qth power. In the split case the cubic and quadratic coordinates of h_d give the deck character λ_d with a consistent root-of-unity embedding. The text correctly labels dx/y as a **deck** eigencharacter; its actual Frobenius pullback in characteristicp is zero, and is not used as a nonzero eigenvalue computation.

On the cellular H₁ plane the twisting map is η(d)C^r, with ρ(d)=ω^r. Starting with j=A₁+B₁ω gives exactly π_d. The difference between the unreduced three-edge polynomial and the normalized A_dI+B_dP is c(I+P+P²), with c=0,η(d)B₁,η(d)A₁ for r=0,1,2. On C₀ the corresponding difference is zero on the vertex sum and multiplication by3c on the boundary line. The homotopy H(v₋−v₊)=c(e₀+e₁+e₂), H(v₊+v₋)=0 therefore satisfies H∂=c(I+P+P²) and ∂H equal to that boundary-line difference. It vanishes in other degrees; both F₂ actions remain q. Thus the claimed rational chain homotopy is an actual calculation, not inferred merely from matching traces.

This is compatibility of the chosen cellular model with the Kummer deck character. The draft does not upgrade it to a canonical integral Tate-lattice or order-derived comparison.

## 5. Inert-prime obstruction and the complex alternative

For q≡2 mod3 the q-power curve morphism satisfies Fσ=σ^qF. Covariant realization gives MC=C²M; the reversed pullback relation is equivalent here because C³=I and inversion has order2. Solving entries gives
\[
M=\begin{pmatrix}a&b\\a+b&-a\end{pmatrix},\qquad
\det M=-(a^2+ab+b^2)
=-\tfrac12(a^2+b^2+(a+b)^2)\le0.
\]
This contradicts the genuine elliptic Frobenius determinantq>0. It excludes a real two-dimensional realization retaining this nontrivial cubic deck action and functorial relation. It is consistent with the real-coefficient issue discussed by Deninger and does not exclude complex/ℓ-adic coefficients, a larger real space, another representation category or an infinite-dimensional Hilbert–Pólya operator.

K=[1 −1;0 −1] has K²=I, KC=C²K and KᵀGK=G. Thus F=i√q K over the complexification has trace0, determinantq, square−qI and F*GF=qG. The local polynomial is correct. Its underlying real space is dimension4 and its real characteristic polynomial is (X²+q)², so it cannot be mislabeled as the original real two-dimensional realization with unchanged determinant multiplicity. The draft explicitly retains complex versus real dimensions and lack of canonical Tate/global comparison.

## 6. Order multiplicities and global scope

The rational order has R-rank18 and each idempotent projective row has rank6. Tensoring with Q² and applying the independent Λ-linear I⊗M_d therefore gives P_d^18 and P_d^6 exactly. The residue simple gives P_d on its finite vector space but is not perfect; restoring all three residue vertices gives P_d³. The deck action permutes the simple labels, so selecting one is not fully deck symmetric. A semilinear map need not have these tensor-action powers and requires its own proof. No determinant-line root is justified by the present construction.

The finite-field curve zeta center1/2, global elliptic center1 and primitive Dirichlet center1/2 are correctly separated. A fixed rational global model and good reductions are now explicit. The Hasse/Jacobi bound proves absolute convergence on Re s>3/2; it proves no determinant-preserving continuation or positive global spectral realization. Local finite-field purity is not multiplied into a global RH assertion.

## 7. Formal and computational evidence

Read all current sixteen Lean theorem types and their proofs. The first four concern genuine MulChar/Jacobi sums over finite fields, including all three nontrivialities for the norm. The matrix components prove CM determinant/polynomial/Gram identities and real quadratic positivity, post-character F₇ matrix polynomials, the concrete cellular inclusion/restriction/three-edge determinant and rational vertex chain equation. The final three verify K identities and the actual real inert determinant obstruction. The positivity and q>0 premises of the obstruction are explicit; no unknown zero location enters.

Not formalized by these declarations: existence/selection of cubic and quadratic characters, the cube-fiber point-count theorem, definitions of j/λ/π as the particular family, actual arithmetic descent, H₀/H₂ determinant cancellation as a categorical theorem, the rational chain homotopy, or an order-to-Frobenius/global spectral functor. The current prose appropriately keeps the complete point-count and comparison deductions outside the formal claims. The complex replacement's full star-norm identity is also a prose calculation, not inferred from the real obstruction lemma.

Executed `check_theta_jacobi.py:checks()` in memory with Python-B, without invoking its output writer. It passed all734 curves at the19 specified primes:516 split twists and218 inert twists, with2,813,918 affine pairs enumerated,67,894 character multiplicativity checks and32,904 twist multiplicativity checks. Its actual cellular tests passed516 split chain checks,2,064 determinant-polynomial identities and516 rational homotopies. These are finite corroboration, not the uniform prime-power proof. The author's focused/full Lean verification was already running; no independent new compilation is claimed in this report.
