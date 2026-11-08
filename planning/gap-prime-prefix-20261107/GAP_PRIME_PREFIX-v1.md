# Prime prefixes inside the two gap factors

Author draft, 7 November 2026 UTC. Independent review is pending. The prefix comparison uses the pending (Q) operator bound. The estimate for the squarefull part of the frequency uses the inherited physical and cubic norms. The exact selection and comparison formulas are finite.

## 1. Actual signed kernel and the parts to estimate

Use the original coprime far-from-cutoff gap pairing of HIGH_CUTOFF_GAP_PAIR-v1, with the two single-column gauges and every original scalar as in cbk:exact-kernel, cbk:two-gauges and mixed (2) with required precisions 6fed549f and 7d62d6c9. Work in \(\mathbb Q(\omega)\). Keep the fixed \(S\) containing the primes above \(2,3\), the fixed literal \(u_0,\nu\) and source/ray data, the original nonprincipal two-pivot unweighted block, \(H\le D^{3/4}\), \(Nu_0 A_1 A_2^2\le H\), and the other four good factors equal to the unit. Use \(2D/7\le U^2\le D\), \(1\le X\le D^{3/8}\), and \(D^{13/40}\le R\le D^{27/80}\) with the actual clip \(R\le Nr<2R,\ Nh\,Nr\le X\). We use \(D\ge2^{128}\) for the final prime-factor classification. This explicit threshold exceeds the bound needed below. The full common fixed smooth complex \(W\) on \([1,2]\), zero at both endpoints, is retained.

Put \(U_*=U(1+D^{-1/32})\). A column \(m\) has the signed original coefficient \(\mu(m)\#\{xy=m:Nx,Ny>U_*\}\), with ordered factors, and the factors are good squarefree and coprime since \(m\) is squarefree. Its other factors include its own gauge and \(g(m)=\prod_{\mathfrak p\mid m}(1-1/N\mathfrak p)\). Both original columns are coprime. The scalar still has the true \(r\)-dependent phase, the principal sixth-part density factor \(\kappa_S(X/(Nh\,Nr))^{1/6}\), the original \(h,k,\ell,e,v_2\), primitive \(S\), source and capacity factors, and the exact finite \(k\) selectors including \((k,v_2)=1\) and the pre-\(S\) cap. No other source component is inserted. The principal-density term has already used the original \(s\) masks in its derivation. Its separate Bessel and counting errors do not enter this note.

The two actual column selections are defined before any \(d\) lift. Put
\[
 T_0=D^{1/24},\qquad T_1=D^{3/10}.
\]
Totally order good prime ideals by norm, with a fixed tie order on ideals. For an actual factor \(x\) choose the prefix of its increasing list of prime divisors whose product first reaches norm \(T_0\). The prefix exists because \(Nx>U_*>T_0\). Call a factor selectable when this prefix has norm at most \(T_1\). First select the ordered factorizations in which either factor is selectable. The disjoint choices are the first factor selectable, and the second factor selectable with the first failing. For the latter we may exchange the two labelled factors within the column, placing the condition of failure on the unselected factor. This exchange does not change the single-column phase at \(m=xy\). We also select the remaining factorizations with large total small cofactor, as defined in Section 4. Every one of these selections retains divisor-bounded multiplicity per column.

## 2. An exact separation of the two comparisons

For integers \(a,b\in[0,N]\) use the cyclic group of order \(M_0=2N+1\). Let \(F(j)\) be one on residues \(1,\ldots,N\) and zero on all other residues. Then
\[
 \mathbf1_{a>b}=F(a-b)=\sum_{\ell\bmod M_0}\widehat F(\ell)
               e^{2\pi i\ell a/M_0}e^{-2\pi i\ell b/M_0},
 \quad
 \widehat F(\ell)=M_0^{-1}\sum_{j=1}^{N}e^{-2\pi i\ell j/M_0}.
\]
The geometric sum gives \(|\widehat F(\ell)|\ll1/\min(\ell,M_0-\ell)\) for \(\ell\ne0\) using the representatives \(0,\ldots,M_0-1\). The zeroth coefficient is bounded by one, so the total absolute mass is \(O(\log(2N))\). The formula includes equality, which returns zero. Reversing the arguments gives the strict reverse comparison. The cyclic support is disjoint from the representatives of all negative differences in \([-N,-1]\).

Suppose \(x=p_0 a_0\) with \(p_0\) proposed as the selected prefix. Its exact selector consists of
\[
 T_0\le Np_0\le T_1,\quad N(p_0/\mathfrak p_{\max}(p_0))<T_0,
 \quad \operatorname{rank}\mathfrak p_{\max}(p_0)<
             \operatorname{rank}\mathfrak p_{\min}(a_0).
\]
In addition the original \(x\) cutoff is \(Na_0>\lfloor U_*/Np_0\rfloor\). The first two conditions depend solely on \(p_0\). The rank comparison uses a last rank above every supported prime for \(a_0=\mathcal O\). Use ranks of all prime ideals up to \(2D\), a finite set of size \(O(D)\) by ideal counting, enlarged by that sentinel. Both the rank comparison and the integer cutoff comparison therefore have the above exact separated form with \(N=O(D)\). Equal norms are not merged. The original real cutoff \(U_*\) is used in the floor, so integer equality produces the correct zero. The two Fourier sums have total absolute mass \(O(\log^2(2D))\). All per-factor comparators below use this same elementary finite argument, independent of \(r\).

## 3. A selectable factor controls the paired part

Apply the full signed common divisor lift over \(d\) to the separated columns. Only the single-column factors are extended in the auxiliary pair. On \(E=Nd\le D^{1/96}\), assign its primes among the disjoint actual factors \(p_0,a_0,y\), so \(d=d_p d_a d_y\), \(p_0=d_p p\), \(a_0=d_a a\), \(y=d_y b\) and \(m=d p a b\). This is the unique assignment for each actual tuple and \(d\). All residual factors are separately coprime to \(d\). Apply the two comparisons of Section 2 on the original \(p_0,a_0\), with each \(d\)-factor fixed. After their finite Fourier separation the \(p\) vector and the vector indexed by \(w=ab\) separate. The \(w\) coefficient is the sum over its actual disjoint factorizations and retains the separate \(y\) cutoff and, when present, failure of its prefix. Its pointwise multiplicity is bounded by the number of divisors of \(w\). The p-only prefix constraints use \(d_p p\) literally. The common \(W(E Np Nw/D)\) separates by the inherited Mellin integral with norm \(M(W)\). All fixed finite selectors and translations use the original expansions. These operations cost at most \((DH)^\varepsilon\) for each required positive \(\varepsilon\), by allocating smaller losses to the finite steps. The density \(g(m)\) factors on the disjoint support.

At each \(p\) dyad, up to fixed dyadic constants,
\[
 D^{1/32}=T_0 D^{-1/96}\le Np\le T_1,\qquad Nw\asymp L/P,
 \quad L=D/E,\quad P\asymp Np .
\]
The original weight \(W\) restricts \(Nw\) to a fixed interval of this size in each dyad. Gauss CRT on the actual \(p,w\) supports puts \(\chi_{3,w}(\alpha_p)\) with the original \(\overline{R_w(r)}\), giving the literal \(\overline{R_w(rp^4)}\). The fixed shifted numerator \(dk\) and the factor \(\overline{R_p(r)}\) keep their raw zeros, so in particular the joint row labels are live only for \((p,r)=1\). The original finite factors at \(r\) do not get evaluated at \(rp^4\). The short and long vectors have the same inverse-square-root weights and divisor bounds used in the proof of (Q), with \(E^{-1/2}\) outside. The \(w\) vector is independent of \(p,r\) in each separated term. The use of (Q) is conditional on that earlier operator comparison. It allows a general divisor-bounded coefficient on \(w\), as in the grouped-column application of PRINCIPAL_DENSITY_MACRO_SPLIT-v1.

The normalized squared column norm on the \(r\) band is bounded, before the common pairing and its density factor, by
\[
 \frac{M(W)^2(DH)^\varepsilon}{E}
       [L/P+RP(R+P)+(RL)^{2/3}]
 \ll \frac{M(W)^2(DH)^\varepsilon}{E} D^{39/40}.
\]
The four exponents are at most \(31/32,\ 39/40,\ 15/16,\ 107/120\). Constants absorb the dyadic endpoints. Sum the divisor assignments, dyads and the two disjoint selections by the same allocated losses. Use the other actual vector or any of its selected parts in the ordinary sixth-free norm, with square bounded by \(O(B_W^2(DH)^\varepsilon D/E)\). The short selection may occur in either column. Express this union as the selected first column paired with the full second, plus the complementary first column paired with the selected second. Apply bilinear Cauchy in \(r\), including the actual bounded phase and the density upper factor \((X/(Nh R))^{1/6}\). Its factor excluding \(h\) is at most \(D^{1/120}\). Use the finite logarithmic \(d\) sum, the original finite \(k\) weight and \(\ell,e,v_2\) sums with capacity, and the convergent positive \(h\) majorant with \((Nh)^{-1/6}\). With normalization and \(A_1 A_2\le H/A_2\), the contribution for small \(d\) is
\[
 \ll (B_W+M(W))^2(DH)^\varepsilon H D^{-1/240},
\]
since \(1/80-1/120=1/240\). For \(E>D^{1/96}\) apply the inherited physical comparison to the same selected original coefficients, with \(O(B_W^2 D^\varepsilon/E)\) coefficient mass and direct unit treatment at \(D<E\le2D\). As in the preceding tail estimate this costs \(O(B_W^2(DH)^\varepsilon H D^{-1/480})\). No assumption of cancellation in that tail is needed. The estimates are for original signed selected terms with the coprime projector intact.

## 4. Small cofactors in both large factors

A failed prefix on \(x\) crosses from a product \(c_x\) of norm below \(T_0\) to a product above \(T_1\) by appending one prime ideal \(q_x\). This prime has norm \(>T_1/T_0=D^{31/120}\). A further prime would have at least that norm by the exact ordering. Its product with \(q_x\) would exceed \(D^{31/60}\), but \(Nx\le2D/U\le\sqrt{14}\,D^{1/2}\). Since \(D^{1/60}>\sqrt{14}\) for \(D\ge2^{128}\), the prefix is the entire \(x=c_x q_x\). Consequently \(Nq_x>U_*/T_0\gg D^{11/24}\) and \(Nc_x<T_0\), with the large prime unique. Conversely if an actual \(x>U_*\) consists of a prime and a cofactor below \(T_0\), the prime has this lower bound and is last, and the greedy prefix is the entire \(x>T_1\). The same holds for \(y\).

For factorizations where both prefixes fail, next select \(N(c_xc_y)\ge T_0\). This is an exact disjoint continuation of the selection in Section 3. In the small \(d\) range \(d\) cannot contain either large prime. Assign it to the two small cofactors \(d=d_x d_y\). Use
\[
 p=(c_x/d_x)(c_y/d_y),\qquad w=q_x q_y
\]
as the short and long residual groups. Now \(T_0/E\le Np<T_0^2\le T_1\). Fixing \(d_x,d_y\), the two original far cutoffs become \(Nq_x>\lfloor U_*/Nc_x\rfloor\) and \(Nq_y>\lfloor U_*/Nc_y\rfloor\). Separate both by Section 2 and include the actual \(Nc_x,Nc_y<T_0\) and their product constraint in the short coefficient. The long vector retains the actual ordered prime ideal factors. For each \(p,w\) the separate short and long assignment sums have divisor-bounded multiplicity. No ordering comparator is needed here since the large prime is unique on the actual support. The same Gauss CRT, all raw zeros, common Mellin profile and (Q) give the same bound as in Section 3 for this selected part, also when only one column admits this split. The physical large-\(d\) tail continues to apply. Thus the joint contribution from the two selection steps is \(O((B_W+M(W))^2(DH)^\varepsilon H D^{-1/480})\).

The remaining original ordered factorization in each column has precisely
\[
 (x,y)=(c_xq_x,c_yq_y),\qquad
    N(c_xc_y)<D^{1/24},\qquad q_x,q_y\text{ prime ideals}.
\]
This includes unit cofactors and distinct split prime ideals of equal norm. It is an exact restriction on the ordered factorization coefficient. An original column can have several such factorizations or none. No positivity or lower bound for the pairing follows.

## 5. A separate estimate for the squarefull frequency part

Write \(r=r_1 u\), where \(r_1\) contains exactly the valuation-one primes and \(u\) contains all positive valuations \(2,\ldots,5\). Select \(Nu\ge D^{1/32}\) before either column selection above, so the total reduction is disjoint. This part can be bounded on the full far gap pairing using the inherited cubic and physical norms alone. There are \(O(Y^{1/2})\) squarefull ideals through \(Y\), by writing each as \(b^2 c^3\) with \(c\) squarefree and summing the upper count \(O(Y^{1/2}\sum_c (Nc)^{-3/2})\). For each \(u\), the number of admissible \(r_1\) is \(O(R/Nu)\) when \(Nu\le2R\). Thus the number of these \(r\) is \(O(R D^{-1/64})\). This counts distinct ideals, allowing actual further masks to reduce the count.

On small \(d\), use the shifted two-factor representation of HIGH_CUTOFF_GAP_PAIR-v1 with \(d=d_xd_y\). At fixed \(r\) both vectors are bounded by the inherited cubic estimate at lengths \(O(\sqrt D)\), giving \(O(M(W)(DH)^\varepsilon E^{-1/2}D^{1/3})\) per column including the divisor allocations. The actual \(r\) symbols and full density factors are retained before this bound. With the exact sign and density present in the pairing, multiply the two pointwise bounds, count the selected \(r\), and use the same finite outer comparisons. The result is bounded by a constant times
\[
 (B_W+M(W))^2(DH)^\varepsilon H\, D^{-1/3-1/64} X^{1/6}R^{5/6}
 \ll (B_W+M(W))^2(DH)^\varepsilon H D^{-1/192}.
\]
Here \(R\le D^{27/80}\) and \(X\le D^{3/8}\) give \(1/96-1/64=-1/192\). The large-\(d\) part costs \(O(B_W^2(DH)^\varepsilon H D^{-1/480})\) by the inherited physical comparison, retaining the same actual \(r\) selection. This estimates a separate part of the actual gap pairing. The valuation-one majority case, including squarefree \(r\), remains.

## 6. Remaining term

For the stated central high-cutoff band the exact surviving coefficient restricts each ordered factorization to two prime ideals with combined small cofactor norm \(<D^{1/24}\), and \(r\) to squarefull part norm \(<D^{1/32}\). The removed part costs \(O((B_W+M(W))^2(DH)^\varepsilon H D^{-1/480})\) subject to (Q) for the prime-prefix steps. The transfer from the original central density still requires the earlier pending inputs in HIGH_CUTOFF_GAP_PAIR-v1. When both cofactors are units, the two actual prime ideals on each side can still have comparable lengths \(\sqrt D\). The generic physical bound still permits its \(D\) term and the earlier joint bound still permits the \(RP^2\) term. A positive count of the small cofactors alone gives no estimate for this signed prime pairing. The whole-prefix candidate remains \(109/144\), and the whole signed \(13/12\), global unsigned \(9/8\), short/principal assembly, determinant and zero-location by scope, Lean and GRH remain open.

The new checks should compare the greedy selectors against independent ordered prefixes, verify exact rank and integer-cutoff comparison including ties and wrap, check the remaining prime/cofactor classification on actual ideal examples, and verify the power budgets. These tests address finite identities. The analytic operator comparison still requires independent review.

## 7. The small-prefix part from the inherited primitive comparison

For the exact sub-selection \(Np_0\le D^{1/8}\) in Section 3 and the entire combined-cofactor selection in Section 4, the same argument can use mcs:ordinary instead of (Q). After short-variable Cauchy the long vector is independent of \(p,r\) and is tested against the literal \(\overline{R_w(rp^4)}\). On the actual live set \((p,r)=1\), every good prime of \(\operatorname{rad}(r)p\) has valuation \(1,\ldots,5\) in \(rp^4\). The good part of the primitive conductor is exactly that radical product and the fixed \(S\)-part is bounded. The raw zeros on good \(w\) therefore agree with the primitive character. Given the good conductor, each prime has at most six possible allocations to \(p\) or to one of the five \(r\) valuations. This bounds the multiplicity in the ordinary primitive norm by a divisor loss. It is the true-conductor comparison, applied here to the separated vectors with the new selectors.

The resulting squared column budget inside \(E^{-1}\) is \(L/P+(RP)^2\). On \(P\ll D^{1/8}\) it is \(O(D^{31/32})\), since \(R\le D^{27/80}\) gives \((RP)^2\ll D^{37/40}\). In Section 4 the shorter bound \(Np<T_0^2=D^{1/12}\) always applies. Thus on these exact original selections the small-\(d\) paired contribution saves \(1/64-1/120=7/960\) relative to \(H\), with the same fixed profile and subpower factors. The inherited tail gives \(H D^{-1/480}\) after restoring all \(d\). The expanded range up to \(T_1\) still uses pending (Q), while this smaller selection and the squarefull frequency estimate do not require it.
