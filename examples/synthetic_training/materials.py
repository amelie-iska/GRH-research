"""Additional Aster effective-model response dataset; CPU only, no crystal claims."""
import argparse,math
from pathlib import Path
import numpy as np
from scipy.special import logsumexp
from common import SEED,fresh,finish,row,write_json,connected_groups,assign_components
BLOCKED_DESIGN=False

def bloch(family,p,n):
    k=np.arange(n)*2*np.pi/n;x,y=np.meshgrid(k,k,indexing='ij')
    if family=='qwz':d=np.stack([np.sin(x),np.sin(y),p['mass']+np.cos(x)+np.cos(y)],-1)
    elif family=='rice_mele_pump':
        a=1+p['dimerization']*np.cos(y);b=1-p['dimerization']*np.cos(y)
        d=np.stack([a+b*np.cos(x),b*np.sin(x),p['stagger']*np.sin(y)],-1)
    else:raise ValueError(family)
    H=np.zeros((*d.shape[:-1],2,2),complex);H[...,0,0]=d[...,2];H[...,1,1]=-d[...,2]
    H[...,0,1]=d[...,0]-1j*d[...,1];H[...,1,0]=H[...,0,1].conj();return H

def chern(H,seed=SEED):
    e,v=np.linalg.eigh(H);u=v[...,0];gap=float(np.min(e[...,1]-e[...,0]));rng=np.random.default_rng(seed)
    def number(u):
        a=np.sum(u.conj()*np.roll(u,-1,0),-1);b=np.sum(u.conj()*np.roll(u,-1,1),-1)
        minimum=float(min(abs(a).min(),abs(b).min()))
        if minimum<1e-9:return None,minimum
        a/=abs(a);b/=abs(b);phase=np.angle(a*np.roll(b,-1,0)/np.roll(a,-1,1)/b)
        return float(phase.sum()/(2*np.pi)),minimum
    value,overlap=number(u);gauge,_=number(u*np.exp(1j*rng.uniform(-np.pi,np.pi,u.shape[:-1]))[...,None])
    err=None if value is None else abs(value-gauge)
    if err is not None:assert err<1e-10
    return dict(value=value,gap=gap,minimum_link_overlap=overlap,gauge_error=err)

def harper(p,n):
    q=p['q'];k=np.arange(n)*2*np.pi/n;x,y=np.meshgrid(k,k,indexing='ij');H=np.zeros((n,n,q,q),complex)
    for j in range(q):H[...,j,j]=2*p['onsite']*np.cos(y+2*np.pi*j/q)
    for j in range(q-1):H[...,j,j+1]=p['hopping'];H[...,j+1,j]=p['hopping']
    H[...,-1,0]=p['hopping']*np.exp(1j*x);H[...,0,-1]=H[...,-1,0].conj();return H

def chain(family,p):
    N=32
    if family=='kitaev':
        h=-p['mu']*np.eye(N)-p['t']*(np.eye(N,k=1)+np.eye(N,k=-1));a=p['delta']*(np.eye(N,k=1)-np.eye(N,k=-1))
        return np.block([[h,a],[-a,-h.T]]).astype(complex)
    if family=='ssh':
        H=np.zeros((N,N),complex)
        for i in range(N-1):H[i,i+1]=H[i+1,i]=p['t1'] if i%2==0 else p['t2']
        return H
    raise ValueError(family)

def make(parent,family,rng):
    p={};topology={};curves={};H=None
    if family=='ssh':
        p=dict(t1=float(rng.uniform(.2,1.8)),t2=float(rng.uniform(.2,1.8)))
        if BLOCKED_DESIGN:p={k:float(rng.choice([.35,.85,1.35,1.75])+rng.uniform(-.025,.025)) for k in ['t1','t2']}
        k=np.linspace(0,2*np.pi,129);q=p['t1']+p['t2']*np.exp(1j*k);gap=2*abs(p['t1']-p['t2'])
        topology=dict(winding=int(round((np.unwrap(np.angle(q))[-1]-np.angle(q[0]))/(2*np.pi))) if gap>.08 else None,gap=gap)
        curves=dict(axis=k.tolist(),bands=[(-abs(q)).tolist(),abs(q).tolist()]);H=chain(family,p)
    elif family=='kitaev':
        p=dict(t=float(rng.uniform(.5,1.5)),delta=float(rng.uniform(.2,1)),mu=float(rng.uniform(-4,4)))
        if BLOCKED_DESIGN:p=dict(t=float(rng.choice([.65,1.2])+rng.uniform(-.015,.015)),delta=float(rng.choice([.3,.7])+rng.uniform(-.015,.015)),mu=float(rng.choice([-1,1])*(rng.choice([.4,1.2,2.4,3.6])+rng.uniform(-.02,.02))))
        k=np.linspace(0,2*np.pi,129);e=np.sqrt((p['mu']+2*p['t']*np.cos(k))**2+(2*p['delta']*np.sin(k))**2)
        gap=2*float(e.min());topology=dict(z2=int(np.sign((p['mu']+2*p['t'])*(p['mu']-2*p['t']))) if gap>.08 else None,gap=gap)
        curves=dict(axis=k.tolist(),bands=[(-e).tolist(),e.tolist()]);H=chain(family,p)
    elif family in ['qwz','rice_mele_pump','harper_photonic']:
        if family=='qwz':p=dict(mass=float(rng.uniform(-3,3)))
        elif family=='rice_mele_pump':p=dict(dimerization=float(rng.uniform(.2,.8)),stagger=float(rng.uniform(.3,1.5)))
        else:p=dict(q=int(rng.choice([3,5])),onsite=float(rng.uniform(.7,1.3)),hopping=float(rng.uniform(.7,1.3)))
        if BLOCKED_DESIGN:
            if family=='qwz':p=dict(mass=float(rng.choice([-2.8,-2.4,-1.75,-1.25,-.75,-.25,0.,.25,.75,1.25,1.75,2.4,2.8])+rng.uniform(-.025,.025)))
            elif family=='rice_mele_pump':p=dict(dimerization=float(rng.choice([.3,.6])+rng.uniform(-.01,.01)),stagger=float(rng.choice([.6,1.2])+rng.uniform(-.015,.015)))
            else:p=dict(q=int(rng.choice([3,5])),onsite=float(rng.choice([.8,1.2])+rng.uniform(-.01,.01)),hopping=float(rng.choice([.8,1.2])+rng.uniform(-.01,.01)))
        factory=(lambda n:harper(p,n)) if family=='harper_photonic' else (lambda n:bloch(family,p,n))
        a,b=chern(factory(32)),chern(factory(64))
        if family=='qwz':gap=2*min(abs(p['mass']+2),abs(p['mass']),abs(p['mass']-2));gap_kind='analytic continuum minimum'
        elif family=='rice_mele_pump':gap=2*min(2*p['dimerization'],p['stagger']);gap_kind='analytic continuum minimum'
        else:
            gap=max(0.,b['gap']-2*np.pi/64*(p['hopping']+2*p['onsite']));gap_kind='conservative mesh Lipschitz lower bound; finite floating arithmetic'
        stable=a['value'] is not None and b['value'] is not None and abs(a['value']-b['value'])<1e-8 and gap>.08
        topology=dict(chern=int(round(b['value'])) if stable else None,mesh_checks=[a,b],orientation='arg(Ux(k)Uy(k+x)/(Ux(k+y)Uy(k))), occupied lowest band',gap=gap,gap_kind=gap_kind,
            evidence='mesh-consistent numerical invariant; analytic/lower-bound gap guard, no interval certificate')
        # Finite open strip at ky=.37; separate from the bulk Brillouin torus.
        N=18;ky=.37
        if family=='harper_photonic':
            H=np.diag([2*p['onsite']*np.cos(ky+2*np.pi*j/p['q']) for j in range(N)]).astype(complex)
            H+=p['hopping']*(np.eye(N,k=1)+np.eye(N,k=-1))
        else:
            sx=np.array([[0,1],[1,0]],complex);sy=np.array([[0,-1j],[1j,0]]);sz=np.diag([1,-1]);I=np.eye(N)
            if family=='qwz':onsite=np.sin(ky)*sy+(p['mass']+np.cos(ky))*sz;hop=(sz-1j*sx)/2
            else:onsite=(1+p['dimerization']*np.cos(ky))*sx+p['stagger']*np.sin(ky)*sz;hop=(1-p['dimerization']*np.cos(ky))*(sx-1j*sy)/2
            H=np.kron(I,onsite)+np.kron(np.eye(N,k=1),hop)+np.kron(np.eye(N,k=-1),hop.conj().T)
        spectrum=np.linalg.eigvalsh(factory(33)[:,0]);curves=dict(axis=(np.arange(33)*2*np.pi/33).tolist(),bands=spectrum.T.tolist())
    else:
        m=int(rng.choice([3,5,9]));p=dict(m=m,genus=(m-1)//2,Jplus=float(rng.uniform(-1.5,1.5)),Jminus=float(rng.uniform(-1.5,1.5)),field=float(rng.uniform(-.5,.5)))
        if BLOCKED_DESIGN:p.update(Jplus=float(rng.choice([-1.,-.4,.4,1.])+rng.uniform(-.01,.01)),Jminus=float(rng.choice([-1.,-.4,.4,1.])+rng.uniform(-.01,.01)),field=float(rng.choice([-.3,.3])+rng.uniform(-.005,.005)))
        bits=(np.arange(2**m)[:,None]>>np.arange(m))&1;t=1-2*bits
        a=p['Jplus']*t.sum(1)+p['field'];b=p['Jminus']*(t*(-1)**np.arange(m)).sum(1)-.6*p['field']
        weights=np.stack([s*a+u*b for s in [-1,1] for u in [-1,1]])
        effective=-logsumexp(weights,axis=0);logZ=float(logsumexp(-effective));prob=np.exp(-effective-logZ)
        topology=dict(surface_genus=p['genus'],not_a_quantum_phase_invariant=True)
        curves=dict(axis=np.arange(2**m).tolist(),effective_action=effective.tolist(),retained_probability=prob.tolist(),log_partition=logZ)
        assert abs(prob.sum()-1)<1e-12
    records=[]
    for variant in ['base','gauge','boundary_defect'] if H is not None else ['base']:
        identity=f'{family}-{parent:04d}-{variant}';group=f'{family}-parent-{parent:04d}'
        conditions=dict(family=family,parameters=p,intervention=variant,boundary='open strip ky=.37 or chain; see payload',units='dimensionless; hbar=1')
        targets=dict(topology=topology,bulk_curve=curves)
        payload=dict(id=identity,conditions=conditions,targets=targets,physical_status='simulated effective model; not a realized material',parent=group)
        if H is not None:
            M=H.copy()
            if variant=='gauge':
                phase=np.exp(1j*rng.uniform(-np.pi,np.pi,len(H)//2 if family=='kitaev' else len(H)))
                if family=='kitaev':phase=np.r_[phase,phase.conj()]
                M=phase[:,None]*M*phase.conj()[None,:]
            elif variant=='boundary_defect':
                if family=='kitaev':
                    N=len(M)//2;M[0,0]+=.15;M[N,N]-=.15;M[N-1,N-1]-=.1;M[2*N-1,2*N-1]+=.1
                else:M[0,0]+=.15;M[-1,-1]-=.1
            e,v=np.linalg.eigh(M);res=float(np.max(abs(M@v-v*e[None,:])));assert res<1e-11
            assert np.max(abs(M-M.conj().T))<1e-12
            if family=='kitaev':
                N=len(M)//2;exchange=np.r_[np.arange(N,2*N),np.arange(N)]
                assert np.max(abs(M.conj()[exchange][:,exchange]+M))<1e-12,'BdG particle-hole symmetry'
            if variant=='gauge':assert np.max(abs(e-np.linalg.eigvalsh(H)))<1e-11
            boundary=[0,1,len(M)-2,len(M)-1]
            if family=='kitaev':
                N=len(M)//2;boundary=[0,1,N-2,N-1,N,N+1,2*N-2,2*N-1]
            targets.update(open_spectrum=e.tolist(),edge_weight=(abs(v[boundary])**2).sum(0).tolist())
            payload.update(targets=targets,hamiltonian_real=M.real.tolist(),hamiltonian_imag=M.imag.tolist(),eigen_residual=res,
                bulk_boundary_scope='Defect changes only finite open matrix; bulk invariant refers to unchanged bulk Hamiltonian. Gauge variant is unitary conjugation of finite matrix, including BdG basis change.')
        records.append(row(identity,family,group,conditions,targets,payload))
    return records

def generate(out,parents):
    out=fresh(out);rng=np.random.default_rng(SEED);rows=[]
    for family in ['ssh','kitaev','qwz','rice_mele_pump','harper_photonic','dessin_classical_rg']:
        for parent in range(parents):rows+=make(parent,family,rng)
    representatives=[r for r in rows if r['record_id'].endswith('-base')];profiles=[]
    for r in representatives:
        c=__import__('json').loads(r['condition_json']);p=c['parameters'];f=c['family']
        if f=='ssh':vec=np.sort([p['t1']/2,p['t2']/2]);categorical=0
        elif f=='kitaev':vec=np.array([p['t']/2,p['delta'],abs(p['mu'])/4]);categorical=0
        elif f=='qwz':vec=np.array([p['mass']/6]);categorical=0
        elif f=='rice_mele_pump':vec=np.array([p['dimerization'],p['stagger']/2]);categorical=0
        elif f=='harper_photonic':vec=np.array([p['hopping']/2,p['onsite']/2]);categorical=p['q']
        else:
            vec=np.array([p['Jplus']/3,p['Jminus']/3,p['field']]);vec=vec if tuple(vec)<tuple(-vec) else -vec;categorical=p['m']
        payload=__import__('json').loads(r['payload_json']);spectrum=np.array(payload['targets'].get('open_spectrum',payload['targets']['bulk_curve'].get('effective_action',[])))
        profiles.append(dict(family=f,vector=vec,category=categorical,spectrum=spectrum))
    def similar(a,b):
        if a['family']!=b['family'] or a['category']!=b['category']:return None
        threshold=.012 if a['family']=='qwz' else .06
        d=float(np.linalg.norm(a['vector']-b['vector']))
        if d<=threshold:return 'normalized_parameter_distance'
        x,y=a['spectrum'],b['spectrum']
        if len(x) and len(x)==len(y) and np.linalg.norm(x-y)/max(np.linalg.norm(x),np.linalg.norm(y),1e-12)<.012:return 'relative_finite_spectrum_distance'
        return None
    components,edges=connected_groups(profiles,similar)
    mapping={r['group_id']:f'material-component-{components[i]:04d}' for i,r in enumerate(representatives)}
    audit=assign_components(rows,mapping)
    assert all(components[i]==components[j] for i,j,_ in edges)
    write_json(out/'split-audit.json',dict(**audit,similarity_edges=len(edges),cross_split_similarity_edges=0,
        thresholds={'qwz_normalized_parameter_L2':.012,'other_family_parameter_L2':.06,'relative_open_spectrum_L2':.012},
        graph_scope='Same Hamiltonian family and discrete q/m; SSH hopping swap and Kitaev mu-sign are conservatively folded. All gauge/defect/desired-task descendants stay together.',
        limitation='No universal unseen-physics or overfitting guarantee; phase stratification and leave-family-out are separate evaluations'))
    report=dict(passed=True,families=6,parents_per_family=parents,computed_label_policy='finite effective-model calculations; unresolved invariant=null',
        training_claim='No Aster changes or admission; candidate supplemental source',parameter_proposal='Separated parameter blocks with disclosed bounded jitter' if BLOCKED_DESIGN else 'Uniform bounded pilot proposal',checks=['Hermiticity','eigen residual<1e-11','32/64 mesh comparison with continuum gap guard','random gauge invariance','BdG particle-hole symmetry','RG normalization'],
        units='dimensionless; no eV, kelvin or experimental calibration inferred',out_of_family_policy='Use family column for separate leave-one-family-out study; default split is parent-heldout')
    finish(out,rows,report,'Additional topological Hamiltonian response/intervention atlas for Aster')
    print({'records':len(rows),'output':str(out)})
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output',required=True,type=Path);p.add_argument('--parents',type=int,default=96);p.add_argument('--blocked-design',action='store_true');a=p.parse_args();BLOCKED_DESIGN=a.blocked_design;generate(a.output,a.parents)
