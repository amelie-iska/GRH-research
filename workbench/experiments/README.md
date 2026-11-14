# Real measured-process component study

`run_realdata.py` uses actual pinned Mora-3 TokenGT and tropical modules as small
CPU graph encoders. It does not use or modify the user's trained/checkpointed
Mora-3 owner, native forest head or 24+2 campaign. All models here are freshly
trained, separately budgeted component references (16-wide, one layer, two heads).

Four measured/observation-derived series: NOAA CO2, SILSO monthly sunspot index,
NOAA ERSST Niño-3.4 anomaly, and public MIT-BIH record 100 MLII. The latter is
one-record temporal evaluation, not cross-patient clinical validation. Monthly
series stop at December 2025, using the current retrospective data vintage.
Keep the source files and acquisition hashes. SILSO raw rows are not published
in the dataset because their noncommercial terms must remain distinct.

Predict the next fixed-point first difference from eight strictly past values
represented as a directed path graph. Entire contexts remain in one chronological
60/20/20 span with an extra gap; scaling, quantile bins and retrieval memory use
training only. Count-model order/smoothing, neural checkpoint and retrieval
mixture are selected on validation only. Test results include every seed/run.

Report separately: categorical bits per symbol; exact signed-residual gamma
code lengths; ideal conditional bits per canonical original 4-byte int32 target;
and a two-part version charging model, quantizer metadata, retrieval bank and
initial value. This is not the original CSV byte stream and not an emitted
arithmetic-coded file. Actual zlib/lzma lengths are separate computable
code-length proxies, not measured Kolmogorov complexity. The public deterministic
lag graph has no per-record side information; arbitrary learned graphs would.

The analogy adapter retrieves training-span windows in the trained native
encoder's normalized embedding. It has a fixed verified lag-chain role/direction;
it is not the full native forest analogy module or evidence of causal transfer.
Exploratory block intervals and circular-offset diagnostics disclose their
stationarity limitations and do not claim discovery of an intentional message.

Example (in an existing PyTorch/NumPy environment):

```sh
CUDA_VISIBLE_DEVICES='' OMP_NUM_THREADS=2 python workbench/experiments/run_realdata.py \
  --data /absolute/raw-cache --output /absolute/results \
  --native /absolute/pinned/Mora-3/src/mora3/model --steps 80
```

No synthetic fixture is reported as a measured process. Unit tests may use
constructed arrays to verify protocol behavior; those are not scientific results.
