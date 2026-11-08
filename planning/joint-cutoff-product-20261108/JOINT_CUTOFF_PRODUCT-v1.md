# Joint row averaging for the cutoff ideal and the unused factor

8 November 2026 UTC. Author checked, independent review pending. Grouping the cutoff ideal into the direct column, or retaining it as a separate factor in a dual fourth-moment bound, enlarges the range of cutoff products controlled in the actual mixed block.

## 1. Setting and result

Use the original Eisenstein field, fixed \(S,\nu\) and fixed literal \(S\)-supported row factor \(u_0\), as in DUAL_CUTOFF_PRODUCT-v1. In particular \(\nu\) is finite order with conductor supported in \(S\). Use one smooth complex \(W\) supported on \([1,2]\), \(U^2\le D\le 7U^2/2\), and the original good squarefree annulus and unweighted nonprincipal two-pivot rows with good physical part \(v_1v_2^2\). Keep their literal ray, squarefree, coprimality and capacity selections. Write \(A_i\le Nv_i<2A_i\), \(R=A_1A_2\), and \(Q_u=N\mathfrak f_u\asymp R\) for the primitive conductor of the row character \(\psi_u\). Its good support is exactly \(v_1v_2\). The \(S\)-part and all induced zeros are kept as in the preceding proof. Put \(M_{12}(W)=\max_{0\le j\le12}\|(x\partial_x)^jW\|_\infty\).

For each intermediate good squarefree divisor \(d\), let \(V_{d,\le Z}\) be the actual annular amplitude on the original rows from the ordered cutoffs
\(Nx,Ny\le U\), \(N(xy)\le Z\). We also allow an additional common selector \(Z_-<N(xy)\) in the coefficient. As in SMALL_CUTOFF_PRODUCT-v2, \(d\) is the divisor introduced by the Möbius inversion. It is separate from the gcd of the original coprime columns. Norms below are counting norms on the original rows.

Let \(\Phi(A,B)=A+B+A^{5/6}B^{1/3}+A^{1/3}B^{5/6}\) from phy:input. For any \(B_*\ge1\), put \(K_*=\max(1,RZ/B_*)\). Then
\[
 \frac{\|V_{d,\le Z}\|_2^2}{D}
 \ll \frac{(DH)^\epsilon M_{12}(W)^2 A_2}{Nd}
 \max\{\Phi(A_1,B_*),
             [\Phi(A_1,Z^2)\Phi(A_1,K_*^2)]^{1/2}\}.
 \tag{1}
\]
We use \(1\le Z\le2D\); beyond \(2D\) the upper selector is redundant. All constants allow the fixed data. Harmonic summation over \(d\) removes \(1/Nd\) at subpower cost. The same bound holds for any further divisor selector in \([0,1]\) in the resulting **positive** squared norm.

## 2. Fourth moments for the physical rows

The bounded-coefficient row comparison in DUAL_CUTOFF_PRODUCT-v1 extends from good ideals to all ideals. On a column length \(L\ge1/2\), first freeze its \(S\)-supported part \(\mathfrak s\), keeping \(\psi_u(\mathfrak s)\) or its conjugate as a row multiplier of magnitude at most one. On the remaining good part, fix its sixth factor and the second physical pivot. The bounded-coefficient squared row norm from phy:input is at most
\[
 (A_1 A_2\max(1,L))^\epsilon L A_2\Phi(A_1,\max(1,L)),
\]
up to the maximum squared coefficient magnitude. The possible \(S\)-parts are summed in the norm with the factor \((N\mathfrak s)^{-1/2}\), a convergent product on the fixed finite set. The fixed good sixth factors have the summable weight \((Nq)^{-3}\). Raw zeros on both fixed parts are retained. A subunit active length uses the unit count. All enlargements are within positive norms on the original rows.

For a sum \(S_L(u)\) of \(\psi_u\) or of \(\overline{\psi_u}\) on a length \(L\), with independent coefficients bounded by a divisor power, square the sum before using this comparison. Multiplicativity with zero extension gives a convolution on ideal products, supported up to \(4L^2\). Its coefficients have a divisor bound even if the two ideals share primes or have equal norm. This gives
\[
 \|S_L\|_4^4\ll (DH\max(1,L))^\epsilon
          L^2 A_2\Phi(A_1,\max(1,L^2)).
 \tag{2}
\]
Coefficient subpowers are included here. This squaring uses the same character on each side of its convolution. It does not require representing a ratio of ideals as a short sixth-free ideal. In the application the two factors with different conjugation will be combined by Hölder after (2).

## 3. Splitting the exact deletion

Use the exact \(d,z\) cutoff allocations from SMALL_CUTOFF_PRODUCT-v2. Thus \(z\) is the part of the residual ideal assigned to the two cutoff divisors, \(\beta_{d,U,Z}(z)\) is independent of the row, \(Nz\le Z\), and \(|\beta|\ll_\epsilon(DH)^\epsilon\). With an additional lower selector use the same allocation restricted by \(Z_-<Nd_xNd_yNz\). Expand the unused squarefree factor as \(r^2 b\) with \(\mu(r)\); \(r,b\) need not be coprime. Fix \(r\) and a dyad \(J\le Nz<2J\), and put \(X=D/(Nd\,(Nr)^2)\). The existing row factors are \({\bf1}_{(d,u)=1}\), \(\psi_u(r)^2\), and \(\mu(r)\). The condition \((r,Sdz)=1\) is an ideal selector. All raw symbols remain, including those on \(z\).

For each \(z\) the unused \(b\)-sum avoids \(S,d,z,u\). Primitive zeros take care of the good primes of \(u\). Expand the other deletions by \(\sum_{e\mid\operatorname{rad}(Sdz)}\mu(e)\). In each summand the \(b\)-variable becomes \(e\,b'\), and the multiplier \(\psi_u(e)\) is included even if it is zero. Split \(e=e_1e_0\) uniquely with \(e_1\mid\operatorname{rad}(S d)\), \(e_0\mid z\), and \(e_0\) prime to \(S d\). Here \((z,Sd)=1\) is part of the original allocation. In the term with fixed \(e_1,e_0\), write \(z=e_0 z_0\) and set
\[
 E_0=Ne_0,\quad E_1=Ne_1,\quad E=E_0E_1,\quad
 J'=J/E_0,\quad X'=X/E_0^2 .
\]
In a nonempty \(z\) subsequence \(J'>1/2\). There are no additional restrictions between \(z_0,b'\) or between \(r,b'\). The restrictions on \(z_0\), including \((z_0,e_0)=1\) and the cutoffs in \(\beta\), are independent of the row. After removing the fixed row factors, the exact expression is
\[
 \sum_{z_0}\beta_{d,U,Z}(e_0z_0)\psi_u(z_0)
       \sum_{b'}\psi_u(b')W(E\,N(e_0z_0)\,Nb'/X). \tag{3}
\]
Its fixed multiplier includes \(\psi_u(e)\psi_u(e_0)\) and the original Möbius sign \(\mu(e)\).

Group \(h=z_0 b'\) directly in (3). Its length is \(X/(E E_0)=X'/E_1\); the coefficient of \(h\) has a divisor bound because it sums over the allowed \(z_0\mid h\). The profile stays common. The direct row norm is therefore at most
\[
 (DH)^\epsilon M_{12}(W)\sqrt{\frac{X A_2}{E E_0}}\,
                        \Phi(A_1,\max(1,X'))^{1/2}. \tag{4}
\]
Subunit active lengths are counted directly. The replacement of \(X'/E_1\) by \(X'\) in the sieve constant uses monotonicity.

## 4. Keeping the cutoff ideal in the dual average

For the same fixed \(e,r,J,d\), use the exact radial primitive Poisson formula of DUAL_CUTOFF_PRODUCT-v1 on the \(b'\)-sum with length \(X/(E Nz)\). Its root number \(\gamma_u\) stays on the row. Its nonzero ideal frequencies have the conjugate primitive character \(\overline{\psi_u(k)}\) and profile
\(G(X Nk/(E Nz Q_u))\). For a dyad \(K\le Nk<2K\), let \(M=R E J/X\). As in the earlier dyadic separation, a fixed-width smooth log cutoff around the argument scale \(K/M\) and two Fourier integrations by parts give \(L^1\) mass
\(O(M_{12}(W)(1+K/M)^{-4})\).
The row factor \(Q_u^{-it}\), the \(z\)-factor \((Nz)^{-it}\) and the \(k\)-factor \((Nk)^{it}\) separate without changing their magnitudes. Also put \(J/Nz\) into the \(z_0\)-coefficient. The scalar prefactor has bound \(O(X/(EJ\sqrt R))\), keeping \(\gamma_u\) and the row dependence of \(Q_u\) in the exact formula.

At each Fourier parameter the remaining row expression is the product of a \(z_0\)-sum of length \(J'\) and a \(k\)-sum of length \(K\). Apply Hölder in the actual rows, followed by (2) on each factor. This gives the row norm
\[
 (DH K)^\epsilon \sqrt{J'K A_2}\,
 [\Phi(A_1,\max(1,J'^2))\Phi(A_1,K^2)]^{1/4}
\]
before the scalar prefactor and dyadic profile mass. In particular the dual frequencies supported at primes in \(S\) retain their primitive phases or zeros in (2). Multiplicativity does not delete these frequencies. The ideal products in both fourth moments keep all their repetitions, and the conjugation of the second factor remains.

Sum over \(K\) using the profile decay. For \(K\le M\) use the monotonicity of \(\Phi\) and sum \(\sqrt{K/M}\). For \(K\ge M\), \(\Phi(A_1,K^2)\le\max(1,(K/M)^2)\Phi(A_1,\max(1,M^2))\), which is summable with the profile factor even when \(M<1\). A nonempty primal summand has \(X/(EJ)>1/2\), so \(M\ll R\) and subpowers from arbitrarily large \(K\) are absorbed by the tail. The prefactor times \(\sqrt{J'M}\) is exactly \(\sqrt{X/(E E_0)}\). Finally
\[
 M=E_1 R J'/X',\qquad
 \Phi(A_1,\max(1,M^2))^{1/4}
 \le E_1^{1/2}\Phi(A_1,\max(1,(R J'/X')^2))^{1/4}.
\]
The factor \(E_1^{1/2}\) cancels the \(E_1^{-1/2}\) in \(\sqrt{X/(E E_0)}\). Thus, after this cancellation, the dual row norm is at most
\[
 (DH)^\epsilon M_{12}(W)\frac{\sqrt{X A_2}}{E_0}
 [\Phi(A_1,\max(1,J'^2))
  \Phi(A_1,\max(1,(R J'/X')^2))]^{1/4}. \tag{5}
\]
Both (4) and (5) are bounds for the same fixed deletion term. Choosing (4) if \(X'\le B_*\), and (5) if \(X'>B_*\), gives in either case the square root of the corresponding sieve budget in (1), multiplied by \(\sqrt{X A_2}/E_0\). Here \(J'\le Z\). The comparison uses \(X'\), so a large common prime in \(z\) can move a term to the direct estimate.

There are \(O_\epsilon((DH)^\epsilon)\) choices for \(e_1\), and \(\sum_{Ne_0\le 2J}1/Ne_0=O(\log(2J))\). These costs enter only after the two factors in (3) have been averaged together. For each dyad \(T\le Nr<2T\), Minkowski over \(r\) gives \(T\sqrt X\ll\sqrt{D/Nd}\); there are logarithmically many \(r,z\) dyads. Squaring and dividing by \(D\) proves (1). This harmonic summation uses the full deletion expansion and all actual row factors, not a replacement of the mask by marginal probabilities.

## 5. Mixed critical range and remaining terms

Take \(A_1\asymp D^{5/12}\) and \(A_2\asymp D^{1/6}\) with feasible capacities. At
\[
 Z=D^{29/120},\qquad B_*=D^{8/15},
\]
the exponents of \(Z^2\) and \(K_*^2\) are \(29/60\) and \(7/12\). For these two lengths the dominating terms of \(\Phi\) have powers \(13/24\) and \(5/8\), respectively. Their average plus the \(A_2\)-exponent is \(3/4\). The direct side has power \(3/4\) as well. Thus the positive squared norm of the selected amplitude, summed over all intermediate \(d\), meets the target for \(Z=D^{29/120}\) up to subpowers. This includes the actual band \(D^{5/36}<N(xy)\le D^{29/120}\) by the additional lower selector.

For \(Z=D^{7/30}\) choose \(B_*=D^{21/40}\). The direct and dual bounds both give \(D^{107/144+\epsilon}\) after harmonic summation, a margin \(1/144\) below \(3/4\). This remains at target size when each mixed pivot log exponent differs by at most \(1/2000\) from its stated value and the capacity remains feasible. Each of the two displayed powers increases by at most \(2/1000\) in this neighborhood. Neither bound needs a fixed-field power hypothesis.

At the pure scales the fourth-moment branch does not give a target improvement over the preceding bounded-\(Z\) result. At the natural unit crossover \(B_*=D^{3/8}\) it gives power \(13/16\); the preceding separate dual estimate remains the one that gives \(3/4\) there. At \(d=1\) the norm triangle leaves the complementary amplitude as the target. Across signed \(d\), absolute Cauchy with the inherited complementary positive norm at the mixed \(Z=D^{7/30}\) cutoff gives only \(D^{263/288+\epsilon}\). This is an upper comparison for the cross term and does not reach target size. The larger cutoff products, the signed cross term, and the full signed form remain open.
