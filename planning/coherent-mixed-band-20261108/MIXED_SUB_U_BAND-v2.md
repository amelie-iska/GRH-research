# A smooth sub-\(U\) annular and continuous band in the mixed block

8 November 2026 UTC. Author checked; independent review pending. This note bounds a specified part of the actual coherent main on the original unweighted two-pivot block. It uses the two signed moving-cell prefixes of MATCHING_CELL_TAIL-v2, but retains the actual two pivot lengths through each row deletion. This makes it possible to move below \(U\) in the mixed block. The result is conditional on the same fixed-field Mertens hypothesis for its power saving; it uses no variable-conductor Mertens input. Acceptance requires the strict original annulus and gaps, correct valuation-dependent row shortening, and an exact common selection in the annular and density terms.

## 1. Same smooth divisor selection in the actual terms

Work over \(K=\mathbb Q(\omega)\), with fixed \(S\) containing the primes over \(2,3\), fixed \(\nu\) as in rma:core, and the one complex \(W\in C_c^\infty\) supported on \([1,2]\), vanishing at its endpoints. Use \(U\ge7\), \(U^2\le D\le7U^2/2\). The original unweighted rows have fixed literal \(S\)-supported factor and good \(v_1v_2^2\), with \(v_1,v_2\) squarefree and coprime, \(A_i\le Nv_i<2A_i\), and all their actual capacity, ray and other row restrictions. Set \(R=A_1A_2,\ M=\max(A_1,A_2)\), \(B=\|W\|_\infty\). A bounded fixed literal multiplicity is separated into its classes. Write \(M_4(W)=\max_{0\le j\le4}\|(x\partial_x)^j W(x)\|_\infty\).

Choose fixed smooth functions \(0\le\psi,\xi\le1\) on \((0,\infty)\), with \(\psi=0\) on \((0,1]\), \(\psi=1\) on \([2,\infty)\), \(\xi=1\) on \((0,1/2]\), \(\xi=0\) on \([1,\infty)\). Let
\[
 \lambda(F)=\psi(F/Y)\xi(F/U),\qquad 1\le Y\le U.
\]
The four log derivatives of the factor have uniform bounds depending on the two fixed profiles; denote their maximum including order zero by \(C_\lambda\), or use the corresponding product bound uniform in \(Y,U\). For \(K_0,K_S,\mathcal J\) of rma:Kzero, rma:KS and cmr:joint, denote by \([\,\lambda\,]\) insertion of this identical scalar multiplier on the original smooth divisor \(f\) of norm \(F\). It multiplies the signed \(\mu(f)\), not a column or a row weight. The comparison concerns exactly the resulting summands in \(K_0-\mathcal J\) and \(K_0-K_S\).

On the support of the selector, \(Y<F<U\), every prime of \(f\) has norm \(<U\). Hence \(K_0[\lambda]/D\) is **exactly** the full intermediate-divisor annular form with multiplier \(\lambda(Nd)\), including all original residual overlap, row masks and character phases. This assertion does not replace the smooth projector at \(F>U\), and does not reinterpret \(K_S[\lambda]\) as a selector on \(N(fp)\): the multiplier in \(K_S\) remains on \(f\) only. The unit at the lower end and the \(F=U\) endpoint both have zero selector.

## 2. Powered row sieve after the full joint deletion

Suppose \(M_S(x)=O_{S,\sigma}(x^\sigma)\) for \(x\ge1\), \(2/3<\sigma\le1\). With the inherited powered two-pivot comparison sw:divisor-budget, mcs:block-bound, we obtain
\[
 \frac{|K_0[\lambda]|}{D}
 \ll (DH)^\epsilon C_\lambda M_4(W)^2
 \left[
 Y^{-(1-\sigma)/2}
 \left(R+\frac{R}{M^{1/3}}(D/Y)^{2/3}\right)
       +\frac{R}{M}\frac{D}{Y}
 \right]. \tag{1}
\]
The constants include the fixed data and the Mertens hypothesis. This is an upper bound for the actual signed band, with no lower-bound or sharp-cutoff claim.

To prove (1), keep the exact high-window identity \(A_U=G-\mu\) on the active annulus, where \(G=\mu\tau_{>U}\) counts ordered pairs of factors of norm strictly above \(U\). For each of the four pairings, use the allocation into 1, 2 or 4 cells of the preceding notes. In a four-cell dyad choose the pair of opposite cells whose scale product is at least the square root of the full dyadic product \(F_{\rm box}\); in a two-cell dyad choose the larger cell, and in a one-cell dyad choose it. Let \(r\) be the number moving (one or two), \(Z=\prod_{i=1}^r X_i\) their dyadic scale product, \(d_0\) the product of the frozen ideals, \(F_0=Nd_0\), \(L=D/(F_0Z)\). Live boxes have \(F_{\rm box}>Y/16\), \(Z\ge F_{\rm box}^{1/2}\), \(L\ge1/2\), and \(L\ll D/F_{\rm box}\).

The exact disjoint-cell Möbius inversion and Mellin steps are those of MATCHING_CELL_TAIL-v2 §§2–3, with the following selector substitution: on \(v_i=Nc_i/X_i\in[1,2)\), separate \(\lambda(F_0Z\prod v_i)\) in the log product, using a fixed compact bump equal to one on \([0,\log4]\). The weighted absolute Fourier integral of order two costs \(O(C_\lambda)\) by four integrations by parts; both scales of the selector are just log translations before the product rule. No derivatives of the strict gap indicators are taken. Each gap threshold is local to one moving cell and its two labelled factors; exact one-sided finite Fourier comparisons assign a tied maximum once. Use the signed modulated prefix on its actual strict or half-open interval, with both endpoints as in that note. Column norms with the same rational value remain different ideals. The signs and product masks on the original \((f,a),(f,b),(f,u)\) stay in the identity.

Let \(\ell\) be the overlap Möbius ideal for the two moving cells, \(E=N\ell<2\min_i X_i\); put \(E=1\) with no summation for one cell. Expand the outside deletion into full prime powers \(h_i\) and four placements per prime relative to \(S\cup\operatorname{supp}(d_0\ell)\). Write \(r_u,r_a,r_b\) for the union radicals across the tuples. A prime assigned to a row in one tuple and to a column in another gives zero before taking the norm, because the latter placement requires its absence from the row. The raw characters remain zero at every common prime, whether or not it is mentioned in a placement.

Now freeze the actual valuation \(1\) or \(2\) of each prime in \(r_u\), writing \(r_u=g_1g_2\) with the primes of \(g_j\) in \(v_j\). Then \(v_j=g_jv_j'\); each frozen factor is a fixed raw column multiplier including its zeros, and the residual row map is injective for this fixed assignment. Put \(q_j=Ng_j\). The surviving row lengths are comparable to \(A_j/q_j\) when nonempty: this quantity is \(>1/2\) since \(q_j\le Nv_j<2A_j\). For \(A_j/q_j<1\) only a bounded unit interval is needed, and replacing its scale by 1 changes the powers by fixed factors. The same fixed primary/ray data give the unweighted powered norm on the remaining positive subsequences, using at most a bounded dyadic refinement; all original remaining restrictions may be enlarged only inside those positive norms. The frozen part does not introduce arbitrary row weights. Use \(CL\ge1\) for the column length when \(L\in[1/2,1)\), with the actual unit counted directly. In particular column squared masses have factors \(O((DH)^\epsilon L/Nr_a)\) and \(O((DH)^\epsilon L/Nr_b)\), with empty side when the corresponding norm exceeds \(2L\). The annular ordered divisor labels have only divisor-bounded multiplicity.

Write \(j_*\) for an index of a largest original pivot, resolving equality once. Then the three terms of the powered bound for the shortened pivots are bounded up to constants by
\[
 \frac{R}{q_1q_2},\qquad
 CL\,\frac{R}{M},\qquad
 (CL)^{2/3}\frac{R}{M^{1/3}}\,
      q_{j_*}^{-2/3}q_{3-j_*}^{-1}. \tag{2}
\]
For the second, \(\min(A'_1,A'_2)\) is at most the original smaller length. For the third, \(R'/M'^{1/3}=\min((A'_1)^{2/3}A'_2,A'_1(A'_2)^{2/3})\) is bounded by the orientation of the **original** larger pivot even if the shortened ordering flips. A loss of row power on the middle term is not ignored.

After combining the signed prefixes, use the powered norm and Cauchy in the actual rows. Before the absolute placement sum, the factor multiplying (2), summed over at most \(2^{\omega(r_u)}\) valuation assignments, is
\[
 \frac{Z^\sigma L}{E^{r\sigma}(\prod_i Nh_i)^\sigma\sqrt{Nr_a Nr_b}},
\]
apart from \((DH)^\epsilon C_\lambda M_4(W)^2\). This keeps the complex profiles and row phases through the signed scalar reduction. In the first and third terms of (2), any singly placed row prime receives at least \(2/3\) from the frozen pivot. Any singly placed column prime receives at least \(1/2\) from the respective column mass. A repeated prime receives at least \(2\sigma\) already from the two powers; a radical is never squared merely because a prime is repeated. Thus the joint local sums converge with the bounded placement and valuation multiplicities, and \(\sum_\ell E^{-2\sigma}\) converges in the two-cell case. The fixed-field deletion prefactor \((EF_0)^\epsilon\) is absorbed by taking smaller internal epsilons.

For the middle term, do not claim a row radical gain. Sum the positive row placements with the separate finite limits \(Nh_{u,i}\le2X_i/E\). This costs \((Z/E^r)^{1-\sigma+\epsilon}\), including the logarithmic endpoint \(\sigma=1\), by ideal counting. The column placement sum still converges. The residual overlap weight is \(E^{-2}\) for two cells, up to the common subpower, so it is summable. No infinite divergent Euler factor is used. Divide by \(D=F_0 ZL\). For the first and third terms the factor is \(Z^{\sigma-1}/F_0\); for the middle it is \(1/F_0\). The frozen-cell sum of \(1/F_0\) is bounded in each dyad by elementary ideal counting. Summing the logarithmically many boxes gives (1). In particular the gain \(Y^{-(1-\sigma)/2}\) was not applied to the whole powered norm.

## 3. Actual density and prime terms on this band

For either of the other terms the elementary estimate suffices:
\[
 \frac{|K_S[\lambda]|+|\mathcal J[\lambda]|}{D}
 \ll B^2 R\,\frac{D}{YU}. \tag{3}
\]
Indeed on their support \(t\ge U\), every active ideal \(g=fa\) obeys \(Ng<2D/t\le7U\). It is good and squarefree. Hence the exact short-coefficient identity gives \(|A_U(g)|=1\) there, including a unit if it occurs. This fact is used only on the short side, not on the annulus. There are \(O(D/(Ft))\) residual ideals whenever \(D/(Ft)\ge1/2\); below this threshold there is no active ideal. Retain the original masks in \(T_f(t;u)\) before taking this upper bound. There are \(O(R)\) original rows. The absolute bound for a fixed \(f\) and \(t\) after division by \(D\) is therefore \(O(B^2R D/(F^2t^2))\), with \(|\lambda|\le1\). Sum \(F>Y\) by the \(O(Y^{-1})\) ideal tail. For \(K_S\), sum the prime ideals with \(Np>U\) by the \(O(U^{-1})\) ideal tail; for \(\mathcal J\), integrate \(t^{-2}/\log t\) from \(U\) with the same upper bound. This does not use prime distribution or discard a PIT endpoint from an identity: the actual two original objects have each been bounded. All auxiliary raw restorations in \(K_S\) stay as explicitly defined there. No additional mask correction in the full decomposition is declared absent.

## 4. Mixed powers, stability and limitation

Use the Mertens hypothesis \(7/8+\eta\) for every \(\eta>0\), as derived conditionally in COHERENT_J_TAIL-v1 §4 from the pinned fixed-field input; take a smaller internal \(\eta\) into \(\epsilon\). At \(H\asymp D^{3/4}\), \(A_1\asymp D^{5/12}, A_2\asymp D^{1/6}\) with feasible constants, put \(Y=D^y\). The three annular powers in order \(R,(R/M)D/Y,(R/M^{1/3})(D/Y)^{2/3}\) are
\[
 7/12-y/16,\qquad 7/6-y,\qquad 10/9-(35/48)y.
\]
The other two selected terms in (3) have power at most \(13/12-y\). At \(y=52/105<1/2\) each is at most \(3/4\). At \(y=199/400<1/2\) the maximum is \(8621/11520\), with margin \(19/11520\) below \(3/4\). For example, the same sufficient target holds for both pivot log exponents within \(1/2000\) of \(5/12,1/6\), respectively, subject to the actual capacity, at \(y=199/400\). In fact the leading exponent increases by at most \((2/3+1)/2000=1/1200<19/11520\); the other exponents have larger slack. The band is nonempty as a real interval at large scales since \(2Y<U/2\) eventually, though this is not an energy lower bound.

With \(\sigma=1\) this argument needs \(y\ge13/24>1/2\) for the leading term, so it gives no nonempty target-size sub-\(U\) band there. With a sharp largest-cell selector and the same powered monomial, the analogous sufficient threshold is \(104/201>1/2\), so it does not give this sub-\(U\) consequence either. The smooth two-cell gain and actual pivot lengths are both used. For comparison, at the pure scale \(A_1\asymp D^{3/4}, A_2\asymp1\), the powered branch leading term at \(y=1/2\) has exponent \(77/96>3/4\); the earlier physical branch has \(73/96>3/4\). No target-size pure band follows. None of these budgets is a necessary lower bound on the actual sums.

The uncovered small-divisor region (in particular \(f=d=1\)), the remaining transition near and above \(U\) (see §5), the far-norm Gauss pairing, and the whole coherent main remain open. This is a selected piece of the original \(K_0-\mathcal J\) and \(K_0-K_S\) with common smooth \(f\)-weights, not a new whole signed bound, determinant/zero-location result, Lean proof or GRH claim.

## 5. A matched band above \(U\)

There is a different exact pairing at the upper transition. Let \(\beta\in C_c^\infty((0,\infty))\) be fixed, supported in \([1,c]\) with \(1<c<7\), and take \(0\le\beta\le1\). In particular \(\beta(1)=0\). Put
\[
 K_0[\beta_U]=\sum_{f\ U\text{-smooth}}\mu(f)\beta(Nf/U)
                      \sum_{u:(f,u)=1}|T_f(1;u)|^2 .
\]
The other masks, good squarefreeness, and the original \(T_f\) are as in §1. Define \(P^T_{1,\beta}\) by retaining only \(f=1\) in \(K_T\) and multiplying its rough prime terms by \(\beta(Np/U)\). Define \(P^S_{1,\beta}\) analogously in \(K_S\); the latter restores the two masks exactly as in rma:KS. Define
\[
 J_{1,\beta}=\int_U^\infty\frac{\beta(t/U)}{\log t}
                       \sum_{u}|T_1(t;u)|^2\,dt .
\]
Here the new multiplier on the short side is on the **prime or density variable**, unlike §1. The full annular intermediate-divisor band \(\mathcal B_{\beta}\) is the sum on the right of sw:mobius with coefficient type \(A_U,A_U\) and multiplier \(\beta(Nd/U)\), still unnormalized.

One has the exact identity
\[
 K_0[\beta_U]-P^T_{1,\beta}=\mathcal B_{\beta}. \tag{4}
\]
Indeed a nonsmooth good squarefree \(d\) in this band contains a prime \(p\) with \(Np>U\). Any additional nonunit factor would give \(Nd\ge7Np>7U\). Hence \(d=p\), its Möbius sign is \(-1\), and it requires \((p,u)=1\). For either column \(pa\) the raw mask \((p,a)=1\) remains. No divisor involving \(p\) has norm \(\le U\), so the actual ternary cutoff coefficient obeys \(A_U(pa)=A_U(a)\) when \(pa\) is squarefree; there is no extra factor \(\mu(p)\) in this identity. This gives the **exact** \(f=1\) raw prime pairing including the original profiles and complex phases. No product of two rough primes can enter (4). This does not remove the unordered semiprime correction outside the selected band.

The proof of (1) applies to \(\mathcal B_\beta/D\) using lower scale \(Y=U\) and \(\beta\) in place of the selector. The estimate before the sub-\(U\) support identification concerned the full \(d\) form, so this application uses no false smoothness assertion. At the same critical mixed pivots and conditional Mertens exponent, its leading power is \(10/9-(35/48)/2=215/288\), below \(3/4\) by \(1/288\). All other powered monomials are smaller. The same \(1/2000\) pivot neighborhood has slack, since \(1/1200<1/288\).

The extra masks can be charged directly on this band:
\[
 |P^S_{1,\beta}-P^T_{1,\beta}|/D\ll M_0(\beta)B^2 R
 \quad(H\le D^{3/4}). \tag{5}
\]
For \(p\nmid u\), the only possible omitted residual ideal with \(p\mid a\) is \(a=p\), since \(Na<2D/Np<7U\) and any further factor has norm \(\ge7\). Its contribution to the amplitude is \(O(B)\); each of the two amplitudes is \(O(BD/Np)\) by the actual short coefficient bound. Their square difference, divided by \(D\), is \(O(B^2/Np)\). Sum over \(U<Np<cU\) by elementary counting. If \(p\mid u\) the original term is zero and the restored square is \(O(B^2D^2/(Np)^2)\). Each actual row has at most one such good prime since \(H\le D^{3/4}\le (7/2)^{3/4}U^{3/2}<U^2\) for \(U\ge7\). The bound after division by \(D\) is \(O(B^2D/U^2)=O(B^2)\) per row. This proves (5), with exact raw restrictions prior to the upper bound.

If in addition the same pinned fixed-field input gives
\(E_S(t)=\pi_K^S(t)-\operatorname{Li}_2(t)=O_{S,\eta}(t^{7/8+\eta})\)
as in GAP_NORM_STRIP_AND_PIT-v1, the continuous replacement is controlled for this specific band. Apply ordinary Stieltjes integration by parts to
\(B_\beta(t)=\beta(t/U)\sum_u|T_1(t;u)|^2\).
The lower-end term is exactly zero because \(B_\beta(U)=0\); this argument does not discard the lower endpoint of the full unsmoothed prime error. At each \(U\le t\le cU\), the column squared masses for \(T_1\) and \(tT_1'\) are \(O(M_1(W)^2D/U)\), using the actual short coefficient and support. The inherited physical row comparison on these original unweighted rows and Cauchy give
\[
 |t B_\beta'(t)|\ll (DH)^\epsilon M_1(\beta)M_1(W)^2
                   (D/U)\Phi_6(H_b,CD/U).
\]
The integral over this fixed ratio interval yields
\[
 |P^S_{1,\beta}-J_{1,\beta}|/D\ll
 (DH)^\epsilon M_1(\beta)M_1(W)^2\,U^{-1/8}
                  \Phi_6(H_b,CD/U),
\]
where a smaller internal \(\eta\) is absorbed. At the critical line this has power \(19/24-1/16=35/48\), smaller than \(215/288\). With (4)–(5) this bounds the actual **matched** normalized pair
\(K_0[\beta_U]-J_{1,\beta}\) by \(O((DH)^\epsilon M_4(\beta)M_4(W)^2D^{215/288})\) at the mixed scales, after dividing by \(D\). The exact prime version \(K_0[\beta_U]-P^T_{1,\beta}\) needs only the fixed-field Mertens hypothesis. The two hypothesis statements are conditional uses of the pinned source, with no new zero-free theorem.

This result uses the \(f=1\) continuous term only at \(U<t<cU\), and with the same \(\beta\) transported from the **annular divisor** to the **prime/density** variable. It cannot bound an unmatched \(K_0[\beta_U]-\mathcal J[\beta_U]\), or \(K_0\) at \(f=1\), or the remaining \(f=1\) prime range. In particular the matched-band identity does not justify changing the index of any selector in §1.
