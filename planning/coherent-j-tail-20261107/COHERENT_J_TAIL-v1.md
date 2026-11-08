# A coherent large-divisor bound for the continuous prime-density term

7 November 2026 UTC. Author checked; independent review pending. This is a bound on a specified part of the actual signed continuous term \(\mathcal J\) of cmr:primeerror, not a bound on \(K_0-\mathcal J\). The power form uses the same pinned external \(7/8\) zero-free statement as GAP_NORM_STRIP_AND_PIT-v1, without an independent certification of that theorem. The structural estimate below explicitly states its Mertens input and also works with the elementary exponent \(1\). Acceptance requires exact half-open and jump accounting, retention of full ideal and row masks, and a bound using only the pinned physical sieve on legitimate unweighted subsequences.

## 1. Statement and scope

Use the original complete good squarefree columns, one common complex \(W\) smooth with support \([1,2]\), fixed \(S,\nu,u_0\), and original unweighted two-pivot rows (\(A_6=1\), no other moving factors). Their outside-\(S\) ideal is \(v_1v_2^2\), with \(v_1,v_2\) squarefree and coprime, physical capacity \(H_b\) as in phy:short, all original internal and literal selections and all raw zeros. We require \(U\ge7,\ U^2\le D\le7U^2/2\) and \(1\le H_b\ll H\le D^{3/4}\); empty blocks are omitted. Bounded natural unit multiplicities can be split into their fixed literal components. No arbitrary row weights are used in the sieve. Set
\[
 M_S(x)=\sum_{N\mathfrak e\le x,\ (\mathfrak e,S)=1}\mu(\mathfrak e)
\]
with value zero for \(x<1\), and use \(M_2(W)=\max_{0\le j\le2}\|(x\partial_x)^jW\|_\infty\). If \(|M_S(x)|\ll_S x^\sigma\) for \(x\ge1\) and a fixed \(2/3<\sigma\le1\), then for \(1\le Y\le2D/U\) the **nonunit-residual** part (the pair \((a,b)=(1,1)\) omitted) satisfies
\[
 \frac{|\mathcal J_{\ge Y,\mathrm{nu}}|}{D}
 \ll_{S,\sigma,\epsilon}(DH)^\epsilon M_2(W)^2
 \left[
 H_bY^{\sigma-1}+\frac{D}{UY}
 +H_b^{5/6}(D/U)^{1/3}Y^{\sigma-4/3}
 +H_b^{1/3}(D/U)^{5/6}Y^{\sigma-11/6}
 \right]. \tag{1}
\]
Here the cutoff is on the literal smooth incidence divisor \(F=Nf\ge Y\), not the residual length in the previous scalar Mertens estimate and not the original column gcd. It is the contribution of the actual signed sum \(\sum_f\mu(f)\) in the continuous density term. For \(\sigma=1\) the formula includes logarithms via the subpower. For larger \(Y\) the term is zero by support.

From the source-dependent \(M_S(x)\ll_{S,\eta}x^{7/8+\eta}\) proved below, use \(7/8\) in (1) with a smaller internal \(\eta\) absorbed into the subpower. At \(H=D^{3/4}\), \(Y=D^{1/10}\), the four upper powers are \(59/80,\ 2/5,\ 179/240,\ 137/240\). Thus the signed continuous large-divisor nonunit tail is at most \(D^{179/240+\epsilon}\) with the stated profile factor, a \(1/240\) margin below \(H\). At \(Y=D^{1/11}\) it is target-sized. Without the external input, \(\sigma=1\) gives target size at \(Y=D^{1/8}\) and no margin in the \(H_b\) term. These are sufficient cutoffs and not optimality claims.

## 2. Exact deletion and finite Abel at a fixed density point

For \(t\ge U\) put \(Z=D/t\). Partition \(F\ge Y\) into half-open intervals \([X,2X)\) with \(X=2^jY\). On active terms in such an interval each residual norm lies in \([L/2,2L]\) where \(L=Z/X\). If the pair is nonunit then \(\max(Na,Nb)\ge7\) and \(F<U\), because \(F t\max(Na,Nb)<2D\le7U^2\). Profile endpoints vanish. Thus we may drop the \(U\)-smooth restriction on \(f\) in this sector, and the short-coefficient identity of cmr:short-coefficient applies. The two separate masks \(a\ne1\) (arbitrary \(b\)) and \(a=1,b\ne1\) partition the nonunit pair selection without changing any multiplicities.

After factoring the actual \(\mu(a)\mu(b)\nu(a)\overline{\nu(b)}\chi_a(u)\overline{\chi_b(u)}\) from a summand, the signed \(f\)-weight is
\[
 w_{a,b}(v)=W(vNa/Z)\overline{W(vNb/Z)}
        \bigl(1-2\mathbf1_{c<v\le d}\bigr),\qquad
 c=\frac{U}{\max(Na,Nb)},\quad d=\frac{U}{\min(Na,Nb)}.
\]
The signed scalar is \(\sum_{X\le Nf<2X,\ (f,Sabu)=1}\mu(f)w_{a,b}(Nf)\). There is no equal-norm projection: if \(Na=Nb\), then \(c=d\) and the jump part is empty, while all orientations still occur in the smooth part and endpoint terms. Neither \(\nu\) nor the literal row symbols were averaged.

For fixed \(a,b,u\), use the finite convolution cmr:deletion-convolution relative to the fixed \(S\): replace the closed prefix by
\[
 \sum_{\substack{\mathfrak h:\ \operatorname{supp}\mathfrak h\subset
                          \operatorname{supp}(abu)\setminus S}}
              M_S(v/N\mathfrak h).
 \tag{2}
\]
This retains **all** prime powers in \(\mathfrak h\) and uses no conductor substitution. At each prime in \(\mathfrak h\), the union projector has the exact expansion
\[
 1_{p\mid a\ \mathrm{or}\ b\ \mathrm{or}\ u}
 =1_{p\mid u}+1_{p\nmid u}
        \bigl(1_{p\mid a}+1_{p\mid b}-1_{p\mid a}1_{p\mid b}\bigr).
 \tag{3}
\]
Place its entire \(\mathfrak h\)-power into one of four mutually prime-support-disjoint ideals \(h_u,h_a,h_b,h_{ab}\). This is a signed expansion, not a partition of the row variables into disjoint ideal supports. Let \(r_u=\operatorname{rad}(h_u)\), \(r_a=\operatorname{rad}(h_a h_{ab})\), \(r_b=\operatorname{rad}(h_b h_{ab})\). In a term of (3) the row has \(r_u\mid(u)\), none of the other assigned primes divides \(u\), and the columns have \(r_a\mid a,\ r_b\mid b\). The original raw symbols remain zero even beyond these restrictions.

For a fixed such tuple let \(C(v)=M_S(v/N\mathfrak h)\) and \(C(v^-)\) its strict prefix. The exact half-open finite Abel identity is
\[
 \sum_{X\le N\mathfrak h N\mathfrak e<2X}
       \mu(\mathfrak e)\mathbf1_{(\mathfrak e,S)=1}
                         w_{a,b}(N\mathfrak h N\mathfrak e)
 = C((2X)^-)w_{a,b}(2X)-C(X^-)w_{a,b}(X)
   -\int_X^{2X}C(v)w'_{a,b,\mathrm{ac}}(v)\,dv
   -\sum_{v\in[X,2X)} C(v)\bigl(w_{a,b}(v+)-w_{a,b}(v)\bigr).
 \tag{4}
\]
The last sum runs only over jumps in \(w\). It uses \(C(v)\), the **closed** prefix, because the coefficient at the jump itself is the left value. For instance a jump at \(X\) is included with the closed prefix, one at \(2X\) is absent, and if an ideal has norm exactly \(c\) or \(d\) its weight is the stated left value. The endpoint values \(w(X),w(2X)\) are the left values at those arguments. This formula follows by telescoping the step prefix on each smooth subinterval or by summing the fundamental theorem of calculus with the displayed jump increments. All sums are finite: the prefixes and jumps vanish for \(N\mathfrak h>2X\).

## 3. Using the row operator before the triangle over the deletion placements

At each smooth \(v\) and each dyadic endpoint the \(w\) factors are separable in \(a,b\) (for the derivative use the sum of two products). The \(2\mathbf1_{vNa\le U}-1\) factors are kept on their own sides. Norms of the profile factors are bounded by \(M_2(W)^2\) after taking the product, with \(dv/v\) for the derivative. All prefix magnitudes in (4) are \(O((X/N\mathfrak h)^\sigma)\) for \(N\mathfrak h\le2X\), and may be zero at a subunit argument.

Each jump has the same bound after separating its variables. Split the two strict orderings of \(Na,Nb\); equality has no jump. At a jump \(v=U/Na\), the prefix \(C(U/Na)\) and the condition \(X\le U/Na<2X\) belong only to the \(a\)-coefficient. The product is \(W(U/Z)\overline{W((U/Z)(Nb/Na))}\); the reversed jump uses the conjugate version. The second factor separates by Mellin inversion in the ratio \(Nb/Na\), with integrable mass \(O(M_2(W))\) on the purely imaginary line; multiplication by \((U/Z)^{-i\tau}\) costs no norm. Its support and smoothness ensure the bound by twice integrating in log coordinate; the first factor is bounded by \(M_2(W)\). The strict comparison of the two integer norms in \([L/2,2L]\) is a finite cyclic interval indicator with logarithmic Fourier mass, as in the previous strip argument (use the one-sided interval in a modulus larger than \(4L+1\)). These factors remain unitary diagonal twists. No derivative of the jump selector or growing reciprocal bound with a Fourier parameter is needed. The \(2,-2\) jump multipliers are kept before taking the bound.

Now restrict rows to \(r_u\mid (u)\). For each prime of \(r_u\) fix its valuation, \(1\) or \(2\), in the physical ideal \(v_1v_2^2\), giving at most \(2^{\omega(r_u)}\) disjoint assignments. Strip this frozen factor: its norm is at least \(Nr_u\); its literal character on either column is a fixed bounded coefficient multiplier, including its raw zero. The remaining physical rows are good sixth-free, of norm \(\le H_b/Nr_u\), and inject for a fixed assignment. Any further row selections are relaxed only within positive norms. This checks the hypotheses of the pinned de Faveri Theorem 1.1 as applied in phy:family/phy:input, with the two original column subsequences of length \(O(L)\). If \(Nr_u>H_b\) the assignment is empty. If an ideal \(r_a\) or \(r_b\) has norm above \(2L\) its column side is empty; otherwise the column squared masses are bounded by \(O(L/Nr_a)\) and \(O(L/Nr_b)\) times the squared bounded coefficient factors by ideal counting. In particular this does not apply a sieve at a subunit residual length.

Apply Cauchy in the remaining rows to each separated bilinear pairing. With the dyadic, Mellin and comparator costs as above, the budget for a tuple before summing placements is
\[
 \ll (DH)^\epsilon M_2(W)^2
   \frac{X^\sigma L}{(N\mathfrak h)^\sigma\sqrt{Nr_a Nr_b}}\,
       2^{\omega(r_u)}\,\Phi_6(H_b/Nr_u,\,C L) ,
 \tag{5}
\]
for fixed absolute \(C\). A factor from the count of orderings or endpoints is harmless. On nonunit support \(L\ge7/2\); outside it the original integral at this dyad is zero. Thus all invoked lengths in (5) are legal. The whole \(a,b\) sum with each raw row correlation was kept until this bound on the separated form. In particular this is not the absolute residual triangle of cmr:mertens-budget.

Only now take the triangle over placements in (5). For \(h_a,h_b,h_{ab}\) the Euler sums converge absolutely: the first two acquire \(p^{-\sigma-1/2}\), the last \(p^{-\sigma-1}\), with additional power tails. The \(H_b\), \(H_b^{5/6}\) and \(H_b^{1/3}\) monomials carry \(r_u\) exponents \(1,5/6,1/3\) respectively; \(\sigma+1/3>1\), so their \(h_u\) Euler sums converge as well, with the factor 2 per selected prime. The monomial \(L\) has no \(r_u\) saving and must use the finite \(Nh_u\le2X\) count, costing \(X^{1-\sigma+\epsilon}\); no divergent Euler product is substituted for it. Altogether the \(X\)-dyad of \(Q(t)\) is bounded by
\[
 \ll (DH)^\epsilon M_2(W)^2 L
   \{X^\sigma H_b+ X L
          +X^\sigma H_b^{5/6}L^{1/3}
          +X^\sigma H_b^{1/3}L^{5/6}\}.
 \tag{6}
\]
Integrate only over \(U\le t<2D/X\) against \(dt/\log t\), using \(L=D/(tX)\). The \(H_b\)-term costs at most an extra logarithm and the others their values at \(D/(UX)\) times \(X^{-1}\) after dividing by \(D\). Summing the \(X\)-dyads proves (1). The separately retained \(a=b=1\) continuous term has absolute normalized bound \(O(B^2R_w\log(2D/U)/\log U)=O(B^2R_w)\) in the high window: use the exact \(f\) sum and bound its \(t\)-interval by \(2D/F\) for each \(f\). This does not replace the unordered rough-prime correction or the prime-error endpoint in the original identity.

## 4. Source-dependent fixed-field Mertens input and failed full step

Use only the strict \(7/8\) assertion for the fixed \(\zeta(s),L(s,\chi_{-3})\) of the September 30 preprint, with the exact commit, blob and file hash of GAP_NORM_STRIP_AND_PIT-v1, inherited in the pin receipt. It makes the fixed \(\zeta_K\) zero-free strictly to the right of \(7/8\), with its pole at \(1\) retained. The following interior reciprocal estimate spells out the extra step not given by the prime-counting deduction. Fix a sufficiently small \(\delta>0\). On the part of the zero-free strip at \(|t|\ge4\), take the analytic logarithm branch agreeing with the absolutely convergent branch at \(\Re s=2\), separately above and below the real axis. From polynomial growth of the two fixed \(L\)-functions in fixed strips (Euler series, functional equations and the three-lines bound), the real part of this logarithm is \(O_\delta(\log(2+|t|))\). Borel–Carathéodory on discs centered at \(2+it\), with radii lying in the zero-free strip and a fixed margin between the discs, gives the same bound on the full logarithm for \(\sigma\ge7/8+\delta/2\) up to \(2\). For \(\sigma\ge1+\delta/2\), absolute convergence bounds the log uniformly. To interpolate, center at a large \(t_0\), use the rectangle \(a=7/8+\delta/2,\ b=1+\delta/2,\ |t-t_0|\le |t_0|/2\), and apply the maximum modulus principle to the log multiplied by
\[
  \exp((s-it_0)^2)\,(\log(2+|t_0|))^{(s-b)/(b-a)} .
\]
The horizontal sides are exponentially small, both vertical sides uniformly bounded. At \(\sigma\ge7/8+\delta\) the resulting log bound is \(O_\delta((\log(2+|t|))^\gamma)\) for a fixed \(\gamma<1\). Thus \(|1/\zeta_K(s)|\ll_{\delta,\epsilon}(1+|t|)^\epsilon\) there; compact heights are harmless and the reciprocal has a zero at \(1\). The fixed \(S\) Euler factors are uniformly bounded in this region and do not produce zeros of their denominators there.

Apply finite Perron to \(1/\zeta_K^S\) on \(c=1+1/\log x_*\), with \(x_*=\lfloor x\rfloor+1/2\) and \(T=x_*^2\) for large \(x\). The coefficients grouped by integer norm are bounded by \(d(n)\), since the degree-two ideal-count coefficients are. The local Perron error is \(O_\epsilon(x_*^{1+\epsilon}T^{-1}\log x_*)\) by the half-integer harmonic sum; the remote error is \(O(x_*T^{-1}\log^2 x_*)\) using \(\sum d(n)n^{-c}=\zeta(c)^2\). Move to \(7/8+\delta\) using the interior reciprocal bound; there is no pole crossed. The vertical integral is \(O_{\delta,\epsilon}(x_*^{7/8+\delta}T^\epsilon\log(2T))\), and the two horizontals are \(O_{\delta,\epsilon}(x_*T^{-1+\epsilon})\). Choosing smaller parameters gives \(M_S(x)\ll_{S,\eta}x^{7/8+\eta}\) for every \(\eta>0\) under the pinned input. No zero is excluded at the boundary by this argument, no varying primitive conductor is introduced, and no source theorem is newly certified.

The exponent of the main monomial at \(Y=1\) is still \(19/24\), even with the source input. The gain in (1) comes from the actual long smooth-divisor tail; it does not estimate the small-\(F\) coherent term (in particular \(f=1\)), the annular \(K_0\) term, or their cancellation. Extending the short coefficient to \(K_0\) would be invalid. The independent auxiliary far-norm Gauss sector, the whole signed estimate, determinant and zero-location by scope, Lean and GRH remain open. Whole-prefix candidate \(109/144\), signed \(13/12\) and unsigned \(9/8\) are unchanged.
