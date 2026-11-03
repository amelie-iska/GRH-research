# P6 actual persistence resolution — 2026-11-03

Concrete target: the complete ungraded free resolution of
M=k[x,y]/(x²,xy,y²), with actual MvPolynomial(Fin2) coefficients and
R-linear maps R²→R³→R→M. Kernel/image equality at R³ is load-bearing:
d²=0 alone is not exactness. Prove the presentation image is the stated
ideal, augmentation exact/surjective and the free terms projective. Products
of regular modules provide finite free coordinate modules, not scalar samples.

Derivation: x divides y²c in a relation x²a+xyb+y²c=0; regularity of y
modulo x twice yields c=xq. Cancellation of x gives
xa+yb+y²q=0. Regularity once more gives b+yq=xp, hence a=-yp.
This exhibits (a,b,c)=d2(p,q). Injectivity uses y≠0 and x≠0 in the
first/last coordinate. Regularity of the actual independent polynomial
variables is proved via finSuccEquiv and the zero constant coefficient
criterion for divisibility by Polynomial.X. No desired positivity is assumed.

Acceptance: warnings-as-errors on the new file and existing pinned suite,
printed types/dependencies and independent semantic review. Existing source
clones and environments stay unchanged. Preserve failed compilations as
diagnostic outputs. The worked module is not a claim of formalized general
staircases, graded minimality, CW realization, E-coefficient mapping cone,
derived categories, channel contractivity or the arithmetic GRH bridge.
Those remain separate obligations even if this interface task succeeds.

Implemented and independently compiled with19 printed dependency reports.
The full pinned wildcard suite passes262 reports (260 standard-foundation,
2 axiom-free). Added actual constant-coefficient residue action and universal
Hom boundary statements. An important elaboration failure exposed the global
coefficientwise MvPolynomial action after introducing the residue module;
explicit regularModule=Semiring.toModule fixes the intended free-module
multiplication. Separate rfl action identities guard that boundary. Ordinary
linear composition notation also fixes scalar-hom inference. Earlier failed
compiler logs are preserved and are not accepted verification evidence.
