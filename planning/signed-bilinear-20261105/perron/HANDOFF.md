# Double-Perron handoff

5 November 2026. Author result, awaiting parent review; Linux only. Exclusive new perron planning/check namespaces only. No production or queue mutation, publication, installation, MCP, credential or GPU action.

The genuine original-family double Euler series has local factor 1+q-q alpha-q beta and exact factorization L^T0(s,psi)/[L^T0(s+z,psi)L^T0(s+w,psi)] times the stated R. The correction is holomorphic and bounded uniformly in all vertical variables when sigma+x,sigma+y>0 and 2sigma+min(x,0)+min(y,0)>1, on fixed positive margins. No nonvanishing of R is presumed.

A second factorization F=F0 G preserves the original independently primitive psi_2 denominator. G has an absolutely convergent two-ideal Dirichlet series when sigma+x,sigma+y>1. This supplies exact sharp double Perron inversion for the actual finite cutoff on every fixed 1/2<sigma<1, with an explicit finite-height error, using V=floor(U)+1/2. Equality endpoints are included; unshifted Perron requires the recorded halfweight corrections. This is not an unjustified continuation of the infinite c series.

Without reciprocal L input, the safe contours require c,d>1-sigma. Their bound recovers U^(2-2sigma+epsilon) in amplitude and the already accepted U^(2-4delta+epsilon) energy loss at sigma=1/2+delta. No U saving is established. Moving contours toward or left of zero requires handling potential z=rho-s,w=rho-s reciprocal poles, single-residue boundary integrals, zero residues and quantitative reciprocal bounds. The exact slices R(s,z,0)=1 and F(s,z,0)=1/L^T0(s+z,psi) rule out assuming all such poles cancel in R. These auxiliary-variable singularities are not singularities of the finite J_U in s. The original principal s pole remains separate.

Focused check command:

    PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 planning/signed-bilinear-20261105/perron/check_double_perron_exact.py --output outputs/checks/2026-11-05-signed-bilinear/perron/exact-controls-v1.json

Passed deterministically on five actual Eisenstein prime ideals of norms 7,7,13,13,25, 32 squarefree support ideals and eight literal rows including third/sixth powers: 800 local rational identities; 160 finite global Euler and G-series cases; 192 actual weighted-cutoff identities; 96 coordinate-slice identities; 384 original-zero checks; 6,144 half-integer endpoint equivalences. Negative controls: 64 omitted-R, 160 forbidden-overlap-square and 136 uncorrected-halfweight witnesses. There is also an actual distinct equal-norm endpoint pair and a sixth-power sentinel control. No random seed, nonstdlib dependency or floating arithmetic was used.

Finite algebra tests do not prove analytic product convergence, Hecke continuation, reciprocal estimates or zero location. Read DOUBLE_PERRON.md for the analytic derivation and inherited classical Hecke input. No new infinite saving, BT_sigma, energy lower bound, Lean, determinant positivity or GRH claim. The existing U-independent sieve envelope remains intact.

Next concrete arithmetic obligation: prove an original-family bound for the genuinely mollified two-variable integral, including any actual zero residues and reciprocal boundary terms, or attack the already specified signed covariance BT_sigma. The accepted numerator AFM alone supplies neither. Constants remain for fixed nu/S, not uniform in varying conductor or infinity type.
