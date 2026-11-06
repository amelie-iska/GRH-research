#!/usr/bin/env python3
"""Run five isolated source-bound editions; no promotion or dependency changes."""
from pathlib import Path
import concurrent.futures, hashlib,json,os,re,subprocess,sys
ROOT=Path("/home/iska/Documents/LaTeX-projects/GRH-from-Mac-20261104")
HERE=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def main():
 out=ROOT/"outputs/checks/2026-11-06-gauss-book/builds/run-v3"
 assert not out.exists();out.mkdir(parents=True)
 marker=ROOT/"outputs/checks/2026-11-06-gauss-book/build-admin/marker-receipt-v1.json";assert marker.is_file()
 integration=ROOT/"outputs/checks/2026-11-06-gauss-book/root/source-integration-v4.json"
 rec=json.loads(integration.read_text());assert rec["passed"]
 guards={x["path"]:x["after"] for x in rec["edits"]}
 for name,digest in guards.items():assert sha(ROOT/name)==digest,(name,"Integrated source changed")
 oldlive=ROOT/"web/book/main.html";old_live_sha=sha(oldlive)
 env={**os.environ,"PYTHONDONTWRITEBYTECODE":"1","OMP_NUM_THREADS":"1","OPENBLAS_NUM_THREADS":"1"}
 physical={"physical-core":"df49c3f938ab80f80e4c0bb2efb4f71004a2d311dc21f952ecd45077dd35f939","physical-details":"4713c2c4e8496a87a8678406d2d43f02ab0bf82e4152fed15938aef52b3b9bf4","coherent-core":"5b3ab5c38b5c9130867793ac2e21c7dbc60560bc7d4eadbcc40fb1f334659f6c","coherent-details":"92dfe3077dffa048471b0705539bd82b2648c2e4b021c331c2753b6fb655176f"}
 jobs=[("book-pdf",["python3",str(HERE/"build_book_pdf_v1.py"),"--consume-book","--output",str(out/"book-pdf")])]
 for ed in ["concise","extended"]:
  jobs.append(("focused-"+ed,["python3",str(ROOT/"scripts/build_remote_articles.py"),"--edition",ed,"--output",str(out/("focused-"+ed))]))
  cmd=["python3",str(ROOT/"planning/physical-sieve-20261105/builds/build_notes_v1.py"),"--edition",ed,"--root-go","--output",str(out/("notes-"+ed))]
  for key,value in physical.items():cmd+=["--"+key+"-sha",value]
  jobs.append(("notes-"+ed,cmd))
 prior=json.loads((ROOT/"outputs/checks/2026-11-06-gauss-book/builds/run-v2/aggregate.json").read_text())
 results={n:prior["results"][n] for n in ["focused-concise","notes-concise"]}
 for n,x in results.items():
  assert x["passed"] and sha(Path(x["pdf"]))==x["pdf_sha256"]
  rr=json.loads(Path(x["record"]).read_text())
  for name,digest in rr["source_sha256"].items():assert sha(ROOT/name)==digest,("Reused concise source changed",n,name)
 jobs=[j for j in jobs if not j[0].endswith("concise")]
 def run(job):
  name,cmd=job
  with (out/(name+".stdout.log")).open("x") as f:
   proc=subprocess.run(["nice","-n","15"]+cmd,cwd=ROOT,env=env,stdout=f,stderr=subprocess.STDOUT)
  records=out/name/"build-record.json"
  result=dict(returncode=proc.returncode,command=cmd,record=str(records),record_sha256=sha(records) if records.exists() else None)
  if proc.returncode==0:
   r=json.loads(records.read_text());assert r["passed"]
   pdfs=list((out/name).glob("*.pdf"));assert len(pdfs)==1
   text=subprocess.check_output(["pdftotext",str(pdfs[0]),"-"],text=True)
   normalize=lambda s:re.sub("[^a-z0-9]","",s.lower())
   for marker in ["A signed short-divisor tail from a physical cubic matrix","The exact discrete top prefix, with every ray retained","Direct original-prefix cutoff reduction"]:
    assert normalize(marker) in normalize(text),(name,marker)
   result.update(passed=True,pdf=str(pdfs[0]),pdf_sha256=sha(pdfs[0]),pages=int(re.search(r"Pages:\s+(\d+)",subprocess.check_output(["pdfinfo",str(pdfs[0])],text=True))[1]))
  else:result["passed"]=False
  return name,result
 with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
  futures=[pool.submit(run,j) for j in jobs]
  for fut in concurrent.futures.as_completed(futures):
   name,result=fut.result();results[name]=result
   (out/"results-so-far.json").write_text(json.dumps(results,indent=2)+"\n")
   print(json.dumps(dict(name=name,passed=result["passed"],pages=result.get("pages"))),flush=True)
 assert all(sha(ROOT/name)==digest for name,digest in guards.items())
 assert sha(oldlive)==old_live_sha
 passed=len(results)==5 and all(x["passed"] for x in results.values())
 record=dict(passed=passed,results=results,source_guard_sha256=guards,old_live_HTML_sha256=old_live_sha,source_integration_sha256=sha(integration),marker_receipt_sha256=sha(marker),producer_sha256=sha(Path(__file__)),production_promoted=False,new_Lean_declarations=0)
 (out/"aggregate.json").write_text(json.dumps(record,indent=2)+"\n")
 print(json.dumps(dict(passed=passed,record=str(out/"aggregate.json"))),flush=True)
 if not passed:raise SystemExit(1)
if __name__=="__main__":main()
