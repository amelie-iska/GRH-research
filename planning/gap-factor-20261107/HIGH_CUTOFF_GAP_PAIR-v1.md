# Exact two-factor reduction at the high cutoff

Author draft, 7 November 2026 UTC. Independent review is pending. The new signed coefficient identity is finite. Its transfer to the whole central principal-density term uses the previous localization, including the pending (Q) and (M) inputs. The separate estimate for the thin cutoff part of the resulting two-factor kernel uses the inherited cubic and sixth-free norms.

## 1. Scope and the literal small-product boundary

Use the original central principal-sixth-part density \(\mathfrak M_R(X)\) of PRINCIPAL_DENSITY_MACRO_SPLIT-v1, with the full fixed original two-pivot and finite primitive kernel from cbk and mixed6456, with required precisions 6fed549f and 7d62d6c9. Keep \(D\ge 2^{64}\), \(1\le H\le D^{3/4}\), \(1\le X\le D^{3/8}\), \(D^{13/40}\le R\le D^{27/80}\), the exact \(R\le Nr<2R,\ Nh\,Nr\le X\) clipping, and the original \(u_0,A_1,A_2\) capacity. This note requires the high cutoff
\[
 2D/7\le U^2\le D .
\]
The complete original ordered coprime squarefree ideal columns, the two possibly distinct gauges, the common fixed complex \(W\) supported in \([1,2]\) with zero endpoints, and all source, primitive \(S\), ray, capacity, orientation and equal-norm data stay in the original pairing. The row is nonprincipal even when the fixed sixth-part ray is principal. The original finite \(k\) range includes \((k,v_2)=1\) and the pre-\(S\) cap. The principal density is the previously derived factor \(\kappa_S g(m)g(n)(X/(Nh\,Nr))^{1/6}\). The actual counting and Bessel errors remain separate.

Insert the full signed column-coprimality lift over \(d\) only in the separated product of the actual columns, with \(m=da\) and \(n=db\). This auxiliary extension is by the original single-column factors. A primitive root at an overlapping pair is never invoked. Write \(E=Nd\), \(J=Nk\), \(L=D/E\). The preceding localization gives the complementary parts and restricts the main calculation to \(E,J,A_2\le D^{1/96}\), with two or three large labels in both columns. In each of these boxes the large dyadic scales exceed \(D^{3/10}\) and all small scales together have product less than \(Z=D^{1/32}\). Use the same finite eleven-label expansion of the actual shifted \(B_U=\mu A_U\). The two original coefficient-one slots have literal cutoffs \(U/Nd_1,U/Nd_2\), and the third original factor is expanded with truncation \((2L)^{1/5}\). The shift has the sum over \(d_1d_2d_3=d\) with coefficient \(\mu(d_3)\). All products are squarefree and disjoint within one column.

We must distinguish the product of the small dyadic scales from the norm of the actual product \(c\) of the small ideals, including both original slots whenever small. First remove the portion \(Nc\ge Z\) on either side. On a remaining no-middle box where this boundary portion is present, the product \(P\) of the small scales satisfies \(Z/2^{11}\le P<Z\). Use the entire small group as the short variable in the same proof of (Q) as in the previous localization. The extra condition \(Nc\ge Z\) is an exact short coefficient selector. The positive three types of monomials are
\[
 L/P,\quad RP(R+P),\quad (RL)^{2/3}.
\]
They are \(O(D^{31/32})\) in this range, with absolute constants from the finite labels. The other column may be any fixed sum of labelled boxes with divisor-bounded coefficients, so its squared norm is \(O(B_W^2 (DH)^\varepsilon D/E)\). For the union where at least one side has \(Nc\ge Z\) use the exact split into that side times the full other side, plus its complement times the selected other side. This is bilinear Cauchy on the actual paired \(r\) band before taking the finite outer bounds. The normalized cost is \(O((B_W+M(W))^2 (DH)^\varepsilon H D^{-7/960})\), since \(D^{-1/64}(X/R)^{1/6}\le D^{-7/960}\). This boundary step is conditional on (Q). The strict literal condition \(Nc<Z\) on both sides is now exact in the remaining expression.

## 2. Signed summation over all label positions

Fix \(d_1,d_2,d_3\) and one residual column. Fix the actual small ideal \(c\) with \(Nc<Z\) and the unordered set \(\{v_1,\ldots,v_q\}\) of its actual large ideals, where \(q=2\) or \(3\). These ideals are distinct because they are nonunit and pairwise coprime. Their prescribed large scales exceed \(D^{3/10}\). The product \(a=c\prod_i v_i\) is fixed, squarefree and coprime to \(d\). No other factorization constraint depends on the ordering of the large labels. Indeed any subset of labels containing a large one has scale product above \(D^{3/10}\), and all small labels together have scale product below \(Z\). Also every small divisor has norm below both short cutoffs and the truncation:
\[
 Z< U/E,\qquad Z<(2L)^{1/5}.
\]
Both follow uniformly in the stated ranges. Every truncated Möbius slot must be small. Thus after the literal small-product clip, dyadic membership imposes no further constraint on the allocation of the small primes among small slots. Reunite their dyads exactly. Keep every ordered large allocation, including one or both original slots as allowed by their actual cutoffs. At fixed \(m=da\) all original profile, phases, gauge, inverse norm, density and raw masks are common to the label sum. The identity is at the level of this signed coefficient before any absolute value.

Let \(I_{ij}=\mathbf1_{Nv_j\le U/Nd_i}\) for \(i=1,2\), with equality included. For the \(j\)-th term of the five-fold identity, its signed scalar is \(c_j=(-1)^{j-1}\binom5j\), there are \(j+1\) coefficient-one slots including the two original slots, and \(j\) truncated Möbius slots. For a choice of allowed distinct large ideals in zero, one, or two original slots, write \(\ell\) for the number of large ideals still to place. The remaining ordered placements count \((j-1)_\ell\), the falling factorial, zero if \(j-1<\ell\). On a live placement the small coefficient at \(c\) is
\[
 (\mathbf1^{*(j+1-q)}*\mu^{*j})(c)=\mu^{*(q-1)}(c).
\]
This is the ordinary finite ideal convolution on divisors of \(c\), where all cutoffs are inactive. It uses the unit cases and the actual signed truncation. The identity
\[
 \sum_{j=1}^{5} c_j (1+z)^{j-1}=1-z+z^2-z^3+z^4
\]
gives \(\sum_j c_j(j-1)_\ell=(-1)^\ell\ell!\) for the needed \(\ell\).

Consequently the multiplier of \(\mu^{*(q-1)}(c)\mu(d_3)\) after every allowed placement is
\[
 \begin{aligned}
 &(-1)^q q!+(-1)^{q-1}(q-1)!\sum_{i,j} I_{ij}
      +(-1)^{q-2}(q-2)!\sum_{j\ne k} I_{1j}I_{2k}\\
 &\qquad=(-1)^q(q-2)!\sum_{j\ne k}(1-I_{1j})(1-I_{2k}).
 \tag{1}
 \end{aligned}
\]
Here the \(j,k\) on the right label actual distinct large ideals. The equality uses the fact that each one-slot indicator occurs \(q-1\) times in the double sum. Formula (1) preserves unequal cutoffs and the sign of the actual third assigned divisor \(d_3\). It replaces the original below-cutoff allocation by an ordered above-cutoff pair. Its derivation is a finite identity, independent of the norm bounds.

For each ordered above-cutoff pair in (1) we have \(N(d_1v_j)N(d_2v_k)>U^2\). Since \(Nm\le2D\),
\[
 N\!\left(d_3 c\prod_{i\notin\{j,k\}}v_i\right)
       <2D/U^2\le7. \tag{2}
\]
The strict inequality retains the lower endpoint \(2D/7=U^2\). Good ideals exclude the primes above \(2,3\), so every good nonunit has norm at least \(7\). Thus \(q=3\) vanishes exactly, and \(q=2\) forces \(d_3=c=\mathcal O\). The sign and convolution factor are then both one. A surviving ordered assignment gives the actual two factors \(x=d_1v_j,\ y=d_2v_k\) of \(m\), with \(Nx,Ny>U\).

Conversely, let \(xy=m\) be any ordered factorization with \(Nx,Ny>U\). The unique assigned divisors are \(d_1=(x,d)\) and \(d_2=(y,d)\), with \(d=d_1d_2\) on the original squarefree support. The residual factors have norms \(>U/E\). Their dyadic scales exceed \(D^{3/10}\) because \(U/(2E)>D^{3/10}\) for \(D\ge2^{64}\). There are no small primes left outside those two residual ideals, meaning \(c=\mathcal O\), and the pair occurs exactly once on the right of (1). The two residual factors are allowed to have small prime divisors internally. The criterion here is on whole factor norms.

It follows that for each small \(d\), the whole remaining expanded coefficient on either side is exactly
\[
 \tau_{\rm gap}(m)=\#\{(x,y):xy=m,\ Nx>U,\ Ny>U\}
 \quad\text{in the }B_U\text{ gauge}.                  \tag{3}
\]
It does not depend on the auxiliary common divisor \(d\). When using the unshifted primitive kernel, the replacement for \(A_U\) is \(\mu(m)\tau_{\rm gap}(m)\). This restores the original sign convention. In particular (3) can be positive on genuine coprime columns and does not give a lower bound for the signed paired expression.

## 3. Restoring the coprime projector and a bound near the cutoff

In the paired term with both gap coefficients, restore the missing \(E>D^{1/96}\) portion of the \(d\) sum with the actual gap coefficients. The restored part is bounded by the inherited physical norm with squared coefficient masses \(O(B_W^2D^\varepsilon/E)\), since \(\tau_{\rm gap}(m)\) is divisor-bounded. The bound is the same \(O(B_W^2(DH)^\varepsilon H D^{-1/480})\) as the previous large-\(d\) tail, including the direct unit case. The signs \(\mu(d)\) remain literal in the identity. The full sum reimposes the original coprime projector exactly. Restore the \(J>D^{1/96}\) or \(A_2>D^{1/96}\) parts of the gap pairing as well, by the same physical comparison with the original finite \(k\) selector and the actual capacity. Thus the original central principal-density term differs from the **original coprime** principal density using the two coefficients \(\mu(\cdot)\tau_{\rm gap}(\cdot)\) by
\[
 O\big((B_W+C_W+M(W))^2 (DH)^\varepsilon H D^{-1/480}\big).
 \tag{4}
\]
The constant in (4) uses the fixed data, the previous localization and the new boundary comparison. The raw \(s\) masks and sixth-part counting error stay in the antecedent exact kernel. The replacement (4) concerns only the specified principal-density term. It does not assert convergence of an extended \(k\)- or \(r\)-sum.

We can further estimate a part of the exact gap pairing. Put \(\Delta=D^{-1/32}\) and call an ordered factorization thin when either original norm is in \((U,U(1+\Delta)]\). The second case is taken only when the first norm exceeds \(U(1+\Delta)\), so the two selectors are disjoint and each restricts the two factors independently. Split each actual gap coefficient into this thin part and its complement. As before select their paired union by the sum of the thin first column times the full second, and the complementary first column times the thin second. The two gauges and the actual \(r\) scalar stay in the signed pairing.

For \(E\le D^{1/96}\), assign \(d=d_1d_2\) to the two original factors as above. At fixed \(r\), after all fixed finite selector decompositions, the exact Gauss CRT makes the interaction of the two residual factors the physical squarefree cubic matrix of rg:cubic-input. Its entries include the squarefree overlap zeros. The actual \(r,d,k,v_2\) symbols and raw masks factor into the original per-factor coefficients or fixed scalars. The original \(g\) factors multiplicatively within each squarefree column. Any remaining common \(W\) is separated by its exact Mellin integral with \(M(W)\). These operations preserve the individual factor cutoffs, including the literal thin boundary. The factor outside the two normalized vectors is \(E^{-1/2}\). If the original factor is thin, its residual lies in an interval of relative width \(\Delta\) at scale \(P\asymp U/Nd_i\gg D^{47/96}\). Elementary lattice cell counting in the Eisenstein plane, or subtracting the two disk main areas with \(O(\sqrt P+1)\) error, gives \(O(\Delta P+\sqrt P+1)\) ideals there. This counts distinct equal-norm ideals. Thus its squared normalized coefficient mass is \(O((DH)^\varepsilon D^{-1/32})\) while the other factor has bounded mass up to subpowers. The two lengths are \(O(\sqrt D)\) by \(U<Nx,Ny\le2D/U\); the inherited cubic squared norm is \(O((DH)^\varepsilon D^{2/3})\). This calculation needs no interval-dependent derivative bound.

Summing squares over actual \(r\) and the finite divisor allocations by the divisor bound, the thin column has squared norm at most \(O(M(W)^2(DH)^\varepsilon R D^{2/3-1/32}/E)\). For the other, use the ordinary physical sixth-free comparison on the actual residual vector and get \(O(B_W^2(DH)^\varepsilon D/E)\). Since \(R\le D^{27/80}\), the thin exponent is at most \(467/480\). Bilinear Cauchy in \(r\), followed by the signed \(d\) absolute upper estimate, gives a saving \(13/960\) relative to \(D\) before the density cost \(D^{1/120}\). The normalized small-\(d\) thin part is \(O((B_W+M(W))^2(DH)^\varepsilon H D^{-1/192})\), counting \(h,v_2,\ell,e\) and the original finite \(k\) weights as in (4). The large-\(d\) tail costs \(O(B_W^2(DH)^\varepsilon H D^{-1/480})\). These thin-gap estimates use the inherited physical and cubic norms only. The comparison between the whole original central density and the far-from-cutoff gap pairing still requires the earlier localization as stated above.

## 4. Remaining exact problem

The surviving central expression is the original signed principal-density pairing with each column built from two actual ordered factors with norms in \((U(1+\Delta),2D/U]\), with the factor \(\mu(m)\) in its \(A_U\) convention. It retains the original coprime projector, both gauges, every primitive phase, fixed profile, exact capacity and complete ideal norm fibres. The remaining two lengths can both be of order \(\sqrt D\). The earlier joint comparison's \(RP^2\) term still permits a power above \(D\), and the physical \(D\)-term still leaves the density cost. There is no improved whole-prefix exponent. The next estimate must handle this signed two-factor expression away from the narrow cutoff, especially at two comparable lengths. The whole signed \(13/12\), unsigned \(9/8\), higher frequencies, extra factors, short/principal assembly, determinant and zero-location by scope, Lean and GRH remain open.

The fresh controls directly enumerate the signed label assignments with unequal cutoffs and independently check the above-cutoff expression. They also test the actual high-cutoff gap on coprime prime-ideal support and a nonunit assigned divisor, strict endpoint inequalities, and the thin-band exponents. They do not certify the analytic norm inputs.
