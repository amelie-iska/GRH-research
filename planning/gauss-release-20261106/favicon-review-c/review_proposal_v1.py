"""Read-only peer audit of exact icon insertion, raw causal probe and QA parity delta."""
from pathlib import Path
from datetime import datetime,timezone
from urllib.parse import unquote
import ast,hashlib,json,re,xml.etree.ElementTree as ET
R=Path("/home/iska/Documents/LaTeX-projects/GRH-from-Mac-20261104")
A=R/"planning/gauss-release-20261106/favicon-fix/lane-a"
RUN=R/"outputs/checks/2026-11-06-gauss-release/favicon-fix/lane-a/probe-20261106T114826855728Z"
P=Path("/home/iska/Documents/LaTeX-projects/GRH-publication-20261106-gauss-tail/outputs/publication/20261106-gauss-tail/release-preparation-v1")
OUT=R/"outputs/checks/2026-11-06-gauss-release/favicon-review-c/proposal-v1"
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
load=lambda p:json.loads(p.read_bytes())
pin=lambda p:{"path":str(p),"sha256":sha(p)}
assert not OUT.exists()
expected={A/"build_public_site.proposal.py":"0065a3a1977cd9b1ef1ecd08c6f334d18c9d1375f4c02a6c40ce4c789a6a0f5d",A/"public-base.treatment.js":"c37b2d5d630e794ccfef01ca316385da755622952adae774c4ce569cbdc13d71",R/"scripts/build_public_site.py":"e26d32ed22c99dd83fed43d5d3613b80385069bd3b9bf09018cd12b37792cf36",R/"planning/gauss-release-20261106/qa/run_browser_v3.py":"c9e3215b94bb05ab68cb3e6a96a9090dfa85d731732465e99843f53ef90f3a17",R/"planning/gauss-release-20261106/qa/freeze_inputs_v4.py":"d86e6b3a48d3689ba4cc87178a336c7283fb2a345269ee7dac2dbc0ef90f7493",RUN/"receipt.json":"7863a6c53de51ab42e517aa2279488ceb3a9dfa28093c1aed542a8572be6c298"}
for p,v in expected.items():assert sha(p)==v,p
old=(R/"scripts/build_public_site.py").read_bytes();new=(A/"build_public_site.proposal.py").read_bytes();ins=(A/"single-insertion.js.txt").read_bytes()
assert len(ins)==651 and old.count(b"(()=>{")==1 and new==old.replace(b"(()=>{",b"(()=>{"+ins,1)
def runtime(p):
 return next(ast.literal_eval(x.value)for x in ast.walk(ast.parse(p.read_text()))if isinstance(x,ast.Assign)and any(isinstance(y,ast.Name)and y.id=="runtime"for y in x.targets)).encode()
control=runtime(R/"scripts/build_public_site.py");treatment=runtime(A/"build_public_site.proposal.py")
assert control==(A/"public-base.control.js").read_bytes() and treatment==(A/"public-base.treatment.js").read_bytes()
assert treatment==control.replace(b"(()=>{",b"(()=>{"+ins,1) and treatment.replace(ins,b"",1)==control
uri=re.search(rb"icon.href='([^']+)'",ins).group(1).decode();assert uri.startswith("data:image/svg+xml,")
svg=unquote(uri.split(",",1)[1]);assert svg==(A/"icon.svg").read_text()
s=ET.fromstring(svg);assert s.tag=="{http://www.w3.org/2000/svg}svg" and s.attrib["width"]==s.attrib["height"]=="32"
assert {x.tag.rsplit("}",1)[-1]for x in s.iter()}=={"svg","rect","path"}
assert not any(k.lower().startswith("on")or k.lower().endswith("href")for x in s.iter()for k in x.attrib)
qa=R/"planning/gauss-release-20261106/qa"
v2=(qa/"run_browser_v2.py").read_bytes();v3=(qa/"run_browser_v3.py").read_bytes()
a=b'if path=="/favicon.ico":self.send_response(204);self.end_headers();return';b=a.replace(b"204",b"404")
assert v2.count(a)==1 and v3==v2.replace(a,b,1)
f3=(qa/"freeze_inputs_v3.py").read_bytes();f4=(qa/"freeze_inputs_v4.py").read_bytes()
assert f3.count(b"run_browser_v2.py")==2 and f3.count(b"freeze_inputs_v3.py")==1
assert f4==f3.replace(b"run_browser_v2.py",b"run_browser_v3.py").replace(b"freeze_inputs_v3.py",b"freeze_inputs_v4.py")
for p in [A/"build_public_site.proposal.py",qa/"run_browser_v3.py",qa/"freeze_inputs_v4.py"]:ast.parse(p.read_text())
r=load(RUN/"receipt.json");summary=load(RUN/"browser-probe.json");cfg=load(RUN/"config.json")
assert r["passed"] and r["returncode"]==0 and r["server_stopped"] and r["inputs_unchanged"]
assert r["inputs_before_sha256"]==r["inputs_after_sha256"]
for n,v in r["inputs_before_sha256"].items():assert sha(Path(n))==v,n
assert sha(RUN/"fixture.html")==r["fixture_sha256"] and sha(RUN/"browser-probe.json")==r["browser_probe_sha256"] and sha(RUN/"server-requests.json")==r["requests_sha256"]
assert summary["passed"]
for n,v in summary["files_sha256"].items():assert sha(RUN/n)==v,n
c=load(RUN/"control.json");t=load(RUN/"treatment.json")
assert c["passed"] and t["passed"] and cfg["icon_uri"]==uri
assert c["DOM"]["iconCount"]==0 and len(c["origin_favicon_requests"])==len(c["HTTP_errors"])==1
assert c["HTTP_errors"][0]["status"]==404 and c["HTTP_errors"][0]["url"]==cfg["origins"]["control"]+"/favicon.ico"
assert t["DOM"]["iconCount"]==1 and t["DOM"]["DOMContentLoaded"]["icons"]==[{"href":uri,"type":"image/svg+xml"}]
assert t["DOM"]["icon"]["href"]==uri and t["DOM"]["icon"]["type"]=="image/svg+xml" and t["DOM"]["icon"]["connected"]
assert t["DOM"]["svg"]["source"]==svg and not t["DOM"]["svg"]["parserError"] and t["imageDecode"]=={"width":32,"height":32,"complete":True}
assert not t["origin_favicon_requests"] and not t["HTTP_errors"]
for x in [c,t]:
 assert x["no_error_filter"] and not x["requests_blocked_or_intercepted"] and not x["prefs_changed"]
 assert not x["fetch_errors"] and not x["page_errors"] and not x["pending_final"]
 assert x["idleWaits"][0]["quiet_ms"]==750 and x["idleWaits"][0]["timeout_ms"]==30000 and not x["idleWaits"][0]["pending_at_exit"]
 assert all(x["cleanup"][k]is True for k in ["owned_tab_closed","owned_user_context_removed","preexisting_contexts_untouched","session_ended"])and not x["cleanup"]["errors"]
assert cfg["origins"]["control"]!=cfg["origins"]["treatment"] and c["events"][0]["context"]!=t["events"][0]["context"]
requests=load(RUN/"server-requests.json")
assert [(x["case"],x["path"],x["status"])for x in requests]==[("control","/GRH-research/",200),("control","/GRH-research/public-base.js",200),("control","/favicon.ico",404),("treatment","/GRH-research/",200),("treatment","/GRH-research/public-base.js",200)]
harnesspins={qa/"check_browser_v2.mjs":"2779842b863c612c4cb92b084af451c54d7d69f6543efdee969f100795fc5f4f",qa/"check_gauss_tail_v2.mjs":"d3b110c8973d01a124a040a3beae31290dfa2a3775a36599b89e558bd5e6e54a",qa/"check_lab_v1.mjs":"094fbfb28a46da943ced6f16ed40207e1fc97a57ff97cd780cc085392999247d",qa/"owned_browser_v2.mjs":"2683eb4027236a54ffb7f06090288aaecf800e7004a8166281d60025bef59256"}
for p,v in harnesspins.items():assert sha(p)==v,p
states=load(P/"baseline-v1.json")["protected_prior_states"];assert len(states)==13
for x in states:assert sha(Path(x["HEAD_path"]))==x["HEAD_file_sha256"] and sha(Path(x["index_path"]))==x["index_sha256"]
oldindex=Path(Path(str(P.parents[3]/".git")).read_text().strip().split(": ",1)[1])/"index"
assert sha(oldindex)=="ce6a9b715f5c38e6f1edb9eb90936f50acc8884f0bb8575abd667bd703b7e9c6"
OUT.mkdir(parents=True)
review=R/"planning/gauss-release-20261106/favicon-review-c/PROPOSAL_REVIEW-v1.md"
text="""# Independent favicon proposal review

The exact proposal0065a3a1 is accepted as a minimal runtime correction candidate. It inserts exactly651bytes at the existing adapter IIFE start. Removing that insertion restores the full original builder and public-base.js bytes. Existing URL mapping, fetch/Request/DOM hooks, runtime injection, scientific copying and exports are untouched.

It declares one original32×32 inline SVG only when no icon link exists, using rel=icon,type=image/svg+xml and a self-contained data URI with svg/rect/path only. It has no script, event handler or external resource. It runs before the prior adapter code in the first synchronous head runtime. The prior diagnosis showed all22 public HTML documents load that runtime once and declare no icon.

I read the complete Python driver and BiDi probe. Two different ephemeral no-store404 origins and fresh owned contexts use identical fixture bytes. Raw server requests and unfiltered browser events reproduce one origin favicon404 in control and no favicon request/HTTP error in treatment. The treatment icon exists byDOMContentLoaded and decodes as32×32. No fetch/page error or pending request remains. Context/session cleanup, preexisting context preservation, server shutdown and exact input hashes are evidenced. This is a focused causal probe, not a substitute for complete staged/LIVE QA or a universal browser guarantee. No screenshot visual approval is claimed by this reviewer.

Runner3 is exactly204→404 for the stage-origin favicon. It strengthens parity without changing HTTP filtering,750ms/30sidle or other assertions. Freezer4 changes only its two runner roles and own producer filename. The full220, focused40, lab58/54 and owned-browser source hashes are unchanged. Fresh maps and input freeze must bind the actual patch bundle and these new helper versions.

No proposal was applied or executed by this reviewer. All14 prior state indices are exact, including the published release's frozen249-file index. Root may apply only these reviewed bytes in its new b6-based patch worktree after its own approval. The old635-file bundle remains immutable, and the patch must preserve all other634 leaves. Scientific PDFs/native HTML/source/assets need no rebuild. Root payload/index/boundary review, full strict staged QA and hosted/LIVE QA remain separate gates; the failed original live run remains preserved as a failure.
"""
with review.open("x")as f:f.write(text)
out={"schema":"gauss-tail-favicon-runtime-proposal-independent-review-v1","passed":True,"scope":"Exact candidate plus focused causal probe and QA parity changes; no patch application/publication/full-QA authorization","proposal":pin(A/"build_public_site.proposal.py"),"runtime":pin(A/"public-base.treatment.js"),"probe":pin(RUN/"receipt.json"),"QA_runner":pin(qa/"run_browser_v3.py"),"QA_freezer":pin(qa/"freeze_inputs_v4.py"),"review":pin(review),"review_producer":pin(Path(__file__)),"input_sha256":{str(p):sha(p)for p in list(expected)+list(harnesspins)+[A/"icon.svg",A/"single-insertion.js.txt",A/"probe_favicon_v1.mjs",A/"run_probe_v1.py",RUN/"browser-probe.json",RUN/"control.json",RUN/"treatment.json",RUN/"server-requests.json"]},"exact_single_insertion_bytes":651,"all_other_adapter_bytes_exact":True,"self_contained_original_SVG_only":True,"control_origin404_reproduced":1,"treatment_favicon_HTTP_fetch_page_errors":0,"fresh_contexts_origins_and_cleanup_verified":True,"full220_focused40_lab58_54_unchanged":True,"runner_stage204_to404_only":True,"freezer_runner3_self4_only":True,"protected_prior_states_exact":14,"prior_frozen249_index_sha256":sha(oldindex),"no_Git_mutation_patch_application_browser_network_auth_by_reviewer":True,"fresh_bundle_bindings_full_strict_stage_and_LIVE_QA_required":True,"old635_bundle_immutable_other634_patch_leaves_must_match":True,"publication_authorized":False,"created_utc":datetime.now(timezone.utc).isoformat()}
p=OUT/"acceptance-v1.json"
with p.open("x")as f:json.dump(out,f,indent=2,sort_keys=True);f.write("\n")
print(json.dumps({"passed":True,"receipt":str(p.relative_to(R)),"sha256":sha(p),"review_sha256":sha(review),"producer_sha256":sha(Path(__file__))},indent=2))
