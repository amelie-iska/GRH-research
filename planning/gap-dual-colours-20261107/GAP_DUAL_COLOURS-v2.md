# Quadratic and cubic conductor sectors of the joint Gaussian comparison

7 November 2026 UTC. Author draft, independent review pending. Acceptance for this scoped result requires a separable treatment of the actual shared Gaussian scale with a summable remainder bound, all local raw zeros and diagonal corrections, and explicit ranges giving power budgets for larger dual conductors. The starting identity is GAP_DOUBLE_POISSON-v1 (2)–(3) on the central far-gap unit-cofactor split-prime positive comparison. Transfer to that comparison from the original signed pairing still uses the preceding pending reductions. No original selection, conductor, gauge, capacity, density, common \(W\) or bound on their signed assembly is changed here.

## 1. Separation of the actual Gaussian at the pair modulus

Retain \(D^{13/40}\le R\le D^{27/80}\), \(P,T\asymp D^{1/2}\), \(A=T^2/P\), \(V=T^2/R\), \(Q=NqNq'\asymp T^2\), with exactly the notation and fixed bands of GAP_DOUBLE_POISSON-v1. In particular \(q,q'\) are good split prime ideals and may be distinct with equal norms. Let \(\mathcal E\) be any selection of the nonzero dual pairs \((\alpha,\beta)\) independent of \(q,q'\). Let \(\mathcal D(\mathcal E)\) be the contribution to (2) with \((\alpha,\beta)\in\mathcal E,\ q\ne q'\), including its prefactor and \(b_q\overline{b_{q'}}\). It can have either sign. Its original raw symbol is \(\theta_q(z)\overline{\theta_{q'}(z)}\) with \(z=\beta\alpha^4\). The \(q=q'\) term of the *primal* norm remains separate.

In (3), \(K(q,q')\) is constant for each pair of fixed mod-four generator classes. Put \(c_q=g_q(2)g_q(5)\). Complex conjugation of the literal Gauss sum gives \(g_q(-j)=\theta_q^j(-1)\overline{g_q(j)}\), since the additive character changes sign. Thus the two Gauss factors on the \(q'\) side of (3) are \(\theta_{q'}(-1)\overline{c_{q'}}\), including the sign. All these factors are unitary. Keep the classes and \(K\) until the exact factorization; no absolute value in \(q,q'\) is required for the sieve route.

Choose a fixed smooth function \(\rho\) of compact support, equal to one on the interval of all \(s=\log(Q/T^2)\) from the fixed prime bands. Set \(u=(4\pi/3)(N\alpha/A+N\beta/V)\). The common radial factor is exactly \(T^{-2}F_u(s)\) at these moduli, where
\[
 F_u(s)=\rho(s)e^{-s}\exp(-u e^{-s}),\qquad
 F_u(s)=\frac1{2\pi}\int_{\mathbb R}\widehat F_u(t)e^{its}\,dt .
\]
On the compact support of \(\rho\), two integrations by parts and the bound with no derivatives give
\[
 |\widehat F_u(t)|\ll (1+|t|)^{-2}(1+u)^2 e^{-c u}
                 \ll (1+|t|)^{-2}e^{-c' u}. \tag{1}
\]
Constants are fixed by the bands and the cutoff. In particular the expansion is absolutely integrable and has exponentially summable two-frequency shell bounds. The identity uses the actual value of \(Q\); replacing \(Q\) by a typical modulus would not justify it.

At each \(t,\alpha,\beta\) and each pair of mod-four classes, insert the diagonal algebraically and subtract it back. The factor \(e^{its}=(Nq/T)^{it}(Nq'/T)^{it}\) yields a product of two single-prime sums, the second conjugated with the opposite norm twist and its own \(\theta(-1)\). Each coefficient vector is a restriction of \(b\) multiplied by fixed phases; its squared mass is at most \(\|b\|_2^2\). The subtraction is present only for equal classes; in absolute value it is at most \(\|b\|_2^2\) per dual pair, since the symbol may be zero. This inserted diagonal is unrelated to the primal diagonal. For fixed shells, apply Cauchy in \(\mathcal E\) to the two single-prime sums. One may relax a restriction *independent of \(q,q'\)* only inside the resulting positive square norms. The raw \(q\)-dependent deletion in each character is never discarded. Equations (1) and the fixed finite class sum justify all these operations and summing the resulting polynomial shell budgets against their Gaussian decay.

## 2. The two conductor parts and the all-element comparisons

Write \(B_2=N\operatorname{rad}(z_2)\) and \(B_3=N\operatorname{rad}(z_3)\), where \(z_2\) is the square-free part by valuation residues of the good part of \((\beta)\), and \(z_3\) is the cube-free part by valuation residues of the good part of \((\alpha\beta)\). In particular \(\operatorname{rad}(z_2)=z_2\), and the unit is allowed. At every good prime the two exponents are \(v(\beta)\bmod2\) and \((v(\alpha)+v(\beta))\bmod3\). Since these are the residues of \(v(\beta)+4v(\alpha)\), the prior \(B\) is the norm of the least common multiple of the two radicals, not generally \(B_2 B_3\). The raw factorization on each \(q\) is
\[
 \theta_q(\beta\alpha^4)=\theta_q^3(\beta)\theta_q^4(\alpha\beta).
 \tag{2}
\]
Here every nontrivial power of \(\theta_q\) has value zero at the nonunits, including on an argument whose valuations give a smaller reciprocal conductor. Formula (2) holds even there. The same statements hold for \(q'\).

For \(n=3,6\), let \(\chi_{n,q}\) denote respectively \(\theta_q^4\) (conjugate cubic) and \(\theta_q\) (sextic). The pinned de Faveri arXiv:2610.04045v1, Theorem 1.1, as in phy:input, implies the following **all nonzero elements** bound at \(L\ge1\) and \(T\ge1\):
\[
 \sum_{0<Nx\le L}\left|\sum_{Nq\asymp T} c(q)\chi_{n,q}(x)\right|^2
 \ll_{S,\varepsilon}(LT)^\varepsilon\|c\|_2^2
 \begin{cases}
 L+TL^{1/3}+(LT)^{2/3}, & n=3,\\
 L+TL^{1/6}+L^{5/6}T^{1/3}+L^{1/3}T^{5/6}, & n=6 .
 \end{cases} \tag{3}
\]
This is an external sieve application. To see the extension from the power-free input, write \(x=u_S\alpha_a\alpha_d^n\) with literal \(S\)-supported \(u_S\) including a unit, good \(n\)-free \(a\), arbitrary good \(d\), and the primary generators \(1\bmod3\). The decomposition is unique. At fixed \(u_S,d\) the factor \(\chi_{n,q}(u_S)\mathbf1_{(q,d)=1}\) is a column multiplier of modulus at most one. Enlarge only the resulting positive \(a\) norm, with length \(L/(Nu_S(Nd)^n)\). Unit lengths are included; subunit ranges are empty. The \(T\)-term sums with the actual count \(O((L/Nu_S)^{1/n})\) of \(d\)'s; the other inverse-power exponents on \(Nd\) are \(3,2\) for \(n=3\) and \(6,5,2\) for \(n=6\). The sums over \(u_S\) converge with positive norm powers, or cost fixed logarithms in a zero-exponent finite bound. The split-prime columns are a subsequence of the power-free columns with zero elsewhere. The cubic literal primary matching follows by the same generator argument as phy:generator-proof: a fractional good generator's cube mod \((3)\) has order at most two, so the unit ambiguity is \(1\) or \(-1\), both cubic residues. The sextic case uses its sixth power and ambiguity one. The fixed data can use modulus divisible by \((3)\) and by the source's local powers at \(S\); the field contains both required root groups. This establishes the intended family, including raw zeros, before using the arbitrary coefficients in the theorem. Neither (3) nor its use requires prime distribution, arbitrary row weights, or replacing a radicand by its conductor.

## 3. High full conductors with small quadratic or cubic part

All bounds below include \((DH)^\varepsilon\|b\|_2^2\); polynomial cutoff factors can be included in the subpower budget. In the first radial box \(N\alpha\le A,N\beta\le V\), take the cutoffs inclusively. Subsequent shells have the usual independent doubled lengths and the decay (1). Estimates stated at \(A,V\) thus include the full two Gaussian tails. Any further \(q,q'\)-independent sub-selection has the same bounds.

**Small quadratic part.** At \(B_2\le Z_2\), the number of \(\beta\)'s through \(V\) is \(\ll_{S,\varepsilon}(V Z_2)^\varepsilon V^{1/2} Z_2^{1/2}\): at a given good squarefree \(z_2\) use \((\beta)_{\rm good}=z_2 d^2\), then sum \((Nz_2)^{-1/2}\), and include the finitely supported \(S\)-norm factors and literal units. For each such \(\beta\), absorb the actual \(\theta_q(\beta)\) (including its zero) into both vectors. The only varying symbol in \(\alpha\) is \(\theta_q^4(\alpha)\). Bound the positive \(\alpha\) norm by (3) for \(n=3\) at \(A\asymp T\), costing \(D^{2/3}\). The diagonal subtraction costs \(A\) at each \(\beta\) and is absorbed. This gives
\[
 |\mathcal D(\mathcal E)|\ll (DH)^\varepsilon\|b\|_2^2
       \frac{PR}{T^2}D^{2/3} V^{1/2} Z_2^{1/2}
 \ll (DH)^\varepsilon\|b\|_2^2 D^{2/3}R^{1/2} Z_2^{1/2}. \tag{4}
\]
At \(Z_2=D^{7/24}\) this is at most \(D^{157/160}\) times mass and subpowers. There is no restriction on \(B\) or \(B_3\).

**Small cubic part.** Fix a good cube-free ideal \(z_3\) of radical norm \(B_3\). At each prime of this radical choose the exponents \(j\in\{0,1,2\}\) of the cube-free part of \((\alpha)\); the exponent in \((\beta)\) is \(k=v(z_3)-j\bmod3\) in \(\{0,1,2\}\). If \(t_0,b_0\) are the two ideals from these choices then \(Nt_0 Nb_0\ge B_3\). At other good primes the residues are complementary. Thus the two good ideals have the unique form
\[
 t_0 a b^2 d^3,\qquad b_0 a^2 b e^3,
\]
with \(a,b\) squarefree, disjoint and outside the radical, and \(d,e\) arbitrary good ideals, including overlaps. For fixed \(a,b,t_0,b_0\), counts of \(d,e\) cost \((AV/(Nt_0 Nb_0))^{1/3}/N(ab)\), with empty ranges when either length is subunit. Sum the two harmonic counts in \(a,b\), the \(\le 3^{\omega(z_3)}\) local choices, and the \(S\) factors and units. Summing over radicals of norm at most \(Z_3\), with \(\le2^{\omega}\) cube-free valuations per radical, gives
\[
 \#\{0<N\alpha\le A,\ 0<N\beta\le V,\ B_3\le Z_3\}
     \ll_{S,\varepsilon}(AV Z_3)^\varepsilon (AV)^{1/3}Z_3^{2/3}.
 \tag{5}
\]
This counts *only the cubic conductor condition*. It leaves the quadratic part unrestricted. Keep the exact character and its zeros in the expression before taking the pair triangle, where \((\sum_q |b_q|)^2\ll T\|b\|_2^2\). Using (5) then bounds this sector by
\[
 \ll(DH)^\varepsilon\|b\|_2^2 D^{1/2}R^{2/3}Z_3^{2/3}. \tag{6}
\]
At \(Z_3=D^{31/80}\) it is at most \(D^{59/60}\). This bound includes all of the previous \(B\le D^{3/8}\) range and can apply for \(B>D^{3/8}\) as well. The exact \(R\)-dependence matters: upon testing against the *prior* other-column squared budget \(D\) and the density \((X/R)^{1/6}\), the worst powers relative to \(H\) of (4) and (6) separately are \(-1/320\) and \(-1/480\). These are scale comparisons for pieces of the auxiliary norm, not estimates on selected terms of the original signed form.

## 4. Sparse first frequencies and the residual obstruction

Freezing \(\alpha\) with its actual \(\theta_q^4(\alpha)\) mask in the two vectors permits (3) with \(n=6\) in \(\beta\). At a given \(\alpha\) the squared cost is the sextic expression \(\Xi_6(V,T)=V+TV^{1/6}+V^{5/6}T^{1/3}+V^{1/3}T^{5/6}\); the subtraction \(V\) is absorbed. With at most \(F\) choices of \(\alpha\) per first radial box, and the analogous growth count in outer boxes, the bound is \((PR/T^2)F\Xi_6(V,T)\) times mass and subpowers, by (1). Thus \(F\ll A D^{-1/12}\) gives an upper power \(467/480\) across the central band. Two instances, with independent further masks allowed, are \(N\alpha\le A D^{-1/12}\), and good squarefull part of \((\alpha)\) of norm at least \(D^{1/6}\). For the second, the good squarefull part \(f\) has all valuations at least two; the count of such \(f\) through \(Y\) is \(O(Y^{1/2})\) by \(f=d^2 e^3\) with \(e\) squarefree. At fixed \(f\), count other good and \(S\) parts through \(L/Nf\), giving \(O_S(L/Nf)\); summing \(f\ge D^{1/6}\) costs \(L D^{-1/12}\). Dyadically the same bound holds at the enlarged length \(L\). The radial cutoff may be empty and requires no manufactured unit below norm one.

For arbitrary \(\alpha\), \(F\ll A\) gives \(R\Xi_6(V,T)\). Its exponents with \(r=\log_D R\) are \(1,\ 2/3+5r/6,\ 1+r/6,\ 3/4+2r/3\), so this improves absolute counting \(D^{3/2}\) for the completed expression to \(D^{169/160}\). It still loses to the prior \(D\) bound on the original squared comparison of the single-column vector; it also does not bound the auxiliary remainder by \(D\). In the three sparse sectors the savings above rely on small counting mass in one coordinate or one conductor component. They do not estimate the two-large-conductor part. A disjoint decomposition can take first \(B_2\le D^{7/24}\), then \(B_3\le D^{31/80}\) on its complement, then the two sparse first-frequency selections on the complement of both (subtract their intersection or take them in sequence). The remaining sector has both \(B_2,B_3\) above those cutoffs, \(N\alpha>A D^{-1/12}\), and small good squarefull part. One cannot keep the sharper parts and claim cancellation by the complement: this is an auxiliary signed off-diagonal comparison after positive enlargement. The needed improvement must use the two varying components together, more of the actual prime coefficient phases, or the pre-Cauchy signed pairing. The full unit-cofactor and nonunit-cofactor pairings, candidate \(109/144\), whole signed \(13/12\), global unsigned \(9/8\), determinant/zero-location, Lean and GRH remain unchanged.


The exact sparse-first-frequency comparison with the same prior partner and density has relative exponent \(1/48-r/12\), hence worst value \(-1/160\) at \(r=13/40\), rather than its value \(-7/960\) at \(r=27/80\). The author control v2 incorrectly used the latter as a uniform guard and stopped. This is only a correction to that guard and an additional scoped scale comparison; the uniform squared budget \(D^{467/480}\) above is unchanged.
