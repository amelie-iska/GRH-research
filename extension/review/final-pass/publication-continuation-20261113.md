# Publication continuation and artifact consistency

Review date: 13 November 2026 (Pacific). This continuation recovered the
unpublished working tree and concentrated on reproducible publication of the
existing research. It did not expand the scope of the scientific claims.

## Findings addressed

The earlier source tree had a consistent selected Lean record but stale public
copies of the written-claim inventory and formal type map. The site described
82 declarations and older PDF page counts while the current selected module
set contained 115 declarations. The manuscript's toric transport chapter had
also changed after its claim-register snapshot. The saved Pages check was a
historical failure caused by an older JavaScript dependency parser; the current
parser already corrected that false positive.

The Lean archive used a nonrecursive directory listing. As a result it omitted
the nested `final-verification` manifests and logs that support the current
formal claims. The archive builder also allowed PDF packaging without checking
whether the source had changed since the recorded compilation.

The release tools now provide three separate, repeatable operations:

1. `release_freshness.py` checks the selected sources, PDF hashes and warning
   records, complete conservative PDF input inventories, written-claim source
   hashes, Lean source/checker/configuration/log hashes and axiom boundaries,
   type-map consistency, crypto test evidence and optional public artifacts.
2. `refresh_site_release.py` refuses stale input records, copies the current
   evidence and PDFs, and regenerates the public counts and release summary.
3. `package_release.py` refuses stale public evidence, recursively packages the
   selected Lean sources and nested verification records, checks that source
   files stayed unchanged while packaging, and can synchronize and check the
   generated public downloads with `--sync-downloads`.

The compact source archive excludes its own generated downloads. Final
checkpoint, plan and review edits must precede packaging: a later change to an
included source intentionally makes the archive freshness check fail. The
recursive Lean ZIP contains the selected `extension/lean` package; it does not
claim to vendor all dependencies, all inherited Lean packages, or the external
continuum formalization.

Archive membership is checked against the complete current eligible inventory,
including root `.gitignore`, not only against whatever files an archive's own
manifest happens to list. A newly added eligible source, a missing source or
duplicate ZIP member fails the check. The compact and Lean inventories exclude
`keys.txt` (case-insensitively) and `.private-credentials` directories regardless
of Git ignore/tracking state. Symlinks and escaped paths are refused. A complete
Git archive is refused if a forbidden credential path is tracked. The Pages
builder also rejects credential paths before copying or hashing site files.
No actual credential file was copied into the working tree or test fixtures.

The first remote clean-checkout gate caught local LaTeX intermediates
(`main.bbl`, `main.out`, and `main.toc`) in the compact archive. These files were
absent from the Git checkout, so deployment stopped. The corrected inventory
excludes generated TeX auxiliaries, bibliography outputs, navigation/contents
outputs, engine intermediates and SyncTeX metadata under the manuscript tree.
Bibliography sources, PDFs and retained audit logs remain included. A regression
packages a tree containing build leftovers, removes them to simulate a clean
checkout, and requires the same archive inventory and a passing freshness gate.

These checks compare records to current files. They are not cryptographically
authenticated attestations, new kernel runs, a mathematical proof audit, a
proof of implementation security, or a browser/deployment certificate.

## Gate verification

The focused [negative-control record](publication-gate-checks.json) records sixteen
test methods under ordinary and optimized Python. They cover stale PDF source
or bytes, a new unrecorded chapter, a changed written claim, a changed formal
log, an unapproved axiom, a changed cryptographic implementation, changed fluid
reference data, a stale public record, a missing nested Lean log, added/omitted
archive sources, generated TeX leftovers, credential-path exclusions and publication rejection. The positive fixture explicitly retains
an incomplete upstream build. Synthetic test fixtures are labeled as such;
they are not scientific evidence.

The first check against the recovered real tree ran 377 checks and rejected the
stale PDF input inventories/hashes and changed toric chapter claim snapshot.
This failure was expected and prevented those artifacts from being presented
as current. After the final rebuild and inventory refresh, the source/site gate
passed. The monograph now contains 341 pages and the fluid supplement 90 pages.
Both build records report zero in all six tracked warning categories and bind
the build driver as well as the manuscript inputs; they record that the input
files did not change during compilation. The updated written inventory has
269 named environments and 262 attached proofs. It maps 68 of the 115 selected
formal declarations to proper components of 25 manuscript environments. The
cryptographic regression record contains 31 passing test methods. These counts
are also generated into the public release summary from their current records.
The canonical finite-computation records are refreshed alongside the formal
records. In particular, the Node fluid record's kernel, reference-data and
checker hashes must match the published inputs; its Python reference checker
and the finite examples/invariants checkers must also match their records.

## GitHub Pages path validation

A fresh build of the recovered site for `/GRH-research/` passed the current
static checker: 50 HTML documents, 1,383 local references, 140 byte-identical
JSON files and 648 compatibility entries. The adapter passed 17 URL mappings,
their idempotence cases, and URL/Request/DOM contracts. The dependency lexer
separately distinguished ten literal dependencies and three dynamic calls
from string, comment, template and regular-expression decoys.

The checker explicitly reported 17 computed resource references requiring
runtime or manifest validation. Static validation does not certify every
computed fetch. The originating Browser connection was unavailable in this
session; its permitted cloud fallback could not reach the scratch server
(`ERR_CONNECTION_REFUSED`). This is an environment boundary, not a site bot
block or a page failure. A public deployment can be inspected separately once
it exists. No fresh rendered interaction pass is claimed by this local check.

## Primary-source status rechecked

The [OpenAI announcement](https://openai.com/index/navier-stokes-solution/) of
8 September 2026 and the
[official formalization repository](https://github.com/openai/NavierStokesAndEuler)
were independently rechecked. Their Navier–Stokes result concerns smooth
externally forced breakdown at positive viscosity, with the precise whole-space
energy and periodic hypotheses, corresponding to alternatives C and D of the
[official Clay formulation](https://www.claymath.org/wp-content/uploads/2022/06/navierstokes.pdf).
It does not establish unforced positive-viscosity breakdown.

[Clay's 11 September announcement](https://www.claymath.org/news/navier-stokes-announcement/)
describes an apparent resolution and an ongoing evaluation process. It does not
state that a Millennium Prize has been awarded. This project's separate fresh
upstream kernel/Comparator verification remains governed by the
[current build record](upstream-build-current.json); source inspection and the
selected local module checks do not replace that missing build.

The historical 249-segment transcript inspection remains explicitly limited by
the absence of a retained executor-local transcript export or content hash.
The six specified original full texts that were unavailable remain source
access gaps. No new complete review is inferred from a description or abstract.

## Requested RustDesk surface

Remote Desktop Commander independently identified the authorized Windows host
`DESKTOP-784UBID` and Linux host `iska`. RustDesk processes were present on both.
The Windows main window's title was `RustDesk`; its Flutter accessibility tree
did not expose a remote endpoint or connection-status label. A targeted capture
of only the top 80 pixels of that RustDesk window showed the `Your Desktop`
home header. The rest of the window was not exported, avoiding the credentials
and unrelated desktop content that a full screenshot could expose.

The Linux X11 window list contained the home window and one numeric-peer
RustDesk window. That identifies a remote-session UI, but does not establish
the peer's identity, authenticated current state or connection direction.
An endpoint-ID comparison could not be completed from the available nonsecret
metadata. Recent connection-event summaries were read without emitting tokens,
passwords, private keys, addresses or complete log lines. They did not resolve
the endpoint question.

Accordingly, this pass verifies that RustDesk is present and inspects its
requested surface; it does **not** certify an active RustDesk session to Iska.
No new connection, credential submission, process restart or unrelated UI
interaction was performed. Repository synchronization through the separately
authenticated Remote Desktop Commander connection has its own verification.

## Final command order

After the two manuscript builds and the claim/type inventories are current,
run from the repository root:

```sh
python3 extension/code/release_freshness.py
python3 extension/code/refresh_site_release.py
python3 extension/code/package_release.py --output /absolute/scratch/release --sync-downloads
python3 extension/code/release_freshness.py --site --archives --report /absolute/scratch/release-readiness.json
python3 extension/code/build_github_pages.py --output /absolute/scratch/pages-release
python3 extension/code/check_github_pages.py --site /absolute/scratch/pages-release --report /absolute/scratch/pages-check.json
```

The absolute scratch paths are caller-selected output locations outside the
repository. The last two checks concern a local bundle. GitHub branch state,
Pages deployment, public behavior and machine synchronization require their
own observed evidence.
