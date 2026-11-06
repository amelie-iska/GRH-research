"""Freeze reviewed public-bundle QA roles/maps. No browser or build."""
from pathlib import Path
import argparse,json,hashlib,datetime
from contract_v3 import validate,GROUPS
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[2];OWN=ROOT/"outputs/checks/2026-11-06-ramified-release/lane-a"
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
ap=argparse.ArgumentParser()
for n in ["bundle","freeze-receipt","expectations","native-map","ramified-native-map","pdf-map","output"]:ap.add_argument("--"+n,type=Path,required=True)
ap.add_argument("--inventory-sha256",required=True);a=ap.parse_args()
bundle=a.bundle.resolve();assert a.output.resolve().is_relative_to(OWN) and not a.output.exists()
roles={"full_harness":HERE/"check_browser_v2.mjs","full_runner":HERE/"run_browser_v4.py","lab_module":HERE/"check_lab_v1.mjs","expectations":a.expectations.resolve(),"focused_harness":HERE/"check_gauss_tail_v1.mjs","focused_runner":HERE/"run_browser_v4.py","ramified_harness":HERE/"check_ramified_v5.mjs","ramified_runner":HERE/"run_browser_v4.py","native_map":a.native_map.resolve(),"ramified_native_map":a.ramified_native_map.resolve(),"pdf_map":a.pdf_map.resolve(),"owned_browser":HERE/"owned_browser_v2.mjs"}
e=json.loads(a.expectations.read_text());n=json.loads(a.native_map.read_text());rg=json.loads(a.ramified_native_map.read_text());pdf=json.loads(a.pdf_map.read_text())
validate(e);assert e["gtl"]==n and e["rg"]==rg and e["pdf_map"]==pdf
assert not e["bundle_assets_pending"] and e["bundle"]["path"]==str(bundle) and e["bundle"]["inventory_sha256"]==a.inventory_sha256 and e["bundle"]["freeze_receipt_sha256"]==sha(a.freeze_receipt)
for m in [n,rg,pdf]:
 assert m["bundle_inventory_sha256"]==a.inventory_sha256
 for path,h in m["public_files"].items():assert sha(bundle/path)==h,path
files=set(roles.values())|{HERE/x for x in ["make_expectations_v4.py","freeze_inputs_v6.py","contract_v3.py","test_contract_v4.py","prior-groups-v3.json"]}
for rel,digest in e["binding_sources"].items():assert sha(ROOT/rel)==digest,rel
files|={ROOT/x for x in e["binding_sources"]}
assert all(x.is_relative_to(ROOT)for x in files)
record={"prepared":True,"schema":"ramified-release-QA-input-freeze-v1","roles":{k:str(v)for k,v in roles.items()},"files_sha256":{str(x):sha(x)for x in sorted(files)},"bundle":{"root":str(bundle),"freeze_receipt_sha256":sha(a.freeze_receipt),"inventory_sha256":a.inventory_sha256},"inherited_group_names":GROUPS["inherited_group_names"],"focused_required_group_names":GROUPS["focused_required_group_names"],"ramified_required_group_names":GROUPS["ramified_required_group_names"],"lab_required_group_names":GROUPS["lab_required_group_names"],"required_counts":GROUPS["required_counts"],"prepared_utc":datetime.datetime.now(datetime.timezone.utc).isoformat(),"source_HTTP_fallback":False,"scope":"Full220+Gauss40+ramified44+frozen lab58/54 in one owned session/global timing; exact PUBLIC bundle maps only."}
a.output.parent.mkdir(parents=True,exist_ok=True);a.output.open("x").write(json.dumps(record,indent=2,sort_keys=True)+"\n");print(str(a.output),sha(a.output))
