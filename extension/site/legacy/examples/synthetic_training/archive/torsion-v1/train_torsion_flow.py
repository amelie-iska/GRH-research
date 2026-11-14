"""CPU-only periodic quantum/classical score and flow learners on MMFF torsions.

New isolated outputs; never imports or changes either active model project.
The target is a softened finite torsion-grid Gibbs model, not full equilibrium.
"""
import argparse,json,math,hashlib
from pathlib import Path
import numpy as np
import torch
from rdkit import Chem,rdBase
from rdkit.Chem import AllChem,rdMolTransforms
from common import fresh,write_json,sha
torch.set_num_threads(1);torch.set_default_dtype(torch.float64)
SEED=20261104;TAU=2*math.pi
def wrap(x):return (x+math.pi)%TAU-math.pi

def chemical_target(smiles,dimension):
    mol=Chem.AddHs(Chem.MolFromSmiles(smiles));p=AllChem.ETKDGv3();p.randomSeed=SEED;p.numThreads=1;assert AllChem.EmbedMolecule(mol,p)==0
    props=AllChem.MMFFGetMoleculeProperties(mol,mmffVariant='MMFF94');ff=AllChem.MMFFGetMoleculeForceField(mol,props,nonBondedThresh=100.);assert ff.Minimize(maxIts=2000)==0
    base=np.array(mol.GetConformer().GetPositions());size=72 if dimension==1 else 24;axis=np.linspace(-math.pi,math.pi,size,endpoint=False)+math.pi/size
    grid=np.array(np.meshgrid(*([axis]*dimension),indexing='ij')).reshape(dimension,-1).T;energy=[];geometry=[];conformer=mol.GetConformer()
    for angles in grid:
        for i,point in enumerate(base):conformer.SetAtomPosition(i,tuple(point))
        for d,theta in enumerate(angles):rdMolTransforms.SetDihedralRad(conformer,d,d+1,d+2,d+3,float(theta))
        x=np.array(conformer.GetPositions());e=ff.CalcEnergy(x.ravel().tolist());assert np.isfinite(e);energy.append(e);geometry.append(x.tolist())
    energy=np.array(energy);temperature=300.;kbt=.00198720425864083*temperature;p=np.exp(-(energy-energy.min())/kbt);p/=p.sum()
    assert abs(p.sum()-1)<1e-12
    return dict(smiles=smiles,dimension=dimension,size=size,angle_grid=grid.tolist(),MMFF_energy_kcal_mol=energy.tolist(),probability=p.tolist(),temperature_kelvin=temperature,kBT_kcal_mol=kbt,
        atomic_numbers=[a.GetAtomicNum() for a in mol.GetAtoms()],bonds=[dict(a=b.GetBeginAtomIdx(),b=b.GetEndAtomIdx(),order=b.GetBondTypeAsDouble()) for b in mol.GetBonds()],
        torsion_atoms=[[d,d+1,d+2,d+3] for d in range(dimension)],geometry_grid_angstrom=geometry,base_coordinates_angstrom=base.tolist(),
        target_smoothing_sigma_radian=.05,scope='Fixed remaining bond lengths/angles; softened finite MMFF94 torsion-grid Gibbs model. Not solvent/full conformer equilibrium or quantum chemistry.')

class Learner(torch.nn.Module):
    def __init__(self,dimension,quantum):
        super().__init__();self.dimension=dimension;self.quantum=quantum
        if quantum:self.angles=torch.nn.Parameter(torch.randn(2,2,3)*.2)
        size=11 if quantum else dimension*4+3
        self.layers=torch.nn.Sequential(torch.nn.Linear(size,64),torch.nn.Tanh(),torch.nn.Linear(64,64),torch.nn.Tanh(),torch.nn.Linear(64,dimension))
    def features(self,x,t):
        time=torch.stack([t,torch.sin(math.pi*t),torch.cos(math.pi*t)],1)
        if not self.quantum:return torch.cat([torch.sin(x),torch.cos(x),torch.sin(2*x),torch.cos(2*x),time],1)
        psi=torch.ones((len(x),4),dtype=torch.complex128)/2
        for layer in range(2):
            for wire in range(2):
                coordinate=x[:,wire] if self.dimension==2 else (wire+1)*x[:,0]
                phase=coordinate+t*self.angles[layer,wire,0]+self.angles[layer,wire,1]
                p=torch.stack([torch.exp(-.5j*phase),torch.exp(.5j*phase)],1)
                q=psi.reshape(-1,2,2);q=q*p[:,:,None] if wire==0 else q*p[:,None,:]
                angle=self.angles[layer,wire,2];c=torch.cos(angle/2);s=torch.sin(angle/2)
                U=torch.stack([torch.stack([c,-s]),torch.stack([s,c])]).to(torch.complex128)
                q=torch.einsum('ij,bjk->bik',U,q) if wire==0 else torch.einsum('bij,kj->bik',q,U);psi=q.reshape(-1,4)
            psi=psi*torch.tensor([1,1,1,-1])
        probability=abs(psi)**2
        z0=probability[:,0]+probability[:,1]-probability[:,2]-probability[:,3];z1=probability[:,0]-probability[:,1]+probability[:,2]-probability[:,3]
        a=psi[:,0].conj()*psi[:,2]+psi[:,1].conj()*psi[:,3];b=psi[:,0].conj()*psi[:,1]+psi[:,2].conj()*psi[:,3]
        zz=probability[:,0]-probability[:,1]-probability[:,2]+probability[:,3];xx=2*(psi[:,0].conj()*psi[:,3]+psi[:,1].conj()*psi[:,2]).real
        return torch.cat([torch.stack([z0,z1,2*a.real,2*b.real,2*a.imag,2*b.imag,zz,xx],1),time],1)
    def forward(self,x,t):return self.layers(self.features(x,t))

def sample_target(target,n,rng):
    grid=np.array(target['angle_grid']);index=rng.choice(len(grid),n,p=target['probability']);return wrap(grid[index]+rng.normal(0,.05,(n,target['dimension'])))

def training_batch(target,method,n,rng):
    x1=sample_target(target,n,rng);t=rng.uniform(.015,1.,n)
    if method=='flow':
        x0=rng.uniform(-math.pi,math.pi,x1.shape);velocity=wrap(x1-x0);x=wrap(x0+t[:,None]*velocity);label=velocity;weight=np.ones(n)
    else:
        tau=.03+(2.-.03)*t;noise=rng.normal(size=x1.shape);sigma=np.sqrt(2*tau);x=wrap(x1+sigma[:,None]*noise);label=-noise/sigma[:,None];weight=2*tau
    return torch.tensor(x),torch.tensor(t),torch.tensor(label),torch.tensor(weight)

def histogram(x,target):
    bins=np.linspace(-math.pi,math.pi,target['size']+1);h=np.histogramdd(x,bins=[bins]*target['dimension'])[0].ravel();return h/h.sum()

def train(target,method,quantum,steps,out):
    dim=target['dimension'];seed=SEED+dim*100+(method=='score')*10+quantum;torch.manual_seed(seed);rng=np.random.default_rng(seed);model=Learner(dim,quantum);optimizer=torch.optim.Adam(model.parameters(),lr=.002)
    validation=training_batch(target,method,2048,np.random.default_rng(seed+900));history=[]
    for step in range(steps+1):
        x,t,label,weight=training_batch(target,method,192,rng);prediction=model(x,t);loss=((prediction-label)**2*weight[:,None]).mean();assert torch.isfinite(loss)
        if step<steps:
            optimizer.zero_grad();loss.backward();assert all(p.grad is None or torch.isfinite(p.grad).all() for p in model.parameters());torch.nn.utils.clip_grad_norm_(model.parameters(),5.);optimizer.step()
        if step%100==0 or step==steps:
            with torch.no_grad():
                a,b,c,w=validation;val=float(((model(a,b)-c)**2*w[:,None]).mean());baseline=float((c*c*w[:,None]).mean())
            history.append(dict(step=step,training_loss=float(loss.detach()),heldout_loss=val,zero_field_loss=baseline))
    with torch.no_grad():
        probe=torch.tensor(rng.uniform(-math.pi,math.pi,(40,dim)));t=torch.tensor(rng.uniform(0,1,40));periodic=float(torch.max(abs(model(probe,t)-model(probe+TAU,t))));assert periodic<1e-10
        n=2048;source=rng.uniform(-math.pi,math.pi,(n,dim)) if method=='flow' else wrap(sample_target(target,n,rng)+rng.normal(size=(n,dim))*2.)
        x=torch.tensor(source);trajectory=[source[:96].tolist()];times=[0.];dt=1/128
        for i in range(128):
            t=torch.full((n,),i*dt)
            if method=='flow':
                a=model(x,t);provisional=torch.remainder(x+dt*a+math.pi,TAU)-math.pi;b=model(provisional,t+dt);x=torch.remainder(x+.5*dt*(a+b)+math.pi,TAU)-math.pi
            else:
                tau=2.-i*dt*(2.-.03);normalized=(tau-.03)/(2.-.03);a=model(x,torch.full((n,),normalized));d=(2.-.03)*dt
                x=torch.remainder(x+2*d*a+math.sqrt(2*d)*torch.tensor(rng.normal(size=(n,dim)))+math.pi,TAU)-math.pi
            if (i+1)%4==0:trajectory.append(x[:96].tolist());times.append((i+1)*dt)
        samples=x.numpy();actual=histogram(samples,target);reference=histogram(sample_target(target,100000,np.random.default_rng(SEED+777)),target)
        tv=float(.5*np.sum(abs(actual-reference)));uniform_tv=float(.5*np.sum(abs(np.ones(len(reference))/len(reference)-reference)))
        grid=torch.tensor(target['angle_grid']);fields=[]
        for t in np.linspace(0,1,17):fields.append(model(grid,torch.full((len(grid),),float(t))).tolist())
    name=f"{'quantum-hybrid' if quantum else 'classical'}-{method}-T{dim}";torch.save(model.state_dict(),out/(name+'.pt'))
    return dict(name=name,method=method,quantum=quantum,dimension=dim,seed=seed,steps=steps,history=history,periodicity_max_error=periodic,
        endpoint_histogram=actual.tolist(),reference_histogram=reference.tolist(),endpoint_total_variation=tv,uniform_total_variation=uniform_tv,
        trajectory=trajectory,generative_time=times,predicted_fields=fields,field_times=np.linspace(0,1,17).tolist(),
        state_dict={k:v.detach().numpy().tolist() for k,v in model.state_dict().items()},parameter_count=sum(p.numel() for p in model.parameters()),
        architecture='Two re-uploading two-qubit Rz/Ry/CZ layers;8 exact Pauli expectations;64-tanh64-tanh readout' if quantum else 'Periodic sin/cos first+second harmonics;64-tanh64-tanh readout',
        initial_law='Uniform on torus' if method=='flow' else 'Exact samples from target plus wrapped Gaussian variance4; not assumed uniform',
        interpretation='Generative interpolation/noise-removal time is not molecular physical time. Quantum-feature circuits classically simulated, not coherent quantum chemistry or advantage.')

def main(out,steps):
    out=fresh(out);experiments=[]
    for smiles,dimension in [('CCCC',1),('CCCCC',2)]:
        target=chemical_target(smiles,dimension);models=[]
        for method in ['flow','score']:
            for quantum in [False,True]:
                result=train(target,method,quantum,steps,out);models.append(result);print(result['name'],result['endpoint_total_variation'],flush=True)
        experiments.append(dict(target=target,models=models))
    write_json(out/'torsion-flow.json',dict(experiments=experiments,seed=SEED,RDKit=rdBase.rdkitVersion,torch=torch.__version__,device='CPU',active_models_read_only=True,
        target_scope='Additional finite-grid MMFF torsion examples, not enrolled data, full equilibrium, quantum-chemical electronic density or a GRH proof'))
    write_json(out/'manifest.json',dict(files={p.name:dict(sha256=sha(p),bytes=p.stat().st_size) for p in out.iterdir() if p.is_file()},source_sha256=sha(__file__)))
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output',type=Path,required=True);p.add_argument('--steps',type=int,default=1200);a=p.parse_args();main(a.output,a.steps)
