"""Lossless compact own-data summary projection; no raw arithmetic or old-case rerun."""
from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parents[3];BASE=ROOT/'outputs/checks/2026-11-05-rough-mask/finite';RUN=BASE/'run-v1'
sha=lambda b:hashlib.sha256(b).hexdigest()
PINS={'run-v1/manifest.json':'d8ebdc9410e0e24c3dfd999ea33c10864d28b4e9f008913e08d26233217268cf','phase-transfer-and-normalization-v1.json':'640979b5120a4d6f5a0b38233db6dc1a804e3764ad397384e3c3d33a81c21ba8','coupled-short-coefficients-v1.json':'b9f57e6953ab6773c2fd4a44952df67f3759fc34c67b9d733f3be31b8ac71232'}
def main():
 captured={p:(BASE/p).read_bytes() for p in PINS}
 for p,h in PINS.items():assert sha(captured[p])==h
 manifest=json.loads(captured['run-v1/manifest.json'])
 for p,pin in manifest['files'].items():
  raw=(RUN/p).read_bytes();assert sha(raw)==pin['sha256'] and len(raw)==pin['bytes']
 phase=json.loads(captured['phase-transfer-and-normalization-v1.json']);coeff=json.loads(captured['coupled-short-coefficients-v1.json']);summary=json.loads((RUN/'summary.json').read_bytes());assert phase['passed'] and coeff['passed'] and summary['passed']
 cases=[]
 for result,table,ph,co in zip(summary['cases'],phase['tables'],phase['cases'],coeff['cases']):
  D=result['D'];assert table['D']==ph['D']==co['D']==D
  raw=json.loads((RUN/f'D{D}-v1.json').read_bytes())
  cases.append(dict(D=D,parameters=result['parameters'],counts=result['counts'],raw_numerators=table['raw_numerators'],normalized_exactly_once=table['normalized_exactly_once'],
    rows=[dict(id=r['id'],v1=r['v1'],v2=r['v2'],u=r['u'],norm=r['N'],literal_unit=r['literal_unit'],nonprincipal_reason=r['nonprincipal_reason'],kappa=co['rows'][i]['kappa'],rough_prime_ideal_ids=co['rows'][i]['rough_prime_ideal_ids'],H_critical=co['rows'][i]['H_critical']) for i,r in enumerate(raw['rows'])],
    phase_checks=dict(full_complex_F_transfer=ph['full_complex_F_transfer_checks'],original_AU_and_phase_product_checks=ph['actual_original_coefficient_and_phase_checks'],auxiliary_nonSF_terms_checked=ph['auxiliary_nonSF_terms_checked'],wrong_mu_p_coefficient_sign_control=ph['coefficient_sign_negative']),
    coefficient_checks=dict(active_profile_occurrences=co['active_occurrence_count'],distinct_active_g=co['distinct_active_g'],all_A_exact_plus_or_minus_one=co['all_active_A_exact_plus_or_minus_one'],unit_g_checked=co['unit_g_checked'],all_saved_SF_g_up_to_7U_checked=len(co['all_saved_SF_g_up_to_7U']),nonfactorization_negatives=co['nonfactorization_negatives']),
    exact_residual_intersection_subtraction=raw['raw_totals']['residual_intersection_subtraction_raw'],negative_controls=raw['negative_controls'],source_case_sha256=manifest['files'][f'D{D}-v1.json']['sha256']))
 data=dict(schema='rough-mask-controls-v1',AA_only=True,nu='principal1',S='Prime ideals above2and3',literal_unit_class=1,
  profile=dict(formula='W_delta(y)=s((y-1)/delta)s((2-y)/delta), standard smooth step',delta='1/4096',fixed_once=True,finite_integer_D_range='1<D<=1024',strict_integer_node_value=1,endpoint_value=0,derivative_cost='O_k(4096^k), potentially large fixed seminorms'),
  identities_raw=['AA=K0-KT+Ctwo','Delta=KS-KT=Erow+Eres','AA-(K0-KS)=Delta+Ctwo'],normalization='Every normalized value is its stored raw numerator divided byD exactly once.',
  conventions=dict(arithmetic='Z[omega], omega^2+omega+1=0',complex_pair='[a,b] meansa+b*omega',conjugation='[a-b,-b]',kernel='KT is masked; KS is S-only extension; both retain signedmu(f)',Ctwo='Unordered DISTINCT rough prime IDEALS with every original row mask; nonnegative component, not an h1 lower bound'),
  cases=cases,out_of_domain_norm247_negative=coeff['explicit_original_norm247_negative'],
  provenance=dict(raw_manifest=dict(path=str((RUN/'manifest.json').relative_to(ROOT)),sha256=PINS['run-v1/manifest.json']),phase_receipt=dict(path=str((BASE/'phase-transfer-and-normalization-v1.json').relative_to(ROOT)),sha256=PINS['phase-transfer-and-normalization-v1.json']),coefficient_receipt=dict(path=str((BASE/'coupled-short-coefficients-v1.json').relative_to(ROOT)),sha256=PINS['coupled-short-coefficients-v1.json']),actual_source_v1_sha256='c705fbb0985d69475f55d59241b27577134b826745a4dc2aa6f55fc77898f7ce',pure_helper_sha256='77dc26658a188ff6669bf577fcb8298b875ab2a5e4f8e0bfe628b94c9b9430d4',accepted_rough_v3_sha256='039548240acab66f883b6fc0d9bcee0e42a84fec5c390472ad501ef045e862c6',review_scope='Author finite exact identities/checks; independent analytic/data acceptance is separately bound by the release receipt.'),
  limitations=['Different declared row blocks, not a growth fit.','MixedD900/H384 is explicitly noncritical, notfloorD^.75; kappa0 is actual.','Only auxiliary rough-kernelg=fa hasNg<7U and A=plusorminus1; not all original columns and not multiplicativity.','Extendedp-squared columns are auxiliary nonsquarefree ideals, never original SFcolumns.','No finite proof of an analytic bound/theorem/constant; no asymptotic saving, PSDh1, GRH, speedup or training claim.'])
 out=ROOT/'web/data/rough-mask-controls.json';blob=(json.dumps(data,sort_keys=True,separators=(',',':'))+'\n').encode()
 with out.open('xb') as f:f.write(blob)
 assert all(sha((BASE/p).read_bytes())==h for p,h in PINS.items())
 receipt=dict(passed=True,projection_only=True,arithmetic_evaluator_rerun=False,old_cases_or_tables_read=False,projector_sha256=sha(Path(__file__).read_bytes()),input_pins=PINS,summary_path=str(out.relative_to(ROOT)),summary_sha256=sha(blob),summary_bytes=len(blob),all_raw_inputs_unchanged=True,scope='Compact own-data downloadable summary only; no new UI/runtime or analytic proof claim')
 p=BASE/'summary-projection-v1.json'
 with p.open('x') as f:json.dump(receipt,f,sort_keys=True,indent=2);f.write('\n')
 print(json.dumps(receipt,sort_keys=True))
if __name__=='__main__':main()
