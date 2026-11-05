from pathlib import Path
from http.server import ThreadingHTTPServer,SimpleHTTPRequestHandler
from urllib.parse import urlsplit,unquote
import threading,subprocess,os,argparse
ROOT=Path('/home/iska/Documents/LaTeX-projects/GRH-from-Mac-20261104');WEB=ROOT/'web'
ap=argparse.ArgumentParser();ap.add_argument('--candidate',required=True,type=Path);ap.add_argument('--pdf',required=True,type=Path);ap.add_argument('--output',required=True,type=Path);a=ap.parse_args()
CANDIDATE=a.candidate.resolve();PDF=a.pdf.resolve();OUT=a.output.resolve();OUT.mkdir(exist_ok=False)
for name in ['qa-integrated-native.mjs','run_native_qa.py']:(OUT/name).write_bytes((ROOT/'planning/book-integration-20261104'/name).read_bytes())
class Handler(SimpleHTTPRequestHandler):
 def translate_path(self,path):
  name=unquote(urlsplit(path).path)
  if name=='/book.pdf':return str(PDF)
  if name=='/baseline/book/main.html':return str(CANDIDATE/'baseline-book.html')
  if name.startswith('/baseline/book/'):
   base=WEB/'book';name=name[len('/baseline/book/'):]
  else:base=CANDIDATE if name.startswith('/book/') else WEB
  resolved=(base/name.lstrip('/')).resolve()
  if not resolved.is_relative_to(base.resolve()):return str(OUT/'missing')
  return str(resolved)
 def log_message(self,*args):pass
server=ThreadingHTTPServer(('127.0.0.1',0),Handler);thread=threading.Thread(target=server.serve_forever,daemon=True);thread.start()
env=dict(os.environ,BOOK_QA_URL='http://127.0.0.1:'+str(server.server_port),BOOK_QA_OUTPUT=str(OUT),BOOK_QA_CANDIDATE=str(CANDIDATE),PYTHONDONTWRITEBYTECODE='1')
try:
 with (OUT/'run.log').open('w') as log:
  run=subprocess.run(['node',str(ROOT/'planning/book-integration-20261104/qa-integrated-native.mjs')],cwd=ROOT,env=env,stdout=log,stderr=subprocess.STDOUT)
 print((OUT/'run.log').read_text());assert run.returncode==0,'Remote browser QA failed; all artifacts preserved'
finally:server.shutdown();server.server_close();thread.join()
