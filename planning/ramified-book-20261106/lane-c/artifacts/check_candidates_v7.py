#!/usr/bin/env python3
"""Independent read-only PDF/native/source preservation gate; candidates only.

The immutable config pins every independently supplied gate and expected edition.
No build, browser, science control, promotion, publication, source or Git mutation.
"""
from pathlib import Path
from datetime import datetime, timezone
from collections import Counter
import argparse, hashlib, html, json, re, subprocess
import xml.etree.ElementTree as ET
ROOT=Path("/home/iska/Documents/LaTeX-projects/GRH-from-Mac-20261104")
OWN=ROOT/"outputs/checks/2026-11-06-ramified-book/lane-c/artifacts"
NS="{http://www.w3.org/1998/Math/MathML}"
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def load(p):return json.loads(p.read_text())
def rel(p):return str(p.relative_to(ROOT))
def pin(p):return dict(path=rel(p),sha256=sha(p),bytes=p.stat().st_size)
def exclusive(p,obj):
 with p.open("x") as f:json.dump(obj,f,indent=2,sort_keys=True);f.write("\n")
 return pin(p)
def repo(name):
 p=(ROOT/name).resolve();assert p.is_relative_to(ROOT),name
 return p
def require(test,message):
 if not test:raise AssertionError(message)
ap=argparse.ArgumentParser();ap.add_argument("--config",type=Path,required=True);ap.add_argument("--output",type=Path,required=True)
a=ap.parse_args();config=a.config.resolve();out=a.output.resolve()
assert config.is_relative_to(OWN) and out.is_relative_to(OWN) and not out.exists()
out.mkdir(parents=True)
cfg=load(config);config_sha=sha(config)
try:
 gates=cfg["required_json_sha256"]
 for name,digest in gates.items():require(sha(repo(name))==digest,("Immutable input changed",name))
 for name in cfg["required_passed_json"]:require(load(repo(name))["passed"] is True,("Input gate not passed",name))
 before=load(repo(cfg["before"]));protected=load(repo(cfg["protected"]))
 integration=load(repo(cfg["integration"]));aggregate=load(repo(cfg["aggregate"]))
 native=repo(cfg["native_dir"]);nrec=load(native/"native-build-record.json")
 figure=load(repo(cfg["figure_gate"]))
 require((before["old_math"],before["old_tables"],before["old_labs"],before["old_svg_refs"])==(10299,389,14,31),"Wrong pre-integration edition")
 require(len(before["old_book_assets_sha256"])==92,"Wrong old book asset baseline")
 require(any(x["path"]==cfg["integration"] and x["sha256"]==sha(repo(cfg["integration"])) for x in aggregate["dependencies"]),"Build source integration mismatch")
 for row in aggregate["dependencies"]:require(sha(repo(row["path"]))==row["sha256"],("Aggregate dependency drift",row["path"]))
 for row in aggregate["generated_shared_chapter_byte_checks"]:
  paper=repo(row["paper"]["path"]);chapter=repo(row["chapter"]["path"])
  require(sha(paper)==row["paper"]["sha256"] and sha(chapter)==row["chapter"]["sha256"],"Shared source binding")
  require(chapter.read_bytes()==row["exact_prefix_UTF8"].encode()+paper.read_bytes(),"Shared chapter not the reviewed paper bytes")
 require(aggregate["production_promoted"] is False and nrec["production_promoted"] is False,"Only unpromoted staging may be accepted")
 require(nrec["chapter_count"]==40 and nrec["new_chapters"]==0 and nrec["canonical_labs"]==14 and nrec["new_Lean_declarations"]==0,"Wrong continuation/tool/Lean scope")
 for row in integration["edits"]:require(sha(repo(row["path"]))==row["after"],("Integrated source drift",row["path"]))
 require(aggregate["rebuild_performed"] is False and aggregate["original_runner_and_results_preserved"] is True,"Recovery must not rebuild or rewrite old evidence")
 source_pins={};pdf_results={};pairs=[]
 rows=aggregate["results"]
 require(set(rows)=={"book-pdf","focused-concise","focused-extended","notes-concise","notes-extended"},"Not all five editions")
 for key,row in rows.items():
  recpath=repo(row["record"]["path"]);pdf=repo(row["PDF"]["path"])
  require(recpath.is_relative_to(ROOT) and pdf.is_relative_to(ROOT),"External candidate path")
  require(row["passed"] and sha(recpath)==row["record"]["sha256"],("Build record not passed",key))
  require(row["historical_command"]["executed_by_original_runner"] is True and row["historical_command"]["executed_by_this_recovery"] is False,"Original jobs only; no rebuild")
  require(sha(repo(row["final_log"]["path"]))==row["final_log"]["sha256"],("Aggregate final log binding",key))
  rec=load(recpath);require(rec["passed"],key)
  require(pdf.read_bytes().startswith(b"%PDF") and sha(pdf)==row["PDF"]["sha256"]==rec["pdf_sha256"],("PDF binding",key))
  info=subprocess.check_output(["pdfinfo",str(pdf)],text=True)
  pages=int(re.search(r"^Pages:\s+(\d+)",info,re.M)[1])
  require(pages==cfg["expected_pages"][key]==row["pages"]==rec.get("pdf_pages",rec.get("pages")),("PDF actual pages",key,pages))
  log=pdf.with_suffix(".log");logtext=log.read_text()
  bad=[line for line in logtext.splitlines() if re.search(r"Overfull|undefined references|Citation .* undefined|Reference .* undefined|multiply defined|multiply-defined|Missing character:|^!",line)]
  require(not bad,("Strict build log",key,bad[:4]))
  for name,digest in rec["source_sha256"].items():
   require(sha(repo(name))==digest,("PDF source drift",key,name));source_pins[name]=digest
  newprefix="book/chapters/" if key=="book-pdf" else "papers/"
  require(newprefix+"ramified-gauss-core.tex" in rec["source_sha256"],("New core missing",key))
  if not key.endswith("concise"):require(newprefix+"ramified-gauss-details.tex" in rec["source_sha256"],("New complete proof missing",key))
  for item in rec.get("figure_records",[]):
   if item.get("exists",True) is False:
    require(not repo(item["path"]).exists() and "sha256" not in item and "inactive IfFileExists branch" in item["scope"],("Unreviewed missing figure",key,item))
   else:require(sha(repo(item["path"]))==item["sha256"],("PDF figure drift",key,item["path"]))
  if "log_sha256" in rec:require(sha(log)==rec["log_sha256"],("Log binding",key))
  if "expanded_source_sha256" in rec:require(sha(pdf.with_name(pdf.stem+".expanded.tex"))==rec["expanded_source_sha256"],("Expanded source binding",key))
  if "original_expanded_source_sha256" in rec:require(sha(recpath.parent/"source-expansion-before-diagram-replacement.tex")==rec["original_expanded_source_sha256"],("Original expansion binding",key))
  pdf_results[key]=dict(pdf=pin(pdf),log=pin(log),record=pin(recpath),pages=pages,source_pin_count=len(rec["source_sha256"]),strict_log_passed=True)
  if key=="book-pdf":
   for ext in ["pdf","log","toc"]:pairs.append((recpath.parent/("main."+ext),ROOT/"outputs/book"/("surface-orders-book."+ext)))
  else:
   target=ROOT/("outputs/papers" if key.startswith("focused") else "outputs/papers/validated-oracle-20261104")
   pairs.extend([(pdf,target/pdf.name),(log,target/log.name)])
 require(nrec["PDF_build_record_sha256"]==rows["book-pdf"]["record"]["sha256"],"PDF/native actual source binding")
 require(sha(repo(rows["book-pdf"]["record"]["path"]).parent/"main.aux")==nrec["pdf_aux_sha256"],"Actual PDF aux/native numbering binding")
 for name,digest in nrec["source_sha256"].items():require(sha(repo(name))==digest,("Native source drift",name))
 browserpath=repo(cfg["browser_receipt"]);browser=load(browserpath)
 require(browser["passed"] and browser["checks"]==browser["checks_passed"]==41,"Focused browser not all41 passed")
 require(browser["harness_sha256"]=="e71175289a066242693ad29f759ffaa537089c0d13c8a0aa8be69ab6493a1f70","Unreviewed browser protocol")
 require(browser["native_record_sha256"]==sha(native/"native-build-record.json") and browser["pdf_record_sha256"]==rows["book-pdf"]["record"]["sha256"],"Browser source/native/PDF binding")
 net=browser["network"];require(all(net[k]==0 for k in ["fetch_errors","http_errors","pending","idle_timeouts"]),"Browser network failure")
 require((net["quiet_ms"],net["timeout_ms"],net["initial_markers"],net["actual_departures"])==(750,30000,1,2),"Browser strict idle/navigation scope")
 require(all(browser["cleanup"].values()),"Owned browser cleanup failed")
 bdir=browserpath.parent;require(sha(bdir/"browser.json")==browser["browser_sha256"] and sha(bdir/"network-navigation-timing.json")==browser["timing_sha256"],"Browser raw evidence hash")
 report=load(bdir/"browser.json");timing=load(bdir/"network-navigation-timing.json")
 for name,digest in report["input_files"].items():require(sha(Path(name))==digest,("Browser input drift",name))
 require(all(c["passed"] for c in report["checks"]) and len(report["checks"])==41,"Raw browser check mismatch")
 events=timing["events"];markers=[(i,x) for i,x in enumerate(events) if x["event"]=="harness.parentNavigate"]
 require(len(markers)==3 and sum(x["is_initial"] for i,x in markers)==1 and all(x["pending"]==0 for i,x in markers),"Raw parent navigation evidence")
 require(not timing["pending"] and not any(x["event"]=="network.fetchError" for x in events),"Raw global fetch/pending evidence")
 require(not any(x["event"]=="network.responseCompleted" and x.get("status",0)>=400 for x in events),"Raw global HTTP evidence")
 quiet=[]
 for w in timing["idleWaits"]:
  require(not w.get("timeout") and w["pending_at_exit"]==[],"Raw network idle failure")
  if w["reason"]=="before-parent-navigation":
   matches=[i for i,x in markers if x["url"]==w["target"] and x["observed_ms"]>=w["end_ms"]]
   require(len(matches)==1,"Idle-to-navigation binding")
   prior=events[:matches[0]]
  else:
   require(w["reason"]=="final-full-idle","Unknown idle filter")
   prior=[x for x in events if x["observed_ms"]<=w["end_ms"]]
  seen_network=[x["observed_ms"] for x in prior if x["event"].startswith("network.")]
  if seen_network:quiet.append(w["end_ms"]-max(seen_network))
  else:
   # The initial guard predates raw network events; its lastActivity Date.now is not logged.
   # Its750ms condition is byte-reviewed, while independent measured minima below use actual network events.
   require(w["reason"]=="before-parent-navigation" and w["from"] is None,"Only initial idle may lack prior raw network activity")
 require(len(timing["idleWaits"])==4 and len(quiet)==3 and min(quiet)>=750,("Measured actual-departure/final global minimum quiet",quiet))
 errors=load(bdir/"page-errors.json")
 require(not errors["fetchErrors"] and not errors["httpErrors"],"Raw page network errors")
 require(all("Incorrect number of children for <munder/>" in json.dumps(x) for x in errors["all"]),"Unexpected page error")
 visual=load(repo(cfg["native_visual"]))
 require(visual["passed"] and visual["visually_inspected"] and visual["native_record_sha256"]==browser["native_record_sha256"] and visual["browser_receipt_sha256"]==sha(browserpath),"Native visual evidence binding")
 for name,digest in visual["screenshots"].items():require(sha(repo(name))==digest,("Native screenshot drift",name))
 pvisual=load(repo(cfg["pdf_visual"]));require(pvisual["passed"],"PDF visual gate failed")
 require({x["edition"] for x in pvisual["pages_inspected"]}==set(rows),"All five PDF editions must have inspected pages")
 for x in pvisual["pages_inspected"]:
  require(sha(repo(x["source"]))==x["source_sha256"]==rows[x["edition"]]["PDF"]["sha256"],"Inspected actual PDF mismatch")
  require(sha(repo(x["png"]))==x["png_sha256"],"PDF screenshot drift")

 require(nrec["figure_semantic_gate_sha256"]==sha(repo(cfg["figure_gate"])),"Unreviewed native figure")
 figrows={Path(name).suffix:row for name,row in figure["staging_assets"].items()}
 for ext in ["tex","pdf","svg"]:
  src=ROOT/("book/figures/ramified-cusp-prefix."+ext);dest=native/("book/figures/ramified-cusp-prefix."+ext)
  require(sha(src)==figrows["."+ext]["sha256"] and src.stat().st_size==figrows["."+ext]["bytes"],("Figure gate drift",ext))
  require(src.read_bytes()==dest.read_bytes(),("Native/source figure mismatch",ext))
 for name in ["ramified-gauss-core.tex","ramified-gauss-figure.tex","ramified-gauss-details.tex"]:
  require((native/"book/sources"/name).read_bytes()==(ROOT/"book/chapters"/name).read_bytes(),("Native copied source mismatch",name))
 oldpath=ROOT/"web/book/main.html";newpath=native/"book/main.html"
 oldbytes=oldpath.read_bytes();newbytes=newpath.read_bytes()
 require(sha(oldpath)==before["source_and_live_before"]["web/book/main.html"]["sha256"]==nrec["old_HTML_sha256"],"Live HTML baseline drift")
 require(sha(newpath)==nrec["new_HTML_sha256"],"Candidate HTML binding")
 old=oldbytes.decode();new=newbytes.decode()
 start='<section class="new-reviewed-chapters" id="ramified-gauss-section">'
 require(new.count(start)==1,"Duplicate/missing new native continuation")
 section=re.search(re.escape(start)+r".*?</section>\n",new,re.S)
 require(section is not None and "<section" not in section[0][len("<section"):],"Nested/unclosed continuation")
 restored=new[:section.start()]+new[section.end():]
 toc=re.findall(r'<br\s*/><span class="sectionToc"><a href="#rg:core">[^<]+</a></span>',restored)
 require(len(toc)==1,"New continuation ToC ambiguous")
 restored=restored.replace(toc[0],"",1);require(restored.encode()==oldbytes,"Old literal HTML byte changed")
 require(old.count("November 6, 2026")==new.count("November 6, 2026")==1,"Existing date changed")
 oldmath=re.findall(r"<math\b[^>]*>.*?</math>",old,re.S);allmath=re.findall(r"<math\b[^>]*>.*?</math>",new,re.S)
 require(len(oldmath)==10299 and len(allmath)==cfg["expected_math"]==nrec["math_nodes"],"Wrong MathML edition")
 pos=0
 for value in oldmath:
  while pos<len(allmath) and allmath[pos]!=value:pos+=1
  require(pos<len(allmath),"Old literal MathML/order changed");pos+=1
 fragment=ET.fromstring("<div>"+section[0]+"</div>");tree=ET.fromstring(new)
 oldtables=re.findall(r"<table\b[^>]*>.*?</table>",old,re.S)
 newtables=re.findall(r"<table\b[^>]*>.*?</table>",new,re.S)
 addedtables=re.findall(r"<table\b[^>]*>.*?</table>",section[0],re.S)
 require(len(oldtables)==389 and newtables==oldtables+addedtables and len(newtables)==nrec["tables"],"Literal old tables/order changed")
 oldframes=re.findall(r"<iframe\b[^>]*>.*?</iframe>",old,re.S)
 require(len(oldframes)==14 and re.findall(r"<iframe\b[^>]*>.*?</iframe>",new,re.S)==oldframes,"Literal old iframes changed")
 oldrefs=re.findall(r'(?:src|data)="([^"]+\.svg)"',old);newrefs=re.findall(r'(?:src|data)="([^"]+\.svg)"',new)
 require(len(oldrefs)==31 and newrefs==oldrefs+["figures/ramified-cusp-prefix.svg"] and nrec["svg_refs"]==32,"Old SVG reference order changed")
 assets=before["old_book_assets_sha256"]
 require({rel(p) for p in (ROOT/"web/book").rglob("*") if p.is_file()}==set(assets),"Old live book inventory changed")
 for name,digest in assets.items():
  require(sha(repo(name))==digest,("Old live asset drift",name))
  if name!="web/book/main.html":require(sha(native/"book"/name.removeprefix("web/book/"))==digest,("Old candidate asset drift",name))
 allowed={"main.html","sources/ramified-gauss-core.tex","sources/ramified-gauss-figure.tex","sources/ramified-gauss-details.tex",
          "figures/ramified-cusp-prefix.tex","figures/ramified-cusp-prefix.pdf","figures/ramified-cusp-prefix.svg"}
 changed=set()
 for p in (native/"book").rglob("*"):
  if not p.is_file():continue
  target=ROOT/"web/book"/p.relative_to(native/"book")
  if not target.exists() or sha(target)!=sha(p):changed.add(str(p.relative_to(native/"book")));pairs.append((p,target))
 require(changed==allowed,("Unexpected changed native files",changed))
 ids=[e.attrib["id"] for e in tree.iter() if "id" in e.attrib]
 fragmentids=[e.attrib["id"] for e in fragment.iter() if "id" in e.attrib]
 oldids=set(re.findall(r'\bid="([^"]+)"',old))
 require(len(fragmentids)==len(set(fragmentids)) and not oldids&set(fragmentids),"New id collision")
 labels=[]
 for name in ["ramified-gauss-core.tex","ramified-gauss-figure.tex","ramified-gauss-details.tex"]:
  labels+=re.findall(r"\\label\{([^}]+)\}",(ROOT/"book/chapters"/name).read_text())
 require(len(labels)==len(set(labels)) and all(ids.count(x)==1 for x in labels),"Lost/duplicated new source label")
 mathnodes=list(fragment.iter(NS+"math"));require(len(mathnodes)==nrec["math_nodes_added"]==len(allmath)-10299,"New formula count binding")
 for e in fragment.iter():
  tag=e.tag.rsplit("}",1)[-1]
  if tag in {"msub","msup","munder","mover"}:require(len(e)==2,("New MathML arity",tag))
  if tag in {"msubsup","munderover"}:require(len(e)==3,("New MathML arity",tag))
  if tag=="a" and e.attrib.get("href","").startswith("#"):require(html.unescape(e.attrib["href"][1:]) in ids,("Broken new internal reference",e.attrib))
 ast=load(native/"supplement.ast.json");astmath=[]
 def walk(x):
  if isinstance(x,dict):
   require(x.get("t") not in {"RawBlock","RawInline"},"Raw TeX in native AST")
   if x.get("t")=="Math":astmath.append(x["c"][1].strip())
   for v in x.values():walk(v)
  elif isinstance(x,list):
   for v in x:walk(v)
 walk(ast)
 annotations=["".join(e.find(".//"+NS+"annotation").itertext()).strip() for e in mathnodes]
 require(annotations==astmath,"New MathML/source AST order mismatch")
 images=[e for e in fragment.iter("img") if e.attrib.get("src")=="figures/ramified-cusp-prefix.svg"]
 require(len(images)==1 and bool(images[0].attrib.get("alt")),"Missing accessible new figure")
 require("filter:none!important" in images[0].attrib.get("style","") and "background-color:#fff" in images[0].attrib.get("style",""),"New figure inherited-night filter not isolated")
 require(any(e.attrib.get("class")=="reader-figure-scroll" and e.attrib.get("tabindex")=="0" for e in fragment.iter()),"Figure lacks keyboard scroll region")
 require(len(pairs)==18 and len({str(x) for x,y in pairs})==18 and len({str(y) for x,y in pairs})==18,"18 artifact mapping")
 baseline={x["path"]:x["sha256"] for x in protected["canonical_artifacts"]};beforetarget={}
 for src,target in pairs:
  actual=sha(target) if target.exists() else None
  if actual is None:require(rel(target).startswith(("web/book/sources/ramified-gauss-","web/book/figures/ramified-cusp-prefix.")),("Unexpected new target",rel(target)))
  else:require(actual==baseline[rel(target)],("Promoted target drift",rel(target)))
  beforetarget[rel(target)]=actual
 artifactsha={rel(src):sha(src) for src,target in pairs}
 manifest=dict(schema="ramified-book-independent-18-candidate-manifest-v1",created_utc=datetime.now(timezone.utc).isoformat(),
               config=pin(config),candidate_to_target={rel(src):rel(target) for src,target in pairs},artifact_sha256=artifactsha,
               target_before_sha256=beforetarget,artifact_count=18,existing_targets=sum(x is not None for x in beforetarget.values()),
               new_targets=sum(x is None for x in beforetarget.values()),pdf_checks=pdf_results,native_record=pin(native/"native-build-record.json"),
               new_edition=dict(book_pages=cfg["expected_pages"]["book-pdf"],focused_pages=[cfg["expected_pages"]["focused-concise"],cfg["expected_pages"]["focused-extended"]],
                                notes_pages=[cfg["expected_pages"]["notes-concise"],cfg["expected_pages"]["notes-extended"]],MathML=len(allmath),
                                old_literal_MathML_preserved=10299,tables=len(newtables),canonical_iframes=14,SVG_refs=32),
               source_closure_sha256=source_pins,new_labels=len(labels),new_MathML=len(mathnodes),old_assets=92,
               focused_browser_evidence=dict(receipt=pin(browserpath),checks=41,global_events=len(events),actual_departures=2,measured_minimum_quiet_ms=min(quiet)),
               all_candidates_current=True,live_targets_mutated=False)
 manifestpin=exclusive(out/"artifact-manifest-v1.json",manifest)
 # Freeze only if every candidate, immutable input and live target still equals its checked preimage.
 require(sha(config)==config_sha,"Config drift")
 for name,digest in gates.items():require(sha(repo(name))==digest,("Final gate drift",name))
 for name,digest in source_pins.items():require(sha(repo(name))==digest,("Final PDF source drift",name))
 for name,digest in nrec["source_sha256"].items():require(sha(repo(name))==digest,("Final native source drift",name))
 for row in integration["edits"]:require(sha(repo(row["path"]))==row["after"],("Final integration source drift",row["path"]))
 for src,target in pairs:
  require(sha(src)==artifactsha[rel(src)],("Final candidate drift",rel(src)))
  require((sha(target) if target.exists() else None)==beforetarget[rel(target)],("Final live target drift",rel(target)))
 acceptance=dict(schema="ramified-book-independent-source-native-artifact-acceptance-c-v1",passed=True,
                 reviewer="/root/interval_schur_review",created_utc=datetime.now(timezone.utc).isoformat(),
                 scope="Read-only exact candidate/source/PDF/native-preservation gate; no browser/science rerun, promotion or publication authorization.",
                 manifest=manifestpin,input_gates_sha256=gates,edition=manifest["new_edition"],config=pin(config),checker=pin(Path(__file__).resolve()),
                 all_five_PDF_actual_pages_and_strict_logs=True,all_current_source_pins_and_figure_assets=True,
                 old_HTML_restored_exact_after_only_section_and_ToC_removal=True,old_literal_MathML_order_exact=True,
                 old_389_literal_tables_preserved=True,old_14_literal_iframes_exact=True,old_31_SVG_refs_and_92_assets_preserved=True,
                 new_math_arity_AST_source_order_labels_references_valid=True,new_figure_keyboard_region_theme_accessibility_valid=True,
                 new_science_controls_or_builds_run=False,browser_run_by_this_reviewer=False,
                 whole_release_audit_performed=False,promotion_authorized=False,live_source_canonical_or_index_mutation=False)
 apin=exclusive(out/"acceptance-v1.json",acceptance)
 print(json.dumps(dict(passed=True,manifest=manifestpin,acceptance=apin,edition=manifest["new_edition"]),indent=2))
except Exception as e:
 exclusive(out/"failure-v1.json",dict(passed=False,error_type=type(e).__name__,error=str(e),config_sha256=config_sha,
                                   checker=pin(Path(__file__).resolve()),created_utc=datetime.now(timezone.utc).isoformat()))
 raise
