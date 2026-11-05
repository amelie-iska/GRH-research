from pathlib import Path
from http.server import ThreadingHTTPServer,SimpleHTTPRequestHandler
from urllib.parse import urlsplit,unquote
import threading,subprocess,os,json,datetime
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[2]
OUT=ROOT/'outputs/checks/2026-11-05-arithmetic-learning/ui-learning';RUN=OUT/('browser-'+datetime.datetime.now().strftime('%Y%m%dT%H%M%S%f'));RUN.mkdir();requests=[]
class Handler(SimpleHTTPRequestHandler):
 def do_GET(self):
  name=unquote(urlsplit(self.path).path);requests.append(name)
  if name=='/favicon.ico':self.send_response(204);self.end_headers();return
  if name=='/GRH-research/arithmetic-learning.html':
   body=(ROOT/'web/arithmetic-learning.html').read_text().replace('href="/','href="/GRH-research/').replace('src="/','src="/GRH-research/').encode();self.send_response(200);self.send_header('Content-Type','text/html');self.send_header('Content-Length',str(len(body)));self.end_headers();self.wfile.write(body);return
  super().do_GET()
 def translate_path(self,path):
  name=unquote(urlsplit(path).path).removeprefix('/GRH-research/');base=(ROOT/'web').resolve();p=(base/name.lstrip('/')).resolve();return str(p) if p.is_relative_to(base) else str(base/'__outside_fixture__')
 def log_message(self,*args):pass
server=ThreadingHTTPServer(('127.0.0.1',0),Handler);thread=threading.Thread(target=server.serve_forever,daemon=True);thread.start()
try:
 env=dict(os.environ,LEARNING_QA_URL='http://127.0.0.1:'+str(server.server_port),LEARNING_QA_RUN_DIR=str(RUN));p=subprocess.run(['node',str(HERE/'check_browser.mjs')],cwd=ROOT,env=env,capture_output=True,text=True);(RUN/'stdout.txt').write_text(p.stdout);(RUN/'stderr.txt').write_text(p.stderr);print('Browser QA:',RUN);print(p.stdout)
 if p.stderr:print(p.stderr)
 assert p.returncode==0,'Browser QA failed; logs preserved'
 assert '/GRH-research/data/arithmetic-learning.json' in requests,'Project-prefix fetch was not exercised'
 (RUN/'requests.json').write_text(json.dumps(sorted(set(requests)),indent=2)+'\n');print(json.dumps(dict(passed=True,requests=sorted(set(requests)),session='ended; existing Firefox process preserved',server='ephemeral loopback fixture stopped in finally')))
finally:server.shutdown();server.server_close();thread.join()
