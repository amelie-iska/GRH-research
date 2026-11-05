"""Render selected NEW proof/control/PIT PDF pages, without recompilation."""
from pathlib import Path
import os,json,hashlib,subprocess,re,struct,xml.etree.ElementTree as ET
os.nice(15);os.sched_setaffinity(0,{min(os.sched_getaffinity(0))})
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[4]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
normalize=lambda s:re.sub('[^a-z0-9]','',s.lower())
run=ROOT/'outputs/checks/2026-11-05-rough-mask/builds/four-builds-v1.json';assert sha(run)=='93b53661ecd2720de8b671512f11e5e32be597c5c3a090fe60897c0cc9536897';build=json.loads(run.read_text());assert build['passed']
records=[]
for name,b in build['builds'].items():
 pdf=ROOT/b['pdf'];assert sha(pdf)==b['pdf_sha256'];pdf_hash=sha(pdf)
 text=subprocess.check_output(['pdftotext','-layout',str(pdf),'-'],text=True);pages=text.split('\f');count=len(pages)-int(not pages[-1].strip());assert count==b['pages']
 def locate(marker):
  found=[i+1 for i,p in enumerate(pages)if normalize(marker)in normalize(p)];assert found,(name,marker);return found[-1]
 selected={'theorem':locate('Explicit rough-prime mask budget'),'controls':locate('following numbers are RAW')}
 if 'extended'in name:
  selected.update(PIT_Stieltjes=locate('A coherent prime-substitution budget'),PIT_variation=locate('TRUE arbitrary-coefficient squared norm bound'))
 seen=set()
 for role,n in selected.items():
  if n in seen:continue
  seen.add(n);prefix=HERE/(name+'-page'+str(n).zfill(3));png=prefix.with_suffix('.png');textfile=prefix.with_suffix('.txt');textbytes=pages[n-1].encode();assert not textfile.exists()or textfile.read_bytes()==textbytes
  if not textfile.exists():textfile.write_bytes(textbytes)
  if not png.exists():subprocess.run(['pdftoppm','-f',str(n),'-l',str(n),'-scale-to','1600','-singlefile','-png',str(pdf),str(prefix)],check=True,stdout=subprocess.DEVNULL,stderr=subprocess.PIPE)
  xml=subprocess.check_output(['pdftotext','-f',str(n),'-l',str(n),'-bbox',str(pdf),'-'],text=True);pm=re.search(r'<page width="([0-9.]+)" height="([0-9.]+)"',xml);assert pm;width,height=map(float,pm.groups());words=re.findall(r'<word xMin="([0-9.eE+-]+)" yMin="([0-9.eE+-]+)" xMax="([0-9.eE+-]+)" yMax="([0-9.eE+-]+)"',xml);assert words and len(words)==xml.count('<word ');controlcodes=sorted(set(ord(c)for c in xml if ord(c)<32 and c not in '\t\r\n'))
  boxes=[tuple(map(float,w))for w in words];assert all(-.01<=x0<=x1<=width+.01 and-.01<=y0<=y1<=height+.01 for x0,y0,x1,y1 in boxes)
  data=png.read_bytes();assert data[:8]==b'\x89PNG\r\n\x1a\n';pix=struct.unpack('>II',data[16:24])
  records.append(dict(edition=name,role=role,physical_page=n,pdf=str(pdf),pdf_sha256=pdf_hash,total_pages=count,PNG=str(png),PNG_sha256=sha(png),PNG_bytes=len(data),PNG_dimensions=list(pix),selected_page_text_sha256=sha(prefix.with_suffix('.txt')),word_boxes=len(boxes),bbox_text_control_codepoints=controlcodes,bbox_all_word_coordinate_attributes_parsed=True,all_word_boxes_inside_page=True,page_points=[width,height],minimum_word_margins_points={'left':min(v[0]for v in boxes),'top':min(v[1]for v in boxes),'right':min(width-v[2]for v in boxes),'bottom':min(height-v[3]for v in boxes)}))
 assert sha(pdf)==pdf_hash
assert sha(run)=='93b53661ecd2720de8b671512f11e5e32be597c5c3a090fe60897c0cc9536897'
r=dict(status='RENDERED; visual inspection pending',renderer_sha256=sha(Path(__file__)),build_receipt_sha256=sha(run),pages=records,rendered_pages=len(records),physical_pages_found_by_pdftotext=True,bbox_parser='strict coordinate attributes; XML-incompatible math-font control text is not interpreted; NO word boxes excluded',resumed_preserved_first_two_PNGs=True,source_PDFs_unchanged=True,recompiled=False,production_edited=False,CPU_affinity_count=len(os.sched_getaffinity(0)),nice_priority=os.getpriority(os.PRIO_PROCESS,0))
with(HERE/'render-manifest-v2.json').open('x')as f:json.dump(r,f,indent=2);f.write('\n')
print(json.dumps({'rendered_pages':len(records),'manifest_sha256':sha(HERE/'render-manifest-v2.json'),'pages':{name:[x['physical_page']for x in records if x['edition']==name]for name in build['builds']}}))
