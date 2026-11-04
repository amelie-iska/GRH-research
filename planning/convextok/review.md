# ConvexTok v1: primary-source review and project adaptation

Reviewed 2026-11-03: [full v1 HTML](https://arxiv.org/html/2605.22821v1) and
[26-page PDF](https://arxiv.org/pdf/2605.22821v1). The exact retrieved hashes
and read scope are in `sources.json`. Main sections 1–6, all footnotes,
references and appendices A–J were read; all PDF pages, plots and tables
were visually inspected in contact sheets. No linked upstream code or
language-model campaign was reproduced. Retrieved source caches remain
local and ignored; original exposition and executable examples are new.

The load-bearing source definitions are §§2–3: a mandatory alphabet is
outside the additional vocabulary budget K; token instances are position-DAG
edges; equal strings share a colour variable. Equations (5) and (6) of the
PDF are respectively the binary programme and its [0,1] relaxation.
The incidence convention is −1 at source, +1 at target. Every priced
occurrence has its own capacity p_e≤c_t. This is not a pooled usage budget.
Terminals may be joined between words, but edges never span word boundaries.
Our equivalent separate unit-flow equations retain word multiplicity.

The paper's §3.3 Det selects the K largest c values; Bias selects the K
largest c/length values; Int keeps approximately integral values (the
paper's code uses 0.999). We use exact rational equality for Int. All
choices are followed by a discrete shortest-path computation. A particular
LP solution's c_t=1 does not imply t occurs in every optimum: the one-word
corpus abc with K=1 and candidates ab,bc has interchangeable optima.
The review found no general approximation-ratio theorem for these rounding
rules; empirical near-optimality must remain attached to the paper's data,
objective, candidate/pretokenization constraints and solver tolerances.

The source's numerical qualification matters. Table 2 includes a Det value
below the displayed LP value at 256k, acknowledged in footnote 13 as within
solver tolerance. A floating feasible primal objective need not be a valid
lower bound. Our use of the paper is a small original formulation followed
by independently checked rational primal AND dual feasibility and equality.
Integer optima come from exhaustive candidate-vocabulary enumeration.

The source's §4 large LP and GPU/nanochat training, §5 intrinsic/BpB/CORE
results, and appendices D–J do not constitute experiments in this project.
Its BpB and downstream findings are empirical; CORE is mixed, and most
deeper-model settings have one training run. Appendix B discusses direct
integer optimisation alternatives; Appendix C sketches the path/token
maps. These do not remove finite-corpus, candidate-set or generalisation
limits. No new NLP performance claim is drawn from our examples.

Project evidence has three distinct labels:

- **Reproduced tiny source example:** abc,abd,abe,bc,bd,be with K=3: LP=IP=9,
  frequency-driven BPE merge output 10. All 35 vocabularies are exhausted.
- **Original finite counterexamples:** a four-word corpus with LP10<IP11
  and a five-word corpus with LP31/2<IP16, including Det/Bias/Int and
  longest-first versus shortest-path comparisons. Literal witnesses and
  all occurrences are in the saved records.
- **Original surface application:** finite corpora of permitted arrow words
  on the actual genus-two/four dessin polynomial locally gentle algebras.
  Symbols are arrow identities, not their label's bytes. Candidate subpaths
  have length two or three. Therefore LP19=IP19 and LP31=IP31 bound those
  candidate classes only. Travel-order products traverse their left factor
  first; a left-operator matrix representation reverses the product.

Tokenization only renames finite substrings. Decoding preserves a corpus
word, endpoints and original path length. Arbitrary token concatenation
still needs composability checks. No algebra homomorphism, quotient,
completion, equivalence of categories, module-map preservation theorem,
token-to-TokenGT identity, training improvement, GPU result, arithmetic
determinant bridge or GRH proof follows.

Verification uses the existing `.tools/book-quantum-cpu` environment with
no package installation or model training. Initial evidence is immutable
under `outputs/checks/2026-11-03-convextok/`; `review-fixes-checks.json`
records the later source hashes and rerun after explicit empty-word guards.
The API rejects an empty corpus or any empty word with ValueError before
constructing incidence rows. The segmenter itself can return an empty
segmentation. UI examples all contain nonempty words.
