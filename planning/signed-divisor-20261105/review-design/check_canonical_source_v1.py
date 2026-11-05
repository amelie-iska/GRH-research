from pathlib import Path
import json,hashlib,re,datetime
from fractions import Fraction
R=Path('/home/iska/Documents/LaTeX-projects/GRH-from-Mac-20261104')
P=R/'planning/signed-divisor-20261105/review-design';O=R/'outputs/checks/2026-11-05-signed-divisor/review-design'
def pin(rel,expected=None):
 p=R/rel;b=p.read_bytes();s=hashlib.sha256(b).hexdigest()
 if expected:assert s==expected,(rel,s)
 return {'path':str(p),'bytes':len(b),'sha256':s}
def load(p):return json.loads(Path(p).read_text())
contracts={
'core':('planning/signed-divisor-20261105/root/signed-divisor-core.tex','bce916fab66aab19718a127b26b3ac581e48f49e0dd0317a64cf1648a4e5b7cb'),
'details_v4':('planning/signed-divisor-20261105/root/signed-divisor-details.tex','504318141e100fd43f1021492c349a655953909b3213a083452d1230fa35cbc9'),
'analytic_v3':('planning/signed-divisor-20261105/analytic-attempt/SIGNED_D_SERIES-v3.md','eff02d2e5cecae7554e873cbd4b9c34a24507b5cc78a27c7837669dc4b9247dc'),
'incidence_v2':('planning/signed-divisor-20261105/root/DIVISOR_INCIDENCE_LIFT-v2.md','a062a9b85603c0e7b300c219db10724c4b33f57c060eb51e6a5b5f201faa3732'),
'analytic_acceptance':('outputs/checks/2026-11-05-signed-divisor/review-design/analytic-acceptance-v1.json','69c748be5733835bcddd689b5b2096606ec8d7b1ed532996a033aa15e4860303'),
'incidence_acceptance':('outputs/checks/2026-11-05-signed-divisor/review-design/incidence-acceptance-v1.json','2ec9dc7967e373da2b99fe3c71e847404975344dfbcff06e2921f902add51434'),
'small_acceptance':('outputs/checks/2026-11-05-signed-divisor/review-design/small-data-acceptance-v1.json','90b93e8e9b99c6d733fd359a1541d34072dab8b7f05109b2cc1d02983b68c9d2'),
'unit_compatibility':('outputs/checks/2026-11-05-signed-divisor/review-design/unit-edge-compatibility-v1.json','51e0888826bdba55e06df33f827e1daf5bc463dbdf47d1a5d236278a6ddc8a85'),
'large_independent':('outputs/checks/2026-11-05-signed-divisor/analytic/large-full-column-review-v1/independent-large-v1.json','5c17b8795f53abdfd3da4b3281c7ca69cfce096a5a28a09f32c91baec4226d6a'),
'large_acceptance':('outputs/checks/2026-11-05-signed-divisor/analytic/large-full-column-review-v1/acceptance-v1.json','9180417cdef0073ea89efac75c2526929496a02c70f445586bebe8dbb95ec094')}
inputs={k:pin(*v) for k,v in contracts.items()}
for k in ['analytic_acceptance','incidence_acceptance','small_acceptance','unit_compatibility','large_independent','large_acceptance']:
 j=load(inputs[k]['path']);assert j.get('passed',j.get('accepted',False)),k
texts=[Path(inputs[k]['path']).read_text() for k in ['core','details_v4']];bs=chr(92)
def tokens(t,name):return [x.split('}',1)[0] for x in t.split(bs+name+'{')[1:]]
labels=sum((tokens(t,'label') for t in texts),[]);refs=sum((tokens(t,'ref')+tokens(t,'eqref') for t in texts),[])
assert len(labels)==len(set(labels))==18
assert not set(x for x in refs if x.startswith('sd:'))-set(labels)
for p in [R/'book/chapters/signed-weights-core.tex',R/'papers/signed-weights-core.tex']:assert bs+'label{sw:core}' in p.read_text()
for t in texts:
 stripped='\n'.join(x.split('%',1)[0] for x in t.splitlines());balance=0
 for i,c in enumerate(stripped):
  if c in '{}':
   j=i-1;n=0
   while j>=0 and stripped[j]==bs:n+=1;j-=1
   if n%2:continue
   balance+=1 if c=='{' else -1;assert balance>=0
 assert balance==0
 stack=[]
 for m in re.finditer(re.escape(bs)+r'(begin|end)\{([^}]+)\}',stripped):
  kind,name=m.groups()
  if kind=='begin':stack.append(name)
  else:assert stack and stack.pop()==name
 assert not stack
 assert stripped.count('$')%2==0
 assert stripped.count(bs+'[')==stripped.count(bs+']')
 commands=[m.group(1) for m in re.finditer(re.escape(bs)+r'([A-Za-z]+|.)',t)]
 assert 'Na' not in commands
assert 'unweighted two-pivot block ($w_u=1$)' in texts[1]
assert 'squarefree,good}'+bs+bs+'Na,Nb' in texts[1]
assert bs+'nu(d)'+bs+'chi_d(u)T_d^X(u)' in texts[1]
cases=[]
for D,AA in [(144,Fraction(-19,36)),(576,Fraction(-221,288)),(60000,Fraction(-5119,5000))]:
 rel=f'outputs/experiments/2026-11-05-signed-divisor-D{D}-v1/'
 s=pin(rel+'summary.json');m=pin(rel+'manifest.json');j=load(s['path']);n=j['normalized_h1'];b=j['divisor_budget']
 for k in n:assert [Fraction(x) for x in n[k]]==[Fraction(x,D) for x in b[k]['signed_numerator_omega']]
 assert Fraction(n['AA'][0])==AA==Fraction(n['CC'][0])-Fraction(n['Cmu'][0])-Fraction(n['muC'][0])+Fraction(n['mumu'][0])
 assert n['Cmu']==n['muC'] and all(n[k][1]=='0' for k in n)
 cases.append({'D':D,'summary':s,'manifest':m,'counts':j['counts'],'h1_all9':n,'AA_even_odd':[b['AA']['even_mu_Z_omega'],b['AA']['odd_mu_Z_omega']]})
large=load(inputs['large_independent']['path']);assert large['input_manifest_sha256']==cases[-1]['manifest']['sha256']
assert large['all_inputs_and_frozen_sources_unchanged'] and not large['author_arithmetic_modules_or_old_checkers_executed']
for k,z in large['all9signed_numerators'].items():assert z==load(cases[-1]['summary']['path'])['divisor_budget'][k]['signed_numerator_omega']
assert sum(c['counts']['columns'] for c in cases)==17158
assert [int(Fraction(cases[-1]['h1_all9'][k][0])*30000) for k in ['AA','AC','Amu','CA','CC','Cmu','muA','muC','mumu']]==[-30714,-11287,19427,-11287,2644,13931,19427,13931,-5496]
report='''# Independent signed-divisor canonical source review\n\nAccepted for canonical copy/build at the exact core and v4 details digests in the receipt. This is a mathematical and source review, not a compilation or a new scientific execution.\n\nThe full ideal-divisor inversion retains original signs, self-divisors and every raw collision. Linear-first pairing, weighted Cauchy and the Frobenius E_d certificate give the stated arbitrary-vector lift and perturbation inequality without a PSD assumption on the coprime form. The classical two-pivot input is explicitly unweighted. F_d has the required common nu(d)chi_d phase relative to T_d.\n\nAt fixed residual a,b (allowed to overlap), d avoids the full S/abu union. Expansion of1-zPQ gives the four numerator and five reciprocal zeta factors. The146+26 degree majorants justify172; the five denominator factors give the stated normal half-plane bound without claiming nonvanishing. Finite-height Perron errors, the half-integer gap and absolute majorants justify only initial-domain Fubini and successive dominated limits. Four infinite Perron integrals are not interchanged with Mellin.\n\nThe eight nonzero states and long00 state have correct signs. Atomic ideals are pairwise coprime while the four short products may overlap. The finite numerator, Nh<=U^4, sigma0 dependence and cutoff U-cost agree with analyticv3. The one common-profile Mellin transform, reversed orientation and ratio-uniform decay are correct. The explicit coherent sum keeps full deletions and raw zeros. Fixed-parameter holomorphy supplies no uniform signed target or uncancelled-pole conclusion.\n\nAll displayed case counts, AA fractions, large even/odd masses, nonsquarefree rational norms and the exact3x3/30000 pairing table match frozen data. Small direct-pair and separate large literal-field/linear-poset acceptances are bound. The unused unit-edge helper fix does not replace any of the17158 saved columns or snapshots. Fixed delta and its potentially enormous derivative cost, different finite row blocks, and measured-versus-hypothetical resource statements are disclosed.\n\nAll18 new sd labels and internal references close; sw:core exists in both canonical copies. Braces, environment nesting and math delimiters pass a focused source check. The corrected substack has no Na control sequence. Earlier root drafts remain preserved. A reviewer-only naive substring check initially mistook valid double-backslash followed by Na for a command; its preserved diagnostic is bound, and the final check parses control tokens. No mathematical support guard was relaxed.\n\nNo canonical source was edited, no scientific table was rerun, and no compiler, browser, Lean, auth or publication action was used. Compilation/layout/UI remain separate. The signed asymptotic gain, arithmetic determinant/zero-location bridges and GRH remain open. No literature-priority claim is accepted.\n'''
rp=P/'CANONICAL-REVIEW-v1.md';assert not rp.exists();rp.write_text(report)
receipt={'schema':'signed-divisor-canonical-source-review-v1','passed':True,'accepted_for':'Root canonical copy/build at these exact bytes','created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'inputs':inputs,'review':pin(str(rp.relative_to(R))),'checker':pin(str(Path(__file__).relative_to(R))),'preserved_harness_diagnostic':pin('outputs/checks/2026-11-05-signed-divisor/review-design/canonical-harness-diagnostic-v1.json'),'new_labels':labels,'references':sorted(set(refs)),'structure_checks':{'braces':True,'environments':True,'math_delimiters':True,'substack_and_control_tokens':True,'unique_labels_and_reference_closure':True},'finite_cases':cases,'proof_review_pass':['Exact ideal inversion/raw zeros/self-pair cancellation','Weighted incidence and exact coefficient-error certificates','Unweighted classical lambda hypothesis','Four numerator/five reciprocal zeta signs and normal constant172','Initial-domain finite Perron errors and limit ordering','Eight short states with overlapping residuals and U-cost','One common-profile Mellin orientation and explicit coherent sum','All9 finite pairing values and independent acceptance bindings','Unit helper compatibility and fixed-profile scope'],'not_run':['Scientific or phase table reruns','Large direct quadratic pair loop','TeX/PDF/native compilation or browser','Lean/compiler install','Auth, publication or ref writes'],'open':['Actual signed asymptotic target','Positive determinant and zero-location bridges','GRH'],'canonical_files_edited':False,'source_guard':{k:hashlib.sha256(Path(v['path']).read_bytes()).hexdigest()==v['sha256'] for k,v in inputs.items()}}
assert all(receipt['source_guard'].values());out=O/'canonical-acceptance-v1.json';assert not out.exists();out.write_text(json.dumps(receipt,indent=2,sort_keys=True)+'\n')
print(json.dumps({'passed':True,'receipt':str(out),'receipt_sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'review_sha256':hashlib.sha256(rp.read_bytes()).hexdigest(),'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'labels':len(labels)},indent=2))
