from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import re
import subprocess
import sys
import unicodedata

o=Path("outputs/checks/2026-11-08-cutoff-appendix")
q=Path("planning/cutoff-appendix-20261108")
s=o/"stage-v2/inputs"
b=s/"outputs/cutoff"
prev=Path("outputs/checks/2026-11-08-pure-intermediate")
recon=Path("outputs/checks/2026-11-08-matched-poisson")
sys.path.insert(0,str(recon))
from reconcile_source_index_v1 import inspect

def read(path):
    return Path(path).read_bytes()

def sha(path):
    return hashlib.sha256(read(path)).hexdigest()

def ref(path):
    return {"path":str(path),"bytes":len(read(path)),"sha256":sha(path)}

def get(path):
    return json.loads(read(path))

def save(path,obj):
    with Path(path).open("x") as f:
        json.dump(obj,f,indent=2)
        f.write("\n")

def normalize(text):
    return "".join(c.lower() for c in unicodedata.normalize("NFKD",text) if c.isascii() and c.isalnum())

source_stage=s.parent/"source-stage-v1.json"
record=get(source_stage)
assert record["passed"] and len(record["source_input_sha256"])==516
wrappers={x["path"]:x for x in record["wrappers"]}
assert len(wrappers)==5
for path,digest in record["source_input_sha256"].items():
    assert sha(path)==digest
    assert sha(s/path)==(wrappers[path]["stage_sha256"] if path in wrappers else digest)
for path,item in record["additions"].items():
    assert sha(s/path)==sha(item["source"])==item["sha256"]
assert len(record["additions"])==8
assert sha(s/"native-baseline.json")==record["native_baseline_sha256"]
assert sha(q/"REVIEW-v1.json")=="e0eec6caca6c559d22a69e0070a7fc1008ed6490ae3c6934b5cac390903ca64b"
review=get(q/"REVIEW-v1.json")
assert review["passed"] and all(ref(v["path"])==v for v in review["reviewed"].values())
assert all(ref(v["path"])==v for v in review["comparison_sources"])
for path,digest in get(o/"WIDE_REVIEW-v1.json")["reviewed"].items():
    assert sha(path)==digest
controls=("wide-correction-controls-v2.json","wide-correction-addendum-controls-v1.json")
for name in controls:
    v=get(o/name)
    assert v["status"]=="pass"
    assert all(sha(path)==digest for path,digest in v["source_sha256"].items())

old_pins=get(prev/"SOURCE_PINS-v1.json")["inputs"]
assert len(old_pins)==311 and all(ref(x["path"])==x for x in old_pins)
paths=set(x["path"] for x in old_pins)
paths.update(("planning/pure-intermediate-20261108/HANDOFF-v1.md",prev/"SOURCE_PINS-v1.json",prev/"REVIEW-v1.json",
    "planning/asymmetric-cutoff-20261108/HANDOFF-v1.md","planning/ramified-book-20261106/root/build_book_pdf_v1.py",
    "planning/ramified-book-20261106/root/render_native_v1.py",
    "planning/ramified-book-20261106/lane-a/check_native_v1.mjs"))
paths.update(x["path"] for x in review["comparison_sources"])
paths.update(x["path"] for x in review["reviewed"].values())
paths.update(str(x) for x in sorted(q.iterdir()) if x.is_file())
paths.update(str(o/n) for n in (
    "bind_stage_v1.py","bind_stage_v2.py","WIDE_REVIEW-v1.json","PDF-MARKER-v1.json",
    "check_wide_correction_v1.py","check_wide_correction_v2.py",*controls))
pins=[ref(p) for p in sorted(set(str(p) for p in paths))]
assert len({x["path"] for x in pins})==len(pins)

old_state=get(recon/"INDEX_RECONCILIATION-v1.json")
assert inspect()=={k:v for k,v in old_state.items() if k!="scope"}
protected=get("outputs/checks/2026-11-06-ramified-release/root/source-state-before-v1.json")["scientific_artifacts"]
assert len(protected)==18 and all(sha(path)==h for path,h in protected.items())
assert sha("examples/quantum/requirements-cpu.lock")=="bbda0be638105efc4f453c239c925d9e77171898fa84866146a6f55031ca7b5a"
assert subprocess.check_output(["git","rev-parse","origin/main"],text=True).strip()=="aeb7705c8bc5b7662a44916ea5039fb2dae7266d"

pdfs={}
entries=(("book-pdf","main",360),("focused-concise","resolutions-concise",88),
         ("focused-extended","resolutions-extended",253),("notes-concise","validated-oracle-concise",45),
         ("notes-extended","validated-oracle-extended",142))
for folder,stem,pages in entries:
    path=b/folder
    manifest=path/"build-record.json"
    v=get(manifest)
    pdf=path/(stem+".pdf")
    assert v["passed"] and v.get("pdf_pages",v.get("pages"))==pages and v["pdf_sha256"]==sha(pdf)
    assert not v["production_promoted"]
    part="book/chapters/" if folder=="book-pdf" else "papers/"
    assert v["source_sha256"][part+"paired-cutoff-core.tex"]==sha(q/"paired-cutoff-core-v3.tex")
    extended=folder=="book-pdf" or folder.endswith("-extended")
    if extended:
        assert v["source_sha256"][part+"paired-cutoff-details.tex"]==sha(q/"paired-cutoff-details-v2.tex")
    extract=normalize(subprocess.check_output(["pdftotext",str(pdf),"-"],text=True))
    assert normalize("Paired cutoffs, exact divisor signs and proved regimes") in extract
    if extended:
        assert normalize("Sharp insertion and ordered cutoff estimates") in extract
    log=(path/(stem+".log")).read_text()
    assert not re.search(r"Overfull|undefined references|Citation .* undefined|Reference .* undefined|multiply defined|multiply-defined|Missing character:|^!",log,re.M)
    pdfs[folder]={"pages":pages,"artifact":ref(pdf),"build":ref(manifest)}
native=b/"native/native-build-record.json"
n=get(native)
assert n["passed"] and n["old_HTML_restored_exactly"] and n["old_math_byte_identical"] and not n["production_promoted"]
assert [n[k] for k in ("chapter_count","math_nodes","old_literal_math_subtrees","tables","canonical_labs","svg_refs")]==[40,11505,10858,389,14,33]
assert not (n["new_Lean_declarations"] or n["raw_TeX_nodes"] or n["conversion_warnings"])
assert n["new_HTML_sha256"]==sha(b/"native/book/main.html")
assert n["PDF_build_record_sha256"]==pdfs["book-pdf"]["build"]["sha256"]
browser=o/"browser-v1/receipt.json"
br=get(browser)
assert br["passed"] and br["checks"]==br["checks_passed"]==41
assert br["native_record_sha256"]==sha(native)
assert br["pdf_record_sha256"]==n["PDF_build_record_sha256"]
assert br["network"]["actual_departures"]==2 and br["network"]["protocol_entries"]==199
assert all(br["network"][k]==0 for k in ("fetch_errors","http_errors","pending","idle_timeouts"))
assert get(o/"PROCESS-EXIT-v1.json")["owned_processes_waited"]
assert not subprocess.check_output(["ss","-H","-ltn","( sport = :9337 )"],text=True).strip()
assert sha(b/"native/book/figures/paired-cutoff-regimes.svg")==sha(q/"figure/paired-cutoff-regimes.svg")
assert sha(b/"native/book/figures/paired-cutoff-regimes.pdf")==sha(q/"figure/paired-cutoff-regimes.pdf")
assert sha(b/"native/book/figures/paired-cutoff-regimes.py")==sha(q/"figure/generate_regime_v3.py")
assert all("59.88504pt" in (o/"stage-v1/inputs/outputs/cutoff"/name).read_text() for name in ("book-build.txt","focused-extended.txt","notes-extended.txt"))
visuals=list(sorted((o/"visual-v2").glob("*.jpg")))
assert len(visuals)==7
save(o/"SOURCE_PINS-v1.json",{"schema":"cutoff-appendix-source-pins-v1","inherited_verified":311,"inputs":pins})
save(o/"STAGE_ACCEPTED-v1.json",{
    "passed":True,"utc":datetime.now(timezone.utc).isoformat(),"status":"VERIFIED_STAGING_ONLY",
    "source_stage":ref(source_stage),"source_pins":ref(o/"SOURCE_PINS-v1.json"),"pin_count":len(pins),
    "appendix_review":ref(q/"REVIEW-v1.json"),"research_review":ref(o/"WIDE_REVIEW-v1.json"),
    "research_controls":[ref(o/name) for name in controls],"pdfs":pdfs,
    "native_build":ref(native),"native_book":ref(b/"native/book/main.html"),"browser":ref(browser),
    "visual_evidence":[ref(p) for p in visuals],
    "visual_review":"Selected PDF pages and native light layouts inspected, with the full mobile figure reachable through focused horizontal scrolling.",
    "page_counts":[360,88,253,45,142],"mathml":11505,"literal_prior_mathml":10858,"chapters":40,"tables":389,"canonical_iframes":14,"svg_refs":33,
    "failed_candidates":"Extended PDF v1 59.88504pt overfull paragraph resolved by aligned displays. First wide-check candidate syntax error corrected. PDF visual lookup needed physical pagination offset. All candidates preserved.",
    "notes":"Three inherited malformed munder nodes are outside the appendix. Older TeX underfull and package notices and source-matched cached diagram constraints persist. Wide correction advances are outside the staged appendix.",
    "production_promoted":False,"published":False,"new_Lean_declarations":0,"project_complete":False,"research_complete":False,
    "protected_HEAD_states":16,"protected_frozen_release_index_states":15,"canonical_artifacts_verified":18,
})
print(len(pins),sha(o/"SOURCE_PINS-v1.json"),sha(o/"STAGE_ACCEPTED-v1.json"))
