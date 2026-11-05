# Exact varying-profile arithmetic unit/tower probe

This is a new finite arithmetic experiment with principal nu=1 and S the
Eisenstein primes above2,3. It does not import the earlier15-column fixture or
any learned checkpoint. It concerns a D-dependent family of common smooth
profiles, rather than the fixed-profile target or GRH.

For a good squarefree ideal m of rational norm N, rational prime factorization
of N determines its Mobius value and ideal-divisor norm MULTISET. A split
p=1mod3 may occur to exponent1 or2: exponent1 gives2 ideal choices; exponent2
gives the single ideal containing both conjugate primes and two norm-p
divisors. An inert p=2mod3 must have exponent2, giving one prime IDEAL of
norm p^2 and Mobius−1. Exclude rational2,3. No valid group is omitted.

With U^2=D and D<N<2D, the actual original coefficient is
A_U(m)=mu(m)(r_U(m)−1), where r counts all ordered ideal factorizations with
BOTH norms STRICTLY greater than U. Its swap symmetry makes r even, so A is
odd/nonzero. Each active norm group saves its multiplicity, Mobius sign,
individual prime-ideal norms, complete duplicated divisor-norm list and r/A.
Every rejected integer norm is saved by its exclusion reason.

The main literal unit is epsilon=1+omega, stored as(1,1) in the omega basis.
The actual sextic character is

    chi_m(epsilon)=zeta6^((N−1)/6).

Define one common complex smooth profile by

    phi(t)=exp(1−1/(1−t^2)) for |t|<1, zero otherwise;
    W_epsilon,D(y)=sum_activeN sign(A_U(N))*conj(chi_N(epsilon))
                                  *phi(4*(D*y−N)).

All finite node values are exact sixth roots, recorded by exponent and
zeta6 coordinates. The supports are disjoint and strictly inside(1,2), so
||W||infinity=1. For each fixed k the derivative bound is
(4D)^k ||phi^(k)||infinity. Derivative constants are NOT uniform in D.
At integer norms only the specified centre can contribute; no exponential
is numerically evaluated.

This profile simultaneously aligns every surviving coefficient on every
literal row u=epsilon*beta_v^6, with v an arbitrary ideal and beta_v any
associate generator. Its sixth power is independent of the chosen associate:

    chi_m(u)=chi_m(epsilon)*1_((m,v)=1),
    I_u=D^(−1/2)*T_v,
    T_v=sum_N allowed_multiplicity(N,v)*|A_U(N)|.

The original sixth-power raw-zero mask is essential. The primitive character
is the same nonprincipal order6 character for every v; all powers1..5 are
nonprincipal, since its value at a norm7 prime is zeta6. Thus P_u=0 in the
principal-nu scope. No exact conductor is asserted in this experiment.

V is NOT indexed by norm alone. The program independently enumerates every
ideal of norm<=64 by canonical unit associates and factors it into actual
prime ideals, without imposing squarefreeness. At a split p, let sigma_p be
the number of its two prime ideals dividing v, regardless of their exponents.
A norm-p column factor has2−sigma_p choices; a norm-p^2 split column survives
only for sigma_p=0. An inert norm-p^2 column survives only if its prime ideal
is absent from v. In particular the two prime squares at norm49 have
sigma7=1, while their product has sigma7=2. These have different raw masks.

The PRIMARY tower statistic is cumulative good-S v with Nv<=X, for
X=2,4,8,16,64, H=X^6. It always contains v=1. Secondary good-S dyadic
statistics use exactly [X/2,X) and explicitly report empty blocks. All small
ideal records, including those at S, remain available for mask diagnostics.
A separate capacity-matched probe uses H=floor(D^(3/4)), X=floor(H^(1/6));
for these modest D the cap is only2..4. Fixed-X64/H64^6 statistics are not
labelled as this capacity-matched range.

A real profile aligning the nonprincipal−1 unit is retained separately:
its node is sign(A_U(N)*chi4(N)). Its unit-row energy is the same exact
(sum_m|A_U(m)|)^2/D. The common unsigned nodal envelope V_D is also saved.
V_D ALSO VARIES WITH D and is never called a fixed-profile baseline.
The order6 comparator amplitude is complex and its exact norm uses
|a+b*zeta6|^2=a^2+ab+b^2.

The default D values are256,1024,4096,16384,65536 and the cheap optional
262144; U is the exact integer square root. Integer SPF arithmetic supplies
all norm groups. Small D256/1024 are independently compared with complete
primary Eisenstein ideal enumeration, the original A_U helper and direct
split/inert finite-field exponentiation. Every epsilon*beta_v^6 raw symbol
is compared to its exact mask. Small-D ordered coprime(m,n) pairs are
computed explicitly, with all A/W/character signs present. Their h1 values
are SELECTED-ROW contributions; no lower bound for the h1 component over
unselected rows is claimed. The full nonnegative row energy is at least the
selected-row energy, which dominates its h1 part in this aligned family.

Freeze sources BEFORE an accepted run, then use a fresh output directory:

```sh
PYTHONDONTWRITEBYTECODE=1 nice -n15 python3 examples/profile_uniformity/test_profile.py
PYTHONDONTWRITEBYTECODE=1 python3 examples/profile_uniformity/unit_profile.py --freeze-source-pin planning/signed-profile-20261105/implementation/source-freeze-v2.json
PYTHONDONTWRITEBYTECODE=1 nice -n15 python3 examples/profile_uniformity/unit_profile.py --source-pin planning/signed-profile-20261105/implementation/source-freeze-v2.json --output outputs/experiments/2026-11-05-profile-uniformity-v2
PYTHONDONTWRITEBYTECODE=1 python3 examples/profile_uniformity/unit_profile.py --verify outputs/experiments/2026-11-05-profile-uniformity-v2
```

Every file/helper source byte is hashed before/after, and helper source is
compiled from captured bytes rather than silently importing cached code.
Sources and exact inputs have immutable snapshots/hashes. Existing output
and pin files are refused; no previous experiment is overwritten. No seed
or randomness, dependency, model training, GPU, credential, toolchain, Lean,
production integration or publication action is involved.

Finite positive E/D and selected tower statistics do not by themselves prove
an asymptotic cD or cDX lower bound. Those require the separate squarefree
ideal/coprime tuple counting proof and its stated parameter ranges. This
experiment supplies exact finite data for that review. A uniform-in-varying-W
claim depending only on ||W||infinity is distinct from any fixed-W or
profile-derivative-dependent statement. No fixed-profile counterexample,
new general analytic saving, positivity/determinant bridge or GRH conclusion
is asserted.
