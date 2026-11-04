# Exact finite persistence laboratory

Open http://127.0.0.1:8765/persistence.html or the single canonical
[book location](http://127.0.0.1:8765/book/main.html#lab-persistence).
The parameter ring k[x,y] is auxiliary; primary coefficients can be the
finite-length module E of the actual infinite completed nodal dessin order.
It is not a lattice or a finite-dimensional replacement for that order.

The staircase view computes four presets, custom minimal Artinian ideals,
standard monomials, adjacent syzygies, graded Betti shifts, comparable-grade
maps, CW cell homology and exact F2 derived-fiber dimensions. The interface
labels the different ranks over R and Lambda[x,y]. General exactness and
minimality are proved in the shared articles/book, not inferred from d²=0.

The quantum view uses eight equatorial inputs and two poles through the
**same saved QCNN4 channel**, with input births fixed at 0/500/1000.
This designed illustrative family is not new training or a held-out result.
Numerical trace distances are not interval-certified. Frozen integer graph
labels define exact flag 2-skeleta; all H0/H1 Betti and induced-map ranks use
exact GF2 elimination. The rank table fixes its target, varies comparable
sources and is not a complete two-parameter barcode. Both drawings use input
Bloch coordinates, not an embedding of output density matrices.

```sh
node scripts/check_persistence_model.mjs
.tools/book-quantum-cpu/bin/python examples/persistence/check_tool.py
python3 scripts/launch_inspector_browser.py
node scripts/check_persistence_browser.mjs
```

The browser launcher uses an isolated preserved headless Chrome profile and
refuses an occupied test port9242. The checker closes its own browser;
the reader preview on8765 stays available. Browser tests cover custom-input
errors, coefficients, fibers, cycle persistence/death, inclusion, rotation,
rank-table selection, mobile, deliberately corrupted downloads and one embed.

`check_tool.py` independently uses row matrices against the browser's bit
columns for36 cases, and SymPy for five staircase/cone/minor/Hilbert examples.
It also checks the actual node actions and immutable numerical/checkpoint/
implementation hashes. Independent review additionally enumerated cycle and
boundary cosets for160 seeded graph inclusions and64 staircases.
`check_resolution.py` preserves the earlier worked (x,y)^2 diagnostics.
`staircase.sage` is supplied **unexecuted**; the existing Sage launcher is
unavailable. Python symbolic and JavaScript finite checks ran successfully.

`export_quantum_bifiltration.py` creates content-addressed records and pins
checkpoint, generator and imported channel-implementation hashes. It runs no
optimizer and does not alter training outputs. The first record is preserved;
the current manifest's record adds the imported implementation hash with
unchanged distance/graph/state data. No package installation is needed.

The worked square-ideal module now has a complete underlying ungraded free
resolution and residue Hom boundaries checked in `/lean/PersistenceResolution.lean`.
General staircase, graded/category, CW/coefficient-cone and channel norm
formalization remain separate. These finite constructions do not solve the original low-gcd
estimate or establish the positive arithmetic determinant/GRH bridge.
