#!/usr/bin/env python3
"""Loopback-only companion server with an explicit file whitelist."""
from pathlib import Path
from http.server import ThreadingHTTPServer,BaseHTTPRequestHandler
from urllib.parse import urlsplit,unquote
import mimetypes
ROOT=Path(__file__).resolve().parents[1]
class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        path=unquote(urlsplit(self.path).path)
        if path=='/book.pdf': file=ROOT/'outputs/book/surface-orders-book.pdf'
        elif path=='/concise.pdf':file=ROOT/'outputs/papers/resolutions-concise.pdf'
        elif path=='/extended.pdf':file=ROOT/'outputs/papers/resolutions-extended.pdf'
        elif path.startswith('/lean/'):
            file=(ROOT/'lean-analytic'/path.removeprefix('/lean/')).resolve()
            if not file.is_relative_to(ROOT/'lean-analytic') or file.suffix!='.lean':self.send_error(403);return
        elif path.startswith('/examples/'):
            file=(ROOT/path.lstrip('/')).resolve()
            if not file.is_relative_to(ROOT/'examples'):self.send_error(403);return
            if file.suffix not in ['.py','.sage','.md','.json']:self.send_error(403);return
        else:
            file=(ROOT/'web'/('index.html' if path=='/' else path.lstrip('/'))).resolve()
            if not file.is_relative_to(ROOT/'web'):self.send_error(403);return
        if not file.is_file():self.send_error(404);return
        data=file.read_bytes();self.send_response(200)
        self.send_header('Content-Type',mimetypes.guess_type(file.name)[0] or 'application/octet-stream')
        self.send_header('Content-Length',str(len(data)));self.send_header('Cache-Control','no-cache')
        self.send_header('X-Content-Type-Options','nosniff');self.end_headers();self.wfile.write(data)
if __name__=='__main__':
    print('Private local companion: http://127.0.0.1:8765',flush=True)
    ThreadingHTTPServer(('127.0.0.1',8765),Handler).serve_forever()
