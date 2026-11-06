"""Integrity closure for this run's new mathematical notes/reviews only.
Administrative hash/schema checks and saved Fraction guards are NOT a proof checker."""
from pathlib import Path
import hashlib,json,re,datetime
R=Path(__file__).resolve().parents[3]
O=R/"outputs/checks/2026-11-06-root-moment"
H=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
out=O/"root/proof-integrity-v1.json"
assert not out.exists()
gates=["review-root-b/acceptance-v1.json","review-root-c/acceptance-v1.json",
       "review-c-a/acceptance-v1.json","review-a-root/acceptance-v1.json",
       "review-b-diagnostic/acceptance-v2.json","review-c-large/acceptance-v1.json",
       "review-b-large/acceptance-v1.json","review-a-finite/acceptance-v1.json"]
bindings={};claims=0
def bind(path,sha):
 global claims
 p=Path(path)
 p=p if p.is_absolute() else R/p
 assert p.is_file(),str(p)
 assert H(p)==sha,str(p)
 name=str(p.relative_to(R)) if p.is_relative_to(R) else str(p)
 if name in bindings:assert bindings[name]==sha
 bindings[name]=sha;claims+=1
def walk(x):
 if isinstance(x,dict):
  if isinstance(x.get("path"),str) and isinstance(x.get("sha256"),str) and re.fullmatch("[a-f0-9]{64}",x["sha256"]):
   bind(x["path"],x["sha256"])
  for k,v in x.items():
   if "/" in k and isinstance(v,str) and re.fullmatch("[a-f0-9]{64}",v):bind(k,v)
   elif isinstance(v,(dict,list)):walk(v)
 elif isinstance(x,list):
  for z in x:walk(z)
for n in gates:
 p=O/n;j=json.loads(p.read_text());assert j["passed"],n
 bind(str(p.relative_to(R)),H(p));walk(j)
for p in O.rglob("*source-pins*.json"):
 bind(str(p.relative_to(R)),H(p));walk(json.loads(p.read_text()))
for n in ["root/reduction-budget-v1.json","root/short-divisor-budget-v1.json","root/large-short-divisor-budget-v1.json"]:
 p=O/n;j=json.loads(p.read_text());assert j["passed"]
 bind(str(p.relative_to(R)),H(p))
record={"passed":True,"kind":"STATIC_BINDING_AND_SAVED_NEW_ALGEBRAIC_GUARD_CLOSURE_NOT_MATHEMATICAL_PROOF_CHECKER",
"utc":datetime.datetime.now(datetime.timezone.utc).isoformat(),"gates":gates,"bindings":bindings,
"binding_assertions":claims,"distinct_bound_files":len(bindings),
"new_scoped_signed_tail_reviewed":True,"whole_signed_power":"13/12 unchanged",
"global_unsigned_power":"9/8 unchanged","GRH":False,"new_Lean":False,
"old_numeric_browser_build_or_publication_audits_rerun":False,
"producer_sha256":H(Path(__file__))}
out.open("x").write(json.dumps(record,indent=2)+"\n")
print(json.dumps({"passed":True,"gates":len(gates),"bound_files":len(bindings),
"assertions":claims,"sha256":H(out)}))
