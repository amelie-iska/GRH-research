"""Finite quantum-feature TokenGT and exact diagnostics. No training at import."""
from pathlib import Path
import hashlib,itertools,json,sys
import numpy as np
import autograd.numpy as anp
from scipy.special import logsumexp
import pennylane as qml
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'examples/rg'))
from rg_math import black_decimation,spins,white_fields
SEED=20261103

def teacher(params):
    a=black_decimation(5,params);lz=logsumexp(a);p=np.exp(a-lz)
    return np.r_[a,lz,p@spins(5)]

def load_fixture():
    manifest=json.loads((ROOT/'web/data/architecture/manifest.json').read_text())
    item=next(v for v in manifest['traces'] if v['id']=='tokengt-softmax')
    path=ROOT/'web/data/architecture'/item['file'];raw=path.read_bytes()
    assert hashlib.sha256(raw).hexdigest()==item['sha256']
    record=json.loads(raw);nodes={v['id']:v for v in record['nodes']}
    return dict(path=str(path.relative_to(ROOT)),sha256=item['sha256'],surface_context=record['surface_context'],
        mask=np.array(nodes['token_mask']['tensor']['values'],bool).reshape(-1).tolist(),
        node_features=nodes['node_features']['tensor']['values'],edge_features=nodes['edge_features']['tensor']['values'],
        endpoints=nodes['endpoints']['tensor']['values'])


def theta_token_angles(fixture):
    """Encode the literal read-only theta node/edge features and identifiers."""
    nodes=np.asarray(fixture['node_features']).reshape(4,2);edges=np.asarray(fixture['edge_features']).reshape(3)
    endpoints=np.asarray(fixture['endpoints']);a=np.zeros((7,3));a[:4,:2]=nodes;a[:4,2]=.13*np.arange(4)
    for j,(u,v) in enumerate(endpoints):a[4+j]=[edges[j],.17*(u+1),.17*(v+1)+.3]
    a[3]=0
    return a

DEVICE=qml.device('default.qubit',wires=3)
@qml.qnode(DEVICE)
def _circuit(angles):
    for q in range(3):qml.RY(angles[q],wires=q);qml.RZ(.23*(q+1),wires=q)
    qml.CNOT(wires=[0,1]);qml.CNOT(wires=[1,2])
    for q in range(3):qml.RX(.19*(q+1),wires=q)
    return qml.state()
Z=spins(3)
# Three Z and three nearest/all pair correlations are measurable features.
OBS=np.column_stack([Z,Z[:,0]*Z[:,1],Z[:,1]*Z[:,2],Z[:,0]*Z[:,2]])

def circuit_features(angles,states=False):
    a=np.asarray(angles);flat=a.reshape(-1,3);psi=np.stack([np.asarray(_circuit(v)) for v in flat])
    features=(abs(psi)**2)@OBS
    f=features.reshape(*a.shape[:-1],6);s=psi.reshape(*a.shape[:-1],8)
    return (f,s) if states else f

def graph_tokens(params):
    """7 physical spin nodes, 10 incidence edges, 1 masked pad. Not quiver vertices."""
    p=np.atleast_2d(params);batch=len(p);ids=[];meta=[]
    for i in range(7):
        ids.append(dict(kind='physical-node',id=i,endpoints=[i,i]));meta.append([.12*i,.09*i,-.11*i])
    for b in range(2):
        for j in range(5):
            ids.append(dict(kind='physical-edge',id=5*b+j,endpoints=[b,2+j]));meta.append([.18*(j+1),.3*b,.07*(b+2+j)])
    ids.append(dict(kind='padding',id=-1,endpoints=[-1,-1]));meta.append([0,0,0])
    a=np.broadcast_to(np.array(meta),(batch,18,3)).copy()
    # Global controls accompany explicit local field/coupling attributes.
    mix=np.array([[.72,.15,-.21],[.18,.64,.27],[.25,-.16,.81]])
    a+= (p@mix)[:,None,:]
    a[:,0,2]+=p[:,2];a[:,1,2]-=.6*p[:,2]
    for j in range(5):a[:,2+j,2]+=white_fields(5)[j]
    a[:,7:12,0]+=p[:,0,None];a[:,12:17,0]+=p[:,1,None]*((-1.)**np.arange(5))
    mask=np.array([True]*17+[False]);a[:,17]=0
    return a,mask,ids

def classical_features(angles):
    # Matched six local trigonometric features; no entanglers, no simulator.
    return np.concatenate([np.sin(angles),np.cos(angles)],axis=-1)

def attention(x,w,mask,mode='hybrid',details=False):
    q,k,v=[anp.dot(x,a) for a in w[:3]];scores=anp.einsum('bid,bjd->bij',q,k)/anp.sqrt(q.shape[-1])
    legal=mask[None,:,None]&mask[None,None,:]
    s=anp.where(legal,scores,-1e6);e=anp.exp(s-anp.max(s,axis=-1,keepdims=True))*legal
    weights=e/anp.maximum(anp.sum(e,axis=-1,keepdims=True),1e-20)
    soft=anp.einsum('bij,bjd->bid',weights,v)
    terms=scores[:,:,:,None]+v[:,None,:,:];trop=anp.max(anp.where(legal[:,:,:,None],terms,-1e6),axis=2)
    trop=anp.where(mask[None,:,None]&anp.any(mask),trop,0)
    context=soft if mode=='softmax' else trop if mode=='tropical' else .5*(soft+trop)
    pooled=anp.sum(anp.tanh(context+x)*mask[None,:,None],axis=1)/anp.maximum(anp.sum(mask),1)
    if details:return pooled,dict(query=q,key=k,value=v,scores=scores,weights=weights,context=context,legal=legal,
        winners=(terms==trop[:,:,None,:])&legal[:,:,:,None])
    return pooled

def persistence(distance):
    """Full Vietoris–Rips 2-skeleton, standard column reduction over F2."""
    d=np.asarray(distance);n=len(d);simplices=[(0.,(i,)) for i in range(n)]
    for size in [2,3]:
        simplices += [(max(d[i,j] for i,j in itertools.combinations(c,2)),c) for c in itertools.combinations(range(n),size)]
    simplices.sort(key=lambda v:(v[0],len(v[1]),v[1]));index={s:i for i,(_,s) in enumerate(simplices)}
    reduced={};pivot={};births=[];pairs=[]
    for j,(birth,s) in enumerate(simplices):
        col=0
        if len(s)>1:
            for face in itertools.combinations(s,len(s)-1):col^=1<<index[face]
        while col and col.bit_length()-1 in pivot:col^=reduced[pivot[col.bit_length()-1]]
        reduced[j]=col
        if col:
            low=col.bit_length()-1;pivot[low]=j;pairs.append((low,j))
        else:births.append(j)
    paired={a for a,b in pairs};bars={f'H{k}':[] for k in [0,1]}
    for i,j in pairs:
        degree=len(simplices[i][1])-1
        if degree<2 and simplices[j][0]-simplices[i][0]>1e-12:bars[f'H{degree}'].append([float(simplices[i][0]),float(simplices[j][0])])
    for i in births:
        degree=len(simplices[i][1])-1
        if degree<2 and i not in paired:bars[f'H{degree}'].append([float(simplices[i][0]),None])
    return dict(**bars,point_count=n,simplices=len(simplices),field='F2',filtration='max pairwise distance; all triangles; zero bars omitted')

def qec_channel(p):
    """Bell-reference entanglement fidelity of actual 3-qubit bit-flip code."""
    device=qml.device('default.mixed',wires=4)
    @qml.qnode(device)
    def noisy():
        qml.Hadamard(0);qml.CNOT([0,1]);qml.CNOT([1,2]);qml.CNOT([1,3])
        for q in [1,2,3]:qml.BitFlip(p,wires=q)
        return qml.density_matrix([0,1,2,3])
    sdk=np.asarray(noisy());psi=np.zeros(16);psi[[0,15]]=1/np.sqrt(2);reference=np.zeros((16,16),complex)
    for errors in itertools.product([0,1],repeat=3):
        weight=np.prod([p if e else 1-p for e in errors]);flip=sum(e<<(2-q) for q,e in enumerate(errors))
        s=psi[np.arange(16)^flip];reference+=weight*np.outer(s,s)
    corrected=np.zeros_like(sdk);syndromes=[]
    bits=((np.arange(16)[:,None]>>np.arange(3,-1,-1))&1)
    for s1,s2 in itertools.product([0,1],repeat=2):
        keep=((bits[:,1]^bits[:,2])==s1)&((bits[:,2]^bits[:,3])==s2)
        block=sdk*keep[:,None]*keep[None,:];prob=float(np.trace(block).real)
        correction={(0,0):0,(1,0):4,(1,1):2,(0,1):1}[s1,s2]
        perm=np.arange(16)^correction;corrected+=block[perm][:,perm]
        syndromes.append(dict(syndrome=[s1,s2],probability=prob,correct_data_qubit={0:None,4:0,2:1,1:2}[correction]))
    # Decode CNOT(data0,data1), CNOT(data0,data2), then trace auxiliary bits.
    perm=np.arange(16)^np.where(bits[:,1],3,0);decoded=corrected[perm][:,perm]
    logical=np.trace(decoded.reshape(4,4,4,4),axis1=1,axis2=3)
    bell=np.array([1,0,0,1])/np.sqrt(2);f=float(np.vdot(bell,logical@bell).real)
    return dict(p=p,logical_error=1-f,entanglement_fidelity=f,unencoded_fidelity=1-p,syndromes=syndromes,
        sdk_density_error=float(np.max(abs(sdk-reference))),logical_density_real=logical.real.tolist(),logical_density_imag=logical.imag.tolist())
