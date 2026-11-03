# Corrected research animations

2026-11-03. These CPU-rendered Manim scenes are mathematical visual aids. They do not certify GRH, an arithmetic spectral comparison, a complete AR classification or physical hardware.

## Implementation plan and boundaries

- `ThetaDessin`: draw the actual three torus arcs from (0,0) to (1/3,1/3), using lifts (1/3,1/3), (-2/3,1/3), (1/3,-2/3). Mark their two common black endpoints and three white midpoints. This is the elliptic theta's topological cellular embedding, not its uniformizing metric or an arithmetic flow.
- `HLSDiamond`: draw the nine named HLS quotient objects and all twelve signed arrows. Highlight one of the four exact mesh relations. The category is intrinsic to the specified H3 quotient-annihilator subcategory of the infinite Chebyshev order, not the ambient order or a derived AR component.
- `Bifiltration`: draw the three nonzero multigraded pieces of R/(x,y)^2 and its finite free resolution over the auxiliary polynomial ring R=k[x,y]. Display and directly check the two polynomial syzygies d1*d2=0. A chain identity or animation alone does not prove exactness or identify this polynomial ring with a surface order.
- `QCNNPooling`: draw the actual two-layer four-qubit Ry/Rz plus ring-CZ circuit, followed by CNOT(0,2), CNOT(1,3) and partial trace. Read its numerical parameters from the saved PennyLane experiment. Moving dots denote data flow, not a quantum state simulation. Pooling is a channel C^16 density matrices -> C^4 density matrices, not an impossible dimension-reducing isometry.

Only existing Manim is used; no installation, upgrade, paid compute or remote execution occurs. Original sources and the older animation remain untouched. The older `manim_surface.py` / `SurfaceClock.mp4` draws three disjoint torus loops and finite basis markers. It is a legacy clock schematic, **not** a theta dessin. New page captions should use the new scene for the actual theta.

## Reproduction

```sh
/Users/amelieschreiber/miniforge3/bin/manim -ql --media_dir outputs/animations examples/quantum/manim_research.py ThetaDessin HLSDiamond Bifiltration QCNNPooling
```

Expected files are under `outputs/animations/videos/manim_research/480p15/`. Render status and visual review will be recorded below after actual execution.

## Executed validation and visual review

All four scenes rendered successfully with the existing Manim 0.19.1 CPU/Cairo environment at low-quality preview resolution 854x480, 15 fps. No dependency or environment changes were made. The render log is `outputs/checks/2026-11-03-architecture/manim.log`. Normal Manim text/partial-video caches were emitted under the existing `outputs/animations` media root; these are intermediates, not additional mathematical deliverables.

| Scene | Duration (seconds) | MP4 SHA256 |
|---|---:|---|
| ThetaDessin | 6.933333 | abd6f495ef26425ab5b15187386c9f3a9f7c04ae9440eacfa63ee51ba24541ae |
| HLSDiamond | 8.133333 | 8c130310063fa6ace17930f6d80d78265bdf498b0b6f1ddf0da61938231db3f6 |
| Bifiltration | 7.866667 | 35f9b4668556686a378b5fcdbd78e9787da5886de98c3056977fc6cf6b2be7b1 |
| QCNNPooling | 8.733333 | d1fc3d038f0e7a4634c875226467b0fb4a594980ac2bc576820dcb3b42a61152 |

Final late frames from every scene were extracted with the existing FFmpeg and visually inspected. A first layout pass exposed bifiltration labels sitting on heavy axes; the final pass uses thinner axes, smaller arrow tips and off-axis labels. White theta vertices are additionally identified W1,W2,W3. The final QCNN caption says that displayed parameters are rounded; the circuit uses the saved actual checkpoint, whose held-out discard loss is 0.2397. The diagram reports that substantial residual instead of implying lossless compression.

The HLS shorthand c,h labels denote hook/cohook operations, not literal extra quiver letters. Its twelve signs are the book's exact central window. The highlighted mesh is A->B->E plus A->D->E, whose signed composites sum to zero. The source does not claim that each composite vanishes separately, nor that finite drawing verifies the entire infinite component.

For the bifiltration example the complete multigraded free modules are

```
F1 = R(-2,0) + R(-1,-1) + R(0,-2)
F2 = R(-2,-1) + R(-1,-2)
d1 = [x^2, xy, y^2]
d2 = [[-y,0], [x,-y], [0,x]].
```

The source contains a direct integer-coefficient monomial check of both entries of d1*d2. The full divisibility/exactness argument and graded shifts are in `book/chapters/persistence.tex`; they are not inferred from the animation. The quantum channel's positivity/trace identities have their own precise finite Kraus formalization in `BookInterfaces.lean`, which does not formalize these video frames or the learned optimizer.
