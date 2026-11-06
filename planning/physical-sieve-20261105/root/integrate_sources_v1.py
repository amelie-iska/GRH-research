from pathlib import Path
import json,hashlib
R=Path('/home/iska/Documents/LaTeX-projects/GRH-from-Mac-20261104')
O=R/'outputs/checks/2026-11-05-physical-sieve/root/integration-v1'
A=R/'outputs/checks/2026-11-05-physical-sieve/review/canonical-acceptance-v1.json'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
a=json.loads(A.read_text());assert a['passed'];assert not O.exists()
planned={};original={}
def edit(name,transform):
 p=R/name;before=p.read_bytes();original[name]=before;planned[name]=transform(before.decode()).encode()
names=[n+'-'+part for n in ['coherent-main','physical-sieve']for part in ['core','details']]
for name in names:
 source=R/('planning/physical-sieve-20261105/canonical/'+name+'.tex');assert sha(source)==a['canonical_sha256'][str(source.relative_to(R))]
 for target,prefix in [('papers/'+name+'.tex',b''),('book/chapters/'+name+'.tex',b'% Generated shared reviewed material.\n')]:
  assert not(R/target).exists();planned[target]=prefix+source.read_bytes()
def weighted(s):
 needle='\\input{chapters/rough-mask-details}';assert s.count(needle)==1
 return s.replace(needle,needle+'\n'+'\n'.join('\\input{chapters/'+n+'}'for n in names))
edit('book/chapters/weighted-cutoff.tex',weighted)
def assemble(s):
 needle="'rough-mask-core','rough-mask-details']";assert s.count(needle)==1
 return s.replace(needle,"'rough-mask-core','rough-mask-details',"+','.join(repr(n)for n in names)+"]")
edit('scripts/assemble_book.py',assemble)
for name in ['resolutions-concise','resolutions-extended','validated-oracle-concise','validated-oracle-extended']:
 def wrapper(s,name=name):
  extended=name.endswith('extended');last='rough-mask-details'if extended else'rough-mask-core';needle='\\input{'+last+'}';assert s.count(needle)==1
  inc=names if extended else[n for n in names if n.endswith('core')]
  s=s.replace(needle,needle+'\n'+'\n'.join('\\input{'+n+'}'for n in inc))
  old='retaining the unresolved $7/6$ power.';assert s.count(old)==1
  s=s.replace(old,'with the former $7/6$ comparison retained as history.')
  marker='The arithmetic positive determinant comparison remains open;'if name.startswith('resolutions')else'No proof of GRH or complete Lean formalization is asserted.';assert s.count(marker)==1
  return s.replace(marker,"A pinned fixed-order preprint theorem, applied to the physical sixth-power-free radicands, improves the global unsigned critical power to $9/8$ and the $A_6=1$ signed slice to $13/12$. Mean-retaining coherent reductions and conditional scalar-input diagnostics keep the fixed-profile signed target open. "+marker)
 edit('papers/'+name+'.tex',wrapper)
for name,before in original.items():assert(R/name).read_bytes()==before,name
O.mkdir(parents=True)
for name in list(original)+['web/book/main.html','outputs/book/surface-orders-book.pdf']:
 p=R/name;b=O/'before'/name;b.parent.mkdir(parents=True,exist_ok=True);b.write_bytes(p.read_bytes())
for name,data in planned.items():(R/name).write_bytes(data)
r={'passed':True,'all_transformations_validated_before_any_mutation':True,'canonical_acceptance_sha256':sha(A),'canonical_sha256':a['canonical_sha256'],'changed_source_sha256':{n:sha(R/n)for n in planned},'before_MathML':8552,'before_book_pages':288,'scope':'Only independently accepted shared TeX/wrappers integrated before isolated builds. Production artifacts untouched; previous bytes preserved. No general assembler run.'}
(O/'source-integration-v1.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps({'passed':True,'sources':len(planned),'record':str(O/'source-integration-v1.json')}))
