# Signed common-ideal cancellation in the small-conjugate-support equality-wide term

9 November 2026 UTC. Use the exact pure two-pivot setting and equality-side wide projection of EQUALITY_WIDE_RATIONAL_MOMENT-v1. Keep the literal unweighted rows, fixed \(S,\nu,u_0\), \(Q_u\asymp R\asymp A_1\asymp D^{3/4}\), \(A_2\asymp1\), and one common complex \(W\). Write \(E=Nd\) for the intermediate squarefree divisor norm and \(T\le N\ell_{\rm g}<2T\) for the conjugate-good equality dyad in that note. This refinement concerns
\[
 D^{17/74}\lesssim E\lesssim D^{11/32},\qquad 1\le T\lesssim D^{1/8}.
\]
The proof uses the original equality projection and its \(C_d\) correction only, with all exact primal, cutoff and middle tests and the original raw zeros. It gives an explicit subpower gain in the equality moment. The companion may be the full original partner complement or its full-frequency step or wide part, each with its original middle compensation. No subset of partner dual modes is bounded by this transfer.

## 1. Open the actual wide coefficient on the equality side

On the equality side write \(z_0=g\ell,\ k=g\bar\ell,\ \zeta=e_0g\ell\) as in GROUPED_EQUAL_CROSS-v4, with \(h=re_0\), \(E_1=Ne_1\). Keep \(g\) good squarefree and coprime to \(\ell,h,d\). There is no imposed \((g,\bar\ell)=1\). In the good labels the actual raw factor is \(|\psi_u(g)|^2=\mathbf1_{(g,u)=1}\), since every good prime of the original literal row occurs in its primitive conductor. The fixed \(\nu\) contributes unit magnitude there. This identity preserves both original zeros and does not reduce a conductor on a new family.

Open the exact coefficient of WIDE_CORRECTION-v1. Fix the ordered pair \(d=mn\), at divisor cost, and take its unit contribution or one of its at most four actual small-prime subtractions. In the latter case keep \(p\mid m\) and the strict first-factor inequality. Fix the ordered split of \(e_0\), and use the actual splits \(\ell=\ell_1\ell_2\), \(g=g_1g_2\) within each ordered \(\zeta=\zeta_1\zeta_2\), so \(\zeta_i=e_{0,i}\ell_i g_i\). These are disjoint ideal products since \(\zeta\) is squarefree. The \(C_d\) unit cutoffs are \(N\zeta_1>U/Nm,\ N\zeta_2>U/Nn\), and the small-prime term replaces the first by \(N\zeta_1>UNp/Nm\). The original upper \(U\) on both factors remains. On the selected live support
\[
 1<\frac{E N\zeta}{U^2}<\frac{14}{E_1Nh}.
\]
Thus \(E_1Nh<14\), all \(h,e_0,e_1\) have bounded norm, and \(Ng_1Ng_2\asymp D/(E T)\). Here the finite factor \(\ell/\ell_{\rm g}\) was frozen and retained. Choose the larger of \(Ng_1,Ng_2\) by a deterministic index order on ties. Denote the chosen ideal by \(g_{\rm l}\) and the other by \(g_{\rm s}\), and let \(G\le Ng_{\rm l}<2G\) be its actual dyad. Up to fixed constants, \(G\gtrsim D^{17/64}\) throughout the stated \(E,T\) range.

Fix \(d,m,n,h,e_0,e_1,J\), the split of \(e_0\), the longer-factor index, \(G,g_{\rm s}\), and \(\ell/\ell_{\rm g}\). At a fixed \(\ell_{\rm g}\) and ordered split of \(\ell\), all remaining norm conditions on \(Ng_{\rm l}\) are intersections of exact intervals. The bounds on \(\zeta_i\) are individual upper and lower bounds. The \(J\)-membership uses \(N\zeta=Ne_0N\ell Ng_{\rm l}Ng_{\rm s}\); the original middle frequency tests use \(Nk=N\ell Ng_{\rm l}Ng_{\rm s}\) with the fixed original \(M\). The direct and primal-zero dyad tests at fixed labels retain their original values. The longer-factor tie rule adds one exact endpoint. The full good deletion set on \(g_{\rm l}\) apart from \(u\) is \(S\cup\operatorname{supp}(d h g_{\rm s}\ell)\), with its fixed factors. Neither the ideal labels nor the norm endpoints are identified with their conjugates.

## 2. Extract the row mask before using the signed sum

In this longer factor use the exact projector
\[
 \mathbf1_{(g_{\rm l},u)=1}=\sum_{q\mid(g_{\rm l},u)}\mu(q).
\]
Here \(q\) is good squarefree and obeys the full fixed deletion set before writing \(g_{\rm l}=q b\). Squarefreeness requires \((b,q)=1\); keep it. The cutoff sign \(\mu(\zeta)=\mu(e_0\ell g_{\rm s})\mu(g_{\rm l})\) combines with \(\mu(q)\) to leave \(\mu(e_0\ell g_{\rm s})\mu(b)\). The exact inverse-norm weight on \(g_{\rm l}\) is \((Nq\,Nb)^{-1}\). Thus the new row factor \(\mathbf1_{q\mid u}\) can be kept outside the \(\ell_{\rm g}\)-array, and the weighted sum in \(b\) is independent of the row. The original raw factor at \(g_{\rm s}\), the \(d\)-row mask, the \(h,e_1,\ell/\ell_{\rm g}\) phases and the primitive root stay in the row. The outer signed \(\mu(d)\) is not changed.

For \(Nq\le D^{3/16}\), every live \(b\)-interval lies in a constant-factor dyad of scale \(G/Nq\gtrsim D^{5/64}\). Its fixed deleted prime union now also includes \(\operatorname{supp}(q)\), and has polynomial radical norm. Use the fixed-field deleted Möbius estimate (7) of DELETED_PRIME_MERTENS_AND_UNIT_CORRECTION-v1 and exact partial summation on the weight \(1/Nb\). This gives, uniformly over the actual intervals and endpoints,
\[
 \left|\sum_{\substack{Nb\text{ in the interval}\\
       (b,Sd h g_{\rm s}\ell q)=1}}\frac{\mu(b)}{Nb}\right|
     \ll \log^{C}(2D)\exp(-c\sqrt{\log(2D)}).
\]
The constants use the polynomial deletion norm and a fixed positive lower exponent for \(G/Nq\). They do not involve a varying primitive character estimate. Each eligible \(\ell_{\rm g}\) coefficient therefore has this bound times \(\tau(\ell_{\rm g})/(T\,Nq)\), after summing its ordered split and including the actual \(1/N\ell_{\rm g}\). The finite \(\ell/\ell_{\rm g}\) contributes only fixed factors. The remaining \(1/Ng_{\rm s}\) stays outside. On good squarefree ideals, \(\tau(\ell_{\rm g})^2=d_4(\ell_{\rm g})\), the four-factor divisor count. By elementary ideal counting and harmonic summation its sum through \(2T\) is \(O(T\log^3(2T))\). This bounds the squared mass without a pointwise \(D^\epsilon\) divisor factor.

At fixed second pivot, the varying rational phase is the exact \(\chi_{\ell_{\rm g}}(Nv_1)\), with its fixed \(\nu\), \(u_0\) and \(v_2\) factors and zeros retained. The primitive rational moduli are \(N\ell_{\rm g}\), as in EQUALITY_WIDE_RATIONAL_MOMENT-v1. To keep the norm-fibre cost logarithmic, use the elementary bound \(\#\{v_1:Nv_1=n\}\le\tau_{\mathbb Z}(n)\) and, for \(n\le2A_1\), the hyperbola inequality
\[
 \tau_{\mathbb Z}(n)\le2\sum_{\substack{r\mid n\\r\le\sqrt{2A_1}}}1.
\]
At each \(r\) put \(n=rk\), keep \(\chi_{\ell_{\rm g}}(r)\) in its column coefficient including zeros, and apply the ordinary dual rational comparison (3) of EQUAL_RATIONAL_SIEVE-v4 on \(k\le2A_1/r\). The sum of its costs is
\[
 O(A_1\log(2D)+\sqrt{A_1}\,T^2)=O(A_1\log(2D)),
\]
since \(T\lesssim D^{1/8}\). The original row subsets are enlarged only within this positive norm. Bounded literal multiplicities have constant cost. The \(q\mid u\) selector is a row contraction in this small-\(q\) estimate. The resulting \(T^{-1/2}\) factor stays paired with the signed \(\exp(-c\sqrt{\log(2D)})\) factor, rather than estimating the \(g_{\rm l}\)-sum only after taking the absolute value of each \(\ell_{\rm g}\)-term.

For \(Nq>D^{3/16}\) use the absolute weighted \(b\)-sum at its true dyadic length, \(O(1)\) including a live unit endpoint. Sum the \(\ell_{\rm g}\) coefficients in absolute value, with cost \(O(\log^C(2D))\) from \(\tau(\ell_{\rm g})/N\ell_{\rm g}\). At fixed \(v_2\), \(q\mid u\) forces the part of \(q\) outside \(v_2\) to divide \(v_1\). The part in \(v_2\) has bounded norm, and \(Nq\le Ng_{\rm l}\le U\ll A_1\), so the number of eligible rows is \(O(R/Nq)\) by the ideal count. Taking its square root and summing \(1/Nq\) gives
\[
 \sum_{Nq>D^{3/16}}(Nq)^{-3/2}\ll D^{-3/32}.
\]
The small-\(q\) sum of \(1/Nq\) is logarithmic. Both sums keep the exact fixed masks before taking these positive comparisons.

## 3. Equality energy and its remaining gap

The equality-side profile still has absolute bound \(O(\mathcal M_{12}(W)(1+D/(ER))^{-4})\), since \(E_1Nh<14\). Its outside coefficient is \(O(D/(E\sqrt R))\) times the original fixed inverse norms. The \(g_{\rm s}\) sum is harmonic, the \(G,J\) counts are logarithmic, and the finite allocations and \(\tau(d)\) ordered divisor pairs stay explicit. Summing the bounds in the actual row norm and using \(T\lesssim D^{1/8}\), the large-\(q\) factor is at most \(O(T^{-1/2}D^{-1/32})\). It is absorbed into the signed subpower bound. Thus for the exact selected equality vector \(F_{d,T}\),
\[
 D^{-1/2}\|F_{d,T}\|_2
 \ll \mathcal M_{24}(W)\,\tau(d)\log^{C'}(2D)
       \frac{\sqrt D}{E}
       \left(1+\frac{D}{ER}\right)^{-4}
       T^{-1/2}\exp(-c'\sqrt{\log(2D)}).                         \tag{1}
\]
Here \(\tau(d)\) counts ideal divisors. In particular the equality estimate itself has no free positive power of \(D\) hiding this gain.

Pair (1) with the actual full partner complement of energy power \(P(e)\) from EQUALITY_WIDE_RATIONAL_MOMENT-v1, with \(e=\log_D E\). The original compensation stays in that partner norm. The resulting bound for the normalized cross per divisor is
\[
 O\!\left((DH)^\epsilon \mathcal M_{24}(W)^2
 \frac RE\,\tau(d)\log^{C'}(2D)
 D^{\theta(e)/2}T^{-1/2}\exp(-c'\sqrt{\log(2D)})\right),
\]
where \(\theta(e)=P(e)-1/2-8(1/4-e)_+\) on the stated closed divisor band. For example the target follows if \(T\gtrsim D^{\theta(e)}\exp(-c'\sqrt{\log(2D)})\), with the same original harmonic summation since \(\sum_{Nd\ll D}\tau(d)/Nd\ll\log^2(2D)\). This is a subpower refinement of the prior threshold. At \(E\asymp D^{1/4}\) and \(T\asymp1\) the same comparison still costs \(D^{13/16+\epsilon}\) after the divisor sum apart from the displayed subpower factor. Thus the signed \(g_{\rm l}\) route using this fixed-field Mertens input does not supply the missing fixed \(1/16\) power at that core point. It does not give a lower bound on the actual signed form.

