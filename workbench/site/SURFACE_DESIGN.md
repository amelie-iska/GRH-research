# Surface / attention / quantum explorer contract

Analytical job: explain how one checked combinatorial surface gives a dessin,
a physical spin-code model, an explicit classical attention controller and an
executed quantum-state circuit. The surface is constructed, not inferred from
measured cosmology. Renderer: one small SVG torus/flat chart, one circuit SVG,
one attention bar view and one 16-bin marginal view; ordinary DOM owns controls
and accessible numeric tables. No WebGL/decorative animation is necessary.

The model is the existing torus3x3 [[18,2,3]] case. Its 36 dessin darts are not
36 physical qubits. White midpoint vertices correspond to the 18 edge qubits.
Torus curves follow periodic parameter coordinates, not straight chord shortcuts.
A flat fundamental-domain view repeats boundary representatives, not qubits.

Select an edge using mouse, focus/keyboard or a native select. Its highlight
connects surface, attention, dessin cycles and star-patch circuit. Controls have
labels/units and URL state; exact config/results and model hash are exportable.
On mobile panels stack; no essential state is hover-only. Rotation has sliders
and reset. Reduced motion is the default (no automatic animation).

The worker executes the existing actual Float64 18-qubit state-vector kernel.
A prepared state is cached, but changed parameters trigger new gates and readout.
Requests are versioned; stale results cannot overwrite newer controller state.
The three modes are distinct: softmax weighted average, score-hard routing and
coordinatewise normalized max-plus. Per-coordinate winners are displayed.
The classical output sets RY angles; max-plus is never depicted as a unitary.

Metrics: expectation and independent analytic identity; state norm; measured
patch marginal (16 outcomes); marginal measurement entropy, not entanglement;
CSS check expectations; dimensionless toric-code Hamiltonian energy with J=1.
Native CPU, browser and optional real cuStateVec execution are compared, retaining
numeric tolerances and failures. No hardware, training or advantage claim follows.

QA: pure topology/controller parity; independent dense CPU/browser/GPU kernels;
coordinate-winner counterexample; URL restore; invalid domains; stale response;
edge/circuit linkage; mobile overflow and keyboard focus; JSON export; page errors.
