# Hodge cancellation and a relative boundary realization

2026-11-03 continuation from the projective-resolution frontier. Attempted claim: the positive Hodge operator built from the corrected resolution differential could provide a determinant-preserving replacement for the Cartan/arithmetic zero-bearing operator. Outcome: the plain finite alternating Hodge determinant cancels every nonzero spectral factor. A concrete relative infinite boundary determinant does recover the weighted Cartan determinant, but its natural finite shift sections fail trace-norm convergence and it is not a positive arithmetic realization. No GRH claim follows.

## 1. Finite complex: exact cancellation, not merely positivity

Let C be a bounded finite-dimensional complex Hilbert complex with differential d and chosen positive Hermitian inner products. Set D=d+d*, Δ=D²=dd*+d*d. Since d²=0, D is self-adjoint and exchanges parity. Let E be the even-degree sum and O the odd-degree sum, dimensions e,o. In orthonormal bases

D = [[0,B*],[B,0]],  Δ_even=B*B, Δ_odd=BB*.

Both Laplacians are positive semidefinite. Sylvester's rectangular identity gives, for every complex z,

det(I_E+zΔ_even)=det(I_O+zΔ_odd).

For μ≠0, factor μ from each square matrix. This proves the cleared equality

μ^o det(μI_E+Δ_even)=μ^e det(μI_O+Δ_odd).

Both sides are polynomials in μ, so the equality also holds at zero. The quotient is μ^(e−o) as a rational/meromorphic function. Pointwise quotient notation additionally requires a nonzero denominator; at μ=−λ for a nonzero Laplace eigenvalue there is common 0/0. This is not a pointwise identity of defined scalar divisions there. In the normalized identity the quotient is1 wherever defined and has its constant meromorphic continuation.

This proof needs neither exactness nor any purity premise. Positive nonzero Laplace eigenvalues pair between parities with identical multiplicities. An explicit cohomological interpretation is also elementary: <Δx,x>=||dx||²+||d*x||² gives kerΔ=kerd∩kerd*. Finite-dimensional orthogonal decomposition of cycles into boundaries and their perpendicular gives one harmonic representative of each class. Alternating dimensions telescope across boundaries, yielding e−o=χ(C)=χ(H(C)). The surviving shifted factor records only this index, not all nonzero eigenvalues. The Euler orientation opposite to ours in a zeta convention just reciprocates it.

Thus a plain alternating determinant built solely from d+d* does not retain the nontrivial cycle factors needed for the proposed arithmetic comparison. This rejects this particular proposed repair, not every Hodge-theoretic/graded/Frobenius construction.

## 2. Taking an ordinary determinant instead changes the problem

Keep the SAME exact two-term complex C⁰=C¹=C and d=1. Give the source metric1 and target metricr>0. The adjoint is multiplication by r, since <dx,y>_target=<x,r y>_source. Both Laplacians are r. The ordinary characteristic factor is r−z; choosing r=1 or4 moves its zero although neither the differential nor the cohomology changed. Positivity is genuine for both choices. A metric or a self-adjoint construction therefore needs its own determinant-preserving arithmetic comparison; exactness alone does not provide it.

If d depends holomorphically on a complex parameter s, d(s)* generally depends antiholomorphically. The scalar example d(s)=s gives Δ(s)=|s|². At s=1 the difference quotient tends2 along real increments and0 along imaginary increments, so it is not complex differentiable there. This local counterexample is compatible with the existing holomorphic-Hermitian rigidity theorem. It does not restrict families that are Hermitian only on a real parameter slice.

Degree-weighted analytic torsion is a DIFFERENT invariant. With a stated positive-Laplacian convention it uses exponents (-1)^(i+1)i/2 on primed determinants, rather than the unweighted parity signs above. Nonzero factors need not cancel in that expression. Its definition and invariance require bases/metrics or geometric hypotheses and, in infinite dimensions, spectral regularization. This finite result does not refute Ray–Singer torsion or known arithmetic applications of torsion. Primary focused source: Ray–Singer1971, §1 pp.147–150, Definition1.6 and Proposition1.7, DOI10.1016/0001-8708(71)90045-4; primary PDF https://www.ms.uky.edu/~hislop/papers/ray-singer1.pdf. Relevant definitions were inspected, not all66pages. Their Laplacian sign convention differs from the positive Δ used here.

An independent arithmetic chain endomorphism F commuting with d still has the cohomological determinant identity in the focused paper. It acts on surviving cohomology, not on the paired positive Laplace spectrum by definition. No argument here forces its eigenvalues to have the desired arithmetic weights. A positive metric making F a scaled isometry would be extra content, not a result of harmonic representatives.

## 3. Infinite boundary relative determinant: an exact replacement construction

Let S be the unilateral shift on ℓ²(N), S e_j=e_(j+1), and P₀ the rank-one orthogonal projection to e₀. Direct coordinate calculation proves S*S=I and SS*=I−P₀. The isometry is bounded; its adjoint deletes the first coordinate. For a finite matrix M on C^r with I−M invertible, put H=ℓ²(N)⊗C^r and

A_M=I−(S*S)⊗M=I⊗(I−M),
C_M=I−(SS*)⊗M=P₀⊗I+(I−P₀)⊗(I−M).

Both are boundedly invertible. Their inverses are respectively I⊗(I−M)^−1 and P₀⊗I+(I−P₀)⊗(I−M)^−1. On the initial r-dimensional boundary, A_MC_M^−1=I−M; on its orthogonal complement it is the identity. Hence

A_MC_M^−1=I−P₀⊗M,
R(M):=det_F(A_MC_M^−1)=det(I−M).

The perturbation is finite rank, so this Fredholm determinant is defined by the ordinary determinant on its finite-dimensional support; no divergent individual determinant is divided. The identity also follows from the universal ring formula in the new Lean module. It is a relative determinant, not det_F(A_M)/det_F(C_M): the two bulk perturbations of I generally are not trace class.

As a function of M, R extends polynomially to det(I−M) through singular I−M. At those points the original quotient operator is undefined: the continuation must be distinguished from that operator. Swapping the relative pair to C_M A_M^−1 inverts the determinant where defined; merely exchanging the order of multiplication does not.

For the finite arrow-transition matrices U,V from the weighted Cartan theorem,

R(−V)/R(U)=det(I+V)/det(I−U)=det C_A.

Initially require both I−U and I+V invertible for the quotient-operator construction. The numerator's polynomial continuation permits I+V singular; the scalar quotient is meromorphic across det(I−U)=0. For the node, scalar boundary parameters give R(−t)/R(t)=(1+t)/(1−t). Thus the corrected resolution/Cartan invariant now has an explicit infinite Hilbert-space relative boundary realization. This is a useful comparison object but is generally non-self-adjoint: U and V need not be Hermitian, and it supplies no Galois action, prime identification, gamma factors or positive metric.

## 4. Exact failure of the natural finite-section limit

For N≥2, let S_N shift on span(e₀,…,e_(N−1)) and kill the last vector. Then

S_N*S_N=I−P_(N−1), S_NS_N*=I−P₀.

Define A_(M,N),C_(M,N) by the same formulas and extend their relative product by identity to the infinite tail. Its action is I−M at e₀⊗C^r, (I−M)^−1 at e_(N−1)⊗C^r, and identity elsewhere. Thus its finite determinant is always1. The proposed infinite boundary relative determinant is det(I−M), which need not be1.

The discrepancy has a precise analytic cause. For each fixed square-summable vector x, ||x_(N−1)||→0, so the terminal defect tends strongly to zero. The operators converge strongly to I−P₀⊗M. But their difference from that limit is

P_(N−1)⊗[(I−M)^−1−I].

Its trace norm is the constant ||(I−M)^−1−I||₁, positive for M≠0. Indeed embedding a finite matrix on a coordinate subspace preserves its nonzero singular values; if the inverse difference were zero, M would be zero. There is no trace-norm convergence and no determinant-continuity theorem to invoke. For the exact scalar M=1/2, finite determinants are1, the limiting relative determinant is1/2, and the trace-norm distance is1 for EVERY N≥2. The defect is at the escaping last boundary, not an unspecified regularization error.

A useful additional warning is that a trace-class DIFFERENCE of heat operators does not suffice for the usual individual heat-trace cancellation theorem. For the infinite unilateral shift, e^(−tS*S)−e^(−tSS*)=(e^(−t)−1)P₀ has trace e^(−t)−1, whereas the Fredholm index of S is−1. Neither individual heat operator is trace class. No unrestricted infinite-dimensional Hodge cancellation claim is made here. Schatten-class conditions, individual trace-class heat operators or a specified compatible relative regularization have to be proved for the actual operator family.

## 5. Verification and continuation

New HodgeDeterminant.lean declarations prove actual block-Dirac squaring, Gram positive semidefiniteness, normalized and cleared shifted determinant identities, positive scalar metrics, the adjoint/metric-zero example, and a general noncommutative ring identity for the relative boundary product. All print theorem types and foundation dependencies. The shifted Lean equality assumes μ≠0; its polynomial extension to μ=0, the general Hilbert-complex decomposition, the infinite ℓ² construction, Fredholm determinant and trace-norm calculation remain proved in prose, not claimed kernel-checked.

The exact rational checker uses five actual finite complexes, three positive metric systems, four normalized and four shifted parameters (including zero and a negative mass), and natural shift sections for four scalar M and N=2,…,7. It tests matrix identities and exact determinant/rank calculations. It does not infer universal or infinite results from finite data. An independent adversarial review reconstructed the finite obstruction, relative-boundary formula, quotient domains and strong/trace-norm failure before accepting them.

Next concrete mathematical question: can one construct an ARITHMETIC boundary correction or a different approximation family whose relative operators converge in trace norm while retaining the intended completed L determinant? For the natural shift family the terminal correction must be explicitly removed/replaced; that changes the finite determinant from1 to det(I−M), and therefore needs its own arithmetic interpretation. In the current positive-length Cartan specialization the previous zero-free/Hurwitz obstruction still applies even after this relative realization. A global arithmetic chain endomorphism and determinant-preserving positive comparison remain open. The categorical three-vertex resolution and nodal projective-patching tasks from the preceding handoff remain useful but are not substitutes for this arithmetic input.
