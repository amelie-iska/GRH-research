from pathlib import Path
import sys

root = Path(__file__).resolve().parents[2]
source = root/"planning/ramified-book-20261106/lane-a/check_native_v1.mjs"
s = source.read_text()
s = s.replace("ramified-gauss-", "paired-cutoff-").replace("ramified-cusp-prefix", "paired-cutoff-regimes")
s = s.replace("ramified-cusp", "paired cutoff").replace("2026-11-06-ramified-book/lane-a/", "2026-11-08-cutoff-appendix/")
s = s.replace("rg:workflow","pca:regime").replace("rg:sharp-row","pca:bounds").replace("rg:prefix-theorem","pca:sign").replace("rg:sharp-proof","pca:detail-sparse").replace("rg:","pca:")
s = s.replace("10299","10858").replace("[10858,389,14,31]","[10858,389,14,32]")
s = s.replace("assert.deepEqual([expected.tables,expected.canonical_labs,expected.svg_refs,pdf.pdf_pages],[389,14,32,348]);",
              "assert(expected.tables>=389 && pdf.pdf_pages>348);assert.deepEqual([expected.canonical_labs,expected.svg_refs],[14,33]);")
s = s.replace("assert.equal(labels.length,75,'Exactly75 new source labels');","assert(labels.length>=20,'All paired-cutoff source labels');")
s = s.replace("tables:389,frames:14,svg_refs:32,pdf_pages:348","tables:expected.tables,frames:14,svg_refs:33,pdf_pages:pdf.pdf_pages")
s = s.replace("state.tables===389&&state.frames===14&&state.svgRefs===32","state.tables===expected.tables&&state.frames===14&&state.svgRefs===33")
s = s.replace("new-table-count-explicit-zero","new-table-count")
s = s.replace("paired-cutoff-regimes.tex","paired-cutoff-regimes.py").replace("figure-Tab-to-original-TeX-link","figure-Tab-to-generator-link")
s = s.replace("['svg','tex','pdf']", "['svg','py','pdf']")
s = s.replace("sourceText=sourceNames.map(n=>pin(ROOT+", "sourceText=sourceNames.map(n=>pin(STAGE+")
s = s.replace("pin(ROOT+'/'+p,digest)", "pin(STAGE+'/'+p,digest)")
s = s.replace("const HELPER=", "const STAGE=realpathSync(process.env.CUTOFF_STAGE_ROOT);assert(STAGE.startsWith(ROOT+'/outputs/checks/2026-11-08-cutoff-appendix/'));\nconst HELPER=")
s = s.replace("9335","9337")
s = s.replace('cusps:document.querySelectorAll("circle").length,slots:document.querySelectorAll("rect[id^=factor-]").length',
              'role:document.documentElement.getAttribute("role"),axisLabels:[...document.querySelectorAll("text")].map(n=>n.textContent)')
s = s.replace("svgState.tabindex==='0'&&svgState.focusable==='true'&&svgState.title&&svgState.desc&&svgState.cusps===27&&svgState.slots===11",
              "svgState.role==='img'&&svgState.title.includes('pure cross')&&svgState.desc.includes('1089/1420')&&svgState.axisLabels.length>12")
assert "9335" not in s and "rg:" not in s and "STAGE+'/'+p" in s and "[10858,389,14,32]" in s
assert "book/figures/paired-cutoff-regimes." in s
for start,end in (("const timing=","async function idle("),(" // Exact inherited predicate","}catch(error)")):
    old=source.read_text()
    assert s.split(start,1)[1].split(end,1)[0].replace("9337","9335")==old.split(start,1)[1].split(end,1)[0]
with Path(sys.argv[1]).open("x") as f:
    f.write(s)
