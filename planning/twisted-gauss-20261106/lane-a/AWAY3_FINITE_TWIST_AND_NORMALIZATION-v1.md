# Fixed finite twists away from 3: exact cube completion and moving-level norm

Research-only candidate v1, 6 November 2026. New mathematical derivation from the pinned Dunn–Radziwiłł general theta transform. It does not assert coverage of a general 3-ramified finite twist, the full actual kernel, or the current whole signed target. Independent review is required.

## 1. Precise admissible family

Let \(K=\mathbb Q(\omega)\), \(\lambda=1+2\omega=i\sqrt3\), and use the SAME primary generator \(1\bmod3\), additive trace pairing, cubic Gauss normalization and angular convention as Dunn–Radziwiłł arXiv:2109.07463v3. In particular
\[
 \widetilde g(c)=(Nc)^{-1/2}\sum_{x\bmod c}(x/c)_3e(\operatorname{Tr}(x/\alpha_c)),
 \quad \Theta_\ell(c)=(\alpha_c/|\alpha_c|)^\ell.
\]
Fix a nonzero integer \(\ell\). Fix a primitive finite multiplicative residue character \(\kappa\) modulo an ideal \(F\) COPRIME TO \(3\), extended by zero off its units. This means its values on the primary section are literally a character of \((\mathcal O/F)^\times\); no general 3-ramified character is being assigned this property. Its finite order need not divide six. Fix all these data before the moving level grows.

Let \(r\) be squarefree primary, \((r,3F)=1\). Let
\[
 \psi_r(x)=\overline{(x/r)_3},\quad
 \psi=\kappa\,\psi_r,\quad M=Fr,\quad R=Nr .
\]
The bar is chosen so that the moving part has the Gauss-times-Ramanujan evaluation below; conjugating the entire construction gives the opposite cubic convention. Both factors are primitive at their disjoint conductors, so \(\psi\) is primitive modulo \(M\). Hence its finite Fourier transform is supported on units, exactly as required in DR Corollary 5.1 and Proposition 5.1. The primary generator of \(M\) exists because \((M,3)=1\). Nothing here permits replacing a conductor by its radical.

Define for \(\Re z>1\)
\[
 R_{\kappa,r,\ell}(z)=
 \sum_{c\equiv1\bmod3}\widetilde g(c)\kappa(c)\psi_r(c)
       \Theta_\ell(c)(Nc)^{-z},
\quad
 L_M(w)=\sum_{(d,M)=1}\kappa(d)^3\Theta_{3\ell}(d)(Nd)^{-w}.
\]
The Gauss coefficient itself retains its squarefree zero and every moving \((c,r)>1\) zero. The fixed raw \((c,F)>1\) zeros are retained by \(\kappa\).

## 2. Exact replacement for the cubic-only conversion

Use the SAME theta coefficient subset \(S\) as DR (5.17), and define \(D_\psi(z)\) by DR (5.44), with this primitive \(\psi\). On its nonzero support,
\[
 \mu=\lambda^{-3}c d^3,\quad c,d\equiv1\bmod3,\quad \mu^2(c)=1,
 \qquad \tau(\mu)=3^{5/2}\widetilde g(c)|d|.
\]
Consequently, by absolute convergence when \(\Re z>1\),
\[
 \boxed{D_\psi(z)=
 3^{5/2+3z}\,\psi(\lambda)\,i^\ell\,
 L_M(3z-\tfrac12)\,R_{\kappa,r,\ell}(z).}                 \tag{1}
\]
Indeed \(\psi(\lambda c d^3)=\psi(\lambda)\psi(c)\psi(d)^3\),
\(\psi_r(d)^3=1\) on the retained unit set, and
\(\Theta_\ell(\lambda^{-3})=i^\ell\).
The inner \(d\) weight is exactly
\(\kappa(d)^3\Theta_{3\ell}(d)(Nd)^{-(3z-1/2)}\).
This proves (1) coefficientwise. It is not an appeal to the cubic-only step in DR Lemma 5.4: that step is precisely replaced by the displayed general Hecke factor.

In particular the completion is \(L_M(3z-1/2)\), NOT the untwisted zeta factor unless the actual character makes it so. The deleted primes in \(M\) remain deleted even if the primitive conductor of \(\kappa^3\) drops.

For \(\Re z>1/2+\eta\), \(L_M(3z-1/2)\) and its reciprocal are controlled by absolutely convergent Euler products, uniformly in squarefree \(r\) up to the customary \(R^\epsilon\) factors. This assertion uses \(3\Re z-1/2>1\), not a zero-free conjecture or a contour shift through zeros.

## 3. Exact finite local matrix; no hidden varying-level loss

Use the finite transform of DR (5.22)-(5.23):
\[
 (\mathcal T_M f)(u)=\sum_{x\bmod M}f(x)S_{1/3}(x,u;M).
\]
Its kernel is a finite sum over units \(a,d\bmod M\) with
\((\lambda^4a)(\lambda^4d)=1\bmod M\), cubic multiplier \((a/M)_3\), the stated unit factor \((\lambda/M)_3\), and additive phase
\(e(\operatorname{Tr}((xd+ua)/M))\).
These formulas define the matrix exactly, including its conjugation convention.

Choose the standard CRT idempotents
\(E_F=r(r^{-1}\bmod F)\) and \(E_r=F(F^{-1}\bmod r)\).
The additive phase factors with the primitive local additive characters
\[
 \epsilon_F^{(r)}(y)=e(\operatorname{Tr}(y(r^{-1}\bmod F)/F)),\qquad
 \epsilon_r^{(F)}(y)=e(\operatorname{Tr}(y(F^{-1}\bmod r)/r)).
\]
The congruence, the cubic multiplier and the input \(\psi=\kappa\psi_r\) factor under the SAME CRT identification. Therefore the full matrix is EXACTLY the tensor product of the two local matrices defined by these characters and the displayed local congruence, with the product of their explicit unit factors. Equivalently it is obtained from the usual local matrices by the unit permutations of rows/columns specified by these idempotents. No independence of characters or probabilistic average is used.

At the fixed \(F\) part there are only finitely many choices, indexed by \(r\bmod F\). The elementary estimate
\[
 \big|(\mathcal T_F^{(r)}\kappa)(u_F)\big|
       \le NF\,\varphi(F)                                      \tag{2}
\]
follows by counting its \(NF\) input states and at most \(\varphi(F)\) kernel states; all summands have modulus at most one. Keeping this finite transform itself, rather than its bound, preserves every local zero. The fixed character's conductor and the additive primitive character are never enlarged by fiat.

At the moving squarefree \(r\) part, sum over \(x\) first. Primitivity gives
\[
 \sum_{x\bmod r}\psi_r(x)\epsilon_r^{(F)}(xd)
   =\tau_{\epsilon_r^{(F)}}(\psi_r)\overline{\psi_r(d)} .
\]
The inverse relation \(a=\lambda^{-8}d^{-1}\) makes the cubic multiplier cancel the \(d\)-character, because \(\psi_r=\overline{(\cdot/r)_3}\). The remaining sum is a Ramanujan sum. Unit changes of \(u\) in a Ramanujan sum change neither its value nor its gcd with \(r\). Thus the moving factor is EXACTLY a unit scalar times
\[
 \tau_{\epsilon_r^{(F)}}(\psi_r)c_r(u_r),\qquad
 |\tau_{\epsilon_r^{(F)}}(\psi_r)|=\sqrt R .                 \tag{3}
\]
All scalar units are the ones in the matrix definition and the chosen primitive additive character; their moduli are one. Equations (2)-(3) prove the bound
\[
 |(\mathcal T_M\psi)(u)|\le NF\,\varphi(F)\sqrt R\,|c_r(u_r)|.
                                                                  \tag{4}
\]
This is a bound derived from an exact finite transform, not a replacement of that transform by a nonzero phase. In particular a fixed-\(F\) factor which vanishes is never divided out.

## 4. Quantitative dual absolute norm

DR Proposition 5.1 transforms the completed \(D_\psi\) into the same fixed combination of the \(F_1^\ast,F_{19}^\ast,F_{10}^\ast\) coefficient series, with \(\mathcal T_M\psi\) as its finite twist, angular order \(-\ell\), the exact modulus \(NM\), and the stated gamma quotient. This proposition requires Fourier support on units, already proved above. It does NOT require \(\psi^3=1\).

For every fixed \(\eta>0\), the absolute dual coefficient norm at real part \(1+\eta\) is
\[
 \ll_{\kappa,F,\ell,\eta,\epsilon} R^{1/2+\epsilon}.        \tag{5}
\]
Here is the moving-prime calculation rather than a sup-norm shortcut. Away from \(r\), DR's explicit theta coefficients (5.7),(5.13),(5.14) have squarefree part \(c\) and cube part \(d^3\); after taking absolute values their local series converges for real part \(u>1\). At a prime of norm \(p\mid r\), the extra Ramanujan weight in (4) is at most \(p-1\) only when that prime divides the coefficient index, and is otherwise one. Its extra local majorant is bounded by
\[
 1+(p-1)\left[p^{-u}
      +(1+p^{-u})\sum_{j\ge1}p^{j(1/2-3u)}\right].          \tag{6}
\]
It is bounded uniformly in \(p\) for each \(u>1\). Products of these factors cost \(C_u^{\omega(r)}\ll_{u,\epsilon}R^\epsilon\), not \(R\). The finitely many ramified theta states and \(F\)-primes change the fixed constant. The separate moving Gauss magnitude in (3) is exactly \(\sqrt R\), giving (5). No general weighted row-norm theorem is invoked.

It follows from (1), DR Proposition 5.1, the explicit gamma factors and (5) that the GENERALIZED cube completion
\[
 E_{\kappa,r,\ell}(z)=L_M(3z-\tfrac12)R_{\kappa,r,\ell}(z)
\]
has, for every fixed small \(\eta>0\), the left-strip estimate
\[
 E_{\kappa,r,\ell}(-\eta+i\tau)
 \ll_{\kappa,F,\ell,\eta,\epsilon}
 R^{1/2+O(\eta)+\epsilon}(1+|\tau|)^{2+O(\eta)}.           \tag{7}
\]
The modulus \(NM=NF\,R\) changes only the fixed constant. The angular entire transform in DR Proposition 5.1 and the fixed nonzero \(\ell\) justify strip interpolation. The absolute right line is bounded independently of \(r\). Hence the usual finite-strip convexity argument yields
\[
 R_{\kappa,r,\ell}(\tfrac12+\eta+i\tau)
 \ll_{\kappa,F,\ell,\eta,\epsilon}
 R^{1/4+O(\eta)+\epsilon}(1+|\tau|)^{1+O(\eta)}.           \tag{8}
\]
Division by \(L_M\) is performed only on this right-of-half line, where its Euler product and reciprocal converge absolutely. Statement (8) is a scoped quantitative fixed-finite-twist interface, not a whole actual-kernel estimate. The precise powers may absorb \(\eta\) into an arbitrarily small final epsilon. Fixed angular constants and fixed \(F\) dependence are retained.

Imprimitive fixed input can be decomposed into its inducing primitive finite character and FINITELY MANY exact exclusions at its dropped fixed primes. That extension has only fixed-size cost, but each original raw zero must be restored by that finite inclusion-exclusion. This is not permission to drop a moving deletion \(Q\).

## 5. A new exact normalization reduction for the actual Jacobi gauge

This reduction uses the already accepted construction of \(\Psi\) with conductor \(2\lambda\); it is not a new conductor claim or a repeat of the old phase controls. For a good primary generator \(\alpha_c\equiv1\bmod3\), the unit making \(\alpha_c\) congruent to \(1\bmod2\lambda\) is in \(\mu_3=\{1,\omega,\omega^2\}\), because \(\alpha_c\equiv1\bmod\lambda\). Its reduction is \((\alpha_c\bmod2)^{-1}\). Cubic reciprocity with the primary inert-prime generator \(-2\) gives
\[
 \chi_{3,c}(2)=\chi_{3,(-2)}(\alpha_c)=\alpha_c\bmod2
\]
under the standard identification \(\mathbb F_4^\times=\mu_3\); the numerator \(-1\) has cubic symbol one on these odd good columns. Therefore
\[
 \boxed{\vartheta(c)=\Theta_1(c)\overline{\chi_{3,c}(2)}.}  \tag{9}
\]
Combining (9) with the independently verified
\(G^{act}(c)=\chi_{3,c}(\lambda)G^{src}(c)\) gives, on the original good nonzero branch,
\[
 \vartheta(c)\overline{G^{act}(c)}\chi_{3,c}(t)
  =\Theta_1(c)\overline{G^{src}(c)}
          \chi_{3,c}\bigl(t(2\lambda)^2\bigr)
  =\Theta_1(c)\overline{\widetilde g(12t,c)}.              \tag{10}
\]
The last equality uses \((2\lambda)^2=-12\), the cubic symbol of \(-1\) being one, and \(\widetilde g(\mu,c)=\overline{\chi_{3,c}(\mu)}G^{src}(c)\). Thus the two specific finite corrections combine into an explicit fixed-S numerator \(12\); they are not two arbitrary characters to be ignored. All original further \(\nu\), source, \(\Gamma\), e/w and primitive-S factors remain.

Equation (10) is a general-frequency source Gauss object with a fixed 3-adic numerator, not yet the away-3 moving-level theorem (8): \(12t\) is not a good squarefree level. It does not permit inserting it in the good-\(r\) theorem unchanged. The exact reduction identifies which fixed ramified theta coefficient sector must be added.

## 6. Exact remaining 3-ramified equation

For a general fixed finite-order \(\nu\) and the original source family, no order-dividing-six assumption has been found or used. A finite 3-ramified part can have higher 3-power order. If \(\kappa_3\) is such a character, the naive DR twist \(\psi(\lambda^4\mu)\) with that ramified modulus can vanish identically on the desired support \(\mu=\lambda^{-3}cd^3\). It is therefore wrong to use (1) with \(\psi(\lambda)=0\) and cancel that value.

A genuine ramified extension must instead construct the fixed local vector of coefficient projectors
\[
 \sum_{\mu}\tau_j(\mu)\,
    \kappa_3(\lambda^3\mu)\,
    \kappa^{(3)}(\lambda^3\mu)\psi_r(\lambda^3\mu)
    \Theta_\ell(\mu)(N\mu)^{-z},
\]
on the precise integral-index sectors where these expressions are defined, and prove its Weyl/level transform, including all fixed cusp components and primitive e/w raw zeros. The required unmatched equation is an EXACT fixed-size local intertwining matrix for this vector whose moving-\(r\) dual absolute norm is still \(O_{\kappa,\eta,\epsilon}(R^{1/2+\epsilon})\). Finite-dimensionality or fixed conductor alone is not that equation. In particular, a fixed noncubic character is not automatically a linear combination of scalar cubic numerator characters: those scalar characters have exponent three, whereas the allowed finite character need not.

This is the remaining task even though new whole-HB-prefix localization may put all moving levels inside \(R<X^{1/2}\). No old large-deletion obstruction is asserted in that new sector. The bounded source normalization (10), the derived away-3 matrix (4), completion (1) and bound (8) are the surviving results of this attempt. The actual full finite-\(\kappa\)/ramified joint theorem, whole signed \(13/12\), global unsigned \(9/8\), determinant/zero-location, Lean and GRH remain unchanged.

Primary input: Dunn–Radziwiłł arXiv:2109.07463v3, PDF SHA256 df888f8527b3647a3428d6677a3e3070aab7439f79f737f3e894218fb64cfef0; extracted text SHA256 636da1119ebebdcab6756e9258554af06a42d67baf0c47026c73e960de2f4767. Equations and proofs read: (5.7),(5.13),(5.14),(5.22)-(5.25), Corollary5.1, Proposition5.1, Lemma5.4 and (5.69)-(5.70). No GRH-conditional prime result is imported. Existing private source bodies remain excluded from public closure; only separate citation metadata may be used later.
