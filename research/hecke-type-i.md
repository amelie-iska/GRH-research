# Full-mask Hecke type-I expansion

Attempt: derive the exact squarefree type-I Euler ratio for the original
sextic family, then determine what scalar contour shifting actually proves.
Result: a complete primitive-factor restoration and scalar asymptotic with
explicit conductor/profile/divisor dependence, using classical degree-one
Hecke theory. Its elementary aggregate is insufficient for the original
short-row mean square. No GRH or spectral positivity conclusion follows.

## Definitions and exact restoration

K=Q(sqrt(-3)); nu is the original fixed finite-order Hecke character; S
contains6 and f_nu. For u!=0 construct the Kummer character of K(u^(1/6))/K
using arithmetic Frobenius, multiply nu, and take primitive psi_u BEFORE
introducing d. Its conductor Q_u=|D_K|Nf_u is independent of d. The primitive
square is a separate character psi_(u,2), not a pointwise square of a zero
sentinel at conductor-drop primes. Put T=S∪supp(u)∪supp(d).

F_(u,d)(s)=sum_sf(c),(c,T)=1 psi_u(c)/(Nc)^s
 = L(s,psi_u)/L(2s,psi_(u,2)) C_T(s), initially Re s>1.
C_T has numerator product_(p∈T,p∤f_u)(1−psi_u(p)q^(−s)) and denominator
product_(p∈T,p∤f_(u,2))(1−psi_(u,2)(p)q^(−2s)). Both products use the SAME
full deleted set. OutsideS a good p|u is ramified in psi iff6∤v_p(u), and
in its square iff3∤v_p(u). T still contains the prime in every case.
At p norm7,u=pi³, principalnu: primitive ratio48/49 at s1; correction49/48.
At u=pi⁶: ratio8/7; correction7/8. Both masked factors are exactly1.

Classical abelian reciprocity constructs the character; local tame Kummer
inertia gives exponent1 at ramified good primes. The finitely many local
sixth-power classes at primes above6 give a uniform wild bound. Thus
f_u divides c_nu product_(p|u,p∤6)p and Q_u<<nu Nu. The product is deliberately
NOT restricted to p∉S: extra fixed goodS primes can also ramify in u.
The reviewer caught and corrected that overstrong divisibility wording.

## Scalar contour with stated uniformities

For sigma=.5+delta,0<delta<.5, inverseL^T(2s,psi2) is bounded by
zeta_K(2sigma) from absolute Euler convergence, independently of character,
T and t. The remaining finite numerator is <<sigma,eps (NradT)^eps.
Classical Hecke continuation/functional equation and strip convexity give
L(s,psi)<< Q_u^((1−sigma)/2+eps)(1+|t|)^(1−sigma+eps), with the principal
pole removed during the strip argument. No zero-free hypothesis is inserted.
Four Mellin integrations by parts suffice after choosing internal losses
<min(eps/8,1/8); the profile constant is M4(W)=sum_(j<=4)sup|(x∂x)^jW|.
For Y>=1 the original inner sum is

  1_(psi=1) rho_T Y W_hat(1)
  +O(M4(W)Y^(.5+delta) Q_u^(.25−delta/2+eps)(NradT)^eps),

rho_T=Res zeta_K(1)/zeta_K(2) product_(p∈T)(1+1/q)^(-1).
This is proved prose using named classical external theorems; Lean checks
only the local/finite-product identities, not Hecke objects or the contour.

For U²<=D insert Y=D/Nd, keeping beta_U(d),nu(d),chi_d(u) and T(u,d).
The truncated factorization sum yields
sum_sf(d)|beta_U(d)|/(Nd)^(.5+delta−eta)
 <=(sum_(Na<=U)(Na)^(-.5−delta+eta))² << U^(1−2delta+2eta).
After the principal term P_u is extracted, the normalized error obeys

 |E_u| << M4(W)D^delta U^(1−2delta+eps)(Nu)^(.25−delta/2+eps).

Counting all nonzero lattice rows without quotienting units gives only
sum_(Nu<=H)|E_u|² << M4(W)² D^(2delta)U^(2−4delta+eps)H^(1.5−delta+eps).
At H=D^.75,U=D^a its power excess overH is3/8+5delta/4+(2−4delta)a,
positive for0<=a<=.5 and0<delta<.5. This is a losing UPPER envelope, not a
lower bound or impossibility result for the true error. We have closed the
scalar Euler/contour bookkeeping, not the averaging problem.

The uniform seminorm statement permits families with boundedM4; it does NOT
interchange a profile supremum and row energy. Holding U fixed while a new
scale D' decreases eventually violates U²<=D'; if D'<=U, the short2a_U term
can meet the annulus and must be restored. Signed covariance withII remains.

## Checks and external dependencies

Primary Milne CFTv4.03 Theorem0.8/ChapterI§1 and Kudla Tate notes selected
§3/§4/Thm4.3/Cor4.4 are pinned in planning/HECKE_TYPE_I_SOURCES.json.
Kudla's notes sketch parts of Tate's proof and have incomplete epsilon
formulas; these are not claimed as fully audited constants. The classical
completed Hecke theorem, finite-order vertical growth, Stirling and strip
principle are explicit external analytic inputs. General Artin holomorphy
is neither needed nor assumed.

Seven new Lean statements prove actual complex local/finite product identities
with independent primitive arrays at deleted primes. Actual ideal-symbol
finite diagnostics check1488 cases on93rows,128squarefree columns from7
split/inert prime ideals,78016nonzero terms and29120originalzero encounters.
An independent no-production-import oracle provides formal local and
squarefree support checks. Failed compile/layout attempts remain retained;
build staging protects the existing live editions.

NEXT: average the Mellin representation before taking pointwise convexity.
Keep the primitive numerator L(.5+delta+it,psi_u), its independently squared
primitive denominator, d-dependent deleted factors, actual beta_U and each
profile. A useful new result would be a specific uniform weighted second
moment for that ORIGINAL row family, including principal/residual classes,
with quantitative height/profile dependence. Do not assert a large-sieve
bound merely from a conductor upper bound or replace Kummer rows by arbitrary
primitive characters without proving multiplicity and weights. Any final
short-row estimate must also reassembleII−I and the short term at smaller
scales. The independent positive determinant/zero-location bridge stays open.

A logical distinction for the next research slice: the type-I squarefree
series involves L(s,psi)/L(2s,psi²), so numerator zeros are permitted zeros
of that series. Its classical continuation is not a zero-free theorem for
L(s,psi). The original Möbius series involves1/L(s,psi), whose poles at
zeros are a different analytic issue. Neither identification may be exchanged
with the other to infer GRH.
