# Pure equal-norm cross: joint conductor and grouped profile estimates

8 November 2026 UTC. Use the original unweighted nonprincipal two-pivot rows, fixed \(S,\nu,u_0\), actual \(Q_u\asymp R=A_1 A_2\), full cutoff \(Z=U^2\), \(U^2\le D\le 7U^2/2\), and the single common smooth complex \(W\) of GROUPED_EQUAL_CROSS-v4. Preserve the original capacity, literal primary section, raw zeros, ray, squarefree and common-prime masks. Write \(E=Nd\), \(E_1=Ne_1\). Here \(d\) is the intermediate Möbius divisor. In the pure comparisons \(H\asymp A_1\asymp R\asymp D^{3/4}\) and \(A_2\asymp1\).

Let \(E_d\) be the entire exact equal-norm projection in the specified middle Poisson window and \(V_d\) the full original amplitude. The cross of a selected subprojection \(E_d^*\) with the original complement is \(2D^{-1}\operatorname{Re}\sum_d\mu(d)\langle E_d^*,V_d-E_d\rangle\). Use the signed identity before absolute Cauchy. Suppress \((DH)^\epsilon\) and the original \(O(\mathcal M_{12}(W)^2)\) cost in energy and cross bounds. The physical positive bound for \(D^{-1}\|V_d-E_d\|_2^2\) is
\[
 \ll \frac{D^{3/4}}E+\frac D{E^2}
             +\frac{D^{23/24}}{E^{4/3}}+\frac{D^{13/12}}{E^{11/6}}.        \tag{1}
\]
Indeed \(V_d\) has the per-divisor comparison of phy:divisor-proof, with the subunit endpoint counted directly. The elementary bound \(R/E\) for \(E_d\) in GROUPED_EQUAL_CROSS-v4 is absorbed into the first term. The group bounds for any row-independent equality selector are
\[
 \ll \min\{D^{5/8}E^{-1/2},D E^{-2},R/E\}.                              \tag{2}
\]
These statements concern actual subprojections of the one fixed exact representation.

## Two profile ranges on the equality side

For fixed \(e_1\) and \(T\le Nh<2T\), the cubic average over \(h=re_0\) gives, in the notation of the grouped proof,
\[
 \frac{A_2}{E E_1}\frac{\Phi_3(A_1,T)}{T}y(1+y)^{-8},
 \qquad T_0=\sqrt{\frac{D}{E E_1R}},\quad y=(T_0/T)^2 .
\]
This bound comes after the harmonic \(g,\ell\) count. In the projection \(Nh\le T_0 D^{-5/312}\), a live dyad has \(T/T_0\le D^{-5/312}\). For \(s=0,1/3,1\), the profile bound \(T^{-s}y(1+y)^{-8}\le T_0^{-s}(T/T_0)^{14-s}\) gains \(D^{-5/24}\) against the earlier scale-free comparison. The \(e_1,T\) sums therefore give energy at most \(D^{5/12}E^{-1/2}\). This includes the pure \(d=1\) threshold \(Nh\le T_0 D^{-5/312}\) of scale \(D^{17/156}\), with its exact \(E_1\) factor.

For \(Nh\ge D^{7/36}\), use \(y(1+y)^{-8}\le y\). At pure the resulting bound on a live dyad is
\[
 \ll \frac{D}{E^2}\left[T^{-3}+A_1^{-1}T^{-2}
                              +A_1^{-1/3}T^{-7/3}\right]
 \ll D^{5/12}E^{-2}.
\]
Here the \(E_1\)-factors only decrease the budget and the clipped dyad threshold costs a fixed constant. This holds even when the natural scale \(T_0\) is subunit.

For either projection the cross with \(V_d-E_d\) has target \(D^{3/4+\epsilon}\) over all \(d\). On \(E\le D^{11/32}\) use energy \(D^{5/12}E^{-1/2}\) and pair it termwise with (1). The first and third terms yield \(D^{7/12}(D^{11/32})^{1/4}\) and \(D^{11/16}(D^{11/32})^{1/12}\) after the ideal sum. The second and fourth are summable with powers \(17/24\) and \(3/4\). On \(E>D^{11/32}\) use the inherited \(D/E^2\) bound for the selected equality and the same pure tail comparison as in GROUPED_EQUAL_CROSS-v4. These are separate upper bounds for the exact profile projections. No decay gain is obtained near \(Nh\asymp T_0\).

## Joint positive norm for \(h\) and a conjugate divisor

On \(z_0=g\ell,\ k=g\bar\ell\), choose a divisor \(t\mid\ell\) with \(t,\bar t\) prime to \(S\) and \(B\le Nt<2B\). If several choices qualify, select one by a fixed ordering of ideal labels, possibly using a row-independent condition involving \(h\). Fix \(g,w=\ell/t\) and \(e_1\), retaining \(|\psi_u(g)|^2\psi_u(w)\overline{\psi_u(\bar w)}\) and all outer row factors. The coefficient of the exact pair \((h,t)\) is a divisor-bounded sum over \(e_0\mid h\) from the grouped proof. At fixed \(h,t\) it retains the actual \(J\)-dyad, \(e_0\)-allocation, physical norm and every middle selector. The variable part of the row phase is \(\psi_u(h)^2\psi_u(t)\overline{\psi_u(\bar t)}\). At fixed \(v_2\), absorb the fixed twist, \(u_0\) and \(v_2\) evaluations into this pair's coefficient, keeping their zeros. As a function of \(\alpha=\alpha_{v_1}\) its raw phase is
\[
 \Theta_{h,t}(\alpha)
  =(\alpha/h)_6^2(\alpha/t)_6(\alpha/\bar t)_6^5 .
\]
Since \(h\) is good squarefree and \((h,t)=1\), its good primitive conductor is \(\operatorname{rad}(h t\bar t)\). The collision \(h\cap\bar t\) has exponent \(2+5\equiv1\pmod6\), and keeps its primitive zero. The only ambiguity when reconstructing a label from the local exponent pattern is a split pair with pattern \((1,1)\), where either orientation may have been chosen for \(t\). In particular the number of labels with any fixed pattern is at most \(2^{\omega(\operatorname{rad}(h t\bar t))}\). At inert primes only the \(h\)-factor occurs.

For \(T\le Nh<2T\), suppose the live \((h,t)\) labels are at most \(O_\epsilon((DH)^\epsilon TB/\sigma)\) and each good conductor has norm at most a constant times \(TB^2/C\). Use \(\sigma,C\ge1\). The positive squared row operator on these labels has bound
\[
 \ll (DH)^\epsilon A_2\left[A_1+\frac{T^2B^3}{\sigma C}\right].           \tag{3}
\]
To prove it, freeze \(v_2\) and majorize the positive sum over the chosen primary \(\alpha_{v_1}\) by a fixed Gaussian on the full Eisenstein lattice of norm scale \(A_1\). Opening the Gram matrix, equal primitive exponent patterns give \(O(A_1)\) per entry, with only divisor multiplicity. On other pairs the product character has a nonunit primitive good modulus of norm \(F\ll(TB^2/C)^2\). Equal local exponents give a finite deletion mask and distinct exponents remain nonprincipal. Expand the deletion over its squarefree divisors \(e\) and put \(\alpha=\alpha_e x\). The primitive Gauss identity followed by lattice Gaussian Poisson, with the fixed inverse-different pairing of QUADRATIC_CROSS_PREFIX-v2, gives a factor \(O(A_1/(Ne\sqrt F))\), the conjugate primitive value at the dual frequency, and a Gaussian on a norm length \(Y\asymp Ne F/A_1\). The zero mode vanishes, and nonunit dual modes keep the primitive zero. The sum over nonzero lattice modes of the Gaussian is \(O(Y)\) even when \(Y<1\), by ideal or lattice counting and rapid decay. Thus each off-pattern entry is \(O_\epsilon((DH)^\epsilon\sqrt F)\), with the divisor cost for \(e\). Schur's bound using the actual label count proves (3). Finite character phases, Gauss roots and deletion signs are used in this Gram identity. Their moduli are bounded only in the positive comparison. Sum over the \(O(A_2)\) choices of \(v_2\).

Here are three choices of the counting parameters, with \(c(h)\) the largest good rational integer \(m\) with \((m)\mid h\) as in RATIONAL_CONTENT_DUAL-v2.

- All pairs: \(\sigma=C=1\).
- \(c(h)\ge M\): \(\sigma=M,\ C=1\), since the number of \(h\) is \(O(T/M)\) by summing \(O(T/m^2)\) over \(m\ge M\).
- \(N(h,\bar t)\ge C\): \(\sigma=C\), and use the same \(C\) in the conductor bound. For fixed \(t\), a live \(h\) is divisible by one of the divisor-bounded number of factors of \(\bar t\) with norm at least \(C\), giving \(O_\epsilon((DH)^\epsilon T/C)\) choices. The conductor loses the actual shared norm.

The profile argument remains \(D/(E E_1(Nh)^2 Q_u)\), independent of \(t\). Separate it with the same compact log Fourier inversion as before, and put \(B/Nt,T^2/(Nh)^2\) into the bounded coefficient. Its squared mass is \(O_\epsilon((DH)^\epsilon TB/\sigma)\). The prefactor before the norm is \(O(D/(E E_1Ng Nw B T^2\sqrt R))\). The sum of \(1/(Ng Nw)\) over live pairs is harmonic with a squared logarithm. Equations (2) of the grouped proof and (3) here therefore give energy on the \(e_1,T,B\) dyad at most
\[
 \ll (DH)^\epsilon\mathcal M_{12}(W)^2
  \frac{A_2}{E E_1}
   \left[\frac{A_1}{T B\sigma}+\frac{T B^2}{\sigma^2 C}\right]
        y(1+y)^{-8}.                                                    \tag{4}
\]
This bound uses both variables inside the positive norm. The two scalar factors \(T^{-1}y(1+y)^{-8}\) and \(Ty(1+y)^{-8}\) are bounded by \(O(1/T_0)\) and \(O(T_0)\) respectively, including the subunit \(T_0\) case. The \(e_1\) divisor count and the logarithmic \(T\)-sum give at pure, for fixed \(B\),
\[
 D^{-1}\|E_{d,B}^*\|_2^2
 \ll (DH)^\epsilon\mathcal M_{12}(W)^2
 \left[\frac{D^{5/8}}{B\sigma E^{1/2}}
       +\frac{D^{1/8}B^2}{\sigma^2 C E^{3/2}}\right].                    \tag{5}
\]

If \(B\asymp D^{1/6}\) and either \(c(h)\ge D^{1/24}\) or \(N(h,\bar t)\ge D^{1/24}\), equation (5) is at most \(D^{5/12}E^{-1/2}\) up to the stated costs. Its second power at \(E=1\) is \(3/8\) in the content case and \(1/3\) in the overlap case. Therefore the cross with the entire original complement reaches \(3/4\), including \(d=1\), by the same divisor split as for the profile projections. For this statement choose one qualifying \(t\), with a deterministic rule on the union if both conditions occur.

With \(\sigma=C=1\), the balanced dyad \(B\asymp D^{1/6}E^{1/3}\) gives energy \(D^{11/24}E^{-5/6}\). On an \(E\)-dyad \(Y\le E<2Y\), pairing with (1) and summing the \(O(Y)\) ideals gives the four budgets
\[
 D^{29/48}Y^{1/12},\quad D^{35/48}Y^{-5/12},\quad
 D^{17/24}Y^{-1/12},\quad D^{37/48}Y^{-1/3}.
\]
For \(D^{1/16}\le Y\le D^{11/32}\) all meet target. The higher tail follows from (2) as before. At \(d=1\) the same unrestricted balance gives \(37/48\), above target. The joint bound does not control small \(d\), \(Nh\asymp T_0\) and a general low-content, low-overlap pair. The full pure equality cross and the signed off-equal assembly remain open.

