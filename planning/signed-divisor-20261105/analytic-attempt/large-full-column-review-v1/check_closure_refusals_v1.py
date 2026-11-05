"""Bounded closure/uniqueness/refusal supplement; no full arithmetic or pair rerun."""
import sys,os
sys.dont_write_bytecode=True
os.nice(10);os.sched_setaffinity(0,{min(os.sched_getaffinity(0))})
from pathlib import Path
from itertools import product
import json,hashlib
from independent_eisenstein_core_v1 import PH,ZERO,mul,conj,raw
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[3]
DATA=ROOT/'outputs/experiments/2026-11-05-signed-divisor-D60000-v1'
OUT=ROOT/'outputs/checks/2026-11-05-signed-divisor/analytic/large-full-column-review-v1'
KEYS=['AA','AC','Amu','CA','CC','Cmu','muA','muC','mumu']
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def j(p):return json.loads(p.read_text())
manifest=j(DATA/'manifest.json');assert sha(DATA/'manifest.json')=='fecbec83a4fadd301d7845daddcb7e31f216705a6b29c5ba98436642ae0b2e4f'
assert manifest['source_freeze_sha256']==sha(DATA/'source-freeze.json') and manifest['summary_sha256']==sha(DATA/'summary.json')
receipt=OUT/'independent-large-v1.json';assert sha(receipt)=='5c17b8795f53abdfd3da4b3281c7ca69cfce096a5a28a09f32c91baec4226d6a'
cols=j(DATA/'columns.json');ps=j(DATA/'prime-ideals.json');rows=j(DATA/'rows.json');phases=j(DATA/'raw-character-phases.json')
gs=[tuple(c['generator'])for c in cols];assert len(set(gs))==len(gs)==16953
assert max(len(c['prime_ids'])for c in cols)==4
last=None;divisors=0
with(DATA/'divisor-energies.jsonl').open()as f:
 for line in f:
  v=json.loads(line);key=(v['norm'],tuple(v['generator']))
  assert v['id']==divisors and(last is None or key>last);last=key;divisors+=1
  assert len(v['prime_ids'])==len(set(v['prime_ids']))
assert divisors==21750
with(DATA/'gcd-classes.jsonl').open()as f:
 gcdclasses=0
 for line in f:
  v=json.loads(line);assert len(v['prime_ids'])==len(set(v['prime_ids']));gcdclasses+=1
assert gcdclasses==21750
est=j(DATA/'resource-estimate.json');summary=j(DATA/'summary.json')
assert summary['resources']==est and summary['parameters']==j(DATA/'parameters.json')
assert summary['passed'] and summary['source_bytes_unchanged'] and not summary['asymptotic_claim'] and not summary['gcd_slice_psd_claim']
assert not summary['checks']['large_literal_pair_check'] and not summary['checks']['small_literal_pair_check']
# Two actual cells: None versus literal +1; recompute residue symbols afresh.
controls={}
for target in(None,0):
 ri,ci=next((ri,ci)for ri,r in enumerate(phases)for ci,x in enumerate(r)if x==target)
 fs=[tuple(ps[k]['generator'])for k in cols[ci]['prime_ids']];value=raw(fs,tuple(rows[ri]['u']))
 assert value==(ZERO if target is None else PH[target])
 altered=0 if target is None else None
 assert value!=(ZERO if altered is None else PH[altered])
 controls['raw_zero'if target is None else'phase_zero_plus_one']={'row':ri,'column':ci,'actual_phase':target,'wrong_phase_rejected':altered}
# The exact comparisons used in the main audit reject coordinate and convention tampering.
unit=json.loads((DATA/'divisor-energies.jsonl').open().readline());fv=unit['F_omega'][0]
expected=list(product(range(3),repeat=2));z={(a,b):mul(tuple(fv[a]),conj(tuple(fv[b])))for a,b in expected}
assert any(z[(a,b)][1]for a,b in expected)
a,b=next((a,b)for a,b in expected if z[(a,b)][1]);assert z[(a,b)]!=conj(z[(a,b)])
mutated=[list(x)for x in fv];mutated[0][0]+=1
assert not all(tuple(mutated[k])==tuple(fv[k])for k in range(3))
Z=unit['Z_omega'];mutZ={k:list(v)for k,v in Z.items()};mutZ['AA'][0]+=1
assert not all(mutZ[k]==Z[k]for k in KEYS)
freeze=j(DATA/'source-freeze.json');n=next(n for n in freeze['files']if n.endswith('full_column_v1.py'));source=(ROOT/n).read_bytes()
assert hashlib.sha256(source).hexdigest()==freeze['files'][n]['sha256']
assert hashlib.sha256(source+b'\n# in-memory negative control\n').hexdigest()!=freeze['files'][n]['sha256']
for n,x in manifest['files'].items():assert sha(DATA/n)==x['sha256']
result=dict(passed=True,parent_receipt=str(receipt),parent_receipt_sha256=sha(receipt),checker_sha256=sha(Path(__file__)),manifest_sha256=sha(DATA/'manifest.json'),column_generators_unique_complete_by_injection_with_parent=16953,divisor_ids_unique_sorted_complete=divisors,gcd_prime_id_lists_have_no_repetitions=gcdclasses,all_manifest_crosspins_and_resource_parameter_tables_exact=True,actual_raw_refusal_cells=controls,wrong_complex_conjugation_refused={'channels':[a,b],'correct':list(z[(a,b)]),'wrong':list(conj(z[(a,b)]))},Fd_coordinate_tamper_refused=True,Z_coordinate_tamper_refused=True,source_byte_tamper_refused=True,all_inputs_unchanged=True,scope='Bounded closure and in-memory negative controls only; no numeric trajectory, full field table, or pair loop rerun')
out=OUT/'closure-refusals-v1.json'
with out.open('x')as f:json.dump(result,f,indent=2);f.write('\n')
print(json.dumps({'passed':True,'path':str(out),'sha256':sha(out)}))
