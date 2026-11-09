# Rational content in actual selected partner frequencies

9 November 2026 UTC. This note uses the original pure, unweighted, nonprincipal two-pivot rows at \(A_1\asymp R\asymp D^{3/4}\), \(A_2\asymp1\), with fixed \(S,\nu,u_0\), \(U^2\le D\le7U^2/2\), primitive \(Q_u\asymp R\), and one common smooth complex \(W\) supported on \([1,2]\). Keep the actual wide unit-pair Poisson representation, including its re-expressed direct component, all row and cutoff masks, and the separately selected original middle equality subtraction. The additional frequency selector may depend on \(\mathfrak k\) and the fixed partner labels of SELECTED_LOW_FREQUENCIES-v2. It is independent of the varying ordered cutoff ideals and the varying equality labels. All comparisons here are for that selected correction.

Let \(c(\mathfrak k)\) be the largest positive rational integer, prime to the rational primes below \(S\), with \((c(\mathfrak k))\mid\mathfrak k\). The selection \(c(\mathfrak k)\ge B\) leaves the frequencies as actual integral ideals, including nonsquarefree ideals, repeated norms, and ideals meeting \(S\). A large rational factor can give sparsity even when the sixth-power part is the unit. The result concerns the rational content of the Poisson frequency itself, which is a different variable from the primal cutoff content or the reduced comparable residual content.

For \(B=D^b\), \(0\le b\le9/28\), the selected normalized cross meets \(O((DH)^\epsilon\mathcal M_{24}(W)^2D^{3/4})\) over all intermediate divisors through
\[
 N\mathfrak k\lesssim D^{9/20+3b/5}.
\]
In particular \(B\asymp D^{7/24}\) permits \(N\mathfrak k\lesssim D^{5/8}\) over all \(d\). For \(Nd\gtrsim D^{1/8}\) the same frequency cap holds with \(B\asymp D^{5/24}\), or with \(B\asymp D^{17/96}\) in the interval \(D^{1/8}\lesssim Nd\lesssim D^{1/4}\). For \(Nd\gtrsim D^{1/4}\), \(B\asymp D^{41/144}\) permits \(N\mathfrak k\lesssim D^{2/3}\). Fixed factors in the dyadic scales are allowed. Empty cells contribute zero.

## Sparse moment with the sixth-power part retained

At one frequency dyad \(T\le N\mathfrak k<2T\), let \(Z_u=\sum_{\mathfrak k} a(\mathfrak k)\overline{\psi_u(\mathfrak k)}\) be the separated frequency array of SELECTED_LOW_FREQUENCIES-v2, including the optional selector. Normalize \([F]_p=R^{-1/p}\|F\|_{\ell^p}\). All bounded coefficients here are row independent at fixed second pivot and Fourier parameters. Support on \(c(\mathfrak k)\ge B\) has \(O(T/B)\) ideals, by summing the ideal count for \(N\mathfrak k/c(\mathfrak k)^2\) over \(c(\mathfrak k)\ge B\). This is the elementary count used in RATIONAL_CONTENT_DUAL-v2. An endpoint with \(B>\sqrt{2T}\) is empty.

For \(j=1,2\), form the actual \(Z^j\) before estimating its squared norm. Group by the product \(J\) of the \(j\) ideals. The grouped coefficients \(\beta(J)\) are divisor bounded and supported in \(NJ\ll T^j\). By Cauchy over each actual product fibre, followed by the ordered tuple count, the total squared mass is \(O((DH)^\epsilon (T/B)^j)\) when \(T\) is in the polynomial range of this note. This preserves actual coefficients through the grouping, including their complex signs. In particular \(T^j/B^j\) is a mass bound for the grouped product, rather than an assertion that \(J\) has a sparse sixth-free residual on every fibre.

Write \(J=\mathfrak s q^6 v\) uniquely, with \(\mathfrak s\) its entire \(S\)-supported part, \(q\) good and \(v\) good sixth-free. Fixed \(\mathfrak s,q\) retain \(\overline{\psi_u(\mathfrak s q^6)}\) as an exact row multiplier, even if \(q\) and \(v\) meet or the row vanishes there. The positive sixth-free sieve on \(v\) at fixed second pivot has normalized squared cost \(\ll(DH)^\epsilon\Phi_6(A_1,\max(1,T^j/(N\mathfrak s(Nq)^6)))/A_1\) times the squared coefficient mass. This is the same physical comparison as DUAL_CUTOFF_PRODUCT-v1. Conjugation does not change the row norm. Fixed \(S\) allows only polylogarithmically many \(\mathfrak s\) up to this polynomial cap.

For \(Q\le Nq<2Q\) take the row norm triangle over \(q\) only after forming the product coefficients. Cauchy over \(O(Q)\) labels and the disjoint sparse squared masses give \(T^{j/2}Q^{1/2}B^{-j/2}\). Alternatively each fibre has squared mass \(O((DH)^\epsilon T^j/(N\mathfrak s (Nq)^6))\), by the ideal count and divisor bound. Summing square roots gives \(O((DH)^\epsilon T^{j/2}Q^{-2})\). A nonempty fibre has \(T^j/(N\mathfrak s(Nq)^6)\gg1\); this includes its unit at constant scale. Both estimates retain the common sieve cost at length \(\max(1,T^j/Q^6)\) by monotonicity. The latter cost may be strictly smaller than at \(T^j\).

Put \(t=\log_D T\), \(b=\log_D B\) and
\[
 \Delta(v)=\max(0,v-3/4,v/3-1/8,5v/6-1/2).
\]
After taking the \(j\)-th root, the bound per dyad, relative to \(\sqrt T\), has power at most
\[
 \min(x/2-b/2,-2x)+\frac{\Delta(j(t-6x)_+)}{2j},
 \qquad x=\log_D Q/j .
\]
For \(0\le x\le b/5\) the first branch is affine and the rest is convex, so the maximum is at an endpoint. For \(x\ge b/5\) the second branch and the sieve term are both nonincreasing. Extending to these full intervals only enlarges the comparison. Thus after dyadic summation
\[
 [Z]_{2j}\ll(DH)^\epsilon\sqrt T\,D^{\lambda_j(t,b)},\qquad
 \lambda_j(t,b)=\max\left\{
 \frac{\Delta(jt)}{2j}-\frac b2,\
 \frac{\Delta(j(t-6b/5)_+)}{2j}-\frac{2b}{5}
 \right\}. \tag{1}
\]
The two branches are essential to the general argument. At some large-content thresholds the shortened sieve length makes the second branch smaller than the first, recovering the full square root of the sparse support fraction there. Removing all shortening first only gives a uniform gain \(B^{-2/5}\).

## Transfer to the original selected correction

Use the exact log separation and partner arrays of SELECTED_LOW_FREQUENCIES-v2 with actual live cap \(14L_i\). Insert (1) in the original row pairing of SELECTED_MOMENT_SYNTHESIS-v1. The sparse selector is a legal independent frequency multiplier. The original signs, common-prime factor \(w\), Gauss root, \(S\)-part, actual \(Q_u\), direct component and all original restrictions remain. Only the positive frequency norms change. The conjugation in the row pairing stays exact. The original elementary compensation comparison still costs \(R/E\) per divisor up to profile and subpower factors, since it accepts every bounded selector of the stated kind.

Write \(E=Nd\), \(e=\log_D E\). The following are upper powers over \(R/E\) in three divisor ranges:
\[
 \begin{array}{ll}
 0\le e\le1/8:&t/2-13/48+\lambda_1/3+2\lambda_2/3,\\
 1/8\le e\le1/4:&t/2-9/32+5\lambda_1/6+\lambda_2/6,\\
 e\ge1/4:&t/2-11/32+\lambda_2 .
 \end{array} \tag{2}
\]
For the first line use equality moment index three, both cutoff fourth moments and interpolate the frequency between its second and fourth moments. The omitted exact divisor term is \(-e/6\). For the second line use equality moment index twelve. The cutoff bound \(13/96-e/6\), equality factor \(-\tau/2+\Delta_3(12\tau)/24\), \(\tau=(1/4-e)/2\), give a convex piecewise affine function of \(e\) with equal endpoint values after adding \(-3/8\). Its maximum is \(-9/32\). For the third line use the equality supremum, longer cutoff second moment and shorter cutoff fourth moment of SELECTED_LOW_FREQUENCIES-v2. Their cutoff excess is at most \(1/32\), and the equality divisor decay can be discarded. For every line the masses still give the harmonic \(R/E\) cost, and the actual squared frequency estimates carry the original normalizations.

For the all-divisor line take \(t_0=9/20+3b/5\), so \(9/20\le t_0\le9/14<3/4\) and \(b=5t_0/3-3/4\). At \(t_0\) the first branch of (1) dominates for both \(j\). Indeed if the shortened argument stays at least \(3/8\), the slope of \(\Delta\) there is at least \(1/3\), so the drop in its contribution is at least \(b/5\). If it crosses below \(3/8\), the loss equals the entire initial contribution, at least \(\Delta(t_0)/2=t_0/6-1/16\), which exceeds \(b/10\) by \(1/80\). These suffice to absorb the difference \(b/10\) in the two sparse powers. For this range \(\Delta(t_0)=t_0/3-1/8\) and \(\Delta(2t_0)=5t_0/3-1/2\). The first line of (2) is \(5t_0/6-3/8-b/2=0\); the other two lines are smaller since their differences from the first are \(-t_0/8+1/48\) and \(t_0/12-3/32\). Every line is nondecreasing in \(t\) and nonincreasing in \(b\). The other stated endpoint pairs follow by substituting their rational values directly in (1) and (2).



## Arbitrary frequency heights with large sixth-power or \(S\)-parts

A second selection reaches all frequency heights. Define \(q(\mathfrak k)\) by removing the entire \(S\)-supported part \(\mathfrak s(\mathfrak k)\) and dividing the good valuations by six with remainder. With the same exact pairing and compensation, target size holds across all \(d\) for either
\[
 Nq(\mathfrak k)\gtrsim D^{1/16}\quad\text{or}\quad
 N\mathfrak s(\mathfrak k)\gtrsim D^{3/10}.
\]
The union follows by taking the first selector and the part of the second outside the first. There is no requirement on the rational content of these frequencies. The claim is only for the actual subsets with the stated parts, and keeps the original profile decay for the infinite dyadic tail.

If \(Nq(\mathfrak k)\ge Q_0\) in each input, then \(q(J)\) is divisible by the product of the \(j\) input \(q\)'s, by the superadditivity of the integer floor of the good valuation divided by six. If \(N\mathfrak s(\mathfrak k)\ge S_0\), the \(S\)-part multiplies exactly. In the positive norm of \(Z^j\) take the generic per-fibre square-root mass \(O((DHT)^\epsilon T^{j/2}(N\mathfrak s)^{-1/2}(Nq)^{-3})\). Summing over \(Nq\ge Q_0^j\) gives \(O(Q_0^{-2j})\) by the ideal count and the dyadic series. Summing \(S\)-parts has finite weight \(\sum_{\mathfrak s}(N\mathfrak s)^{-1/2}\). With the \(S\)-part threshold instead, use the same sum restricted to \(N\mathfrak s\ge S_0^j\), bounded by \(O_{S,\epsilon}(S_0^{-j/2+j\epsilon})\) by the convergent \(S\)-Euler product at exponent \(\epsilon>0\). The \(q\)-sum is convergent in that case. The sieve on the sixth-free residual retains the shortened length after either deletion, and live subunit lengths cost the unit-scale bound. For \(Q_0=D^a\) or \(S_0=D^s\), the replacement frequency exponents in (2) are respectively
\[
 \lambda_j^{(6)}(t,a)=-2a+\frac{\Delta(j(t-6a)_+)}{2j},\qquad
 \lambda_j^{(S)}(t,s)=-s/2+\frac{\Delta(j(t-s)_+)}{2j}.
 \tag{3}
\]
Constants and subpowers include fixed lower comparability constants in the thresholds. All phases and zeros of the grouped \(S\)- and sixth-power factors remain in their actual fibres. This is a sparsity argument on the chosen frequency subset.

At \(t=3/4,a=1/16\), the two sixth-power exponents in (3) are \(-1/8,-3/32\). The three excesses in (2) are \(0,-5/192,-1/16\). At \(t=3/4,s=3/10\), (3) yields the same excesses as the unmodified frequency exponents evaluated at \(t-s=9/20\), because \(-s/2\) combines with \(t/2\). All three are nonpositive. Monotonicity gives each smaller frequency dyad. Above \(R\) the positive exponents in (2) grow with slope at most one in \(t\) since \(\Delta\) has slope at most one. The unchanged \((1+T/R)^{-4}\) then gives a convergent geometric sum, including the \(T^\epsilon\) losses by taking the internal epsilon small. The original compensation was already controlled for arbitrary bounded selectors of this kind.

The main scale with small \(S\)- and sixth-power parts and small rational content remains outside these estimates. In particular, the rational-content-only bound (1) has all-divisor excess \(1/16\) at \(t=3/4,b=3/8\), even at that maximal content exponent. The excess is a limitation of this positive estimate and has no lower-bound interpretation.
