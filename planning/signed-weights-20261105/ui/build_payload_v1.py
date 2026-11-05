from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parents[3];P=Path(__file__).resolve().parent;O=R/'outputs/checks/2026-11-05-signed-weights/ui';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
paths=['outputs/checks/2026-11-05-signed-weights/joint-budget/fixed-profile-h1-v1.json','outputs/checks/2026-11-05-signed-weights/review-diagnostic/independent-diagnostic-v1.json','outputs/checks/2026-11-05-signed-weights/review-diagnostic/acceptance-v1.json','outputs/checks/2026-11-05-signed-weights/joint-budget/signed-components-v1.json','outputs/checks/2026-11-05-signed-weights/joint-budget/variance-only-negative-control-v1.json']
sources={p:sha(R/p) for p in paths};a=json.loads((R/paths[0]).read_text());d=json.loads((R/paths[1]).read_text());assert a['passed'] and d['passed'];PH=[(1,0),(1,1),(0,1),(-1,0),(-1,-1),(0,-1)]
def mul(x,y):return x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0]-x[1]*y[1]
def add(x,y):return x[0]+y[0],x[1]+y[1]
def conj(x):return x[0]-x[1],-x[1]
def norm(z):return z[0]**2-z[0]*z[1]+z[1]**2
def ray(z):return(z[0]%2,z[1]%2,(z[0]+z[1])%3)
columns=[]
for n in [97051,96091]:
 c=d['columns'][str(n)];g=tuple(c['generator']);psi=next(mul(g,u) for u in PH if ray(mul(g,u))==(1,0,1));j=tuple(c['mu']*v for v in psi);assert norm(j)==n
 columns.append({**c,'N':n,'Psi_omega':psi,'j_omega':j,'rho_exact':'j/sqrt(N)','Psi_finite_conductor_norm':12})
rows=[]
for i,r in enumerate(d['all20_rows']):
 phases=[]
 for ids in [[0,1,2],[3,4]]:
  local=[r['q_raw_exponents'][j] for j in ids];phases.append(None if None in local else sum(local)%6)
 rows.append({**r,'id':i+1,'phases':phases,'values_omega':[(0,0) if e is None else PH[e] for e in phases]})
G=[[(0,0),(0,0)],[(0,0),(0,0)]]
for row in rows:
 for i in range(2):
  for j in range(2):G[i][j]=add(G[i][j],mul(row['values_omega'][i],conj(row['values_omega'][j])))
assert G==[[(14,0),(-4,-2)],[(-2,2),(20,0)]]
assert norm(G[0][1])==12 and sum(row['phases'][0] is None for row in rows)==6
C={'A':[1,1],'C':[0,2],'mu':[-1,1]};pairings={}
for mode in ['full','h1']:
 pairings[mode]={}
 for x,v in C.items():
  for y,w in C.items():
   total=(0,0)
   for i in range(2):
    for j in range(2):
     if mode=='h1' and i==j:continue
     total=add(total,tuple(v[i]*w[j]*k for k in G[i][j]))
   pairings[mode][x+':'+y]=total
assert pairings['full']['A:A']==(28,0) and pairings['h1']['A:A']==(-6,0)
payload={'schema':'fixed-h1-display-v1','source_sha256':sources,'parameters':{'D':60000,'U':244,'H':3833,'A1':37,'A2':7,'unit':1,'nu':1,'S':'above2,3'},'scope':'All20 rows of one literal unit class and two orientations of ONE selected q. Other column ideals and q values remain active under the same fixed W. No full-h1/energy/asymptotic claim.','profile':{'formula':'s(8(y−1))s(8(2−y))','plateau':['9/8','15/8'],'fixed_in_D':True,'nodes':['97051/60000','96091/60000']},'candidate_counts':{'candidate_pairs':44,'coprime_rejections':2,'capacity_rejections':22,'actual_rows':20},'q':d['selected_q'],'columns':columns,'coefficients':C,'rows':rows,'gram_omega':G,'pairings_before_D':pairings,'gamma_mean_omega':[-3,0],'centered_variance_sum':6,'centered_variance_average':3,'naive_mean_deleted_bound':{'actual_squared':36,'wrong_bound_squared':12},'spectral':{'full':{'trace':34,'determinant':268,'eigenvalues':'17 ± sqrt(21)'},'h1':{'trace':0,'determinant':-12,'eigenvalues':'±2 sqrt(3)'}},'provenance':'Display projection of saved exact integer/root-of-unity records; no browser training or arithmetic experiment rerun.'}
p=R/'web/data/fixed-h1.json';assert not p.exists();p.write_text(json.dumps(payload,separators=(',',':'),ensure_ascii=False)+'\n');assert all(sha(R/p)==h for p,h in sources.items())
receipt={'passed':True,'source_sha256':sources,'payload_sha256':sha(p),'payload_bytes':p.stat().st_size,'checker_sha256':sha(Path(__file__)),'rows':len(rows),'raw_values':40,'gram_omega':G,'all_projections_match_saved_exact_records':True,'old_payload_sha256':sha(R/'web/data/profile-uniformity.json')};(O/'payload-v1.json').write_text(json.dumps(receipt,indent=2)+'\n');print(json.dumps(receipt,indent=2))
