# Iterative implementation and publication plan

Updated 13 November 2026, Pacific time. This plan implements the author's request
to consolidate the research, verify its claims, publish it to
`amelie-iska/GRH-research`, combine the two research sites, and synchronize the
authorized machines. The initial review is comprehensive; implementation then
proceeds in bounded, independently checkable chunks.

## Operating method

Each chunk follows **inspect → implement → validate → record → commit**. A chunk
is complete only when its stated acceptance criteria have evidence. Save concise
checkpoints after each chunk. Reuse an existing validation only if its input
hashes, toolchain and dependency assumptions still match. Rerun the smallest
meaningful affected checks after a correction; do not rerun GPU training merely
to repackage an unchanged checkpoint. Keep full logs in files and report only
outcomes and blockers in chat. Do not start another open-ended improvement cycle
after the publication gates pass.

Preserve the inherited repository and authorship. Use ordinary fast-forward
publication, never replace unrelated machine changes, and compare exact commits
and file hashes when synchronizing. No private keys, access tokens, third-party
full-text books, or unlicensed paper copies belong in the publication.

## Initial review — establish the complete baseline

Recover all existing source, PDFs, proofs, source audits, numerical experiments,
model checkpoints, and page sources before implementing anything further.
Compare prior worktrees with GitHub and the authorized device clones. Identify
the actual default branch and hosting configuration. Review the supplied video
and its source ledger, the OpenAI announcement and mathematical paper, and the
two tropical/toric repositories, retaining exact reviewed commits and the
distinction between direct full-text review, selected-section review and missing
sources. Independently inspect the new mathematical interfaces and code.

The recovered baseline is local commit `c72fa33`, descended from GitHub's
`dbd954eede479a5129831e4e7c30537389ae973d`, plus unpublished corrections in the
previous working tree. It includes a 316-page monograph, a 70-page fluid
supplement, interactive laboratories and 82 historical Lean declarations. The
unpublished additions bring the selected formal interface set to 115 and add
cryptographic wrappers, reduction contracts, transport corrections and a Pages
builder. The resumed build now records 341 monograph pages, 90 supplement pages, 269
named mathematical environments and 115 selected extension declarations.
The original arithmetic/analytic package has a separate audit and is not
added to the extension declaration count.

**Acceptance:** an inventory, source-coverage records, independent reviews, a
cleanly identified publication baseline, and an explicit list of unresolved
claims. This is a review of the actual available material, not a promise that
every outbound link or every line of every inherited proof has been audited.

## Chunk 1 — consolidate the mathematical extension

Integrate the existing fluid, reduction, quantum/spin, toric transport and
implemented-cryptography chapters into both manuscript entry points. Retain
exact hypotheses and distinguish local proofs, external theorems, numerical
evidence and open research obligations. Update the claim register and formal
coverage map after the integration.

The OpenAI result concerns smooth **externally forced**, finite-energy
three-dimensional breakdown (Clay C/D). Its analytic and formal artifacts must
be cited at their actual scope. The extension must not recast it as an unforced
positive-viscosity result. Finite-dimensional energy decay, tropical leading
orders, information reduction, neural trainability and numerical examples do
not establish the missing infinite-dimensional regularity estimates.

The GRH/Hilbert–Pólya application remains conditional on an independently
constructed positive spectral realization and the required arithmetic
determinant comparison. A finite matrix gap is not a continuum Yang–Mills mass
gap. Present these as precise research obligations, not completed theorems.

**Acceptance:** chapter dependencies resolve, the written claims are scoped,
independent review findings are addressed, and all new statements are classified.

## Chunk 2 — validate the Lean interfaces

Compile all six selected modules using the existing pinned Lean 4.24.0 and
mathlib revision. Print each theorem's exact type and axiom dependencies. Reject
`sorryAx`, unproved project axioms, compilation errors and warnings. Map each
declaration to the precise manuscript component it actually formalizes; avoid
claiming that a component theorem formalizes an entire composite argument.

Keep the external Navier–Stokes formalization separate, with its own Lean
version and source pins. Its previous full rebuild stopped because dependency
downloads were rate-limited. Only mark it independently kernel-verified if the
entire required build and appropriate statement/comparator checks actually
finish. A source audit and a successful local interface build are separate
forms of evidence. Do not repeatedly stress a rate-limited service.

**Acceptance:** fresh, source-hashed local verification logs; a complete local
type/axiom inventory; an honest external build status and remaining obligations.

## Chunk 3 — validate executable mathematics and cryptography

Run the existing finite algebra, fluid, quantum-channel, toric and transport
checks with meaningful positive and negative cases. Correct any validation
driver that can falsely pass when checks are disabled. Preserve the previous
GPU experiments as recorded experiments and retain their data/checkpoint hashes.

Validate the implemented AES-256-GCM, ChaCha20-Poly1305, Ed25519 and ML-KEM
interfaces against the actual maintained backend. Verify malformed inputs,
tampered ciphertexts, wrong contexts, signatures, KEM sizes and implicit
rejection. Document key/nonce lifetimes, trust boundaries and the difference
between a KEM and an authenticated communication protocol. These wrappers do
not invent a cipher or derive cryptographic security from GRH. A regression
suite is not a proof of computational security or a FIPS certificate.

**Acceptance:** affected checks pass normally, negative cases fail as intended,
versions/hashes are recorded, and no secrets enter artifacts or logs.

## Chunk 4 — rebuild the documents and combined website

Rebuild the monograph and fluid supplement from the integrated source. Reject
undefined references/citations, missing characters and layout overflow; inspect
representative new pages visually. Refresh the claim register, downloads, Lean
archive and compact source archive only after their source inputs are stable.

Combine the current atlas with the inherited GRH Pages material. Preserve old
paths, fragments and query strings where practical. Build for the project path
`/GRH-research/`, including module imports, workers, fetches, images and download
links. Run static dependency/link checks and rendered browser checks for the
main page and representative interactive laboratories. Add reproducible Pages
deployment configuration using the existing repository's supported mechanism.

**Acceptance:** PDFs and download archives match final source, local references
resolve, representative interactive controls work, and the publication package
preserves both bodies of work.

## Chunk 5 — publish and verify GitHub Pages

Commit the consolidated source and evidence. Re-read GitHub's branch head before
publishing so concurrent work is preserved. Transfer the content through the
authorized GitHub connection, verify uploaded object/tree hashes, and move
`main` with a non-forced update only after all required objects exist. Confirm
the resulting remote commit. Deploy the combined Pages bundle and check the
actual public page and representative downloadable artifacts.

**Acceptance:** GitHub `main` has the reviewed content, the deployment's source
commit is identified, the site is served successfully at the requested Pages
URL, and the published artifacts match the release manifest. If a hosting
permission or upstream service blocks completion, record the exact failure
without reporting publication as successful.

## Chunk 6 — synchronize machines and deliver the completion record

Use Remote Desktop Commander to inspect and update the confirmed Iska clone at
`/home/iska/Documents/amelie/GRH-research`, and establish the corresponding clone
on the user's local machine. Use the requested RustDesk surface to confirm the
remote machine/session where available. Preserve local modifications and use
fast-forward pulls when possible; isolate the published revision if unrelated
local work prevents a clean update. Initialize required submodules at their
pinned commits rather than silently advancing their branches.

Compare each clone's commit, clean/dirty status and selected source/document
hashes with GitHub. An installed or running RustDesk process alone does not
prove that a remote desktop session was established. Record actual device
identities, clone paths and verification outcomes.

**Acceptance:** confirmed remote and local clones contain the published work;
the final report links the repository, Pages site, documents, plan and evidence,
and states exactly which mathematical, source-access or infrastructure
obligations remain open.

## Checkpoint and context policy

Maintain `extension/review/final-pass/IMPLEMENTATION_STATE.md` with the current
chunk, changed files, exact commands/evidence, commits, device identities and
next executable step. Refresh it before context becomes crowded. Full logs and
source inventories remain in files; continuation reads the checkpoint and only
the relevant sections. This supplies durable continuation even when automatic
conversation compaction happens; it does not depend on a chat-only memory.

## Resumed execution status

The frozen interrupted work is published on `research/recovery-20261113` at
`97345b643f6d6c576ef4b3cb9900dab4d820c585`. Fresh continuation work has corrected
optimized-Python false passes, warning acceptance in the Lean driver, Linux
proof-runner portability, incomplete proof archives, stale public metadata,
and process-local TeX discovery. The current documents pass their source-hash
and typesetting gates, and 11 representative physical pages have been visually checked.

The source and site publication steps use ordinary non-forced branch updates.
The existing Pages configuration serves the `gh-pages` branch at repository
root. Each publication reads the branch head first and preserves concurrent
changes. Private authentication material is neither copied into the repository
nor included in any artifact. Terminal output must not expose credential values.

Final publication and machine receipts live in
`planning/continuation-20261113/PUBLICATION_STATUS.json`. This plan defines the
acceptance procedure; that post-release receipt records observed commits and
deployment outcomes without a self-referential archive hash.
