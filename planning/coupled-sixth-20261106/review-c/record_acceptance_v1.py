from pathlib import Path
import json,hashlib,datetime,subprocess,os
R=Path('/home/iska/Documents/LaTeX-projects/GRH-from-Mac-20261104')
O=R/'outputs/checks/2026-11-06-coupled-sixth/review-c';O.mkdir(parents=True,exist_ok=True)
H=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
note='planning/coupled-sixth-20261106/lane-a/COHERENT_SIXTH_PART_RAY_MEAN-v1.md'
pins='outputs/checks/2026-11-06-coupled-sixth/lane-a/source-pins-v1.json'
assert H(R/note)=='4315f8d2fb10b5c0a5f91fb8ae4c1e3271582fb27bd2bc5ee5d44912e81621fd'
assert H(R/pins)=='1e4584b88412750f72aa2a6178a0aa243297612b728b2927cfc1a38f5840752d'
p=json.loads((R/pins).read_text());technical={};context=[]
for n,h in p['source_sha256'].items():
 current=H(R/n)
 if n in ['README.md','planning/MASTER_IMPLEMENTATION_PLAN.md']:
  context.append(dict(path=n,author_context_sha256=h,current_sha256=current,historical_context_not_technical_source=True))
 else:
  assert current==h,n;technical[n]=h
states=[]
for row in p['protected_states']:
 q=Path(row['path']);head=subprocess.check_output(['git','-C',str(q),'rev-parse','HEAD'],env={**os.environ,'GIT_OPTIONAL_LOCKS':'0'}).decode().strip()
 assert head==row['HEAD'] and H(Path(row['index_path']))==row['index_sha256'],str(q)
 states.append(dict(path=str(q),HEAD=head,index_sha256=row['index_sha256'],unchanged=True))
assert len(states)==12
review='planning/coupled-sixth-20261106/review-c/REVIEW-v1.md'
out={'schema':'coupled-sixth-independent-proof-acceptance-v1','created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'passed':True,'note':{'path':note,'sha256':H(R/note)},'author_source_pins':{'path':pins,'sha256':H(R/pins)},'review':{'path':review,'sha256':H(R/review)},'technical_source_sha256':technical,'historical_context_pins':context,'proved_normalized_error':'O_epsilon(B^2 (DXA2)^epsilon R X V^(-11/2) [1+sqrt(A1 X/D^2)])','retained_mean':'Exact principal psi=bar(rho)^6 density integral with full q=mn deletion and all original coefficient/root/ray/h/r/k/ell/e/capacity factors','full_ideal_inclusion_exclusion_including_Nd_greater_than_t':True,'closed_prefix_endpoints':True,'primitive_S_zeros_and_r_s_overlap_retained':True,'no_k_divides_s_assumption':True,'normalization_1_over_D_exactly_once':True,'scope':'Complete original good SF annulus, original unweighted two-pivot rows, finite primitive prefix; optionally projected first onto original unequal-norm pairs. Fixed S/ray/source and common W.','top_band_pure_error_power':'25/32','top_band_mixed_error_power':'59/96','principal_coherent_mean_not_estimated':True,'whole_signed_power':'13/12','global_unsigned_power':'9/8','GRH_Lean_or_full_target_gain':False,'outside_frozen_release_book_Main_selection':True,'old_controls_or_scientific_numeric_runs':0,'build_browser_auth_publication_index_actions':False,'protected_prior_states':states,'review_method':'Independent analytic reconstruction and direct comparison with current cbk exact kernel/Bessel source; no numerical tests.'}
out['receipt_producer']={'path':str(Path(__file__).relative_to(R)),'sha256':H(Path(__file__))}
path=O/'acceptance-v1.json'
with path.open('x') as f:json.dump(out,f,indent=2,sort_keys=True);f.write('\n')
print(json.dumps({'receipt':str(path.relative_to(R)),'sha256':H(path),'review_sha256':H(R/review),'technical_inputs':len(technical),'protected_states':len(states)},indent=2))
