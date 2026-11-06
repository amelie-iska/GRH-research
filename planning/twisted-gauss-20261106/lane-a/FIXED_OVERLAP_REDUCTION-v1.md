# Fixed support overlap: exact reduction without evaluating or dividing by kappa(t)

Research-only companion v1, 6 November 2026. This supplies the fixed-overlap bookkeeping for AWAY3_FINITE_TWIST_AND_NORMALIZATION-v1.md. It does not enlarge that theorem to general 3-ramified characters.

Let the fixed finite denominator-character modulus \(F\) be coprime to \(3\). A moving squarefree frequency \(t\) need not be coprime to \(F\). Put
\[
 t=q_0r,\qquad q_0=\prod_{\mathfrak p\mid(t,F)}\mathfrak p,\qquad (r,F)=1 .
\]
There are only \(2^{\omega(F)}\) possibilities for \(q_0\); no original legal k/w overlap is deleted by this partition. All primary generators are the same multiplicative section.

For the unconjugated source orientation use the actual direct column coefficient
\[
 \kappa(c)\overline{\chi_{3,c}(t)}
 =\left[\kappa(c)\overline{\chi_{3,c}(q_0)}\right]
                       \overline{\chi_{3,c}(r)}.         \tag{1}
\]
No value of \(\kappa(t)\) occurs. In particular (1) remains valid if \(t\) meets the fixed character's conductor and \(\kappa(t)=0\). The bracket has a fixed finite denominator-character realization modulo \(F\) on the primary section, by cubic reciprocity; its primitive inducing conductor \(F_0\) may drop, but the ORIGINAL \((c,F)=1\) mask is retained.

Write that bracket as \(\kappa_0(c)1_{(c,F)=1}\), where \(\kappa_0\) is primitive modulo \(F_0\mid F\). Let \(J\) be the product of the fixed primes dividing \(F\) but not \(F_0\). Since \(\kappa_0\) already vanishes at the \(F_0\)-primes,
\[
 \kappa_0(c)1_{(c,F)=1}
   =\kappa_0(c)\sum_{h\mid J,\ h\mid c}\mu(h).             \tag{2}
\]
This is a FINITE exact sum, not a moving conductor divisor bound. Original c-squarefreeness gives \(c=hv\), with \(h\) squarefree and \((h,v)=1\). The Gauss CRT identity splits the h-summand into its direct scalar
\(\mu(h)\kappa_0(h)\widetilde g(h)\overline{\chi_{3,h}(r)}\Theta_\ell(h)\)
and a v-series with a fixed additional cubic numerator factor at \(h\), together with the exact rescaled interval/profile. If a scalar is zero it remains zero and is never divided out. The cubic factor itself has the raw \((v,h)>1\) zero, so no original squarefree collision is restored.

The new fixed finite character is the product of \(\kappa_0\) and this primitive cubic character at \(h\), with disjoint conductors \(F_0,h\). Thus it is primitive modulo \(F_0h\), still coprime to 3. The moving \(r\) is coprime to every one of these fixed moduli. This is an admissible member of the away-3 family. All h choices, norm scalings, profiles and character moduli form one fixed finite family, independent of the growing conductor.

Equations (1)-(2) prove the overlap reduction. They do not prove that an arbitrary additional 3-ramified finite factor has disappeared, and they do not expand the full moving union mask Q. The raw fixed zeros are recovered only by the FULL finite h-sum. The conjugate source orientation is obtained by conjugating the entire identity and its profile.
