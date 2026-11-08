# Overlap, residual sixth powers, and the compensated Gauss phase

7 November 2026 UTC. Author draft, independent review pending. Acceptance requires the exact phase in the existing primary convention, a joint overlap/sixth-power budget for the actual completed comparison, and explicit retention of raw zeros, the pair-dependent Gaussian, and the still-open sector. This note works in the central far-gap split-prime unit-cofactor comparison of GAP_DOUBLE_POISSON-v1 (2)–(3) and GAP_DUAL_COLOURS-v2. The transfer from the original signed pairing still uses the prior pending reductions. No new claim about the other actual signed terms is made.

## 1. The angular factor cancels against the local completion phases

Let \(q\) be a good split prime of the prime band, \(\gamma=\alpha_q\equiv1\bmod3\), \(p=Nq\), \(\theta=(\cdot/q)_6\), \(\chi=\theta^2\), and \(\phi=\theta^3\). Write \(g(j)=\tau_\gamma(\theta^j)/\sqrt p\) in the existing additive pairing \(e_\gamma(z)=\exp(2\pi i\operatorname{Tr}(z/(\delta\gamma)))\), \(\delta=1+2\omega\). In particular \(g(2)=G_q^{\rm act}\) in rg:normalizations, not its conjugate or the source frequency convention. Use the actual accepted Jacobi gauge
\[
 \rho_J(q)=J(\theta,\chi)/\sqrt p=\mu(q)\vartheta(q).
\]
Here \(\vartheta=\Psi/\sqrt N\) has the nonzero infinity type stated in sw:character. In the orientation where the original separated \(q\)-coefficient contains \(\vartheta(q)\overline{G_q^{\rm act}}\), write
\[
 b_q=\widetilde b_q\vartheta(q)\overline{g_q(2)}.
\]
This is a modulus-preserving factorization of that actual coefficient. Its signs (including a separately assigned \(\mu\), if present), inverse-norm weight, literal \(k\) symbol, finite ray/source phases, other deletions and Mellin factors all stay in \(\widetilde b\). For the wholly conjugate orientation conjugate the whole formula; do not conjugate just a Gauss factor. The statement about cancellation concerns the displayed Jacobi angle, not an assertion that every factor in \(\widetilde b\) is a finite-order character.

For completeness, let \(\xi\) be either \(\chi\) or \(\bar\chi\). All involved characters other than the implicit principal count are nontrivial. The change \(t=2x-1\) over the residue field gives
\[
 J(\xi,\xi)
   =\bar\xi(4)\sum_t\xi(1-t^2)
   =\bar\xi(4)J(\xi,\phi).
\]
The second equality uses the count \(1+\phi(y)\) of square roots of \(y\) (including \(y=0\)) and \(\sum_y\xi(1-y)=0\). The elementary Gauss–Jacobi product formula at the same additive character then gives, in normalized notation,
\[
 g(\xi)g(\xi\phi)=\bar\xi(4)g(\xi^2)g(\phi).
 \tag{1}
\]
Indeed \(\tau(\xi)\tau(\phi)/\tau(\xi\phi)=\xi(4)\tau(\xi)^2/\tau(\xi^2)\), and these denominators are nonzero by primitivity. Applying (1) first with \(\chi\) and then with \(\bar\chi\), and using \(g(4)=\overline{g(2)}\) because \(\chi(-1)=1\), gives
\[
 g(2)g(5)=\bar\chi(4)\overline{g(2)}\,g(3),
 \qquad
 \rho_J(q)=\frac{g(1)g(2)}{g(3)}=\chi(4)g(2)^3 .
 \tag{2}
\]
Consequently the actual compensated single-prime coefficient is
\[
 b_q g_q(2)g_q(5)=\mu(q)\widetilde b_q\,g_q(2)g_q(3).
 \tag{3}
\]
The cubic Gauss factor now has the positive orientation. There is no extra \(\chi(4)\) left over and there is no disappearance of the cubic Gauss factor.

For distinct \(q,q'\), the CRT multiplier in the joint Poisson formula is \(K(q,q')=\theta_q(\alpha_{q'})\overline{\theta_{q'}(\alpha_q)}\). In the primary convention \(K=K^3\) by cubic reciprocity. The exact conjugation relation on the \(q'\) side of the two Gauss factors supplies \(\theta_{q'}(-1)\). As \(g_{q'}(3)=\theta_{q'}(-1)\overline{g_{q'}(3)}\), the product of the quadratic Gauss factors and this sign is
\[
 K(q,q')\,g_q(3)\,\theta_{q'}(-1)\overline{g_{q'}(3)}
 = K(q,q')g_q(3)g_{q'}(3)=\Gamma(\alpha_q\alpha_{q'}),
\]
by the already recorded literal period-four evaluation in gtl:root-cubic. Thus the complete coefficient multiplying the raw joint symbol in (2) of the earlier draft can be written exactly as
\[
 b_q\overline{b_{q'}} L(q,q')
   =\mu(q)\mu(q')\Gamma(\alpha_q\alpha_{q'})
       \widetilde b_q\overline{\widetilde b_{q'}}\,
          G_q^{\rm act}\overline{G_{q'}^{\rm act}} . \tag{4}
\]
For prime \(q,q'\) the displayed pair of Möbius factors equals one; the expression makes the single-column sign convention explicit. The same formula applies to distinct conjugate prime ideals of equal norm, which are coprime ideals; it is not a primitive calculation at \(q=q'\). The remaining mod-four factor is constant on fixed pairs of generator classes and is kept throughout. This exact normalization removes the identified varying angular character from the coefficient. It does not permit a fixed cubic prime sequence in the high-sector estimate: \(\theta_q^3(\beta)\) remains an actual growing quadratic twist in \(\theta_q(\beta\alpha^4)\), with all raw zeros, as does the cubic factor \(\theta_q^4(\alpha\beta)\). We apply no prime Gauss distribution theorem to it.

## 2. A simultaneous overlap and sixth-power cut with all zeros retained

Use \(A=T^2/P,\ V=T^2/R,\ P,T\asymp D^{1/2}\) and \(D^{13/40}\le R\le D^{27/80}\), as before. For nonzero \(\alpha,\beta\), define \(g=((\alpha),(\beta))_{\rm good}\), the common ideal with the **full minimum** valuation at good primes and zero at \(S\). This is not the gcd of the two conductor radicals, nor is it the gcd in the original signed pairing. In particular a prime dividing only \(\beta\) can occur in both conductor components without dividing \(g\). Write \(\alpha=\alpha_g x,\ \beta=\alpha_g y\). Factor the nonzero element \(y=u_S\alpha_a\alpha_d^6\), with \(u_S\) literal including its unit, \(a\) a good sixth-free ideal and \(d\) an arbitrary good ideal. These are unique from the valuations and the multiplicative primary section. A prime of \(d\) may divide \(a\) or \(g\). At each of the actual prime columns \(q\) the exact identity is
\[
 \theta_q(\beta\alpha^4)=
 \theta_q(\alpha_g)^5 \theta_q(x)^4 \theta_q(u_S)
       \theta_q(\alpha_a)\,\mathbf1_{(d,q)=1}. \tag{5}
\]
The individual powers are extended by zero. The fact that the sixth-power phase becomes an indicator is an equality even when \(a,d\) overlap. No primitive-conductor substitution removes a prime at which the original symbol is zero.

Let \(\mathcal E\) be any further \(q,q'\)-independent selection of dual pairs, with \(G\le Ng<2G\) and \(Nd\ge J\) (\(G,J\ge1\)). In particular \(\mathcal E\) can retain both-large conductor conditions and the preceding first-frequency complement. Perform the exact log-\(Q\) separation of GAP_DUAL_COLOURS-v2 §1 with either the original coefficient representation or (4). At each Fourier parameter and pair of classes, algebraically subtract the inserted \(q=q'\) terms and apply Cauchy over \(\mathcal E\) to the two single-prime sums. In the resulting positive norms fix \(g,x,u_S,d\), absorbing every factor of (5) except \(\theta_q(\alpha_a)\) into the corresponding coefficient vectors. Only then relax the row selection on \(a\) to a power-free ideal family. The fixed multipliers are bounded by one; their exact raw zeros are not relaxed. Apply the already pinned de Faveri Theorem 1.1 in the literal family phy:input, phy:generator-proof, with physical sixth-free length \(L/(Nu_S(Nd)^6)\), \(L=V/G\). There is no claim about a conductor-indexed replacement for this physical length.

For the first box the number of \(g,x\) pairs is \(O(A)\): for each \(g\), there are \(O(A/Ng)\) nonzero \(x\)'s when this length is at least one, and there are \(O(G)\) ideals in the \(g\) band. A subunit length means no pair, with the unit included at equality. For the sixth-free sum the terms with powers \(1,5/6,1/3\) in its first length have tail factors \(J^{-5},J^{-4},J^{-1}\) respectively after summing \(d\) with \(Nd\ge J\). This is ordinary ideal counting with exponents \(6,5,2\). The \(T\)-term costs \(T L^{1/6}\) because \(Nd\le(L/Nu_S)^{1/6}\); it does not acquire a decreasing power of \(J\) by absolute summation. The \(u_S\) factors have convergent positive norm powers, including the count for that \(T\)-term. The inserted diagonal is covered by the same counting as the first term: at fixed \(g,x,u_S,d\) the number of \(a\)'s is \(O(L/(Nu_S(Nd)^6))\) when nonempty. This diagonal is not the genuine primal \(q=q'\) term.

The net prefactor is \((PR/T^2)A=R\). In the outer boxes use \(A_i=2^i A,\ V_j=2^j V\) in place of the count lengths and multiply by the corresponding exponential factors from log-\(Q\) separation. The resulting polynomial increases are summable; if \(L<1\) in the first box one can keep the monomials at \(L\) as upper bounds after summing the nonempty outer boxes. Hence the absolute contribution of this entire off-diagonal sector is bounded by
\[
 \ll_{S,\varepsilon}
 (DH)^\varepsilon\|b\|_2^2 R
 \left\{
   (V/G)J^{-5} + T(V/G)^{1/6}
   + (V/G)^{5/6}T^{1/3} J^{-4}
   + (V/G)^{1/3}T^{5/6} J^{-1}
 \right\}. \tag{6}
\]
Take fixed cut parameters in polynomial ranges; more distant dyads are absorbed by the same tails. Both underlying cutoff boundaries and all orientations are kept by using a subset of the actual pairs before positivity. There is no absolute triangle over prime conductors in this argument.

In particular, select the joint region
\[
 (Ng)^{5/6}(Nd)^4\ \ge D^{1/12}. \tag{7}
\]
For a dyadic \(G\), (7) implies \(Nd\ge J=\max(1,D^{1/48}(2G)^{-5/24})\), so \(G^{5/6}J^4\gg D^{1/12}\), also when \(J=1\). The third term of (6) therefore has exponent at most \(1+r/6-1/12\) with \(r=\log_D R\); the first has exponent at most \(11/12\) since \(GJ^5\ge G^{5/6}J^4\). Even ignoring the cuts in the second and fourth, their exponents are at most \(2/3+5r/6\) and \(3/4+2r/3\). Across the central interval the four worst exponents are \(11/12,\ 91/96,\ 467/480,\ 39/40\). Summing the dyads costs subpowers. The resulting joint piece has upper budget \(D^{39/40+\varepsilon}\|b\|_2^2\). In the prior density scale comparison, testing with a squared partner \(D\) and \(X\le D^{3/8}\), each of the four powers would give relative exponent at most \(-1/160\): for the third the test is \(1/48-r/12\), for the fourth it is \(-1/16+r/6\), and the first two are smaller on the interval. This remains a comparison of parts of an auxiliary norm, not a statement about separately selected original signed terms. Large overlap \(Ng\ge D^{1/10}\), large residual sixth-power root \(Nd\ge D^{1/48}\), and intermediate combinations satisfying (7) are included. A large sixth-power factor of \(\beta\) must not simply be identified with \(d^6\) after dividing by \(g\).

## 3. Surviving principal-scale case and limitation of this route

The current unestimated joint sector may now be restricted to \(B_2>D^{7/24}\), \(B_3>D^{31/80}\), \(N\alpha>A D^{-1/12}\), small good squarefull part of \((\alpha)\), and \((Ng)^{5/6}(Nd)^4<D^{1/12}\), with the same raw Gaussian, fixed classes, angular compensation (4) and residual phases. This includes coprime squarefree \((\alpha),(\beta)\), where \(g=d=1\), the quadratic conductor can be \(N\beta\), and the cubic conductor can be \(N(\alpha\beta)\). No division by \(b_q\), removal of orientations, or replacement of the two component conductors by their product has been used. At \(g=d=1\) the separated sextic term of (6) still costs \(D^{1+r/6}\). The overlap/sixth-power method therefore fails to improve the inherited \(D\) bound on the full squared original comparison; cancellation of the angle alone gives no saving in that estimate. The next step is to use the actual cubic Gauss phases with the growing quadratic twist jointly at these principal scales, or to work directly before the original signed Cauchy comparison. The full unit/nonunit-cofactor pairing, candidate \(109/144\), whole signed \(13/12\), global \(9/8\), determinant/zero-location, Lean and GRH remain open.
