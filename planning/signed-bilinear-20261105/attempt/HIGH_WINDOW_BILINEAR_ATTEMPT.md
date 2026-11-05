# High cutoff bilinear reduction and the remaining balanced row loss

5 November 2026. Remote research attempt in the original Eisenstein sextic family.

For \(2D/7\le U^2\le D\), the actual long-long complement on the active annulus is an exact two-factor polynomial. This structural reduction does not yet prove \(BT_\sigma\). Applying the accepted powered BGL inequality after a legitimate factorwise Cauchy estimate retains \(DX\). The stronger available upper bound remains the previously accepted recombined envelope. A product of marginal BGL norms cannot be used as if the two factors were evaluated on independent rows.

## Exact objects and scope

Use precisely the objects and conventions in
[the accepted signed target](../../weighted-moment-20261105/frontier/CENTERING_AND_SIGNED_TARGET.md)
and its [v2 reconciliation](../../weighted-moment-20261105/review/CLARIFICATION_ACCEPTANCE_ADDENDUM.md).
Thus \(K=\mathbb Q(\omega)\), \(S\) is fixed and contains primes above \(6\) and the conductor of the fixed finite-order character \(\nu\), \(D>1\), \(1\le U\le\sqrt D\), and one common smooth, possibly complex, \(W\) is supported in \([1,2]\). Every column and convolution ideal is squarefree and prime to \(S\). The raw symbol is
\[
 x_m(u)=(u/m)_6,\qquad
 I_u=D^{-1/2}\sum_m A_U(m)\nu(m)W(Nm/D)x_m(u).
\]
In particular \(x_m(u)=0\) at every shared prime.

The balanced block consists of the literal six generators of
\((u)=r s^2\), with \(r,s\) nonunit, squarefree, coprime, prime to \(S\),
\(X\le Nr,Ns<2X\), and \(S\)-part one. Write this block as \(B_X\).
On this block alone the accepted nonprincipality argument gives
\(P_u=0\), so \(E_u=I_u\). The original residue on other rows is still
\[
 P_u=1_{\psi_u=1}\sqrt D\,\widehat W(1)
 \sum_d\frac{\beta_U(d)\nu(d)x_d(u)\rho_{T(u,d)}}{Nd}.
\]
No new residue is assigned to the pieces below; no principal cancellation
elsewhere is asserted. Independently primitive \(\psi_u\) and
\(\psi_{u,2}\) and the original full deleted set retain their accepted meanings.

## 1 The high cutoff window is exactly bilinear

Let
\[
 C_U(m)=\sum_{\substack{abc=m\\Na>U,\ Nb>U}}\mu(a)\mu(b),
 \qquad
 r_U(m)=\#\{(a,b):ab=m,\ Na>U,\ Nb>U\}.
\]
The factorization is ordered and disjoint because \(m\) is squarefree.
The accepted active-annulus identity is \(A_U=C_U-\mu\).

The least norm of a good nonunit ideal is \(7\): above rational \(2\)
and \(3\) are in \(S\); the next Eisenstein prime ideals have norm \(7\).
If \(c\ne1\), a summand of \(C_U\) with \(Nm\le2D\) would satisfy
\[
 Nm=Na\,Nb\,Nc>7U^2\ge2D,
\]
a contradiction. The strict inequalities \(Na,Nb>U\) prove this even
at \(7U^2=2D\), including \(Nm=2D\). If \(S\) deletes the norm \(7\)
primes too, \(7\) remains a valid lower bound. Consequently, throughout
the active annulus, including its endpoints,
\[
 C_U(m)=\mu(m)r_U(m),\qquad
 A_U(m)=\mu(m)(r_U(m)-1).                         \tag{HW}
\]
This is a window theorem, not an identity for every cutoff.

The swapping involution \((a,b)\mapsto(b,a)\) on the set counted by
\(r_U(m)\) has no fixed point. Indeed \(a=b\) and \((a,b)=1\) force
\(a=b=1\), incompatible with \(Na,Nb>U\ge1\). Hence \(r_U(m)\) is even
and \(A_U(m)\) is an odd integer times \(\mu(m)\). In particular
\[
 |A_U(m)|\ge1.                                   \tag{CN}
\]
This last assertion concerns coefficients, not row energy.

For every contributing pair,
\[
 U<Na,Nb<2D/U,\qquad D\le Na\,Nb\le2D.             \tag{HS}
\]
The upper inequality can be strict because the other factor is strictly
larger than \(U\). Thus both norms lie between fixed positive multiples
of \(\sqrt D\); their full ranges have ratio at most \(7\). There are
only a bounded number of dyadic pairs \(Na\asymp A,Nb\asymp B\), and
each nonempty pair has \(AB\asymp D\) and \(A,B\asymp\sqrt D\).
All restrictions in (HS), rather than a rectangular replacement, belong
to the exact polynomial.

## 2 The raw bilinear polynomial retains every common prime

In this window define
\[
 L_u=D^{-1/2}
 \sum_{\substack{a,b\ {\rm sf},\ (ab,S)=1,\ (a,b)=1\\
                Na,Nb>U,\ D\le Na\,Nb\le2D}}
 \mu(a)\mu(b)\nu(a)\nu(b)
 W(Na\,Nb/D)\,x_a(u)x_b(u),
 \quad
 M_u=D^{-1/2}\sum_m\mu(m)\nu(m)W(Nm/D)x_m(u).
                                                               \tag{BP}
\]
Then \(I=L-M\) on all rows, and \(E=L-M\) on \(B_X\).
Here \(x_{ab}(u)=x_a(u)x_b(u)\) is an exact equality, including zeros:
it vanishes if any prime of \(ab\) divides \(u\).
For a literal row \(u=\varepsilon\alpha\beta^2\), where
\((\alpha)=r,(\beta)=s\),
\[
 x_{ab}(u)=x_a(\varepsilon)x_b(\varepsilon)
          x_a(\alpha)x_b(\alpha)
          x_a(\beta)^2x_b(\beta)^2.               \tag{RF}
\]
The same \(r,s\) occur in both column factors. The conditions
\((a,b)=1\), \((r,s)=1\), and all intersections of \(ab\) with \(rs\)
remain as displayed masks. One cannot remove \((a,b)=1\) by enlarging
a complex inner sum: absolute values do not make such enlargement
monotone.

The finite unit/ray-class partitions and reciprocity used by the
accepted BGL transfer identify the raw factors with the
COLUMN-indexed primitive characters \(\vartheta_a,\vartheta_b\).
Their outside-\(S\) conductors are exactly the squarefree columns \(a,b\);
that orientation keeps the zeros. No row-indexed primitive character
with erased sixth-power primes, or common sentinel for the distinct
primitive square denominator, is substituted.

The exact quadratic expansion still has the original union mask:
\[
 \sum_{u\in B_X}|I_u|^2
 =Q_B(C_U,C_U)+Q_B(\mu,\mu)-2\Re Q_B(C_U,\mu),
\]
\[
 Q_B(f,g)=D^{-1}\sum_{m,n}f(m)\overline{g(n)}
 \nu(m)\overline{\nu(n)}
 W(Nm/D)\overline{W(Nn/D)}
 \sum_{u\in B_X}x_m(u)\overline{x_n(u)}.            \tag{Q}
\]
Neither factorization nor (HW) changes the signs, conjugates, or the
required lower direction of the real covariance in \(BT_\sigma\).

## 3 A legal factorwise BGL estimate

Write
\[
 \Delta(X,N)=X+N+(XN)^{2/3}.
\]
The accepted power-one and power-two squarefree BGL inequalities give,
after the same fixed finite partitions, a one-row-factor norm at most
\((XN)^\epsilon\Delta(X,N)\). This is the classical input, not a newly
proved sieve theorem.

For one dyadic pair in (BP), set
\[
 T_a(u)=\sum_{\substack{b\sim B,\ Nb>U,\ (a,b)=1\\
                       D\le Na\,Nb\le2D}}
       \mu(b)\nu(b)W(Na\,Nb/D)x_b(u).
\]
The exact support, including its dependence on \(a\), is retained.
Pointwise Cauchy gives
\[
 \left|\sum_{a\sim A,\ Na>U}\mu(a)\nu(a)x_a(u)T_a(u)\right|^2
 \le O_K(A)\sum_{a\sim A,\ Na>U}|T_a(u)|^2.        \tag{CS}
\]
The use of \(|x_a(u)|\le1\) here is an upper-bound inequality, not a
replacement of its raw zero in any identity.

For fixed \(a\), fixed \(s\), and fixed unit/ray-class choices, the
coefficients of \(b\) in \(T_a\) are independent of the pivot row \(r\).
They include \(1_{(a,b)=1}\), the exact hyperbolic support,
\(W(Na\,Nb/D)\), and the original factor \(\vartheta_b(s)^2\).
Their squared norm is at most
\(O_K(B)\|W\|_\infty^2\). The positive sum over \(r\) may be enlarged
beyond \((r,s)=1\); no complex inner sum is enlarged. Applying power-one
BGL to \(r\), then summing the \(O_K(X)\) possible \(s\) and
\(O_K(A)\) possible \(a\), proves
\[
 \begin{split}
 \mathcal E_{A,B}
 &:=D^{-1}\sum_{u\in B_X}
   \left|\sum_{a\sim A}\mu(a)\nu(a)x_a(u)T_a(u)\right|^2\\
 &\ll_{\nu,S,\epsilon}(DX)^\epsilon\|W\|_\infty^2
       {A^2B\over D}\,X\,\Delta(X,B)\\
 &\ll (DX)^\epsilon\|W\|_\infty^2
       \{AX^2+DX+D^{2/3}A^{1/3}X^{5/3}\}.         \tag{FC}
 \end{split}
\]
The factor \(AB/D\asymp1\) is absorbed in the constants. One may
interchange \(a,b\), replacing \(A\) by \(\min(A,B)\) in the last line.
One may instead pivot on \(s\), using the power-two inequality, with the
same exponents. No Mellin separation, row-dependent profile supremum,
or derivative norm of \(W\) is used; the bound has precisely
\(\|W\|_\infty^2\).

Since \(A,B\asymp\sqrt D\), boundedly many blocks and an upper triangle
inequality give
\[
 Q_B(C_U,C_U)
 \ll (DX)^\epsilon\|W\|_\infty^2
 \{\sqrt D\,X^2+DX+D^{5/6}X^{5/3}\}.              \tag{LC}
\]
This is a valid bound on the actual polynomial with the full original
masks. It is weaker than regrouping \(C_U(m)\), whose divisor bound
also permits the previously accepted
\[
 Q_B(C_U,C_U),\ Q_B(\mu,\mu),\ Q_B(A_U,A_U)
 \ll (DX)^\epsilon\|W\|_\infty^2
 \{X^2+DX+D^{2/3}X^{5/3}\}.                      \tag{RB}
\]
For the first estimate in (RB), use \(|C_U|\le2^{\omega(m)}\) in this
window; for the last two the accepted actual-coefficient application
already applies. It is the old theorem being compared, not new progress.

## 4 Exponent optimization and the exact unsupported step

At \(X\asymp D^{1/4}\), the terms are:

| Bound | First exponent | Middle exponent | Last exponent |
|---|---:|---:|---:|
| Factor Cauchy (LC) | \(1\) | \(5/4\) | \(5/4\) |
| Recombined (RB) | \(1/2\) | \(5/4\) | \(13/12\) |
| Target \(BT_\sigma\) | \(1/2\) | \(5/4-\sigma\) | \(13/12\) |

For a hypothetical unbalanced factorization with
\(\min(A,B)=D^t\), \(0\le t\le1/2\), (FC) has exponents
\[
 t+\tfrac12,\qquad \tfrac54,\qquad \tfrac{13}{12}+\tfrac t3.
\]
Its maximum is \(5/4\) for every such \(t\). In the actual high window
\(t=1/2+O(1/\log D)\), so there is not even an asymptotic factor-length
parameter to optimize. The \(D X\) term remains after either legal
pivot. Taking the minimum with the existing envelope proves no
\(D^\sigma\) saving for any fixed \(\sigma>0\).
For \(0<\sigma\le1/12\), the target's leading exponent is
\(5/4-\sigma\), strictly below \(5/4\).

The tempting next step would treat the two factors in (RF) as independent
BGL transforms, multiply their marginal norms, and omit the shared row
correlation. BGL does not give that estimate. Even for a rectangular,
unmasked, exactly separated product the needed fourth moment is
\(\sum_{r,s}|P_A(r,s)P_B(r,s)|^2\), not the product of two second moments
over independent copies of \(r,s\). Cauchy supplies fourth moments;
it does not supply independence or a signed lower covariance.

There is an exact abstract counterexample to this generic inference.
Let \(n\ge2\), \(A=B=n^2\), rows \(r,s\in\mathbb Z/n\mathbb Z\), and
columns \((k,\ell)\in(\mathbb Z/n\mathbb Z)^2\). Put
\[
 V_{r,(k,\ell)}=e(kr/n),\qquad
 T_{s,(k,\ell)}=e(-ks/n).
\]
Both matrices satisfy \(VV^*=TT^*=A I_n\), so both marginal operator
norms squared are \(A\). For coefficient vectors \(\alpha=\beta=1\),
of squared norm \(A\),
\[
 F_{rs}=\sum_{k,\ell}V_{r,(k,\ell)}T_{s,(k,\ell)}
       =A\,1_{r=s},\qquad
 \sum_{r,s}|F_{rs}F_{rs}|^2=nA^4.
\]
The unsupported product-of-marginals inequality would give
\(\|V\|_{\rm op}^2\|T\|_{\rm op}^2
  \|\alpha\|_2^2\|\beta\|_2^2=A^4\), missing the factor \(n\).
With \(D=AB=A^2\) and \(X=n=D^{1/4}\), its normalized actual value is
\(D X\), although the two marginal constants have precisely their
BGL-sized scale \(A\).

These Fourier arrays are not the arithmetic sextic family and have no
Möbius or coprimality requirement. They refute only the proposed generic
norm deduction from two marginal inequalities. They give no arithmetic
energy lower bound and no counterexample to \(BT_\sigma\).
The precise missing arithmetic input is control of the coupled fourth
moment, or the required signed \(C_U\)-versus-\(\mu\) covariance,
with the actual support and masks. The calculation above does not show
that every conceivable use of BGL and arithmetic identities must fail.

## 5 A coefficient norm lower bound with no energy conclusion

For a fixed nonzero \(W\), (CN) also shows that a power saving cannot
come just from a smaller ordinary coefficient norm in this window:
\[
 D^{-1}\sum_{\substack{m\ {\rm sf}\\(m,S)=1}}
 |A_U(m)W(Nm/D)|^2\gg_{W,S}1                 \tag{CL}
\]
for sufficiently large \(D\), uniformly in the high-window cutoff.
Here is an elementary count establishing that statement, included with
its distinct scope.

The Eisenstein element lattice has covolume \(\sqrt3/2\). Disk counting
with boundary error \(O(\sqrt x)\), division by the six units, and the
principal-ideal property of \(\mathbb Z[\omega]\) give
\[
 N_K(x)=\#\{\mathfrak a:N\mathfrak a\le x\}
       =\kappa x+O(\sqrt x),\qquad
 \kappa={\pi\over3\sqrt3}.
\]
For \(y\ge1\), finite inclusion-exclusion at the fixed primes in \(S\)
gives
\[
 N_{K,S}(y)=\kappa y\prod_{p\in S}(1-Np^{-1})
            +O_S(\sqrt y).
\]
Insert \(1_{\rm sf}(m)=\sum_{d^2\mid m}\mu(d)\).
The main series is
\(\sum_{(d,S)=1}\mu(d)/(Nd)^2
 =\zeta_K(2)^{-1}\prod_{p\in S}(1-Np^{-2})^{-1}\).
The summed lattice errors are
\(O_S(\sqrt x\sum_{Nd\le\sqrt x}(Nd)^{-1})
 =O_S(\sqrt x\log(2x))\); the tail of the main series contributes
\(O_S(\sqrt x)\). Thus
\[
 N_{{\rm sf},S}(x)=c_S x+O_S(\sqrt x\log(2x)),\quad
 c_S={\pi\over3\sqrt3\,\zeta_K(2)}
       \prod_{p\in S}(1+Np^{-1})^{-1}>0.
\]
Choose a fixed interval \([a,b]\subset(1,2)\) on which
\(|W|\ge\eta>0\). Counting columns with \(aD\le Nm\le bD\) and
using (CN) proves, for large \(D\),
\[
 D^{-1}\sum |A_U(m)W(Nm/D)|^2
 \ge {\eta^2 c_S(b-a)\over2}>0.
\]
The constant depends on the fixed profile and is not claimed to be
uniform among all smooth profiles of the same sup norm.

A lower bound for this coefficient norm cannot be combined with the
UPPER bound (RB) to produce a LOWER bound for row energy. The row
operator has no asserted lower singular value on the actual vector.
In particular (CL) neither refutes \(BT_\sigma\) nor proves the actual
energy reaches \(DX\).

## Sources and verification boundary

The external analytic input is unchanged: Blomer–Goldmakher–Louvel,
[L-functions with n-th order twists](https://arxiv.org/abs/1112.1650),
arXiv:1112.1650v1, Theorem 1.3, Lemma 2.1, section 3 and Appendix II.
The exact cached PDF SHA256 remains
1ab29e362c592b9f4078eb85e495ecce6a4665972e6427e7cc2ab0fb214e303b.
The accepted power-one/two extension and original full-mask transfer are
the prior reviewed inputs; no all-conductor theorem is substituted.

The adjacent deterministic checker tests the new window and its strict
boundary, a failure outside that window, the literal raw bilinear
identity and complex-conjugated covariance with common finite rational
profiles on actual balanced rows, the exact Fourier marginal
counterexample, and the exponent arithmetic. These are algebra and
bookkeeping diagnostics, not proof of an infinite analytic saving or of
a smooth-profile moment estimate. The count in section 5 is proved by
the displayed lattice and Möbius argument, not by finite diagnostics.

Only this attempt's exclusive planning/check directories were written.
The queue, production documents, original source, old outputs, worktree
progress, caches and environments are preserved. No dependency install,
MCP activation, authentication, model/GPU job, promotion, publication,
new Lean result, arithmetic energy lower bound, \(BT_\sigma\) proof,
or GRH conclusion is claimed.
