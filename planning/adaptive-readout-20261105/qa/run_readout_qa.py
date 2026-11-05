from pathlib import Path
from http.server import ThreadingHTTPServer,SimpleHTTPRequestHandler
from urllib.parse import urlsplit,unquote
import threading,subprocess,os,argparse
ROOT=Path(__file__).resolve().parents[3];WEB=ROOT/'web'
p=argparse.ArgumentParser();p.add_argument('--book',type=Path,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args()
OUT=a.output.resolve();OUT.mkdir(parents=True,exist_ok=False);BOOK=a.book.resolve()
class Handler(SimpleHTTPRequestHandler):
 def translate_path(self,path):
  name=unquote(urlsplit(path).path);base=BOOK if name.startswith('/book/') else (ROOT if name.startswith('/examples/') else WEB)
  target=(base/name.lstrip('/')).resolve()
  return str(target) if target.is_relative_to(base) else str(OUT/'missing')
 def log_message(self,*args):pass
server=ThreadingHTTPServer(('127.0.0.1',0),Handler);thread=threading.Thread(target=server.serve_forever,daemon=True);thread.start()
try:
 env=dict(os.environ,READOUT_QA_URL='http://127.0.0.1:'+str(server.server_port),READOUT_QA_OUTPUT=str(OUT))
 with (OUT/'run.log').open('w') as log:result=subprocess.run(['node',str(Path(__file__).with_name('readout.mjs'))],env=env,stdout=log,stderr=subprocess.STDOUT)
 print((OUT/'run.log').read_text());assert result.returncode==0
finally:server.shutdown();server.server_close();thread.join()
