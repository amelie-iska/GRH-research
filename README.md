# Orders, Complexes, Cryptography and Quantum Yang–Mills

A research monograph and executable companion prepared for Amelie Schreiber,
built on the frozen **amelie-iska/GRH-research** repository at
**dbd954eede479a5129831e4e7c30537389ae973d**.

The new work is in **extension/**. The inherited repository remains available;
its original introduction is preserved as **README-UPSTREAM.md**. This project
does not assert a proof of GRH or of the Yang–Mills mass gap.

## Current implementation and review

The [iterative implementation plan](extension/IMPLEMENTATION_PLAN.md) defines
bounded chunks, validation gates, and a durable checkpoint. The final review
adds exact reduction and transport contracts, a nonnormal Jacobian counterexample,
and tested standard cryptographic artifact interfaces. Independent [formal](extension/review/final-pass/independent-formal-audit-20261113.md),
[source](extension/review/final-pass/independent-source-audit-20261113.md), and
[implementation](extension/review/final-pass/independent-implementation-audit-20261113.md)
audits state their actual coverage and remaining obligations.

## Read and run

- **Hosted research atlas:** [Orders, Complexes and Quantum Fields](https://orders-complexes-quantum-fields.wolvieworld.chatgpt.site/) (existing account access is required). All static page sources are also included below.
- **Manuscript:** [compiled PDF](extension/manuscript/main.pdf), [LaTeX source](extension/manuscript/main.tex), [build instructions](extension/manuscript/BUILD.md).
- **Fluid supplement:** [compiled PDF](extension/manuscript/fluid-extension.pdf), [LaTeX entry point](extension/manuscript/fluid-extension.tex), and [interactive fluid laboratory](extension/site/fluids.html).
- **Interactive research atlas:** [site source](extension/site/index.html), with six mathematical laboratories, a live 18-qubit circuit/QNN companion, an algebra companion, live quantum ToricGT, diagram/language, synthetic-cosmology and fluid pages, original research pages, downloads, and verification records.
- **Formal proofs:** [Lean package](extension/lean/README.md), comprising 115 selected declarations freshly checked across six modules with Lean 4.24.0 and a pinned mathlib revision.
- **Actual GPU experiments:** [quantum methods and results](extension/quantum/README.md), with immutable-input hashes and measured execution records.
- **Review coverage:** [review ledger](extension/review/README.md), source inventories, book-page coverage, primary-source audits, and explicitly unreviewed material.

Serve the static companion from the repository root:

    python3 -m http.server 8000 --directory extension/site

Then open http://localhost:8000/. An HTTP server is required for the worker and
JSON data; opening the HTML directly from a file URL is insufficient. This is
a local development address, not the published project-page URL.

The quantum page executes a real classical state-vector simulation in a browser
worker: 18 qubits, an actual 42-gate encoder, Pauli errors, arbitrary supported
single-qubit gates, and a trainable four-angle surface-local circuit. Its 30-,
32-, 46-, and 2,048-qubit topology views do not allocate those dense states in the
browser. Larger runs are displayed as separately recorded GPU evidence.

## Mathematical content

The manuscript develops orders and lattices; complex multiplication and elliptic
curves; varieties of complexes and exactness; exterior powers, wedge shuffles,
Young tableaux, Schur modules, standard monomials, associated graded algebras
and semigroup rings; gentle-quiver module decompositions and semi-invariants;
Schofield determinants, exterior traces and finite zeta functions; elliptic
complexes and index theory; Shor/Regev-type algorithms and their actual scope;
module-lattice cryptography; quantum surface codes and dessins; gauge theory;
the dated 2026 OpenAI Yang–Mills assessment; typed tensor diagrams and graph
grammars; conformal cyclic cosmology and identifiability; and neural
computation, language and counterfactual mechanisms.
The fluid extension connects these structures to microscopic mechanics,
kinetic limits, exact memory, finite Hodge theory, quantum channels,
Carleman lifting, and the September 2026 forced Navier–Stokes result.

Complete elementary proofs are supplied for the selected interfaces and examples.
Deep external theorems are cited with their hypotheses. The monograph's proofs,
numerical experiments, inherited claims and compiled Lean statements have
different evidence status; the reports keep those statuses explicit.

Specific corrections include the cubic-generator issue in the second uploaded
volume and the band-generator typo in the arXiv-v1 Carroll–Weyman matching
example. Both corrections are supported by explicit independent arguments.

## Reproduce the finite checks

From the repository root, using Python 3, NumPy for state-vector validation, and Node.js:

    python3 extension/code/verify_examples.py
    python3 extension/code/verify_invariants.py
    python3 extension/quantum/surface_codes.py
    node extension/site/verify-math.cjs
    node extension/site/verify-quantum.cjs
    node extension/site/verify-quantum-worker.cjs
    node extension/site/verify-algebra.cjs

Consult the quantum README for the exact NVIDIA environment and commands.
The dense GPU experiments reached 31 total qubits with complex64 storage.
The separately represented Pauli-frame followup completed 819,200 data qubits
plus 819,200 ancillas at 32,768 shots under its stated memory policy. This is
not a million-qubit dense state-vector or non-Clifford neural simulation.

The QNN training experiment reduces mean squared error on a small synthetic
correlator task. Its prediction signs were already correct at initialization;
no classification-accuracy improvement or quantum advantage is claimed.

## Second-pass quantum learning and cosmology

The [quantum ToricGT implementation](extension/quantum/toricgt/README.md) trains
three-qubit Weyl features jointly with a 25,515-parameter graph model. Nine actual
RTX 4090 runs compare three seeds of a trainable quantum model, matched classical
features and a frozen quantum encoder. The complete dataset, all checkpoints,
8,064 per-example records, timing data, independent gradient checks and exact
path certificates are included. The [browser model](extension/site/learning.html)
executes the full exported network; changes to its circuit parameters propagate
to predictions and attention. Results establish trainability, not quantum advantage.

The [cosmology review](extension/review/cosmology/README.md) distinguishes CCC
proposals and conditional conformal/spinor results from empirical claims. Eight
central papers were fully text-read, with other works explicitly reviewed only
in selected sections. Its executable example uses **synthetic** skies: 96 sampled
directions, 288 templates and 4,095 full-search null calibrations. No observed CMB
or decoded message is presented. The language chapter gives exact constructive
neural mechanisms and a direct critique of categorical impossibility claims,
with primary linguistic findings and their published objections both examined.

Additional finite checks:

    node extension/site/verify-grammar.cjs
    node extension/site/verify-cosmology.cjs
    python3 extension/quantum/toricgt/algebra_checks.py

## Publication

[Publication instructions](extension/PUBLISHING.md) preserve the original upstream,
require the intended GitHub account, and verify the pushed commit. The supplied
script publishes to the existing **amelie-iska/GRH-research** repository, as
requested by the author, using a fast-forward update. It creates no new repository
and makes no visibility change.

## Fluid dynamics, exact reduction and the 2026 Navier–Stokes release

The new [review directory](extension/review/navier-stokes/) records complete
coverage of the 166-page released paper, all 249 exposed video-transcript
segments, specified microscopic sources and lecture decks, and 129 pages of
three quantum-fluid papers. The source ledger identifies six requested
originals whose full text could not be obtained and marks selected-section
reviews separately.

The released continuum result concerns **smooth externally forced breakdown
from rest**, including positive viscosity, bounded kinetic energy, and the
whole-space and periodic settings. It addresses the forced alternatives of
the Clay statement; it is not an unforced positive-viscosity theorem. The
project explains its analytic construction and supplies additional proofs
for the finite algebraic interfaces. It does not claim a stronger solution
of an unsettled problem.

New arguments include the real quadratic order behind the toral cover,
small-divisor and moment corrections, exact hidden-state memory, energy-stable
finite closures, completely positive heat channels, contractive Carleman
estimates, and corrected unitary collision encodings. A nonnormal matrix
counterexample identifies a missing hypothesis in a cited preliminary energy
bound. Exact XOR and normalized dilation constructions repair two displayed
block encodings while retaining their success probabilities.

The fluid browser evaluates an exact Taylor–Green solution, complete toral
fibres, a two-qubit parameterized circuit coupled to a separate finite heat
channel, and concentration exponents. Its circuit is untrained and simulated
classically; its scaling panel is not a simulation of the singular solution.
The previously trained GPU quantum ToricGT remains a distinct tokenization
experiment. A fluid adaptation is specified with structural energy constraints
and a validation design, without a claimed training result or speedup.

Additional reproducible checks:

    python3 extension/code/verify_fluid_interfaces.py
    node extension/site/verify-fluids.cjs

All 115 local Lean declarations were freshly checked, with exact types and
axiom reports. The separate pinned upstream Navier–Stokes source audit covers
the 609-module solution import closure. Its fresh full kernel build did not
complete because dependency cache downloads were rate-limited; that source
audit is not represented as a completed continuum proof verification.

## Sources, scope and rights

The OCR text of all 701 pages of the uploaded two-volume *Lattices over Orders*
was read across the review team, with selected formulas checked against page
images. This is distinct from an independent proof audit of every line.
The repository and outbound-link inventories do not mean all linked works or
all files of the large linked math repository were fully reviewed.

The source scans, full OCR texts and downloaded third-party research PDFs are
not redistributed here. Their bibliographic references, review notes and
hashes are retained. Existing upstream authorship and notices are preserved.
No new open-source license is imposed on inherited material.

The revised manuscript has **pending final-build count pages**, with a separate **pending final-build count fluid
supplement**. Its [claim register](extension/review/claim-register.md) contains
**264 named environments**: 252 local arguments, five specially marked
conditional arguments, six cited external results, and one open problem.
The **257 attached proofs** are written arguments. Nine additional external
statements in prose have explicit source and proof-scope classifications.

The [independent second audit](extension/review/second-pass-math-audit.md)
covered all 125 original statements and all 55 additions in the earlier
180-environment version. That historical coverage is preserved. The subsequent
[fluid review records](extension/review/navier-stokes/) document the additional
source reading, theorem checks, corrections, and their own reviewed snapshots;
the earlier audit is not presented as an audit of all 264 current environments.

The six Lean modules contain **115 kernel-checked declarations**, all freshly
rechecked with zero warnings. The [formal type map](extension/review/formal-type-map.md)
records every declaration and maps **68** to precise partial components of
**25** manuscript environments; no whole composite manuscript theorem is
labelled fully formalized. The [fresh verification record](extension/lean/final-verification/verification.json)
preserves the exact tools, source hashes, axiom inventories, and kernel logs.
It covers the local companion and leaves the separately documented upstream
continuum verification attempt incomplete.

The original Git submodule references remain pinned in the inherited tree.
A source archive does not recursively vendor their entire contents; use the
recorded repository URLs and commits when obtaining those separate projects.
