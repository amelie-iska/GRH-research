# Exact 3-ramified theta coefficient projector; unproved Weyl closure isolated

Research-only companion v1, 6 November 2026. This is a new exact finite Fourier identity, not a completed ramified Type-I theorem. Read with AWAY3_FINITE_TWIST_AND_NORMALIZATION-v1.md. The primary is the pinned DR2109.07463v3 theta expansion (5.7), with \(\lambda=1+2\omega\), the different generator.

## 1. Definition on the actual integral index

Let \(\kappa_3\) be a fixed finite multiplicative residue character modulo \(\lambda^f\), extended by zero at nonunits; \(f\ge1\). Its order is arbitrary. The \(F_1=\theta\) coefficients have support in \(\lambda^{-3}\mathcal O\), so \(\lambda^3\mu\) is integral on that support. Define
\[
 \Theta_{\kappa_3}(z,v)=
   \sum_{\mu\in\lambda^{-3}\mathcal O\setminus\{0\}}
   \tau(\mu)\kappa_3(\lambda^3\mu)
           vK_{1/3}(4\pi|\mu|v)e(\operatorname{Tr}(\mu z)).
                                                               \tag{1}
\]
No artificial \(\kappa_3(\lambda)\) factor is inserted. In particular this is not the identically vanishing expression obtained by putting a ramified character into \(\psi(\lambda^4\mu)\) on the desired \(-3\) valuation sector.

Because \(\kappa_3\) is zero on nonunits, (1) retains precisely indices with \(v_\lambda(\mu)=-3\). For the theta expansion these are the actual \(\mu=\pm\lambda^{-3}cd^3\) branches with \(c,d\) prime to \(3\), including their genuine unit states. A claim about a single primary branch still requires its explicit unit/source selector; (1) does not silently choose that branch.

## 2. Exact finite translation formula and norm

Set \(q=N(\lambda^f)=3^f\). The perfect finite trace pairing on \(\mathcal O/\lambda^f\) is
\[
 [x,h]=e\!\left(\operatorname{Tr}\frac{xh}{\lambda^{f+1}}\right).
\]
Indeed the trace dual of \(\mathcal O\) is \(\lambda^{-1}\mathcal O\), so this is exactly the annihilator quotient pairing, not an unnormalized Euclidean pairing.

For \(h\bmod\lambda^f\) define normalized coefficients
\[
 b_h=q^{-1}\sum_{x\bmod\lambda^f}\kappa_3(x)
        e\!\left(-\operatorname{Tr}\frac{xh}{\lambda^{f+1}}\right).
\]
Finite orthogonality gives
\[
 \kappa_3(x)=\sum_h b_h[x,h],\qquad
 \sum_h|b_h|^2=q^{-1}\sum_x|\kappa_3(x)|^2\le1,\qquad
 \sum_h|b_h|\le\sqrt q.                                  \tag{2}
\]
Substitute \(x=\lambda^3\mu\). Then
\([x,h]=e(\operatorname{Tr}(\mu h\lambda^{2-f}))\), so the exact automorphic-function identity is
\[
 \boxed{\Theta_{\kappa_3}(z,v)=
       \sum_{h\bmod\lambda^f} b_h\,
           \theta(z+h\lambda^{2-f},v).}                 \tag{3}
\]
The constant terms on the right cancel because
\(\sum_hb_h=\kappa_3(0)=0\). For \(v>0\), Fourier convergence justifies the finite exchange. Equation (3) has a fixed coefficient mass at most \(3^{f/2}\), independent of the moving good conductor or norm length.

The sign in (3) corresponds to the negative sign in the definition of \(b_h\); using the opposite Fourier convention reverses both signs. The finite fractional translation is \(\lambda^{2-f}h\), not \(\lambda^{3-f}h\): the inverse different supplies the missing factor.

All fixed angular derivative operators used in DR commute with these fixed translations. Thus (3) also holds after the same angular differentiation on both sides. This proves exact coefficient selection, not an asserted angular functional equation or a global bound.

## 3. Precise remaining matrix equation

For a good moving squarefree primary level \(r\), one can now apply its cubic coefficient twist to the vector of the finitely many translates in (3). This retains the fixed character, the full primary unit selectors and all raw zeros before any analytic estimate. It does not prove that this translate vector is closed under the moving level/Fricke transform used in DR Lemma5.2 and Corollary5.1.

The missing theorem is an EXACT fixed-size ramified/cusp intertwining matrix for this coefficient-projected vector and its angular derivatives under that transform, including any additional necessary fixed rational cusp states, together with the quantitative assertion
\[
 \|\text{dual coefficient series at }1+\eta\|_{\rm abs}
       \ll_{\kappa_3,\eta,\epsilon}(Nr)^{1/2+\epsilon}.     \tag{4}
\]
The Weyl matrix must retain its actual dependence on the finite class of \(r\), its primitive e/w values and every conductor-drop zero. Merely saying that the conductor or the number of translations is fixed does not prove closure or (4). Inverting a translated theta function is a Möbius operation, not another translation by inspection.

Thus the defective naive ramified insertion has been replaced by a correct explicit finite local projector with a proved norm, but no full ramified quantitative Type-I theorem follows. The separately proved away-3 primitive-character interface is unchanged. New whole-HB-prefix localization can remove the old moving-level obstruction; it does not supply this missing local analytic equation. No actual full small-d/unit mean, whole exponent saving, Lean or GRH conclusion is claimed.
