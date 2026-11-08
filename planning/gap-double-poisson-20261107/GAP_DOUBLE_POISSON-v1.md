# Joint Gaussian completion for the unit-cofactor split-prime comparison

Author draft, 7 November 2026 UTC; independent review pending. Acceptance for this scoped comparison requires an exact two-variable transform with the actual local powers and CRT phases, a uniform count of the dual conductor fibres including their Gaussian tails, and separate accounting for what this says about the signed kernel. No new input about prime distribution is used.

## Actual unit-cofactor reduction

Work under GAP_CORE_PAIR-v1 §§1–2. Restrict both actual columns to unit cofactors, so they are ordered products of two distinct good split prime ideals, each of norm \(>U_*\), with the original annulus \([D,2D]\). Each prime norm is in fixed multiples of \(\sqrt D\) since \(U_* \ge \sqrt{2D/7}\). This is only a part of the remaining split-prime problem. The marked collision between the two original columns is restored by the bound in that note, on its stated hypotheses. The comparison below acts on the auxiliary separated columns. It does not define a primitive gauge on shared-prime pairs. The transfer from the original central density still uses the preceding pending reductions.

Fix the original finite outer \(h,k,\ell,e,v_2\) and source components. Keep the bounded scalar, actual \(r\) clip and small squarefull selection, principal sixth-part density, both gauges, and raw masks. Use the primary generators \(\alpha_{\mathfrak a}\equiv1\bmod3\) of good ideals. Write \(\theta_q(x)=(x/q)_6\) and use zero on all multiples of \(q\) for any nontrivial power here. In one of the two columns, Gauss CRT on coprime \(p,q\) gives the factor
\(\theta_q(\alpha_p)^2\overline{\theta_q(\alpha_r)}\), as in rg:gauss-cross and the actual joint symbol in GAP_PRIME_PREFIX-v1 §3. The second column can be treated with its own phases and the conjugate of the same comparison. The other \(r\)-dependent factor is \(\overline{\theta_p(\alpha_r)}\), of modulus at most one; the actual \(k\) symbol and all fixed and source multipliers stay on the appropriate separate prime coefficients or in the \(r\) scalar. The individual-column collision is zero in \(\theta_q(\alpha_p)^2\). No common-prime zero is restored by a primitive character of a smaller conductor.

Separate the common \(W(Np\,Nq/D)\) by its Mellin integral with mass \(M(W)\). In each separated term the two inverse-norm weighted prime coefficients are \(a_p,b_q\); both have squared norm \(O((DH)^\varepsilon)\) by ideal counting. The actual \(g(p)g(q)\), signs, fixed shifted symbols, Gauss root phases and radial powers remain in these coefficients. Finite source/ray conditions can be expanded as in the preceding column reductions; one can equivalently use the resulting fixed prime subsequences for this comparison. The truncated ideal factors \(p,q\) are each supported in fixed multiples of \(P,T\) respectively, with \(P,T\asymp D^{1/2}\). We only use fixed outer terms for which the separated coefficients have this support and are independent of \(r\). The exact \(r\)-scalar is unchanged before it is bounded by its existing density/phase majorant.

Apply Cauchy in \(p\) separately at each actual \(r\); this removes \(\overline{\theta_p(\alpha_r)}\) only inside the positive norm. A resulting squared bound, apart from a fixed Gaussian majorization constant, \(\|a\|_2^2\) and the Mellin and finite-selector costs, is
\[
 \mathcal N = \sum_{x,y\in\mathcal O} e^{-\pi N x/P-\pi N y/R}
     \left|\sum_q b_q\theta_q(x)^2\theta_q(y)^5\right|^2. \tag{1}
\]
Indeed, \(x=\alpha_p,y=\alpha_r\) inject the selected prime and row ideal representatives into the element lattice, and the Gaussian is bounded below on the two original bands. Only after squaring do we enlarge to the full element lattice, which is a positive majorization. The Gaussian sum includes \(0\) but the character powers give zero there. For nonsquarefree \(r\) in the original band the local power still refers to its actual primary generator, so this reduction does not require \(r\) squarefree. Separate row/ray selectors after absolute value only inside (1). Formula (1) is an upper comparison, not an alternative exact expression for the original signed pairing.

## Exact completion of the comparison

Let \(\gamma=\alpha_q,\gamma'=\alpha_{q'}\), \(Q=NqNq'\). Define \(e_\lambda(z)=\exp(2\pi i\operatorname{Tr}(z/(\delta\lambda)))\), \(\delta=1+2\omega\), and \(\tau_\lambda(\chi)=\sum_{z\bmod\lambda}\chi(z)e_\lambda(z)\), as in cbk:finite-Fourier. For \(q\ne q'\), put \(\Theta=\theta_q\overline{\theta_{q'}}\), character modulo \(\gamma\gamma'\). This includes distinct conjugate prime ideals of equal rational norm. Both \(\Theta^2\) and \(\Theta^5\) are primitive at both local primes. The two Gaussian transforms, with variables \(\alpha,\beta\in\mathcal O\), give the exact summand of (1) divided by \(b_q\overline{b_{q'}}\):
\[
 \frac{4PR}{3Q}\,L(q,q')
 \sum_{\alpha,\beta\in\mathcal O}
 e^{-\frac{4\pi}{3Q}(P N\alpha+R N\beta)}
 \Theta(\beta\alpha^4),
 \qquad
 L(q,q')=\frac{\tau_{\gamma\gamma'}(\Theta^2)
                 \tau_{\gamma\gamma'}(\Theta^5)}{Q}. \tag{2}
\]
This statement refers to the coefficient of \(b_q\bar b_{q'}\) and does not divide by a potentially zero number. The Gaussian in one variable has transform \(P\exp(-\pi P|w|^2)\), lattice covolume \((\sqrt3/2)Q\) and dual lattice \(2(\overline{\delta\gamma\gamma'})^{-1}\mathcal O\); the Euclidean pairing of the residue \(z\) with \(2\bar\alpha/(\overline{\delta\gamma\gamma'})\) gives \(e_{\gamma\gamma'}(\alpha z)\). The two transforms produce the factor \(\bar\Theta^2(\alpha)\bar\Theta^5(\beta)=\Theta(\beta\alpha^4)\). Both zero frequencies and all nonunit dual arguments are still zero, including any \(\alpha,\beta\) divisible by a prime in the corresponding pair. The diagonal \(q=q'\) is treated before completion; its whole contribution is nonnegative and bounded by \(O(PR\|b\|_2^2)\) by counting the two Gaussian lattices. In particular it is \(O(D^{67/80}\|b\|_2^2)\) throughout the central band. No principal-character primitive completion is used for this diagonal.

Writing \(g_q(j)=\tau_\gamma(\theta_q^j)/\sqrt{Nq}\), the actual CRT phase in (2) is
\[
 L(q,q')=g_q(2)g_q(5)g_{q'}(-2)g_{q'}(-5)K(q,q'),
 \qquad K(q,q')=\theta_q(\gamma')\overline{\theta_{q'}(\gamma)}. \tag{3}
\]
The local exponents add to \(2+5=7\equiv1\bmod6\). Every \(g\) in (3) has modulus one. Cubic reciprocity for the primary generators gives \(K^2=1\). Thus \(K=K^3\) is exactly the quadratic CRT multiplier, and may also be read as \(\gamma_4(\gamma\gamma')/(\gamma_4(\gamma)\gamma_4(\gamma'))\) with the existing period-four Gauss factor of the literal generator in sw:dual. In particular it is fixed on pairs of prescribed mod-four generator classes; no new Gauss evaluation is invoked. One can retain (3) without this last description. It is still necessary to retain the single-prime \(g\)'s and the actual prime coefficients, including the original cubic Gauss phases. The two Fourier frequencies do not sample two independent characters.

## Bound for all small good conductors, including the coherent part

For a nonzero pair \((\alpha,\beta)\), let \(z\) be the good sixth-free part of the ideal \((\beta\alpha^4)\); at each good prime \(v(z)\) is the residue in \(\{0,\ldots,5\}\) of \(v(\beta)+4v(\alpha)\). Put \(B=N\operatorname{rad}(z)\), with \(B=1\) allowed. This is the norm of the good part of the conductor of the reciprocal sextic character of the dual argument (each nontrivial tame local power has conductor exponent one). It is not the conductor \(Q\) used in the Fourier transform. S-supported factors and literal unit phases of \(\alpha,\beta\) are not removed from the character in (2). This selection is a conductor cutoff in a bound; there is no substitution of \(z\) for the raw dual argument in (2).

For \(A,V\ge1\), count all pairs with \(0<N\alpha\le A,\ 0<N\beta\le V\) at a given \(z\). Ignore only the pair-dependent raw zeros in this upper count. Split each ideal into its S-supported and good parts. There are \(O_S((1+\log(AV))^{2|S|})\) ways to choose the two S-supported ideals; ignore their lengths in the following count. Each pair of ideals corresponds to 36 pairs of nonzero elements, with unit phases kept in the analytic expression. The good part of \((\alpha)\) uniquely has the form \(t\,d^3\) with \(t\) cubefree. Write \(t=t_0 t_1\), with \(t_0\) supported on \(\operatorname{rad}(z)\) and \(t_1\) coprime to it. At the primes of \(z\) choose \(t_0\)'s exponents from \(0,1,2\); this costs at most \(3^{\omega(z)}\). At those primes \(b_0\)'s exponents are the unique representatives of \(v(z)+2v(t_0)\bmod6\) between 0 and 5. At all other good primes the exponent of the sixth-free part of \((\beta)\) is \(2v(t_1)\). Therefore the good part of \((\beta)\) is precisely \(b_0 t_1^2 e^6\). The powers \(d,e\) are arbitrary good ideals and can overlap any permitted factors. This representation does not require \(\alpha,\beta\) to be squarefree. At every prime dividing \(z\), at least one of \(t_0,b_0\) is divisible by it, so \(Nt_0\,Nb_0\ge B\).

Set \(A'=A/Nt_0,\ V'=V/Nb_0\); if either is below one the contribution is zero. Ideal counting gives a contribution bounded by
\[
 A'^{1/3}V'^{1/6}\!
 \sum_{Nt_1\le\min(A',\sqrt{V'})}(Nt_1)^{-2/3}
 \ll A'^{1/3}V'^{1/6}\min(A',\sqrt{V'})^{1/3}
 \le (AV/B)^{1/3}. \tag{4}
\]
In particular the class \(z=1\) counts the family \(t\,d^3,\ t^2e^6\), not just separately sixth powers in both variables. Summing over radicals of norm at most \(Z\) and their at most \(5^{\omega}\) valuations, and using \(15^\omega\ll_\varepsilon B^\varepsilon\) and ideal counting, yields
\[
 \#\{0<N\alpha\le A,\ 0<N\beta\le V,\ B\le Z\}
 \ll_{S,\varepsilon}(AVZ)^\varepsilon (AV)^{1/3} Z^{2/3}. \tag{5}
\]
This count includes equal-norm and conjugate labels with multiplicity. It follows by a harmonic sum of \(B^{-1/3+\varepsilon}\) over actual squarefree ideals, not by a rational norm squarefree restriction.

In (2), \(Q\asymp T^2\). Use (5) with \(A=T^2/P,\ V=T^2/R\) and their multiples \(2^iA,2^jV\), \(i,j\ge0\), taking the first box inclusively. Every higher shell has a Gaussian factor \(O(\exp(-c(2^i+2^j)))\) with fixed constants, interpreting the first shell by a harmless larger constant. Polynomially growing factors and logarithms are summable. Since \((\sum_q|b_q|)^2\ll T\|b\|_2^2\), the absolute aggregate of the \(q\ne q'\) terms in (2) restricted to \(B\le Z\) is bounded by
\[
 \ll_{S,\varepsilon}(DH Z)^\varepsilon
      \|b\|_2^2\,\frac{PR}{T}\,(T^4/(PR))^{1/3}Z^{2/3}
 \asymp_{\rm scales} (DHZ)^\varepsilon\|b\|_2^2 D^{1/2}R^{2/3}Z^{2/3}. \tag{6}
\]
The last comparison refers to the displayed upper-budget monomial, not an asymptotic for the sum. With \(Z=1\) this is at most \(D^{29/40}\) times mass and subpowers. With \(Z=D^{3/8}\) it is at most \(D^{39/40}\), uniformly through \(R=D^{27/80}\). The bound does not require fixed Gauss phases or any absence of coherent means. Both the true diagonal and this entire small-conductor sector are below the squared norm size \(D^{59/60}\) that would, if it held for the full comparison, offset the prior \(D^{1/120}\) density factor when paired with the inherited size \(D\) for the other column. For example \(D^{39/40}\) on one full squared norm would give \(H D^{-1/240}\) in that argument. Here that exponent is only a budget for components of the comparison.

## Failed full-comparison estimate and remaining signed problem

The rest of (2) has \(B>D^{3/8}\). With no cancellation, counting all Fourier arguments at lengths \(A,V\) costs \(AV\); the right-hand side would then cost \(T^3\|b\|_2^2\asymp D^{3/2}\|b\|_2^2\) by the same Gaussian summation and pair triangle. This is worse than the inherited squared size \(D\). This argument has not estimated the high-conductor part. The cutoff split is in a positive auxiliary norm after majorization, and the individual off-diagonal pieces can be signed. Neither the small-conductor bound nor its sum with the diagonal is a standalone bound for any subcollection of terms in the original signed pairing.

The next problem is to estimate the larger dual conductors with the joint \(\Theta(\beta\alpha^4)\), both single-prime phases, exact Gaussian dependence on \(Q\) and full raw masks still present, or to bypass this upper comparison by exploiting the original signed pairing. In particular one cannot use a single fixed cubic prime coefficient sequence for the original mixed symbol: before completion it also contains the row-dependent quadratic factor \(\theta_q(\alpha_r)^3\) in \(\theta_q(\alpha_p)^2\theta_q(\alpha_r)^5\). The whole unit-cofactor term and the nonunit-cofactor continuation stay open. The whole-prefix candidate \(109/144\), signed \(13/12\), unsigned \(9/8\), determinant/zero-location by scope, Lean and GRH do not change.
