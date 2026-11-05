# Signed covariance milestone release preparation

Inventory only. No publication worktree or source copy has been created.

Public baseline: 290f6a2ce5b9f2acb4e321c8b957ecaa3d82c385. Requested worktree: /home/iska/Documents/LaTeX-projects/GRH-publication-20261105-signed. Original research checkout HEAD and index are bound in inventory-v1.json.

After root final document and promotion signal: create a fresh detached worktree at the baseline; copy only inventoried changed/new milestone files and any explicitly identified link closure dependency; retain origin-identical dependencies without copying; explicitly stage selected files (including approved PDF logs despite ignore rules); run credential-pattern, source-pin/original manuscript, final PDF/log/MathML/source integrity and local-link checks; create a fresh static bundle with scripts/build_public_site.py after new sources are staged; adapt the previous stdout-only API inventory/content generator into outputs/publication/20261105-signed/release-preparation-v1; freeze main/pages overlay manifests and return them for root-only authenticated publication. No commit, push, authentication, package installation or root-index changes.

The static builder reads git ls-files, so all selected new web/source inputs must be staged before bundle construction. It copies the three canonical book/focused PDFs directly; ensure the two notes are included through their already-public web links/assets and inspect all scoped links. Keep the public bundle's existing source-link closure file papers/dessin-core.tex if the builder still omits it, using exact baseline bytes.

Final v3 articles/notes: 51/133 and 9/24 pages. Expected book:237 pages,40 chapters,6412 MathML nodes. Historical standalone-note title dates remain unchanged per root. Initial inventory is provisional until the final signal.
