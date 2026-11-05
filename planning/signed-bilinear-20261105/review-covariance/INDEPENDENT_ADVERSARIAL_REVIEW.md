# Independent adversarial review of the actual signed covariance case

5 November 2026. Remote-only review on iska-linux-vscode. This review covers the author script examples/arithmetic_cutoff/signed_covariance.py, its frozen root-covariance-v1/counterexample.json, and the high-window attempt named below. The accompanying manifest identifies exact bytes. The author's explanatory covariance proof note was not yet available when this review was written.

Verdict: **accepted within the stated finite scope; no arithmetic or algebraic error found**. Automatic nonnegative real covariance is false in the actual original Eisenstein ideal/sextic family, even for a real nonnegative common smooth weight and pointwise nonnegative \(C_U\mu\). No asymptotic energy saving or lower bound, \(BT_\sigma\) counterexample, new Lean theorem, arithmetic positive determinant or GRH conclusion follows.

## Independent implementation and complete phase agreement

check_independent_covariance.py imports only the Python standard library. It does not import the author's ring, ideal, phase, reciprocity or character helpers. It enumerates the Eisenstein lattice independently, represents each ideal prime to 6 by its unique generator \(a+b\omega\equiv1\pmod3\), factors those generators, and computes each sextic residue directly by exponentiation to \((q-1)/6\). Split residue fields use \(\mathbb F_{439}\) and \(\mathbb F_{19}\), with \(\omega=-a/b\); the inert field is \(\mathbb F_5[\omega]/(\omega^2+\omega+1)\), of order 25. Resulting field values are matched against the six images of the actual units \((1+\omega)^j\).

Every one of the 1,272 raw row/column character values agrees with the author's frozen report. All 1,272 direct column/row conjugation controls also pass. Both full **complex** Gram matrices, their Hermitian symmetry and real parts agree. All 12 profile-amplitude observations, energies, diagonal terms, off-diagonal terms and conjugated covariance identities agree exactly as rational numbers. This is stronger than agreement of the final real covariance alone.

The fresh independent command passed:

    PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 planning/signed-bilinear-20261105/review-covariance/check_independent_covariance.py --output outputs/checks/2026-11-05-signed-bilinear/review-covariance/independent-v1

The independent output records its own source hash, the author source hash and the author report hash. Every helper hash recorded inside the author report was separately compared with current source bytes and agrees.

## Profile and retained columns

Here \(D=400\), \(U=17\), \(\nu=1\), and \(S\) consists of the prime ideals above 2 and 3. The profile
\[
 W_x(y)=x\phi(4(400y-439))+\phi(4(400y-475))
\]
uses the standard flat bump \(\phi(t)=\exp(1-1/(1-t^2))\) for \(|t|<1\), zero outside. It is \(C^\infty\), nonnegative for \(x\ge0\), and supported strictly inside \((1,2)\). The support closures are
\([351/320,1757/1600]\) and \([1899/1600,1901/1600]\), which are disjoint. Since \(0\le\phi\le1\) and \(\phi(0)=1\), the sup norm at \(x=10\) is exactly 10.

At integer ideal norms, only 439 and 475 have nonzero weights. There are exactly four good squarefree ideals at those norms, and all four are retained. In the author's order their primary generators are
\[
 (-23,-18),\quad(-5,18),\quad(10,-15),\quad(25,15).
\]
The two norm-439 ideals are conjugate primes. The two norm-475 ideals are the inert norm-25 ideal times the two conjugate norm-19 primes. Thus the implementation includes all ideals selected by the single norm-dependent profile. No arbitrary isolated column or phase assignment is used.

Direct three-placement enumeration gives
\[
 A=(1,1,1,1),\quad C=(0,0,2,2),\quad\mu=(-1,-1,1,1).
\]
The high-window inequalities \(U^2\le D\), \(7U^2\ge2D\) hold, \(A=C-\mu\), and \(C_j\mu_j\ge0\) at every retained column. The normalized ordinary coefficient norm is
\[
 D^{-1}\sum |A_jW(Nm_j/D)|^2=(100+100+1+1)/400=101/200.
\]
This is not a row-energy lower bound.

## Complete balanced block and finite covariance

There are exactly four good squarefree ideals in \([7,14)\), the two primes over 7 and the two over 13. Distinct ordered pairs and all six literal units give precisely 72 distinct rows \(\varepsilon a_1a_2^2\); no chosen row subfamily replaces this complete \(B_7\). Their maximum norm is 2197. Each row has outside-\(S\) prime valuations 1 and 2, so tame Kummer theory makes its primitive character nonprincipal. The original principal residue is therefore zero on the entire block.

The Gram convention independently checked is
\[
 G_{jk}=\sum_{u\in B_7}x_{m_j}(u)\overline{x_{m_k}(u)}.
\]
In particular
\[
 \Re G=\begin{pmatrix}
 72&0&0&18\\0&72&18&0\\0&18&72&0\\18&0&0&72
 \end{pmatrix}.
\]
For the real weights \(w=(x,x,1,1)\), this yields
\[
 \Re Q_{B_7}(C,\mu)=\frac{18}{25}-\frac9{50}x.
\]
At \(x=10\) its value is \(-27/25\), while the diagonal covariance is \(18/25>0\) and the off-diagonal covariance is \(-9/5\). The energies are
\[
 Q(A,A)=954/25,\quad Q(C,C)=36/25,\quad Q(\mu,\mu)=864/25.
\]
They satisfy \(Q(A,A)=Q(C,C)+Q(\mu,\mu)-2\Re Q(C,\mu)\). Thus both the sign and the conjugation/normalization have been independently verified.

This complete \(B_7\) is not claimed to lie below \(H=\lfloor400^{3/4}\rfloor=89\); its separate maximum norm is explicit. It is a finite balanced-block sign counterexample, not a \(BT_\sigma\) counterexample or evidence for an asymptotic lower energy.

## Separate guaranteed nonprincipal rows below H=89

The second row set consists of every literal \(0<N(u)\le89\) whose remainder after stripping the primes above 2 and 3 is nonunit. It has 246 rows and maximum norm 84. Because the least good prime norm is 7 and \(7^3>89\), every nonzero outside-\(S\) valuation in this set is 1 or 2. At least one such prime exists for each selected row, so all rows are guaranteed nonprincipal. The set is not asserted to exhaust all nonprincipal rows; \(S\)-unit rows can require a separate character analysis.

There are 60 exact raw zeros in its four-column table. They remain zero. The independently reproduced covariance is \(-69/50\), with positive diagonal \(54/25\). Its energies also match the report. This is a distinct finite covariance example inside the short literal norm range, not a complete balanced block and not an all-nonprincipal-row energy claim.

## Review of the high-window attempt

I also read planning/signed-bilinear-20261105/attempt/HIGH_WINDOW_BILINEAR_ATTEMPT.md, its checker and handoff, and reran its checker to a fresh file in the review namespace.

The reduction is correct: if \(a,b\) are long and a complementary good ideal \(c\) is nonunit, then \(N(abc)>7U^2\ge2D\). The strict factor cutoffs handle equality of the window endpoints. Hence \(C_U=\mu r_U\), and swapping the ordered coprime factors is fixed-point-free, so \(r_U\) is even and every active coefficient \(A_U=\mu(r_U-1)\) is odd with modulus at least 1.

The coefficient-density proof is also correct. The Eisenstein lattice count divided by six units gives \(\kappa=\pi/(3\sqrt3)\). Finite \(S\)-exclusion and squarefree Möbius inversion yield the stated positive density and error \(O_S(\sqrt x\log(2x))\). A fixed interval where a fixed nonzero smooth \(W\) is bounded away from zero gives the ordinary coefficient-norm lower bound uniformly in the high-window cutoff. Its constant depends on that fixed profile; it gives no lower singular-value bound for the row operator and no row-energy lower bound.

The factorwise Cauchy/BGL algebra is consistent:
\[
 \frac{A^2B}{D}X\{X+B+(XB)^{2/3}\}
 \asymp AX^2+DX+D^{2/3}A^{1/3}X^{5/3}.
\]
At \(A,B\asymp\sqrt D\), \(X\asymp D^{1/4}\), its exponents are \(1,5/4,5/4\); the previously accepted recombined bound is stronger and still has \(5/4\). The abstract Fourier-array example correctly disproves the generic inference from two marginal second moments to an independent shared-row product estimate. It is not claimed to be an arithmetic family. These facts establish only that the displayed estimates do not prove a \(D^\sigma\) saving. They do not prove that every possible use of BGL/arithmetic must fail.

The fresh author-checker rerun passed 753 high-window cases, 148 equality-window cases, 720 literal bilinear/complex covariance cases and 64 rational exponent cases. Its complete output is outputs/checks/2026-11-05-signed-bilinear/review-covariance/high-window-rerun-v1.json. These finite checks complement the displayed proof; they do not certify an analytic inequality.

## Review boundary

No production, queue, publication, authentication, environment or dependency action was performed. Only the review's exclusive planning/check namespaces were created. Existing outputs were not overwritten. No Lean compilation or global analytic/GRH test was attempted; this review contains no new such claim.
