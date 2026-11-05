#!/usr/bin/env python3
"""Optional bounded Linux fallback; builds candidates without live promotion.

Intended destination: scripts/build_remote_book_candidate.py. Existing helpers
remain in planning/book-integration-20261104 and are source-controlled. No auth,
network, package installation, cache mutation, index changes or live writes.
"""
from pathlib import Path
import argparse, hashlib, json, subprocess, sys
ROOT=Path(__file__).resolve().parents[1]
if ROOT.name=='planning':
    ROOT=ROOT.parent
BASE='38816daa63af5cb7986c0694e34b4948a3a4ea39'
BASE_SHA='bce3d2b6c7feda66ff03a5a7531300d07b4b054beb915461547ed68566c84545'

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--output',required=True,type=Path)
    p.add_argument('--svg-only',action='store_true',help='Reproduce using public source-matched SVGs only, without reading local diagram-PDF caches')
    a=p.parse_args();out=a.output.resolve()
    if out.exists():raise FileExistsError('Preserve prior build attempts; choose a new directory')
    baseline=subprocess.check_output(['git','show',BASE+':web/book/main.html'],cwd=ROOT)
    if hashlib.sha256(baseline).hexdigest()!=BASE_SHA:
        raise RuntimeError('Pinned old HTML baseline mismatch')
    out.mkdir(parents=True);(out/'baseline-book.html').write_bytes(baseline)
    helpers=ROOT/'planning/book-integration-20261104'
    subprocess.run([sys.executable,str(helpers/'build_isolated.py'),'--consume-book','--output',str(out/'pdf')]+(['--svg-only'] if a.svg_only else []),check=True)
    subprocess.run([sys.executable,str(helpers/'render_native.py'),'--pdf-build',str(out/'pdf'),'--baseline-book',str(out/'baseline-book.html'),'--output',str(out/'native')],check=True)
    pdf=json.loads((out/'pdf/build-record.json').read_text());native=json.loads((out/'native/native-build-record.json').read_text())
    if pdf['source_sha256']['book/main.tex']!=native['source_sha256']['book/main.tex']:
        raise RuntimeError('PDF/HTML book-source mismatch')
    record={'passed':True,'baseline_revision':BASE,'baseline_sha256':BASE_SHA,'pdf_record':'pdf/build-record.json','native_record':'native/native-build-record.json','pdf_pages':pdf['pdf_pages'],'native_math_nodes':native['math_nodes'],'canonical_labs':13,'diagram_asset_mode':pdf['diagram_asset_mode'],'diagram_cache_reads':pdf['diagram_cache_reads'],'promoted':False,'scope':'Bounded40-chapter Nov4 source integration; not a general replacement for make4ht, formal verification or a GRH proof.'}
    (out/'candidate-record.json').write_text(json.dumps(record,indent=2)+'\n');print(json.dumps(record,indent=2))

if __name__=='__main__':main()
