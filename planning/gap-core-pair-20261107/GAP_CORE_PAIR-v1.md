# Joint cofactor bound in the signed two-prime pairing

Author draft, 7 November 2026 UTC. Independent review is pending. This note estimates specified parts of the two-prime kernel using the inherited physical sixth-free and ordinary primitive comparisons. The transfer from the original central density uses the earlier gap and prime-prefix reductions with their stated pending inputs.

## 1. Original kernel and its exact coprimality

Use GAP_PRIME_PREFIX-v1 on the normalized far-gap central band with \(D\ge2^{128}\), \(2D/7\le U^2\le D\), \(1\le H\le D^{3/4}\), \(1\le X\le D^{3/8}\), \(D^{13/40}\le R\le D^{27/80}\). Keep \(R\le Nr<2R,\ Nh\,Nr\le X\) and the exact squarefull-part selection on \(r\) from that draft. Set \(U_*=U(1+D^{-1/32})\). The original nonprincipal two-pivot capacity, the fixed \(S,\nu,u_0\) and source/ray data, and the one common fixed smooth complex \(W\) are as in cbk:exact-kernel and mixed (2) with required 6fed549f and 7d62d6c9. The four other good row factors are units. Keep all original finite \(h,k,\ell,e,v_2\) data, including the pre-\(S\) cap on \(k\) and \((k,v_2)=1\). The original scalar carries the primitive \(S\) phases and \(\kappa_S(X/(Nh\,Nr))^{1/6}\). The principal-sixth-part selection is the one already present in the far-gap kernel.

Each column is an ordered factorization \(m=(c_x p)(c_y q)\) with \(p,q\) prime ideals, \(N(c_xp),N(c_yq)>U_*\) and \(c=c_xc_y\) of norm \(<D^{1/24}\). Write \(n=(c_z p')(c_w q')\), \(c'=c_zc_w\) for the other column. Both columns are good and squarefree, with the same original annuli and all ordered ideal norm fibres. The sign in the original coefficient is \(\mu(m)\) or \(\mu(n)\). After the accepted single-column gauges, the associated cubic Gauss factors and coefficients carry the corresponding signs as in the earlier gap argument. The exact density \(g(m)g(n)\) remains.

Every marked prime ideal has norm \(>Y=\sqrt{2/7}\,D^{11/24}\), since \(N(c_xp)>U_*\) and \(Nc_x<D^{1/24}\). This exceeds every small cofactor norm. Thus a marked prime of either column cannot occur in the other column's cofactor. On the original factorizations the exact pair projector is
\[
 \mathbf1_{(m,n)=1}=\mathbf1_{(c,c')=1}
     \mathbf1_{\{p,q\}\cap\{p',q'\}=\varnothing}.
 \tag{1}
\]
Prime labels are ideals. Distinct split conjugates of the same norm do not meet in the set on the right. The individual-column squarefree conditions are unchanged. The original \(r\)-mask is kept. In particular \(Nr<2D^{27/80}<Y\), so a marked prime cannot divide \(r\), whereas it is still possible for a prime of a cofactor to divide \(r\) and give a raw zero.

## 2. Removing the large-prime collision with an explicit error

Use the two original single-column gauges on their actual coprime support. Extend their separated product to all pairs of allowed individual columns, with the same separated fixed scalar factors. This defines an auxiliary product on a pair with shared prime. No primitive root or conductor of a shared-prime pair is used. The scalar bound on the extension follows from the original separated factors. After dividing by the original \(D\), and before summing \(r,h,k,\ell,e,v_2\), the size per pair is bounded by the same constant times \(A_1 B_W^2/D^2\) with the original finite outer weights and density, where \(B_W=\|W\|_\infty\). This follows from the two column inverse-square-root norms and the fixed \(S\) factor. The column signs, finite components and exact phases are retained in the extension before bounding its collision error.

For fixed \(c,c'\) the ways to assign their small divisors to the two ordered factors cost at most \(\tau(c)\tau(c')\). If \(p_0\) is the shared marked prime, there are four possible positions and at most \(O(D/(Nc\,Np_0))\) and \(O(D/(Nc'\,Np_0))\) choices of the two other primes. If one quotient is below a fixed positive constant the corresponding family is empty. Ideal counting therefore bounds the total collision count by
\[
 \ll D^2
  \left(\sum_{Nc<D^{1/24}}\frac{\tau(c)}{Nc}\right)^2
  \sum_{Np_0>Y}(Np_0)^{-2}
 \ll_\varepsilon D^{2+\varepsilon}Y^{-1}.
\]
A pair with both marked primes shared is included in this upper count. This count is valid for any further selection of these pairs, and it keeps distinct equal-norm prime labels. Only for the error bound one may relax the cofactor coprimality and the actual remaining finite selectors. The original \(r\) count costs \(O(R)\), the density factor is at most \((X/(Nh R))^{1/6}\) times fixed data, and the finite outer estimates give \(A_1A_2\le H/A_2\le H\) with the usual subpowers. Thus the error from omitting the second factor in (1) in the auxiliary product is
\[
 O\!\left(B_W^2(DH)^\varepsilon H Y^{-1} X^{1/6}R^{5/6}\right)
   =O\!\left(B_W^2(DH)^\varepsilon H D^{-11/96}\right).
 \tag{2}
\]
The same bound restores that factor on any of the sections below. In the auxiliary expression the remaining signed Möbius inversion is solely
\(\sum_{d\mid(c,c')}\mu(d)\), with the actual \(E=Nd<D^{1/24}\) throughout. This is a shorter signed lift of the pairing. It leaves all original row coprimalities in each coefficient and all finite factors in the scalar.

## 3. Both cofactor groups in the ordinary primitive norm

Fix the original \(k,\ell,e,v_2,h\) and a finite component. In the auxiliary product, insert the entire signed cofactor lift and fix \(d\). In the first column split \(d=d_xd_y\) between \(c_x,c_y\), as determined uniquely by their squarefree disjoint support. Put \(a=c/d\) and \(w=pq\), so \(m=d a w\). Keep both actual \(c_x,c_y\) and their assignment inside the short coefficient. Let \(C\le Nc<2C\) be a dyadic band, clipped at the original cutoff, with \(C\ge1\). Its residual short scale is \(P\asymp C/E\). One can use a bounded number of dyads with \(P\ge1\), since a nonempty band has \(E\le Nc<2C\). The unit \(a=\mathcal O\) is included directly. The long scale is \(T\asymp D/C\) by \(D\le Nm\le2D\), uniformly over the assignments.

At fixed \(d_x,d_y\), separate the two original cutoffs
\[
 Np>\left\lfloor U_*/Nc_x\right\rfloor,\qquad
 Nq>\left\lfloor U_*/Nc_y\right\rfloor
\]
by the exact finite comparator of GAP_PRIME_PREFIX-v1. Its logarithmic Fourier mass applies with \(N=O(D)\) and includes literal equality. The two ordered primes in \(w\) retain their own phases from this separation. Sum their actual factorizations in the long coefficient. The common \(W(Nm/D)\) has its exact Mellin separation with \(M(W)\). The actual \(g(m)\) factors on disjoint support. Source and primitive finite factors separate as in the original shifted column. Thus the two vectors have divisor-bounded mass after inverse norm weights, with \(E^{-1/2}\) outside. The long vector depends on neither \(a\) nor \(r\) in each separated term.

Gauss CRT and the shifted cubic numerator \(dk\) give the same joint symbol as in the earlier primitive comparison. Specifically the varying long symbol \(\chi_{3,w}(\alpha_a)\overline{R_w(r)}\) equals \(\overline{R_w(ra^4)}\), with the \((a,r)>1\) branch already zero from the short symbol. All original fixed and short zeros stay, including those at \(dk\). The scalar at \(r\) remains evaluated at the original \(r\). For live \(r,a\), the good primitive conductor of \(ra^4\) is \(\operatorname{rad}(r)a\), with norm \(O(RP)\). Every prime has one of five valuations in \(r\) or belongs to \(a\). Hence a fixed conductor has divisor-bounded multiplicity. The raw zeros on good \(w\) agree with this primitive character. Short-variable Cauchy and the inherited mcs:ordinary give squared band norm
\[
 \ll_\varepsilon M(W)^2(DH)^\varepsilon E^{-1}
             [D/C+(RC/E)^2].
 \tag{3}
\]
The unit short factor obeys this bound, by the same primitive comparison with \(P=1\). Dyadic constants are harmless. In the entire cofactor range the second term is \(O(D^{91/120})\), and the first scale is at least a constant times \(D^{23/24}\). Thus (3) costs \(O(M(W)^2(DH)^\varepsilon D/(EC))\). This estimate uses the inherited ordinary primitive comparison and the exact current selectors.

Apply (3) to the second column at \(C'\le Nc'<2C'\) with its own gauge, not identifying it with the first. If an additional pair restriction \(Nc\,Nc'\ge V\) is required, separate the exact integer comparison \(Nc'>\lceil V/Nc\rceil-1\) by the same finite comparator. For \(1\le V\le D^{1/12}\), each index is \(O(D)\), and the new phases enter only the respective short coefficients, even if the short factor is the unit. The logarithmic mass is absorbed into subpowers. This handles the boundary dyads without assuming that the product cutoff is constant on a cell.

The two bounds in (3), applied by bilinear Cauchy over the same actual \(r\) band, cost \(O(M(W)^2(DH)^\varepsilon D/(E\sqrt{CC'}))\) before the normalization and finite outer weights. Include the exact bounded \(r\) scalar before taking its density upper bound. Use the finite harmonic \(d\) sum and the original finite \(k,\ell,e,v_2\) estimates and \(h\) weight. The normalized paired upper budget on the dyadic cells is
\[
 \ll_\varepsilon M(W)^2(DH)^\varepsilon H
                  (X/R)^{1/6} (CC')^{-1/2}.
 \tag{4}
\]
There is no separate loss from extending \(E\) to \(D^{1/24}\), since \(D/C=L/P\) in the long length and \(E^{-1}\) is harmonic. On \(Nc\,Nc'\ge D^{1/48}\) only cells with \(CC'>D^{1/48}/4\) contribute. Summing the finitely many dyadic cells and using \((X/R)^{1/6}\le D^{1/120}\) gives
\[
 O\!\left((B_W+M(W))^2(DH)^\varepsilon H D^{-1/480}\right).
 \tag{5}
\]
Equation (2) restores the original marked-prime coprimality for this bound. The section therefore controls a part of the original signed pairing. In particular the surviving exact product cut is \(Nc\,Nc'<D^{1/48}\), rather than separate bounds on the two sides.

## 4. Removing marked inert prime ideals

There is a separate bound when at least one marked prime ideal is inert. Use this on the complement of the large-cofactor selection so the two removals can be disjoint. In the Eisenstein field, away from \(S\), an inert prime ideal has norm the square of its rational prime. Thus for one marked inert factor with \(Np>Y\), \(\sum_{Np>Y,\ {\rm inert}}1/Np\ll Y^{-1/2}\) by summing over rational integers beyond \(\sqrt Y\). The other prime has \(O(D/(Nc\,Np))\) choices for fixed \(c\). A fixed cofactor lift \(d\) has
\(\sum_{d\mid c,\,Nc<D^{1/24}}\tau(c)/Nc\ll_\varepsilon D^\varepsilon/E\). The column coefficient is supported on at most \(O_\varepsilon(D^{1+\varepsilon}Y^{-1/2}/E)\) ideals, allowing multiple factorizations by the divisor bound. Its squared inverse-norm coefficient mass is
\(O_\varepsilon(B_W^2 D^\varepsilon Y^{-1/2}/E)\). The other vector has the full \(O_\varepsilon(B_W^2 D^\varepsilon/E)\) mass. The signed union is the inert first column paired with the full second, plus the complementary first paired with the inert second.

If the product cutoff \(Nc\,Nc'<D^{1/48}\) is imposed here, use its exact comparator as in Section 3 before grouping by residual ideals. Each short coefficient acquires a unitary phase depending on its own \(c\) and bounded multiplicity per column. The coefficient mass estimate survives. Apply the inherited sixth-free norm at the actual shifted length \(D/E\) to each column and then Cauchy in \(r\). The norm constant is \(O((DH)^\varepsilon D)\) in the stated range, and the inert restriction therefore gives \(Y^{-1/4}\) in the paired bound. After the same finite sums and density factor the estimate is
\[
 O\!\left(B_W^2(DH)^\varepsilon H D^{1/120}Y^{-1/4}\right)
   =O\!\left(B_W^2(DH)^\varepsilon H D^{-17/160}\right).
 \tag{6}
\]
One can restore the large-prime mask by (2), which is smaller. This controls the actual inert section and uses no distribution theorem for the split primes.

## 5. Remaining signed pairing

In the stated central band the surviving exact signed two-prime term has four split prime ideals, two on each side, and \(Nc\,Nc'<D^{1/48}\), with the previous small squarefull part of \(r\). The full cofactor projector can be retained as its short signed Möbius sum, and the original marked-prime projector can either be retained exactly or treated with the explicit error (2). The common \(W\), exact density and both original gauges remain. In the unit-cofactor case the ordinary norm still contains \(D/C=D\) at \(C=1\). For two prime lengths comparable to \(\sqrt D\), the older \(RP^2\) alternative still does not provide the required gain. Thus the central split-prime pairing with small cofactors needs a different estimate. The whole-prefix candidate \(109/144\), whole signed \(13/12\), global unsigned \(9/8\), short/principal assembly, determinant and zero-location by scope, Lean and GRH remain open.

The new finite checks compare the two actual coprimality projectors with the short signed inversion, preserve split-conjugate labels and test the joint exponent budgets and endpoint signs. They do not test the analytic norm theorems or claim a lower bound on the signed pairing.
