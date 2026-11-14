# Publishing this research clone

The reviewed working branch is `research/orders-complexes-20261113`, based on
the original GRH repository at
`dbd954eede479a5129831e4e7c30537389ae973d`. The original remote is named
`upstream`. At the author's explicit request, the publication destination is
the existing **amelie-iska/GRH-research** repository and its `main` branch.
Publication preserves the original history and uses a fast-forward update.

The supplied publication command is:

```sh
bash extension/code/publish_github.sh
```

It requires an existing, valid GitHub CLI session for `amelie-iska` and a clean
committed working tree. It verifies the existing repository, adds `origin`
only when absent, checks that the published `main` is an ancestor of `HEAD`,
pushes the reviewed commit, and verifies the remote commit hash. It never
force-pushes, creates another repository, changes visibility, collects
credentials, or changes `upstream`. If `origin` points elsewhere, it stops.

Normal GitHub CLI sign-in, when needed, is performed interactively by the
account owner with `gh auth login --hostname github.com`. Passwords, access
tokens and verification codes must not be added to this source tree.

## Website preparation

The website source is `extension/site`. Rebuild the inherited section with:

```sh
python3 extension/code/prepare_legacy.py
python3 extension/code/verify_legacy.py
```

These commands preserve the original `web/` files, assemble publication
dependencies into `extension/site/legacy/`, and verify the source and served
asset hashes. The build requires the full cloned repository; the compact
companion archive alone omits the inherited assets.

Create the compact deliverables outside the source tree with Python 3.11 or newer:

```sh
python3 extension/code/package_release.py --output /absolute/path/to/deliverables
```

Copy the resulting monograph PDF, fluid supplement PDF, compact source ZIP
and Lean ZIP into the documented `extension/site/downloads/` paths before
publishing the website.
The release's published copies already contain these files. The source ZIP
excludes that generated download directory to prevent recursive archives.

The complete repository ZIP is generated from a clean commit using the same
command with `--complete`. Git submodule dependencies retain their pinned
references and are not recursively vendored into that archive.

The hosted page is published from a separate managed Site checkout. Its
deployment record identifies that pushed Site commit; the research clone's
commit and the Site commit are different repositories and are reported
separately. A successful Site deployment does not by itself verify the GitHub
branch; both publication records are checked independently.
