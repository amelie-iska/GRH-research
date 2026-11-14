# Conformal cyclic cosmology: primary-source review and reproducible demonstration

Review date: **13 November 2026**. The associated chapter is
`extension/manuscript/chapters/cyclic-cosmology.tex`. Bibliography entries are
in `sources.bib`, all with the `CC` prefix. The machine-readable provenance and
coverage record is `source-manifest.json`.

## What was reviewed

Eight central primary papers were read throughout their extracted text,
including references and extracted captions: **96 PDF pages and 46,784
whitespace-delimited extracted words**. This is a full content review of those
versions, not an independent verification of every proof or a replication of
their observational pipelines. Four selected source pages were additionally
inspected as rendered images to check equations and quantitative claims.

The longer Tod minicourse, Planck analysis and Simons Observatory forecast were
read only in the exact sections and text-line ranges recorded below. The latter
is used as a historical example of forecast methodology, not as a report of
instrument status in 2026. Foundational Shannon and Wootters–Zurek references
were checked at metadata/opening-material or abstract level; they are not
counted as full reviews. The chapter supplies its own complete finite proofs
of the information and quantum statements it uses.

| Source and frozen version | Scope actually read | Role in the chapter |
|---|---|---|
| [Gurzadyan–Penrose, 1011.3706v1](https://arxiv.org/abs/1011.3706v1) | All 8 PDF pages, extracted lines 1–254 | Original low-variance circle claim |
| [Moss–Scott–Zibin, 1012.1305v3](https://arxiv.org/abs/1012.1305v3) | All 4 PDF pages, lines 1–208 | Correlated Gaussian null, variance statistics |
| [Gurzadyan–Penrose, 1512.00554v2](https://arxiv.org/abs/1512.00554v2) | All 5 PDF pages, lines 1–215 | Explicit cross-aeon SETI proposal |
| [An et al., 1808.01740v5](https://arxiv.org/abs/1808.01740v5) | All 7 PDF pages, lines 1–457 | Hawking-point claim and its tested scale statistics |
| [Jow–Scott, 1909.09672v2](https://arxiv.org/abs/1909.09672v2) | All 11 PDF pages, lines 1–551 | Global scale-scan comparison and related tests |
| [Markwell–Stevens, 2212.06914v2](https://arxiv.org/abs/2212.06914v2) | All 14 PDF pages, lines 1–739 | Restricted conformal-factor and matter ansatzes |
| [Bodnia et al., 2208.06021v3](https://arxiv.org/abs/2208.06021v3) | All 27 PDF pages, lines 1–1228 | High-resolution ring and HawkingNet null searches |
| [Meissner–Penrose, 2503.24263v1](https://arxiv.org/abs/2503.24263v1) | All 20 PDF pages, lines 1–1218 | Revised crossover/GWE proposal, spinor charge, FLRW quartic |
| [Tod, 2102.02701v1](https://arxiv.org/abs/2102.02701v1) | Lines 123–363, 532–566, 2049–2400; §§1.2–1.2.4, 1.3.1, 3.6–3.7; printed pp. 3–9, 13–14, 47–54, with adjacent fragments | Conformal identities and physical qualifications |
| [Planck, 1906.02552v2](https://arxiv.org/abs/1906.02552v2) | Lines 1–204 and 6151–6360; abstract/introduction/data material and all §8 conclusions, printed pp. 52–55, with adjacent fragments | Shared sky, polarization, systematics and anomaly testing |
| [Simons Observatory, 1808.07445v2](https://arxiv.org/abs/1808.07445v2) | Lines 160–190 and 793–1039; contents and §2.6, printed pp. 11–14, with adjacent fragments | Conditional Fisher and simulation-based forecasting methodology |

Text lines refer to the SHA-256-frozen `pdftotext -layout` extraction in the
manifest. A page range can contain adjacent sections because of PDF text
ordering; it does not expand the claimed section coverage. The PDFs were cached
outside the git repository and are not vendored here. Their explicit versioned
URLs and hashes allow retrieval and comparison.

## Evidence distinctions retained in the chapter

**Geometry.** Positive conformal changes preserve null trajectories and the
source-free four-dimensional Maxwell system on regular domains. The chapter
proves the connection, Hodge and stress-tensor scaling formulas. A zero or pole
at crossover requires additional extension and field-equation hypotheses.

**Dynamics.** The 2025 source develops a weak-field spinor/twistor charge and
invokes an additional no-net-flux/local-isotropy argument in the succeeding
aeon. The chapter states and proves the regular source-free Stokes component
with its hypotheses. It does not promote that component to a general nonlinear
crossover existence theorem. Its Friedmann elliptic-curve bridge is restricted
to the intervals on which the displayed matter-conservation laws hold.

**Observations.** Positive ring and Hawking-point claims are presented together
with independent Gaussian-null and neural-search analyses. The quoted 13%
probability to exceed is specific to Jow–Scott's global scale-search statistic.
The later HawkingNet negative result is specific to its tested profile family
and pipeline. Neither becomes a posterior probability for all of CCC.

**Intentional messages.** The 2015 SETI proposal is described fairly as a
proposal. No decoded intentional message is established by the reviewed
sources. The chapter requires an explicit sender/encoding/transfer/detection
model and proves what follows when message-dependent data laws coincide or
nearly coincide. The synthetic code is not an attempted message decoder.

**Computation.** A learned statistic can improve feasible inference from an
identifiable noisy channel; post-processing cannot create mutual information
absent from the channel. The formal statement is proved rather than used as a
generic assertion about machine learning.

## Specific transcription and interpretation checks

- Meissner–Penrose's equation (99) is a **radius of 0.03–0.04 radians**, hence a
  diameter approximately 3.4–4.6 degrees. A secondary 2026 web claim of a 6–8
  degree prediction is not substituted for the primary equation.
- The same paper's PDF page 10 explicitly distinguishes the late-vacuum field
  argument from its early-aeon isotropy/no-net-flux argument. Page 13 restricts
  the constant-coefficient Weierstrass solution outside the proposed GWE.
- HawkingNet's operational injection range in §4 is **100–400 microkelvin**.
  The introduction's “100 mK” wording is not propagated into the chapter. Its
  quoted width parameter is not silently relabeled as a FWHM or standard
  deviation of an unspecified profile convention.
- The Markwell–Stevens preprint contains convention/typographical hazards,
  including reversed limiting descriptions of reciprocal conformal factors in
  introductory prose. The chapter defines its own consistent convention.
  Author order follows the reviewed PDF; arXiv metadata reverses it.
- The local twist `(theta, phi) -> (theta, phi + S theta)` is not conformal for
  the round-sphere metric when `S != 0`; the chapter displays the pullback
  metric. More generally, a conformal map need not preserve a null covariance.
- Repeating parameter fitting inside a parametric bootstrap is not asserted to
  make a fitted null exactly exchangeable. The exact rank theorem is stated
  only for exchangeable statistics.
- Matching the same feature in two satellite maps helps distinguish certain
  instrumental errors, but their underlying cosmic realization is shared.

Rendered source pages inspected: Meissner–Penrose PDF pp. 10 and 13;
Jow–Scott PDF p. 7; Bodnia et al. PDF p. 15 (printed p. 14).

## Original mathematical exposition and audit

The chapter gives full proofs of the conformal connection/null-geodesic and
Hodge identities; a square-free quartic compactification and its explicit
Weierstrass substitution; a conditional spinor/Stokes conservation statement;
finite classical data processing, total-variation identifiability and a
decoding-error bound; trace-distance contraction, no-cloning and no-signalling;
Gaussian quadratic-form moments, matched filtering, finite Monte Carlo rank
calibration, elementary cosmic variance and nuisance-projected information.
These are established mathematical results or direct derivations assembled for
the synthesis, not claims to have originated the underlying theorems.

A separate agent independently checked the quartic-to-cubic substitution,
differential, simple-branch-point count and infinity charts. The resulting
field-of-definition qualification was added: the root-based substitution is
over the complex numbers or a field containing the selected root, and need not
be defined over the original real or arithmetic coefficient field. This
focused check does not certify every other proof or the source papers.

No claim is made that this entire chapter is Lean verified. A typed finite
linear-map fragment elsewhere in the project has a separate formalization
scope.

## Executed synthetic experiment

Run `python extension/review/cosmology/synthetic_search.py` from the repository.
It requires NumPy and uses no downloaded data or SciPy. It fixes 96
Fibonacci-sphere directions, an explicitly positive-definite smooth covariance,
288 templates, 4,095 calibration simulations, 2,048 independent validation
simulations, and PCG64 seed 20261113. The script hash and versions are included
in `synthetic-results.json`.

The one base noise sky and predetermined matched-SNR injections give:

| Injected matched SNR | Maximum filter score | Selected-template local tail | Full-scan rank p |
|---:|---:|---:|---:|
| 0 | 2.7171463973 | 0.0032923737 | 0.4621582031 |
| 1 | 3.0877987120 | 0.0010082250 | 0.1809082031 |
| 3 | 4.1109883424 | 0.0000196985 | 0.0034179688 |
| 5 | 6.0413910067 | 0.000000000764 | 0.0002441406 |

Zero exceedances in the last row give the finite rank resolution `1/4096`, not
a measured tail below that resolution. The separate null validation has 119
rejections among 2,048 draws at nominal 0.05; this is a finite conditional
diagnostic, not exact equality to the nominal rate. The selected local tail is
deliberately labeled uncorrected. Actual CMB power-spectrum estimation,
foreground processing, published-pipeline replication and source transfer
physics are outside this demonstration.

## Additional source handling

The current-date freshness check is recorded in `freshness-check.json`: five
focused searches with 365- or 730-day recency hints, followed by primary
metadata checks, with cutoff **13 November 2026**. The Meissner–Penrose record
still lists only its March 2025 version. A later theoretical preprint,
[Marosek–Balcerzak, 2608.27014v1](https://arxiv.org/abs/2608.27014v1), was located
and its primary abstract and submission history were read. Its varying-constant
bimetric proposal is not a reported empirical CMB confirmation or decoded
message. The search-service open failed, but ordinary public HTTPS retrieval
of the primary abstract succeeded; that response is hashed in the freshness
record. This is **abstract-level coverage only**, and it does not increase the
eight-paper full-reading totals.

The bounded search did not locate a substantiated later empirical confirmation
of the reviewed signature claims or an established intentional cross-aeon
message. Search incompleteness remains possible. In particular, the chapter
does not describe the 2025 proposal as the latest CCC paper of every kind.

An institutional download for Eckstein's 2023 paper returned HTML rather than
PDF; it is recorded as a failed PDF retrieval, and no full-PDF review is
claimed. Selected publisher HTML was inspected during source discovery but is
not used as a technical foundation in this chapter. Secondary 2026 web claims
without a substantiated primary source were excluded. The search does not
claim exhaustive coverage of every CCC-related publication.

## Browser implementation verification

`extension/site/verify-cosmology.cjs` passed against the exported Python
fixture. It checked all four recorded experiment scores, winning template
indices, exceedance counts and rank probabilities; all 288 normalized
filter/injection pairings (maximum error `1.5543122344752192e-15`); normal tails
against Python references; all 96 unit-sphere rotation/face calculations;
rank ties and endpoints; URL-state bounds and round trip; and preservation of
all 4,095 histogram counts. Static HTML inspection found 48 unique IDs, no
missing explicit label targets and no missing local linked assets. The browser
fixture is 1,276,098 bytes. Actual desktop and mobile browser QA is separately
owned by the root integration workflow.
