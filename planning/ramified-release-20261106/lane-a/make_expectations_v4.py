"""Map a reviewed frozen public bundle to inherited+ramified QA inputs; no browser/build."""
from pathlib import Path
from html.parser import HTMLParser
import argparse,json,hashlib,datetime,re
from contract_v3 import validate,validate_math_preservation,BUILDER,RUNTIME,GROUPS
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[2];OWN=ROOT/"outputs/checks/2026-11-06-ramified-release/lane-a"
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
ap=argparse.ArgumentParser()
for n in ["bundle","freeze-receipt","output-dir"]:ap.add_argument("--"+n,type=Path,required=True)
ap.add_argument("--inventory-sha256",required=True);a=ap.parse_args()
bundle=a.bundle.resolve();out=a.output_dir.resolve()
assert bundle.is_dir() and not bundle.is_relative_to(ROOT) and bundle.name=="site-bundle-v1" and "/outputs/publication/"in str(bundle)
assert out.is_relative_to(OWN) and not out.exists()
entries=list(bundle.rglob("*"));assert not any(x.is_symlink() for x in entries)
rows=[dict(path=f.relative_to(bundle).as_posix(),bytes=f.stat().st_size,sha256=sha(f)) for f in sorted(entries) if f.is_file()]
raw=(json.dumps(rows,separators=(",",":"),sort_keys=True)+"\n").encode();assert hashlib.sha256(raw).hexdigest()==a.inventory_sha256
prior_bundle=Path("/home/iska/Documents/LaTeX-projects/GRH-publication-20261106-gauss-favicon/outputs/publication/20261106-gauss-favicon/site-bundle-v1")
oldqa=ROOT/"planning/gauss-release-20261106/qa";e=json.loads((oldqa/"expectations-favicon-v2.json").read_text())
assert sha(ROOT/"scripts/build_public_site.py")==BUILDER
assert sha(bundle/"public-base.js")==sha(prior_bundle/"public-base.js")==RUNTIME
nr=ROOT/"outputs/checks/2026-11-06-ramified-book/native/run-v1/native-build-record.json"
ag=ROOT/"outputs/checks/2026-11-06-ramified-book/lane-b/build-aggregate-v1/aggregate-v1.json"
milestone=ROOT/"outputs/checks/2026-11-06-ramified-book/root/MILESTONE_ACCEPTED-v1.json"
native=json.loads(nr.read_text());agg=json.loads(ag.read_text())
assert sha(nr)=="7f6b8ba69696207d85f3fb38deb6ef2197fd701f9b38decd215e70873a22aa44" and agg["passed"] and native["passed"]
assert sha(ag)=="763e2edbfa1207470752fb0dcd478d7f22aaf20c6916d707b89f56aabe3b834c"
assert sha(ROOT/"web/book/main.html")==native["new_HTML_sha256"]
for file,source_digest in native["source_sha256"].items():assert sha(ROOT/file)==source_digest,file
oldmath=validate_math_preservation((prior_bundle/"book/main.html").read_text(),(bundle/"book/main.html").read_text())
class Tags(HTMLParser):
 def __init__(self):super().__init__();self.frames=[];self.svgs=[]
 def handle_starttag(self,tag,attrs):
  d=dict(attrs)
  if tag=="iframe":self.frames.append(d["src"])
  if tag=="img"and d.get("src","").endswith(".svg"):self.svgs.append(d["src"])
prev=Tags();prev.feed((prior_bundle/"book/main.html").read_text());tags=Tags();tags.feed((bundle/"book/main.html").read_text())
assert len(prev.svgs)==31 and tags.svgs[:31]==prev.svgs and len(tags.svgs)==32 and tags.frames==prev.frames and len(tags.frames)==14
def native_map(prefix,fig,data):
 data=json.loads(json.dumps(data))
 files=["book/main.html"]+["book/sources/"+prefix+"-"+x+".tex" for x in ["core","figure","details"]]+["book/figures/"+fig+"."+x for x in ["svg","tex","pdf"]]
 for p in files[1:]:assert sha(bundle/p)==sha(ROOT/"web"/p),p
 data.update(schema="ramified-release-public-native-map-v1",bundle_inventory_sha256=a.inventory_sha256,public_files={p:sha(bundle/p) for p in files},raw_source_HTML_sha256=native["new_HTML_sha256"],new_HTML_sha256=sha(bundle/"book/main.html"),current_full_native_record={"path":str(nr),"sha256":sha(nr)},math_nodes=10858,svg_refs=32,PDF_build_record_sha256=native["PDF_build_record_sha256"])
 data["source_sha256"]={**data["source_sha256"],**{p:h for p,h in native["source_sha256"].items()if p in data["source_sha256"]},**{"book/chapters/"+Path(p).name:sha(bundle/p) for p in files if "/sources/"in p},**{"book/figures/"+Path(p).name:sha(bundle/p) for p in files if "/figures/"in p}}
 return data
gtl=native_map("gauss-tail","gauss-tail-partition",e["gtl"])
rg=native_map("ramified-gauss","ramified-cusp-prefix",native)
sourcefiles=[ROOT/"book/chapters"/("ramified-gauss-"+x+".tex")for x in ["core","figure","details"]]
rg["labels"]=[x for p in sourcefiles for x in re.findall(r"\\label\{(rg:[^}]+)\}",p.read_text())]
rg["old_literal_math_sha256"]=oldmath;rg["prior31_svg_srcs"]=prev.svgs
# The current PDF auxiliary must retain every inherited Gauss label value.
aux=ROOT/"outputs/checks/2026-11-06-ramified-book/builds/run-v1/book-pdf/main.aux"
assert sha(aux)==native["pdf_aux_sha256"]
for name,value in gtl["equations"].items():assert re.search(r"\\newlabel\{"+re.escape(name)+r"\}\{\{"+re.escape(value)+r"\}",aux.read_text()),name
pdf_map={"schema":"ramified-release-public-PDF-map-v1","bundle_inventory_sha256":a.inventory_sha256,"public_files":{},"pages":{},"parent_aggregate":{"path":str(ag),"sha256":sha(ag)}}
names={"book.pdf":"book-pdf","concise.pdf":"focused-concise","extended.pdf":"focused-extended","validated-oracle-concise.pdf":"notes-concise","validated-oracle-extended.pdf":"notes-extended"};e["pdfs"]={}
for name,role in names.items():
 item=agg["results"][role];src=ROOT/item["PDF"]["path"]
 assert sha(bundle/name)==sha(src)==item["PDF"]["sha256"]
 pdf_map["public_files"][name]=sha(bundle/name);pdf_map["pages"][name]=item["pages"]
 e["pdfs"]["/"+name]={"sha256":sha(bundle/name),"bytes":(bundle/name).stat().st_size,"pages":item["pages"],"production_path":item["PDF"]["path"]}
for path,v in e["cbk_downloads"].items():assert sha(bundle/path.lstrip("/"))==v["sha256"]
assert sha(bundle/"data/coherent-band-schur-v1.json")==e["lab"]["payload_sha256"]
native_paths=set(gtl["public_files"])|set(rg["public_files"])
assets=set(e["assets"])|set(e["pdfs"])|set(e["cbk_downloads"])|{"/"+p for p in native_paths}|{"/public-base.js"}
e["assets"]={p:sha(bundle/p.lstrip("/"))for p in sorted(assets)}
e.update(schema="ramified-release-expectations-v1",book_pages=348,math_nodes=10858,focused_pages=[85,243],notes_pages=[43,131],bundle_assets_pending=False,gtl=gtl,rg=rg,pdf_map=pdf_map,bundle_iframe_srcs=tags.frames,bundle_svg_srcs=tags.svgs,prior31_svg_srcs=prev.svgs,old10299_literal_math_sha256=oldmath,preserved_public_builder_sha256=BUILDER,source_HTTP_fallback=False,required_lab_layouts=54,required_saved_strings=1218,required_rendered_cells=3654,ramified_required_group_names=GROUPS["ramified_required_group_names"],lab_required_group_names=GROUPS["lab_required_group_names"],bundle={"path":str(bundle),"files":len(rows),"bytes":sum(x["bytes"]for x in rows),"inventory_sha256":a.inventory_sha256,"freeze_receipt_path":str(a.freeze_receipt.resolve()),"freeze_receipt_sha256":sha(a.freeze_receipt)},prepared_utc=datetime.datetime.now(datetime.timezone.utc).isoformat())
e["binding_sources"]={**e["binding_sources"],str(nr.relative_to(ROOT)):sha(nr),str(ag.relative_to(ROOT)):sha(ag),str(milestone.relative_to(ROOT)):sha(milestone)}
publicfiles={**gtl["public_files"],**rg["public_files"],**pdf_map["public_files"]}
e["changed_tested_files"]={p:h for p,h in publicfiles.items()if not(prior_bundle/p).exists()or sha(prior_bundle/p)!=h}
e["unchanged_tested_files"]={p:h for p,h in publicfiles.items()if p not in e["changed_tested_files"]}
validate(e);out.mkdir(parents=True)
for name,value in [("expectations-v1.json",e),("native-map-gauss-v1.json",gtl),("native-map-ramified-v1.json",rg),("pdf-map-v1.json",pdf_map)]:
 p=out/name;p.open("x").write(json.dumps(value,indent=2,sort_keys=True)+"\n");print(str(p),sha(p))
