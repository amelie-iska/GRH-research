"""Finish integrated-edition framing, mobile layout and new-data integrity.

Only exact integration sources/outputs are changed. Measurements and frozen
models are not modified. Execute before the source-binding commit.
"""
from pathlib import Path
import argparse,hashlib,json,re
ROOT=Path(__file__).resolve().parents[2]

def apply(evidence):
 atlas=ROOT/'extension/site';page=atlas/'index.html';text=page.read_text()
 style='''<style id="integration-layout-fix">#integratedMount{min-width:0;max-width:100%}#integrated-laboratory{min-width:0}.site-header nav{flex-wrap:wrap}@media(max-width:580px){.site-header nav{justify-content:flex-start;column-gap:18px;row-gap:4px}.site-header nav a{display:inline-flex;align-items:center;min-height:44px}}</style>'''
 if 'id="integration-layout-fix"'not in text:text=text.replace('</head>',style+'</head>',1)
 text=text.replace('<h3>121 selected formal declarations</h3>','<h3>Source-scoped formal evidence</h3>')
 old='<p id="proofStatus">';pos=text.index(old);end=text.index('</p>',pos)
 text=text[:pos]+old+'The original seven-module development retains its dated record of 121 selected declarations. This unified integration separately rechecks 26 declarations, including four new arithmetic/operator contracts. These source-scoped counts are not a claim that every theorem in the full monograph or its external continuum sources has been formalized.'+text[end:]
 text=text.replace('<p id="proofDetails">','<p id="proofDetails">The <a href="verification/integration/manifest.json">unified integration record</a> identifies the new source, tests and document. ',1);page.write_text(text)
 p=ROOT/'extension/manuscript/chapters/preface.tex';s=p.read_text();anchor='\\addcontentsline{toc}{chapter}{Abstract and reading contract}\n'
 paragraph=r'''\noindent\textbf{Unified edition, 14 November 2026.} The original monograph and both later research bodies now form this one source-built book, with continuous chapter and theorem numbering. The integrated chapters add certified surface computation, measured graph-learning controls, complete finite elliptic circuits, covering theory for orders and networks, trained quantum coarse graining, observed WMAP searches and executed uniform-arithmetic, operator-learning and calibration steps. Earlier dated verification records retain their original scope; the new integration has its own source-bound tests. The existing project homepage embeds the new experiments and links to this same current document.

'''
 if 'Unified edition, 14 November 2026.'not in s:s=s.replace(anchor,anchor+paragraph,1);p.write_text(s)
 target=atlas/'verification/integration/next-steps.json';meta={'schema':'grh.next-steps.integrity.v1','bytes':target.stat().st_size,'sha256':hashlib.sha256(target.read_bytes()).hexdigest(),'scope':'Exact integrated uniform circuits, exported neural operator and precision-study data.'};(target.parent/'next-steps-manifest.json').write_text(json.dumps(meta,indent=2)+'\n')
 p=atlas/'integrated-next-steps.js';s=p.read_text();old="const response=await fetch('verification/integration/next-steps.json');if(!response.ok)throw new Error('Missing integrated evidence');const data=await response.json();";new="const integrity=await(await fetch('verification/integration/next-steps-manifest.json')).json();const data=await window.Program3.verifiedJSON('verification/integration/next-steps.json',integrity.sha256);"
 if old not in s:raise ValueError('Exact evidence-loader anchor missing')
 s=s.replace(old,new).replace('window.GRHExtensionReplay=()=>({state:{...state},','window.GRHExtensionReplay=()=>({evidence_sha256:integrity.sha256,state:{...state},');p.write_text(s)
 c=json.loads((evidence/'calibration.json').read_text());p=ROOT/'extension/manuscript/integrated/calibration-table.tex';s=p.read_text();addition='Conditional tail interval (95\\%) & '+f"[{c['conditional_tail_binomial_interval_95'][0]:.6f}, {c['conditional_tail_binomial_interval_95'][1]:.6f}]"+'\\\\\n'+'Null-validation interval (95\\%) & '+f"[{c['null_validation']['interval_95'][0]:.6f}, {c['null_validation']['interval_95'][1]:.6f}]"+'\\\\\n';p.write_text(s.replace('\\bottomrule',addition+'\\bottomrule'))
 print('Current-edition framing, responsive navigation, data hashes and numerical uncertainty intervals integrated.')
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--evidence',type=Path,required=True);a=p.parse_args();apply(a.evidence)
