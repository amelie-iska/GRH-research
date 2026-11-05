# Four isolated signed-divisor staging builds

PASS. All four existing three-pass workflows completed from the frozen canonical core `bce916fab66aab19718a127b26b3ac581e48f49e0dd0317a64cf1648a4e5b7cb` and details `504318141e100fd43f1021492c349a655953909b3213a083452d1230fa35cbc9`. No source or production artifact was edited or promoted by these builds.

| Candidate | Pages | Build-record SHA256 |
|---|---:|---|
| concise-v1 | 64 | `0f00a1f57e0f9a95be138eeb877e2f2bfcf4c7be06af653154d7744221494a6a` |
| extended-v1 | 175 | `42029d78ca2876457d260498d72110a89562f58fc96dd08b41413f73c4663cea` |
| notes-concise-v1 | 23 | `382ceedb0cd7e70b6881d21b90c8a4ea459a6553a700d52f84c946dbbc7c40d8` |
| notes-extended-v1 | 66 | `24a106ba899c48815cc93e4aaca17c337941b57faeaf0410508d42f567f608b9` |

All recorded recursive sources remain current. The focused articles use unchanged `scripts/build_remote_articles.py`; notes use the newly preserved stdlib recursive expander `build_notes_v1.py`, implementing the prior inline notes workflow. Every TeX pass runs at nice increment15 on one allowed CPU with OMP/OPENBLAS threads1. Fresh staging paths preserve all prior attempts.

The final logs contain no overfull box, undefined reference/citation, multiply-defined reference/label, missing-character diagnostic or TeX error. Their complete Warning-line lists equal those of the prior accepted signed-weights builds, including multiplicities. Inherited amsmath warnings concern foreign commands atop (all editions) and over (focused extended); the extended editions retain the same two hyperref PDF-string warnings. Underfull counts equal the prior7/7/0/0. No additional warning was found.

The new signed-divisor section is present in extracted text of every PDF; extended notes also verify the new details heading. The focused builder and preserved notes helper check unique expanded labels and exact source hashes. All nine protected source/release HEAD/index states match their pre-build pins. The four builds took6.586 seconds in total. No browser, new dependency, compiler installation, science rerun, auth, publication, or production promotion occurred.

This acceptance concerns exact-source compilation and log/source checks. It does not add a mathematical result or standalone visual PDF review. Root owns promotion and final book/native review.
