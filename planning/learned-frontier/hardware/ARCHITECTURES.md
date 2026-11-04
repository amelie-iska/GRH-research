# Candidate architectures and a falsifiable evaluation campaign

These are research designs, not tapeouts. The three executable references use
only Python's standard library and synthetic public-free inputs. They make
arithmetic and control choices reviewable before proposing any dependency,
remote hardware job, process-design kit, paid solver or fabrication expense.

## Candidate A: fixed-point max-plus context tile

For supplied scores S[i,j], values V[j,d] and legality mask M[i,j], compute
Y[i,d] = max over legal j of (S[i,j] + V[j,d]). Query padding disables all its
terms. Store a separate validity bit and an earliest-index argmax witness;
invalid raw zero is never included in a maximum. W-bit signed Q-format inputs
are sign-extended before W+1-bit addition/comparison. Saturate the winning
value once to W bits and report overflow. This avoids both wraparound winner
reversal and false ties introduced by early saturation.

For N queries, K keys and D value coordinates, an all-valid context requires
NKD additions and ND(K-1) comparisons, with no multiplies **inside this context
primitive**. The direct dense score representation occupies NKW bits and the
values KDW bits, before banking, alignment, masks and metadata. Streaming can
avoid writing all scores if the scoring unit produces them in a useful order.
Training witnesses require ND*ceil(log2 K) index bits when K>1, plus validity
and overflow metadata. Recomputing winners instead trades storage for traffic
and arithmetic. A score based on dot products still costs its projections and
dot products; the audited Tropical Attention projective score has a different
operation inventory. Quantization can change winners, especially near ties.

Executable: `maxplus_tile.py`. Its backward routine is an unsaturated integer
VJP with an explicit earliest-winner tie rule; it is not an optimizer, a full
training implementation, or a universal derivative of fixed-point rounding.

## Candidate B: mixed MAC/max-plus engine

Keep an ordinary MAC unit alongside an add/compare unit, separate operand banks
and a shared ordered completion buffer. This supports ordinary projections,
residuals and heads around a tropical block. A job has opcode, raw operands,
valid lane bits and an implicit sequence tag. Input program order is retained;
each unit allows one outstanding operation in this conservative reference.
Independent units can complete in a different order. Backpressure reserves
bounded buffer capacity; only the oldest completed tag retires.

MAC products accumulate exactly before arithmetic right-shift by F fractional
bits and one final W-bit saturation. For a maximum reduction length L, a signed
2W+ceil(log2 L) accumulator suffices for L products when L>=1. The Python model
uses exact integers and tests output semantics, not overflow of an actual
finite RTL accumulator. Max-plus sums retain W+1 bits until the final maximum.
Unit latencies default to 3 and 2 abstract cycles, explicitly chosen parameters.
They do not predict device timing, bandwidth, overlap after synthesis, or power.

Executable: `mixed_scheduler.py`. The scheduler's oracle precomputes arithmetic
results, then simulates launch/completion/retirement; it models buffer/order
behavior rather than the internal pipeline registers of a hardware unit.

## Candidate C: quantum-readout feature and steering controller

At a fixed calibrated frame boundary, integrate valid signed IQ samples, apply
a fixed-point affine discriminator and emit an allowlisted action request.
For a frame with at most L valid W-bit samples, each sum uses
W+ceil(log2 L) signed bits. Coefficient products and bias are accumulated before
rescaling/saturating. Threshold, minimum margin, calibration epoch, sample count
and modeled deadline guard the action. Empty frames, overrun, stale calibration,
low margin, saturation and missed deadlines return HOLD. An opposite-sign valid
classification also returns HOLD without being confused with invalidity.

Executable: `readout_controller.py`. Input is **synthetic digital IQ**, not a
quantum state or measured device dataset. There is no ADC/DAC driver, RF pulse,
network connection, Qiskit import, quantum inference circuit or physical feedback
operation. Scores integrate rather than average samples, so deployments must
match calibrated frame length/validity treatment. The modeled decision latency
excludes ADC, transport, FIFO, clock crossings, DAC and qubit relaxation.
The QICK+hls4ml experiment motivates this interface, but no fidelity or latency
number transfers from its experiment to this reference.

If the user identifies `baremetalQiskit`, an adapter can translate a verified
compiled circuit's measurement schedule into frame IDs, calibration epochs and
device-native acquisition metadata. Keep a separate deterministic controller
for feature/reduction/deadline work; map an accepted request into calibrated
native actions only after backend conformance and device-specific approval.
Test offline replay, stale epochs, changed channel maps, unsupported mid-circuit
feedback, missing timestamps and reset behavior before touching instruments.
No claim is made that current Qiskit C/Python interfaces supply this full path.

## Candidate D: training witness/scatter companion

Pair candidate A with a winner-index SRAM and a banked gradient scatter engine.
Route upstream gradients to selected score/value coordinates, merge collisions
deterministically, and expose tie/clip counters. Ordinary gradient addition and
optimizer arithmetic remain explicit. Test random collision-heavy masks,
identical/near-identical maxima, invalid rows, and finite-difference agreement
away from ties and saturation. Compare fixed-winner, split-tie and chosen QAT
rules as different training methods. The reference VJP covers exact routing
only; a finite-width gradient buffer, stochastic rounding and optimizer are
further implementation work, not silently certified by the reference.

## Candidate E: semiring graph/dynamic-programming tile

Reuse add/compare lanes for max-plus path propagation or a separately specified
min-plus operator with explicit unreachable bits. This offers an interpretable
small graph baseline alongside learned tropical attention. Unsigned validity
and signed weights must remain distinct. Negating signed INT_MIN overflows, so
"min-plus equals max-plus with negated values" requires widened conversion.
For finite path-length bounds, record accumulator growth and cycle conditions;
do not claim a bounded tile solves arbitrary negative-cycle or NP-hard tasks.
This candidate is a design proposal, with no extra executable accelerator claim.

## Evaluation campaign and stopping criteria

1. **Semantics:** pin a full operator graph, dimensions, widths, rounding,
   saturation, masks, ties, gradient rules and all layouts. Preserve source
   datasets/checkpoints; use new named result directories with source hashes,
   seed 20261104 and every material parameter. The current integer checks are
   the first gate and have saved machine-readable evidence.
2. **Algorithms:** match accuracy and task definition before comparing cost.
   Test softmax, tropical, hybrid, ternary and hand-coded graph baselines on
   the same held-out splits, including unseen lengths/weights/geometry families.
   Report failed runs and quality losses; do not silently replace the task.
3. **Software baselines:** compare scalar, existing vectorized/GPU libraries
   and pinned tropical-gemm, counting conversion and transfers. Upstream speed
   tables are source claims, not results of this workspace. These runs remain
   pending because no environment or GPU job is authorized by these references.
4. **RTL and formal conformance:** implement precise ready/valid/reset behavior,
   accumulator bounds, tie order, tag reuse, buffer capacity and clock crossings.
   Independently simulate all reference vectors and prove bounded invariants.
   No RTL simulator or formal tool was installed or run for this campaign.
5. **Implementation:** with an explicitly approved installed toolchain/PDK,
   compare hand-directed ORFS placement, analytic placement and AlphaChip on the
   same synthesized netlist. Record library/PDK/tool SHA, timing/area constraints,
   seeds, clock tree, routing, parasitics and signoff settings. Distinguish proxy
   cost from completed post-route PPA; preserve every run in a fresh directory.
6. **System and physical validation:** report energy per accepted inference or
   complete training step at matched quality, measured throughput/latency,
   memory traffic, host/transfer/optimizer costs and thermal conditions. Quantum
   control additionally needs calibrated measured readout, error bars, leakage,
   crosstalk, drift and full feedback latency. Any real device access is separate
   from the offline reference and requires actual available hardware and scope.

A failed quality, overflow, timing, power, routing or reproducibility gate blocks
the corresponding performance claim. Neither a lower primitive operation count
nor a successful software trace closes a physical, arithmetic or GRH theorem.
