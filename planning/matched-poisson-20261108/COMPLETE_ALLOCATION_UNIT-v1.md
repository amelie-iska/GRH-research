# The unit frequency in the signed complete allocation window

8 November 2026 UTC. Use the original pure nonprincipal unweighted two-pivot block, \(R\asymp D^{3/4}\), \(U^2\le D\le7U^2/2\), fixed \(S,\nu,u_0\) and the common smooth \(W\). This is a separate exact calculation inside the equality projection of GROUPED_EQUAL_CROSS-v4. Take \(d=e_1=1\), \(\ell=1\), \(h=re_0\) good squarefree and \(Nh\asymp\sqrt{D/R}\), with fixed positive comparison constants. Let \(X_*=U/Nh\), so \(X_*\asymp D^{3/8}\). Select good squarefree \(g\perp h\) with \(1<Ng\le X_*^2\) and \(z_0=k=g\).

For all sufficiently large \(D\), every \(e_0\mid h\) survives the original primal-zero and middle tests when evaluated at this label. Indeed its \(J\)-dyad obeys \(J/Ne_0\in[Ng/2,Ng]\) up to the endpoint conventions. Thus
\[
 X'=D/(Nh)^2\asymp R>D^{3/8},\qquad
 \frac{X}{Ne_0 J}\ge \frac{D}{(Nh)^2 Ng}\ge D/U^2\ge1,
 \qquad M/Ng\asymp R(Nh)^2/D\asymp1 .
\]
With the original pure lower cutoff \(K_0=1\), this is in the middle for \(Ng>1\). The upper middle condition \(Ng\le M D^\eta\) holds for fixed \(\eta>0\). The unit \(g=1\) has the same exact tests apart from the lower frequency boundary and belongs to the low piece.

Fix an ordered split \(g=g_xg_y\). In the grouped coefficient expand the original ordered cutoffs by assigning the primes of \(h\) to \(h_x,h_y,r\). The sign is \(\mu(g)\mu(r)\) and the predicates are \(Ng_xNh_x\le U,\ Ng_yNh_y\le U\). At least one of \(Ng_x,Ng_y\) is at most \(X_*\) because \(Ng\le X_*^2\). Suppose \(Ng_y\le X_*\). Then the \(y\)-cutoff allows every \(h_y\mid h/h_x\). For fixed \(h_x\), summing \(\mu((h/h_x)/h_y)\) over these \(h_y\) gives zero unless \(h_x=h\), in which case the weight is one and the remaining condition is \(Ng_x\le X_*\). The other case follows by exchanging the roles of the two cutoffs. Hence the grouped coefficient for each such \(g\) is exactly
\[
 \mu(g)\#\{g_xg_y=g:\ Ng_x,Ng_y\le X_*\}.                             \tag{1}
\]
The \(h\)-Möbius sign has already been used in this cancellation. The argument does not replace the signed coefficient by a product for other middle labels.

At fixed \(u,h\) set \(T=S\cup\operatorname{supp}(hu)\) and \(M_T^\#(x)=\sum_{Nv\le x,\ (v,T)=1}\mu(v)/Nv\). The exact \(g\)-row factor \(|\psi_u(g)|^2\) deletes every common good prime with \(u\). The scalar \(1/Ng\) from the original Poisson prefactor and (1) give the middle coefficient
\[
 -1+\sum_{\substack{Nq\le X_*\\(q,T)=1}}
           \frac{\mu(q)}{(Nq)^2}
                \left[M_{T\cup\operatorname{supp}q}^\#(X_*/Nq)\right]^2. \tag{2}
\]
Indeed the full sum over ordered \(g_x,g_y\) is coprime. Möbius inversion imposes this condition and the two remaining squarefree factors stay prime to \(q\). Both are at most \(X_*\), hence their product before the gcd inversion has norm at most \(X_*^2\). Subtracting the simultaneous unit gives the \(-1\). The low piece has exactly the missing \(+1\) on the same \(h,e_1\) slice and with the same \(\psi_u(h)^2\), \(\gamma_u,Q_u\) and common radial profile. All these factors are constant in \(g\) on this projection.

The double sum in (2) is subpower small, uniformly over its original \(h,u\) at the stated scale. Use the previously pinned fixed-field deleted-prime Mertens estimate (7) of DELETED_PRIME_MERTENS_AND_UNIT_CORRECTION-v2. Here \(N\operatorname{rad}(hu)\ll D^C\) for fixed \(C\); adjoining \(q\) with \(Nq\le X_*\) preserves the polynomial bound. For \(x\ge D^\delta\) with any fixed \(\delta>0\), partial summation gives
\[
 M_T^\#(x)\ll (\log(2D))^{C'}\exp(-c\sqrt{\log(2D)})
\]
uniformly for these \(T\). In fact the full harmonic series converges by the fixed-field bound and its Abel limit is \(1/\zeta_K^T(1+0)=0\). Applying partial summation from \(x\) to infinity to the deleted-prime Mertens sum gives the displayed bound; the integral of \(e^{-c\sqrt{\log t}}/t\) loses at most a square-root logarithm at the lower endpoint. For \(Nq\le\sqrt{X_*}\) both harmonic sums in (2) have polynomially large arguments. The inverse square \(q\)-weight is summable. The remaining tail \(Nq>\sqrt{X_*}\) is \(O(X_*^{-1/2}\log^2(2X_*))\) by the elementary ideal count and the trivial harmonic bound. Therefore the middle scalar in this exact window is
\[
 -1+O((\log(2D))^{C''}e^{-c'\sqrt{\log(2D)}}).
\]
The corresponding recombined low and middle scalar has the subpower error alone. In particular an argument seeking an unconditional power saving by bounding this isolated middle scalar against zero cannot work. This is an actual unit boundary effect on a selected window. It does not give a power bound on the recombined whole equality vector, its signed cross, or the generic unequal complement.

