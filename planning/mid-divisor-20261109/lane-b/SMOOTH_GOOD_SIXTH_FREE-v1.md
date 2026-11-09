# Good sixth-free modes in the smooth partner band

9 November 2026 UTC. This isolated candidate combines SMOOTH_RADIAL_PARTNER-v1 with the large sixth-power-base selection of FREQUENCY_RATIONAL_CONTENT-v2. Keep their actual pure scales, unweighted rows, primitive \(Q_u\), fixed data, common complex \(W\), full ordered cutoff and exact unit-pair allocations and middle compensation. Use a smooth radial selector \(\sigma(N\mathfrak k/T)\) with \(1\le T\lesssim R\), common compact support in the positive radial variable and uniformly bounded \(C^6\) norm. This selector may depend on the fixed partner labels, independently of the two varying partner cutoff ideals and all equality labels. Apply the additional condition that the actual frequency has no good sixth-power divisor except the unit. Its \(S\)-part remains present. No additional arbitrary selector or rational-content restriction is imposed.

The resulting smooth selected cross reaches \(D^{3/4+\epsilon}\), with the same fixed-data and profile costs as SMOOTH_RADIAL_PARTNER-v1, for \(Nd\lesssim D^{1/6}\) or, more generally, \(e\le1/4\) with \(l_s\ge1/4+e/2\) at exponent level. It includes the proper smooth band \(T\asymp R\) on the actual good sixth-free frequencies. This is a research-only candidate pending independent review.

## 1. Keep the inverse ideal inside one cutoff norm

Write \(p=T/R\), and select \(\mathfrak v\mid\mathfrak k\), \(V=N\mathfrak v\). Use the exact second transform (2) and the two-variable log inversion (5) of SMOOTH_RADIAL_PARTNER-v1. Fix the separated Fourier parameters and other original labels, including the exact ordered allocation and common-prime projector. The \(\mathfrak v\)-phase is fixed raw. On an inverse-ideal dyad \(B\le N\mathfrak b<2B\), \(B\ge1\), the coefficient bound apart from the summable Fourier envelope and profile seminorm is
\[
 \frac pV(1+pB/V)^{-2}.
\]
The two cutoff arrays keep their exact lengths \(M_s,M_l\) and masks. In the original pairing, apply Cauchy between \(F_P\overline{B_s}\) and \(\overline{B_lB_{\mathfrak b}}\), where \(F_P\) is the actual equality dyad and \(B_{\mathfrak b}\) is the separated inverse-ideal sum. This Cauchy split is available since the inverse profile does not depend on the equality allocation. The shorter joint norm is unchanged and uses the same forced-radical labels \(h_0^2 b_s\).

The other norm groups the actual product \(b_l\mathfrak b\) of length \(O(M_l B)\). Its raw phase is \(\psi_u(b_l\mathfrak b)\), preserving all common-prime zeros. After extracting the displayed envelope, the coefficient is divisor bounded by the actual product multiplicity. Freeze its unique \(S\)-part and good sixth-power base and apply the physical sixth-free sieve to the residual. The shortened coefficient square mass is at most its physical length up to divisor factors. The fixed \(S\)-part and sixth-power row factors retain their original raw values, and the sums of their inverse square roots and inverse cubes converge, respectively. Thus the norm for this inverse dyad is at most
\[
 (DHB)^\epsilon \sqrt{M_l B}\,
 \Phi_6(A,L_l^\# B)^{1/2}\,
 \frac pV(1+pB/V)^{-2},
 \qquad L_l^\#=\max(1,L_l),
\]
times the uniform Fourier and profile factors. Bounded live subunit scales use direct counting, with \(M_l>1/14\).

For \(V/p\ge1\) the \(B\)-sum is bounded at \(B\asymp V/p\). Below it use monotonicity and the square-root mass in \(B\). Above it the sieve factor grows at most as \((B/(V/p))^{1/2}\), and the inverse weight gives decay of order \((B/(V/p))^{-2}\). The factor \(B^\epsilon\) is harmless there for small internal \(\epsilon\), and the scale \(V/p\) is polynomial in the application below. The bounded endpoint \(V/p<1\) is handled at unit scale. The resulting longer norm factor is
\[
 \sqrt{M_l}\left((p/V)\Phi_6(A,L_l^\# V/p)\right)^{1/2}.
 \tag{1}
\]
Constants at bounded subunit values are understood in (1). For \(p\le1\), the function \(\Phi_6(A,L x)/x\) is nonincreasing in \(x\ge1\) at fixed \(A,L\). Thus (1) is bounded by its value at \(p=1\). The same comparison with a fixed constant holds for \(p>1\) bounded.

## 2. Sum the exact sixth-free projector

Let \(c_6(\mathfrak k)\) be the good ideal whose prime valuations are the floors of the good frequency valuations divided by six. The exact selector is
\[
 \mathbf1_{c_6(\mathfrak k)=1}
   =\sum_{\mathfrak q^6\mid\mathfrak k,\ (\mathfrak q,S)=1}
                  \mu(\mathfrak q).
\]
Cut the sum at \(N\mathfrak q\le D^{1/16}\). For each such \(\mathfrak q\), take \(\mathfrak v=\mathfrak q^6\) in (1). Then \(V\le D^{3/8}\). If \(v=\log_D V\) and \(l=\log_D L_l^\#\), convexity of the physical exponent \(\Delta_6\) and \(l\le1/2\) up to scale constants give
\[
 \Delta_6(l+v)-\Delta_6(l)
 \le \Delta_6(1/2+v)-\Delta_6(1/2)
 =\begin{cases}
 v/3,&0\le v\le1/4,\\
 5v/6-1/8,&1/4\le v\le3/8.
 \end{cases}
 \le v/2.
\]
Accordingly the new longer norm in (1) is at most \(O(V^{-1/4})\) times the ordinary longer cutoff norm bound. The shorter forced-radical moment is unchanged. Absolute summation of this gain uses \(\sum_{\mathfrak q}(N\mathfrak q)^{-3/2}<\infty\). It preserves the same exponent relative to \(R/E\) as the full smooth calculation.

The truncated projector is kept as one coefficient when applying the separately selected original middle compensation. It has modulus at most \(\tau(c_6(\mathfrak k))\), bounded by a subpower on the smooth band. Thus the original exact middle count gives the same \(R/E\) cost, without a separate copy of that cost for each \(\mathfrak q\). The remainder of the full projector vanishes unless \(Nc_6(\mathfrak k)>D^{1/16}\), and it is again divisor bounded. The accepted large sixth-power-base estimate of FREQUENCY_RATIONAL_CONTENT-v2 applies to this remainder, including its exact middle subtraction. Normalize the remainder weight by its subpower supremum before using that estimate. Each arithmetic sign and the original \(\mu(d)\) is retained in the exact decomposition before absolute comparison.

This addresses the good sixth-free slice of the smooth main band, including small or unit good sixth-power part, with no loss from summing the truncated projector. It does not select low rational content, allow an arbitrary sharp mode weight at the main scale, or extend to equality-dependent \(\sigma\).

