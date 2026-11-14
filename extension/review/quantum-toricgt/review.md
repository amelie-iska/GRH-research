# Quantum ToricGT: source, proof, and experiment review

Review date: 13 November 2026. This record concerns the new bounded quantum graph-learning extension. It supplements the earlier monograph reviews; it does not turn a selected ToricGT review into a review of every linked paper or every implementation in the author's program.

## Pinned primary repositories

| Repository | Reviewed commit | Scope |
|---|---|---|
| [amelie-iska/ToricGT](https://github.com/amelie-iska/ToricGT/tree/a5199bc989a6fb170e21220e5e87bf95bc2fc0b4) | `a5199bc989a6fb170e21220e5e87bf95bc2fc0b4` | Four full implementation modules, full current-state document, selected README material |
| [amelie-iska/ToricGT-Program](https://github.com/amelie-iska/ToricGT-Program/tree/f91ba1811b5a4f70d53c7120acf8ca2a0049f85b) | `f91ba1811b5a4f70d53c7120acf8ca2a0049f85b` | Full program README; selected complete sections of Paper V's primary TeX |

The four ToricGT modules read completely were `src/toricgt/graph_tokenizer.py` (145-line local text copy), `tropical_attention.py` (353), `toric_algebra.py` (140), and `soft_moe.py` (219). `docs/CURRENT_OAI_TORICGT_STATE.md` was also read completely (240-line local copy). The large 2,509-line README was inspected selectively; no full-read claim is made for it. The Program README was read in full (258-line local copy).

Paper V is `ToricGT-V/assets/toricgt_toric_algebra_training_paper.tex`, Git blob `be50f5cbbf5a0481f89ffd43bcf255560a0d6155`. The reviewed local copy has 1,103 lines. Content read in this continuation comprises the title/front matter (1–57), all of the trajectory and tropical-interface sections (158–284), all worked examples and additional guarantees (582–654), and all expanded-theory material (719–857). These correspond to Sections 3, 4, 8, 9, and 11, plus front matter. The catalog, implementation plan, and remaining sections are **not** claimed as read in full. The local extracted copies have a terminal newline added during storage; Git blob IDs identify the original source, while the JSON ledger labels SHA-256 values as local-text-copy hashes.

The Program tree also contains a ToricGT gitlink at `17960fc87f0aba147e7a886a3ebc95da92bd5263`; this is distinct from the separately reviewed ToricGT branch pin. The new implementation does not import that gitlink or silently conflate the two revisions.

## Other primary sources actually used

- [TokenGT, arXiv:2207.02505v2](https://arxiv.org/abs/2207.02505v2): node/edge-token construction and relevant equivariance/expressivity hypotheses. Selected construction/theory passages were read; the 26-page paper is not represented as fully audited. The general expressivity theorem is not transferred to our finite-width circuit model.
- [ConvexTok, arXiv:2605.22821v1](https://arxiv.org/html/2605.22821v1): introduction, token-DAG construction, generalized graph definition, and Section 3.2 colored-flow integer-program formulation. Its full experimental campaign and all rounding analyses were not reproduced. The companion implements a new small colored-flow example and a fixed-vocabulary weighted decoding dataset.
- [Schuld et al., analytic gradients](https://arxiv.org/html/1811.11184v1): Sections II and III.1, especially the single-occurrence hypothesis, two-eigenvalue normalization, and occurrence-wise sum for shared parameters. The manuscript gives its own elementary Pauli-case derivation and a nonlinear-loss counterexample. The retrieved experimental HTML does not constitute full coverage of every continuous-variable result.
- [Puigcerver et al., Soft MoE](https://proceedings.iclr.cc/paper_files/paper/2024/file/79fea214543ba263952ac3f4e5452b14-Paper-Conference.pdf): algorithm description in Section 2.1, printed page 2, including dispatch over tokens and combination over slots. Upstream large-scale performance results are not claimed as reproduced.
- [Author's ToricBLM proposal](https://huggingface.co/blog/AmelieSchreiber/toricblm): introduction/architecture, affine-steering definitions, selected closing/training discussion, and further-reading links. A separate independently pinned ToricBLM code repository was not located in the reviewed material. This is an explicitly bounded search finding, not proof that no such repository exists.

The inherited `examples/quantum_tokengt/README.md`, `model.py`, `sources.json`, and `research/toricgt-hybrid-design.md` were read in full for design comparison. The old example used frozen quantum features for a small exact-spin teacher. Its model and metrics remain distinct from the new trainable encoder and token-DAG task.

## What the new implementation retains and changes

The four reviewed ToricGT modules provide concrete antecedents for vertex/edge tokens, endpoint structure, max-plus attention, finite clock/shift matrices, and Soft-MoE. The new code implements those selected ingredients directly and introduces a jointly trained circuit encoder. It does not execute an upstream BPB training campaign or claim that every research-program auxiliary is present.

The reviewed standalone tokenizer includes learned identifier embeddings; arbitrary relabeling invariance of that table is not automatic. The new implementation uses endpoint equality (orthonormal Gram comparisons) and transports intrinsic byte positions with the attributed graph. Its equivariance proof has exactly that scope. It is a fully observed graph task, not a prefix-causal language model; no bits-per-byte result is fabricated from graph-regression loss.

Each token uses three qubits, six encoded input angles, two circuit layers, and twelve learned offsets. Quantum and classical variants each have 25,515 trainable parameters. The frozen-feature ablation freezes all 66 encoder parameters, leaving 25,449 trainable. The separate larger surface circuits elsewhere in the project were not trained by this experiment.

## Concrete source qualifications

### QT-S01 — Ambient-lattice saturation example

**Source:** pinned Paper V, lines 601–603, subsection “A saturation hole.”

The example uses `Q=N{(2,0),(0,2),(1,1)}` and calls `(1,0)` a saturation hole because twice that point belongs to Q. The generated lattice consists of pairs whose coordinate sum is even. Every nonnegative point of this lattice lies in Q: even/even pairs are sums of the first two generators, and odd/odd pairs are one `(1,1)` plus those generators. Thus Q is saturated in its own generated lattice. `(1,0)` is outside that lattice. A larger ambient-lattice saturation is a different specification.

**Disposition:** the new chapter proves the lattice and saturation assertions completely. `algebra_checks.py` checks the explicit decomposition on 545 nonnegative same-parity pairs. The finite check illustrates the general proof; it is not its replacement. No upstream source file was altered.

### QT-S02 — Predictive transfer sign and artifact accounting

**Source:** pinned Paper V, lines 746–753, especially line 750. Compare its earlier codelength discussion at 196–218.

Positive reduction in negative log likelihood is the sum of `log2(q_new/q_old)`. The later displayed definition uses the inverse ratio while calling positivity a gain. For a symbol whose probability rises from 1/4 to 1/2, codelength improves by one bit; the inverted expression is minus one bit. An additional deployed artifact cost B should be subtracted from the total gain. Ordinary predictive bits per byte and artifact-adjusted codelength should be named separately.

**Disposition:** the new chapter uses one explicit convention, derives the difference, and records the rational example. The graph-learning experiment makes no BPB claim.

### QT-S03 — Inclusion is insufficient for a monotone homology penalty

**Source:** pinned Paper V, lines 834–856, especially the theorem and proof at 848–854.

The support-inclusion argument can establish that a chosen coverage construction grows. Inclusion of complexes does not imply either monotonic direction for Betti dimensions. A point included in the boundary triangle included in the filled triangle has first Betti numbers 0, 1, and 0. The new chapter gives the explicit 3-by-3 edge boundary and 3-by-1 face boundary, with ranks 2 and 1 and zero composition.

**Disposition:** exact rational rank checks accompany the full proof. The correction concerns an unsupported monotonicity interpretation; it does not deny the displayed set-inclusion implication under its stated fixed-poset assumptions. Scientific truth or completeness of real-world evidence does not follow from persistent topology of a chosen internal representation.

### Other hypotheses retained

The finite binomial-kernel factorization is a quotient-ring statement, not a proof that all ordered trajectories with equal counts are interchangeable. Nonnegative flow and DAG hypotheses are required to turn a boundary-preserving rewrite into a legal path. A finite list of stable binomial leading sides need not determine an entire initial ideal unless an appropriate complete Gröbner-basis condition is supplied. Affine sign margins apply in the chosen affine feature space; their pullbacks through a quantum circuit need not be polyhedra. General normalized-dot-product attention is not globally affine in its inputs. A chain-complex residual alone does not prove exactness, minimality, or correctness of an external scientific assertion.

## Proof audit of the new chapter

`extension/manuscript/chapters/quantum-toricgt.tex` contains approximately 6,973 whitespace words and 17 explicit proofs. An independent team reviewer read the complete chapter and every proof. Corrections made before freeze were:

1. Require distinct source and sink in the integral-unit-flow lemma.
2. Define the maximum of the empty set in max-plus contraction.
3. State epsilon/zero-vector conventions for normalized feature operations.
4. Describe the finite Weyl representation as having a rational phase parameter, rather than suggesting rational matrix entries.
5. Use `D=-B` for toric endpoint grading, preserving the original source-minus-target flow convention in rewrite proofs.

The review found no remaining mathematical proof failure. This is a human-readable mathematical audit of the finite claims, not a formal verification of the program or of every theorem in the upstream papers. The 17 proofs are not labelled Lean-formalized. The project's exact declaration/type mapping remains authoritative for formal proof coverage.

## Actual experiment and verification boundary

The fixed dataset contains 896 distinct strings in 512/128/128/128 training/validation/test/length-shift graphs. All nine 80-epoch runs were completed on the authorized RTX 4090 using the existing PyTorch 2.8.0+cu128 environment. Training used analytic statevector expectations; no quantum hardware, finite-shot noise, or cuStateVec training is represented. The run manifests retain five training-source hashes and the dataset hash, and all checkpoint and run-record hashes were checked after transfer.

The data show mixed outcomes: classical features slightly outperform trainable quantum features in ordinary-test proposal accuracy/regret, whereas the quantum model has somewhat better mean longer-string path performance. Frozen quantum features slightly outperform trainable ones on longer-string node RMSE. No superiority or quantum-advantage claim follows from three seeds on one synthetic task. The exact dynamic program is already an efficient zero-regret solver.

Independent verification uses dense NumPy versus indexed PyTorch circuits, analytic shift versus automatic-differentiation Jacobians, the full nonlinear-loss chain rule, 48 exhaustive path enumerations, rational LP-dual feasibility, graph permutation/padding, and router normalization. The full JavaScript graph model is independently compared against saved GPU predictions on two test and two longer-string graphs; maximum normalized node error is 6.81e-7, with matching paths and final certificates. A theta perturbation changes the full output, so the browser is live inference rather than a replayed score.

All final certificates become valid after the explicitly separate exact repair. Reported neural proposal accuracy and initial-certificate frequency remain separate. The checker and repair establish exact finite combinatorial claims, not generalization or physical theory. The chapter's final commuting-projector theorem is explicitly a proposed conditional quantum interface, not an undocumented property of the trained three-qubit feature encoder.

## Records

- [Implementation README](../../quantum/toricgt/README.md)
- [Full nine-run benchmark](../../quantum/toricgt/results/training-v1/benchmark.json)
- [Final CUDA verification](../../quantum/toricgt/results/cuda-verification-final.json)
- [Browser forward verification](../../quantum/toricgt/results/browser-fullforward-verification.json)
- [Exact source-qualification checks](../../quantum/toricgt/results/algebra-checks.json)
- [Bibliography fragment](sources.bib)

The external source texts were retrieved for review and are not bulk-republished as new original writing. Source URLs, pins, coverage, and localized counterarguments allow the review to be followed independently.
