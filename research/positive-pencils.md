# Positive generalized pencils and the arithmetic test

Research heartbeat2026-11-02. Attempted claim: find a valid spectral zero-location mechanism compatible with complex holomorphy after the preceding Hermitian-rigidity obstruction. Result: fixed Hermitian A and positive-definite Hermitian B yield a valid pencil; the arithmetic realization remains open. These are classical linear-algebra deductions, not a novelty or GRH claim.

## Exact positive mechanism

If (A−zB)v=0 with v nonzero, then v*Av=zv*Bv. The numerator is real and denominator strictly positive real, forcing Imz=0. With z=−i(s−1/2), all determinant zeros lie on the critical line. The actual Matrix.PosDef and Matrix.IsHermitian statements, kernel/determinant equivalence, and the substitution are verified in lean-analytic/PositivePencil.lean.

Writing H=B^(−1/2)AB^(−1/2) gives A−zB=B^(1/2)(H−zI)B^(1/2). Thus det(A+i(s−1/2)B)=i^d detB det(sI−(1/2I+iH)). This is exactly the existing fixed self-adjoint architecture in weighted coordinates, not a shortcut that proves GRH by itself.

For B≥bI>0, Cauchy–Schwarz and the imaginary quadratic form give ||(A−zB)v||≥b|Imz| ||v||. Finite-dimensional invertibility follows and ||(A−zB)^−1||≤1/(b|Imz|). The quantitative operator-norm statement is proved in prose, not in the present Lean module. Uniform determinant approximation needs additional control of dimension, prefactors, and b_N.

## Exact failure without positivity

A=[[0,epsilon],[epsilon,0]], B=diag(1,−1) are Hermitian, but det(A−zB)=−(z²+epsilon²). For0<epsilon<1/2 the transported zeros are s=1/2±epsilon within the critical strip. The Lean witness checks epsilon=1/4, its determinant vanishing, and its off-line real part; the transparent Hermitian-entry facts are discussed in prose.

## Strict imaginary positivity

At a point, if Im(v*Mv)>0 for every nonzero v, then M has no kernel and detM≠0. This actual matrix criterion is formalized. If M is holomorphic upstairs and ImM>0, this supplies nonvanishing there. Reflection M(conjz)=M(z)* extends that exclusion downstairs. Without strictness, diag(z,0) is singular everywhere; without reflection, z+i can vanish downstairs. General reflected Herglotz functions may have real-axis poles; these cannot be silently identified with an entire completed L-function.

## Concrete next arithmetic test

Specify A_N,B_N and all normalizations from arithmetic data independently of unknown zeros. Certify B_N>0, then establish determinant equality or compact-uniform approximation. For a prescribed factorization F_N/g_N=det(A_N−zB_N), the negative logarithmic derivative equals trace((A_N−zB_N)^−1B_N)=sum_j1/(lambda_j−z), with positive imaginary part upstairs when dimension is positive. A rigorous violation would reject that prescribed candidate; finite successful tests do not establish positivity globally. No arithmetic A_N,B_N satisfying the needed matching identity has been constructed in this run.

Independent adversarial review confirmed the conditions, signs, determinant normalization, inverse bound, indefinite witness and reflection caveats. Source clones remain unchanged. Next run should choose one explicit arithmetic polynomial or normalized approximant and test the required positive-metric/Herglotz certificate; it must not repeat this already-proved abstract spectral mechanism as though it supplied arithmetic matching.
