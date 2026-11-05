from pathlib import Path
from http.server import ThreadingHTTPServer,SimpleHTTPRequestHandler
import threading,subprocess,os,json
ROOT=Path(__file__).resolve().parents[3];C=ROOT/'outputs/adaptive-theta-book-20261105/v1/native';OUT=ROOT/'outputs/checks/2026-11-05-adaptive-theta/math-diagnosis';OUT.mkdir(exist_ok=False)
class Handler(SimpleHTTPRequestHandler):
 def translate_path(self,path):
  if path.startswith('/book/'):return str(C/path.lstrip('/'))
  return str(ROOT/'web'/path.lstrip('/'))
 def log_message(self,*a):pass
s=ThreadingHTTPServer(('127.0.0.1',0),Handler);t=threading.Thread(target=s.serve_forever,daemon=True);t.start()
code="""import {Browser} from '/home/iska/Documents/LaTeX-projects/project-pages-20261104/qa/bidi.mjs';import{writeFileSync}from'node:fs';
let b=await new Browser().connect();try{await b.viewport(390,844);await b.navigate(process.env.URL+'/book/main.html');await b.until('document.querySelectorAll("math").length===6868');
let r=await b.evaluate(`(()=>[...document.querySelectorAll('msub,msup,msubsup,munder,mover,munderover')].filter(x=>x.children.length!==(x.tagName.includes('subsup')||x.tagName.includes('underover')?3:2)).map(x=>({tag:x.tagName,children:x.children.length,outer:x.outerHTML,math:x.closest('math')?.outerHTML})))()`);writeFileSync(process.env.OUT+'/bad-dom.json',JSON.stringify(r,null,2));writeFileSync(process.env.OUT+'/errors.json',JSON.stringify(b.pageErrors(),null,2));console.log(JSON.stringify({bad:r,errors:b.pageErrors()}));}finally{await b.close();}"""
try:
 r=subprocess.run(['node','--input-type=module','-e',code],env=dict(os.environ,URL='http://127.0.0.1:'+str(s.server_port),OUT=str(OUT)),capture_output=True,text=True);(OUT/'run.log').write_text(r.stdout+r.stderr);print(r.stdout+r.stderr)
finally:s.shutdown();s.server_close();t.join()
