# Independent review of the rational-cusp angular interface

6 November2026. Lane B independently reviews lane-C candidate
RATIONAL_CUSP_CONSTANTS_AND_MELLIN-v1.md SHA256
e19cced215fe0eeaa6a51545538d51c5779f1c6735c7145a9284cb570312d7c4.
PASS for its exact rational matrix, constants, angular Mellin, primary
projector/completion and coarse general fixed-finite-character theorem.
Its last actual-family match and full DIRECT assembly are checked in
lane B's separate candidate, requiring its own independent review. This
is not a gate accepting all h1/global/GRH scopes.

The pinned unconditional DR Section5/table data were read directly:
Gamma2 automorphy and known character, all27cosets, known Fourier
coefficients/constants, and source angular Mellin Gamma normalization.
No GRH-conditional prime theorem or unavailable Patterson body is used.

1. Matrix and full-coordinate derivative. Direct multiplication gives
gamma^-1 U(A/C)=[[D,1/C],[-C,0]]=U(-D/C)W_(-C).
Its H3 action has z'=-D/C-barz/[C^2(|z|^2+v^2)] and
v'=v/[NC(|z|^2+v^2)]. At barz=0 the transformed z and v are constant
as functions of z, while barz' is affine in z. Pure positive angular
derivatives therefore act through ONLY the opposite angular derivative.
This holds at every order, with no lower derivatives from the height.

2. Constants and poles. The known j<=9constant pulls back to
chi(delta)sigma(NC)^(-2/3) v^(2/3)(|z|^2+v^2)^(-2/3).
It is radial; pure nonzero holomorphic/antiholomorphic derivatives at0
kill it. For ell0, direct endpoint integration gives residues
-C_infinity/2 at1/6 and+C_zero/2 at5/6. A zero total infinite constant
does not imply zero C_zero. The candidate retains this distinction.

3. Exact Mellin normalization. For ell>0 the derivative factor is
(-1)^ell barC^(-2ell) v^(-2ell). Substituting y=1/(NC*v) in the
v^(2s+ell-2) integral supplies
(NC)^(1-2s)(C/barC)^ell. The other angular sign is its corresponding
conjugate. Thus 1-2s, the angular phase and the sign are all correct.
Known cusp nonconstant coefficients at translate -D/C have precisely
unit-modulus additive phases; no unknown cusp coefficient is introduced.
The complete angular Mellin is entire because both endpoints decay
exponentially for fixed rational shift and ell!=0.

4. Actual primary index. Source tau has support inlambda^-3 O.
Phi(lambda^3mu), with Phi(x)=kappa_lambda(x)1_(x1modlambda^2), selects
EXACTLY S: other valuation sectors are nonunit; the negative n0 branch
is-1mod3; the positive n0 branch is1mod3. On S, x=c*d^3.
Multiplicativity on the primary section therefore gives kappa(c) and
kappa(d)^3, while moving cubic(d)^3 is the raw (d,t)=1 mask.
The 3^(5/2+3s)i^ell factor follows directly fromNlambda^-3 and its angle.
There is no kappa(lambda) zero to divide. All raw F/t/lambda Euler
deletions survive even if the genuine primitive conductor drops.

5. General finite Fourier normalization. For ANY bounded periodic
psi_M on the literal away periodM=F*t, normalized coefficient mass is
at mostsqrt(NM), whether primitive or imprimitive and whether F,t overlap.
The lambda fixed projection has mass at most3^(f/2).
The resulting rational shifts have reduced denominators dividing a
fixed lambda-power timesM, so NC<=Cfixed R. Nonunit Fourier residues
lower this denominator and need not be discarded. This is a new
all-rational construction, not an application of the old unit-support
theta corollary beyond its hypotheses.

6. Quantitative norm. Every one of the KNOWN27 cusp coefficient families
is a unit rotation/phase of tau,tau1,tau2 in DRAppendixA. Their explicit
lambda/c*d^3 formulas give absolutely convergent Dirichlet norm at1+eta;
lane B independently derives an explicit bound3^8 zeta_good(1+eta)
zeta_good(5/2+3eta) for0<eta<1/12. Hence the finite coefficient mass
sqrtR, denominatorfactorR^(1+2eta) and two-Gamma height quotient give
R^(3/2+2eta)(1+height)^(2+4eta). No unproved refined Ramanujan mass or
fixed-dimensionality shortcut is involved.

7. Convexity safety. The whole completed numerator, not the uncompleted
Gauss series, is entire and gets Phragmen--Lindelof first. The actual
L completion is divided ONLY where3Re(s)-1/2>1, by absolute Euler
products retaining raw omissions. The previously independently proved
sharp-Perron/convexity machinery then gives H(3/4,3/8), with trivial
fallback and literal subunit/unit extension. No zero-free strip/GRH is
assumed. Constants may depend on fixed conductor/character/angular
data; no all-finite-conductor uniformity is asserted.

Complex conjugating the WHOLE construction gives conjugateGauss roots
and opposite cubic/angular signs with unchanged absolute norm. The
actual fixed-family factor-list match and all original raw masks are
not replaced by an assertion about arbitrary bounded multiplicative
functions; they are a separate review dependency for the model result.

All work is SSH-Linux, owned paths, with primary bodies kept private.
No old controls, theta fixtures, tail/norm audits, builds, auth,
dependency, Lean, Git/index/canonical/global/publication/MCP changes.
