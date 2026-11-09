# A powerful-part sieve for the joint equality and shorter cutoff moment

9 November 2026 UTC. Author derivation pending independent review. Use the full-frequency partner unit term and original separate middle equality compensation of UNIT_PAIR_FULL_FREQUENCY-v1. Keep actual unweighted nonprincipal two-pivot rows at the pure scales \(A=A_1\asymp R\asymp D^{3/4}\), \(A_2\asymp1\), the exact \(Q_u\asymp R\), fixed \(S,\nu,u_0\), one common complex \(W\) supported on \([1,2]\), full ordered \(U^2\) cutoff and \(U^2\le D\le7U^2/2\). All original ray, capacity, squarefree, direct and raw-zero conditions stay in force. A row-independent selector on \((d,m,n)\) at \(d=mn\) is allowed.

For all \(Nd\lesssim D^{5/24}\), the resulting normalized selected cross is \(O((DH)^\epsilon\mathcal M_{24}(W)^2D^{73/96})\). This improves the previous \(37/48=74/96\) on that divisor range, including the balanced constant-nonunit-divisor edge and the low-content, small-overlap configurations in the full sum. On \(Nd\asymp D^e\) with \(0\le e\le1/8\), the relative power over \(R/Nd\) is at most \(1/96-e/24\) per divisor before the harmonic sum. No lower bound on content, overlap or cutoff-product width is used. A separate selector that couples the two varying cutoff factors to the varying equality label is not asserted. There is no unrestricted all-divisor improvement from this comparison alone.

## 1. Retaining the powerful-part dyads in the pinned physical sieve

Use de Faveri, arXiv:2610.04045v1, Theorem 1.1 and its proofs of Lemmas 4.3, 4.4, 5.1, 6.1. The existing pinned PDF has SHA256 97720b3cacccbedb9c2014520ad4d128ae23afd0a781bdeff27dab4e86b7c726. The scope and symbol convention are those of the established \(n=6\) physical application. For a good sixth-free column \(\mathfrak b\), put \(\mathfrak b^\flat=\operatorname{rad}\mathfrak b\) and \(\mathfrak b^\sharp=\mathfrak b/\mathfrak b^\flat\). Fix \(B,P\ge1\). Let the coefficients have support \(N\mathfrak b\asymp B,\ N\mathfrak b^\sharp\ge P\). The following support-sensitive comparison follows by retaining a parameter in the proof:
\[
 \sum_{A\le N\mathfrak a<2A}^{\text{original rows}}
       \left|\sum_{\mathfrak b}\lambda_{\mathfrak b}
                  \chi_{\mathfrak a}(\mathfrak b)\right|^2
 \ll_\epsilon (AB)^\epsilon
    \left[A+P^{-1/6}\bigl(A^{-1/6}B^{4/3}+A^{5/6}B^{1/3}\bigr)\right]
       \sum_{\mathfrak b}|\lambda_{\mathfrak b}|^2.                     \tag{1}
\]
One may also use the ordinary \(\Phi_6(A,B)\) comparison on the same coefficients. Neither \(B\) nor any raw mask has been replaced by the radical norm in (1).

Here is the proof of (1), using the notation \(L_1,L_2,L_3\) of that source. All fixed ray classes and fixed primitive bad-prime data in its reductions remain as in the original physical application. In the positive comparison, Lemma 4.3 completes the row sum, then the proof of Lemma 4.4 sorts the actual common ideal \(\mathfrak d_g\) of the two columns. Write \(F=N\mathfrak d_g\) and \(\mathfrak b_i=\mathfrak d_g\mathfrak b_i'\). The shortened column scale is \(B'\asymp B/F\). The original removed row primes in Lemma 4.4 use a divisor of the product of a fixed ideal and \(\mathfrak d_g\), so the row scale \(A'\) after stripping satisfies \(A/(C F)\le A'\le C A\). The residuals are sixth-free. Furthermore
\[
 N(\mathfrak b_i')^\sharp
 = \frac{N\mathfrak b_i^\sharp}{F}
    \frac{N\operatorname{rad}\mathfrak b_i}{N\operatorname{rad}\mathfrak b_i'}
 \ge \frac{P}{F}.                                                       \tag{2}
\]
This covers the case of partly removing a prime power. No new primitive values at a deleted prime are introduced. The shortened coefficient is the original coefficient at \(\mathfrak d_g\mathfrak b_i'\), multiplied by the source's fixed row-deletion character factor and exact support indicators. The final mass sum over those labels in Lemma 4.4 costs a divisor factor, since \(\mathfrak d_g\) divides each original label. It suffices to bound the shortened \(L_3\) with the support (2) before this mass sum.

In the proof of Lemma 5.1, equations (5.1) to (5.3) and the subsequent two Cauchy estimates keep dyadic norms \(P_i\) of \((\mathfrak b_i')^\sharp\) until the final supremum. Only dyads \(P_i\gtrsim P/F\) are live with these coefficients. This is true before all positive completions because each shortened coefficient vanishes outside (2). The displayed \(L_3\) comparison, at fixed such dyads, is the prefactor \(A'\sqrt{P_1P_2}/B'\) times the product of square roots of the two \(L_2(K_i,L_i)\) factors. Up to the source's subpower factors one has
\[
 K_i\lesssim \frac{(B')^2}{A'P_i},\qquad L_i\lesssim \frac{B'}{P_i}.
\]
The first cap is exactly the source's \(K\lesssim (B')^2/(A'P_1P_2)\) after grouping the opposite powerful part with the Poisson frequency. Its \(S\)-part remains frozen in that argument and can only reduce the frequency cap. Nonempty bounded endpoint lengths are counted directly. If the pre-grouping ideal-frequency range is empty there is no main term from that dyad. The source's unit or diagonal term is bounded by \(O(A')\), and its truncated errors are absorbed by that bound and subpowers.

By Lemma 6.1 and Theorem 1.1,
\[
 L_2(K,L)\ll_\epsilon (KL)^\epsilon(K^{7/6}+K^{1/6}L).
\]
Indeed in Lemma 6.1 put the sixth-power scale \(q\le O(K^{1/6})\). The four monomials of \(q\,\Phi_6(K/q^6,L)\) are bounded by constant multiples of \(K,\ K^{1/6}L,\ K^{5/6}L^{1/3},\ K^{1/3}L^{5/6}\). For each of the last two, splitting at \(L=K\) gives the stated bound. Hence both terms in the \(i\)-th \(L_2\) estimate have the same factor \(P_i^{-7/6}\). Multiplying and taking square roots gives
\[
 \frac{A'\sqrt{P_1P_2}}{B'}
   \sqrt{L_2(K_1,L_1)L_2(K_2,L_2)}
 \ll_\epsilon (AB)^\epsilon (P_1P_2)^{-1/12}
       \bigl((A')^{-1/6}(B')^{4/3}+(A')^{5/6}(B')^{1/3}\bigr).
\]
In particular the product gain is bounded above by \(O((P/F)^{-1/6})\), valid also when \(P/F<1\). Substituting \(A',B'\) leaves \(F^{-1}\) in the first term and \(F^{-1/6}\) in the second. Both are at most one. The positive mass sum of Lemma 4.4 now yields (1). In a bounded nonempty subunit dyad the scales can be replaced by one up to constants. The support-sensitive gain comes from the original conductor shortening and root phases in Lemma 5.1, rather than a new reciprocity assertion for reduced labels.

## 2. Group a genuine joint row norm

Write \(E=Nd\), \(L_1=U/Nm,\ L_2=U/Nn\), and label the shorter and longer \(L_s,L_l\) by a fixed tie convention. The actual full-frequency primal reduction gives the two partner arrays in UNIT_PAIR_FULL_FREQUENCY-v1. Their common ideal projector \(w\) is good squarefree and coprime to \(d\) before stripping. At fixed \(w\) their residual lengths are \(M_i=L_i/Nw\). Keep the exact \(\mu(w),\psi_u(w)^2,\mu(d)\mathbf1_{(d,u)=1}\), both cutoff signs, \(L_i<N\zeta_i\le U\), the independent caps \(N\zeta_i<7L_i\), and the residual deletions by \(d,w\). The Mellin separation of the actual \(W(EN\zeta_1N\zeta_2/D)\) uses only row-independent norm twists and the same bounded absolute Fourier mass.

On the equality side fix \(e_1,g,\ell\) and the original grouped \(h=re_0\) dyad \(T\le Nh<2T\), using equation (2) of GROUPED_EQUAL_CROSS-v4. Its coefficient is the original divisor-bounded, row-independent allocation count with all cutoffs and primal/middle tests. In this notation \(T_1=\sqrt{D/(EE_1R)}\), \(E_1=Ne_1\). The actual radial weight separates by the same compact log Fourier inversion as HIGHER_EQUALITY_MOMENTS-v1, with mass \(O(\mathcal M_{12}(W)(1+(T_1/T)^2)^{-4})\). Leave the primitive root, \(Q_u^{-1/2}\), the exact \(g,\ell,e_1,d\) phases and the log twist on \(Q_u\) as fixed row multipliers. Write the resulting equality character sum as \(F_T(u)=\sum_h c_h\psi_u(h)^2\) and the shorter and longer partner sums as \(B_s(u),B_l(u)\). Here the scale \(T^2/(Nh)^2\) is included in \(c_h\). At fixed literal second pivot, the exact paired product contains \(F_T(u)\overline{B_s(u)B_l(u)}\). Use Cauchy and the pointwise modulus identity
\[
 \|F_T\overline{B_s}\|_2=\|F_T B_s\|_2.
\]
This equality of positive norms does not change the phase of the paired product. Contractions from the fixed row factors can be applied after forming the product.

The \(F_T B_s\) sum now groups by the actual ideal \(\mathfrak b=h^2 b_s\), where \(h,b_s\) are both good squarefree. At each prime the exponent \(0,1,2,3\) encodes the two bits of membership in \(h,b_s\) uniquely. Thus no extra multiplicity arises in this grouping, even when the labels overlap. The raw value is exactly \(\psi_u(h)^2\psi_u(b_s)=\psi_u(h^2 b_s)\), including common-prime zeros. The true column length is \(B\asymp T^2\max(1,M_s)\), and
\[
 N\mathfrak b^\sharp=Nh\,N(h,b_s)\ge T.
\]
The coefficient square mass is \(O((DH)^\epsilon T M_s)\) by ideal counting, with bounded live subunit \(M_s>1/7\) counted directly. Fixed \(v_2,\nu,u_0\) column phases and zeros are still coefficients. Applying (1) gives joint norm at most
\[
 O((DH)^\epsilon\sqrt{TM_s}\,\Psi(A,T^2\max(1,M_s),T)^{1/2}),
 \qquad
 \Psi(A,B,P)=A+P^{-1/6}(A^{-1/6}B^{4/3}+A^{5/6}B^{1/3}).
\]
The longer norm is \(O((DH)^\epsilon\sqrt{M_l}\,\Phi_6(A,\max(1,M_l))^{1/2})\). This is a joint sieve on original physical product labels. In particular no signed original conjugate character was changed into a positive-power character inside the exact cross.

## 3. Radial and divisor budgets

In the joint estimate, the equality prefactor contributes \(D/(EE_1 Ng\,N\ell\sqrt R)\) and \(T^{-2}(1+(T_1/T)^2)^{-4}\). Multiplying the mass \(\sqrt T\) and summing \(T\) dyads amounts to using \(T_1\) up to constants when \(T_1\ge1\): the normalized \(\Psi^{1/2}\) grows at most as \(T^{13/12}\) with \(M_s\) fixed, whereas the remaining radial power for \(T\ge T_1\) is \(T^{-3/2}\). For \(T\le T_1\) the radial decay contributes \((T/T_1)^8\), and the normalized \(\Psi\) is increasing in \(T\). With \(T_0=\sqrt{D/(ER)}\), after using \(T_1=T_0/\sqrt{E_1}\) the prefactor is bounded by \(\sqrt{D/E}\,T_0^{-1/2}E_1^{-1/4}/(Ng\,N\ell)\), taking \(\Psi\) at the larger \(T_0\). If \(T_1<1\), use the unit-scale bound instead. For \(T_0\ge1\) its prefactor relative to the bound at \(T_0\) is at most \(T_0^{3/2}/E_1\le1\). Fixed comparability constants at \(T_0\asymp1\) are harmless. The original \(g,\ell\) sums are harmonic and \(e_1\) costs a divisor factor.

Keep \(\sqrt{M_sM_l}=U/(\sqrt E Nw)\) in the masses and enlarge only the sieve lengths monotonically from \(M_i\) to \(L_i^\#=\max(1,L_i)\). The \(w\)-sum is harmonic, \(A_2\asymp1\) and \(A\asymp R\), and dividing by \(D\) leaves \(R/E\) times the sieve excesses and \(T_0^{-1/2}\). More precisely write \(e=\log_D E\le1/4\), \(l_i=\log_D L_i^\#\), \(\tau=(1/4-e)/2\), and use \(A\asymp D^{3/4}\). The joint sieve length exponent \(x=l_s+2\tau\le3/4\). Of the two extra monomials in \(\Psi/A\), the second dominates the first at that length because the ratio of the first to the second is \(B/A\). Its excess exponent is \(l_s/3+\tau/2-1/8\). The longer usual sieve excess is \((l_l/3-1/8)_+\). The relative bound from this joint comparison is therefore
\[
 \rho_{\rm J}(e,l_s,l_l)=
     \tfrac12(l_s/3+\tau/2-1/8)_+
    +\tfrac12(l_l/3-1/8)_+-\tau/2.                                   \tag{3}
\]
The middle equality compensation remains \(O((DH)^\epsilon\mathcal M_{24}(W)^2R/E)\), separately for the same exact selected ordered \(m,n\) as in UNIT_PAIR_FULL_FREQUENCY-v1. Any negative exponent in (3) applies to the primal pairing only.

At exponent level \(l_s+l_l=1-e\), \(0\le l_s\le l_l\le1/2\), with the fixed constants in the original length scales absorbed. When both terms in positive parts in (3) are active, it gives \(1/96-e/24\). This always applies for \(e\le1/8\). At \(e\le1/4\) the longer length is at least \(3/8\). If the shorter term is inactive, the relative loss is at most \(1/48-\tau/2=-1/24+e/4\). Both comparisons are at most \(1/96\) through \(e=5/24\). Summing the original harmonic \(R/E\) and divisor-bounded ordered factorizations proves the claimed selected \(73/96\).

For completeness, the inherited sharpened equality pointwise estimate gives at most the same \(73/96\) when \(e\ge13/48\), since the smaller length is then at most \(3/8\) and the relative loss is bounded by \(1/48-(e-1/4)/2\). In the middle range, (3) below \(e=1/4\) and the inherited bound above it also give \(73/96\) whenever both ordered divisor norms are \(\gtrsim D^{1/16}\), equivalently \(l_l\le7/16\) at exponent level. Without this restriction, the branch with \(e\) near \(1/4\) and \(l_l\) near \(1/2\) still permits the old \(1/48\) excess. This is only an upper comparison. It does not establish an actual magnitude or resolve that remaining branch, a coupled equality-label selection, any proper frequency selection, the whole signed form or the determinant and zero-location obligations.
