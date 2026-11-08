# A smooth long factor at small prefixes

Author draft, 7 November 2026 UTC. Independent review is pending. This note removes the artificial long-factor dyadic cut in the small-prefix part of the exact eleven-factor expansion. The new smooth comparison uses the already established growing-modulus bound on the safe Mellin strip. The final finite-prefix comparison also uses (Q) from QUADRATIC_CROSS_PREFIX-v2, which is awaiting independent review. The smooth row and its exact regrouping do not use (Q).

## 1. Scope and the exact small-prefix regrouping

Use the original nonprincipal unweighted two-pivot projection \(P(X)\), normalized by \(D\), as in cbk:exact-kernel and accepted mixed formula (2), with its required 6fed549f and 7d62d6c9 precisions. Here \(D\ge 2^{64}\), \(1\le H\le D^{3/4}\), \(1\le U\le\sqrt D\), and \(1\le X\le D^{3/8}\). The fixed data are \(S,\nu,u_0\) and the source and ray conditions. The other four good factors are units. The original nonempty capacity implies \(Nu_0 A_1 A_2^2\le H\). The single common complex or real smooth \(W\) is supported on \([1,2]\), with zero endpoints. All ordered ideal norm fibres are retained. The exact frequency is \(y=hrs^6\) with \(Ny\le X\). Here \(h\) is \(S\)-supported, \(r\) is good sixth-free, and \(s\) is an arbitrary good ideal. The original finite \(k\) range has \((k,v_2)=1\), \(Nk\le\sqrt{b(v_2)/N\ell}\), before the \(S\)-deletion. The exact primitive \(S\) and good root values, \(\overline{\rho(s)}^6\), both \(s\) column masks and the full source and capacity factors remain. We bound the leading term \(\dot G\mapsto g_0(v_2)\), and handle its explicit error at the end.

Insert \(\mathbf1_{(m,n)=1}=\sum_{d\mid m,n}\mu(d)\) into the separated leading form. The two shifted vectors are distinct and have the actual coefficients at \(m=da,n=db\). Each residual is squarefree and coprime to \(d\), and the residuals may overlap each other. The product of separated coefficients at an overlapping pair only serves the inversion. For \(E=Nd\le D^{1/16}\) set \(L=D/E\). The three-factor coefficient identity splits \(d=d_1d_2d_3\), retains the two different short cutoffs \(U/Nd_1,U/Nd_2\), and puts \(\mu(d_3)\mu(a_3)\) on the third factor. It is applied to the actual \(B_U(da)=\mu(da)A_U(da)\) with \(N(da)>U\). Expand the third factor by the exact eleven-factor identity rg:hb-identity, at \(z_0=(2L)^{1/5}\). Its remainder vanishes because the residual norm is at most \(2L\). Each factorization has its original labelled coefficients, own cutoffs, squarefree and pairwise disjoint support. A subunit cutoff eliminates its branch, and equality retains the unit.

For one label corresponding to an unrestricted coefficient-one factor, write the residual as \(pv\), where \(v\) has that label and \(p\) is the product of all other factors. Take a real \(Z\) with \(1\le Z\le L^{1/3}/2\) and restrict to the literal \(Np\le Z\). Every nonzero summand has \(Nv\ge L/Np\) from \(W(NpNv/L)\). In the inherited dyadic box, let \(M_v\) be the scale of \(v\) and \(B_0\) the product of the scales of the other factors. Then \(M_v>Nv/2\ge L/(2Np)\), \(B_0\le Np\), and \(M_v>B_0^2\) because \(2(Np)^3\le L/4\). Every subset of labels omitting \(v\) has scale product below \((M_v B_0)^{1/3}\). Every subset containing \(v\) has product above \((M_v B_0)^{2/3}\). Thus the inherited box is unbalanced and chooses exactly this \(v\). In particular this choice is the same for every admissible \(v\) with \(p\) and the other factors fixed.

Conversely, every small-prefix tuple in an inherited unbalanced box with \(Np\le Z\) appears in this regrouping. The inherited long factor is an unrestricted label, since its box scale exceeds \((L/2^{11})^{2/3}>\sqrt D\) and exceeds the truncated cutoff. Two labels cannot both pass the small-prefix test on a single tuple. Summing the eligible long dyads therefore gives exactly the whole smooth profile \(W(Nv/T)\) at \(T=L/Np\), with no long interval left in the small-prefix row. All short labels and their own sharp cutoffs stay in the short coefficient. The prefix has the original divisor bound. There is no change in the balanced boxes, or in the unbalanced boxes with \(Np>Z\) where the long dyadic restriction can remain. If \(Z<1\), the entire smooth part is empty. These statements include \(p=1\), the complete equal-norm ideal fibres and the \(W\) endpoints.

## 2. Uniform smooth Gauss row and the surviving deletions

Use the original nonzero angular component \(+1\) or \(-1\), the fixed source normalization and exact primitive \(S\) selector. The original good factors of the growing twist have raw zeros on \(rv_2\) and safe period norm \(\ll A_2R\) on \(R\le Nr<2R\). The physical cubic frequency after the \(d\) shift and prefix CRT is \(t=dpk\). On live support its factors are squarefree and pairwise coprime. Its cubic symbol carries the raw \(t\) mask. Keep all three factors and their original short collision branches. The two columns use the corresponding whole conjugations, including the common profile. We use \(Q_\gamma=N\operatorname{rad}(rv_2)\), \(J=Nk\), and the canonical source correction at the fixed primes. These are the exact finite components of the same row in the accepted mixed and growing-modulus inputs.

Let \(C_W=B_W+\sum_{i=0}^4\int_1^2 |(x\partial_x)^i W(x)|\,dx/x\), \(B_W=\|W\|_\infty\). In the no-interval long row with the literal \(W\), set \(B_1=Q_\gamma Nt\). The already established growing-modulus completed convexity estimate bounds the actual Dirichlet series \(\mathcal R\) on \(\sigma=1/2+\eta\) by
\[
 |\mathcal R(\sigma+i\tau)|
 \ll_\varepsilon (B_1(2+|\tau|))^\varepsilon
 B_1^{(3/2)(1-\sigma)}(1+|\tau|)^{2(1-\sigma)} .
\]
Use the actual angular, local and raw coefficients from growing-modulus (12)–(14), with the accepted mixed-period transfer. The numerator is entire for the nonzero angular components. In moving the Mellin integral from absolute convergence to \(\sigma\), its raw cube denominator is only inverted where \(\Re(3s-1/2)>1\). Absolute Euler convergence there gives the uniform inverse bound for all raw omissions. No zero-free strip or cancellation in the cusp coefficients is assumed.

For \(T\ge1\), the exact inverse Mellin integral for the normalized long row has \(T^{z-1/2}\widehat W(z-1/2)\mathcal R(z)\), where \(\widehat W(w)=\int W(x)x^w\,dx/x\). Uniformly on the closed strip between the two lines, the \(C_W\) bound gives \(O(C_W(1+|\Im z|)^{-4})\). Thus the horizontal edges tend to zero by the polynomial bounds on that strip. The vertical integral at \(1/2+\eta\) is absolutely bounded by
\[
 \ll_\varepsilon C_W(TB_1)^\varepsilon B_1^{3/4}. \tag{M}
\]
Choose \(\eta>0\) small enough for the requested subpower loss. In the range \(1/2\le T<1\) use the literal unit, with the bound \(O(C_W)\). For \(T<1/2\) the row is empty. Formula (M) is derived for the coalesced smooth row and does not apply to an uncoalesced interval.

The original long-column restrictions in this lifted row are those against \(d,p,k,r,v_2,s\), with the support of \(\ell\) included in \(v_2\). All fixed restrictions stay in the fixed finite factors. One can open the full long mask by the accepted rg:deletion-identity. If its divisor \(b'\) shares a prime with \(t=dpk\), that branch has the cubic zero. If it meets \(rv_2\), the actual raw growing character at \(b'\) is zero. This includes a prime whose primitive conductor dropped under a power cancellation. Consequently every live \(b'\) divides \(\operatorname{rad}(s)\), with whatever extra exclusions the original mask demands. Equivalently the other moving masks are already included as zeros before expanding the \(s\) restriction. The signed identity retains the literal \(\mu(b')\), Gauss phase and raw numerator value. All overlaps of \(s\) with \(r,v_2,t\) are allowed in the original data.

The surviving \(b'\) scales the row to \(T/Nb'\), replaces the cubic numerator by \(b't\), and contributes \((Nb')^{-1/2}\). Its cost in (M) is therefore at most \((Nb')^{1/4}(Q_\gamma Nt)^{3/4}\) up to \(C_W\) and subpowers. The subunit branch obeys the same upper bound by its literal unit. Summing over the original eligible divisors costs \(O_\varepsilon((Ns)^{1/4+\varepsilon})\) times the cost without deletion. This positive bound uses the full signed deletion first. It does not make \(s\) squarefree.

With the original short weights \(O((DH)^\varepsilon/\sqrt{Np})\), and \(Q_\gamma\ll A_2R\), the small-prefix portion for each shifted column is bounded pointwise by
\[
 \ll C_W(DH)^\varepsilon E^{-1/2}
       (EJA_2R)^{3/4}(Ns)^{1/4} Z^{5/4}.
\]
Indeed \(\sum_{Np\le Z}(Np)^{1/4}\ll Z^{5/4}\) by ideal counting with the allocated divisor loss. The factor \(E^{-1/2}\) is from the original column normalization. Sum its square over the clipped band in \(r\), at fixed \(h,s,k,\ell,e,v_2,d\) and fixed component. If the band is nonempty for \(h,s\), \(Ns\le (X/R)^{1/6}\). The resulting squared mean is
\[
 \ll C_W^2(DH)^\varepsilon E^{-1}
       R(EJA_2R)^{3/2}(X/R)^{1/12}Z^{5/2}. \tag{S_{\rm sm}}
\]
The original \(r\)-dependent complex scalar and both columns remain in the signed pairing. This is a bound on each shifted column used there.

## 3. Balance with the joint norm and finite assembly

For \(1\le R\le D^{1/3}\) use (Q) of the previous author draft only on the large unbalanced prefix \(Np>Z\). Its clipped short dyad scale \(P\) satisfies \(P\gg Z\), or \(P\ge1>Z\) if the smooth part is empty. It obeys \(P\ll L^{1/3}\). The two other terms of (Q) are \(\ll R D^{2/3}\) inside \(E^{-1}\), since \(R\le D^{1/3}\) and \(R\ge1\). The inherited balanced boxes cost \(\ll E^{-1}R L^{2/3}\) with the same profile and subpower allowances. Both conclusions follow by summing the polynomially many in \(\log D\) label boxes using the Hilbert-space triangle inequality. The other coefficient factors in (Q) have the same unchanged finite selectors and exact Mellin-separated profile. Its hypotheses do not require a sharp long row for the smooth branch.

Choose the threshold
\[
 Z=D^{2/7}E^{-5/7}(JA_2)^{-3/7}X^{-1/42}R^{-29/42}.
\]
It solves \(R(EJA_2R)^{3/2}(X/R)^{1/12}Z^{5/2}=L/Z\). Also \(Z/L^{1/3}\le D^{-1/21}<1/2\) for \(D\ge2^{64}\), so Section 1 applies whenever \(Z\ge1\). If \(Z<1\), the smooth branch is empty and the remaining \(L/P\) is still \(\ll L/Z\). Thus both column squared means are bounded by
\[
 \ll (C_W+M)^2(DH)^\varepsilon E^{-1}
       [D^{5/7}E^{-2/7}(JA_2)^{3/7}X^{1/42}R^{29/42}
           +R D^{2/3}], \tag{9}
\]
with the same \(M=\mathcal M(W)\) as before. This is an assembly of the three column portions in the \(r\)-Hilbert norm. It includes their cross pairings through the norm bound.

Use bilinear Cauchy on the two shifted columns over the same actual \(r\) band at fixed \(d,h,s,k,\ell,e,v_2\) and source component. The bounded original scalar is retained in that pairing. Only then sum the positive majorants in \(d,k,h,s\), retaining the signs in the finite identity. The two \(d\) powers are \(9/7,1\), and the \(k\) powers after the original \((Nk)^{-2}\) are \(11/7,2\). They give convergent sums apart from the logarithmic \(d\) term. The compatible \(h,s\) count is \(O_S(X^{1/6}R^{-1/6})\), from the original bound \(Ns\le(X/(NhR))^{1/6}\). The \(v_2,\ell,e\) mass costs \(O(A_2(DH)^\varepsilon)\). Use the original \(A_1/D\) once and \(A_1A_2\le H/A_2\). The normalized small-\(d\) contribution of a band \(R\le D^{1/3}\) is bounded by
\[
 \ll (C_W+M)^2(DH)^\varepsilon H
  [X^{4/21}D^{-2/7}A_2^{-4/7}R^{11/21}
       +X^{1/6}D^{-1/3}A_2^{-1}R^{5/6}].
\]
The first term is at most \(D^{-5/126}\) inside the bracket on the full stated \(X,R\) ranges, and the second is bounded by \(X^{1/6}D^{-1/18}A_2^{-1}\). At the old pure transition \(R\asymp D^{2/7}\), the latter relative exponent at critical \(X\) is \(-11/336\), and the first is smaller. Thus the previous short-prefix transition is covered at target size in the combined comparison.

For \(R\ge D^{1/3}\), use the inherited physical sixth-free comparison on the original columns after the same common-divisor lift, with no short-factor comparison. The physical norm satisfies \(\Phi_6(R,D)\ll D\) throughout \(R\le X\le D^{3/8}\). The resulting positive outer count gives \(H X^{1/6}R^{-1/6}A_2^{-1}\) with the fixed \(B_W^2(DH)^\varepsilon\) factor, hence the same \(D^{-1/18}\) loss in the coefficient of \(X^{1/6}\). At lower \(R\), the inherited \(E>D^{1/16}\) tail uses the same physical norm at length \(D/E\). After the \(E^{-1}\) mass, its four terms are bounded by \(R+D^{15/16}+R^{5/6}D^{1/3-1/48}+R^{1/3}D^{5/6-5/96}\) up to subpowers, with the literal unit for \(D<E\le2D\). Multiplication by \(X^{1/6}R^{-1/6}/D\) gives a bounded factor. These complementary estimates retain all the old masks. No new cancellation of Möbius signs is used there.

Before the lift the derivative-free Bessel error is bounded by \(B_W^2(DH)^\varepsilon A_1A_2 X(A_1X/D^2)\). The optional projection onto unequal norms is obtained by subtracting the complete equal-norm ideal fibre and costs at most \(B_W^2(DH)^\varepsilon A_1A_2 X/D\). Both are target-sized by the stated capacity and prefix limits. These estimates use no regularity of the sharp-capacity interpolant beyond its accepted derivative-free error.

The combined candidate is
\[
 |P(X)|\ll [B_W^2+(C_W+M)^2](DH)^\varepsilon H
          [1+X^{1/6}D^{-1/18}A_2^{-1}]. \tag{10}
\]
Clip the split at \(D^{1/3}\) and sum the finitely many bands, absorbing logarithms. The pure critical power is \(109/144\), a gain \(1/126\) over the previous \(257/336\) draft and \(1/18\) over the established \(13/16\) same-prefix bound. This candidate reaches target for \(X\le D^{1/3}\) or, at \(X=D^{3/8}\), when \(A_2\ge D^{1/144}\).

The remaining upper-budget excess is \(1/144\) at \(X=D^{3/8}\), \(A_2=1\), and \(R\) near \(D^{1/3}\). It comes from the balanced \(R L^{2/3}\) comparison and the comparable joint large-prefix and inherited physical bounds. A further improvement of the smooth small-prefix Mellin line alone does not remove these terms. The next task is the signed balanced pairing or a strengthened joint comparison that covers this scale. There is no lower bound from this comparison. The full signed \(13/12\), global unsigned \(9/8\), higher-frequency and extra-factor complement, principal and short assembly, determinant and zero-location by scope, analytic and categorical Lean, and GRH remain open.

Acceptance requires the exact small-prefix partition, safe Mellin line, full deletion support and weights, explicit exponent and endpoint checks, and independent review of this argument and the prior (Q) operator input. The fresh controls check the regrouping and divisor survival algebra and the exponent calculation. They do not run an analytic proof checker or rerun any earlier CRT, functional-equation or release controls.

