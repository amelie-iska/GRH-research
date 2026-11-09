# Higher equality moments with selected partner frequencies

9 November 2026 UTC. Keep the original unweighted nonprincipal pure two-pivot rows, \(A_1\asymp R\asymp D^{3/4}\), \(A_2\asymp1\), actual primitive \(Q_u\), fixed \(S,\nu,u_0\), one common complex \(W\) supported on \([1,2]\), and \(U^2\le D\le7U^2/2\). Use the original wide unit-pair correction with the precise row-independent selection of SELECTED_LOW_FREQUENCIES-v2: at fixed \(d,m,n,r,e_0,e_1,J\) and fixed ordered allocation of \(e_0\), the partner frequency selector depends on \(\mathfrak k\) and these labels only. Retain the actual primal-zero dyad, the direct component, full original masks, and the separate selected middle equality subtraction.

This comparison gives normalized target size \(O((DH)^\epsilon\mathcal M_{24}(W)^2 D^{3/4})\) for all intermediate divisors through \(N\mathfrak k\lesssim D^{9/20}\). It gives target through \(N\mathfrak k\lesssim D^{1/2}\) on \(Nd\gtrsim D^{1/8}\). In the smaller-divisor range the refined threshold at a fixed physical \(e=\log_D Nd\) is \(t\le9/20+e/5\). The two estimates concern the selected actual Poisson amplitudes. The full-frequency primal-unit reduction is not used.

## The paired moments

Use the three exact formed arrays, log-step separation, and radial separation of SELECTED_LOW_FREQUENCIES-v2, with the inherited live cap \(14L_i\), where \(L_1=U/Nm,\ L_2=U/Nn,\ d=mn\). In particular, the common-prime projector \(w\) is good squarefree and coprime to the fixed forbidden union before stripping. All raw \(w\) and primitive frequency factors are retained. Denote the cutoff arrays by \(F_1,F_2\), at shortened lengths \(M_i=L_i/(Ne_{0,i}Nw)\). The partner frequency array \(Z\) has actual integral ideal length \(T\), with \(t=\log_D T\). Its signs, powers, \(S\)-part and raw values are the ones in that note. The subunit, empty, and unit cells have the same direct conventions.

Write \([F]_p=R^{-1/p}\|F\|_{\ell^p}\). At fixed log Fourier parameters and second pivot, the positive norm bounds, up to subpowers, are
\[
 [F_i]_4\ll \sqrt{M_i}D^{\Delta_6(2l_i)/4},\quad
 [Z]_2\ll \sqrt T D^{\Delta_6(t)/2},\quad
 [Z]_4\ll \sqrt T D^{\Delta_6(2t)/4},\qquad
 l_i=\log_D\max(1,L_i),
\]
where \(\Delta_6(v)=\max(0,v-3/4,v/3-1/8,5v/6-1/2)\). These are the same moments as in SELECTED_LOW_FREQUENCIES-v2, used also with the other cutoff in the fourth moment. Both cutoff arrays are actually squarefree, so their squared products retain common-prime exponents up to two. For the arbitrary-ideal frequency second moment one freezes the \(S\)-part and the sixth-power part on the actual product input of degree one. The mass loss is at most \((Ns\,Nq^6)^{-1/2}\) per fixed part and is summable. The corresponding degree-two argument on the actual squared product proves the stated fourth moment. Both retain all raw phases and zeros. Exponents for the cutoff arrays were enlarged monotonically from \(M_i\) to \(L_i\); the mass still uses \(M_i\).

Put \(E=Nd\), \(e=\log_D E\) and \(\tau=(1/4-e)/2\) for \(e\le1/4\). Use the normalized equality \(2j\)-moment from (2) of HIGHER_EQUALITY_MOMENTS-v1 for a fixed integer \(j\ge2\):
\[
 [\mathcal E_d]_{2j}\ll (DH)^\epsilon \mathcal M_{12}(W)\sqrt{D/E}\,
 D^{-\tau/2+\Delta_3(j\tau)/(2j)},\qquad
 \Delta_3(v)=\max(0,v-3/4,2v/3-1/4).
\]
It is uniform over the fixed second pivots, since that proof establishes the bound first at fixed pivot. Use Hölder with exponents \(2j,4,4,p\) on \(\mathcal E_d,F_1,F_2,Z\), respectively, where \(1/p=1/2-1/(2j)\). Interpolate \(Z\) between \(2\) and \(4\) with weight \(2/j\) on \(4\). Fixed row multipliers are contractions in this positive comparison, with phases unchanged in the exact sum.

The mass factors give \(\sqrt{D/E}\sqrt{L_1L_2}/(\sqrt{Ne_0}Nw)\), whose normalized cost is \(O(1/(E Nw))\). The actual Poisson scalar contributes \(R^{-1/2}\), the frequency mass \(\sqrt T\), and converting the normalized row norms back to the row sum contributes \(R\). The total relative power over \(R/E\), after the harmonic \(w\)-sum, is at most
\[
 \rho_j(t,e)=\frac t2-\frac38+
  \frac{\Delta_6(2l_1)+\Delta_6(2l_2)}4
 +\left(\frac12-\frac1j\right)\Delta_6(t)
 +\frac{\Delta_6(2t)}{2j}-\frac{\tau}2+\frac{\Delta_3(j\tau)}{2j}.
 \tag{1}
\]
The unused radial factor \((1+T/R)^{-4}\) can be kept. The compensation is unchanged from the exact elementary selected equality comparison in SELECTED_LOW_FREQUENCIES-v2, of size \(R/E\) per divisor up to the same profile and subpower costs. There is no transfer of the higher moment to the selected compensation.

## Two useful ranges

Fixed constants in the scales below are absorbed in the common implied constants. When \(0\le e\le1/8\), use \(j=3\). Both original lengths satisfy \(3/8\le l_i\le1/2\) at exponent level since their sum is \(1-e\). On \(3/8\le t\le1/2\) one has \(\Delta_6(t)=t/3-1/8\), \(\Delta_6(2t)=5t/3-1/2\), and \(\Delta_3(3\tau)=0\). The sum of the two cutoff losses is \(1/6-5e/12\). Thus (1) simplifies to
\[
 \rho_3(t,e)=5t/6-3/8-e/6 .
\]
It is nonpositive through \(t=9/20+e/5\). For smaller \(t\) use monotonicity of the positive frequency costs.

For \(1/8\le e\le1/4\), use the single fixed index \(j=12\). At fixed sum \(l_1+l_2=1-e\) and \(l_i\le1/2\), convexity of \(\Delta_6(2l)\) bounds the sum of the two cutoff losses by its endpoint value at \(l_l=1/2,\ l_s=1/2-e\), namely \(13/96-e/6\). Evaluate (1) at \(t=1/2\). The result is
\[
 -1/32+1/96+e/12+\Delta_3(12\tau)/24.
\]
If \(e\le3/16\), then \(12\tau=6(1/4-e)\) lies between \(3/8\) and \(3/4\); the displayed exponent equals \(1/96-e/12\le0\). If \(e\ge3/16\), the cubic excess is zero and the exponent equals \(-1/48+e/12\le0\). Monotonicity covers every smaller frequency dyad. For \(e\ge1/4\), the inherited \(45/88>1/2\) threshold of SELECTED_LOW_FREQUENCIES-v2 suffices with the original equality supremum.

The allocation and frequency dyad sums have subpower cost, and the original divisor sum uses the harmonic \(R/E\) budget after taking absolute values. Every selector here satisfies the independence conditions stated at the start. The conclusion does not cover selectors that couple \(\mathfrak k\) to the varying cutoff or equality labels. The remaining selected frequencies near \(R\), unbalanced full-frequency wide core and whole signed form remain open.
