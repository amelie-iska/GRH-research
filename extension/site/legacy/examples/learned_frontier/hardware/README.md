# Three executable hardware reference designs

Python >= 3.10, standard library only. No installation or hardware is required.
These files specify integer/control behavior; they are not synthesized RTL,
cycle-accurate device models, trained chips or quantum hardware experiments.

| Reference | Executable behavior |
|---|---|
| `maxplus_tile.py` | Masked widened max-plus context; earliest witness; output saturation; explicit integer backward routing |
| `mixed_scheduler.py` | Ordinary MAC and max-plus units; bounded ordered completion; stalls, tags, operation counts |
| `readout_controller.py` | Synthetic IQ integration; affine discriminator; calibration/margin/deadline checks; allowlisted steering requests |

The shared default format is signed 8-bit raw integers with four fractional
bits: raw 16 represents 1.0. Max-plus terms add without a fractional shift.
MAC and readout products rescale once using arithmetic shift, rounding negative
fractions toward minus infinity, then saturate. Masked raw zero never represents
minus infinity. True maximum ties choose the lowest key index. This differs from
split-tie gradient conventions; no upstream training equivalence is claimed.

Run from the repository root:

```sh
python3 -B examples/learned_frontier/hardware/check_reference_designs.py
python3 -B examples/learned_frontier/hardware/maxplus_tile.py
python3 -B examples/learned_frontier/hardware/mixed_scheduler.py
python3 -B examples/learned_frontier/hardware/readout_controller.py
```

The checker emits JSON with source hashes, seed 20261104, parameters, checks,
detected negative controls and a small execution trace. `--output PATH` writes
a new JSON file and refuses to overwrite an existing one. The saved
`evidence-2026-11-04.json` records the initial passing run. Rerunning without
`--output` preserves that evidence. No cache, package, model, dataset or prior
output is deleted or upgraded.

Checks cover 256 two's-complement patterns, 65,536 8-bit additions, 262,144
exhaustive 4-bit two-lane mask/winner combinations, 300 seeded tiles, integer
VJP routing, 200 mixed jobs under three buffer capacities, backpressure and
out-of-order completion, six fail-closed readout conditions, 66 accumulator
boundary cases and nine malformed-input conditions. Twelve deliberate wrong
behaviors are distinguished from the valid contract. These are finite exact
program checks, not proofs of all dimensions or HDL equivalence.

The wider [architecture/evaluation notes](../../../planning/learned-frontier/hardware/ARCHITECTURES.md)
specify memory, training, toolchain and physical-measurement work still needed.
No universal speedup, synthesized frequency/area/power, quantum advantage,
measured readout fidelity or GRH result follows from these checks.
