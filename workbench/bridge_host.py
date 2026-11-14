"""Opt-in live lab adapters without changing historical release files on disk.

Runs the existing restricted loopback server with a narrowly scoped HTML response
adapter for fluids.html and cosmology.html. No general template execution.
"""
from pathlib import Path
import argparse
from urllib.parse import urlsplit
import server

class LiveHandler(server.Handler):
    def send_data(self,status,payload,content_type):
        if status==200 and content_type=='text/html' and urlsplit(self.path).path in ('/fluids.html','/cosmology.html'):
            tags=b'<script src="workbench/core.js" defer></script><script src="workbench/bridge.js" defer></script>'
            payload=payload.replace(b'</body>',tags+b'</body>')
        super().send_data(status,payload,content_type)

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--port',type=int,default=8767);p.add_argument('--lean',type=Path)
    a=p.parse_args();s=server.make_server(a.port,a.lean);s.RequestHandlerClass=LiveHandler
    print(f'Live workbench http://127.0.0.1:{s.server_port}/workbench/',flush=True)
    try:s.serve_forever()
    except KeyboardInterrupt:pass
    finally:s.server_close()
