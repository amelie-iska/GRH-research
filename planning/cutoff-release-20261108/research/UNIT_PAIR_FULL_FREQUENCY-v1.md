# Full-frequency unit-pair wide correction

8 November 2026 UTC. Use the original equality-versus-complement cross, primitive \(Q_u\asymp R=A_1A_2\), unweighted literal two-pivot rows, fixed \(S,\nu,u_0\) and one common complex \(W\in C_c^\infty\) supported on \([1,2]\). Keep the full ordered \(U^2\) cutoff and \(U^2\le D\le7U^2/2\). Write \(E=Nd\) for a good squarefree intermediate divisor. This selects the partner's unit part of \(C_d\) from WIDE_CORRECTION-v1, with any row-independent selection of its ordered divisor pairs \(m,n\) at fixed \(d\). The full partner frequency complement is essential.

## Primal unit reduction

At fixed ordered good squarefree cutoff \(\zeta=\zeta_1\zeta_2\) and \(d=mn\), this unit part of the cutoff coefficient is
\[
 \mu(\zeta)\mu(d)\,
 \mathbf1_{\{Nm>U/N\zeta_1,\ Nn>U/N\zeta_2\}}.
\]
Keep both individual upper bounds \(N\zeta_i\le U\), the original squarefreeness and \((d,\zeta)=1\). The sum over permitted \(m,n\) and ordered splits is independent of partner frequency and divisor bounded. Let \(V_d^{\rm unit}\) be its contribution to the original primal amplitude and \(E_d^{\rm unit}\) its original middle equality projection. Their exact complement is \(V_d^{\rm unit}-E_d^{\rm unit}\), including the re-expressed direct component. The Poisson identity is linear in this coefficient.

The strict inequalities give \(E N\zeta>U^2\). Before squarefree and prime-deletion expansions, the unused ideal \(c\) is good squarefree and coprime to \(d\zeta\) and the row support. Its weight is \(W(E N\zeta Nc/D)\). Nonzero weight implies \(Nc<2D/(E N\zeta)<2D/U^2\le7\). Every good nonunit ideal has norm at least seven, so \(c=1\) exactly. This uses the original \(W\) and never restores a raw zero from a deletion expansion. The contribution of fixed \(m,n\) is
\[
 \begin{split}
 V_{d;m,n}^{\rm unit}(u)
  ={}&\mu(d)\mathbf1_{(d,u)=1}
    \sum_{\substack{\zeta_1,\zeta_2\ {\rm good\ squarefree}\\
        (\zeta_1,\zeta_2)=1,\ (d,\zeta_1\zeta_2)=1\\ L_i<N\zeta_i\le U}}
      \mu(\zeta_1)\mu(\zeta_2)\psi_u(\zeta_1)\psi_u(\zeta_2)
             W(E N\zeta_1N\zeta_2/D),\\
 &L_1=U/Nm,\qquad L_2=U/Nn .
 \end{split}                                                     \tag{1}
\]
The primitive values on good labels agree with the literal factors and include their zeros. Two conjugate or equal-norm ideal labels remain distinct, with their raw product in (1). On the profile support \(N\zeta_i<7L_i\), since \(L_1L_2=U^2/E\) and the other factor exceeds its own \(L_j\) strictly. If \(L_i<1/7\) the array is empty. Nonempty subunit lengths have bounded unit-scale support, counted directly with exact endpoints. Write \(L_i^\#=\max(1,L_i)\), comparable to \(L_i\) on nonempty support.

## Equality amplitude at each actual row

Use exact formula (2) of GROUPED_EQUAL_CROSS-v4. The primitive Gauss root has unit modulus, all raw factors have modulus at most one, and the grouped coefficient is divisor bounded on its polynomial support. With \(h=re_0\) and \(E_1=Ne_1\), the radial argument is comparable to \(D/(E E_1R(Nh)^2)\). Sum the original \(g,\ell\) against \(1/(NgN\ell)\) at logarithmic cost. Set \(T=(D/(E E_1R))^{1/2}\). Elementary ideal counting gives
\[
 \sum_h \frac{(1+T^2/(Nh)^2)^{-4}}{(Nh)^2}
      \ll\min(1,T^{-1}).
\]
For \(T\ge1\), split at \(Nh=T\) and use \(T^{-8}(Nh)^6\) below and \((Nh)^{-2}\) above. For \(T\le1\) use the convergent inverse square sum. Multiplication by \(D/(E E_1\sqrt R)\) gives \(O(\sqrt{D/E}\,E_1^{-1/2})\) in either case. The \(e_1\)-choices have divisor cost. Thus the original equality projection obeys the pointwise bound
\[
 \|E_d\|_\infty\ll (DH)^\epsilon\mathcal M_{12}(W)\sqrt{D/E}.      \tag{2}
\]
The proof uses no enlarged row weighting.

## Two exact partner arrays

In (1) expand the squarefree common-prime projector by \(\sum_{w\mid(\zeta_1,\zeta_2)}\mu(w)\) and put \(\zeta_i=w b_i\). The \(b_i\) stay good squarefree, avoid \(w\) and \(d\), and satisfy the shortened individual cutoffs. The two original Möbius signs factor exactly. Keep the raw multiplier \(\psi_u(w)^2\) and \(\mathbf1_{(d,u)=1}\). Insert the independent caps \(N\zeta_i<7L_i\) as above and Mellin-separate the common complex \(W(E(Nw)^2Nb_1Nb_2/D)\) exactly. Its logarithmic Fourier transform has bounded absolute integral in \(\mathcal M_{24}(W)\). At each frequency the separated norm twists have modulus one, and the remaining profile factor is row independent.

Fix the second pivot. The pinned physical sixth-order moment gives an \(\ell^2\) row norm bound for the \(i\)-th shortened array of
\[
 O\!\left((DH)^\epsilon\sqrt{(L_i/Nw)\Phi_6(A_1,L_i^\#)}\right),
 \quad \Phi_6(A,L)=A+L+A^{5/6}L^{1/3}+A^{1/3}L^{5/6}.
\]
The input acts on the actual squarefree ideal labels with their raw values and true shortened lengths. Nonempty shortened subunit lengths have \(L_i/Nw\ge1/7\) by the independent upper cap and give the same bound up to fixed constants by direct counting. Fixed row multipliers remain contractions in the positive norm.

Use (2) on the equality side and Cauchy on the two formed partner arrays. Their product gives \(\sqrt{L_1L_2}/Nw\) times the square root of the two sieve factors. The \(w\)-sum is harmonic and the \(v_2\)-sum costs \(O(A_2)\). As \(L_1L_2=U^2/E\), the scalar \(\sqrt{D/E}\sqrt{L_1L_2}/D\) is \(O(1/E)\). Consequently
\[
 D^{-1}|\langle E_d,V_{d;m,n}^{\rm unit}\rangle|
 \ll (DH)^\epsilon\mathcal M_{24}(W)^2
       \frac{A_2}{E}\sqrt{\Phi_6(A_1,L_1^\#)\Phi_6(A_1,L_2^\#)} .    \tag{3}
\]
The signs in (1) and the outer \(\mu(d)\) are kept before the comparisons. The sum over ordered \(m,n\) costs only a divisor factor at fixed \(d\).

The compensating equality term remains. The elementary equality estimate in GROUPED_EQUAL_CROSS-v4 uses only a divisor-bounded, row-independent coefficient at each allocation and therefore gives \(D^{-1}\|E_d\|_2^2,D^{-1}\|E_d^{\rm unit}\|_2^2\ll (DH)^\epsilon\mathcal M_{24}(W)^2R/E\). This includes any prescribed selection of \(m,n\) at fixed \(d\). Cauchy bounds its cross contribution by the same scalar \(R/E\) up to the common costs.

## Pure exponent consequences

Take \(A_1\asymp R\asymp D^{3/4}\), \(A_2\asymp1\). If \(Nm,Nn\gtrsim D^{1/8}\), then \(L_i^\#\ll D^{3/8}\), both sieve factors in (3) are \(O(A_1)\), and the harmonic divisor sum reaches \(D^{3/4+\epsilon}\).

In general let \(l_i=\log_D L_i^\#\). On nonempty support each \(0\le l_i\le1/2\) and \(l_1+l_2=1-\log_D E\), up to fixed scale constants. The sieve excess is \(\Delta(l_i)=\max(0,l_i/3-1/8)\) on this range. It is at most \(1/24\) on each side, so (3) summed harmonically over all \(d\) has power \(19/24\). If \(E\gtrsim D^{1/8}\), then \(l_1+l_2\le7/8\) up to the fixed constants. When both \(l_i\ge3/8\) their excesses sum to at most \((7/8-3/4)/3=1/24\). When one is below \(3/8\), its excess is zero and the other is at most \(1/24\). The geometric mean then costs \(D^{1/48}\) and the harmonic sum has power \(37/48\). All powers include \(D^\epsilon\) and the common profile costs. The equality compensation has target size throughout.

The unit primal reduction requires full partner frequencies. These estimates do not give the same bounds on the earlier selected dual defect modes. The unrestricted unit-pair sector at target power and the whole signed estimate remain open.

