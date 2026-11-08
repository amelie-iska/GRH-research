# Rational ideal content in the comparable dual cross

8 November 2026 UTC. Author draft for independent review.

## Actual terms and a sparse count

Use the original unweighted nonprincipal two-pivot Eisenstein rows, the exact conjugate reduction, and the middle-window selectors of EQUAL_NEAR_DUAL_CROSS-v2. Keep the fixed \(S,\nu,u_0\), common smooth complex \(W\) supported on \([1,2]\), primitive conductor norm \(Q_u\asymp R=A_1A_2\), exact Gauss phase and all raw zeros. Keep the original allocation \(\beta_{d,U,Z}\), literal ray and capacity conditions, \(Z\le U^2\), and \(U^2\le D\le 7U^2/2\). The full ordered cutoff coefficient has \(Z=U^2\). Use the original intermediate divisor \(d\) in the signed form.

As before write \(z_0=g\ell a'\), \(k=g\bar\ell b'\), with \(g\) the original ideal gcd and \(\ell=(a,\bar b)\) in the first residual pair. The reduced pair has \(\gcd_{\mathbb Z}(Na',Nb')=1\), and the row factor on \(g,\ell\) is \(|\psi_u(g)|^2\psi_u(\ell)\overline{\psi_u(\bar\ell)}\). Work on \(Nb'/2\le Na'\le2Nb'\) and exclude \(Na'=Nb'\) from the cross partner. With the previous dyads let \(P=J'/(CB)\), \(T=K/(CB)\), \(y=K/M\), and \(F=\sqrt{X A_2}/(E_0\sqrt{E_1})\). Comparability gives \(P\asymp T\), and \(P,T\ll yR\) since \(M<2R\). The profile argument is \(\lambda Nb'/Na'\), \(\lambda=X/(E E_0 Q_u)\asymp y\). The following bounds apply to the full profile or its frozen leading term \(G_W(\lambda)\) in that comparable range. The full profile uses the previous Fourier separation. In the frozen term the same decay \(O(\mathcal M_{12}(W)(1+y)^{-4})\) is a row multiplier. The physical prefactor \(1/Nz\) is retained in both.

For an integral ideal \(I\), define \(c(I)\) to be the largest positive rational integer prime to the rational primes below \(S\) such that \((c(I))\mid I\). It is defined by prime valuations. At a good split rational prime it uses the smaller of the two ideal valuations, and at a good inert prime it uses the ideal valuation. At rational primes below \(S\) it has valuation zero. In particular a good squarefree ideal can have a nontrivial \(c(I)\) even though its ideal sixth-power factor is a unit. If \(c(I)=m\), write \(I=(m)I_1\), with \(NI=m^2 NI_1\). The condition \(c(I_1)=1\) is exact, and the original ideal squarefreeness is a separate selector.

At norm \(NI\asymp L\), \(L\gg1\), the count with \(c(I)\ge M_0\ge1\) is
\[
 \ll \sum_{m\ge M_0}\#\{I_1:NI_1\ll L/m^2\}\ll L/M_0.               \tag{1}
\]
The summation can be restricted to \(m\ll\sqrt L\); a subunit cap with no ideals contributes zero. This proof counts ideals and preserves both labels over a split prime. It uses no assumption on \(\psi_u((m))\) beyond its exact unitary value or zero.

## A single large rational factor in the near strip

Take \(0<|Na'-Nb'|\le\Delta\) and \(c(b')\ge M_0\). For fixed \(g,\ell,b'\) the thin \(a'\)-support in the previous proof has coefficient squared mass \(\ll (DH)^\epsilon\min(P,1+\Delta)\), with exact masks. Equation (1) cuts the number of \(b'\)-choices to \(O(T/M_0)\). Therefore the same one-column estimate gives the squared row bound
\[
 (DH)^\epsilon\mathcal M_{12}(W)^2 F^2\,
    M_0^{-2}\frac{T}{P}\min(P,1+\Delta)
       \Phi(A_1,\max(1,P))\,y(1+y)^{-8}
\]
up to a fixed constant. If instead \(c(a')\ge M_0\), fix \(a'\) and apply the same thin-interval bound to \(b'\). The bounded \(\beta_{d,U,Z}\) is then part of the fixed coefficient. The column estimate for arbitrary ideals on \(b'\) keeps its exact \(S\)-supported value. The same proof applies after exchanging \(P,T\). In each case both coprimalities and the inherited masks are column selectors for the variable being averaged.

On the comparable support \(P\asymp T\ll yR\). The degree at most one of \(\Phi(A_1,\cdot)\) and bounded \(y\max(1,y)(1+y)^{-8}\) yield normalized energy
\[
 \frac{\|V_d^{\mathrm{one}}\|_2^2}{D}
 \ll_{\epsilon,\eta}
 \frac{(DH)^\epsilon\mathcal M_{12}(W)^2 A_2}{Nd}\,
       \frac{1+\Delta}{M_0^2}\Phi(A_1,R).                            \tag{2}
\]
The union of the two pieces is disjoint by taking the denominator condition first. The remaining exclusions are kept exactly. The row norm triangle costs a fixed factor.

## Two large rational factors in the full comparable range

Take \(c(a')=m\ge M_0,\ c(b')=n\ge N_0\) and write \(a'=(m)a_1,\ b'=(n)b_1\). Put \(m\in[M,2M)\), \(n\in[N,2N)\) in integer dyads. For fixed \(g,\ell,m,n\), the exact phase retains
\(\psi_u((m))\overline{\psi_u((n))}\) with its zeros. The cutoff weight and radial profile retain \(m^2 Na_1,n^2 Nb_1\), including the original \(Nz\) in the prefactor. The condition \(\gcd_{\mathbb Z}(Na',Nb')=1\) forces \((m,n)=1\). Then it is equivalent to the two individual selectors against \((n)\) and \((m)\), respectively, and \((a_1,b_1)=(a_1,\bar b_1)=1\). Neither \((m)\) nor \((n)\) is assumed coprime to its own residual unless this follows from an original squarefree requirement.

The inherited cutoffs involving \(Na',Nb'\) are split into finitely many cells as before, with their exact endpoints. Comparability, any gap selection, and exclusion of equality are finite Fourier masks in the integer linear forms in \(m^2 Na_1,n^2 Nb_1\). A polynomial-size modulus larger than twice the full ranges of these forms makes the indicators exact and costs polylogarithmic Fourier mass. Each Fourier phase separates into a factor on \(a_1\) and a factor on \(b_1\). The radial profile also separates with the previous mass and retains the primitive row factor.

Apply the exact two-lcm projector of CONJUGATE_DUAL_OVERLAP-v2. At fixed \(q,h\) its two lengths are \(O(P/(M^2 N[q,h]))\) and \(O(T/(N^2 N[q,\bar h]))\), with the bracket denoting ideal lcm and the leading \(N[\cdot]\) the ideal norm. Keep \(\psi_u([q,h])\overline{\psi_u([q,\bar h])}\) with both zeros. The product of fourth moments and Hölder gives the weight \((N[q,h]N[q,\bar h])^{-1/2}\), whose sum is polylogarithmic. A live subunit length is bounded by the unit count at constant scale. The \(O(MN)\) choices of \(m,n\) cancel the length factor \(1/(MN)\) in the row norm. The \(O(CB)\) choices of \(g,\ell\) then restore \(\sqrt{J'K}\) as in the previous joint estimate. The resulting squared energy at fixed dyads is bounded by the original factor \((DH)^\epsilon\mathcal M_{12}(W)^2 F^2 y(1+y)^{-8}\) times
\[
 [\,\Phi(A_1,\max(1,(P/M^2)^2))\,\Phi(A_1,\max(1,(T/N^2)^2))\,]^{1/2}.
\]
Use \(P,T\ll yR\), \(M\gg M_0,\ N\gg N_0\). By the degree bound the growth from \(y>1\) is at most \(\max(1,y)^2\) after taking the square root, absorbed by the profile. After the harmonic and dyadic sums this gives
\[
 \frac{\|V_d^{\mathrm{two}}\|_2^2}{D}\ll_{\epsilon,\eta}
 \frac{(DH)^\epsilon\mathcal M_{12}(W)^2 A_2}{Nd}
 \left[
 \Phi(A_1,\max(1,R^2/M_0^4))
 \Phi(A_1,\max(1,R^2/N_0^4))
 \right]^{1/2}.                                                     \tag{3}
\]
This includes far gaps on the comparable range. Both (2) and (3) sum harmonically in \(d\). The sectors can be kept disjoint from the earlier ones through the exact original masks and fixed number of cells.

## A separate gain from the original deletion length

For comparison, keep \(L=X'/E_1\) in the comparable frozen leading term. Then \(y\asymp L/R\) and \(J'<2L\) from \(M<2R\). Thus \(P,T\ll L\). For the subset \(L\le L_*\le R\), \(L_*\ge1\), the factor \(E_1^{-1}\) in \(F^2\) is at most \(\min(1,L_*/B_*)\) by \(X'>B_*\). Equation (1) of EQUAL_NEAR_DUAL_CROSS-v2 therefore gives, after the same sums, the following normalized energy factor after \((DH)^\epsilon\mathcal M_{12}(W)^2 A_2/Nd\):
\[
 (1+\Delta)\frac{L_*}{R}\min(1,L_*/B_*)\,\Phi(A_1,L_*).              \tag{4}
\]
The subunit case is included by monotonicity at \(L_*\ge1\). This applies to all comparable near terms selected by the indicated length. It uses the existing positive bound with the deletion length and prefactor retained. For \(L_*<B_*\) a live term requires \(E_1>B_*/L_*\). In particular this part of the improvement is empty at \(d=1\) for growing \(B_*/L_*\) and fixed \(S\).

## Powers and the signed cross

For a projection \(V_d^*\) above use the exact signed cross with the equal-norm projection, \(2D^{-1}\operatorname{Re}\sum_d\mu(d)\langle V_d^{\mathrm{eq}},V_d^*\rangle\), with any further divisor interval restriction. Absolute Cauchy gives the average of the two positive energy exponents. At mixed \(A_1\asymp D^{5/12}, A_2\asymp D^{1/6}\), the equal-norm exponent is \(7/12\).

* With \(\Delta=D^{73/216}\), equation (2) at \(M_0=D^{23/216}\) gives energy power \(11/12\) and cross power \(3/4\). The slack choice \(M_0=D^{11/100}\) gives cross power \(4031/5400\) and persists in the feasible \(1/2000\) mixed neighborhood. This selection applies at \(d=1\).
* In the entire comparable middle range, (3) at \(M_0=N_0=D^{13/120}\) also gives \(11/12\) and cross \(3/4\), including far gaps and \(d=1\). At \(M_0=N_0=D^{11/100}\) the cross power is \(269/360\) with the feasible mixed neighborhood. The trial threshold \(M_0=N_0=D^{1/10}\) gives cross \(55/72\) by this budget, above target.
* With the earlier mixed \(B_*=D^{21/40}\), (4) at \(L_*=D^{29/60}\) and \(\Delta=D^{73/216}\) gives cross power \(1607/2160\). It uses the stated deletion restriction and has \(E_1\gg D^{1/24}\).
* At pure \(A_1\asymp D^{3/4}, A_2\asymp1\), equation (3) with both thresholds \(D^{9/32}\) gives energy \(3/4\), hence cross \(3/4\) over the comparable middle range. The equal-norm positive power here is \(3/4\).

These comparisons leave the actual small-divisor cross with long comparable terms of small rational content and the remaining noncomparable far terms. They use positive norm estimates after preserving the signed identity. Independent review is pending. The whole signed bound, determinant, zero-location and analytic Lean obligations remain open.
