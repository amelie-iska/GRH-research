# A high-divisor and thin-product refinement for the full unit-pair correction

8 November 2026 UTC. Keep the exact full-frequency partner selection of UNIT_PAIR_FULL_FREQUENCY-v1, with optional ordered divisor-pair selection depending only on \((d,m,n)\). Keep all original rows, fixed data, exact primitive phases, raw masks, and the one common complex profile. Take the pure critical scales \(A_1\asymp R\asymp D^{3/4}\), \(A_2\asymp1\). Write \(E=Nd\), \(d=mn\), \(L_1=U/Nm\), \(L_2=U/Nn\), and \(\Omega=E N\zeta_1N\zeta_2/U^2\). Both lower cutoffs \(N\zeta_i>L_i\) are strict. The full partner frequency sum and its original equality compensation are retained in every result.

## 1. The sharper pointwise equality factor

In the proof of (2) of UNIT_PAIR_FULL_FREQUENCY-v1, the \(h\)-sum with \(T=(D/(E E_1R))^{1/2}\) is \(O(\min(1,T^{-1}))\). The bound by one gives \(O(D/(E E_1\sqrt R))\) at fixed \(e_1\), and the second choice gives \(O(\sqrt{D/E}E_1^{-1/2})\). Both \(e_1\)-sums have divisor cost. Retain the smaller of the two inequalities:
\[
 \|E_d\|_\infty
   \ll (DH)^\epsilon\mathcal M_{12}(W)
       \min\{\sqrt{D/E},D/(E\sqrt R)\}.
\]
This uses the same exact grouped equality formula and actual primitive factors. In the two-array bound (3) it retains the extra factor
\[
 \min\{1,\sqrt{D/(ER)}\}.
\]
No partner masks change. The separate equality compensation is still \(O((DH)^\epsilon\mathcal M_{24}(W)^2R/E)\).

For \(e=\log_D E\ge1/4\), write \(l_i=\log_D \max(1,L_i)\). On nonempty support \(l_1+l_2=1-e\) up to fixed scale constants, and \(0\le l_i\le1/2\). At most one sieve excess \(\Delta(l_i)=\max(0,l_i/3-1/8)\) is positive at exponent level. Thus after the extra equality factor, the geometric mean has no power loss whenever
\[
 e\ \ge\ \frac14+\frac{(\max(l_1,l_2)-3/8)_+}{3}.
\]
In particular \(E\gtrsim D^{7/24}\) gives target size for every ordered pair \(m,n\), including the unbalanced pairs. Sum harmonically over the actual intermediate divisors. This statement is on the full partner frequency correction, which may contain terms outside earlier comparable insertion and erasure dyads.

## 2. Thin product near the true wide boundary

Consider the original unit-pair coefficient with the additional selector \(1<\Omega\le1+\eta\), where \(0<\eta\le1\). This depends on the partner cutoff labels and \(d\), independently of partner frequency. The primal unit reduction is unchanged. Each factor now lies in \((L_i,(1+\eta)L_i]\) because both ratios exceed one. Restrict each array to this independent interval and retain the actual upper product inequality.

Use the original common-prime projector in the exact form \(w\mid(\zeta_1,\zeta_2)\), where \(w\) is good squarefree and \((w,d)=1\) before stripping. These conditions are inherited from the original two cutoff ideals. Set \(\zeta_i=w b_i\), with each squarefree residual \(b_i\) avoiding \(w,d\). Keep \(\mu(w)\), the raw \(\psi_u(w)^2\), the two residual Möbius signs, and all fixed row factors. The joint upper inequality now compares the integer \(Nb_1Nb_2\) with \(U^2(1+\eta)/(E(Nw)^2)\). For fixed \(d,w\), take the last allowed integer on the candidate product range and the next integer. Put the transition at their midpoint, with support for the transition strictly between those integers. On the log scale the gap is bounded below by a fixed inverse power of \(D\), as all candidate products are positive integers of polynomial size. The weak upper endpoint is then exact even if the threshold is an integer. If the threshold allows all candidates, discard the constant projector. If it allows none or an array is empty, the cell contributes zero.

Use a smooth compact log step on a log interval of length \(O(\log(2D))\) containing the candidate products. Its first derivative has bounded absolute integral and the second derivative has absolute integral \(O(D^C)\) for a fixed \(C\), by taking transitions in the indicated gaps. Fourier splitting at frequencies \(1,D^C\), with zero, one and two integrations by parts respectively, gives absolute Fourier mass \(O(\log(2D))\). This yields the exact joint selector as separate norm twists. The exact Mellin separation of the common \(W\) is unchanged. Both transforms are independent of the row, and all fixed raw factors stay in the paired expression.

Write \(M_i=L_i/Nw\) for the actual shortened lengths and \(l'_i=\log_D\max(1,M_i)\). A nonempty shortened array has \(M_i\ge1/(1+\eta)\). Its integer norm support has size \(O(1+\eta M_i)\), with divisor-bounded distinct ideal fibres. Hence its squared positive coefficient mass is at most \(O((DH)^\epsilon M_i\min(1,\eta+M_i^{-1}))\). Apply the physical sieve at the true shortened lengths \(\max(1,M_i)\), with the direct unit convention. The calculation leading to (3), before summing \(w\), now uses the same factor \(1/Nw\), the sharpened equality factor from section 1, and the two shortened sieve losses multiplied by
\[
 \sqrt{\min(1,\eta+M_1^{-1})\min(1,\eta+M_2^{-1})}.
\]
No selection of a row by norm and no merging of conjugate ideals is involved. The separate equality compensation with the thin selector still has divisor-bounded coefficients and costs \(O((DH)^\epsilon\mathcal M_{24}(W)^2R/E)\).

For \(\eta=D^{-1/24}\), any shortened array with positive sieve excess has \(M_i\gtrsim D^{3/8}\) and squared loss at most \(D^{1/24}\). Its own thin mass pays the full loss, while a shorter array can use the ordinary full mass. This gives target size on the thin product strip for all \(d\) after the harmonic \(w\)- and \(d\)-sums.

For \(E\gtrsim D^{1/8}\), the strip can be widened to \(\eta=D^{-1/48}\). It suffices to handle \(1/8\le e\le7/24\), since section 1 covers larger \(e\). At any common shortening, the lengths satisfy
\[
 l'_1+l'_2\le 7/8+O(1/\log D),\qquad |l'_1-l'_2|\le e.
\]
The first follows from the original product \(L_1L_2=U^2/E\), the shortening, and the bounded-scale convention on nonempty arrays. The second follows from \(L_1/L_2=Nn/Nm\) and the fact that truncation of a log length at zero does not increase differences. If either shortened array has positive excess, the other length has exponent at least \(3/8-7/24=1/12\), up to fixed constants. Both thin masses therefore give a square-root factor \(O(D^{-1/96})\). The sum of the two sieve excesses is at most \(1/24\), by the same two cases as the \(37/48\) estimate of UNIT_PAIR_FULL_FREQUENCY-v1. The product of the two thin gains pays their geometric-mean loss. If neither excess is positive, ordinary full masses suffice. Thus this wider strip also reaches \(D^{3/4+\epsilon}\) on the stated divisor range.

## 3. The limitation of replacing the shorter moment by its count

For \(e\le1/4\), (3) of GROUPED_EQUAL_CROSS-v4 gives \(D^{-1}\|E_d\|_2^2\ll(DH)^\epsilon\mathcal M_{24}(W)^2D^{5/8}E^{-1/2}\) at pure scales. Its bound for \(\|E_d\|_2\) has gain exponent \((1/4-e)/4\) against \(\sqrt R\) times the pointwise \(\sqrt{D/E}\) budget. Attempting to use this equality energy, the longer cutoff second moment and the literal count bound on the shorter cutoff instead of both cutoff second moments gives a relative cost exponent
\[
 \frac{l'_s-\Delta(l'_s)}2-\frac{1/4-e}{4},
 \qquad l'_s=\min(l'_1,l'_2).
\]
The first term is the replacement of the short second moment by its pointwise count. On any cell with positive sieve excess, \(l'_s\ge3/8-e\), since the longer length exceeds \(3/8\) and the difference is at most \(e\). Also \(\Delta(l'_s)\le l'_s/3\). The cost is therefore at least \((3/4-e)/12>0\) on these cells. For \(e>1/4\) the sharper pointwise budget already yields the \(D/E^2\) comparison for the equality energy after the row count. Thus that exchange does not lower the displayed bounds on the unbalanced wide cells. This is a comparison of upper estimates, not a lower bound on the signed cross.

The thin-product savings use the actual counts of distinct ideal norm fibres and both exact cutoff factors. Wide product intervals away from the thin strip, and the unbalanced cases outside the new high-divisor criterion, are still open at target power. These results do not apply after selecting particular partner defect modes.

