from pathlib import Path
import argparse,json,hashlib,re,collections,subprocess,html
import xml.etree.ElementTree as ET
ROOT=Path('/home/iska/Documents/LaTeX-projects/GRH-from-Mac-20261104')
NS='{http://www.w3.org/1998/Math/MathML}'
def sha(data):return hashlib.sha256(data).hexdigest()
def main(pdf,native,output):
 if output.exists():raise FileExistsError('Preserve previous review output')
 rec=json.loads((pdf/'build-record.json').read_text());nr=json.loads((native/'native-build-record.json').read_text())
 original=(pdf/'source-expansion-before-diagram-replacement.tex').read_text();actual=(pdf/'main.tex').read_text()
 manifest=json.loads((ROOT/'outputs/book/diagram-exports.json').read_text())
 diagrams=list(re.finditer(r'\\begin\{(tikzpicture|tikzcd)\}.*?\\end\{\1\}',original,re.S))
 assert len(diagrams)==len(manifest)==19
 cache_count=svg_count=0;hashes=[]
 for i,m in enumerate(diagrams):
  h=sha(m[0].encode());entry=manifest[i];assert h==entry['source_sha256'];hashes.append(h)
  svg=ROOT/'web/book'/f'main{i}x.svg';assert sha(svg.read_bytes())==entry['sha256']
  target=pdf/'compiled-diagrams'/(h+'.pdf');assert sha(target.read_bytes())==rec['diagram_records'][i]['pdf_sha256']
  cache=ROOT/'outputs/html-diagrams'/h[:16]
  if (cache/'diagram.pdf').exists():
   assert target.read_bytes()==(cache/'diagram.pdf').read_bytes()
   tex=(cache/'diagram.tex').read_text();body=tex.split(r'\begin{document}',1)[1].split(r'\end{document}',1)[0].strip();assert body==m[0];cache_count+=1
  else:svg_count+=1
  assert not re.search(r'\\(?:label|input)\{',m[0])
 it=iter(hashes)
 expected=re.sub(r'\\begin\{(tikzpicture|tikzcd)\}.*?\\end\{\1\}',lambda m:r'\includegraphics[trim=5pt 5pt 5pt 5pt,clip]{compiled-diagrams/'+next(it)+'.pdf}',original,flags=re.S)
 expected=expected.replace(r'\usepackage{microtype,graphicx,tikz,tikz-cd,fancyhdr}',r'\usepackage{microtype,graphicx,xcolor,fancyhdr}')
 expected,n=re.subn(r'^\\usetikzlibrary\{[^}]+\}\s*\n','',expected,flags=re.M);assert n==1 and expected==actual
 assert all(sha((ROOT/name).read_bytes())==value for name,value in rec['source_sha256'].items())
 assert all(sha((ROOT/z['path']).read_bytes())==z['sha256'] for z in rec['figure_records'])
 old_chapters=subprocess.check_output(['git','ls-tree','-r','--name-only','origin/main','book/chapters'],cwd=ROOT,text=True).splitlines()
 for name in old_chapters:assert subprocess.check_output(['git','show','origin/main:'+name],cwd=ROOT)==(ROOT/name).read_bytes()
 assert len(old_chapters)==45
 baseline=(native/'baseline-book.html').read_text();combined=(native/'book/main.html').read_text()
 assert sha(baseline.encode())==nr['old_HTML_sha256'] and sha(combined.encode())==nr['new_HTML_sha256']
 marker='<section class="new-reviewed-chapters" id="new-reviewed-chapters">';start=combined.index(marker);end=combined.index('</section>\n',start)+len('</section>\n');inserted=combined[start:end]
 old_heads=list(re.finditer(r'<h2\b[^>]*>.*?</h2>',baseline,re.S));numbered=[m for m in old_heads if m[0].startswith('<h2 class="chapterHead">')]
 bib=[m for m in old_heads if ' '.join(html.unescape(re.sub('<[^>]+>',' ',m[0])).split())=='Bibliography'];assert len(bib)==1 and len(numbered)==37
 assert start>numbered[-1].end()
 tree=ET.fromstring(combined);seq=[]
 for el in tree.iter('h2'):
  if el.attrib.get('class')=='chapterHead':seq.append(int(re.search(r'(?:Chapter\s*)?(\d+)',' '.join(el.itertext()))[1]))
 assert seq==list(range(1,41))
 restored=combined[:start]+combined[end:]
 part=r'<br /><span class="partToc"><a href="#new-certified-analytic-targets">.*?</a></span>'
 restored,n=re.subn(part,'',restored,flags=re.S);assert n==1
 frag=(native/'fragment-resolved.html').read_text();chapter_ids=re.findall(r'<h2 class="chapterHead"[^>]*id="([^"]+)"',frag);assert len(chapter_ids)==3
 for ident in chapter_ids:
  restored,n=re.subn(r'<br /><span class="chapterToc"><a href="#'+re.escape(ident)+r'">.*?</a></span>','',restored,flags=re.S);assert n==1
 for z in reversed(nr['intentional_old_prose_changes']):
  assert restored.count(z['new'])==1;restored=restored.replace(z['new'],z['old'],1)
 assert restored==baseline
 ast=json.loads((native/'supplement.ast.json').read_text());raw=[];math=[]
 def walk(x):
  if isinstance(x,dict):
   if x.get('t') in ['RawBlock','RawInline']:raw.append(x)
   if x.get('t')=='Math':math.append(x['c'][1].strip())
   for v in x.values():walk(v)
  elif isinstance(x,list):
   for v in x:walk(v)
 walk(ast);assert not raw
 ft=ET.fromstring('<div>'+frag+'</div>');nodes=list(ft.iter(NS+'math'));annotations=[]
 for node in nodes:
  a=node.find('.//'+NS+'annotation');assert a is not None;annotations.append(''.join(a.itertext()).strip())
  for e in node.iter():
   if e.tag==NS+'annotation':continue
   assert '\\' not in (e.text or ''),'Raw command rendered outside annotation'
 assert len(nodes)==860 and collections.Counter(annotations)==collections.Counter(math)
 assert nr['normalizations']=={'old_rm':5,'hbox':9,'notag':4,'atop':14}
 aux=(pdf/'main.aux').read_text();labels=dict(re.findall(r'\\newlabel\{([^}]+)\}\{\{([^}]*)\}',aux))
 ids={x.attrib['id']:x for x in ft.iter() if 'id' in x.attrib}
 for z in nr['theorems']:
  if z['id']:assert labels[z['id']]==z['number'] and z['id'] in ids
 for ident,number in nr['equation_numbers'].items():
  assert labels[ident]==number and ident in ids
  text=' '.join(ids[ident].itertext());assert '('+number+')' in text
 for a in ft.iter('a'):
  if 'data-reference' in a.attrib:
   ident=a.attrib['data-reference'];number=labels[ident];expected='('+number+')' if a.attrib['data-reference-type']=='eqref' else number
   assert ''.join(a.itertext())==expected
 assert len(nr['theorems'])==6 and nr['proof_environments']==6
 report={'passed':True,'pdf_build':str(pdf),'native_build':str(native),'pdf_source_exact_except_documented_diagram_package_substitutions':True,'diagrams':19,'identical_cached_single_diagram_PDFs':cache_count,'source_matched_SVG_conversions':svg_count,'old_chapter_files_byte_identical_to_origin':len(old_chapters),'HTML_reversible_to_baseline_except_2_authorized_prose_edits':True,'numbered_chapters':seq,'MathML_nodes':860,'raw_TeX_AST':0,'source_math_annotation_multisets_match':True,'math_normalizations':nr['normalizations'],'explicit_label_count':nr['explicit_labels'],'theorems':6,'proofs':6,'pdf_aux_numbers_and_references_checked':True,'pdf_sha256':sha((pdf/'main.pdf').read_bytes()),'HTML_sha256':sha(combined.encode()),'checker_sha256':sha(Path(__file__).read_bytes()),'new_Lean_declarations':0,'scope':'Source/semantic transformation and numbering fidelity only. No fresh TikZ compilation, visual/browser signoff, analytic theorem verification or GRH claim.'}
 output.parent.mkdir(parents=True,exist_ok=True);output.write_text(json.dumps(report,indent=2)+chr(10));print(json.dumps(report,indent=2))
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--pdf-build',required=True,type=Path);p.add_argument('--native-build',required=True,type=Path);p.add_argument('--output',required=True,type=Path);a=p.parse_args();main(a.pdf_build,a.native_build,a.output)
