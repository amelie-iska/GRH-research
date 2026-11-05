"""Read-only frozen-bundle/live browser QA. Every invocation gets a new output."""
from pathlib import Path
from http.server import ThreadingHTTPServer,SimpleHTTPRequestHandler
from urllib.parse import urlsplit,unquote
from urllib.request import Request,urlopen
from datetime import datetime,timezone
import argparse,hashlib,json,os,subprocess,threading
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[2]
OUT=ROOT/'outputs/checks/2026-11-05-signed-weights/live-qa'
sha=lambda b:hashlib.sha256(b).hexdigest()
p=argparse.ArgumentParser();p.add_argument('--mode',choices=['stage','live'],required=True);p.add_argument('--bundle',type=Path,required=True);p.add_argument('--inventory-sha256',required=True);p.add_argument('--freeze-receipt',type=Path,required=True);p.add_argument('--publication-receipt',type=Path);p.add_argument('--harness',type=Path,default=HERE/'check_browser_v1.mjs');a=p.parse_args()
bundle=a.bundle.resolve();expected=bundle;assert bundle.is_dir() and bundle.name.startswith('site-bundle-');assert bundle.is_relative_to(Path('/home/iska/Documents/LaTeX-projects')) and not bundle.is_relative_to(ROOT);assert '/outputs/publication/' in str(bundle),'Use an explicit frozen publication bundle, never source web/'
assert a.freeze_receipt.is_file();freeze_bytes=a.freeze_receipt.read_bytes()
run=OUT/(a.mode+'-browser-'+datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ'));run.mkdir(parents=True,exist_ok=False)
def inventory():
 rows=[dict(path=f.relative_to(bundle).as_posix(),bytes=f.stat().st_size,sha256=sha(f.read_bytes())) for f in sorted(bundle.rglob('*')) if f.is_file()]
 raw=(json.dumps(rows,separators=(',',':'),sort_keys=True)+'\n').encode();return rows,raw,sha(raw)
before,raw,before_hash=inventory();(run/'bundle-inventory-before.json').write_bytes(raw);assert before_hash==a.inventory_sha256,'Bundle does not match frozen inventory'
assert not any((bundle/n).is_symlink() for n in [r['path'] for r in before])
script=a.harness.resolve();script_bytes=script.read_bytes();(run/'executed-harness.mjs').write_bytes(script_bytes);(run/'freeze-receipt.json').write_bytes(freeze_bytes);requests=[];server=None;thread=None
if a.mode=='stage':
 class Handler(SimpleHTTPRequestHandler):
  def do_GET(self):
   path=unquote(urlsplit(self.path).path);requests.append(dict(method='GET',path=path))
   if path=='/favicon.ico':self.send_response(204);self.end_headers();return
   super().do_GET()
  def do_HEAD(self):requests.append(dict(method='HEAD',path=unquote(urlsplit(self.path).path)));super().do_HEAD()
  def translate_path(self,path):
   name=unquote(urlsplit(path).path)
   if not name.startswith('/GRH-research/'):return str(bundle/'__outside_project_prefix__')
   target=(bundle/name[len('/GRH-research/'):]).resolve();return str(target) if target.is_relative_to(bundle) else str(bundle/'__outside_fixture__')
  def log_message(self,*args):pass
 server=ThreadingHTTPServer(('127.0.0.1',0),Handler);thread=threading.Thread(target=server.serve_forever,daemon=True);thread.start();base='http://127.0.0.1:'+str(server.server_port)+'/GRH-research'
else:
 assert a.publication_receipt is not None,'Live mode requires new-release publication receipt and explicit root go signal before invocation'
 receipt=json.loads(a.publication_receipt.read_text());assert receipt['published'] is True and receipt['target']=='pages'
 assert a.publication_receipt.resolve().is_relative_to(expected.parent/'release-preparation-v1')
 assert 'profile-uniformity.html' in receipt['changed_paths'] and receipt['changed_file_sha256']['profile-uniformity.html']==sha((bundle/'profile-uniformity.html').read_bytes())
 (run/'publication-receipt.json').write_bytes(a.publication_receipt.read_bytes());base='https://amelie-iska.github.io/GRH-research'
passed=False;error=None;external=[]
try:
 env=dict(os.environ,PROFILE_QA_URL=base,PROFILE_QA_OUTPUT=str(run));result=subprocess.run(['node',str(script)],cwd=ROOT,env=env,capture_output=True,text=True,timeout=300);(run/'stdout.txt').write_text(result.stdout);(run/'stderr.txt').write_text(result.stderr)
 assert result.returncode==0,'Browser worker failed; all evidence preserved'
 browser=json.loads((run/'browser.json').read_text());assert browser['passed']
 for url in browser.get('externalDownloads',[]):
  with urlopen(Request(url,headers={'User-Agent':'GRH-signed-weights-reviewed-link-check'}),timeout=35) as r:sample=r.read(1024);external.append(dict(url=url,status=r.status,first_bytes=len(sample)))
 assert all(x['status']==200 and x['first_bytes']>0 for x in external)
 passed=True
except Exception as e:error=str(e)
finally:
 if server is not None:server.shutdown();server.server_close();thread.join()
 (run/'requests.json').write_text(json.dumps(requests,indent=2)+'\n');(run/'external-downloads.json').write_text(json.dumps(external,indent=2)+'\n')
 after,after_raw,after_hash=inventory();(run/'bundle-inventory-after.json').write_bytes(after_raw)
 unchanged=after_hash==before_hash and script.read_bytes()==script_bytes and a.freeze_receipt.read_bytes()==freeze_bytes
 passed=passed and unchanged
 record={'passed':passed,'mode':a.mode,'tested_base':base,'bundle':str(bundle),'bundle_files':len(before),'bundle_bytes':sum(x['bytes'] for x in before),'inventory_before_sha256':before_hash,'inventory_after_sha256':after_hash,'bundle_unchanged':before_hash==after_hash,'freeze_receipt_sha256':sha(freeze_bytes),'harness_path':str(script),'harness_sha256':sha(script_bytes),'runner_sha256':sha(Path(__file__).read_bytes()),'inputs_unchanged':unchanged,'error':error,'browser_result_sha256':sha((run/'browser.json').read_bytes()) if (run/'browser.json').exists() else None,'server_stopped':server is None or not thread.is_alive(),'strict_integration_groups':browser.get('strict_integration_groups') if passed else None,'scope':'Signed-weights frozen-bundle/public-release UI and bytes only. Strict global WS timing/quiet-idle preserved. No arithmetic rerun, proof of new mathematics or publication performed.'}
 target=run/'receipt.json';target.write_text(json.dumps(record,indent=2)+'\n');print(json.dumps({'passed':passed,'run':str(run),'receipt_sha256':sha(target.read_bytes()),'error':error}))
if not passed:raise SystemExit(1)
