# Strip the forced radical in the joint equality moment

9 November 2026 UTC. Author derivation pending independent review. Use the exact pure scales, original row family, profiles, masks and full-frequency partner unit-pair scope of POWERFUL_JOINT_MOMENT-v1 (SHA256 3bcb549ead75ae6ab78b3254d06a7d651eedd2369b50f089f63dca989a13ed9f). This note strengthens that comparison. In its §3 radial calculation the first bound \(\Psi(A,T^2M,T)^{1/2}\) can grow as \(T^{5/4}\), because \((2(4/3)-1/6)/2=5/4\). Its earlier \(13/12\) is a typo. The required strict inequality \(5/4<3/2\) still holds, so none of its exponent conclusions change. The stronger comparison below uses a different radial growth bound.

The original normalized full-frequency unit-pair cross reaches \(O((DH)^\epsilon\mathcal M_{24}(W)^2D^{3/4})\) on every intermediate divisor \(Nd\lesssim D^{1/6}\), including the balanced constant-nonunit-divisor edge and the full wide product support. More generally at \(e=\log_D Nd\le1/4\) it reaches target on the physical ordered cutoff selections with \(l_s\ge1/4+e/2\), where \(l_s=\log_D\max(1,L_s)\) and \(L_s=\min(U/Nm,U/Nn)\). Here and below fixed comparability constants in the scales are allowed. The original separate middle equality compensation is retained. Neither rational content, overlap nor product thinness is needed. The scope permits selectors on \((d,m,n)\) and the derived physical lengths, with \(d=mn\). It does not extend to a proper partner frequency selection or an arbitrary selector coupling both cutoff factors to the varying equality labels.

## 1. The forced radical in the pinned Poisson comparison

Continue with the proof of de Faveri, arXiv:2610.04045v1, Theorem 1.1, pinned PDF SHA256 97720b3cacccbedb9c2014520ad4d128ae23afd0a781bdeff27dab4e86b7c726, especially Lemma 5.1, equations (5.1)–(5.3) and the two positive Cauchy estimates after (5.3). Use the same \(n=6\) symbol and fixed data as the established physical application. Suppose now that an original good sixth-free column \(\mathfrak b\), of norm scale \(B\), has
\[
 N\operatorname{rad}(\mathfrak b^\sharp)\ge P,\qquad
 \mathfrak b^\sharp=\mathfrak b/\operatorname{rad}\mathfrak b.
\]
Then \(N\mathfrak b^\sharp\ge P\) also. If the outer common-ideal sorting of Lemma 4.4 removes \(\mathfrak d_g\) of norm \(F\), both thresholds hold on each residual at level \(P/F\). Indeed any prime lost from the radical of the sharp part must divide \(\mathfrak d_g\), and the product of those lost prime ideals has norm at most \(F\). For the sharp part itself use the exact identity (2) of POWERFUL_JOINT_MOMENT-v1. Keep \(B'\asymp B/F\) and \(A/(CF)\le A'\le CA\) after the outer deletion, with its original raw masks. Positive mass sums are the same as in Lemma 4.4.

In the proof of Lemma 5.1, at fixed sharp label \(\mathfrak s_i=(\mathfrak b'_i)^\sharp\) and fixed inner Möbius divisor \(\mathfrak r\) in (5.3), write the squarefree radical label as \(\mathfrak r\mathfrak u_i\). The original coefficient support contains the literal condition \(\mathfrak s_i\mid(\mathfrak r\mathfrak u_i)^\infty\). Equivalently \(\operatorname{rad}\mathfrak s_i\mid\mathfrak r\mathfrak u_i\). Put
\[
 \mathfrak q_i=\frac{\operatorname{rad}\mathfrak s_i}
                {(\operatorname{rad}\mathfrak s_i,\mathfrak r)},\qquad
 \mathfrak u_i=\mathfrak q_i\mathfrak v_i .
\]
This is an exact stripping on the existing coefficient support. Because \(\mathfrak r\mathfrak u_i\) is squarefree, \(\mathfrak v_i\) is squarefree and prime to \(\mathfrak q_i\mathfrak r\). The support and all ray restrictions remain in the coefficients. Keep the source's denominator \(N(\mathfrak r\mathfrak q_i\mathfrak v_i)^{1/2-\epsilon+it}\), the phases attached to \(\mathfrak s_i\), and the raw fixed column character \(\chi_{\mathfrak q_i}\) at the grouped row variable \(\mathfrak s_{3-i}\mathfrak a'\). Its literal factorization with \(\chi_{\mathfrak v_i}\) is the source's good-ideal multiplicativity, with the same zeros even when a row prime divides \(\mathfrak q_i\). After forming the positive second norm at fixed \(\mathfrak s_i,\mathfrak r\), this factor is a contraction. The new column label \(\mathfrak v_i\) is in bijection with \(\mathfrak u_i\) at those fixed labels. The source's positive coefficient mass sum, still with the original denominator, is unchanged.

Write \(P_i\asymp N\mathfrak s_i\), and let \(C_i\) be a dyadic scale for \(N\operatorname{rad}\mathfrak s_i\). Insert these latter dyads before the positive estimates at a logarithmic cost. Because \(N(\mathfrak r\mathfrak q_i)\ge N\operatorname{rad}\mathfrak s_i\), the second norm in the proof of Lemma 5.1 now has
\[
 K_i\lesssim \frac{(B')^2}{A'P_i},\qquad
 L_i\lesssim \frac{B'}{P_i C_i},\qquad P_i,C_i\gtrsim\max(1,P/F).
\]
Here \(L_i\) denotes the sieve scale in the source, separate from the later physical cutoff notation. The row cap is unchanged: it comes from the exact Poisson conductor shortening followed by grouping \(\mathfrak s_{3-i}\mathfrak a'\). A bounded nonempty subunit scale is counted directly. In particular the forced sharp part and its radical divide the physical column in product, so \(P_i C_i\lesssim B'\) on a nonempty original dyad. The primitive \(S\)-part of the frequency stays frozen and does not enlarge the cap.

Use the full upper bound
\[
 L_2(K,L)\ll_\epsilon (KL)^\epsilon
       (K+K^{1/6}L+K^{5/6}L^{1/3}+K^{1/3}L^{5/6}),
\]
obtained by inserting Theorem 1.1 into Lemma 6.1 and maximizing each of the four monomials separately over the sixth-power scale \(1\le q\lesssim K^{1/6}\). In the source prefactor rewrite \(A'\sqrt{P_1P_2}/B'\) as \(A'/B'\) times \(\sqrt{P_1}\sqrt{P_2}\). For each \(i\), the four monomials of \((A'/B')P_i L_2(K_i,L_i)\) are bounded, up to subpowers, by
\[
 B',\qquad
 (A')^{5/6}(B')^{1/3}P_i^{-1/6}C_i^{-1},\qquad
 (A')^{1/6}B'P_i^{-1/6}C_i^{-1/3},\qquad
 (A')^{2/3}(B')^{1/2}P_i^{-1/6}C_i^{-5/6}.
\]
The square roots of the two factors can each use the same upper bounds. Put \(G=\max(1,P/F)\), so the three inverse factors are bounded by \(G^{-7/6},G^{-1/2},G^{-1}\), respectively. In the first of those three terms the \(F\)-cost is \(F^{-1/3}G^{-7/6}\le P^{-1/3}\). In the second it is \(F^{-1}G^{-1/2}\le P^{-1/2}\). In the third it is \(F^{-1/2}G^{-1}\le P^{-1/2}\). These inequalities hold on both \(F\le P\) and \(F\ge P\), without fixing the outer common ideal or dropping it. Including the source's \(O(A')\) unit or diagonal term, the restricted sieve comparison is thus
\[
 \widetilde\Psi(A,B,P)
 = A+B
   +A^{5/6}B^{1/3}P^{-1/3}
   +A^{1/6}B P^{-1/2}
   +A^{2/3}B^{1/2}P^{-1/2} .
 \tag{1}
\]
It multiplies the original coefficient squared mass and the subpower factor. This strips a forced factor only inside the already positive source comparison. It makes no unconditional reciprocity or radical-conductor substitution for the original signed cross.

## 2. Actual joint labels and the sharpened low-divisor budget

Use precisely the joint norm of POWERFUL_JOINT_MOMENT-v1, keeping the actual conjugate partner in the signed pairing. Cauchy gives the norm of \(F_T\overline{B_s}\), whose modulus is pointwise that of \(F_T B_s\). At fixed \(w,e_1,g,\ell\) and profile variables, the resulting positive norm groups \(h^2 b_s\) injectively with the true physical length \(B\asymp T^2\max(1,L_s/Nw)\), square mass \(O((DH)^\epsilon T L_s/Nw)\), and \(N\operatorname{rad}((h^2 b_s)^\sharp)=Nh\ge T\). The equality \(h\) and cutoff \(b_s\) are squarefree, so the radical is exactly \(h\), even at a common prime. All fixed raw values, original zero factors, both strict cutoff inequalities, harmonic \(w,g,\ell\) and the separate original compensation remain as in that proof.

At fixed shortened cutoff length \(M\), \(\widetilde\Psi(A,T^2M,T)^{1/2}\) grows at most linearly with \(T\). Its five individual square-root growth powers are \(0,1,1/6,3/4,1/4\). This is dominated by the radial \(T^{-3/2}\) on the upper side of \(T_1\) and by the same radial decay on the lower side. Thus the argument in §3 of POWERFUL_JOINT_MOMENT-v1 applies with (1), still using the true shortened mass and taking the sieve length monotonically at the original \(L_s^\#=\max(1,L_s)\).

Set \(e=\log_D E\le1/4,\ \tau=(1/4-e)/2\) and \(l_s=\log_D L_s^\#,\ l_l=\log_D L_l^\#\) at the pure point. The normalized \(\widetilde\Psi/A\) has no excess from its \(B\) term since \(l_s+2\tau\le3/4\). The other three possible excesses are
\[
 l_s/3+\tau/3-1/8,\qquad
 l_s+3\tau/2-5/8,\qquad
 l_s/2+\tau/2-1/4.
\]
The first dominates the second by \(1/2-2l_s/3-7\tau/6\ge1/48\) and the third by \(1/8-l_s/6-\tau/6\ge1/48\), using \(l_s\le1/2,\ \tau\le1/8\). Pairing this joint second moment with the longer ordinary second moment yields the relative power above \(R/E\)
\[
 \begin{split}
 \widetilde\rho_{\rm J}
 &=\tfrac12(l_s/3+\tau/3-1/8)_+
       +\tfrac12(l_l/3-1/8)_+-\tau/2\\
 &=\frac16(1/4+e/2-l_s)_+ . 
 \end{split}
 \tag{2}
\]
Indeed \(l_l\ge3/8\), and \(l_s+l_l=1-e\) at the level of powers. If the shorter excess is active the two excesses cancel the equality factor exactly, and otherwise the remaining value is \((1/4+e/2-l_s)/6\). The middle equality compensation costs \(R/E\) independently of (2).

For all \(e\le1/6\), \(l_s\ge1/2-e\ge1/4+e/2\). Hence (2) yields target size with the original harmonic divisor and divisor-bounded ordered-factorization sums, as claimed. It also gives the longer stated selection up to \(e=1/4\). In particular the previous \(37/48\) barrier for separate moments on the balanced constant-divisor edge is bypassed by the joint positive norm and the forced radical in its Poisson comparison. At \(e=1/4,l_l=1/2,l_s=1/4\), the exact upper budget still allows \(1/48\) relative loss. No unconditional all-divisor improvement, selected-mode transfer, magnitude lower bound, whole signed estimate or determinant bridge follows.
