# New complete-column signed-divisor experiment

This isolated standard-library CPU implementation belongs to P7 claim a2373086-375f-4dd7-92a8-f211c286e55f. It computes the ORIGINAL h=1 coprime sum, at principal nu=1 and S the primes above2,3, for all squarefree good annular ideal columns and an explicitly declared actual row block. It does not rerun the old selected-q fixture or prove an asymptotic saving/GRH statement.

Write X in {A_U,C_U,mu}. For each squarefree ideal divisor d of at least one column, including d=1 and d=m, it executes
F_d^X(u)=sum_(m,d|m) X_U(m) chi_m(u) W_delta(Nm/D),
Z_d^{XY}=sum_u F_d^X(u) conjugate(F_d^Y(u)).
Expanding ordered column pairs gives sum_d mu(d) Z_d^{XY}=D S_1^{XY}, by sum_(d|gcd(m,n))mu(d)=1_(m,n)=1. X already has its original signs; no extra mu(q) is inserted. The linear-first omega convention is used: omega²+omega+1=0; conjugate(a,b)=(a-b,-b), squared absolute value a²-ab+b².

The common profile is chosen ONCE for this experiment: delta=1/240000; s(t)=0 for t<=0, exp(-1/t)/(exp(-1/t)+exp(-1/(1-t))) for0<t<1, and1 for t>=1; W_delta(y)=s((y-1)/delta)s((2-y)/delta). For integer1<D<=60000, every strict integer norm node is at least1/D>=4delta from the endpoints, hence W=1 exactly there, while W=0 at D,2D. No exponential or floating-point approximation is executed. The code rejects D>60000. The fixed kth derivative cost is O_k(240000^k), potentially enormous. This is a DIFFERENT global profile from the old broad-plateau fixture, even though its two selected nodes also had weight1. It is neither a varying-profile counterexample nor evidence for a bounded-seminorm uniform asymptotic target.

Complete support is built from an SPF ledger of every integer N in[D,2D]. Split rational primes may have exponents0,1,2; exponent1 gives two distinct ideal choices, exponent2 gives both conjugates once. Inert primes must have exponent0 or2; an inert p² is one ideal prime with mu=-1. Primes2,3 and repeated ideal primes are excluded. Every split primary generator is found by bounded exact lattice enumeration and the expected pair of embeddings is checked. The direct original A and C convolutions assign each ideal prime to the ordered a,b,c factors, use their actual individual norms and cutoff U, and retain all signs. Only afterwards does the program verify A=C-mu and the applicable C=mu*r_U identity.

Small row blocks are pure v1: primary1mod3 squarefree good v1 in[A1,2A1), v2=1, other factors1, literal unit1. D144/U12/A1=13 has H41; D576/U24/A1=37 has H117. In the large case D60000/U244/A1=37/A2=7/H3833, exactly the20 old frozen row arrays are reused after NEW independent block enumeration matches them. All their new annular column symbols are evaluated. Prime factors of v1 have valuation1 outsideS, proving these rows nonprincipal; no primitive-conductor claim is made. Raw zeros delete only the colliding column/row value, not the entire row or a primitive conductor.

Each accepted run snapshots every implementation/helper byte before arithmetic and checks the same source hashes after arithmetic. Helpers are loaded from captured bytes into new modules; no old main/run/test is invoked and pycache is disabled. Old JSON inputs are immutable row and two-column submatrix controls only. Output directories refuse overwrite.

## Run commands

From the repository root:

    PYTHONDONTWRITEBYTECODE=1 python3 planning/signed-divisor-20261105/full-column/test_full_column_v1.py
    PYTHONDONTWRITEBYTECODE=1 python3 planning/signed-divisor-20261105/full-column/full_column_v1.py --D 144 --U 12 --A1 13 --A2 1 --literal-pairs --out outputs/experiments/2026-11-05-signed-divisor-D144-v1
    PYTHONDONTWRITEBYTECODE=1 python3 planning/signed-divisor-20261105/full-column/full_column_v1.py --D 576 --U 24 --A1 37 --A2 1 --literal-pairs --out outputs/experiments/2026-11-05-signed-divisor-D576-v1

Use --estimate-only before the large character job. The estimate computes support/incidence only, explicitly marks that state and does not claim a completed energy calculation. The large run requires --old-rows. Independent direct pair reconstruction is small-case only; the large result covers all pairs by exact divisor inversion and all-gcd reconstruction, not a large quadratic pair loop. There is no claim that a signed/gcd slice is positive semidefinite.

## Frozen output schema

All JSON/JSONL is exact, deterministic key-sorted compact JSON plus LF, with Z[omega] pairs stored as integer arrays and division by D as exact rational strings. Every file is bound by SHA256 and bytes in manifest.json; source-freeze.json and the source-snapshot subtree bind executable source and immutable inputs.

- parameters.json: D,U,H,dyadic endpoints/unit/capacity/S/nu/profile/quantifiers.
- prime-ideals.json: stable IDs, primary generators, rational prime, ideal norm, split/inert.
- norm-ledger.jsonl: EVERY N in the closed annulus, rejection reason or exact ideal multiplicity/coefficients.
- columns.json: ALL ideal columns, IDs/generators/factor IDs, original A,C,mu,r_U,W.
- rows.json: exact u,v1,v2,ideal supports,capacity/nonprincipal witness. The row order is frozen old order for the large case.
- raw-character-phases.json: row-major full column array; phase0 is1, null is an actual raw zero.
- divisor-energies.jsonl: full divisor union including self divisors, ideal prime IDs/generator/norm/mu, incidences, per-row raw d masks and surviving active counts, per-row F_omega in order[A,C,mu], all9 Z_omega keyed AA,AC,Amu,CA,CC,Cmu,muA,muC,mumu.
- gcd-classes.jsonl: exact-gcd ordered column-pair counts and all9 weighted contribution numerators. Full superset inversion and reconstruction check every Z, not only the gcd1 sum. Pair counts include endpoint zero-weight columns in the declared full family.
- row-identities.json: each row's full energy, diagonal and coprime h1 numerator matrices.
- literal-ordered-pair-check.json: SMALL cases only; independent algorithm within this implementation explicitly visits every surviving ordered coprime pair and checks all9 components per row. External independent reconstruction supplies separate acceptance.
- summary.json: nonnegative even/odd-mu diagonal masses, signed net/cancellation ratio, complex crosscomponents, full energy/diagonal/h1 divided by D exactly once, raw zero vs value1 counts, resource measurements, all checks and limitations. For crosscomponents the output stores complex even/odd sums and squared norms; it does not equate those with sums of absolute values.
- resource-estimate.json: incidence/character operation counts and rough planning ceilings, generated BEFORE character arithmetic.

Finite observations do not imply a new signed estimate. Other row blocks/nu/profiles are not silently included; the common fixed profile and exact selected row block remain part of every result.
