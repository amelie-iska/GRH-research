"""Execute finite hybrid experiments; immutable named output generation."""
import argparse,hashlib,json,platform,time
from pathlib import Path
import numpy as np
import autograd.numpy as anp
from autograd import grad
from autograd.misc.flatten import flatten
from scipy.special import logsumexp
from model import *

def adam(objective,initial,steps,lr,rng,batch_builder,record_every=1):
    flat,unflatten=flatten(initial);m=np.zeros_like(flat);v=m.copy();history=[]
    gfun=grad(lambda w,b:objective(unflatten(w),b))
    for t in range(1,steps+1):
        batch=batch_builder(rng,t);loss=float(objective(unflatten(flat),batch));g=np.asarray(gfun(flat,batch))
        if not np.isfinite(loss) or not np.all(np.isfinite(g)):raise ValueError('nonfinite training')
        m=.9*m+.1*g;v=.999*v+.001*g*g;flat-=lr*m/(1-.9**t)/(np.sqrt(v/(1-.999**t))+1e-8)
        if t==1 or t%record_every==0 or t==steps:history.append(dict(step=t,loss=loss,gradient_norm=float(np.linalg.norm(g))))
    return unflatten(flat),history

def init_model(rng):
    return [rng.normal(0,.25,(6,6)) for _ in range(3)]+[rng.normal(0,.25,(6,24)),np.zeros(24),rng.normal(0,.12,(24,32)),np.zeros(32)]
def predict(w,x,mask,mode):
    z=attention(x,w,mask,mode);return anp.dot(anp.tanh(anp.dot(z,w[3])+w[4]),w[5])+w[6]
def metrics(y,a):
    lz=logsumexp(a,axis=1);truth=logsumexp(y,axis=1);p=np.exp(a-lz[:,None]);q=np.exp(y-truth[:,None])
    return dict(logweight_rmse=float(np.sqrt(np.mean((a-y)**2))),logZ_rmse=float(np.sqrt(np.mean((lz-truth)**2))),
        retained_magnetization_rmse=float(np.sqrt(np.mean(((p-q)@spins(5))**2))),mean_TV=float(.5*np.abs(p-q).sum(1).mean()),
        identity_coefficient_rmse=float(np.sqrt(np.mean((a.mean(1)-y.mean(1))**2))))

def train_models(data,steps,rng):
    p=np.asarray(data['parameters']);po=np.asarray(data['ood_parameters']);tr=np.array(data['train']);te=np.array(data['test'])
    y=np.stack([teacher(v)[:32] for v in p]);yo=np.stack([teacher(v)[:32] for v in po])
    np.testing.assert_allclose(y,np.asarray(data['targets']),atol=1e-12)
    angles,mask,ids=graph_tokens(np.r_[p,po]);f,states=circuit_features(angles,True);classical=classical_features(angles)
    mean=y[tr].mean(0);scale=np.maximum(y[tr].std(0),.1);ys=(y-mean)/scale
    models={};weights={};init=init_model(np.random.default_rng(SEED+1))
    for name,mode,features in [('quantum-softmax','softmax',f),('quantum-tropical','tropical',f),('quantum-hybrid','hybrid',f),('classical-hybrid','hybrid',classical)]:
        obj=lambda w,b:anp.mean((predict(w,features[b],mask,mode)-ys[b])**2)+1e-5*sum(anp.sum(a*a) for a in w)
        w,h=adam(obj,[a.copy() for a in init],steps,.008,np.random.default_rng(SEED+2),lambda r,t:r.choice(tr,min(48,len(tr)),replace=False))
        pred=np.asarray(predict(w,features,mask,mode))*scale+mean
        models[name]=dict(mode=mode,history=h,train=metrics(y[tr],pred[tr]),heldout=metrics(y[te],pred[te]),ood=metrics(yo,pred[len(p):]),
            parameter_count=sum(a.size for a in w),initial_full_train_loss=float(obj(init,tr)),final_full_train_loss=float(obj(w,tr)))
        weights[name]=w;print(name,models[name]['heldout'],flush=True)
    w=weights['quantum-hybrid'];z=np.asarray(attention(f[:len(p)],w,mask,'hybrid'))
    tracez,trace=attention(f[te[:1]],w,mask,'hybrid',True)
    trace={k:np.asarray(v).tolist() for k,v in trace.items()}
    # Physical decoder from pooled learned embeddings; fixed after training.
    zm=z[tr].mean(0);zs=np.maximum(z[tr].std(0),.01);zn=(z-zm)/zs
    design=np.c_[zn[tr],np.ones(len(tr))];decoder=np.linalg.solve(design.T@design+.003*np.eye(7),design.T@p[tr])
    return dict(models=models,weights=weights,features=f,angles=angles,mask=mask,ids=ids,z=zn,zmean=zm,zscale=zs,decoder=decoder,
        trace=dict(sample_index=int(te[0]),parameters=p[te[0]].tolist(),angles=angles[te[0]].tolist(),features=f[te[0]].tolist(),
            state_real=states[te[0]].real.tolist(),state_imag=states[te[0]].imag.tolist(),pooled=tracez.tolist(),**trace),mean=mean,scale=scale)

def learn_concepts(bundle,data,rng):
    z=bundle['z'];tr=np.array(data['train']);te=np.array(data['test']);d=z.shape[1];classes=6
    initial=[rng.normal(0,.4,(3,d)),rng.normal(0,.2,(d,classes))]
    def losses(w,b):
        B,C=w;B=B/anp.sqrt(anp.sum(B*B,axis=1,keepdims=True)+1e-10)
        base,labels=b;direction=labels//2;sign=2*(labels%2)-1
        delta=anp.tanh(.3*base+.7*B[direction]*sign[:,None])-anp.tanh(.3*base)
        logits=anp.dot(delta,C)/.2;lp=logits-anp.log(anp.sum(anp.exp(logits-anp.max(logits,axis=1,keepdims=True)),axis=1,keepdims=True))-anp.max(logits,axis=1,keepdims=True)
        ce=-anp.mean(lp[anp.arange(len(labels)),labels]);gram=anp.dot(B,B.T)
        return ce+.08*anp.sum((gram-anp.eye(3))**2)
    def batch(r,t):return z[r.choice(tr,96,replace=True)],r.integers(0,classes,96)
    w,h=adam(losses,initial,600,.012,rng,batch);B=w[0]/np.linalg.norm(w[0],axis=1,keepdims=True)
    # Heldout classifier cross entropy without the decorrelation penalty.
    base=np.repeat(z[te],classes,axis=0);labels=np.tile(np.arange(classes),len(te));sign=2*(labels%2)-1
    delta=np.tanh(.3*base+.7*B[labels//2]*sign[:,None])-np.tanh(.3*base);logits=delta@w[1]/.2
    ce=float(np.mean(logsumexp(logits,axis=1)-logits[np.arange(len(labels)),labels]))
    decoder=bundle['decoder'];base=z[te[0]];points=[]
    for k in range(3):
        for a in np.linspace(-1,1,9):
            latent=base+a*B[k];params=np.clip(np.r_[latent,1]@decoder,[.15,.15,-.6],[1.1,1.1,.6]);t=teacher(params)
            points.append(dict(direction=k,amount=float(a),embedding=latent.tolist(),parameters=params.tolist(),logZ=float(t[32]),magnetization=t[33:].tolist()))
    return dict(basis=B.tolist(),critic=w[1].tolist(),history=h,heldout_cross_entropy=ce,heldout_InfoNCE_lower_bound_nats=float(np.log(classes)-ce),
        code='C uniform over direction x sign (6 values); Delta=tanh(.3 z+.7 sign B_direction)-tanh(.3z)',
        objective='categorical InfoNCE cross entropy + .08 ||BB^T-I||_F^2; log(6)-CE lower bound for sampled C,Delta distribution',
        gram=(B@B.T).tolist(),steering=points)

def analogies(bundle,data):
    # Learn a single A->B embedding displacement from train pairs; transfer to heldout bases.
    params=np.asarray(data['parameters']);tr=np.array(data['train']);te=np.array(data['test']);change=np.array([.07,-.04,.06])
    shifted=np.clip(params+change,[.15,.15,-.6],[1.1,1.1,.6]);a,mask,_=graph_tokens(shifted)
    zshift=(np.asarray(attention(circuit_features(a),bundle['weights']['quantum-hybrid'],mask,'hybrid'))-bundle['zmean'])/bundle['zscale']
    displacement=(zshift[tr]-bundle['z'][tr]).mean(0);estimate=np.c_[bundle['z'][te]+displacement,np.ones(len(te))]@bundle['decoder']
    raw=np.c_[bundle['z'][te],np.ones(len(te))]@bundle['decoder'];estimate=np.clip(estimate,[.15,.15,-.6],[1.1,1.1,.6]);raw=np.clip(raw,[.15,.15,-.6],[1.1,1.1,.6])
    truth=np.stack([teacher(v) for v in shifted[te]]);pred=np.stack([teacher(v) for v in estimate]);base=np.stack([teacher(v) for v in raw])
    # Actual finite PH of 12 heldout learned embedding points, not a physical phase invariant.
    points=bundle['z'][te[:12]];distance=np.linalg.norm(points[:,None]-points[None,:],axis=-1)
    return dict(transformation=change.tolist(),train_pairs=len(tr),heldout_pairs=len(te),learned_displacement=displacement.tolist(),
        parameter_rmse=float(np.sqrt(np.mean((estimate-shifted[te])**2))),
        heldout_transferred=metrics(truth[:,:32],pred[:,:32]),no_transfer_control=metrics(truth[:,:32],base[:,:32]),
        example=dict(base_parameters=params[te[0]].tolist(),target_parameters=shifted[te[0]].tolist(),predicted_parameters=estimate[0].tolist(),target_observables=truth[0,32:].tolist(),predicted_observables=pred[0,32:].tolist()),
        persistence=dict(points=points.tolist(),distance=distance.tolist(),**persistence(distance)),
        physical_observable_topology=observable_topology(truth[:12,32:],pred[:12,32:]))

def observable_topology(target,predicted):
    """Compare actual RG observable point-cloud geometry after analogy transfer."""
    scales=np.array([3,.25,.25,.25,.25,.25]);a=target/scales;b=predicted/scales
    da=np.linalg.norm(a[:,None]-a[None,:],axis=-1);db=np.linalg.norm(b[:,None]-b[None,:],axis=-1)
    return dict(target_points=a.tolist(),predicted_points=b.tolist(),coordinate_scales=scales.tolist(),
        target=persistence(da),predicted=persistence(db),pairwise_distance_rmse=float(np.sqrt(np.mean((da-db)**2))),
        scope='Rips barcodes of exact physical observables at12 target and decoded transferred parameterpoints; no proven analogy invariant or topologicalphase')

def forest(bundle,concepts,data):
    B=np.asarray(concepts['basis']);decoder=bundle['decoder'];target=teacher([.82,.37,.3])[32:];root=bundle['z'][data['test'][0]]
    def evaluate(z):
        params=np.clip(np.r_[z,1]@decoder,[.15,.15,-.6],[1.1,1.1,.6]);obs=teacher(params)[32:]
        error=np.mean(((obs-target)/np.array([3,.25,.25,.25,.25,.25]))**2)
        return params,obs,float(-error)
    nodes=[];p,o,r=evaluate(root);nodes.append(dict(id=0,parent=None,depth=0,embedding=root.tolist(),parameters=p.tolist(),observables=o.tolist(),reward=r));beam=[0]
    for depth in range(1,5):
        candidates=[]
        for parent in beam:
            for k in range(3):
                for sign in [-1,1]:
                    z=np.array(nodes[parent]['embedding'])+sign*(.45/depth)*B[k];p,o,r=evaluate(z);idx=len(nodes)
                    nodes.append(dict(id=idx,parent=parent,depth=depth,direction=k,sign=sign,embedding=z.tolist(),parameters=p.tolist(),observables=o.tolist(),reward=r));candidates.append(idx)
        beam=sorted(candidates,key=lambda i:nodes[i]['reward'],reverse=True)[:3]
    best=max(range(len(nodes)),key=lambda i:nodes[i]['reward']);path=[];i=best
    while i is not None:path.append(i);i=nodes[i]['parent']
    return dict(nodes=nodes,best=best,path=path[::-1],beam_width=3,depth=4,target_observables=target.tolist(),
        scope='Finite branching latent candidate optimization with exact physical RG observable reward; no natural-language or human-reasoning claim')

# Continuous GFN: time-expanded R2 state space, delta root, all other measures Lebesgue.
def gfn_reward(x):
    p0=.62+.35*anp.tanh(x[:,0]);p1=.58+.34*anp.tanh(x[:,1]);b=.12;s=spins(5);eta=(-1.)**np.arange(5)
    a=anp.logaddexp(b+p0[:,None]*s.sum(1),-b-p0[:,None]*s.sum(1))+anp.logaddexp(-.6*b+p1[:,None]*(s@eta),.6*b-p1[:,None]*(s@eta))+s@white_fields(5)
    m=anp.max(a,axis=1);logz=m+anp.log(anp.sum(anp.exp(a-m[:,None]),axis=1))
    return -.5*anp.sum(x*x,axis=1)+.35*(logz-7.)
def gaussian_log(x,mu,logs):return -.5*anp.sum(((x-mu)/anp.exp(logs))**2+2*logs+anp.log(2*anp.pi),axis=-1)
def gfn_mu(w,x,t):
    inp=anp.concatenate([x,anp.ones((len(x),1))*t/3],axis=1)
    return x+anp.dot(anp.tanh(anp.dot(inp,w[0])+w[1]),w[2])+w[3]
def gfn_tb(w,paths):
    forward=0.;backward=0.
    for t in range(1,4):
        forward=forward+gaussian_log(paths[:,t],gfn_mu(w,paths[:,t-1],t),w[4][t-1])
        if t>1:backward=backward+gaussian_log(paths[:,t-1],paths[:,t]*(t-1)/t,np.log(np.sqrt((t-1)/(3*t))))
    return w[5][0]+forward-backward-gfn_reward(paths[:,-1])
def gfn_sample(w,rng,n):
    paths=np.zeros((n,4,2))
    for t in range(1,4):paths[:,t]=gfn_mu(w,paths[:,t-1],t)+np.exp(w[4][t-1])*rng.normal(size=(n,2))
    return paths

def train_gfn(rng):
    w=[rng.normal(0,.08,(3,16)),np.zeros(16),rng.normal(0,.08,(16,2)),np.zeros(2),np.full((3,2),np.log(1/np.sqrt(3))),np.array([1.8])]
    initial=[v.copy() for v in w]
    # Fixed proposal training trajectories ensure objective gradients include density terms, not sampling gradients.
    pool=gfn_sample(initial,rng,10000)
    objective=lambda w,p:anp.mean(gfn_tb(w,p)**2)
    w,h=adam(objective,w,1800,.006,rng,lambda r,t:pool[r.integers(0,len(pool),192)],record_every=1)
    heldout_proposal=gfn_sample(initial,rng,3000);sample=gfn_sample(w,rng,10000);endpoint=sample[:,-1]
    # Deterministic finite quadrature is verification only; training and sampling are continuous.
    grid=np.linspace(-5,5,201);xx,yy=np.meshgrid(grid,grid);pts=np.c_[xx.ravel(),yy.ravel()];lr=np.asarray(gfn_reward(pts));weight=np.exp(lr)*(.05**2)
    z=float(weight.sum());mean=weight@pts/z;second=(weight[:,None]*pts**2).sum(0)/z
    bins=np.linspace(-5,5,21);hist=np.histogram2d(*endpoint.T,bins=[bins,bins])[0]/len(endpoint)
    centers=(bins[:-1]+bins[1:])/2;gx,gy=np.meshgrid(centers,centers,indexing='ij');q=np.exp(np.asarray(gfn_reward(np.c_[gx.ravel(),gy.ravel()]))).reshape(20,20);q/=q.sum()
    return dict(weights=[v.tolist() for v in w],history=h,steps=1800,horizon=3,dimensions=2,
        root_measure='delta_(0,0) at time 0; Lebesgue dx at times 1,2,3; termination deterministically at time3',
        backward='for t=2,3: N(x_(t-1); ((t-1)/t)x_t, ((t-1)/(3t)) I); t=1: unit point mass on root',
        forward='N(x_t; x_(t-1)+MLP(x_(t-1),t), diag(exp(2 log_sigma_t)))',
        reward='R(x)=exp(-||x||²/2 + .35(logZ_K2,5(.62+.35tanh x0,.58+.34tanh x1,.12)-7)); bounded logZ term makes integrable',
        objective='mean(logZ_parameter + sum logPF - sum logPB - logR)^2; 10000 fixed off-policy Gaussian trajectories, fresh heldout proposal and onpolicy evaluation',
        initial_heldout_TB_mse=float(np.mean(gfn_tb(initial,heldout_proposal)**2)),heldout_TB_mse=float(np.mean(gfn_tb(w,heldout_proposal)**2)),
        onpolicy_TB_mse=float(np.mean(gfn_tb(w,sample)**2)),learned_logZ=float(w[5][0]),quadrature_logZ=float(np.log(z)),
        quadrature=dict(bounds=[-5,5],spacing=.05,points=201**2,mean=mean.tolist(),second_moment=second.tolist(),scope='finite box approximation, tails omitted'),
        sample_mean=endpoint.mean(0).tolist(),sample_second_moment=(endpoint**2).mean(0).tolist(),histogram_TV_to_midpoint_quadrature=float(.5*np.abs(hist-q).sum()),
        samples_outside_box=int(np.sum(np.max(abs(endpoint),axis=1)>5)),sample_count=len(endpoint),paths=sample[:30].tolist(),sample_endpoints=endpoint[:700].tolist())

def serial(x):
    if isinstance(x,np.ndarray):return x.tolist()
    if isinstance(x,np.generic):return x.item()
    if isinstance(x,dict):return {k:serial(v) for k,v in x.items()}
    if isinstance(x,(tuple,list)):return [serial(v) for v in x]
    return x

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--run',default='run-20261103-v1');parser.add_argument('--steps',type=int,default=900);args=parser.parse_args()
    out=ROOT/'outputs/experiments/quantum-tokengt'/args.run;out.mkdir(exist_ok=False)
    start=time.time();rng=np.random.default_rng(SEED);path=ROOT/'outputs/experiments/actual-rg/dataset.json';data=json.loads(path.read_text())
    bundle=train_models(data,args.steps,rng)
    (out/'trained-models.json').write_text(json.dumps(serial(bundle),separators=(',',':'),allow_nan=False))
    concepts=learn_concepts(bundle,data,rng);analogy=analogies(bundle,data);tree=forest(bundle,concepts,data);gfn=train_gfn(rng)
    fixture=load_fixture();thetaangles=theta_token_angles(fixture);thetafeatures,thetastates=circuit_features(thetaangles,True)
    record=dict(schema=1,seed=SEED,source_hashes={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in [Path(__file__),Path(__file__).with_name('model.py'),ROOT/'examples/rg/rg_math.py']},versions=dict(python=platform.python_version(),numpy=np.__version__,pennylane=qml.__version__),
        dataset=dict(path=str(path.relative_to(ROOT)),sha256=hashlib.sha256(path.read_bytes()).hexdigest(),train=data['train'],test=data['test'],ood_count=len(data['ood_parameters'])),
        training=dict(steps=args.steps,optimizer='Adam',learning_rate=.008,batch_size=48,target='all32 exact m5 coarse logweights, constant retained; derived observables only at evaluation',
            quantum_feature_parameters='fixed RY(input), RZ(.23(q+1)), CNOT01,CNOT12,RX(.19(q+1)); exact simulator expectations; classical QKV and MLP trained',
            shared_initialization=True,shared_batches=True,head_hidden=24),models=bundle['models'],weights=bundle['weights'],
        normalization=dict(mean=bundle['mean'],scale=bundle['scale'],zmean=bundle['zmean'],zscale=bundle['zscale'],decoder=bundle['decoder']),
        physical_graph=dict(m=5,genus=2,spin_nodes=7,incidence_edges=10,quiver_vertices=5,token_count=18,valid_tokens=17,mask=bundle['mask'],identifiers=bundle['ids'],
            scope='Physical incidence graph K2,5 from clean dessin; 7 spin nodes are distinct from 5 order quiver vertices; metadata transported with tokens'),
        theta_reference=dict(**fixture,angles=thetaangles,features=thetafeatures,state_real=thetastates.real,state_imag=thetastates.imag,
            scope='Separate read-only original elliptic theta miniature demonstration; not the physical m5 RG input graph or a faithful surface-order representation'),
        trace=bundle['trace'],concepts=concepts,analogy=analogy,forest=tree,gfn=gfn,qec=[qec_channel(p) for p in [0,.01,.03,.05,.1,.15,.2,.3,.4,.5]],
        boundaries=['No quantum advantage or upstream TokenGT/GraphCG training claimed','Frozen finite quantum features and classical learned attention; no coherent quantum attention',
            'Embedding persistent homology is not topological order','Contrastive intervention-code recoverability does not establish semantic disentanglement','Forest candidates are finite optimization, not human reasoning','Repetition code protects independent X errors only; no phase protection or universal fault tolerance',
            'No arithmetic GRH proof, faithful completed-order representation, Fukaya/HMS equivalence, materials discovery or GPU/nonGaussian execution'],elapsed_seconds=time.time()-start)
    payload=json.dumps(serial(record),separators=(',',':'),allow_nan=False).encode();(out/'record.json').write_bytes(payload)
    digest=hashlib.sha256(payload).hexdigest();web=ROOT/'web/data/quantum-tokengt';name=f'record-{digest[:16]}.json';(web/name).write_bytes(payload)
    manifest=dict(file=name,sha256=digest,run=str(out.relative_to(ROOT)),seed=SEED);(web/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
    (out/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n');print(json.dumps(dict(manifest=manifest,elapsed=record['elapsed_seconds'],gfn={k:gfn[k] for k in ['heldout_TB_mse','onpolicy_TB_mse','histogram_TV_to_midpoint_quadrature']})),flush=True)
if __name__=='__main__':main()
