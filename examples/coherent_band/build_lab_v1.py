#!/usr/bin/env python3
"""Assemble the one new standalone page with the existing shared theme helper."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
import argparse,hashlib,json,types
ROOT=Path(__file__).resolve().parents[2];HERE=Path(__file__).parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def main():
 p=argparse.ArgumentParser();p.add_argument('--output',required=True);p.add_argument('--receipt',required=True);a=p.parse_args()
 out=Path(a.output);out=out if out.is_absolute() else ROOT/out;rec=Path(a.receipt);rec=rec if rec.is_absolute() else ROOT/rec
 runtime=(HERE/'runtime.mjs').read_text();css=(HERE/'lab.css').read_text();template=(HERE/'template.html').read_text();payload=ROOT/'web/data/coherent-band-schur-v1.json';digest=sha(payload)
 assert "DATA_SHA = '"+digest+"'" in runtime
 html=template.replace('@@CSS@@',css).replace('@@RUNTIME@@',runtime).replace('@@RUNTIME_SHA@@',sha(HERE/'runtime.mjs')).replace('@@PAYLOAD_SHA@@',digest)
 assert '@@' not in html
 module=types.ModuleType('coherent_band_existing_theme');exec(compile((ROOT/'scripts/theme_assets.py').read_bytes(),'scripts/theme_assets.py','exec'),module.__dict__);html=module.attach_theme(html)
 out.parent.mkdir(parents=True,exist_ok=True);out.open('x').write(html);rec.parent.mkdir(parents=True,exist_ok=True)
 value=dict(passed=True,page=str(out.relative_to(ROOT)),sha256=sha(out),bytes=out.stat().st_size,payload_sha256=digest,runtime_sha256=sha(HERE/'runtime.mjs'),inputs_sha256={str(x.relative_to(ROOT)):sha(x) for x in [HERE/'runtime.mjs',HERE/'lab.css',HERE/'template.html',ROOT/'scripts/theme_assets.py',Path(__file__)]},no_external_dependencies=True)
 rec.open('x').write(json.dumps(value,indent=2,sort_keys=True)+'\n');print(json.dumps(value))
if __name__=='__main__':main()
