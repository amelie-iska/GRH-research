"""Serve only the staged book/PDF plus reviewed source-web assets on a new loopback port."""
from pathlib import Path
from urllib.parse import unquote,urlsplit
from http.server import ThreadingHTTPServer,SimpleHTTPRequestHandler
import argparse,json,os,hashlib
ROOT=Path("/home/iska/Documents/LaTeX-projects/GRH-from-Mac-20261104")
p=argparse.ArgumentParser();p.add_argument("--native",required=True,type=Path);p.add_argument("--builds",required=True,type=Path);p.add_argument("--receipt",required=True,type=Path);p.add_argument("--book-pdf",required=True,type=Path);p.add_argument("--aggregate",required=True,type=Path);p.add_argument("--aggregate-sha256",required=True);a=p.parse_args()
N=a.native.resolve();B=a.builds.resolve()
assert N.is_relative_to(ROOT/"outputs") and B.is_relative_to(ROOT/"outputs")
assert a.book_pdf.resolve().is_relative_to(ROOT/"outputs") and a.book_pdf.read_bytes().startswith(b"%PDF")
assert a.aggregate.resolve().is_relative_to(ROOT/"outputs");assert hashlib.sha256(a.aggregate.read_bytes()).hexdigest()==a.aggregate_sha256;aggregate=json.loads(a.aggregate.read_text());assert aggregate["passed"]
assert hashlib.sha256(a.book_pdf.read_bytes()).hexdigest()==aggregate["results"]["book-pdf"]["PDF"]["sha256"]
routes={"/book.pdf":a.book_pdf.resolve()}
for route,name in [("/concise.pdf","focused-concise"),("/extended.pdf","focused-extended"),("/validated-oracle-concise.pdf","notes-concise"),("/validated-oracle-extended.pdf","notes-extended")]:
 item=aggregate["results"][name];assert item["passed"];pdf=(ROOT/item["PDF"]["path"]).resolve();assert pdf.is_relative_to(ROOT/"outputs") and pdf.read_bytes().startswith(b"%PDF");assert hashlib.sha256(pdf.read_bytes()).hexdigest()==item["PDF"]["sha256"];routes[route]=pdf

class Handler(SimpleHTTPRequestHandler):
 def do_GET(self):
  if urlsplit(self.path).path=="/favicon.ico":self.send_response(204);self.end_headers();return
  super().do_GET()
 def translate_path(self,path):
  q=unquote(urlsplit(path).path)
  if ".." in Path(q).parts:return "/dev/null"
  if q in routes:return str(routes[q])
  if q=="/baseline/book/main.html":return str(N/"baseline-book.html")
  base=N/"book" if q.startswith("/book/") else ROOT/"web"
  rel=q[len("/book/"):] if q.startswith("/book/") else q.lstrip("/")
  if not rel:rel="index.html"
  target=(base/rel).resolve()
  return str(target) if target.is_relative_to(base) else "/dev/null"
 def log_message(self,*args):pass
server=ThreadingHTTPServer(("127.0.0.1",0),Handler)
record=dict(pid=os.getpid(),aggregate=str(a.aggregate.resolve()),base="http://127.0.0.1:"+str(server.server_port),port=server.server_port,native=str(N),builds=str(B),scope="Owned staging server; old8765 untouched.")
assert not a.receipt.exists();a.receipt.write_text(json.dumps(record,indent=2)+"\n")
print(json.dumps(record),flush=True)
server.serve_forever()
