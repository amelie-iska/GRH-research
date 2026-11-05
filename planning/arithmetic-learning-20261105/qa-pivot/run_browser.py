"""Read-only isolated web-root fixture. Existing Firefox9335 session only."""
from pathlib import Path
from http.server import ThreadingHTTPServer,SimpleHTTPRequestHandler
from urllib.parse import urlsplit,unquote
import subprocess,threading,os,json,datetime
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
OUT=ROOT/'outputs/checks/2026-11-05-arithmetic-learning/ui-pivot'
RUN=OUT/('run-'+datetime.datetime.now().strftime('%Y%m%dT%H%M%S%f'))
RUN.mkdir()
requests=[]
class Handler(SimpleHTTPRequestHandler):
 def do_GET(self):
  name=unquote(urlsplit(self.path).path);requests.append(name)
  if name=='/__pivot_embed_fixture__':
   body=b'<!doctype html><html><head><meta charset="utf-8"><script src="/theme.js"></script></head><body><iframe title="Quadratic pivot" src="/quadratic-pivot.html" style="width:100%;height:800px"></iframe></body></html>'
   self.send_response(200);self.send_header('Content-Type','text/html');self.send_header('Content-Length',str(len(body)));self.end_headers();self.wfile.write(body);return
  if name=='/favicon.ico':self.send_response(204);self.end_headers();return
  super().do_GET()
 def translate_path(self,path):
  base=(ROOT/'web').resolve();target=(base/unquote(urlsplit(path).path).lstrip('/')).resolve()
  return str(target) if target.is_relative_to(base) else str(base/'__outside_fixture__')
 def log_message(self,*args):pass
server=ThreadingHTTPServer(('127.0.0.1',0),Handler)
thread=threading.Thread(target=server.serve_forever,daemon=True);thread.start()
try:
 env=dict(os.environ,PIVOT_QA_URL='http://127.0.0.1:'+str(server.server_port),PIVOT_QA_RUN_DIR=str(RUN))
 result=subprocess.run(['node',str(HERE/'check_browser.mjs')],cwd=ROOT,env=env,capture_output=True,text=True)
 (RUN/'browser-run.stdout').write_text(result.stdout);(RUN/'browser-run.stderr').write_text(result.stderr)
 print('QA run:',RUN)
 print(result.stdout)
 if result.stderr:print(result.stderr)
 assert result.returncode==0,'Firefox browser QA failed; preserved stderr records details'
 print(json.dumps(dict(passed=True,requests=sorted(set(requests)),server='ephemeral loopback fixture; shut down in finally',browser='Existing Firefox9335 session ended; browser process preserved')))
finally:
 server.shutdown();server.server_close();thread.join()
