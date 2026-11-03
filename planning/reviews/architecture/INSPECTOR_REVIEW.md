# Architecture inspector review — 2026-11-03

Independent reviewer: `/root/inspector_review`. Read-only review of the new
original local HTML/CSS/Canvas inspector, numerical helper module and pure
Node checks against P1 of the master plan and the immutable 22-case trace
manifest. No implementation file, checkpoint, source clone, environment or Git
state was changed. The only authored file is this report. No network service,
training, dependency installation or authentication was used.

The implementer owns the isolated test browser. This reviewer did not navigate
or alter that browser, so browser acceptance and screenshot inspection remain
the implementer's separate evidence rather than an inferred review result.

## Independent numerical checks

The project's existing Node executable was used. The committed checker passes
for all 22 saved cases and its 20 clock parameter cases. Additional independent
read-only checks traversed every exported coordinate and compared the helper's
lookup with recursive indexing of the original nested arrays:

- **82,295 coordinates** matched exactly.
- All **168** tropical context witness sets matched the recorded coordinate-wise
  winner masks, retaining equality ties of computed floating-point terms.
- All **392** block-validity cases correctly distinguished stored invalid-block
  zero from a legitimate max-plus contribution.
- **24** photonic covariance marginals satisfied the independent eigenvalue
  trace and determinant identities for their two-dimensional covariance blocks.
- For every dimension 3 through 16 and tick count 0 through 16, the dynamic
  clock matched the closed formula
  `psi'_j = omega^(t*j - t*(t+1)/2) psi_(j-t mod d)`, independently of its
  sequential matrix-vector implementation. Maximum component error was
  **3.15e-14**.

The forward shift uses `UV=omega VU`, correctly distinguished from the trained
Harper record's backward-shift convention. Complex tensors retain separate
real/imaginary components; integer coordinate lookup and the displayed squared
magnitude agree with those actual stored values. Covariance ordering remains
`x0,x1,p0,p1`, with hbar=2. The ellipse is labelled as a Gaussian marginal, not
an interacting field-theory reconstruction.

## Findings communicated to the implementer

1. **CNOT target symbol — corrected in reviewed working files.** The initial
   target circle had only a horizontal diameter and the incoming half of a
   vertical connection. The correction explicitly draws the full target-local
   vertical diameter, giving the intended plus-in-circle symbol.
2. **State preparation scope — corrected in reviewed working files.** The
   circuit displays exported post-preparation gates. The caption now explains
   that the encoder is represented by the stored StatePrep input, rather than
   claiming that an unexported preparation decomposition is drawn.
3. **3D painter ordering — corrected.** The original world-y ordering ignored
   camera yaw. The final implementation uses the actual projection depth,
   sorts far to near, and preserves that order for picking. The side-face
   selection follows camera direction, and the fit calculation considers the
   projected box corners. The saved browser checker explicitly verifies the
   depth ordering at multiple rotations and checks unzoomed bounds.
4. **Playback during asynchronous load — corrected.** The original timer could
   survive a new record load if Play was pressed during the fetch. Loading now
   sets a guarded busy state, disables workspace controls, prevents programmatic
   stepping/playback and pauses again on successful commit. Errors retain and
   identify the previous valid case, restore its selector/live parameters and
   display the error. The browser checker reproduces the original race and
   verifies the corrected behavior, rapid selection and checksum rejection.
   Abort/request-generation guards continue to reject stale completions.
5. **Minor accessibility issue — corrected.** The native step buttons no longer
   have their roles overridden by `role=listitem`, and the surrounding div no
   longer declares an incompatible list role. Separate step, coordinate and
   numerical cell controls remain keyboard-operable.

## Scientific and product boundaries

The numerical scene is an original computation-graph view, not a reproduction
of a hardware layout or a faithful infinite-order representation. Shape and
height labels describe tensor cardinalities. The trace selector distinguishes
trained CPU checkpoint replay, fixed-weight miniature references and a live
computed finite carrier. It does not relabel upstream reference weights as
trained TokenGT weights.

The mask and witness helpers follow the verified actual attention formulas.
Softmax weights in tropical records are correctly called comparison
diagnostics. Dispatch normalizes over tokens; combination normalizes over
expert-slots. Padded query contexts and invalid blocks are not interpreted as
positive evidence or useful zero maxima. Strict-prefix expert routing and
equal-rank attention remain distinct conventions in the underlying records.

The Harper UI reports the recorded exact rational principal-minor verifier and
accept/repair outcome, rather than treating a learned spectral proposal as a
proof. The source records already contain the independent Fraction checks;
the display itself is not a newly implemented rational proof checker.

Selected quantum states, probabilities, density matrices and gate records can
be inspected without replacing a partial trace by a smaller unitary state.
Unsupported optional upstream probes, non-Gaussian networks, GPU execution and
physical hardware remain explicitly unimplemented. Neither these displays nor
the numerical checker formalizes the whole book or proves the arithmetic
determinant bridge or GRH.

## Final integration review

The reviewer reread the corrected implementation and
`book/chapters/architecture.tex`. The chapter correctly distinguishes the
quantum feature vectors from classical attention heads, token versus slot
normalization, strict-prefix versus reveal-rank rules, partial trace versus a
smaller pure state, Gaussian marginals and known-spectrum finite Harper
certificates. The 3D scene is explicitly a computation-graph visualization.
No new theorem, full upstream training reproduction, whole-book Lean result,
hardware run or arithmetic positive-determinant comparison is claimed.

The immutable 22 manifest record entries and all 22 content hashes were
independently compared with the existing committed baseline and preserved.
Only presentation/status metadata has been updated; trained data and weights
were not regenerated. The pure numerical checker still passes.

The saved `outputs/checks/2026-11-03-inspector/browser.json` records all 22
saved cases plus the computed clock, numerical cell comparisons, playback and
view/slice/mask/circuit/covariance/certificate controls, 390-pixel mobile layout,
checksum interception rejection with no source mutation, no uncaught
exceptions, and a single canonical fifth in-book iframe. Its checker source
was read to confirm these are actual assertions rather than status labels.
Browser execution and screenshot inspection were performed by the implementer,
not repeated by this reviewer.

All important review findings are resolved. This is accepted as the scoped
P1 architecture-inspector implementation, subject to the implementer's final
fresh browser/build and repository-integrity checks. Comprehensive categorical
formalization, larger matched experiments and the arithmetic GRH bridge remain
independent open obligations.
