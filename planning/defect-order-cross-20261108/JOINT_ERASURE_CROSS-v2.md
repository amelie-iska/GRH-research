# Coherent erasures from the cutoff and conjugate overlap

8 November 2026 UTC. Use the exact selected pairing of MATCHED_POISSON_CROSS-v2, with the same \(d,E_i,h_i,z,g,\ell,k\) notation, unweighted literal rows, fixed \(S,\nu,u_0\), common \(W\), \(Z=U^2\) and \(U^2\le D\le7U^2/2\). Write \(R=A_1A_2\), \(E=Nd\), and \(A_1A_2^2\ll H\). This note estimates a joint part of the original normalized cross. Use the original \(Nk>D^5\) rapid tail first, and keep all exact allocation, primal-zero, endpoint, capacity, ray, conductor, and union mask factors on the remaining terms.

Let the defects outside \(d\) be the union of these two disjoint classes, with no other off-\(d\) change:

1. \(\mathfrak q_z\mid z\) consists of primes \(p\nmid a b\ell\bar\ell_{\rm g}d\), each with the old \(\beta=1\) from \(z\) and the new \(\beta'=0\).
2. \(\mathfrak q_\ell\mid\bar\ell_{\rm g}\) consists of primes \(p\nmid a b d\), each with the old \(\beta=1+\mathbf 1_{p\mid z}\) from \(\bar\ell_{\rm g}\) and possibly \(z\), and the new \(\beta'=0\). Put \(\mathfrak e_\ell=\prod_{p\mid\mathfrak q_\ell}p^{1+\mathbf 1_{p\mid z_*}}\) with \(z_*=z/\mathfrak q_z\), so \(N\mathfrak e_\ell\le(N\mathfrak q_\ell)^2\).

Allow arbitrary defect changes at good primes of \(d\). Write \(\widetilde q_d\) for the actual ideal with the new residues in \(\{0,\dots,5\}\) on \(d\). All three sets may occur in the same pairing. Any one may be empty, and we use the unit convention for its product. As in the parent proof, \(k\) still carries the unrestricted good sixth-power factor \(v^6\) and its raw zeros.

## Freeze the conjugate overlap and average the cutoff ideal

Put \(z=\mathfrak q_z z_*\), and freeze the other labels, including \(\mathfrak q_\ell,\widetilde q_d\). On this support \(c=(z,a,\bar\ell_{\rm g})\) and \(\ell_0=\ell/(\ell,zb)\) are unchanged when \(z\) is replaced by \(z_*\). The exact sixth-free representative in the partner is
\[
 k'_\flat=\frac{z_* a^4 b^2\ell_0^6(\bar\ell_{\rm g}/j)\,\widetilde q_d}
                   {\ell c^6\mathfrak e_\ell}.
 \tag{1}
\]
The supports of \(\mathfrak q_z\) and \(\mathfrak q_\ell\) avoid \(d\), and \(j=(\bar\ell_{\rm g},d)\). Formula (1) follows by substituting the two erased factors in the matched representative, and uses the exact new residue on \(d\), rather than dividing by a removed prime there. At fixed remaining labels, \(k=k_S k'_\flat v^6\) is independent of \(\mathfrak q_z\). The sole variable good character factor on the first row pivot is the raw sextic symbol at \(\mathfrak q_z\), or its conjugate if the pairing is conjugated. This factor includes its own zero. All other phase factors and raw zeros are fixed in the \(\mathfrak q_z\) sum. The symbol of the fixed \(u_0\alpha_{v_2}^2\) and \(\nu\) on \(\mathfrak q_z\) stay in the coefficient. Collisions of \(\mathfrak q_z\) with the fixed \(g\) or \(v\) are permitted and retain the corresponding raw mask.

Use a norm dyad \(B\le N\mathfrak q_z<2B\), with \(B\le D\). At fixed other labels, the coefficient of each \(\mathfrak q_z\) contains the original grouped cutoff values and selectors, and is divisor bounded after removing \(1/N\mathfrak q_z\). The exact partner argument is a fixed multiple of \((N\mathfrak q_z Q_u)^{-1}\). Separate these two variables by Fourier inversion on a bounded log interval, as in the \(z\)-only calculation. The Fourier absolute integral is bounded by the same radial majorant \(O(\mathcal M_{12}(W)(1+y'_1)^{-4})\), including its dyadic scale. The equality profile and \(Q_u^{-1}\) remain row multipliers. Cauchy in the original row variable followed by the pinned sixth-order comparison \(\Phi_6(A_1,B)=A_1+B+A_1^{5/6}B^{1/3}+A_1^{1/3}B^{5/6}\) applies after the \(\mathfrak q_z\) phases have been summed together. The squared column mass is \(O((DH)^\epsilon/B)\), and for fixed second pivot the row count is \(O(A_1)\). Thus the cost relative to the trivial row count and harmonic dyadic \(\mathfrak q_z\) count is
\[
 L(B)=\left(\frac{\Phi_6(A_1,B)}{A_1 B}\right)^{1/2}.
\]
The case \(\mathfrak q_z=1\) has trivial relative cost 1, also bounded by \(L(1)\). Exact cutoffs can impose arbitrary ideal predicates on \(\mathfrak q_z\). They remain coefficients before Cauchy. Enlargement to apply the sieve occurs only in the positive row norm.

## The conjugate charge and divisor sum

Now use the profile split \(y_0^{-5/6}(y'_1)^{-1/6}\). Compared with (1) in DEFECT_ORDER_CROSS-v1, replace \(Nz\) by \(Nz_*\) in the outer harmonic weight, since \(1/N\mathfrak q_z\) went into the sieve. The partner radial scale contains the extra factor \((B N\mathfrak e_\ell)^{-1}\), and \(q_d\) in that scale is now \(\widetilde q_d\). Up to fixed constants, the resulting factor is \(R L(B) B^{1/6}(N\mathfrak e_\ell)^{1/6}/E\) times
\[
 \frac{(Nj)^{1/6}}{E_0^{1/6}E_1^{5/6}(N\widetilde q_d)^{1/6}}\,
 \frac{1}{Ng\,N\ell\,Nz_*\, (Nf)^2\,Na_0\,(Nb)^2\,N\ell_0\,Nv\,(Nk_S)^{1/6}} .
 \tag{2}
\]
The \(c\)-power cancels, and choices of \(c\mid\bar\ell_{\rm g}\) cost a divisor factor. Summing \(\ell\) harmonically uses \(\overline{\mathfrak q_\ell}\bar j\mid\ell\), with the two divisors disjoint. This pays \(1/(N\mathfrak q_\ell\,Nj)\). The \(d\)-dependent factor in (2) is then bounded by 1 up to fixed \(S\)-constants. The choices of \(j,j_0,j_1,\widetilde q_d\) at fixed \(d\) cost a divisor factor, including arbitrary new \(d\)-residues. No coprimality between \(d\) and the original raw row has been dropped in the exact sum.

There is a second payment for each \(p\mid\mathfrak q_\ell\). Its conjugate \(\bar p\) divides \(\ell\), and therefore lies in exactly one of \(\ell_0,z_*,b\) on the original support. Indeed \(\ell_0=\ell/(\ell,zb)\), \(z\perp b\), and \(\mathfrak q_z\perp\ell\). Partition by these three cases. In the first case use the explicit \(1/N\ell_0\) in (2); in the second use a forced divisor in the harmonic \(z_*\) sum; in the third use the inverse square in the \(b\)-sum. The first payment used the harmonic \(\ell\) count. This second payment uses the explicit factor \(1/N\ell_0\) or an independent label weight. No harmonic count is charged twice at the same prime. Distinct \(p\) have distinct conjugates, and no \(\mathfrak q_z\) label is counted in any of these payments. Thus \(N\mathfrak q_\ell\) costs altogether at least \((N\mathfrak q_\ell)^{-5/3}\) after its radial factor. Its ideal sum converges, with only divisor multiplicity for the case partition.

The remaining scalar counts are convergent or harmonic with polynomial cutoffs. In particular \(Nv\ll D^{5/6}\) after the exact frequency tail and \(Nk_S\) has a fixed geometric sum at exponent \(1/6\). The normalized bound at fixed \(d,B\) is
\[
 \ll_\epsilon (DH)^\epsilon\mathcal M_{12}(W)^2
       \frac{R}{E}\,B^{1/6} L(B).
 \tag{3}
\]
The factors \(\mu(d)\) are part of the original expression. We bound the \(d\)-sum harmonically in absolute value after the coherent \(\mathfrak q_z\) estimate.

The four terms bounding \(B^{1/6}L(B)\) are
\(B^{-1/3}, A_1^{-1/2}B^{1/6}, A_1^{-1/12}B^{-1/6}, A_1^{-1/3}B^{1/12}\).
For \(1\le B\le D\), after multiplying by \(R\) they are bounded by \(R,\sqrt{H}D^{1/6},R,H^{2/3}D^{1/12}\), since \(R/\sqrt{A_1}\ll\sqrt H\) and \(R/A_1^{1/3}\ll H^{2/3}\). Consequently this simultaneous selected sector reaches \(D^{3/4+\epsilon}\) at \(H=D^{3/4}\) in every original two-pivot block with the stated capacity, with no good-defect conductor cap. At the critical pure and mixed points with \(B\ge D^{5/8}\), the respective exponents sharpen to \(7/12\) and \(13/24\). These powers use the lower bound on \(B=N\mathfrak q_z\) up to fixed dyadic factors, not a lower bound on the total defect conductor. The result includes the unit divisor. It leaves the pairing of weak insertions and erasures from other sources open, along with the whole signed form, determinant and zero-location bridge.
