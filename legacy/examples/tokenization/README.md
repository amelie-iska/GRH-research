# Certified finite tokenization examples

This original CPU implementation uses the graph/LP formulation of
[Tempus et al., ConvexTok v1](https://arxiv.org/html/2605.22821v1).
The paper's small six-word example is reproduced. Two other tiny corpora
show strict integrality gaps; genus-two and genus-four corpora compress
actual permitted paths in the project's infinite polynomial locally gentle
algebras. Each arrow identity is one alphabet symbol.

Run in the existing approved environment, without installing anything:

```sh
.tools/book-quantum-cpu/bin/python examples/tokenization/check.py
node --check web/convextok.mjs
node examples/tokenization/check_web.mjs
```

`check.py --write` creates deterministic evidence only if a path is new or
already has identical bytes. It refuses to change a differing saved file.
Initial evidence records the initial code hashes; `review-fixes-checks.json`
records a fresh validation after the independent-review fixes. The normal
command performs checks without modifying saved artifacts. Imports never
train, access the network, or write files.

Five corpora, sixteen budget cases, sixteen exact rational primal/dual
certificates, and 2,312 exhaustive vocabulary subsets are checked. Focused
checks compare the DP against 29 independent all-segmentation enumerations,
reject three corrupted witnesses, enforce separate word boundaries and
test reuse of a selected token in two occurrences. Empty LP corpora/words
raise ValueError. The JavaScript segmenter independently replays all 48
rounded vocabularies, both shortest and greedy counts and every decoding.

The saved full witnesses are `outputs/checks/2026-11-03-convextok/results.json`
and `web/data/convextok.json`. They use min qx, Ax=b, Gx≤h, x≥0, including
upper bounds in G. Dual vectors satisfy z≤0 and Aᵀy+Gᵀz≤q; exact equality
of primal and dual values certifies the displayed finite LP optimum.
SciPy/HiGHS merely proposes vectors; rational checks have no float tolerance.

K counts extra token types beyond mandatory symbols. Each candidate
occurrence has its own x_e≤c_t constraint. Candidates never cross words.
Rounding ties are lexicographic; Int uses exactly c_t=1, which does not
imply that token occurs in every optimum. BPE is a frequency-driven pair
merger with a deterministic overlap/tie convention. Surface examples omit
BPE comparison because unrestricted merges would change the allowed
candidate class; their candidate subpaths have two or three arrows.

[Local interactive lab](http://127.0.0.1:8765/convextok.html) ·
[Scope and source review](source-review.md).
The lab uses saved LP bounds and integer optima and recomputes live
discrete segmentations. It never trains a language model or changes the
algebra. TokenGT's node/edge feature tokens are a different representation.
No categorical equivalence or arithmetic/GRH claim is made.
