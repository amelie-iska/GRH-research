# Navier–Stokes release: mathematical and formalization audit

Review date: 13 November 2026. This review distinguishes the released theorem,
full-paper reading, inspection of selected Lean definitions and adapters, lexical
source screening, fresh compilation, and independent certificate checking.

## Outcome and exact scope

The [official OpenAI announcement](https://openai.com/index/navier-stokes-solution/)
is dated 8 September 2026. Its [166-page manuscript](https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf)
states smooth finite-time blowup for three-dimensional Navier–Stokes with an
externally imposed smooth force, for every positive viscosity. The initial
velocity is zero. Velocity and pressure have fixed compact spatial support up to
the singular time; the force has compact support in space and positive time.
The velocity has bounded kinetic energy and unbounded supremum norm at time one.
The same datum and force admit no global smooth whole-space competitor with
uniformly bounded kinetic energy. Periodization supplies the periodic counterpart.

These statements address alternatives (C) and (D) of
[Fefferman's official problem statement](https://www.claymath.org/wp-content/uploads/2022/06/navierstokes.pdf).
They do not assert unforced positive-viscosity blowup. The separate Euler result
uses zero viscosity and cannot supply that missing conclusion. The
[Clay response of 11 September](https://www.claymath.org/news/navier-stokes-announcement/)
describes an apparent resolution and ongoing evaluation. This audit makes no
claim that a Millennium Prize has been awarded.

The new chapter is an original exposition of proof interfaces and several
supporting propositions. It preserves the released theorem's hypotheses. It does
not claim an independently reconstructed proof of the entire analytic
construction, a stronger Navier–Stokes theorem, or a new microscopic derivation
of the singular flow.

## Reading coverage

All 166 pages were read as complete extracted text in bounded segments. Some
initial tool responses were truncated; the affected segments were retrieved
again before being counted. The two reviewers' union, rather than either
reviewer individually, covers the complete paper.

| Reviewer | Complete page ranges |
|---|---|
| Release reviewer | 1–61, 100–125, 144–156, 165–166 |
| Root mathematical reviewer | 62–99, 126–144, 157–165 |

The manifest records each page, its reviewer, and a hash of the extracted text.
The root review's detailed notes are in `primary-root-review.json`. The
six-page Clay statement, including its errata, was also read in full. The
57-page Euler manuscript was downloaded and identified but was not fully read
in this audit. Adjacent literature was used for its precise statement and
setting, not represented as fully reviewed here.

## Main mathematical checks

### 1. Geometric concentration and energy

The construction's small parameter is `tau = 1-t`, with transverse scale
`tau^(1/2)` and axial scale `tau^(1/2-h)`. Tangential and axial amplitudes have
order `tau^(-1/2-h)`. The corresponding core-volume exponent is `3/2-h`, so
the core energy exponent is `1/2-3h` and the strongest squared-gradient exponent
is `-1/2-3h`. For `h < 1/6`, this concentration can have decreasing core energy
and finite time-integrated dissipation while its maximum diverges. The paper
uses a smaller admissible range of `h`.

The chapter proves a comparison-family scaling lemma, explicitly without
asserting that the arbitrary comparison family solves the PDE. This keeps a
useful dimensional calculation separate from existence. The critical spatial
integrability threshold of that family is below three, so its growing L3 norm
does not contradict endpoint regularity hypotheses requiring bounded L3.

### 2. Similarity coordinates and the axis

The coordinate `q` is defined implicitly by
`q - z^2 q^(2h) = tau`. On `q > |z|^(1/(1/2-h))`, the derivative with respect
to `q` is bounded below by `1-2h`. This gives a unique smooth coordinate.
The exact chain rules in the chapter include the factors
`L = 1-2h eta^2`, `eta_t = (1/2-h) eta/(q L)`, and
`eta_z = (1-eta^2)/(q^(1/2-h) L)`.

Cartesian smoothness at the axis is stronger than bounded cylindrical
components. The source uses the parity and radial factors needed to turn an
azimuthal expression into smooth Cartesian coefficients. The analytic-axis
construction is followed by smooth flat collars; global analyticity is not
claimed or needed.

### 3. Profile matching, positivity, and the order of choices

The leading profile construction keeps five cumulative quantities compatible:
axial flux, swirl moment, mixed moment, quadratic moment, and pressure moment.
Matching them as functions of the axial profile parameter is needed to keep
outer velocity, pressure, and integrated stress compatible. Merely matching
field values at a joining radius is insufficient.

The stress cone has a strict margin for its normalized direction, including
where the stress magnitude becomes flat. High-frequency radial modulation can
change a radial derivative by order one while changing profile values and
moments by order `1/N`. The subsequent five-moment correction is exact. The
parameter choices are ordered: profile parameters and a finite modulation
frequency are fixed before the physical singular scale tends to zero. An
estimate whose inverse constant diverges with a fixed profile parameter is
not silently promoted to a uniform estimate in that parameter.

Appendix B's analytic norms control mixed radial and parameter derivatives
using factorial/binomial weights and the radial integration denominators.
The large normalization parameters are chosen to keep the holomorphic profile
inside a fixed complex domain. Analytic construction near the axis and
smooth continuation through an outer collar serve different purposes.

### 4. The sparse analytic recursion

In Lemma 5.1, the derivative-carrying matrix maps the first four coordinates
into the last two and annihilates those last two. The radial kernels preserve
that splitting. Thus two adjacent derivative-carrying factors vanish, including
the product-rule term where a derivative strikes the intervening coefficient.
At most `ceil(k/2)` parameter derivatives survive in a word of length `k`.

The chapter proves the corresponding forbidden-word count and a sparse
Volterra convergence estimate. Radial integration contributes an inverse
factorial, while the Cauchy loss grows only like a power of order `k/2`.
The resulting kth root tends to zero. This is a concrete quadratic relation
and regular path language. It is not automatically a gentle algebra:
the one-vertex presentation `k<N,D>/(D^2)` is infinite-dimensional and fails
the unique allowed-successor condition for `N`.

### 5. Residual iteration and all-order realization

The four parts of the residual cycle handle nonzero angular modes, signed wave
amplitudes, auxiliary zero-mean terms, and the compact mean system. Later wave
increments are found by linearizing around fixed positive leading amplitudes;
they are not obtained by taking a new positive square root of every current
stress. Pressure and the full residual are recomputed after each change.

The source keeps supported residuals and already-flat errors separate. Flat
cutoff tails are retained as additive terms and are not fed indefinitely back
into forward wave sources. The functional bounds imply stage improvements
larger than `1/10`; the chapter verifies representative rational inequalities
with `kappa = 10^-5`, while identifying the analytic estimates as separate
obligations. A finite directed dependency graph determines derivative demand.

The uncut formal series need not converge. Stage-dependent cutoffs are applied
to potentials, followed by the complete curl. The derivative of the cutoff
is part of the actual velocity. For each required derivative order and target
power, one first selects a sufficiently high but finite stage and then shrinks
the physical scale. One does not sum all flat finite-stage errors, exchange
these quantifiers, or choose one finite stage for all derivative orders.

### 6. Smooth forcing is an exact terminal-jet assertion

The local field has an exact divergence constraint and a momentum residual
whose every fixed physical derivative is flat at the singular point. Away
from that point the heat exterior and the potential representation have
controlled one-sided terminal derivatives. Both facts are needed when the
field is localized.

The chapter expands the localization residual completely. In particular it
retains the term `(c^2-c)(u dot grad)u`, the gradient-cutoff contribution to the
curl, the Laplacian product terms, and all cross terms involving the potential
correction. Defining the force as the exact final residual then leaves no
equation error. A diagonal Borel-type construction realizes the limiting force
jets past the terminal time with compact support. This is smooth, not analytic,
extension. Flatness at the singular point alone would not justify it without
uniform endpoint control in the transition region.

### 7. Excluding global competitors requires the correct pressure class

The periodic comparison is an energy estimate. The whole-space result has an
additional issue: the accepted global smooth competitor need not satisfy an
extra pressure-decay hypothesis. Lemma 10.5 removes the possible harmonic
pressure-gradient ambiguity through a negative-Sobolev argument, then uses
expanding spatial cutoffs and quantitative commutator estimates. One cannot
replace it with an integration by parts that assumes the missing decay.

The chapter proves a separate quantitative torus estimate for the difference
between an exact and residual-bearing approximate solution. Its use for learned
fields requires continuum residual control, divergence control, initial-error
control, and a stability coefficient. A sampled residual or a training loss
does not automatically provide those bounds.

### 8. Viscosity and periodic adaptation

The conversion from viscosity one uses
`u_nu(x,t)=sqrt(nu) u(x/sqrt(nu),t)` and
`p_nu(x,t)=nu p(x/sqrt(nu),t)`. Energy and viscosity-weighted dissipation both
gain the factor `nu^(5/2)`. Time is unchanged.

Parabolic scaling can place the compact support strictly inside a fundamental
cube. Integer translates then have disjoint supports, so nonlinear cross terms
vanish exactly. Both velocity and pressure are periodic. The latter condition
is required by the official statement's erratum and appears explicitly in the
Lean comparison definitions.

## Lean audit and execution status

The pinned upstream commit is
`f9e8bc5b38b6e212696e8a30e3e91517af887bbd`, tree
`a503f07635f200c0f2f9c5361df1fa07f95c4741`.
The toolchain is `leanprover/lean4:v4.34.0-rc2`; the compiler reports commit
`6a10ac8c22beadecabdbb0919c2b50214762f91d`. Mathlib is pinned to
`85e3a25e006c35636f0e53b0e9296caca2685bc0`. All downloaded dependency
checkouts match the manifest.

The repository has 2,669 tracked files, including 816 under `NavierStokes/`.
The final solution's local import closure contains 609 modules and 20,364,883
bytes of source. The detailed manual pass covered the final theorem types,
their whole-space and periodic adapters, the PDE/regularity predicates, theorem
assembly, metadata, and pins. It did not manually audit all 609 modules.

The final declarations are:

- `NavierStokes.Comparator.navier_stokes_breakdown_R3`
- `NavierStokes.Comparator.navier_stokes_breakdown_periodic`

The solution closure imports no `ComparatorChallenges` module. A lexical
screen, after stripping comments and strings, found zero occurrences of
`sorry`, `admit`, `sorryAx`, `axiom`, `unsafe`, `native_decide`, and
`implemented_by` in that local closure. The challenge files intentionally
contain challenge placeholders; their presence elsewhere is not a gap in this
solution closure. Conversely, the clean lexical screen is not a kernel check.

The upstream `formalization.yaml` reports the standard dependencies
`propext`, `Classical.choice`, and `Quot.sound`, and labels its review status
`self-assessed`. That report was not independently reproduced in this pass.
The exact compiler distribution was downloaded and its published SHA-256
verified. Cache retrieval failed with HTTP 429 responses after decompression
of 2,211 files. A direct elaboration attempt then stopped at unavailable local
`NavierStokes` import artifacts. The final theorem bodies were not reached.
No successful fresh full build or independent Comparator/nanoda run is claimed.
The upstream proof was not edited, and no alternative compiler was substituted.

## Reproduction

`release-verify.py` audits an existing clean pinned checkout. It checks the
revision, tree, toolchain, installed dependency pins, local import closure,
source hashes, and lexical markers. Its optional execution flags distinguish
cache retrieval, a real final-target build, and independent Comparator execution.
Each requested process is time-bounded and writes a separate log. A cache
failure stops the requested build path rather than silently proceeding under
the label of a completed verification.

Example, after obtaining the exact upstream checkout and extracted compiler:

```sh
python release-verify.py \
  --upstream /absolute/path/to/NavierStokesAndEuler \
  --toolchain /absolute/path/to/lean-4.34.0-rc2-linux \
  --output /absolute/path/to/release-source-audit.json
```

For an actual build, add `--cache --build --timeout 7200`. For Comparator,
install the upstream-required `landrun`, `lean4export`, and `nanoda_bin`, then
also add `--comparator`. Successful exit codes and the generated axiom/certificate
output, rather than the presence of a script, are the evidence of completion.
The script does not modify the upstream proof or update its dependency pins.

## Files and contribution boundary

- `release-source-manifest.json`: sources, hashes, theorem scope, and complete
  page-by-page reading attribution.
- `release-source-audit.json`: 609-module source closure with per-module hashes,
  dependency pins, and lexical findings.
- `release-build-verification.json`: exact observed compiler/cache/elaboration
  outcomes, including the missing-artifact diagnostic.
- `release-verify.py`: executable reproduction workflow with explicit optional
  build and Comparator stages.
- `navier-stokes-release.tex` and `ns-release.bib`: original proof-interface
  exposition, supporting proofs, and primary citations for the monograph.

The algebraic bridge is useful where it specifies an actual operator relation,
tensor identity, covariance cone, moment map, arithmetic bound, or filtered
estimate. Neither a surface-code analogy nor quantum learning replaces the
continuum construction, the force regularity argument, or the comparison theorem.
The companion chapters develop those bridges while keeping these interfaces
explicit.
