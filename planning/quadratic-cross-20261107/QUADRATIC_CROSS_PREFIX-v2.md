# Quadratic cross terms in the short-factor frequency norm

Author draft v2, 7 November 2026 UTC. V1 is preserved. V2 balances the two finite comparisons at fixed actual k before summing and keeps a stronger mixed capacity factor. Independent review is pending. This note derives a new operator comparison by Poisson summation in the long variable of the dual Gram form. The two kinds of prime in the literal \(rp^4\) yield two quadratic matrices after the common primes are removed. Their norms replace the ordinary conductor-square loss near the previous transition.

## 1. The two-colour operator estimate

Work over \(\mathcal O=\mathbb Z[\omega]\), with the same fixed \(S\) containing the primes over \(2,3\). For good squarefree \(a,b\) with \((a,b)=1\), and good squarefree \(v\), put \(K_{a,b;v}=\overline{R_v(ab^4)}\). Let \(Na\in[A,2A)\), \(Nb\in[B,2B)\), and \(Nv\in[T,2T)\), with \(A,B,T\ge1\). The claim for arbitrary coefficients on \(v\) is
\[
 \|K\|_{\rm op}^{\,2}\ll_{S,\varepsilon}
 (ABT)^\varepsilon\big[T+AB(A+B)\big]. \tag{1}
\]
Any restriction on the pair label \((a,b)\) can be made by taking a submatrix. All raw zeros are part of the matrix.

Write \((\alpha/u)_6\) for the literal product of local sextic symbols for a squarefree good ideal \(u\). The fixed-class sextic reciprocity used in wc:literal-reciprocity and phy:family identifies \(R_v(a)R_v(b)^4\), on coprime arguments, with
\[
 \theta_{a,b}(\alpha_v)=(\alpha_v/a)_6(\alpha_v/b)_6^4
\]
times a fixed finite-class factor. Both sides vanish on \((v,ab)>1\). This comparison is applied separately to the two squarefree factors. In the duality proof partition the rows by the fixed reciprocity classes of \(a,b\). On each part the comparison factor is a column diagonal of modulus one. Complex conjugation does not change the matrix norm, so it suffices to handle \(\theta\). The finitely many comparisons cost a fixed constant. At this point the column coordinates are a subset of the primary lattice representatives \(\alpha_v\). No change to an original primitive \(S\) value has been made. The auxiliary \(\theta_{a,b}\) is a residue character on elements, primitive modulo \(ab\), with local powers \(1,4\) at its good primes. It need not be unit-trivial on the full lattice.

For dual coefficients \(\lambda_{a,b}\), enlarge the positive column sum to all lattice elements with the Gaussian majorant \(e^2 e^{-N\alpha/T}\), which is at least one on the original column annulus. Open this smooth dual Gram form. Its diagonal is \(\ll T\sum|\lambda_{a,b}|^2\) by lattice counting, including the unit and zero conventions. For the remaining pairs use the exact four pairwise-coprime common ideals
\[
 g_{11}=(a_1,a_2),\quad g_{14}=(a_1,b_2),\quad
 g_{41}=(b_1,a_2),\quad g_{44}=(b_1,b_2).
\]
Put \(c=g_{11}g_{44}\), \(j=g_{14}g_{41}\), and \(g=cj\). Write
\[
 \begin{aligned}
 a_1&=g_{11}g_{14}a'_1,& b_1&=g_{41}g_{44}b'_1,\\
 a_2&=g_{11}g_{41}a'_2,& b_2&=g_{14}g_{44}b'_2,\qquad
 q_i=a'_i b'_i .
 \end{aligned}
\]
Here \(q_1,q_2,g\) are pairwise coprime. The product of the two element characters is
\[
 \theta_{a_1,b_1}(\alpha)\overline{\theta_{a_2,b_2}(\alpha)}
 =\mathbf1_{(\alpha,c)=1}\,
       \theta_{a'_1,b'_1}(\alpha)
       \overline{\theta_{a'_2,b'_2}(\alpha)}
       (\alpha/j)_6^3 . \tag{2}
\]
At \(c\) the local exponents agree and the raw zero remains. At \(j\) their difference is \(3\) or \(-3\), giving the same nontrivial quadratic character and its own zero. Thus \(F_0=q_1q_2j\) is the primitive element modulus in (2) after the \(c\) mask. The modulus \(F_0\) is a nonunit except on the diagonal already counted. Opposite-colour primes do not disappear from the conductor.

For each \(e\mid c\), expand the \(c\) mask by \(\mu(e)\) and put \(\alpha=\alpha_e x\). The primitive character of (2) on \(x\) has the same modulus \(F_0\), and the factor at \(\alpha_e\) separates into the two residual row factors and the fixed \(j\) value. The Gaussian scale is \(T/Ne\). The finite Fourier and Gaussian Poisson identities from cbk:finite-Fourier and cbk:gaussian-proof, applied here to this primitive residue character on elements, give a sum over \(\beta\in\mathcal O\) of the conjugate primitive character at \(\beta\) times
\[
 C_{\mathcal O}\frac{T}{Ne\sqrt{NF_0}}\,
 \frac{\tau_{F_0}}{\sqrt{NF_0}}\,
       \exp\!\left(-C'_{\mathcal O}\frac{T N\beta}{Ne\,NF_0}\right).
 \tag{3}
\]
The exact fixed positive constants depend only on the Gaussian and lattice convention. The inverse different is retained in the finite additive pairing. The zero frequency vanishes by primitivity. At all nonunit frequencies the finite Fourier identity gives the raw zero. The product generators in (3) are the multiplicative primary ones.

In \(\tau_{F_0}/\sqrt{NF_0}\), CRT separates the local Gauss factors on \(q_1,q_2,j\), each of modulus one. The crosses involving \(j\) are products of one factor on each row. Only the remaining cross
\[
 \theta_{a'_1,b'_1}(\alpha_{q_2})
       \overline{\theta_{a'_2,b'_2}(\alpha_{q_1})} \tag{4}
\]
couples the two residual rows. Fix the four residual reciprocity classes, or take their finitely many component pairs. On the coprime support the same-colour edges in (4) are finite-class scalars. At the edge \((a'_1,b'_2)\), the two powers in (4) are \(1,-4\), and their sum modulo six is \(3\). At the edge \((b'_1,a'_2)\) they are \(4,-1\), with the same sum. Thus (4) equals a fixed unit scalar times
\[
 (\alpha_{b'_2}/a'_1)_6^3\,(\alpha_{a'_2}/b'_1)_6^3 . \tag{5}
\]
Either reciprocal direction of each quadratic factor can be used after accounting for its finite-class scalar. This is the place where the actual fourth power in \(ab^4\) is essential.

The product (5) automatically supplies the cross-colour zeros. The two remaining exact coprimality indicators, for \((a'_1,a'_2)=1\) and \((b'_1,b'_2)=1\), must still be inserted. Expand them with \(\mu(x)\) and \(\mu(z)\) respectively and divide the corresponding two residual factors by \(x\) and \(z\). For each \(x,z\), the within-row disjointness and the masks against \(g\) are row selectors. In particular \((x,z)=1\) whenever either row coefficient survives. Multiplicativity of primary generators and quadratic symbols on each cross edge gives the quadratic symbols between the shortened factors and fixed \(x,z\) phases with their raw zeros. For instance
\[
 (\alpha_{z B_2}/(x A_1))_6^3
 =(\alpha_z/x)_6^3
  (\alpha_{B_2}/x)_6^3
  (\alpha_z/A_1)_6^3
  (\alpha_{B_2}/A_1)_6^3 .
\]
Here \(a'_i=x A_i\), \(b'_i=z B_i\) with the individual squarefree factorizations. Each equality includes zeros at a cross collision. All factors other than the last are fixed or one-row diagonals. This is a separable extension for the Möbius identity. It does not assert a CRT Gauss identity for an overlapping pair. The two Möbius expansions retain cancellation of every disallowed same-colour overlap.

We now have, for each fixed \(g_{ij},e,\beta,x,z\), a bilinear form on two arrays indexed by \((A_1,B_1)\) and \((A_2,B_2)\), with kernel the product of two independent quadratic matrices on the crossed indices. The permutation of the second array indices is isometric. The norm of their tensor product is the product of their norms. By the pinned Goldmakher–Louvel Corollary 1.2 at \(n=6\), as transferred to literal quadratic symbols in qp:details, each matrix has norm \(\ll (AB)^\varepsilon (A+B)^{1/2}\). The actual residual squarefree ideal lengths are at most the original \(2A,2B\), including the unit. Arbitrary pair-dependent coefficients on either side are allowed. Bounds on these kernels use the true quadratic symbol matrices rather than an independence model.

Here is the separation and summation of (3). For fixed \(g_{ij},e\) write \(Q=AB\) and \(Y=Q^2 Ne/(T (Nc)^2 Nj)\). Then \(Nq_i\asymp Q/Ng\) and \(T/(Ne\sqrt{NF_0})\ll T Nc\sqrt{Nj}/(Ne Q)\), with the two normalized norm factors in the prefactor separated. The exponential depends on the sum of the logarithms of \(Nq_i/(Q/Ng)\) and on \(N\beta/Y\). On their fixed compact log interval, extend the resulting one-variable function with a fixed smooth cutoff. Fourier inversion and two integrations by parts give Fourier \(L^1\) mass \(\ll_M (1+N\beta/Y)^{-M}\) for every fixed \(M\). The Fourier phases in the two row arrays have modulus one. For \(M>2\), lattice counting gives
\(\sum_{\beta\ne0}(1+N\beta/Y)^{-M}\ll Y\) for all \(Y>0\), with the bound \(\ll Y^M\) when \(Y<1\). Hence the prefactor times the frequency majorant is \(\ll Q/(Nc\sqrt{Nj})\le Q\). The subunit dual length has been covered without inventing a zero-frequency term.

The remaining sum over fixed common-prime data costs a divisor loss, by Cauchy in the products of the two restricted coefficient norms. Each individual original row \((a_1,b_1)\) can occur only for \(g_{11}g_{14}\mid a_1,\ g_{41}g_{44}\mid b_1\), \(e\mid c,\ x\mid a'_1,\ z\mid b'_1\), with bounded finite-class multiplicity. This is \(\ll (AB)^\varepsilon\) possible labels by the divisor bound. The same count on the right uses \(g_{11}g_{41}\mid a_2,\ g_{14}g_{44}\mid b_2\) and the right divisors. The unit diagonal exclusion is also compatible with this summation. Indeed \(F_0=1\) forces \(j=1,q_1=q_2=1\), which can be separated by restricting each side to its unit or nonunit residual support and omitting the both-unit case for \(j=1\). No diagonal primitive nonzero-frequency calculation is needed. Together with the diagonal \(O(T)\) estimate this proves (1).

## 2. All sixth-free \(r\), with the original short zero

Use the actual joint Type-I setup in cbk:exact-kernel, rg:hb-proof, rg:matrix-proof and accepted mixed6456d737 with 6fed549f and 7d62d6c9. In an actual small-divisor shift \(m=da\), write \(a=pv\) in an unbalanced box, \(E=Nd\), \(L=D/E\), \(T\asymp L/P\). Fix the original \(h,s,k,\ell,e,v_2\) and source component. As in the original shifted identity, the short coefficient contains \(\overline{R_p(r)}\), so \(p,r\) are coprime on its live support. The long factor is
\[
 \chi_{3,v}(\alpha_p)\overline{R_v(r)}=\overline{R_v(rp^4)}.
\]
The equality includes both long raw zeros. The fixed \(\chi_{3,v}(\alpha_{dk})\) is a bounded long diagonal, including its original zero. The original short \(p,r\) zero is applied before Cauchy in the short vector, which has squared mass \(\ll(DH)^\varepsilon\). All fixed masks and the original primitive \(S\) scalar at \(r\) are kept. Exact Mellin separation of \(W(NpNv/L)\) costs \(M=\mathcal M(W)\) once in each unsquared column norm. In the remaining positive norm the long vector is independent of \(r,p\), so comparison (1) applies to the appropriate live pair subset.

For general sixth-free \(r\), write \(r=a u\) where \(a\) has the valuation-one primes and \(u\) the valuations \(2,\ldots,5\). Thus \(u\) is squarefull and \((a,u)=1\). Work on \(R\le Nr<2R\), \(C\le Nu<2C\), with \(C\ge1\) and clipped original bands. There are \(O(C^{1/2})\) possibilities for \(u\). Indeed \(u=d_0^2 d_1^3\) with squarefree \(d_1\) obtained from its odd valuations, and \(\sum_{d_1}(Nd_1)^{-3/2}<\infty\). For each \(u\), its entire raw phase \(R_v(u)\) is a fixed long-column diagonal. Apply (1) with \(Na\asymp R/C,\ Np\asymp P\), counting the unit directly at subunit dyadic endpoints. The resulting squared operator budget on this \(C\)-band is
\[
 (RPT)^\varepsilon\left[C^{1/2}T+
             \frac{RP}{C^{1/2}}(R/C+P)\right]. \tag{6}
\]
The ordinary all-primitive comparison gives another budget on the same actual pairs. Their good conductor is \(\operatorname{rad}(r)p\) with norm \(\ll RP/C^{1/2}\), since \(N\operatorname{rad}(u)\le (Nu)^{1/2}\). At most \(6^{\omega(q)}\) literal \(r,p\) pairs have good conductor \(q\), by the five valuation choices for a prime of \(r\) or its assignment to \(p\). Primitive extension on good \(v\) keeps the \(rp\) zeros because every live valuation of \(rp^4\) is in \(1,\ldots,5\). Thus the all-primitive bound is \(\ll (RPT)^\varepsilon[T+(RP)^2/C]\). This use of the conductor does not replace the physical radicand in an order-six sieve.

If \((RP)^2<T\), the ordinary bound is already \(O(T)\). Otherwise split at \(C_0=((RP)^2/T)^{2/3}\). For \(C\le C_0\) use (6), and for \(C>C_0\) use the ordinary estimate. Both \(C^{1/2}T\) on its side and \((RP)^2/C\) on its side are at most \((RPT)^{2/3}\). Summing the logarithmically many \(C\)-bands gives the new Type-I squared mean over the **actual** \(r\) band, for each shifted column,
\[
 \ll M^2(DH)^\varepsilon E^{-1}
        [L/P+RP(R+P)+(RL)^{2/3}]. \tag{Q}
\]
No squarefree restriction on \(r\) has been inserted. At the previous transition \(E=1,\ R\asymp P\asymp D^{1/4}\), this budget costs \(D^{5/6+\varepsilon}\) in that box, whereas the ordinary comparison permitted \(D^{1+\varepsilon}\).

## 3. Finite-prefix consequence and the new short-factor obstruction

The projection is the original normalized nonprincipal unweighted two-pivot \(P(X)\) of accepted mixed formula (2), with \(D\ge2^{64}\), \(1\le H\le D^{3/4}\), \(1\le U\le\sqrt D\), and \(1\le X\le D^{3/8}\). The original capacity \(Nu_0 A_1 A_2^2\le H\), all exact masks, one common \(W\), actual \(A_U\), and \(Ny\le X\) for \(y=hrs^6\) remain. The other four good factors are units. The actual \(k\) range is finite, pre-\(S\), and satisfies \((k,v_2)=1\), \(Nk\le\sqrt{b(v_2)/N\ell}\). The primitive \(\eta(e),\eta(h)\), finite source/ray factors, all phases including \(\bar\rho(s)^6\), and both \(s\) column exclusions are retained. Keep the leading replacement \(\dot G\mapsto g_0(v_2)\) and estimate its explicit error at the end.

Before a norm, insert the exact \(\sum_{d\mid m,n}\mu(d)\) into the separated leading form. Use the two distinct actual shifted columns at \(m=da,n=db\), each residual squarefree and coprime to \(d\). The residuals may overlap each other in the auxiliary product. The transported \(B_U=\mu A_U\) coefficients are the disjoint allocations \(d_1d_2d_3=d\), with cutoffs \(Na_i\le U/Nd_i\) for \(i=1,2\), and sign \(\mu(d_3)\mu(a_3)\) on the third factor. This follows from the original three-factor coefficient identity. Subunit own cutoffs give zero, equality includes the unit. The Gauss CRT cross shifts the cubic numerator to \(dk\) and its original collision zero stays. Use the established eleven-label partition at \(L=D/E\) for \(E\le D^{1/16}\). Its balanced boxes cost squared mean \(\ll M^2(DH)^\varepsilon E^{-1} R L^{2/3}\). Its genuine unbalanced coefficient-one long variable has \(P\ll L^{1/3}\), since the long scale exceeds \((L/2^{11})^{2/3}>\sqrt D\) and thus cannot be one of the restricted factors. Both shifted orientations use whole conjugation of their respective profiles and phase factors.

For small \(P\) use the inherited sharp long row, including its all-level trivial fallback, with the explicit growing \(Q_\gamma=N\operatorname{rad}(rv_2)\ll A_2 R\), numerator \(dpk\), and full deletion against \(\operatorname{rad}(dpksrv_2)\) with \(\ell\mid v_2\). The literal raw deletion scalar and subunit endpoint rules are as in rg:deletion-identity. After short counting and summing over the clipped \(r\)-band its squared mean is
\[
 \ll V_1(W)^2(DH)^\varepsilon E^{-1}
     R L^{1/2}(E Nk A_2 R)^{3/4}P^{5/4}. \tag{S}
\]
The long deletion \(b'\) contributes \((Nb')^{-3/8}\) after taking out the scale, because it changes the length to \(T/Nb'\), the physical numerator norm to \(N(b'dpk)\), and the inverse square-root weight by \((Nb')^{-1/2}\). No additional residual-column deletion is inserted.

For \(R\le D^{2/7}\), balance (S) with the \(L/P\) term of (Q) at \(P_0=D^{2/9}E^{-5/9}(A_2 Nk)^{-1/3}R^{-7/9}\). Below \(P_0\) use (S), above use (Q). If \(P_0<1\), the first branch is empty and \(L/P\le L/P_0\) still holds. Since \(R\le D^{1/3}\) and \(P\ll L^{1/3}\), the remaining two terms of (Q) and the balanced boxes are \(\ll R D^{2/3}\) inside \(E^{-1}\). Each column squared mean is therefore
\[
 \ll (M+V_1)^2(DH)^\varepsilon E^{-1}
       [D^{7/9}E^{-4/9}(A_2 Nk)^{1/3}R^{7/9}+R D^{2/3}].
\]
Apply bilinear Cauchy in \(r\) at fixed \(d,h,s,k,\ell,e,v_2\) to the actual two shifted columns, with the bounded original \(r\) scalar. Then use the absolute \(d\) sum with powers \(13/9,1\), the compatible \(h,s\) count \(O_S(X^{1/6}R^{-1/6})\), and the original normalization \(A_1/D\). Use \(A_1 A_2\le H/A_2\) after counting \(v_2,\ell,e\) by \(O(A_2(DH)^\varepsilon)\). Keep \(k\) fixed in this comparison, with its finite selector and actual complex weight outside. When a fixed \(k\) is not in an original \(v_2,\ell\) fibre, that summand is zero. With \(J=Nk\), the small-\(R\) band bound, before the absolute \(k\) weight \(J^{-2}\), is
\[
 \ll (M+V_1)^2(DH)^\varepsilon H X^{1/6}
       [D^{-2/9}A_2^{-2/3}J^{1/3}R^{11/18}
                 +D^{-1/3}A_2^{-1}R^{5/6}]. \tag{7}
\]
The original finite \(k\) range may equivalently be written with its indicator on each \(v_2,\ell\) term. This is only a finite change of summation order.

For every \(R\), there is also the inherited physical sixth-free \(r\) norm \(\Phi_6(R,D/E)\) at the same fixed \(k\), after the common-divisor lift on the two original subsequences. On \(R\le X\le D^{3/8}\), \(\Phi_6(R,D)\ll D\) and the \(d\) sum is \(\ll D\log(2D)\) with the actual squared coefficient mass \(O(B_W^2D^\varepsilon/E)\). This comparison applies both to the small-\(d\) slice in (7) and to all \(d\) at high \(R\). After the same outer counts it gives the fixed-\(k\) bound \(\ll B_W^2(DH)^\varepsilon H X^{1/6}A_2^{-1}R^{-1/6}\), before \(J^{-2}\).

In the low range \(R\le D^{2/7}\), take the minimum of these two comparisons for the **same** actual small-\(d\) band. For nonnegative \(u,v,w\), \(\min(u+v,w)\le\min(u,w)+v\). The \(R\) powers cancel in the geometric comparison between the first term of (7) and the inherited bound, with powers \(3/14,11/14\):
\[
 \min\{D^{-2/9}A_2^{-2/3}J^{1/3}R^{11/18}, A_2^{-1}R^{-1/6}\}
 \le D^{-1/21}A_2^{-13/14}J^{1/14}.
\]
The second term of (7) costs at most \(D^{-2/21}A_2^{-1}\). Now take the positive \(k\) bounds, of powers \(27/14\) and \(2\), after multiplication by \(J^{-2}\). They converge, with a sufficiently small allocated epsilon, and do not change the original signed finite kernel. This fixed-\(k\) order of comparison improves the mixed capacity power in v1 from \(A_2^{-2/3}\) to \(A_2^{-13/14}\). For \(R\ge D^{2/7}\), the inherited comparison on all \(d\) gives \(D^{-1/21}A_2^{-1}\), which is covered by the same result after the convergent \(k\) majorant.

For the remaining \(E>D^{1/16}\) at small \(R\), the four inherited norm monomials after the \(d\) sums are bounded by
\[
 R+D^{15/16}+R^{5/6}D^{1/3-1/48}
                       +R^{1/3}D^{5/6-5/96}
\]
up to profile and epsilon losses. The literal unit residual is counted for \(D<E\le2D\). Multiplying by \(X^{1/6}R^{-1/6}/D\) gives a bounded factor since \(X,R\le D^{3/8}\). This complementary step uses no cancellation of the \(d\)-signs.

The inherited Bessel \(O(x)\) error, bounded before the lift with \(x\ll A_1 X/[(Nk)^2D^2]\), is \(\ll B_W^2(DH)^\varepsilon A_1A_2 X(A_1X/D^2)\). The optional original unequal-norm selection uses subtraction of the entire equal-norm ideal fibre, with error \(\ll B_W^2(DH)^\varepsilon A_1A_2 X/D\). Both are target-sized. Clip boundary dyads and sum the finite bands. The resulting candidate is
\[
 |P(X)|\ll [B_W^2+(M+V_1)^2](DH)^\varepsilon
      H[1+X^{1/6}D^{-1/21}A_2^{-13/14}]. \tag{8}
\]
The \(D^{-2/21}\) term of (7) is absorbed here. For \(X=D^{3/8}, H=D^{3/4}, A_2=1\) the pure power is \(257/336\), saving \(1/168\) from the preceding author's \(37/48\) candidate and \(1/21\) from the established same-prefix \(13/16\). The candidate reaches target for \(X\le D^{2/7}\), and at critical \(X\) for \(A_2\ge D^{5/312}\).

The new pure transition \(R\asymp D^{2/7}\), \(P\asymp1\) leaves \(5/336\) above target in this upper budget. There \(P_0=1\) at unit \(d,k\), the sharp bound meets the long-variable \(L/P\) term, and improving only the crossed quadratic term does not address it. This locates a short-factor obstruction in the comparison, without providing an arithmetic lower bound. The next estimate needs the actual small-\(p\) Gauss column or the signed joint pairing at this transition. The high-frequency complement, additional good factors, principal/short assembly, whole signed \(13/12\), unsigned \(9/8\), independent determinant/zero-location by scope, analytic/category Lean and GRH remain open.

Acceptance requires review of the four shared-prime cases, the CRT and reciprocity phases, the two residual Möbius masks, the Gaussian separation at subunit dual length, the all-\(r\) interpolation and finite-prefix assembly. The new algebra uses the pinned [Goldmakher–Louvel v2](https://arxiv.org/abs/1112.1642v2) and [de Faveri v1](https://arxiv.org/abs/2610.04045v1) inputs. The literature version and proof files are bound in the source receipt. Finite author controls only check algebraic and rational-budget identities.

