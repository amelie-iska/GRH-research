#!/usr/bin/env python3
"""Independent frozen-instance audit. No author arithmetic helpers imported.
The only author function called is verify_run for in-memory stale-byte controls.
All arithmetic reconstruction uses doubled rational/sqrt(-3) coordinates.
"""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
from fractions import Fraction as F
from collections import Counter
from itertools import product
from unittest.mock import patch
import hashlib,json,math,time
ROOT=Path('/home/iska/Documents/LaTeX-projects/GRH-from-Mac-20261104')
BASE=ROOT/'planning/arithmetic-learning-20261105/review-learning'
OUT=ROOT/'outputs/checks/2026-11-05-arithmetic-learning/review-learning'
RUN=ROOT/'outputs/experiments/2026-11-05-arithmetic-learning-v2'
PIN=json.loads((BASE/'review-input-pins-v1.json').read_text())
T0=time.monotonic(); COUNTS=Counter()
def ck(ok,kind):
 if not ok:raise AssertionError(kind)
 COUNTS[kind]+=1
# z=(x+y sqrt(-3))/2, independent from the implementation's zeta6 basis.
Z=(F(0),F(0)); ONE=(F(2),F(0))
R=((2,0),(1,1),(-1,1),(-2,0),(-1,-1),(1,-1))
def zread(z): a,b=map(F,z);return (2*a+b,b)
def zwrite(z):return [str((z[0]-z[1])/2),str(z[1])]
def za(z,w):return (z[0]+w[0],z[1]+w[1])
def zs(z,w):return (z[0]-w[0],z[1]-w[1])
def scale(t,z):return (t*z[0],t*z[1])
def conj(z):return (z[0],-z[1])
def zm(z,w):return ((z[0]*w[0]-3*z[1]*w[1])/2,(z[0]*w[1]+z[1]*w[0])/2)
def zn(z):return (z[0]**2+3*z[1]**2)/4
def zsum(xs):
 s=Z
 for z in xs:s=za(s,z)
 return s
def en(v):return v[0]**2-v[0]*v[1]+v[1]**2
def em(v,w):return (v[0]*w[0]-v[1]*w[1],v[0]*w[1]+v[1]*w[0]-v[1]*w[1])
def divide(v,w):
 n=en(w);a,b=em(v,(w[0]-w[1],-w[1]))
 return None if a%n or b%n else (a//n,b//n)
def strip(v):
 for p in ((2,0),(1,-1)):
  while True:
   q=divide(v,p)
   if q is None:break
   v=q
 return v

def binding():
 ck(hashlib.sha256((RUN/'manifest.json').read_bytes()).hexdigest()==PIN['manifest_sha256'],'binding')
 for name,sha in PIN['source_sha256'].items():ck(hashlib.sha256((ROOT/name).read_bytes()).hexdigest()==sha,'binding')
 for name,sha in PIN['artifact_sha256'].items():ck(hashlib.sha256((RUN/name).read_bytes()).hexdigest()==sha,'binding')
binding(); m=json.loads((RUN/'manifest.json').read_text()); d=json.loads((RUN/'input.json').read_text())
ck((d['D'],d['U'],d['H'],d['nu'])==(6000,60,625,'principal'),'scope')
D,U,H=6000,60,625
norms={7507,7519,8281,10507};B=2*math.isqrt(2*D)+2
all_node_generators=sorted(((a,b) for a in range(-B,B+1) for b in range(-B,B+1) if a%3==1 and b%3==0 and en((a,b)) in norms),key=lambda v:(en(v),v))
# Integer-factor support determines candidate prime ideals independently.
prime_norms={7,13,19,73,79,103,7507}
primes=sorted((a,b) for a in range(-B,B+1) for b in range(-B,B+1) if a%3==1 and b%3==0 and en((a,b)) in prime_norms)
ck(primes==list(map(tuple,d['prime_ideals'])),'column_support')
indcols=[]
for gen in all_node_generators:
 v=gen;factors=[];sf=True
 for p in primes:
  e=0
  while True:
   q=divide(v,p)
   if q is None:break
   v=q;e+=1
  if e:factors.append(p);sf &= e==1
 ck(v==(1,0),'factorization')
 if not sf:continue
 factors=sorted(factors);ds=[]
 for bits in product((0,1),repeat=len(factors))):
  ds.append(math.prod(en(p) for p,bit in zip(factors,bits) if bit))
 N=en(gen);indcols.append({'generator':gen,'norm':N,'primes':factors,'r_U':sum(v>U and N//v>U for v in ds),'mu':(-1)**len(factors),'divisors':sorted(ds)})
ck(len(indcols)==15,'column_support')
for a,b in zip(indcols,d['columns']):
 ck(a['generator']==tuple(b['generator']) and a['norm']==b['norm'] and a['primes']==list(map(tuple,b['primes'])) and a['r_U']==b['r_U'] and a['mu']==b['mu'] and a['divisors']==sorted(b['divisor_norms']),'column_support')
ck(Counter(c['norm'] for c in indcols)==Counter({7507:2,7519:4,8281:1,10507:8}),'column_support')
# Independent full literal row support and all local symbols.
BR=2*math.isqrt(H)+2
rows=sorted(((a,b) for a in range(-BR,BR+1) for b in range(-BR,BR+1) if 0<en((a,b))<=H),key=lambda v:(en(v),v))
ck(rows==[tuple(r['element']) for r in d['rows']],'row_support')
ck(len(rows)==2262 and sum(en(v)==1 for v in rows)==6,'row_support')
tables=[]
for a,b in primes:
 p=en((a,b));w=(-a*pow(b,-1,p))%p;roots=[pow(1+w,k,p) for k in range(6)]
 ck((w*w+w+1)%p==0 and len(set(roots))==6,'phase_embedding')
 tables.append((p,w,{v:k for k,v in enumerate(roots)}))
local=[];raw=[];ip={p:i for i,p in enumerate(primes)}
for u,stored in zip(rows,d['rows']):
 ph=[]
 for p,w,roots in tables:
  z=(u[0]+u[1]*w)%p;ph.append(None if z==0 else roots[pow(z,(p-1)//6,p)])
 ck(ph==stored['prime_phases'],'local_phase_row')
 vals=[]
 for c in indcols:
  es=[ph[ip[p]] for p in c['primes']];vals.append(None if None in es else sum(es)%6)
 ck(vals==stored['raw_column_phases'],'raw_phase_row');local.append(ph);raw.append(vals)
 ck(en(strip(u))==stored['outside_S_norm'],'row_S_classification')
rowsets={'all_literal':list(range(len(rows))),'guaranteed_nonprincipal':[i for i,u in enumerate(rows) if en(strip(u))>1]}
ck(len(rowsets['guaranteed_nonprincipal'])==2148 and 7**4>H,'guaranteed_scope')
pairs=d['pairs'];blocks=d['blocks'];ck(len(pairs)==210 and len(blocks)==95,'orientation_structure')
for i,j in product(range(15),repeat=2):
 if i==j:continue
 p=next(t for t in pairs if t['m']==i and t['n']==j);b=blocks[p['block']]
 a=set(indcols[i]['primes']);c=set(indcols[j]['primes']);h=tuple(sorted(a&c));q=tuple(sorted(a^c));sg=[1 if x in a-c else -1 for x in q]
 ck(h==tuple(map(tuple,b['h'])) and q==tuple(map(tuple,b['q'])) and math.prod(en(x) for x in h)==b['Nh'] and math.prod(en(x) for x in q)==b['Nq'],'orientation_structure')
 ck(p['mu_q']==(-1)**len(q)==indcols[i]['mu']*indcols[j]['mu'],'signed_mu')
 o=next(t for t in b['orientations'] if t['pair']==p['id'])
 ck(o['signs']==sg and o['mask']==p['orientation_mask']==sum(1<<k for k,x in enumerate(q) if x in a-c),'orientation_structure')
for b in blocks:
 ck(len({o['mask'] for o in b['orientations']})==len(b['orientations']),'orientation_unique')
 for a,c in product(b['orientations'],repeat=2):
  # Exact factorized finite-group character orthogonality, not dense6^k enumeration.
  value=ONE
  for x,y in zip(a['signs'],c['signs']):value=zm(value,scale(F(1,6),zsum(R[((x-y)*e)%6] for e in range(6))))
  ck(value==(ONE if a['mask']==c['mask'] else Z),'phase_orthogonality')
Gs={};histcells=0
for name,inds in rowsets.items():
 case=d['row_cases'][name]
 ck(inds==case['row_indices'] and len(inds)==case['row_count'],'row_support')
 G=[]
 for i in range(15):
  line=[]
  for j in range(15):
   xx=yy=0
   for r in inds:
    a,b=raw[r][i],raw[r][j]
    if a is not None and b is not None:
     x,y=R[(a-b)%6];xx+=x;yy+=y
   got=(F(xx),F(yy));ck(got==zread(case['Gamma_matrix'][i][j]),'Gram_target');line.append(got)
  G.append(line)
 Gs[name]=G
 ck([G[p['m']][p['n']] for p in pairs]==list(map(zread,case['Gamma'])),'Gamma_orientation_vector')
 ck(sum(e is None for r in inds for e in raw[r])==case['raw_zero_entries']==4530,'raw_zero_count')
 for b,hist in zip(blocks,case['histograms']):
  h=list(map(tuple,b['h']));q=list(map(tuple,b['q']));counter=Counter();invalid=0
  for r in inds:
   if any(local[r][ip[p]] is None for p in h+q):invalid+=1
   else:counter[tuple(local[r][ip[p]] for p in q)]+=1
  stored={tuple(c['phase']):c['count'] for c in hist['cells']}
  ck(counter==stored and invalid==hist['invalid_rows'] and sum(counter.values())+invalid==len(inds),'sparse_histogram')
  histcells+=len(counter)
print(json.dumps({'progress':'independent rows, columns, phases, Gram, histograms PASS','elapsed':round(time.monotonic()-T0,2)}),flush=True)
negative=[];case_reports=[]
for summary in m['cases']:
 run=json.loads((RUN/summary['file']).read_text());name,profile=run['row_set'],run['profile'];inds=rowsets[name];G=Gs[name];target=[G[p['m']][p['n']] for p in pairs]
 ck(run['input_sha256']==PIN['input_sha256'] and run['seed']==20261105,'case_binding')
 W=[ONE if profile=='real' else (2+F(4*c['norm']-30000,D),F(4*c['norm']-30000,D)) for c in indcols]
 dc=[];dm=[];lam=[]
 for p in pairs:
  i,j=p['m'],p['n'];w=zm(W[i],conj(W[j]));dc.append(scale(indcols[i]['r_U']*indcols[j]['r_U'],w));dm.append(scale(indcols[i]['r_U'],w));lam.append(1+zn(dc[-1])+zn(dm[-1]))
 ck(dc==list(map(zread,run['weights_CC'])) and dm==list(map(zread,run['weights_CM'])) and lam==list(map(F,run['positive_weights'])),'weights')
 # Direct literal amplitudes, independent of Gamma/signed assembly.
 CC=CM=MM=Z
 for r in inds:
  C=M=Z
  for c,w,e in zip(indcols,W,raw[r]):
   if e is not None:
    v=scale(c['mu'],zm(w,R[e]));M=za(M,v);C=za(C,scale(c['r_U'],v))
  CC=za(CC,(2*zn(C),F(0)));CM=za(CM,zm(C,conj(M)));MM=za(MM,(2*zn(M),F(0)))
 exact={'CC':scale(F(1,D),CC),'CM':scale(F(1,D),CM),'MM':scale(F(1,D),MM)}
 ck(exact=={k:zread(v) for k,v in run['exact'].items()},'direct_readout')
 diagCC=sum((c['r_U']**2*zn(w)*G[i][i][0]/2 for i,(c,w) in enumerate(zip(indcols,W))),F(0));diagCM=sum((c['r_U']*zn(w)*G[i][i][0]/2 for i,(c,w) in enumerate(zip(indcols,W))),F(0))
 def predict(g,coeff,diag):return scale(F(1,D),za((2*diag,F(0)),zsum(scale(p['mu_q'],zm(a,x)) for p,a,x in zip(pairs,coeff,g))))
 ck(predict(target,dc,diagCC)==exact['CC'] and predict(target,dm,diagCM)==exact['CM'],'signed_readout')
 Kcc=sum((zn(a)/w for a,w in zip(dc,lam)),F(0));Kcm=sum((zn(a)/w for a,w in zip(dm,lam)),F(0));ck(Kcc==F(run['K_CC_squared']) and Kcm==F(run['K_CM_squared']),'certificate_constant')
 init=[]
 for p in pairs:
  i,j=p['m'],p['n'];a,b=min(i,j),max(i,j);h=hashlib.sha256(f'20261105:{a}:{b}'.encode()).digest();z=zread((F(int.from_bytes(h[:4],'big')%19-9,8),F(int.from_bytes(h[4:8],'big')%19-9,8)));init.append(z if i<j else conj(z))
 errors=[zs(g,t) for g,t in zip(init,target)];L0=sum((w*zn(e) for w,e in zip(lam,errors)),F(0));tau=F(run['tau']);accepted=[]
 for k,state in enumerate(run['metric_GD']['states']):
  g=list(map(zread,state['coordinates']));ck(state['step']==k and g==[za(t,scale(F(1,2**k),e)) for t,e in zip(target,errors)],'metric_state')
  loss=sum((w*zn(zs(x,y)) for w,x,y in zip(lam,g,target)),F(0));ck(loss==F(state['weighted_full_loss'])==L0/4**k,'metric_loss')
  pc=predict(g,dc,diagCC);pm=predict(g,dm,diagCM);bc=Kcc*loss/D**2;bm=Kcm*loss/D**2;unif=loss/min(lam)
  ck(pc==zread(state['predicted_CC']) and pm==zread(state['predicted_CM']),'metric_prediction')
  ec=zn(zs(pc,exact['CC']));emv=zn(zs(pm,exact['CM']))
  ck(ec==F(state['actual_error_CC_squared'])<=bc and emv==F(state['actual_error_CM_squared'])<=bm,'metric_actual_error')
  ck(bc==F(state['certificate_CC_squared']) and bm==F(state['certificate_CM_squared']) and unif==F(state['uniform_coordinate_certificate_squared']),'metric_certificate')
  ck(all(zn(zs(x,y))<=unif for x,y in zip(g,target)),'uniform_certificate')
  ok=max(bc,bm,unif)<=tau*tau;ck(state['accepted']==ok,'acceptance');accepted.append(ok)
 ck(accepted[-1] and not any(accepted[:-1]) and len(accepted)-1==summary['updates']==run['metric_GD']['updates_executed'],'first_accepted_state')
 final=g
 # Ordinary GD independently diagonalized in a+b and a-b eigencoordinates.
 eta=F(2,3)/max(lam);rho=1-min(lam)/(3*max(lam));ck(eta==F(run['ordinary_GD']['eta']) and rho==F(run['ordinary_GD']['rho']),'ordinary_step_parameters')
 eab=[((e[0]-e[1])/2,e[1]) for e in errors];st=[(a+b,a-b) for a,b in eab];fast=[1-3*eta*w/2 for w in lam];slow=[1-eta*w/2 for w in lam];prev=None
 for k,state in enumerate(run['ordinary_GD']['states']):
  expect=[];loss=F(0)
  for t,w,(s0,t0),fh,fl in zip(target,lam,st,fast,slow):
   s=s0*fh**k;tt=t0*fl**k;a=(s+tt)/2;b=(s-tt)/2;expect.append(za(t,(2*a+b,b)));loss+=w*(3*s*s+tt*tt)/4
  ck(state['step']==k and expect==list(map(zread,state['coordinates'])),'ordinary_state')
  ck(loss==F(state['weighted_full_loss']),'ordinary_loss')
  if prev is not None:ck(loss<=rho*rho*prev,'ordinary_contraction')
  prev=loss
 ck(len(run['ordinary_GD']['states'])==51 and run['ordinary_GD']['updates_executed']==50 and run['ordinary_GD']['budget_limited'] and not run['ordinary_GD']['requested_tau_certified'],'ordinary_scope')
 for b,feat in zip(blocks,run['feature_predictions']):
  ck(feat['block']==b['id'] and feat['active_orientation_count']==len(b['orientations']) and feat['phase_group_size']==6**len(b['q']),'feature_structure')
  for item in feat['values']:
   val=Z;tv=Z
   for o in b['orientations']:
    p=pairs[o['pair']];a=set(indcols[p['m']]['primes']);exponent=-sum((1 if tuple(pr) in a else -1)*e for pr,e in zip(b['q'],item['phase']))%6
    val=za(val,zm(final[p['id']],R[exponent]));tv=za(tv,zm(target[p['id']],R[exponent]))
   ck(val==zread(item['prediction']) and tv==zread(item['target']),'feature_value')
 neg=[p['id'] for p,a,t in zip(pairs,dc,target) if p['mu_q']==-1 and a!=Z and t!=Z];ck(neg==run['negative_q_nonzero_CC_pair_ids'] and len(neg)==64,'negative_mu_nonzero')
 unsigned=scale(F(1,D),zsum(zm(a,t) for a,t in zip(dc,target)));signed=scale(F(1,D),zsum(scale(p['mu_q'],zm(a,t)) for p,a,t in zip(pairs,dc,target)));ck(unsigned!=signed and unsigned==zread(run['negative_control_unsigned_offdiag_CC']) and signed==zread(run['signed_offdiag_CC']),'negative_unsigned_mu')
 # An incorrect no-conjugate complex profile and scalar-only fit are detected.
 if profile=='complex':
  wrong=[scale(indcols[p['m']]['r_U']*indcols[p['n']]['r_U'],zm(W[p['m']],W[p['n']])) for p in pairs]
  ck(wrong!=dc and predict(target,wrong,diagCC)!=exact['CC'],'negative_W_conjugation')
 nonzero=[scale(p['mu_q'],a) for p,a in zip(pairs,dc) if a!=Z];a,b=nonzero[:2];e1,e2=b,scale(-1,a)
 ck(za(zm(a,e1),zm(b,e2))==Z and zn(e1)+zn(e2)>0,'negative_scalar_only_fit')
 case_reports.append({'file':summary['file'],'metric_updates':len(accepted)-1,'ordinary_updates':50,'CC':zwrite(exact['CC']),'CM':zwrite(exact['CM']),'nonzero_negative_mu_CC_orientations':len(neg),'final_certificates_le_tau_squared':True})
 print(json.dumps({'progress':summary['file']+' all states/certificates PASS','elapsed':round(time.monotonic()-T0,2)}),flush=True)
 # Release huge ordinary rational strings before reading next case.
 del run
# Additional local negative controls are exact, not source mutations.
ck(len({c['norm'] for c in indcols})==4<15,'negative_norm_keys')
ck(zn(zread((1,1)))==3>2,'negative_Euclidean_norm')
ck(Gs['all_literal'][0][0][0]/2==2262 and sum(en(u)==1 for u in rows)==6,'negative_drop_units')
common_example=None
for p in pairs:
 b=blocks[p['block']]
 if b['h']:
  for ri in rowsets['all_literal']:
   if all(local[ri][ip[tuple(pr)]] is not None for pr in b['q']) and any(local[ri][ip[tuple(pr)]] is None for pr in b['h']):
    ck(raw[ri][p['m']] is None and raw[ri][p['n']] is None,'negative_drop_common_h');common_example={'pair':p['id'],'row':rows[ri],'h':b['h'],'q':b['q']};break
 if common_example:break
ck(common_example is not None,'negative_drop_common_h')
# Source/artifact stale-byte refusal: import solely this verification routine.
sys.path.insert(0,str(ROOT/'examples/arithmetic_learning'));import learn
original=Path.read_bytes;tamper=[]
for rel in ('examples/arithmetic_learning/learn.py','outputs/experiments/2026-11-05-arithmetic-learning-v2/input.json','outputs/experiments/2026-11-05-arithmetic-learning-v2/all_literal-complex.json'):
 target=(ROOT/rel).resolve()
 def reader(path):
  data=original(path);return data+b' in-memory reviewer alteration' if path.resolve()==target else data
 with patch.object(Path,'read_bytes',reader):
  try:learn.verify_run(RUN)
  except RuntimeError as e:message=str(e)
  else:raise AssertionError('tampered bytes accepted: '+rel)
 ck('Stale ' in message,'tamper_refusal');tamper.append({'path':rel,'refused':True,'message':message})
ck(learn.verify_run(RUN),'author_binding_restore');binding()
receipt={'verdict':'PASS','scope':'Independent exact code/math and immutable v2 artifact review; no analytic/Lean/GRH/generalization or PSD claim','counts':dict(COUNTS),'total_check_units':sum(COUNTS.values()),'local_symbols_reconstructed':len(rows)*len(primes),'Gram_entries_reconstructed':450,'histogram_cells_reconstructed':histcells,'metric_updates_replayed':216,'ordinary_updates_replayed':200,'cases':case_reports,'common_zero_negative_control':common_example,'in_memory_tamper_controls':tamper,'protected_bytes_mutated':False,'reviewer_code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'run_manifest_sha256':PIN['manifest_sha256'],'input_sha256':PIN['input_sha256'],'source_sha256':PIN['source_sha256'],'artifact_sha256':PIN['artifact_sha256'],'elapsed_seconds':round(time.monotonic()-T0,3),'limitations':['Weights define a Fourier-coordinate/RKHS norm; unweighted phase L2 Parseval alone gives sum|delta g|^2, not sum lambda|delta g|^2.','verify_run is a hash-binding check against the manifest, not a mathematical replay or authentication signature; this review pins the external immutable manifest hash.','All15 active columns of the specified four-bump W; principal nu; two specified finite row sets. No range/conductor/profile generalization.','Metric training uses exact supervised Gamma labels. Ordinary50-step trajectories remain budget limited and unrequested-error-certified.']}
with (OUT/'independent-review-v1.json').open('x') as f:json.dump(receipt,f,indent=2);f.write('\n')
print(json.dumps({'verdict':'PASS','checks':sum(COUNTS.values()),'elapsed':receipt['elapsed_seconds'],'receipt':str(OUT/'independent-review-v1.json')}),flush=True)
