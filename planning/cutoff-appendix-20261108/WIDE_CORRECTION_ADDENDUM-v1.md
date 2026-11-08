# Full-frequency compensation and an equality-side divisor prefix

8 November 2026 UTC. Retain the original unweighted rows, fixed data, exact primitive conductor, common profile and original Poisson windows of WIDE_CORRECTION-v1. The two conclusions below use different selections of the original equality-versus-complement cross.

## 1. Recombine the partner small-prime subtractions over its full frequency sum

Fix \(p\in\mathcal P\), an actual good prime ideal of norm \(7\) or \(13\), and fix the order of each cutoff factorization \(\zeta=\zeta_1\zeta_2\). The signed \(p\)-subtraction in the coefficient of (1) of WIDE_CORRECTION-v1 is
\[
 -\mu(\zeta)\mu(d)
 \sum_{\substack{mn=d,\ p\mid m\\Nm>T_1Np,\ Nn>T_2}}1 .
\]
Use this coefficient on the partner side, summing the original ordered splits. It is independent of the partner frequency and bounded by a divisor factor, since at fixed split its count is at most the number of divisors of \(d\). The fixed signs are part of the coefficient. Define \(V_d^{[p]}\) by replacing the partner cutoff coefficient with this one in the original primal amplitude, keeping the original allocation and zero-removal tests. Define \(E_d^{[p]}\) as its original middle equality projection. These are linear coefficient modifications of the same exact Poisson representation.

Every contributing split has \(E N\zeta>Np\,U^2\ge7U^2\ge2D\), with \(E=Nd\). The original primal profile is
\[
 W\!\left(\frac{E E_1(Nh)^2 Nz_0\,Nb}{D}\right),
 \qquad \zeta=e_0z_0,\quad h=re_0,\quad Nb\ge1 .
\]
Here \(E_1=Ne_1\) is the partner deletion factor, and \(E_1(Nh)^2\ge Ne_0\). The argument exceeds two, so each primal summand vanishes. Thus \(V_d^{[p]}=0\) exactly and the full original partner complement with this coefficient is
\[
 V_d^{[p]}-E_d^{[p]}=-E_d^{[p]} .
\]
In particular it cannot be replaced by zero inside the cross. It is the compensating middle equality term.

The elementary equality estimate of GROUPED_EQUAL_CROSS-v4 applies to \(E_d^{[p]}\). Its proof uses the number of \((g,\ell)\) at fixed norm scale, the raw row factors bounded by one, \(Q_u\asymp R\) and a divisor-bounded row-independent coefficient at each allocation. The new coefficient meets these conditions because its additional divisor sum is over \(m\mid d\) and the ordered split of \(\zeta\) only. The original \(r,e_0,e_1,J\) sums, the primitive \(S\)-values and the exact window remain as in that estimate. Consequently both \(D^{-1}\|E_d^{[p]}\|_2^2\) and \(D^{-1}\|E_d\|_2^2\) are \(O((DH)^\epsilon\mathcal M_{24}(W)^2 R/E)\). Cauchy in the actual row norm followed by the harmonic divisor sum gives \(O((DH)^\epsilon\mathcal M_{24}(W)^2R)\) for this original cross contribution. The same holds after summing the finitely many \(p\)'s.

The compensation requires the full partner frequency sum, including the re-expressed direct part. This argument does not estimate the \(p\)-subtraction after selecting only particular partner defect modes or physical insertion dyads.

## 2. Equality-side wide corrections at smaller pure divisors

Now restrict to the original pure comparable sector of TWO_FAMILY_CROSS-v1 and POWERFUL_FREEZE-v1, with \(A_1\asymp R\asymp D^{3/4}\), \(A_2\asymp1\) and \(B,K\asymp R\). Take the \(C_d\) correction part of (1) of WIDE_CORRECTION-v1 on the equality side, with the original partner cutoff coefficient or either of its step and correction parts. Retain both erasure kinds, all permitted positive increments, arbitrary changed \(d\)-residues and every raw mask. The bound here applies to the actual complement, including the re-expressed direct term. An equality-side correction may be paired with a partner correction, so the double-wide part is included.

All modified cutoff coefficients are divisor bounded on the polynomial support and depend only on their own actual cutoff label and the fixed allocations. In particular the partner coefficient, if changed, is a predicate or coefficient on \(x\) alone after fixing its other labels. The \(I\)-array stays the same complete eligible insertion interval with the same fixed masks. Apply the ordinary erased sieve and the pure sharp insertion moment of SHARP_INSERTION_POISSON-v1, using the powerful freezing of POWERFUL_FREEZE-v1 and the exact \(s_1\)-eligibility of PROJECTOR_CLARIFICATION-v1. The squared erased mass at length \(B/Ns_1\) is \(O((DH)^\epsilon/(B Ns_1))\), and its sieve factor has \(\Phi_6(A_1,B/Ns_1)/A_1\ll D^{1/8}\). At fixed powerful part \(P\), the sharp insertion squared row norm is \(O((DH)^\epsilon A_1 K/(NP\,Ns_1))\) per fixed second pivot, with the original exact profile separation. Thus the product of the moments has a relative factor \(D^{1/16}\) above \(A_1\sqrt{K/B}\), times \((Ns_1)^{-1}(NP)^{-1/2}\). The \(s_1\)-sum is harmonic and the count \(O(\sqrt M)\) for \(NP\asymp M\) pays the powerful shortening.

Write \(E_0=Ne_{1,0}\) and \(h_0\) for the equality-side deletion and grouped square divisor. A nonzero equality-side correction requires \(\Omega_0>1\) and hence \(E_0Nh_0<14\) by the original primal dyad bound. The equality-side radial scale is
\[
 y_0=\frac{D}{E E_0(Nh_0)^2 R}\gg \frac{D}{ER} .
\]
The comparison \(Q_u\asymp R\) here only bounds the actual profile. Keep the original \(Q_u\), phases and all raw zeros in the exact sum.

Use both half radial powers in the label comparison of TWO_FAMILY_CROSS-v1. On the equality side
\((1+y_0)^{-4}\le y_0^{-1/2}(1+y_0)^{-7/2}\). On the partner side use the same half power of its separated Fourier mass, which has the original fourth power of decay with the weighted log integral. The \(R/E\) label comparison then holds with the additional uniform equality factor \((1+D/(ER))^{-7/2}\) and the relative moment loss \(D^{1/16}\) above. The exact conjugate erasure, \(d\)-residue, common-prime and fixed-label charges in that half-power comparison remain available, because no label weight has been dropped before forming the two arrays. Thus the rectangle contributes at most
\[
 O\!\left((DH)^\epsilon\mathcal M_{24}(W)^2
           \frac{R}{E}D^{1/16}\left(1+\frac{D}{ER}\right)^{-7/2}\right)
\]
at fixed \(d\). Restore the exact middle subtraction separately at cost \(O((DH)^\epsilon\mathcal M_{24}(W)^2R/E)\), since the integer norm equality and the divisor-bounded coefficient count are unchanged.

For \(E\le D^{13/56}\) one has \(D/(ER)\gg D^{1/56}\). The retained equality decay then pays the whole loss \(D^{1/16}\), since \((7/2)(1/56)=1/16\). The harmonic divisor sum gives \(D^{3/4+\epsilon}\) on this prefix. This does not give the same automatic decay for a partner-only wide correction, since its actual argument retains the factor \(Nk/(Nz_*Nx)\). The remaining comparable wide sector and the coherent masked divisor sum stay open.

