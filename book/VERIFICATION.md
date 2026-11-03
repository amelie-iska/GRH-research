# Verification and inclusion ledger

The book is a developed critical edition of the two supplied manuscripts, not a certification of every original assertion. Both complete originals are preserved byte-identically in `book/source-editions` and on the local page. Their hashes, all chapter headings and original line positions are recorded in `source-provenance.json`. The coverage review documents what was read in this run versus earlier audits. Historical false claims are retained as sources, with corrections in the critical text; they cannot consistently be formalized as valid theorems.

## Current kernel-checked layer

The working critical book has 27 chapters, with four unique canonical on-page interactive tools, full-source code views and complete historical source volumes. Larger examples include genus4/5/9/16, finite depth-capped hyperbolic lattice windows and a nine-qubit QCNN.

The pinned Lean 4.24/mathlib suite has **240 printed theorem dependency reports** after the new short-row and book modules. The full suite passed with warnings treated as errors: 238 reports use standard foundational axioms only and 2 are axiom-free. There are no admissions or custom project axioms. This is a report count, not a count of all book theorems. The historical standalone seven-result suite is unchanged and was not rerun for this milestone.

| Material | Actual formal/computational interface | Remaining boundary |
|---|---|---|
| Nodal/projective resolutions | Existing PowerSeries/module resolution layer; exact path and matrix diagnostics | General dessin category interfaces and all module classifications not fully formalized |
| Semi-invariants/AR | BookInterfaces Plücker and actual nodal matrices; nine-module/twelve-map/four-mesh exact checker | Almost-split universal factorization, whole component classification, Ringel quilt and derived equivalences remain prose/primary theorems |
| Clock/shift and channels | BookInterfaces explicit clock/shift, distinct-site matrices, arbitrary finite complex Kraus positivity and trace preservation | Infinite operator domains, C* completions, physical implementations and QFT reconstruction not fully formalized |
| Arithmetic character/Gram | ShortRowGram actual finite-field masks, complete orthogonality, finite energy expansion, Eisenstein norm and mod7 evaluation | Planar Poisson, full CRT/ideal-character interface and low-gcd short-row estimate remain separate |
| Theta arithmetic/descent | Existing Jacobi/projective/tame power-series and matrix layers | Full order functor, arithmetic descent and global positive determinant comparison remain open |
| Higher genus/hyperbolic geometry | HyperbolicCoordinates formal disk/Lorentz and 4D norm identities; uniform prose passport proof; exact permutation/ramification checks through genus16; bounded reflection diagnostics | No formalized general uniformization or certified compact hyperbolic quotient; displayed patch is numerical and finite |
| Learned renormalization | Actual PennyLane three-architecture and larger nine-qubit training; NumPy comparison, analytic target/gradient checks; actual Strawberry Fields training | No optimizer convergence theorem, hardware run, general QFT RG theorem or quantum advantage claim |
| ToricGT hybrid | Actual pinned upstream Weyl module, trained PennyLane surrogate, six exact rational 15-minor PSD certificates | No upstream language-model campaign reproduced; no inferred arithmetic L-function operator |
| Persistence extension | Complete prose resolution/CW/Schur/flag-incidence and actual surface-order coefficient construction; independent review | These new full module/category arguments are not yet Lean formalized |
| Numerical architecture traces | 22 cases and 836 shape-labelled DAG nodes; unchanged trained checkpoint replay, fixed-weight classical references, independent gate/covariance/scalar-loop checks | Step-through 3D inspector is a separate queued task; numerical arrays are not kernel-checked theorems or new training |
| Sage | Exact scripts supplied | Installed launcher points to missing app; Sage execution not passed |
| NVIDIA | Two requested upstream-only public forks and pinned local clones; optional adapters | No supported NVIDIA GPU runtime on this Apple machine; GPU execution not passed |

The web book places selected Lean and executable code beside chapter content. These panels label scope rather than imply complete chapter formalization. The original manuscripts also contain experimental and proposed engineering statements: they need measurements or model validation, not a Lean proof that unperformed experiments happened.

## Book-wide formalization backlog

1. Connect the existing actual path/order definitions to each general dessin resolution and prove its exactness uniformly.
2. Formalize the exact-category AR factorization properties and separate quotient, lattice, stable and derived interfaces.
3. Develop determinant-functor maps with their perfection, linearity and symmetry hypotheses.
4. Formalize the analytic lattice Poisson and low-gcd kernel estimates; the latter is still an unresolved mathematical problem.
5. Formalize operator domains, regularized determinant convergence and the precise spectral zero-location bridge once independently constructed.
6. Formalize physical finite-channel statements further, and treat continuum, hardware, measurement and learning claims according to their actual evidential type.

A complete GRH proof and complete Lean formalization of all material have **not** been established. No fitted spectrum, trained network, finite numerical check or restatement of an open bridge is accepted as completion.
