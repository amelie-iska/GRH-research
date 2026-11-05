"""New saved-state check of the coupled short-coefficient lemma; no evaluator rerun."""
from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parents[3];RUN=ROOT/'outputs/checks/2026-11-05-rough-mask/finite/run-v1'
sha=lambda b:hashlib.sha256(b).hexdigest()
assert sha((RUN/'manifest.json').read_bytes())=='d8ebdc9410e0e24c3dfd999ea33c10864d28b4e9f008913e08d26233217268cf'
results=[]
for D in (200,512,900):
 d=json.loads((RUN/f'D{D}-v1.json').read_bytes());U=d['parameters']['U'];ideals=d['all_good_ideals'];active=[];short=[];nonfactor=[]
 for g in ideals:
  if not g['squarefree'] or g['norm']>7*U:continue
  formula=g['mu']*(2*int(g['norm']<=U)-1)
  assert g['A']==formula and abs(g['A'])==1
  short.append(dict(g_id=g['id'],N=g['norm'],A=g['A'],mu=g['mu'],coupled_short_indicator=int(g['norm']<=U),formula=formula))
 for state in d['rough_states']:
  assert state['P']>U
  f=ideals[state['f']]
  for term in state['terms']:
   g=ideals[term['fa_id']];a=ideals[term['a_id']];assert g['norm']==f['norm']*a['norm']
   assert D<term['extended_column_norm']<2*D and g['norm']*state['P']==term['extended_column_norm'] and g['norm']<7*U
   formula=g['mu']*(2*int(g['norm']<=U)-1)
   assert term['original_A_fa']==g['A']==formula and abs(formula)==1
   active.append(dict(row=state['row'],f=state['f'],p=state['p'],a=term['a_id'],g=term['fa_id'],N_g=g['norm'],P=state['P'],A=g['A'],formula=formula,raw_f_mask=state['f_raw_mask'],raw_phase=term['raw_phase'],nonSF_extended_auxiliary=term['auxiliary_nonSF']))
   if g['A']!=f['A']*a['A'] and len(nonfactor)<4:nonfactor.append(dict(f=f['id'],a=a['id'],g=g['id'],N_g=g['norm'],A_g=g['A'],wrong_separate_product=f['A']*a['A'],profile_node=term['extended_column_norm'],raw_f_mask=state['f_raw_mask']))
 rowcounts=[]
 critical=d['parameters']['H']**4<=D**3
 for row in d['rows']:
  support=set(row['v1_prime_ids'])|set(row['v2_prime_ids']);rough=[pid for pid in support if d['prime_ideals'][pid]['norm']>U]
  if critical:assert len(rough)<=1
  rowcounts.append(dict(row=row['id'],Nu=row['N'],H=d['parameters']['H'],H_critical=critical,rough_prime_ideal_ids=rough,kappa=len(rough)))
 if D==900:assert not critical and all(r['kappa']==0 for r in rowcounts)
 else:assert critical and all(r['kappa']==1 for r in rowcounts)
 results.append(dict(D=D,U=U,passed=True,all_saved_SF_g_up_to_7U=short,active_rough_g_occurrences=active,active_occurrence_count=len(active),distinct_active_g=len({r['g']for r in active}),all_active_A_exact_plus_or_minus_one=True,unit_g_checked=any(r['N']==1 and r['A']==1 for r in short),nonfactorization_negatives=nonfactor,rows=rowcounts))
d=json.loads((RUN/'D200-v1.json').read_bytes());columns=[d['all_good_ideals'][i] for i in d['original_columns']];bad=next(m for m in columns if m['norm']==247)
blind=bad['mu']*(2*int(bad['norm']<=10)-1)
assert bad['A']==1 and bad['mu']==1 and blind==-1 and bad['norm']>7*10
negative=dict(D=200,U=10,original_column=bad['id'],generator=bad['generator'],prime_ideal_ids=bad['prime_ids'],norm=247,lemma_applicable=False,seven_U=70,actual_A=1,blind_out_of_domain_formula=-1,rejected=True,scope='The short lemma cannot be applied to all original columns or turned into unrestricted multiplicativity')
value=dict(passed=True,input_manifest_sha256=sha((RUN/'manifest.json').read_bytes()),checker_sha256=sha(Path(__file__).read_bytes()),cases=results,explicit_original_norm247_negative=negative,total_active_occurrences=sum(r['active_occurrence_count']for r in results),raw_evaluator_rerun=False,old_runs_read=False,scope='New exact saved-state checks only. No proof of the allU coefficient lemma, geometric kappa theorem, explicit2^18 analytic error constant or asymptotic saving is claimed from finite data.')
p=ROOT/'outputs/checks/2026-11-05-rough-mask/finite/coupled-short-coefficients-v1.json'
with p.open('x') as f:json.dump(value,f,sort_keys=True,indent=2);f.write('\n')
print(sha(p.read_bytes()));print(json.dumps(dict(total=value['total_active_occurrences'],cases=[dict(D=r['D'],active=r['active_occurrence_count'],distinct_g=r['distinct_active_g'],short_g=len(r['all_saved_SF_g_up_to_7U']),kappa=[x['kappa']for x in r['rows']])for r in results],negative=negative),sort_keys=True))
