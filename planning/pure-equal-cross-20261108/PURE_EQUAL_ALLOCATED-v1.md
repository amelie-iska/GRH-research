# Exact cutoff separation and a larger pure equality range

8 November 2026 UTC. Use the full original \(Z=U^2\) ordered cutoff in GROUPED_EQUAL_CROSS-v4, with \(U^2\le D\le7U^2/2\), the same fixed \(S,\nu,u_0\), one smooth complex \(W\) supported on \([1,2]\), original unweighted nonprincipal two-pivot rows, and exact primitive \(Q_u\asymp R=A_1A_2\). Here \(E=Nd\) is the intermediate divisor norm and \(E_1=Ne_1\). For powers take pure \(H\asymp R\asymp A_1\asymp D^{3/4}, A_2\asymp1\).

## Separate the actual sharp allocations

On the equal-norm projection \(z_0=g\ell,\ k=g\bar\ell\), choose \(t\mid\ell\) with \(t,\bar t\) good and \(B\le Nt<2B\), by a fixed deterministic rule depending on \(\ell,U,D\), independent of \(h\) and the row. Freeze \(g,w=\ell/t,e_1,J\). Retain the row multipliers on these fixed labels, including primitive \(S\) values, the root and \(Q_u\). In the grouped coefficient sum over \(e_0\mid h\), expand each original \(\beta_{d,U,U^2}(e_0gwt)\) using SMALL_CUTOFF_PRODUCT-v2:
\[
 \beta_{d,U,U^2}(z)=
 \mu(z)\sum_{d_x,d_y\mid d,\ (d_x,d_y)=1}
   \mu(d_x)\mu(d_y)\sum_{z_xz_y=z}
          {\bf1}_{N(d_xz_x)\le U}{\bf1}_{N(d_yz_y)\le U}.
\]
The \(U^2\) product cap follows from the two individual bounds. Fix \(d_x,d_y\) and an ordered split \(gw=x_0 y_0\), at divisor cost. Write
\[
 h=r h_x h_y,\quad e_0=h_xh_y,\quad
 t=t_x t_y,\quad z_x=x_0h_xt_x,\quad z_y=y_0h_yt_y .
\]
All factorizations within a squarefree ideal are disjoint. On the original support \(\mu(h)\mu(z)=\mu(r)\mu(gw)\mu(t)\), so the signs separate between the two arrays. The cutoff inequalities are
\[
 N(d_xx_0)Nh_xNt_x\le U,\qquad N(d_yy_0)Nh_yNt_y\le U .
\]
The \(J\)-dyad imposes \(J\le Ne_0 N(gw)Nt<2J\). The primal-zero and direct/middle separation tests at fixed \(J\) are \(D Ne_0/(E E_1 J (Nh)^2)>1/2\) and \(D/(E(Nh)^2)>B_*\). Both are on the \(h\)-allocation alone. The lower frequency bound \(K_0<N(gw)Nt\) is on \(t\) alone. The upper frequency bound is
\[
 \frac{Nt\,Ne_0}{(Nh)^2}
           \le \frac{R E E_1 J D^\eta}{D N(gw)} .
\]
This is the exact \(Nk\le M D^\eta\) test, including its endpoint. No condition involving \(Q_u\) replaces this selector. The radial profile itself uses \(Q_u\) exactly.

At fixed data all mixed indicators are step functions of a product of one positive rational on the \(h\)-allocation and one on the \(t\)-allocation. Every possible rational here has numerator and denominator at most \(D^{C_0}\) for some fixed \(C_0\), by the original live scales. One can include all values from the bounded rectangular arrays before imposing each step. The distinct logs of these rationals have separation \(\gg D^{-C_1}\) for fixed \(C_1\), since distinct rationals with denominators at most \(D^{C_0}\) differ by at least \(D^{-2C_0}\). Put each smooth transition in the gap between the last allowed value and the first disallowed value, using the actual endpoint convention. This works also when the real threshold equals a rational value. If either side is empty the step is constant on the support. Extend by a smooth compact cutoff in a log interval of length \(O(\log(2D))\). The resulting multiplier has \(L^1\) norm \(O(\log(2D))\), first derivative of \(L^1\) norm \(O(1)\), and second derivative of \(L^1\) norm \(O(D^{C_2})\) for fixed \(C_2\). Its Fourier \(L^1\) norm is \(O(\log(2D))\) by splitting the frequencies at \(1,D^{C_2}\) and using zero, one and two integrations by parts. Every Fourier phase separates as a product of phases on the two allocations. There are only a fixed number of mixed indicators. This proves an exact separation with polylogarithmic mass on the actual integer nodes.

After fixing the Fourier parameters, collect the respective allocations on each \(h\) and \(t\). Their coefficients are divisor bounded. The fixed ideal coprimalities are one-side selectors, including the selection of \(t\) at fixed \(w\). The remaining variable coprimality is \((h,t)=1\). Indeed \((h,z_0)=1\) imposes this and \((h,gw)=1\), while the orientation and all fixed \(t\)-conditions can be tested at fixed \(g,w\). There is no condition \((h,\bar t)=1\). Expand \((h,t)=1\) by \(\sum_{q\mid h,t}\mu(q)\). At fixed \(q\) put \(h=q h'\) and \(t=q t'\). The exact fixed row factor of this substitution is \(\psi_u(q)^2\psi_u(q)\overline{\psi_u(\bar q)}\), with its zeros. Both arrays keep the squarefreeness conditions on \(h',t'\) and the original selectors on their own arguments. No claim of a phase identity outside the Möbius-weighted support is used.

## Sixth and third moments on the separated arrays

For a divisor-bounded cubic sum on \(h'\) of length \(L\), freeze \(v_2\) or sum over its bounded pure support. The sixth moment satisfies
\[
 \left\|\sum_{h'} a_{h'}\psi_u(h')^2\right\|_6^2
 \ll (DH)^\epsilon L\,\Phi_3(A_1,\max(1,L^3))^{1/3}.                  \tag{1}
\]
Indeed cube the sum and group the three ideal factors. All have squarefree support. At any prime the total exponent is at most three. Freeze the squarefree ideal \(c\) of exponent-three primes and keep the raw \(\psi_u(c)^6\) multiplier. The remaining cubefree products have length \(O(L^3/(Nc)^3)\) and divisor-bounded coefficients. Apply the pinned \(n=3\) moment input of POWERED_DUAL_ROOT-v1 to their squared norm. The norm triangle over \(c\) has the summable weight \((Nc)^{-3/2}\). A live subunit length is treated at bounded length. Taking the cube root of the resulting squared norm gives (1). This calculation never restores a zero on a prime with exponent three.

For a divisor-bounded sum of the oriented rational characters \(\chi_{t'}(Nu)\) at length \(L'\), the second moment bound on the pure rows is \(O((DH)^\epsilon L'(A_1+(L')^{5/3}))\) from EQUAL_RATIONAL_SIEVE-v4, using the norm fibres of the physical rows. The fourth moment is at most
\[
 (DH)^\epsilon (L')^2(A_1+(L')^{10/3}).                               \tag{2}
\]
To prove (2), square the sum and at each ordered pair let \(c\) be its common same-orientation ideal and \(j\) its opposite-orientation ideal, chosen on the first side. Write \(t'_1=cj a,\ t'_2=c\bar j b\). The common same phase is \(\chi_c(Nu)^2\), the common opposite phase is \({\bf1}_{(Nu,Nj)=1}\), and the remaining phase is \(\chi_{ab}(Nu)\), since the two residuals have disjoint rational supports. Freeze \(c,j\). Both fixed factors retain their zeros, and \(ab\) is oriented squarefree with norm \(O((L')^2/(Nc Nj)^2)\). The coefficient on \(ab\) is divisor bounded by its possible ordered splittings. Apply the rational second-moment input and the norm triangle over \(c,j\), with harmonic weight \((Nc Nj)^{-1}\) in the unsquared comparison. Squaring gives (2). The fixed \(\nu(t')\overline{\nu(\bar t')}\) from the equality phase is a column coefficient throughout. Interpolation between the second and fourth moments gives
\[
 \left\|\sum_{t'} b_{t'}\chi_{t'}(Nu)\right\|_3^2
 \ll (DH)^\epsilon L'
    [(A_1+(L')^{5/3})(A_1+(L')^{10/3})]^{1/3}.                      \tag{3}
\]
This is the elementary log convexity of \(L^p\) with weights \(1/3,2/3\) on \(p=2,4\).

## Pure band and whole-complement cross

At dyadic \(Nh\asymp T,\ Nt\asymp B\), use (1) and (3) at lengths \(T/Nq,B/Nq\), up to fixed constants, inside Hölder with \(1/2=1/6+1/3\). The unsquared harmonic weight is \(1/Nq\), even for live subunit lengths. Use the same radial profile separation in \(Nh,Q_u\) as in the grouped proof. The \(\mathcal M_{12}(W)\) seminorm, the coefficient \(T^2/(Nh)^2\) and exact \(B/Nt\) are retained. With \(T_0=\sqrt{D/(E E_1R)}\), \(y=(T_0/T)^2\), the squared norm divided by \(D\) is bounded on the dyad by
\[
 \ll (DH)^\epsilon \mathcal M_{12}(W)^2
 \frac{y(1+y)^{-8}}{E E_1 T B}
 [\Phi_3(A_1,T^3)(A_1+B^{5/3})(A_1+B^{10/3})]^{1/3}.                \tag{4}
\]
For the scalar, the prefactor in the grouped representation is \(D/(E E_1 Ng Nw\,B T^2\sqrt R)\) up to fixed constants. The two array norm factors contribute \(\sqrt{TB}\) before taking the square. The \(g,w\) sum has the harmonic weight \(1/(Ng Nw)\). The exact sharp allocations above cost only divisor counts and powers of \(\log(2D)\), and \(e_1\) has its original finite divisor sum. Thus (4) refers to the actual full cutoff coefficient on the selected band.

In (4) the \(T\)-dependent polynomial factor after the cube root is a nonnegative sum inside that root with growth at most degree one in \(T\). For \(T_0\ge1\), compare \(T\le T_0\) by monotonicity of \(\Phi_3\) and bound \((T_0/T)y(1+y)^{-8}\). For \(T\ge T_0\), use the degree bound and \(y(1+y)^{-8}\ll1\). For \(T_0<1\), the same comparison at the unit length is bounded by \(O(1/T_0)\) times the unit polynomial factor. Hence the optimization replaces \(T^{-1}\Phi_3(A_1,T^3)^{1/3}\) with \(T_0^{-1}\Phi_3(A_1,\max(1,T_0^3))^{1/3}\) up to constants after retaining the profile factor. At pure \(T_0^3\ll D^{3/8}\), and this last polynomial is \(O(D^{3/4})\). When \(B\le D^{3/8}\), \(A_1+B^{5/3}\ll D^{3/4}\). Use \(1/(E E_1 T_0)\ll D^{-1/8}E^{-1/2}\) and sum the original dyads. The resulting energy is at most
\[
 \ll (DH)^\epsilon\mathcal M_{12}(W)^2 E^{-1/2}
       \left[\frac{D^{5/8}}B+D^{3/8}B^{1/9}\right].                  \tag{5}
\]
It is \(O(D^{5/12}E^{-1/2})\) in the full band \(D^{5/24}\le Nt\le D^{3/8}\), including clipped boundary dyads. The proof of PURE_EQUAL_JOINT-v1 now gives \(D^{3/4+\epsilon}\) for the cross against \(V_d-E_d\) over all \(d\), including \(d=1\), using the inherited \(D/E^2\) selected bound on the large divisor tail. The smaller band \([D^{13/60},D^{1/3}]\) gives unit-divisor energy \(D^{89/216}\) and unit-divisor cross \(D^{323/432}\). The all-divisor target uses the split above. This estimate places no lower bound on the rational content of \(h\) or its opposite overlap.

In particular the pure equality projection with \(N\ell_{\rm good}\ge D^{5/24}\) has target cross. Here \(\ell_{\rm good}\) keeps precisely the factors of \(\ell\) whose conjugates also avoid \(S\). If \(D^{5/24}\le N\ell_{\rm good}<D^{5/12}\), take \(t=\ell_{\rm good}\). Otherwise every nonzero original allocation splits \(\ell_{\rm good}\) into two subideals of norm at most \(U\le D^{1/2}\), since each divides one original cutoff factor. One of these subideals has norm at least \(D^{5/24}\). Thus a qualifying divisor with \(D^{5/24}\le Nt\le D^{1/2}\) exists whenever the grouped coefficient is nonzero. Choose one by a rule on \(\ell,U,D\) only. The estimate just proved applies through \(D^{3/8}\); the prior oriented rational Gram bound of EQUAL_RATIONAL_SIEVE-v4 applies for \(D^{1/3}\le Nt\le D^{1/2}\) and has target cross. The intervals overlap. This gives the stated projection without a smoothness assumption or a balanced-divisor assumption. The pure small-divisor cross with \(N\ell_{\rm good}<D^{5/24}\) remains open on the complement of the separate profile and sparse sectors. The whole signed assembly, determinant and zero-location comparisons remain open.

