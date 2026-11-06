"""Own two ephemeral404 fixtures; preserve all probe evidence and frozen input bytes."""
import pathlib,json,hashlib,http.server,threading,subprocess,os,datetime
from urllib.parse import urlsplit,quote
S=pathlib.Path('/home/iska/Documents/LaTeX-projects/GRH-from-Mac-20261104')
P=S/'planning/gauss-release-20261106/favicon-fix/lane-a'
O=S/'outputs/checks/2026-11-06-gauss-release/favicon-fix/lane-a'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
inputs=[S/'scripts/build_public_site.py',S/'planning/gauss-release-20261106/qa/owned_browser_v2.mjs',S/'planning/gauss-release-20261106/qa/check_browser_v2.mjs',S/'planning/gauss-release-20261106/qa/check_gauss_tail_v2.mjs',S/'planning/gauss-release-20261106/qa/run_browser_v2.py',P/'public-base.control.js',P/'public-base.treatment.js',P/'build_public_site.before.py',P/'build_public_site.proposal.py',P/'icon.svg',P/'single-insertion.js.txt',P/'probe_favicon_v1.mjs',pathlib.Path(__file__)]
before={str(p):sha(p)for p in inputs}
assert before[str(S/'scripts/build_public_site.py')]=='e26d32ed22c99dd83fed43d5d3613b80385069bd3b9bf09018cd12b37792cf36'
run=O/('probe-'+datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%S%fZ'));run.mkdir()
fixture=b'''<!doctype html><html lang="en"><head><script>document.addEventListener("DOMContentLoaded",()=>{window.__probeDOMContentLoaded={readyState:document.readyState,icons:[...document.querySelectorAll('link[rel~="icon"]')].map(x=>({href:x.href,type:x.type}))};},{once:true});</script><script src="/GRH-research/public-base.js"></script><meta charset="utf-8"><title>Owned favicon probe</title><style>body{font:17px system-ui;margin:40px;color:#163b34}pre{white-space:pre-wrap;overflow-wrap:anywhere;background:#eff4ef;padding:20px}img{width:96px;height:96px;image-rendering:auto}</style></head><body><h1>Owned favicon probe</h1><p>Identical page and404 fixture; only the public runtime changes.</p><img id="icon-preview" alt="Declared inline SVG icon" hidden><pre id="state">Waiting for DOM evidence</pre></body></html>'''
(run/'fixture.html').write_bytes(fixture)
requests=[];servers=[];threads=[];origins={}
def handler_for(case,runtime):
 class Handler(http.server.BaseHTTPRequestHandler):
  def do_GET(self):
   path=urlsplit(self.path).path
   if path=='/GRH-research/':status,data,mime=200,fixture,'text/html; charset=utf-8'
   elif path=='/GRH-research/public-base.js':status,data,mime=200,runtime,'text/javascript; charset=utf-8'
   else:status,data,mime=404,b'Not found\n','text/plain; charset=utf-8'
   requests.append(dict(case=case,method='GET',path=path,status=status,bytes=len(data),utc=datetime.datetime.now(datetime.timezone.utc).isoformat()))
   self.send_response(status);self.send_header('Content-Type',mime);self.send_header('Content-Length',str(len(data)));self.send_header('Cache-Control','no-store');self.end_headers();self.wfile.write(data)
  def log_message(self,*args):pass
 return Handler
result=None
try:
 for case in ['control','treatment']:
  server=http.server.ThreadingHTTPServer(('127.0.0.1',0),handler_for(case,(P/('public-base.'+case+'.js')).read_bytes()))
  servers.append(server);thread=threading.Thread(target=server.serve_forever,daemon=True);thread.start();threads.append(thread);origins[case]='http://127.0.0.1:'+str(server.server_port)
 config=dict(output=str(run),origins=origins,runtime_sha256={c:sha(P/('public-base.'+c+'.js'))for c in ['control','treatment']},icon_uri='data:image/svg+xml,'+quote((P/'icon.svg').read_text(),safe=''))
 (run/'config.json').write_text(json.dumps(config,sort_keys=True,indent=2)+'\n')
 env=dict(os.environ,FAVICON_PROBE_CONFIG=json.dumps(config))
 result=subprocess.run(['node',str(P/'probe_favicon_v1.mjs')],env=env,capture_output=True,text=True,timeout=150)
 (run/'stdout.txt').write_text(result.stdout);(run/'stderr.txt').write_text(result.stderr)
except BaseException as e:
 (run/'driver-failure.txt').write_text(repr(e)+'\n')
finally:
 for server in servers:server.shutdown();server.server_close()
 for thread in threads:thread.join(timeout=5)
 (run/'server-requests.json').write_text(json.dumps(requests,sort_keys=True,indent=2)+'\n')
 after={str(p):sha(p)for p in inputs}
 report=dict(passed=result is not None and result.returncode==0 and before==after,scope='Root-cause/fix proposal only. Exact old runtime on404 fixture versus single-insertion treatment. No production file, source/index, shared browser/server or published ref changed.',fixture_sha256=sha(run/'fixture.html'),origins=origins,server_stopped=all(not t.is_alive()for t in threads),ephemeral_loopback_only=True,ports8765and9335_not_modified=True,browser_process_not_killed=True,inputs_before_sha256=before,inputs_after_sha256=after,inputs_unchanged=before==after,returncode=result.returncode if result else None,browser_probe_sha256=sha(run/'browser-probe.json')if(run/'browser-probe.json').exists()else None,requests_sha256=sha(run/'server-requests.json'),public_builder_unmodified_sha256=sha(S/'scripts/build_public_site.py'),proposal_sha256=sha(P/'build_public_site.proposal.py'),single_insertion=True,all_other_runtime_bytes_identical=True,run=str(run))
 (run/'receipt.json').write_text(json.dumps(report,sort_keys=True,indent=2)+'\n')
 print(json.dumps(dict(passed=report['passed'],run=str(run),receipt_sha256=sha(run/'receipt.json'),browser_probe_sha256=report['browser_probe_sha256'],server_stopped=report['server_stopped'],inputs_unchanged=report['inputs_unchanged'])))
 if not report['passed']:raise SystemExit(1)
