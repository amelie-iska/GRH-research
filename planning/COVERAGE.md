# Review coverage

This file records textual coverage, not a guarantee that every background theorem, transform identity, or formal dependency is independently certified.

| Material | Coverage | Limitations |
|---|---|---|
| GRH PDF, commit0c77122d | All223physical pages, including appendices and bibliography; selected formula pages rendered and inspected | External theorems not all rederived; multiple decisive false steps identified |
| Surface TeX, commit212ff730 | Full textual reading1–15556: foundations reviewer1–9999 and15370–15556; completion reviewer10000–15376 | Selective derivation checks and exact counterexamples; not certification of all algebraic/hardware claims |
| Surface PDF in same repository | File inventoried and hashed; TeX audited in full | PDF is a distinct tracked artifact and has not been read end to end or proved identical to TeX |
| math September7/8 paper | All16677source lines read; exact blob verified; selected endpoint algebra and continuation checks | Lengthy theta/sieve/moment estimates and external inputs not independently certified in full |
| math October11/12 paper | All3988source lines read; exact blob verified | Main reflection/uniformity and Poisson regrouping require specialist verification |
| math Landau–Siegel paper | All773 source lines read; exact blob verified; determinant/interpolation stress checks | No decisive refutation established in this review; not a certification of the major claim |
| math Lean root/config | README, family003 docs, comparator instructions, lakefile, manifest/toolchain; actual two conclusion modules and comparator files inspected | Upstream Lean4.34.1/package graph not built |
| math formalization graph | Static transitive OAI graph of two actual solution modules:3125 modules, no missing local import and no sorry/admit/axiom token matches | No kernel verification; external packages not traversed; static token scans cannot certify semantics |
| Other math text matches | 27candidate TeX files triaged by matching contexts | GrH cohomology/macros/vendor-code false positives excluded; applications and historical RH mentions not full proof sources |
| New papers | Full core/details reviewed independently; PDFs compiled, representative pages rendered and inspected | Research drafts, not full GRH proofs or journal acceptance |
| New Lean | All6 named statements built and axiom reports inspected | Only finite/arithmetic obstructions; no analytic GRH formalization |

No repository AGENTS.md files were found in the three clones. Root user instructions governed preservation. No source clone was edited, updated, cleaned, migrated or rewritten. The large math clone contains174524tracked files; reviewing the selected RH family is not a claim to have reviewed the entire collection.
