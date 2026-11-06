"""Generate public-adapter bundle expectations and native/PDF maps; no browser/build."""
from pathlib import Path
from html.parser import HTMLParser
import argparse,json,hashlib,datetime
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[2]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
ap=argparse.ArgumentParser()
for n in ["bundle","freeze-receipt","output","native-map","pdf-map"]:ap.add_argument("--"+n,type=Path,required=True)
ap.add_argument("--inventory-sha256",required=True);a=ap.parse_args()
bundle=a.bundle.resolve();assert bundle.is_dir() and not bundle.is_relative_to(ROOT) and bundle.name.startswith("site-bundle-") and "/outputs/publication/" in str(bundle)
entries=list(bundle.rglob("*"));assert not any(x.is_symlink() for x in entries)
rows=[dict(path=f.relative_to(bundle).as_posix(),bytes=f.stat().st_size,sha256=sha(f)) for f in sorted(entries) if f.is_file()]
raw=(json.dumps(rows,separators=(",",":"),sort_keys=True)+"\n").encode();assert hashlib.sha256(raw).hexdigest()==a.inventory_sha256
e=json.loads((HERE/"expectations-template-v1.json").read_text());assert e["bundle_assets_pending"] and e["schema"]=="gauss-tail-release-expectations-v1"
nr=ROOT/"outputs/checks/2026-11-06-gauss-book/native/run-v3/native-build-record.json";native=json.loads(nr.read_text())
ag=ROOT/"outputs/checks/2026-11-06-gauss-book/builds/run-v3/aggregate.json";agg=json.loads(ag.read_text())
assert e["gtl"]["accepted_raw_native_record_sha256"]==sha(nr),"Template must refer to this exact accepted native record"
assert agg["passed"] and sha(Path(agg["results"]["book-pdf"]["record"]))==native["PDF_build_record_sha256"]
assert native["passed"] and native["math_nodes"]==10299 and native["canonical_labs"]==14 and native["svg_refs"]==31
assert sha(ROOT/"web/book/main.html")==native["new_HTML_sha256"]
native_paths=["book/main.html","book/sources/gauss-tail-core.tex","book/sources/gauss-tail-details.tex","book/sources/gauss-tail-figure.tex","book/figures/gauss-tail-partition.tex","book/figures/gauss-tail-partition.svg","book/figures/gauss-tail-partition.pdf"]
native_map=e["gtl"];native_map.update(schema="gauss-tail-public-native-map-v1",bundle_inventory_sha256=a.inventory_sha256,public_files={p:sha(bundle/p) for p in native_paths},raw_source_HTML_sha256=native["new_HTML_sha256"],new_HTML_sha256=sha(bundle/"book/main.html"),parent_record={"path":str(nr),"sha256":sha(nr)})
for p in native_paths[1:]:assert sha(bundle/p)==sha(ROOT/"web"/p),p
native_map["source_sha256"]={**native_map["source_sha256"],**{"book/chapters/"+Path(p).name:sha(bundle/p) for p in native_paths if "/sources/" in p},**{"book/figures/"+Path(p).name:sha(bundle/p) for p in native_paths if "/figures/" in p}}
pdf_targets={"book.pdf":("outputs/book/surface-orders-book.pdf",333),"concise.pdf":("outputs/papers/resolutions-concise.pdf",81),"extended.pdf":("outputs/papers/resolutions-extended.pdf",228),"validated-oracle-concise.pdf":("outputs/papers/validated-oracle-20261104/validated-oracle-concise.pdf",39),"validated-oracle-extended.pdf":("outputs/papers/validated-oracle-20261104/validated-oracle-extended.pdf",118)}
pdf_map={"schema":"gauss-tail-public-PDF-map-v1","bundle_inventory_sha256":a.inventory_sha256,"public_files":{},"pages":{},"parent_aggregate":{"path":str(ag),"sha256":sha(ag)}}
e["pdfs"]={}
for name,(src,pages) in pdf_targets.items():
 assert sha(bundle/name)==sha(ROOT/src),name
 pdf_map["public_files"][name]=sha(bundle/name);pdf_map["pages"][name]=pages
 e["pdfs"]["/"+name]={"sha256":sha(bundle/name),"bytes":(bundle/name).stat().st_size,"pages":pages,"production_path":src}
class Tags(HTMLParser):
 def __init__(self):super().__init__();self.frames=[];self.svgs=[]
 def handle_starttag(self,tag,attrs):
  d=dict(attrs)
  if tag=="iframe":self.frames.append(d["src"])
  if tag=="img" and d.get("src","").endswith(".svg"):self.svgs.append(d["src"])
tags=Tags();tags.feed((bundle/"book/main.html").read_text())
assert len(tags.frames)==14 and tags.frames==e["prior_bundle_iframe_srcs"]
assert len(tags.svgs)==31 and tags.svgs[:30]==e["prior_bundle_svg_srcs"]
e["bundle_iframe_srcs"]=tags.frames;e["bundle_svg_srcs"]=tags.svgs
for path,v in e["cbk_downloads"].items():assert sha(bundle/path.lstrip("/"))==v["sha256"]
assert sha(bundle/"data/coherent-band-schur-v1.json")==e["lab"]["payload_sha256"]
assets=set(e["assets"])|set(e["pdfs"])|set(e["cbk_downloads"])|{"/"+p for p in native_paths}|{"/public-base.js"}
e["assets"]={p:sha(bundle/p.lstrip("/")) for p in sorted(assets)}
e.update(bundle_assets_pending=False,gtl=native_map,pdf_map=pdf_map,bundle={"path":str(bundle),"files":len(rows),"bytes":sum(x["bytes"] for x in rows),"inventory_sha256":a.inventory_sha256,"freeze_receipt_path":str(a.freeze_receipt.resolve()),"freeze_receipt_sha256":sha(a.freeze_receipt)},prepared_utc=datetime.datetime.now(datetime.timezone.utc).isoformat())
e["binding_sources"]={str(nr.relative_to(ROOT)):sha(nr),str(ag.relative_to(ROOT)):sha(ag),"outputs/checks/2026-11-06-gauss-book/MILESTONE_ACCEPTED-v1.json":sha(ROOT/"outputs/checks/2026-11-06-gauss-book/MILESTONE_ACCEPTED-v1.json")}
for p,value in [(a.output,e),(a.native_map,native_map),(a.pdf_map,pdf_map)]:
 assert p.resolve().parent==HERE and not p.exists(),"New SOURCE QA output only"
for p,value in [(a.output,e),(a.native_map,native_map),(a.pdf_map,pdf_map)]:p.open("x").write(json.dumps(value,indent=2,sort_keys=True)+"\n");print(str(p),sha(p))
