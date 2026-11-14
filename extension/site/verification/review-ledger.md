# Public source and proof review ledger

This index distinguishes reading, mathematical review, numerical execution, and
formal kernel verification. The complete repository review metadata is included
in the [research source archive](../downloads/source.zip). The public copies
listed here preserve their source hashes and historical verification boundaries.

## Current release

The monograph has 316 pages; the standalone fluid supplement has 70 pages.
The [claim register](claim-register.md) records 246 environments: 234 local
arguments, five conditional arguments, six cited external results, and one open
problem. There are 239 attached written proofs, plus nine separately classified
external statements in prose.

The [formal type map](formal-type-map.md) records all 82 local Lean declarations.
Thirty-five are mapped to exact components of sixteen manuscript environments;
no complete composite environment is labelled fully formalized. The
[fresh four-module run](navier-stokes/local-kernel-verification.md) returned zero
exit codes and zero warnings with the original sources, manifests, and logs
unchanged. It is independent of the incomplete upstream continuum build attempt.

## Historical second mathematical audit

The [per-claim second audit](second-pass-math-audit.md) read 125 original
statements and 55 additions in the version 1.1 snapshot. That version contained
180 environments and 173 attached proofs. Its [kernel record](second-pass-math-audit-core-kernel.json)
covered the then-current three modules and 48 declarations. Those numbers
identify the earlier snapshot; they are not the current manuscript or formal
package totals.

The later fluid extension adds 66 proved environments. Its source and chapter
reviews below retain their own exact reviewed snapshots and corrections. The
historical 180-environment audit is not relabelled as a proof audit of all 246
current environments.

## Books and earlier research

| Material | Actual coverage |
|---|---|
| Uploaded *Lattices over Orders I* | All 309 OCR page texts read across the team, with selected formula and statement checks against page images |
| Uploaded *Lattices over Orders II* | All 392 OCR page texts read across the team, with selected image checks and the independently supported cubic-generator correction |
| Main pinned GRH repository | Tracked-file and outbound-link inventories; four principal TeX sources fully read, with additional architecture and formal-interface inspection |
| Linked large math repository | Name-tree inventory of 174,524 files, not a full-content or proof review |
| Carroll–Weyman arXiv:1106.0774v1 | All 42 pages read across the team; selected formulas visually checked and the matching-example relation independently corrected |
| *Hodge Algebras* and Akin–Buchsbaum–Weyman | All extracted text from 88 and 72 PDF pages respectively read across the team, with selected visual checks; this is not a complete independent proof certification |
| Other cryptographic, invariant-theoretic, tensor, linguistic, and gauge sources | Source-specific primary-statement and hypothesis checks; partial or inaccessible sources retain that status in the full archive |
| Cosmology | Eight central papers fully text-read; other works reviewed only in specified sections or as abstracts; executable skies are synthetic |

The 409 extracted outbound URL strings include fragments, software references,
local addresses, and punctuation artifacts. They are not a count of 409 distinct
papers or fully reviewed works. Neither a file inventory nor complete OCR
reading establishes that every proof in every linked source has been audited.

## Fluid source and chapter reviews

| Record | Scope |
|---|---|
| [Microscopic source review](navier-stokes/microscopic-source-review.md) and [coverage JSON](navier-stokes/microscopic-source-coverage.json) | All 249 exposed English video-transcript segments; source-by-source full, partial, and unavailable coverage. Six requested original full texts remain unavailable. |
| [Farhat review](navier-stokes/farhat-review.md) | All 627 physical PDF pages of nine current replacement decks, including overlays; 48 selected visual inspections. Historical filenames returned 404, so identical editions are not asserted. |
| [Released proof review](navier-stokes/release-review.md) and [page ledger](navier-stokes/release-source-manifest.json) | All 166 pages assigned to the two reviewers; the exact externally forced theorem scope, analytic interfaces, and pinned sources. |
| [Quantum-fluid literature review](navier-stokes/quantum-algorithms-review.md) | All 129 pages of three reviewed paper versions, including appendices; source defects and local finite repairs retain precise boundaries. |
| [Microscopic chapter review](navier-stokes/microscopic-review-qa.json) | Source hashes, 21 named proof statements, assumption corrections, and the stated independent-reading scope. |
| [Release-chapter independent review](navier-stokes/release-chapter-independent-review.json) | All 15 ordinary proofs in the reviewed chapter, including the clarified Cartesian smoothness assumption for localization. |
| [Fluid structures and quantum-fluid audit](fluids-math-audit.json) | The named statements in its recorded snapshots, required qualifications, and integration resolutions; later additions remain identifiable by their own records. |

The continuum release proves forced breakdown from rest with positive viscosity
and bounded kinetic energy, including whole-space and periodic formulations.
It is not an unforced positive-viscosity theorem. The [upstream source audit](navier-stokes/release-source-audit.json)
records the 609-module solution import closure. The [fresh upstream build attempt](navier-stokes/release-build-verification.json)
stopped at dependency artifacts after rate-limited cache retrieval; neither a
complete fresh kernel check nor Comparator verification is claimed here.

## Finite execution and display evidence

The [Python fluid checks](fluids-python.json) and [Node comparison](fluids-node.json)
cover the specified finite examples, including independent circuit matrices,
integer complexes, manufactured-solution residuals, and toral fibres. The
[fluid browser inspection](fluids-browser-qa.json) records observed interactions
and a narrow layout. The [rendered supplement review](fluid-pdf-visual-qa.json)
separately records inspection of the final 70-page PDF. These are separate from exact Lean proofs, continuum
convergence theorems, and visual inspection of every possible parameter state.

The [public evidence manifest](public-evidence-manifest.json) lists byte-identical
copies of the selected authored review, code, and log files. Downloaded
third-party PDFs, full OCR texts, transcript dumps, and private authentication
material are excluded. Reproduction scripts should be run from their original
repository locations in the source archive, not from their copied site paths.
