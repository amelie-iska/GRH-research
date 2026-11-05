# Focused article build handoff

Completed remotely on iska-linux-vscode, 5 November 2026. No production source/PDF edit, promotion, package installation, environment change, deletion, Git staging or Firefox use was performed.

## Accepted candidates

| Edition | PDF path | Pages | SHA256 |
| --- | --- | ---: | --- |
| Concise | outputs/article-integration-20261104/concise-v1/resolutions-concise.pdf | 49 | 864343a20f9eb9bbed6fcb51ce51b6d620d1e67a5f69b57c88613f0a07358788 |
| Extended | outputs/article-integration-20261104/extended-v1/resolutions-extended.pdf | 129 | 2fb084edc769952ea11628a37d3f8323516542d91af3f1ba5cd75dfd9462f93f |

Each candidate passed three fresh-directory pdflatex passes using an absolute expanded-input filename. All four new proof markers and their aux labels are present. Complete current-source expansion and the exact closed transformation were audited; all 61 unique recorded inputs remain SHA-identical, including 30 concise and 52 extended canonical paper inputs.

The only renderer changes are full-source-hash diagram substitutions, removal of unused drawing package imports, addition of installed graphicx/xcolor imports and absolute figure paths. All remaining source/math/prose/caption/label order is exact. Canonical TikZ bytes remain unchanged. Earlier source-before wrapper snapshots differ from the already integrated task-start wrappers; their earlier integration diffs are retained separately, not attributed to this worker.

No overfull boxes, unresolved citations/references, duplicate-reference warnings or compile errors remain. The preserved exact-source logs contain one existing amsmath atop warning in concise and atop plus over warnings in extended, with seven underfull hboxes per edition.

## Review acceptance boundaries

Root independently compared the source/node/edge/geometry manifest and label sides/signs for both source-specific grids, then inspected their standalone previews. Root also inspected final extended pages 40 and 41, concise page 42 and extended page 118, accepting those layouts as clean and readable with the exact signs/hooks. The acceptance is bound to the original candidate PDF hashes above and the selected image hashes in final-page-root-acceptance.json. This is representative layout acceptance, not a claim that every page received a new independent visual examination.

Quotient grid source dd2a7bb5cd4f6a3c8d94e8bd3616cc9442d0ce31655c67d34226b99af16ae0d4 has 15 nodes, 12 rightward arrows including three hooks, and six downward arrows. The x labels occur only in the first two Lambda-to-X rows, u labels only on the top downward layer; no vertical arrows at the zero columns were added.

Signed diamond source 5cebac09f8e9accfd86178b4ea896294573b28039291334f28aa9f46ce34b722 has nine nodes and 12 arrows. Rows carry p,i; downward layers carry -p,p,-p and -i,i,-i. Left-column minus labels stay left, remaining vertical labels stay right. The period after I remains punctuation. No short-exact-row/column claim is added.

These checks certify fixed-source rendering fidelity. They establish no new analytic theorem, Lean declaration, full-article formalization or GRH proof. The source's mathematical qualifications remain unchanged.

## Evidence

- candidate-summary-v1.json: combined source freeze and candidate identities.
- audit-v1/source-preservation-audit.json: exact expansion/transformation, cache sole-body/source-hash checks, three-pass and proof-marker checks.
- grids-v1/grid-manifest.json: exact original blocks, node/edge geometry and vector hashes.
- grids-v1/root-acceptance.json: independent semantic and standalone visual acceptance.
- final-page-root-acceptance.json: selected final-page acceptance.
- visual-v1/visual-manifest.json: all 16 rendered page-preview hashes.
- reproduction-v1/reproduction-record.json: successful fresh reproduction through the proposed standalone script.
- planning/article-integration-20261104/audit_candidates.py: audit source.
- planning/article-integration-20261104/README.md: commands and scope.

All output evidence paths above are relative to outputs/article-integration-20261104 except those beginning with planning/.

## Proposed production copy plan for root

The standalone candidate is planning/article-integration-20261104/proposed-build_remote_articles.py, SHA256 59b09b7b1f5acc24d416efa3884fc496edbc6a9dab867389e54310dff8c5afc2. It differs from the executed original builder only in repository-root discovery, allowing it to live under scripts/. It retains fresh-output refusal, source-freeze and independent grid acceptance gates, and does not publish.

Root may review and copy that exact script to scripts/build_remote_articles.py. Root may separately promote the accepted original candidate PDFs above to outputs/papers/resolutions-concise.pdf and outputs/papers/resolutions-extended.pdf after checking the frozen inputs still match. Do not copy expanded render sources over canonical papers or original TikZ blocks. This worker has performed none of these production copies or any checkpoint.

The proposed script was executed in reproduction-v1/concise and reproduction-v1/extended. Both reproduced the original candidate PDF text byte-identically, retained 49/129 pages, used identical canonical hashes and produced identical expanded compile source except the absolute output-directory paths. PDF file hashes differ because fresh PDF metadata/IDs are not byte-deterministic; accepted original candidates remain the promotion targets.
