# Quantum-game, Connes-boundary and hubs/spokes review

Independent review2026-11-04 of both `quantum-games-*.tex` files,
`hubs-spokes-core.tex`, `hubs-spokes-boundaries.tex`,
`quantum-game-model.mjs`, `hubs-spokes-model.mjs`, relevant training/checker
source and receipts, final analytic parameter fixes and `electron-clouds.tex`.
Only review files/evidence changed. No credentials, remote jobs, model
repositories, production source, new dependency, solver or Lean execution.

Verdict: accepted after the root agent resolved two precision issues:
constructive tilted-angle branches and primal/dual NPA-bound wording. No
load-bearing mathematical error remains in the inspected additions. These are
finite examples/prose proofs plus external theorems under their stated
hypotheses, not a new Connes separation, HoTT formalization or GRH proof.

## Game identities and attainable values

The CHSH SOS expands exactly. The two squared terms sum to
`4I-sqrt(2)*B`, so multiplying by `1/sqrt(2)` gives
`2sqrt(2)I-B`. Only self-adjoint involutions and cross-party commutation are
used. This proves the same bound for tensor and commuting representations.

For tilted CHSH the classical16-sign enumeration gives `2+alpha`.
The displayed state/observables yield
`alpha*cos(2theta)+2*cos(mu)+2*sin(mu)*sin(2theta)` and attain
`sqrt(8+2alpha^2)` when the branches are
`theta in[0,pi/4]`, `mu=arctan(sin(2theta)) in[0,pi/4]`.
Those branch conditions were initially omitted; they are now explicit.
The universal upper bound is correctly external rather than inferred from
the restricted trained ansatz. The pinned
[Bamps--Pironio v1](https://arxiv.org/abs/1504.06960v1) SOS covers
`0<=alpha<2`; the manuscript now extends the endpoint by operator-norm
continuity and product-state attainment. The CHSH winning-probability conversion
is correctly restricted to the untilted uniform game.

All nine magic-square observables have the stated signs. They commute within
each row/column; every row product is+I, the first two column products+I and
the final column product-I. Bob's transpose, not an unqualified conjugation,
is the proper maximally-entangled-state identity. The joint projectors preserve
parity and give correlation one at each intersection. The stated classical
table loses exactly one of nine uniformly sampled question pairs. Exhaustive
enumeration of all4096 parity-admissible deterministic strategy pairs confirms
the classical optimum8/9. The exact score denominator72 in terms of local
traces agrees with denominator18 in terms of correlations.

Local conjugation preserves each player's projective measurement relations.
The source's two-layer local Rz/Ry/CNOT frame map is unitary. White-noise mixing
uses the correct total dimensions4 and16 and retains positive normalized,
no-signalling probabilities. The Hoeffding statement is conditional on fixed
local question inputs and ideal IID outcomes; the browser samples exactly that
conditional table. It is not an actual loophole-free Bell experiment.

## Learning, NPA and Connes scope

The12 saved runs are finite tensor strategies. The retained tilted seed43
at alpha1.5 remains at3.5; it is not hidden or promoted to global optimizer
convergence. Finite-dimensional compact-net approximation is an existence/
computability statement with fixed dimensions and finite input/output sets,
not a guarantee for local Adam or a universal dimension schedule.

Actual displayed moments are state Gram matrices, so PSD follows from the
norm-square proof. Their state need not be tracial; PSD does not imply cyclic
moments or normalized matrix-trace microstates. The manuscript explicitly
keeps those extra conditions separate.

The initial NPA sentence could be read as claiming an upper bound from one
feasible primal moment matrix. **Resolved:** it now distinguishes the outer
feasible set/optimized level value from an individual primal point, and requires
a validated optimum or dual certificate for an upper bound. An exact SOS
identity proves its own bound; a small residual does not. The pinned
[NPA v1](https://arxiv.org/abs/0803.4290v1) completeness target is commuting
measurements, as the manuscript states. Finite feasibility is not a realization
or finite-tensor approximation theorem.

The external MIP*=RE/Connes consequence and unbounded-dimension undecidability
are correctly distinguished from these elementary games. All displayed
strategies belong to both Cqa and Cqc and cannot demonstrate their strict
separation. This does not imply that all finite games have equal values in
those models. A universal computable dimension/error schedule deciding all
promised games would contradict the stated external undecidability result;
specified finite games and fixed-dimension approximations remain possible.
No impossibility or positivity result for GRH follows.

## Hubs/spokes and actual dessin topology

For an attaching loop, the homotopy pushout with the cone on S1 attaches a
disk through continuously indexed spokes. A finite star is a graph and cannot
replace that coherent2D attachment. The annulus/punctured-disk and deleted
star-vertex examples are correctly distinguished.

Checked the exact pinned [HoTT book](https://homotopytypetheory.org/wp-content/uploads/2013/03/hott-online-257-g5561b73.pdf)
Sections6.6--6.8, particularly Remarks6.7.1--6.7.2 on PDF page200.
Their hub/coherence and propositional-versus-judgmental computation distinctions
match the manuscript. No imported univalence/HIT axiom or complete Lean
formalization is asserted.

For a connected genus-g ribbon spine with n positive boundary components,
Euler characteristic gives graph rank `2g+n-1`. The boundary-word presentation
eliminates one peripheral generator; capping sets all peripheral generators
to one and leaves the closed-surface commutator relation. The once-punctured
and closed torus therefore share H1 but not fundamental group/H2; the analogous
genus-two statements are correct.

The same cyclic rotations at the two black vertices and the pairing involution
give one2m-cycle precisely for these odd m. For clean K2,m,
`V=m+2,E=2m,F=1,g=(m-1)/2`. Ranks2/4/8, filled H2=1 and unfilled H2=0
match the renderer. The original clean graph cover is biregular; its contracted
tree and a free-basis Cayley tree are not silently identified. Filling faces
changes the covering problem and requires lifted2-cells. Homotopy type alone
does not recover ribbon/complex/arithmetic/order-completion data or module/
derived/Fukaya descent. Those boundaries are explicit and appropriate.

## Fresh independent checks

```sh
node planning/synthetic-training/review/export_games_review.mjs
.tools/book-quantum-cpu/bin/python -B planning/synthetic-training/review/check_games_hubs.py
```

Evidence `games-hubs-review.json` includes CHSH SOS error `1.78e-15`, constructive
tilted attainment/classical bounds for alpha0,.5,1,1.5,2, exact magic-square
commutation/parities and exhaustive8/9 classical optimum. Independent full
NumPy Born calculations agree with12 actual browser-model visibility fixtures:
probabilities `1.95e-16`, scores `1.67e-15`, moments `1.23e-15` and the JS
Hermitian spectrum `2.89e-15`. Six filled/unfilled dessin cases pass independent
clean-graph incidence-rank, face-permutation and Euler checks. The general
topological and operator statements rest on the prose/source results, not
on a finite test cutoff.

## Analytic/density follow-up

The earlier `n0>=1`, `delta>0` fixes and HLNTK/HLDirichlet/HLFredholm
bibliography definitions are present. The beta>0 rate condition remains correct.
`electron-clouds.tex` states the correct nonnegative coherent finite-basis
density and exact full-space occupied-rank normalization. Gain/loss integrates
to zero, while finite voxels/8bit interpolation retain quantified display
errors. H2+ total energy correctly adds the half-hartree nuclear repulsion;
the Trp model retains explicit uncalibrated20-orbital/10-particle status and
angstrom-based Gaussian units. No actual protein DFT/valence count, chemical
accuracy, interval certificate or new arithmetic bridge is claimed.
