# Observational CMB control protocol

This source checkpoint precedes observation scoring. Acquire the three WMAP DR5
native map products (ILC, foreground-reduced V and W) and KQ85 mask only through
links present on NASA LAMBDA's official product pages. Record native FITS axes,
units, ordering, byte hashes and processing. Never infer microkelvin from values.

Analysis is intentionally broad: Gaussian widths 12, 18 and 24 degrees, and
four radial bands per template. NASA's ILC documentation states reliability
above approximately 10 degrees and warns about uncertain smaller-scale bias.
This is not a replication of a degree-scale Hawking-point search. The pipeline
uses pixel averaging to Nside16, lmax32, removes monopole/dipole, applies an
additional 5-degree beam, and keeps KQ85 fraction >=0.8 and |latitude|>=20 degrees.
The three original effective beams are not claimed identical.

Three predeclared statistics are scanned over every eligible center and scale:
a normalized broad temperature profile, low annular variance, and a frozen
4-to-2-to-1 learned quantum-channel readout. The latter is trained only on
independent random-phase reference skies and injected broad Gaussian profiles,
with a held-out validation selection. It is a classically simulated QNN, not
quantum hardware or the full Mora-3 model. No observed feature selects a gate,
threshold, center grid, scale, mask or amplitude.

The full location/scale/method maximum is recalculated for each of 511
calibration surrogates. Independent validation uses 256 draws; injection controls
use 64 draws per declared amplitude. Report finite rank resolution, Wilson
intervals, all products and all outcomes. No p=0 is emitted. The three products
share observations and the sky; use a family bound rather than multiplying their
probabilities or treating them as independent replication.

The null is conditional phase randomization of processed harmonic coefficients.
It preserves each coefficient magnitude, not a full instrument model. Exact
rank calibration requires invariance under this phase group. Anisotropic noise,
foreground-cleaning uncertainty, mask effects and harmonic-estimation error are
not completely represented. Therefore reported tails are **phase-surrogate
control ranks**, not posterior probabilities of CCC or universally calibrated
physical discovery p-values. A future full-instrument study must supply that
model and rerun the complete selection procedure.

Interactive views expose observed maps separately from synthetic injected
profiles and null realizations. A user-selected injection changes a fixed test
input; it does not retroactively change the trained model or calibration. The
original 96-point synthetic demonstration remains a separate regression example.
