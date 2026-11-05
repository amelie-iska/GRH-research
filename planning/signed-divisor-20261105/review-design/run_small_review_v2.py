from pathlib import Path
import sys,json,hashlib,time
sys.dont_write_bytecode=True
from independent_small_family_v1 import *
R=Path(__file__).resolve().parents[3];O=R/'outputs/checks/2026-11-05-signed-divisor/review-design';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
keys=[['AA','AC','Amu'],['CA','CC','Cmu'],['muA','muC','mumu']]
def pairs_matrix(q):return[[tuple(q[keys[i][j]])for j in range(3)]for i in range(3)]
results=[{'D': 144, 'columns': 41, 'divisors': 53, 'rows': 5, 'all9_direct_h1_numerators': [[[-76, 0], [-50, 0], [26, 0]], [[-50, 0], [-8, 0], [42, 0]], [[26, 0], [42, 0], [16, 0]]], 'ordered_pair_incidence_checks': 1681, 'raw_values': 205, 'F_values': 795, 'Z_values': 477, 'output': 'outputs/checks/2026-11-05-signed-divisor/review-design/independent-D144-v1.json', 'sha256': '3024ff4d3480e640d566cee21ff025acd24d046b783e4401bd2c106f2ea61adb', 'preserved_completed_v1_case': True}];start=time.monotonic()
for D,U,H,A1,mhash in [(576,24,117,37,'ea68ea46eec092da39e3e6d282152f69e6c944cb6a15ae1e1efac439ef4a8675')]:
 base=R/f'outputs/experiments/2026-11-05-signed-divisor-D{D}-v1';assert sha(base/'manifest.json')==mhash;manifest=json.loads((base/'manifest.json').read_text());assert manifest['passed'];
 for name,meta in manifest['files'].items():p=base/name;assert p.stat().st_size==meta['bytes']and sha(p)==meta['sha256'],name
 pars=json.loads((base/'parameters.json').read_text());assert(pars['D'],pars['U'],pars['H'],pars['A1'],pars['A2'])==(D,U,H,A1,1);assert pars['profile']['fixed_once']and pars['profile']['delta']=='1/240000'and pars['nu']=='principal1'
 t=time.monotonic();own=reconstruct(D,U,H,A1);cols=own['columns'];authorcols=json.loads((base/'columns.json').read_text());authorrows=json.loads((base/'rows.json').read_text());primes=json.loads((base/'prime-ideals.json').read_text());byid={p['id']:tuple(p['generator'])for p in primes};assert len(byid)==len(primes)==len(set(byid.values()))
 for pi in primes:
  g=tuple(pi['generator']);n=norm(g);p=pi['rational_prime'];assert prime(p)and n==pi['norm']and g[0]%3==1 and g[1]%3==0
  if pi['kind']=='inert':assert p%3==2 and n==p*p and g[1]==0
  else:assert p%3==1 and n==p and pi['kind']=='split'
 assert len(cols)==len(authorcols)and len(own['rows'])==len(authorrows)
 amap={tuple(c['generator']):c for c in authorcols};index={tuple(c['generator']):i for i,c in enumerate(authorcols)};rowindex={tuple(u['u']):i for i,u in enumerate(authorrows)}
 for c in cols:
  a=amap[c['g']];assert norm(c['g'])==a['norm']and c['x']==(a['A'],a['C'],a['mu'])and a['W']==1 and a['nu_omega']==[1,0];assert set(c['fs'])=={byid[i]for i in a['prime_ids']}
 assert set(own['rows'])==set(rowindex)
 allideals=dict(ideal_universe(2*D))
 for ar in authorrows:
  u=tuple(ar['u']);assert u==tuple(ar['v1'])and ar['v2']==[1,0]and norm(u)==ar['N']<=H and ar['literal_unit']==[1,0];fs=allideals[u];assert fs and len(fs)==len(set(fs))and set(fs)=={byid[i]for i in ar['v1_prime_ids']}
 rawphases=json.loads((base/'raw-character-phases.json').read_text());rawcount=maskchecks=0
 for oi,u in enumerate(own['rows']):
  for ci,c in enumerate(cols):
   e=rawphases[rowindex[u]][index[c['g']]];expected=ZERO if e is None else PH[e];assert own['raw_character_values'][oi][ci]==expected;rawcount+=1
   for pi in c['fs']:assert(local_phase(pi,u)is None)==(quotient(u,pi)is not None);maskchecks+=1
 divauthor={tuple(d['generator']):d for d in map(json.loads,(base/'divisor-energies.jsonl').read_text().splitlines())};assert len(divauthor)==len(own['divisors']);fdmaps=[{tuple(d['d']):d['values']for d in row['F']}for row in own['per_row_checks']]
 fdchecks=zchecks=0
 for d in own['divisors']:
  a=divauthor[d['g']];fsid=[byid[i]for i in a['prime_ids']];productgen=(1,0)
  for pi in fsid:productgen=mul(productgen,pi)
  assert productgen==d['g'] and len(fsid)==len(set(fsid))and a['mu']==(-1)**len(fsid)
  assert a['mu']==d['mu']and a['norm']==norm(d['g'])and pairs_matrix(a['Z_omega'])==d['Z'];zchecks+=9
  for ri,u in enumerate(own['rows']):
   assert [tuple(v)for v in a['F_omega'][rowindex[u]]]==fdmaps[ri][d['g']];fdchecks+=3
  incident=[i for i,c in enumerate(cols)if quotient(c['g'],d['g'])is not None];assert a['incident_columns']==len(incident)
  for ri,u in enumerate(own['rows']):
   assert a['row_raw_d_masks'][rowindex[u]]==(quotient(u,d['g'])is None if prime(norm(d['g']))else not any(quotient(u,byid[p])is not None for p in a['prime_ids']))
   assert a['row_allowed_active_column_counts'][rowindex[u]]==sum(own['raw_character_values'][ri][ci]!=ZERO for ci in incident)
 authorclasses={frozenset(byid[p]for p in g['prime_ids']):g for g in map(json.loads,(base/'gcd-classes.jsonl').read_text().splitlines())};assert set(authorclasses)=={frozenset(byid[i]for i in d['prime_ids'])for d in divauthor.values()}
 observed={frozenset(tuple(x)for x in d['prime_generators'])for d in own['gcd_classes']}
 for fs in set(authorclasses)-observed:
  a=authorclasses[fs];assert a['ordered_column_pair_count']==0 and all(tuple(v)==ZERO for v in a['contribution_omega'].values())
 for g in own['gcd_classes']:
  a=authorclasses[frozenset(tuple(x)for x in g['prime_generators'])];assert a['ordered_column_pair_count']==g['ordered_pair_count']and pairs_matrix(a['contribution_omega'])==g['contribution']
 authrow=json.loads((base/'row-identities.json').read_text())['rows']
 for rr in own['per_row_checks']:assert pairs_matrix(authrow[rowindex[rr['u']]]['coprime_h1_numerator_omega'])==rr['direct_pair']
 ledger=list(map(json.loads,(base/'norm-ledger.jsonl').read_text().splitlines()));assert[n['norm']for n in ledger]==list(range(D,2*D+1))
 for n in ledger:assert n['multiplicity']==sum(norm(c['g'])==n['norm']for c in cols)
 summary=json.loads((base/'summary.json').read_text());assert summary['counts']['columns']==len(cols)and summary['counts']['divisors']==len(own['divisors'])and summary['counts']['rows']==len(own['rows'])
 for i in range(3):
  for j in range(3):assert tuple(summary['divisor_budget'][keys[i][j]]['signed_numerator_omega'])==own['direct_pair'][i][j]
 for name,meta in manifest['files'].items():assert sha(base/name)==meta['sha256'],name
 own.update({'passed':True,'author_manifest':str((base/'manifest.json').relative_to(R)),'author_manifest_sha256':mhash,'raw_values_compared':rawcount,'raw_zero_mask_checks':maskchecks,'F_values_compared':fdchecks,'Z_values_compared':zchecks,'gcd_classes_compared':len(authorclasses),'elapsed_seconds':round(time.monotonic()-t,3)})
 output=O/f'independent-D{D}-v2.json'
 with output.open('x')as f:json.dump(own,f,separators=(',',':'));f.write('\n')
 results.append({'D':D,'columns':len(cols),'divisors':len(own['divisors']),'rows':len(own['rows']),'all9_direct_h1_numerators':own['direct_pair'],'ordered_pair_incidence_checks':own['incidence_pair_checks'],'raw_values':rawcount,'F_values':fdchecks,'Z_values':zchecks,'output':str(output.relative_to(R)),'sha256':sha(output)})
receipt={'passed':True,'cases':results,'old_checks_or_author_checkers_imported_or_run':False,'D144_completed_case_reused_without_rerun':True,'harness_diagnostic_sha256':sha(O/'harness-diagnostic-v1.json'),'method':'Independent lattice ideal enumeration/factorization; direct finite-field powers; original ordered-divisor A/C/mu; direct ordered pair and exact gcd classes; separate divisor buckets.','checker_sha256':{str(Path(__file__).relative_to(R)):sha(Path(__file__)),str(Path(__file__).with_name('independent_small_family_v1.py').relative_to(R)):sha(Path(__file__).with_name('independent_small_family_v1.py'))},'elapsed_seconds':round(time.monotonic()-start,3)}
p=O/'small-data-checks-v2.json'
with p.open('x')as f:json.dump(receipt,f,indent=2);f.write('\n')
print(json.dumps({'passed':True,'receipt':str(p.relative_to(R)),'sha256':sha(p),'cases':results},indent=2))
