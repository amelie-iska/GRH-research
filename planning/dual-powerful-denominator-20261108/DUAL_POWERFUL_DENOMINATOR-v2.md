# Counting sixth powers in the reduced dual denominator

8 November 2026 UTC. Author draft for independent review. Two sparse sets of actual reduced denominators give further positive bounds for the full original cutoff coefficient.

## Setting and count

Use the original nonprincipal unweighted two-pivot Eisenstein rows and all fixed data of REDUCED_DUAL_WINDOW-v2. In particular \(Q_u=N\mathfrak f_u\asymp R=A_1A_2\), \(1\le R\le H\le D\), \(U^2\le D\le7U^2/2\), and the same common smooth complex \(W\) is supported on \([1,2]\). Retain the complete ordered cutoff allocation \(\beta_{d,U,Z}\), \(1\le Z\le U^2\), including \(Z=U^2\) for the full coefficient. Keep the fixed physical ray, squarefree and capacity conditions. The estimates concern the actual residual from that note:
\[
 X'>B_*,\qquad K_0<Nk\le MD^\eta,\qquad
 Nb>K_0,\qquad Na>L_0,\qquad (Na>P_0\text{ or }Nb>T_0).
\]
Here \(z=e_0z_0,\ g=(z_0,k)\) is an ideal gcd, \(z_0=g a,\ k=g b\). The exact phase is \(|\psi_u(g)|^2\psi_u(a)\overline{\psi_u(b)}\), with \((a,b)=1\). The prior deletion notation \(E_i,E,X,X',J,J',M\) and the original row factors are retained. In particular \(M=REJ/X<2R\) on terms with nonzero primal support, \(M\ge RJ'/D\) and \(J'=J/E_0\). The primitive Poisson root \(\gamma_u\), conjugation, \(Q_u\), and full radial profile \(G_W(XNk/(E Nz Q_u))\) remain in the exact amplitudes.

Write the unique decomposition
\[
 b=\mathfrak s\,b_0 v^6,\qquad
 \mathfrak s\text{ supported on }S,\qquad
 (b_0v,S)=1,\qquad b_0\text{ sixth-free}.
\]
Each valuation away from \(S\) is divided by six with its remainder in \(\{0,\ldots,5\}\). Overlap of \(b_0\) and \(v\), or of \(b\) and \(g\), is allowed. The exact character is still the conjugate of \(\psi_u(b)\) including its zeros. On the good factors, the sextic part of \(\psi_u(v)^6\) is a mask and the \(\nu(v)^6\) phase remains, which need not equal one. At primes in \(S\) keep the primitive value \(\psi_u(\mathfrak s)\), including zero. We use this decomposition only for counting and do not replace character values.

Let \(T\ge1/2\) and count ideals in \(T/2<Nb<2T\) with either \(Nb_0\le B_0\) or \(Nv\ge V_0\), with \(B_0,V_0\ge1\). Additional restrictions can only decrease the count. The two counts satisfy
\[
 B_{\rm core}(T)\ll T\min\{1,(B_0/T)^{5/6}\},\qquad
 B_{\rm power}(T)\ll T V_0^{-5}.                                     \tag{1}
\]
For the first, fix \(\mathfrak s,b_0\) and count \(v\) using \(N v\le(2T/(N\mathfrak s\,N b_0))^{1/6}\). Use the ideal count \(O(Y)\) for \(Y\ge1\), with zero if \(Y<1\). Then sum \((N\mathfrak s)^{-1/6}\) over the fixed finite set of prime generators of the \(S\)-supported monoid, meaning over all their products with arbitrary nonnegative valuations. This converges by geometric series. The sum of \((Nb_0)^{-1/6}\) up to \(B_0\) is \(O(B_0^{5/6})\) by partial summation, even when enlarged to all ideals. Intersect with the unrestricted ideal count. For the second, fix \(\mathfrak s,v\), count \(b_0\) by \(O(T/(N\mathfrak s(Nv)^6))\), and sum. The convergent \(S\)-sum and \(\sum_{Nv\ge V_0}(Nv)^{-6}\ll V_0^{-5}\) give (1). All counts are of ideals with multiplicity across equal-norm labels.

## Transfer to the original row amplitudes

In dyads \(K\le Nk<2K,\ C\le Ng<2C\), let \(P=J'/C,\ T=K/C,\ y=K/M\), and \(F=\sqrt{X A_2}/(E_0\sqrt{E_1})\). A live term has \(P,T>1/2\) and \(T/2<Nb<2T\). Fix \(g,b\) and apply the same separated profile and cutoff-column sieve as in REDUCED_DUAL_WINDOW-v2, (3). All masks on \(a\), including \((a,b)=1\), \((a,g)=1\), and any required exclusion from the prior rectangle, are selectors independent of \(u\). The shared gcd zero and \(\overline{\psi_u(b)}\) remain row contractions. The row coefficient \(Q_u^{-1/2}\gamma_u\) and Fourier phase in \(Q_u\) remain outside the column sum. For a denominator set of size \(B(T)\) for each fixed \(g\), the count \(O(C B(T))\) replaces \(O(CT)\) and yields the bound
\[
 (DH)^\epsilon\mathcal M_{12}(W) F
 \sqrt{\Phi(A_1,\max(1,P))}
 \frac{B(T)}{\sqrt T}\,\sqrt y(1+y)^{-4},                             \tag{2}
\]
where \(\Phi(A,B)=A+B+A^{5/6}B^{1/3}+A^{1/3}B^{5/6}\). This uses the pinned cutoff-column comparison for arbitrary ideal coefficients as in the cited note. It uses the ordinary ideal count on the denominator and leaves the full radial oscillation in the Fourier representation.

### Short sixth-free core

Select \(Nb_0\le B_0\) and \(Na\le L\), where \(1\le B_0,L\le D\). Put \(L_*=\min(L,Z)\), \(B=DB_0/R\ge1\), and define
\[
 \Psi(A;B,L_*)=
 \sum_{(c,\alpha)}
 c\,\min(B,L_*)^\alpha
       \max(1,L_*/B)^{(\alpha-2/3)_+},
 \qquad
 (c,\alpha)\in\{(A,0),(1,1),(A^{5/6},1/3),(A^{1/3},5/6)\}.
\]
In a live dyad \(P\le2L_*\). Also \(y\le DT/(RP)\) by \(M\ge RJ'/D\). Using \(y(1+y)^{-8}\le\min(1,y)\), the scalar in the square of (2) after removing \(\Phi\) is bounded by
\[
 \frac{B_{\rm core}(T)^2}{T} y(1+y)^{-8}
 \ll B_0\,t\min(1,t^{-5/3})\min(1,(B/P)t),\quad t=T/B_0 .
\]
For \(h=B/P\) the product after \(B_0\) is at most \(\min(1,h^{2/3})\). If \(h\ge1\), bound both factors by one. If \(h<1\), use the three intervals \(t\le1,\ 1<t\le h^{-1},\ t>h^{-1}\). The respective upper bounds are \(h\), \(h t^{1/3}\le h^{2/3}\), and \(t^{-2/3}<h^{2/3}\). For \(P\ge1\), maximizing each power \(P^\alpha\min(1,(B/P)^{2/3})\) over \(P\le L_*\) gives precisely the term of \(\Psi\). Enlarging the upper endpoint to \(2L_*\) costs a bounded factor by the degrees. The subunit case \(1/2<P<1\) uses \(\Phi(A_1,1)\) and is covered by the same upper bound.

With the same outer harmonic and dyadic sums as before this proves
\[
 \frac{\|V_d^{\rm core}\|_2^2}{D}
 \ll_{\epsilon,\eta}
 \frac{(DH)^\epsilon\mathcal M_{12}(W)^2 A_2}{Nd}
 B_0\Psi(A_1;DB_0/R,L_*).                                           \tag{3}
\]

### Large sixth-power factor

Select \(Nv\ge V_0,\ Na\le L,\ Ng\ge G_0\), with \(1\le G_0\le Z\); the latter condition can be omitted by setting \(G_0=1\). These selectors may also exclude the short-core piece to make the two parts disjoint. At fixed \(g,b\) the only added condition involving \(a\) is its exact norm cutoff. Now \(P\ll\min(L,Z/G_0)\) and \(T=K/C\le 2yR/C\ll yR/G_0\). Apply (1) in (2) and use bounded \(y^2(1+y)^{-8}\). This gives
\[
 \frac{\|V_d^{\rm power}\|_2^2}{D}
 \ll_{\epsilon,\eta}
 \frac{(DH)^\epsilon\mathcal M_{12}(W)^2 A_2 R}{Nd\,G_0 V_0^{10}}
 \Phi(A_1,\min(L,Z/G_0)).                                           \tag{4}
\]
For both estimates the count of frequency and gcd dyads is logarithmic by \(K\le2R D^\eta\) and \(C\le2J'\). Sum over \(e_1\) at divisor cost and \(e_0\) with the harmonic weight \(1/E_0\) in \(F\). For \(N r\) in a dyad its ideal count absorbs the \(1/Nr\) in \(\sqrt X\). The remaining cutoff dyads are logarithmic. Subpowers absorb all these sums and the harmonic sum over \(d\) in the positive quantity. The final estimates are uniform over the actual row conductor variations, squarefree allocations, and endpoint masks in this scope.

## Critical powers and the unresolved part

Take \(H\asymp D^{3/4}, Z=U^2,\eta=1/16\) with the prior critical cutoffs. The threshold \(L=D\) includes all \(a\) here because \(Na\le Nz\le Z\le D\).

* Pure \(A_1\asymp D^{3/4}, A_2\asymp1\). Use \(B_0=1,L=D\) in (3). The four exponents in order of the terms of \(\Phi\) are \(3/4,1/2,17/24,7/12\). Thus the entire residual with \(b=\mathfrak s v^6\) meets \(D^{3/4+\epsilon}\). Equation (4) with \(V_0=D^{13/120},L=D,G_0=1\) also meets the target for every core on that large-power set. The \(A_1^{1/3}D^{5/6}\) sieve term has power \(13/12\) before the large-power saving. The trial cutoff \(D^{1/10}\) gives \(5/6\) in (4).
* Mixed \(A_1\asymp D^{5/12}, A_2\asymp D^{1/6}\). Use \(B_0=D^{1/100},L=D^{17/20}\) in (3). The maximal power is \(67/90\), from the linear monomial. With \(B_0=1\) the same method reaches \(L=D^{11/12}\) at target \(3/4\). Allowing \(L=D\) for \(B_0=1\) gives \(7/9\) in this budget. The obstruction is the loss from summing the sixth-power ideals with no cancellation when \(T\asymp R P/D\) and \(P\asymp D\). This is an upper-bound limitation.
* At mixed, (4) with \(V_0=D^{1/12},L=D^{33/40},G_0=1\) has power \(107/144\). With \(V_0=D^{1/12},L=D,G_0=D^{1/12}\) it meets \(3/4\), using \(A_2R\ll H\) on feasible blocks. The slack mixed powers \(67/90\) and \(107/144\) stay below \(3/4\) when the pivot log exponents vary by at most \(1/2000\) in either direction subject to capacity.

Adding these pieces by the positive norm triangle still leaves the prior largest controlled power \(67/90\) at the slack mixed cutoffs and \(3/4\) at pure. The exact leftover is the prior large reduced window with the stated sparse sets removed. In particular sixth-free large denominators survive. The signed cross budget still gives \(329/360\) at mixed and \(11/12\) at pure by absolute Cauchy, above the target. Independent review remains pending for this draft and its immediate inputs. The whole signed bound, determinant, zero-location and analytic Lean obligations remain open.
