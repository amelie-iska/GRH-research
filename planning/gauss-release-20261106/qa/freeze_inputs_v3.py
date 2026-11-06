"""Freeze exact QA roles/input bytes after public-bundle map generation; no browser."""
from pathlib import Path
import argparse,json,hashlib,datetime
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[2]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
ap=argparse.ArgumentParser()
for n in ["bundle","freeze-receipt","expectations","native-map","pdf-map","output"]:ap.add_argument("--"+n,type=Path,required=True)
ap.add_argument("--inventory-sha256",required=True);a=ap.parse_args()
bundle=a.bundle.resolve();prep=bundle.parent/"release-preparation-v1";assert a.output.resolve()==prep/"QA_INPUT_FREEZE-v1.json" and not a.output.exists()
roles={"full_harness":HERE/"check_browser_v2.mjs","full_runner":HERE/"run_browser_v2.py","lab_module":HERE/"check_lab_v1.mjs","expectations":a.expectations.resolve(),"focused_harness":HERE/"check_gauss_tail_v2.mjs","focused_runner":HERE/"run_browser_v2.py","native_map":a.native_map.resolve(),"pdf_map":a.pdf_map.resolve(),"owned_browser":HERE/"owned_browser_v2.mjs"}
e=json.loads(a.expectations.read_text());n=json.loads(a.native_map.read_text());p=json.loads(a.pdf_map.read_text())
assert e["gtl"]==n and e["pdf_map"]==p,"Map/expectations projections must agree exactly"
assert not e["bundle_assets_pending"] and e["bundle"]["path"]==str(bundle) and e["bundle"]["inventory_sha256"]==a.inventory_sha256
assert e["bundle"]["freeze_receipt_sha256"]==sha(a.freeze_receipt)
for v in [n,p]:
 assert v["bundle_inventory_sha256"]==a.inventory_sha256
 for path,h in v["public_files"].items():assert sha(bundle/path)==h
files=set(roles.values())|{HERE/"make_expectations_v2.py",HERE/"freeze_inputs_v3.py",HERE/"prior-groups-v1.json",HERE/"expectations-template-v1.json"}
for rel,digest in e["binding_sources"].items():assert sha(ROOT/rel)==digest,rel
files|={ROOT/x for x in e["binding_sources"]}
for x in files:assert x.is_relative_to(ROOT) or x.is_relative_to(prep)
groups=json.loads((HERE/"prior-groups-v1.json").read_text())
out={"prepared":True,"schema":"gauss-tail-release-QA-input-freeze-v1","roles":{k:str(v) for k,v in roles.items()},"files_sha256":{str(x):sha(x) for x in sorted(files)},"bundle":{"root":str(bundle),"freeze_receipt_sha256":sha(a.freeze_receipt),"inventory_sha256":a.inventory_sha256},"focused_required_group_names":groups["focused_required_group_names"],"inherited_group_names":groups["inherited_group_names"],"prepared_utc":datetime.datetime.now(datetime.timezone.utc).isoformat(),"source_HTTP_fallback":False,"scope":"Full220 and focused40 share one owned public-prefix session and global timing. All maps use exact public adapter BUNDLE content; parent records are provenance, no HTTP fallback."}
a.output.open("x").write(json.dumps(out,indent=2,sort_keys=True)+"\n");print(str(a.output),sha(a.output))
