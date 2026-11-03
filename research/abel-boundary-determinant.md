# An explicit arithmetic trace-class boundary family and its metric obstruction

2026-11-03. Continuation of the relative-boundary frontier. Attempted claim: replace the escaping-terminal-block approximation by an arithmetic trace-class family realizing the existing convergent nonprincipal Dirichlet approximants, then test a common positive metric. Result: an elementary rank-one Abel construction gives an exact holomorphic Fredholm determinant L(s,χ) on Re s>0, explicit trace-norm approximations, and operators realizing every raw partial sum. A common positive inner product making this same limiting family symmetric along the critical-height line is impossible. This is an analytic realization and a failed direct symmetrization route, not a new zero-location theorem or a GRH proof. No novelty claim is made for encoding an analytic scalar function in a rank-one determinant.

## 1. Arithmetic data and a fixed Hilbert space

Fix a nonprincipal Dirichlet character χ modulo q, extended by zero at nonunits. Let A_n=Σ_(1≤k≤n)χ(k). Complete periods sum to zero and |χ(k)|≤1, hence B=sup_n|A_n|≤q. Also A_1=1. These elementary facts use no unknown zeros. Initially target ordinary L(s,χ); for completion use primitive χ of conductor q. Principal characters, general Hecke/Dedekind functions and general Artin representations are not covered by the bounded-partial-sum premise.

Use H=ℓ²({1,2,…};C). For 2^k≤n<2^(k+1), put ℓ_n=k+1 and w_n=√n ℓ_n. Set

u_n=A_n/w_n,  v_n(s)=w_n[n^(−s)−(n+1)^(−s)],  Re s>0.

Here w_1=u_1=1. A dyadic block gives Σ_(2^k≤n<2^(k+1))|u_n|²≤B²/(k+1)². Since Σ_(j≥1)j^(−2)≤2 by integral comparison, ||u||²≤2B². In particular u is nonzero and square summable; this is a fixed arithmetic vector, independent of s and of unknown zeros.

For σ=Re s>0,

n^(−s)−(n+1)^(−s)=s∫_n^(n+1)x^(−s−1)dx,

so the modulus is ≤|s|n^(−σ−1). For a compact K in Re s>0 fix 0<σ0≤inf_(s∈K) Re s and M≥sup_K|s|. Put r=2^(−2σ0) in(0,1). The kth block of ||v(s)||² is at most M²(k+1)²r^k. Thus

sup_K||v(s)||²≤M²(1+r)/(1−r)^3.

The coordinate functions are entire. The compact-uniform ℓ² tail bound below proves v is holomorphic into ℓ²: finite-coordinate holomorphic truncations converge locally uniformly in the Banach norm. The coefficient map J(v)(x)=Σ_n v_n x_n is complex linear and isometric from ℓ² to its continuous complex-linear dual, by Cauchy–Schwarz and the test vector proportional to conjugate(v). There is NO conjugation on s or on the coefficient v_n in this pairing. Confusing it with an antilinear Riesz convention would destroy the intended holomorphy.

## 2. Exact determinant and actual partial sums

Define φ_s=J(v(s))−e_1*, and K_s(x)=φ_s(x)u. It is a rank-one trace-class operator, holomorphic in trace norm. For a rank-one map u⊗φ, the sole possible nonzero eigenvalue is φ(u), and its Fredholm determinant is 1+φ(u), including the nilpotent case. Its trace norm is ||u|| ||φ||; this follows from its single nonzero singular value. Here

1+φ_s(u)=Σ_(n≥1)A_n[n^(−s)−(n+1)^(−s)]=L(s,χ).

The series is absolutely convergent in this Abel form. Finite summation by parts gives exactly

T_N(s)=Σ_(n≤N)A_n[n^(−s)−(n+1)^(−s)]
      =S_N(s)−A_N(N+1)^(−s),
S_N(s)=Σ_(n≤N)χ(n)n^(−s).

The last endpoint tends to zero and S_N has the usual Dirichlet continuation on Re s>0. Equivalently the absolutely convergent Abel expression agrees with the Euler series on Re s>1 and therefore with its continuation. There is no use of GRH or Artin holomorphy.

For N≥1 let v_N=P_Nv and φ_N=J(v_N)−e_1*, keeping the FULL u fixed. Then K_N=u⊗φ_N has determinant T_N. To recover every existing RAW partial sum, not only a subsequence, put

φ_N^raw=φ_N+A_N(N+1)^(−s)e_1*,  K_N^raw=u⊗φ_N^raw.

Since e_1*(u)=1, det_F(I+K_N^raw)=S_N exactly. At N divisible by q the endpoint is zero. The correction is explicit arithmetic data, not a fitted zero set or an unexplained determinant normalization.

The finite Galerkin compression has the same determinant. Conjugating its N×N matrix by W_N=diag(w_1,…,w_N) yields

I + A⊗(δ−e_1*)  (corrected sums),
I + A⊗[δ−e_1*+A_N(N+1)^(−s)e_1*]  (raw sums),

where A=(A_1,…,A_N)^T and δ_n=n^(−s)−(n+1)^(−s). This is an explicit finite matrix using only character sums and arithmetic exponents. The similarity is finite dimensional ONLY; W_N does not define a bounded invertible diagonal conjugacy on the infinite Hilbert space.

## 3. Quantitative trace-norm convergence

For dyadic cutoffs N_J=2^J−1 with J≥1, define

Q_J(r)=r^J[(J+1)^2/(1−r)+2(J+1)r/(1−r)^2+r(1+r)/(1−r)^3].

Writing k=J+j and expanding (k+1)^2 proves Q_J(r)=Σ_(k≥J)(k+1)^2r^k from the ordinary, first-moment and second-moment geometric series. In particular Q_J→0. The dyadic bound gives

sup_K||v−P_(N_J)v||²≤M²Q_J(r).

Hence

sup_K||K−K_(N_J)||_1≤√2 B M√Q_J(r),
sup_K||K−K_(N_J)^raw||_1≤√2 B[M√Q_J(r)+B(N_J+1)^(−σ0)].

This is O_K(N_J^(−σ0)log N_J), up to harmless small-cutoff conventions. For arbitrary N use J=floor(log2(N+1)); the remaining tail is contained in blocks k≥J, giving the same limiting control. Raw endpoint terms satisfy |A_N(N+1)^(−s)|≤B(N+1)^(−σ0).

Actual Galerkin matrices also converge in trace norm, not merely strongly. For J≥1,

||u−P_(N_J)u||²≤B²Σ_(k≥J)(k+1)^(−2)≤B²/J.

Split u⊗φ−u_N⊗φ_N=(u−u_N)⊗φ+u_N⊗(φ−φ_N). With C_K=1+M√[(1+r)/(1−r)^3], this gives

sup_K||K−P_N K P_N||_1≤B C_K/√J + √2 B M√Q_J(r).

The raw compression adds at most √2 B²(N+1)^(−σ0). No fixed terminal trace-norm defect survives. These estimates establish the required topology for this particular arithmetic analytic family. General trace-class determinant continuity is an external standard theorem, but the determinant limits here also follow directly from the exact Abel expressions. The scalar tail has the sharper elementary bound

|L(s,χ)−T_N(s)|≤B|s|/σ (N+1)^(−σ).

## 4. Correct completion

For primitive χ, parity a with χ(−1)=(−1)^a, let

g(s)=(q/π)^((s+a)/2)Γ((s+a)/2).

It is holomorphic and nonzero on Re s>0. To obtain the completed determinant use φ_s^g=g(s)J(v(s))−e_1*, NOT g(s)φ_s. Then det_F(I+u⊗φ_s^g)=g(s)L(s,χ)=Λ(s,χ). The finite raw version is g(s)[J(v_N)+A_N(N+1)^(−s)e_1*]−e_1*, giving exactly g(s)S_N. The trace-norm bounds acquire sup_K|g| on their v/endpoint terms. Multiplying the entire previous φ by g would instead produce1+g(L−1), the wrong function. This normalization is explicit.

This supplies an elementary arithmetic analytic family and its complete convergence proof. Its only potentially nonzero eigenvalue is L(s,χ)−1, or Λ(s,χ)−1 after completion. It is not a fixed height-generating operator with an independently known real spectrum. Encoding a scalar analytic function in a rank-one determinant does not prove anything about its zeros by itself.

## 5. A fixed positive metric cannot make this same family symmetric

A general Hilbert-space fact is decisive. Let u≠0 and φ≠0 be a functional. If T=u⊗φ is symmetric for a positive inner product, then for every x,

φ(x)<u,u>=conjugate(φ(u))<u,x>.

This follows by applying <Tu,x>=<u,Tx>. Thus φ is a scalar multiple of the one fixed inner-product functional <u,·>; symmetry also forces φ(u) real. If φ(u)=0 the formula would make φ=0, a contradiction. Therefore two nonzero symmetric fixed-range rank-one operators must have proportional functionals. This is valid for any one positive inner product on the same vector space with these operators everywhere defined; changing domains/completions is a different construction.

Now fix σ>0 and t≠0. The coefficient functionals φ_(σ+it) and φ_σ are NOT proportional. For n≥2 their coefficients have ratio

v_n(σ+it)/v_n(σ)=((σ+it)/σ)n^(−it)(1+O_(σ,t)(1/n)).

Indeed the integral formula in §1 gives δ_n(s)=s n^(−s−1)(1+O_s(1/n)); the positive real denominator δ_n(σ) is nonzero. Choose integers near exp(2πk/|t|) and exp((2πk+π)/|t|). Relative rounding errors tend to zero. Along the first subsequence n^(−it)→1, along the second it tends−1. The two ratio limits are nonzero and opposite, so the ratios cannot be one constant. Multiplication by a nonzero scalar g(σ+it)/g(σ) does not change this conclusion for the completed functionals. The unchanged e_1 subtraction is irrelevant on these n≥2 coordinates.

Taking σ=1/2 excludes ANY fixed positive metric making all these K_(1/2+it) symmetric, already by comparing t=0 with one nonzero t. This is an obstruction for the ACTUAL proposed family, independent of unknown zero locations. It does not exclude an enlarged operator, a different determinant representation, nonlinear Birman–Schwinger constructions, parameter-dependent metrics with a separate theorem, or a positive Hermitian pencil having the same scalar determinant through another comparison.

There is also an exact finite real-axis witness: δ_2(1)=1/6, δ_3(1)=1/12, δ_2(2)=5/36, δ_3(2)=7/144. Their normalized minor is−1/288. Nonzero weights preserve its nonvanishing, so φ_1 and φ_2 are not proportional either. This corroborates a different real-axis shortcut failure; it is not substituted for the critical-height proof.

## 6. Verification, source scope and next claim

AbelBoundary.lean verifies exact finite summation by parts, the universal finite rank-one determinant, the actual infinite geometric majorant HasSum, genuine continuous rank-one operator identities and norm difference on arbitrary complex inner-product spaces, the symmetry-imposed functional formula/nonzero eigenvalue/proportionality relation, and the exact rational kernel minor. It does NOT construct the particular dyadic u and v as mathlib ℓ² objects, define a Fredholm determinant, prove trace-norm holomorphy or formalize the critical-height asymptotic/subsequence argument. Those are full prose proofs, not hidden formal premises. No project-specific axioms or zero-location assumptions are added.

Exact rational diagnostics test χ3/χ4 finite matrices and endpoint corrections for integer real s, dyadic norm-square inequalities, the geometric tail formula and the finite minor. They also identify the previously certified χ3 fifth partial sum with the full-period cutoff S_6=T_6. Its known off-line zero persists for the corrected/raw determinant at N=6. This reuses an existing certificate, not a new numerical zero claim. No conclusion excludes all later truncations or other approximants.

Primary background checked: NIST DLMF2.10.9 (finite summation by parts),25.15 (Dirichlet L notation/completion); Bornemann, arXiv:0804.2543v1, §§3–5, pp9–15, especially determinant definition(3.2), trace-class perturbation(4.1), projection Theorem5.1. This is a focused primary theorem review, not a reading of all43pages. The rank-one and dyadic computations above are supplied directly; the corrected version of Bornemann's separate special-case numerical estimate is not used.

Next claim: a determinant-preserving comparison to a DIFFERENT positive spectral realization, or a precisely specified arithmetic derived realization, remains necessary. The fixed-metric shortcut for this particular arithmetic rank-one family is now closed negatively. Do not continue local rank-one tests as if they provided arithmetic purity. Possible productive rotation is the exact categorical three-vertex resolution/Ext splice, nodal projective patching or the preserved two-mask hybrid-energy problem. Surface-order functoriality, finite-order Hecke/Dedekind and general Artin scopes remain distinct open tasks. GRH remains unresolved.
