# Coherent-band auxiliary matrix display

This is a replay of saved source-bound controls, not training or a new scientific calculation. The source is `outputs/checks/2026-11-06-coherent-band/root/finite-schur-controls-v1/controls-v1.json`, SHA256 `fd5b33de0c54632b46d0515f5a3f67c7b91ceb896d09bd5f0303256f9fe91a04`. It contains1511 passed numerical consistency assertions at55-digit mpmath working precision and three14x29 auxiliary matrices at D121/289/529, U11/17/23. These are actual good-ideal indices, not the complete original physical-row family or interval enclosures. No browser SVD, Perron integration or learning occurs.

Runtime assets are ONLY `web/coherent-band.html` (embedded CSS/module) and `web/data/coherent-band-schur-v1.json`. Source CSS/module/template live here; the existing `scripts/theme_assets.py` installs the shared palette/controller. The payload SHA256 is `e540ac344bbf3d4d07d1ac9fcb8c5cd336a6195c7130a602567242c33bc73171`.

The1218 saved positions include786 SOURCE-MASKED zeros: the support is both `(d,a)=1` and `Nd*Na<=X=2D`. A product-cutoff zero must not be called an evaluated character phase. At masked positions the source did not evaluate AU,AT,W; the matrix stages remain0. Phase6=0 is the nonzero cubic value1. There are42 supported positions with an inert factor. Its prime-ideal norm p^2 still represents one squarefree ideal factor.

The source canonical generators are kept exactly, including its nontrivial unit representative. They are not silently changed to primary generators. Prime factor generators and distinct split embeddings remain explicit. Integer AU/cubic phase strings are exact; saved AT and W complex coordinates and operator norms are55-digit numerical outputs. The profile is the fixed C2 function `((x-1)*(2-x))^3*exp(i*x/7)` on1<x<2 and0 elsewhere. Browser complex coordinates are double display projections.

## Reproduce into fresh named outputs

Run from the Linux project root using its EXISTING Python/Node/TeX/Poppler tools. These commands do not overwrite the saved scientific source or production assets. Choose fresh output names; all writers refuse an existing receipt.

```sh
python3 examples/coherent_band/extract_payload_v1.py --output outputs/checks/2026-11-06-coherent-book/reproduce/payload.json --receipt outputs/checks/2026-11-06-coherent-book/reproduce/extraction.json
python3 examples/coherent_band/build_lab_v1.py --output outputs/checks/2026-11-06-coherent-book/reproduce/coherent-band.html --receipt outputs/checks/2026-11-06-coherent-book/reproduce/page.json
python3 examples/coherent_band/check_payload_v1.py --output outputs/checks/2026-11-06-coherent-book/reproduce/payload-check.json
node examples/coherent_band/check_runtime_v1.mjs outputs/checks/2026-11-06-coherent-book/reproduce/runtime-check.json
python3 examples/coherent_band/build_workflow_v4.py --work outputs/checks/2026-11-06-coherent-book/reproduce/workflow
```

Extraction invokes only the pinned pure ideal METADATA enumerator with bytecode disabled; it never executes `check_finite_schur_v1.py`, numerical SVD or Perron/Ei controls. The display checker compares EVERY saved numerical string to source, verifies masks/factors and profile arguments, and checks conversion tolerance. The JS check covers all3654 stage values. Re-extracted payload bytes should match the frozen web payload. The page assembler reads that frozen payload and source module; it verifies the embedded payload SHA.

The FINAL workflow producer is `build_workflow_v4.py`. Its default fresh asset directory is `<work>/assets/`, using plain LaTeX picture/xcolor and existing pdflatex/Poppler; no TikZ install is required. It regenerates SVG/TeX deterministically from the same D121 case and numerical norm strings. PDF metadata may differ across builds; rendered content is source-bound. The current production figure is `book/figures/coherent-band-workflow.{svg,tex,pdf}` in a readable2+1 arrangement. Every source label is at least12pt, exceeding10pt when printed at6in width. Earlier failed/mistimed layouts and their logs remain in the local QA history; v1-v3 producers are historical, not the final reproduction command.

## Browser checks

`planning/coherent-book-20261106/lane-c/check_lab_v1.mjs` exports `runLab(b,base,out)` for the existing remote Firefox BiDi helper. It never connects/closes a session, changes navigation or filters errors. Root must supply its unchanged GLOBAL WS750ms-quiet/30s-idle guard and explicit loopback candidate URL; do not test source8765 or start a competing9335 session. New checks cover all source strings, all3case/3stage rendered matrices, exact masks/inert/finite-Perron states, native keyboard/ranges,54 layouts at320/390/1440 in both palettes, and native newURL/Request fetching. Root owns combined book/browser/visual QA and future publication gates.

All source data, old assets and outputs remain unchanged. The current full signed13/12/global9/8, unequal-norm coherent target, principal/short assembly and GRH/determinant obligations are not improved by this display.
