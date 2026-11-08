# The mixed equal-norm cross on a near-norm strip

8 November 2026 UTC. Author draft for independent review.

## Exact projected terms

Use the original unweighted nonprincipal two-pivot Eisenstein rows and the actual residual of CONJUGATE_DUAL_OVERLAP-v2, before taking any absolute row or divisor sums. Keep \(S,\nu,u_0,Q_u\asymp R=A_1A_2\), the same common smooth complex \(W\) supported on \([1,2]\), \(U^2\le D\le7U^2/2\), and all \(\beta_{d,U,Z}\), literal ray, squarefree, capacity and common-prime masks. The full ordered cutoff coefficient is the case \(Z=U^2\). Use the original intermediate Möbius divisor \(d\). Keep the primitive Gauss phase \(\gamma_u\) and the full Poisson scalar.

After the ideal gcd \(g\) and conjugate overlap \(\ell\), write \(z_0=g\ell a'\) and \(k=g\bar\ell b'\). Thus \(\gcd(Na',Nb')=1\), with the exact phase
\[
 |\psi_u(g)|^2\psi_u(\ell)\overline{\psi_u(\bar\ell)}
                    \psi_u(a')\overline{\psi_u(b')}.
\]
Let \(V_d^{\mathrm{eq}}\) denote the equal-norm projection from that note, so \(Na'=Nb'=1\). Let \(V_d^{\mathrm{near}}(\Delta)\) use the same residual and keep precisely \(0<|Na'-Nb'|\le\Delta\). Use \(1\le\Delta\le D\), with exact inclusive upper endpoint. These are disjoint terms of the same exact amplitude. One may also keep only the remainder of the near strip after the other previously controlled pieces, by the inherited selectors. This definition takes the difference of the reduced integer norms, so it does not equate distinct ideal labels.

There is an exact additional identity on the equal-norm part where \(a=\ell\) and \(\bar a\) are both good:
\[
 \psi_u(a)\overline{\psi_u(\bar a)}
 =\nu(a)\overline{\nu(\bar a)}
       \left(\frac{Nu}{a}\right)_6 .
\]
Indeed conjugating the residue field and the sixth roots of unity gives
\((\bar u/a)_6=\overline{(u/\bar a)_6}\) with the same raw zero. Multiply by the raw symbol of \(u\) to get the symbol of \(u\bar u=Nu\). The factor \(|\psi_u(g)|^2\) remains, even for equal row norms. If \(\bar a\) meets \(S\), use its primitive value from the original formula. The proof below does not require \(S\) to be conjugation invariant or average equal row norms as independent phases.

## A row bound for the near-norm strip

For \(C\le Ng<2C,\ B\le N\ell<2B,\ K\le Nk<2K\), use \(P=J'/(CB)\), \(T=K/(CB)\), \(y=K/M\), and \(F=\sqrt{X A_2}/(E_0\sqrt{E_1})\), with the original definitions of \(J',X,E_0,E_1,M\). Then \(P,T\) are bounded below on live dyads, and \(T\le 2yR/(CB)\) from \(M<2R\). Let \(\Phi\) be the pinned sixth-order comparison polynomial of CONJUGATE_DUAL_OVERLAP-v2. The radial separation has mass \(O(\mathcal M_{12}(W)(1+y)^{-4})\).

First impose \(Nb'/2\le Na'\le2Nb'\). Now \(P\asymp T\) on any live dyad. At fixed \(g,\ell,b'\), the \(a'\)-sum has a coefficient support of size
\[
 O_\epsilon((DH)^\epsilon\min\{P,1+\Delta\}).
\]
The bound by \(P\) follows by ideal counting. For the other bound, the possible integer norms form an interval with at most \(2\lfloor\Delta\rfloor+1\) integers. There are at most \(\tau(n)\) integral Eisenstein ideals of norm \(n\). This follows by multiplying the counts at rational prime powers. They are \(j+1\) at a split prime with exponent \(j\), at most one at an inert prime, and one at the ramified prime. The actual coefficient of each selected ideal is divisor bounded, including the \(\beta_{d,U,Z}\) and the separated profile factor \(J/Nz\). Both coprimalities, the earlier projections, and the gap predicate are column selectors at fixed \(b'\) and fixed outer data. The row factor \(\overline{\psi_u(b')}\) retains its zero and phase.

Insert this coefficient squared mass into the sixth-order comparison for the \(a'\)-column after freezing the second pivot. The same \(O(CBT)\) choices for \(g,\ell,b'\) and Poisson prefactor as in (3) of CONJUGATE_DUAL_OVERLAP-v2 give the following squared row norm bound before the remaining harmonic sums:
\[
 (DH)^\epsilon\mathcal M_{12}(W)^2 F^2\,
 \frac{T}{P}\min\{P,1+\Delta\}\Phi(A_1,\max(1,P))\,y(1+y)^{-8}.
 \tag{1}
\]
In particular it is valid with the exact strict exclusion of the equal-norm terms.

Use \(P\ll T\ll yR\) and the degree at most one of \(\Phi\) in its length to bound the factor following \(F^2\) by
\(O((1+\Delta)\Phi(A_1,R))\). The remaining dyadic sums cost subpowers. If the norms are not comparable, the gap condition implies both \(Na',Nb'\le2\Delta\). Split into the two disjoint directions \(Na'>2Nb'\) or \(Nb'>2Na'\). For each, the exact ratio and gap cuts can be separated at a subpower cost as follows. On the rectangle \(Na',Nb'\le2\Delta\), use the two additive step indicators in the integer linear forms \(Na'-Nb'\) and \(Na'-2Nb'\) for the first direction, or their exchanged versions for the second. Take a common cyclic modulus larger than twice every absolute linear-form value on the rectangle. Use the interval of positive gaps \(1,\ldots,\lfloor\Delta\rfloor\) and the interval of positive values of the second form in that modulus. Their Fourier coefficient absolute sums are \(O(\log(2D))\) by the geometric series. Each Fourier phase factors into the two column coefficients. The exact two-lcm coprimality projector then applies as in the joint rectangle of CONJUGATE_DUAL_OVERLAP-v2. This gives a squared bound with \(\Phi(A_1,(1+\Delta)^2)\) in place of the comparable contribution, including subunit dyads and the boundary factor of two.

Summing \(e_1,e_0,r,z,g,\ell,k\) in the row norm as in that note gives
\[
 \frac{\|V_d^{\mathrm{near}}(\Delta)\|_2^2}{D}
 \ll_{\epsilon,\eta} \frac{(DH)^\epsilon \mathcal M_{12}(W)^2 A_2}{Nd}
 \left[(1+\Delta)\Phi(A_1,R)+\Phi(A_1,(1+\Delta)^2)\right].
 \tag{2}
\]
The same bound after harmonic summation in \(d\) holds with \(1/Nd\) removed. For the comparable branch alone, adding both \(Nb'\le B_0\) and \(NgN\ell\ge G_0\) replaces \(R\) by \(\min\{B_0,\max(1,R/G_0)\}\) in its length. Indeed \(T\ll\min(B_0,yR/G_0)\) and \(y\max(1,y)(1+y)^{-8}\) is bounded. This variant uses the same physical norms in the kernel.

## Freezing the comparable radial profile at equality

In the comparable branch the profile argument is \(\lambda s\), with \(\lambda=X/(E E_0 Q_u)\) and \(s=Nb'/Na'\). Retain the exact prefactor \(1/Nz\), row phases, all masks and the gap. Split only
\[
 G_W(\lambda s)=G_W(\lambda)+
    (\log s)\int_0^1 (\lambda s^\theta)G'_W(\lambda s^\theta)\,d\theta .
 \tag{3}
\]
Here \(s\) stays in \([1/2,2]\), \(\lambda\asymp y\), and \(|\log s|\ll\min(1,\Delta/P)\). The comparability \(\lambda\asymp y\) follows from \(y/\lambda=(K/J')(Q_u/R)\) and \(T/P=K/J'\). Use the same log Fourier separation for the derivative profile in (3), with mass \(O(\mathcal M_{16}(W)(1+y)^{-4})\), uniformly in \(\theta\). To see the regularity budget, the two log derivatives for the Fourier absolute sum, together with the one derivative in (3), give up to three powers of the radial frequency multiplying derivatives of the two-dimensional Fourier transform. Twelve integrations by parts in the radial direction suffice for \((1+y)^{-4}\) on large arguments, with the smooth compactly supported radial lift of \(W\). Bounded arguments use its bounded moments. A fixed-width log cutoff covers the actual ratios, and the Fourier phase from \(s^\theta\) splits between \(a'\) and \(b'\). The extra \(\log s\) is an \(a'\)-coefficient at fixed \(b'\).

Thus the error in (3) gains \(\min(1,\Delta/P)^2\) in (1). The length and count satisfy
\[
 \min\{P,1+\Delta\}\min(1,\Delta/P)^2\Phi(A_1,\max(1,P))
      \ll (1+\Delta)\Phi(A_1,1+\Delta).
\]
For \(P\le1+\Delta\) use monotonicity. For larger \(P\) use the degree bound and the factor \((\Delta/P)^2\). Let \(V_d^{\mathrm{err}}\) be the resulting comparable variation term. Its normalized positive energy after the \(d\)-sum is at most
\[
 (DH)^\epsilon \mathcal M_{16}(W)^2 A_2(1+\Delta)\Phi(A_1,1+\Delta)
 \tag{4}
\]
up to a fixed implied constant. This split does not claim cancellation in the comparable leading term \(G_W(\lambda)\).

## Mixed cross bounds and remaining obligation

At the exact mixed scales \(A_1\asymp D^{5/12}, A_2\asymp D^{1/6}\) the equal-norm energy has power \(7/12\). The comparable term of (2) at \(\Delta=D^\delta\) has power \(19/24+\delta\). At \(\delta=1/8\) this is \(11/12\), and the noncomparable term has power \(43/72\). Hence the actual signed cross
\[
 \frac{2}{D}\operatorname{Re}\sum_d\mu(d)
        \langle V_d^{\mathrm{eq}},V_d^{\mathrm{near}}(D^{1/8})\rangle
\]
is \(O((DH)^\epsilon\mathcal M_{12}(W)^2D^{3/4})\) by absolute Cauchy. This applies also to any restriction of the divisor sum, including the unit divisor. At \(\Delta=D^{7/60}\) the cross power is \(179/240\) at the exact mixed scales and remains below \(3/4\) in the feasible \(1/2000\) pivot neighborhood. The result uses the signed identity with the original \(\mu(d)\), followed by absolute Cauchy.

For (4), the choice \(\Delta=D^{29/96}\) gives variation power \(11/12\) and therefore target cross with the equal-norm projection. The noncomparable term for this wider strip has power \(233/288\), also below \(11/12\). Thus from the region \(D^{1/8}<|Na'-Nb'|\le D^{29/96}\) only the comparable leading profile term remains in this cross comparison. A trial that keeps the full wider comparable term in (2) gives cross power \(161/192\), above target. For the entire mixed cross the previous \(Nd\ge D^{1/5}\) bound still applies. The remaining small-divisor cross includes the leading comparable term in the intermediate strip and the far strip, with all original phases and masks. No whole signed bound or zero-location estimate follows. Independent review is pending.

## Further localization by the comparable length

An additional dyadic split improves the variation comparison. At \(P\le L\) on the comparable strip, \(Na',Nb'\ll L\). Insert the exact gap and the two inclusive comparison inequalities by finite Fourier expansion of step indicators in \(Na'-Nb'\), \(2Na'-Nb'\) and \(2Nb'-Na'\). For each finite frequency their factors separate between \(a'\) and \(b'\). Choose the modulus larger than twice all absolute arguments, as above, and use the same two-lcm projector. The joint fourth moment bounds the full comparable term by a positive energy with factor \(A_2\Phi(A_1,L^2)\). It gives the same bound for the frozen leading term because \(G_W(\lambda)\) is a row multiplier of size \(O(\mathcal M_{12}(W)(1+y)^{-4})\), uniformly in the dyad. The variation is their difference and inherits the bound by the norm triangle.

At \(P>L\ge1+\Delta\) use (1) with the variation factor. Since the polynomial has degree at most one in \(P\), \(\Phi(A_1,P)/P^2\) is decreasing. After the harmonic sums the high-length variation has energy with factor
\[
 A_2(1+\Delta)^3\,\Phi(A_1,L)/L^2 .
\]
Take \(L=D^{11/30}\) at the exact mixed scales. The low-length energy has power \(11/12\), giving target-size cross for the full strip there. The high-length variation also reaches energy power \(11/12\) at \(\Delta=D^{73/216}\), up to fixed constants and subpowers. Here the monomial of \(\Phi(A_1,L)\) is \(A_1^{5/6}L^{1/3}\) and the high-length power is \(3\delta-7/72\). The noncomparable term of the full strip has power \(563/648\) at that wider gap, again below \(11/12\). Thus in the wider strip only the leading comparable profile on \(P>D^{11/30}\), outside the already controlled narrow gap, remains for this cross. The off-strip and other small-divisor crosses retain their previous status.
