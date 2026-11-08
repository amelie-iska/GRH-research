# Conjugate overlaps in the squarefree dual window

8 November 2026 UTC. Author draft for independent review.

## Exact reduction of the norm ratio

Use the actual remaining middle window of POWERED_DUAL_ROOT-v1 and its inputs. Keep the original unweighted nonprincipal Eisenstein rows, the fixed \(S,\nu,u_0\), \(Q_u=N\mathfrak f_u\asymp R=A_1A_2\), and the same common smooth complex \(W\) supported on \([1,2]\). The cutoff product \(Nz\le Z\le U^2\) and all original ordered cutoffs, \(\beta_{d,U,Z}\), squarefree, capacity, ray, and deletion masks remain. The full coefficient uses \(Z=U^2\), with \(U^2\le D\le7U^2/2\). In each retained summand use the previous notation
\[
 z=e_0z_0,\quad J'=J/E_0,\quad X'=X/E_0^2>B_*,
 \quad M=REJ/X<2R,\quad K_0<Nk\le MD^\eta .
\]
Here \(M<2R\) follows from the prior removal of primal-zero summands, and \(M\ge RJ'/D\). All primitive Poisson prefactors, including \(\gamma_u,Q_u^{-1/2}\), the exact radial profile, and its row-dependent argument are retained.

The first ideal gcd \(g=(z_0,k)\) gives \(z_0=ga,\ k=gb\) with \((a,b)=1\), \(a\) good squarefree. Now put
\[
 \ell=(a,\bar b),\qquad a=\ell a',\qquad b=\bar\ell b',
\]
where the bar on an ideal is the nontrivial automorphism of the Eisenstein field. Every prime of \(\ell\) is split and \((\ell,\bar\ell)=1\). The phase and radial ratio become exactly
\[
 \psi_u(z_0)\overline{\psi_u(k)}
  =|\psi_u(g)|^2\psi_u(\ell)\overline{\psi_u(\bar\ell)}
                    \psi_u(a')\overline{\psi_u(b')},
 \qquad \frac{Nk}{Nz}=\frac{Nb'}{E_0 Na'} .
 \tag{1}
\]
The factor on \(\ell,\bar\ell\) retains its complex phase and both raw zeros. Even when \(\ell\) is good, \(\bar\ell\) can meet \(S\) if \(S\) is not conjugation invariant. The primitive value at that factor stays in (1). The overlap of \(g\) with \(b\), or of \(\bar\ell\) with \(b'\), is allowed unless a separate squarefree selector forbids it.

In fact
\[
 N\ell=\gcd_{\mathbb Z}(Na,Nb),\qquad \gcd_{\mathbb Z}(Na',Nb')=1.       \tag{2}
\]
For an inert rational prime there is one ideal above it and ideal coprimality rules out its simultaneous occurrence. The ramified prime of the field is absent from \(a\) since \(a\) is good. At a split prime, if \(a\) contains both primes above it, neither can occur in \(b\). If \(a\) contains exactly one, a shared rational prime can occur only through the opposite ideal in \(b\). The exponent of the rational gcd is one because \(a\) is squarefree. These cases prove (2) even for arbitrary \(b\), including repeated valuations. Distinct split prime ideals remain distinct in all the coefficients. In particular \(Na=Nb\) is equivalent to \(a'=b'=\mathcal O\), or \(b=\bar a\) on the coprime support.

For a fixed \(g,\ell\), the two remaining coprimality conditions are \((a',b')=(a',\bar b')=1\). All other coprimalities are fixed selectors on one variable, including \((a',g\ell\bar\ell)=1\) and \((b',\ell)=1\). The first condition on \(a'\) means coprimality with the product, without requiring the factors of that product to be pairwise coprime. Prior exclusions involving \(Na\) or \(Nb\) can be kept by splitting \(Na'\) into a bounded number of cells at the inherited numerator thresholds after fixing \(\ell\). On each cell the remaining exclusions are predicates on \(b'\) and fixed data. The original raw zeros and every prior selector remain in the exact amplitude. Additional projections below can be made disjoint by this same finite partition.

## Simultaneous coprimality projector

For the joint estimate expand both conditions by \(\mu(q)\mu(h)\) with \(q\mid a',b'\) and \(h\mid a',\bar b'\). Set
\[
 L_a=[q,h],\qquad L_b=[q,\bar h],\qquad a'=L_a a'',\qquad b'=L_b b''.
\]
The brackets are least common multiples of ideals. Their raw factor is \(\psi_u(L_a)\overline{\psi_u(L_b)}\). In general neither product \(qh\) nor \(q\bar h\) is an admissible replacement for the corresponding least common multiple. Any overlap between \(q,h\), or between \(q,\bar h\), is permitted by the exact projector. The original \(a'\) remains squarefree inside each term, so \(a''\) is coprime to \(L_a\); the corresponding \(b''\) condition is applied only when inherited.

The sum of \((NL_a NL_b)^{-1/2}\) over all supported \(q,h\) is polylogarithmic in \(DH\). For a split conjugate pair with prime norm \(p\), the four binary valuations of \(q,h\) at the pair give at most fifteen nonempty patterns. Each places at least one prime in each least common multiple. Thus the local absolute sum is at most \(1+15/p\). For an inert prime the same argument gives at most \(1+3/N\mathfrak p\). All appearing prime norms are bounded by a fixed power of \(DH\) for fixed \(\eta\). The resulting product is bounded by a constant times a fixed power of \(\zeta_K(1+1/\log(2DH))\) by comparison of local factors, since \(N\mathfrak p^{1/\log(2DH)}\) is bounded on this range. The elementary ideal count \(O(Y)\) bounds this zeta value by \(O(\log(2DH))\). This summation uses both original coprimality conditions without treating the two projectors as independent.

## Positive bounds for the two new shortened lengths

Let \(C\le Ng<2C,\ B\le N\ell<2B,\ K\le Nk<2K\), and put
\[
 P=J'/(CB),\qquad T=K/(CB),\qquad y=K/M,\qquad
 F=\sqrt{X A_2}/(E_0\sqrt{E_1}).
\]
In live dyads \(P,T\) are bounded below by a positive constant. The lengths of \(a',b'\) are \(O(P),O(T)\). Exact \(Q_u\), \(Nz\), \(Nk\) enter the same Fourier separation as in REDUCED_DUAL_WINDOW-v2, with mass \(O(\mathcal M_{12}(W)(1+y)^{-4})\). Keep the phase (1) and the original root and row multipliers as contractions, with \(Q_u^{-1/2}\ll R^{-1/2}\). The \(O(CB)\) choices for \(g,\ell\) give \(CB\sqrt{PT}=\sqrt{J'K}\).

For fixed \(g,\ell,b'\), all the coprimalities are column selectors on \(a'\). The one-column sieve and counting the \(O(T)\) choices of \(b'\) gives the row bound, up to \((DH)^\epsilon\mathcal M_{12}(W)\),
\[
 F\sqrt{T\Phi(A_1,\max(1,P))}\sqrt y(1+y)^{-4}.
 \tag{3}
\]
The corresponding bound for fixed \(g,\ell,a'\) is
\(F\sqrt{P\Phi(A_1,\max(1,T))}\sqrt y(1+y)^{-4}\).
For the joint branch use the exact projector above, then Hölder and the two fourth moments from JOINT_CUTOFF_PRODUCT-v1 on lengths \(P/NL_a,T/NL_b\). Their product contributes the harmonic weight \((NL_a NL_b)^{-1/2}\) and the fourth root of \(\Phi(A_1,\max(1,P^2))\Phi(A_1,\max(1,T^2))\). Subunit live lengths are handled by the unit count. Thus the row bound for this branch is \(F\sqrt y(1+y)^{-4}\) times that fourth root, up to the same subpower and profile seminorm.

Write \(\Phi(A,L)=A+L+A^{5/6}L^{1/3}+A^{1/3}L^{5/6}\). For \(Nb'\le K_1\), use \(T\ll K_1\) and \(y\le DT/(RP)\), since \(M\ge RJ'/D\). With degree at most one in the second argument of \(\Phi\), (3) gives the same optimized cap as the previous single denominator estimate. For \(Na'\le L_1\), use \(P\ll L_1\) and \(T=y E_1 RP/X'\) with \(X'>B_*\). Its \(E_1\) factor cancels the \(E_1^{-1}\) in \(F^2\) by the same degree bound. For the joint rectangle with \(Na'\le P_1,\ Nb'\le T_1\), monotonicity suffices. Finally, if \(Ng N\ell\ge G_1\) with \(1\le G_1\le Z\), then \(P\ll Z/G_1,\ T\ll y R/G_1\), so (3) and bounded \(y^2(1+y)^{-8}\) give a bound for all \(a',b'\) in that sector.

Explicitly, after the \(r,z,e_0,e_1,g,\ell,k\) dyads and harmonic weights as in the previous proofs, each of these projections has squared norm divided by \(D\) bounded by
\((DH)^\epsilon\mathcal M_{12}(W)^2 A_2/Nd\) times its indicated quantity:
\[
\begin{array}{c|l}
 Nb'\le K_1 & K_1\Phi(A_1,\min(Z,DK_1/R))\\
 Na'\le L_1 & L_1\Phi(A_1,\max(1,RL_1/B_*))\\
 Na'\le P_1,\ Nb'\le T_1 &
 [\Phi(A_1,P_1^2)\Phi(A_1,T_1^2)]^{1/2}\\
 Ng N\ell\ge G_1 & (R/G_1)\Phi(A_1,Z/G_1).
\end{array}                                                         \tag{4}
\]
The number of added \(\ell\)-dyads is logarithmic. On a dyad of \(Nr\), its ideal count absorbs \(1/Nr\) in \(\sqrt X\). The divisor bound on \(e_1\) and harmonic sum of \(1/E_0\) preserve the existing factors. Harmonic summation in \(d\) gives the same powers for the positive sum over \(d\).

## Critical ranges and signed remainder

At mixed \(A_1\asymp D^{5/12}, A_2\asymp D^{1/6}\), \(H\asymp D^{3/4}\), \(Z=U^2\), \(B_*=D^{21/40}\), take \(K_1=D^{1/20}\), \(L_1=D^{3/20}\), \(P_1=T_1=D^{21/80}\). The first three powers are respectively \(67/90,\ 11/15,\ 107/144\), now for the **integer reduced ratio** (2). The high overlap \(G_1=D^{8/15}\) also gives \(67/90\) with no upper cut on either original reduced factor. All four remain below \(3/4\) in the feasible \(1/2000\) mixed neighborhood. At the exact mixed point the fourth bound reaches \(3/4\) already at \(G_1=D^{35/66}\). For example, using \(G_1=D^{1/2}\) instead gives \(29/36\) from that bound, which exceeds target.

At pure \(A_1\asymp D^{3/4}, A_2\asymp1,\ B_*=D^{3/8}\), take \(K_1=L_1=1,\ P_1=T_1=D^{3/16},\ G_1=D^{3/4}\). Each power is \(3/4\). The first projection includes the whole equal-norm locus, with exact phase (1), and includes unequal norms when the integer reduced denominator is a unit. In both blocks these results allow squarefree \(b\) and include conjugate pairs with \(g=\mathcal O\). No physical norm or row conductor is replaced in the original Poisson expression.

For the signed sum, let \(V_d^{\rm old}\) be the union of previously controlled pieces and \(V_d^{\rm new}\) the disjoint union selected from the residual by (4). The new contribution and its cross with \(V_d^{\rm old}\) have target-size upper bounds by the positive estimates and Cauchy, with the exact sign \(\mu(d)\) in the signed form. The cross with the uncontrolled remainder is still above target by the available absolute comparison. In particular large \(Na',Nb'\) with trivial or small conjugate overlap remain. Independent review is pending. The whole signed bound, determinant, zero-location and analytic Lean obligations remain open.

## Cross term for the equal-norm locus

Let \(V_d^{\rm eq}\) select \(Na=Nb\) within the actual residual. The joint line of (4) with \(P_1=T_1=1\) bounds its positive energy by \(O((DH)^\epsilon\mathcal M_{12}(W)^2 R)\) after summing over \(d\). This follows because \(\Phi(A_1,1)\ll A_1\) and \(\Phi\) is evaluated at both unit lengths. At mixed the resulting power is \(7/12\). The same bound applies when both reduced integer norms are bounded by fixed constants. The signed cross of this projection with the remaining part of the full amplitude is
\[
 \frac{2}{D}\operatorname{Re}\sum_d\mu(d)
       \langle V_d^{\rm eq}, V_d-V_d^{\rm eq}\rangle .
\]
At the exact mixed scales, the known positive \(13/12\) budget for \(V_d\), followed by the norm triangle and absolute Cauchy in \(d,u\), gives power \(5/6\) for this particular cross. This is smaller than the comparison for all the controlled pieces but exceeds the target.

There is a target-size mixed part of this cross with \(Nd\ge D^{1/5}\). The per-divisor positive estimate of phy:divisor-proof in papers/physical-sieve-details.tex applies to \(V_d\), with its exact coefficient and row masks. Summing it for \(Nd\ge Y\), \(1\le Y\le 2D\), gives, up to subpowers and the fixed profile norm,
\[
 H+D/Y+H^{5/6}(D/Y)^{1/3}+H^{1/3}(D/Y)^{5/6}.
\]
This follows term by term from the ideal sums with powers \(1,2,4/3,11/6\), keeping the unit endpoint when \(D/Nd<1\). At \(Y=D^{1/5}\) and \(H\asymp D^{3/4}\) the four powers are \(3/4,4/5,107/120,11/12\). The energy of \(V_d-V_d^{\rm eq}\) on the tail has the same \(11/12\) upper power by the norm triangle. Its cross with the equal-norm projection therefore has power \((7/12+11/12)/2=3/4\). The cross on small \(d\), in particular \(d=1\), still requires a different estimate. This argument bounds part of a signed cross through an absolute norm comparison.
