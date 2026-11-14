# Architecture ↔ surface-order bridge

The original 22 saved records and their manifest are untouched. The added
`web/surface-bridge-model.mjs` computes a crosswalk, rather than rewriting
saved metadata. `surface-bridge.mjs` renders it beside the numerical pass.
All rendering is original local Canvas code with no dependency or CDN.

The numerical DAG and the surface panel remain distinct. Selecting a numerical
coordinate or gate updates the second panel synchronously. The panel's edge
menu and white midpoints select a quiver vertex independently; a ring denotes
that selection and thick colored strokes denote numerical support. Orbit,
zoom, keyboard arrow navigation, algebra-construction steps, every forbidden
pair and exact diagnostic-module checks are available.

| Cases | Exact parent dessin/order | Finite-carrier dictionary and scope |
|---|---|---|
| Four-qubit QCNN | Elliptic square, σ=(0123), α=(02)(13), g=1, rank 16 | Four wires label four **darts**. There are only **two** α-orbits/quiver vertices, [0]={0,2}, [1]={1,3}. No algebra action is inferred from the four spins. |
| Nine-qubit QCNN | y²=x⁹−1, β=x⁹; σ=(0…8)(9…17), α=(0 9)…(8 17), g=4, rank 162 | Wire q labels edge [q]={q,q+9}. The finite Ising/CZ ring is auxiliary adjacency. Pooling keeps wires 0…4 and traces out 5…8; it does not contract the dessin or change its genus. |
| Quantum convolution | Elliptic theta, g=1, rank 18 | Panel explicitly labels k₁,k₂ by edges [0],[1] and local wires by those patch inputs. This added inspection dictionary is not stored module metadata or an order functor. |
| Quantum-feature attention | Same elliptic theta | Couplings label [0],[1],[2]; the stored pairs (0,1),(1,2),(2,0) determine each two-wire patch. Softmax mixes numerical features. |
| Six classical categories | The actual saved elliptic theta `surface_context`, σ=(012)(345), α=(03)(14)(25), g=1, rank 18 | Explicit relabelling: node positions 0,1,2 ↦ [0],[2],[1]. Saved edge tokens 4,5,6 ↦ a₀,a₂,a₁. Thus the saved endpoint cycle follows τ=σ⁻¹ in travel order. Token 3 is padding with no geometry. All six categories use their actual common context. Tokens, channels and expert slots forget the other branch and α-gluing. |
| Photonic pooling | Nodal interval on ℙ¹, β=4z(1−z), σ=(0)(1), α=(01), rank 2 | **Auxiliary analogy** labels modes 0,1 by branches x,y of k[x,y]/(xy). Quadrature coordinates x₀,x₁,p₀,p₁ locate these mode labels; symplectic evolution has no proved nodal-module functor. |
| Harper hybrid | Elliptic theta order displayed separately from auxiliary Weyl torus | Saved d=4 U=diag(iʲ), backward V, VU=iUV. Basis sites are auxiliary, not dessin edges. Learned patch features and exact PSD certificates concern the finite Harper model. |
| Computed clock | Same distinction | Adjustable forward shift, UV=ζVU. Invertible U,V cannot satisfy the zero relation of a forbidden pair; no order representation is asserted. |

For each exact dessin the code derives τ=σ⁻¹, φ=ατ, its passport,
Euler characteristic, arrows a_h:[h]→[τh], permitted successors a_τh
and forbidden successors a_φh. The UI gives

```
A = kQ / (a_h a_φh : h in H),  J = A₊,
Λ = lim_n A/J^n,
Λ ⊂ product_c B_c ⊂ product_c M_l(c)(k[[u_c]]),
R = k[[u]], u ↦ (u_c I)_c, rank_R Λ = sum_c l(c)^2.
```

Paired diagonal constant terms agree. The conductor contains u product B_c.
Permitted cycles repeat indefinitely, so A is infinite-dimensional and locally
gentle. Path degree and order-base u-degree differ. The finite carrier dimension
is neither an order rank nor a proof of a module action.

A separate diagnostic makes actual relation checking concrete. For any selected
arrow a_h, a two-dimensional module has M(a_h)=E₂₁, every other arrow zero,
and vertex idempotents project onto the indicated source/target basis vectors.
The checker verifies idempotent orthogonality/completeness, endpoints and every
forbidden product in the column-action convention. Every length-two product
is zero, so this is an actual A/J²-module and extends continuously to Λ. For
the nodal loop uM is nonzero but u²M=0; in the theta/square/higher-genus examples
uM=0. These modules are finite torsion modules, not R-free lattices and not the
trained spin/token/photonic carriers. A test assigning invertible identity
matrices to both nodal branches rejects both forbidden products.

The theta and square diagrams are genuine topological torus embeddings,
not analytic metric uniformizations. The genus-four plot uses actual radial
lifts x=r exp(2πie/9), y=±i sqrt(1−r⁹) and a sampled projection of the two
complex sheets. The compactification/infinity chart is not rendered; projected
sheets may overlap. Quiver arrows are schematic turns at the edge midpoints,
with their directions and branch choice determined by the permutations.

The independent `/rg.html` laboratory uses spins on clean-dessin black/white
vertices for actual Hamiltonian decimation and generated interactions. Those
spin labels differ deliberately from these quiver-edge/dart labels.

## Reproduce checks

No installation, training, checkpoint mutation, publication or external service
is required. From the repository root:

```
node examples/architecture/surface_bridge_check.mjs
node scripts/check_architecture_model.mjs
python3 scripts/launch_inspector_browser.py
node examples/architecture/surface_bridge_browser.mjs
```

The custom browser checker leaves its browser open for the original regression
harness. That harness closes only its isolated browser at completion. It has a
pre-existing initial-navigation race reading `document.body.dataset` before
the new document has a body. The retained evidence copy
`outputs/checks/2026-11-03-actual-rg/architecture/original-browser-harness-raceguard.mjs`
changes only `document.body.dataset.ready` to
`document.body?.dataset.ready`, keeping every original assertion. Run:

```
node outputs/checks/2026-11-03-actual-rg/architecture/original-browser-harness-raceguard.mjs outputs/checks/2026-11-03-actual-rg/architecture/original-browser outputs/renders/2026-11-03-inspector/actual-rg-regression
```

Results: all 23 bridge cases, 843 numerical nodes at first/last coordinate,
1300 exact forbidden-product diagnostics, unchanged saved SHA256 hashes,
all original numerical-model checks (22 cases and 20 clock configurations),
23-case bridge browser interactions and the original 22-case browser regression
pass. Bridge browser coverage includes gate/wire support, token/edge support,
padding, algebra steps, edge selection, orbit/zoom, quadrature branches, Harper
orientation, light/dark rendering, mobile width, reduced motion and browser
exceptions. Nine bridge screenshots and eight regression screenshots are
preserved under the already ignored local inspector render directory. The
isolated browser was closed after the final passing regression.

## Optional independent collections

`/architecture.html?collection=rg` reads only `/data/rg/manifest.json` and its
`records/` files. `?collection=qtoken` reads only
`/data/quantum-tokengt/manifest.json` and its `records/` files. Any other
collection value falls back to the original `/data/architecture/` collection;
query text is never treated as a URL or path. Record paths retain the original
strict `records/[A-Za-z0-9_-]+.json` whitelist, SHA256 verification and async
request guards. Raw-record links follow the same selected constant base.
The default original 22-case collection and computed clock remain intact.

A new `quantum-full-action-rg` profile uses `input.surface_m` (default 5), the
actual odd-hyperelliptic dessin, and the general sheet projection. For m=5 its
passport is (5,5; 2,2,2,2,2; 10), genus 2 and order rank 50. Physical clean-dessin
spins occupy two black plus five white sites (seven spins); black-spin decimation
leaves five physical white boundary spins. The quiver has five edge vertices.
A three-feature-qubit circuit encodes the **three coupling registers** J+, J−, b;
those wires are neither the physical boundary spins nor quiver vertices.
Parameter highlighting marks Hamiltonian support: J+ along the upper black-to-
white half-edges, J− along the lower half-edges with alternating signs (−1)^j,
and b at the **two black spin sites**, with coefficients +1 and −0.6. The
white fields are fixed separately.
A `boundary_configuration` coordinate represents one of the 32 full white-spin
configurations and highlights the five retained sites/edges. Binary-to-spin
signs follow the record's conventions; arbitrary learned head channels have
no unique geometric edge.

`quantum-tokengt-rg` receives the same exact m5 parent-surface context with an
explicit fallback explanation. It does not inherit the old theta fixture's
node/edge relabelling. Its dedicated interface owns its detailed token semantics.

Minimal manifest fields for each numerical case: `id`, `title`, `category`,
`kind`, `file` and `sha256`. A trace must satisfy the existing schema v1 and
finite numerical validation. The full-action profile recognizes node id
`couplings` with final coordinate 0/1/2 for J+/J−/b; usual `gate`, `wires` and
`basis` metadata for three-qubit gates; and axis `boundary_configuration` for
the 32-value full action. The circuit renderer requires `<group>.input` before
its gates so it can infer the register width. `training_source.path` supplies
the reproduction link. No new cases are added to the original manifest.
