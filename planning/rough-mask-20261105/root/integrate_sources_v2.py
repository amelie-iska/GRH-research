from pathlib import Path
import json,hashlib
R=Path('/home/iska/Documents/LaTeX-projects/GRH-from-Mac-20261104')
O=R/'outputs/checks/2026-11-05-rough-mask/root/integration-v1'
A=R/'outputs/checks/2026-11-05-rough-mask/review/canonical-acceptance-v1.json'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
a=json.loads(A.read_text());assert a['passed'];assert not O.exists()
planned={};original={}
def edit(name,transform):
 p=R/name;before=p.read_bytes();original[name]=before;planned[name]=transform(before.decode()).encode()
for part in ['core','details']:
 source=R/('planning/rough-mask-20261105/canonical/rough-mask-'+part+'.tex');assert sha(source)==a['canonical_sha256'][str(source.relative_to(R))]
 for target,prefix in [('papers/rough-mask-'+part+'.tex',b''),('book/chapters/rough-mask-'+part+'.tex',b'% Generated shared reviewed material.\n')]:
  assert not(R/target).exists();planned[target]=prefix+source.read_bytes()
def weighted(s):
 needle='\\input{chapters/signed-divisor-details}';assert s.count(needle)==1
 return s.replace(needle,needle+'\n\\input{chapters/rough-mask-core}\n\\input{chapters/rough-mask-details}')
edit('book/chapters/weighted-cutoff.tex',weighted)
def assemble(s):
 needle="'signed-divisor-core','signed-divisor-details']";assert s.count(needle)==1
 return s.replace(needle,"'signed-divisor-core','signed-divisor-details','rough-mask-core','rough-mask-details']")
edit('scripts/assemble_book.py',assemble)
for name in ['resolutions-concise','resolutions-extended','validated-oracle-concise','validated-oracle-extended']:
 def wrapper(s,name=name):
  extended=name.endswith('extended');last='signed-divisor-details'if extended else'signed-divisor-core';needle='\\input{'+last+'}';assert s.count(needle)==1
  s=s.replace(needle,needle+'\n\\input{rough-mask-core}'+('\n\\input{rough-mask-details}'if extended else''))
  marker='The arithmetic positive determinant comparison remains open;'if name.startswith('resolutions')else'No proof of GRH or complete Lean formalization is asserted.';assert s.count(marker)==1
  return s.replace(marker,'An exact rough-prime support identity gives an explicit target-budget mask correction; the remaining coherent signed main term is still unestimated. '+marker)
 edit('papers/'+name+'.tex',wrapper)
# Validate ALL changes before writing any source. Preserve both production artifacts and source bytes.
for name,before in original.items():assert(R/name).read_bytes()==before,name
O.mkdir(parents=True)
for name in list(original)+['web/book/main.html','outputs/book/surface-orders-book.pdf']:
 p=R/name;b=O/'before'/name;b.parent.mkdir(parents=True,exist_ok=True);b.write_bytes(p.read_bytes())
for name,data in planned.items():(R/name).write_bytes(data)
r={'passed':True,'all_transformations_validated_before_any_mutation':True,'canonical_acceptance_sha256':sha(A),'canonical_sha256':a['canonical_sha256'],'changed_source_sha256':{n:sha(R/n)for n in planned},'before_MathML':8176,'before_book_pages':279,'scope':'Only independently accepted shared TeX/wrappers integrated before isolated builds. Production artifacts untouched; previous bytes preserved. No general assembler run.'}
(O/'source-integration-v1.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps({'passed':True,'sources':len(planned),'record':str(O/'source-integration-v1.json')}))
