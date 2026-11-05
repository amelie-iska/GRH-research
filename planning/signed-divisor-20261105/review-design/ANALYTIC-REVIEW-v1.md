# Independent analytic signed-d-series review — PASS

Accepted exact source: SIGNED_D_SERIES-v3.md SHA256 eff02d2e5cecae7554e873cbd4b9c34a24507b5cc78a27c7837669dc4b9247dc. Independently derived all principal formulas and read the whole v2 source; v3 adds only the raw/principal-row qualifier and the explicit0<eta<1/2 range for the near-half-plane U-cost sentence. Both prior versions/author controls remain unchanged. This is an auxiliary analytic reduction, not the signed P7 estimate or a global pole obstruction.

## Actual common divisor and raw support

Expanding the exact d-divisible row norm leaves the coefficient mu(d)A_U(da)A_U(db), with d squarefree/coprime to S*a*b*u. The residual a,b may overlap, and each must remain squarefree separately. The original character on d cancels only in |chi_d(u)|²=1_((d,u)=1); finite nu cancels by its unit modulus outside its full declared defining S. Residual raw chi_a(u)*conjugate(chi_b(u)) is never replaced by a primitive quotient at shared primes. The common complex profile and actual row/capacity/ray restrictions remain. The computed object is the raw coprime slice; current mixed/pure applications have nonprincipal rows, while a generic principal-row residue assembly is explicitly separate.

## Nine factors and the explicit normal-product constant

For P=1-alpha1-alpha2, Q=1-beta1-beta2, the common-d local coefficient is1-zPQ: its initial linear terms are -z+z*sum(alpha,beta)-z*sum(alpha_i beta_j). Thus the correct ratio has FOUR numerator zeta factors at s+v_i,s+w_j, and FIVE reciprocal factors at s and s+v_i+w_j. It is not the earlier coprime-pair1+xP+yQ factor. Residual shared primes supply P_p Q_p twice in the two residual finite factors; they are excluded from d, not removed from the original columns.

The local correction R/D has R=(1-zPQ)*four linear factors(1-zalpha),(1-zbeta), D=(1-z)*four(1-zalpha beta). Both linear coefficients are -1-sum(alpha_i beta_j). With |PQ|<=9 and the four other factor coefficients bounded1, the unexpanded R majorants in degrees2..5 are42,58,37,9, totaling146; D contributes10+10+5+1=26. Hence172|z|² bounds |R-D|. Dividing by at least(1-|z|)^5 and using every good prime norm>=7 gives exactly the stated C_eta. This is a loose valid majorant; the author's expanded symbolic R tail124 is compatible with it. The product is normally convergent for sigma>=1/2+eta and nonnegative auxiliary real parts, at fixed positive margins and uniformly over deleted primes/vertical phases. Finite H factors can vanish. This supplies neither inverse-H control nor holomorphy/nonvanishing for the nine-zeta ratio. All auxiliary slice identities at zero variables check algebraically.

## Perron is finite before limits

For V=floor(U)+1/2, integer norm n is separated by Delta_V>=1/(2V+1). The explicit one-variable error2*(V/n)^c/(pi*T*|log(V/n)|) follows by integration by parts on each of the two oscillatory tails: each contributes at most2/(T*|log x|) before the1/(2pi) factor. This constant is uniform in c>0 and needs no critical-strip assertion. Expanding the product of four truncated kernels against their indicator products gives exactly product(1+2/(pi*T_j*Delta_V))-1. The absolute placement series is the stated A_abs; it is bounded by3^(omega(a)+omega(b))*zeta_K(sigma)^9 for sigma>1.

Finite-height Fubini is therefore justified, and height-uniform C_U*(V/n)^c majorants justify successive Perron limits in the initial absolute d-series. The note never asserts absolute convergence of four infinite vertical integrals or swaps them through a later Mellin integral. Those ordering restrictions are necessary and correctly stated.

## Eight-state finite numerator

A d-prime's nine joint states have sign(-1)^[1+1_(i>0)+1_(j>0)]:00negative, four single-short positive, four double-short negative. Split d into its00 part e and the eight nonzero-state atomic ideals h_ij. They are pairwise coprime atoms, but their four short-divisor products are NOT mutually coprime across the two columns. The double-short atom must appear in both cutoff products. Residual a,b partitions are independent even at shared primes; mu(a1a2)mu(b1b2) must not be collapsed into a Mobius factor of their potentially repeated product.

Summing the squarefree e, avoiding T and h, gives1/zeta_K^T(s) times product_(p|h)(1-q^-s)^(-1). The remaining signs in the finite numerator are exactly the two residual signs and mu(h11h12h21h22). Multiplying the four cutoff inequalities counts single atoms once and double atoms twice, proving Nh<=U^4 without imposing false cross-column disjointness. The numerator is finite/holomorphic for sigma>0; local denominators there cannot vanish. At U1 only unit shorts/h survive, so N_U=1, consistent with the original direct coefficient A_1(m)=1.

The bound on N_U follows from residual3^omega, atomic8^omega, the local-denominator subpolynomial bound at fixed sigma0>0 and ideal counting up to U^4. Internal epsilons absorb logs near sigma1. The formula U^[4max(1-sigma,0)+epsilon] is uniform for sigma>=sigma0; its U^(2-4eta+epsilon) specialization is now explicitly restricted to0<eta<1/2. There is no uniform sigma0->0 claim. The full finite deletion product depends on rad(a*b*u), bounded by the actual H,D support with fixed S, and does not bound the central reciprocal zeta or its residues.

## One common-profile Mellin integral

For M=max(Na,Nb), r=min/M, the product profile is zero for r<=1/2. Otherwise Phi_r(t)=W(t)conjugate(W(rt)) or its conjugate, supported in[1/r,2]. Log derivatives of W(rt) remain bounded by the SAME M_k(W); no1/(2-1/r) factor is introduced when the support shrinks. Integration by parts in log t proves uniform rapid decay on every fixed strip. This retains the actual fixed W and its explicit seminorm cost.

After the finite numerator identity has been established separately on sigma>1, ordinary one-variable Mellin inversion at c>1 is absolutely convergent against the initial d-series. The residual a,b and row sums are finite on the annular support, so they may then be collected into the finite coherent A(s). Its local factors are holomorphic for sigma>0, and vertical rapid decay has constants depending on the actual finite D,H,U,W. This is no uniform target estimate. No contour shift over zeta zeros/poles or inferred reciprocal moment occurs.

## Actual tiny omission control and scope

The explicit prime norms7,13,19,31,43 give residual norms247/403 with overlap13, d7, row43, D1500/U25/H241. Direct divisor placements give A(a)=A(b)=-1,A(da)=1,A(db)=-1. Thus the actual scalar d coefficient is+1, while00alone is-1. For either left-single state, the remaining a placements sum-1 and b placements-1, producing+1; the right-single and all double states vanish because the remaining b placement sum is0. This independently explains the +2 nonzero-state correction without rerunning the729 author assignments. Both columns are annular and the nonprincipal row is coprime to every factor.

Their original gcd is7*13, so the complete original pair cancels over d1,7,13,7*13. The sector calculation is not an uncanceled global residue or lower bound. The surviving target remains the complete coherent integral/row sum, with all eight states, cutoff and profile costs, raw masks and possible global cancellation. No signed5/12 gain, global zero obstruction, determinant, GRH or new formalization follows.

The author's fresh symbolic/729/finite-prime control ef030ea3... is source-bound corroboration, not an old700/52/181 rerun and not a substitute for the proof review. No author checker or scientific experiment was executed by this analytic review.
