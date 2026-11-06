from pathlib import Path
import hashlib,json,re
R=Path('/home/iska/Documents/LaTeX-projects/GRH-from-Mac-20261104')
O=R/'outputs/checks/2026-11-05-physical-sieve/canonical/layout-cmr-v1'
G=R/'outputs/checks/2026-11-05-physical-sieve/review/canonical-acceptance-v2.json'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
g=json.loads(G.read_text());assert g['passed'];assert sha(G)=='6c741ff8f9844fc89b0fa23fd17196fcb842c835b42382dafc210cf4bd1667c2';assert not O.exists()
C='planning/physical-sieve-20261105/canonical/coherent-main-details.tex'
assert sha(R/C)==g['canonical_sha256'][C]=='20098c4210a24b0893662fe0020c6c8daf204f154bb071118f2ff207a63ac94e'
names=[C,'papers/coherent-main-details.tex','book/chapters/coherent-main-details.tex']
original={n:(R/n).read_bytes() for n in names}
assert original[names[1]]==original[C]
assert original[names[2]]==b'% Generated shared reviewed material.\n'+original[C]
old=rb'&\hspace{8mm}=';new=rb'&='
assert all(data.count(old)==1 for data in original.values())
planned={n:data.replace(old,new) for n,data in original.items()}
for n in names:
 assert (R/n).read_bytes()==original[n]
 for pattern in (rb'\\label\{([^}]+)\}',rb'\\(?:eqref|ref)\{([^}]+)\}'):
  assert re.findall(pattern,original[n])==re.findall(pattern,planned[n])
O.mkdir(parents=True)
for n,data in original.items():
 p=O/'before'/n;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(data)
for n,data in planned.items():(R/n).write_bytes(data)
r={'passed':True,'scope':'Root-authorized native-portability spacing-only correction after B confirmed all4PDF v1 jobs complete; no process/build in flight','source_producer_sha256':sha(__file__),'prior_canonical_gate':{'path':str(G.relative_to(R)),'sha256':sha(G)},'targets':names,'before_sha256':{n:hashlib.sha256(data).hexdigest() for n,data in original.items()},'after_sha256':{n:sha(R/n) for n in names},'exact_replacement':{'old':old.decode(),'new':new.decode(),'occurrences_per_target':1},'all_originals_preserved_before_any_mutation':True,'all_labels_refs_and_mathematical_operands_unchanged':True,'font_sizes_and_general_renderer_unchanged':True,'independent_gate_v3_required':True,'old_PDF_and_native_failures_preserved_by_build_owners':True}
p=O/'layout-amendment-v1.json';p.write_text(json.dumps(r,indent=2,sort_keys=True)+'\n');print(json.dumps({'record':str(p.relative_to(R)),'sha256':sha(p),'canonical_details_sha256':sha(R/C),'paper_sha256':sha(R/names[1]),'book_sha256':sha(R/names[2])},sort_keys=True))
