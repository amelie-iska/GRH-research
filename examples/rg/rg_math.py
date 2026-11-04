"""Exact finite RG definitions; floating-point evaluation is separately checked.

Actions are dimensionless log Boltzmann weights. Keep their constant! Spins
are ordered black0,black1,white0,...; qubit0 is most significant. The clean
dessin incidence graph is distinct from its quiver and completed algebra.
"""
import itertools
import math
import numpy as np
from scipy.special import logsumexp

def spins(n):
    return 1-2*((np.arange(2**n)[:,None]>>np.arange(n-1,-1,-1))&1)

def cycles(p):
    left=set(range(len(p)));result=[]
    while left:
        a=min(left);c=[]
        while a in left:left.remove(a);c.append(a);a=p[a]
        result.append(c)
    return result

def dessin(m):
    assert m>=3 and m%2==1
    sigma=[(i+1)%m if i<m else m+(i-m+1)%m for i in range(2*m)]
    alpha=[(i+m)%(2*m) for i in range(2*m)]
    inv=[sigma.index(i) for i in range(2*m)]
    phi=[alpha[inv[i]] for i in range(2*m)]
    faces=cycles(phi);genus=(2-len(cycles(sigma))+m-len(faces))//2
    assert len(faces)==1 and genus==(m-1)//2
    return dict(m=m,genus=genus,curve=f'y^2=x^{m}-1; beta=x^{m}',
        sigma=sigma,alpha=alpha,phi=phi,faces=faces,
        quiver_vertices=m,arrows=[dict(id=i,source=i%m,target=inv[i]%m,forbidden_next=phi[i]) for i in range(2*m)],
        order_DVR_rank=2*m*m,physical_sites=m+2,
        physical_edges=[[b,2+j] for b in [0,1] for j in range(m)],
        scope='Actual clean dessin passport; finite physical spins on black/white vertices, not a faithful order representation')

def white_fields(m):return .045*np.cos(1.7*np.arange(m))+.02*np.arange(m)/m

def fine_action(m,params):
    jp,jm,b=map(float,params);s=spins(m+2);white=s[:,2:];eta=(-1.)**np.arange(m)
    return jp*s[:,0]*white.sum(1)+jm*s[:,1]*(white@eta)+b*s[:,0]-.6*b*s[:,1]+white@white_fields(m)

def black_decimation(m,params):
    jp,jm,b=map(float,params);s=spins(m);eta=(-1.)**np.arange(m)
    x=b+jp*s.sum(1);y=-.6*b+jm*(s@eta)
    return np.logaddexp(x,-x)+np.logaddexp(y,-y)+s@white_fields(m)

def decimate(action,keep):
    v=np.asarray(action,dtype=float);n=int(round(math.log2(len(v))));keep=list(keep)
    assert len(v)==2**n and keep==sorted(set(keep)) and all(0<=q<n for q in keep)
    s=((np.arange(2**n)[:,None]>>np.arange(n-1,-1,-1))&1)
    group=s[:,keep]@(2**np.arange(len(keep)-1,-1,-1)) if keep else np.zeros(len(v),dtype=int)
    return np.array([logsumexp(v[group==j]) for j in range(2**len(keep))])

def walsh(values,normalized=True):
    a=np.asarray(values,dtype=float).copy();n=len(a);assert n and n&(n-1)==0
    h=1
    while h<n:
        for i in range(0,n,2*h):
            x=a[i:i+h].copy();y=a[i+h:i+2*h].copy();a[i:i+h]=x+y;a[i+h:i+2*h]=x-y
        h*=2
    return a/n if normalized else a

def transfer_step(K,h,C=0.):
    # Square a normalized transfer, carrying the scalar logarithm separately.
    T=np.array([[np.exp(K+h),np.exp(-K)],[np.exp(-K),np.exp(K-h)]])
    P=T@T;a,b,d=P[0,0],P[0,1],P[1,1]
    return .25*np.log(a*d/(b*b)),.5*np.log(a/d),2*C+.25*np.log(a*d*b*b)

def transfer_logz(N,K,h,C=0.):
    T=np.array([[np.exp(K+h),np.exp(-K)],[np.exp(-K),np.exp(K-h)]])
    ev=np.linalg.eigvalsh(T);ratio=ev[0]/ev[1]
    return float(N*(C+np.log(ev[1]))+np.log1p(ratio**N))

def correlation_length(K,h):
    T=np.array([[np.exp(K+h),np.exp(-K)],[np.exp(-K),np.exp(K-h)]])
    ev=np.linalg.eigvalsh(T);r=abs(ev[0]/ev[1])
    return float(-1/np.log(r)) if r>1e-15 else 0.

def classical_flow(m,params,initial=None):
    labels=list(range(m+2));v=fine_action(m,params) if initial is None else np.asarray(initial)
    if initial is not None:labels=list(range(2,m+2))
    result=[]
    while True:
        n=len(labels);c=walsh(v);p=np.exp(v-logsumexp(v));s=spins(n)
        truncated=c.copy();truncated[[k for k in range(len(c)) if k.bit_count()>2]]=0
        vt=walsh(truncated,normalized=False)
        terms=[dict(mask=k,sites=[labels[q] for q in range(n) if k>>(n-1-q)&1],coupling=float(c[k]),degree=k.bit_count()) for k in range(len(c))]
        result.append(dict(sites=labels.copy(),logweights=v.tolist(),couplings=c.tolist(),terms=terms,
            logZ=float(logsumexp(v)),magnetizations=(p@s).tolist(),
            higher_body_norm=float(np.linalg.norm([c[k] for k in range(len(c)) if k.bit_count()>2])),
            pair_truncation_logZ_error=float(logsumexp(vt)-logsumexp(v)),
            pair_truncation_TV=float(.5*np.abs(np.exp(vt-logsumexp(vt))-p).sum())))
        if n==1:break
        keep=list(range(2,n)) if len(result)==1 and initial is None else list(range(0,n,2))
        v=decimate(v,keep);labels=[labels[q] for q in keep]
    return result

def partial_trace(W,keep):
    n=int(round(math.log2(W.shape[0])));keep=sorted(keep);a=W.reshape([2]*(2*n));current=n
    for q in sorted(set(range(n))-set(keep),reverse=True):
        a=np.trace(a,axis1=q,axis2=q+current);current-=1
    return a.reshape(2**len(keep),2**len(keep))

def pauli_expansion(H):
    d=len(H);n=int(round(math.log2(d)));basis=np.arange(d);coeff=[];reconstructed=np.zeros_like(H,dtype=complex)
    for word in itertools.product('IXYZ',repeat=n):
        target=basis.copy();phase=np.ones(d,dtype=complex)
        for q,p in enumerate(word):
            bits=(basis>>(n-1-q))&1
            if p in 'XY':target^=1<<(n-1-q)
            if p=='Y':phase*=1j*(1-2*bits)
            elif p=='Z':phase*=1-2*bits
        c=np.sum(H[basis,target]*phase)/d
        assert abs(c.imag)<1e-10
        reconstructed[target,basis]+=c.real*phase
        coeff.append(dict(word=''.join(word),value=float(c.real),degree=sum(p!='I' for p in word)))
    return coeff,float(np.linalg.norm(reconstructed-H))

def quantum_example(m,params,beta=.73,transverse=.47):
    assert m<=5 and beta>0
    n=m+2;s=spins(n);v=fine_action(m,params);H=np.diag(-v);basis=np.arange(2**n)
    for q in range(n):H[basis,basis^(1<<(n-1-q))]-=transverse
    eig,U=np.linalg.eigh(H);W=(U*np.exp(-beta*eig))@U.T
    fineZ=float(np.trace(W));keep=list(range(2,n));Wc=partial_trace(W,keep)
    e,V=np.linalg.eigh(Wc);assert np.min(e)>0
    Heff=(V*(-np.log(e)/beta))@V.T
    reconstructed=(V*np.exp(-beta*(-np.log(e)/beta)))@V.T
    coeff,paulierr=pauli_expansion(Heff)
    rho=Wc/fineZ;mag=np.diag(rho)@spins(m)
    directmag=np.diag(W)/fineZ@spins(n)[:,2:]
    nextkeep=list(range(0,m,2));nested=partial_trace(Wc,nextkeep)
    direct=partial_trace(W,[keep[q] for q in nextkeep])
    # Reconstruct a deliberately truncated Hamiltonian, retaining its identity term.
    trunc=np.zeros_like(Heff,dtype=complex);d=2**m;ib=np.arange(d)
    for term in coeff:
        if term['degree']>2:continue
        target=ib.copy();phase=np.ones(d,dtype=complex)
        for q,p in enumerate(term['word']):
            bit=(ib>>(m-1-q))&1
            if p in 'XY':target^=1<<(m-1-q)
            if p=='Y':phase*=1j*(1-2*bit)
            elif p=='Z':phase*=1-2*bit
        trunc[target,ib]+=term['value']*phase
    et,Ut=np.linalg.eigh(trunc);Wt=(Ut*np.exp(-beta*et))@Ut.conj().T;zt=float(np.trace(Wt).real)
    checks=dict(partition_abs_error=abs(float(np.trace(Wc))-fineZ),
        retained_observable_error=float(np.max(abs(mag-directmag))),
        spectral_log_exp_residual=float(np.linalg.norm(reconstructed-Wc)),
        nested_partial_trace_residual=float(np.linalg.norm(nested-direct)),
        pauli_reconstruction_residual=paulierr)
    flow=[];current=Wc.copy();labels=list(range(2,n))
    while True:
        ek,uk=np.linalg.eigh(current);he=(uk*(-np.log(ek)/beta))@uk.conj().T
        pc,pe=pauli_expansion(he)
        flow.append(dict(sites=labels.copy(),coefficients=pc,logZ=float(np.log(np.trace(current).real)),
            identity_energy=pc[0]['value'],reconstruction_residual=pe,
            higher_body_norm=float(np.linalg.norm([t['value'] for t in pc if t['degree']>2]))))
        if len(labels)==1:break
        ks=list(range(0,len(labels),2));current=partial_trace(current,ks);labels=[labels[q] for q in ks]
    return dict(m=m,genus=(m-1)//2,beta=beta,transverse=transverse,parameters=list(params),
        fine_dimension=2**n,retained_dimension=2**m,keep=keep,flow=flow,logZ=float(np.log(fineZ)),
        identity_energy=coeff[0]['value'],coefficients=coeff,
        higher_body_norm=float(np.linalg.norm([t['value'] for t in coeff if t['degree']>2])),
        marginal_magnetizations=mag.tolist(),effective_eigenvalues=(-np.log(e)/beta).tolist(),
        pair_truncation_logZ_error=float(np.log(zt/fineZ)),
        pair_truncation_trace_distance=float(.5*np.abs(np.linalg.eigvalsh(Wt/zt-rho)).sum()),checks=checks,
        scope='Finite beta-dependent full effective Hamiltonian; retained equal-time observables and partition only, not full real-time or thermodynamic RG')
