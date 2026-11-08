# Coherent averages of insertion and erasure in the exact signed cross

8 November 2026 UTC. Use the original paired Poisson form of MATCHED_POISSON_CROSS-v2 and JOINT_ERASURE_CROSS-v2. Use the original unweighted literal nonprincipal rows \(u_0\alpha_{v_1}\alpha_{v_2}^2\), \(A_i\le Nv_i<2A_i\), fixed \(S,\nu,u_0\), \(R=A_1A_2\), \(A_1A_2^2\ll H\le D\), \(U^2\le D\le7U^2/2\), ordered cutoff \(Z=U^2\) and one common \(W\in C_c^\infty\) supported on \([1,2]\). The estimates concern the selected part of \(2D^{-1}\operatorname{Re}\sum_d\mu(d)\langle E_d,V_d-E_d\rangle\). Here \(E_d\) is the equal-norm middle projection of GROUPED_EQUAL_CROSS-v4. The complement includes the original direct term re-expressed by the same exact Poisson formula after the primal-zero removal. Write \(E=Nd,\ E_i=Ne_{1,i}\) and \(\Phi(A,T)=A+T+A^{5/6}T^{1/3}+A^{1/3}T^{5/6}\). All bounds below have a factor \(O_{\epsilon,S,\nu,u_0}((DH)^\epsilon\mathcal M_{16}(W)^2)\). Use the inherited negligible tail \(Nk>D^5\) first. It is valid on arbitrary selections of pairs by the absolute tail proof in MATCHED_POISSON_CROSS-v2.

## Exact selection and separators

Let \(x=\mathfrak q_z,\ q_\ell=\mathfrak q_\ell\) be the two erasure supports of JOINT_ERASURE_CROSS-v2. Thus \(x\mid z\) is good squarefree and avoids \(a b\ell\bar\ell_{\rm g}d\), with old exponent one and new exponent zero. The good primes of \(q_\ell\mid\bar\ell_{\rm g}\) avoid \(a b d\), and have old exponent \(\beta=1+\mathbf1_{p\mid z}\) and new exponent zero. Keep the exact \(\mathfrak e_\ell=\prod_{p\mid q_\ell}p^\beta\). As before, allow arbitrary changed residues on \(d\), and write \(\widetilde q_d\) for the exact actual representative there. Additionally let \(I\) be the good sixth-free ideal whose exponent at each increasing off-\(d\) prime is the positive difference \(\beta'-\beta\in\{1,\ldots,5\}\). Its support is disjoint from \(x q_\ell d\). No other change is made off \(d\). There may be overlap between \(I\) and fixed labels, including a nonzero matched residue if the sum is at most five. Keep all primitive zeros at those primes and every sixth-power repetition.

Write \(z=xz_*\), \(h_0=fa,h_1=fb\), \(j=(\bar\ell_{\rm g},d)\), \(c=(z_*,a,\bar\ell_{\rm g})\), \(a_0=a/c\), \(\ell_0=\ell/(\ell,z_*b)\). On the support these \(c,\ell_0\) agree with the original values at \(z\). The exact partner frequency is \(k=I k_*\), with
\[
 k_* = k_S v^6\,\frac{z_* a^4 b^2\ell_0^6(\bar\ell_{\rm g}/j)\widetilde q_d}
                          {\ell c^6\mathfrak e_\ell}.
 \tag{1}
\]
In particular, \(k_*\) is fixed when the other labels are fixed. On the coprime support \((x,I)=1\), the phase from the two varying labels is \(\psi_u(x)\overline{\psi_u(I)}\), or its conjugate if one conjugates the pairing. The full union of fixed zeros multiplies this exact expression. The character of the literal row on \(x,I\) includes the twists and original zeros. These factors need not be coprime to \(g\) or \(v\). On \(p\mid I\), whether the old residue plus the increment is at most five is a predicate on \(I\) at the fixed data. The old residue there agrees with that computed at \(z_*\) once \(p\nmid x\). No physical norm is replaced by a radical.

For the partner expand \(e_0\mid h_1\), put \(r=h_1/e_0\), and freeze its original \(J\)-dyad before the two-family estimate. These choices have divisor and logarithmic cost. The equality allocation stays in a divisor-bounded factor at fixed equality labels. On the partner, the original coefficient \(\beta_{d,U,U^2}(e_0 xz_*)\), its \(J\)-membership, and all original cutoff and primal coprimalities are predicates on \(x\). The primal-zero removal and \(X'>B_*\) are fixed by the original cell. The frequency cutoff \(Nk\le D^5\) and the original middle tests \(K_0<Nk\le MD^\eta\) are predicates on \(I\), with \(M\) fixed by the cell. The exclusion of the equality middle component is exactly
\[
 1-\mathbf1_{\{X'>B_*,\,K_0<Nk\le MD^\eta\}}
       \mathbf1_{\{Nz_* Nx=Nk_* NI\}}.                            \tag{2}
\]
The ideal conjugate reduction characterizes the equality projection by equality of these norms. In particular, (2) does not remove equal norms from the re-expressed direct, low or far components. For a positive integer \(m\) greater than every absolute difference of the two integer norm products on the clipped cell, the last indicator is exactly
\[
 \frac1m\sum_{t=0}^{m-1}
 e^{2\pi i t Nz_* Nx/m}\,e^{-2\pi i t Nk_* NI/m}.                  \tag{3}
\]
One can choose \(m=\lfloor D+D^5\rfloor+1\), or any larger integer for the given finite cell. Only the total absolute mass one of this projector is used. This keeps both endpoints of the middle range, even at equality. No rational-gap approximation is needed.

On \(B\le Nx<2B,\ K\le NI<2K\), the exact partner profile is \(G_W(\mathcal A NI/(Nx Q_u))\) for a fixed positive \(\mathcal A\). Its fixed-width log Fourier extension, using the variables \(\log(NI/K)-\log(Nx/B)-\log(Q_u/R)\), has absolute Fourier mass \(O(\mathcal M_{16}(W)(1+y'_1)^{-4})\) where \(y'_1=\mathcal A K/(BR)\). The compact extension, with two integrations by parts in log Fourier, has this bound by the same radial derivative estimates as the parent formula. Thus it factors on the two label arrays and the row. The equality profile is still exact and independent of \(x,I\). The row scalar \(Q_u^{-1}\) is retained in the exact form and has bound \(O(R^{-1})\). The roots from the two Poisson terms cancel. Both Fourier decompositions are exact on the cell and independent of any analytic cancellation hypothesis.

## Coprimality and two second moments

Insert \(\mathbf1_{(x,I)=1}=\sum_{s\mid(x,I)}\mu(s)\) on the enlarged rectangular sum, using \(x=sx'\), \(I=t_s I'\) with \(t_s=\prod_{p\mid s}p^{v_p(I)}\). Here \(s\) is squarefree and the partition of its primes into the possible exponents costs \(5^{\omega(s)}\). The conditions on \(x'\) and \(I'\) induced by the exact shortening stay in their separate arrays. In particular \(I'\) is good sixth-free. The fixed raw multiplier \(\psi_u(s)\overline{\psi_u(t_s)}\) stays in the row and preserves the common-prime zeros. The expansion is on the literal character products extended to all pairs in the rectangle, so the Möbius sum cancels precisely the disallowed pairs even if some of those terms already vanish. On the desired support formula (1) agrees with the actual representatives. There is no algebraic assertion about matched representatives at the excluded pairs.

Freeze the second pivot \(v_2\). The remaining variable column symbols are the sixth-order symbols in the literal first pivot, with fixed \(u_0,\nu,v_2\) factors in the coefficients. Keep any fixed good and \(S\)-row factors as contractions in Cauchy. The two \(L^2\) moments on the original first pivot are bounded by the pinned physical sixth-order sieve. The normalized column masses have bounds \(O((DH)^\epsilon/(B Ns))\) for the \(x'\) array, where \(1/Nx\) stays in the coefficient, and \(O((DH)^\epsilon K/Nt_s)\) for the \(I'\) array. Any nonempty subunit shortened dyad has length at least \(1/2\) and satisfies the same bounds with a fixed constant by unit counting. In the sieve factors one can use \(\Phi(A_1,B),\Phi(A_1,K)\) by monotonicity and constants. Thus the product of the two row norms, summed over \(s\), costs at most
\[
 (DH)^\epsilon \sqrt{K/B}\sqrt{\Phi(A_1,B)\Phi(A_1,K)}
\]
per fixed \(v_2\), since \((Ns\,Nt_s)^{-1/2}\le(Ns)^{-1}\). The divisor factor in the \(s\)-sum is subpower and the ideal sum is harmonic. Sum \(v_2\) in absolute value at cost \(O(A_2)\). This replaces the trivial row count \(R\) and the harmonic \(x\) count and gives the relative factor
\[
 \frac{1}{A_1}\sqrt{K/B}\sqrt{\Phi(A_1,B)\Phi(A_1,K)}.                \tag{4}
\]
This is a product of two second moments after both raw symbol sums have been formed. The exact phases of the sum are used before row Cauchy. No enlargement occurs outside the positive row norms or scalar label counts.

## Radial powers and label counts

For \(1/6\le\theta\le1\) use \(y_0^{-(1-\theta)}(y'_1)^{-\theta}\). The scalar count is (2) of JOINT_ERASURE_CROSS-v2 with exponents adjusted to \(\theta\) as in (1) of DEFECT_ORDER_CROSS-v1. It has outer factor
\[
 \frac{R}{E}\,(B/K)^\theta(N\mathfrak e_\ell)^\theta
 \frac{(Nj)^\theta}{E_0^\theta E_1^{1-\theta}(N\widetilde q_d)^\theta}
\]
and the weight \(1/(Ng\,N\ell\,Nz_* (Nf)^2 (Na_0)^{6\theta}(Nb)^2
 (N\ell_0)^{6\theta}(Nv)^{6\theta}(Nk_S)^\theta)\). The full \(1/Nx\) already occurred in the column mass. The harmonic \(\ell\)-count with \(\bar j\,\bar q_\ell\mid\ell\) pays both fixed norms, since the two divisors are coprime. This pays the \(j\)-factor and leaves the \(d\)-choices at divisor cost. For each \(p\mid q_\ell\), its conjugate is in exactly one of \(\ell_0,z_*,b\). Use the explicit \(\ell_0^{-6\theta}\), the harmonic \(z_*\) count, or the inverse square \(b\)-count, as appropriate. This pays a second factor at least \((Np)^{-1}\). When \(\beta=2\), the original \(p\) also divides \(z_*\), and we charge it in that harmonic count too. The two primes are distinct, and primes of \(q_\ell\) lie on the opposite side to their conjugates because \((\ell,\bar\ell)=1\). All forced products of primes in the \(z_*\) count can therefore be combined without duplicate charges. The net weights on \(q_\ell\) are at most \((Np)^{-2+\theta}\) for \(\beta=1\) and \((Np)^{-3+2\theta}\) for \(\beta=2\). Both are harmonic or better through \(\theta=1\). The \(c\)-power cancels. The sums over \(a_0,v\) are harmonic at \(\theta=1/6\) after the polynomial clip, and the other factors have the same convergent or harmonic sums as the preceding proof.

The primal test on every live partner cell gives \(D/(E E_1(Nh_1)^2)>Nz/4\), where \(Nz=Nz_*Nx\). It follows that the profile scale is \(y'_1\gg Nk/R\gg K/R\). Retain \((1+y'_1)^{-3}\) as well as the \(\theta\)-power for \(0\le\theta\le1\), using the actual Fourier mass above. Therefore after summing the fixed labels, and after an absolute harmonic sum in \(d\), the normalized dyadic bound is
\[
 \boxed{\quad A_2 (B/K)^{\theta-1/2}
      \sqrt{\Phi(A_1,B)\Phi(A_1,K)}(1+K/R)^{-3} .\quad}              \tag{5}
\]
At fixed \(d\) put the additional factor \(E^{-1}\) on (5). The logarithmic number of dyads is absorbed by the stated subpower factor. Here \(1\le B\le D\) up to fixed dyadic constants, and \(K\le D^5\). The sign \(\mu(d)\) is exact before taking this outer absolute sum.

For \(K\ge B\), \(\theta=1\) makes the part before decay at most \(A_2\Phi(A_1,B)\), since \(\Phi(A_1,K)/K\) is nonincreasing. Thus this sector reaches the target with \(B\le D^{3/8}\) pure or \(B\le D^{8/15}\) mixed, regardless of the insertion length. For comparable \(B\asymp K\) the same caps follow with \(\theta=1/2\) in either orientation. Retaining the stronger decay exponent \(7/2\) when \(\theta=1/2\) gives in the comparable sector the bound \(A_2\Phi(A_1,B)(1+B/R)^{-7/2}\). This also meets target for \(B\ge D^{51/64}\) pure and \(B\ge D^{115/192}\) mixed. At the exact pure point the maximum monomial for \(B\ge R\) is \(A_1^{1/3} B^{5/6}\). At mixed it is the maximum of that term and \(B\). Each remaining slope after the decay is negative, so it suffices to check the lower endpoints.

## Small intermediate divisor and the unit slice

Use instead \(y_0^{-1}(y'_1)^{-1/2}\), retaining \((1+K/R)^{-7/2}\). The relative factor (4) cancels the remaining \(B^{1/2}K^{-1/2}\). The new prefactor is \(R^{3/2}/(\sqrt D\sqrt E)\), with scalar label weight
\[
 \frac{Nc}{E_1^{1/2}}\left(\frac{Nj}{N\widetilde q_d}\right)^{1/2}
 \frac{(N\mathfrak e_\ell)^{1/2}}
      {Ng\,N\ell\,Nz_*\,Nf\,(Na_0)^2(Nb)^2(N\ell_0)^3(Nv)^3(Nk_S)^{1/2}} .
\]
Pay \(Nc\) by \(c\mid z_*\), independently of every earlier forced \(z_*\)-prime: \(c\mid a\) and \(c\mid\bar\ell_{\rm g}\), whereas \(q_\ell\perp a\) and its conjugates lie in \(\ell\). The \(j\)-payment and both conjugate charges are valid as above. The \(f\)-sum is harmonic on polynomial support. The resulting per-\(d\) bound is
\[
 \frac{R^{3/2}}{\sqrt D\sqrt E\,A_1}
      \sqrt{\Phi(A_1,B)\Phi(A_1,K)} (1+K/R)^{-7/2}.                 \tag{6}
\]
For \(Nd\le X\) it costs at most \(O(X^{1/2})\) times the \(d=1\) budget by ideal counting. In particular the unit divisor meets the target for all comparable \(B\asymp K\) in both critical blocks. Pure \(B\le R\) costs at most \(D^{5/8}D^{1/8}=D^{3/4}\), and larger \(B\) decays. Mixed \(B\le R\) costs at most \(D^{3/8}D^{5/24}=D^{7/12}\), and larger \(B\) again decays by the same slope check.

The generic comparable midrange in the full divisor sum still exceeds target by (5). For example at \(B\asymp K\asymp R\) pure, the bound is \(D^{7/8}\), while summing (6) over \(Nd\le D^{1/4}\) spends the gain from its \(E^{-1/2}\) scale. These are bounds for the method. The result does not assert occupancy of the bound witnesses or lower energy estimates. The whole signed form and determinant and zero-location bridges remain open.
