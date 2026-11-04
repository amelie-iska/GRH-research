#!/usr/bin/env python3
"""Original hybrid quantum-feature diffusion/flow models for actual RG marginals.

No installation, authentication or training occurs on import. The target is
Z-measurement data from a reduced quantum Gibbs state, not full tomography,
a coherent quantum denoiser, an infinite-width trained QNN or a GRH proof.
"""
from pathlib import Path
import argparse, json, math, time, platform, hashlib
import numpy as np
import torch
from torch import nn

ROOT = Path(__file__).resolve().parents[2]
SEED = 20261104


def spins(n, device='cpu', dtype=torch.float32):
    indices = torch.arange(2**n, device=device)
    bits = (indices[:, None] >> torch.arange(n-1, -1, -1, device=device)) & 1
    return (1-2*bits).to(dtype)


def physical_teacher(device='cpu', m=5, beta=1.0):
    """Actual clean-dessin K_(2,m) interaction graph; columns are spin states."""
    n = m+2
    if n > 11:
        raise ValueError('Dense exact teacher restricted to at most11spins; no silent approximation')
    z = spins(n, device, torch.float64); idx = torch.arange(2**n, device=device)
    eta = (-1.)**torch.arange(m, device=device, dtype=torch.float64)
    white_fields = .045*torch.cos(1.7*torch.arange(m, device=device, dtype=torch.float64))+.02*torch.arange(m, device=device)/m
    diag = -.50*z[:, 0]*z[:, 2:].sum(1)-.35*z[:, 1]*(z[:, 2:]@eta)-.12*z[:, 0]+.072*z[:, 1]-z[:, 2:]@white_fields
    H = torch.diag(diag)
    for q in range(n):
        H[idx, idx ^ (1 << (n-1-q))] -= .55
    energy, U = torch.linalg.eigh(H)
    weights = torch.softmax(-beta*(energy-energy.min()), dim=0)
    rho = (U*weights[None, :])@U.T
    reduced = torch.einsum('aibi->ab', rho.reshape(4, 2**m, 4, 2**m))
    coarse = torch.diagonal(reduced).clamp_min(0); coarse /= coarse.sum()
    fine = torch.diagonal(rho).clamp_min(0); fine /= fine.sum()
    entropy = lambda p: float(-(p.clamp_min(1e-30)*p.clamp_min(1e-30).log()).sum())
    channels = []
    for t in [0., .25, .5, 1., 2., 5.]:
        # CPTP depolarizing semigroup on the retained two-qubit density matrix.
        p = math.exp(-t); state = p*reduced+(1-p)*torch.eye(4, device=device, dtype=reduced.dtype)/4
        ev = torch.linalg.eigvalsh(state)
        assert abs(float(torch.trace(state))-1)<1e-10 and float(ev.min())>-1e-10
        channels.append(dict(t=t,density=state.cpu().tolist(),eigenvalues=ev.cpu().tolist(),entropy=entropy(ev)))
    assert torch.allclose(reduced, reduced.T, atol=1e-10)
    assert abs(float(torch.trace(rho))-1)<1e-10
    return dict(m=m,genus=(m-1)//2,n_spins=n,beta=beta,
                interaction_edges=[[b,2+j] for b in (0,1) for j in range(m)],
                parameters=dict(Jp=.5,Jm=.35,hx=.55,black_field=.12,second_black_field=-.072),
                probabilities=coarse.float(),fine_probabilities=fine.float(),
                reduced_density=reduced.cpu().tolist(),quantum_channel=channels,
                minimum_density_eigenvalue=float(torch.linalg.eigvalsh(reduced).min()),
                offdiagonal_norm=float(torch.linalg.norm(reduced-torch.diag(torch.diagonal(reduced)))),
                coarse_graining='Exact partial trace of white spins; retained black0,black1',
                scope='Finite quantum-matter model on actual dessin incidence graph, not a faithful order representation')


def cnot_permutation(n, control, target, device):
    i = torch.arange(2**n, device=device)
    return i ^ (((i >> (n-1-control)) & 1) << (n-1-target))


def apply_gate(state, gate, q, n):
    batch = len(state)
    return torch.einsum('bij,bajc->baic', gate, state.reshape(batch,2**q,2,2**(n-q-1))).reshape(batch,2**n)


class QuantumFeatures(nn.Module):
    def __init__(self, n=4, layers=2, entangle=True):
        super().__init__();self.n=n;self.layers=layers;self.entangle=entangle
        self.theta=nn.Parameter(.15*torch.randn(layers,n,2))
        index=torch.arange(2**n)
        self.register_buffer('observables',torch.stack([(-1.)**((index[:,None] >> torch.arange(n)) & 1).mul(((mask >> torch.arange(n)) & 1)).sum(1) for mask in range(1,2**n)],1))
        for q in range(n):self.register_buffer(f'perm{q}',cnot_permutation(n,q,(q+1)%n,'cpu'))

    def forward(self, angles):
        batch=len(angles);state=torch.zeros(batch,2**self.n,device=angles.device,dtype=torch.complex64);state[:,0]=1
        for layer in range(self.layers):
            for q in range(self.n):
                a=angles[:,q]+self.theta[layer,q,0];c=torch.cos(a/2);s=torch.sin(a/2)
                gate=torch.stack([c,-s,s,c],1).reshape(batch,2,2).to(torch.complex64)
                state=apply_gate(state,gate,q,self.n)
                phase=angles[:,q]*.37+self.theta[layer,q,1]
                diagonal=torch.stack([torch.exp(-.5j*phase),torch.exp(.5j*phase)],1)
                state=apply_gate(state,torch.diag_embed(diagonal),q,self.n)
            if self.entangle:
                for q in range(self.n):state=state[:,getattr(self,f'perm{q}')]
        return (state.real.square()+state.imag.square())@self.observables


class HybridField(nn.Module):
    def __init__(self, dimension=2, entangle=True, hidden=64):
        super().__init__();self.dimension=dimension
        self.encoder=nn.Linear(dimension+5,4);self.quantum=QuantumFeatures(entangle=entangle)
        self.head=nn.Sequential(nn.Linear(dimension+5+15,hidden),nn.SiLU(),nn.Linear(hidden,hidden),nn.SiLU(),nn.Linear(hidden,dimension))

    def forward(self,x,t):
        if t.ndim==1:t=t[:,None]
        context=torch.cat([x,t,torch.sin(2*math.pi*t),torch.cos(2*math.pi*t),torch.sin(4*math.pi*t),torch.cos(4*math.pi*t)],1)
        features=self.quantum(math.pi*torch.tanh(self.encoder(context)))
        return self.head(torch.cat([context,features],1))


def schedule(T, device):
    t=torch.arange(T+1,device=device,dtype=torch.float32)/T
    raw=torch.cos((t+.008)/1.008*math.pi/2).square();raw/=raw[0].clone()
    beta=(1-raw[1:]/raw[:-1]).clamp(.0001,.999)
    alpha=1-beta;abar=torch.cat([torch.ones(1,device=device),torch.cumprod(alpha,0)])
    return beta,alpha,abar


def sample_data(probabilities, count, sigma=.2):
    idx=torch.multinomial(probabilities,count,replacement=True)
    s=spins(int(math.log2(len(probabilities))),probabilities.device)[idx]
    return s+sigma*torch.randn_like(s)


def oracle_field(x,t,probabilities,objective,T=64,sigma=.2):
    centers=spins(x.shape[1],x.device)
    if objective=='diffusion':
        _,_,ab=schedule(T,x.device);a=ab[(t*T).round().long().clamp(1,T)].view(-1,1,1)
        means=a.sqrt()*centers[None];var=a*sigma*sigma+1-a
        diff=x[:,None]-means
        posterior=torch.softmax(probabilities.clamp_min(1e-30).log()[None]-.5*(diff.square().sum(-1)/var[:,:,0]),1)
        return ((posterior[:,:,None]*diff/var).sum(1))*(1-a[:,0]).sqrt()
    tt=t[:,None,None];var=(1-tt).square()+tt.square()*sigma*sigma
    diff=x[:,None]-tt*centers[None]
    posterior=torch.softmax(probabilities.clamp_min(1e-30).log()[None]-.5*(diff.square().sum(-1)/var[:,:,0]),1)
    conditional=centers[None]+(tt*sigma*sigma-(1-tt))/var*diff
    return (posterior[:,:,None]*conditional).sum(1)


def metrics(samples,p):
    d=samples.shape[1];bits=(samples<0).long();idx=(bits*(2**torch.arange(d-1,-1,-1,device=samples.device))[None]).sum(1)
    hist=torch.bincount(idx,minlength=len(p)).float()/len(samples);s=spins(d,p.device)
    reference=sample_data(p,len(samples))
    angle=torch.arange(16,device=samples.device,dtype=samples.dtype)*math.pi/16
    directions=torch.stack([angle.cos(),angle.sin()],1)
    sliced=(torch.sort(samples@directions.T,dim=0).values-torch.sort(reference@directions.T,dim=0).values).abs().mean()
    return dict(histogram=hist.cpu().tolist(),total_variation=float(.5*abs(hist-p).sum()),
                mean_absolute_error=float(abs(hist@s-p@s).mean()),correlation_error=float(abs(hist@(s[:,0]*s[:,1])-p@(s[:,0]*s[:,1]))),
                continuous_mean=samples.mean(0).cpu().tolist(),second_moment=samples.square().mean(0).cpu().tolist(),
                dequantization_MSE=float((abs(samples)-1).square().mean()),sliced_W1_16directions=float(sliced))


@torch.no_grad()
def generate(model,p,objective,count=4096,T=64,oracle=False,steps=128):
    x=torch.randn(count,model.dimension,device=p.device)
    field=lambda v,t:oracle_field(v,t,p,objective,T) if oracle else model(v,t)
    if objective=='flow':
        dt=1/steps
        for k in range(steps):
            t=torch.full((count,),k*dt,device=p.device);v=field(x,t)
            # Explicit Heun integration of a learned classical velocity field.
            nextx=x+dt*v;nextt=torch.full((count,),(k+1)*dt,device=p.device)
            x+=dt*.5*(v+field(nextx,nextt))
    else:
        beta,alpha,ab=schedule(T,p.device)
        for k in range(T,0,-1):
            t=torch.full((count,),k/T,device=p.device);eps=field(x,t)
            mu=(x-beta[k-1]/(1-ab[k]).sqrt()*eps)/alpha[k-1].sqrt()
            variance=beta[k-1]*(1-ab[k-1])/(1-ab[k])
            x=mu+(variance.sqrt()*torch.randn_like(x) if k>1 else 0)
    return x


def train_one(p,objective,entangle,out,steps=2000,batch=512,seed=SEED):
    torch.manual_seed(seed);np.random.seed(seed);start=time.perf_counter();device=p.device
    net=HybridField(int(math.log2(len(p))),entangle).to(device)
    opt=torch.optim.Adam(net.parameters(),lr=.0015);history=[];T=64;_,_,ab=schedule(T,device)
    # Fixed disjoint pools; all target labels are synthetic draws from the exact teacher.
    train=sample_data(p,16384);held=sample_data(p,4096)
    for step in range(steps):
        x1=train[torch.randint(len(train),(batch,),device=device)];noise=torch.randn_like(x1)
        if objective=='flow':
            t=torch.rand(batch,device=device);x=(1-t[:,None])*noise+t[:,None]*x1;target=x1-noise
        else:
            k=torch.randint(1,T+1,(batch,),device=device);t=k.float()/T;a=ab[k,None]
            x=a.sqrt()*x1+(1-a).sqrt()*noise;target=noise
        prediction=net(x,t);loss=(prediction-target).square().mean();opt.zero_grad(set_to_none=True);loss.backward()
        torch.nn.utils.clip_grad_norm_(net.parameters(),2.);opt.step()
        if step%100==0 or step==steps-1:history.append(dict(step=step,loss=float(loss.detach())))
    net.eval();count=4096
    with torch.no_grad():
        noise=torch.randn_like(held);t=torch.rand(len(held),device=device)
        if objective=='flow':x=(1-t[:,None])*noise+t[:,None]*held;target=held-noise
        else:
            k=(t*T).ceil().long().clamp(1,T);t=k.float()/T;a=ab[k,None];x=a.sqrt()*held+(1-a).sqrt()*noise;target=noise
        pred=net(x,t);truth=oracle_field(x,t,p,objective,T)
        evaluation=dict(heldout_loss=float((pred-target).square().mean()),oracle_field_MSE=float((pred-truth).square().mean()))
        generated=generate(net,p,objective,count=count);evaluation.update(metrics(generated,p))
        # Oracle control isolates sampler/time-discretization error from model error.
        control=generate(net,p,objective,count=count,oracle=True);oracle_metrics=metrics(control,p)
    if device.type=='cuda':torch.cuda.synchronize()
    elapsed=time.perf_counter()-start
    # Path arithmetic kept explicit to avoid accidental replacement of old runs.
    checkpoint=out/(objective+('-entangled' if entangle else '-product')+'.pt')
    torch.save(dict(state_dict=net.state_dict(),objective=objective,entangle=entangle,dimension=net.dimension,seed=seed),checkpoint)
    return dict(objective=objective,architecture='entangled-quantum-feature-hybrid' if entangle else 'matched-product-circuit-hybrid',
                parameters=sum(v.numel() for v in net.parameters()),quantum_qubits=4,quantum_layers=2,
                seed=seed,steps=steps,batch=batch,train_count=len(train),heldout_count=len(held),sample_count=count,
                wall_seconds=elapsed,device=str(device),history=history,evaluation=evaluation,
                oracle_sampler_control=oracle_metrics,checkpoint=checkpoint.name,
                checkpoint_sha256=hashlib.sha256(checkpoint.read_bytes()).hexdigest(),
                samples=generated[:256].cpu().tolist(),scope='Trained hybrid classical sampler with differentiable quantum-circuit features; not a coherent CPTP denoiser or upstream QFM reproduction')


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--output',required=True,type=Path)
    parser.add_argument('--device',choices=['cpu','cuda'],default='cpu');parser.add_argument('--steps',type=int,default=2000)
    parser.add_argument('--objective',choices=['both','diffusion','flow'],default='both');parser.add_argument('--entangle',choices=['both','yes','no'],default='both');args=parser.parse_args()
    if args.output.exists():raise SystemExit('New output directory required; prior experiments are protected')
    if args.device=='cuda' and not torch.cuda.is_available():raise SystemExit('CUDA requested but unavailable; no silent CPU fallback')
    args.output.mkdir(parents=True);device=torch.device(args.device);teacher=physical_teacher(device)
    p=teacher.pop('probabilities');teacher.pop('fine_probabilities')
    torch.manual_seed(SEED);np.random.seed(SEED)
    baseline=metrics(torch.randn(4096,2,device=device),p)
    target_control=metrics(sample_data(p,4096),p)
    records=[]
    for objective in (['diffusion','flow'] if args.objective=='both' else [args.objective]):
        for entangle in ([False,True] if args.entangle=='both' else [args.entangle=='yes']):
            record=train_one(p,objective,entangle,args.output,args.steps);records.append(record)
            (args.output/'partial-record.json').write_text(json.dumps(dict(teacher=teacher,probabilities=p.cpu().tolist(),gaussian_baseline=baseline,independent_target_control=target_control,records=records),indent=2)+'\n')
            print(json.dumps(dict(objective=objective,entangle=entangle,evaluation=record['evaluation'],seconds=record['wall_seconds'])),flush=True)
    result=dict(seed=SEED,hardware=dict(platform=platform.platform(),torch=torch.__version__,device=args.device,gpu=torch.cuda.get_device_name(0) if args.device=='cuda' else None),teacher=teacher,probabilities=p.cpu().tolist(),gaussian_baseline=baseline,independent_target_control=target_control,records=records)
    (args.output/'record.json').write_text(json.dumps(result,indent=2)+'\n')


if __name__=='__main__':main()
