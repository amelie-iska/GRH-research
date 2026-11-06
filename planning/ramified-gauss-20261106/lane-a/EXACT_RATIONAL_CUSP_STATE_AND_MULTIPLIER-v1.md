# Exact rational-translate cusp reduction and Kubota phase algorithm

Research-only candidate v1, 6 November 2026. This proves an exact one-step closure of the actual fixed finite Fourier translate family into fixed affine transforms of the known 27 integral theta cusps. It does not infer pole behavior or a dual Dirichlet bound merely from the number of states. Those are separate analytic questions.

## 1. Source group and exact cusp basis

Use the pinned DR2109.07463v3, (5.1)–(5.16), Corollary5.1 and AppendixA. Put \(\mathcal O=\mathbb Z[\omega]\), \(\lambda=1+2\omega\),
\(\Gamma=\mathrm{SL}_2(\mathcal O)\),
\(\Gamma_1(3)=\ker(\Gamma\to\mathrm{SL}_2(\mathcal O/(3)))\), and
\(\Gamma_2=\mathrm{SL}_2(\mathbb Z)\Gamma_1(3)\).
Its index in \(\Gamma\) is 27. The cubic theta is a weight-zero function on hyperbolic three-space with
\(\theta(gw)=\chi(g)\theta(w)\) for \(g\in\Gamma_2\).
The multiplier is independent of \(w\) and is an actual cube root of unity.

Here is an exact computable phase rule, including for a nonprincipal integral cusp. Choose one integral representative \(\gamma_j\) for each LEFT coset \(\Gamma_2\backslash\Gamma\), \(1\le j\le27\), and set \(F_j=\theta|\gamma_j\), where \((F|g)(w)=F(gw)\). For any \(\gamma\in\Gamma\), choose the unique \(j\) with
\[
 g=\gamma\gamma_j^{-1}\in\Gamma_2 .
\]
Choose \(\sigma\in\mathrm{SL}_2(\mathbb Z)\) having the SAME reduction as \(g\) modulo3. Such a lift exists by the defining equality for \(\Gamma_2\). Then
\[
 \delta=\sigma^{-1}g=
 \begin{pmatrix}a&b\\c&d\end{pmatrix}\in\Gamma_1(3),\qquad
 \boxed{\theta|\gamma=\chi(\delta)F_j,\quad
 \chi(\delta)=
 \begin{cases}(c/a)_3,&c\ne0,\\1,&c=0.\end{cases}}          \tag{1}
\]
The denominator \(a\equiv1\bmod3\) is nonzero and \((a,c)=1\); the ordinary cubic Jacobi symbol is well-defined. This is exactly DR (5.4) and \(\chi|\mathrm{SL}_2(\mathbb Z)=1\), not an unknown sign set to one.

A finite representative algorithm is to use the generators \(P,T,E\) from DR (5.1) and breadth-first traversal of the 27-state permutations in its AppendixA, starting at the identity. A 24-element traversal of \(E,T\) modulo3 gives the rational \(\sigma\) lifts. This fixes actual integral matrices and words, not just labels. If these word representatives differ from the published representatives, the corresponding functions differ by the fixed multiplier prescribed by (1). Their published \(\tau,\tau_1,\tau_2\) coefficient formulas acquire that fixed unit; it remains part of the exact state. In an absolute coefficient bound its modulus is one, rather than a new unknown cusp coefficient bound.

## 2. Exact identity for an arbitrary reduced rational translate

Write
\[
 U(z)=\begin{pmatrix}1&z\\0&1\end{pmatrix},\quad
 W_r=\begin{pmatrix}0&-1/r\\r&0\end{pmatrix},\quad
 A_z=\operatorname{diag}(z,z^{-1}).
\]
Let \(\beta=A/C\in K\) be reduced: \(A,C\in\mathcal O\), \(C\ne0\), \((A,C)=1\).
Choose ANY \(D,B\in\mathcal O\) with \(AD-BC=1\), and set
\(\gamma=\left(\begin{smallmatrix}A&B\\C&D\end{smallmatrix}\right)\).
Direct multiplication gives
\[
 U(A/C)W_C=\gamma U(-D/C),\qquad
 \boxed{U(A/C)W_r=\gamma U(-D/C)A_{r/C}.}                 \tag{2}
\]
There is no omitted metaplectic factor: this is a matrix identity, and the subsequent evaluation of the integral \(\gamma\) uses the EXACT constant multiplier (1).

In the actual finite Fourier family, after splitting the fixed support overlap \(q_0\), the reduced denominator has the form
\[
 C=c_0r,\qquad (c_0,r)=1 ,
\]
where \(r\) is the moving good squarefree level and \(c_0\) ranges over a FIXED FINITE set of generators supported on the fixed local modulus. This is because the moving inverse-cubic Fourier transform is supported on units modulo \(r\); the numerator of each Fourier translation therefore cannot cancel any prime of \(r\). Cancellation can occur only at the fixed modulus. In particular \(NC\ll_{\rm fixed}Nr\), but \(C\) is not falsely declared squarefree or unramified.

Choose \(b\) representing
\[
 b\equiv D r^{-1}\pmod{9c_0},
 \qquad d=\frac{D-br}{9c_0}\in\mathcal O.
\]
These are exact equalities, with \(b\) in a fixed finite residue set. Then
\[
 -D/C=-b/c_0-9d/r .
\]
Keep the order in (2). Since \(U(t)A_z=A_zU(t/z^2)\), it follows that
\[
 \boxed{\theta|U(\beta)W_r
   =\chi(\delta)\,
       \underbrace{F_j|U(-b/c_0)A_{c_0^{-1}}}_{\mathcal F_{j,c_0,b}}
           \bigm|U(-9c_0^2d/r).}                         \tag{3}
\]
Thus the output cusp index \(j\), fixed denominator \(c_0\), and fixed residue \(b\bmod9c_0\) lie in an explicit FINITE family. The remaining translation has the growing denominator \(r\) and its actual numerator; it is not discarded. Formula (3), with (1), is the requested exact one-step local/cusp matrix entry. No assertion that a fixed-dimensional space automatically has a bounded intertwining operator is used.

All coefficients of that finite matrix are either the literal original finite Fourier coefficients, the primitive moving Fourier coefficients, or the actual unit \(\chi(\delta)\) in (1). They may depend on the moving Fourier variable; that dependence is retained. A coarse triangle bound is allowed only AFTER this exact identity has been established.

## 3. Primitive lambda-character specialization and diagonal order

For a primitive \(\lambda^f\) character with \(f\ge3\), put \(B_0=f-2\). The primary-sector selector \(1_{x\equiv1\bmod3}\) may be refined into fixed characters modulo3; each resulting primitive \(\lambda^f\) character still has unit-supported finite Fourier transform. A single translate can therefore be written
\[
 \beta=\frac{h}{\lambda^{B_0}}-\frac{\lambda^4a}{r}
       =\frac{n}{q},\quad
 n=hr-\lambda^{B_0+4}a,\quad q=\lambda^{B_0}r,
 \quad (h,\lambda)=(a,r)=1 .
\]
Here \((n,q)=1\) exactly, including at \(\lambda\). Choose
\(y=n^{-1}\bmod9q\), \(x=(ny-1)/q\), so \(9\mid x\), and
\(\gamma=\left(\begin{smallmatrix}n&x\\q&y\end{smallmatrix}\right)\in\Gamma\).
Then (2) reads
\[
 U(n/q)W_r=\gamma U(-y/q)A_{\lambda^{-B_0}} .
\]
Choose \(b\equiv yr^{-1}\bmod\lambda^{B_0+4}\).
Because \(n\equiv hr\bmod\lambda^{B_0+4}\),
\[
 b\equiv h^{-1}r^{-2}\pmod{\lambda^{B_0+4}},
\]
independent of the moving Fourier variable \(a\). Also \(\gamma\bmod3\), hence its cusp coset, is independent of \(a\). This displays a particularly small explicit lambda-state update.

The exact ordered output is
\[
 F_j|U(-b/\lambda^{B_0})U(-\lambda^4 d/r)A_{\lambda^{-B_0}} .
\]
If the fixed state is defined INCLUDING the diagonal, the moving translation to its RIGHT becomes
\(U(-\lambda^{4+2B_0}d/r)\).
It would be incorrect to retain \(-\lambda^4d/r\) after commuting across that diagonal. The additional fixed lambda-unit factor changes actual Fourier phases and is retained.

The general reduction (2)–(3) does not require this primitive specialization. In particular it handles low conductors, nonunit fixed Fourier indices and mixed fixed-away/lambda denominators after reducing their fractions. It avoids an unjustified inverse modulo \(9q\) when the numerator is not a lambda-unit.

## 4. What the exact state identity permits analytically

Every output state in (3) is an explicitly fixed translation and fixed diagonal scaling of a known integral theta cusp \(F_j\). Its Fourier coefficients are therefore the published \(\tau,\tau_1,\tau_2\) coefficients, with their exact unit, index scaling and unit-modulus translation phase. Any analytic estimate must still prove the appropriate absolute Dirichlet norm of those coefficients. The transformation of its constant term and angular Mellin integral must likewise be computed, rather than inferred from the finite number of states.

The moving normalized primitive Fourier coefficients have total mass \(\ll_{\rm fixed}\sqrt{Nr}\); all other finite Fourier masses are fixed. The factor \(NC\) in a per-translate Mellin relation satisfies \(NC\ll_{\rm fixed}Nr\). These are the quantities entering the coarse \(R^{3/2+\epsilon}\) route investigated separately by lanes B/C and root. This note does NOT itself replace that Mellin calculation, establish a pole-free transformed numerator, or assert a full original signed target.

The exact matrix retains original finite unit/source/ray selectors, the real primitive e/w evaluations and their zeros, arbitrary fixed finite-order \(\nu\), and the original moving inverse-cubic orientation. Fixed Fourier summands can be nonzero on an originally forbidden local class; ONLY their full finite sum recovers that zero. No such summand is individually renamed an original nonzero row. No \(\psi(t)\) value is divided out.

The primary is DR arXiv:2109.07463v3, PDF df888f8527b3647a3428d6677a3e3070aab7439f79f737f3e894218fb64cfef0, extracted text636da1119ebebdcab6756e9258554af06a42d67baf0c47026c73e960de2f4767. Its conditional prime theorems are not inputs. Full primary bodies/private local pins stay excluded from public closure. Whole signed13/12/global9/8, Lean and GRH conclusions are unchanged by this exact geometry note.
