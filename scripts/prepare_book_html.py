#!/usr/bin/env python3
"""Repair TeX4ht image-alt escaping and add local executable reading panels.

Native MathML and SVG keep all mathematics local. Source manuscripts are copied
byte-for-byte into explicitly historical source volumes, never endorsed as proof.
"""
from theme_assets import install_theme
from pathlib import Path
import re,html,json,hashlib,shutil,sys,xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[1];WEB=ROOT/'web';BOOK=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else WEB/'book';p=BOOK/'main.html';s=p.read_text()
s=re.sub(r'<aside class="reader-lab"[^>]*>.*?</aside>','',s,flags=re.S)
s=re.sub(r'<aside class="reader-animation"[^>]*>.*?</aside>','',s,flags=re.S)
s=re.sub(r'<aside class="reader-covering"[^>]*>.*?</aside>','',s,flags=re.S)
s=re.sub(r'<div class="reader-nav">.*?</div>','',s,flags=re.S)
s=s.replace('<link rel="stylesheet" href="reader.css" />','')
s=re.sub(r"<script>document.querySelectorAll\('\.load-code'\).*?</script>",'',s,flags=re.S)
s=re.sub(r'(<img\b.*?\balt=")(.*?)("\s*/>)',lambda m:m[1]+html.escape(html.unescape(m[2]),quote=True)+m[3],s,flags=re.S)
# After TeX4ht the malformed alt string is the only XML-level corruption.
ET.fromstring(s)
style='''<link rel="stylesheet" href="reader.css" />'''
s=s.replace('</head>',style+'</head>')
header='''<div class="reader-nav"><a href="/">Research atlas</a> · <a href="/book.pdf">PDF</a> · <a href="/source-volumes.html">Full source volumes</a><span>Critical working edition · selected Lean checks · GRH open</span></div>'''
s=re.sub(r'(<body\s*>)',r'\1'+header,s,count=1)
count=0
canonical={
 'cellular dessins and their infinite orders':('atlas','examples/sage/dessin_orders.sage','Exact Sage construction'),
 'almost-split geometry, hom control and determinant relations':('ar','lean/BookInterfaces.lean','Lean matrix and determinant interfaces'),
 'positive evolution, clocks and holonomy':('circuits','examples/quantum/backend_adapters.py','Six-backend carrier code'),
 'quantum feature models and auxiliary compression':('auxiliary-training','examples/quantum/train_pennylane.py','Preserved auxiliary training code'),
 'actual renormalization: effective actions and scale':('rg','examples/rg/rg_math.py','Actual finite RG definitions and checks'),
 'quantum tokengt, concept navigation and error correction':('qtoken','examples/quantum_tokengt/EXPOSITION.md','Executed quantum TokenGT and learning methods'),
 'dg foundations, clock lifts and endpoint-sensitive extensions':('dg','examples/dg/check_nodal_dg.py','Exact DG and theta endpoint checks'),
 'two-parameter persistence, schur syzygies':('persistence','examples/persistence/check_tool.py','Exact staircase and finite homology checks'),
 'reading an architecture from its tensors':('architecture','examples/architecture/README.md','Numerical architecture records and reproduction')}
def panel(m):
 global count
 heading=m[0];text=' '.join(re.sub('<[^>]+>',' ',heading).lower().split())
 selected=next((v for title,v in canonical.items() if title in text),None)
 if selected is None:
  if 'coverings, equivariant ar theory and graded surfaces' in text:
   return heading+'<aside class="reader-covering"><h3>Exact covering calculation</h3><p>The displayed quiver window is a cover of a finite theta quotient, not an AR component. <a href="/data/theta-cover.json">Exact Hom/radical and higher-genus results</a>.</p><details><summary>Complete exact Python source</summary><button class="load-code" data-source="/examples/coverings/theta_cover.py">Load complete source</button><pre class="source-code"></pre></details><details><summary>Lean matrix obstruction and theorem dependencies</summary><button class="load-code" data-source="/lean/CoveringBand.lean">Load Lean source</button><pre class="source-code"></pre></details><p>Three matrix statements are kernel checked; the general categorical results remain separately scoped.</p></aside>'
  return heading
 count+=1;section,code,label=selected
 video={'atlas':'ThetaDessin','ar':'HLSDiamond','auxiliary-training':'QCNNPooling','persistence':'Bifiltration'}.get(section)
 animation=(f'<video controls="controls" preload="metadata" style="width:100%" src="/media/{video}.mp4"></video>' if video else '')
 formal=('<details><summary>Lean: actual worked polynomial resolution and Hom differentials</summary><button class="load-code" data-source="/lean/PersistenceResolution.lean">Load kernel-checked source</button><pre class="source-code"></pre><p>Ungraded worked module only; general staircase, graded, CW, coefficient-cone and arithmetic interfaces remain separate.</p></details>' if section=='persistence' else ('<details><summary>Lean: actual DG algebra and ambient nodal resolution components</summary><button class="load-code" data-source="/lean/NodalDG.lean">Load kernel-checked components</button><pre class="source-code"></pre><p>Full graded/category/completion objects and higher transfers remain separately scoped.</p></details>' if section=='dg' else ''))
 if section=='rg':formal+='<details><summary>Lean: actual finite RG marginal, partition and error identities</summary><button class="load-code" data-source="/lean/FiniteRG.lean">Load kernel-checked RG source</button><pre class="source-code"></pre><p>Nine scalar finite identities; quantum spectral logs, optimization, continuum and categorical interfaces remain separately scoped.</p></details>'
 frame='/'+section+'.html?embed=book' if section in {'architecture','persistence','dg','rg','qtoken'} else '/?embed='+section
 standalone='/'+section+'.html' if section in {'architecture','persistence','dg','rg','qtoken'} else '/#'+section
 height=1100 if section in {'architecture','persistence','dg','rg','qtoken'} else 700
 return heading+f'''<aside class="reader-lab" id="lab-{section}"><h3>Interactive {section} laboratory</h3><p>This is the canonical location of this tool. Related chapters link here instead of repeating it. Numerical illustrations are separate from proof.</p><p><a href="{standalone}">Open this laboratory separately</a>.</p><iframe loading="lazy" src="{frame}" title="Interactive {section} examples" height="{height}"></iframe>{animation}{formal}<details><summary>{label}</summary><button class="load-code" data-source="/{code}">Load complete source</button><pre class="source-code"></pre></details><p><a href="/verification.html">Exact formalization and execution coverage</a>.</p></aside>'''
s=re.sub(r'<h2 class="chapterHead">.*?</h2>',panel,s,flags=re.S)
s=s.replace('</body>','''<script>document.querySelectorAll('.load-code').forEach(button=>button.onclick=async()=>{const r=await fetch(button.dataset.source);const p=button.parentElement.querySelector('pre');p.textContent=r.ok?await r.text():'Source unavailable';button.hidden=true;});</script></body>''')
p.write_text(s)
(BOOK/'reader.css').write_text('''body{max-width:960px;margin:90px auto 60px;padding:0 32px;background:#f5f3ec;color:#182c2b;font:18px/1.7 Georgia,serif}h1,h2,h3,h4{color:#145e4d}h2.chapterHead{margin-top:95px;padding-top:25px;border-top:1px solid #bdc9bc}a{color:#145e4d}img{max-width:100%;height:auto}math[display=block]{overflow-x:auto;padding:12px 0}.reader-nav{position:fixed;z-index:10;top:0;left:0;right:0;padding:14px 4vw;background:#f5f3ecef;border-bottom:1px solid #d4ded3;font:13px/1.5 system-ui}.reader-nav span{float:right;color:#56706a}.reader-lab,.reader-covering{background:#e9eee5;border:1px solid #d4ded3;border-radius:10px;padding:20px;margin:25px 0 45px;font:14px/1.6 system-ui}.reader-lab iframe{width:100%;border:0;border-radius:8px;background:#f5f3ec}.reader-lab pre,.reader-covering pre{white-space:pre-wrap;max-height:650px;overflow:auto;padding:15px;background:white;font:12px/1.7 monospace}button,summary{cursor:pointer}figure,table{max-width:100%}@media(max-width:700px){body{padding:0 14px}.reader-nav span{display:none}}''')
# Preserve both supplied sources in full; trust neither filename nor source claims.
rows=json.loads((ROOT/'book/source-provenance.json').read_text());dest=ROOT/'book/source-editions';dest.mkdir(exist_ok=True);online=WEB/'sources';online.mkdir(exist_ok=True)
links=[]
for row in rows:
 original=Path(row['path']);preserved=ROOT/'book/source-editions'/original.name
 data=(original if original.exists() else preserved).read_bytes();assert hashlib.sha256(data).hexdigest()==row['sha256']
 edition='2053' if '_2053.tex' in original.name else 'COMPLETED'
 target=dest/original.name
 if not target.exists():target.write_bytes(data)
 assert hashlib.sha256(target.read_bytes()).hexdigest()==row['sha256']
 shutil.copyfile(target,online/(edition+'.tex'))
 sections=[];lines=data.decode().splitlines();heads=[(r['line'],r['title']) for r in row['chapters'] if r['title'].lstrip().startswith('\\chapter')]
 heads=[(1,'Preamble and front matter')]+heads
 for j,(start,title) in enumerate(heads):
  end=heads[j+1][0]-1 if j+1<len(heads) else len(lines)
  code='\n'.join(f'{i}: {lines[i-1]}' for i in range(start,end+1))
  sections.append(f'<details><summary>{html.escape(title)} · lines {start}–{end}</summary><pre>{html.escape(code)}</pre></details>')
 body=f'<h1>Complete historical source: {edition}</h1><p>This is the entire supplied source, preserved byte-for-byte. It includes refuted and unproved assertions. Read the critical book and correction ledger for current status; this source volume is not a certified GRH proof.</p><p>SHA256 {row["sha256"]} · {len(lines)} lines. <a href="{edition}.tex">Download exact TeX</a> · <a href="/book/main.html">Critical book</a></p>'+''.join(sections)
 (online/(edition+'.html')).write_text('<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Historical source '+edition+'</title><link rel="stylesheet" href="/style.css"></head><body><main>'+body+'</main><style>pre{white-space:pre-wrap;max-height:75vh;overflow:auto}summary{cursor:pointer;padding:12px;border-bottom:1px solid #ccc}</style></body></html>')
 links.append(f'<li><a href="/sources/{edition}.html">Complete {edition} source: {len(lines)} lines</a></li>')
(WEB/'source-volumes.html').write_text('<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Complete source volumes</title><link rel="stylesheet" href="/style.css"></head><body><main><section><h1>Complete source volumes</h1><p>All text, formulas, source diagrams and code from both supplied TeX files is preserved here. These historical documents contain claims corrected or refuted by the audits. Preservation is distinct from endorsement, complete rewriting, execution or Lean formalization.</p><ul>'+''.join(links)+'</ul><p><a href="/book/main.html">Read the developed critical book</a> · <a href="/verification.html">See formalization coverage and outstanding work</a></p></section></main></body></html>')
print('Native-MathML book prepared:',count,'chapter panels; both complete source volumes preserved')

# Preserve the shared theme on regenerated book and historical HTML views.
for themed_page in [BOOK/"main.html", WEB/"source-volumes.html", *online.glob("*.html")]:
 install_theme(themed_page)
