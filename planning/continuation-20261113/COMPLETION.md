# Published continuation: verification and delivery

Recorded 13 November 2026 (Pacific); machine-readable observations use UTC.

The consolidated research extension is published to
[GRH-research](https://github.com/amelie-iska/GRH-research), the combined
[research atlas](https://amelie-iska.github.io/GRH-research/) is live, and the
three source-release checkouts have matching commits and selected file hashes.
The full observation record is [PUBLICATION_STATUS.json](PUBLICATION_STATUS.json).
This receipt supersedes the operational next steps and old intermediate counts
in the pre-publication checkpoint and continuation notes.

## Published snapshots

| Snapshot | Commit |
|---|---|
| Preserved recovery branch | `97345b643f6d6c576ef4b3cb9900dab4d820c585` |
| Verified research and document release | `3e3aa651e765d170482b348dab5cc9e4e6091390` |
| Clean-checkout archive correction | `6b8b6ec31779fe322804ae45ef3bd2dd440b95b3` |
| Quantum heading correction | `caf1bab7a90799dc55678b41f6e73ba4275c7cf7` |
| Final published source, including versioned script URL | `4b9adb4f9c598e7d01b8ca15ed502e169b83ab13` |
| Live `gh-pages` deployment | `4d6341b5a8bf072c20525868255f43eb238438c1` |

The Git commit containing this receipt adds post-release evidence. The website
and downloadable research artifacts were built from the final source snapshot
above. Keeping the receipt outside the compact archive avoids a circular hash
dependency. Each source update used an expected-head check and a non-forced
fast-forward; unrelated history was preserved.

## Documents and runnable material

- [341-page monograph](https://amelie-iska.github.io/GRH-research/downloads/paper.pdf)
- [90-page fluid and quantum-information supplement](https://amelie-iska.github.io/GRH-research/downloads/fluid-extension.pdf)
- [Compact source archive](https://amelie-iska.github.io/GRH-research/downloads/source.zip)
- [Selected extension Lean package and verification records](https://amelie-iska.github.io/GRH-research/downloads/lean4.zip)
- [Iterative implementation plan](../../extension/IMPLEMENTATION_PLAN.md)

The live PDFs, both archives and release metadata returned HTTP 200 and matched
their source SHA-256 values. Both PDF builds had zero warnings in all six tracked
categories, stable input inventories and embedded fonts. Eleven representative
physical pages received visual inspection. That is a layout sample, not an
every-page proof audit.

The compact Lean ZIP contains six extension source modules and recursive
verification evidence. The 37 inherited Lean source files are available in the
full repository and the synchronized clones; they are not all vendored in that
compact ZIP. Compiler and mathlib dependencies remain separately pinned.

## Corrections made during this continuation

The recovered work was preserved before implementation. The continuation then
fixed a reproducible Python optimization false pass: an elliptic-curve driver
could claim 6,859 comparisons after optimization removed the assertions. All
five affected assertion-bearing verifiers now reject disabled assertions before
producing evidence. The ordinary run executes the actual comparisons.

The Lean driver now rejects warnings, missing exact types, incomplete axiom
inventories and unapproved axioms. The original arithmetic and analytic runners
also support explicit Linux toolchain and mathlib paths. A bounded recovery of
missing pinned dependencies enabled a complete fresh check of the inventoried
local declarations.

Cryptographic boundary probes became permanent regressions. Publication checks
now reject stale sources and evidence, include nested Lean logs, and exclude
credential paths independently of Git ignore rules. A real deployment attempt
caught generated TeX files in the source ZIP that were absent from clean clones;
the archive inventory was corrected and checked against a clean tracked tree.
The live browser sample then found a repeated qubit-count label. The renderer
was corrected and its script URL versioned so clients request the revised
asset. Failed intermediate rendered checks remain in the audit alongside the
final successful public recheck.

## Verification results and their scope

| Area | Recorded result |
|---|---|
| Local Lean | 483 distinct declarations in 43 files; zero warnings; exact types and axiom dependencies retained |
| Package split | 115 extension declarations, 361 inherited analytic declarations and 7 inherited arithmetic declarations |
| Written manuscript inventory | 269 named environments, 262 attached written proof environments |
| Formal coverage map | 68 extension declarations mapped to components of 25 written environments; zero whole composite environments marked fully formalized |
| Cryptographic regressions | 31 passing methods, no failures, errors or skips |
| Optimized-runtime refusal checks | 25 scenarios passed under ordinary and optimized parent interpreters |
| Release regressions | 16 methods passed under ordinary and optimized Python |
| Source/site/archive freshness | 2,518 checks passed, including the actual remote Linux checkout |
| Static Pages validation | 50 HTML documents, 1,382 local references, 158 byte-identical JSON records and 648 compatibility entries |
| Public browser sample | Four interactive pages passed; a final narrow recheck confirms the corrected quantum heading |

The [formal report](../../extension/review/final-pass/formal-continuation-20261113.md)
records Lean 4.24.0, the mathlib pin, source hashes and permitted foundational
axioms. No theorem source changed in this continuation. The 483 declarations
do not imply 483 new theorems or complete formalization of the manuscript.

The cryptographic implementation uses maintained-library AES-256-GCM,
ChaCha20-Poly1305, Ed25519 and ML-KEM interfaces. The tests include actual payload
and UTF-8 context limits, tampering, canonical encodings and malformed Unicode.
These results are implementation regression evidence, with no new security
reduction or certification claim.

The [public browser record](PUBLIC_BROWSER_QA.json) retains rendered observations
of the fluid channel, learned proposal versus exact certificate, 18-qubit worker
and inherited model controls. [The label recheck](PUBLIC_BROWSER_LABEL_RECHECK.json)
records the final correction. No application-origin console warnings or errors
appeared in the sampled interactions. This covers one desktop browser and
selected controls, not every dynamic request or responsive layout.

Optional screenshots: [fluid](browser/fluids.jpg),
[learning and certificate](browser/learning.jpg),
[quantum syndrome](browser/quantum-syndrome.jpg),
[inherited project](browser/legacy.jpg), and
[corrected final heading](browser/quantum-label-versioned.jpg).

## Machine synchronization and credentials

[Clone parity](CLONE_RELEASE_PARITY.json) records the source-release observations:

| Machine role | Checkout |
|---|---|
| Workspace | `GRH-research` working clone |
| Requested remote Linux host | `GRH-research` at the user-specified project location |
| Local Windows desktop | `GRH-research` in the user's documents directory |

All three have the same verified source commit, clean working trees and matching
selected PDF/archive/source hashes. Their `GRH`, `Surface-Orders-Hilbert-Polya`
and `math` submodules are initialized at the recorded gitlinks, with clean child
working trees. The `math` pin contains 174,524 tracked files. Windows required
only a repository-local long-path setting and restoration of one pinned file.
The receipt-only commit is synchronized after publication; it does not change
these research payloads or submodule pins.

Remote Desktop Commander completed synchronization on the user devices.
RustDesk resolved the intended Linux target, but its connection closed or timed
out; authenticated viewing was not established. No endpoint identifier is
published and no access settings were changed.

Private authentication material is untracked and excluded from the published
commits, archives and site. The ignore rule and independent archive/Pages exclusions were
verified. No credential values or private credential-source path are included
in this receipt.

## Remaining research obligations

1. Complete the separate upstream Lean 4.34.0-rc2 full target and Comparator
   verification when its dependencies are available. The historical attempt
   stopped after HTTP 429; the successful local Lean 4.24.0 checks do not replace it.
2. Extend formal coverage from precise components to complete manuscript
   arguments. Resolve the six remaining original full-text access/review gaps
   and retain a reproducible transcript export for the video source.
3. Establish the GRH/Hilbert-Polya arithmetic determinant and spectral
   identification, including the required analytic convergence inputs.
4. Prove the uniform continuum estimates needed for the proposed fluid and
   Yang-Mills applications. Demonstrated quantum advantage and formal protocol
   security also remain separate obligations.

The [OpenAI announcement](https://openai.com/index/navier-stokes-solution/)
concerns smooth externally forced, positive-viscosity finite-time breakdown,
the Clay C/D alternatives. [Clay's announcement](https://www.claymath.org/news/navier-stokes-announcement/)
describes an apparent resolution and an evaluation process. This project does
not claim an awarded prize, an independently completed upstream verification,
a stronger unforced result, GRH or a continuum Yang-Mills mass-gap proof.
