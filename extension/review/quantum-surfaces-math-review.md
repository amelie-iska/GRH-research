# Independent mathematical review: quantum surfaces

## Coverage and boundary

Read all 673 lines / 4,349 whitespace-delimited source words of extension/manuscript/chapters/quantum-surfaces.tex. This is an independent mathematical consistency review, performed after completing the standard-monomial chapters. No source edits were required.

The review checks the stated definitions, finite mathematical arguments, and interfaces. It does not independently rerun the gate-count, CPU error, GPU timing, memory, or large-cellulation certificate artifacts. Those numerical claims rely on their separately recorded execution evidence. External Riemann existence, Belyi, and surface-classification results remain cited external theorems.

## Checked conclusions

1. **Dessin conventions.** With right-to-left composition, sigma0 = phi sigma1 and sigma-infinity = phi inverse give product one. Reversal switches the dart basepoint, and then the face successor restores it, so sigma0 indeed rotates darts at one vertex. The cycle-count Euler formula is consistent with subdivision into a clean dessin.

2. **Elliptic Belyi map.** Over the complex numbers, E: y² = x³ − x is smooth after projective completion. The map beta = x² has degree four. Local orders at (0,0), (±1,0), and infinity give the passport (4), (2,2), (4). The ramification sum is 3+1+1+3 = 8, yielding 2g−2 = −8+8 = 0. The black vertex, two collapsed edges, and single disk face give a torus cut graph.

3. **The grid cover.** A connected unramified cover corresponding to Lx Z direct-sum Ly Z inside the torus fundamental group pulls the cut graph back to the rectangular periodic square cellulation. Pulling back the complex structure makes the cover holomorphic, and composition with beta has degree 4LxLy. The chapter correctly uses a topological cellulation argument and does not identify a rendering's Euclidean metric with the Belyi pair's uniformizing metric.

4. **Higher-genus Belyi example.** For Cg: y² = 1+x^(2g+1) and beta_g = −x^(2g+1), the degree is 4g+2. The two points over x=0 each have index 2g+1; the 2g+1 points with y=0 each have index two; infinity has index 4g+2. The ramification sum is 10g+2, and Riemann–Hurwitz gives −2(4g+2)+(10g+2)=2g−2. Collapsing the clean subdivision yields two vertices, 2g+1 parallel edges, and one face. Over F2, HX has rank one and HZ is zero, so the code parameters are [[2g+1,2g,1]]. This verifies the stated warning that genus alone does not provide useful distance.

5. **CSS code space.** The boundary-composition identity gives binary row orthogonality. The separate X and Z masks establish independent joint stabilizer rank, and the absence of minus identity makes the averaged group projector legitimate. Its trace gives code dimension 2^(E−rankHX−rankHZ). Connectedness of primal and dual graphs gives the two rank formulas, including cellulations where an edge borders the same face twice.

6. **Distance and encoding.** The winding argument for the rectangular grid applies separately to primal and dual cycles. The support-union argument rules out a smaller mixed-Pauli distance. The row-echelon encoder preserves pivot controls and computes exactly the uniform row-space superposition, with positive amplitudes. Its extra logical-Z constraints are consistent with the selected encoded sector.

7. **Finite Hamiltonian.** Products of all star checks and all face checks give the even-defect lower bound. A single Z on an edge with distinct endpoints attains energy two. This proves the gap for the explicitly normalized finite commuting-projector Hamiltonian and supplies no continuum Yang–Mills implication.

8. **Variational correlator.** The patch (0,2,9,15) is the full star at the origin of the 3-by-3 torus; its four neighboring vertices are distinct. Every nonempty Z subset on the patch has nonzero incidence. The row-space character sum therefore kills every term except the all-X star after backward conjugation. The rotation identity has the stated minus sign, whose fourth power is positive. This yields parity times the product of cosines. The loss derivative, parameter-shift rule, and shot variance follow with the stated signs and remain valid where a cosine vanishes.

The claims about a held-out truth-table input are appropriately limited: the exact factorization already fixes every input's learned scale. The chapter does not infer statistical generalization, quantum advantage, decoder performance, or a new asymptotic code family from these demonstrations.
