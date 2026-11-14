# Current upstream Navier–Stokes verification pass

Review date: 13 November 2026. This pass rechecked public release information, the current upstream revision, source provenance, and a bounded dependency-cache retrieval. **The fresh source audit passed; the fresh full theorem build remains incomplete.**

## Released result and exact boundary

The [OpenAI announcement](https://openai.com/index/navier-stokes-solution/) dated 8 September 2026 releases an analytical proof and Lean formalization. The [manuscript](https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf) constructs, for every positive viscosity, smooth forced three-dimensional flow from rest with finite-time unbounded velocity and bounded kinetic energy. The force is smooth and compactly supported in space and positive time. It establishes the forced breakdown alternatives C and D in the [official Clay statement](https://www.claymath.org/wp-content/uploads/2022/06/navierstokes.pdf). This does not assert unforced positive-viscosity blowup.

The [Clay announcement](https://www.claymath.org/news/navier-stokes-announcement/) dated 11 September describes an apparent settlement and an ongoing evaluation process. A release, a successful local proof check, independent validation of the theorem's encoding, and a prize decision are distinct assertions. This project does not conflate them or claim that its additional finite algebraic interfaces strengthen the continuum theorem.

## Fresh source audit

A fresh `git ls-remote` returned current upstream revision `f9e8bc5b38b6e212696e8a30e3e91517af887bbd`, matching the earlier pinned audit. Its Git tree is `a503f07635f200c0f2f9c5361df1fa07f95c4741`. The isolated checkout remained clean. All installed dependency checkouts matched the manifest.

The compiler is Lean 4.34.0-rc2, commit `6a10ac8c22beadecabdbb0919c2b50214762f91d`; mathlib is `85e3a25e006c35636f0e53b0e9296caca2685bc0`. The 609-module local solution import closure contains 20,364,883 source bytes and imports no Comparator challenge module. A fresh comment/string-aware lexical scan found no `sorry`, `admit`, `sorryAx`, `axiom`, `unsafe`, `native_decide`, or `implemented_by` tokens in that closure. This is provenance and source-screening evidence, not kernel acceptance.

The final target remains `NavierStokes.ComparatorSolution`, exposing:

- `NavierStokes.Comparator.navier_stokes_breakdown_R3`;
- `NavierStokes.Comparator.navier_stokes_breakdown_periodic`.

## Bounded cache retry and observed blocker

The retry used an isolated checkout and cache, the exact installed compiler, and a process-local curl configuration with four parallel transfers. No global configuration, source file, toolchain pin, or dependency revision was changed. The configuration also requested a transfer-start rate, but the installed curl manual states that `--rate` is ineffective with `--parallel`; no effective requests-per-second cap is claimed.

The cache reached 2,303 successful downloads and 2,341 attempted transfers in the last status sample. That sample reported 38 failures; the complete retained log contains 34 HTTP 429 diagnostics. The watchdog terminated the transfer process after 92.104 seconds when the configured rate-limit stop condition was observed. The mathlib artifact count increased from 2,124 to 3,160 `.olean` files but remained incomplete. No aggressive retry followed.

The final-target build and independent Comparator run were therefore not executed. The released final axiom report was not independently reproduced. This outcome is a dependency-transport blocker, not a demonstrated defect in the mathematical proof.

## Earlier transcript attempt (retained history)

The earlier [coverage ledger](../navier-stokes/microscopic-source-coverage.json) records a complete exposed English YouTube transcript review through the public browser interface: 249 timed segments from 00:00 through 32:36. It separately records that an executor-local transcript export was not verified. This pass inspected that ledger and attempted a fresh public retrieval: the watch page exposed English caption metadata, while the caption request returned an empty body. The earlier DOM review is retained as prior evidence; it is not represented as a new full transcript reading.

Other full-text access gaps recorded in the earlier ledger remain explicit. A newly found university-hosted Loudon 1959 PDF returned HTTP 503 in this pass and was not counted as reviewed.

## Reproducible evidence

- [upstream-source-current.json](upstream-source-current.json): exact revision, tree, dependency pins, every local closure module hash, and lexical findings.
- [upstream-build-current.json](upstream-build-current.json): current outcome, exact invocation, elapsed time, source asset hashes, transcript provenance, and limitations.
- [upstream-cache-current.log](upstream-cache-current.log): authentic cache output, retained without substituting a synthetic success log.

The JSON records SHA-256 hashes for the manuscript, official problem statement, compiler distribution, final adapter, prior provenance ledgers, and current audit/log evidence. Downloaded papers remain review inputs rather than being republished with this report.

## Latest offline and transcript continuation

The [offline continuation](upstream-offline-20261113.json) used existing files
only: one additional artifact was unpacked, giving 3,161 mathlib-library
`.olean` files. Of 210 direct external imports in the pinned solution closure,
125 remain missing; `Mathlib.Init.olean` is also absent. The exact missing
archive was not found in the inspected existing local caches. Neither the
full target nor the independent Comparator was run. No new download command,
source change or pin change occurred, and independent kernel verification
remains incomplete.

The [transcript continuation](../navier-stokes/source-gap-continuation-20261113.json)
subsequently reread all 249 entries and verified a 35,743-byte canonical UTF-8
extraction in a private source cache. Its SHA-256 is
`0cbc23bb1d1d6c3fe46f46dcfa337f4aa78f0d8966f377eea35ea525e86e3884`.
The public record preserves the failed exporter attempt separately from the
successful DOM extraction; 32:36 is the last entry's start time. The six
remaining original-paper access gaps are unchanged.
