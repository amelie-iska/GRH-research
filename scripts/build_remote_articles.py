#!/usr/bin/env python3
"""Isolated exact-source article builds; never edit/promote production artifacts.

Cached diagrams are matched by full source hash, not article order. Two explicitly
specified historical grids may use reviewed standard-LaTeX picture renderings.
Every unknown environment fails closed. No dependency installation or TikZ shim.
"""
from pathlib import Path
import argparse,hashlib,json,os,re,subprocess,sys,unicodedata
ROOT=next(p for p in Path(__file__).resolve().parents if (p/'papers/resolutions-concise.tex').is_file() and (p/'outputs/book/diagram-exports.json').is_file())
PUBLIC_GRIDS=ROOT/'book/figures/article-grids'
PATTERN=r'\\begin\{(tikzpicture|tikzcd)\}.*?\\end\{\1\}'
GRIDS={
 'dd2a7bb5cd4f6a3c8d94e8bd3616cc9442d0ce31655c67d34226b99af16ae0d4':{
 'name':'quotient-grid','width':350,'height':170,'xs':[15,85,175,265,335],'ys':[140,85,30],
 'nodes':[[0,0,'0'],[0,1,'Y'],[0,2,r'\Lambda'],[0,3,'X'],[0,4,'0'],[1,0,'0'],[1,1,'Y'],[1,2,r'\Lambda'],[1,3,'X'],[1,4,'0'],[2,0,'0'],[2,1,'Y/uY'],[2,2,r'\Lambda/u\Lambda'],[2,3,'X/uX'],[2,4,'0']],
 'edges':[[r,c,r,c+1,'hook' if c==1 else 'normal','x' if c==2 and r<2 else '', 'above'] for r in range(3) for c in range(4)]+[[r,c,r+1,c,'normal','u' if r==0 else '', 'right'] for r in range(2) for c in [1,2,3]]},
 '5cebac09f8e9accfd86178b4ea896294573b28039291334f28aa9f46ce34b722':{
 'name':'signed-diamond','width':230,'height':180,'xs':[30,115,200],'ys':[155,90,25],
 'nodes':[[r,c,'ABCDEFGHI'[3*r+c]+('.' if r==2 and c==2 else '')] for r in range(3) for c in range(3)],
 'edges':[[r,c,r,c+1,'normal','p' if c==0 else 'i','above'] for r in range(3) for c in range(2)]+[[0,0,1,0,'normal','-p','left'],[0,1,1,1,'normal','p','right'],[0,2,1,2,'normal','-p','right'],[1,0,2,0,'normal','-i','left'],[1,1,2,1,'normal','i','right'],[1,2,2,2,'normal','-i','right']]}
}
def sha(data):return hashlib.sha256(data).hexdigest()
def env():return dict(os.environ,PYTHONDONTWRITEBYTECODE='1',OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1')
def command(args,cwd,log):
 with log.open('w') as f:subprocess.run(['nice','-n','15',*args],cwd=cwd,env=env(),stdout=f,stderr=subprocess.STDOUT,check=True)
def info(pdf):
 s=subprocess.check_output(['pdfinfo',str(pdf)],text=True)
 return int(re.search(r'Pages:\s+(\d+)',s)[1])
def clean(log):
 s=log.read_text();bad=[x for x in s.splitlines() if re.search(r'Overfull|undefined references|Citation .* undefined|Reference .* undefined|multiply defined|multiply-defined',x)]
 if bad:raise RuntimeError('Unacceptable final log: '+repr(bad))
def normalized(text):return ''.join(c.lower() for c in unicodedata.normalize('NFKD',text) if c.isascii() and c.isalnum())
def source_hashes_unchanged(sources):return all(sha((ROOT/p).read_bytes())==h for p,h in sources.items())
def record_source(path,sources):
 path=path.resolve();name=str(path.relative_to(ROOT));data=path.read_bytes();h=sha(data)
 if name in sources:assert sources[name]==h,'Concurrent source change: '+name
 sources[name]=h;return data

def picture_source(case):
 lines=[r'\documentclass[11pt]{article}',r'\usepackage{lmodern,amsmath}',
 r'\usepackage[paperwidth='+str(case['width']+16)+r'pt,paperheight='+str(case['height']+16)+r'pt,margin=8pt]{geometry}',
 r'\pagestyle{empty}\setlength{\parindent}{0pt}\setlength{\parskip}{0pt}\setlength{\topskip}{0pt}',
 r'\setlength{\unitlength}{1pt}',r'\begin{document}\noindent',r'\begin{picture}('+str(case['width'])+','+str(case['height'])+')']
 nodes={(r,c):s for r,c,s in case['nodes']};xs,ys=case['xs'],case['ys']
 for r,c,s in case['nodes']:lines.append(r'\put('+str(xs[c])+','+str(ys[r])+r'){\makebox(0,0){$'+s+r'$}}')
 def halfwidth(label):return 18 if '/' in label else (7 if label=='I.' else 5)
 for r,c,rr,cc,style,label,side in case['edges']:
  x,y=xs[c],ys[r];xx,yy=xs[cc],ys[rr]
  if rr==r:
   start=x+halfwidth(nodes[r,c])+7;end=xx-halfwidth(nodes[rr,cc])-7;assert end>start
   if style=='hook':
    # Explicit injection tail; standard picture Bezier followed by right arrow.
    lines.append(r'\qbezier('+str(start)+','+str(y+5)+')('+str(start-4)+','+str(y+5)+')('+str(start-4)+','+str(y+2.5)+')')
    lines.append(r'\qbezier('+str(start-4)+','+str(y+2.5)+')('+str(start-4)+','+str(y)+')('+str(start)+','+str(y)+')')
   lines.append(r'\put('+str(start)+','+str(y)+r'){\vector(1,0){'+str(end-start)+'}}')
   if label:lines.append(r'\put('+str((start+end)/2)+','+str(y+9)+r'){\makebox(0,0){$'+label+r'$}}')
  else:
   assert cc==c and rr==r+1 and style=='normal'
   start=y-11;end=yy+11;assert start>end
   lines.append(r'\put('+str(x)+','+str(start)+r'){\vector(0,-1){'+str(start-end)+'}}')
   if label:
    dx=-9 if side=='left' else 9;anchor='r' if side=='left' else 'l'
    lines.append(r'\put('+str(x+dx)+','+str((start+end)/2)+r'){\makebox(0,0)['+anchor+r']{$'+label+r'$}}')
 lines.extend([r'\end{picture}\end{document}']);return '\n'.join(lines)+'\n'

def prepare_grids(out,sources):
 # Recover the exact source blocks from current article inputs, without changing them.
 raw=record_source(ROOT/'papers/dessin-details.tex',sources).decode();blocks={sha(m[0].encode()):m[0] for m in re.finditer(PATTERN,raw,re.S)}
 records=[]
 for h,case in GRIDS.items():
  assert h in blocks,'Historical source grid changed; no renderer fallback'
  dest=out/case['name'];dest.mkdir();(dest/'original.tikz-source.tex').write_text(blocks[h])
  text=picture_source(case);(dest/'diagram.tex').write_text(text)
  command(['pdflatex','-interaction=nonstopmode','-halt-on-error','-output-directory='+str(dest),str(dest/'diagram.tex')],dest,dest/'build.log')
  clean(dest/'diagram.log');assert info(dest/'diagram.pdf')==1
  subprocess.run(['pdftocairo','-jpeg','-jpegopt','quality=80','-r','120','-singlefile',str(dest/'diagram.pdf'),str(dest/'preview')],check=True,stdout=subprocess.DEVNULL,stderr=subprocess.PIPE)
  records.append(dict(source_sha256=h,name=case['name'],node_count=len(case['nodes']),edge_count=len(case['edges']),nodes=case['nodes'],edges=case['edges'],source=blocks[h],geometry=case,render_tex_sha256=sha(text.encode()),pdf_sha256=sha((dest/'diagram.pdf').read_bytes()),pdf=str(dest/'diagram.pdf'),preview=str(dest/'preview.jpg'),trim='0pt 0pt 0pt 0pt',method='explicit source-correct standard LaTeX picture grid; no TikZ macro shim',semantic_review_required=True))
 assert source_hashes_unchanged(sources)
 result={'source_sha256':sources,'grids':records,'production_edited':False,'production_promoted':False,'scope':'Source-specific candidate vector redraws require independent semantic and root visual review before article use.'}
 (out/'grid-manifest.json').write_text(json.dumps(result,indent=2)+'\n');return result

def svg_pdf(svg_data,target):
 import ctypes as C,ctypes.util,xml.etree.ElementTree as ET
 tree=ET.fromstring(svg_data)
 def points(x):
  if x.endswith('pt'):return float(x[:-2])
  assert re.fullmatch(r'[0-9]+(?:\.[0-9]+)?',x);return float(x)
 width,height=points(tree.attrib['width']),points(tree.attrib['height'])
 class Rect(C.Structure):_fields_=[('x',C.c_double),('y',C.c_double),('width',C.c_double),('height',C.c_double)]
 rsvg=C.CDLL(C.util.find_library('rsvg-2'));cairo=C.CDLL(C.util.find_library('cairo'));gobj=C.CDLL(C.util.find_library('gobject-2.0'))
 rsvg.rsvg_handle_new_from_data.argtypes=[C.c_void_p,C.c_size_t,C.POINTER(C.c_void_p)];rsvg.rsvg_handle_new_from_data.restype=C.c_void_p
 rsvg.rsvg_handle_render_document.argtypes=[C.c_void_p,C.c_void_p,C.POINTER(Rect),C.POINTER(C.c_void_p)];rsvg.rsvg_handle_render_document.restype=C.c_int
 cairo.cairo_pdf_surface_create.argtypes=[C.c_char_p,C.c_double,C.c_double];cairo.cairo_pdf_surface_create.restype=C.c_void_p
 cairo.cairo_create.argtypes=[C.c_void_p];cairo.cairo_create.restype=C.c_void_p
 for name in ['cairo_destroy','cairo_surface_finish','cairo_surface_destroy']:getattr(cairo,name).argtypes=[C.c_void_p]
 gobj.g_object_unref.argtypes=[C.c_void_p]
 error=C.c_void_p();buf=C.create_string_buffer(svg_data);handle=rsvg.rsvg_handle_new_from_data(buf,len(svg_data),C.byref(error));assert handle and not error.value
 surface=cairo.cairo_pdf_surface_create(str(target).encode(),width,height);context=cairo.cairo_create(surface);view=Rect(0,0,width,height)
 ok=rsvg.rsvg_handle_render_document(handle,context,C.byref(view),C.byref(error));cairo.cairo_destroy(context);cairo.cairo_surface_finish(surface);cairo.cairo_surface_destroy(surface);gobj.g_object_unref(handle)
 assert ok and not error.value

def build_article(edition,out,sources,grids):
 base=ROOT/'papers';wrapper=base/('resolutions-'+edition+'.tex')
 def expand(text,stack=()):
  def include(m):
   q=(base/(m[1] if m[1].endswith('.tex') else m[1]+'.tex')).resolve();assert q not in stack,'Input cycle'
   return expand(record_source(q,sources).decode(),stack+(q,))
  return re.sub(r'\\input\{([^}]+)\}',include,text)
 original=expand(record_source(wrapper,sources).decode(),(wrapper.resolve(),));(out/'expanded-original.tex').write_text(original)
 required=['validated-oracle-core.tex','masked-moment-core.tex','weighted-cutoff-core.tex','uniform-cutoff-moment-core.tex']
 if edition=='extended':required += [n.replace('-core','-details') for n in required]
 assert all('papers/'+n in sources for n in required),'Actual new proof input missing'
 entries=json.loads(record_source(ROOT/'outputs/book/diagram-exports.json',sources));by={e['source_sha256']:e for e in entries};assert len(by)==len(entries)
 compiled=out/'compiled-diagrams';compiled.mkdir();diagrams=[];unknown=[]
 def replace(m):
  expression=m[0];h=sha(expression.encode());target=compiled/(h+'.pdf')
  if h in by:
   entry=by[h];svg=ROOT/'web/book'/('main'+str(entry['index'])+'x.svg');svg_data=record_source(svg,sources);assert sha(svg_data)==entry['sha256'] and len(svg_data)==entry['bytes']
   cache=ROOT/'outputs/html-diagrams'/h[:16];pdf=cache/'diagram.pdf'
   if pdf.exists():
    cache_tex=record_source(cache/'diagram.tex',sources).decode();assert expression in cache_tex and r'\documentclass[border=5pt]{standalone}' in cache_tex
    target.write_bytes(record_source(pdf,sources));method='exact-source cached standalone PDF'
   else:svg_pdf(svg_data,target);method='exact-source accepted vector SVG via existing librsvg/cairo'
   trim='5pt 5pt 5pt 5pt';accepted_svg=entry['sha256']
  elif h in grids:
   record=grids[h];assert record['source']==expression and sha(expression.encode())==record['source_sha256'];pdf=Path(record['pdf']);pdf=pdf if pdf.is_absolute() else ROOT/pdf;data=record_source(pdf,sources);assert sha(data)==record['pdf_sha256'];target.write_bytes(data)
   # Original source and reviewed redraw hashes remain independently inspectable.
   method=record['method'];trim=record['trim'];accepted_svg=None
  else:unknown.append({'source_sha256':h,'source':expression,'environment':m[1]});return m[0]
  assert target.read_bytes().startswith(b'%PDF')
  diagrams.append(dict(source_sha256=h,source=expression,pdf_sha256=sha(target.read_bytes()),accepted_svg_sha256=accepted_svg,method=method,trim=trim))
  return r'\includegraphics[trim='+trim+',clip]{'+str(target)+'}'
 text=re.sub(PATTERN,replace,original,flags=re.S)
 (out/'diagram-preflight.json').write_text(json.dumps({'matched':diagrams,'unknown':unknown},indent=2)+'\n')
 if unknown:raise RuntimeError('Uncached source diagram(s); no weak renderer fallback')
 removed=[]
 def package(m):
  names=m['names'].split(',');keep=[n for n in names if n not in {'tikz','tikz-cd','pgfplots','pgf'}];removed.extend(n for n in names if n not in keep)
  return r'\usepackage'+(m['options'] or '')+'{'+','.join(keep)+'}' if keep else ''
 text=re.sub(r'\\usepackage(?P<options>\[[^\]]*\])?\{(?P<names>[^}]+)\}',package,text)
 text,libs=re.subn(r'^\\use(?:tikz|pgfplots)library\{[^}]+\}\s*\n','',text,flags=re.M)
 assert not re.search(r'\\(?:tikz|pgf|usetikz|foreach|node\b)',text),'Unsupported unrendered drawing command'
 packages=set(n for m in re.finditer(r'\\usepackage(?:\[[^\]]*\])?\{([^}]+)\}',text) for n in m[1].split(','));needed=[n for n in ['graphicx','xcolor'] if n not in packages]
 if needed:
  text,count=re.subn(r'(\\documentclass(?:\[[^\]]*\])?\{[^}]+\})',lambda m:m[0]+'\n'+r'\usepackage{'+','.join(needed)+'}',text,count=1);assert count==1
 figures=[]
 def figure(m):
  name=m['name']
  if name.startswith(str(compiled)):return m[0]
  src=(base/name).resolve();src=src if src.suffix else src.with_suffix('.pdf');src.relative_to(ROOT)
  if src.exists():data=record_source(src,sources);figures.append({'path':str(src.relative_to(ROOT)),'sha256':sha(data),'exists':True})
  else:figures.append({'path':str(src.relative_to(ROOT)),'exists':False,'scope':'May be an inactive IfFileExists branch; compilation must reject any active missing figure'})
  return r'\includegraphics'+(m['options'] or '')+'{'+str(src)+'}'
 text=re.sub(r'\\includegraphics(?P<options>\[[^\]]*\])?\{(?P<name>[^}]+)\}',figure,text)
 text=re.sub(r'\\IfFileExists\{([^}]+)\}',lambda m:r'\IfFileExists{'+str((base/m[1]).resolve())+'}',text)
 target=out/('resolutions-'+edition+'.expanded.tex');target.write_text(text)
 labels=re.findall(r'\\label\{([^}]+)\}',text);assert len(labels)==len(set(labels)),'Duplicate labels in expanded source'
 assert all(s in text for s in [r'\label{mm:afm}',r'\label{rc:core}',r'\label{wc:uniform}'])
 for turn in [1,2,3]:command(['pdflatex','-interaction=nonstopmode','-halt-on-error','-jobname=resolutions-'+edition,'-output-directory='+str(out),str(target.resolve())],out,out/f'build-pass{turn}.log')
 log=out/('resolutions-'+edition+'.log');clean(log);pdf=out/('resolutions-'+edition+'.pdf');assert pdf.read_bytes().startswith(b'%PDF')
 extract=subprocess.check_output(['pdftotext',str(pdf),'-'],text=True);(out/'extracted-text.txt').write_text(extract)
 markers=['A finite, validated approximation result','An arithmetic-family moment with every original row retained','Recombining the actual weighted cutoff','A cutoff-uniform envelope for the original masked remainder']
 assert all(normalized(s) in normalized(extract) for s in markers),'New proof marker missing from compiled PDF'
 assert source_hashes_unchanged(sources),'Concurrent input change; reject build'
 return {'edition':edition,'pages':info(pdf),'pdf_sha256':sha(pdf.read_bytes()),'new_proof_markers':markers,'diagram_records':diagrams,'figure_records':figures,'removed_unused_packages':removed,'removed_drawing_library_declarations':libs,'source_sha256':sources,'source_unchanged':True,'production_edited':False,'production_promoted':False,'new_Lean_declarations':0,'complete_book_formalization':False,'compile_input':str(target.resolve()),'compile_output':str(out.resolve())}

def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--mode',choices=['prepare-grids','build'],default='build');p.add_argument('--edition',choices=['concise','extended'],default='concise');p.add_argument('--output',type=Path,required=True);p.add_argument('--grid-assets',type=Path);p.add_argument('--grid-review',type=Path);p.add_argument('--root-visual-approved',action='store_true');a=p.parse_args()
 if a.mode=='build' and a.edition=='extended' and a.grid_assets is None:
  a.grid_assets=PUBLIC_GRIDS
  if a.grid_review is None:a.grid_review=PUBLIC_GRIDS/'root-acceptance.json'
 out=a.output.resolve();assert not out.exists(),'Preserve prior build attempts';out.mkdir(parents=True);snapshot=Path(__file__).read_bytes();(out/'builder.py').write_bytes(snapshot);sources={}
 try:
  if a.mode=='prepare-grids':result=prepare_grids(out,sources)
  else:
   grids={}
   if a.grid_assets:
    assert a.grid_review,'Grid use requires independent semantic and root visual acceptance'
    raw=record_source(a.grid_assets/'grid-manifest.json',sources);review=json.loads(record_source(a.grid_review,sources));assert review['accepted'] is True and review['grid_manifest_sha256']==sha(raw),'Unmatched independent grid acceptance'
    packaged_acceptance=a.grid_assets.resolve()==PUBLIC_GRIDS.resolve() and review.get('semantic_accepted') is True and review.get('root_visual_approved') is True
    assert a.root_visual_approved or packaged_acceptance,'Grid use requires independent semantic and root visual acceptance'
    manifest=json.loads(raw);grids={e['source_sha256']:e for e in manifest['grids']}
   result=build_article(a.edition,out,sources,grids)
  assert Path(__file__).read_bytes()==snapshot,'Builder changed during run';assert source_hashes_unchanged(sources)
  (out/'build-record.json').write_text(json.dumps({'passed':True,'builder_sha256':sha(snapshot),**result},indent=2)+'\n');print(json.dumps({'passed':True,'output':str(out),'pages':result.get('pages'),'grid_count':len(result.get('grids',[])),'production_promoted':False},indent=2))
 except Exception as e:
  failure={'passed':False,'error_type':type(e).__name__,'error':str(e),'builder_sha256':sha(snapshot),'source_sha256':sources,'source_unchanged':source_hashes_unchanged(sources),'production_edited':False,'production_promoted':False}
  (out/'failure-record.json').write_text(json.dumps(failure,indent=2)+'\n');raise
if __name__=='__main__':main()
