#!/usr/bin/env python3
"""Promote only fully reviewed coherent-book artifacts, preserving every before byte."""
from pathlib import Path
import hashlib,json,shutil,subprocess
R=Path("/home/iska/Documents/LaTeX-projects/GRH-from-Mac-20261104")
C=R/"outputs/checks/2026-11-06-coherent-book"
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def main():
 out=C/"promotion-v1";assert not out.exists()
 required=["review-math-a/acceptance-v1.json","root/source-integration-v1.json","review-integration-a/acceptance-v1.json","review-integration-a/browser-policy-v1.json","review-integration-a/artifact-acceptance-v1.json","builds/aggregate-v2.json","root/pdf-visual-v2/review-v1.json","root/lab-visual-v1.json","root/native-browser-v3/browser.json","root/combined-browser-v2/browser.json","lane-c/frozen-receipt-v1.json"]
 gates={}
 for n in required:
  p=C/n;x=json.loads(p.read_text());assert x.get("passed",x.get("accepted",False)) is True,(n,"Acceptance missing")
  gates[str(p.relative_to(R))]=sha(p)
 aggregate=json.loads((C/"builds/aggregate-v2.json").read_text())
 book=C/"builds/book-pdf-v2";native=C/"builds/native-v2"
 nrec=json.loads((native/"native-build-record.json").read_text());assert nrec["passed"] and nrec["math_nodes"]==9810 and nrec["canonical_labs"]==14
 before=json.loads((C/"root/integration-before-v1.json").read_text())
 assert sha(R/"web/book/main.html")==before["source_and_live_before"]["web/book/main.html"]["sha256"]
 for name,digest in before["old_book_assets_sha256"].items():assert sha(R/name)==digest,("Old live asset changed",name)
 frozen=json.loads((C/"lane-c/frozen-receipt-v1.json").read_text())
 for name,m in frozen["files"].items():assert sha(R/name)==m["sha256"] and (R/name).stat().st_size==m["bytes"],("Frozen UI/figure changed",name)
 builds=[book/"build-record.json",native/"native-build-record.json"]
 pairs=[(book/("main."+ext),R/"outputs/book"/("surface-orders-book."+ext)) for ext in ["pdf","log","toc"]]
 allowed={"main.html","sources/coherent-band-core.tex","sources/coherent-band-details.tex","sources/coherent-band-figure.tex","figures/coherent-band-workflow.pdf","figures/coherent-band-workflow.svg","figures/coherent-band-workflow.tex"}
 for p in (native/"book").rglob("*"):
  if not p.is_file():continue
  rel=p.relative_to(native/"book");target=R/"web/book"/rel
  if not target.exists() or p.read_bytes()!=target.read_bytes():
   assert str(rel) in allowed,("Unexpected native edit",str(rel));pairs.append((p,target))
 for edition in ["concise","extended"]:
  for group,stem,targetdir in [("focused","resolutions-"+edition,R/"outputs/papers"),("notes","validated-oracle-"+edition,R/"outputs/papers/validated-oracle-20261104")]:
   d=C/"builds/run-v1"/(group+"-"+edition);builds.append(d/"build-record.json")
   for ext in ["pdf","log"]:pairs.append((d/(stem+"."+ext),targetdir/(stem+"."+ext)))
 for p in builds:
  x=json.loads(p.read_text());assert x["passed"],p
  for name,digest in x.get("source_sha256",{}).items():assert sha(R/name)==digest,(p,name)
 for name,digest in nrec["source_sha256"].items():assert sha(R/name)==digest
 assert len(pairs)==18,len(pairs)
 assert subprocess.check_output(["git","rev-parse","HEAD"],cwd=R,text=True).strip()=="dba37ffaa78c82ade1385f7ee56c907ab0c67d3a"
 index=R/subprocess.check_output(["git","rev-parse","--git-path","index"],cwd=R,text=True).strip()
 index_before=sha(index);assert index_before=="0ef1af515b143ef68fed1d9a42aef7c00d5d1d7c3ef6832d2926d48e0925214c"
 artifact_gate=json.loads((C/"review-integration-a/artifact-acceptance-v1.json").read_text())
 artifact_pins=artifact_gate["artifact_sha256"];target_pins=artifact_gate["target_before_sha256"]
 assert set(artifact_pins)=={str(source.relative_to(R)) for source,target in pairs}
 assert set(target_pins)=={str(target.relative_to(R)) for source,target in pairs}
 for source,target in pairs:
  assert source.is_file() and (not target.exists() or target.is_file())
  assert sha(source)==artifact_pins[str(source.relative_to(R))],("Staged artifact changed",source)
  current=sha(target) if target.exists() else None
  assert current==target_pins[str(target.relative_to(R))],("Concurrent target change",target)
  assert not target.with_name(target.name+".coherent-book-pending").exists(),("Existing pending artifact",target)

 # Assets and PDFs first; the single HTML switch occurs after all new links exist.
 pairs.sort(key=lambda pair:pair[1]==R/"web/book/main.html")
 out.mkdir();changes=[]
 for source,target in pairs:
  old=sha(target) if target.exists() else None
  if old==sha(source):continue
  if target.exists():
   b=out/"before"/target.relative_to(R);b.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(target,b)
  target.parent.mkdir(parents=True,exist_ok=True)
  pending=target.with_name(target.name+".coherent-book-pending");assert not pending.exists()
  shutil.copyfile(source,pending);assert pending.read_bytes()==source.read_bytes();pending.replace(target)
  changes.append(dict(source=str(source.relative_to(R)),target=str(target.relative_to(R)),before_sha256=old,after_sha256=sha(target)))
 assert sha(index)==index_before and sha(R/"web/book/main.html")==nrec["new_HTML_sha256"]
 record=dict(passed=True,changed_artifacts=changes,acceptance_records_sha256=gates,independently_reviewed_artifact_sha256=artifact_pins,producer_sha256=sha(Path(__file__)),build_records_sha256={str(p.relative_to(R)):sha(p) for p in builds},edition=dict(book_pages=319,chapters=40,MathML=9810,old_literal_MathML_preserved=9172,old_tables_preserved=389,tables=389,canonical_iframes=14,old_canonical_iframes_preserved=13,SVG_refs=30,old_SVG_refs_preserved=29,focused_pages=[76,215],notes_pages=[34,105]),source_HEAD_preserved=True,source_index_sha256=index_before,index_edited=False,old8765_untouched=True,new_Lean_declarations=0,public_release_performed=False,scope="Only five valid editions and append-only nativecontinuation/unique workflow promoted. Fixedprofile fullunequalnorm signed estimate/determinant/fullLean/GRH remain open. Earlier candidates/failures remain preserved.")
 (out/"promotion-v1.json").write_text(json.dumps(record,indent=2)+"\n");print(json.dumps(dict(passed=True,changed=len(changes),record=str(out/"promotion-v1.json"),sha256=sha(out/"promotion-v1.json"))))
if __name__=="__main__":main()
