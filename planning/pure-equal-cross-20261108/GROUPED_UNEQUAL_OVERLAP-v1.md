# Grouped deletion against the unequal dual denominator

8 November 2026 UTC. Use the original middle Poisson window of LOW_DUAL_CUTOFF-v1 and the exact conjugate reduction of CONJUGATE_DUAL_OVERLAP-v2. Keep the original unweighted nonprincipal two-pivot rows with fixed \(S,\nu,u_0\), primitive conductor \(Q_u\asymp R=A_1A_2\), full cutoff \(Z=U^2\), \(U^2\le D\le7U^2/2\), and one common smooth complex \(W\) supported on \([1,2]\). The notation \(E=Nd,E_1=Ne_1\) uses the intermediate Möbius divisor \(d\). Throughout, all previous exact dyadic and middle-window selectors can be kept. The positive comparisons concern the original counting norm.

## Exact grouped unequal kernel

For every fixed \(g,\ell,a',b'\) with \(z_0=g\ell a'\) and \(k=g\bar\ell b'\), let \(h=re_0\) as in GROUPED_EQUAL_CROSS-v4. The disjoint \(r,e_0\) are good and squarefree, and \(h\) is prime to \(z_0\). In particular no coprimality is imposed between \(h\) and \(k\). Keep \(Nz_0\ne Nk\) and the original reduced norm coprimality \(\gcd_{\mathbb Z}(Na',Nb')=1\). The allocation coefficient is
\[
 C(h;z_0,k)=\mu(h)\!\sum_{e_0\mid h}\!
                  \beta_{d,U,U^2}(e_0z_0)\,{\bf1}_{\rm original\ selectors}.
\]
It is divisor bounded and row independent. The tests use \(r=h/e_0\), the original \(J\)-dyad of \(e_0z_0\), and all original \(X',M\) and norm cutoffs. Thus the exact summand is the outer row factor \(\mu(e_1)\mathbf1_{(d,u)=1}\psi_u(e_1)\gamma_u Q_u^{-1/2}\) times
\[
 \frac{2D}{\sqrt3\,E E_1 Nz_0 (Nh)^2}
 C(h;z_0,k)\psi_u(h)^2\psi_u(z_0)\overline{\psi_u(k)}
 G_W\!\left(\frac{D}{E E_1 (Nh)^2 Q_u}\frac{Nb'}{Na'}\right).             \tag{1}
\]
Here the conjugate-overlap factor in \(\psi_u(z_0)\overline{\psi_u(k)}\) is still \(|\psi_u(g)|^2\psi_u(\ell)\overline{\psi_u(\bar\ell)}\). The primitive value at any \(S\)-factor of \(k\) is retained. Raw zero extension is multiplicative. The expression allows repeated prime factors of \(k\) and exact cancellations of powers only with their zero masks.

## Comparable near gaps

Let \(U_d(\Delta)\) be the projection of (1) onto \(1/2\le Nb'/Na'\le2\) and \(0<|Na'-Nb'|\le\Delta\), \(\Delta\ge1\). For fixed \(z_0\), its factorizations \(g\ell a'\) have divisor count. At each such factorization the allowed \(b'\) have at most \(O(1+\Delta)\) integer norms, each with at most divisor-many ideals. The bound on each norm fibre holds even when a norm is nonsquarefree as an integer. Thus the weighted outer count is \(O_\epsilon((DH)^\epsilon(1+\Delta))\), using the weight \(1/Nz_0\) and summing \(Nz_0\le Z\). The choices \(g,\ell,b'\) retain every raw character. At fixed \(z_0,k\) and fixed \(e_1\), the log Fourier separation for \(h\) in (1) has the same uniform mass as in the equality proof, because the ratio is in \([1/2,2]\). It follows that the squared norm divided by \(D\) is at most \((1+\Delta)^2\) times each of the cubic bounds in GROUPED_EQUAL_CROSS-v4. In particular at pure, writing
\[
 F(E)=\min(D^{5/8}E^{-1/2},D E^{-2}),
\]
it is \(O_\epsilon((DH)^\epsilon\mathcal M_{12}(W)^2(1+\Delta)^2 F(E))\). The equal projection itself is bounded by the same \(F(E)\) without the gap factor.

Take the actual \(d\)-dependent projection
\[
 \Delta_d=
 \begin{cases}
 D^{1/8}E^{-1/2},&E\le D^{1/4},\\
 E D^{-1/4},&E>D^{1/4}.
 \end{cases}
\]
Both endpoints are inclusive and one uses integer gap values within the real cutoff. The two formulas agree at the boundary. By the exact cross identity and absolute Cauchy, the signed cross of \(U_d(\Delta_d)\) with \(E_d\) is bounded at pure by \(D^{3/4+\epsilon}\) after the harmonic divisor sum, since \((1+\Delta_d)F(E)\ll D^{3/4}/E\). At \(d=1\) the gap is \(D^{1/8}\). This result allows long comparable reduced factors. It also holds for a prescribed row-independent set of \(O(1+\Delta_d)\) reduced integer denominator norms at fixed numerator, provided the same compact comparable ratio condition holds.

For the further projection \(Nh\ge D^{7/36}\) of the off-equal side, the small-profile argument of PURE_EQUAL_JOINT-v1 gives energy \(O_\epsilon((DH)^\epsilon\mathcal M_{12}(W)^2 D^{5/12}(1+\Delta)^2/E^2)\). Pairing with the whole equality bound \(D^{5/8}E^{-1/2}\) yields \(D^{25/48}(1+\Delta)\sum E^{-5/4}\). Thus this selected near cross reaches target for \(\Delta=D^{11/48}\) over all \(d\). This estimate is for the equality/near cross.

## Overlap with \(h^2\) on the denominator side

Set \(b_*=(b',h^2)\), the ideal gcd, and write uniquely
\[
 b_*=c_1c_2^2,\qquad b'=c_1c_2^2 b_0,\qquad h=c_1c_2 s
\]
where \(c_1,c_2,s\) are good squarefree and pairwise coprime. The residual \(b_0\) can meet \(S\) and can share a prime with \(c_2\) when its original \(b'\)-valuation is greater than two. It is prime to \(c_1,s\). All these statements follow from clipping each valuation of \(b'\) at \(2v_{\mathfrak p}(h)\). No squarefreeness of \(b_0\) is needed. The exact powered factor becomes
\[
 \psi_u(h)^2\overline{\psi_u(b')}
   =\psi_u(c_1)\psi_u(s)^2|\psi_u(c_2)|^4\,\overline{\psi_u(b_0)}.          \tag{2}
\]
The fourth absolute power is the zero mask on \(c_2\). Dropping it would replace a nonunit dual value by a nonzero one. When \(b_0\) meets \(S\), it carries the exact primitive value. The numerator coprimality is still the original \(\gcd_{\mathbb Z}(Na',Nb')=1\), including conjugate collisions. Because \(h\) is prime to \(z_0\), there is no analogous nonunit cancellation between \(h\) and \(a'\).

The profile argument after (2) is
\[
 \frac{D Nb_0}{E E_1 Q_u Na' Nc_1 (Ns)^2}.
\]
Fix \(g,\ell,c_1,c_2,s,b_0,e_1\) and use the dyad \(Na'\asymp P\), \(Ns\asymp T\), both at least one up to fixed constants. All row-independent selectors, including the exact \(b_*\)-allocation, remain in the divisor-bounded coefficient on \(a'\). Separate the profile by the compact log Fourier comparison with mass \(O(\mathcal M_{12}(W)(1+y)^{-4})\), \(y=D Nb_0/(E E_1 R P Nc_1 T^2)\). Freeze \(v_2\) and apply the pinned sixth-order \(\Phi(A_1,P)\) row comparison as in the one-column bound of CONJUGATE_DUAL_OVERLAP-v2. Its norm factor is \(O_\epsilon((DH)^\epsilon\sqrt{A_2P\Phi(A_1,P)})\). The primitive row multipliers and raw zeros in (2) are retained as contractions inside this norm. Summing over the \(O(T)\) choices of \(s\) in the dyad, the normalized row norm is bounded by
\[
 \ll (DH)^\epsilon\mathcal M_{12}(W)
 \frac{\sqrt{A_2/(E E_1)}}
      {Ng\,N\ell\, (Nc_1)^{3/2}(Nc_2)^2\sqrt{Nb_0}}\,
       \sqrt{\Phi(A_1,P)}\sqrt y(1+y)^{-4}.                              \tag{3}
\]
In fact the scalar from (1) is \(D/(E E_1 Ng N\ell\, P (Nc_1Nc_2 T)^2\sqrt R)\). The \(T\)-count and the \(\sqrt P\) from the column norm give exactly the scalar in (3) after division by \(\sqrt D\). There are logarithmically many \(P,T\) dyads by the original support.

Since \(T,Nc_1,E_1\ge1\), \(y\ll D Nb_0/(E R P)\). The degree-at-most-one bound for \(\Phi\) in its length gives a uniform estimate for \(\Phi(A_1,P)y(1+y)^{-8}\) by \(O(\Phi(A_1,\max(1,D Nb_0/(E R))))\). The \(g,\ell\) sums are harmonic. The sums over \(c_1,c_2\) converge, and \(\sum_{Nb_0\le B_0}(Nb_0)^{-1/2}\ll B_0^{1/2}\). The \(e_1\)-sum costs a divisor factor. For the actual off-equal projection \(T_d(B_0)\) with \(Nb_0\le B_0\), this proves
\[
 D^{-1}\|T_d(B_0)\|_2^2
 \ll (DH)^\epsilon\mathcal M_{12}(W)^2
       \frac{A_2 B_0}{E}\Phi(A_1,\max(1,D B_0/(E R))).                    \tag{4}
\]
The estimate is a norm of the original selected summands, with its signs and physical cutoffs intact.

At pure take \(B_0=\max(1,D^{1/8}E^{-1/2})\). The second argument in (4) is \(O(D^{3/8})\), so \(\Phi(A_1,\max(1,D B_0/(E R)))\ll D^{3/4}\). For \(E\le D^{1/4}\) pair energy \(D^{7/8}E^{-3/2}\) with equality energy \(D^{5/8}E^{-1/2}\). This gives \(D^{3/4}/E\) for the exact cross before summing. For \(E>D^{1/4}\) pair \(D^{3/4}/E\) with \(D/E^2\), giving a tail \(D^{7/8}\sum_{E>D^{1/4}}E^{-3/2}\ll D^{3/4}\). Thus this equality/off-equal cross has target power across all \(d\), including \(d=1\) and nonunit residuals \(Nb_0\le D^{1/8}\) there.

## Two projections with target cross against the full complement

For the projection in (4) with the additional condition \(Na'\ge P_0\ge1\), use \(y(1+y)^{-8}\le y\) in (3). Because \(\Phi(A_1,P)/P\) is nonincreasing, the resulting bound for the normalized energy is
\[
 \ll (DH)^\epsilon\mathcal M_{12}(W)^2
       \frac{A_2D}{R E^2}\,B_0^2\,\frac{\Phi(A_1,P_0)}{P_0}.             \tag{5}
\]
The extra \(\sqrt{Nb_0}\) cancels its inverse weight in the unsquared estimate. At pure, \(B_0=1,\ P_0=D^{11/16}\) gives \(D^{5/12}/E^2\). So does \(B_0=D^{1/48},\ P_0=D^{3/4}\). These are long numerator sectors, with the original allocations still in place.

Alternatively require \(Nb'\ge Y\ge B_0\) in (4). Since \(Nc_1(Nc_2)^2\ge Y/B_0\), the positive sum of \((Nc_1)^{-3/2}(Nc_2)^{-2}\) in (3) is \(O_\epsilon((Y/B_0)^{-1/2+\epsilon})\) over this range. This follows by multiplying the summand by \((Nc_1(Nc_2)^2)^{1/2-\epsilon}\) and summing the resulting convergent ideal powers. Thus (4) improves by a factor \(B_0/Y\) up to subpowers. At pure, \(B_0\le D^{1/8}\) and \(Y\ge D^{1/3}B_0^2\) give \(D^{5/12}/E\). For example the unit residual case \(Y=D^{1/3}\) admits powered denominators. The support may be empty on some dyads. No assertion equates the squarefree and powered denominator capacities.

Write \(P_d^*\) for either one of these exact off-equal projections. Its cross with the full complement is \(2D^{-1}\operatorname{Re}\sum_d\mu(d)\langle P_d^*,V_d-P_d^*\rangle\). The energy \(D^{5/12}/E\) dominates either selected bound and is itself absorbed into the first physical term in the positive estimate for \(V_d-P_d^*\). Pairing it termwise with the four terms of (1) in PURE_EQUAL_JOINT-v1 yields, before subpowers, powers \(7/12,17/24,11/16,3/4\), with harmonic or convergent ideal sums. Thus both crosses reach \(D^{3/4+\epsilon}\), including \(d=1\). These bounds concern actual unequal summands and their full complements. The projection squared also meets target by its positive bound. They leave the interactions in the unselected complement, including generic large \(b_0\), unestimated at target. The determinant, zero locations and full signed arithmetic assembly remain open.

