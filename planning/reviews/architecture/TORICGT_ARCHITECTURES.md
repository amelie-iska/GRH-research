# ToricGT architecture inspector and persistent-feature study

2026-11-03. Independent source-based design audit. This report is the only file authored in this task. No upstream code, UI, environment, checkpoint or training output was changed. The suggestions below are executable **small demonstrations**, not a claim that the inspector has already reproduced every upstream architecture or loaded its trained weights.

## Pins and actual categories

ToricGT `a5199bc989a6fb170e21220e5e87bf95bc2fc0b4`; ToricGT-Program `f91ba1811b5a4f70d53c7120acf8ca2a0049f85b`. Inspected README/configuration and relevant portions of `graph_tokenizer.py`, `model.py`, `tropical_attention.py`, `soft_moe.py`, `toric_algebra.py`, `gudhi_persistence.py`, `koszul_persistence.py`, `gflownet.py`, `trajectory_memory.py`, `toric_vector_bundles.py`, and the current book quantum examples. The `soft_moe_toric.py` and `causal_soft_moe.py` files are compatibility re-exports, not new architectures. This is targeted architecture coverage, not a full repository code/security/performance audit.

The actual primary stack is: graph tokenization → pre-norm transformer blocks, choosing softmax/tropical/tropical-ring attention and MLP/Soft-MoE feedforward → normalization → node, edge, graph and optional language-model heads. Optional heads/probes add GFlowNet actions, trajectory retrieval, toric/commutative-algebra and persistence/categorical diagnostics. NC-torus matrices and phase helpers are finite classical numerical features upstream; they are not automatically quantum hardware operations.

The local project adds trained finite QCNN pooling, quantum graph-patch convolution, quantum-feature classical attention, Gaussian photonic pooling and the ToricGT/Harper surrogate. These are different architectures, not aliases for a fully trained quantum ToricTokenGT transformer.

## A common tiny deterministic fixture

For the classical inspector use `B=1, N=3, E=3, L=6, d_model=4, heads=2, d_head=2`, node width2, edge width1, no dropout, two experts with one slot each. Choose a labelled triangle or a three-edge dessin record and explicit fixed weights, e.g. integer fractions in `[-1/2,1/2]`. Display the seed/weight source as **didactic fixed weights**, never “upstream learned weights.” Expose each tensor with its shape and row/column meanings. A separate “trained finite quantum example” mode may load the actual saved parameters and show its recorded backend and dataset.

A good inspector shows actual numbers, the selected scalar's dependency path, and the precise operation producing it. An arrow animation alone is not a forward pass. Provide reset/pause/step, a small editable input, layer/head/token/coordinate selection, mask controls, and numerical differences against a reference calculation. An adaptation inspired by a public transformer visualizer should use original code/assets, not copied ones.

## Core demonstrations: exact operations and inspection targets

### 1. Graph-token construction / TokenGT structure

Inputs `node_features:[1,3,2]`, `edge_features:[1,3,1]`, `edge_index:[1,3,2]`, valid masks. Node output is

`t_v = W_n x_v + b_n + e_type(node) + e_node_id(v) + W_toric φ(v) + b_toric`,

where for rank2 `φ(v)=[sin(2πθv), sin(4πθv), cos(2πθv), cos(4πθv)]`. Edge output uses `W_e x_e+b_e`, edge type/id, and the projection of the concatenated source/destination identifier embeddings. Concatenate to `[1,6,4]`. Show every additive contribution separately, then their sum. Endpoint ids should illuminate the corresponding node-identifier rows, not falsely use the evolving node hidden state where this implementation uses learned identifier embeddings.

**Boundary:** adding absolute `node_id`, `edge_id` and index phases means blanket permutation equivariance is not established by merely permuting raw feature rows. IDs/metadata must be transported consistently, or use an explicitly invariant alternative. Active-edge truncation assumes the fixture's valid edge rows are packed first; do not use an arbitrary sparse padding mask to demonstrate that packing rule.

### 2. Masked Q/K/V and multi-head splitting

`X:[1,6,4] → LN(X) → Linear(4,12) → Q,K,V:[1,2,6,2]`. Upstream then subtracts each Q/K vector's maximum and L2-normalizes it before scoring. Show raw Q/K, max shift, normalized Q/K and the result separately. Do not present raw textbook dot attention as numerically equal to this normalized implementation. The comment about projective normalization does not prove that ordinary dot products are unchanged by these shifts.

Mask `M:[1,1,6,6]` combines valid query/key tokens and, if used, `rank(key)≤rank(query)`. Visualize excluded entries as masked, not as numerical zeros receiving probability. Entirely masked query rows produce zero context by an explicit guard. Equal reveal ranks are permitted by this mask; a strictly-past mode is a distinct rule.

### 3. Softmax attention

Per head `S=QKᵀ/√2:[1,2,6,6]`, then `A_ij=exp(S_ij)/Σ_legal_j exp(S_ij)`, `Y=AV:[1,2,6,2]`. Show score, allowed-key normalization, a selected weighted value sum, head gate `sigmoid(norm_gate)`, concatenation `[1,6,4]`, and output projection. Verify row sums1 for nonempty legal rows and zero output for empty rows. A temperature knob changes the demonstrated model; name it explicitly if added.

### 4. Tropical aggregation

The inspected implementation **still uses ordinary normalized dot-product scores** `S=QKᵀ/√2`. It replaces aggregation by

`Y_irc = max_(legal j) (S_irj + V_ijc)`.

Thus display one winning key **for each query and value coordinate**; different coordinates can select different keys. No row-stochastic attention matrix exists for this operation. The separate `maxplus_matmul` helper computes `max_k(a_ik+b_kj)` and is not the actual QK score computation above. Do not label every multiply/add in the whole network as max-plus. At ties show all maximizers and a deterministic tie rule for animation, not a unique differentiable winner.

### 5. Tropical-ring / block schedule

Partition the six keys into blocks of2. For each block compute the same coordinatewise maximum context as in item4, then take a maximum over blocks. Show a running partial context and its current winning block/key. The final value equals the unblocked tropical aggregation (up to the same floating operations). A block-size control should change scheduling, not the mathematical output. This fixture is a single-process schedule demonstration, not a multi-GPU benchmark or a distinct trained attention architecture.

The upstream `attention='hybrid'` mode means earlier layers use softmax and later layers tropical-ring. A layer switch can illustrate that actual mode choice. It does not mean “quantum–classical hybrid.”

### 6. Dense feedforward and residual block

For `H:[1,6,4]` use pre-norm `Linear(4,8) → GELU → Linear(8,4)` then add the residual. Also show the preceding attention residual. Expose activation signs, the nonlinear GELU curve and the selected output's full dot product. LayerNorm normalizes across hidden coordinates per token with epsilon and learned scale/bias, not across tokens. A residual is an addition, not a pooling or categorical quotient.

### 7. Graph-token Soft-MoE

Let `X:[1,6,4]`, keys `[E=2,S=1,d=4]`. Normalize X and keys, compute logits `ℓ_ies=exp(logit_scale)⟨x̂_i,k̂_es⟩:[1,6,2,1]`. Two different normalizations follow:

- Dispatch `D_ies=softmax_over_valid_tokens_i ℓ_ies`; slots `z_es=Σ_i D_ies x_i:[1,2,1,4]`.
- Apply each expert MLP to its own slots.
- Combine `C_ies=softmax_over_(e,s) ℓ_ies`; token output `y_i=output_scale Σ_es C_ies Expert_e(z_es):[1,6,4]`.

Show dispatch columns summing1 over tokens and combine rows summing1 over slots; label their axes. An expert-mass bar is not top-k hard routing. Padding should have no dispatch/combine mass. Masking active experts is a valid interaction; every expert may be active by default. Preserve the surrounding residual addition. The module itself is token-permutation equivariant, which does not remove the tokenizer's identifier qualification.

### 8. Prefix-causal Soft-MoE

Use length4, two slots, width4. Its expert slots at time t use only states with indices `<t`, via cumulative weighted numerator/denominator shifted by one position. The current token may determine combine logits. Animate the source-prefix boundary and verify perturbing a future token cannot change earlier outputs. The first strict-prefix slot is zero; an expert MLP with bias may still produce a nonzero output. This differs from global GraphTokenSoftMoE. `causal_soft_moe.py` merely re-exports this class.

### 9. Readout heads and optional routing

Node head `[N,4]→[N,o]`; edge head `[E,4]→[E,o]`; graph head uses the model's specified pooling and MLP. Expose the actual mask-aware pooling if implemented; do not silently substitute sum for mean. A language-model head is a distinct optional map to vocabulary logits, and any causal score demo must reveal only permitted context. A tiny head with o=2 can display both logits and softmax, but should not be labelled a reproduced language-model benchmark.

## Finite geometric, quantum and auxiliary demonstrations

### 10. Torus/Weyl features and the actual trained Harper hybrid

For q=4 use the pinned upstream convention `Ue_j=i^j e_j, Ve_j=e_(j−1)`, so `VU=iUV`. Show U/V entries, ordered products, their phase and the explicit norm residual. Do not mix this with the forward-shift convention elsewhere in the book. For W(a,b)=U^aV^b the multiplier is `i^(bc)`. The symmetric gauge `D(a,b)=exp(πi ab/4)W(a,b)` has multiplier `exp(πi(bc−ad)/4)`; the generic skew-Theta `projective_phase` has its own factor-of-two issue described in the ToricGT chapter.

The implemented `examples/quantum/toricgt_hybrid.py` genuinely imports `RotationAlgebraApproximant(1/4,max_denominator=4)`, uses `H(λ)=U+U†+λ(V+V†)`, encodes `[λ,.7λ²]` through two Ry gates, applies the common two-layer Ry/Rz/CZ/CNOT circuit (8 gate parameters), and reads three Pauli expectations plus an affine head (4 coefficients). Training is actual PennyLane CPU, 75/25 samples,160epochs, seed20261104. It predicts `λ_min(H)/6`. The inspectable pathway is λ → encoded amplitudes → gate/state evolution → Pauli features → affine prediction → rational proposal → **15 exact Fraction principal minors** of H−E I → accept or repair by exact bisection. The lower certificate is a finite Harper bound, not a global L-function zero certificate. This tiny carrier also has an exact analytic baseline: its real matrix has diagonal (2,0,−2,0) and cycle off-diagonals λ, so det(EI−H)=E²(E²−4−4λ²) and the target is −sqrt(1+λ²)/3. Direct symbolic determinant expansion was checked in the approved isolated environment. Display this known ground-truth curve beside the learned output; a numerical eigenpair alone is not needed as its justification. Upstream full transformer training is not reproduced by this surrogate.

### 11. Actual graph-patch convolution, quantum attention and QCNN pooling

- Shared graph patch: two coupling angles → two-qubit circuit → z=[⟨Z0⟩,⟨Z1⟩,⟨Z0Z1⟩] → shared affine exact-Ising-decimation target. Show the exact coupling formula alongside the learned prediction. This is a shared patch encoder, not an already implemented arbitrary global message-passing graph transformer.
- Attention: three edge-patch vectors `F:[3,3]`, classical scores `Fq:[3]`, softmax over three patches, context `Σα_iF_i:[3]`, shared affine output per pair. Show all3weights and conservation Σα=1. This is quantum-feature **classical** attention, not a coherent all-quantum attention circuit.
- QCNN: explicit n-qubit state → shared unitary → bipartite CNOT pooling → partial trace. Show both retained density matrix and discarded probability, not only an unphysical smaller statevector. Four-qubit and nine-qubit models have different capacities/data; do not conflate their saved weights or performance. One pooling step is not an established Wilson fixed-point RG flow.
- Photonic Gaussian pooling: two input squeezed modes → source beamsplitter → learned passive beamsplitter → covariance. Show quadrature ordering x0,x1,p0,p1, angle, covariance and known optimum. It is a finite Gaussian principal-axis problem, not a universal interacting photonic neural network.

### 12. Optional certificate/probe/head categories

The following are meaningful small numerical panels, but label them as **auxiliary demonstrations** unless the actual exported upstream records/weights are loaded:

| Category / actual source | Tiny executable record | Inspector boundary |
|---|---|---|
| GFlowNet `EmbeddingPolicy`, `trajectory_balance_loss` | Three states, two discrete actions, positive terminal rewards; forward/backward logits and the scalar residual `logZ+ΣlogPf−logR−ΣlogPb` | This is full-trajectory balance, not automatically SubTB. A backward policy must index actual reverse transitions. Do not infer solved proof search from a low finite residual. |
| Trajectory retrieval query/key/quality heads | Three stored 4-vectors, projection to2, cosine or implemented score, softmax over candidates, provenance labels | Show retrieved id/score and exact metadata; retrieval is not theorem verification, unlimited memory or demonstrated10M-context performance. |
| Toric semigroup/initial-form certificate | Four square exponent columns, candidate z, exact binomial z00z11−z10z01; max-plus cells | Float `int` conversion is not an exact certificate of the original real input. Opposite-corner ties are points, not extra facets. |
| Klyachko/sheaf probe | Two rays, three decreasing coordinate-subspace masks, three orthogonal chart frames | Check facewise inclusion plus displayed transition compositions. The helper uses transpose as inverse; use orthogonal frames or change to actual inverses, not arbitrary invertible frames. A zero residual on this tiny record is not full vector-bundle classification. |
| Koszul local-action probe | Two commuting rational2×2 diagonal actions; d1=[A B], d2=[−B;A] | d1d2=BA−AB. Generic learned neighborhood/time actions need not commute; a residual is not an exact complex. |
| Persistence/derived signature probes | Frozen 4point square, its full F2 boundary matrices and inclusion maps | Exact finite rank/homology for that complex is meaningful. Soft ranks/persistence images/signatures are summaries and are not a derived equivalence or complete multiparameter invariant. |
| PolarQuant KV feature compression | One 4vector, fixed orthogonal preconditioner, polar angles, quantized angles, decoded vector, norm error | Show bits and error; no claimed exact equality to unquantized attention or GPU acceleration. |

These optional heads/probes should not become indistinguishable boxes labelled “category theory” or “quantum.” Attach the schema, actual formula, provenance and verified output to each.

## Persistent-feature study: constructions with valid maps

### A. Radius persistence for a fixed layer or checkpoint

Freeze a finite labelled point cloud `p_i` (e.g. token hidden states after one layer). Fix its normalization once, then let `K_r` contain every finite σ with `max_(i,j∈σ) ||p_i−p_j|| ≤ r`. Include all faces and explicitly state a simplex-dimension cap. This is a Vietoris–Rips filtration; the inclusion maps induce homology maps. For a four-point unit square H1 appears at r=1 and is filled at r=√2 when diagonal edges and triangles enter (with the usual simultaneous-birth convention). Using only3vertices and immediately filling all triangles does not demonstrate a positive-length H1 interval.

The point cloud and metric do not depend on r. Re-normalizing separately at each threshold would define a different construction. Rational coordinates with squared-radius comparisons allow exact edge inclusion; floating point clouds give numerical diagnostics. If a dimension cap is2, an H2 class might only be a truncation artifact since missing3simplices cannot kill it.

### B. Prefix/radius bifiltration with frozen coordinates

If vertex i is revealed at time i and its coordinate remains fixed, put `K_(s,r)={σ: max σ≤s, diam(σ)≤r}`. For `(s,r)≤(s',r')` there is an actual inclusion. This matches the intent of `gudhi_persistence.simplex_birth_bidegrees`: birth degree is `(max(vertex index), radius index of diameter)`. Over a finite grid, chain generators and monomial boundary entries live over F2[x_level,y_radius]. Faces have no later birth, so boundary exponents are nonnegative and ∂²=0. Multiparameter persistence generally has no complete barcode decomposition; pointwise Betti numbers alone do not determine its maps/rank invariant.

### C. Neural layers or training checkpoints are not automatically a filtration

For arbitrary learned embeddings `p_i^(s)`, edges may appear and disappear as s changes. Thus a sequence of layerwise Rips complexes does NOT give `K_s⊂K_(s+1)` in general. A slider through saved checkpoints must display “independent per-checkpoint persistence” unless one of the following extra constructions is chosen and named:

1. **Union history:** `L_(s,r)=⋃_(t≤s) K_r^(t)` is a genuine bifiltration in stage/radius. The union is taken at the simplex-set level. It need not equal the flag completion of the union of edges, which may add triangles whose edges never coexisted.
2. **Minimum dissimilarity envelope:** `δ_s(i,j)=min_(t≤s) d_t(i,j)` decreases in s, so its flag complexes grow for fixed r. δ_s need not satisfy the triangle inequality: call it a flag/dissimilarity filtration rather than an assumed metric Rips construction. Its mixed-stage cliques have a different interpretation from union history.
3. **Maximum envelope:** `Δ_s=max_(t≤s)d_t` increases; its r-threshold complexes SHRINK with s. Reverse the finite stage index, use the corresponding inverse diagram, or use a fixed all-stage maximum to obtain one robust radius filtration. Do not draw forward inclusions in the wrong direction.
4. **Zigzag:** `K_s → K_s∪K_(s+1) ← K_(s+1)` gives valid inclusions and a zigzag persistence problem. A dedicated zigzag algorithm and maps are required; plotting ordinary independent diagrams is not its computation.
5. **Verified chain maps:** if a proposed inter-layer vertex map takes each source simplex to a target simplex (or is given as explicit matrices commuting with ∂), it induces homology maps. Check simplicial or chain-map conditions, not only matching Betti numbers. An arbitrary learned linear feature map does not automatically preserve a threshold complex.

Attention is generally asymmetric. If constructing a graph from it, declare the symmetrization, e.g. `(Aij+Aji)/2`, threshold direction and face completion. The resulting edge weights need not define a metric. Directed flag complexes are a different chosen model.

### D. A positive quantum pooling connection

There IS a useful monotonic case: apply the SAME fixed finite CPTP channel Φ to every state's density matrix and use trace distance `d(ρ,σ)=||ρ−σ||_1/2`. Contractivity gives `d(Φρ_i,Φρ_j)≤d(ρ_i,ρ_j)`, hence the identity on sample labels induces inclusions of their threshold flag complexes at every radius. Unitary conjugation followed by partial trace, as in one fixed trained QCNN pooling channel, satisfies this hypothesis. A sequence of common CPTP channels gives a genuine stage/radius bifiltration, even though the Hilbert-space dimensions can decrease.

Sketch: for Hermitian X, `||X||_1=max_(-I≤A≤I) Tr(AX)`. The dual of a trace-preserving positive channel is unital positive and takes the order interval [-I,I] into itself, so the supremum cannot increase. This proves contractivity on differences of states. The construction compares topology of a finite state family, not geodesic distances on the dessin surface.

This does NOT make training epochs monotonic: independently changing θ generally does not supply a channel mapping every epoch-s output state to its epoch-(s+1) output. Nor does it cover a different input-dependent channel for each sample, postselected renormalization without success-probability control, or Euclidean embeddings of expectation vectors without a separately proved contraction bound.

## Required inspector evidence and scope labels

For each architecture store: source module/pin; own fixture or real checkpoint; tensor shapes; gate or matrix conventions; exact/current operation; trained versus didactic status; backend; scalar loss/check; and any truncation/normalization. Interactive edits should recompute actual values. Test softmax row sums, all-pad rows, ring/full equality, dispatch/combine axis sums, absence of future-token influence in the causal fixture, exact cocycle/zero-relation identities, and ∂²/chain-map conditions. For persistence, show birth data and inclusion maps, not just a decorative barcode. Keep original UI code/assets; the public transformer visualizer is conceptual inspiration only.

The learned ToricGT/Harper circuit can generate finite spectral proposals and exact PSD certificates. The optional proof-search narrative remains proposals plus independent checking. None of these architecture panels or persistence constructions identifies a global arithmetic self-adjoint determinant, supplies Artin holomorphy, or proves GRH.
