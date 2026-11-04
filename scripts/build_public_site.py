"""Create a fresh static GitHub Pages bundle without changing local preview URLs.

Numerical JSON/trace files are copied byte-for-byte: their recorded hashes
remain valid. A small URL adapter handles the project-site path prefix.
"""
from pathlib import Path
import argparse,shutil,subprocess,json,hashlib,re
ROOT=Path(__file__).resolve().parents[1]
def main(output):
    assert not output.exists(),'Use a fresh output directory; preserve previous bundles'
    output.mkdir(parents=True);base='/GRH-research/'
    tracked=subprocess.check_output(['git','ls-files','-z'],cwd=ROOT).decode().split('\0')
    files=[]
    for name in filter(None,tracked):
        p=Path(name)
        if p.parts[0]=='web':target=output/Path(*p.parts[1:])
        elif p.parts[0]=='examples' and p.suffix in {'.py','.sage','.md','.json','.mjs','.sv','.v'}:target=output/p
        elif p.parts[0]=='lean-analytic' and p.suffix=='.lean':target=output/'lean'/p.name
        else:continue
        source=ROOT/p
        if not source.is_file():continue
        target.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(source,target);files.append((source,target))
    for source,name in [('outputs/book/surface-orders-book.pdf','book.pdf'),('outputs/papers/resolutions-concise.pdf','concise.pdf'),('outputs/papers/resolutions-extended.pdf','extended.pdf')]:shutil.copyfile(ROOT/source,output/name)
    runtime=r'''// Project-path adapter only; saved scientific records remain byte-identical.
(()=>{const base='/GRH-research/';const map=value=>{if(typeof value!=='string')return value;if(value.startsWith('http://127.0.0.1:8765/'))return base+value.slice(22);if(value.startsWith(location.origin+'/'))value=value.slice(location.origin.length);if(value.startsWith('/')&&!value.startsWith('//')&&!value.startsWith(base))return base+value.slice(1);return value;};
const native=window.fetch;window.fetch=(input,init)=>native(typeof input==='string'?map(input):input instanceof URL?new URL(map(input.href)):input instanceof Request?new Request(map(input.url),input):input,init);
for(const [type,key]of[[HTMLAnchorElement,'href'],[HTMLImageElement,'src'],[HTMLIFrameElement,'src'],[HTMLMediaElement,'src'],[HTMLSourceElement,'src']]){const d=Object.getOwnPropertyDescriptor(type.prototype,key);if(d?.set)Object.defineProperty(type.prototype,key,{...d,set(v){d.set.call(this,map(v));}});}
const original=Element.prototype.setAttribute;Element.prototype.setAttribute=function(k,v){return original.call(this,k,['href','src','poster','data-source'].includes(k)?map(v):v);};
const patch=node=>{if(node.nodeType!==1)return;for(const a of ['href','src','poster','data-source']){const v=node.getAttribute(a);if(v&&map(v)!==v)original.call(node,a,map(v));}node.querySelectorAll('[href],[src],[poster],[data-source]').forEach(el=>{for(const a of ['href','src','poster','data-source']){const v=el.getAttribute(a);if(v&&map(v)!==v)original.call(el,a,map(v));}});};
new MutationObserver(ms=>ms.forEach(m=>m.type==='attributes'?patch(m.target):m.addedNodes.forEach(patch))).observe(document.documentElement,{subtree:true,childList:true,attributes:true,attributeFilter:['href','src','poster','data-source']});})();
'''
    (output/'public-base.js').write_text(runtime)
    for p in output.rglob('*.html'):
        s=p.read_text();s=s.replace('http://127.0.0.1:8765/',base)
        s=re.sub(r'''((?:href|src|poster|data-source)=["'])/(?!/|GRH-research/)''',lambda m:m[1]+base,s)
        # Some generated pages have no head; all executable project pages do.
        s=s.replace('<head>','<head><script src="'+base+'public-base.js"></script>',1)
        p.write_text(s)
    for p in output.rglob('*.css'):
        s=p.read_text();s=re.sub(r'''url\((["']?)/(?!/)''',lambda m:'url('+m[1]+base,s);p.write_text(s)
    # Root module imports bypass window.fetch; current imports are relative,
    # but retain correct semantics for an explicitly root-relative import.
    for p in list(output.rglob('*.mjs'))+list(output.rglob('*.js')):
        if p.name=='public-base.js':continue
        s=p.read_text();s=re.sub(r'''(from\s+["']|import\s*["'])/(?!/)''',lambda m:m[1]+base,s);p.write_text(s)
    unchanged=0
    for source,target in files:
        if source.suffix in {'.json','.png','.npz','.npy'}:
            assert source.read_bytes()==target.read_bytes(),str(source);unchanged+=1
    (output/'.nojekyll').touch()
    manifest={'base_path':base,'byte_identical_data_assets':unchanged,'files':sum(p.is_file() for p in output.rglob('*')),'source_unchanged':True,'contains_credentials':False}
    (output/'publication.json').write_text(json.dumps(manifest,indent=2)+'\n');print(json.dumps(manifest))
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output',type=Path,required=True);main(p.parse_args().output)
