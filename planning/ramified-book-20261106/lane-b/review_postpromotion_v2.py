#!/usr/bin/env python3
"""Read-only post-promotion gate; never executes a promoter or page builder."""
from pathlib import Path
import hashlib,json,html,re,os,subprocess
R=Path("/home/iska/Documents/LaTeX-projects/GRH-from-Mac-20261104")
C=R/"outputs/checks/2026-11-06-ramified-book"
OUT=C/"lane-b/independent-review-post-v1"
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def pin(p):return {"path":str(p.relative_to(R)),"sha256":sha(p)}
def load(path,digest):
 p=R/path;assert sha(p)==digest,(path,"Hash mismatch");return json.loads(p.read_text())
def main():
 assert not OUT.exists(),"Preserve any previous review"
 promotion_path="outputs/checks/2026-11-06-ramified-book/lane-b/promotion-v1/promotion-v1.json"
 promotion_sha="a0c8b3f842d97e649a79a26a7cf6f927260ee15987169526280f2aec75e2aa81"
 pr=load(promotion_path,promotion_sha);assert pr["passed"] and not pr["Git_mutations"] and not pr["public_release_performed"]
 mr_path="outputs/checks/2026-11-06-ramified-book/metadata-final-v1/receipt-v1.json"
 mr_sha="bdbd4df0228e45e554e0c24e19325c42629cf397b28c85109d2836dd3b82368e"
 mr=load(mr_path,mr_sha);assert mr["passed"] and mr["promotion_sha256"]==promotion_sha
 bgpath="outputs/checks/2026-11-06-ramified-book/lane-a/browser-v1/acceptance-v1.json"
 bg=load(bgpath,"da7b30697fedd69b11a732615edac6ec38b45a8914eab8b4c800a6cbb13c7f9c")
 assert bg["schema"]=="ramified-book-focused-native-browser-acceptance-v1"
 for key in ["passed","all_checks_passed","no_new_errors","global_idle","own_context_and_server_cleanup"]:assert bg[key] is True,key
 assert bg["native_build_record_sha256"]=="7f6b8ba69696207d85f3fb38deb6ef2197fd701f9b38decd215e70873a22aa44"
 assert bg["PDF_aggregate_sha256"]=="763e2edbfa1207470752fb0dcd478d7f22aaf20c6916d707b89f56aabe3b834c"
 assert bg["book_PDF_build_record_sha256"]=="9ce2ff72259f6414f2ef686b4b053aef3bab654566141905cc55d0e29780eb2d"
 for item in bg["source_pins"]:assert sha(R/item["path"])==item["sha256"]
 assert bg["checks"]==bg["checks_passed"]==41 and bg["first_browser_execution_passed"]
 for key in ["fetch_errors","http_errors","pending","idle_timeouts"]:assert bg["network"][key]==0,key
 assert bg["minimum_observed_quiet_ms"]>=750 and bg["network"]["actual_departures"]==2
 agpath="outputs/checks/2026-11-06-ramified-book/lane-c/artifacts/candidate-review-v1/acceptance-v1.json"
 ag=load(agpath,"18a8900f719600c0a7aade5cb4e291bdd299b49253aff0d89d10ce1554f4b155")
 assert ag["passed"] and ag["old_literal_MathML_order_exact"] and ag["new_math_arity_AST_source_order_labels_references_valid"]
 for path,digest in ag["input_gates_sha256"].items():assert sha(R/path)==digest,path
 mfentry=ag["manifest"]
 mf=load(mfentry["path"],"c1a10436f4785637aa411181d4b21b4c284af2964fdb9780242662ef165286a9")
 assert (R/mfentry["path"]).stat().st_size==mfentry["bytes"]
 assert mf["schema"]=="ramified-book-independent-18-candidate-manifest-v1"
 assert mf["artifact_count"]==18 and mf["existing_targets"]==12 and mf["new_targets"]==6
 closure=mf["source_closure_sha256"];assert len(closure)==201
 for path,digest in closure.items():assert sha(R/path)==digest,path
 expected=load("outputs/checks/2026-11-06-ramified-book/lane-b/promotion-proposal-v1/expected-map-v1.json","eba13bd1cb90b088b18f24d4afc62d8ad6c8ded2d3bbf482367d11090762a294")
 assert mf["artifact_sha256"]=={x["source"]:x["source_sha256"] for x in expected["pairs"]}
 assert mf["target_before_sha256"]=={x["target"]:x["target_before_sha256"] for x in expected["pairs"]}
 assert mf["candidate_to_target"]=={x["source"]:x["target"] for x in expected["pairs"]}
 changes=pr["changed_artifacts"];assert len(changes)==18
 assert changes[-1]["target"]=="web/book/main.html","HTML was not last in preserved promotion record"
 actual_changes={x["target"]:x for x in changes}
 preserved=pr["preserved_before_images"];assert len(preserved)==12
 backups={x["target"]:x for x in preserved}
 artifact_checks=[]
 for item in expected["pairs"]:
  source=R/item["source"];target=R/item["target"]
  assert sha(source)==item["source_sha256"]==sha(target)
  change=actual_changes[item["target"]]
  assert change=={"source":item["source"],"target":item["target"],"before_sha256":item["target_before_sha256"],"after_sha256":item["source_sha256"]}
  if item["target_before_sha256"] is not None:
   backup=backups[item["target"]]
   assert backup["sha256"]==item["target_before_sha256"]==sha(R/backup["backup"])
  else:assert item["target"] not in backups
  assert not target.with_name(target.name+".ramified-book-pending").exists()
  artifact_checks.append({"source":item["source"],"target":item["target"],"after_sha256":sha(target),"before_preserved":item["target_before_sha256"] is not None,"new_target":item["target_before_sha256"] is None})
 nr=load("outputs/checks/2026-11-06-ramified-book/native/run-v1/native-build-record.json","7f6b8ba69696207d85f3fb38deb6ef2197fd701f9b38decd215e70873a22aa44")
 assert sha(R/"web/book/main.html")==nr["new_HTML_sha256"]
 assert len(nr["old_assets_unchanged"])==91
 for path,digest in nr["old_assets_unchanged"].items():assert sha(R/path)==digest,path
 # Current metadata must equal the reviewed candidate except the intentionally
 # regenerated implementation page, which is rederived from CURRENT queue.
 prepared=load("outputs/checks/2026-11-06-ramified-book/metadata-stage-v3/prepared-v3.json","e264c9228dfde6dbd3a605d8c05393e190434b701487ad6f707503b872f1bc85")
 review=load("outputs/checks/2026-11-06-ramified-book/lane-b/review-metadata-v3/acceptance-v1.json","fd60c9004bdb0dcf90040ea56bc56024c27c4ef31a6f91cde24bc6e954344209")
 assert review["passed"] and mr["review"]["sha256"]==sha(C/"lane-b/review-metadata-v3/acceptance-v1.json")
 candidate=R/prepared["candidate_root"]
 meta_checks=[]
 for path,change in mr["changes"].items():
  assert sha(R/path)==change["after"]
  backup=C/"metadata-final-v1/before"/path
  assert sha(backup)==change["before"],path
  if path!="web/implementation-plan.html":assert (R/path).read_bytes()==(candidate/path).read_bytes(),path
  meta_checks.append({"path":path,"current_sha256":sha(R/path),"before_preserved_sha256":sha(backup)})
 assert len(meta_checks)==11
 for path,digest in mr["generated_from_current_inputs"].items():assert sha(R/path)==digest,path
 queue=json.loads((R/"planning/IMPLEMENTATION_QUEUE.json").read_text())
 assert queue["project_complete"] is False and queue["research_complete"] is False
 task=next(x for x in queue["tasks"] if x["id"]=="P4-source-expansion")
 assert task["status"]=="in_progress" and task["owner"]=="grh-research-loop"
 assert promotion_path in task["evidence"] and "348pages" in task["last_result"] and "10858MathML" in task["last_result"]
 complete=sum(x["status"]=="complete" for x in queue["tasks"]);assert complete==14 and len(queue["tasks"])==21
 theme='<link rel="stylesheet" href="/theme.css" data-site-theme="palette" />\n<script src="/theme.js" data-site-theme="controller"></script>\n'
 themed=lambda s:s.replace("</head>",theme+"</head>",1)
 verification=(R/"book/VERIFICATION.md").read_text()
 expected_ver=themed('<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Verification coverage</title><link rel="stylesheet" href="/style.css"></head><body><main><section><h1>Verification and inclusion</h1><p><a href="/book/main.html">On-page book</a> · <a href="/source-volumes.html">Complete original sources</a></p><pre>'+html.escape(verification)+'</pre></section></main></body></html>')
 assert (R/"web/verification.html").read_text()==expected_ver
 cards=[]
 for t in queue["tasks"]:
  cards.append('<article><p class="eyebrow">'+html.escape(t['id'])+' · '+html.escape(t['status'])+'</p><h3>'+html.escape(t['objective'])+'</h3><p>'+html.escape(t['acceptance'])+'</p>'+('<p class="scope">Latest checkpoint: '+html.escape(t['last_result'])+'</p>' if t.get('last_result') else '')+'</article>')
 plan=(R/"planning/MASTER_IMPLEMENTATION_PLAN.md").read_text()
 body='<p><a href="/">Research atlas</a> · <a href="/book/main.html">On-page book</a></p><h1>Plan and implementation loop</h1><p>The existing hourly loop is active. '+str(complete)+' of '+str(len(queue['tasks']))+' queued tasks have checked evidence. This is a task count, not a percentage of a GRH proof.</p><p>Implementation completion and rigorously reviewed research completion are separate gates. The loop resumes one ready concrete deliverable, records checks, updates the page and publishes reviewed substantive milestones.</p><div class="cards">'+''.join(cards)+'</div><details><summary>Read the complete governing plan</summary><pre>'+html.escape(plan)+'</pre></details>'
 expected_impl=themed('<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Implementation plan and loop</title><link rel="stylesheet" href="/style.css"></head><body><main><section>'+body+'</section></main></body></html>')
 assert (R/"web/implementation-plan.html").read_text()==expected_impl
 assert html.escape(task["last_result"]) in expected_impl
 # Carry the already completed root preservation gate; do not rerun Git/state
 # checks after root explicitly requested only the remaining scoped strength.
 integrity_path="outputs/checks/2026-11-06-ramified-book/root/final-integrity-v1.json"
 integrity=load(integrity_path,"9ec621879edf55c035cc69727ef64f0238fc7f00edf7724dd4feb476c89231a8")
 assert integrity["passed"] and integrity["verified_promoted_artifacts"]==18 and integrity["preserved_before_images"]==12
 assert integrity["CPU_lock_preserved"] and integrity["old_non_HTML_assets_preserved"]==91
 states=pr["HEAD_index_states_before"]
 assert len(states)==15 and states==pr["HEAD_index_states_after"]
 assert [{"path":x["path"],"HEAD":x["HEAD"],"index_sha256":x["index_sha256"]} for x in states]==integrity["HEAD_index_states"]
 unexecuted=load("outputs/checks/2026-11-06-ramified-book/lane-b/promotion-proposal-v1/proposal-source-v2.json","442760e1d3cf0c7000cb4ac438b3aaebb9ec7f5f1c429d12c1981c79408afe18")
 assert not unexecuted["execution_performed"] and not unexecuted["promotion_performed"]
 assert sha(R/unexecuted["governing_producer"]["path"])==unexecuted["governing_producer"]["sha256"]
 assert pr["producer_sha256"]=="84bca36c187c58fd7401795d05ee1a5ba5bf1a50919c2e6f9370122c21fbc496"
 result={"schema":"ramified-book-independent-postpromotion-strengthening-v1","passed":True,
 "reviewer":"/root/unit_gauss_coprime","producer":pin(Path(__file__).resolve()),
 "promotion":{"path":promotion_path,"sha256":promotion_sha},"metadata_final":{"path":mr_path,"sha256":mr_sha},
 "strict_browser_gate":pin(R/bgpath),"independent_artifact_gate":pin(R/agpath),"artifact_manifest":mfentry,
 "A_direct_flags_all_true":["passed","all_checks_passed","no_new_errors","global_idle","own_context_and_server_cleanup"],
 "A_exact_native_aggregate_book_record_bindings":True,"A_checks":41,"A_first_run_passed":True,"A_all_zero_network_errors_pending_timeouts":True,
 "C_full_source_closure_count":201,"C_full_source_closure_current":True,
 "all18_candidate_and_promoted_target_hashes_exact":True,"artifacts":artifact_checks,
 "all12_before_preimages_exact":True,"six_new_targets_verified":True,"HTML_last_preserved_change_record":True,"no_pending_copies_left":True,
 "all91_nonHTML_old_assets_current":True,"metadata":{"all11_applied_file_and_before_hashes_exact":True,"files":meta_checks,"static_v3_gate_carried":True,"exact_verification_page_current_escaped_ledger":True,"exact_implementation_page_CURRENT_queue_plan":True,"helper_latest_result_visible":True,"queue_complete":14,"queue_tasks":21,"both_completion_gates_false":True},
 "root_final_integrity_carried":pin(R/integrity_path),"HEAD_index_state_evidence_carried_not_rerun":states,"unexecuted_proposal_v2_preserved":True,
 "execution":{"promotion_run_by_this_reviewer":False,"new_project_mutations":False,"builds":False,"browser":False,"page_builders":False,"new_controls":False,"Git_mutations":False,"only_new_lane_B_review_evidence_written":True},
 "scope":"Read-only independent strengthening of the already performed local18-artifact promotion and final metadata. No second promotion or publication. Actual finite pure prefix101/144 only; whole signed13/12/global unsigned9/8/GRH unchanged."}
 OUT.mkdir(parents=True);p=OUT/"acceptance-v1.json";p.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n")
 print(json.dumps({"passed":True,"acceptance":str(p.relative_to(R)),"sha256":sha(p),"producer":pin(Path(__file__).resolve())}))
if __name__=="__main__":main()
