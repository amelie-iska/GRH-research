# Small dual frequencies with the full cutoff coefficient

8 November 2026 UTC. Author draft for independent review. This bounds a specified positive amplitude of the actual low-gcd family, retaining the full original cutoff-product range in that amplitude.

## Setting and exact split

Use the original nonprincipal unweighted two-pivot rows of JOINT_CUTOFF_PRODUCT-v1, with fixed \(S,\nu,u_0\) as there and a single smooth complex \(W\) supported on \([1,2]\). In particular \(U^2\le D\le7U^2/2\), \(1\le R=A_1 A_2\le H\le D\), and \(Q_u=N\mathfrak f_u\asymp_{S,\nu,u_0} R\). The good physical part of the row is \(v_1 v_2^2\), not its conductor radical. Keep all original squarefree, literal, ray, coprimality and capacity restrictions. Let \(\Phi(A,B)=A+B+A^{5/6}B^{1/3}+A^{1/3}B^{5/6}\). Use \(\mathcal M_j(W)=\max_{0\le i\le j}\|(x\partial_x)^iW\|_\infty\).

For each intermediate good squarefree \(d\), use the exact cutoff allocations, square-divisor expansion, and deletion split of JOINT_CUTOFF_PRODUCT-v1, §3. In particular \(V_d\) uses the exact signed coefficient of the original ordered cutoff pairs \(Nx,Ny\le U\); one may also use a common upper selector \(N(xy)\le Z\), where \(1\le Z\le U^2\), and/or a lower product selector. Set \(Z=U^2\) for the full coefficient. The allocation on \(z\) is independent of the row, has a divisor bound, and is supported at \(Nz\le Z\); no changes to its signs or endpoints are made. The \(d\) variable belongs to the Möbius inversion, not to the gcd of the original coprime columns.

At fixed \(d,r,e_1,e_0\) and cutoff dyad \(J\le Nz<2J\), use the following scales and exact sum from that proof:
\[
 \begin{gathered}
 E_i=Ne_i,\quad E=E_0E_1,\quad X=D/(Nd\,(Nr)^2),\quad
 z=e_0z_0,\quad J'=J/E_0,\quad X'=X/E_0^2,\quad
 M=REJ/X,\\
 \sum_{z_0}\beta_{d,U,Z}(e_0z_0)\psi_u(z_0)
        \sum_b\psi_u(b) W(E\,N(e_0z_0)\,Nb/X).
 \tag{1}
 \end{gathered}
\]
Here \(e_1\mid\operatorname{rad}(Sd)\), \(e_0\mid z\) with \((e_0,Sd)=1\). The exact outer factors include \(\mu(r)\mu(e)\mathbf1_{(d,u)=1}\psi_u(r)^2\psi_u(e)\psi_u(e_0)\); the fixed column masks, including \((r,Sdz)=1\), remain in the \(z_0\)-subsequence. Zero values of the extended characters are retained. In a live \(z_0\)-subsequence \(J'>1/2\). We may discard entire summands with \(X/(EJ)\le1/2\) since every primal \(b\)-weight is then zero, including at \(2\). For every summand kept, \(M<2R\), and without assuming it is near 1 one has \(M\ge RJ/D\).

Choose \(B_*,K_0\ge1\) and \(\eta>0\). For \(X'\le B_*\) include the entire direct term (1) in \(V_d^{\rm dir}\). For \(X'>B_*\) use the exact radial primitive Poisson formula for its \(b\)-sum. The dual profile is \(G(XNk/(E Nz Q_u))\) with \(G(x)=\widehat h(\sqrt{4x/3}\,e_1^{\rm coord})\), \(h(w)=W(|w|^2)\), and prefactor \(2X\gamma_u/(\sqrt3 E Nz\sqrt{Q_u})\). Here \(\gamma_u\) is the actual Gauss root in the inverse-different trace pairing, and \(e_1^{\rm coord}\) is a unit vector. No zero frequency occurs by nonprincipality. Split the dual ideal labels into
\[
 \begin{array}{ll}
 {\rm low}:& Nk\le K_0,\\
 {\rm mid}:& K_0<Nk\le M D^\eta,\\
 {\rm far}:& Nk>\max(K_0,M D^\eta).
 \end{array} \tag{2}
\]
The middle is empty when \(MD^\eta\le K_0\). All three use \(\overline{\psi_u(k)}\), including the primitive zeros and values on \(S\)-supported frequency factors. These ranges depend only on the deletion and dyad scales and not on \(u\). The character, \(Q_u\) and \(\gamma_u\) are unchanged. Sum with the exact outer factors to get the identity \(V_d=V_d^{\rm dir}+V_d^{\rm low}+V_d^{\rm mid}+V_d^{\rm far}\). The omitted primal-zero summands are discarded before making this split; we do not assert that their separate low projections would vanish. The split is for this specified representation.

## The low estimate

In each dual dyad \(K\le Nk<2K\) intersect the exact frequency selectors (2); the bound does not smooth those selectors. Use the fixed-width log Fourier separation of JOINT_CUTOFF_PRODUCT-v1, §4. The profile mass is
\(O(\mathcal M_{12}(W)(1+K/M)^{-4})\), and \(Q_u^{-it}\) and \(Q_u^{-1/2}\gamma_u\) stay in the row factor. Fix each ideal \(k\) before bounding the \(z_0\)-sum. Its separated coefficient, including \(J/Nz\), has divisor bound and length \(J'\). The all-ideal positive row comparison of that note, §2, gives a row norm at most
\[
 (DH)^\epsilon\sqrt{J'A_2\,\Phi(A_1,\max(1,J'))}.
\]
Multiplication by \(\overline{\psi_u(k)}\) is a contraction of this counting norm. Taking the triangle inequality over the at most \(O(K)\) ideals of the frequency dyad is now cheap on the low range. We do not take the triangle inequality over \(z_0\). With the exact Poisson prefactor bounded using \(Q_u\asymp R\), the fixed-deletion bound is
\[
 (DH)^\epsilon \mathcal M_{12}(W)
 \frac{\sqrt{X A_2}}{E_0\sqrt{E_1}}\,
 \Phi(A_1,\max(1,J'))^{1/2}
 \frac{K}{\sqrt M}(1+K/M)^{-4}.
 \tag{3}
\]
Indeed \(X\sqrt{J' M}/(EJ\sqrt R)=\sqrt{X/(E E_0)}\). All constants in (3) are uniform over the specified block. There is no \(K^\epsilon\) cost: at fixed \(k\) the only sieve is on \(z_0\), and the scalar \(k\)-phase has modulus one.

Set \(B_K=DK/R\ge1\). Since \(M\ge RJ/D\),
\[
 \left(\frac{K}{\sqrt M}(1+K/M)^{-4}\right)^2
 \le K\min(1,B_K/J).
\]
The upper bound by \(K\) follows from \(y(1+y)^{-8}\le1\) for \(y=K/M\); the other follows by discarding the decay factor. All powers of the second argument in \(\Phi\) lie in \([0,1]\). Since \(\max(1,J')\le J\le Z\),
\[
 \min(1,B_K/J)\Phi(A_1,\max(1,J'))
 \le \Phi(A_1,\min(Z,B_K)).
 \tag{4}
\]
For \(J\le B_K\) use monotonicity; for \(J>B_K\) apply the degree bound term by term. Therefore the extra length from increasing the cutoff dyad is absorbed once \(RJ/D\) exceeds \(K\). The dyad sum of \(\sqrt K\) on \(K\le K_0\) is \(O(\sqrt{K_0})\), and the right side of (4) increases with \(K\).

For the direct estimate use the grouped column \(z_0 b\), exactly as in (4) of JOINT_CUTOFF_PRODUCT-v1. For both terms sum over \(e_1\) at divisor cost, \(e_0\) at harmonic cost \(O(\log(2J))\), and over \(r\) on each norm dyad: the \(O(T)\) ideals at \(T\le Nr<2T\) multiply \(\sqrt X\ll\sqrt{D/Nd}/T\). The number of \(r,z\) dyads is logarithmic. This proves
\[
 \frac{\|V_d^{\rm dir}+V_d^{\rm low}\|_2^2}{D}
 \ll_{\epsilon} \frac{(DH)^\epsilon\mathcal M_{12}(W)^2 A_2}{Nd}
 \max\{\Phi(A_1,B_*),\ K_0\Phi(A_1,\min(Z,DK_0/R))\}.
 \tag{5}
\]
The harmonic sum over \(d\) is \(O(\log(2D))\), since \(Nd\le 2D\) before Poisson. It can be absorbed at subpower cost. The same holds with any selector in \([0,1]\) in the positive sum.

## Far tail and the critical blocks

For the far tail use the same separation with exponent 10 in place of 4 and \(\mathcal M_{24}(W)\). Indeed, two log derivatives of \(G(x)\) produce at most two powers of \(\sqrt x\) multiplying Fourier transforms of \(h\) times bounded coordinate polynomials; 22 integrations by parts in the radial frequency direction give decay \(x^{-10}\) for \(x\ge1\). Compact annular support bounds the needed \(L^1\) derivatives by \(\mathcal M_{24}(W)\). At \(x\le1\) use boundedness, and the log cutoff and two integrations in its Fourier transform give the asserted \(L^1\) separation cost. Each dyad intersecting the far range has \(K>MD^\eta/2\). The scalar in (3) with exponent 10 is at most \(\sqrt M(K/M)^{-9}\). Summing over these dyads gives \(O(\sqrt R D^{-9\eta})\) by \(M<2R\), also if \(M D^\eta<1\). Using \(J'\le Z\) and summing the remaining indices as above yields
\[
 \frac{\|V_d^{\rm far}\|_2^2}{D}
 \ll_{\epsilon,\eta}\frac{(DH)^\epsilon \mathcal M_{24}(W)^2 A_2 R}{Nd}
                   \Phi(A_1,Z)D^{-18\eta}.
 \tag{6}
\]
The far sum converges absolutely before the row bound; at no step is the nominal scale treated as actual compact dual support.

At \(H\asymp D^{3/4}\), use \(Z=U^2\), and for the far split take \(\eta=1/16\).
* Mixed \(A_1\asymp D^{5/12}, A_2\asymp D^{1/6}\): with \(B_*=D^{21/40}\) and \(K_0=D^{1/20}\), the direct exponent is \(107/144\) and the low exponent is \(47/72+11/120=67/90\). Both are less than \(3/4\), also when the two pivot log exponents each vary by at most \(1/2000\), with feasible capacities. At the exact mixed exponents one may take \(B_*=D^{8/15}\), \(K_0=D^{7/132}\) to reach \(3/4\) on both. In either case (6) gives \(5/8\) at the exact mixed point, because \(A_2R\ll D^{3/4}\) and \(\Phi(A_1,Z)\ll D\). The same \(5/8\) upper bound holds throughout the feasible mixed neighborhood by capacity \(A_1A_2^2\le H\).
* Pure \(A_1\asymp D^{3/4}, A_2\asymp1\): take \(B_*=D^{3/8}\), \(K_0=1\). The exponents from (5) are \(3/4\) on both branches, and (6) again gives \(5/8\). Here \(K_0=1\) selects the unit dual ideal. This includes all cutoff products in those branches, whereas the previous pure positive estimate for the entire dual sum only reaches bounded products.

Thus the positive sum of squared norms divided by \(D\) for \(V_d^{\rm dir}+V_d^{\rm low}+V_d^{\rm far}\) meets the target in the stated blocks (with \(67/90+\epsilon\) at the exact mixed point for \(K_0=D^{1/20}\)). The exact residual is the middle window (2) with \(X'>B_*\). In the branches \(MD^{1/16}\le K_0\) there is no residual. In particular the bound controls a projection defined by the unused factor's dual frequency, even for cutoff products larger than \(D^{29/120}\); it does not enlarge the product range for the **entire** dual sum.

For \(d=1\) the norm triangle reduces the target to the exact middle amplitude. For the signed sum over \(d\), with the inherited positive comparison of power \(13/12\) for the whole coefficient, a norm triangle for the middle and absolute Cauchy for its cross term give at best the exponents \(329/360\) (mixed with \(K_0=D^{1/20}\)) and \(11/12\) (pure) by these budgets, both above \(3/4\). These are upper comparisons, not lower bounds. The middle amplitude and its signed cross term remain open. No fixed-field power estimate, improved whole-form bound, determinant, zero-location or Lean claim follows.
