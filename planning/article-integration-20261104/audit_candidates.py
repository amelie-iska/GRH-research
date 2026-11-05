#!/usr/bin/env python3
"""Audit exactly the two isolated article candidates without changing their inputs."""
from pathlib import Path
import argparse, collections, datetime, difflib, hashlib, json, re, subprocess, unicodedata
ROOT=Path('/home/iska/Documents/LaTeX-projects/GRH-from-Mac-20261104')
PAT=r'\\begin\{(tikzpicture|tikzcd)\}.*?\\end\{\1\}'
def sha(b): return hashlib.sha256(b).hexdigest()
def normal(t): return ''.join(c.lower() for c in unicodedata.normalize('NFKD',t) if c.isascii() and c.isalnum())
def expand(path,stack=()):
 path=path.resolve()
 assert path not in stack
 text=path.read_text()
 return re.sub(r'\\input\{([^}]+)\}',lambda m:expand(ROOT/'papers'/(m[1] if m[1].endswith('.tex') else m[1]+'.tex'),stack+(path,)),text)
def audit(edition,folder,gridmanifest,acceptance):
 rec=json.loads((folder/'build-record.json').read_text())
 assert rec['passed'] and rec['edition']==edition and rec['source_unchanged']
 assert not rec['production_edited'] and not rec['production_promoted']
 unchanged={n:sha((ROOT/n).read_bytes())==h for n,h in rec['source_sha256'].items()}
 assert all(unchanged.values())
 original=expand(ROOT/'papers'/('resolutions-'+edition+'.tex'))
 assert original==(folder/'expanded-original.tex').read_text()
 actual=(folder/('resolutions-'+edition+'.expanded.tex')).read_text()
 assert str(folder.resolve())==rec['compile_output'] and str((folder/('resolutions-'+edition+'.expanded.tex')).resolve())==rec['compile_input']
 assert not re.search(r'\\input\{',actual)
 diagram_blocks=list(re.finditer(PAT,original,re.S))
 assert len(diagram_blocks)==len(rec['diagram_records'])
 accepted=json.loads((ROOT/'outputs/book/diagram-exports.json').read_text())
 by_hash={x['source_sha256']:x for x in accepted};assert len(by_hash)==len(accepted)
 grids={x['source_sha256']:x for x in gridmanifest['grids']}
 ds=[];expected=original
 for block,entry in zip(diagram_blocks,rec['diagram_records']):
  h=sha(block[0].encode());assert h==entry['source_sha256'] and block[0]==entry['source']
  assert not re.search(r'\\(?:label|input)\{',block[0])
  pdf=folder/'compiled-diagrams'/(h+'.pdf');assert sha(pdf.read_bytes())==entry['pdf_sha256']
  if h in by_hash:
   asset=by_hash[h]
   svg=ROOT/'web/book'/('main'+str(asset['index'])+'x.svg')
   assert sha(svg.read_bytes())==entry['accepted_svg_sha256']==asset['sha256']
   cache=ROOT/'outputs/html-diagrams'/h[:16]
   if (cache/'diagram.pdf').exists():
    doc=(cache/'diagram.tex').read_text()
    body=doc.split(r'\begin{document}',1)[1].split(r'\end{document}',1)[0].strip()
    assert body==block[0] and pdf.read_bytes()==(cache/'diagram.pdf').read_bytes()
    method='byte-identical sole-body cache PDF'
   else:method='accepted source-hash-matched SVG converted with installed librsvg/cairo'
  else:
   assert acceptance['accepted'] and acceptance['grid_manifest_sha256']==sha((ROOT/'outputs/article-integration-20261104/grids-v1/grid-manifest.json').read_bytes())
   g=grids[h];assert g['source']==block[0] and g['pdf_sha256']==entry['pdf_sha256']
   assert pdf.read_bytes()==Path(g['pdf']).read_bytes()
   method='independently accepted exact source-specific vector grid'
  ds.append({'source_sha256':h,'pdf_sha256':entry['pdf_sha256'],'method':method})
  replacement=r'\includegraphics[trim='+entry['trim']+',clip]{'+str(pdf.resolve())+'}'
  assert expected.count(block[0])==1
  expected=expected.replace(block[0],replacement,1)
 def packages(m):
  keep=[n for n in m['names'].split(',') if n not in {'tikz','tikz-cd','pgfplots','pgf'}]
  return r'\usepackage'+(m['options'] or '')+'{'+','.join(keep)+'}' if keep else ''
 expected=re.sub(r'\\usepackage(?P<options>\[[^\]]*\])?\{(?P<names>[^}]+)\}',packages,expected)
 expected=re.sub(r'^\\use(?:tikz|pgfplots)library\{[^}]+\}\s*\n','',expected,flags=re.M)
 packages_used={n for m in re.finditer(r'\\usepackage(?:\[[^\]]*\])?\{([^}]+)\}',expected) for n in m[1].split(',')}
 added=[n for n in ['graphicx','xcolor'] if n not in packages_used]
 if added:
  expected,n=re.subn(r'(\\documentclass(?:\[[^\]]*\])?\{[^}]+\})',lambda m:m[0]+'\n'+r'\usepackage{'+','.join(added)+'}',expected,count=1);assert n==1
 def figure(m):
  name=m['name']
  if name.startswith(str((folder/'compiled-diagrams').resolve())):return m[0]
  p=(ROOT/'papers'/name).resolve();p=p if p.suffix else p.with_suffix('.pdf')
  return r'\includegraphics'+(m['options'] or '')+'{'+str(p)+'}'
 expected=re.sub(r'\\includegraphics(?P<options>\[[^\]]*\])?\{(?P<name>[^}]+)\}',figure,expected)
 expected=re.sub(r'\\IfFileExists\{([^}]+)\}',lambda m:r'\IfFileExists{'+str((ROOT/'papers'/m[1]).resolve())+'}',expected)
 assert expected==actual,'Undocumented transformation'
 for n in [1,2,3]:
  log=(folder/f'build-pass{n}.log').read_text()
  assert 'Output written on' in log and not re.search(r'^!',log,re.M)
 final=(folder/('resolutions-'+edition+'.log')).read_text()
 bad=[s for s in final.splitlines() if re.search(r'Overfull|undefined references|Citation .* undefined|Reference .* undefined|multiply defined|multiply-defined|^!',s)]
 assert not bad
 warnings=[s for s in final.splitlines() if 'Warning' in s]
 underfull=[s for s in final.splitlines() if 'Underfull' in s]
 pdf=folder/('resolutions-'+edition+'.pdf')
 assert sha(pdf.read_bytes())==rec['pdf_sha256']
 pages=subprocess.check_output(['pdfinfo',str(pdf)],text=True);assert int(re.search(r'Pages:\s+(\d+)',pages)[1])==rec['pages']
 extracted=subprocess.check_output(['pdftotext',str(pdf),'-'],text=True)
 assert extracted==(folder/'extracted-text.txt').read_text()
 proofpages={m:[i for i,t in enumerate(extracted.split('\f'),1) if normal(m) in normal(t)] for m in rec['new_proof_markers']}
 assert all(proofpages.values())
 aux=(folder/('resolutions-'+edition+'.aux')).read_text()
 labelnames=re.findall(r'\\label\{([^}]+)\}',actual)
 assert len(labelnames)==len(set(labelnames))
 for l in ['mm:afm','rc:core','wc:uniform']:
  assert r'\newlabel{'+l+'}' in aux
 prior=ROOT/'outputs/article-integration-20261104/source-before'/('resolutions-'+edition+'.tex')
 return {'edition':edition,'passed':True,'pages':rec['pages'],'pdflatex_passes':3,'pdf_sha256':rec['pdf_sha256'],'canonical_input_count':sum(n.startswith('papers/') for n in unchanged),'all_input_hashes_unchanged':True,'input_hashes':rec['source_sha256'],'expanded_original_sha256':sha(original.encode()),'compiled_source_sha256':sha(actual.encode()),'exact_source_expansion_verified':True,'only_changes':'Documented full-source-hash diagram substitution, unused drawing imports, installed graphicx/xcolor imports and absolute figure paths. All other source bytes retained in expansion.','absolute_compile_input':rec['compile_input'],'no_input_shadowing':True,'diagrams':ds,'proof_marker_PDF_pages':proofpages,'source_label_count':len(labelnames),'new_proof_aux_labels_present':True,'final_log_unacceptable_lines':bad,'final_log_warnings':warnings,'underfull_box_count':len(underfull),'underfull_box_lines':underfull,'production_edited':False,'production_promoted':False,'previous_preintegration_wrapper_sha256':sha(prior.read_bytes()),'current_integrated_wrapper_sha256':sha((ROOT/'papers'/('resolutions-'+edition+'.tex')).read_bytes()),'scope':'Build/source fidelity only. Independent grid acceptance is external; root final article visual review and publication are separate.'}
def main():
 p=argparse.ArgumentParser();p.add_argument('--output',required=True,type=Path);a=p.parse_args();out=a.output.resolve()
 assert not out.exists();out.mkdir(parents=True)
 gm=json.loads((ROOT/'outputs/article-integration-20261104/grids-v1/grid-manifest.json').read_text())
 acceptance=json.loads((ROOT/'outputs/article-integration-20261104/grids-v1/root-acceptance.json').read_text())
 results=[audit(e,ROOT/'outputs/article-integration-20261104'/(e+'-v1'),gm,acceptance) for e in ['concise','extended']]
 report={'passed':True,'timestamp_UTC':datetime.datetime.now(datetime.timezone.utc).isoformat(),'checker_sha256':sha(Path(__file__).read_bytes()),'articles':results,'production_edited':False,'production_promoted':False}
 (out/'source-preservation-audit.json').write_text(json.dumps(report,indent=2)+'\n')
 for e in ['concise','extended']:
  p=ROOT/'papers'/('resolutions-'+e+'.tex');prior=ROOT/'outputs/article-integration-20261104/source-before'/p.name
  diff=''.join(difflib.unified_diff(prior.read_text().splitlines(True),p.read_text().splitlines(True),fromfile='prior-source-before/'+p.name,tofile='current-pre-task-integrated/'+p.name))
  (out/(e+'-earlier-wrapper-integration.diff')).write_text(diff)
 print(json.dumps({'passed':True,'articles':[{k:x[k] for k in ['edition','pages','pdf_sha256','canonical_input_count','underfull_box_count','final_log_warnings']} for x in results],'output':str(out)},indent=2))
if __name__=='__main__':main()
