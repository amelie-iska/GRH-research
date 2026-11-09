# Smooth radial partner modes by inverse Poisson

9 November 2026 UTC. Use the original pure two-pivot scales \(A=A_1\asymp R\asymp D^{3/4}\), \(A_2\asymp1\), original literal unweighted nonprincipal rows, actual primitive \(Q_u\asymp R\), fixed \(S,\nu,u_0\), one common complex \(W\) supported on \([1,2]\) and \(U^2\le D\le7U^2/2\). The partner is the original wide unit-pair term, including the re-expressed direct component of MATCHED_POISSON_CROSS-v2 and the allocation and strict cutoff tests of SELECTED_LOW_FREQUENCIES-v2. The original middle equality is subtracted with the same selection on the actual equality frequency.

Let \(1\le T\le C R\), with \(C\) fixed. Multiply the partner modes in every original frequency window, including the re-expressed direct part, by \(\sigma(N\mathfrak k/T)\), where \(\sigma\) is smooth and supported in a fixed compact subinterval of \((0,\infty)\). The profile may depend on the fixed partner labels and the actual row-independent equality allocations of JOINT_EQUALITY_FREQUENCY-v2. It is independent of the two varying cutoff ideals and the row and has uniformly bounded \(\|\sigma\|_{C^6}\). The claimed bound also allows a fixed additional condition \(\mathfrak v\mid\mathfrak k\), or an additional avoidance \((\mathfrak k,\mathfrak v)=1\), for an ideal \(\mathfrak v\) of polynomial norm fixed on these cells independently of the grouped equality label \(h_0\). In particular it can depend on fixed \(d,m,n,r_1,e_{0,1},e_{1,1},J_1,g,\ell,e_{1,0}\). These are selections in the actual frequency representation. A uniform target bound for general sharp selectors at this scale is open.

In this setting the normalized selected cross, including the separate exact compensation, reaches \(O((DH)^\epsilon \mathcal M_{24}(W)^2D^{3/4})\) times the uniform selector seminorm on all \(Nd\lesssim D^{1/6}\). More generally for \(e=\log_D Nd\le1/4\) the relative power over \(R/Nd\) before compensation is at most
\[
 \frac16(1/4+e/2-l_s)_+,\qquad
 l_s=\log_D\max(1,\min(U/Nm,U/Nn)).
\]
Here \((d,m,n)\) selections may be arbitrary and row independent, as in the base result. The proof reaches the proper smooth main band \(T\asymp R\) on this low-divisor range, without assigning a conductor shape or content class to every mode in that band.

## 1. The exact second transform

Keep the unit allocation and definitions of SELECTED_LOW_FREQUENCIES-v2. In particular put \(E=Nd\), \(d=mn\), \(L_i=U/N(m_i)\) with \((m_1,m_2)=(m,n)\), \(\zeta=e_0 z_0=\zeta_1\zeta_2\), \(h_1=r e_0\), \(E_1=Ne_1\), and
\[
 L=\frac{D}{E E_1(Nh_1)^2 Nz_0},\qquad 1/4<L<7/2,\qquad
 L_i<N\zeta_i<14L_i,\quad N\zeta_i\le U .
\]
Keep the exact live \(J\) test, primal-zero test, fixed row factors, original masks and phases. In the total partner Poisson contribution the full set of nonzero ideal frequencies is covered once per live allocation after the direct window is re-expressed. The selected middle compensation is treated separately below. Summing the selected full partner contribution on that allocation therefore permits a full Poisson identity with the multiplier, including when the support crosses an original window boundary.

Write \(F(x)=W(|x|^2)\) for \(x\in\mathbf R^2\), with Fourier convention \(e^{-2\pi i x\cdot\xi}\). In the original identity \(G_W(y)=\widehat F(\sqrt{4y/3}\,\mathbf e)\) for a fixed unit vector \(\mathbf e\). At fixed actual \(L,Q=Q_u,T\) define the radial Schwartz function
\[
 \widetilde F_{L,Q,T}
 =\mathcal F^{-1}\!\left[
  \widehat F(\xi)\,\sigma\!\left(\frac{3Q|\xi|^2}{4LT}\right)\right].
 \tag{1}
\]
The multiplier evaluated at the actual primitive dual point is exactly \(\sigma(N\mathfrak k/T)\). If the added condition is \(\mathfrak v\mid\mathfrak k\), set \(V=N\mathfrak v\) and reindex \(\mathfrak k=\mathfrak v\mathfrak k'\). The profile scale becomes \(LV\), the band scale becomes \(T/V\), and (1) is unchanged because their product is \(LT\). The original Poisson scalar \(2L\gamma_u/(\sqrt3\sqrt Q)\) is \(1/V\) times the scalar for \(LV\). Raw multiplicativity retains the exact \(\overline{\psi_u(\mathfrak v)}\) even when it is zero. Apply the same radial primitive Poisson formula at scale \(LV\) with the profile (1). The exact selected partner amplitude on this allocation is thus the fixed original signs and raw phases times
\[
 \frac{\overline{\psi_u(\mathfrak v)}}{V}
       \sum_{\mathfrak b\ne0}
          \psi_u(\mathfrak b)\,
          \widetilde F_{L,Q,T}\!\left(
                  \sqrt{\frac{N\mathfrak b}{LV}}\,\mathbf e\right).
 \tag{2}
\]
The fixed phases include the original \(\psi_u(h_1)^2\psi_u(e_1)\psi_u(z_0)\) and \(\mathbf1_{(d,u)=1}\). Take \(\mathfrak v=1\) for the unconditioned case. No extra restriction at any prime is inserted into the \(\mathfrak b\)-sum. In particular the \(\mathfrak b\)-sum is no longer the original compact primal sum, and one cannot use its old unit-only support. Formula (2) holds with the actual Gauss normalization because it is an application of the original formula from primal to dual with a new Schwartz profile. The primitive zero mode is still absent by nonprincipality. The extension from a compactly supported radial profile to this Schwartz profile follows by radial smooth truncation and convergence in the Schwartz topology on both lattices. The possible primal zero lattice point has zero primitive character. Every original live and zero-removal condition was imposed before (1).

For a fixed prime-avoidance condition expand \(\mathbf1_{(\mathfrak k,\mathfrak v)=1}=\sum_{\mathfrak v'\mid\operatorname{rad}\mathfrak v,\ \mathfrak v'\mid\mathfrak k}\mu(\mathfrak v')\). Use (2) on each fixed \(\mathfrak v'\). The number of terms has subpower size for polynomial norm. Each raw character and all terms in the Möbius expansion remain in the exact amplitude. This comparison alone gives no gain in \(V\) after the absolute primal sum, so summing unbounded families of divisibility selectors needs further input.

## 2. Uniform log separation with summable primal mass

Let \(p=T/R\), \(z=\log L\), \(q=\log(Q/R)\). Both log variables range over fixed compact sets. Define \(Y=4 L T/(3Q)\) and \(X=\sqrt{4TN\mathfrak b/(3QV)}\). After the change of variable \(\xi=\sqrt Y\,\eta\) in (1), the weight in (2) is
\[
 H_{\mathfrak b}(z,q)=\frac{Y}{V}
       \int_{\mathbf R^2}
           e^{2\pi i X\mathbf e\cdot\eta}\,
           \widehat F(\sqrt Y\,\eta)\,\sigma(|\eta|^2)\,d\eta .
 \tag{3}
\]
Extend \(H_{\mathfrak b}\) by multiplying by fixed smooth compact log cutoffs equal to one on the actual \(z,q\) ranges. For \(0\le i,j\le2\), its mixed derivative in \(z,q\) has the pointwise bound
\[
 \left|\partial_z^i\partial_q^j H_{\mathfrak b}\right|
 \ll \|\sigma\|_{C^6}\|W\|_\infty
       \frac pV(1+(p/V)N\mathfrak b)^{-2}.
 \tag{4}
\]
Indeed \(X\) does not depend on \(z\). Each \(q\) derivative of the exponential contributes a bounded-degree polynomial of degree at most \(j\) in \(X\) on the fixed support in \(\eta\). Apply \((1-\Delta_\eta)^3\) by integration by parts, moving it onto the amplitude including any polynomial in \(\eta\). This supplies \((1+4\pi^2 X^2)^{-3}\), which absorbs that polynomial and leaves \((1+X^2)^{-2}\). At \(p\le C\), all differentiated \(\widehat F\) factors are bounded by \(O_C(\|W\|_\infty)\) because \(F\) is supported on the fixed annulus. The derivatives of \(Y\) in the log variables are bounded by fixed multiples of \(Y\). The fixed log cutoff derivatives satisfy the same bounds.

Consequently the exact two-variable log Fourier inversion has a uniform pointwise majorant
\[
 |\widehat H_{\mathfrak b}(\alpha,\beta)|
 \ll \|\sigma\|_{C^6}\|W\|_\infty
 \frac{p/V}
      {(1+(p/V)N\mathfrak b)^2(1+\alpha^2)(1+\beta^2)} .
 \tag{5}
\]
This is uniform over allowed equality-label-dependent profiles \(\sigma\). The factor \((Q_u/R)^{2\pi i\beta}\) is an exact row multiplier, and \(L^{2\pi i\alpha}\) separates into exact fixed constants times the two independent norm twists on \(\zeta_1,\zeta_2\). The original integer product test \(J\le N\zeta<2J\) uses the separate exact log step of SELECTED_LOW_FREQUENCIES-v2. In particular it is still independent of the inverse profile's new primal ideal. The full sum of (5) over that ideal and the Fourier variables is bounded by \(O_C(\|\sigma\|_{C^6}\|W\|_\infty)\), uniformly in \(V\ge1\), since ideal counting gives
\[
 \frac{p}{V}\sum_{\mathfrak b\ne0}
      (1+(p/V)N\mathfrak b)^{-2}\ll_C1.
 \tag{6}
\]
This uses no orthogonality of equal-norm ideal fibres. All operations before the positive comparisons use the exact ideals and raw phases. A sharp interval selector does not supply the derivative bound (4). Replacing it by an exact nodal step with shrinking transitions makes the constant depend on their inverse widths, so (5)–(6) give no uniform sharp-mode theorem.

## 3. Transfer to the actual joint cutoff norm

Fix the remaining partner and equality outer labels. Use the exact \(e_0=e_{0,1}e_{0,2}\) assignment and \(w\)-projector of SELECTED_LOW_FREQUENCIES-v2. The shortened independent lengths are \(M_i=L_i/(Ne_{0,i}Nw)\), live \(M_i>1/14\), with the exact \(14L_i\) cap, both strict lower bounds and original upper bounds. Keep all residual \(w,d,r,e_0\) masks and the fixed raw factors. At each \(\mathfrak b,\alpha,\beta\) from (2)–(5), the fixed new raw multipliers involving \(\mathfrak b,\mathfrak v\) have modulus at most one and are independent of the varying cutoffs and the equality \(h_0\) label. In the original conjugate partner they are conjugated as dictated by the pairing. No row-dependent deletion from them is removed in the exact signed expression.

If \(\sigma\) depends on the actual equality allocation, at fixed \(h_0\) include the profile coefficient \(\widehat H_{\mathfrak b}(\alpha,\beta)\) inside the signed finite allocation sum. After dividing by the positive uniform majorant (5), the resulting coefficient is still divisor bounded on the same \(h_0\) support. The equality radial profile is unchanged. This is the same allocation convention as JOINT_EQUALITY_FREQUENCY-v2, now with an inverse-profile coefficient. For a vanishing majorant the corresponding contribution is zero. At fixed \(\mathfrak b,\alpha,\beta\) and original log steps, the paired product is therefore the actual equality sum times the conjugate of the two cutoff arrays and the fixed row phases.

Apply Cauchy to the actual product, taking the joint norm with the shorter cutoff. Inside the positive joint norm only, \(\|F_{T_0}\overline{B_s}\|_2=\|F_{T_0}B_s\|_2\). Group the true label \(h_0^2 b_s\), using the notation of FORCED_RADICAL_JOINT-v1. Its squarefree two-bit reconstruction, forced radical \(h_0\), raw zeros and true mass \(O((DH)^\epsilon N(h_0)_{\mathrm{dyad}}M_s)\) are unchanged. Apply the forced-radical comparison in that note and the ordinary norm for the longer cutoff. The inverse profile adds only the summable scalar (6) and the fixed contractions already present in the signed expression. The actual \(h_0\) radial dyad sum, \(g,\ell,e_{1,0}\) weights, harmonic \(w\) and original mass \(\sqrt{L_1L_2}\asymp\sqrt{D/E}\) are the same as in that comparison. The extra fixed \(e_0\) shortening can only reduce the mass. Thus the exact exponent and radial budget of equation (2) of FORCED_RADICAL_JOINT-v1 remain valid, with unchanged live subunit conventions.

For the separate middle term retain \(X'>B_*\), \(K_0<N\mathfrak k\le MD^\eta\) and \(Nz_0=N\mathfrak k\), with the same \(\sigma\) and same optional ideal condition. These may be applied directly to the original frequency in that term. The original divisor-bounded equality count with the coefficient bounded by \(\|\sigma\|_\infty\) gives the target \(R/E\) after pairing. If \(\sigma\) depends on equality labels, use the allocation-wise middle count and sum the direct per-label equality majorants as in JOINT_EQUALITY_FREQUENCY-v2. This keeps the exact compensation distinct from (2). The sign \(\mu(d)\) remains in the original paired expression until the final harmonic comparison.

No content-based or power-based union of varying frequency masks is inferred from this result. It covers smooth radial selections through the main physical scale, with the stated optional fixed-ideal predicates. The unbalanced intermediate divisor regime, arbitrary sharp main-mode selections and the whole signed form remain open.

