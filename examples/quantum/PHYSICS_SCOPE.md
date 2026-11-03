# Physics chapter scope and verification

Goal: retain all source physics topics with correct mathematical hypotheses, measured evidence and explicit proposed-design status. Original source TeX and protected clones remain immutable.

Authorized targets only: `book/chapters/physics.tex`, `book/chapters/physics-references.tex`, this file. Labels use `phys:`; bibliography keys use `Phys`. Bibliography contains bibitems only for insertion into the parent book's bibliography.

Implementation plan: (1) operators, positive transfers, clocks and derived holonomy; (2) entanglement and trained graph-channel renormalization, memory and persistence; (3) noise, measurements, molecular motifs, design tools, hyperbolic geometry and CSS. Then compile a standalone wrapper in /tmp with existing TeX packages. Parent owns full-book integration and executable QNN training.

Preservation map: total positivity/wiring/positive Grassmannian and QFT; finite/infinite clocks, rotation algebras, root towers and odometers; DG/A-infinity and persistence; gluing, MI geometry, modular time and Einstein-limit hypotheses; trained/random quanvolution, QGCN/QGAT, geodesic CNN, cyclic equivariance and pooling; Hopfield/HRR, Fourier memory and tensor-network holography; routing, 10k/100k scaling and shadows; peptide/1TJB, spin gates/readout, RFdiffusion3/Proteina/BoltzDesign1 and ThermoGFN-IF/SPURS/BioEmu/UMA; kagome assembly and hyperbolic CSS; conditional spectral arithmetic and the unresolved GRH interface.

Evidence rules: training claims require saved seeds, dataset splits, optimizer/ansatz/loss, checkpoint, predictions, noise/shot specification and baselines. An analytic optimum or proposed workflow is not a completed training experiment. Structural confidence is not coherence; measured EPR is not gate fidelity. Distance/threshold claims need explicit code/decoder/noise certificates. No model, quantum hardware or molecular simulation was run for these chapters.

Audit: `/tmp/grh-book-physics-review.md`. Standalone TeX validation pending.
