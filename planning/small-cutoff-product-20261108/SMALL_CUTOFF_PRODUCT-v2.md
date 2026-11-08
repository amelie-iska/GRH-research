# A bound for the small cutoff-product part of the actual annular coefficient

8 November 2026 UTC. Author checked, independent review pending. This note separates one part of the original cutoff coefficient at the amplitude level. At the mixed two-pivot scales it gives a target-size bound for the squared norm of this part, summed over all intermediate divisors. It also reduces the target at \(d=1\) to the complementary amplitude. The proof uses the inherited sixth-free sieve and primitive lattice Poisson summation, without the fixed-field \(7/8\) hypothesis.

## 1. Original cutoffs and the partial amplitude

Use the original \(K=\mathbb Q(\omega)\), fixed \(S,\nu\) with the conductor of \(\nu\) supported in \(S\), and \(W\in C_c^\infty((0,\infty))\) supported in \([1,2]\). Use \(U^2\le D\le7U^2/2\), the complete original good squarefree annulus, and the original unweighted literal rows with good \(v_1v_2^2\), \(A_i\le Nv_i<2A_i\), fixed \(S\)-supported \(u_0\), and all original row capacity, ray and squarefree restrictions. Assume the original column character is nonprincipal on each such row, as in the mixed and pure blocks under consideration. Write \(R=A_1A_2\), and \(M_4(W)=\max_{0\le j\le4}\|(x\partial_x)^jW\|_\infty\). A fixed bounded literal multiplicity is handled by splitting literal classes. Here the intermediate divisor \(d\) is from sw:mobius, so it is separate from the gcd of the original coprime columns.

For \(Z\ge1\), restrict the actual two cutoff divisors by their **joint** norm:
\[
 A_{U,\le Z}(m)=
   \sum_{\substack{xy\mid m,\ (x,y)=1\\
                    Nx,Ny\le U,\ N(xy)\le Z}}\mu(x)\mu(y).
\]
Use this as a part of the original \(A_U\), with the exact complementary summands \(N(xy)>Z\). For good squarefree \(d\) with \(Nd\le2D\), define the vector on the actual rows
\[
 V_{d,\le Z}(u)=
 {\bf1}_{(d,u)=1}\!
 \sum_{\substack{a\ {\rm good\ squarefree}\\ (a,d)=1}}
       A_{U,\le Z}(da)\nu(a)\chi_a(u)W(Nd\,Na/D).
\]
All norms on the row vectors are the usual unweighted Euclidean norms. For any \(1\le C_0\le D\) we obtain
\[
 \frac{\|V_{d,\le Z}\|_2^2}{D}
 \ll_{S,\nu,\epsilon}(DH)^\epsilon M_4(W)^2
 \frac{Z}{Nd}
 \left(\frac{R^2}{C_0}+A_2\Phi_6(A_1,C_0)\right), \tag{1}
\]
where \(\Phi_6(A,C)=A+C+A^{5/6}C^{1/3}+A^{1/3}C^{5/6}\) is the pinned physical comparison phy:input. We may assume \(Z\le2D\), since \(N(xy)\le Nm<2D\) on the support. The same bound with \(Nd\) removed holds for \(D^{-1}\sum_d\|V_{d,\le Z}\|_2^2\) by the harmonic ideal count and a smaller internal \(\epsilon\). The weighted positive sum with an additional selector in \([0,1]\), including the complementary product cutoff of PRODUCT_CUTOFF_REDUCTION-v2, obeys this upper bound.

## 2. The exact remaining squarefree sum for fixed outer factors

Write \(a=zc\), with \(z\) the part of \(a\) used in \(x,y\) and \(c\) the unused part. Assign the primes of \(d\) to \(x,y,\) or neither. Equivalently use \(d_x,d_y\mid d\) disjoint, and the ordered splitting \(z=z_xz_y\). For a fixed good squarefree \(z\) coprime to \(d\), the coefficient is
\[
 \beta_{d,U,Z}(z)=
 \sum_{\substack{d_x,d_y\mid d,\ (d_x,d_y)=1\\
                  z_xz_y=z\\
                  N(d_xz_x),N(d_yz_y)\le U\\
                  Nd_xNd_yNz\le Z}}
        \mu(d_x)\mu(d_y)\mu(z).
\]
In particular \(Nz\le Z\) and \(|\beta_{d,U,Z}(z)|\le 3^{\omega(d)}2^{\omega(z)}\). These bounds do not change the individual cutoffs or merge conjugate ideals. At \(d=1\) the sum is exactly the two cutoff divisors inside \(a\). At \(Z=1\) it includes the unit pair \(x=y=1\).

Let \(\psi_u\) be the primitive finite-order Hecke character from hti:core, agreeing with \(\nu(c)\chi_c(u)\) away from \(S\cup\operatorname{supp}(u)\). On an actual row its conductor \(\mathfrak f_u\) satisfies \(N\mathfrak f_u\ll_{S,\nu}R\), since the tame conductor at good primes in \(v_1v_2\) is supported on their radical and the \(S\)-part is fixed or uniformly bounded by the original fixed data. Use the complete deleted set
\(\mathcal T=S\cup\operatorname{supp}(dzu)\). The exact \(z\)-summand in \(V_{d,\le Z}\) is
\[
 {\bf1}_{(d,u)=1}\beta_{d,U,Z}(z)\nu(z)\chi_z(u)
 \sum_{\substack{c\ \rm squarefree\\(c,\mathcal T)=1}}
       \psi_u(c)W(Nc/X),\qquad X=D/(Nd\,Nz).
\]
The multiplier \(\chi_z(u)\) already retains its raw zeros. Expand the last squarefree condition by \({\bf1}_{\rm SF}(c)=\sum_{r^2\mid c}\mu(r)\). On writing \(c=r^2 b\), both \(r\) and \(b\) avoid \(\mathcal T\) and the exact summand is
\[
 \mu(r)\psi_u(r)^2
       \sum_{(b,\mathcal T)=1}\psi_u(b)
                      W(Nb\,Nr^2/X). \tag{2}
\]
The inner ideal \(b\) can be nonsquarefree and can share primes with \(r\). It would change the original squarefree projector to forbid those overlaps. Both the factor \(\psi_u(r)^2\) and the entire deleted set remain.

## 3. Small square divisor by Poisson and large square divisor by the sieve

The full primitive norm sum
\[
 \sum_b\psi_u(b)W(Nb/L)\ll_K M_4(W)\sqrt{N\mathfrak f_u} \tag{3}
\]
holds uniformly in \(L>0\) for the specified nonprincipal primitive characters. Use the \(1/6\) element sum on the Eisenstein lattice, since the finite-order character is unit-trivial. Complete in residue classes modulo \(\mathfrak f_u\) using the inverse-different pairing of mcs:gauss, then apply lattice Poisson. The zero frequency is zero by nonprincipality, and the primitive Gauss sums at nonzero frequencies have magnitude at most \(\sqrt{N\mathfrak f_u}\) including the nonunit zeros. With \(Q_u=N\mathfrak f_u\) the bound is a constant times
\[
 M_4(W)\frac{L}{\sqrt{Q_u}}
 \sum_{\mathbf k\in\Lambda\setminus0}
          (1+\sqrt{L/Q_u}\,|\mathbf k|)^{-4},
\]
where \(\Lambda\) is a fixed two-dimensional lattice up to rotation and fixed covolume factors. The sum is \(O(Q_u/L)\) both below and above \(L=Q_u\), by disk counting for small \(\sqrt{L/Q_u}\) and the convergent fourth-power lattice sum for large \(\sqrt{L/Q_u}\). Four ordinary derivatives of the compact radial profile are bounded by a fixed multiple of \(M_4(W)\). For the actual deleted sum in (2), the primes of the primitive conductor already give raw zeros in (3). Apply finite inclusion-exclusion at every other prime of \(\mathcal T\) and apply (3) to each dilated profile. The absolute cost is at most \(2^{\omega(\mathcal T)}\ll_{S,\epsilon}(DH)^\epsilon\) on support, with the fixed \(S\) contribution absorbed. This uses the full masks, including primes forgotten by conductor induction. The bound of (3) with this subpower factor and \(Q_u\ll R\) is uniform for each small \(r\).

For the large \(r\) use the inherited norm at the actual \(b\)-length \(C=X/Nr^2\), whenever the support is nonempty. We require a version for the bounded coefficients of (2) on **all** good ideals \(b\). For fixed \(d,z,r\), first retain the exact \((dzu,r)=1\) and all other row-only raw factors. The \(b\)-character on the original live support is \(\nu(b)\chi_b(u)\), including its zeros. Fix \(v_2\), which puts its literal character and the fixed \(u_0\) contribution in the column coefficient. Next write \(b=b_0 q^6\) with \(b_0\) sixth-power-free and \(q\) arbitrary, using the unique valuation decomposition. For fixed \(q\), its symbol is a row mask because the sextic phase to the sixth power equals one off the raw zeros. Its \(\nu(q)^6\) is a fixed factor of modulus one. The \(b_0\)-coefficients for this fixed \(v_2,q\) are independent of \(v_1\); \((b,dzS)=1\) is a column restriction, and the other row and common-prime restrictions are retained before enlargement of positive norms. In particular \(q\) and \(b_0\) need not be coprime.

The pinned sixth-free estimate applies to \(v_1,b_0\) at lengths \(O(A_1)\) and \(O(C/(Nq)^6)\). The pointwise coefficient bound and ideal counting bound the squared column mass by \(O(B^2 C/(Nq)^6)\) with \(B=\|W\|_\infty\), whenever \(C/(Nq)^6\ge1/2\). A subunit length uses the unit count and a comparison at bounded length. Apply Minkowski in the actual rows over the fixed \(q\) and use \(\sum_q(Nq)^{-3}<\infty\). Finally sum the squared norm over the \(O(A_2)\) possible \(v_2\). For fixed \(d,z,r\) this gives an upper bound
\[
 (DH)^\epsilon B^2 C A_2 \Phi_6(A_1,C_0) \tag{4}
\]
when \(C\le C_0\). This establishes the needed bounded-coefficient comparison on arbitrary ideals through the fixed sixth factors. The argument does not apply a squarefree-column theorem directly to the auxiliary \(b\).

Partition \(z\) by \(J\le Nz<2J\) and let \(K=(D/(Nd\,J C_0))^{1/2}\). Use (3) on \(Nr<K\), which is empty for \(K\le1\). There are \(O(K)\) such ideals, \(O(J)\) ideals \(z\), and \(O(R)\) actual rows. The triangle in this range, followed by the squared row norm divided by \(D\), gives
\[
 (DH)^\epsilon M_4(W)^2 \frac{R^2J^2K^2}{D}
       =(DH)^\epsilon M_4(W)^2\frac{J}{Nd}\frac{R^2}{C_0}.
\]
For \(Nr\ge K\) use (4) since \(C\le C_0\), and group \(r\) in dyads of scale \(L_r\ge1\) keeping the exact cutoff. For each such dyad use Minkowski over \(z,r\) in the actual row norm and \(C\ll D/(Nd\,J L_r^2)\). The two counts \(O(J),O(L_r)\), squared, give \(J^2 L_r^2 C/D\ll J/Nd\). Both dyadic sums and \(|\beta_{d,U,Z}(z)|\) are absorbed by taking smaller internal subpowers, using \(J\le Z\). This proves (1).

## 4. Critical powers and the remaining cross term

At the original mixed scales \(A_1\asymp D^{5/12},A_2\asymp D^{1/6}\), choose \(C_0=D^{31/66}\). The two terms \(R^2/C_0\) and \(A_2 A_1^{1/3}C_0^{5/6}\) both have exponent \(23/33\). The three other sieve powers are \(7/12,7/11,59/88\). Therefore the whole positive budget for the small-product amplitudes is
\[
 \frac1D\sum_d \|V_{d,\le Z}\|_2^2
       \ll (DH)^\epsilon M_4(W)^2 Z D^{23/33}.
\]
In particular \(Z=D^{1/20}\) costs \(D^{493/660+\epsilon}\), below the critical target \(D^{3/4}\) by \(1/330\). The same target remains valid at that cutoff if the two pivot log exponents are within \(1/2000\) of \(5/12,1/6\) with feasible capacities. The largest possible increase in the Poisson power at this fixed \(C_0\) is \(4/2000\), and each sieve power increases by at most \(2/2000\). The cutoff \(Z=D^{7/132}\) gives the target exactly at the stated mixed scales with the subpower.

At the pure point \(A_1\asymp D^{3/4},A_2\asymp1\), the same bound with \(C_0=D^{21/32}\) gives \(Z D^{27/32+\epsilon}\). Its unit product already exceeds the critical target. In this budget the \(R^2/C_0\) term would require \(\log_D C_0\ge3/4\), while the \(A_1^{5/6}C_0^{1/3}\) term would require \(\log_D C_0\le3/8\). This is a limitation of the upper bound.

At \(d=1\), the full amplitude is exactly \(V_{1,\le Z}+V_{1,>Z}\). In the mixed block, the triangle in both directions means that the target row norm of the full amplitude is equivalent to the target row norm of the complementary amplitude for \(Z=D^{1/20}\). The target bound on the small-product squared norm does not permit deleting the cross term in a signed sum over \(d\). More explicitly, with a selector \(\rho_d\in[0,1]\), define \(S_\pm=D^{-1}\sum_d\rho_d\|V_{d,\pm}\|_2^2\). The cross term in the signed form has absolute bound \(2\sqrt{S_{\le Z}S_{>Z}}\), which remains unestimated at target scale without a complementary positive norm bound or a new signed comparison. The inherited physical bound on the positive sum for the complementary coefficients, using their divisor bound and summing the absolute divisor budgets, gives \(S_{>Z}\ll D^{13/12+\epsilon}\) at the critical line with fixed profiles. Thus this particular cross-term triangle gives only \(D^{235/264+\epsilon}Z^{1/2}\) at the mixed scales. This argument supplies a target-size component of the actual original \(d=1\) amplitude and a uniform positive budget over \(d\). The full small annular signed form, the larger cutoff-product channel, the far-norm Gauss pairing, and the determinant and zero-location problems remain open.
