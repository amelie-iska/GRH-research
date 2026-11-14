# Primary source and reproduction boundary

[Tokenisation via Convex Relaxations, arXiv:2605.22821v1](https://arxiv.org/html/2605.22821v1),
Tempus, Whittington, Schmidt, Komm and Pimentel, 21 May 2026.
Reviewed 3 November 2026: full main text, references, footnotes and
appendices A–J; all 26 PDF pages and their figures/tables visually inspected.
The pinned HTML SHA-256 is
`b1a86c7185b1c674130035544eb33c56f7d7518bc366288066b59d682b2f41c1`;
the pinned PDF SHA-256 is
`af3697cadcc9091ffcd2421734f89dc2404b7a4384753ea0b875e3d268056212`.
Original files remain in a local ignored review cache.

The project uses the finite position graph, per-occurrence token capacities,
extra-token budget, LP relaxation and three rounding rules of §§2–3.
The paper's six-word example is the one reproduced tiny benchmark.
The two integrality-gap corpora, higher-genus arrow-path application,
exact rational certificates and interactive interface are original.

A solver's approximate objective does not alone certify a lower bound.
The paper itself qualifies its numerical values and reports a small
below-bound anomaly within solver tolerance in Table 2, footnote 13.
Here every displayed optimum has a checked rational feasible primal and
dual with equal objectives, and integer comparison uses exhaustive subsets.
Rounding has no asserted universal approximation ratio. Integral colours
in a selected optimum are not universally forced tokens.

The source's large LP/GPU and NLP experiments were read as reported results
and are not reproduced. No upstream code, training corpus, weights or
language-model experiment was installed or executed. This finite tool
cannot imply downstream model gains or a theorem about the full surface
order, categories, arithmetic determinants or GRH. The detailed repository
review and machine-readable provenance are `planning/convextok/review.md`
and `planning/convextok/sources.json`.
