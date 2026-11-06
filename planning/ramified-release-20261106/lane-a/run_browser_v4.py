"""Full220+Gauss40+ramified44 SAME-session staged/LIVE QA, frozen bundle only; explicit root GO."""
from pathlib import Path
from http.server import ThreadingHTTPServer,SimpleHTTPRequestHandler
from urllib.parse import urlsplit,unquote
from urllib.request import Request,urlopen
from datetime import datetime,timezone
import argparse,hashlib,json,os,subprocess,threading,re
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[2];OUT=ROOT/"outputs/checks/2026-11-06-ramified-release/lane-a"
sha=lambda b:hashlib.sha256(b).hexdigest()
file_sha=lambda p:sha(Path(p).read_bytes())
p=argparse.ArgumentParser()
p.add_argument("--mode",choices=["stage","live"],required=True);p.add_argument("--root-go",action="store_true")
for n in ["bundle","freeze-receipt","qa-freeze"]:p.add_argument("--"+n,type=Path,required=True)
p.add_argument("--inventory-sha256",required=True);p.add_argument("--qa-freeze-sha256",required=True);p.add_argument("--publication-receipt",type=Path);a=p.parse_args()
assert a.root_go,"Explicit root GO required; no automatic stage or LIVE"
bundle=a.bundle.resolve();prep=bundle.parent/"release-preparation-v1"
assert bundle.is_dir() and not bundle.is_relative_to(ROOT) and "/outputs/publication/"in str(bundle) and bundle.name=="site-bundle-v1"
freeze_bytes=a.freeze_receipt.read_bytes();qbytes=a.qa_freeze.read_bytes();assert sha(qbytes)==a.qa_freeze_sha256
q=json.loads(qbytes);assert q["prepared"] and q["source_HTTP_fallback"] is False and q["bundle"]=={"root":str(bundle),"freeze_receipt_sha256":sha(freeze_bytes),"inventory_sha256":a.inventory_sha256}
roles={k:Path(v).resolve() for k,v in q["roles"].items()}
for k,path in roles.items():assert str(path) in q["files_sha256"] and file_sha(path)==q["files_sha256"][str(path)]
for path,h in q["files_sha256"].items():assert file_sha(path)==h,path
assert roles["full_runner"]==roles["focused_runner"]==roles["ramified_runner"]==Path(__file__).resolve()
e_bytes=roles["expectations"].read_bytes();e=json.loads(e_bytes);assert not e["bundle_assets_pending"] and e["schema"]=="ramified-release-expectations-v1"
native_bytes=roles["native_map"].read_bytes();ramified_bytes=roles["ramified_native_map"].read_bytes();pdf_bytes=roles["pdf_map"].read_bytes();nm=json.loads(native_bytes);rm=json.loads(ramified_bytes);pm=json.loads(pdf_bytes)
assert e["gtl"]==nm and e["rg"]==rm and e["pdf_map"]==pm,"The exact mapped bytes must be the expectations actually consumed"
assert len(q["inherited_group_names"])==220 and len(q["focused_required_group_names"])==40 and len(q["ramified_required_group_names"])==44 and len(q["lab_required_group_names"])==58
assert [e["book_pages"],e["math_nodes"],e["tables"],e["frames"]]==[348,10858,389,14]
assert nm["bundle_inventory_sha256"]==rm["bundle_inventory_sha256"]==pm["bundle_inventory_sha256"]==a.inventory_sha256
assert len(nm["public_files"])==len(rm["public_files"])==7 and len(pm["public_files"])==5
for path,h in {**nm["public_files"],**rm["public_files"],**pm["public_files"]}.items():assert file_sha(bundle/path)==h,path
run=OUT/(a.mode+"-browser-"+datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ"));full=run/"full";focused=run/"focused";ramified=run/"ramified";full.mkdir(parents=True);focused.mkdir();ramified.mkdir()
def inventory():
 entries=list(bundle.rglob("*"));assert not any(p.is_symlink() for p in entries)
 rows=[dict(path=f.relative_to(bundle).as_posix(),bytes=f.stat().st_size,sha256=file_sha(f)) for f in sorted(entries) if f.is_file()]
 raw=(json.dumps(rows,separators=(",",":"),sort_keys=True)+"\n").encode();return rows,raw,sha(raw)
before,raw,ih=inventory();(run/"bundle-inventory-before.json").write_bytes(raw);assert ih==a.inventory_sha256
assert not(bundle/"__outside_project_prefix__").exists() and not(bundle/"__outside_fixture__").exists()
for path in ["QA_INPUT_FREEZE-v1.json","qa-expectations.json","native-map.json","ramified-map.json","pdf-map.json"]:
 data={"QA_INPUT_FREEZE-v1.json":qbytes,"qa-expectations.json":e_bytes,"native-map.json":native_bytes,"ramified-map.json":ramified_bytes,"pdf-map.json":pdf_bytes}[path];(run/path).write_bytes(data)
# Frozen byte-identical lab reads only a fresh BUNDLE-derived file fixture.
fixture=run/"lab-expectation-fixture";lab=fixture/"planning/coherent-release-20261106/qa/check_lab_v1.mjs";lab.parent.mkdir(parents=True);lab.write_bytes(roles["lab_module"].read_bytes())
payload=fixture/"web/data/coherent-band-schur-v1.json";payload.parent.mkdir(parents=True);payload.write_bytes((bundle/"data/coherent-band-schur-v1.json").read_bytes())
assert file_sha(lab)==e["lab"]["module_sha256"]=="094fbfb28a46da943ced6f16ed40207e1fc97a57ff97cd780cc085392999247d" and file_sha(payload)==e["lab"]["payload_sha256"]
requests=[];server=None;thread=None;browser={};focus={};ramified_focus={};timing={};passed=False;error=None;base=None;external=[];counters={};cleanup={}
try:
 for path,v in e["pdfs"].items():
  assert file_sha(bundle/path.lstrip("/"))==v["sha256"]
  info=subprocess.check_output(["pdfinfo",str(bundle/path.lstrip("/"))],text=True);assert int(re.search(r"Pages:\s+(\d+)",info)[1])==v["pages"]
 if a.mode=="stage":
  class Handler(SimpleHTTPRequestHandler):
   def do_GET(self):
    path=unquote(urlsplit(self.path).path);requests.append(dict(method="GET",path=path))
    if path=="/favicon.ico":self.send_response(404);self.end_headers();return
    super().do_GET()
   def do_HEAD(self):requests.append(dict(method="HEAD",path=unquote(urlsplit(self.path).path)));super().do_HEAD()
   def translate_path(self,path):
    name=unquote(urlsplit(path).path)
    if not name.startswith("/GRH-research/"):return str(bundle/"__outside_project_prefix__")
    target=(bundle/name[len("/GRH-research/"):]).resolve()
    return str(target) if target.is_relative_to(bundle) else str(bundle/"__outside_fixture__")
   def log_message(self,*args):pass
  server=ThreadingHTTPServer(("127.0.0.1",0),Handler);thread=threading.Thread(target=server.serve_forever,daemon=True);thread.start();base="http://127.0.0.1:"+str(server.server_port)+"/GRH-research"
 else:
  assert a.publication_receipt and a.publication_receipt.resolve().is_relative_to(prep),"New actual Pages receipt required after explicit LIVE GO"
  pubbytes=a.publication_receipt.read_bytes();pub=json.loads(pubbytes);assert pub["published"] is True and pub["target"]=="pages" and pub["force"] is False
  for path,h in e["changed_tested_files"].items():assert path in pub["changed_paths"] and pub["changed_file_sha256"][path]==h,path
  (run/"publication-receipt.json").write_bytes(pubbytes);base="https://amelie-iska.github.io/GRH-research"
 env={**os.environ,"PROFILE_QA_URL":base,"PROFILE_QA_OUTPUT":str(full),"SIGNED_DIVISOR_QA_EXPECTATIONS":str(roles["expectations"]),"CBK_LAB_MODULE":lab.as_uri(),"GTL_QA_MODULE":roles["focused_harness"].as_uri(),"RAMIFIED_QA_MODULE":roles["ramified_harness"].as_uri(),"GAUSS_QA_INPUT_FREEZE":str(a.qa_freeze),"GAUSS_QA_INPUT_FREEZE_SHA":a.qa_freeze_sha256}
 result=subprocess.run(["node",str(roles["full_harness"])],cwd=full,env=env,capture_output=True,text=True,timeout=900)
 (run/"stdout.txt").write_text(result.stdout);(run/"stderr.txt").write_text(result.stderr);assert result.returncode==0,"Worker failed; all output preserved"
 browser=json.loads((full/"browser.json").read_text());assert browser["passed"]
 assert len(browser["integration"])==220 and all(x["passed"] for x in browser["integration"])
 assert set(q["inherited_group_names"])=={x["name"] for x in browser["integration"]}
 cl=browser["coherentBandLab"];assert cl["passed"] and len(cl["checks"])==58 and len(cl["layouts"])==54 and all(x["passed"] for x in cl["checks"])
 assert set(q["lab_required_group_names"])=={x["name"]for x in cl["checks"]}
 assert cl["savedStringPositionsChecked"]==1218 and cl["renderedCellsChecked"]==3654
 focus=browser["gaussTail"];assert focus["passed"] and len(focus["checks"])==40 and all(x["passed"] for x in focus["checks"]) and set(q["focused_required_group_names"])=={x["name"] for x in focus["checks"]}
 ramified_focus=browser["ramifiedGauss"];assert ramified_focus["passed"] and len(ramified_focus["checks"])==44 and all(x["passed"]for x in ramified_focus["checks"]) and set(q["ramified_required_group_names"])=={x["name"]for x in ramified_focus["checks"]}
 timing_bytes=(full/"network-navigation-timing.json").read_bytes();timing=json.loads(timing_bytes)
 assert timing["quiet_ms"]==750 and timing["timeout_ms"]==30000 and not timing["pending"]
 events=timing["events"];navs=[x for x in events if x["event"]=="harness.parentNavigate"];waits=timing["idleWaits"]
 counters=dict(global_fetch_errors=sum(x["event"]=="network.fetchError" for x in events),idle_timeouts=sum(bool(x.get("timeout")) for x in waits),pending_at_departures=sum(x["pending"] for x in navs if not x["is_initial"]),pending_final_requests=len(timing["pending"]),initial_navigation_count=sum(x["is_initial"] for x in navs),actual_departure_count=sum(not x["is_initial"] for x in navs),navigation_count=len(navs),quiet_ms=750,timeout_ms=30000,idle_wait_count=len(waits))
 assert all(counters[k]==0 for k in ["global_fetch_errors","idle_timeouts","pending_at_departures","pending_final_requests"])
 assert counters["initial_navigation_count"]==1 and counters["actual_departure_count"]>=13 and len(waits)>=len(navs)+1
 assert all(x["pending"]==0 for x in navs) and all(not x.get("timeout") and x["pending_at_exit"]==[] for x in waits)
 cleanup=browser["cleanup"];assert all(cleanup[k] is True for k in ["owned_tab_closed","owned_user_context_removed","preexisting_contexts_untouched","session_ended"])
 (focused/"browser.json").write_text(json.dumps(focus,indent=2)+"\n");(focused/"network-navigation-timing.json").write_bytes(timing_bytes)
 (ramified/"browser.json").write_text(json.dumps(ramified_focus,indent=2)+"\n");(ramified/"network-navigation-timing.json").write_bytes(timing_bytes)
 for url in browser.get("externalDownloads",[]):
  with urlopen(Request(url,headers={"User-Agent":"GRH-gauss-tail-reviewed-public-link-check"}),timeout=35) as resp:sample=resp.read(1024);external.append({"url":url,"status":resp.status,"first_bytes":len(sample)})
 assert all(x["status"]==200 and x["first_bytes"]>0 for x in external)
 passed=True
except Exception as ex:error=str(ex)
finally:
 if server is not None:server.shutdown();server.server_close();thread.join()
 (run/"requests.json").write_text(json.dumps(requests,indent=2)+"\n");(run/"external-downloads.json").write_text(json.dumps(external,indent=2)+"\n")
 after,after_raw,ah=inventory();(run/"bundle-inventory-after.json").write_bytes(after_raw)
 inputs_same=a.qa_freeze.read_bytes()==qbytes and a.freeze_receipt.read_bytes()==freeze_bytes and all(file_sha(path)==h for path,h in q["files_sha256"].items())
 passed=passed and ih==ah and inputs_same
 common=dict(passed=passed,mode=a.mode,tested_base=base,bundle=str(bundle),files=len(before),bundle_files=len(before),bundle_bytes=sum(x["bytes"] for x in before),inventory_sha256=ih,inventory_before_sha256=ih,inventory_after_sha256=ah,bundle_unchanged=ih==ah,inputs_unchanged=inputs_same,server_stopped=server is None or not thread.is_alive(),freeze_receipt_sha256=sha(freeze_bytes),input_freeze_sha256=sha(qbytes),runner_sha256=file_sha(Path(__file__)),expectations_sha256=sha(e_bytes),lab_module_sha256=file_sha(roles["lab_module"]),native_map_sha256=sha(native_bytes),ramified_map_sha256=sha(ramified_bytes),pdf_map_sha256=sha(pdf_bytes),owned_browser_sha256=file_sha(roles["owned_browser"]),browser_checks_passed=passed,source_HTTP_fallback=False,cleanup=cleanup,error=error,**counters)
 for kind,directory,report,harness in [("full",full,browser,roles["full_harness"]),("focused",focused,focus,roles["focused_harness"]),("ramified",ramified,ramified_focus,roles["ramified_harness"])]:
  record={**common,"schema":"ramified-release-"+kind+"-QA-v1","harness_sha256":file_sha(harness),"browser_result_sha256":file_sha(directory/"browser.json") if(directory/"browser.json").exists()else None,"timing_sha256":file_sha(directory/"network-navigation-timing.json") if(directory/"network-navigation-timing.json").exists()else None,"same_global_session":True,"shared_global_timing":True,"role_paths":{k:str(v) for k,v in roles.items()},"public_native_files":nm["public_files"],"public_ramified_files":rm["public_files"],"public_PDF_files":pm["public_files"],"scope":"Frozen /GRH-research bundle or authorized actual public HTTPS; same owned session/global timing; no source HTTP fallback/auth/publication/old science run."}
  if kind=="ramified":record.update(native_map_sha256=sha(ramified_bytes),public_native_files=rm["public_files"])
  if kind=="full":record.update(strict_integration_groups=len(browser.get("integration",[])),required_inherited_group_names=q["inherited_group_names"],lab_checks=len(browser.get("coherentBandLab",{}).get("checks",[])),lab_layouts=len(browser.get("coherentBandLab",{}).get("layouts",[])))
  else:record.update(checks=len(report.get("checks",[])),checks_passed=sum(x["passed"] for x in report.get("checks",[])),focused_required_group_names=q["focused_required_group_names"] if kind=="focused" else q["ramified_required_group_names"])
  (directory/"receipt.json").write_text(json.dumps(record,indent=2,sort_keys=True)+"\n")
 print(json.dumps({"passed":passed,"run":str(run),"full_receipt_sha256":file_sha(full/"receipt.json"),"focused_receipt_sha256":file_sha(focused/"receipt.json"),"ramified_receipt_sha256":file_sha(ramified/"receipt.json"),"error":error}))
if not passed:raise SystemExit(1)
