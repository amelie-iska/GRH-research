# Physical signals and known communication: pre-execution protocol

The new controls use actual GWOSC GW150914 32-second v2 strain from H1/L1 and
18 LibriSpeech test-clean utterances (six from each of speakers 6930, 1320, 5639).
These source objects were acquired and hashed before fitting. The source manifest
records exact member hashes and the streamed archive prefix, not a false hash of
an archive that was not fully downloaded. Both sources state CC BY 4.0.

Speech is re-split by speaker for this small cross-speaker experiment. This is not
the official LibriSpeech ASR benchmark, and no transcription accuracy is claimed.
It supplies known communicative provenance independently of any compression score.
Native PCM16 is retained at 16 kHz. The lossless codec emits a real byte packet,
including model, representatives, segment sizes, initial samples and termination;
an independent decoder must recover every integer before a BPB is accepted.

GW training/validation uses H1 times 0–8/8–12 seconds from GPS 1126259446, while
test uses L1 24–28 seconds. The cataloged event around 16.44 seconds is excluded
from all fitting. The predictor's fixed-point view uses 1e-24 strain units; its
quantization error is measured and reported. Codec replay is exact for that view,
not for original float64 or ASCII. A separate fixed-band/lag waveform diagnostic
uses the known event and off-source windows, and makes no discovery p-value.
Its retrospective zero-phase filter is never used as a predictive feature.

Native comparison reuses the pinned actual Mora-3 TokenGT/tropical modules,
width 16, one layer, seeds 17/29, 80 optimizer updates. Bins, normalization and
retrieval memory use training only. Validation selects checkpoints/count order/
smoothing/retrieval weight. Test outcomes, including errors, remain in results.
These runs are component experiments, not the full Mora-3 campaign.

The whole-stream emitted codec and sampled-window neural likelihood answer
separate questions. They have different exposures and coding conventions and
are not pooled into one misleading leaderboard. Counts, bytes, residuals,
side information and source-specific semantics accompany each result. The graph
is the public directed successor/lag relation, with no target-derived topology.

Known speech, structured gravitational strain and off-source instrument noise
are three distinct interpretive controls. Neither a good compressor nor a neural
score identifies intentional language in an uncharacterized physical process.
