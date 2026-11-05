from pathlib import Path
from http.server import ThreadingHTTPServer,SimpleHTTPRequestHandler
from urllib.parse import unquote,urlsplit
import ast,hashlib,json,os,subprocess,threading,datetime
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[2];OUT=ROOT/'outputs/checks/2026-11-05-signed-profile/lab';RUN=OUT/('browser-'+datetime.datetime.now().strftime('%Y%m%dT%H%M%S%f'));RUN.mkdir();requests=[]
tree=ast.parse((ROOT/'scripts/build_public_site.py').read_text());runtime=next(n.value.value for n in ast.walk(tree) if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='runtime' for t in n.targets));assert hashlib.sha256(runtime.rstrip('\n').encode()).hexdigest()=='f8671345461a67648dd313817cf13209810f24314e343ece5a73862597feb94b'
class Handler(SimpleHTTPRequestHandler):
 def do_GET(self):
  name=unquote(urlsplit(self.path).path);requests.append(dict(method='GET',path=name))
  if name=='/favicon.ico':self.send_response(204);self.end_headers();return
  if name=='/GRH-research/public-base.js':body=runtime.encode();kind='application/javascript'
  elif name=='/GRH-research/profile-uniformity.html':body=(ROOT/'web/profile-uniformity.html').read_text().replace('href="/','href="/GRH-research/').replace('src="/','src="/GRH-research/').replace('<head>','<head><script src="/GRH-research/public-base.js"></script>',1).encode();kind='text/html'
  else:return super().do_GET()
  self.send_response(200);self.send_header('Content-Type',kind);self.send_header('Content-Length',str(len(body)));self.end_headers();self.wfile.write(body)
 def do_HEAD(self):requests.append(dict(method='HEAD',path=unquote(urlsplit(self.path).path)));super().do_HEAD()
 def translate_path(self,path):
  name=unquote(urlsplit(path).path).removeprefix('/GRH-research/');root=(ROOT/'web').resolve();p=(root/name.lstrip('/')).resolve();return str(p) if p.is_relative_to(root) else str(root/'__outside_fixture__')
 def log_message(self,*args):pass
server=ThreadingHTTPServer(('127.0.0.1',0),Handler);thread=threading.Thread(target=server.serve_forever,daemon=True);thread.start()
try:
 env=dict(os.environ,PROFILE_QA_URL='http://127.0.0.1:'+str(server.server_port),PROFILE_QA_OUTPUT=str(RUN));p=subprocess.run(['node',str(HERE/'check_browser.mjs')],cwd=ROOT,env=env,capture_output=True,text=True);(RUN/'stdout.txt').write_text(p.stdout);(RUN/'stderr.txt').write_text(p.stderr);(RUN/'requests.json').write_text(json.dumps(requests,indent=2)+'\n');print('Profile browser run:',RUN);print(p.stdout)
 if p.stderr:print(p.stderr)
 assert p.returncode==0,'Focused browser QA failed; all evidence retained'
 print(json.dumps(dict(passed=True,session='ended; Firefox process preserved',server='ephemeral loopback fixture stopped in finally',runtime_sha256=hashlib.sha256(runtime.encode()).hexdigest())))
finally:server.shutdown();server.server_close();thread.join()
