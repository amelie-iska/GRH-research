# Source-led proof port

`inventory.py` preserves exact statements, adjacent proofs, source locations,
Git object identities and SHA-256 hashes. Its original-source bundle and JSONL
claim register are publication artifacts, not an automatic validation of every
claim. Duplicate source versions remain attributable and have distinct identities.
Mora-3 Markdown methods are preserved as documents rather than silently assigned
LaTeX theorem counts. The inaccessible TropicalGT-Program name is recorded, not
silently substituted by ToricGT-Program.

The dedicated graph expressivity manuscript `TropicalGT/references/main.tex`
is essential source material in addition to the ToricGT and tropical-quiver
proofs. The integrated treatment will preserve both positive constructions and
explicit upstream qualifications. It will also expose, not conceal, dependency
repairs and exact counterexamples found during review.

Reproduce offline from pinned source snapshots:

```
python3 workbench/proof_port/inventory.py --snapshots /path/snapshots --output /path/fresh-port
```

Add `--download` to acquire the specified public source objects. No credentials
are read. The source archive is separate from original measured-data training
records; mathematical text is not admitted into a model corpus by this utility.
