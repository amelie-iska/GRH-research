# Three coherent arrays for selected low frequencies of the unit-pair correction

8 November 2026 UTC. Use the pure critical scales \(A=A_1\asymp R\asymp D^{3/4}\), \(A_2\asymp1\), and the original unweighted literal nonprincipal two-pivot rows, primitive \(Q_u\asymp R\), fixed \(S,\nu,u_0\), one common smooth complex \(W\) on \([1,2]\), and \(U^2\le D\le7U^2/2\). Keep the full ordered cutoff and all original ray, squarefree, capacity and raw-zero restrictions. Use the partner unit term of the exact wide factorization, with its original coefficient \(\mu(\zeta)\mu(d)\) for each ordered \(d=mn\) and \(\zeta=\zeta_1\zeta_2\) satisfying the strict lower cutoffs. The argument is for a frequency selection in the original Poisson representation, including the re-expressed direct component.

At fixed \(d,m,n,r,e_0,e_1,J\), and fixed allocation of \(e_0\) to the ordered cutoffs, one may multiply the partner frequency terms by a bounded row-independent function of \(\mathfrak k\), of modulus at most one. It can retain any selection of the ordered pairs \(m,n\) depending on \(d,m,n\) alone. It can retain the original frequency windows as they depend on these fixed labels. This function is independent of the two varying cutoff ideals and the varying equality labels. Restrict to \(N\mathfrak k\lesssim D^{19/44}\). After subtracting exactly the selected part of the original middle equality, the normalized selected cross with the original equality projection is \(O_{\epsilon,S,\nu,u_0}((DH)^\epsilon\mathcal M_{24}(W)^2D^{3/4})\) over all \(d\). On \(Nd\gtrsim D^{1/8}\) the same conclusion holds through \(N\mathfrak k\lesssim D^{83/176}\). On \(Nd\gtrsim D^{1/4}\) it holds through \(N\mathfrak k\lesssim D^{45/88}\).

These are bounds on low partner frequencies in the actual wide unit-pair term. The separate full-frequency primal-unit identity is unnecessary here. Coupled selections by the defect ideals or by varying equality labels need a different argument. Neither the main frequency scale near \(R\) nor the coherent signed sum over \(d\) is estimated by this low-frequency comparison.

## Exact allocation and the live bounds

Write \(E=Nd,\ E_1=Ne_1,\ h=re_0\), \(L_1=U/Nm,\ L_2=U/Nn\), so \(L_1L_2=U^2/E\). The unit-pair selector gives \(L_i<N\zeta_i\le U\), \((\zeta_1,\zeta_2)=1\), \((d,\zeta)=1\), and \(EN\zeta>U^2\). Put \(\zeta=e_0z_0\). On the original live primal dyad one has
\[
 D/(EE_1(Nh)^2)>Nz_0/4,\qquad
 \Omega=EN\zeta/U^2<14/(E_1Nh).
\]
Indeed the first inequality is the unchanged dyadic primal-zero test. Multiply by \(Ne_0/U^2\) and use \(Ne_0\le Nh,\ D/U^2\le7/2\) for the second. In particular the varying cutoff ideals satisfy \(N\zeta_i<14L_i\) independently, because the other factor strictly exceeds its own lower cutoff. The number 14 here uses the live dyad, so it also covers individual cutoff nodes with zero primal profile. The sharper primal support cap \(7L_i\) need not hold on the selected frequencies.

Consequently \(E_1Nh<14\), and the number of \(r,e_0,e_1\) choices is bounded independently of \(D\) after all their actual selectors. Define
\[
 L=\frac{D}{EE_1(Nh)^2Nz_0},\qquad
 \frac14<L<\frac{(7/2)Ne_0}{E_1(Nh)^2}\le\frac72 .
\]
The upper bound follows from \(EN\zeta>U^2\), the lower from the live dyad. The exact partner Poisson factor is
\[
 \frac{2L\gamma_u}{\sqrt3\sqrt{Q_u}}\,
 \psi_u(h)^2\psi_u(e_1)\psi_u(z_0)
 \sum_{\mathfrak k\ \mathrm{nonzero\ integral}}
     \overline{\psi_u(\mathfrak k)}
                 G_W(LN\mathfrak k/Q_u),
\]
where the sum is over nonzero integral ideal frequencies, including the unit ideal, and the additive zero frequency is absent by nonprincipality. Keep the original \(\mu(e_1)\), the grouped \(\mu(h)\), the ordered unit-pair coefficient, and \(\mathbf1_{(d,u)=1}\). The grouped signs and phase agree with MATCHED_POISSON_CROSS-v2, including the original fixed \(S\)-values and every raw zero. Here the displayed frequency sum is intersected with the stated selection and its original windows. Each positive comparison below uses actual primitive \(Q_u\) in the profile and only bounds its outside factor by \(O(R^{-1/2})\).

## Three exact arrays in a cell

Fix the ordered allocation \(e_0=e_{0,1}e_{0,2}\), where \(e_{0,i}\mid\zeta_i\). Write \(\zeta_i=e_{0,i}a_i\). Each \(a_i\) is good squarefree, avoids \(d,r\) and the full fixed \(e_0\), and keeps all original individual bounds after shortening. There is no extra condition \((r,\mathfrak k)=1\). Expand \((a_1,a_2)=1\) by \(\sum_{w\mid(a_1,a_2)}\mu(w)\). The common divisor \(w\) itself is good squarefree and avoids \(d,r,e_0\) before stripping. Write \(a_i=w b_i\), with squarefree residuals avoiding \(w\) and all fixed forbidden primes. Retain the exact cutoff signs and \(\psi_u(w)^2\), including its raw zero. The original \(z_0\)-phase is the product of the two residual phases times \(\psi_u(w)^2\). No \(w\)-deletion is added on the frequency.

Put \(M_i=L_i/(Ne_{0,i}Nw)\). The independent bounds on the two arrays have \(M_i<Nb_i<14M_i\) and the original \(N\zeta_i\le U\). A nonempty subunit cell has \(M_i>1/14\) and is counted at constant scale. The original dyad \(J\le N\zeta<2J\) is an exact integer-product selector on \(Nb_1Nb_2\), with fixed multiplier \(Ne_0(Nw)^2\). On the polynomially clipped range it separates into individual log norm twists with polylogarithmic absolute Fourier mass. To justify this, insert a smooth compact log step equal to the indicator on integer norms. Transitions lie strictly in the gaps between consecutive candidate integers, with fixed inverse-polynomial log width. Its first derivative has bounded integral and its second derivative polynomial integral. Splitting the Fourier integral at frequencies one and a fixed power of \(D\) yields the polylogarithmic bound. The original strict and weak endpoints remain exact. Constant or empty selectors have the direct conventions.

At a frequency dyad \(T\le N\mathfrak k<2T\), the fixed-width log extension of \(G_W\) at argument scale \(T/R\) separates \(b_1,b_2,\mathfrak k,Q_u\), since \(L\asymp1\) on the live cell. Its absolute Fourier mass is \(O(\mathcal M_{12}(W)(1+T/R)^{-4})\). This follows from the original radial log derivative bounds and two integrations by parts. The physical inverse norms in \(L\) factor as bounded individual coefficients \(L_i/N\zeta_i\) times
\[
 \frac{D\,Ne_0}{EE_1(Nh)^2 L_1L_2}
       =\frac{D}{U^2}\frac{Ne_0}{E_1(Nh)^2}\ll1 .
\]
Thus, at each integrated phase and each fixed second pivot, the two cutoff arrays and the selected frequency array have bounded coefficients at their true lengths. Their orientations are \(\psi_u,\psi_u,\overline{\psi_u}\), respectively. The selected frequency may still meet \(S\), have repeated prime factors, or share primes with the cutoffs. The exact row factors retain their multiplicative zeros.

## Row pairing and the exponent budget

Use the equality supremum from UNIT_PAIR_SHARPENING-v1,
\[
 \|E_d\|_\infty\ll (DH)^\epsilon\mathcal M_{12}(W)
             \sqrt{D/E}\min(1,\sqrt{D/(ER)}).
\]
It follows from the actual grouped equality formula by the \(h\)-sum split, with its complete original equality support. Apply Hölder to the three formed partner arrays, with \(\ell^2\) on the longer cutoff and \(\ell^4\) on the shorter cutoff and the frequency. Write \(\Phi_6(A,V)=A+V+A^{5/6}V^{1/3}+A^{1/3}V^{5/6}\). The physical moment of the longer cutoff costs
\[
 \sqrt{M_l}\,\Phi_6(A,\max(1,M_l))^{1/2}.
\]
For a fourth moment at length \(V\), square the actual sum before the second moment. The product ideal has length \(O(V^2)\), with divisor-bounded coefficient. Its raw character is still sextic. For the frequency array the squared product can have arbitrary exponents and an \(S\)-part. Freeze the unique \(S\)-part and sixth-power part in the actual product, use the physical sieve on the good sixth-free residual, and sum the square-root shortening weights. They converge as in the all-ideal extension in DUAL_CUTOFF_PRODUCT-v1. Conjugation of the whole frequency array preserves its moment. Thus the fourth moment norms cost
\[
 \sqrt{M_s}\,\Phi_6(A,\max(1,M_s)^2)^{1/4},\qquad
 \sqrt T\,\Phi_6(A,T^2)^{1/4},
\]
up to the common subpowers. In particular the square of an ideal sum uses products of two distinct labels as well as the diagonal. Replacing this sixth-order moment by a cubic one would require an additional argument.

The product of physical cutoff masses is \(\sqrt{L_1L_2}/(\sqrt{Ne_0}Nw)\). The \(w\)-sum is harmonic, the second pivot sum costs \(O(A_2)\), and the frequency dyads and allocation labels have subpower cost. Including the factor \(1/\sqrt R\) from the Poisson scalar and dividing by \(D\), the normalized paired comparison on a live cell at fixed \(d\) is at most a subpower times
\[
 \frac{R}{E}
 \min(1,\sqrt{D/(ER)})\sqrt{T/R}\,(1+T/R)^{-4}\,
 \frac{\Phi_6(A,\max(1,M_l))^{1/2}
       \Phi_6(A,\max(1,M_s)^2)^{1/4}
       \Phi_6(A,T^2)^{1/4}}{A},
\]
with the common profile factor. The three-array comparison uses the actual row product inside Hölder. It does not replace the phase of a selected frequency by an independent row factor. Positive enlargements occur only after the signed products are formed.

Write \(t=\log_D T\) and \(l_i=\log_D\max(1,M_i)\), with \(l_s\le l_l\). Both \(l_i\le1/2\) up to fixed constants, and \(l_s+l_l\le 1-\log_D E+O(1/\log D)\). At the pure point put \(\Delta(v)=\max(0,v-3/4,v/3-1/8,5v/6-1/2)\). Ignoring the two nonincreasing profile factors, the exponent over \(R/E\) is at most
\[
 \frac t2-\frac38+
       \frac{\Delta(l_l)}2+\frac{\Delta(2l_s)}4
       +\frac{\Delta(2t)}4 .
\]
At \(l_i\le1/2\) the two cutoff losses together are at most \(5/48\). For \(3/8\le t\le19/44\), the upper exponent is \(11t/12-19/48\le0\). At smaller \(t\) it is bounded by monotonicity. For \(E\gtrsim D^{1/8}\), use the additional cap \(l_s+l_l\le7/8\) at exponent level. If \(l_s\le3/8\) the cutoff loss is at most \(5/96\). If \(3/8\le l_s\le7/16\), replace \(l_l\) by \(7/8-l_s\) inside the increasing positive bound. The resulting affine expression has slope \(1/4\), with maximum \(13/192\) at \(l_s=l_l=7/16\). The relative exponent for \(3/8\le t\le83/176\) is therefore at most \(11t/12-83/192\le0\), and smaller \(t\) again follows by monotonicity. For \(E\gtrsim D^{1/4}\), the cap \(l_s+l_l\le3/4\) bounds the cutoff loss by \(1/32\). If \(l_s\le1/4\), use the two independent upper lengths \(1/4,1/2\). If \(1/4\le l_s\le3/8\), replace \(l_l\) by \(3/4-l_s\); the two affine slopes cancel, giving the same constant \(1/32\). Thus the relative upper exponent is \(11t/12-15/32\le0\) through \(t=45/88\). This uses only the portion \(2t<3/2\), where the stated upper monomial of \(\Delta(2t)\) is active for \(t\ge3/8\).

## Exact equality subtraction and scope

The corresponding middle equality term keeps the original tests \(X'>B_*,\ K_0<N\mathfrak k\le MD^\eta\) and the original equality \(Nz_0=N\mathfrak k\). It has the same selected frequency weight evaluated at \(\mathfrak k\), without any equality constraint outside the middle window. The elementary equality count in GROUPED_EQUAL_CROSS-v4 bounds its energy by \(O((DH)^\epsilon\mathcal M_{24}(W)^2R/E)\). Indeed on the equality dyad the additional selector has modulus at most one, and the same count of \((g,\ell)\), actual radial scale, and divisor-bounded ordered cutoff coefficient apply. No square norm of a difference is used to cancel this term. Pair it with the original equality projection by Cauchy in the actual row norm and then sum \(d\) harmonically. Together with the three-array estimate, this proves the stated frequency selections. The full original outer \(\mu(d)\) remains in the signed identity until the absolute divisor comparison.

The wide-unit primal reduction for all frequencies cannot be applied to a proper mode selection. In this proof the original live dyad, fixed masks and middle equality subtraction are all retained explicitly. The high selected frequency range, coupled defect conditions, unrestricted wide correction, signed assembly and determinant comparisons remain open.
