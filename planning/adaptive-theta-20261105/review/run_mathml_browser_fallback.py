"""Read-only isolated HTTP fixture; intentionally404 the optional math helper."""
from pathlib import Path
from http.server import ThreadingHTTPServer,SimpleHTTPRequestHandler
from urllib.parse import urlsplit,unquote
import argparse,os,subprocess,threading,json
ROOT=Path(__file__).resolve().parents[3]
p=argparse.ArgumentParser();p.add_argument('--candidate',type=Path,required=True);args=p.parse_args()
candidate=args.candidate.resolve();blocked=[]
class Handler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if unquote(urlsplit(self.path).path)=='/book/reviewed-math-scroll.js':
            blocked.append(self.path);self.send_error(404,'Intentional optional helper failure');return
        super().do_GET()
    def translate_path(self,path):
        name=unquote(urlsplit(path).path)
        base=candidate if name.startswith('/book/') else ROOT/'web'
        target=(base/name.lstrip('/')).resolve()
        return str(target) if target.is_relative_to(base.resolve()) else str(ROOT/'missing-review-fixture')
    def log_message(self,*args):pass
server=ThreadingHTTPServer(('127.0.0.1',0),Handler)
thread=threading.Thread(target=server.serve_forever,daemon=True);thread.start()
try:
    env=dict(os.environ,MATHML_FALLBACK_URL='http://127.0.0.1:'+str(server.server_port))
    result=subprocess.run(['node',str(Path(__file__).with_name('check_mathml_browser_fallback.mjs'))],cwd=ROOT,env=env,capture_output=True,text=True)
    print(result.stdout)
    if result.stderr:print(result.stderr)
    assert result.returncode==0,'Real browser fallback regression failed'
    assert blocked,'Helper was never requested; blocked fixture ineffective'
    print(json.dumps({'intentional_helper_404_requests':len(blocked),'server_shutdown':'finally'}))
finally:
    server.shutdown();server.server_close();thread.join()
