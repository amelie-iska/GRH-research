# Exact original weighted-cutoff diagnostics

The code checks identities for the actual truncated ideal coefficients beta_U and A_U on seven split/inert prime ideals in Z[omega]. It uses exact Fraction/Eisenstein arithmetic and the project's existing raw sextic-symbol implementations. This is a finite diagnostic, not a proof of an infinite large sieve, critical-strip convergence, or GRH.

From the repository root on Linux:

```sh
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 nice -n 15 python3 examples/arithmetic_cutoff/exact_recombination.py --output outputs/checks/NEW-weighted-cutoff
```

The output directory must not exist. Existing experiments are never overwritten. There is no random seed; all inputs and arithmetic are exact. The frozen v1 report is under `outputs/checks/2026-11-04-weighted-moment/exact-recombination-v1/`.

The 128 squarefree support ideals use seven actual distinct prime ideals of norms 7,7,13,13,19,19,25, including both split conjugates and an inert prime. Thirty-three actual rows include cubic/sixth powers; two finite phase twists and two integer s-values are checked at six cutoffs. All 792 direct masked-sum/coefficient/Euler-packaging cases and 2304 coefficient controls pass. Original raw zeros remain zero even when a sixth power drops from the primitive conductor. The report records 660 failures of the forbidden unconstrained-square replacement; these are precise local/finite counterexamples, not energy lower bounds.

Independent controls and full proofs are under `planning/weighted-moment-20261104/`. The separate sign-window checker passes 504 exact cases (170 in the intermediate band): A_U=mu for Nm<=U and A_U=-mu for U<Nm<=U^2. Active smoothed columns lie at Nm>=D>=U^2, so this does not replace their actual coefficients by -mu.

The reviewed analytic result is a U-independent envelope for the original residue-subtracted type-I energy:

`sum_{0<Nu<=H}|E_u|^2 <= C ||W||_infinity^2 (HD)^epsilon [H + D H^(1/3) + (HD)^(2/3)]`.

It uses the pinned BGL classical large sieve, exact row orientation/conductor masks and a principal-residue upper bound. At H=D^(3/4) it still loses exponent 1/2. The exact cutoff converges to the incomplete reciprocal L-function with a proved rate only on Re s>=1+kappa. Extending actual cutoff convergence locally uniformly to Re s>1/2 would itself require zero-freeness; a family mean bound does not supply it. These analytic results are independently reviewed prose and are not new Lean declarations.

## Actual signed covariance fixture (5 November 2026)

Run the exact smooth-profile original-family fixture with a fresh output directory:

```sh
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 nice -n 15 python3 examples/arithmetic_cutoff/signed_covariance.py --output outputs/checks/NEW-signed-covariance
```

The complete four active ideal columns and all72B7 rows give covariance-27/25
although coefficient overlap is nonnegative. A second246-row guaranteed
nonprincipal subset atH89 gives-69/50 with raw zeros retained. The report
contains all character values and full complex Gram matrices; independent
finite-field exponentiation reproduces them. The smooth profile has exact
integer-norm values, so no exponential approximation is used. This is a finite
counterexample to an automatic covariance-sign shortcut, not toBT_sigma orGRH.
High-cutoff coefficients are odd/nonzero; their lower norm is not an energy
lower bound. See research/signed-cutoff-covariance.md and shared TeX proofs.
