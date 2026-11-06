# Exact row-dependent interval Schur truncation with norm fibres

Research-only elementary lemma, 6 November 2026. This is a technical operator estimate for a NEW actual long-factor-gcd attempt. It is not a new cubic large sieve, a bound for the remaining Gauss mean, a coefficient-energy lower bound, or any GRH conclusion. It avoids declaring a zero-one Schur mask a free operator contraction.

## 1. Statement with repeated scalar values retained

Let A: l2(C) -> l2(R) be ANY finite complex matrix, with arbitrary finite row labels R and column labels C. Each column c has a real scalar x(c). Let x_1<...<x_n be the DISTINCT scalar values. The whole fibre C_j={c:x(c)=x_j} is retained; no coefficient in a repeated-value fibre is merged or discarded.

For each row r choose integers a_r,b_r in{0,...,n}. Define
M_rc=1_(a_r<j(c)<=b_r) when a_r<=b_r, and0 otherwise.
Then, for n>=1,
||M Schur A||op <= 2[1+ceil(log2 n)] ||A||op.             (1)

For n=0 the matrix is empty and the norm is0. An empty row interval is an exact zero row. For a single prefix
P_rc=1_(j(c)<=b_r),
the better explicit bound
||P Schur A||op <= [1+ceil(log2 n)] ||A||op               (2)
holds. These are bounds on an arbitrary-coefficient matrix; they do not require positive entries, distinct ideal norms, a tensor factorization of its rows, or an orthogonality assertion about arithmetic phases.

Every chosen real interval with any specified open/closed endpoints gives ranks a_r,b_r exactly: a_r counts scalar values excluded on the lower side, and b_r counts those allowed by the upper endpoint. This includes a closed singleton at a repeated norm. There are no half-weights at ties. Intersections of finitely many such scalar intervals can be converted to these ranks first.

The transpose/adjoint version is immediate from ||A*||=||A|| and the corresponding transposed mask. Thus the same estimate applies when a row-dependent cutoff is written after transposing a physical cubic matrix.

## 2. Elementary proof by finite dyadic decomposition

Put h=ceil(log2 n) and N=2^h. Pad the ordered DISTINCT-value rank axis with empty fibres n+1,...,N. The padded column Hilbert space is the original one plus zero-dimensional blocks, so the matrix norm is unchanged. Use the usual dyadic tree of{1,...,N}, with depth0 consisting of the whole set.

Every prefix{1,...,b_r}, including b_r=0 and b_r=N, has its canonical maximal-dyadic-block partition. At each depth ell=0,...,h, at most ONE block occurs in that row's partition. This follows directly from the binary expansion of b_r, or by traversing the unique tree path to the boundary: every left subtree passed when the path goes right is one block, and the all-N prefix is the root block.

For a dyadic block B at a fixed depth, let Q_B be the coordinate projection onto ALL original columns with j(c) in B, retaining each repeated-value fibre in full. Let P_B be the coordinate projection onto the rows whose canonical prefix partition contains B. At fixed depth:
- Q_B have pairwise disjoint coordinate ranges;
- P_B also have pairwise disjoint coordinate ranges, because a row uses at most one block at that depth.

Consequently the fixed-depth Schur piece is exactly
T_ell(A)=sum_(B at depth ell) P_B A Q_B.
For every vector z,
||T_ell(A)z||2^2
 =sum_B ||P_B A Q_B z||2^2
 <=||A||op^2 sum_B ||Q_B z||2^2
 <=||A||op^2 ||z||2^2.                                 (3)
Thus ||T_ell(A)||op<=||A||op. Summing the h+1 depths gives (2). No column sum has been replaced by a norm-level scalar sum: Q_B is a projection on the original coordinate space, and equal-norm columns stay distinct inside it.

Let E={r:a_r<=b_r}. The desired interval mask is EXACTLY the row contraction on E applied to the difference of its upper and lower prefixes:
M Schur A=P_E[(P^b Schur A)-(P^a Schur A)].
The triangle and (2) give (1). This explicitly pays the logarithmic Schur cost; it does not assert that arbitrary row intervals act with norm1.

## 3. Exact form for two sharp long-factor constraints

In the motivating auxiliary expansion, rows may be pairs(a,b) and columns the squarefree common divisor d. On each finite d-band, x(d)=Nd. If original long-factor intervals are
L_v < N(da) <= U_v,     L_z < N(db) <= U_z,
their intersection is
max(L_v/Na,L_z/Nb) < Nd <= min(U_v/Na,U_z/Nb).            (4)
The row can be empty. Other endpoint conventions are handled by the exact rank rule above. Dyadic clipping and capacity constants remain literal; they do not require derivatives of a smoothed replacement.

Alternatively, after Cauchy in d the matrix may have rows d and columns a. The fixed long interval N(da) in I_v gives a column-dependent d-interval; transpose to apply (1). The relevant n is the number of distinct scalar ranks in the variable whose cutoff is ordered, not a new primitive conductor or a count of angular orientations.

All source/ray/Gamma phases and raw common-prime masks must still be placed legitimately in the surrounding arithmetic coefficient vectors or kernels. This lemma supplies ONLY the sharp interval operator bound. It cannot make a joint arithmetic Schur multiplier free, cannot turn an overlapping auxiliary conductor into a primitive root, and cannot remove a full-union raw zero. Mellin separation of the actual common W, if used, retains its explicit seminorm cost.

A band Nd~R has at most O(R) integer norm values, so its logarithmic cost is O(log(2R)); the ideal columns with the same norm remain in the operator. More generally any polynomially bounded rank cardinality makes the logarithm absorbable into an explicitly allocated D^epsilon loss. This absorption requires the stated range, not an unbounded-dimension claim.

## 4. Why norm1 is genuinely false for generic interval masks

Take
A=[[1,1],[-1,1]],     M=[[1,0],[1,1]].
The mask is a row-prefix mask with thresholds1,2. Since A* A=2I, ||A||op^2=2. But for z=(1,-1/2),
||(M Schur A)z||2^2/||z||2^2=13/5>2.
Thus even a two-row prefix mask need not be an operator contraction. This is a generic finite-matrix negative control only; it is not a lower bound or an obstruction for any actual arithmetic Gauss vector.

## 5. Verification boundary

The companion deterministic standard-library script exhaustively reconstructs finite canonical prefixes and interval differences, checks repeated scalar fibres with exact endpoint ranks, and verifies the Fraction negative control. These controls test this new combinatorial truncation statement only. They are not actual ideal/character/Gauss-family data, numerical spectral evidence, or Lean. The full operator proof is (3).

The lemma is an input to a separately reviewed new long-gcd attempt. It does not itself improve whole signed13/12, global unsigned9/8, the actual unit/very-short-k BOTH-TypeI mean, determinant/zero-location, category/analytic Lean, or GRH.
