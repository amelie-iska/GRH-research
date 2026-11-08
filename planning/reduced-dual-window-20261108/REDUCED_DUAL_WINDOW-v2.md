# Reducing the ideal ratio in the middle dual window

8 November 2026 UTC. Author draft for independent review. This bounds two further pieces of the full original cutoff coefficient. The cutoffs are on the reduced ideal numerator and denominator, and may include dual frequencies beyond the previous low-frequency cutoff.

## Scope and exact partition

Use LOW_DUAL_CUTOFF-v1, including its original unweighted nonprincipal two-pivot Eisenstein rows, fixed \(S,\nu,u_0\), primitive \(\psi_u\), \(Q_u=N\mathfrak f_u\asymp R=A_1A_2\), and the single common smooth complex \(W\) supported on \([1,2]\). Keep literal ray, squarefree, capacity, and common-prime restrictions. Use \(U^2\le D\le 7U^2/2\) and \(1\le R\le H\le D\). Write \(\mathcal M_j(W)=\max_{0\le i\le j}\|(x\partial_x)^i W\|_\infty\) and
\(\Phi(A,B)=A+B+A^{5/6}B^{1/3}+A^{1/3}B^{5/6}\), the pinned physical sieve comparison of phy:input. The column comparison for arbitrary ideals freezes the second physical pivot, sixth factors, and the \(S\)-supported column part; see JOINT_CUTOFF_PRODUCT-v1, §2. It is used only inside positive counting norms on the actual rows.

For each intermediate good squarefree divisor \(d\), keep the exact allocation \(\beta_{d,U,Z}(z)\) of the ordered original cutoff pairs, with \(Nz\le Z\), \(1\le Z\le U^2\). Taking \(Z=U^2\) gives the full coefficient. As before, for fixed \(d,r,e_1,e_0\) and cutoff dyad \(J\le Nz<2J\), put
\[
 X=D/(Nd\,(Nr)^2),\quad E_i=Ne_i,\quad E=E_0 E_1,\quad
 z=e_0 z_0,\quad J'=J/E_0,\quad X'=X/E_0^2,\quad M=REJ/X .
\]
The deletion factors are exactly \(e_1\mid\operatorname{rad}(Sd)\) and \(e_0\mid z\) prime to \(Sd\). Discard primal-zero terms with \(X/(EJ)\le1/2\) before Poisson, so \(M<2R\) on the terms used below. Also \(M\ge RJ/D\). The original row multiplier is
\(\mu(r)\mu(e_0e_1){\bf1}_{(d,u)=1}\psi_u(r)^2\psi_u(e_0e_1)\psi_u(e_0)\); the original column masks are in the \(z_0\) selection and allocation. In the previous middle window \(X'>B_*\), \(K_0<Nk\le MD^\eta\), the exact primitive Poisson summand has scalar
\(2X\gamma_u/(\sqrt3 E Nz\sqrt{Q_u})\), profile \(G_W(XNk/(E NzQ_u))\), and character factor \(\psi_u(z_0)\overline{\psi_u(k)}\). Here \(G_W\) and \(\gamma_u\) are the same radial transform and normalized Gauss factor as in that proof. There is no zero mode by nonprincipality.

Let
\[
 g=(z_0,k),\qquad z_0=g a,\qquad k=g b .
\]
This is an ideal gcd, not an integer gcd of norms. In particular \(g\) is good squarefree and \((a,b)=1\), while \(g\) and \(b\) **can** share primes. The squarefreeness condition still imposes \((g,a)=1\). With primitive zero extension,
\[
 \psi_u(z_0)\overline{\psi_u(k)}
   =|\psi_u(g)|^2\psi_u(a)\overline{\psi_u(b)},\qquad
 \frac{Nk}{Nz}=\frac{Nb}{E_0 Na}.                                      \tag{1}
\]
The multiplier \(|\psi_u(g)|^2\) is essential; it may be zero even when the two reduced factors are units. The exact gcd condition uses \((a,b)=1\), with no new restriction on \((g,b)\). Norm collisions do not identify ideals. An \(S\)-part of \(k\) lies in \(b\), with its exact value or zero.

Within the previous middle window, split into three disjoint sets:
\[
 \mathrm{den}:\ Nb\le K_0;\qquad
 \mathrm{num}:\ Nb>K_0,\ Na\le L_0;\qquad
 \mathrm{rem}:\ Nb>K_0,\ Na>L_0 ,
 \tag{2}
\]
where \(1\le L_0,K_0\le D\). Let \(V_d^{\rm den},V_d^{\rm num},V_d^{\rm rem}\) denote the resulting exact amplitudes. The previous direct, low and far pieces are untouched. In particular a frequency satisfying \(Nk\le K_0\) is still in the previous low piece. Both new pieces can be nonempty at \(Nk>K_0\). Each definition uses the exact inclusive or strict endpoints displayed.

## Bound for the reduced denominator

For \(K\le Nk<2K\) and \(C\le Ng<2C\) let
\[
 P=J'/C,\qquad T=K/C,\qquad y=K/M,\qquad
 F=\frac{\sqrt{X A_2}}{E_0\sqrt{E_1}}.
\]
A nonempty dyad has \(P,T>1/2\). Separate the radial profile by the fixed-width log Fourier cutoff as before. At each Fourier parameter the factors involving \(Q_u,Nz,Nk\) are phases; \(J/Nz\) stays in the bounded \(z\)-coefficient. The row multiplier \(Q_u^{-1/2}\gamma_u\) is used exactly and bounded only after taking the norm. The profile mass is \(O(\mathcal M_{12}(W)(1+y)^{-4})\).

For fixed \(g,b\), the \(a\)-sum has length \(O(P)\), with divisor-bounded coefficients independent of the row. All restrictions, including \((a,b)=1\), are column selectors. The middle frequency selector and denominator cut depend only on \(g,b\) and the fixed dyad, not on \(a\) or the row. Bound the \(a\)-sum by the pinned row comparison, \((DH)^\epsilon \sqrt{P A_2\Phi(A_1,\max(1,P))}\). The factor \(|\psi_u(g)|^2\overline{\psi_u(b)}\) stays a row contraction. There are \(O(C)\) ideals \(g\) and \(O(T)\) ideals \(b\) for each. The triangle over these two indices gives, after multiplication by the profile cost and \(O(X/(EJ\sqrt R))\), the row bound
\[
 (DH)^\epsilon\mathcal M_{12}(W) F
     \sqrt{T\Phi(A_1,\max(1,P))}\,\sqrt y(1+y)^{-4}.                    \tag{3}
\]
This uses \(X\sqrt{J'M}/(EJ\sqrt R)=\sqrt{X/(EE_0)}\). The count \(O(CT)=O(K)\) does not undo the shorter cutoff column \(P\).

On the denominator branch \(T\le 2K_0\), and \(y\le DT/(R(J/C))\) since \(M\ge RJ/D\). Put \(B=DK_0/R\ge1\). Because \(P\le J/C\le Z\) and all powers in the second argument of \(\Phi\) are in \([0,1]\),
\[
 y(1+y)^{-8}\Phi(A_1,\max(1,P))\ll\Phi(A_1,\min(Z,B)).
\]
For \(J/C\le1\) this follows from the bound by \(\Phi(A_1,1)\); otherwise use \(\min(1,2B/(J/C))\) and apply the degree bound term by term. Thus (3) is uniformly bounded with \(T\Phi\) replaced by \(K_0\Phi(A_1,\min(Z,DK_0/R))\) and with no remaining scalar \(y\).

## Bound for the reduced numerator

On the numerator branch, fix \(g,a\). The \(b\)-sum has length \(O(T)\), and its selectors \(Nb>K_0,\ K_0<Ng\,Nb\le MD^\eta,\ (a,b)=1\) are independent of the row. All other selectors on \(a,z_0,z\) remain fixed. The factor \(|\psi_u(g)|^2\psi_u(a)\) is a row contraction; apply the same all-ideal comparison to \(\overline{\psi_u(b)}\), including its exact \(S\)-supported part. The \(O(C)\) choices for \(g\) and \(O(P)\) choices for \(a\) give, by the same prefactor identity,
\[
 (DH)^\epsilon\mathcal M_{12}(W) F
     \sqrt{P\Phi(A_1,\max(1,T))}\,\sqrt y(1+y)^{-4}.                    \tag{4}
\]
In this branch \(P\le2L_0\), and
\(T=y E_1 R P/X'\). Use \(X'>B_*\) to get
\[
 \max(1,T)\le 2E_1\max(1,y)\max(1,R L_0/B_*).
\]
Apply the same degree bound to \(\Phi\). The \(E_1\) factor cancels \(E_1^{-1}\) in the square of \(F\); \(y\max(1,y)(1+y)^{-8}\) is bounded. Thus the numerator sieve budget is \(L_0\Phi(A_1,\max(1,R L_0/B_*))\), with scalar \(\sqrt{X A_2}/E_0\) before squaring. There is no additional loss from a large \(S d\)-deletion factor.

In either estimate \(K\le 2R D^\eta\) and \(C\le 2J'\), so the number of frequency and gcd dyads is logarithmic for fixed \(\eta\). Sum over \(e_1\) at divisor cost, over \(e_0\) with \(\sum(Ne_0)^{-1}\ll\log(2D)\), and over \(r\) at each dyad as before: \(O(L)\) choices for \(L\le Nr<2L\) cancel \(1/L\) in \(\sqrt X\). The remaining cutoff and square-divisor dyads are logarithmic. This proves the uniform bounds
\[
 \begin{aligned}
 \frac{\|V_d^{\rm den}\|_2^2}{D}
 &\ll_{\epsilon,\eta} \frac{(DH)^\epsilon\mathcal M_{12}(W)^2 A_2}{Nd}\,
             K_0\Phi(A_1,\min(Z,DK_0/R)),\\
 \frac{\|V_d^{\rm num}\|_2^2}{D}
 &\ll_{\epsilon,\eta} \frac{(DH)^\epsilon\mathcal M_{12}(W)^2 A_2}{Nd}\,
             L_0\Phi(A_1,\max(1,R L_0/B_*)).
 \end{aligned}                                                       \tag{5}
\]
They hold also in the positive sum over \(d\) with an additional selector in \([0,1]\), absorbing the harmonic sum at subpower cost. Nothing here replaces a signed sum over \(d\) by an equality of positive norms.

## Critical scales and the remaining window

At \(H\asymp D^{3/4}\), take \(Z=U^2,\ \eta=1/16\).
* Mixed \(A_1\asymp D^{5/12}, A_2\asymp D^{1/6}\): set \(B_*=D^{21/40},\,K_0=D^{1/20},\,L_0=D^{3/20}\). The denominator has power \(67/90\). For the numerator the second sieve argument has exponent \(7/12+3/20-21/40=5/24\). The maximum sieve exponent is \(5/12\) (attained by the constant term and \(A_1^{5/6}B^{1/3}\)), so the total numerator exponent is \(11/15\). Both bounds stay below \(3/4\) when the pivot log exponents each vary by at most \(1/2000\) with feasible capacities. At the exact mixed exponents one may use \(B_*=D^{8/15}\), \(K_0=D^{7/132}\), \(L_0=D^{79/480}\): each budget meets \(3/4\).
* Pure \(A_1\asymp D^{3/4}, A_2\asymp1\): set \(B_*=D^{3/8}\) and \(K_0=L_0=1\). Both budgets have power \(3/4\). These include the nonunit middle frequencies \(k\mid z_0\) and \(z_0\mid k\), respectively, with overlap assigned by (2). The exact \(S\)-frequency behavior and repeated good prime powers in \(k\) remain. Equal norm alone does not give either divisibility.

Adding the new pieces to the previous direct, low and far amplitudes by the positive norm triangle leaves their total powers unchanged, up to the same subpowers and the far \(\mathcal M_{24}(W)\) cost. The residual middle window now requires both \(Nk/N(z_0,k)>K_0\) and \(Nz_0/N(z_0,k)>L_0\). In particular the **coprime** portion with both ideals large is still present. At \(d=1\) it is enough to bound that exact residual to reach the full target. In the signed sum the inherited absolute cross comparison still costs \(329/360\) at the exact mixed point with slack cutoffs and \(11/12\) at pure. These are upper bounds and are not target estimates. No improvement in a whole-form exponent, fixed-field power theorem, determinant, zero-location or Lean result follows from (5).

## Joint rectangle in the remaining window

In the branch \(\mathrm{rem}\) of (2), select the exact subregion \(\mathrm{rect}\) where \(Na\le P_0,\ Nb\le T_0\), with \(1\le P_0,T_0\le D\). This is disjoint from the denominator and numerator branches. The joint positive bound is
\[
 \frac{\|V_d^{\rm rect}\|_2^2}{D}
 \ll_{\epsilon,\eta}
 \frac{(DH)^\epsilon\mathcal M_{12}(W)^2 A_2}{Nd}
      [\Phi(A_1,P_0^2)\Phi(A_1,T_0^2)]^{1/2}.                         \tag{6}
\]
In particular the rectangle can reach larger reduced factors than the two single-factor cuts.

To prove (6), fix \(g\) in its dyad and separate the profile exactly as for (3). For this fixed \(g\), the conditions on \(a\) and \(b\) are individually fixed except for \((a,b)=1\). Both factors keep their own upper and lower selectors. Expand the coprime selector by \(\sum_{q\mid a,\,q\mid b}\mu(q)\). For fixed \(q\), put \(a=q a',\,b=q b'\); keep \(\mu(q)|\psi_u(q)|^2\) as a row multiplier. Here \(q\) is good squarefree, may be nonunit, and \(q\) is automatically prime to \(g\) when \(a\) occurs. The restriction \((a',q)=1\) from the squarefreeness of \(a\) remains in the first coefficient. There is no disjointness condition between \(q,b'\), or between \(a',b'\), in the individual expansion term. In particular the two raw zero factors on \(g,q\) stay, and no primitive value at a deleted prime is restored.

At a fixed Fourier parameter, Hölder and the all-ideal fourth moment of JOINT_CUTOFF_PRODUCT-v1, (2), bound the product of the two shortened sums by
\[
 (DH)^\epsilon\frac{\sqrt{PT A_2}}{Nq}
 [\Phi(A_1,P_0^2)\Phi(A_1,T_0^2)]^{1/4}.
\]
Indeed their dyadic lengths are at most constants times \(P/Nq,T/Nq\), and their exact upper support bounds are \(P_0/Nq,T_0/Nq\). If a dyadic length is subunit and nonempty it is at least a fixed positive constant, so the unit count gives the same inequality up to constants. The row comparison on each factor uses the actual phases and masks; the two fourth moments do not identify a reduced ratio with a generic short physical radicand. The exponent \(\epsilon\) absorbs divisor coefficients and constants from fixed \(\eta\) since \(K\ll R D^\eta\).

Sum over \(q\) at harmonic cost. The \(O(C)\) choices of \(g\) give \(C\sqrt{PT}=\sqrt{J'K}\). With the original Poisson prefactor, the row bound is therefore \(F\sqrt y(1+y)^{-4}\) times the fourth-root sieve budget and profile seminorm, up to subpowers. The scalar \(\sqrt y(1+y)^{-4}\) is bounded, and \(E_1^{-1/2}\le1\) in \(F\). The same remaining dyadic and harmonic sums as in (5) prove (6). The decomposition is exact before applying these norm bounds.

At the mixed point \(P_0=T_0=D^{21/80}\) gives power \(107/144\) with the feasible \(1/2000\) pivot neighborhood; at the exact mixed point \(P_0=T_0=D^{4/15}\) meets \(3/4\). At pure \(P_0=T_0=D^{3/16}\) meets \(3/4\). These bounds include pairs in which neither reduced factor is a unit. In all cases one may add the rectangle to the previous controlled pieces without increasing the largest power. The revised exact remaining window is
\[
 X'>B_*,\quad K_0<Nk\le M D^\eta,\quad
 Nb>K_0,\quad Na>L_0,\quad (Na>P_0\ {\rm or}\ Nb>T_0).
\]
The signed cross comparisons at the end of the preceding section remain unchanged. In particular (6) is a positive estimate for a portion of the middle amplitude; it does not bound the coprime portion of the revised residual.
