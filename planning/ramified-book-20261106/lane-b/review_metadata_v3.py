#!/usr/bin/env python3
"""Read-only static review of the frozen v3 metadata candidate; no application."""
from pathlib import Path
import csv,hashlib,html,io,json,re
R=Path("/home/iska/Documents/LaTeX-projects/GRH-from-Mac-20261104")
C=R/"outputs/checks/2026-11-06-ramified-book"
P=C/"metadata-stage-v3/prepared-v3.json"
EXPECTED="e264c9228dfde6dbd3a605d8c05393e190434b701487ad6f707503b872f1bc85"
OUT=C/"lane-b/review-metadata-v3"
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def pin(p):return {"path":str(p.relative_to(R)),"sha256":sha(p)}
def snapshot(base):return {str(p.relative_to(R)):sha(p) for p in sorted(base.rglob("*")) if p.is_file()}
def main():
 assert not OUT.exists()
 assert sha(P)==EXPECTED
 data=json.loads(P.read_text());assert data["prepared"] and data["promotion_pending"] and not data["scientific_book_edited"]
 cand=R/data["candidate_root"];before=C/"metadata-stage-v3/before"
 oldv2=C/"metadata-stage-v1/prepared-v2.json";assert sha(oldv2)==data["preserved_v2_receipt"]["sha256"]
 v2root=C/"metadata-stage-v1/project"
 candidate_before=snapshot(cand);v2_before=snapshot(v2root)
 records={}
 for path,entry in data["records"].items():
  assert sha(R/path)==entry["before"],("Live metadata changed before review",path)
  assert sha(before/path)==entry["before"],("Before preimage differs",path)
  assert sha(cand/path)==entry["candidate"],path
  records[path]={"before":entry["before"],"candidate":entry["candidate"]}
 for path,digest in data["generated_pages"].items():assert sha(cand/path)==digest,path
 note=data["ledger_note"]
 assert note.startswith("\n\n## 6 November 2026")
 history={}
 for path in ["planning/MASTER_IMPLEMENTATION_PLAN.md","planning/PROGRESS.md","planning/CONTINUATION.md","planning/OPEN_OBLIGATIONS.md"]:
  assert (cand/path).read_text()==(before/path).read_text()+note,path
  history[path]="entire historical prefix byte-identical; one identical ledger append"
 src_old="The critical180-page working book"
 src_new="The critical348-page Linux working book"
 path="book/SOURCE_COVERAGE.md"
 s=(before/path).read_text();assert s.count(src_old)==1
 assert (cand/path).read_text()==s.replace(src_old,src_new,1)+note
 history[path]="one stale opening page-count correction; remainder exact; identical ledger append"
 old="The working critical book has 40 chapters (237 pages), with thirteen unique canonical on-page interactive tools"
 new="The working critical book has 40 chapters (348 pages in the Linux working edition), with fourteen unique canonical on-page interactive tools"
 path="book/VERIFICATION.md";s=(before/path).read_text();assert s.count(old)==1
 assert (cand/path).read_text()==s.replace(old,new,1)+note
 history[path]="one stale opening page/tool-count correction; remainder exact; identical ledger append"
 path="README.md";s=(before/path).read_text();t=(cand/path).read_text()
 first,rest=s.split("\n",1)
 assert t.startswith(first+"\n\n\n**Latest reviewed Linux edition:**")
 match=re.fullmatch(re.escape(first)+r"\n(?P<intro>\n\n\*\*Latest reviewed Linux edition:\*\*.*?)"+re.escape(rest)+re.escape(note),t,re.S)
 assert match,"README only inserts one new opening status paragraph and appends same ledger"
 assert "public333page/10299MathML release is unchanged" in match["intro"]
 history[path]="complete former body preserved after new scoped opening status paragraph; identical ledger append"
 csvpath="planning/CLAIMS.csv"
 oldbytes=(before/csvpath).read_bytes();newbytes=(cand/csvpath).read_bytes()
 assert newbytes.startswith(oldbytes),"No old CSV byte rewritten"
 oldrows=list(csv.reader(io.StringIO(oldbytes.decode())));rows=list(csv.reader(io.StringIO(newbytes.decode())))
 assert rows[:len(oldrows)]==oldrows and len(rows)==len(oldrows)+2
 assert all(len(x)==6 for x in rows)
 assert len({x[0] for x in rows})==len(rows)
 assert [x[0] for x in rows[-2:]]==["RGBBOOK01","RGBCONE01"]
 assert "not wholekernel/Lean/GRH" in rows[-2][3]
 assert "outsidefrozenbook" in rows[-1][3] and "fullballopen" in rows[-1][3]
 queue_path="planning/IMPLEMENTATION_QUEUE.json"
 assert (cand/queue_path).read_bytes()==(before/queue_path).read_bytes()==(R/queue_path).read_bytes()
 queue=json.loads((cand/queue_path).read_text())
 assert queue["project_complete"] is False and queue["research_complete"] is False
 assert queue["governing_plan"]=="planning/MASTER_IMPLEMENTATION_PLAN.md"
 complete=sum(x["status"]=="complete" for x in queue["tasks"])
 assert len(queue["tasks"])==21 and complete==14
 # Reconstruct the two existing page producers as PURE strings, not by executing
 # their write functions. Comparison includes exact HTML escaping and theme.
 theme='<link rel="stylesheet" href="/theme.css" data-site-theme="palette" />\n<script src="/theme.js" data-site-theme="controller"></script>\n'
 def themed(s):return s.replace("</head>",theme+"</head>",1)
 verification=(cand/"book/VERIFICATION.md").read_text()
 expected_ver=themed('<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Verification coverage</title><link rel="stylesheet" href="/style.css"></head><body><main><section><h1>Verification and inclusion</h1><p><a href="/book/main.html">On-page book</a> · <a href="/source-volumes.html">Complete original sources</a></p><pre>'+html.escape(verification)+'</pre></section></main></body></html>')
 assert (cand/"web/verification.html").read_text()==expected_ver
 plan=(cand/"planning/MASTER_IMPLEMENTATION_PLAN.md").read_text();cards=[]
 for task in queue["tasks"]:
  cards.append('<article><p class="eyebrow">'+html.escape(task['id'])+' · '+html.escape(task['status'])+'</p><h3>'+html.escape(task['objective'])+'</h3><p>'+html.escape(task['acceptance'])+'</p>'+('<p class="scope">Latest checkpoint: '+html.escape(task['last_result'])+'</p>' if task.get('last_result') else '')+'</article>')
 body='<p><a href="/">Research atlas</a> · <a href="/book/main.html">On-page book</a></p><h1>Plan and implementation loop</h1><p>The existing hourly loop is active. '+str(complete)+' of '+str(len(queue['tasks']))+' queued tasks have checked evidence. This is a task count, not a percentage of a GRH proof.</p><p>Implementation completion and rigorously reviewed research completion are separate gates. The loop resumes one ready concrete deliverable, records checks, updates the page and publishes reviewed substantive milestones.</p><div class="cards">'+''.join(cards)+'</div><details><summary>Read the complete governing plan</summary><pre>'+html.escape(plan)+'</pre></details>'
 expected_impl=themed('<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Implementation plan and loop</title><link rel="stylesheet" href="/style.css"></head><body><main><section>'+body+'</section></main></body></html>')
 assert (cand/"web/implementation-plan.html").read_text()==expected_impl
 # Exact bounded v2 -> v3 index clarification, all other candidate files unchanged.
 v2index=(v2root/"web/index.html").read_text();index=(cand/"web/index.html").read_text()
 old_scope=data["index_scope_precision"]["old"];new_scope=data["index_scope_precision"]["new"]
 assert v2index.count(old_scope)==1 and index==v2index.replace(old_scope,new_scope,1)
 for p in cand.rglob("*"):
  if p.is_file() and p.relative_to(cand)!=Path("web/index.html"):
   assert p.read_bytes()==(v2root/p.relative_to(cand)).read_bytes(),str(p)
 # Every old landing-page href retained; exactly one new anchor, checked in staged MathML.
 href=lambda s:re.findall(r'\bhref=["\']([^"\']+)["\']',s)
 from collections import Counter
 oldhref=Counter(href((before/"web/index.html").read_text()));newhref=Counter(href(index))
 assert not oldhref-newhref
 added=list((newhref-oldhref).elements());assert added==["/book/main.html#rg:core"]
 native=C/"native/run-v1/book/main.html";nhtml=native.read_text()
 assert 'id="rg:core"' in nhtml
 assert "348 pages · 40 chapters · 10,858 MathML expressions" in index
 assert "focused articles 85/243 pages and notes 43/131 pages" in index
 assert "Public release remains333pages" in index
 # Semantic scope checks use bounded, explicit phrases rather than substring
 # proof certification of historical manuscript text.
 required=[
 "348pages/40chapters/10858nativeMathML","10299 earlier literal math","389tables,14canonical",
 "31earlierSVG","all91 earlier non-HTML","92 original book files including HTML",
 "original rational-cusp/whole-factor","Focused concise/extended PDFs are85/243pages",
 "analytic notes43/131pages","TOP prefix P_X[AU,AU]","normalized leading upper power101/144",
 "margin7/144","raw numerator D*P_X has one extraD","not the whole signed h1 form",
 "B_U=mu*A_U is not","Nm>U","prefix(p,n)/k/s/w rawzeros",
 "OUTSIDE this frozen book package","primitive power raw masks","NEW fixed numerator family",
 "Growing good sixth-free Nr>=64","Public Main1f346d1a825aa6eff1479197aef45d293a878902",
 "Pagesde2614bf439e1c6ab8af09f3242af5a163f16f79","verified333page/10299MathML",
 "Whole signed13/12/global unsigned9/8 are unchanged","Both implementation/research completion gates remain FALSE"]
 assert all(s in note for s in required)
 assert sha(C/"native/run-v1/native-build-record.json")=="7f6b8ba69696207d85f3fb38deb6ef2197fd701f9b38decd215e70873a22aa44"
 assert sha(C/"lane-b/build-aggregate-v1/aggregate-v1.json")=="763e2edbfa1207470752fb0dcd478d7f22aaf20c6916d707b89f56aabe3b834c"
 cone=C/"lane-c/research/RESEARCH_ACCEPTED-v1.json";assert sha(cone).startswith("23285bc4")
 oldprepared=C/"metadata-stage-v1/prepared-v1.json"
 correction=C/"metadata-stage-v1/count-precision-v1.json"
 assert sha(oldprepared)=="04734f9d03fe058ae15f12920c83465da9fada978c219ffae726ee83e29220cb"
 assert sha(correction)=="847e16ce8c1ba5dc54e6dddb2cfe0dca363f8c5f89e3e184982d0e1ea50a212b"
 oldv1=json.loads(oldprepared.read_text())
 preserved=C/"metadata-stage-v1/v1-candidate-preserved/project"
 for path,record in oldv1["records"].items():assert sha(preserved/path)==record["candidate"]
 for path,digest in oldv1["generated_pages"].items():assert sha(preserved/path)==digest
 assert snapshot(cand)==candidate_before and snapshot(v2root)==v2_before
 OUT.mkdir(parents=True)
 result={
 "schema":"ramified-book-independent-staged-metadata-review-v3","passed":True,
 "governing_prepared":pin(P),"candidate_root":str(cand.relative_to(R)),
 "producer":pin(Path(__file__).resolve()),"source_and_candidate_pins":records,
 "generated_pages":data["generated_pages"],"history_preservation":history,
 "CSV":{"before_rows_including_header":len(oldrows),"after_rows_including_header":len(rows),"new_IDs":[x[0] for x in rows[-2:]],"all_six_fields":True,"all_IDs_unique":True,"old_bytes_prefix_exact":True},
 "queue":{"byte_identical":True,"complete":complete,"tasks":len(queue["tasks"]),"project_complete":False,"research_complete":False},
 "exact_existing_producer_reconstruction":{"verification":True,"implementation_plan":True,"escaped_ledger_bytes_exact":True,"theme_assets_exact":True},
 "index":{"all_old_hrefs_preserved":True,"only_added_href":added[0],"added_anchor_present_in_staged_book":True,"v2_to_v3_only_required_scope_sentence":True,"local348_public333_distinction":True},
 "accepted_scope":{"local_edition":[348,10858],"public_edition_unchanged":[333,10299],"normalized_pure_prefix_upper_power":"101/144","cone_research_only_outside_frozen_book":True,"whole_signed_and_global_unchanged":["13/12","9/8"],"old_assets_precision":"92 including oldHTML;91 unchanged nonHTML"},
 "input_records":[pin(C/"lane-b/build-aggregate-v1/aggregate-v1.json"),pin(C/"native/run-v1/native-build-record.json"),pin(cone),pin(oldv2),pin(oldprepared),pin(correction),pin(R/"scripts/build_verification_page.py"),pin(R/"scripts/build_implementation_page.py"),pin(R/"scripts/theme_assets.py")],
 "preserved_historical_candidates":{"v1_exact":True,"v2_exact":True,"v3_not_modified_by_review":True},
 "execution":{"candidate_applied":False,"canonical_source_edited":False,"PDF_native_rebuilt":False,"project_files_changed":False,"only_new_lane_b_review_evidence_written":True},
 "required_finalization":["Apply metadata only after the independently gated18-artifact local promotion; before bytes must be preserved",
 "Create/bind governing final milestone and handoff referenced by the prepared staged ledger and RGBBOOK01 evidence",
 "If research_loop checkpoint changes the queue, regenerate implementation-plan page exactly against CURRENT plan/queue with existing producer and record fresh exact validation; this gate covers only the pinned candidate queue snapshot"],
 "not_claimed":["metadata already applied","artifact promotion already performed by reviewer","new public release","both completion gates satisfied"]}
 out=OUT/"acceptance-v1.json";out.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n")
 print(json.dumps({"passed":True,"acceptance":str(out.relative_to(R)),"sha256":sha(out),"producer":pin(Path(__file__).resolve())}))
if __name__=="__main__":main()
