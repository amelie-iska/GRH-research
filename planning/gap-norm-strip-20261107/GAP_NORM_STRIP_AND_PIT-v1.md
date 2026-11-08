# Prime-norm strip and a source-dependent short prime error

7 November 2026 UTC. Author checked; independent review pending. The first comparison removes a pair-of-prime-moduli strip in the auxiliary central unit-cofactor Gaussian expression. The second bounds the **original short prime-counting discrepancy** using the pinned external \(7/8\) zero-free statement. The first is independent of the second. Acceptance requires the exact inclusive strip and pair-label treatment, a power budget after all inherited exclusions, and an explicit pin and fixed-field derivation for the prime input. Neither comparison estimates the full original signed main term.

## 1. An exact close-norm strip in the auxiliary comparison

Use GAP_DOUBLE_POISSON-v1 (1)–(3), GAP_DUAL_COLOURS-v2 and GAP_DUAL_OVERLAP-v1, with \(T,P\asymp D^{1/2}\), \(D^{13/40}\le R\le D^{27/80}\). Transfer from the original signed problem to this auxiliary comparison is still independently pending. The moduli are labelled good split prime ideals \(q,q'\), and both actual weights and the compensated positive cubic Gauss factors, if used, remain. Write \(\mathcal D\) for the off-diagonal \(q\ne q'\) contribution with its exact dual Gaussian. The primal diagonal is unchanged. For real \(Y\ge0\) impose \(|Nq-Nq'|\le Y\).

For the full dual frequency range, double Poisson returns the product of the two primal Gaussian sums at fixed \(q,q'\). Its absolute value is \(O(PR)\), since each raw character is bounded by one and the two Eisenstein lattice Gaussian sums are \(O(P)\) and \(O(R)\). This is an estimate for the full frequency contribution at the pair and cannot just be used for a truncated dual frequency range. At most two split prime ideals have a given rational prime norm, so the pair mask has row degree at most \(2(2\lfloor Y\rfloor+1)\). Its symmetry and \(2|b_qb_{q'}|\le |b_q|^2+|b_{q'}|^2\) give a bound for the full-frequency strip
\[
 O\!\left(PR(1+Y)\|b\|_2^2\right). \tag{1}
\]
At \(Y=0\) this still includes distinct equal-norm conjugate ideals; it is not the true ideal diagonal.

## 2. Restricting the strip to the surviving frequency sector

The previous bounds on \(\mathcal D(\mathcal E)\) for a dual selection \(\mathcal E\) were proved with no pair-of-prime cut. A pair mask cannot in general be inserted in the positive single-prime norms. For this strip choose odd \(M=O(T+1+Y)\) with \(M>2\max(\lfloor Y\rfloor,\max_{q,q'}|Nq-Nq'|)\). On \(\mathbb Z/M\mathbb Z\) use the indicator of \(-y,\ldots,y\), \(y=\lfloor Y\rfloor\). Then on the whole prime support
\[
 \mathbf1_{|Nq-Nq'|\le Y}
  =\sum_{\ell\bmod M} h_\ell e^{2\pi i\ell Nq/M} e^{-2\pi i\ell Nq'/M},
 \qquad h_\ell=\frac1M\sum_{j=-y}^y e^{-2\pi i\ell j/M}.
\]
This includes equality. The geometric series gives \(|h_\ell|\ll\min((2y+1)/M,1/\min(\ell,M-\ell))\) for \(\ell\ne0\) and \(\sum_\ell|h_\ell|\ll\log(2M)\). Replace \(b_q\) by \(b_q e^{2\pi i\ell Nq/M}\) in each summand. This preserves the squared mass, the original \(q\ne q'\) restriction and the algebraic subtraction of the inserted diagonal. It commutes with the exact log-\(Q\) separation and fixed mod-four split, preserving all raw masks. Thus all preceding upper bounds for \(\mathcal D(\mathcal E)\) hold with this strip at subpower cost for polynomial \(Y\).

Partition the excluded dual frequency union disjointly: small \(B_2\), small \(B_3\), sparse first frequency (take the two sparse selections in order), then the joint \(g,d\) overlap cut. Their boundaries are \(B_2\le D^{7/24}\), \(B_3\le D^{31/80}\), \(N\alpha\le A D^{-1/12}\) or good squarefull part norm at least \(D^{1/6}\), and \((Ng)^{5/6}(Nd)^4\ge D^{1/12}\). Each disjoint piece inherits its bound. The prior small total conductor part is included by the \(B_3\) cut. Use the **full-frequency** strip (1) minus the strip-restricted exclusions, as an equality before bounds with the same coefficients. At \(Y=D^{7/48}\), (1) has power at most \(1/2+r+7/48\le59/60\), \(r=\log_D R\). The exclusions are each at most \(D^{59/60+\varepsilon}\|b\|^2\), with their earlier \(R\)-dependence. Hence the close-norm part of the surviving auxiliary off-diagonal sector is \(O(D^{59/60+\varepsilon}\|b\|^2)\). Using the prior density for a **scale test only**, the full strip paired with a squared partner \(D\) has relative exponent
\[
 (1/2+r+7/48-1)/2+(3/8-r)/6=-3/16+r/3+7/96\le-1/480.
\]
The exclusion terms have test exponents at most \(-1/320,-1/480,-1/160,-1/160\) respectively. This leaves \(|Nq-Nq'|>D^{7/48}\) in the auxiliary complement, with both large conductors, non-sparse first frequencies and small joint overlap as before. The degree argument on the full far strip loses the power; the actual remaining Gauss weights and both twists still need cancellation. No selected original signed estimate follows.

## 3. What the pinned \(7/8\) statement would give for the short prime error

This section is a **source-dependent deduction**, not a verification of the preprint. The external input is Theorem 1.1 of OpenAI, *The Quasi-Riemann Hypothesis: A Zero-Free Half-Plane \(\Re s>7/8\)*, 30 September 2026. Pin: source math commit 4eaee87548250b2682affda7d05d947c05554bae, preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex, Git blob 268c4e3206d460c617d3d2129742a72b831b3def, SHA-256 42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3, lines 106–119. Research/exponent-frontier.md already records the source and the limits of its independent verification. Only the fixed Dirichlet functions \(\zeta(s)\) and \(L(s,\chi_{-3})\) are needed here. No growing-conductor prime theorem, new zero-free theorem or critical-line hypothesis enters the deduction.

To see the fixed-field implication, fix \(0<\eta<1/16\) and \(\sigma_0=7/8+\eta\). The fixed-\(L\) logarithmic derivatives are \(O_\eta(\log(2+|t|))\) for \(\sigma_0\le\sigma\le2,\ |t|\ge2\). The usual local partial fractions for each completed \(L\)-function, from the Hadamard product compared at \(2+it\) and the gamma factor, use the zeros with \(|\Im\rho-t|\le1\) plus an \(O(\log(2+|t|))\) remainder. There are \(O(\log(2+|t|))\) such zeros from the real part at \(2+it\). Every local denominator has modulus at least \(\eta\). Compactness gives boundedness on the vertical line for \(|t|\le2\); the pole of \(-\zeta'/\zeta\) at 1 is crossed explicitly.

For either fixed function use the coefficients \(\Lambda(n)\chi(n)\), where \(\chi=1\) for \(\zeta\), the half-integer \(x_*=\lfloor x\rfloor+1/2\), \(c=1+1/\log x_*\), \(T=x_*^2\) for large \(x\). Finite Perron inversion on \(c\) has error \(O((x_*/T)\log^2 x_*)\). In \(x_*/2\le n\le2x_*\) this follows from \(|\log(x_*/n)|\gg |n-x_*|/x_*\) and the half-integer harmonic sum; outside use \(\sum_n(\log n)n^{-c}\ll\log^2 x_*\). Moving to \(\sigma_0\) costs \(O_\eta(x_*\log(2T)/T)\) on the horizontals and \(O_\eta(x_*^{\sigma_0}\log^2(2T))\) on the vertical. The only residue is \(x_*\) for \(\zeta\). The cutoffs \(x_*,x\) contain the same integers. Absorbing logarithms with a smaller \(\eta\) gives
\[
 \psi(x;1)=x+O_\epsilon(x^{7/8+\epsilon}),\qquad
 \psi(x;\chi_{-3})=O_\epsilon(x^{7/8+\epsilon}).
\]
The difference between \(\zeta\) and the principal character modulo 3 contributes \(O(\log x)\) from powers of 3. The higher prime powers cost \(O(\sqrt x\log^2 x)\). Character orthogonality and partial summation now give \(\pi(x;3,1)=\tfrac12\operatorname{Li}(x)+O_\epsilon(x^{7/8+\epsilon})\). Exactly,
\[
 \pi_K(x)=2\pi(x;3,1)+\pi(\sqrt x;3,2)+\mathbf1_{x\ge3}.
\]
This counts both split prime ideals, the inert prime ideals of norm \(p^2\), and the ramified prime including equality. Removing fixed \(S\) costs at most \(|S|\). Thus under the stated source input,
\[
 |E_S(x)|\ll_{S,\epsilon}x^{7/8+\epsilon},\qquad
 \delta_S(U)\ll_{S,\epsilon}U^{-1/8+\epsilon},\qquad
 \mathfrak d_2(T)\ll_{S,\epsilon}T^{-1/8+\epsilon}. \tag{2}
\]
The supremum uses \(\epsilon<1/8\); the square function follows by integration on \([T,2T]\). In particular this controls the lower endpoint independently of the square function. It concerns the fixed unmasked prime count \(\pi_K^S\) only and does not restore any deleted row or residual primes.

For the original unweighted \(A_6=1\) two-pivot block in phy:short, \(v_1v_2^2\) determines the two good squarefree coprime factors. At fixed literal \(u_0\) the row count \(R_w=O(H_b)\) allows only the already justified finite natural multiplicities. This controls the unit-column range \(1/2\le L<1\). For \(1\le L\le D/U\) retain the valid branch \(\Phi_6(H_b,L)\) of the true norm. Substituting (2) into the pointwise version of cmr:joint, equivalently the absolute \(f\)-error budget rma:PIT-variation, yields
\[
 \frac{|\mathcal E_{\rm PIT}|}{D}
 \ll_{S,\epsilon}(HD)^\epsilon M_1(W)^2 U^{-1/8}
 \left[H_b+D/U+H_b^{5/6}(D/U)^{1/3}
                   +H_b^{1/3}(D/U)^{5/6}\right]. \tag{3}
\]
The \(H_b\)-term can gain logarithms, absorbed into subpowers, as is \(U^\epsilon\) from (2) with a smaller epsilon. This uses an upper branch uniformly in \(L\), without exchanging the minimum and the integral. The lower endpoint \(-E_S(U)Q(U)\) remains with its original sign before the bound. No arbitrary weights are added.

For \(2D/7\le U^2\le D\), \(U\ge7\), and \(H_b\le H=D^{3/4}\), the four powers are \(11/16,\ 7/16,\ 35/48,\ 29/48\). The largest \(35/48\) is \(1/48\) below \(3/4\) on the specified blocks. At the earlier mixed witness one can instead use its \(7/9\) norm majorant and obtain \(103/144\). More generally (3) is \(O_{S,\epsilon}((HD)^\epsilon M_1(W)^2 H)\) on \(D^{5/8}\le H\le D^{3/4}\): the last three terms require thresholds \(D^{7/16},D^{5/8},D^{17/32}\), respectively; the first needs no lower threshold. This deduction is separate from the earlier converse diagnostic linking hypothetical power errors to zero-free strips.

## 4. Limits

The strip bound is independent of the external zero-free input and estimates only one piece of the unit-cofactor auxiliary comparison. The far-norm main-frequency part and the signed unit/nonunit-cofactor pairing remain open. Under the external statement the prime-counting discrepancy has target size in the stated range, not the coherent \(K_0-\mathcal J\) term or the remaining short/principal and signed assembly. The original masks remain in the full identity. Nothing here proves a new zero-free result, treats arbitrary Dedekind, elliptic or general Artin scopes, certifies analytic/category Lean, or establishes the determinant bridge or GRH. Candidate \(109/144\), whole signed \(13/12\) and global unsigned \(9/8\) are unchanged.
