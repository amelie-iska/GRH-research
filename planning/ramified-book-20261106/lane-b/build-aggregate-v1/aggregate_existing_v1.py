#!/usr/bin/env python3
"""Validate five EXISTING staged PDFs after a source-key-only orchestrator failure.
Never rebuild, edit canonical inputs, change a saved build record, or promote.
"""
from pathlib import Path
import datetime,hashlib,json,re,subprocess
ROOT=Path("/home/iska/Documents/LaTeX-projects/GRH-from-Mac-20261104")
OUT=ROOT/"outputs/checks/2026-11-06-ramified-book/lane-b/build-aggregate-v1"
RUN=ROOT/"outputs/checks/2026-11-06-ramified-book/builds/run-v1"
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def rel(p):return str(p.relative_to(ROOT))
def pin(path,digest=None):
 p=ROOT/path
 actual=sha(p)
 if digest is not None:assert actual==digest,(path,actual,digest)
 return {"path":path,"sha256":actual}
def write(name,obj):
 p=OUT/name
 assert not p.exists(),str(p)
 p.write_text(json.dumps(obj,indent=2,sort_keys=True)+"\n")
 return {"path":rel(p),"sha256":sha(p)}
def tree():
 return {rel(p):{"sha256":sha(p),"bytes":p.stat().st_size} for p in sorted(RUN.rglob("*")) if p.is_file()}
def main():
 assert not OUT.exists(),"Preserve previous candidate; choose a fresh output if needed"
 before=tree()
 OUT.mkdir(parents=True)
 command_log=[]
 dependencies=[
 pin("planning/ramified-book-20261106/root/run_builds_v2.py","0122a3aab763d2bd9d423bbd34f6d4635eb34a3ba10fa11f455e20b6af71c8d2"),
 pin("outputs/checks/2026-11-06-ramified-book/root/source-integration-v1.json","26809557c35fe9dbe9fb27fd33f6fff4aa1e03928df9510deaafd2f09262e5df"),
 pin("outputs/checks/2026-11-06-ramified-book/root/figure-acceptance-v1.json","d0777191dd7a437748870dfd0ee7b3a565bcb9a854e538c970b226781609cc68"),
 pin("outputs/checks/2026-11-06-ramified-book/root/pdf-skill-marker-v1.json","dcff8a258746f384eb3731194579bf03087be9f223c31245e27e03ded1f9ce71"),
 pin("outputs/checks/2026-11-06-ramified-book/root/protected-baseline-v1.json","1c3b234a5ee3253a27a709ac788d9801ed9154593193e0c3211b735d69a1f7a3"),
 pin("outputs/checks/2026-11-06-ramified-book/builds/run-v1/results-so-far.json","86b9a6be3ceb29666e13afd6c33a0585ab8cf619d0156f2b03cbdbc1def6fe22"),
 pin("outputs/checks/2026-11-06-ramified-book/lane-b/source-precision-v1.json","0da59761327bd5f411d2b0125102d2549ddc3dc8d72ef3a412ca08baea7fbedf"),
 pin("outputs/checks/2026-11-06-ramified-book/lane-b/AUTHOR_RESULT-v2.json","344e6d9fe8cd6ce0dd9a39d593f373107d9cad41cf492842e12561120031f7e0"),
 pin("outputs/checks/2026-11-06-ramified-book/lane-a/review-math-v1/acceptance-v1.json","249f0a8680616b6a94e20a68de35154a387c16b58ab63ac165686c43bddac882")]
 integration=json.loads((ROOT/dependencies[1]["path"]).read_text())
 assert integration["passed"] and integration["chapter_count"]==40 and integration["old_chapter_inventory_exact"]
 source_guards={}
 for entry in integration["edits"]:
  source_guards[entry["path"]]=pin(entry["path"],entry["after"])["sha256"]
 core="papers/ramified-gauss-core.tex";details="papers/ramified-gauss-details.tex"
 core_sha="da33e607f548f37ad811b45a86969c315d4b1c680656a25fd72f2fb945283c3f"
 details_sha="c1f30a76a87e319fca5bddb134990afe00cc0eaab054964d2a8738bf6fac65f3"
 assert sha(ROOT/core)==core_sha==integration["source_sha256"]["core"]
 assert sha(ROOT/details)==details_sha==integration["source_sha256"]["details"]
 prefix=b"% Generated shared reviewed material.\n"
 chapter_checks=[]
 for short,paper in [("core",core),("details",details)]:
  chapter="book/chapters/ramified-gauss-"+short+".tex"
  assert (ROOT/chapter).read_bytes()==prefix+(ROOT/paper).read_bytes(),chapter
  chapter_checks.append({"paper":pin(paper),"chapter":pin(chapter),"exact_prefix_UTF8":prefix.decode(),"exact_bytes":True})
 figure=json.loads((ROOT/dependencies[2]["path"]).read_text())
 assert figure["passed"] and figure["root_visual"]["passed"]
 for path,record in figure["staging_assets"].items():
  assert sha(ROOT/path)==record["sha256"] and (ROOT/path).stat().st_size==record["bytes"],path
 for key in ["author_gate","independent_gate"]:
  entry=figure[key];dependencies.append(pin(entry["path"],entry["sha256"]))
  assert json.loads((ROOT/entry["path"]).read_text())["passed"]
 marker=json.loads((ROOT/dependencies[3]["path"]).read_text())
 assert marker["returncode"]==0 and marker["expected_PDF_deliverables"]==5 and marker["executed_once_SSH_Linux"]
 baseline=json.loads((ROOT/dependencies[4]["path"]).read_text())
 assert baseline["passed"]
 live_checks=[]
 for old in baseline["canonical_artifacts"]:
  live_checks.append({**pin(old["path"],old["sha256"]),"unchanged":True})
 oldlive="web/book/main.html"
 oldlive_sha=next(x["sha256"] for x in live_checks if x["path"]==oldlive)
 assert oldlive_sha=="5a54223737c1b35f7fcaa7371fd3d04c0e233e9bd3e8241dad0262bce73f560d"
 jobs=[
 ("book-pdf",348,"9ce2ff72259f6414f2ef686b4b053aef3bab654566141905cc55d0e29780eb2d",
 ["python3",str(ROOT/"planning/ramified-book-20261106/root/build_book_pdf_v1.py"),"--consume-book","--output",str(RUN/"book-pdf")]),
 ("focused-concise",85,"df31ef1bfee05cf50c61b7f81c8d277521d625f8ec06f95d8b2eb2175616d40e",None),
 ("focused-extended",243,"00507dfbe4dabb47b419119f706f0898d8dbf79ac703628ae3eb103a14e9b724",None),
 ("notes-concise",43,"c1256c214df6664d08cccad0de2e23f5fd308fd799f3bce9f36f520f9e17090c",None),
 ("notes-extended",131,"660c262ec2e2340783f887b916f02b914af12997bd5f5cecefdf8b6fc3b233cb",None)]
 physical={"physical-core":"df49c3f938ab80f80e4c0bb2efb4f71004a2d311dc21f952ecd45077dd35f939","physical-details":"4713c2c4e8496a87a8678406d2d43f02ab0bf82e4152fed15938aef52b3b9bf4","coherent-core":"5b3ab5c38b5c9130867793ac2e21c7dbc60560bc7d4eadbcc40fb1f334659f6c","coherent-details":"92dfe3077dffa048471b0705539bd82b2648c2e4b021c331c2753b6fb655176f"}
 historical_commands={}
 results={}
 old_predicate={}
 new_title=re.search(r"\\section\{([^}]+)\}",(ROOT/core).read_text())[1]
 details_title=re.search(r"\\section\{([^}]+)\}",(ROOT/details).read_text())[1]
 markers=["A signed short-divisor tail from a physical cubic matrix","The exact discrete top prefix, with every ray retained","Direct original-prefix cutoff reduction",new_title]
 norm=lambda s:re.sub("[^a-z0-9]","",s.lower())
 critical_patterns={
  "overfull_hbox":r"Overfull \\hbox","overfull_vbox":r"Overfull \\vbox",
  "undefined_control_sequence":r"Undefined control sequence","undefined_references":r"LaTeX Warning: There were undefined references",
  "reference_undefined":r"Reference [^\n]+undefined","citation_undefined":r"Citation [^\n]+undefined",
  "rerun_crossreferences":r"Rerun to get cross-references right","fatal_error":r"Fatal error","latex_error":r"! LaTeX Error",
  "emergency_stop":r"Emergency stop","multiply_defined_label":r"Label [^\n]+multiply defined"}
 for name,pages,record_sha,hcmd in jobs:
  out=RUN/name
  record=out/"build-record.json"
  pin(rel(record),record_sha)
  data=json.loads(record.read_text());assert data["passed"]
  assert data.get("production_promoted",False)==False and data.get("new_Lean_declarations")==0
  if hcmd is None:
   ed=name.split("-",1)[1]
   if name.startswith("focused"):
    hcmd=["python3",str(ROOT/"scripts/build_remote_articles.py"),"--edition",ed,"--output",str(out)]
   else:
    hcmd=["python3",str(ROOT/"planning/physical-sieve-20261105/builds/build_notes_v1.py"),"--edition",ed,"--root-go","--output",str(out)]
    for key,value in physical.items():hcmd+=["--"+key+"-sha",value]
  historical_commands[name]={"job_command":hcmd,"executed_wrapper":["nice","-n","15"]+hcmd,"cwd":str(ROOT),"executed_by_original_runner":True,"executed_by_this_recovery":False}
  builder=Path(hcmd[1])
  assert sha(builder)==data["builder_sha256"],(name,"producer changed")
  producer=pin(rel(builder),data["builder_sha256"])
  if name=="book-pdf":
   assert sha(out/"build_isolated.py")==data["builder_sha256"]
  actual_sources={path:pin(path,digest)["sha256"] for path,digest in data["source_sha256"].items()}
  book=name=="book-pdf"
  expected_core="book/chapters/ramified-gauss-core.tex" if book else core
  expected_details="book/chapters/ramified-gauss-details.tex" if book else details
  assert expected_core in actual_sources
  assert actual_sources[expected_core]==sha(ROOT/expected_core)
  needs_details=book or name.endswith("extended")
  assert (expected_details in actual_sources)==needs_details,(name,"wrong concise/extended closure")
  if needs_details:assert actual_sources[expected_details]==sha(ROOT/expected_details)
  old_predicate[name]=(core in actual_sources and (name.endswith("concise") or details in actual_sources))
  pdfs=list(out.glob("*.pdf"));assert len(pdfs)==1
  pdf=pdfs[0];assert pdf.read_bytes().startswith(b"%PDF")
  assert sha(pdf)==data["pdf_sha256"]
  commands=[["pdfinfo",str(pdf)],["pdftotext",str(pdf),"-"]]
  info=subprocess.check_output(commands[0],text=True)
  text=subprocess.check_output(commands[1],text=True)
  command_log += [{"command":cmd,"returncode":0,"scope":"read-existing-PDF-only"} for cmd in commands]
  actual_pages=int(re.search(r"Pages:\s+(\d+)",info)[1])
  assert actual_pages==pages==data.get("pages",data.get("pdf_pages"))
  checked=[{"marker":s,"present":norm(s) in norm(text)} for s in markers]
  if needs_details:checked.append({"marker":details_title,"present":norm(details_title) in norm(text)})
  assert all(x["present"] for x in checked),(name,checked)
  final_log=pdf.with_suffix(".log")
  log=final_log.read_text(errors="replace")
  counts={label:len(re.findall(pattern,log)) for label,pattern in critical_patterns.items()}
  assert not any(counts.values()),(name,counts)
  warning_lines=[line for line in log.splitlines() if "Warning:" in line or "Underfull" in line]
  final_pass=out/"build-pass3.log"
  if final_pass.exists():
   final_text=final_pass.read_text(errors="replace")
   assert not any(re.search(pattern,final_text) for pattern in critical_patterns.values())
  if book:
   assert data["consume_actual_integrated_book"] and data["original_HTML_sha256"]==oldlive_sha
   assert data["new_chapters"]==0 and data["canonical_labs"]==14 and not data["native_HTML_rebuilt"]
   newfig=[x for x in data["figure_records"] if x["path"]=="book/figures/ramified-cusp-prefix.pdf"]
   assert len(newfig)==1 and newfig[0]["sha256"]==figure["staging_assets"]["book/figures/ramified-cusp-prefix.pdf"]["sha256"]
  info_path=OUT/(name+".pdfinfo.txt")
  info_path.write_text(info)
  stdout=RUN/(name+".stdout.log")
  assert '"passed": true' in stdout.read_text()
  results[name]={
   "passed":True,"pages":pages,"PDF":pin(rel(pdf),data["pdf_sha256"]),"record":pin(rel(record),record_sha),
   "producer":producer,"historical_command":historical_commands[name],
   "actual_core_source_key":expected_core,"actual_details_source_key":expected_details if needs_details else None,
   "source_sha256":actual_sources,"source_count":len(actual_sources),"markers":checked,
   "pdftotext_UTF8_sha256":hashlib.sha256(text.encode()).hexdigest(),
   "pdfinfo":pin(rel(info_path)),"build_stdout":pin(rel(stdout)),
   "final_log":pin(rel(final_log)),"final_log_critical_diagnostics":counts,
   "final_log_warnings_and_underfull_lines":warning_lines,
   "final_pass3_log":pin(rel(final_pass)) if final_pass.exists() else None,
   "visual_review":"pending separate artifact review; no PDF rerender or layout claim by this aggregate"}
 assert old_predicate=={"book-pdf":False,"focused-concise":True,"focused-extended":True,"notes-concise":True,"notes-extended":True}
 # Reproduce ONLY the historical administrative predicate, never a build.
 caught=None
 try:
  assert old_predicate["book-pdf"]
 except AssertionError as exc:
  caught=type(exc).__name__
 assert caught=="AssertionError"
 runner=(ROOT/dependencies[0]["path"]).read_text()
 failed_line=next(i for i,l in enumerate(runner.splitlines(),1) if 'assert "papers/ramified-gauss-core.tex" in r["source_sha256"]' in l)
 partial=json.loads((RUN/"results-so-far.json").read_text())
 assert set(partial)=={"focused-concise","notes-concise"} and all(x["passed"] for x in partial.values())
 for name,item in partial.items():
  assert item["command"]==historical_commands[name]["job_command"]
  assert item["record_sha256"]==results[name]["record"]["sha256"] and item["pdf_sha256"]==results[name]["PDF"]["sha256"]
 assert not (RUN/"aggregate.json").exists(),"Original missing aggregate must remain missing, not retroactively rewritten"
 after=tree()
 assert after==before,"Saved build outputs changed during read-only validation"
 for path,digest in source_guards.items():assert sha(ROOT/path)==digest
 for item in live_checks:assert sha(ROOT/item["path"])==item["sha256"]
 inventory=write("preserved-build-tree-v1.json",{"passed":True,"before_equals_after":True,"files":before,"file_count":len(before)})
 failure=write("failed-harness-receipt-v1.json",{
  "schema":"ramified-book-source-key-harness-failure-v1","failure_preserved":True,
  "runner":dependencies[0],"failed_line":failed_line,
  "exact_failed_guard":runner.splitlines()[failed_line-1].strip(),
  "deterministic_readonly_predicate_replay":old_predicate,"replayed_exception":caught,
  "original_book_source_key":"book/chapters/ramified-gauss-core.tex",
  "reason":"The integrated book correctly records consumed chapter paths. The administrative runner incorrectly required the shared papers path for every edition after all independent builders had passed.",
  "build_failure":False,"all_five_saved_build_records_passed":True,
  "original_partial_results":dependencies[5],"original_partial_result_names":sorted(partial),
  "original_aggregate_not_created_and_not_rewritten":True,
  "runner_edited":False,"saved_build_records_edited":False,
  "resolution":"Separate strict source-bound read-only aggregation uses the book's actual chapter keys AND exact generated-prefix byte equality to reviewed shared papers; all prior marker/source/live guards retained.",
  "build_outputs_preserved":inventory,"rebuild_performed":False})
 commands=write("commands-v1.json",{
  "recovery_invocation":["python3",str(Path(__file__).resolve())],
  "recovery_cwd":str(ROOT),"execution_host":"iska-linux-vscode via SSH",
  "historical_jobs_from_pinned_runner":historical_commands,
  "new_commands_executed":command_log,
  "new_build_or_render_commands_executed":[]})
 record={
  "schema":"ramified-book-five-existing-editions-source-bound-aggregate-v1",
  "passed":True,"created_utc":datetime.datetime.now(datetime.timezone.utc).isoformat(),
  "producer":pin(rel(Path(__file__).resolve())),
  "scope":"Strict read-only recovery of five valid isolated PDF builds after a path-key-only post-build harness failure; native/browser/visual artifact review remains separate.",
  "results":results,"expected_pages":{"book-pdf":348,"focused-concise":85,"focused-extended":243,"notes-concise":43,"notes-extended":131},
  "dependencies":dependencies,"source_guard_sha256":source_guards,
  "generated_shared_chapter_byte_checks":chapter_checks,"figure_gate":dependencies[2],
  "PDF_operation_marker":dependencies[3],"old_live_HTML_sha256":oldlive_sha,
  "old_canonical_artifacts_unchanged":live_checks,
  "preserved_build_tree":inventory,"failure_receipt":failure,"commands":commands,
  "original_runner_and_results_preserved":True,"rebuild_performed":False,
  "canonical_source_edited":False,"production_promoted":False,"new_Lean_declarations":0,
  "remaining_checks":["independent native-MathML candidate preservation/render checks","PDF artifact visual inspection","strict staged browser checks","promotion only after all acceptance gates"]}
 aggregate=write("aggregate-v1.json",record)
 print(json.dumps({"passed":True,"aggregate":aggregate,"failed_harness_receipt":failure,"commands":commands,"preserved_build_tree":inventory,"pages":record["expected_pages"],"producer":record["producer"]}))
if __name__=="__main__":main()
