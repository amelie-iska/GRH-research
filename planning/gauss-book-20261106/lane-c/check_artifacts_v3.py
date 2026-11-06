#!/usr/bin/env python3
"""Read-only verification and an explicit manifest of the 18 Gauss-book candidates."""
from pathlib import Path
from datetime import datetime, timezone
from collections import Counter
import argparse, hashlib, html, json, re, subprocess
import xml.etree.ElementTree as ET

ROOT=Path("/home/iska/Documents/LaTeX-projects/GRH-from-Mac-20261104")
C=ROOT/"outputs/checks/2026-11-06-gauss-book"
NS="{http://www.w3.org/1998/Math/MathML}"
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def pin(p):return {"path":str(p.relative_to(ROOT)),"sha256":sha(p),"bytes":p.stat().st_size}
def load(p):return json.loads(p.read_text())
def write(p,o):
    p.parent.mkdir(parents=True,exist_ok=True)
    with p.open("x") as f:json.dump(o,f,indent=2,sort_keys=True);f.write("\n")
    return pin(p)
ap=argparse.ArgumentParser()
ap.add_argument("--output",required=True,type=Path)
args=ap.parse_args()
out=args.output.resolve()
assert out.is_relative_to(C) and not out.exists()
out.mkdir(parents=True)
try:
    expected={
      C/"root/integration-before-v1.json":"a8953053d4296a0c699611945a8f870b65967a8c63cacff48a5c3d06cd1036b5",
      C/"root/source-integration-v4.json":"7756286e637f0740dc694c41b98659d1b17615cc5c751a9e7eb5946e04f18e36",
      C/"review-integration-a/acceptance-v2.json":"a9207995e0b6e4b90ecd9bc38161005228eb0feab9b507b59e1ded1e824d8dd5",
      C/"builds/run-v3/aggregate.json":"bd9e7ef2011c581f22a56aa5b3c55716f80f3a3fb147b6aacbe92c9d22c19966",
      C/"native/run-v3/native-build-record.json":"57157b4a17fc805b6be75ba96d88bd9235ae28586433b15f24d25e221863d242",
      C/"pdf-visual/run-v2/review-v1.json":"9f14f621f3da310dfc3e248327f70393de521f624bfc21cd72575c5564950f5a",
      C/"lane-b/native-browser-v2/receipt.json":"cc16f3d146e8096465a09dcab5a1ba5e9949ea040e2ec6fea012630829e16bf4",
      C/"root/native-visual-v1.json":"c2d7d0f80efc42100cbbd51aef313ade4114199d9e6003aec7f38dba656acf17",
    }
    for p,h in expected.items():
        assert sha(p)==h,(p,"Gate changed")
        assert load(p)["passed"],p
    before=load(C/"root/integration-before-v1.json")
    integration=load(C/"root/source-integration-v4.json")
    aggregate=load(C/"builds/run-v3/aggregate.json")
    native=C/"native/run-v3"
    nrec=load(native/"native-build-record.json")
    visual=load(C/"pdf-visual/run-v2/review-v1.json")
    browser=load(C/"lane-b/native-browser-v2/receipt.json")
    native_visual=load(C/"root/native-visual-v1.json")
    assert browser["native_record_sha256"]==sha(native/"native-build-record.json")
    assert browser["checks"]==browser["checks_passed"]==40
    assert browser["harness_sha256"]=="b36b69af268ed47b1b548bc08344a1616fc153035254a7181d40a3d9f455dba6"
    assert all(browser["network"][k]==0 for k in ["fetch_errors","http_errors","pending","idle_timeouts","actual_departures"])
    assert (browser["network"]["quiet_ms"],browser["network"]["timeout_ms"])==(750,30000)
    assert all(browser["cleanup"].values())
    bdir=C/"lane-b/native-browser-v2"
    assert sha(bdir/"browser.json")==browser["browser_sha256"]
    assert sha(bdir/"network-navigation-timing.json")==browser["timing_sha256"]
    assert native_visual["native_record_sha256"]==browser["native_record_sha256"]
    assert native_visual["browser_receipt_sha256"]==sha(bdir/"receipt.json")
    for name,h in native_visual["inspected_screenshots"].items():assert sha(bdir/name)==h
    assert aggregate["source_integration_sha256"]==sha(C/"root/source-integration-v4.json")
    for row in integration["edits"]:
        assert sha(ROOT/row["path"])==row["after"],row["path"]
    assert sha(ROOT/"papers/gauss-tail-core.tex")==integration["source_sha256"]["core"]
    assert sha(ROOT/"papers/gauss-tail-details.tex")==integration["source_sha256"]["details"]
    assert sha(ROOT/"papers/gauss-tail-details.tex")=="7e048a780b60223f42b74411971df6616ea0f437fd699aac0d743c461e0c4314"
    source_pins={}
    build_records={}
    pdf_checks={}
    pairs=[]
    rows=aggregate["results"]
    assert set(rows)=={"book-pdf","focused-concise","focused-extended","notes-concise","notes-extended"}
    wanted_pages={"book-pdf":333,"focused-concise":81,"focused-extended":228,"notes-concise":39,"notes-extended":118}
    for key,row in rows.items():
        record=Path(row["record"]);pdf=Path(row["pdf"])
        assert record.is_relative_to(ROOT) and pdf.is_relative_to(ROOT)
        assert row["passed"] and row["returncode"]==0 and sha(record)==row["record_sha256"]
        rec=load(record);assert rec["passed"]
        assert sha(pdf)==row["pdf_sha256"]==rec["pdf_sha256"] and pdf.read_bytes().startswith(b"%PDF")
        info=subprocess.check_output(["pdfinfo",str(pdf)],text=True)
        pages=int(re.search(r"^Pages:\s+(\d+)",info,re.M)[1])
        assert pages==wanted_pages[key]==row["pages"]==rec.get("pdf_pages",rec.get("pages"))
        log=pdf.with_suffix(".log")
        bad=[l for l in log.read_text().splitlines() if re.search(r"Overfull|undefined references|Citation .* undefined|Reference .* undefined|multiply defined|multiply-defined|Missing character:|^!",l)]
        assert not bad,(key,bad[:4])
        for name,h in rec["source_sha256"].items():
            p=(ROOT/name).resolve();assert p.is_relative_to(ROOT) and sha(p)==h,(key,name,"Source changed")
            source_pins[name]=h
        for item in rec.get("figure_records",[]):
            if item.get("exists",True) is False:
                # The article builder explicitly records inactive IfFileExists candidates.
                # Keep absence exact; any active missing include is rejected by the strict build.
                assert not (ROOT/item["path"]).exists() and "sha256" not in item
                assert "inactive IfFileExists branch" in item["scope"]
            else:assert sha(ROOT/item["path"])==item["sha256"],(key,item["path"])
        if "log_sha256" in rec:assert sha(log)==rec["log_sha256"]
        if "expanded_source_sha256" in rec:
            expanded=pdf.with_name(pdf.stem+".expanded.tex")
            assert sha(expanded)==rec["expanded_source_sha256"]
        if "original_expanded_source_sha256" in rec:
            assert sha(record.parent/"source-expansion-before-diagram-replacement.tex")==rec["original_expanded_source_sha256"]
        build_records[str(record.relative_to(ROOT))]=sha(record)
        pdf_checks[key]={"pages":pages,"pdf":pin(pdf),"log":pin(log),"source_pin_count":len(rec["source_sha256"]),"strict_final_log_passed":True}
        if key=="book-pdf":
            for ext in ["pdf","log","toc"]:
                pairs.append((record.parent/("main."+ext),ROOT/"outputs/book"/("surface-orders-book."+ext)))
        else:
            targetdir=ROOT/("outputs/papers" if key.startswith("focused") else "outputs/papers/validated-oracle-20261104")
            pairs.extend([(pdf,targetdir/pdf.name),(log,targetdir/log.name)])
    for name,h in aggregate["source_guard_sha256"].items():assert sha(ROOT/name)==h,name
    assert nrec["PDF_build_record_sha256"]==rows["book-pdf"]["record_sha256"]
    assert browser["pdf_record_sha256"]==rows["book-pdf"]["record_sha256"]
    for name,h in nrec["source_sha256"].items():assert sha(ROOT/name)==h,name
    for row in visual["representative_visuals_byte_identical_to_inspected_v1"].values():
        assert row["passed"] and row["after"]==row["prior"] and row["pdf_sha256"] in {x["pdf_sha256"] for x in rows.values()}
    # Candidate copied sources and all three figure assets must be the current source bytes.
    for name in ["gauss-tail-core.tex","gauss-tail-figure.tex","gauss-tail-details.tex"]:
        assert (native/"book/sources"/name).read_bytes()==(ROOT/"book/chapters"/name).read_bytes()
    for ext in ["tex","pdf","svg"]:
        name="gauss-tail-partition."+ext
        assert (native/"book/figures"/name).read_bytes()==(ROOT/"book/figures"/name).read_bytes()
    baseline_path=ROOT/"web/book/main.html";candidate_path=native/"book/main.html"
    assert sha(baseline_path)==before["source_and_live_before"]["web/book/main.html"]["sha256"]==nrec["old_HTML_sha256"]
    assert sha(candidate_path)==nrec["new_HTML_sha256"]=="5a54223737c1b35f7fcaa7371fd3d04c0e233e9bd3e8241dad0262bce73f560d"
    old=baseline_path.read_text();new=candidate_path.read_text()
    assert new.count('<section class="new-reviewed-chapters" id="gauss-tail-section">')==1
    section=re.search(r'<section class="new-reviewed-chapters" id="gauss-tail-section">.*?</section>\n',new,re.S)
    assert section and "<section" not in section[0][len('<section'):]
    restored=new[:section.start()]+new[section.end():]
    toc=re.findall(r'<br\s*/><span class="sectionToc"><a href="#gtl:core">[^<]+</a></span>',restored)
    assert len(toc)==1
    restored=restored.replace(toc[0],"",1)
    assert restored==old,"An old HTML byte changed"
    assert new.count("November 6, 2026")==old.count("November 6, 2026")==1
    old_math=re.findall(r"<math\b[^>]*>.*?</math>",old,re.S)
    new_math=re.findall(r"<math\b[^>]*>.*?</math>",new,re.S)
    assert len(old_math)==9810 and len(new_math)==10299
    pos=0
    for value in old_math:
        while pos<len(new_math) and new_math[pos]!=value:pos+=1
        assert pos<len(new_math),"Old literal MathML/order changed"
        pos+=1
    old_tables=re.findall(r"<table\b[^>]*>.*?</table>",old,re.S)
    assert len(old_tables)==389 and re.findall(r"<table\b[^>]*>.*?</table>",new,re.S)==old_tables
    old_frames=re.findall(r"<iframe\b[^>]*>.*?</iframe>",old,re.S)
    assert len(old_frames)==14 and re.findall(r"<iframe\b[^>]*>.*?</iframe>",new,re.S)==old_frames
    svg_old=re.findall(r'(?:src|data)="([^"]+\.svg)"',old)
    svg_new=re.findall(r'(?:src|data)="([^"]+\.svg)"',new)
    assert len(svg_old)==30 and svg_new==svg_old+["figures/gauss-tail-partition.svg"]
    before_assets=before["old_book_assets_sha256"];assert len(before_assets)==86
    for name,h in before_assets.items():
        assert sha(ROOT/name)==h,(name,"Old live asset changed")
        if name!="web/book/main.html":
            assert sha(native/"book"/name.removeprefix("web/book/"))==h,(name,"Old candidate asset changed")
    allowed_native={"main.html","sources/gauss-tail-core.tex","sources/gauss-tail-figure.tex","sources/gauss-tail-details.tex",
                    "figures/gauss-tail-partition.tex","figures/gauss-tail-partition.pdf","figures/gauss-tail-partition.svg"}
    changed_native=set()
    for p in (native/"book").rglob("*"):
        if not p.is_file():continue
        rel=p.relative_to(native/"book");target=ROOT/"web/book"/rel
        if not target.exists() or sha(p)!=sha(target):
            changed_native.add(str(rel));pairs.append((p,target))
    assert changed_native==allowed_native
    tree=ET.fromstring(new);fragment=ET.fromstring("<div>"+section[0]+"</div>")
    ids=[e.attrib["id"] for e in tree.iter() if "id" in e.attrib]
    new_ids=[e.attrib["id"] for e in fragment.iter() if "id" in e.attrib]
    old_ids=set(re.findall(r'\bid="([^"]+)"',old))
    assert len(new_ids)==len(set(new_ids)) and not set(new_ids)&old_ids,"New id duplicate/collision"
    source_labels=[]
    for name in ["gauss-tail-core.tex","gauss-tail-figure.tex","gauss-tail-details.tex"]:
        source_labels+=re.findall(r"\\label\{([^}]+)\}",(ROOT/"book/chapters"/name).read_text())
    assert len(source_labels)==len(set(source_labels))==86 and all(ids.count(x)==1 for x in source_labels)
    math_nodes=list(fragment.iter(NS+"math"));assert len(math_nodes)==489
    for e in fragment.iter():
        tag=e.tag.rsplit("}",1)[-1]
        if tag in {"msub","msup","munder","mover"}:assert len(e)==2,(tag,"Wrong arity")
        if tag in {"msubsup","munderover"}:assert len(e)==3,(tag,"Wrong arity")
        if tag=="a" and e.attrib.get("href","").startswith("#"):
            assert html.unescape(e.attrib["href"][1:]) in ids
    ast=load(native/"supplement.ast.json");ast_math=[]
    def walk(x):
        if isinstance(x,dict):
            assert x.get("t") not in {"RawBlock","RawInline"}
            if x.get("t")=="Math":ast_math.append(x["c"][1].strip())
            for v in x.values():walk(v)
        elif isinstance(x,list):
            for v in x:walk(v)
    walk(ast)
    annotations=["".join(e.find(".//"+NS+"annotation").itertext()).strip() for e in math_nodes]
    assert annotations==ast_math
    figure=[e for e in fragment.iter("img") if e.attrib.get("src")=="figures/gauss-tail-partition.svg"]
    assert len(figure)==1 and figure[0].attrib.get("alt")
    assert "filter:none!important" in figure[0].attrib.get("style","") and "background-color:#fff" in figure[0].attrib.get("style","")
    assert any(e.attrib.get("class")=="reader-figure-scroll" and e.attrib.get("tabindex")=="0" for e in fragment.iter())
    assert len(pairs)==18 and len({str(a) for a,b in pairs})==18 and len({str(b) for a,b in pairs})==18
    artifact_sha={str(a.relative_to(ROOT)):sha(a) for a,b in pairs}
    target_sha={}
    for source,target in pairs:
        name=str(target.relative_to(ROOT));current=sha(target) if target.exists() else None
        if current is None:
            assert name.startswith(("web/book/sources/gauss-tail-","web/book/figures/gauss-tail-partition."))
        else:
            assert current==before["promoted_artifacts_before"][name],(name,"Old promoted target changed")
        assert not target.with_name(target.name+".gauss-book-pending").exists(),target
        target_sha[name]=current
    manifest={
      "schema":"gauss-book-18-candidate-manifest-v1","created_utc":datetime.now(timezone.utc).isoformat(),
      "artifact_sha256":artifact_sha,"target_before_sha256":target_sha,
      "candidate_to_target":{str(a.relative_to(ROOT)):str(b.relative_to(ROOT)) for a,b in pairs},
      "artifact_count":18,"existing_targets":sum(x is not None for x in target_sha.values()),
      "new_targets":sum(x is None for x in target_sha.values()),"pdf_checks":pdf_checks,
      "build_records_sha256":build_records,
      "native_record":pin(native/"native-build-record.json"),
      "new_edition":{"book_pages":333,"focused_pages":[81,228],"notes_pages":[39,118],
                     "MathML":10299,"old_literal_MathML_preserved":9810,"tables":389,
                     "canonical_iframes":14,"SVG_refs":31},
      "source_closure_sha256":source_pins,"source_pin_instances_checked":sum(x["source_pin_count"] for x in pdf_checks.values()),
      "all_candidates_current":True,"no_gauss_book_pending_file":True,
      "live_targets_mutated":False,
    }
    manifest_pin=write(out/"artifact-manifest-v1.json",manifest)
    # Check the guarded inputs and every candidate/live target again before freezing the gate.
    for p,h in expected.items():assert sha(p)==h
    for source,target in pairs:
        assert sha(source)==artifact_sha[str(source.relative_to(ROOT))]
        assert (sha(target) if target.exists() else None)==target_sha[str(target.relative_to(ROOT))]
    acceptance={
      "schema":"gauss-book-artifact-source-native-acceptance-c-v1",
      "passed":True,"reviewer":"/root/quadratic_pivot_lab","created_utc":datetime.now(timezone.utc).isoformat(),
      "scope":"Read-only exact 18-artifact/source/native acceptance; not a browser, publication or promotion authorization.",
      "artifact_sha256":artifact_sha,"target_before_sha256":target_sha,"manifest":manifest_pin,
      "candidate_to_target":manifest["candidate_to_target"],
      "input_gates_sha256":{str(p.relative_to(ROOT)):h for p,h in expected.items()},
      "edition":manifest["new_edition"],"strict_new_build_logs_and_actual_PDF_pages_checked":True,
      "all_five_build_source_pins_current":True,"concise_v2_reuse_checked_against_actual_inputs":True,
      "current_A_math_layout_lineage_bound":True,"current_root_PDF_visual_gate_bound":True,
      "old_live_and_candidate_85_nonHTML_assets_exact":True,
      "old_HTML_restored_exact_after_only_section_and_ToC_removal":True,
      "old_9810_literal_MathML_order_exact":True,"old_389_literal_tables_exact":True,
      "old_14_literal_iframes_exact":True,"old_30_SVG_reference_order_and_assets_exact":True,
      "all_86_new_labels_present_once":True,"new_MathML_arity_and_AST_source_order_valid":True,
      "new_figure_only_filter_override_and_focus_region":True,
      "focused_independent_B_browser_acceptance_bound":True,
      "root_native_visual_gate_bound":True,
      "browser_performed_by_this_reviewer":False,
      "whole_release_audit_performed":False,"promotion_authorized":False,
      "new_scientific_controls_or_builds_run":False,"new_Lean_or_GRH":False,
      "live_source_canonical_or_index_mutation":False,"checker_sha256":sha(Path(__file__)),
    }
    receipt=write(out/"acceptance-v1.json",acceptance)
    print(json.dumps({"passed":True,"manifest":manifest_pin,"acceptance":receipt,
                      "artifact_count":18,"source_pin_instances":manifest["source_pin_instances_checked"],
                      "edition":manifest["new_edition"]},indent=2))
except Exception as e:
    write(out/"failure-v1.json",{"passed":False,"error_type":type(e).__name__,"error":str(e),
          "created_utc":datetime.now(timezone.utc).isoformat(),"checker_sha256":sha(Path(__file__))})
    raise
