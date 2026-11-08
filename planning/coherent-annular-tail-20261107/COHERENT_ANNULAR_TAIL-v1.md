# A signed full-divisor tail for the actual annular coefficient

7 November 2026 UTC. Author checked; independent review pending. This note gives a bound on the **large intermediate common-divisor part of the full signed Möbius inversion** for the original annular \(A\)–\(A\) form. It is not a high original-column-gcd estimate, a bound on the smooth \(K_0\) tail alone, or a bound on \(K_0-\mathcal J\). The power result takes the same pinned external fixed-field \(7/8\) statement as COHERENT_J_TAIL-v1, and does not independently certify that statement. Acceptance requires the exact annular coefficients, each prime allocation and literal cutoff, and the full deleted-prime and row/column mask bookkeeping.

## 1. Setup and result

Use exactly rma:core/sd:form: \(K=\mathbb Q(\omega)\), fixed \(S\) containing primes above \(2,3\), fixed \(\nu\), a single smooth complex \(W\) supported on \([1,2]\) and vanishing at the endpoints, \(U^2\le D\le7U^2/2\), and \(U\ge7\). Use the original unweighted two-pivot block with literal \(S\)-supported \(u_0\) fixed and physical good outside-\(S\) ideal \(v_1v_2^2\) of norm at most \(H_b\le H\) (phy:short); retain every original row restriction and raw zero. Both pivot ideals are good squarefree and coprime. Any fixed finite natural multiplicities are split into their literal classes. No weighted row extension is needed. Let \(M_2(W)\) be the maximum of the sup norms of its log-derivatives of order \(0,1,2\). For the raw coprime pairing \(S_1^{AA}\), write the normalized tail as
\[
 \mathscr T_{\ge Y}^{AA}
 =\frac1D\sum_{\substack{d\ \mathrm{good\ squarefree}\\Nd\ge Y}}\mu(d)
  \sum_{\substack{u\ \mathrm{actual}\\(d,u)=1}}
  \left|\sum_{\substack{a\ \mathrm{good\ squarefree}\\(a,d)=1}}
       A_U(da)\nu(a)\chi_a(u)W(Nd\,Na/D)\right|^2 .
 \tag{1}
\]
This is exactly the stated selection in the full divisor inversion for \(S_1^{AA}\). In particular it retains rough \(d\); selecting \(d\) smooth would be a different sum. The ideal \(d\) is an intermediate divisor of the pair of columns before Möbius cancellation. There is no assertion that the original column gcd is at least \(Y\).

Write \(M_S(x)=\sum_{Ne\le x,(e,S)=1}\mu(e)\), equal to zero below one. Suppose \(M_S(x)=O_S(x^\sigma)\) for fixed \(2/3<\sigma\le1\). Exponent \(1\) uses elementary ideal counting; \(\sigma=7/8+\eta\) for every \(\eta>0\) follows from the fixed-field interior reciprocal estimate and finite Perron in COHERENT_J_TAIL-v1 §4 conditional on the pinned September 30 theorem. No zero-location input from the original signed or determinant problem is assumed.

Define the two annular coefficient types \(\mu\) and \(G=\mu\tau_{>U}\), with \(\tau_{>U}\) the count of ordered ideal factorizations into two factors each of norm \(>U\). Let \(\mathscr T_{\ge Y}^{XY}\) be the analogous bilinear tail using types \(X,Y\) on its two sides; the second amplitude is conjugated, including \(W\). Give \(\mu\) one factor and \(G\) two, and let \(k=1,2,4\) be the product of the two numbers of factors. For \(1\le Y\le2D\) we prove
\[
 |\mathscr T_{\ge Y}^{XY}|
 \ll_{S,\sigma,\epsilon} (DH)^\epsilon M_2(W)^2
 \left[
 H_bY^{-(1-\sigma)/k}+\frac DY+
 H_b^{5/6}(D/Y)^{1/3}Y^{-(1-\sigma)/k}
 +H_b^{1/3}(D/Y)^{5/6}Y^{-(1-\sigma)/k}
 \right]. \tag{2}
\]
As usual the constants include the Mertens bound used and the fixed data. Terms at \(Y\ge2D\) are zero by the endpoint of the profile. This is a sufficient estimate, not a lower bound for the actual tail.

## 2. Exact annular factorization, before taking norms

For a good squarefree ideal \(m\) in the active annulus, \(Nm>U\). Begin with the unrestricted ordered disjoint divisor sum \(\sum_{xy\mid m,(x,y)=1}\mu(x)\mu(y)=\mu(m)\). For the part with \(Nx>U\), sum first over \(y\mid m/x\); the inner sum vanishes unless \(x=m\), so the result is \(\mu(m)\). The same holds for \(Ny>U\). If both exceed \(U\), the leftover norm is \(Nm/N(xy)< 2D/U^2\le7\), so the leftover ideal is the unit. The weight is then \(\mu(m)\) for each ordered pair. Inclusion–exclusion gives the exact annular identity
\[
 A_U(m)=\mu(m)(\tau_{>U}(m)-1)=G(m)-\mu(m). \tag{3}
\]
The strict inequalities at \(U\) are indispensable. The argument uses the original annulus and does not assert this identity outside the stated domain. It is a direct coefficient identity, independent of the previous pending Type-I/Type-II reductions for the finite Gauss prefix. In particular it does not replace \(A_U\) on the annulus by the short sign coefficient in the continuous \(\mathcal J\) argument.

Expand the bilinear tail into the four \(\mu,G\) pairings by (3). In a side of type \(G\) use its actual ordered factorization (and one factor for a side of type \(\mu\)). For squarefree \(d\) the two sides assign each of its primes to one factor on each side. Hence \(d\) splits uniquely into \(k\) pairwise coprime squarefree good cell ideals \(d_{ij}\), \(i,j\) the factor indices. The residual \(a\) splits into one or two actual labelled ideals \(a_i\), and likewise \(b=\prod b_j\). They are pairwise coprime within each side, and share no prime with \(d\). Overlap of \(a,b\) between the two sides remains allowed, as in the full divisor inversion. The \(\mu(d)\) outside survives; the two coefficient signs \(\mu(da)\mu(db)\) reduce to \(\mu(a)\mu(b)\), including the gap-labelled sides. The factors \(\nu(d)\) and the raw row phase at \(d\) cancel only on their live domain; the exact \((d,u)=1\) condition remains.

Partition the \(k\) cell norms into independent half-open dyads \([X_{ij},2X_{ij})\) with \(X_{ij}\ge1\); choose a largest dyadic length \(X\), breaking ties by cell index, not by a comparison of the actual cell ideals. There are logarithmically many boxes, and the active ones have product of lengths \(F\le2D\) and \(F>Y/2^k\). Freeze the other cells, let their product be \(d_0\) with \(F_0=Nd_0\), and write \(c\) for the largest cell. Then \(F_0X\asymp F\), \(X\ge F^{1/k}\), \(L=D/(F_0X)\), and the profile confines \(Na,Nb\) to \([L/2,2L]\), with \(L\ge1/2\) on nonempty support. The variable \(c\) has the exact range
\[
 \max(X,Y/F_0)\le Nc<2X,\qquad (c,Sd_0abu)=1,
\]
and its literal coefficient is \(\mu(c)\). All fixed masks on \(d_0\) remain. A gap side imposes two strict norm conditions on its factors: the factor not containing \(c\) has a fixed cutoff on its own residual labels, and the factor containing \(c\) imposes \(Nc>U/(F_a Na_i)\), where \(F_a\) is the product of the frozen cell norms in its factor. The other side has the analogous cutoff \(U/(F_b Nb_j)\). A \(\mu\) side has no such cutoff. Consequently the weight as a function of \(v=Nc\) is
\[
 W(F_0vNa/D)\overline{W(F_0vNb/D)}\,\mathbf1_{v>v_0},
\]
where \(v_0\) is the maximum of the present thresholds; omit the indicator when neither is present. This is a single jump, and the value at the jump is the left value (zero). It is not necessary to expand the original four short-divisor cutoffs or take a triangle over them.

## 3. Largest-cell Abel and the actual physical comparison

Use finite deletion relative to \(S_0=S\cup\operatorname{supp}(d_0)\). From the full prime-power convolution,
\[
 |M_{S_0}(x)|\ll (Nd_0)^\epsilon x^\sigma ,
\]
since \(\prod_{p\mid d_0}(1-(Np)^{-\sigma})^{-1}\ll_\epsilon (Nd_0)^\epsilon\) for fixed \(\sigma>0\): sufficiently large primes each contribute at most \((Np)^\epsilon\), the finitely many others only a constant. Now expand the remaining deletion against \(abu\), always outside \(S_0\), using the four signed placements in COHERENT_J_TAIL-v1 (2)–(3), assigning an entire prime power per prime. In the resulting term \(h=h_u h_a h_b h_{ab}\), use \(r_u=\operatorname{rad}(h_u)\), \(r_a=\operatorname{rad}(h_a h_{ab})\) and \(r_b=\operatorname{rad}(h_b h_{ab})\). The row must contain \(r_u\), avoid the other assigned primes and still respect the original masks; the columns satisfy \(r_a\mid a,\ r_b\mid b\). In particular no primitive extension restores a prime at which the raw character vanishes.

Apply the half-open Abel identity of that note with endpoints \(\max(X,Y/F_0),\,2X\), prefix \(M_{S_0}(v/Nh)\) and the exact left-value cutoff above. The outer endpoints use strict prefixes. A jump at the left endpoint is included with the closed prefix; a jump at the right endpoint is absent. Both the smooth derivative terms and the endpoints factor on the two sides with prefix bound \(O((Nd_0)^\epsilon(X/Nh)^\sigma)\) when nonzero. If there are two thresholds, split into the two exact orderings, assigning equality to one, so the jump is counted once. The comparison is between the integer values \(F_aNa_i\) and \(F_bNb_j\) and separates by the same finite cyclic one-sided Fourier comparator as before (logarithmic mass). At the jump \(v=U/(F_aNa_i)\), its prefix and interval membership belong to the first side, the first profile depends only on \(a\) and its labels, and the second is
\(\overline{W((UF_0/(DF_a))(Nb/Na_i))}\).
Separate the latter by the Mellin transform on the purely imaginary line. Its absolute integral is \(O(M_2(W))\) by integration by parts twice in log-coordinate, and the positive constant \(UF_0/(DF_a)\) enters only in a unitary phase. The other orientation is identical with the sides interchanged. Consequently the jump preserves the same \(M_2(W)^2\) profile factor and the same prefix bound, apart from logarithmic Fourier mass. Norm-tied residual ideals are not identified.

After separation, group the labels into the actual residual coefficient on \(a\) or \(b\). Each ideal has divisor-bounded multiplicity; the pointwise coefficient before its profile or prefix scale is \(O(D^\epsilon)\). The two squared coefficient masses have the factors \(O(L/Nr_a)\) and \(O(L/Nr_b)\), respectively. For \(Nr_a>2L\) or \(Nr_b>2L\) the corresponding side is empty; subunit counting lengths in \([1/2,1)\) can contribute only the unit and fit the displayed upper count up to constants. Use actual annular residual lengths \(\max(1,2L)\le C L\), not an operator at subunit length.

To use the physical row norm, on rows containing \(r_u\) freeze its prime valuations (1 or 2 in the actual physical ideal). This gives at most \(2^{\omega(r_u)}\) assignments and a fixed raw character multiplier at the frozen factor. The remaining sixth-free physical ideal has length at most \(H_b/Nr_u\) and determines the row for each fixed assignment. Empty subunit row ranges contribute zero. Enlarge other row restrictions only inside the positive operator norms. The two fixed-\(h\) coefficient vectors then use the same inherited unweighted \(\Phi_6(H_b/Nr_u,CL)\) from phy:input, via the literal family identification, followed by Cauchy in the actual rows. This repeats the legitimate sieve setup of the continuous tail on the new separated annular amplitudes; no arbitrary row weights enter. The joint budget before the placement triangle is
\[
 (DH)^\epsilon M_2(W)^2\,
 \frac{X^\sigma L}{(Nh)^\sigma\sqrt{Nr_a Nr_b}}\,
 2^{\omega(r_u)}\Phi_6(H_b/Nr_u,CL).
\]
All row-independent cutoff masks, phase weights and factor labels were retained before this bound.

Now sum the placements as in the continuous tail: the \(h_a,h_b,h_{ab}\) local exponents gain at least \(1/2\) from the column masses; three physical monomials gain at least \(1/3\) from \(r_u\); their Euler sums converge for \(\sigma>2/3\). The \(L\) monomial has no \(r_u\) gain, so use only \(Nh_u\le2X\) and ideal counting, giving \(X^{1-\sigma+\epsilon}\), including the logarithmic endpoint. No divergent Euler product is inserted. Thus for the largest cell at fixed frozen cells, division by \(D\) gives the bound
\[
 \ll (DH)^\epsilon M_2(W)^2\frac1{F_0}
   \left\{X^{\sigma-1}\bigl[H_b+H_b^{5/6}L^{1/3}
                                  +H_b^{1/3}L^{5/6}\bigr]+L\right\}.
\]
The harmonic sum of \(1/F_0\) over frozen ideals in their own dyads is bounded by a constant depending only on \(k,K\), by ideal counting; their coprimality can be relaxed for this upper sum after the signed argument. Use \(L\ll D/F\), \(X\ge F^{1/k}\), \(F>Y/2^k\) and the logarithmically many boxes to obtain (2).

## 4. Critical powers and what has not been transferred

At \(H=D^{3/4}\), with the conditional exponent \(7/8\) (use \(7/8+\eta\) and absorb the smaller \(\eta\) into the stated subpower), put \(Y=D^y\). The dominant physical monomial has exponent \(23/24-(1/3+1/(8k))y\). Its sufficient thresholds are \(5/11\) for \(\mu\)–\(\mu\), \(10/19\) for either mixed gap pair, and \(4/7\) for \(G\)–\(G\). All other monomials are at most \(3/4\) at these thresholds. Hence by the exact annular expansion the full tail (1) is target-sized at \(Y=D^{4/7}\). At \(Y=D^{3/5}\), the four upper powers for the worst \(k=4\) case are \(117/160,\ 2/5,\ 71/96,\ 271/480\), yielding \(D^{71/96+\epsilon}\), a \(1/96\) margin. With only \(\sigma=1\), the corresponding sufficient cutoff is \(D^{5/8}\); it is not a new power gain without the external input.

This is an actual signed **tail**, but it has not estimated small \(d\) or \(d=1\). The largest cell in a box with unit components gives no cancellation at unit scale. Nor can (2) be read as a smooth-\(f\) bound on \(K_0\): the argument uses the full Mertens prefix for the moving cell, including rough primes. Forcing smoothness there would replace it by a different prefix with no such fixed power justified; subtracting the rough terms requires their own coupling to the continuous term and the unit correction. The previous continuous large-\(F\) bound remains separate. Coherent \(K_0-\mathcal J\), the far-norm Gauss sector, full signed pairing, short/principal assembly and the independent determinant/zero-location problems remain open. No new zero-free theorem, Lean result or GRH conclusion is claimed; candidate \(109/144\), whole signed \(13/12\) and global unsigned \(9/8\) are unchanged.
