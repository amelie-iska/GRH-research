# Higher equality moments in the full-frequency unit-pair cross

8 November 2026 UTC. Author derivation, independent review pending. Use the original full-frequency partner unit part of WIDE_CORRECTION-v1 in the exact form of UNIT_PAIR_FULL_FREQUENCY-v1 and UNIT_PAIR_SHARPENING-v1. Keep the original literal unweighted nonprincipal two-pivot rows, fixed \(S,\nu,u_0\), actual primitive \(Q_u\asymp R\), one smooth complex \(W\) supported on \([1,2]\), full ordered \(U^2\) cutoff, \(U^2\le D\le7U^2/2\), and every original ray, capacity, squarefree and raw mask. Work at the exact pure scales \(A=A_1\asymp R\asymp D^{3/4}\), \(A_2\asymp1\). An optional row-independent selector on \((d,m,n)\) may restrict the actual ordered factorizations \(d=mn\). It cannot impose a joint condition on the two cutoff arrays. The original full partner frequency sum, including the re-expressed direct part, is necessary. The exact original middle equality compensation remains separate.

The normalized selected full-frequency unit-pair cross is \(O(D^{37/48+\epsilon})\) over all \(d\) and all ordered pairs, with the inherited profile and fixed-data cost. This improves the unrestricted \(19/24\) in UNIT_PAIR_FULL_FREQUENCY-v1. It does not restrict the product to a thin interval. Further, for each fixed integer \(j\ge6\), it reaches \(D^{3/4+\epsilon}\) on the actual scales
\[
 Nd\asymp D^{e_j},\qquad e_j=\tfrac14-\frac{3}{4j},\qquad
 L_s\asymp D^{3/8},\qquad L_l\asymp D^{3/8+3/(4j)},
 \tag{1}
\]
where \(L_i=U/Nm_i\) for \(m_1=m,\ m_2=n\), and \(L_s,L_l\) are the shorter and longer lengths in that order. Here the constants depend on the fixed moment index \(j\); no uniformity for growing \(j\) is asserted. For example \(j=8\) allows \(Nd\asymp D^{5/32}\) with the two ordered divisor norms of scales \(D^{1/8}\) and \(D^{1/32}\), in either orientation. These target sectors retain the complete wide product range and need neither the thin selector nor the previous high-divisor threshold.

## Actual normalized equality moments

Write \(E=Nd,\ e=\log_D E,\ a=3/4\), and let \(\mathcal E_d\) be the entire original equal-norm middle projection. For a row vector use the normalized counting norm
\[
 [F]_p=R^{-1/p}\|F\|_{\ell^p},\qquad [F]_\infty=\|F\|_\infty .
\]
This normalization uses the physical row scale, not a new weighting. Denote
\(\Phi_3(A,L)=A+L+2(AL)^{2/3}\), the pinned cubic physical comparison used in POWERED_DUAL_ROOT-v1 and PURE_EQUAL_ALLOCATED-v1. At length \(D^x\), its excess above \(A\) has exponent
\[
 \Delta_3(x)=\max(0,x-a,2x/3-a/3).
\]
For every fixed integer \(j\ge2\) we prove
\begin{equation}\tag{2}
 [\mathcal E_d]_{2j}
 \ll_{\epsilon,j}(DH)^\epsilon\mathcal M_{12}(W)
     \sqrt{D/E}\,D^{-\tau/2+\Delta_3(j\tau)/(2j)},
 \qquad \tau=\tfrac12(\tfrac14-e),\quad e\le\tfrac14 .
\end{equation}
Fixed comparability constants in the displayed physical scales are allowed.

Use exact equation (2) of GROUPED_EQUAL_CROSS-v4. At fixed \(e_1,g,\ell\) and \(T\le Nh<2T\), the row sum in \(h=re_0\) has raw phase \(\psi_u(h)^2\). Its coefficient is the actual divisor-bounded sum over the \(e_0\)-allocations, including every original \(J\), cutoff, primal and middle test. The factors at \(g,\ell,e_1,d\), and the primitive Gauss root and actual \(Q_u\), remain in their original places. Freeze \(v_2\). The fixed \(\nu,u_0,v_2\) contributions on \(h\) are coefficients, with all zeros. The variable first pivot acts through the order-three symbol. Use exact compact log Fourier separation of the radial profile on \(Nh\asymp T\). Its absolute Fourier mass is bounded by \(O(\mathcal M_{12}(W)(1+(T_1/T)^2)^{-4})\), with \(T_1=\sqrt{D/(E E_1 R)}\) and \(E_1=Ne_1\). This is a bound after retaining the actual \(Q_u\) in the inversion. The normalized \(T^2/(Nh)^2\) stays in the coefficients, as does the bounded norm twist at each Fourier frequency.

For the \(2j\)-th moment, raise the actual signed \(h\)-sum to its \(j\)-th power and group by the product ideal \(b\). This is exact by raw multiplicativity. The coefficient at \(b\) is divisor bounded for fixed \(j\); its product length is \(O_j(T^j)\). Split the good product uniquely as \(b=b_0 q^3\) with \(b_0\) cubefree. Freeze \(q\), keeping the exact fixed row multiplier \(\psi_u(q)^6\), including its zeros and any fixed twist. In particular dropping the exponent-three part from the cubic residue symbol does not restore a raw zero or remove its fixed phase. At fixed \(q\), the residual mass bound is \(O((DH)^\epsilon T^j/(Nq)^3)\) on its actual length. The pinned cubic comparison applies to \(b_0\). Use the triangle in the positive row norm over \(q\), with convergent weight \((Nq)^{-3/2}\), and count a live bounded subunit residual directly. Taking the \(j\)-th root gives normalized \(2j\)-moment
\[
 O_{\epsilon,j}\!\left((DH)^\epsilon
       \sqrt T\,(\Phi_3(A,\max(1,T^j))/A)^{1/(2j)}\right)
\]
for the \(h\)-sum. The normalization is justified at fixed \(v_2\) by \(A\asymp R\) and then by the bounded second-pivot count. There is no change to the row family. This extends the same grouped-product moment argument as the cubic sixth moment in PURE_EQUAL_ALLOCATED-v1, without a new sieve input.

Multiplying by the original radial scale and \(1/(Nh)^2\), the fixed-\(e_1,g,\ell,T\) contribution to the normalized norm is bounded by the profile cost times
\[
 \frac{D}{E E_1 Ng\,N\ell\,\sqrt R}\,
 T^{-3/2}(1+(T_1/T)^2)^{-4}
 \left(\frac{\Phi_3(A,\max(1,T^j))}{A}\right)^{1/(2j)}.
\]
If \(T_1\ge1\), the \(T\)-factor is largest up to constants at \(T_1\). Below \(T_1\) use monotonicity of the sieve and the eighth power of \(T/T_1\). Above it the sieve factor in parentheses to the stated power grows at most as \((T/T_1)^{1/2}\). Summing dyads costs at most a subpower. Put \(T_0=\sqrt{D/(ER)}\), which is at least constant scale for \(e\le1/4\). Since \(T_1=T_0/\sqrt{E_1}\), the resulting \(E_1\) factor is \(E_1^{-1/4}\), and the sieve argument is at most that at \(\max(1,T_0^j)\). If \(T_1<1\), use the unit-scale maximum instead. When \(T_0\ge1\) its prefactor relative to the bound at \(T_0\) is at most \(T_0^{3/2}/E_1\le1\); the bounded endpoints change only constants. The \(e_1\)-choices cost a divisor factor. The \(g,\ell\) norm counts are harmonic on their original polynomial support. This proves (2), since
\[
 \frac{D}{E\sqrt R}T_0^{-3/2}
       =\sqrt{D/E}\,T_0^{-1/2}.
\]
It is a positive upper bound on the actual equality vector and uses neither a restriction on \(\ell\) nor an independence assumption on its raw phases.

## Interpolation on the two cutoff arrays

For each fixed actual \(d=mn\), use the exact primal reduction \(c=1\) in UNIT_PAIR_FULL_FREQUENCY-v1. The raw partner cutoff phases are \(\psi_u(\zeta_1)\psi_u(\zeta_2)\) with their two original Möbius signs and the common profile \(W(EN\zeta_1N\zeta_2/D)\). Preserve the individual \(L_i<N\zeta_i\le U\), the caps \(N\zeta_i<7L_i\) on nonzero support, and every original coprimality. Expand \(w\mid(\zeta_1,\zeta_2)\) with \(w\) good squarefree and \((w,d)=1\) before stripping. The residual arrays \(b_i=\zeta_i/w\) are squarefree and avoid \(w,d\). Keep the exact \(\mu(w)\), raw \(\psi_u(w)^2\) and all original fixed row factors. Mellin-separate the common \(W\) exactly as in that note, with the same bounded absolute Fourier mass and norm twists of modulus one. This gives the actual two formed arrays; no mixed cutoff condition has been discarded.

At fixed \(w\) and log Fourier parameter write \(S_i(u)\) for the \(i\)-th residual sum, with length \(M_i=L_i/Nw\) and divisor-bounded coefficients. A nonempty subunit \(M_i\) is at least \(1/7\), so its unit-scale bound is uniform. Write \(l_i=\log_D\max(1,L_i)\), and
\[
 \Delta_6(x)=\max(0,x-a,x/3-a/6,5x/6-2a/3).
\]
The physical order-six sieve and monotonicity in the column length give
\[
 [S_i]_2\ll (DH)^\epsilon\sqrt{M_i}\,D^{\Delta_6(l_i)/2}.
\]
Likewise square the residual sum and group by the product of its two squarefree good ideal labels. That product is sixth-free, with possible exponent two at common primes. Its length is \(O(L_i^2/(Nw)^2)\), and the coefficient is divisor bounded by the number of ordered factorizations. Its actual raw phase is the product of the two original symbols, also at common primes. The same order-six second moment on this product gives
\[
 [S_i]_4\ll (DH)^\epsilon\sqrt{M_i}\,D^{\Delta_6(2l_i)/4}.
\]
Both norm estimates act on the actual shortened labels. The exponents may be enlarged to their unshortened lengths, but \(\sqrt{M_i}\) still uses the exact shortening. These are positive estimates of the formed partner arrays with their exact phases.

Pair the equality \(2j\)-moment with the longer cutoff \(2\)-moment and the shorter cutoff \(p_j=2j/(j-1)\)-moment, using \(1/(2j)+1/2+1/p_j=1\). Interpolate the shorter moment between \(2\) and \(4\) with weight \(2/j\) on the latter, which is admissible for \(j\ge2\). Label its physical log length \(l_s\), and the longer one \(l_l\). Multiplication by the actual fixed row factors remains a contraction. The two physical mass factors give \(\sqrt{L_s L_l}/Nw=U/(\sqrt E Nw)\). Together with \(\sqrt{D/E}\) from (2), the normalized trilinear prefactor is \(O(R/(E Nw))\), after dividing by \(D\). The \(w\)-sum is harmonic and the number of actual ordered \(m,n\) at fixed \(d\) is divisor bounded. Thus at \(e\le1/4\) the relative power in the unit-primal cross above \(R/E\) is at most
\begin{equation}\tag{3}
 \rho_j=
 \frac{\Delta_6(l_l)+\Delta_6(l_s)}{2}
  +\frac{2}{j}\left(\frac{\Delta_6(2l_s)}4
                   -\frac{\Delta_6(l_s)}2\right)
  -\frac{\tau}{2}+\frac{\Delta_3(j\tau)}{2j}.
\end{equation}
The sign of the original \(\mu(d)\), and the two cutoff signs, are unchanged before the estimates. Every comparison includes \(O_{\epsilon,j}((DH)^\epsilon\mathcal M_{24}(W)^2)\), after combining the equality and partner profiles. The separate equality compensation is still \(O((DH)^\epsilon\mathcal M_{24}(W)^2R/E)\) by the elementary original projection norm. In particular it is not discarded when the rectangle comparison gains a power.

## All divisors and unbalanced target dyads

For \(e\le1/8\), the constraints \(l_1+l_2=1-e,\ l_i\le1/2\) imply \(3/8\le l_s\le l_l\le1/2\) at the level of powers, with all fixed endpoint constants retained. Take \(j=3\). Since \(3\tau\le3/8\), the cubic moment is in the diagonal range and \(\Delta_3(3\tau)=0\). On these cutoff lengths,
\[
 \Delta_6(l)=l/3-1/8,\qquad
 \Delta_6(2l)=5l/3-1/2 .
\]
The loss in (3) simplifies exactly to
\[
 \rho_3=\frac1{48}-\frac{l_l-l_s}{12}\le\frac1{48}.
\]
In particular the uniformly chosen shorter third moment pays no extra length comparison across this range. For \(e\ge1/8\) use the previously reviewed \(37/48\) branch of UNIT_PAIR_FULL_FREQUENCY-v1. Harmonic summation of \(R/E\) across the actual divisors gives the new unrestricted all-divisor \(37/48\), including the equality compensation. The stronger high-divisor and thin-product target sectors of UNIT_PAIR_SHARPENING-v1 still apply independently.

On the dyads (1), \(j\tau=3/8\), \(\Delta_3(j\tau)=0\), and \(l_s=3/8\) at the level of powers. In (3) the longer half-excess is \(1/(8j)\), the extra shorter interpolation cost is \(1/(16j)\), and the equality gain is \(3/(16j)\). Their sum is zero. Thus the full-frequency partner cross, with its original compensation, reaches \(D^{3/4+\epsilon}\) on these physical dyads. The selectors are only on \((d,m,n)\) and the derived physical lengths. They do not make a new thin restriction on \(W\), the cutoff products or the partner frequencies. For \(j=6\) one ordered divisor norm stays on constant scale and the other has scale \(D^{1/8}\). The exact strict lower cutoff still rules out a unit divisor on either side, even at this exponent endpoint. For \(j>6\) both norms grow and the exponent of the smaller one is \(1/8-3/(4j)\).

For comparison, using the equality second moment and both cutoff fourth moments on \(e\le1/8\) increases the relative loss by \(1/16\) compared with the original pointwise equality and two second moments: the two fourth-moment increments sum to \(1/8-e/4\), while the equality second-moment gain is \(1/16-e/4\). Thus that symmetric exchange does not produce the displayed improvement. It is the higher equality moment together with the shorter interpolated cutoff moment that gives (3). This is a statement about upper comparisons. It does not give a lower bound, solve the remaining unbalanced wide cells away from these dyads, or transfer any bound to the selected dual-mode sectors or whole signed form.
