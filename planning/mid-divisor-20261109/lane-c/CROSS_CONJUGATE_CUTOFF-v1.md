# Transfer the cross-conjugate cutoff factor in the full-frequency unit-pair cross

9 November 2026 UTC. Author derivation pending independent review. Use the original pure full-frequency partner unit-pair correction and its separate middle equality compensation in UNIT_PAIR_FULL_FREQUENCY-v1. Retain the literal original unweighted nonprincipal two-pivot rows with \(A=A_1\asymp R\asymp D^{3/4}\), \(A_2\asymp1\), actual primitive \(Q_u\asymp R\), fixed \(S,\nu,u_0\), one common complex \(W\) supported on \([1,2]\), and \(U^2\le D\le7U^2/2\). Preserve all original ray, squarefree, capacity and raw-zero tests, and the re-expressed direct part. Let \(E=Nd\), \(d=mn\), \(L_i=U/Nm_i\), \(m_1=m,m_2=n\), and designate the longer and shorter scales by a deterministic tie convention. Write \(a=\zeta_l,b=\zeta_s\) for the corresponding original ordered cutoffs. At exponent level put \(e=\log_D E\), \(l_i=\log_D\max(1,L_i)\). The selection is on the actual cross-conjugate overlap
\[
 \ell=(a,\bar b),\qquad r=N\ell,\qquad \eta=\log_D J
 \quad\text{on a dyad }J\le r<2J .
\]
It can include both cutoff factors of rational content one. It is independent of the row and of the partner frequency. Fixed constants in all norm scales below are allowed.

The normalized selected cross, including its actual compensation, reaches \(O((DH)^\epsilon\mathcal M_{24}(W)^2D^{3/4})\) on the following mid-divisor selections:
\[
 \begin{array}{ll}
 1/6\le e\le1/4:&
 \eta\ \ge\ (1/4+e/2-l_s)_+/4
 \quad\text{in particular }\eta\ge3e/8-1/16\text{ suffices for all pairs},\\
 e\ge1/4:&
 \eta\ \ge\ (1/32-3(e-1/4)/4)_+ .
 \end{array}                                                        \tag{1}
\]
In particular \(\eta\ge1/32\) suffices for every \(e\ge1/6\). These statements may be summed over all their selected \(d,m,n\) and \(J\). The small-overlap part of the original middle-divisor gap and the unrestricted all-divisor comparison remain open.

## 1. Exact projectors and transfer of the rational factor

The original primal full-frequency unit reduction gives good squarefree coprime \(a,b\), both prime to \(d\), with \(L_l<Na\le U,\ L_s<Nb\le U\), and independent caps \(Na<7L_l,\ Nb<7L_s\) on nonzero \(W(ENaNb/D)\). Each prime in \(\ell\) is split and its conjugate is absent from \(\ell\): an inert prime is its own conjugate and would divide both \(a,b\); the ramified prime lies in \(S\); and a full split pair in \(\ell\) likewise contradicts original coprimality. Thus \(r\) is a squarefree rational integer and \(\lambda=\ell\bar\ell=(r)\). Both orientations are good, even for a non-conjugation-invariant \(S\), and \((\lambda,d)=1\) on the original support.

Write \(a=\ell x,\ b=\bar\ell y\). Exactly the required remaining conditions are that \(x,y\) are good squarefree and avoid \(d,\lambda\), with \((x,y)=(x,\bar y)=1\), together with the original norm cutoffs. Conversely these conditions recover the exact original overlap. In particular each prime of \(\ell\) contributes its two orientations only through the phase \(\psi_u(\lambda)\), including both raw zeros, and \(\mu(\ell)\mu(\bar\ell)=1\). For any fixed permissible \(r\) the orientation count is at most \(2^{\omega(r)}\). This count and every additional original orientation restriction are applied at the original labels; in the actual unit term these restrictions depend only on the fixed divisor pair, the norms, and eligibility of both orientations. Keep \(y\perp\lambda\) and expand the other three conditions by
\[
 \sum_{j\mid(x,y)}\mu(j)
 \sum_{k\mid(x,\bar y)}\mu(k)
 \sum_{v\mid(x,\lambda)}\mu(v).
\]
Use actual good squarefree \(j,k,v\) with all fixed \(d,S\) eligibility before stripping. The conjugate \(\bar k\) is also good because it divides \(y\). For each term set
\[
 B=[j,\bar k],\qquad A_0=[j,k],\qquad A=vA_0=[j,k,v],\qquad
 x=AX,\qquad y=BY .
\]
Here brackets denote ideal least common multiples. The identity \(A=vA_0\) holds on every live term: \(B\perp\lambda\) since \(y\perp\lambda\), \(\bar B\perp\lambda\) since \(\bar\lambda=\lambda\), \(j\mid B,k\mid\bar B\) and \(v\mid\lambda\). Drop fixed triples failing this necessary disjointness. Retain \(X\perp A,\ Y\perp B\), both squarefree, the original \(d\)-deletions, \(B,Y\perp\lambda\), and \(v\mid\lambda\). These conditions and original norm bounds are now exact for each summand; no new constraint is imposed between \(X,Y\) or between \(X,\lambda\) after stripping. The projectors cancel the invalid tuples in their expanded sums. Keep all three Möbius projector signs, the two residual signs \(\mu(AX)\mu(BY)\), \(\mu(d)\mathbf1_{(d,u)=1}\), and the fixed raw phase \(\psi_u(AB)\).

At fixed \(j,k,v\), put the variable \(\lambda\) into the shorter residual column as
\[
 Z=(r)Y .
\]
It is a good squarefree ideal because \(Y\perp\lambda\); its phase \(\psi_u(Z)\) is exactly the product \(\psi_u(\lambda)\psi_u(Y)\). Thus the two formed physical arrays have phases \(\psi_u(X)\), \(\psi_u(Z)\). There is no primitive normalization of the rational phase. The common profile is exactly \(W(E NA NB\,NX\,NZ/D)\), separated by its usual log Mellin inversion with bounded absolute Fourier mass. The shorter original norm cutoff is a coefficient condition on \((r,Y)\), because \(Nb=r NB NY\). The longer cutoff has the fixed-scale product \(Na=r NA NX\); its actual strict and weak endpoints, including the cap \(Na<7L_l\), are separated by exact integer log-step inversion in \(r\,NX\). For clarity, on polynomially clipped positive integer products one takes a smooth compact log step equal to the indicator at every integer, with transitions strictly between the adjacent integers at the endpoints. Widths can be chosen bounded below by an inverse polynomial in \(D\); the first derivative has bounded integral and the second derivative polynomial integral. The Fourier absolute mass is \(O(\log(2D))\) by splitting at one and that polynomial frequency. This gives an exact product of a norm twist in \(X\) and one in \(r\), the latter included in the sum forming each \(Z\)-coefficient. All their modulus-one factors are thus row independent. One can first clip the two original independent support ranges, which follows from \(J\le r<2J\) and the separate caps; the sharp tests are still retained by the step and the shorter coefficient.

## 2. Actual masses and the harmonic deletion charge

Define \(r_v\) as the product of distinct rational primes below \(v\). Skip any \(v\) not supported on the split primes eligible for \((r)\). Then \(v\mid(r)\) is exactly \(r_v\mid r\); if \(v\) contains both orientations over \(p\), the condition is \(p\mid r\) and \(Nv\) contributes \(p^2\). At fixed \(j,k,v\), the live \(r\)-count is \(O(J/r_v)\), with \(r_v<2J\) on nonempty support. The lengths and squared coefficient masses of the formed arrays, up to divisor subpowers, are
\[
 \begin{array}{c|c|c}
 &\text{physical length up to fixed constants}&\text{squared coefficient mass}\\
 X&L_l/(J NA)&O(L_l/(J NA))\\
 Z&J L_s/NB&O(L_s/(r_v NB)).
 \end{array}
\]
Indeed for each eligible \(r\) the \(Y\)-count is \(O(L_s/(J NB))\), with original caps giving empty arrays if the shortened length is less than \(1/7\). The \(X\)-count is analogous. The \(Z\) length counts \(N(r)=r^2\). At fixed \(Z\), each \(r\) is determined by a rational ideal divisor of \(Z\), and then \(Y\) is determined. This and the orientation count are divisor bounded. Squaring the grouped coefficients therefore costs only a subpower times the number of actual pairs \((r,Y)\), by Cauchy or the divisor bound at each \(Z\). Bounded nonempty subunit cases are counted directly, with their exact endpoints.

Relative to the unshortened product mass \(\sqrt{L_lL_s}\), their product of square-root masses gives
\[
 J^{-1/2}\bigl(NA_0\,NB\,Nv\,r_v\bigr)^{-1/2}.
\]
All fixed phase and raw mask factors are contractions after forming positive norms. The \(j,k\) sum has subpower cost: if a split rational prime occurs in \(j\) or \(k\), each of \([j,k]\) and \([j,\bar k]\) contains at least one orientation and the weight is at most \(p^{-1}\), with only boundedly many local states. For an inert rational prime the weight is at most \(p^{-2}\). The product of the underlying distinct primes has polynomial norm on the actual clip. The sum over supports is harmonic with \(C^{\omega(\cdot)}\) multiplicity and thus subpower. For \(v\), \(Nv\ge r_v\) and the number of choices is at most \(3^{\omega(r_v)}\), so \(1/\sqrt{Nv r_v}\) sums at subpower cost as well. These are positive enlargements after the exact signed projectors. They do not assume \(v\) disjoint from its own conjugate or identify equal-norm ideal labels.

## 3. Two normalized comparisons

With the exact equality pointwise envelope of UNIT_PAIR_SHARPENING-v1, apply the ordinary physical sixth-order second moment to \(X,Z\) at their true shortened lengths and take Cauchy in the actual rows at fixed second pivot. The row masks still act by contraction only in this positive comparison. Their sieve lengths may be enlarged monotonically to \(\max(1,L_l/J)\) and \(\max(1,J L_s)\), but their masses stay shortened. Including the equality amplitude and dividing by \(D\) gives \(R/E\) times the subpower, profile factors and
\[
 D^{-\eta/2+\{\Delta_6((l_l-\eta)_+)+\Delta_6(l_s+\eta)\}/2
                       -(e-1/4)_+/2},\qquad
 \Delta_6(x)=\max(0,x-3/4,x/3-1/8,5x/6-1/2).                  \tag{2}
\]
The compensation is separate. The new cutoff selector is row and frequency independent, so its allocation coefficient in the original middle projection is still divisor bounded by the number of actual ordered factorizations. Its elementary equality norm and its pairing with the original equality amplitude still cost \(R/E\) up to the common factors. This does not give it the \(J^{-1/2}\) gain. Both original signs and exact complex profiles stay in the identities before the norm comparisons.

The relative exponent in (2) is nonincreasing in \(\eta\), since \(\Delta_6\) is increasing and \(1\)-Lipschitz, while \((l_l-\eta)_+\) is nonincreasing. For \(\eta=1/32\) and \(e\ge1/6\), the two sieve arguments are at most \(1/2\), since \(l_s\le5/12\). Their sum of excesses is convex along the upper length segment \(l_s+l_l=5/6\), \(1/3\le l_s\le5/12\). Monotonicity allows enlargement to that segment from any shorter admissible lengths. At the extreme \((l_s,l_l)=(1/3,1/2)\) the sum of excesses is \(1/32\); at the balanced endpoint it is \(1/36\). This proves target for \(\eta\ge1/32\).

For \(1/6\le e\le1/4\), it remains to allow smaller \(\eta\). The two transferred length exponents are \(l_s+\eta,l_l-\eta\), both nonnegative and at most \(1/2\) when \(\eta\le1/32\). Their sum is \(1-e\) at exponent level. Apply the genuine joint positive norm of FORCED_RADICAL_JOINT-v1 to the equality side and whichever transferred column is shorter, with the other in the ordinary second moment. The joint product is \(h^2X\) or \(h^2Z\); the latter is still squarefree in \(Z\) and has forced radical \(h\) after forming the positive norm. This uses the actual pointwise norm identity after Cauchy with the conjugated partner, with the original conjugate unchanged in the signed expression. The coefficient-side log-step and norm-profile separations above do not depend on the equality labels, so the same radial and harmonic equality comparison applies. The extra mass factor \(J^{-1/2}\) survives. Equation (2) of FORCED_RADICAL_JOINT-v1 gives the relative power
\[
 -\eta/2+\tfrac16(1/4+e/2-\min(l_s+\eta,l_l-\eta))_+ .
\]
Put \(b=1/4+e/2\). If \(\eta\ge(b-l_s)_+/4\), then \(l_s+\eta\ge b-3\eta\). Also \(l_l-\eta\ge b-3\eta\) because \(l_l\ge3/8\ge b\). The exponent is nonpositive. Using \(l_s\ge1/2-e\) gives the stated sufficient \(3e/8-1/16\).

For \(e\ge1/4\) and \(\eta\le1/32\), enlarge the length pair to the segment \(l_s+l_l=3/4\) by monotonicity. It has extreme \((1/4,1/2)\) and balanced \((3/8,3/8)\). Convexity of the sum of excesses in (2) bounds it by the maximum of their two endpoint contributions. At the extreme the relative power is \(1/48-2\eta/3-(e-1/4)/2\). At the balanced endpoint it is at most \(-\eta/2+\eta/6-(e-1/4)/2\le0\). This proves the second branch of (1). When the exponent selections are combined over dyads and ordered divisors, the \(R/E\) budget sums harmonically. The exact original \(\mu(d)\) is retained before that final absolute comparison. No extension to selected partner dual frequencies, arbitrary additional coupled coefficient selectors, signed cancellation across divisors, or a whole-form determinant claim is made.
