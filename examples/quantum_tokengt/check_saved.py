"""Independent saved-record audits, physical observables and continuous densities."""
import hashlib,itertools,json,sys
import numpy as np
from scipy.special import logsumexp
from model import ROOT,teacher,spins,persistence,circuit_features,graph_tokens,attention,SEED
from train import predict,gfn_tb,gfn_reward,gfn_sample,metrics

def main():
    directory=ROOT/'web/data/quantum-tokengt';manifest=json.loads((directory/'manifest.json').read_text());raw=(directory/manifest['file']).read_bytes();assert hashlib.sha256(raw).hexdigest()==manifest['sha256'];d=json.loads(raw)
    dataset=json.loads((ROOT/d['dataset']['path']).read_text());assert hashlib.sha256((ROOT/d['dataset']['path']).read_bytes()).hexdigest()==d['dataset']['sha256']
    assert len(set(dataset['train'])&set(dataset['test']))==0;assert len(dataset['train'])==120 and len(dataset['test'])==40
    p=np.array(d['trace']['parameters']);angles,mask,ids=graph_tokens(p);features,states=circuit_features(angles,True)
    np.testing.assert_allclose(features[0],d['trace']['features'],atol=1e-13);np.testing.assert_allclose(states[0].real,d['trace']['state_real'],atol=1e-13)
    w=[np.array(v) for v in d['weights']['quantum-hybrid']];z,a=attention(features,w,mask,'hybrid',True)
    for key in ['query','key','value','scores','weights','context']:np.testing.assert_allclose(a[key],d['trace'][key],atol=1e-13)
    # Transport tokens and mask together: pooled output must be permutation invariant.
    order=np.random.default_rng(SEED).permutation(18);pred=np.array(predict(w,features,mask,'hybrid'));permuted=np.array(predict(w,features[:,order],mask[order],'hybrid'))
    perm_error=float(np.max(abs(pred-permuted)));assert perm_error<1e-12
    te=np.array(dataset['test']);allparams=np.array(dataset['parameters']);angles,mask,_=graph_tokens(allparams[te]);f=circuit_features(angles)
    prediction=np.array(predict(w,f,mask,'hybrid'))*np.array(d['normalization']['scale'])+np.array(d['normalization']['mean']);truth=np.stack([teacher(p)[:32] for p in allparams[te]])
    measured=metrics(truth,prediction)
    for key,value in measured.items():np.testing.assert_allclose(value,d['models']['quantum-hybrid']['heldout'][key],atol=1e-12)
    assert d['training']['steps']==900
    for m in d['models'].values():
        assert len(m['history'])==900 and m['history'][-1]['step']==900
        assert m['final_full_train_loss']<m['initial_full_train_loss']*.1
    assert len(d['concepts']['history'])==600 and len(d['gfn']['history'])==1800
    # Recompute discrete-code variational MI lower bound on actual heldout embeddings.
    zm=np.array(d['normalization']['zmean']);zs=np.array(d['normalization']['zscale']);emb=(np.array(attention(f,w,mask,'hybrid'))-zm)/zs
    c=d['concepts'];B=np.array(c['basis']);C=np.array(c['critic']);labels=np.tile(np.arange(6),len(te));base=np.repeat(emb,6,axis=0)
    delta=np.tanh(.3*base+.7*B[labels//2]*(2*(labels%2)-1)[:,None])-np.tanh(.3*base);logits=delta@C/.2
    ce=np.mean(logsumexp(logits,axis=1)-logits[np.arange(len(labels)),labels]);np.testing.assert_allclose(np.log(6)-ce,c['heldout_InfoNCE_lower_bound_nats'],atol=1e-11)
    # All finite forest rewards really are computed by exact physical teacher.
    tree=d['forest'];target=np.array(tree['target_observables']);errors=[]
    for node in tree['nodes']:
        exact=teacher(node['parameters'])[32:];np.testing.assert_allclose(exact,node['observables'],atol=1e-12)
        r=-np.mean(((exact-target)/np.array([3,.25,.25,.25,.25,.25]))**2);errors.append(abs(r-node['reward']))
    assert max(errors)<1e-12
    # Brownian-bridge identity: product forward / backward equals N(x_T;0,I).
    rng=np.random.default_rng(SEED+90);w0=[np.zeros((3,16)),np.zeros(16),np.zeros((16,2)),np.zeros(2),np.full((3,2),np.log(1/np.sqrt(3))),np.zeros(1)]
    paths=gfn_sample(w0,rng,100);expected=-np.log(2*np.pi)-.5*(paths[:,-1]**2).sum(1)-gfn_reward(paths[:,-1])
    bridge_error=float(np.max(abs(gfn_tb(w0,paths)-expected)));assert bridge_error<1e-12
    wgf=[np.array(v) for v in d['gfn']['weights']];p=np.array(d['gfn']['paths']);x=p[:,-1]
    # Direct scalar Gaussian density calculation vs vectorized trained TB residual.
    def loggauss(v,mu,logs):return float(-.5*np.sum(((v-mu)/np.exp(logs))**2+2*logs+np.log(2*np.pi)))
    residual=[]
    for path in p:
        forward=0;backward=0
        for t in range(1,4):
            inp=np.r_[path[t-1],t/3];mu=path[t-1]+np.tanh(inp@wgf[0]+wgf[1])@wgf[2]+wgf[3];forward+=loggauss(path[t],mu,wgf[4][t-1])
            if t>1:backward+=loggauss(path[t-1],path[t]*(t-1)/t,np.log(np.sqrt((t-1)/(3*t))))
        residual.append(float(wgf[5][0]+forward-backward-gfn_reward(path[-1:])[0]))
    density_error=float(np.max(abs(np.array(residual)-gfn_tb(wgf,p))));assert density_error<1e-12
    # Independent F2 matrix-rank Betti1 at every barcode critical midpoint.
    ph=d['analogy']['persistence'];dist=np.array(ph['distance']);n=len(dist);assert persistence(dist)['H1']==ph['H1']
    def rank(matrix):
        a=np.array(matrix,dtype=int)%2;row=0
        for col in range(a.shape[1]):
            pivot=next((i for i in range(row,len(a)) if a[i,col]),None)
            if pivot is None:continue
            a[[row,pivot]]=a[[pivot,row]]
            for i in range(row+1,len(a)):
                if a[i,col]:a[i]^=a[row]
            row+=1
            if row==len(a):break
        return row
    radii=sorted(set(dist[np.triu_indices(n,1)].tolist()));checked=0
    for r in [(a+b)/2 for a,b in zip([0]+radii,radii+[radii[-1]+1])]:
        edges=[e for e in itertools.combinations(range(n),2) if dist[e]<=r];faces=[f for f in itertools.combinations(range(n),3) if all(dist[e]<=r for e in itertools.combinations(f,2))]
        d1=np.zeros((n,len(edges)),int);d2=np.zeros((len(edges),len(faces)),int)
        for j,e in enumerate(edges):d1[list(e),j]=1
        for j,f in enumerate(faces):
            for e in itertools.combinations(f,2):d2[edges.index(e),j]=1
        betti=len(edges)-rank(d1)-rank(d2);bars=sum(b<=r and (end is None or r<end) for b,end in ph['H1']);assert betti==bars;checked+=1
    for q in d['qec']:
        assert abs(q['logical_error']-(3*q['p']**2-2*q['p']**3))<1e-12
        assert abs(sum(s['probability'] for s in q['syndromes'])-1)<1e-12
    sys.path.insert(0,str(ROOT/'examples/architecture'));from trace_schema import validate
    for item in manifest['traces']:
        raw=(directory/item['file']).read_bytes();assert hashlib.sha256(raw).hexdigest()==item['sha256'];trace=json.loads(raw);validate(trace);assert trace['input']['surface_m']==5
    report=dict(passed=True,record_sha256=manifest['sha256'],heldout_metrics=measured,permutation_error=perm_error,bridge_density_identity_error=bridge_error,
        independent_scalar_TB_error=density_error,independent_F2_radius_checks=checked,forest_teacher_checks=len(tree['nodes']),trace_records=len(manifest['traces']),
        scope='Finite program/float checks; no theorem prover, hardware, upstream benchmark, topological phase or GRH proof')
    out=ROOT/'outputs/checks/2026-11-03-actual-rg/quantum-tokengt';out.mkdir(exist_ok=True,parents=True);(out/'independent.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
if __name__=='__main__':main()
