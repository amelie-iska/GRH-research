# Local divisor sign recombination and a thin cutoff-product sector

8 November 2026 UTC. Work in the original normalized equality-versus-complement cross of TWO_FAMILY_CROSS-v1 and COUPLED_POWERFUL_CROSS-v2. Keep the full ordered cutoff \(Z=U^2\), \(U^2\le D\le7U^2/2\), fixed \(S,\nu,u_0\), literal unweighted nonprincipal rows, primitive \(Q_u\asymp R\), one common smooth \(W\), and the original raw zeros, allocations and frequency windows. The target estimate below concerns the exact pure scales \(A_1\asymp R\asymp D^{3/4}\), \(A_2\asymp1\), and physical defect dyads \(B,K\asymp R\). The elementary identity itself has no restriction on those dyads.

## 1. Recombine the actual ordered cutoff signs

Let \(d\) be a good squarefree ideal, \(E=Nd\), and fix one ordered factorization \(\zeta=\zeta_1\zeta_2\) of an actual good squarefree cutoff ideal with \((d,\zeta)=1\). On either side of the pairing, \(\zeta=e_0 z_0\) uses that side's actual fixed \(e_0\) allocation. Omit any factorization with \(N\zeta_i>U\). Put \(T_i=U/N\zeta_i\ge1\). The remaining two cutoff assignments contribute \(\mu(\zeta)F_d(T_1,T_2)\), where
\[
 F_d(T_1,T_2)=\sum_{\substack{a,b\mid d,\ (a,b)=1\\Na\le T_1,\ Nb\le T_2}}\mu(a)\mu(b).
\]
The original product cap \(N(a\zeta_1)N(b\zeta_2)\le U^2\) follows from the two individual cutoffs. This identity is per ordered factorization, before summing the original \(\zeta_i\) allocations. No phase depends on the assignments \(a,b\).

First sum \(b\) over all divisors of \(d/a\), then subtract the \(Nb>T_2\) terms. The full sum leaves only \(a=d\) since \(\sum_{b\mid d/a}\mu(b)=\mathbf1_{a=d}\). In the subtracted sum put \(m=d/b\), so \(a\mid m\) and \(\mu(a)\mu(b)=\mu(d)\mu(m/a)\). Therefore
\[
 F_d(T_1,T_2)=\mu(d)\left[
 \mathbf1_{E\le T_1}+\mathbf1_{E\le T_2}-1
 -\sum_{\substack{m\mid d\\ T_1<Nm<E/T_2}}
       \ \sum_{\substack{a\mid m\\Na\le T_1}}\mu(m/a)\right].       \tag{1}
\]
Here \(Nb>T_2\) is exactly \(Nm<E/T_2\), with a strict upper endpoint. All nonunit \(m\) with \(Nm\le T_1\) have zero inner sum. The unit contributes exactly when \(E>T_2\). The formula includes \(d=1\), for which \(F_1=1\), and is symmetric under interchanging the two cutoff factors even though this expression uses one orientation.

If \(E N\zeta\le U^2\), equivalently \(E\le T_1T_2\), the band in (1) is empty. In that case \(F_d=\mu(d)\) if both capacities are at least \(E\), \(F_d=0\) if just one is, and \(F_d=-\mu(d)\) if both are below \(E\). If the equality cutoff satisfies \(E N\zeta\le U\), every ordered factorization of that cutoff has both capacities at least \(E\), and the full equality coefficient is \(\beta_d(\zeta)=\mu(d)\beta_1(\zeta)\). For a general equality cutoff, use (1) on its individual factorizations. If \(E>U/\sqrt{N\zeta}\), both capacities cannot reach \(E\). Thus above this scale every nonzero factorization uses two partial capacities. In the pure comparable partner block this applies, up to fixed scale constants, beyond the existing \(D^{9/68}\) prefix because \(N\zeta\ge Nx\asymp D^{3/4}\) and \(1/8<9/68\).

The correction in (1) is supported on the actual band \(T_1<Nm<E/T_2\). For either live Poisson allocation the primal-zero test gives \(D/(E E_1(Nh)^2)>Nz_0/4\), with \(e_0\mid h\). In particular
\[
 \frac{E N(e_0z_0)}{U^2}<\frac{4D}{U^2}\frac{Ne_0}{E_1(Nh)^2}
 \le\frac{14}{E_1Nh}.
\]
Consequently the correction vanishes whenever \(E_1Nh\ge14\) on that side. For smaller \(E_1Nh\) the band need not have a power-small relative width. The test above preserves the original primal-zero removal and does not alter the exact Poisson phase.

## 2. A passive divisor scalar with an actual remaining Möbius sign

Fix the row and all other labels, both ordered factorizations, and the original allocation dyads. Select the terms in which both \(e_{1,i}\) are fixed \(S\)-supported ideals, the good new residue ideal \(\widetilde q_d\) is the unit, and \(d\) avoids the full fixed prime union of the row and the primal and dual labels. Retain the original raw factors and deletion conditions. In particular there is no good overlap \(j\) on this selection and no changed residue on \(d\). Suppose also \(E N\zeta_i\le U^2\) for the two whole cutoff ideals \(\zeta_i\), where \(i\) here indexes the sides. Then the product of the two \(F_d\) factors and the outer \(\mu(d)\) is exactly \(\mu(d)\) times the product of their two capacity step functions, since \(d\) is squarefree. This holds also when the equality cutoff is not fully saturated. The constant signs \(\mu(\zeta_i)\) remain. All row phases are fixed in this selected scalar, with zeros in the same places.

For \(E\in[Y,2Y]\), the capacity steps and the original primal, direct and middle tests give a union of a bounded number of norm intervals with their exact endpoints. Indeed \(X'\) is proportional to \(1/E\), the original \(M\) is proportional to \(E\), and the physical integer relation for middle equality is fixed after fixing the two ideal labels. Equal norms in the re-expressed direct component remain. Both radial arguments are positive fixed constants times \(1/E\), and the two Poisson scalar factors together give \(E^{-2}\) times a fixed scalar. Let \(\mathcal T\) be the full fixed forbidden prime union, of polynomial norm on the original clipped support. The accepted fixed-field deleted Möbius estimate in DELETED_PRIME_MERTENS_AND_UNIT_CORRECTION-v1, equation (7), and exact partial summation now bound the \(d\)-scalar, after factoring off the fixed scalar and phase, by
\[
 O\!\left(\mathcal M_{24}(W)^2 Y^{-1}
        \log^C(2D)\exp(-c\sqrt{\log(2Y)})\right)
\]
for \(Y\ge D^\kappa\) with fixed \(\kappa>0\). The profile weight \(E^{-2}G_W(c_0/E)\overline{G_W(c_1/E)}\) has supremum plus integrated absolute derivative \(O(\mathcal M_{24}(W)^2Y^{-2})\) on each interval. This gives the displayed scalar estimate with the original norm endpoints. Its decay is subpower. The result fixes the column labels and does not transfer that decay to the coherent row and column comparison.

## 3. Target-size cross in a thin physical cutoff-product interval

Consider the same pure comparable block, now allowing the full original erasure and positive increment families and arbitrary changed \(d\)-residues. At fixed \(d\) and fixed partner allocation labels, select any row-independent interval in \(Nx\) of width \(O(BD^{-1/8})\) on \(B\le Nx<2B\). In particular one may take the true cutoff-product boundary interval
\[
 1< E N(e_{0,1}z_*x)/U^2\le1+D^{-1/8},
\]
with the partner's actual \(e_{0,1}\). Once \(E,e_{0,1},z_*\) are fixed, this is an interval of the asserted width whenever it meets the dyad. The selector is on the erased array only, independent of the inserted ideal. The same conclusion permits any convention at either endpoint.

Use the original sharp insertion comparison of SHARP_INSERTION_POISSON-v1 and POWERFUL_FREEZE-v1, keeping the common divisor \(s_1\) eligible before stripping and fixing the powerful part \(P\). With \(x=s_1x'\) the shortened erased coefficient is divisor bounded times \(1/B\). Its norm interval has width \(O(BD^{-1/8}/Ns_1)\). The number of such ideal labels, including all distinct ideals of equal norm, is \(O((DH)^\epsilon(1+BD^{-1/8}/Ns_1))\) by counting integer norms and their divisor-bounded ideal fibres. Thus for \(Ns_1\le D^{3/8}\), the squared erased coefficient mass is at most the usual \(O((DH)^\epsilon/(B Ns_1))\) times
\[
 O(D^{-1/8}+Ns_1/B)=O(D^{-1/8}).
\]
The square-root gain \(D^{-1/16}\) pays the entire pure erased sieve loss, since \(\Phi(A_1,B/Ns_1)/A_1\ll D^{1/8}\). For \(Ns_1>D^{3/8}\), use the full ordinary erased mass without thinness. The shortened length is \(O(D^{3/8})\), so \(\Phi(A_1,B/Ns_1)\ll A_1\). The unit is counted on a nonempty subunit dyad.

The sharp insertion moment acts on the unchanged eligible shortened interval of length \(O(K/(NP\,Ns_1))\) and uses the exact raw factors. At fixed \(P\) the erased mask on \(P\) is retained. The product of row norms in either case is bounded by
\[
 O\!\left((DH)^\epsilon
       A_1\sqrt{K/B}\,(Ns_1)^{-1}(NP)^{-1/2}\right)
\]
per fixed second pivot, apart from the separated radial factors. The \(O(\sqrt M)\) count for \(NP\asymp M\) pays the powerful shortening. The \(s_1\)-sum is harmonic. The weighted log separation and partial summation in the insertion norm are unchanged because the new interval is on \(x'\) alone. The original two half radial powers and fixed-label weights then give \(O((DH)^\epsilon\mathcal M_{24}(W)^2R/E)\) at each \(d\). Count the exact middle subtraction separately within the selector using at most one integer norm in either direction, with the physical \(1/Nx\). It has the same bound. The harmonic divisor sum reaches \(D^{3/4+\epsilon}\) for this selected pure cross.

The thin interval estimate is an absolute comparison on a new part of the original cross. Equation (1) additionally identifies where the remaining divisor sign can be recombined before absolute values. Neither result bounds the wide above-cap correction or the coherent masked divisor sum in the remaining pure core, and neither changes the whole signed estimate.

