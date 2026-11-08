# Grouping the square divisor and deletion factor on the equal-norm projection

8 November 2026 UTC. Use the actual original unweighted nonprincipal two-pivot rows, full \(Z=U^2\) cutoff coefficient, and middle Poisson window of LOW_DUAL_CUTOFF-v1. In particular \(U^2\le D\le7U^2/2\), \(A_i\le Nv_i<2A_i\), \(R=A_1A_2\), \(Q_u\asymp R\), and the literal \(S\)-supported factor \(u_0\) and \(\nu,S\) are fixed. There is one common smooth complex \(W\) supported on \([1,2]\). All original row, cutoff, common-prime and ray selectors are part of the amplitude. All estimates use the original counting norm.

Let \(V_d\) be the full original amplitude after the intermediate Möbius divisor \(d\), so the signed form has terms \(\mu(d)\|V_d\|^2/D\). Within its Poisson middle window, let \(E_d\) be the entire equal-norm projection of the conjugate reduction, before any assignment that removes this projection. The condition is \(Nz_0=Nk\), equivalently \(Na'=Nb'=1\) with the exact reduced factors of CONJUGATE_DUAL_OVERLAP-v2. Thus \(z_0=g\ell,\ k=g\bar\ell\). Any inherited choices of exact windows or terms may be kept if their restrictions in this projection are independent of the row apart from the original row multipliers and primitive zeros.

## The exact grouped sum

At fixed \(d,r,e_1,e_0,J,z_0,k\) in the original representation, \(e_1\mid\operatorname{rad}(Sd)\), \(z=e_0 z_0\), \(e_0\mid z\) is good and prime to \(d\), and \((r,Sdz)=1\). The squarefree \(r\) has the factor \(\mu(r)\). Keep the deleted-prime factors
\[
 \mu(r)\mu(e_1)\mu(e_0)\,\mathbf1_{(d,u)=1}
      \psi_u(r)^2\psi_u(e_1)\psi_u(e_0)^2 .
\]
Set \(h=re_0\). The original masks give \((r,e_0)=1\), so \(h\) is good squarefree, and \(\mu(r)\mu(e_0)=\mu(h)\). The character factor is exactly \(\psi_u(h)^2\), with its raw zero. On the equal-norm projection, with \(E_1=Ne_1\), the two scalars in the original Poisson formula are
\[
 \frac{X}{E Nz}=\frac{D}{Nd\,E_1 (Nh)^2 N(g\ell)},\qquad
 \frac{X Nk}{E Nz Q_u}=\frac{D}{Nd\,E_1 (Nh)^2 Q_u},
 \quad X=\frac{D}{Nd(Nr)^2},\quad E=Ne_0 E_1.                 \tag{1}
\]
The Gauss root and \(Q_u^{-1/2}\) are unchanged. The common-ideal factor is still \(|\psi_u(g)|^2\psi_u(\ell)\overline{\psi_u(\bar\ell)}\), including the exact primitive \(S\)-value if \(\bar\ell\) meets \(S\).

For fixed \(d,e_1,g,\ell\), define \(c(h)\) as \(\mu(h)\) times the sum over \(e_0\mid h\), using \(r=h/e_0\), of \(\beta_{d,U,U^2}(e_0 g\ell)\) with every original selector. Use the actual dyad \(J\le N(e_0g\ell)<2J\) for each allocation, and use its actual \(X'\) and \(M\) for the direct, primal-zero and middle tests. All these tests use \(R\), with \(Q_u\) retained separately in the profile. No \(r\)-\(k\) disjointness is added. The product \(g\bar\ell\) can repeat primes, and \(Nk\) and its character value count their actual valuations. Each allocation belongs to exactly one \(J\), so it occurs at most once in \(c(h)\). The coefficient is independent of the row and divisor bounded. The nonannular zero cases discarded before Poisson remain discarded. The remaining row dependence on the outer data is
\[
 \mu(e_1)\mathbf1_{(d,u)=1}\psi_u(e_1)
 |\psi_u(g)|^2\psi_u(\ell)\overline{\psi_u(\bar\ell)}\gamma_u Q_u^{-1/2}.
\]
Consequently the exact inner \(h\)-sum is
\[
 \frac{2D}{\sqrt3\,Nd\,E_1 N(g\ell)}
 \sum_h \frac{c(h)\psi_u(h)^2}{(Nh)^2}
     G_W\!\left(\frac{D}{Nd\,E_1(Nh)^2Q_u}\right),              \tag{2}
\]
times this outer row factor. Grouping \(h\) before taking the norm is essential. Applying a cubic norm to \(r\) at fixed \(e_0\), then optimizing the radial scale, can leave \(E_0^{-1/2}\) in the unsquared norm. Its sum over \(e_0\) is larger than logarithmic.

## Cubic average and the divisor budget

Let \(\Phi_3(A,B)=A+B+2(AB)^{2/3}\). On the dyad \(T\le Nh<2T\), the bounded-coefficient comparison for the good squarefree \(h\)-column is
\[
 \left\|\sum_h b_h\psi_u(h)^2\right\|_2^2
 \ll_\epsilon (DH)^\epsilon T A_2\Phi_3(A_1,T)
\]
for divisor-bounded \(b_h\). This is the pinned \(n=3\) application of de Faveri, arXiv:2610.04045v1, Theorem 1.1, with the literal primary section and fixed second pivot as in POWERED_DUAL_ROOT-v1. It includes the good raw zeros. The fixed twist and second-pivot phase go into the coefficients at each fixed \(v_2\), including their zeros. The original capacity only restricts the positive norm.

For fixed \(e_1\) put \(T_0=(D/(Nd E_1R))^{1/2}\), \(y=(T_0/T)^2\). On the dyad the profile in (2) separates the \(h\)-phase from the row \(Q_u\)-phase by log Fourier inversion. The fixed-width log extension has Fourier absolute integral \(O(\mathcal M_{12}(W)(1+y)^{-4})\), as in the original radial formula. The coefficient \(T^2/(Nh)^2\) stays in the \(h\)-sum. Summing \(1/N(g\ell)\) over the live \(g,\ell\), with \(N(g\ell)\le Z\le D\), costs at most \(O(\log^2(2D))\) by ideal counting, after applying the cubic average at each fixed \(g,\ell\). Both possible \(S\)-values and the root multiply the same row exactly. Squaring, dividing by \(D\), and using \(Q_u\asymp R\) give, up to the common subpower and profile costs, the bound
\[
 \frac{A_2}{Nd E_1}\,
       \frac{\Phi_3(A_1,T)}{T}\,y(1+y)^{-8}
\]
for the squared norm at fixed \(e_1,T\). In live terms \(Nh\ll\sqrt{D/Nd}\) by the original primal-zero test, so there are logarithmically many \(T\)-dyads. Indeed \(X/(EJ)>1/2\) implies \(D/(Nd E_1 (Nh)^2)>J/(2Ne_0)\), and a live \(J/Ne_0\ge 1/2\).

For \(s=0,1/3,1\), the factor \(T^{-s} y(1+y)^{-8}\) is bounded by \(C T_0^{-s}\), by writing \(T^{-s}=T_0^{-s} y^{s/2}\). This covers \(T_0<1\) without a fictitious ideal below unit norm. The \(E_1^{-1}\) and \(T_0^{-s}\) factors combine as \(E_1^{-1+s/2}\le1\) in the squared norm. The number of \(e_1\) choices is divisor bounded. After the norm triangles this proves the per-divisor estimate
\[
 \boxed{\displaystyle
 \frac{\|E_d\|_2^2}{D}
 \ll_{\epsilon,\eta,S,\nu,u_0}(DH)^\epsilon\mathcal M_{12}(W)^2
 \frac{A_2}{Nd}
 \left[1+A_1\sqrt{\frac{Nd\,R}{D}}
             +A_1^{2/3}\!\left(\frac{Nd\,R}{D}\right)^{1/6}\right].}  \tag{3}
\]
This is an estimate of the entire equality projection. It needs no eligible divisor of \(\ell\) and no conjugation invariance of \(S\).

Two complementary estimates also follow directly. In the fixed \(e_1,T\) bound, \(\Phi_3(A_1,T)/T\ll A_1\) and \(y\le D/(Nd E_1 R)\). After the same sums this gives \(D^{-1}\|E_d\|_2^2\ll (DH)^\epsilon\mathcal M_{12}(W)^2D/(Nd)^2\). The elementary equality count gives a different bound \(O((DH)^\epsilon\mathcal M_{12}(W)^2 R/(Nd))\). For that count, return to a fixed \(r,e_0,e_1,J\), put \(L=X/(E Ne_0)\), and count the \(O(J'\log(2+2J'))\) choices of \(g,\ell\). The Poisson factor then gives pointwise \(O((DH)^\epsilon\mathcal M_{12}(W)(L/\sqrt R)(1+L/R)^{-4})\). The \(O(R)\) rows give squared norm \(O((DH)^\epsilon\mathcal M_{12}(W)^2 R L)\) since \((L/R)(1+L/R)^{-8}\) is bounded. Now \(\sqrt L=\sqrt X/(Ne_0\sqrt{E_1})\), so the original \(r,e_0,e_1,J\) sums have the harmonic cost. This count applies to the same entire equality projection.

## Mixed full equal-norm cross

Take \(H\asymp D^{3/4}\), \(A_1\asymp D^{5/12}\), \(A_2\asymp D^{1/6}\). Equation (3) gives
\[
 D^{-1}\|E_d\|_2^2\ll (DH)^\epsilon \mathcal M_{12}(W)^2
                         D^{3/8}(Nd)^{-1/2}.
\]
Both nonconstant monomials at \(Nd=1\) have power \(3/8\). Their inverse divisor powers are respectively \(1/2\) and \(5/6\), while the constant monomial is \(D^{1/6}/Nd\).

For \(1\le Nd\le D^{1/4}\), the per-divisor physical bound for \(D^{-1}\|V_d\|_2^2\) is dominated by \(D^{13/12}(Nd)^{-11/6}\). Indeed this term dominates \(H/Nd\), \(D/(Nd)^2\), and \(H^{5/6}D^{1/3}(Nd)^{-4/3}\) on that range. It also dominates (3) there. Apply the norm triangle to \(V_d-E_d\), then take absolute Cauchy on the actual inner product at each \(d\). The resulting summable divisor majorant for the cross is \(D^{35/48}(Nd)^{-7/6}\). This part includes \(d=1\).

For \(Nd>D^{1/4}\), the summed positive bound for \(V_d\) from the four physical terms is \(O((DH)^\epsilon\|W\|_\infty^2 D^{7/8})\). The two larger powers are \(H^{5/6}(D/D^{1/4})^{1/3}\) and \(H^{1/3}(D/D^{1/4})^{5/6}\). The original unit endpoint when \(D/Nd<1\) remains in the term \(H/Nd\). The previous unit-length equality bound gives positive energy \(O((DH)^\epsilon\mathcal M_{12}(W)^2 R)\) for \(E_d\) over all \(d\), with \(R\asymp D^{7/12}\). The norm triangle for the complementary amplitude and absolute Cauchy in \(d,u\) give power \((7/8+7/12)/2=35/48\) on this tail as well.

Hence the actual cross
\[
 \frac{2}{D}\operatorname{Re}\sum_d\mu(d)\langle E_d,V_d-E_d\rangle
   \ll (DH)^\epsilon\mathcal M_{12}(W)^2 D^{35/48}
\]
in absolute value. Both parts allow further restrictions on the divisor sum. This also implies the target \(D^{3/4+\epsilon}\) in the feasible mixed neighborhood where the two pivot log exponents differ by at most \(1/2000\). In that neighborhood the two small-\(d\) prefactor exponents can increase by at most \(3/2000\), and the large-\(d\) equality exponent by at most \(1/1000\), using the same physical \(H\) cap. The target margin is \(1/48\) at the exact mixed point.

The exact pure point \(A_1\asymp D^{3/4},A_2\asymp1\) gives the leading small-\(d\) equality energy \(D^{5/8}\) in (3). With the full complementary comparison the resulting \(d=1\) cross budget is \(D^{41/48}\), above target. The separate \(D/(Nd)^2\) bound above does cover the entire pure equal-norm cross on \(Nd\ge D^{11/32}\). At \(Nd\ge D^\delta\), pair it separately with each of the four physical monomials for \(V_d\) before summing the ideal tail. The resulting powers are \(7/8-\delta/2,\ 1-\delta,\ 47/48-2\delta/3,\ 25/24-11\delta/12\). The equality norm term from \(V_d-E_d\) costs \(D/D^\delta\). All meet the target for \(\delta=11/32\). The pure small-divisor case needs a different estimate or a more restrictive projection. The mixed estimate controls the entire equal-norm cross of the specified middle representation and uses no sign cancellation in \(d\). The remaining full signed assembly includes the off-equal amplitude squared, other projections and their interactions. The whole-form, determinant, zero-location and Lean obligations remain open.

