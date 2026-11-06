# Required finite-S joint-selector refinement

6 November 2026. Bounded companion to LONG_DIVISOR_CUBIC_MEAN_ATTEMPT-v4.md,
SHA256 1a5634aa2d01aaa0a42bc8c3613c90d005e22b8f70a1b8d94ef5f99d278f4d12.
Read them together. This makes the finite-residue factorization used before
(3) explicit; independence of the old k variable ALONE would not imply it.
No quantitative estimate or completed formal control is changed or rerun.

## 1. Finite state before primitive-type selection

The accepted finite S/source package has a FIXED S-supported modulus c
(its allowed exponents depend on the fixed field, original nu, S, source/ray
data and the fixed original unit/S-supported u0, not D or the good column
conductors). Enlarge this fixed modulus to include all of its finite source,
ray and conductor-drop tests, and the O/4 Gamma state if desired. Let
H=(O/c)^times; a product of such fixed groups works identically.

For every good ideal m choose the SAME multiplicative primary1mod3
generator alpha_m used in v4 and put h_m=[alpha_m] in H. Then h_mn=h_m h_n,
including for overlapping good ideals. All these states are units because
the S primes are excluded from the good ideals. This statement does NOT
make arbitrary e/w into units: their separate primitive S values, including
zero at deleted primes, belong to the function below.

Freeze an original outer source/rho/e/w/s/k component and prefixes only
AFTER retaining its actual finite-type information. Before any d,a,b
separation, assemble its remaining joint finite-S/source/conductor-drop
selector into an actual bounded function

    f=f_(fixedouter): H x H -> C.

This includes the finite type partition, its root phase, and the SEPARATE
actual primitive S evaluations at e and w. A class with a forbidden
evaluation has value zero. If a primitive evaluation depends on which
conductor type was selected, keep that dependence in f; never replace it
by evaluation at the undeleted or induced modulus. The accepted package
provides a fixed uniform bound B_f for these finite functions and a fixed
total outer mass. No varying good-conductor group is inserted here.

On virtual overlapping m,n this is the chosen finite-state AUXILIARY
extension f(h_m,h_n), bounded on all H x H. It is not asserted to equal a
primitive Hecke root at an overlapping product conductor. Equality to the
original coprime kernel follows only after the full Mobius reconstruction
of v4(1), exactly as in v4.

## 2. Exact product Fourier expansion and its mass

For chi,psi in the full character group Hhat, define

    c_(chi,psi)=|H|^(-2) sum_(h,t in H)
                     f(h,t) conjugate(chi(h)) conjugate(psi(t)).
    f(h,t)=sum_(chi,psi in Hhat) c_(chi,psi) chi(h) psi(t).       (S1)

This is a finite exact identity. Character orthogonality gives

    sum_(chi,psi)|c_(chi,psi)|^2
       = |H|^(-2) sum_(h,t)|f(h,t)|^2 <= B_f^2,
    sum_(chi,psi)|c_(chi,psi)| <= |H| B_f.                    (S2)

Thus product-character refinement has a FIXED coefficient mass, independent
of D, d, a,b, K, the good conductors or any residual norm. If the originally
displayed finite package has several bounded components, sum their actual
masses; do not call that sum one. Every raw zero of f is retained by the
FULL sum (S1). Individual Fourier summands may be nonzero on such a class;
they are not individually called original nonzero rows.

## 3. The precise d phase

For m=p*d*a and n=r*d*b, apply (S1) BEFORE freezing a primitive S type or
separating residual coefficients. Each term factors EXACTLY as

    chi(h_m) psi(h_n)
      = chi(h_p) psi(h_r)
        [chi(h_d) psi(h_d)] chi(h_a) psi(h_b).                 (S3)

The prefix factor is fixed; the residual factors are unitary own-ideal
multipliers independent of d. The common d factor is chi(h_d) psi(h_d),
NOT generally a square. It is a square only when chi=psi or for a separate
explicit same-character factor. The coefficients c_(chi,psi) retain their
actual dependence on outer e,w/source/rho data and are bounded only after
the exact finite expansion.

Accordingly, the v4 phrases 'theta_S(alpha_d)^2' describe only an already
separable identical own-ideal multiplier. For a GENERAL joint finite-S
selector they are SUPERSEDED by (S1)--(S3), with its fixed total Fourier
mass kept outside v4(3). No general theta_S is assumed multiplicative.

The separate accepted linear-first rho(m)rho(n) factor still contributes
rho(d)^2. The separate Gamma(alpha_m alpha_n) Fourier factor still
contributes gamma(d)^2. Those genuine factors remain, together with
mu(d), the actual source gauges and all fixed good deletions. None is
replaced by one. For each Fourier component v4's gamma(d;k) may include
chi(h_d)psi(h_d) and the genuine rho/Gamma square factors, so its modulus
is at most one AFTER the scalar coefficient is kept outside. The residual
vectors X(a),Y(b) remain independent of d and satisfy their old absolute
envelopes. On the right vector use conjugate(psi(h_b)) in Y if needed to
match the displayed X(a) conjugate(Y(b)) convention.

Raw cubic entries still impose (d,a*b)=1. Separate common-prime e/w/k
zeros on d remain present; finite-state refinement does not restore any
prime dropped from a primitive conductor and introduces no (k,s) or (w,s)
mask. The finite refinement is performed before either Cauchy or any
positive enlargement.

## 4. Consequence and exact limitation

Equations v4(7)--(14) hold componentwise after (S3). Summation costs the
fixed actual mass (S2), included in the v4 fixed-data constant. The new
auxiliary long-divisor tail is unchanged:

    |P_long(>R0)| << M(W)^2 (D X A1)^eps A1 V I(c Lambda)
                       [D^(-1/2)+R0^(-2)+D^(-1/6)/R0].

This does not bound the unit or short-d Gauss mean and is not the missing
full original unit/short-k cancellation estimate. Whole signed13/12,
unsigned9/8 and GRH remain unchanged. The completed lane-b controls are
formal monomial/Mobius/Fraction checks, not actual character data; they
are not rerun or relabelled for this finite Fourier proof. No new
dependency, primary download, Git/index/global-document/publication,
environment, Lean, browser or production change occurs.
