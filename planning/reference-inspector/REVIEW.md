# Reference-informed architecture inspector — 2026-11-03

The approved request was to study [Brendan Bycroft's LLM visualization](https://bbycroft.net/llm) and substantially improve this repository's numerical architecture inspector, while keeping saved experiments, source editions, trained weights, and the single canonical book embedding intact.

## Reference and evidence scope

Pinned public source: [bbycroft/llm-viz at 9da93742382f1bf36c020c38a1ace454e82c4490](https://github.com/bbycroft/llm-viz/tree/9da93742382f1bf36c020c38a1ace454e82c4490). `source-manifest.json` records exact SHA-256, byte size, path, and the actual reviewed sections for ten retrieved source files. Complete retrieval is distinguished from selected code review; this is not a claim to have audited the entire upstream application. Local `upstream-*` files are preserved research snapshots, not application imports or proposed runtime assets. The reference's LICENSE is MIT, copyright Brendan Bycroft, with upstream README exceptions for homepage and third-party assets. No upstream renderer, model weights, fonts, shaders, images, or implementation code were incorporated into the local application. Its interaction vocabulary informed an original dependency-free Canvas2D implementation. Visible attribution links point to the reference and pinned source.

Observed directly in isolated Chrome/CDP at 1550×1000:

- A full-model overview uses a tall spatial stack, separated parameter/activation solids and a persistent left chapter/narrative rail. Saved screenshot: `outputs/renders/2026-11-03-reference-inspector/reference-open.png`.
- Selecting Self Attention changes the chapter; Continue moves the camera and expands Q/K/V matrices and parallel heads beside the narrative. Saved screenshot: `reference-walkthrough.png` in the same folder.
- A later reference hover attempt failed after the reference application raised `Shape 144, 48 requires 6912 buffer, but buffer has size 0`. The saved `reference-hover.png` records that failed page, **not successful hover evidence**. The reference's hover and cell formula behavior are source-confirmed rather than claimed as directly observed in that failed attempt.

Source-confirmed design observations:

| Source | Confirmed behavior | Local mapping |
|---|---|---|
| `GptModelLayout.ts` | Dimension-labelled tensor solids; spatial heads/QKV; separate weights; explicit dot/add dependency metadata; residual and feed-forward paths | Shape-derived grids, real head planes, Q/K/V/residual/expert lanes; trace edges retained |
| `Camera.ts` | Model bounds, camera target and timed position/angle transition | Fit/overview/operation focus; smooth target movement; reduced-motion jump |
| `Interaction.ts` | Ray/box picking converted to cell coordinates, dependency-index mapping, source row/column highlights | Inverse projected-face picking and literal coordinate tooltips; supported source coordinates highlighted |
| `render/blockRender.ts` | Value textures and camera-distance nested grid LOD | Exact small planes; explicit sampled-coordinate strides for larger planes, plus an exact 8×8 lens |
| `components/BlockInfo.ts` | Camera-scaled block names above solids | Node IDs, tensor shapes, plane/head labels |
| `components/DataFlow.ts` | Coordinate/value popup with dot/add/LayerNorm/softmax/attention formula and dependency arrows | Stored formula, actual input links and independently evaluated supported scalar/complex terms |
| `walkthrough/Walkthrough*.ts[x]` | Chapter selection, commentary/time breaks, focusing one head, aligning QKV | Persistent operation narrative, architectural stage navigation, play/pause/step and focus camera |

## Implementation

`web/architecture-layout.mjs` is a pure module deriving family, DAG rank, semantic lanes, shapes, planes and cell dependencies from the existing validated trace. `web/architecture-viewport.mjs` renders and picks tensor faces without packages or external services. `web/architecture.mjs` keeps the existing collection allowlist, SHA-256 loading, request/abort generation guards, existing stable control IDs and `window.architectureInspector` methods. Its snapshot adds selected coordinates and viewport/plane metadata without removing old fields.

The main viewport replaces the old uniform-card, 18-node window. Full model mode lays out the complete visible numerical graph. Focus mode displays actual parents → selected operation → actual consumers, preserving true links while arranging them for inspection. Small planes have one cell per stored coordinate. Larger displayed planes explicitly state sampling strides; those are **literal sampled coordinates**, not averages or invented missing values. The 8×8 cell lens and existing numerical pane inspect exact coordinates, including coordinates between overview samples. Rank-one state vectors are folded in basis order, with that fold labelled. Up to three real head planes appear at once; leading-axis inputs reach every stored head/batch/other slice.

Attention uses its real Q/K/V, masks, head planes, residual and expert tensors. Softmax winners/block contexts/block-validity arrays are labelled comparison diagnostics, muted, and connected with dashed lines. Softmax weights in tropical mode receive the same comparison label; max-plus winner masks are labelled witness diagnostics. These saved diagnostic tensors are not presented as the active aggregation path. Quantum models show actual state tensors and the selected gate's labelled wire support; the existing full circuit remains accessible. Gaussian models show true symplectic/covariance branches and retain the marginal inspector. Critic and continuous GFlowNet traces keep their own latent, intervention, forward/backward-density and objective structure. Quantum TokenGT's measured features feed explicitly classical attention; no coherent quantum attention or GPT structure is invented.

Hover reads an exact stored real/complex value and mask status. Click pins it, synchronizes the numerical pane, surface/order inspector, supported source-cell highlights and formula terms. Supported independent calculations are Q·K/√d, masked softmax, softmax context, max-plus context, the saved half-softmax/half-max-plus hybrid, matching-shape residual/difference sums, and saved RY/RZ/RX/CZ/CNOT complex amplitudes. Other operations retain their source formula and input tensor links, with an explicit notice that a general cell-index map is not declared. The interface does not invent a complete symbolic derivation for unsupported operations.

Camera controls: drag orbit, Shift-drag pan, wheel or +/- zoom, F fit, O overview, Enter operation focus, arrow keys step, Shift-arrow pan, Space play/pause. Visible buttons provide equivalent actions. Camera movement follows operation selection, and OS reduced motion removes it. Scientific cells do not blink. Shared living/night controls remain; the tensor canvas renders its own dark colors rather than applying the shared canvas inversion twice. The synchronized surface/order construction is in a secondary drawer. No book iframe was added or replaced.

## Verification and preserved inputs

Commands run from repository root:

```sh
node --check web/architecture.mjs
node --check web/architecture-layout.mjs
node --check web/architecture-viewport.mjs
node scripts/check_architecture_model.mjs
node examples/architecture/check-reference-layout.mjs
node examples/architecture/check-reference-browser.mjs
node examples/architecture/check-reference-compat.mjs outputs/checks/2026-11-03-reference-inspector/compat outputs/renders/2026-11-03-reference-inspector/compat
```

The browser scripts use the existing isolated Chrome/CDP harness on 9242 and the existing loopback server on 8765; no package install. The new browser checker leaves the browser available; the compatibility checker closes only that isolated browser. Its copy of the existing legacy suite changes the obsolete fixed book iframe count of seven to dynamic uniqueness and canonical-architecture checks, and uses optional-body polling during navigation. It does not change application expectations. The book has continued to gain independently owned tools, so the new checker also avoids a fixed total iframe count.

Results recorded under `outputs/checks/2026-11-03-reference-inspector/`:

- Original model checker: 22 original cases, every exported tensor indexed, 20 computed-clock parameter combinations, masks/ties checked.
- `layout-numerics.json`: all **34** saved cases across original/actual-RG/Quantum-TokenGT collections; **55,299** displayed coordinates match saved arrays; **37,701** supported cell formulas independently agree within 1e-8; topological order, non-overlap, QKV lane order, exact/LOD behavior, narrative generation and diagnostic/live mode distinction checked. A separate computed eight-dimensional/four-tick clock is checked too. Tests are deterministic and do not train or generate scientific results.
- `browser.json`: **34** cases and **15** screenshots; actual viewport hover/click picks the expected coordinate; numeric windows match arrays; camera/fit/keyboard controls, depth order, playback/loading pause guard, final-choice race, corrupt-checksum rejection, diagnostic labels, reduced motion, shared theme, all-collection mobile overflow, and unique canonical book embedding pass, with zero local uncaught exceptions.
- `compat/architecture-browser.json`: **22** original cases and **8** legacy screenshots, including original gate/covariance/tropical/expert/certificate/clock controls, invalid-parameter retention, races, checksum rejection, mobile and book integration pass.
- `preserved-inputs.json`: **20** unique saved source/checkpoint paths match their declared hashes; `architecture-model.mjs` is byte-identical to Git HEAD. The 34 content-addressed trace records match their manifest digests; all three manifest digests are recorded in `layout-numerics.json`. No saved trace, training output or checkpoint was rewritten.

Review screenshots: `attention-cell-hover.png`, `attention-cell-selected.png`, `attention-overview.png`, `quantum-gate.png`, `tropical-context.png`, `expert-dispatch.png`, `quantum-features-classical-attention.png`, `family-gaussian.png`, `family-critic.png`, `family-gflownet.png`, `shared-night.png`, `mobile.png`. The last small copy change qualifies full upstream optional-head limitations and links executed local critic/GFlowNet/persistence examples; the final dark-canvas inversion override and stale-tooltip dismissal were syntax/model checked after the complete browser runs and handed to the parent for final browser confirmation.

## Limits

This remains a local numerical replay. It is an original axonometric Canvas2D adaptation, not Bycroft's WebGL engine, visual asset set, camera matrices, GPT model, or full tutorial. Geometry compresses large dimensions with explicit LOD; overview labels can be dense and operation focus/lens are the reading views. Only recorded heads and operations exist. No new training, arithmetic theorem, physical quantum hardware result, complete upstream campaign, or full symbolic formula coverage is claimed. No production dependency, infrastructure, authentication, MCP activation, public deployment, or external write was added. No Git staging, commit, or push was performed by this UI worker.
