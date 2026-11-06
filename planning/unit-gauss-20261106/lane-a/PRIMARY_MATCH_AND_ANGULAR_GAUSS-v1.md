# Primary cubic-Gauss inputs and the actual angular/deletion package

Research-only author note v1, 6 November 2026. Owned lane A of the unit-Gauss run. This is source matching and a quantitative remaining-interface calculation; it does not prove an actual signed-family estimate. The public 333-page release, canonical book, all environments and Git states are unchanged.

## 1. Object and acceptance criteria

The accepted Type-I transfer note 77660bde6a635d5de376e384f7570cee78a0f5dd981e01660ae22a948cbba48b requires
\[
 F_\psi(T;t;Q,I)=
 \sum_{\substack{\mathfrak v\ {\rm good\ SF}\\
                 N\mathfrak v\in I,\;(\mathfrak v,Q)=1}}
 \psi(\mathfrak v)\overline{G^{\rm act}_{\mathfrak v}}\,
 \chi_{3,\mathfrak v}(\alpha_t)
 W(N\mathfrak v/T)/\sqrt{N\mathfrak v}.
\]
The interval \(I\) is literal, not an implicitly smoothed substitute. The good squarefree frequency \(t=abuk\) varies; \(Q=\operatorname{rad}_{\rm good}(abunksw)\) contains the full original union and collision masks. \(Nw<64\); arbitrary \(s\), legal overlaps and all original source/ray/primitive-S data survive. This note never replaces \(Q\) by the primitive conductor, \(t\) by a fixed integer, or the actual character values by labels.

Acceptance means (i) pin/read actual primary theorem/proof interfaces, (ii) establish the exact normalization and angular mapping, (iii) identify which parameter ranges and masks a cited statement covers, and (iv) retain the first unmatched step explicitly. No prime-only asymptotic, cuspidal theorem, residue removal, or holomorphic continuation is being accepted as the required full bound.

## 2. Source objects and the exact normalization obstruction

The September 2026 OpenAI preprint uses
\[
 G^{\rm src}(c)=(Nc)^{-1/2}
       \sum_{x\bmod c}\chi_{3,c}(x)
           \exp(2\pi i\,\operatorname{Tr}(x/\alpha_c)).
\]
The source definition is in (1.1)/(2.1); its \(e(x)\) is \(\exp(2\pi ix)\). Our accepted \(G^{\rm act}\) uses the inverse-different pairing with \(\delta=1+2\omega\):
\[
 G^{\rm act}(c)=(Nc)^{-1/2}
       \sum_{x\bmod c}\chi_{3,c}(x)
           \exp(2\pi i\,\operatorname{Tr}(x/(\delta\alpha_c))).
\]
For a good column, \((c,\delta)=1\), so the literal change \(x=\delta y\) gives
\[
 G^{\rm act}(c)=\chi_{3,c}(\delta)G^{\rm src}(c),\qquad
 \overline{G^{\rm act}(c)}
 =\overline{\chi_{3,c}(\delta)}\,\overline{G^{\rm src}(c)}.       \tag{N}
\]
The fixed numerator \(\delta\) is S-supported. Its character is not set to one and is not a good squarefree level. This is already an additional finite twist before the other actual phases are inserted.

In ONE matched normalization, the accepted CRT identity is
\[
 \overline{G_{tv}}
 =\overline{G_t}\,\overline{G_v}\chi_{3,v}(\alpha_t)
 \quad ((t,v)=1).
\]
Thus the *bare source* angular summand
\(\Theta_\ell(v)\overline{G^{\rm src}_v}\chi_{3,v}(\alpha_t)\)
equals the source level coefficient
\[
 \Theta_\ell(t)^{-1}\overline{G^{\rm src}_t}^{\, -1}
        \Theta_\ell(tv)\overline{G^{\rm src}_{tv}}.
\]
The prefactor has modulus one on the nonzero good squarefree branches. It is the complex conjugate of the source angular family of order \(-\ell\), with a fixed unit scalar. This observation does not remove (N), the finite actual twists, or the full \(Q\).

The actual multiplicative factor has the form \(\psi=\Theta_\ell\kappa_0\), with its genuine finite part \(\kappa_0\) and raw zeros. The Jacobi gauge \(\vartheta\) has angular order 1. Fixed-numerator sextic/cubic symbols at \(e,w,u_0,\gamma_S\), finite source/ray characters, the mod-4 Fourier characters, and \(\theta_S(\alpha_v)\) have infinity type zero. A fixed generator change, primitive conductor drop or finite Fourier expansion changes those finite factors and scalars; it does not subtract one from an angular order. If the original \(\nu\) has angular order zero, the Jacobi angular order therefore remains \(1\), or \(-1\) after conjugation. If \(\nu\) has a nonzero angular order, the total order must instead be added explicitly; this note does not assume that a general fixed \(\nu\) cannot cancel it. A fixed norm twist can be included in a smooth radial weight, with its actual dependence retained.

## 3. Primary result that really addresses nonzero angular order

Dunn–Radziwiłł, arXiv:2109.07463v3 (14 May 2024), Proposition 5.2, treats squarefree primary \(r\), the cubic twist \((\cdot/r)_3\), and every integer \(\ell\). Its completed series
\[
 \zeta_K(3z-\tfrac12;1_r,3\ell)\,
 \sum_{c\equiv1\bmod3}
  \widetilde g(c)(c/r)_3\Theta_\ell(c)(Nc)^{-z}
\]
has its \(5/6\) pole only for \(\ell=0\); for \(\ell\ne0\) this completed object is entire. Proposition 5.3 gives the corresponding cube-completed Voronoi formula with the explicit indicator \(1_{\ell=0}\). These statements are unconditional parts of that paper. Its prime-bias theorems in the introduction are GRH-conditional and are not inputs here.

The distinction between the primal angular index and dual phases is essential. The source-level rewriting in the 2026 preprint, equation (A.5), has a dual phase
\(\Theta_{3\ell}(r)\Theta_{-\ell}(d^3\nu)\). This is a phase of the transformed coefficients, not a rule changing the residue indicator to a shifted primal index. Merely exhibiting such a dual phase cannot revive or remove an actual orientation mean.

There is a broader but still precisely specified statement in Dunn–Radziwiłł. Corollary 5.1 and Proposition 5.1 use a periodic finite twist whose finite Fourier transform is supported on units. Applying nonzero angular derivatives to that exact theta-transform family kills its constant terms, and the completed angular transform is entire. This explains why a finite periodic factor does not itself change the angular derivative into the zeroth derivative *within that covered family*. However, their conversion from this theta series to the displayed Gauss Dirichlet series, Lemma 5.4, explicitly assumes a primitive CUBIC character. The proof and its hypotheses must be supplied again for an additional noncubic or ramified finite twist. Proposition 5.1 alone is not the full actual Gauss-series conversion, nor is absence of a constant term a quantitative bound.

For \(\Re z>1/2\), the cubic completion's Euler factor has real argument \(3\Re z-1/2>1\); in that region its reciprocal can be controlled by absolute Euler products. This observation is local to the displayed cubic family, not a pole-free shift for an unrelated inverse-L series or the desired coupled signed integral.

## 4. Two neighboring primaries do not fill the finite-twist gap

A. Yoshimoto, *On the Cubic Theta Function*, Nagoya Mathematical Journal 105 (1987), 153–167, Theorem 2, does treat angular order together with a noncubic character. Its stated level is \(3r\), where \(r\) is a degree-one prime congruent to \(1\bmod9\); its character \(\alpha\) satisfies \(\alpha^3\ne1_r\) and the parity condition \(\alpha(-1)(-1)^\ell=1\). The completed transform is entire and has a functional equation. That is a real separate noncubic interface, but it does not state a squarefree composite growing-\(t\), full-union, sharp-interval estimate uniform in our parameters. It also explicitly excludes the cubic case \(\alpha^3=1_r\). No enlargement from this special prime level is performed here.

Alexander Dunn, arXiv:2403.13151v5 (22 October 2026), *Metaplectic Cusp Forms and the Large Sieve*, Lemma 1.4 and Theorem 1.5, concern Fourier coefficients of a FIXED CUSPIDAL cubic metaplectic form, with constants depending on that form. The paper's introduction distinguishes the noncuspidal cubic-theta/Gauss-sum case; §3.2 identifies the theta residual form separately. The actual Gauss coefficients are not obtained by declaring the theta residual form to be cuspidal. Those cuspidal Type-I bounds cannot be imported here.

## 5. New 2026 full preprint: useful bare theorem and exact limits

The pinned OpenAI paper, *An unconditional first moment for cubic Gauss sums*, 25 September 2026, is an actual full PDF at the immutable public repository commit recorded in PUBLIC-CITATION-v1.json; it is not an announcement used as a theorem. We read its defining conventions, imported level formulas, Type-I proof, fixed-angular appendix and the interfaces relevant here. This is not independent acceptance of every argument in the paper or of its prime theorem.

Its Appendix A fixes \(\ell\) before \(X\) grows. Proposition A.4, (A.8), compares a source angular Gauss sum averaged over squarefree levels \(r\), with arbitrary divisor-bounded coefficients \(a_r\), at \(RU\asymp X\), \(R\ll X^{51/100}\). The weights may depend on \(r\) but have fixed compact support and logarithmic derivative bounds uniformly in \(r\). The error is \(X^{5/6-1/100}\). For \(\ell\ne0\), the corresponding angular model is separately bounded by annular lattice discrepancy, not by replacing a discrete sum with a zero area integral.

Its (A.9) is an absolute-outer-sum, Mellin-height average. With derivatives fixed independently of \(X\), \(2\le H\ll X^{1/6+\rho}\), it bounds
\[
 \int_{|\tau|\asymp H}\sum_r |a_r|
 \left|\sum_u G^{\rm src}_\ell(ru)(Nu)^{i\tau}
                   W_r(Nu/U)\right|\frac{d\tau}{H}
 \ll_{\ell,\epsilon}X^{1/2+\epsilon}R^{3/4}H^{1/2}
\]
plus a zeroth-angular pole term. The latter is absent at \(\ell=\pm1\). The displayed theorem has neither an arbitrary additional finite multiplicative twist in \(u\), nor the full moving \(Q\) mask. Fixed order \(\ell\) is adequate for a genuine Jacobi order \(1\); uniformity in a growing angular order is neither stated nor needed for that narrow point.

Root has derived and is recording separately a sharp-interval consequence for the SOURCE COMPLETE BARE angular object, \(R\le X^{1/2}\). I independently checked the interfaces: half-integer norm thresholds preserve exact endpoint inclusion, norm-fibre multiplicity costs only \(X^\epsilon\), the truncation error is \(O(X^\epsilon(X/H+R))\), and (A.9) has exactly the absolute outer integral needed for \(r\)-dependent endpoint phases. At \(H=X^{1/12}\) the error is \(X^{11/12+\epsilon}\), or \(X^{5/12+\epsilon}\) after \(X^{-1/2}\) normalization. Low heights use (A.8) and the angular lattice model; the latter is \(O(X^{1/3+\epsilon}R^{1/2})\). No proof is duplicated here. In particular, sharp intervals are no longer listed as an unresolved interface for that bare source object. Our actual finite \(\kappa_0\), normalization (N), and full \(Q\) remain unmatched.

## 6. Exact moving-level obstruction after the required deletion

The accepted deletion is
\[
 F_\psi(T;t;Q,I)=
 \sum_{\substack{d\mid\operatorname{rad}Q,\;(d,t)=1\\Nd<2T}}
 \frac{\mu(d)\psi(d)\overline{G_d}
             \chi_{3,d}(\alpha_t)}{\sqrt{Nd}}\,
 F_\psi(T/Nd;dt;1,I/d).
\]
Subunit residual lengths retain their exact unit/empty rules. On the nonzero branches \(dt\) is squarefree. Its product parameter is exactly
\[
 (T/Nd)N(dt)=T\,Nt=D\,Nk .
\]
It is false that this invariance also preserves the level range: the LEVEL becomes \(Nt\,Nd\).

For \(Nk=D^\kappa\), \(0\le\kappa\le1/32\), the accepted bounds give
\[
 X=T Nt=D^{1+\kappa},\qquad Nt\le C D^{1/2+\kappa}.
\]
Even the smooth Proposition A.4 range would therefore only permit, at the worst admissible level,
\[
 Nd\ll D^{\, (51/100)(1+\kappa)-(1/2+\kappa)}
       =D^{1/100-(49/100)\kappa}.                         \tag{L}
\]
At \(k=1\) this allows a small \(D^{1/100}\) deletion window, but not every divisor of \(Q\). At \(\kappa=1/64\) the exponent is \(3/1280\), and at \(\kappa=1/32\) it is \(-17/3200\), so even the undeleted worst level can exceed that range. The crossover is \(\kappa=1/49\). Constants and finite dyadic covers do not change these powers.

Thus an \(NQ^\epsilon\) divisor count cannot justify applying a theorem outside its length range. The root's sharp bare consequence uses the stricter range \(R\le X^{1/2}\), so (L) is only a generous necessary comparison to the underlying smooth result, not a claimed transfer of the sharp result. The needed estimate is on the actual mean-retaining vector before opening/triangulating all these deletions, or a new quantitative extension handling the resulting larger levels together with the genuine finite twists.

## 7. Surviving result and next exact task

The primary matching has identified a real, strong source-object Type-I input and has ruled out a false cuspidal substitution. Nonzero Jacobi angular order is compatible with the source formula; finite factors do not automatically shift that order. The actual inverse-different normalization contributes the explicit extra character (N). Matching the full fixed finite package to a quantitative composite-level angular Gauss theorem is still required; merely quoting entireness of an auxiliary theta transform is insufficient. Independently, the full deletion shifts the level beyond the displayed range even while preserving the product parameter.

The next task is to prove the complete actual finite-twist conversion/uniform bound, or control the original jointly masked two-column vector without per-divisor absolute separation. It must retain finite \(w\), arbitrary legal \(s\), coherent means/equal-norm fibres, all common-prime/source/ray/capacity masks and the fixed common profile. No change to the whole \(13/12\) signed comparison, global \(9/8\) envelope, positive determinant/zero-location bridge or GRH conclusion follows.

All new downloads, reading-cache generation, edits and exact rational checks ran via SSH on iska-linux-vscode. Primary cache bodies and private download receipts are local-only and excluded from any public closure. No credentials, authentication, dependency, Lean, publication, environment, canonical product or Git mutation occurred.
