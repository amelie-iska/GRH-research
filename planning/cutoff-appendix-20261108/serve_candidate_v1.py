from argparse import ArgumentParser
from hashlib import sha256
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
from urllib.parse import unquote, urlsplit
import json
import os

root = Path(__file__).resolve().parents[2]
out = root/"outputs/checks/2026-11-08-cutoff-appendix"
parser = ArgumentParser()
parser.add_argument("--builds", type=Path, required=True)
parser.add_argument("--receipt", type=Path, required=True)
args = parser.parse_args()
builds = args.builds.resolve()
assert builds.is_relative_to(out)
assert args.receipt.resolve().is_relative_to(out)
native = builds/"native"
pdf = builds/"book-pdf/main.pdf"
pdf_record = json.loads((pdf.parent/"build-record.json").read_text())
record = json.loads((native/"native-build-record.json").read_text())
assert pdf_record["passed"] and record["passed"]
assert record["PDF_build_record_sha256"] == sha256((pdf.parent/"build-record.json").read_bytes()).hexdigest()
assert pdf_record["pdf_sha256"] == sha256(pdf.read_bytes()).hexdigest()
assert record["new_HTML_sha256"] == sha256((native/"book/main.html").read_bytes()).hexdigest()

class Candidate(SimpleHTTPRequestHandler):
    def do_GET(self):
        if urlsplit(self.path).path == "/favicon.ico":
            self.send_response(204)
            self.end_headers()
        else:
            super().do_GET()

    def translate_path(self, path):
        route = unquote(urlsplit(path).path)
        if ".." in Path(route).parts:
            return "/dev/null"
        if route == "/book.pdf":
            return str(pdf)
        base = native/"book" if route.startswith("/book/") else root/"web"
        rel = route.removeprefix("/book/") if route.startswith("/book/") else route.lstrip("/")
        dest = (base/(rel or "index.html")).resolve()
        return str(dest) if dest.is_relative_to(base) else "/dev/null"

    def log_message(self, *args):
        pass

server = ThreadingHTTPServer(("127.0.0.1", 0), Candidate)
status = {"pid": os.getpid(), "base": f"http://127.0.0.1:{server.server_port}", "builds": str(builds)}
with args.receipt.open("x") as f:
    json.dump(status, f, indent=2)
    f.write("\n")
server.serve_forever()
