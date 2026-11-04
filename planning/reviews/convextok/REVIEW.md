# Independent review: ConvexTok finite certificates and path-corpus adaptation

Reviewed 2026-11-03 by a separate reviewer agent. **Accepted within the
finite optimization scope below.** No outstanding mathematical defect was
found in the frozen files identified by `hashes.json`. This review does
not certify a language-model experiment, algebraic equivalence, or GRH.

## Source and exact scope

The primary source is Tempus, Whittington, Schmidt, Komm and Pimentel,
[*Tokenisation via Convex Relaxations*, arXiv:2605.22821v1](https://arxiv.org/html/2605.22821v1),
21 May 2026. I independently read the source's definitions, position-graph
construction, integer and relaxed programmes, rounding descriptions/code,
six-word example and experimental qualifications, against the cached
primary text. I did not independently audit all NLP experiments, appendix
plots, upstream training code, model weights or corpus. The implementing
agent's broader source-reading record is separate from this review.

The cached HTML and PDF hashes agree with `planning/convextok/sources.json`:

- HTML: `b1a86c7185b1c674130035544eb33c56f7d7518bc366288066b59d682b2f41c1`
- PDF: `af3697cadcc9091ffcd2421734f89dc2404b7a4384753ea0b875e3d268056212`

The adaptation correctly counts mandatory single-symbol tokens in the
objective but excludes them from the additional vocabulary budget. Equal
substrings share a colour variable across all occurrences. The capacity
inequality is per occurrence, not an aggregate cap on use of a selected
type. Separate unit flows through the nonempty words are equivalent to
the source's joined terminal graph because no candidate edge crosses a
word boundary. Duplicate words retain their multiplicity.

Det and Bias match the source rankings. Exact equality to one in Int is
an explicit rational-witness adaptation of the source's numerical 0.999
threshold. An integral colour in one optimum need not belong to every
optimum. The text supplies the correct interchangeable `ab`/`bc` example
instead of asserting such universal forcing.

## Independent exact oracle

The review artifact
`outputs/checks/2026-11-03-convextok/review/oracle.py` imports only Python
standard-library modules. It does **not** import production tokenization
code, SciPy, NumPy, saved integer optimality values as lower bounds, or an
LP solver. From the literal words and candidate arrays it reconstructs
every occurrence, incidence equation, capacity constraint, budget row and
upper-bound row. It verifies each stored witness with `Fraction`:

\[
Av=b,\quad Gv\le h,\quad v\ge0,\qquad z\le0,
\quad A^Ty+G^Tz\le q,\qquad q^Tv=b^Ty+h^Tz.
\]

Every variable's upper bound is included in `G`, so its dual contribution
is included as well. The sign convention is correct for a minimization
problem with `Gv <= h` and nonnegative variables. Weak duality establishes
the lower bound independently of the integer search; primal equality
certifies the LP optimum. Rational reconstruction is accepted only after
exact feasibility and equality checks, so solver tolerances do not enter
these optimality claims.

For the separate integer comparison, my oracle uses its own **forward**
shortest-path recurrence and exhausts every subset of every size from zero
through K. This checks 2,486 vocabularies. The production count of 2,312
subsets at exactly `min(K, |C|)` agrees; that shortcut is valid by
monotonicity under adding candidates. The oracle also checks Det/Bias/Int
rankings, budgets, greedy counts, valid segmentation tokens and exact
detokenization, independently of production functions.

All 16 stored certificates passed. The decisive final-budget cases are:

| Corpus | K | Exact LP optimum | Exhaustive integer optimum |
|---|---:|---:|---:|
| Source six-word example | 3 | 9 | 9 |
| Original four-word gap | 2 | 10 | 11 |
| Original five-word fractional value | 2 | 31/2 | 16 |
| Genus-two permitted paths, candidates of length 2–3 | 2 | 19 | 19 |
| Genus-four permitted paths, candidates of length 2–3 | 2 | 31 | 31 |

The original four-word corpus's fractional word costs are `3,3,1,3`;
the five-word corpus's costs are `7/2,11/2,5/2,3,1`, matching the prose.
The source example starts with 15 mandatory symbols. The unique most
frequent pair is `ab`, saving three, after which two BPE merges each save
one; cost 10 agrees with the saved baseline. Selecting `bc,bd,be` gives
cost 9, and the independent dual makes this optimality exact. No universal
rounding ratio follows from these examples.

## Actual surface-path scope and convention correction

For m=5 and m=9, the oracle independently reconstructs sigma, alpha,
tau and phi, verifies their stored arrays, the two vertex cycles, m edges,
single face and Euler characteristic `2-2g`. It checks every successive
arrow against tau and against the forbidden successor phi. Labels such as
`a17` remain **one atomic symbol**, rather than multiple printed
characters. The candidate set is exactly the occurring length-two and
length-three subpaths, and the duplicated path remains duplicated.

This is a finite corpus in the project's actual infinite polynomial
locally gentle algebra. It does not replace the algebra by a finite
quotient. The primary source's generalized candidate-set formulation
allows this restriction, but the resulting optimum concerns only that
restriction. The manuscript correctly distinguishes word-position DAG
nodes from surface-quiver vertices and TokenGT's node/edge feature tokens.

An initial version omitted a multiplication convention. This matters
because `a_h a_phi(h)` expresses the forbidden pair only in **travel
order**, whereas a left matrix action writes the factors in reverse
order. The current HTML and TeX explicitly state travel-order products
and their reversal under the left-operator convention, resolving the
ambiguity. The path data itself was unaffected.

Decoding preserves original labels, endpoints and path lengths of these
corpus words. It proves no multiplicativity for arbitrary token
concatenations, no representation of arbitrary completed sums, no
preservation theorem for module maps, no Fukaya/derived equivalence, and
no reduction of the completed order's rank. These limits are correctly
stated. The pre-existing rank `2m^2` is retained, not newly derived from
token compression.

## Focused replays and boundaries

The following fresh replays passed in the existing approved environment:

- Independent oracle: 16 exact certificates; 2,486 at-most-K vocabularies;
  all saved rounding and surface checks. See `review/oracle.json` and
  `review/oracle.log`.
- Production Python checker, run without `--write`: 16 certificates,
  2,312 size-K subsets, 29 independent small segmentation checks, repeated
  capacity, boundary exclusion, three perturbed-witness rejections and
  the interchangeable optimum example. See `review/production-check.log`.
- Node checker: 48 rounded vocabulary replays with shortest/greedy counts
  and decoding. See `review/web-check.log`. This is a numerical JavaScript
  replay, **not** a browser visual/layout review.

An initial empty-word incidence-row bug was confined to inputs outside
the saved corpus. The API now rejects an empty corpus or any empty word
before constructing the LP; fresh rejection checks passed. The TeX
explicitly assumes nonempty words. No saved numerical evidence changed.

I inspected `papers/convextok.tex` and the laboratory HTML/JavaScript.
Their certificate proposition and derivation are correct within the
stated scope. This review did not build or visually inspect the compiled
book/PDF or launch the laboratory in a browser. No Lean theorem is
introduced by this change: exact executable rational certificates and
the written weak-duality proof must not be reported as full Lean
formalization. Large-scale NLP/GPU training, generalization, TokenGT
retraining and the arithmetic determinant/zero-location bridge remain
outside the evidence.

## Reviewed snapshot

Full hashes are saved in `review/hashes.json`. Principal frozen inputs:

- `examples/tokenization/model.py`:
  `70d326f9c961bf4f3b8c936662df481c9b10e020fd87da1bd4f7f6994d6faa73`
- `examples/tokenization/check.py`:
  `0a29a3b02b15b146974e3e60ac01ff953fa6a12ccf8b1988ed9f96a506abdf5e`
- `papers/convextok.tex`:
  `8afdf681c7694f72cc34bfbcbb3ff0bbb185c3ac0f9b91c3dfd8c31cf232ebb2`
- Saved results and identical web dataset:
  `64c3c378b86c127a849bb2bdb35d6500aee574469945e78a1323b6718638065a`
- Independent oracle:
  `4af4e79c74fd25444f45326ca86d5375ee0b53dff63d2504f6be38dd24ae6e0f`

The findings support integrating this as a bounded, original finite
optimization laboratory and explanatory section. They do not change the
project's open mathematical or full-formalization obligations.
