"""One native manuscript and one existing atlas, preserving historical source."""
import argparse,hashlib,json,re,shutil
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def table(path,columns,headers,rows):
 path.write_text('\\begin{tabular}{'+columns+'}\\toprule '+headers+'\\\\\\midrule\n'+'\n'.join(' & '.join(map(str,row))+'\\\\'for row in rows)+'\n\\bottomrule\\end{tabular}\n')

def manuscript(evidence):
 directory=ROOT/'extension/manuscript';generated=directory/'integrated';generated.mkdir(exist_ok=True);a=json.loads((evidence/'arithmetic/results.json').read_text());q=json.loads((evidence/'neural-operator.json').read_text());c=json.loads((evidence/'calibration.json').read_text())
 table(generated/'uniform-field-table.tex','rlrrr','Prime & Operation & Gates & Scratch & Tested inputs',[[r['p'],r['operation'],r['resources']['total_gates'],r['resources']['clean_scratch'],r['tested_words']]for r in a['records']])
 table(generated/'operator-table.tex','lrrr','Seed & Held-out cases & Maximum learned error & Maximum analytic error',[[s,len([r for r in q['results']if r['seed']==s]),f"{max(r['operator_norm_error']for r in q['results']if r['seed']==s):.6f}",f"{max(r['analytic_poisson_error']for r in q['results']if r['seed']==s):.3g}"]for s in(17,29,47)])
 table(generated/'calibration-table.tex','lr','Precision-study quantity & Value',[["Calibration draws",c['calibration_draws']],["Observed exceedances",c['exceedances']],["Finite rank",f"{c['rank_p']:.6f}"],["Independent null rejections",str(c['null_validation']['rejections'])+'/'+str(c['validation_draws'])]])
 p=directory/'main.tex';s=p.read_text()
 if 'INTEGRATED-EDITION-20261114'in s:raise ValueError('Integration already applied')
 inherited_inputs=re.findall(r'\\input\{([^}]+)\}',s)
 config=r'''
% INTEGRATED-EDITION-20261114: continuous book counters and table of contents.
\newcommand{\WorkbenchResearchRoot}{../../workbench/research}
\makeatletter
\def\input@path{{../../workbench/research/}{../../releases/program3-20261114/evidence/paper/}}
\makeatother
\graphicspath{{../../releases/program3-20261114/evidence/paper/}}
\setlength{\emergencystretch}{3em}
'''
 s=s.replace('\\begin{document}',config+'\n\\begin{document}',1)
 s=re.sub(r'\\date\{13 November 2026.*?\n',lambda m:r'\date{14 November 2026\\\small Unified research monograph, version 1.5: integrated constructions and completed computational steps}'+'\n',s,count=1)
 s=s.replace('\\input{chapters/implemented-cryptography}','\\input{chapters/implemented-cryptography}\n\\input{../../workbench/research/program3-arithmetic}')
 s=s.replace('\\input{chapters/quantum-tropical-realizations}','\\input{chapters/quantum-tropical-realizations}\n\\input{../../workbench/research/program3-covering-rg}\n\\input{../../workbench/research/program3-dependent-width}\n\\begin{center}\\small\\input{gate-controls-table}\\end{center}')
 s=s.replace('\\input{chapters/cyclic-cosmology}','\\input{chapters/cyclic-cosmology}\n\\input{../../workbench/research/program3-cosmology}\n\\input{../../workbench/research/program3-joint-controls}')
 wb=r'''
\part{Certified surface computation and its measured realizations}
\input{../../workbench/research/unified-program}
\input{../../workbench/research/framework-map}
\input{../../workbench/research/half-density}
\input{../../workbench/research/source-proof-repair}
\input{../../workbench/research/finite-formalization}
\chapter{Graph languages and computational mechanisms}
\input{../../workbench/research/language-graph-computation}
\chapter{Physical data, coding and the measured study}
\input{../../workbench/research/physical-information}
\input{../../workbench/research/results-summary}
\input{../../workbench/research/information-and-controls}
\chapter{BGG, category \texorpdfstring{$\mathcal O$}{O} and structural synthesis}
\input{../../workbench/research/bgg-category-o}
\input{../../workbench/research/surface-guide}
\input{../../workbench/research/surface-diagram}
\part{Completed computational steps and the unified research program}
\input{../../workbench/integration/completed-next-steps}
'''
 s=s.replace('\\input{chapters/synthesis}',wb+'\n\\input{chapters/synthesis}')
 appendix=r'''
\begingroup\footnotesize\raggedright
\input{../../workbench/research/references}
\input{integrated/program3-source-register}
\endgroup
\input{integrated/prior-program3-execution}
'''
 s=s.replace('\\backmatter',appendix+'\n\\backmatter')
 if not all('\\input{'+x+'}'in s for x in inherited_inputs):raise AssertionError('Original input omitted')
 p.write_text(s);prior=(ROOT/'workbench/research/program3-main.tex').read_text();sources=prior.split('\\appendix',1)[1].split('\\end{document}',1)[0].replace('\\chapter{Primary sources and evidence boundaries}','\\chapter{Arithmetic and quantum-renormalization source register}');(generated/'program3-source-register.tex').write_text(sources);body=prior.split('\\chapter{Execution and reproducibility}',1)[1].split('\\appendix',1)[0];(generated/'prior-program3-execution.tex').write_text('\\chapter{Source-bound verification of the earlier computational continuation}\nThe following preserved execution record refers to the pinned program-three release. This unified edition has an additional integration record; earlier test counts are not represented as expanded proof coverage.\n'+body)
 synth=directory/'chapters/synthesis.tex';text=synth.read_text();start=text.index('\\subsection{Resource-certified elliptic-curve quantum arithmetic}');end=text.index('\\subsection{',start+20)
 text=text[:start]+r'''\subsection{Resource-certified elliptic-curve quantum arithmetic}
The finite reproducibility program is executed in Chapter~\ref{ch:p3-ecc}, within this same monograph. It fixes affine/infinity encoding, total invalid-word behavior, logical gates, clean work, coherent signed decomposition and independent resource accounting. The measured decomposition costs more for the original bounded compiler; this result is retained rather than replaced by an unsupported efficiency claim.

Chapter~\ref{ch:integrated-next-steps} completes the next field-arithmetic step with uniform carry, borrow, product, reduction and inversion circuits, together with executed small-domain and wider sampled checks. This replaces exponential input-table synthesis for those primitives, without claiming that a complete large-curve elliptic algorithm or fault-tolerant compilation has already been built. Chapter~\ref{ch:p3-coverings} develops the covering, integral-order and learned-channel constructions; Chapter~\ref{ch:p3-ccc} and the completed-steps chapter supply the observed-sky tests and their calibration limits. Their statements, measurements and interactive examples belong to the same continuing document and project page.

'''+text[end:];synth.write_text(text)
 names=['unified-program.tex','framework-map.tex','half-density.tex','source-proof-repair.tex','finite-formalization.tex','language-graph-computation.tex','language-expressivity.tex','language-machines.tex','language-training.tex','language-synthesis.tex','analogy-deduction.tex','physical-information.tex','results-summary.tex','information-and-controls.tex','bgg-category-o.tex','surface-guide.tex','surface-diagram.tex','references.tex','program3-arithmetic.tex','program3-covering-rg.tex','program3-dependent-width.tex','program3-cosmology.tex','program3-joint-controls.tex','program3-main.tex'];record={'schema':'grh.unified-source-map.v1','main':'extension/manuscript/main.tex','original_input_count':len(inherited_inputs),'all_original_inputs_retained':True,'supplement_sources':{str((ROOT/'workbench/research'/x).relative_to(ROOT)):sha(ROOT/'workbench/research'/x)for x in names},'native_continuous_numbering':True,'pdf_concatenation':False};(evidence/'manuscript-integration.json').write_text(json.dumps(record,indent=2)+'\n')

def site(evidence):
 atlas=ROOT/'extension/site';site=ROOT/'workbench/site';p=atlas/'index.html';s=p.read_text()
 if 'id="integratedMount"'in s:raise ValueError('Already integrated')
 snippet='''<section id="integrated-laboratory" class="section-width" aria-labelledby="integrated-title"><div class="section-heading"><div><p class="eyebrow">Integrated research and completed steps</p><h2 id="integrated-title">One manuscript.<br>Executable constructions.</h2></div><p class="section-intro">The arithmetic, covering, learned-channel and observed-sky studies are embedded here. Their proofs and results are in the same current monograph, with existing chapters and laboratories preserved.</p></div><p><a class="button primary" href="downloads/paper.pdf">Read the unified monograph</a> <a class="button secondary" href="#research">Document and evidence</a></p><div id="integratedMount"><p>Loading the integrated experiments. The same monograph remains available above.</p></div></section>'''
 s=s.replace('<section id="research"',snippet+'\n<section id="research"',1).replace('<a href="#research">Research</a>','<a href="#research">Research</a><a href="#integrated-laboratory">Integrated experiments</a>',1).replace('355-PAGE RESEARCH MONOGRAPH','UNIFIED CURRENT RESEARCH MONOGRAPH').replace('href="downloads/fluid-extension.pdf"','href="downloads/paper.pdf"').replace('STANDALONE RESEARCH SUPPLEMENT','INCLUDED IN THE SAME MONOGRAPH')
 s=s.replace('</head>','<script defer src="quantum-core.js"></script><script defer src="workbench/program3-core.js"></script><script defer src="integrated-app.js"></script><script defer src="integrated-next-steps.js"></script></head>',1);p.write_text(s)
 html=(site/'program3.html').read_text();content=html.split('<main>',1)[1].split('</main>',1)[0].replace('href="program3-report.pdf"','href="downloads/paper.pdf"').replace('Read the 21-page supplement','Read the unified monograph');content='<p id="loadStatus" role="status">Checking the preserved scientific assets...</p><main>'+content+'</main>';css=(site/'program3.css').read_text().replace(':root',':host').replace('body{',':host{')+'\n:host{display:block}main{padding:0}input[type=number]{width:100%;min-height:44px;border:1px solid #91a9ae;border-radius:5px;padding:8px}#completed-steps{margin-top:24px}';js=(site/'program3-app.js').read_text()
 changes={"(function(){'use strict';":"(function(root){'use strict';","$=id=>document.getElementById(id)":"$=id=>root.getElementById(id)","fetch('program3-manifest.json')":"fetch('workbench/program3-manifest.json')","P.verifiedJSON(a.url,a.sha256)":"P.verifiedJSON(new URL(a.url,new URL('workbench/program3-manifest.json',location.href)).href,a.sha256)","document.documentElement.dataset.program3Ready":"root.host.dataset.program3Ready","p.has(key)":"p.has('p3_'+key)","p.get(key)":"p.get('p3_'+key)","const p=new URLSearchParams();for(const[k,v]of Object.entries(state))p.set(k,v);history.replaceState(null,'','?'+p);":"const p=new URLSearchParams(location.search);for(const[k,v]of Object.entries(state))p.set('p3_'+k,v);history.replaceState(null,'','?'+p+location.hash);","state:{...state},arithmetic:last.arithmetic":"state:{...state},completedNextSteps:window.GRHExtensionReplay?window.GRHExtensionReplay():null,arithmetic:last.arithmetic"}
 for old,new in changes.items():
  if old not in js:raise ValueError('JS anchor missing '+old)
  js=js.replace(old,new)
 if not js.rstrip().endswith('})();'):raise ValueError('Unexpected closure')
 js=js.rstrip()[:-5]+"})(document.getElementById('integratedMount').shadowRoot);\n";bootstrap="(function(){const host=document.getElementById('integratedMount');host.replaceChildren();const root=host.attachShadow({mode:'open'});root.innerHTML="+json.dumps('<style>'+css+'</style>'+content)+";})();\n";(atlas/'integrated-app.js').write_text(bootstrap+js);shutil.copy2(ROOT/'workbench/integration/next-steps.js',atlas/'integrated-next-steps.js');target=atlas/'workbench';target.mkdir(exist_ok=True)
 for name in('program3-core.js','program3-manifest.json'):shutil.copy2(site/name,target/name)
 shutil.copytree(site/'program3-assets',target/'program3-assets',dirs_exist_ok=True)
 data={'arithmetic':json.loads((evidence/'arithmetic/results.json').read_text()),'operator':json.loads((evidence/'neural-operator.json').read_text()),'calibration':json.loads((evidence/'calibration.json').read_text()),'circuits':{}}
 for f in(evidence/'arithmetic').glob('field-*.json'):
  circuit=json.loads(f.read_text());data['circuits'][str(circuit['p'])+'-'+circuit['operation']]=circuit
 dest=atlas/'verification/integration';dest.mkdir(parents=True,exist_ok=True);(dest/'next-steps.json').write_text(json.dumps(data,separators=(',',':'))+'\n')
 redirect='''<!doctype html><html lang="en"><meta charset="utf-8"><title>Integrated research experiments</title><p>The experiments now belong to the <a href="../#integrated-laboratory">same main project page</a>.</p><script>const p=new URLSearchParams(location.search),u=new URL('../',location.href);for(const[k,v]of p)u.searchParams.set(k.startsWith('p3_')?k:'p3_'+k,v);u.hash='integrated-laboratory';location.replace(u.href);</script></html>''';(target/'program3.html').write_text(redirect);(site/'program3.html').write_text(redirect)
 readme=ROOT/'README.md';text=readme.read_text();entry='''## Unified current edition\n\nThe current manuscript is built from `extension/manuscript/main.tex`. It includes\nCertified Surface Computation, elliptic arithmetic, covering-compatible learned\nquantum channels, real-WMAP controls and executed next steps in one continuously\nnumbered book. The existing homepage embeds the experiments at\n`#integrated-laboratory`; `downloads/paper.pdf` is the same current document.\nHistorical releases remain immutable evidence, not current installments.\nThe integration record is in `planning/integrated-research-20261114/`.\n\n''';pos=text.index('## ');readme.write_text(text[:pos]+entry+text[pos:])

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--evidence',type=Path,required=True);a=p.parse_args();manuscript(a.evidence);site(a.evidence);print('Native manuscript and main-page integration generated.')
