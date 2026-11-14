"""Opt-in, loopback-only proof service and static atlas; never execute uploaded Lean.

Run: python3 workbench/server.py --lean /absolute/pinned/bin/lean
The service exposes only workbench/site and extension/site. It does not expose
the repository root, credential stores, directory listings or arbitrary commands.
"""
from __future__ import annotations
import argparse
import hashlib
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json
import mimetypes
from pathlib import Path
import threading
from urllib.parse import unquote,urlsplit
from lean_export import check, lean_source, strict_json, TEMPLATE

ROOT=Path(__file__).resolve().parent
LOCK=threading.BoundedSemaphore(1)


def asset_path(url: str, workbench: Path, atlas: Path) -> Path:
    path=unquote(urlsplit(url).path)
    if '\\' in path or '\x00' in path: raise ValueError('Invalid path')
    if path in ('/','/workbench'): path='/workbench/index.html'
    if path.startswith('/workbench/'):
        base=workbench;relative=path[len('/workbench/'):]
    else: base=atlas;relative=path.lstrip('/')
    if not relative or relative.endswith('/'): relative+='index.html'
    candidate=(base/relative).resolve()
    if not candidate.is_relative_to(base.resolve()) or not candidate.is_file(): raise FileNotFoundError('Not an exposed asset')
    return candidate


class Handler(BaseHTTPRequestHandler):
    server_version='GRHWorkbench/1'
    def log_message(self, fmt, *args): pass
    def send_data(self, status: int, payload: bytes, content_type: str):
        self.send_response(status);self.send_header('Content-Type',content_type)
        self.send_header('Content-Length',str(len(payload)));self.send_header('Cache-Control','no-store')
        self.send_header('X-Content-Type-Options','nosniff');self.end_headers();self.wfile.write(payload)
    def send_json(self, status: int, data: dict):
        self.send_data(status,json.dumps(data,allow_nan=False).encode(), 'application/json; charset=utf-8')
    def origin_ok(self) -> bool:
        allowed={f'127.0.0.1:{self.server.server_port}',f'localhost:{self.server.server_port}'}
        host=self.headers.get('Host','')
        return host in allowed and self.headers.get('Origin',f'http://{host}')==f'http://{host}' and self.headers.get('Sec-Fetch-Site','same-origin') in ('same-origin','none')
    def do_GET(self):
        if not self.origin_ok(): self.send_json(403,{'error':'Same-origin loopback requests only'});return
        if self.path=='/api/status':
            self.send_json(200,{'schema':'grh.workbench.service.v1','lean_configured':self.server.lean is not None,
              'template_sha256':hashlib.sha256(TEMPLATE.read_bytes()).hexdigest()});return
        try:
            p=asset_path(self.path,ROOT/'site',ROOT.parent/'extension/site')
            self.send_data(200,p.read_bytes(),mimetypes.guess_type(p.name)[0] or 'application/octet-stream')
        except (ValueError,FileNotFoundError): self.send_json(404,{'error':'Asset not found'})
    def do_POST(self):
        if not self.origin_ok(): self.send_json(403,{'error':'Same-origin loopback requests only'});return
        if self.path not in ('/api/verify','/api/source'): self.send_json(404,{'error':'Unknown endpoint'});return
        if self.headers.get('Transfer-Encoding') or self.headers.get('Content-Type','').split(';')[0]!='application/json':
            self.send_json(415,{'error':'Bounded JSON required'});return
        try:
            length=int(self.headers.get('Content-Length','0'))
            if not 0<length<=65536: raise ValueError('Body outside size budget')
            self.connection.settimeout(5)
            c=strict_json(self.rfile.read(length).decode('utf8'))
            if self.path=='/api/source': self.send_json(200,{'source':lean_source(c)});return
            if self.server.lean is None: self.send_json(503,{'error':'No Lean compiler configured; arithmetic is not kernel verification'});return
            if not LOCK.acquire(blocking=False): self.send_json(429,{'error':'One proof at a time'});return
            try: receipt=check(c,self.server.lean)
            finally: LOCK.release()
            self.send_json(200,receipt)
        except (ValueError,TypeError,KeyError,UnicodeDecodeError,json.JSONDecodeError,OSError) as error:
            self.send_json(400,{'error':str(error)[:300]})
        except Exception:
            self.send_json(500,{'error':'Proof service failed; no verification receipt issued'})


def make_server(port: int, lean: Path | None=None) -> ThreadingHTTPServer:
    if type(port) is not int or not 0<=port<=65535: raise ValueError('Invalid port')
    server=ThreadingHTTPServer(('127.0.0.1',port),Handler)
    server.daemon_threads=True;server.lean=lean
    return server

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--port',type=int,default=8767);p.add_argument('--lean',type=Path)
    a=p.parse_args();s=make_server(a.port,a.lean)
    print(f'Workbench: http://127.0.0.1:{s.server_port}/workbench/ (Ctrl+C stops)',flush=True)
    try:s.serve_forever()
    except KeyboardInterrupt:pass
    finally:s.server_close()
