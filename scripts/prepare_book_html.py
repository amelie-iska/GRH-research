#!/usr/bin/env python3
"""Repair TeX4ht image-alt escaping and add local executable reading panels.

Native MathML and SVG keep all mathematics local. Source manuscripts are copied
byte-for-byte into explicitly historical source volumes, never endorsed as proof.
"""
from theme_assets import install_theme
from pathlib import Path
from html.parser import HTMLParser
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
 'linear relations, filtrations and actual branch modules':('relations','examples/relations/check_relations.py','Exact dessin-module relation and filtration code'),
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
  if 'the remaining arithmetic theorem and a verifiable research loop' in text:
   return heading+'<aside class="reader-covering" id="mobius-proof"><h3>Signed arithmetic: exact split and a fixed-cutoff obstruction</h3><p>The two Vaughan pieces retain the original squarefree support, character zeros, conductors and annular weight. A separate-piece short-row bound for every cutoff is false at U=1; the original signed estimate and moving-cutoff approaches remain open.</p><details><summary>Lean: eight actual arithmetic-function identities and coefficient statements</summary><button class="load-code" data-source="/lean/MobiusSplit.lean">Load kernel-checked source</button><pre class="source-code"></pre></details><details><summary>Exact finite ideal/sextic evidence, with explicit profile and component order</summary><button class="load-code" data-source="/data/mobius-split.json">Load exact computed record</button><pre class="source-code"></pre></details><p><a href="https://github.com/amelie-iska/GRH-research/blob/main/scripts/check_mobius_split.py">Complete Python checker in the private repository</a>. The natural-number Dirichlet statements do not formalize the full ideal-character or prime-counting application.</p><h3 id="hecke-type-i-proof">Full-mask Hecke type-I expansion</h3><p>The squarefree inner series now has explicit primitive Euler restoration, including quadratic conductor drops and sixth-power row zeros. A classical scalar Mellin/convexity argument retains the moving divisor and profile, but its resulting error envelope does not prove the short-row mean square.</p><details><summary>Lean: seven actual complex local and finite-product restoration statements</summary><button class="load-code" data-source="/lean/HeckeTypeI.lean">Load kernel-checked Euler source</button><pre class="source-code"></pre><p>Infinite Hecke continuation, class field theory and the scalar contour proof remain named prose/external dependencies.</p></details><details><summary>Exact split/inert ideal-symbol and deleted-factor checks</summary><button class="load-code" data-source="/data/hecke-type-i.json">Load exact full-mask evidence</button><pre class="source-code"></pre></details></aside>'
  if 'coverings, equivariant ar theory and graded surfaces' in text:
   return heading+'<aside class="reader-covering"><h3>Exact covering calculation</h3><p>The displayed quiver window is a cover of a finite theta quotient, not an AR component. <a href="/data/theta-cover.json">Exact Hom/radical and higher-genus results</a>.</p><details><summary>Complete exact Python source</summary><button class="load-code" data-source="/examples/coverings/theta_cover.py">Load complete source</button><pre class="source-code"></pre></details><details><summary>Lean matrix obstruction and theorem dependencies</summary><button class="load-code" data-source="/lean/CoveringBand.lean">Load Lean source</button><pre class="source-code"></pre></details><p>Three matrix statements are kernel checked; the general categorical results remain separately scoped.</p></aside>'
  return heading
 count+=1;section,code,label=selected
 video={'atlas':'ThetaDessin','ar':'HLSDiamond','auxiliary-training':'QCNNPooling','persistence':'Bifiltration'}.get(section)
 animation=(f'<video controls="controls" preload="metadata" style="width:100%" src="/media/{video}.mp4"></video>' if video else '')
 formal=('<details><summary>Lean: actual worked polynomial resolution and Hom differentials</summary><button class="load-code" data-source="/lean/PersistenceResolution.lean">Load kernel-checked source</button><pre class="source-code"></pre><p>Ungraded worked module only; general staircase, graded, CW, coefficient-cone and arithmetic interfaces remain separate.</p></details>' if section=='persistence' else ('<details><summary>Lean: actual DG algebra and ambient nodal resolution components</summary><button class="load-code" data-source="/lean/NodalDG.lean">Load kernel-checked components</button><pre class="source-code"></pre><p>Full graded/category/completion objects and higher transfers remain separately scoped.</p></details>' if section=='dg' else ''))
 if section=='rg':formal+='<details><summary>Lean: actual finite RG marginal, partition and error identities</summary><button class="load-code" data-source="/lean/FiniteRG.lean">Load kernel-checked RG source</button><pre class="source-code"></pre><p>Nine scalar finite identities; quantum spectral logs, optimization, continuum and categorical interfaces remain separately scoped.</p></details>'
 if section=='relations':formal+='<details><summary>Lean: graphs, intertwiners and finite Fitting splitting</summary><button class="load-code" data-source="/lean/LinearRelations.lean">Load kernel-checked relation source</button><pre class="source-code"></pre><p>Eleven general linear statements; the whole dessin category and infinite-word classification are not thereby formalized.</p></details>'
 if section=='relations':formal+='<details><summary>Lean: the actual infinite algebra and its nonsplit module extension</summary><button class="load-code" data-source="/lean/BranchExtension.lean">Load complete algebra and module proof</button><pre class="source-code"></pre><p>Actual infinite polynomial algebra: nonsplit module extension, unbounded normal-image membership and spanning, and bijective algebra-valued finite expansion with explicit inverse coefficients. The separately defined path-quotient algebra comparison, categorical/AR universality and GRH remain open formal interfaces.</p></details>'
 if section=='relations':formal+='<details><summary>Exact normal-path coordinates, including million-degree examples</summary><button class="load-code" data-source="/data/normal-paths.json">Load finite exact evidence</button><pre class="source-code"></pre><p><a href="/examples/relations/check_normal_paths.py">Executable exact checker</a>. Finite diagnostics validate conventions; the arbitrary finite-support independence statement is in the Lean source above.</p></details>'
 if section=='relations':formal+='<details><summary>Actual generator products and normal-coordinate round trips</summary><button class="load-code" data-source="/data/normal-algebra.json">Load constructive exact evidence</button><pre class="source-code"></pre><p><a href="/examples/relations/check_normal_algebra.py">Constructive arrow-product checker</a>. The Lean source proves membership and spanning at every degree, including arbitrary finite expansions in the actual generated algebra.</p></details>'
 frame='/'+section+'.html?embed=book' if section in {'architecture','persistence','dg','rg','qtoken','relations'} else '/?embed='+section
 standalone='/'+section+'.html' if section in {'architecture','persistence','dg','rg','qtoken','relations'} else '/#'+section
 height=1100 if section in {'architecture','persistence','dg','rg','qtoken','relations'} else 700
 return heading+f'''<aside class="reader-lab" id="lab-{section}"><h3>Interactive {section} laboratory</h3><p>This is the canonical location of this tool. Related chapters link here instead of repeating it. Numerical illustrations are separate from proof.</p><p><a href="{standalone}">Open this laboratory separately</a>.</p><iframe loading="lazy" src="{frame}" title="Interactive {section} examples" height="{height}"></iframe>{animation}{formal}<details><summary>{label}</summary><button class="load-code" data-source="/{code}">Load complete source</button><pre class="source-code"></pre></details><p><a href="/verification.html">Exact formalization and execution coverage</a>.</p></aside>'''
s=re.sub(r'<h2 class="chapterHead">.*?</h2>',panel,s,flags=re.S)
def token_panel(m):
 global count
 heading=m[0];text=' '.join(re.sub('<[^>]+>',' ',heading).lower().split())
 if 'convextok:' not in text:return heading
 count+=1
 return heading+'<aside class="reader-lab" id="lab-convextok"><h3>Certified vocabulary and surface-path laboratory</h3><p>Original small examples of ConvexTok: inspect the occurrence DAG, fractional capacities, vocabulary choices and shortest segmentations, with exact rational certificates. The genus-two and genus-four cases encode finite permitted words of the infinite dessin algebra; they do not replace it by a finite algebra.</p><p><a href="/convextok.html">Open the tokenisation laboratory separately</a> · <a href="https://arxiv.org/html/2605.22821v1">Primary paper v1</a></p><iframe loading="lazy" src="/convextok.html?embed=book" title="ConvexTok vocabulary, LP certificates and dessin paths" height="1100"></iframe><details><summary>Complete executable optimisation and certificate code</summary><button class="load-code" data-source="/examples/tokenization/model.py">Load complete source</button><pre class="source-code"></pre></details><p>Exact small-instance optimisation, not trained language-model evidence, a coherent quantum tokenizer or a GRH proof. LP and rounding examples are not yet formalized in Lean.</p></aside>'
s=re.sub(r'<h3 class="sectionHead">.*?</h3>',token_panel,s,flags=re.S)
assert count==11, 'Expected eleven unique canonical laboratories, including ConvexTok'

s=s.replace('</body>','''<script>document.querySelectorAll('.load-code').forEach(button=>button.onclick=async()=>{const r=await fetch(button.dataset.source);const p=button.parentElement.querySelector('pre');p.textContent=r.ok?await r.text():'Source unavailable';button.hidden=true;});
function fitReaderMath(){
 const targets=[];
 for(const math of document.querySelectorAll('math')){
  if(math.closest('.reader-table-scroll,.reader-inline-math'))continue;
  const parent=math.closest('p,li,dd,dt,div,section,article,aside,body');
  if(!parent)continue;
  const style=getComputedStyle(parent);
  const width=parent.clientWidth-parseFloat(style.paddingLeft)-parseFloat(style.paddingRight);
  if(math.getBoundingClientRect().width>width+1)targets.push(math);
 }
 for(const math of targets){
  const box=document.createElement('span');box.className='reader-inline-math';
  box.tabIndex=0;box.setAttribute('aria-label','Scrollable mathematical expression');
  math.replaceWith(box);box.append(math);
 }
}
fitReaderMath();
addEventListener('resize',()=>requestAnimationFrame(fitReaderMath));
document.addEventListener('toggle',fitReaderMath,true);
if(document.fonts)document.fonts.ready.then(fitReaderMath);
</script></body>''')
# TeX4ht equation tables retain their intrinsic width on small screens.
# An outer scroll box preserves all MathML/table geometry without allowing
# mobile browsers to shrink the entire book to the widest equation.
if 'class="reader-table-scroll"' not in s:
 class TableScroll(HTMLParser):
  def __init__(self, source):
   super().__init__(convert_charrefs=False)
   self.source=source;self.depth=0;self.edits=[]
   self.starts=[0]+[m.end() for m in re.finditer('\n',source)]
  def source_offset(self):
   line,column=self.getpos();return self.starts[line-1]+column
  def handle_starttag(self,tag,attrs):
   if tag=='table':
    if self.depth==0:self.edits.append((self.source_offset(),'<div class="reader-table-scroll" tabindex="0" aria-label="Scrollable mathematical or data table">'))
    self.depth+=1
  def handle_endtag(self,tag):
   if tag=='table':
    self.depth-=1
    if self.depth==0:self.edits.append((self.source.index('>',self.source_offset())+1,'</div>'))
 scroll=TableScroll(s);scroll.feed(s);assert scroll.depth==0
 for offset,markup in sorted(scroll.edits,reverse=True):s=s[:offset]+markup+s[offset:]
ET.fromstring(s)
p.write_text(s)
(BOOK/'reader.css').write_text('''body{max-width:960px;margin:90px auto 60px;padding:0 32px;background:#f5f3ec;color:#182c2b;overflow-wrap:anywhere;font:18px/1.7 Georgia,serif}h1,h2,h3,h4{color:#145e4d}.reader-covering h3[id],h2.chapterHead{scroll-margin-top:100px}h2.chapterHead{margin-top:95px;padding-top:25px;border-top:1px solid #bdc9bc}a{color:#145e4d}img{max-width:100%;height:auto}math[display=block]{overflow-x:auto;padding:12px 0}.reader-nav{position:fixed;z-index:10;top:0;left:0;right:0;padding:14px 4vw;background:#f5f3ecef;border-bottom:1px solid #d4ded3;font:13px/1.5 system-ui}.reader-nav span{float:right;color:#56706a}.reader-lab,.reader-covering{background:#e9eee5;border:1px solid #d4ded3;border-radius:10px;padding:20px;margin:25px 0 45px;font:14px/1.6 system-ui}.reader-lab iframe{width:100%;border:0;border-radius:8px;background:#f5f3ec}.reader-lab pre,.reader-covering pre{white-space:pre-wrap;max-height:650px;overflow:auto;padding:15px;background:white;font:12px/1.7 monospace}button,summary{cursor:pointer}figure,table{max-width:100%}.reader-table-scroll{max-width:100%;overflow-x:auto;margin:12px 0;-webkit-overflow-scrolling:touch}.reader-inline-math{display:inline-block;max-width:100%;overflow-x:auto;vertical-align:middle}.reader-inline-math:focus-visible,.reader-table-scroll:focus-visible{outline:2px solid #078b96;outline-offset:3px}@media(max-width:700px){body{padding:0 14px}.reader-nav span{display:none}}''')
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
