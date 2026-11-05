from pathlib import Path
import json,hashlib
R=Path('/home/iska/Documents/LaTeX-projects/GRH-from-Mac-20261104');O=R/'outputs/checks/2026-11-05-signed-divisor/root/integration-v1';O.mkdir(parents=True,exist_ok=False)
def backup(n):
 p=R/n
 if p.exists():
  q=O/'before'/n;q.parent.mkdir(parents=True,exist_ok=True);q.write_bytes(p.read_bytes())
for n in ['scripts/assemble_book.py','planning/book-integration-20261104/render_native.py','book/chapters/weighted-cutoff.tex','papers/resolutions-concise.tex','papers/resolutions-extended.tex','papers/validated-oracle-concise.tex','papers/validated-oracle-extended.tex','web/book/main.html','outputs/book/surface-orders-book.pdf']:backup(n)
accept=R/'outputs/checks/2026-11-05-signed-divisor/review-design/canonical-acceptance-v1.json';assert hashlib.sha256(accept.read_bytes()).hexdigest()=='7380ac5b188a1f0a3db8fb87509d9d0ab3e81c072d8a270aef1b4d09654047f2'
for part,h in [('core','bce916fab66aab19718a127b26b3ac581e48f49e0dd0317a64cf1648a4e5b7cb'),('details','504318141e100fd43f1021492c349a655953909b3213a083452d1230fa35cbc9')]:
 src=R/('planning/signed-divisor-20261105/root/signed-divisor-'+part+'.tex');data=src.read_bytes();assert hashlib.sha256(data).hexdigest()==h
 p=R/('papers/signed-divisor-'+part+'.tex');assert not p.exists();p.write_bytes(data)
 p=R/('book/chapters/signed-divisor-'+part+'.tex');assert not p.exists();p.write_bytes(b'% Generated shared reviewed material.\n'+data)
figure=R/'book/chapters/signed-divisor-figure.tex';assert not figure.exists();figure.write_text(r'''% Original data-bound workflow figure; no repeated generic panel.
\begin{figure}[ht]
\centering
\includegraphics[width=\linewidth]{figures/signed-divisor-workflow.pdf}
\caption{Exact divisor workflow for the complete D=60000 reference: 16953 columns, 21750 divisor buckets and twenty rows. The fixed study profile and literal class are specified in the text; no asymptotic saving is asserted.}
\label{sd:workflow}
\end{figure}
''')
p=R/'book/chapters/weighted-cutoff.tex';s=p.read_text();assert 'signed-divisor' not in s;s+='\\input{chapters/signed-divisor-core}\n\\input{chapters/signed-divisor-figure}\n\\input{chapters/signed-divisor-details}\n';p.write_text(s)
p=R/'scripts/assemble_book.py';s=p.read_text();needle="'signed-weights-core','signed-weights-details'";assert s.count(needle)==1;s=s.replace(needle,needle+",'signed-divisor-core','signed-divisor-details'");p.write_text(s)
for name in ['resolutions-concise','resolutions-extended','validated-oracle-concise','validated-oracle-extended']:
 p=R/('papers/'+name+'.tex');s=p.read_text();islong=name.endswith('extended');last='signed-weights-details' if islong else 'signed-weights-core';needle='\\input{'+last+'}';assert s.count(needle)==1
 inputs='\\input{signed-divisor-core}'+ ('\n\\input{signed-divisor-details}'if islong else '')
 s=s.replace(needle,needle+'\n'+inputs)
 marker='The arithmetic positive determinant comparison remains open;' if name.startswith('resolutions') else 'No proof of GRH or complete Lean formalization is asserted.'
 assert s.count(marker)==1;s=s.replace(marker,'A signed common-divisor zeta expansion and a complete-column exact laboratory retain every raw mask; weighted divisor certificates do not close the required asymptotic saving. '+marker);p.write_text(s)
record={'passed':True,'scope':'Accepted canonical sources and original book-only figure integrated before isolated staging; no production artifact promotion','canonical_acceptance_sha256':hashlib.sha256(accept.read_bytes()).hexdigest(),'core_sha256':'bce916fab66aab19718a127b26b3ac581e48f49e0dd0317a64cf1648a4e5b7cb','details_sha256':'504318141e100fd43f1021492c349a655953909b3213a083452d1230fa35cbc9','prior_full_native_MathML':7891,'prior_book_pages':272}
(O/'source-integration-v1.json').write_text(json.dumps(record,indent=2)+'\n');print(json.dumps(record))
