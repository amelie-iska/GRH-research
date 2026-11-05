from pathlib import Path
from http.server import ThreadingHTTPServer,SimpleHTTPRequestHandler
from datetime import datetime,timezone
import threading,subprocess,os,json,hashlib
ROOT=Path(__file__).resolve().parents[3];HERE=Path(__file__).resolve().parent
run=ROOT/'outputs/checks/2026-11-05-signed-divisor/ui'/('browser-'+datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ'));run.mkdir(parents=True,exist_ok=False)
files=[ROOT/('web/signed-divisor.'+ext) for ext in ('html','css','mjs')]+list((ROOT/'web/data/signed-divisor').iterdir());pins={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in files};requests=[]
class Handler(SimpleHTTPRequestHandler):
 def __init__(self,*args,**kwargs):super().__init__(*args,directory=str(ROOT/'web'),**kwargs)
 def log_message(self,*args):pass
 def do_GET(self):
  requests.append(self.path)
  if self.path=='/favicon.ico':self.send_response(204);self.end_headers();return
  super().do_GET()
server=ThreadingHTTPServer(('127.0.0.1',0),Handler);thread=threading.Thread(target=server.serve_forever,daemon=True);thread.start()
try:
 r=subprocess.run(['node',str(HERE/'check_browser_v3.mjs')],cwd=ROOT,env={**os.environ,'SD_QA_URL':'http://127.0.0.1:'+str(server.server_port),'SD_QA_OUTPUT':str(run)},capture_output=True,text=True,timeout=240)
 (run/'stdout.txt').write_text(r.stdout);(run/'stderr.txt').write_text(r.stderr)
finally:server.shutdown();server.server_close();thread.join()
passed=r.returncode==0 and all(hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h for p,h in pins.items())
receipt=dict(passed=passed,returncode=r.returncode,inputs=pins,inputs_unchanged=all(hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h for p,h in pins.items()),requests=requests,harness_sha256=hashlib.sha256((HERE/'check_browser_v3.mjs').read_bytes()).hexdigest(),runner_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),browser_sha256=hashlib.sha256((run/'browser.json').read_bytes()).hexdigest() if (run/'browser.json').exists() else None,server_stopped=not thread.is_alive(),scope='NEW standalone UI source QA, read-only frozen display projection; no raw science or publication')
(run/'receipt.json').write_text(json.dumps(receipt,indent=2)+'\n');print(json.dumps(dict(passed=passed,path=str(run),receipt_sha256=hashlib.sha256((run/'receipt.json').read_bytes()).hexdigest(),stderr=r.stderr[-2000:])))
if not passed:raise SystemExit(1)
