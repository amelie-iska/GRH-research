# Publishing the reviewed research and combined atlas

The existing destination is **amelie-iska/GRH-research**. Source belongs on
`main`; GitHub Pages is already configured to serve the `gh-pages` branch at
its repository root. Both updates must be fast-forward updates preserving
concurrent work. No repository creation, visibility change or force push is
part of this procedure. The original public base is
`dbd954eede479a5129831e4e7c30537389ae973d`.

## Validate source and artifacts

Work in the full clone. Finish source edits and the pinned Lean/numerical checks
before rebuilding the manuscripts. Then run, in order:

```sh
python3 extension/manuscript/build_pdf.py
python3 extension/manuscript/build_pdf.py --main fluid-extension --min-pages 1
python3 extension/review/build_claim_register.py
python3 extension/review/final-pass/check_evidence_health.py --self-test --output-dir extension/review/final-pass
node extension/site/verify-fluids.cjs
python3 extension/code/refresh_site_release.py
python3 extension/code/package_release.py --output /absolute/path/outside-the-clone --sync-downloads
python3 extension/code/release_freshness.py --site --archives
```

The PDF build verifies stable source inputs, citations, glyphs and layout
overflows. Representative final pages need visual review as well. The release
gate checks input hashes and archive membership, including nested Lean logs;
it does not independently prove the underlying mathematics. Do not edit an
included source after packaging without refreshing the affected evidence and
repackaging. Generated download directories are excluded to avoid recursion.

The complete committed repository can additionally be archived with
`package_release.py --complete`. The compact companion omits the duplicated
legacy assets and retains original submodule URLs/pins; clone the repository
and initialize its required submodules when those dependencies are needed.
Third-party book scans, downloaded full texts and private authentication
material are not publication inputs.

## Publish the source

Commit the reviewed tree, fetch the current remote main, and ensure it is an
ancestor of the candidate. The existing script performs these checks:

```sh
bash extension/code/publish_github.sh
```

It uses the ordinary authorized GitHub CLI session and a per-command GitHub
credential helper. A process-provided `GH_TOKEN` can be used without persisting
credentials in Git configuration. Credential values must never enter source,
command arguments, logs, archives or commit messages. `keys.txt` is ignored.
The script verifies the repository/account and checks the resulting remote SHA.
The selected GitHub connector is also supported: upload objects, verify the
exact tree hash, create the commit with the observed parent, and update the
branch non-forced with the expected-head lease. Record the resulting remote
commit rather than assuming the unpublished local commit hash is preserved.

## Build and publish Pages

Build into a fresh directory outside the clone:

```sh
python3 extension/code/build_github_pages.py --output /absolute/fresh/pages --base /GRH-research/
python3 extension/code/check_github_pages.py --site /absolute/fresh/pages --report /absolute/outside/pages-check.json
```

The builder combines the atlas and inherited GRH pages, preserves compatibility
paths and emits `.nojekyll`. Static reference checks and adapter tests do not
replace rendered checks of dynamic fetches and controls.

Fetch `gh-pages` immediately before publishing. Create an isolated worktree
based on that exact commit, copy the verified output into it while preserving
its `.git` worktree metadata, commit, and push `HEAD:gh-pages` without force.
If concurrent changes prevent the push, inspect and integrate them first.
Confirm GitHub's deployment source commit and inspect the public
[project site](https://amelie-iska.github.io/GRH-research/), its laboratories,
compatibility pages and downloadable PDFs/archives.

## Synchronize and record

Preserve machine-local changes. A clean clone can fetch and fast-forward
`main`; a dirty clone requires an isolated checkout or explicit reconciliation.
Compare commit IDs and selected document/source hashes with the published
release. Never report a running RustDesk process as proof of an authenticated
remote desktop session.

Post-release receipts are stored under
`planning/continuation-20261113/PUBLICATION_STATUS.json`. This location sits
outside the compact source archive and records publication/deployment/machine
observations without creating a self-referential archive hash. The hosted
managed Site remains a distinct historical deployment; GitHub Pages is the
requested combined publication target.
