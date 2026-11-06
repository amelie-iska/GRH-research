from pathlib import Path
import argparse,http.server,socketserver
R=Path('/home/iska/Documents/LaTeX-projects/GRH-from-Mac-20261104')
p=argparse.ArgumentParser();p.add_argument('--port',type=int,required=True);p.add_argument('--candidate',required=True,type=Path);a=p.parse_args();N=a.candidate.resolve();UI=R/'planning/physical-sieve-20261105/inspector/candidate-v3'
class Handler(http.server.SimpleHTTPRequestHandler):
 def translate_path(self,path):
  from urllib.parse import unquote,urlsplit
  q=unquote(urlsplit(path).path)
  if '..'in Path(q).parts:return '/dev/null'
  if q=='/baseline/book/main.html':return str(N.parent/'baseline-book.html')
  if q.startswith('/baseline/'):q=q[len('/baseline'):]
  if q.startswith('/book/'):base=N/'book';rel=q[len('/book/'):]
  elif q=='/book.pdf':return str(N.parent/'pdf/main.pdf')
  elif Path(q).name in ['quadratic-pivot.html','quadratic-pivot.mjs','quadratic-pivot.css','physical-sieve-model.mjs']:base=UI;rel=Path(q).name
  else:base=R/'web';rel=q.lstrip('/')
  out=(base/rel).resolve()
  if not out.is_relative_to(base.resolve()):return '/dev/null'
  return str(out)
class Server(socketserver.ThreadingMixIn,http.server.HTTPServer):daemon_threads=True
print('Owned candidate-only loopback server',a.port,flush=True)
Server(('127.0.0.1',a.port),Handler).serve_forever()
