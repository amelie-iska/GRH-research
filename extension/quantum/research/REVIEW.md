# Primary-source and mathematical review: surface codes, dessins, QNN

Retrieval and review date: **2026-11-13**.

## Scope and source coverage

The mathematical statements proved in the new chapter are self-contained
derivations for the implemented cellulations and circuits. They are not presented
as new discoveries of homological coding or quantum convolutional networks.

| Source | Primary material inspected | Use and boundary |
|---|---|---|
| Kitaev, arXiv:quant-ph/9707021v1, submitted 9 July 1997; Annals of Physics 303 (2003), 2–30 | Original preprint, especially Section 1 and its toric-code/stabilizer/loop/Hamiltonian derivations | Historical and mathematical basis. We independently prove the finite code statements used. No claim of a new nonabelian anyon simulator. |
| Calderbank–Shor, Physical Review A 54 (1996), 1098–1105 | Author-hosted published PDF, definitions and codeword construction in Sections II–III | CSS antecedent and linear-code state construction. No imported asymptotic rate claim for the project’s examples. |
| Steane, Proc. Royal Society A 452 (1996), 2551–2577 | Primary arXiv record and author-hosted article excerpt | Historical CSS attribution; no additional technical claim depends on unaudited later sections. |
| Dennis–Kitaev–Landahl–Preskill, arXiv:quant-ph/0110143v1; J. Math. Phys. 43 (2002), 4452–4505 | Primary preprint, abstract and introduction/recovery-assumption discussion | Distinguishes syndrome simulation from decoded fault-tolerant memory. No threshold number is asserted. |
| Cong–Choi–Lukin, arXiv:1810.03787v2 (2 May 2019); Nature Physics 15, 1273–1278, published 26 August 2019 | Primary preprint QCNN architecture, phase-recognition setup and measurement/pooling description | Establishes what a QCNN architecture actually contains. The four-parameter project circuit is explicitly different and analytically soluble. |
| Schuld et al., arXiv:1811.11184v1; Physical Review A 99, 032331 (21 March 2019) | Primary preprint Section III, Theorem 1 and equations (13)–(14) | Two-eigenvalue generator condition and single-gate parameter occurrence. Our special-case derivative is proved directly. |
| Belyi, Math. USSR-Izvestiya 14 (1980), 247–256 | Math-Net primary bibliographic record and indexed abstract | Cited external existence theorem. Direct PDF retrieval returned HTTP 403; no full-paper review or fresh proof audit is claimed. |
| Leslie, arXiv:1310.5376, thesis (2013) | Primary arXiv abstract | Prior hypermap-code work. No parameter comparison is imported into the manuscript. |
| Sarvepalli, Physical Review A 89, 052316 (13 May 2014), arXiv:1312.6344 | Primary journal and arXiv abstracts | Existing constructive relation of canonical/noncanonical hypermap codes to surface codes. No claim that a dessin automatically improves protection. |

Downloaded primary texts were used as research intermediates outside the
publication tree. `source-manifest.json` records their URLs, byte lengths and
SHA-256 values. The repository includes citations and original derivations,
rather than redistributing those downloaded PDFs.

## Key derivations checked independently

1. **Permutation convention:** `phi = sigma0 sigma1`; the white involution
   consists of `n` transpositions on `2*n` darts. Therefore clean-dessin degree
   is twice the number of qubits. Face cycles and vertex links are checked.
2. **CSS conventions:** `HX=boundary_1`, `HZ=boundary_2.T`. Both are binary;
   signs are retained in the underlying oriented boundaries. Their product
   vanishes because the boundary of a polygon has zero boundary.
3. **Higher genus:** explicitly reverse the disk-boundary gluing. Genus two
   has `(V,E,F)=(14,32,16)` and genus three `(19,46,23)`. Every vertex link is
   one cycle. No extra identification by coincident endpoint pairs is made.
4. **Ranks:** exact integer-bitset RREF agrees with `(V-1,F-1)` in all stored
   cases, including the 2048-qubit torus. Thus `k=2g`.
5. **Distance:** exhaustive masks of weights 1–3 certify distance three for
   the 18,30,32,46-qubit cases. Missing witnesses are never reported as a
   proved distance. The 32×32 torus distance is a theorem-based value.
6. **Encoder:** pivot Hadamards and only pivot-to-nonpivot CNOTs give the
   uniform row-space state without phases. Preparation is not asserted to
   preserve nearest-neighbor locality.
7. **QNN:** `RY† Z RY = cos(phi) Z - sin(phi) X`. Every mixed term with a
   nonempty Z subset on the chosen star has nonzero vertex syndrome. Only
   the four-X stabilizer remains. This proves the stated parity-times-cosine
   expectation, including its sign.
8. **Loss:** using mean squared error without a factor of one half, the loss
   is `(product(cos(theta))-1)^2`. Parameter shifts differentiate expectation
   values; the loss derivative then uses the ordinary chain rule.
9. **Hamiltonian:** the projector-normalized code Hamiltonian has gap two,
   since global check relations force paired defects and a single-edge Pauli
   attains two. This is a finite Z2 gauge-code result, not a Yang–Mills mass gap.

## Recorded CPU execution

`cases/cpu-validation.json` records an actual NumPy complex128 state-vector
execution on all 18 qubits. It verifies the prepared amplitudes, all 18 local
checks, and all 16 variational inputs. The maximum state discrepancy is below
`4.2e-17`, and the QNN expectation identity error is below `1.1e-15`.
These numerical tolerances are distinct from the exact algebraic proofs.

## Uncomputed analytic data and scope limits

The torus family has an explicit Belyi interpretation through unramified covers
of `y²=x³−x, beta=x²`. Higher-genus permutation triples give combinatorial Belyi
pairs, but their algebraic coefficients and uniformizing maps were not computed.
The independent hyperelliptic example in the chapter is not identified with the
connected-sum data. Its unrefined code is degenerate, and is explicitly excluded
as evidence of a useful higher-genus error-correcting code.

The QNN task is an exactly soluble 16-input truth table. Four training inputs and
twelve held-out inputs provide execution checks, not a statistical generalization
study. There is no demonstrated speedup over its analytic classical formula, no
learned decoder, and no hardware quantum execution. Large GPU workloads must be
identified as state-vector, stabilizer, or Pauli-frame workloads in their reports.
