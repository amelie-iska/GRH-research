# A cutoff on the full intermediate divisor, and the resulting small-divisor problem

8 November 2026 UTC. Author checked; independent review pending. The purpose is to identify the remainder of the **whole original raw \(h=1\) A–A form** after a target-size tail, not just to bound another isolated band. The same smooth multiplier is transported through every exact branch of the intermediate-divisor decomposition. A refinement of the powered row comparison gives a below-\(U\) cutoff on a region of pivot sizes. For that region the entire remaining expression is annular, with no short-density remainder. Acceptance requires the product rather than the \(f\)-only selector, exact row and column masks and endpoints, the weighted two-rough-prime correction, and the shortened-pivot power bounds.

## 1. Exact cutoff transport

Use rma:core and sw:mobius: \(K=\mathbb Q(\omega)\), fixed \(S\) containing the primes above \(2,3\), fixed unitary multiplicative \(\nu\), one common smooth complex \(W\) supported on \([1,2]\) and vanishing at the endpoints, and the complete original good squarefree annulus. Assume \(U\ge7\), \(U^2\le D\le7U^2/2\) and \(1\le H\le D^{3/4}\). Analytic norm estimates below concern the original unweighted two-pivot rows, with \(u_0\) fixed and the good outside-\(S\) ideal \(v_1v_2^2\), at \(A_i\le Nv_i<2A_i\), capacity \(H_b\le H\), retaining all literal, ray and squarefree selections and all raw zeros. Fixed literal classes may be treated separately. Write \(R=A_1A_2\), \(M=\max(A_1,A_2)\), and \(B=\|W\|_\infty\). The exact identity itself allows the original nonnegative row weights in rma:core.

Take a fixed smooth \(0\le\psi\le1\), zero on \((0,1]\) and one on \([2,\infty)\), and let \(\rho=1-\psi\). Write \(M_j(g)=\max_{0\le i\le j}\|(x\partial_x)^i g\|_\infty\). For either \(g=\psi\) or \(g=\rho\) and scale \(Y\ge1\), insert \(g(Nd/Y)\) on the full good squarefree intermediate divisor \(d\) in sw:mobius. Call the **unnormalized** result \(\mathcal B_g(Y)\). In this full \(d\) sum the residual \(a,b\) may overlap across sides; \((d,abuS)=1\) remains. The exact partition gives
\[
 D S_1^{AA}=\mathcal B_\rho(Y)+\mathcal B_\psi(Y).
\]
In the rough decomposition of rma:core the identical multiplier gives
\[
 \mathcal B_g(Y)=K_0[g(Nf/Y)]-K_T^\times[g;Y]+C_2^\times[g;Y]. \tag{1}
\]
The notation on \(K_0\) means insertion of \(g(F/Y)\), \(F=Nf\), into its signed \(U\)-smooth sum. In the **original** \(K_T^\times\), a term indexed by \(f,p,u\) instead has multiplier \(g(FP/Y)\), \(P=Np>U\); keep \((f,u)=1,\ p\nmid u\), and the residual deletion \((a,p)=1\). The original coprimalities \((a,f)=1\) and the character zeros remain. In \(C_2^\times\) the multiplier is \(g(PQ/Y)\) on the original unordered pair of two distinct rough prime ideals, including conjugate ideals of equal norm, with both original row masks.

Indeed the common \(d\)-phase cancels only on its raw live support. On writing \(d=fe\) with the actual smooth \(f\) and rough \(e\), the common cutoffs in \(A_U\) cannot use primes in \(e\), so \(A_U(fea)=A_U(fa)\) on the squarefree live columns. The multiplier depends on the full divisor and is unchanged while completing the residual squares. For \(e=1,p,pq\) this gives the three different arguments in (1) and signs \(+,-,+\). In the third case the residual pair is the unit pair and \(f=1\), as in rma:exact: three rough primes are impossible in the active high window, and two rough primes with any further good factor exceed \(2D\). This is not an expansion by the gcd of the original coprime columns. Placing the same \(f\)-only multiplier on both terms in (1) would in general change the sum.

Two exact support consequences are useful:
* If \(2Y\le U\), then \(\mathcal B_\rho(Y)=K_0[\rho(Nf/Y)]\). Both rough contributions are zero; every live small divisor is automatically \(U\)-smooth.
* If \(2Y\le U^2\), the \(\rho\)-weighted two-prime correction is zero. Any remaining rough-prime term has \(FP<2Y\), hence \(F<2Y/U\). The endpoint is strict because \(\rho=0\) at and above \(2\).

## 2. The positive short error after product transport

Replace \(K_T^\times\) by \(K_S^\times\), restoring exactly the two usual masks, retaining the same product multiplier. For \(0\le g\le1\) the proof of rma:mask applies term by term and gives \(O(B^2 R)\) after division by \(D\), under the unweighted block and capacity above. To see why the new argument makes no extra assumption, on \(p\mid u\) bound the same restored squares by \(O(B^2D^2/(F^2P^2))\), then sum \(F^{-2}\) and the at most one good rough prime of a row. If \(p\nmid u\), an active removed residual with \(p\mid a\) requires \(F P\,Na<2D\le7U^2\); since \(P>U\), this forces \(f=1,a=p\). The difference of squares is then bounded by \(O(B^2D/P)\); summing \(P\) uses only \(U<P<\sqrt{2D}\) and ideal counting. The multiplier was constant across both residual amplitudes of each \((f,p,u)\), so no extra terms have been created. The unordered distinct correction, when present, remains the original weighted correction, not an ordered product with a diagonal.

The transported continuous object for \(g=\rho\) is
\[
 Q_g^\times(t;Y)=
   \sum_{f\ U\text{-smooth}}\mu(f)g(Ft/Y)
            \sum_{u:(f,u)=1}|T_f(t;u)|^2,\qquad
 \mathcal J_g^\times(Y)=\int_U^\infty Q_g^\times(t;Y)\frac{dt}{\log t}.
\]
The \(f\) sum is still over good squarefree ideals. The prime replacement is exactly
\[
 K_S^\times[g;Y]-\mathcal J_g^\times(Y)
 =-E_S(U)Q_g^\times(U;Y)
   -\int_U^\infty E_S(t)\,(Q_g^\times)'(t;Y)\,dt. \tag{2}
\]
Here \(E_S(t)=\pi_K^S(t)-\operatorname{Li}_2(t)\) with the inclusive prime count, so the lower term enforces \(P>U\), not \(P\ge U\). In contrast to a bump vanishing at \(t=U\), the endpoint of this remainder can be nonzero.

If the pinned fixed-field input gives \(E_S(t)\ll_{S,\eta} t^{7/8+\eta}\), the same absolute error bound as before holds uniformly in \(Y\):
\[
 |K_S^\times[g;Y]-\mathcal J_g^\times(Y)|/D
 \ll (DH)^\epsilon M_1(g)M_1(W)^2
               U^{-1/8}\Phi_6(H_b,CD/U). \tag{3}
\]
Indeed \(t\partial_t g(Ft/Y)\) has uniform norm \(M_1(g)\), with no \(F\) or \(Y\) cost. At each \(t\ge U\), \(FNa<2D/t\le7U\) on active columns; the exact short coefficient is of absolute value one. The two coefficient vectors for \(T_f,tT_f'\) have squared masses \(O(M_1(W)^2D/(Ft))\). Apply the unweighted physical norm inside their positive row comparisons on the original live rows; if \(D/(Ft)<1/2\) the term is zero, and unit lengths use the elementary unit count. Summing \(1/F\) up to \(2D/t\) costs \(O(\log(2D))\). Bounding the resulting monotone \(\Phi_6(H_b,CD/t)\) by its value at \(U\), the endpoint and integral in (2) both give \(U^{-1/8+\eta}\), with \(\eta\) absorbed in \((DH)^\epsilon\). Thus the exponent at \(H\asymp D^{3/4}\) is \(35/48\) as before; the novelty here is its validity for the joint **product** selector. This is a conditional application of the same fixed-field input as GAP_NORM_STRIP_AND_PIT-v1. In the rough-free case of §1 no prime-distribution hypothesis is used.

## 3. A signed gain for the middle powered-sieve monomial

The full \(\mathcal B_\psi(Y)\) (no upper smoothness restriction) is estimated by the two-cell signed argument and shortened-pivot comparisons of MATCHING_CELL_TAIL-v2 and MIXED_SUB_U_BAND-v2. We keep the exact high-window \(A_U=G-\mu\), the \(1,2,4\) labelled cell decomposition, dyadic opposite matching, the two strict signed prefixes, the overlap Möbius ideal \(\ell\), and the entire prime-power deletion with union radicals. The log transform of the selector, multiplied by the fixed local bump on the product of the dyadic variables, costs \(O(M_4(\psi))\); the phase and endpoint rules are unchanged. The preceding powered bound took the middle term \(L\min(A_1',A_2')\) with no deletion gain. A different admissible majorant gives a second option for it.

Label the original smaller/larger pivot scales \(A_-,A_+\), using a fixed tie order, with frozen prime norms \(q_-,q_+\) assigned to these original indices by the literal valuation of the row. Thus the shortened scales \(A_-',A_+'\) are comparable to \(A_-/q_-,A_+/q_+\) on nonempty families; a length in \((1/2,1)\) may be set to 1 at bounded cost. Their order may reverse. Nevertheless
\[
 L\min(A_-',A_+')\le L(A_-')^{5/6}(A_+')^{1/6}
 \ll L A_-^{5/6}A_+^{1/6}\,q_-^{-5/6}q_+^{-1/6}. \tag{4}
\]
The powered row estimate only enters after both signed prefixes are taken, in positive norms for the two original subsequences. This is not a change of row weight in a sieve. Let \(M_S(x)\ll_{S,\sigma}x^\sigma\) for fixed \(5/6<\sigma\le1\). In the new term (4), a singly placed row prime receives at least \(1/6\) from its shortened pivot, so its local exponent is \(\sigma+1/6>1\). A singly placed column prime receives \(1/2\) in the coefficient masses. A prime repeated in both tuples has exponent at least \(2\sigma>1\) before any radical gain. No radical is counted twice. Bounded valuation/placement multiplicities and all higher powers sum in a convergent Euler product. As in the original two-cell argument, the overlap sum converges by \(2\sigma>1\); for a single moving cell it is absent. The other two monomials of the powered sieve already have a row exponent at least \(2/3\) in each pivot. The full deletion prefactor from the frozen cells and \(\ell\) is a subpower, not a conductor-free assumption on a varying primitive character.

After division by \(D\) the remaining signed factor is \(Z^{-(1-\sigma)}/Nd_0\) in all three monomials, where \(Z\) is the product of the moving cell dyadic lengths and \(d_0\) the frozen product. Since \(Z\ge F_{\rm box}^{1/2}\) and \(F_{\rm box}>Y/16\), summing the frozen harmonic weight and the dyads gives
\[
 \frac{|\mathcal B_\psi(Y)|}{D}
 \ll (DH)^\epsilon M_4(\psi)M_4(W)^2
 Y^{-(1-\sigma)/2}\!
 \left[R+(D/Y) A_-^{5/6} A_+^{1/6}
             +(D/Y)^{2/3}R/M^{1/3}\right]. \tag{5}
\]
This middle option may be worse than the old no-gain bound \( (D/Y)A_-\); either is legitimate. In particular the no-gain proof does not imply a saving on \(A_-\) without the larger geometric majorant. Formula (5) and the physical branch of MATCHING_CELL_TAIL-v2 are estimates of the same actual full signed tail; the smoothness restriction on \(f\) in (1) is not imposed in a Mertens prefix.

## 4. Conditional reduction of the complete original form

At \(H\asymp D^{3/4}\) let \(A_i\asymp D^{a_i}\) with \(a_1,a_2\ge0,\ a_1+2a_2\le3/4\) (fixed feasible constants), and use \(\sigma=7/8+\eta\) for all \(\eta>0\), under the pinned fixed-field hypothesis, with smaller \(\eta\) absorbed in \(\epsilon\). Put \(m=\min(a_1,a_2)\), \(b=\max(a_1,a_2)\), \(s=m+b\) and \(Y\asymp D^y\). The three powers in (5) are
\[
 s-y/16,\qquad 1+(5m+b)/6-(17/16)y,\qquad
 2/3+s-b/3-(35/48)y.
\]
Consequently an available cutoff exponent is
\[
 y_{\rm loc}
 =\min\!\left\{\frac{10}{19},
       \max\!\left(0,\frac{16}{17}\left(\frac14+\frac{5m+b}{6}\right),
             \frac{48}{35}\left(s-\frac b3-\frac1{12}\right)\right)\right\}. \tag{6}
\]
The first branch is the physical two-cell bound at the critical line. This expression gives sufficient cutoffs, not necessary bounds. On the feasible region \(s\le3/4\) and \(5m+b\le3/2\): if \(a_1\le a_2\), then \(5a_1+a_2=(a_1+2a_2)/2+9a_1/2\), with \(a_1\le1/4\); if \(a_1\ge a_2\), use \(a_1+5a_2=(a_1+2a_2)+3a_2\) with \(a_2\le1/4\). Thus the middle cutoff in (6) is at most \(8/17\). In particular:
* For \(s-b/3\le43/96\), \(y_{\rm loc}\le1/2\). One can take \(2Y\le U\), choosing a small fixed multiple of \(U\) at equality. This region contains the entire \(a_1\le a_2\) wedge, where \(s-b/3=a_1+2a_2/3\le5/12\), and it contains all feasible \(a_1\ge a_2\) with \(a_2\ge5/32\), since \(2a_1/3+a_2\le1/2-a_2/3\). At \((a_1,a_2)=(5/12,1/6)\) the cutoff is \(D^{52/105}\), and at \((1/4,1/4)\) it is \(D^{8/17}\). Here the **entire** original normalized form reduces to
\[
 S_1^{AA}=\frac{K_0[\rho(Nf/Y)]}{D}+O_{S,\nu,\epsilon,W,\psi}(H(DH)^\epsilon).
 \tag{7}
\]
All rough prime and semiprime branches are included in the signed tail bound, not estimated separately or omitted. This reduction needs only the pinned Mertens consequence, not the PIT consequence.
* For the pure point \((3/4,0)\), (6) gives \(Y=D^{10/19}\). There \(2Y<U^2\) at sufficiently large scales, so only the product-cut \(f,p\) rough term can remain alongside the small smooth annular term. The prime version follows exactly with \(K_T^\times[\rho;Y]\). With the extra pinned fixed-field prime discrepancy and the mask error, one may instead write
\[
 S_1^{AA}
 =\frac{K_0[\rho(Nf/Y)]-\mathcal J_\rho^\times(Y)}{D}
       +O_{S,\nu,\epsilon,W,\psi}(H(DH)^\epsilon).
 \tag{8}
\]
This remaining short term is supported on \(Nf<2Y/U\ll D^{1/38}\) and \(U\le t<2Y/Nf\). At \(f=1\) the integrand and the Stieltjes endpoint need not vanish. The same reduction works with the corresponding \(Y\) at other points outside the rough-free region. No estimate on this remaining continuous term or on its pairing with the annulus is asserted.

All statements about fixed-field powers are conditional on the same pinned source as COHERENT_J_TAIL-v1 and GAP_NORM_STRIP_AND_PIT-v1. With elementary \(\sigma=1\) one can still use the prior full tail at \(Y=D^{5/8}\) and the exact discrete product transport, but that does not give the critical mixed cutoff below \(U\). The new statement is a localization of the signed problem, including the sharp structural disappearance of the short remainder in (7). It does not bound the localized small annular sum, in particular \(f=d=1\), prove the pure pairing, improve the whole \(13/12\) or global \(9/8\) exponents, or establish any zero-free, determinant, Lean or GRH result. The next analytic step in the rough-free region is a bound for the actual small signed annular sum in (7), retaining the common profile and original phases; elsewhere the product-selected short term in (8) must also be retained.

## 5. Elementary localization on the cubic-dominant wedge

There is also a conclusion with **no fixed-field \(7/8\) hypothesis**, using the already inherited powered sieve. Take the absolute \(d\)-triangle of sw:divisor-budget on the support of \(\psi\) (or \(\sigma=1\) with the preceding no-gain middle term). The normalized full tail is bounded by
\[
 (DH)^\epsilon B^2\{R+(D/Y)A_-+(D/Y)^{2/3}R/M^{1/3}\}.
\]
This includes nonsmooth \(d\); no claim of sign gain is made here. The sufficient cutoff is
\[
 y_0=\max\{1/4+m,\ (3/2)(s-b/3-1/12)\}.
\]
If \(s-b/3\le5/12\), then \(y_0\le1/2\) since \(m\le1/4\). In that region use \(Y\asymp D^{y_0}\) with \(2Y\le U\), choosing a fixed fraction of \(U\) at \(y_0=1/2\). Equation (7) follows with no use of the fixed-field Mertens or prime-counting powers. This covers the whole feasible \(a_1\le a_2\) wedge, including the balanced endpoint. At the balanced point the elementary cutoff is a fixed fraction of \(U\); the conditional tilted comparison improves the exponent from \(1/2\) to \(8/17\). At the earlier mixed point the elementary leading cutoff is \(13/24>1/2\), so it does not give a rough-free remainder there. This corollary concerns the smaller support of the remaining problem, not an elementary bound on the whole signed form.
