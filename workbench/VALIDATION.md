# Reproduce the version-two checks

The Python suite uses Python 3.12+, NumPy, SciPy and Node. The measured speech
study additionally uses SoundFile and PyTorch. Browser checks use Playwright and
an existing Chrome executable. GPU checks require the separately recorded CUDA,
CuPy and cuQuantum environment; there is no CPU fallback labeled as GPU.
No installation or environment replacement is performed by these commands.

```sh
python -m unittest discover -s workbench/tests -v
python -O -m unittest discover -s workbench/tests -v
python workbench/proof_port/check_models.py --output /tmp/expressivity.json
python workbench/realization_bridges.py --output /tmp/realizations.json
python workbench/half_density.py --output /tmp/half-density-cpu.json
python workbench/quantum_surface.py --output /tmp/surface-cpu.json
```

Run the six new Lean modules from the pinned mathlib checkout with
`lake env lean /absolute/repository/workbench/lean/<module>.lean`:
ExpressivityContracts, ConstructiveGraph, FiniteGraphNetworks, OrderRealization,
InformationContracts and HalfDensityContracts. The release audit checks complete
printed declaration/axiom inventories, source stability, no warnings, no sorryAx,
and no unexpected foundational dependencies. It records the compiler and mathlib
pins rather than assuming that a successful process status proves the claim.

The source archive is reproduced by `proof_port/inventory.py` and then annotated
by `proof_port/review_register.py`. Source preservation and per-claim mathematical
review have separate status fields. In particular, a preserved source proof is
not silently counted as a completed Lean formalization.

Physical controls use the fixed selection in `experiments/acquire_controls.py`.
Re-run acquisition into a fresh directory or one containing matching source
bytes; mismatches stop the acquisition. `physical_controls.py` accepts the data,
output and pinned native Mora-3 module directories explicitly. The tested source
pin and module hashes are recorded with the runs. No full-model campaign is
started by the workbench.

The release includes actual lossless test packets. Decode them with
`experiments/exact_codec.py`'s `decode` function and compare every integer with the
source representation. An int32 strain view has an explicit quantization step;
a successful packet replay does not claim recovery of an original float64 file.

For interactive checks run the loopback `bridge_host.py` service, or the static
`server.py` service for Pages parity. The publication evidence contains the exact
browser script and screenshots. A public HTTP/hash check is separate from a
rendered-interaction check. Do not present a static host as a remote Lean server.

The prior 37-page supplement, prior measured results and prior final-audit packet
remain historical artifacts. The current volume and new source/data evidence are
additional versioned objects with their own hashes and publication receipt.
