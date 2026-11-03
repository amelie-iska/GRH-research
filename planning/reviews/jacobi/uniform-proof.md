# Uniform Jacobi-sum benchmark for the sextic elliptic twists

2026-11-03. Independent read-only proof/review of the proposed arithmetic local benchmark. No shared source, manuscript, Lean, script or certificate was edited. The factorization, including its sign and conjugation, is correct. One scope correction is important: center 1 belongs to the global elliptic L-function in its usual normalization, whereas the finite-field curve zeta function has center 1/2.

## Exact statement

Let k=F_q be a finite field of characteristic different from 2 and 3, let d∈k* and let E_d be the smooth projective completion of y²=x³−d. Its discriminant is −432d²≠0, and it has one point at infinity. Put a_q(E_d)=q+1−#E_d(k).

Suppose q≡1 mod3. Fix a nontrivial cubic multiplicative character ρ:k*→μ₃ and the quadratic character η:k*→{±1}, each extended by zero at 0. Define
\[
J=\sum_{u\in k}\rho(u)\eta(1-u),\qquad
j=-\eta(-1)J,\qquad \lambda_d=\eta(d)\rho(d),\qquad
\alpha_d=\lambda_dj.
\]
Then
\[
a_q(E_d)=\alpha_d+\overline{\alpha_d},\qquad
j\overline j=q,\qquad
\alpha_d\overline{\alpha_d}=q.
\]
Consequently the local trace polynomial factors exactly as
\[
1-a_q(E_d)T+qT^2=(1-\alpha_dT)(1-\overline{\alpha_d}T).
\]
All these assertions hold uniformly for prime powers q, not only primes. If q≡2 mod3, then a_q(E_d)=0 and the polynomial is 1+qT².

## 1. Uniform point-count proof, including zero arguments

For each t∈k,
\[
\#\{x:x^3=t\}=1+\rho(t)+\overline{\rho(t)}.
\]
For t≠0 this follows from cyclicity of k*: cubes have three preimages, other elements none. For t=0 the count is one because both nontrivial characters vanish there. The first term is the **literal constant function 1**, not the zero-extended trivial multiplicative character. Confusing those conventions loses the x=0 term.

Similarly the number of y with y²=b is 1+η(b), including b=0. Thus
\[
a_q(E_d)=-\sum_{x\in k}\eta(x^3-d).
\]
Use the cube-fiber identity to rewrite its negative as
\[
\sum_{t\in k}(1+\rho(t)+\overline{\rho(t)})\eta(t-d).
\]
The constant-character-free term is zero because translation permutes k and η is nontrivial. For the cubic term substitute t=du:
\[
\begin{aligned}
\sum_t\rho(t)\eta(t-d)
 &=\rho(d)\eta(d)\sum_u\rho(u)\eta(u-1)\\
 &=\rho(d)\eta(d)\eta(-1)J.
\end{aligned}
\]
The other term is its complex conjugate, since η is real valued. Restoring the initial negative sign gives
\[
a_q(E_d)=-\eta(d)\eta(-1)
\bigl(\rho(d)J+\overline{\rho(d)}\,\overline J\bigr)
=\lambda_dj+\overline{\lambda_dj}.
\]
There is no d↦d⁻¹ change hidden here; λ_d has the orientation stated in the question. Changing ρ to its inverse conjugates both j and λ_d, so the unordered pair {α_d,overline(α_d)} is unchanged.

## 2. Elementary proof of the Jacobi norm

No unknown zero location, global purity input or Weil bound is needed for this step. Choose any nontrivial additive character ψ of k, and for a nontrivial multiplicative character χ put
\[
G(\chi)=\sum_{x\in k}\chi(x)\psi(x).
\]
A nontrivial additive character exists by choosing a nonzero F_p-linear functional k→F_p and composing it with exp(2πi·/p). All character values on k* have modulus one. Changing variables x=uy in the squared norm gives
\[
\begin{aligned}
|G(\chi)|^2
 &=\sum_{u\in k^*}\chi(u)
   \sum_{y\in k^*}\psi((u-1)y)\\
 &=(q-1)-\sum_{u\ne0,1}\chi(u)=q.
\end{aligned}
\]
The additive inner sum is q−1 for u=1 and −1 otherwise; the multiplicative sum over k* is zero.

For multiplicative characters χ₁,χ₂ with χ₁χ₂ nontrivial, expand G(χ₁)G(χ₂) and group by z=x+y. The z=0 contribution is
\[
\chi_2(-1)\sum_{x\in k}(\chi_1\chi_2)(x)=0.
\]
For z≠0 write x=zu, y=z(1−u). This gives exactly
\[
G(\chi_1)G(\chi_2)
=J(\chi_1,\chi_2)G(\chi_1\chi_2).
\]
In our application ρ and η are nontrivial and have coprime orders 3 and 2; their product is nontrivial of order 6. Taking squared absolute values therefore yields
\[
|J(\rho,\eta)|^2=\frac{q\cdot q}{q}=q.
\]
The real sign −η(−1) has modulus one, so |j|²=q; d≠0 also gives |λ_d|=1. This proves the polynomial factorization and, incidentally, the Hasse bound |a_q(E_d)|≤2√q for this family.

The product-character condition is essential in the general Jacobi norm theorem. When χ₁χ₂ is trivial, the usual norm-√q assertion does not apply. Here it is guaranteed, rather than assumed without checking.

## 3. The q≡2 case and exceptions

If q≡2 mod3, gcd(3,q−1)=1, so x↦x³ is a bijection of k, including 0. It follows immediately that
\[
\sum_x\eta(x^3-d)=\sum_t\eta(t-d)=0.
\]
There is no nontrivial cubic character over this field, and none is required. This covers every admissible prime power with q≡2 mod3. It does **not** say that every extension of a residue field of characteristic p≡2 mod3 has trace zero: even extension degrees have q≡1 mod3 and belong to the first case.

Exclude d=0 and characteristics 2,3 as stated. Their discriminant vanishes, and in characteristic 2 there is no nontrivial quadratic multiplicative character at all. An expression with zero-extended λ_0 is not a substitute for a smooth elliptic local factor.

## 4. Exact F₇ example and a sign-sensitive additional check

Take ω²+ω+1=0 and ρ(3)=ω. The element 3 generates F₇*, η(−1)=−1, η(2)=1 and ρ(2)=ω². The nonzero Jacobi summands for u=2,3,4,5,6 are
\[
-\omega^2,\ -\omega,\ \omega,\ -\omega^2,\ 1.
\]
Thus J=1−2ω²=3+2ω and j=J. For d=1, α_1=3+2ω has trace 4 and norm 7. For d=2,
\[
\lambda_2=\omega^2,\qquad
\alpha_2=\omega^2(3+2\omega)=-1-3\omega,
\]
whose trace is 1 and norm 7. The local polynomials are 1−4T+7T² and 1−T+7T², matching the independently counted four and seven points.

F₇ alone conceals a missing sign in j because η(−1)=−1. An additional exact check at F₁₃ with primitive generator 2 and ρ(2)=ω gives η(−1)=1, J=1+4ω and j=−1−4ω. The trace for d=1 is 2; incorrectly taking j=J would reverse it. In-memory Z[ω] arithmetic checked the uniform trace identity and norm for every nonzero d over F₇,F₁₃,F₁₉,F₃₁, a total of 66 twists. These checks supplement the uniform proof and do not replace it.

## 5. An optional explicit positive local matrix

Since J is a sum of products of cubic roots and signs, α_d∈Z[ω]. Write α_d=A+Bω. Multiplication by α_d in the basis 1,ω has the integral matrix
\[
M_d=\begin{pmatrix}A&-B\\B&A-B\end{pmatrix}.
\]
Its trace is 2A−B=a_q(E_d) and determinant A²−AB+B²=q. The fixed positive Gram matrix
\[
G=\begin{pmatrix}1&-1/2\\-1/2&1\end{pmatrix}
\]
satisfies M_dᵀGM_d=qG, by multiplicativity of the Eisenstein norm |x+yω|²=x²−xy+y². Hence q^(−1/2)M_d is G-unitary. This gives an explicit arithmetic matrix with the correct local polynomial and metric. It does not by itself establish a canonical functorial integral Frobenius-lattice identification, an adelic trace formula or a global determinant comparison.

## 6. Primary-source cross-check and scope

André Weil, **Numbers of solutions of equations in finite fields**, Bull. Amer. Math. Soc. 55 (1949), 497–508, [DOI](https://doi.org/10.1090/S0002-9904-1949-09219-4), [primary-paper scan](https://math.ucr.edu/~res/math205B-2021/app2number-theory/weil-conjectures1949.pdf), was inspected in the relevant printed pp.499–502. These pages explicitly work over a finite field k of cardinality q, with a fixed nontrivial additive character and nontrivial multiplicative characters. Equation (4), p.501, is the Gauss norm identity; the adjacent product expression yields the Jacobi norm. Weil's homogeneous multi-character j(a) has its own normalization, so it has not been silently identified with the benchmark's signed two-character j. The proof above fixes the latter from scratch. No full reading of the entire Weil article is claimed.

For a normalization cross-check, Keith Conrad's author-hosted **Gauss and Jacobi sums on finite fields and Z/mZ**, Theorems 2.2 and 2.4, pp.1–3, states precisely the nontrivial-character norm and nontrivial-product Gauss/Jacobi identities, with zero extension explicitly noted. This is supplementary exposition, not a missing proof premise: both identities have been proved above.

The factorization supplies the weight-one local numerator. Identifying that polynomial with the H¹ Frobenius polynomial uses the standard elliptic trace/determinant theorem; no new proof of the full cohomological trace formalism is asserted. For a smooth projective elliptic curve over F_q the finite-field zeta function is
\[
Z(E_d/F_q,T)=\frac{1-a_qT+qT^2}{(1-T)(1-qT)}.
\]
Its functional equation T↦1/(qT), or s↦1−s after T=q^(−s), is centered at 1/2. In contrast, the **global elliptic L-function over Q**, assembled from its weight-one local H¹ factors in the usual unshifted normalization, is centered at s=1. A primitive Dirichlet global L-function is centered at s=1/2. Local Euler-factor zeros/poles at Re s=1/2 do not determine global elliptic zeros at Re s=1. This benchmark establishes neither a Dirichlet GRH assertion nor a global elliptic RH theorem.
