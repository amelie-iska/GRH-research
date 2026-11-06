"""Fresh fail-closed QA contract controls, synthetic only; no browser/science data rerun."""
from pathlib import Path
import argparse,copy,json,hashlib,re,datetime,subprocess
from contract_v3 import validate,validate_math_preservation,GROUPS,BUILDER,RUNTIME
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[2];OWN=ROOT/"outputs/checks/2026-11-06-ramified-release/lane-a"
ap=argparse.ArgumentParser();ap.add_argument("--output",type=Path,required=True);a=ap.parse_args();assert a.output.resolve().is_relative_to(OWN)and not a.output.exists()
e=json.loads((ROOT/"planning/gauss-release-20261106/qa/expectations-favicon-v2.json").read_text())
rg=json.loads((ROOT/"outputs/checks/2026-11-06-ramified-book/native/run-v1/native-build-record.json").read_text())
rg["labels"]=[x for suffix in ["core","figure","details"]for x in re.findall(r"\\label\{(rg:[^}]+)\}",(ROOT/"book/chapters"/("ramified-gauss-"+suffix+".tex")).read_text())]
oldrefs=e["bundle_svg_srcs"];assert len(oldrefs)==31
e.update(schema="ramified-release-expectations-v1",book_pages=348,math_nodes=10858,focused_pages=[85,243],notes_pages=[43,131],ramified_required_group_names=GROUPS["ramified_required_group_names"],lab_required_group_names=GROUPS["lab_required_group_names"],required_lab_layouts=54,required_saved_strings=1218,required_rendered_cells=3654,prior31_svg_srcs=oldrefs,bundle_svg_srcs=oldrefs+["figures/ramified-cusp-prefix.svg"],old10299_literal_math_sha256="a"*64,preserved_public_builder_sha256=BUILDER,source_HTTP_fallback=False)
rg["old_literal_math_sha256"]="a"*64;rg["prior31_svg_srcs"]=oldrefs;e["rg"]=rg;e["gtl"]["math_nodes"]=10858;e["gtl"]["svg_refs"]=32
for key,pages in zip(["/book.pdf","/concise.pdf","/extended.pdf","/validated-oracle-concise.pdf","/validated-oracle-extended.pdf"],[348,85,243,43,131]):e["pdfs"][key]["pages"]=pages
assert validate(e)
neg=[]
def reject(name,mutate):
 d=copy.deepcopy(e);mutate(d)
 try:validate(d)
 except (AssertionError,KeyError,TypeError):neg.append(name);return
 raise AssertionError("Negative control accepted: "+name)
for field in ["legacy_group_names","prior191_group_names","prior220_group_names","focused_required_group_names","ramified_required_group_names","lab_required_group_names"]:
 for i in range(len(e[field])):reject(field+"-drop-"+str(i),lambda d,f=field,i=i:d[f].pop(i))
for i in range(31):reject("old31-SVG-drop-"+str(i),lambda d,i=i:d["prior31_svg_srcs"].pop(i))
for i in range(75):reject("ramified75-label-drop-"+str(i),lambda d,i=i:d["rg"]["labels"].pop(i))
for field,value in [("book_pages",333),("math_nodes",10857),("tables",388),("frames",13),("focused_pages",[81,228]),("notes_pages",[39,118]),("required_lab_layouts",53),("required_saved_strings",1217),("required_rendered_cells",3653),("source_HTTP_fallback",True),("preserved_public_builder_sha256","0"*64)]:
 reject(field+"-wrong",lambda d,f=field,v=value:d.__setitem__(f,v))
for field,value in [("quiet_ms",749),("idle_timeout_ms",30001),("new_fetch_filters",True),("initial_separate_from_departures",False)]:
 reject("WS-"+field+"-weakened",lambda d,f=field,v=value:d["global_WS"].__setitem__(f,v))
reject("runtime-icon-adapter-wrong",lambda d:d["assets"].__setitem__("/public-base.js","0"*64))
for field,value in [("old_math_byte_identical",False),("old_HTML_restored_exactly",False),("math_nodes_added",558),("old_svg_refs",30)]:
 reject("ramified-"+field+"-wrong",lambda d,f=field,v=value:d["rg"].__setitem__(f,v))
# Literal-source preservation controls use clearly synthetic numbered MathML.
prior="\n".join("<math><mn>"+str(i)+"</mn></math>"for i in range(10299));nodes=prior.splitlines();current="\n".join(nodes[:10288])+'<section class="new-reviewed-chapters" id="ramified-gauss-section">'+"\n".join("<math><mn>new"+str(i)+"</mn></math>"for i in range(559))+'</section>'+"\n".join(nodes[10288:])
validate_math_preservation(prior,current)
for name,bad in [("changed-old-bibliography-node",current.replace("<mn>10298</mn>","<mn>changedtail</mn>",1)),("changed-old-node",current.replace("<mn>17</mn>","<mn>170</mn>",1)),("lost-old-node",current.replace("<math><mn>17</mn></math>","",1)),("reordered-old-prefix",current.replace("<mn>0</mn>","<mn>TEMP</mn>",1).replace("<mn>1</mn>","<mn>0</mn>",1).replace("<mn>TEMP</mn>","<mn>1</mn>",1))]:
 try:validate_math_preservation(prior,bad)
 except AssertionError:neg.append(name)
 else:raise AssertionError("Literal MathML negative accepted")
# Browser protocol helpers and strict error/quiet/departure/cleanup code are exactly inherited.
old=ROOT/"planning/gauss-release-20261106/qa";m=(HERE/"check_browser_v2.mjs").read_text();base=(old/"check_browser_v3.mjs").read_text()
for x in ["owned_browser_v2.mjs","check_lab_v1.mjs"]:assert (HERE/x).read_bytes()==(old/x).read_bytes()
for left,right in [("const collectedErrors=","const check="),(" const errors=","report.bound_expectations=")]:
 exact=base[base.index(left):base.index(right,base.index(left))];assert exact in m
 for wrong in [exact.replace(">=750",">=749"),exact.replace("network.fetchError","network.fetchIGNORED")]:
  if wrong!=exact:assert wrong not in m
assert base[base.index("}catch(error){"):] in m
for name in ["check_browser_v2.mjs","check_gauss_tail_v1.mjs","check_ramified_v5.mjs","check_lab_v1.mjs","owned_browser_v2.mjs"]:subprocess.run(["node","--check",str(HERE/name)],check=True,capture_output=True)
record={"passed":True,"schema":"ramified-release-guard-negative-controls-v1","positive_synthetic_contract":True,"negative_controls_rejected":len(neg),"negative_names":neg,"strict_helpers_and_error_idle_departure_cleanup_byte_identical":True,"node_syntax":True,"science_or_training_or_browser_run":False,"scope":"Synthetic pre-execution QA guard controls only; no bundle approval or actual-family data.","created_at_utc":datetime.datetime.now(datetime.timezone.utc).isoformat()}
a.output.parent.mkdir(parents=True,exist_ok=True);a.output.open("x").write(json.dumps(record,indent=2)+"\n");print(json.dumps({"passed":True,"rejected":len(neg),"path":str(a.output),"sha256":hashlib.sha256(a.output.read_bytes()).hexdigest()}))
