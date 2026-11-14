> Historical checkpoint: this file records the initial 158-page review pass. The subsequent complete OCR-content coverage is documented in `supplemental-content-review.md` and `content-reading-coverage.json`. Staging paths and “when built” language below describe that earlier checkpoint; current deliverables are in `extension/manuscript/`, `extension/lean/`, and `extension/review/volume-two/`. The final first-release 187-page PDF and its successful build records are already present.

# Review of *Lattices over Orders II* and the complexes interface

## Identity and scope

The supplied scan is Klaus W. Roggenkamp, *Lattices over Orders II*, Lecture Notes in Mathematics 142, Springer, 1970, DOI [10.1007/BFb0058955](https://doi.org/10.1007/BFb0058955). Roggenkamp is the sole named author of this volume. Verena Huber-Dyson, the coauthor of Volume I, is acknowledged in the preface. The source has 392 PDF pages. Beginning with PDF page 6, the printed page is the PDF page minus five.

Source SHA-256: `279f7df1a2e07373ff2aa88a1692e12946b4c2e98a16e2269e6469190fb8ff85`.

This review supports an original mathematical exposition. It does **not** certify a complete line-by-line proof audit of the scanned volume or an exhaustive review of Roggenkamp's entire oeuvre. The original scan and its full OCR transcription are research intermediates; they are not intended for republication in the project repository.

## Coverage and reproducibility

All **392 of 392 pages** were rendered and processed with Tesseract, at 145 dpi, with three worker processes and one OpenMP thread per process. The resulting 99,149 OCR words permit text search and thematic review. The page-level manifest, `ocr-coverage.json`, records extraction status, chapter, printed page, and review tier. Successful OCR extraction is not a certificate that a formula has been read correctly.

The prose surrounding selected statements was read closely, particularly the beginning of Chapter VI, Chapter VIII's definitions and comparisons of Grothendieck groups, portions of Chapters IX and X on hereditary and Bass orders and finite representation type, and the bibliography and errata. Explicitly recorded passage-level reading covers PDF pages 1, 3–30, 75–181, 199–202, 257–259, 265–266, 292–295, 309–311, and 387–392. Several additional pages were rendered for targeted inspection. The essential original-page checks for the claims below are PDF119 (printed114), PDF144 (printed139), and PDF392 (printed387). Not every rendered page is counted as a visual proof audit.

The OCR frequently confuses subscripts, ideals, Greek letters, arrows, and equality versus isomorphism. Statements requiring those distinctions were either reconstructed independently under explicit hypotheses, checked against the page image, or left as cited external results. The manuscript does not inherit a formula simply because it appears in OCR output.

| PDF pages | Printed pages | Content | Use in the new exposition |
|---|---:|---|---|
| 1–5 | front matter | Title, preface, contents | Authorship and historical scope |
| 6–74 | 1–69 | VI. Modules over orders and ideals | Integral versus generic categories; lattice presentations |
| 75–109 | 70–104 | VII. Genera | Local/global distinction and stable classification context |
| 110–180 | 105–175 | VIII. Grothendieck groups | Exact and split Grothendieck groups, stable equivalence, scalar extension |
| 181–291 | 176–286 | IX. Special types of orders | Hereditary and Bass hypotheses; warnings against unrestricted transfer |
| 292–387 | 287–382 | X. Number of indecomposable lattices | Finiteness depends on algebra and coefficient-ring hypotheses |
| 388–392 | 383–387 | Bibliography, index, Volume I corrections | Primary-source traceability and correction of a false proof |

## Mathematical findings and corrections

### 1. An order supplies an integral category, not a Euclidean metric

The volume studies lattices as modules over an order in a finite-dimensional algebra over the fraction field. Their relevant structure is integral, local, and representation theoretic. A cryptographic lattice additionally needs a specified embedding into a real inner-product space, an effective basis, distributions, and complexity parameters. None of those follows from an abstract module category. The manuscript therefore keeps the algebraic and metric structures distinct and introduces a comparison only after specifying the additional data.

A second distinction is equally important: a lattice is torsion-free over the base domain, but need not be projective over the order. Over a Dedekind base it is projective as a module over that base. Projectivity over the order requires extra hypotheses. The exposition proves extension closure directly and isolates the hereditary-order case, where a lattice embeds in a finite free module and is consequently projective.

### 2. Several different Grothendieck constructions occur

Chapter VIII distinguishes relations from short exact sequences, relations from direct sums, and projective-module versions. Relevant landmarks include VIII.1.2 (exact-sequence construction), VIII.1.6 (split construction), VIII.1.7 (stable-isomorphism criterion), VIII.1.12 (Morita invariance), VIII.2.4 (Whitehead-type groups), and VIII.3.1 (comparison involving lattice presentations and Schanuel's lemma). The original chapter uses historical notation that is not uniform with current conventions.

The manuscript explicitly distinguishes `K_0^split`, exact `G_0`, and projective `K_0`. It supplies new proofs of the universal property, the stable-equivalence criterion in the split group, the Euler characteristic identity for finite complexes, contractibility of bounded acyclic complexes of projectives, and Schanuel's lemma. These proofs state their hypotheses independently of uncertain OCR formulas.

VIII.5.1, a cancellation/classification result associated with Jacobinski, must retain its Eichler-type and summand hypotheses. It is not a general statement that every stable equivalence cancels. Likewise, the finiteness theorem near X.2.1 is proved in a particular complete local setting, including restrictions on the semisimple algebra and residue field. It does not establish a universal finite classification of lattices over arbitrary orders.

The full OCR prose of Chapters VII and VIII was also read. Its definitions of genus (local isomorphism) and restricted genus (stable equivalence), the local-to-global direct-summand discussion, and Jacobinski's cancellation conditions support these distinctions. The notation-heavy idelic and norm formulas remain OCR-sensitive. The review therefore relies on their explicitly visible hypotheses and thematic role, not an assertion that every formula was reconstructed.

The weighted Gram-rank comparison in VIII.3.5 (printed139/PDF144) is another direct bridge. The original page explicitly uses equality of the rank of a real matrix and its Gram matrix. The manuscript now supplies a complete independent weighted-kernel proof and connects the stacked differential matrix to the finite Hodge Laplacian. Strict positivity of the weights and the real coefficient field are kept explicit; the same claim fails for indefinite weights and cannot be copied unchanged over finite fields.

### 3. The book already contains a genuine Atiyah connection

The remark after VIII.2.4 on **printed page114, PDF119** explicitly mentions Atiyah–Hirzebruch topological K-theory and the relationship between vector bundles and finitely generated projective modules. This is the strongest direct historical bridge from the supplied volume to index theory. The new exposition builds on this bridge using a precise modern statement of the Serre–Swan theorem.

Two corrections are necessary when translating the historical discussion into present notation:

- For compact Hausdorff `X`, `K_0(C(X,C))` is naturally the topological complex vector-bundle group `K^0(X)`. This correspondence does not identify **algebraic** `K_1` with **topological** `K_1`. Already at a point, algebraic `K_1(C)=C^×`, whereas topological `K_1(C)=0`.
- Recovery of a compact Hausdorff space from continuous functions concerns its character or maximal-ideal space, with the appropriate topology. It should not be stated as an identification with the full prime spectrum of the abstract ring.

These qualifications follow from inspecting the original page and from the definitions, rather than silently repairing OCR.

### 4. The final page contains substantive errata to Volume I

**Printed page387, PDF392**, contains corrections to Volume I. One adds a restriction excluding simple components that are full matrix rings over totally definite quaternion algebras. Another explicitly corrects the proof of IV.13: a decomposition into torsion and torsion-free parts need not be linear over the order. The replacement argument uses local generators and faithful-flatness/Hom comparison rather than the invalid splitting.

Consequently the new manuscript does not use an order-linear torsion splitting without proof. The companion Volume I review has been informed of this erratum. Independent elementary proofs in the new manuscript are not substitutes for checking the hypotheses of the original classification theorems.

### 5. Later primary work confirms the Grothendieck/Bass interface

Roggenkamp's [*Grothendieck Groups of Bass Orders* (1971)](https://doi.org/10.4153/CJM-1971-011-9) directly extends the part of the volume most relevant to the proposed bridge. It distinguishes categories and exact structures and studies finite-generation and classification phenomena under Bass-order hypotheses. The paper was retrieved and its relevant arguments read; it is cited as a primary extension of the monograph, not as a claim that every theorem was formally verified.

[ *On the Irreducible Lattices of Orders* (1969)](https://doi.org/10.4153/CJM-1969-106-x) supplies primary context for integral representation and irreducible lattice questions. Its statements concern specified orders and ambient semisimple algebras, not complexity bounds for lattice cryptography. These are selected relevant works, not an exhaustive bibliography of all research by the author.

## Independent complexes research

### Attribution

Buchsbaum and Eisenbud's [*What Makes a Complex Exact?* (1973)](https://doi.org/10.1016/0021-8693(73)90044-6) is the primary source for the rank-and-grade acyclicity criterion. The paper was obtained as a readable ten-page PDF and read in text. The resulting manuscript states the theorem as an external theorem with local Noetherian and finite-free hypotheses and explains the role of determinantal ideals. It gives complete proofs for accessible special cases and does not invent a short proof of the full acyclicity theorem.

The geometry commonly called the **variety of complexes** should not be attributed to one exactness-criterion paper alone. The dedicated primary treatment is De Concini and Strickland, [*On the Variety of Complexes* (1981)](https://doi.org/10.1016/S0001-8708(81)80004-7). Original-author exposition in De Concini, Eisenbud, and Procesi, [*Hodge Algebras* (1982), §16](https://archive.numdam.org/item/AST_1982__91__1_0/) was consulted for the scheme-theoretic context. Reducedness, normality, and Cohen–Macaulay assertions require the original rank-locus hypotheses and are not proved by a tangent-space count alone.

### Original elementary derivations supplied

For `A:k^a→k^b`, `B:k^b→k^c` with `BA=0`, the manuscript proves:

- The rank condition `r+s≤b`, the cohomology dimensions, and Euler identity.
- Classification of field-valued complexes by the rank pair under independent basis changes.
- Smoothness and dimension of the fixed-rank stratum: `r(a+b−r)+s(b−r+c−s)`.
- The first-order equation `BU+VA=0`, its derivative-image dimension, and tangent dimension `ab+bc−as−cr+rs`.
- The identity between tangent excess over the fixed-rank stratum and `h_1(h_0+h_2)`, with a warning that a stratum dimension alone is not the local dimension of the entire variety.
- The differential graded endomorphism complex, its square-zero identity, the first-order quotient by changes of basis, and the second-order obstruction class.
- A two-generator Koszul exactness argument, and the separate role of flat base change.

For the real dimension vector `(1,2,1)`, the equation is the four-coordinate quadric `x_1 y_1+x_2 y_2=0`. The manuscript derives its singular locus, its smooth exact locus, and the `S^1×S^1` link after an orthogonal change of coordinates. This is a mathematically exact model for an interactive four-dimensional projection; no numerical projection is treated as a proof.

## Elliptic and gauge-complex interface

The original [Atiyah–Singer index paper](https://annals.math.princeton.edu/1968/87-3/p05), the [third index paper](https://annals.math.princeton.edu/1968/87-3/p07), [Atiyah–Bott's elliptic-complex fixed-point paper](https://annals.math.princeton.edu/1967/86-2/p07), [Atiyah–Hitchin–Singer's self-duality paper](https://doi.org/10.1098/rspa.1978.0143), and [Atiyah–Bott's Yang–Mills paper](https://doi.org/10.1098/rsta.1983.0017) provide the primary mathematical lineage. Bibliographic identities and relevant results were checked. The full scanned Atiyah–Singer and Atiyah–Bott papers were retrieved, but their entire proofs were **not** audited or converted into Lean.

The manuscript proves the wedge–contraction identity, exactness of the de Rham symbol complex away from the zero section, finite-dimensional Hodge decomposition, positivity identities, curvature square identity, and the symbol exactness of the four-dimensional anti-self-dual deformation complex. Analytic Hodge theory, elliptic regularity, the index theorem, and the gauge-theoretic index formula are explicitly cited external inputs. Smoothness of a gauge moduli space is conditional on irreducibility and the vanishing of the obstruction space.

The covariant exterior derivative satisfies `d_A²=[F_A,−]`. Thus a general connection does not give a de Rham-type complex on adjoint-valued forms. Flatness is sufficient; some central-curvature situations also act trivially in the adjoint representation. In four dimensions the anti-self-dual equation supplies the different complex `Ω^0(ad P)→Ω^1(ad P)→Ω^2_+(ad P)`. The manuscript makes these hypotheses explicit.

Finally, an index is an integer measuring alternating kernel dimensions; it is not a uniform positive lower bound on the rest of the spectrum. Both a finite-dimensional exact family and circles of increasing length exhibit this distinction. Neither an index formula nor a classical Yang–Mills energy inequality proves the quantum Yang–Mills mass-gap conjecture.

## Deliverables from this review

- `manuscript/chapters/complexes.tex`: three original chapters, approximately 9,500 words, with elementary proofs and explicit external-theorem boundaries.
- `research/volume-two/sources.bib`: twelve primary-source entries with unique `v2...` keys.
- `research/volume-two/ocr-coverage.json`: all-page extraction and selective review metadata.
- This review: provenance, corrections, substantive findings, and limits.

The complete supplied-book review request remains larger than the verified proof coverage here. The project should report this limitation rather than relabeling extraction as mathematical verification. The selected Lean files, when built, certify only the declarations actually accepted by the Lean kernel under the pinned toolchain and standard imported foundations.
