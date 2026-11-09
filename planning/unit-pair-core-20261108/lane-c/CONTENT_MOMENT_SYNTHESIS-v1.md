# Rational content with higher equality moments

8 November 2026 UTC. Author derivation, independent review pending. This combines the exact one-sided rational-content projector of PRIMAL_RATIONAL_CONTENT-v1 (SHA256 1941be5c403ae542308c9e3ec18efcec5816bf6104969c9f64b76e00f3691615) with the actual trilinear estimate of HIGHER_EQUALITY_MOMENTS-v1 (SHA256 6796c5bf4c0608530efdfef666da6fd5889dfe76c704163d51262490b9eaa5d1). Use their original pure scales \(A_1\asymp R\asymp D^{3/4}\), \(A_2\asymp1\), primitive \(Q_u\asymp R\), literal unweighted two-pivot rows, fixed \(S,\nu,u_0\), one common complex \(W\), and \(U^2\le D\le7U^2/2\). Keep the original exact full-frequency partner unit term including the direct reconstruction and the separate middle equality compensation. The only new restriction is a lower bound \(B\ge1\) on rational content \(c(\zeta_i)\) of a designated ordered partner cutoff factor. Either designation is allowed. An optional row-independent selector on \((d,m,n)\) stays permitted.

Let \(E=Nd,\ d=mn,\ L_1=U/Nm,\ L_2=U/Nn\), with \(l_s,l_l\) the sorted log exponents of \(\max(1,L_i)\), and \(e=\log_D E\). For \(e\le1/4\) and each fixed integer \(j\ge2\), the normalized cross at fixed \(d,m,n\) is bounded by
\[
 O_{\epsilon,j,S,\nu,u_0}\left((DH)^\epsilon\mathcal M_{24}(W)^2
       \frac R E\left(1+B^{-1/2}D^{\rho_j}\right)\right),
\]
with the exact relative exponent \(\rho_j\) in equation (3) of HIGHER_EQUALITY_MOMENTS-v1. The first term is the separate middle equality compensation.

Indeed use the exact two ideal Möbius projectors of PRIMAL_RATIONAL_CONTENT-v1. At fixed \(v,w\), the first array has the original good squarefree label \(z=(q)x\) and the second has the original good squarefree label \(y\). Their coefficients include the original endpoints, all residual tests and the norm twists from exact profile separation. Their raw row multiplier is \(\psi_u(v)\psi_u(w)^2\mathbf1_{(d,u)=1}\), apart from the separated column phases. The signs remain \(\mu(d)\mu(w)\mu(z)\mu(y)\). In particular the rational part is never replaced by a constant phase. For each \(r\) formed from the distinct rational primes below \(v\), the two arrays have eligible cardinalities bounded by
\[
  K_z\ll L_1/(Nw\,r\max(B,r)),\qquad K_y\ll L_2/(NwNv).
\]
These are mass bounds from the actual supports and no selector here depends on the row or on the other array. A union over both content designations is disjointized by assigning the intersection to the first designation and requiring below-threshold content on the other array in the remaining sector. That extra condition is a coefficient-side selector. All below-threshold and above-threshold tests are evaluated on the original cutoff ideals before stripping. The same projectors and upper counts still apply.

Let \(Z(u)\) be either formed array, with \(K\) actual eligible ideals and coefficient magnitude at most one. At fixed second pivot, the pinned physical sixth-order sieve gives the usual second-moment estimate with normalized mass \(\sqrt K\). For its fourth moment group \(Z(u)^2\) by the actual ideal product \(b\). The product is good sixth-free and its exponents are at most two. If \(t_b\) is the number of eligible ordered pairs giving \(b\), its coefficient \(\gamma_b\) satisfies \(|\gamma_b|\le t_b\). Also \(\sum_b t_b=K^2\) and \(\max_b t_b\ll_\epsilon (DH)^\epsilon\) by the divisor bound on the polynomial length. Thus
\[
 \sum_b|\gamma_b|^2\le (\max_b t_b)K^2.
\]
Taking the square root of the second-moment norm bound for \(Z^2\) gives the same \(\sqrt K\) in the fourth-moment estimate, with the sieve factor now at the squared shortened length. Actual repeated-prime phases are products of the original raw values. A nonempty array of shortened subunit length has uniformly bounded length and the direct count gives the same normalization. In particular rational-content sparsity is retained whether the designated array receives the second moment or the interpolated shorter moment. The raw multipliers remain contractions in the positive row comparison.

Apply the same equality \(2j\)-moment and pair it with the longer second moment and shorter \(2j/(j-1)\)-moment. Keep \(\sqrt{K_zK_y}\) before using the unshortened sieve exponents. Its ratio to \(\sqrt{L_1L_2}\) is bounded by \(O(1/(Nw\sqrt{r\max(B,r)Nv}))\). The original harmonic \(w\) sum and the \(r\)-sum in PRIMAL_RATIONAL_CONTENT-v1 then yield \(B^{-1/2}\) up to subpowers. This gives the displayed estimate. It keeps the actual selected equality compensation with divisor-bounded allocation and makes no sparsity claim for it.

For \(e\le1/8\) use \(j=3\). The sufficient content exponent on the designated side is
\[
 \log_D B\ \ge\ \max\{0,\ 1/24-(l_l-l_s)/6\}.
\]
For \(e\ge1/8\), PRIMAL_RATIONAL_CONTENT-v1 already gives target at \(B\gtrsim D^{1/24}\). Therefore \(c(\zeta_i)\gtrsim D^{1/24}\) on at least one side reaches \(D^{3/4+\epsilon}\) after the original harmonic divisor summation, uniformly over all intermediate \(d\) and their permitted ordered factorizations at these pure scales. This extends the earlier all-divisor content threshold \(D^{1/12}\). The estimate retains the full wide product range and does not control the low-content complement, arbitrary row weights, or a selected set of partner dual frequencies.
