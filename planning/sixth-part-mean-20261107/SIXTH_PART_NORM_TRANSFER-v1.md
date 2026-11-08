# The sixth-part counting error in the balanced finite prefix

Author draft, 7 November 2026 UTC. Independent review is pending. We transport the accepted fixed-ray \(t^{1/3}\) count error through the physical sixth-free norm on the original columns. Its two raw sixth-part masks lead to two least common multiples with the common-divisor index. The improvement concerns the counting remainder. The principal density term retains the actual signed pairing.

## 1. Exact reduction on the original columns

Use the normalized nonprincipal unweighted two-pivot projection \(P(X)\) of cbk:exact-kernel and mixed (2), with the required 6fed549f and 7d62d6c9 precisions. Use \(D\ge2^{64}\), \(1\le U\le\sqrt D\), \(1\le H\le D^{3/4}\), \(1\le X\le D^{3/8}\), \(A_1,A_2\ge1\), and the fixed \(S,\nu,u_0\) and source/ray data. The other four good row factors are units. An active capacity block has \(Nu_0 A_1 A_2^2\le H\). The complete ordered good squarefree ideal annulus, the coprimality of the original columns \(m,n\), their actual \(A_U\) coefficients, and the single possibly complex smooth \(W\) supported on \([1,2]\) with zero endpoints are unchanged. Distinct equal-norm ideals stay distinct.

The actual dual ideal is \(y=hrs^6\), with \(h\) supported on \(S\), \(r\) good sixth-free, \(s\) an arbitrary good ideal, and \(Nh\,Nr\,(Ns)^6\le X\). Overlap of \(r,s\) is allowed. Keep the original finite \(k\) range, with \((k,v_2)=1\) and \(Nk\le \sqrt{b(v_2)/N\ell}\) before the \(S\) deletion, and every \(\ell,e\), source, primitive and capacity restriction. In the leading term \(L(X)\) use \(\dot G\mapsto g_0(v_2)\). The accepted normalized error is
\[
 |P(X)-L(X)|\ll B_W^2(DH)^\varepsilon A_1A_2 X\,A_1X/D^2,
 \qquad B_W=\|W\|_\infty .
\]
It is target-sized by \(A_1 A_2\le H/A_2\), \(A_1\le H\le D^{3/4}\), \(X\le D^{3/8}\). The bounded \(g_0(v_2)\) is independent of \(m,n,h,r,s,k\), which permits the following closed-prefix replacement.

Fix an actual finite ray component \(\rho\) and let \(\psi=\bar\rho^6\) on good ideals. By the accepted exact sixth-part formula the full \(s\) dependence is \(\psi(s)\mathbf 1_{(s,mn)=1}\). The original \(h,r,k\) phases and zeros are separate from this factor and stay in the kernel. In a clipped band \(R\le Nr<2R,\ Nh\,Nr\le X\) put \(V=(X/(Nh\,Nr))^{1/6}\). The accepted SMOOTHED_RAY_COUNT_AND_SIXTH_MEAN-v1 count on good ideals is
\[
 N_\psi(t)=\delta_\psi\kappa_S t+e_\psi(t),\qquad
 |e_\psi(t)|\ll_{S,\psi}t^{1/3}\quad(t\ge0),\qquad
 \kappa_S=\frac{\pi}{3\sqrt3}\prod_{\mathfrak p\in S}(1-1/N\mathfrak p).
\]
Here \(\delta_\psi=1\) for the principal character and zero otherwise. For \(t<1\) the ideal count is zero and the same principal linear term is still subtracted in \(e_\psi\). The result and its fixed-modulus hypothesis are inherited. We use it only for the finitely many fixed source ray characters.

For good coprime squarefree \(m,n\), the exact signed identity is
\[
 \sum_{Ns\le V}\psi(s)\mathbf 1_{(s,mn)=1}
 =\sum_{b_1\mid m,\,b_2\mid n}
   \mu(b_1)\mu(b_2)\psi(b_1 b_2)\,
     N_\psi(V/(Nb_1Nb_2)).
 \tag{1}
\]
The ideals \(s\) on the left are good, and all closed endpoints are literal. The principal part is
\(\delta_\psi\kappa_S V\,g(m)g(n)\), where
\(g(m)=\prod_{\mathfrak p\mid m}(1-1/N\mathfrak p)\).
Include all divisors in (1), even when \(Nb_1Nb_2>V\). The residual is the same double sum with \(N_\psi\) replaced by \(e_\psi\). The entire coherent principal replacement uses this product in the original signed kernel, with all \(h,r,k,\ell,e\), root, ray and orientation data. Principality here is for the sixth-part ray character, while the original row projection remains nonprincipal.

## 2. Transport through the exact least common multiples

For the counting remainder fix \(h,k,\ell,e,v_2\) and a source component, and use the accepted cbk:two-gauges separation of the primitive root and fixed phases on the original coprime support. Strip \(A_1\) and the original factors \(\mu(k)\mu(\ell)\mu(e)/((Nk)^2N\ell Ne)\) from this leading form. The two actual column vectors, say \(x_m,z_n\), include \(W,A_U,\nu\), the two original gauges and their fixed raw factors. They have magnitude \(O_\varepsilon(B_W D^{-1/2+\varepsilon})\), since the original \(\sqrt F\) factors as \(\sqrt{N f_S}\sqrt{Nm}\sqrt{Nn}\). The finite \(S\) factor and each separated source component keep their original indicators and coefficient. The bounded \(r\)-scalar retains the original \(S\)-phase of \(r\). The moving good factors of \(r\) are \(\overline{R_m(r)}R_n(r)\), including zeros. The two vectors and fixed factors can differ. This separation uses the root identity only on the original coprime support.

After inserting (1), invert the original \(\mathbf 1_{(m,n)=1}\) by \(\sum_{d\mid m,n}\mu(d)\) in the product of the separated columns. We can keep \((b_1,b_2)=1\) as a fixed selector, since it held on the original support and its retention commutes with inversion. For fixed \(d,b_1,b_2\) put \(E=Nd,\ f_i=[d,b_i]\), so \(m=f_1 a,n=f_2 b\). Both residual ideals are good squarefree and coprime to their respective \(f_i\) at nonzero entries. They may overlap each other. Full original divisors are included. This is an auxiliary extension by products, so it requires no primitive root at an overlapping column pair.

In the \(r\)-pairing the \(f_1,f_2\) factors of the two good sextic symbols are bounded diagonal factors, including their zeros. Only for the Cauchy bound absorb them into the scalar alongside the fixed \(S\) factor, the exact clipping, and \(e_\psi(V/(Nb_1Nb_2))\). The resulting scalar is bounded by
\[
 \ll_{S,\psi} (X/(Nh R))^{1/18}(Nb_1Nb_2)^{-1/3}.
 \tag{2}
\]
There is no extra mask between \(r,k,s\) or between \(r,v_2\). The two residual vectors carry the actual values at \(f_1a,f_2b\); their squared coefficient masses are each \(\ll_\varepsilon B_W^2D^\varepsilon/Nf_i\), by ideal counting up to \(2D/Nf_i\).

For \(Nf_i\le D\), apply the inherited physical sixth-free row norm phy:input/phy:family to the unweighted good sixth-free \(r\) rows up to \(2R\) and good squarefree residual columns up to \(2D/Nf_i\). Its bound, with the customary subpowers and harmless endpoint constants, is
\[
 \Phi_6(R,L)=R+L+R^{5/6}L^{1/3}+R^{1/3}L^{5/6},
 \qquad L=D/Nf_i.
\]
This is the application of de Faveri v1, Theorem 1.1, with \(n=6\). The bounded scalar in (2) is paid outside the norm. For \(D<Nf_i\le2D\), the only possible residual is the unit and direct counting gives squared norm \(O_\varepsilon(B_W^2D^\varepsilon R/Nf_i)\). For \(Nf_i>2D\) the vector is empty. The displayed majorant also dominates the subunit calculation.

First apply bilinear Cauchy over the same actual \(r\) band to the two residual vectors. Then take the triangles in \(d,b_1,b_2\). Dropping \((b_1,b_2)=1\) only in this positive majorant bounds the error for the fixed outer parameters by
\[
 \ll B_W^2(DH)^\varepsilon (X/(Nh R))^{1/18}
     \sum_d Q(Nd;d)^2,\qquad
 Q(E;d)=\sum_{\substack{b\ {\rm good,\ squarefree}\\N[d,b]\le2D}}
      (Nb)^{-1/3}
      \left(\frac{\Phi_6(R,D/N[d,b])}{N[d,b]}\right)^{1/2}.
 \tag{3}
\]
This argument keeps both column vectors until Cauchy. It uses an unweighted norm of physical labels, with no uniform estimate over arbitrarily weighted row measures or arbitrary conductor characters.

Write \(b=g t\), \(g=(b,d)\mid d\), \((t,d)=1\). Then \([d,b]=dt\). For the positive majorant drop \(Ng^{-1/3}\le1\), sum over \(g\) with cost at most \(\tau(d)\), and bound the \(t\) sums by all ideals with norm \(\le2D/E\). The four square roots of the physical terms give \(t\)-weights of powers \(5/6,4/3,1,5/4\), respectively, after the \((Nt)^{-1/3}\) from (2). Ideal counting gives
\[
 Q(E;d)\ll \tau(d)\left[
  R^{1/2}D^{1/6}E^{-2/3}
 +D^{1/2}E^{-1}
 +R^{5/12}D^{1/6}E^{-2/3}\log(2D)
 +R^{1/6}D^{5/12}E^{-11/12}\right].
\]
Here the first term uses \(\sum_{Nt\le2D/E}(Nt)^{-5/6}\ll(D/E)^{1/6}\). Each squared \(E\)-power, namely \(4/3,2,4/3,11/6\), is summable with \(\tau(d)^2\) by the ideal divisor bound with a sufficiently small exponent. Consequently
\[
 \sum_d Q(Nd;d)^2 \ll_\varepsilon (DH)^\varepsilon
   \left(R D^{1/3}+D+R^{5/6}D^{1/3}+R^{1/3}D^{5/6}\right)
 \ll_\varepsilon (DH)^\varepsilon D,                  \tag{4}
\]
as \(R\le D^{3/8}\) on a live band.

There are no \(h\)-terms if \(NhR>X\). Summing the positive majorant uses \(\sum_{h\ S\text{-supported}}(Nh)^{-1/18}<\infty\). The finite \(k\)-weights are dominated by the absolute \(Nk^{-2}\) sum, and the \(v_2,\ell,e\) mass costs \(O(A_2(DH)^\varepsilon)\). Put back \(A_1/D\) once. By capacity the new **normalized** band error between leading term and signed principal mean is
\[
 |L_R(X)-\mathfrak M_R(X)|
 \ll B_W^2(DH)^\varepsilon \frac{H}{A_2}(X/R)^{1/18}.
 \tag{5}
\]
The main \(\mathfrak M_R\) is exactly the finite expression of Section 1. For \(\psi\) nonprincipal the corresponding part of (5) bounds the whole leading branch. This conclusion is independent of the previous pending quadratic-cross comparison (Q).

## 3. What remains at the balanced transition

The previous smooth-long author draft and its pending input (Q) give target-size for the whole \(Nr<Y_0\) portion with \(Y_0=D^{13/40}\). Indeed the previous first band monomial is already target-size on \(R\le D^{1/3}\), while \(X^{1/6}D^{-1/3}R^{5/6}\le1\) at \(X\le D^{3/8}\) and \(R\le Y_0\). The earlier large-\(d\) tail and pre-lift Bessel error remain target-size. With half-open bands and exact clipping at \(Y_0\), sum (5) above this cutoff. The combined reduction, still conditional on acceptance of the preceding drafts for the low part, is
\[
 |P(X)-\mathfrak M_{\ge Y_0}(X)|
 \ll (DH)^\varepsilon H\left[
 B_W^2+(C_W+\mathcal M(W))^2+
 B_W^2 A_2^{-1}(X/Y_0)^{1/18}\mathbf 1_{X\ge Y_0}\right]. \tag{6}
\]
Here \(C_W,\mathcal M(W)\) are the fixed seminorms in the previous smooth-long estimate. At pure critical \(X=D^{3/8}\), the relative error excess in (6) is \(1/360\), giving exponent \(271/360\). For a single band at \(R=D^{1/3}\) the excess in (5) is \(1/432\). These are upper-bound exponents for the remainder.

Attempting the same physical norm for \(\mathfrak M_R\) pays the principal coefficient \(V\), rather than \(V^{1/3}\). The factors \(g(m),g(n)\le1\) can be included directly in the column vectors. The resulting bound is \(B_W^2(DH)^\varepsilon (H/A_2)(X/R)^{1/6}\), with the same clipping and phases prior to Cauchy. At the balanced critical band this still permits the \(1/144\) excess of the previous whole-prefix candidate. In particular (6) by itself gives no improved whole-prefix power. The next task is a signed estimate for the actual principal-density pairing near \(R=D^{1/3}\), with the full two original column vectors, raw zeros, equal-norm fibres, fixed common \(W\) and all outer phases. The high-frequency complement, extra good factors, short/principal assembly, whole signed \(13/12\), global unsigned \(9/8\), determinant and zero-location by scope, analytic and categorical Lean, and GRH remain open.

Acceptance requires the exact finite identity including subunit arguments, the two original column subsequences, the unit endpoint, the explicit summation of the three divisor indices, and independent review of the analytic transfer. The new finite checks test divisor algebra on explicitly distinguished ideal labels and rational exponent arithmetic. They do not check character-sieve theorems or replay the accepted fixed-ray controls.
