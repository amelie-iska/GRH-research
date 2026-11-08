# Quadratic and cubic sieves on roots of dual denominators

8 November 2026 UTC. Author draft for independent review.

## The exact selected terms

Use the remaining original two-pivot window in DUAL_POWERFUL_DENOMINATOR-v2, including the deletion variables and all prior selectors. Keep one common smooth complex \(W\) supported on \([1,2]\), the original unweighted nonprincipal rows with fixed \(u_0,\nu,S\), and \(Q_u=N\mathfrak f_u\asymp R=A_1 A_2\). Let \(Z\le U^2\) be the cutoff-product cap. The full original coefficient uses \(Z=U^2\) and \(U^2\le D\le 7U^2/2\). The dyadic decomposition uses \(z=e_0z_0\), \(J'=J/E_0\), \(g=(z_0,k)\), \(z_0=g a\) and \(k=g b\). In the surviving middle window, \(X'>B_*\), \(K_0<Nk\le MD^\eta\), \(M=REJ/X<2R\). All roots and cutoffs below concern ideals. They preserve distinct labels with equal norms.

Fix \(m\in\{2,3\}\). Outside \(S\), divide the valuations of \(b\) by \(m\), with remainders in \(\{0,\ldots,m-1\}\). Write the resulting unique decomposition as
\[
 b=\mathfrak s f c^m,\qquad \mathfrak s\text{ supported on }S,\quad
 (fc,S)=1,\qquad f\text{ is }m\text{-free}.
\]
An overlap between \(f\) and \(c\) is allowed. Select \(Nf\le F_0,\ Na\le L,\ Nb\ge Y\), with \(F_0,L,Y\ge1\). The exact Poisson summand still contains
\[
 |\psi_u(g)|^2\psi_u(a)\overline{\psi_u(\mathfrak s f)}
             \overline{\psi_u(c)}^{\,m},\qquad
 G_W\!\left(\frac{X N(\mathfrak s f)(Nc)^m}{E E_0 Na Q_u}\right).
\]
The root \(\gamma_u\), \(Q_u^{-1/2}\), and all original row multipliers remain in the sum. In particular \(\overline{\psi_u(\mathfrak s f)}\) is a row factor, including its zeros. The cut \(Nb\ge Y\) and the upper middle endpoint use the actual powered norm.

For fixed \(g,\mathfrak s,f\) in each previous dyadic term, the conditions on \(a,c\) separate except for \((a,c)=1\). Indeed \(a\) is good and \((a,b)=1\) is exactly \((a,f)=1,\ (a,c)=1\). The first is an \(a\)-selector. To retain the earlier exclusions, partition the range of \(Na\) at the finitely many previous numerator thresholds, with their original endpoint choices. On each interval any previous rectangle or sparse-set exclusion becomes a condition on \(b=\mathfrak s f c^m\) and the fixed data. This uses \(O(1)\) cells, and allows an additional split between the \(m=2\) and \(m=3\) projections by excluding the earlier denominator conditions in the later projection.

## The two powered row inputs

Write
\[
 \Phi_6(A,B)=A+B+A^{5/6}B^{1/3}+A^{1/3}B^{5/6},\quad
 \Phi_3(A,B)=A+B+2(AB)^{2/3},\quad \Phi_2(A,B)=A+B.
\]
The \(a\)-sum uses the existing sixth-order fourth moment of JOINT_CUTOFF_PRODUCT-v1. The root sum uses the powered character \(\overline{\psi_u(c)}^m\) and the same fourth-moment argument with \(\Phi_{6/m}\), as follows.

Fix \(v_2\) in the literal row \(u=u_0\alpha_{v_1}\alpha_{v_2}^2\). On good \(c\) the fixed twist \(\overline{\nu(c)}^m\), the symbol of \(u_0\), and the \(v_2\) phase or zero are column multipliers. The variable \(v_1\)-factor is the conjugate \(6/m\)-th residue symbol of \(\alpha_{v_1}\). The equality also holds at a common prime, where the raw symbol and the primitive character on good ideals are zero. Conjugation preserves the squared operator norm by conjugating the coefficients.

For \(m=3\) the input on squarefree good \(v_1,c\) is the pinned quadratic comparison in papers/quadratic-pivot-details.tex, applying Goldmakher–Louvel, arXiv:1112.1642v2, Corollary 1.2, to the cubes of the sextic family. It includes the finite reciprocity partition of the literal symbol. For \(m=2\) use de Faveri, arXiv:2610.04045v1, Theorem 1.1 with \(n=3\) on cubefree good \(v_1,c\). Here \(K\) contains \(\mu_3\) and the same \(S\)-integer ring is principal. For the exact primary section repeat the generator argument of papers/physical-sieve-details.tex with \(m_E=\alpha_E\), modulus divisible by \(3\), and a third power \(\gamma^3\). The unit quotient \(\epsilon=\alpha_{v_1}/(x m_E\gamma^3)\) is \(\pm1\) modulo \(3\) because \((\mathcal O/(3))^\times\) has order six and its cubes are the residues of \(\pm1\). Injectivity on the six units then gives \(\epsilon=\pm1\), both cubes in \(K\). Thus the construction yields the primary cubic symbol at coprime ideals. The source's induced zero applies at common primes. In both inputs \(v_1\) remains its original squarefree physical ideal. All enlargements of the \(v_1\)-sum occur within a positive norm after the fixed data are absorbed into column coefficients.

For arbitrary good root ideals of norm \(O(V)\), let \(n=6/m\) and write each as \(c_0 j^n\) with \(c_0\) \(n\)-free. For fixed \(j\), the row multiplier \(\overline{\psi_u(j)}^{mn}=\overline{\psi_u(j)}^{6}\) has modulus at most one and retains its zeros and \(\nu\)-phase. The \(c_0\)-length is \(O(V/(Nj)^n)\). Sum over \(j\) by Minkowski with weight \((Nj)^{-n/2}\). This is summable for \(n=3\) and logarithmic for \(n=2\) by ideal counting. A live subunit length of bounded ratio to one uses the unit count. Summing the squared norms over the actual choices for \(v_2\) contributes \(O(A_2)\). Therefore the second moment of a powered root sum with bounded or divisor-bounded coefficients is at most
\[
 (DH)^\epsilon V A_2\,\Phi_n(A_1,\max(1,V)).
\]
For the fourth moment, square the root sum and combine coefficients on the ideal products. The number of factorizations of each ideal is divisor bounded, with no coprimality hypothesis, and the product length is \(O(V^2)\). Hence the fourth moment is at most
\((DH)^\epsilon V^2 A_2\Phi_n(A_1,\max(1,V^2))\).
All quantities used are bounded powers of \(D,H\) for fixed \(\eta\).

## Joint estimate

Let \(P=J'/C,\ T=K/C,\ y=K/M\) at \(C\le Ng<2C,\ K\le Nk<2K\), and let \(L_*=\min(L,Z)\). For fixed \(g,\mathfrak s,f\) set \(S_f=N(\mathfrak s f)\). The \(c\)-length is \(O((T/S_f)^{1/m})\). In the separated profile, the Fourier weight has mass \(O(\mathcal M_{12}(W)(1+y)^{-4})\) as in LOW_DUAL_CUTOFF-v1. The phases split between the \(a\)-sum, the \(c\)-sum, and the row factor. In particular the factor from the frequency is computed with \((Nc)^m\).

Use the exact expansion \({\bf1}_{(a,c)=1}=\sum_{q\mid a,\,q\mid c}\mu(q)\) and write \(a=q a',c=q c'\) in each term. The row multiplier is \(\mu(q)\psi_u(q)\overline{\psi_u(q)}^{\,m}\). It keeps a phase of power \(1-m\) on units as well as the zero. The required coprimalities of \(a\) with \(g,f\), and squarefreeness of \(a\), remain as selectors. There is no new exclusion of \(q\) from \(c'\). Hölder and the two fourth moments give the product of the \(a'\)- and \(c'\)-sums an upper bound
\[
 (DH)^\epsilon \frac{\sqrt{P A_2}\,(T/S_f)^{1/(2m)}}{Nq}
 \big[\Phi_6(A_1,\max(1,P^2))\Phi_n(A_1,\max(1,T^{2/m}))\big]^{1/4}.
\]
This uses \(Nq\) in the root length. Its contribution to the **physical** denominator norm is \((Nq)^m\). The \(q\)-sum is harmonic. Sum over the \(O(C)\) possible \(g\) and use \(C\sqrt{PT}=\sqrt{J'K}\). The previous Poisson prefactor and profile bound yield
\[
 (DH)^\epsilon \mathcal M_{12}(W)\frac{\sqrt{X A_2}}{E_0\sqrt{E_1}}\,
 S_f^{-1/(2m)}
 T^{-(1-1/m)/2}\sqrt y(1+y)^{-4}
 \big[\Phi_6(A_1,\max(1,P^2))\Phi_n(A_1,\max(1,T^{2/m}))\big]^{1/4}.
\]
The \(S\)-supported sum of \((N\mathfrak s)^{-1/(2m)}\) converges. The \(f\)-sum is at most \(O(F_0^{1-1/(2m)})\) by ideal counting and partial summation. Since \(P\le2L_*\), \(T>Y/2\), and \(\sqrt y(1+y)^{-4}\) is bounded, we obtain
\[
 \boxed{\displaystyle
 \frac{\|V_d^{(m)}\|_2^2}{D}
 \ll_{\epsilon,\eta}
 \frac{(DH)^\epsilon\mathcal M_{12}(W)^2 A_2}{Nd}
 F_0^{2-1/m}Y^{-(1-1/m)}
 \big[\Phi_6(A_1,L_*^2)\Phi_n(A_1,Y^{2/m})\big]^{1/2}.}
\]
In the last comparison \(T^{-(1-1/m)}\sqrt{\Phi_n(A_1,T^{2/m})}\) is nonincreasing for \(T\ge1\). Squaring it expands into monomials of degree at most zero since \(1/m\le1-1/m\). The range \(1/2<T<1\) costs only a bounded factor. The count of \(g,k,r,z\) dyads and the \(q,d,e_0\) harmonic weights are as in REDUCED_DUAL_WINDOW-v2. The \(e_1\)-choices cost a divisor bound and \(E_1^{-1/2}\le1\). The final estimate also holds after the positive sum over \(d\).

## Critical examples and scope

For \(H\asymp D^{3/4}, Z=U^2,\eta=1/16\), the following are powers of the normalized positive squared norm. Use the same prior critical thresholds.

| Block | \(m\) | \(F_0\) | \(L\) | \(Y\) | Power |
|---|---:|---:|---:|---:|---:|
| Mixed \(A_1\asymp D^{5/12}, A_2\asymp D^{1/6}\) | 3 | \(D^{1/100}\) | \(D^{3/5}\) | \(D^{3/8}\) | \(89/120\) |
| Mixed | 2 | \(D^{1/200}\) | \(D^{1/2}\) | \(D^{2/5}\) | \(2687/3600\) |
| Pure \(A_1\asymp D^{3/4}, A_2\asymp1\) | 3 | \(D^{1/100}\) | \(D^{2/3}\) | \(D^{1/2}\) | \(133/180\) |
| Pure | 2 | \(D^{1/100}\) | \(D^{21/40}\) | \(D^{1/2}\) | \(893/1200\) |

The mixed powers remain below \(3/4\) for the feasible \(1/2000\) pivot neighborhood. In particular, the cube estimate includes the sector with \(f=\mathfrak s=1\), squarefree \(c\), and \(Nb=(Nc)^3\ge Y\). Here \(b\) is sixth-free with \(v=1\), and its good sixth-free core is all of \(b\). This sector lies outside the earlier sparse sixth-power selectors. The square estimate includes the corresponding squarefree root sector with \(b=c^2\). Their actual Poisson coefficients and all earlier exclusions still apply.

The gain uses the powered support in the positive joint moment. For example the unconstrained mixed cube trial \(L=D,F_0=1,Y=D^{3/8}\) gives \(9/8\) in the displayed budget. The remaining amplitude includes large squarefree denominators with a large \(m\)-free remainder and large numerators. The signed cross and whole signed estimate remain open. The powered row inputs are pinned sieve applications, and independent review of this draft and its inherited window estimates is pending.
