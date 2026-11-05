# Frozen profile-uniformity implementation handoff

Accepted new run: `outputs/experiments/2026-11-05-profile-uniformity-v2/`.
Code: `examples/profile_uniformity/{unit_profile.py,ideal_tower.py,test_profile.py,README.md}`.
Source freeze before run: `planning/signed-profile-20261105/implementation/source-freeze-v2.json`.
Evidence: `outputs/checks/2026-11-05-signed-profile/implementation/`.

Main witness epsilon=1+omega, omega coordinates(1,1), has actual unit character
zeta6^((Nm-1)/6). Common complex W_D nodes are sign(A_U)*conjugate(character),
so every surviving original A_U coefficient equals |A_U|. Retained real-minus-one
witness is separate. The common unsigned nodal comparator ALSO varies with D.
Profiles have exact finite nodes/supnorm1 and derivative bound O_k(D^k).
Principal nu only; no exact primitive conductor is asserted.

All six integer-square D cases through262144 ran, with exact SPF norm groups,
all rejected integer norms, split/inert squarefree ideal multiplicities,
duplicated divisor norms and actual r_U/A_U. Sources and helper bytes were
frozen before the accepted run and copied into immutable snapshots.
Main input files: norm-groups-D{D}.json; summary files: summary-D{D}.json.
Each main input records all40 canonical ideals v of norm<=64 for diagnostics,
actual prime-ideal factorizations, raw masks and allowed multiplicity vectors.
The PRIMARY family is good-S v with Nv<=X (19 rows atX64, including unit).
Secondary dyadic is exactly[X/2,X), with X4 empty. H=X^6 is explicit.
Capacity-matched H=floor(D^(3/4)) gives caps2,2,2,3,4,4; only good-S unit
v=1 occurs at these small caps. Fixed-X64 statistics are a separate range.

Norm49 has two non-squarefree prime-square ideals with sigma7=1 and one
squarefree conjugate product with sigma7=2. Their masks and T_v differ;
row ideals are never keyed by rational norm alone. Serialized JSON object
keys in split_prime_coverage are strings; normalize them to integers when
using the in-memory integer-key representation.

Seven focused tests pass with no skips. Fresh small-D256/1024 checks compare
368 actual ideal columns/A_U values,368 order6 unit symbols and14720 literal
epsilon*beta_v^6 raw symbols by independent split/inert finite-field exponentiation,
plus the approved raw-symbol helper. All small-D ordered coprime column pairs
are explicitly counted. These h1 values are selected-row contributions, not
lower bounds on the h1 component over unselected rows.

The saved-record checker imports no author arithmetic routine. It verifies
30482 saved norm groups,1219280 allowed-multiplicity entries and33 nontrivial
|A_U|>1 cases directly from the original ternary divisor-assignment definition.
It checks all40 tower rows are distinct, exact energies, cumulative/dyadic
endpoints, norm49 mask separation, source/input/snapshot hashes, pin-before-run
ordering and existing-output/pin/non-square/float-D refusals without modifying
any accepted byte. Its scope is implementation consistency; the independent
scientific proof/code audit belongs to the separate reviewer.

The original source HEADdba37ff/index0ef1af remain exact. No production/pin/history,
dependency, environment, toolchain, GPU, authentication or publication action.
The v1 attempt reached all six arithmetic cases but failed manifest path
formatting; every prior source/data/log byte is preserved. V2 is governing.

Finite E/D or tower ratios do not prove asymptotic cD/cDX. Fixed-profile targets,
derivative-dependent estimates, and GRH are not contradicted by these D-dependent
profiles. Root/reviewer own the separate analytic counting proof and any exact
conductor statement. No such theorem is inferred from finite checks.

Exact case summaries:

|D|U|ideal columns|absolute coefficient sum|unit energy|unit E/D|X64 selected energy|
|---:|---:|---:|---:|---:|---:|---:|
|256|16|74|74|1369/64|1369/16384|45235/128|
|1024|32|294|294|21609/256|21609/262144|90397/64|
|4096|64|1145|1145|1311025/4096|1311025/16777216|10930287/2048|
|16384|128|4638|4652|1352569/1024|1352569/16777216|180568497/8192|
|65536|256|18491|18539|343694521/65536|343694521/4294967296|2870253347/32768|
|262144|512|73988|74120|85840225/4096|85840225/1073741824|91791978401/262144|

Frozen run manifest SHA256: `a90d1c356c276b36430b58e342ea7aee6dfe6cb33c0d7db0a4ffcb5ab17bc460`

Source pin SHA256: `eeb405583fbd9256a1a8a54ffa4a56b79ad4e3e70b3ff1abd0f9c83cf5001f54`

Implementation result SHA256: `07a13198a693ad06fe035ad0c3bf82da07c54c66f3baa2d58d2cf8573dd53160`

- `examples/arithmetic_cutoff/exact_recombination.py`: `a0628db65089286c60df6e06eee38e0eca225d0e47319b1f5f6afe80fea4c330`
- `examples/profile_uniformity/README.md`: `6e98d8582585637f74e1df52e03ac8d419c43ae449b5c44ba23458de8cf5bf08`
- `examples/profile_uniformity/ideal_tower.py`: `77dc26658a188ff6669bf577fcb8298b875ab2a5e4f8e0bfe628b94c9b9430d4`
- `examples/profile_uniformity/test_profile.py`: `4b401bf4c00b3ec544216a0c510446d0198e777bf8eec7506c711ea57fec7128`
- `examples/profile_uniformity/unit_profile.py`: `66b117ef6536b52315c4a4f2b27f03d9f2d00ae60149e2b1a55c48f2e843b203`
- `scripts/check_finite_correlation.py`: `5f8da7467f93071fc19b4a1a1e8c415a880a95305d847cce9a42c386d1f3d3e8`
- `scripts/check_mobius_split.py`: `a3f1d3d89acafc187d6ca6851f370712b2544c92802b4d95dc5187e18a770638`
- `scripts/check_reciprocity_period.py`: `34eef99b491f6b8d64b55b39c3a42400c6df3d0e1ddf5ba8494bc01f300e8925`
