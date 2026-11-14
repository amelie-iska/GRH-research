# Executable surface-code companion

## Numerical contract

The live case is the 3 × 3 torus with 18 data qubits. Qubit `q` is bit `q` of an integer basis index. `quantum-core.js` allocates separate real and imaginary `Float64Array`s, so a dense state occupies exactly `16 * 2^18 = 4,194,304` bytes. The worker keeps a current state, a fixed encoded reference and a scratch state, totalling 12 MiB in state buffers; browser, model and display overhead is additional.

The preparation gates and CSS checks are read from the generated topology JSON. On initialization the worker actually applies the encoder to the reference vector and checks every stabilizer and normalization. The interactive current vector begins at the all-zero basis state. H, X, Z, RY, RZ, CX and CZ modify amplitudes. A gate inserted at the playhead is executed immediately and inserted before the unexecuted tail. Play is paced; run is unpaced but yields between gates. Stop is honoured at a yield point.

Reported check expectations, Born probabilities, reference overlap, basis support and basis Shannon entropy are sums over the current amplitudes. No expectation is inferred from an error label. The support count uses a probability threshold of 1e-12. Reading diagnostics does not perform a projective collapse. Basis entropy is not described as entanglement entropy.

The remaining cases show exact topology, preparation data where available, and separate recorded experiments. They never silently allocate an 18-qubit surrogate for a larger register. The 2,048-qubit torus is explicitly a topology-only browser case.

## Trainable circuit

The four ordered qubits are the first star support `[0, 2, 9, 15]`. Every sample starts from the complete encoded 18-qubit reference. Apply `RY(sign[i]*pi/2 + theta[i])` to each patch qubit, then `CX(patch[i], patch[0])` for `i = 1,2,3`. Read `Z` on `patch[0]`.

Training examples are `++++`, `-+++`, `--++`, `+-++`, with target equal to the product of signs. The initial parameters are `[0.65, -0.4, 0.5, -0.6]`; the learning rate is 0.2. Each expectation derivative is evaluated from two complete shifted state-vector circuits. The mean squared loss gradient is `mean(2*(prediction-target)*expectationDerivative)`. The squared loss itself is not parameter-shifted. All sixteen sign patterns are evaluated after training, separating the four training and twelve held-out patterns.

An independent analytic identity, `prediction = product(signs) * product(cos(theta))`, is used in tests and described to the reader. It is not substituted for state-vector execution in the worker. This constructed task is deliberately simple and supports no quantum advantage or external learning-performance claim.

## Visualization and interaction

One Canvas2D surface view projects actual torus coordinates. Its modest line count and explicit camera transform make a self-contained canvas practical. SVG carries the circuit, loss graph, probability chart and paired polygon so their text remains accessible. The higher-genus graph drawing is a combinatorial layout with crossings; the checked rotation system, not the planar geometry, establishes genus. A canonical paired polygon supplies a separate topological schema. No analytic embedding, conformal uniformization or Belyi coefficient calculation is claimed.

The canvas backing store uses CSS size and a device-pixel-ratio cap of 2. A resize observer redraws the scene. Mouse drag has pointer capture and cancel handling; arrow keys and labelled camera sliders provide alternatives. Touch retains vertical page scrolling. Qubit selection uses screen-coordinate nearest-point hit testing within 14 CSS pixels, with an equivalent labelled native select. White-vertex labels and HTML check buttons connect the graph to the circuit wires.

The circuit displays twelve gates at a time and a labelled timeline-window control. It uses a bounded horizontal scroll area on narrow screens. A topology-only case with no encoder does not generate thousands of circuit wires. No animation runs automatically; Play is a deliberate user action. The page honours the base stylesheet’s reduced-motion policy.

## Evidence and records

`verify-quantum.cjs` checks the same kernel used by the worker: Bell preparation, complex phases, inverse rotations, the exact CSS reference, every single-qubit X/Z syndrome, all sixteen QNN patterns, the parameter-shift gradient and a decreasing training step. `data/cpu-validation.json` is an independent NumPy calculation from the topology workstream.

The page looks for `data/gpu-results.json` and `data/qnn-training.json`. Missing records display an explicit pending message. No GPU timing, precision or success is invented. Their results remain separate from the live browser session, and any imported final parameters require an explicit user click.

Run locally from an HTTP server: Worker and fetch paths require an ordinary same-origin web environment. The companion has no CDN or external runtime dependency. Browser rendering and interaction checks must be recorded separately from the Node numerical checks.
