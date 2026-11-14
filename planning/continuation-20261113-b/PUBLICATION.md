# Published quantum-tropical realization release

## Published source and website

The validated source payload is commit
`70ffffe6a58c12fae3d8e228286336675274f9ed`, tree
`2843ce07108e0f2f370d2f77d1ffc218eef7aff9`. Both `main` and
`research/continuation-20261113-b` were advanced with expected-head checks
and without forcing. Its parent is the independently preserved exact-gain
checkpoint `2f97dc961a95e1ac795b58bf362a3b419d355557`.

The Pages payload is commit `0cee58ad33aa2ea256f35e5dfe69187035bd964b`,
tree `00d227244035884f9cba0fbae47070306f0a4970`, with parent
`4d6341b5a8bf072c20525868255f43eb238438c1`. Its 1,469 files match the
isolated local bundle exactly. The `gh-pages` reference was advanced with
an expected-head check and without forcing. Both published branch heads
were read back through GitHub after their updates. GitHub Actions run
[`43544149730`](https://github.com/amelie-iska/GRH-research/actions/runs/43544149730)
reports successful completion of the Pages build and deployment for that
exact Pages commit. The source-head Actions query returned no runs; the
source verification described here is the recorded local audit.

Publication URLs:

- [Research atlas](https://amelie-iska.github.io/GRH-research/)
- [Quantum-tropical realizations](https://amelie-iska.github.io/GRH-research/realizations.html)
- [355-page monograph](https://amelie-iska.github.io/GRH-research/downloads/paper.pdf)
- [105-page fluid supplement](https://amelie-iska.github.io/GRH-research/downloads/fluid-extension.pdf)
- [Current release summary](https://amelie-iska.github.io/GRH-research/verification/release-summary.json)

## Evidence from the deployed site

`PUBLIC_HTTP_VERIFICATION.json` records all eleven requested public files
returning HTTP 200 and exactly matching the bundle's lengths and SHA-256
hashes on the first attempt. It covers 14,441,813 received bytes, including
both books, both archives, the three relevant HTML pages and selected
research/verification records. The observation window was
2026-11-14 02:04:14.932–02:04:25.312 UTC. There were no redirects, stale
responses or transfer errors. The public output itself was checked; this
does not assert access to GitHub's internal Pages-build API.

`BROWSER_VERIFICATION.json` records the subsequent desktop browser review.
Navigation from the atlas reached the new page. Its exact-feedback formula,
gain table, seven-row substrate table and evidence links were checked, and
the observed viewport had no horizontal page overflow. The saved hero
image is `REALIZATIONS_LIVE.jpg`. The record distinguishes browser-extension
metadata errors from page-origin errors and does not claim a mobile-browser
test. Static responsive and link checks are recorded separately.

The release payload already passed 3,139 source/site/archive consistency
checks. PDF visual review covers 31 selected main-book pages and 27 selected
supplement pages, including every page of the new chapter in each book;
it is not an assertion that every page of both books was visually inspected.

## Source, formal and experimental scope

The new material connects quantum channels, tropical gain/path envelopes,
nonlinear control and seven candidate substrate families. The seventeen
primary-source entries state exactly which full texts, selected passages
or abstracts were reviewed. Natural and generated physical substrates are
research candidates, with encoding, control, measurement and validation
obligations stated explicitly.

The exact two-qubit controller and the rational-input correction have
reproducible implementation evidence. Six new weighted-gain/residual Lean
results raise the strict source audit to 121 extension declarations plus
368 inherited declarations. The 489 checked declarations are not a claim
that the full monograph or a continuum theorem has been formalized.

The independent upstream Navier–Stokes build remains incomplete, and six
requested microscopic-source full texts remain unavailable. Proposed
applications to GRH, the continuum mass gap and cryptographic security
retain their separate mathematical obligations. No new physical experiment,
trained fluid controller or quantum computational advantage is asserted.

## Clone synchronization

The workspace clone was fetched and fast-forwarded to the exact source
payload, with a clean worktree and unchanged initialized submodules. Iska
Linux subsequently recovered command connectivity and was fast-forwarded
to the same payload at 2026-11-14 02:07:25 UTC. Its worktree and all three
recursive submodules were verified clean. Windows returned an MCP request
timeout before its read-only preflight produced a current HEAD or status;
no fetch or merge was attempted there. Its current synchronization is
unconfirmed. These observations are recorded in `MACHINE_SYNC.json`.
The publication receipts form a later metadata-only checkpoint; they do not
change the validated books, code, archives or Pages bundle.

Credential material is excluded from the release and its archives.
