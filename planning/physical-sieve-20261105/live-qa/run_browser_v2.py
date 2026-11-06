"""Frozen bundle/live QA with explicit root-count SHA binding; no auth/ref/publication writes."""
from pathlib import Path
from http.server import ThreadingHTTPServer,SimpleHTTPRequestHandler
from urllib.parse import urlsplit,unquote
from urllib.request import Request,urlopen
from datetime import datetime,timezone
import argparse,hashlib,json,os,subprocess,threading,re
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[2]
OUT=ROOT/'outputs/checks/2026-11-05-physical-sieve/live-qa'
sha=lambda b:hashlib.sha256(b).hexdigest()
p=argparse.ArgumentParser();p.add_argument('--mode',choices=['stage','live'],required=True);p.add_argument('--bundle',type=Path,required=True);p.add_argument('--inventory-sha256',required=True);p.add_argument('--freeze-receipt',type=Path,required=True);p.add_argument('--publication-receipt',type=Path);p.add_argument('--harness',type=Path,default=HERE/'check_browser_v1.mjs');p.add_argument('--expectations',type=Path,default=HERE/'expectations-v1.json');p.add_argument('--expectations-sha',required=True);a=p.parse_args()
bundle=a.bundle.resolve();assert bundle.is_dir() and bundle.name.startswith('site-bundle-') and bundle.is_relative_to(Path('/home/iska/Documents/LaTeX-projects')) and not bundle.is_relative_to(ROOT) and '/outputs/publication/'in str(bundle),'Use frozen new release bundle, never sourceweb'
freeze_bytes=a.freeze_receipt.read_bytes();expect_bytes=a.expectations.read_bytes();assert sha(expect_bytes)==a.expectations_sha,'Root-approved explicit expectations SHA required';expected=json.loads(expect_bytes);assert expected['schema']=='physical-sieve-release-expectations-v1' and expected['old_math_nodes']==8552 and len(expected['rma_anchors'])==40 and expected['prior_harness_sha256']=='57640381b26548582c0012ca6577fcce82af68500d34497686700e698fae4e98'
run=OUT/(a.mode+'-browser-'+datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ'));run.mkdir(parents=True,exist_ok=False)
def inventory():
 rows=[dict(path=f.relative_to(bundle).as_posix(),bytes=f.stat().st_size,sha256=sha(f.read_bytes())) for f in sorted(bundle.rglob('*')) if f.is_file()];raw=(json.dumps(rows,separators=(',',':'),sort_keys=True)+'\n').encode();return rows,raw,sha(raw)
before,raw,before_hash=inventory();(run/'bundle-inventory-before.json').write_bytes(raw);assert before_hash==a.inventory_sha256 and not any((bundle/r['path']).is_symlink() for r in before)
script=a.harness.resolve();script_bytes=script.read_bytes();(run/'executed-harness.mjs').write_bytes(script_bytes);(run/'freeze-receipt.json').write_bytes(freeze_bytes);(run/'root-count-expectations.json').write_bytes(expect_bytes)
requests=[];server=None;thread=None;browser={};passed=False;error=None;external=[];base=None
try:
 for name,pages in [('book.pdf',expected['book_pages']),('concise.pdf',expected['focused_pages'][0]),('extended.pdf',expected['focused_pages'][1])]:
  info=subprocess.check_output(['pdfinfo',str(bundle/name)],text=True);assert int(re.search(r'Pages:\s+(\d+)',info)[1])==pages,('Frozen PDF count mismatch',name)
 expected['assets']={name:sha((bundle/name.lstrip('/')).read_bytes()) for name in ['/signed-divisor.html', '/book.pdf', '/book/sources/rough-mask-core.tex', '/book/sources/rough-mask-details.tex', '/book/sources/coherent-main-core.tex', '/book/sources/coherent-main-details.tex', '/book/sources/physical-sieve-core.tex', '/book/sources/physical-sieve-details.tex', '/physical-sieve-model.mjs', '/quadratic-pivot.html', '/quadratic-pivot.css', '/quadratic-pivot.mjs']}
 for rel,h in expected['ui_source_hashes'].items():
  if rel.endswith(('.css','.mjs')):assert sha((bundle/rel.removeprefix('web/')).read_bytes())==h,('Frozen UI differs from accepted source',rel)
 (run/'qa-expectations.json').write_text(json.dumps(expected,sort_keys=True,indent=2)+'\n')
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
  assert a.publication_receipt is not None,'New publication receipt and explicit rootLIVEGO required';publication=json.loads(a.publication_receipt.read_bytes());assert publication['published'] is True and publication['target']=='pages' and publication['force'] is False
  assert a.publication_receipt.resolve().is_relative_to(bundle.parent/'release-preparation-v1') and all(path in publication['changed_paths'] and publication['changed_file_sha256'][path]==sha((bundle/path).read_bytes()) for path in ['book/main.html','quadratic-pivot.mjs','physical-sieve-model.mjs'])
  (run/'publication-receipt.json').write_bytes(a.publication_receipt.read_bytes());base='https://amelie-iska.github.io/GRH-research'
 result=subprocess.run(['node',str(script)],cwd=ROOT,env={**os.environ,'PROFILE_QA_URL':base,'PROFILE_QA_OUTPUT':str(run),'SIGNED_DIVISOR_QA_EXPECTATIONS':str(run/'qa-expectations.json')},capture_output=True,text=True,timeout=300)
 (run/'stdout.txt').write_text(result.stdout);(run/'stderr.txt').write_text(result.stderr);assert result.returncode==0,'Browser worker failed; all evidence preserved'
 browser=json.loads((run/'browser.json').read_bytes());assert browser['passed']
 for url in browser.get('externalDownloads',[]):
  with urlopen(Request(url,headers={'User-Agent':'GRH-physical-sieve-reviewed-link-check'}),timeout=35) as r:sample=r.read(1024);external.append(dict(url=url,status=r.status,first_bytes=len(sample)))
 assert all(r['status']==200 and r['first_bytes']>0 for r in external);passed=True
except Exception as e:error=str(e)
finally:
 if server is not None:server.shutdown();server.server_close();thread.join()
 (run/'requests.json').write_text(json.dumps(requests,indent=2)+'\n');(run/'external-downloads.json').write_text(json.dumps(external,indent=2)+'\n')
 after,after_raw,after_hash=inventory();(run/'bundle-inventory-after.json').write_bytes(after_raw);unchanged=after_hash==before_hash and script.read_bytes()==script_bytes and a.freeze_receipt.read_bytes()==freeze_bytes and a.expectations.read_bytes()==expect_bytes;passed=passed and unchanged
 record=dict(passed=passed,mode=a.mode,tested_base=base,bundle=str(bundle),bundle_files=len(before),bundle_bytes=sum(x['bytes'] for x in before),inventory_before_sha256=before_hash,inventory_after_sha256=after_hash,bundle_unchanged=before_hash==after_hash,freeze_receipt_sha256=sha(freeze_bytes),explicit_root_counts_sha256=sha(expect_bytes),harness_path=str(script),harness_sha256=sha(script_bytes),runner_sha256=sha(Path(__file__).read_bytes()),inputs_unchanged=unchanged,error=error,browser_result_sha256=sha((run/'browser.json').read_bytes()) if(run/'browser.json').exists()else None,server_stopped=server is None or not thread.is_alive(),strict_integration_groups=browser.get('strict_integration_groups'),navigation_count=browser.get('navigation_count'),initial_navigation_count=browser.get('initial_navigation_count'),actual_departure_count=browser.get('actual_departure_count'),expected_book_pages=expected['book_pages'],expected_MathML=expected['math_nodes'],expected_tables=expected['tables'],scope='New physical-sieve frozen-bundle/publicHTTPS only; all161 legacy groups plus additive current inspector/coherent proof/source checks. Counts from accepted artifacts. Exact globalWS750msquiet/30sidle/errorguards unchanged; no raw science/auth/ref/publication.')
 target=run/'receipt.json';target.write_text(json.dumps(record,indent=2)+'\n');print(json.dumps(dict(passed=passed,run=str(run),receipt_sha256=sha(target.read_bytes()),error=error)))
if not passed:raise SystemExit(1)
