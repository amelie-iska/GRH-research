"""Local NumPy review of periodic DSM/flow batch math and Pauli conventions."""
import ast,json,math,types
from pathlib import Path
import numpy as np
ROOT=Path(__file__).resolve().parents[3]
def main():
    source=ROOT/'examples/synthetic_training/train_torsion_flow.py'
    nodes=[x for x in ast.parse(source.read_text()).body if isinstance(x,ast.FunctionDef) and x.name in ['wrap','sample_target','training_batch']]
    ns=dict(np=np,math=math,TAU=2*math.pi,torch=types.SimpleNamespace(tensor=np.asarray))
    exec(compile(ast.Module(body=nodes,type_ignores=[]),str(source),'exec'),ns)
    target=dict(angle_grid=[[-2.8],[-.3],[1.2]],probability=[.2,.5,.3],dimension=1)
    class Recorded:
        def __init__(self):self.rng=np.random.default_rng(20261104);self.log=[]
        def choice(self,*a,**k):
            x=self.rng.choice(*a,**k);self.log.append(('choice',x));return x
        def normal(self,*a,**k):
            x=self.rng.normal(*a,**k);self.log.append(('normal',x));return x
        def uniform(self,*a,**k):
            x=self.rng.uniform(*a,**k);self.log.append(('uniform',x));return x
    batches=[]
    for method in ['flow','score']:
        rng=Recorded();x,t,label,w=ns['training_batch'](target,method,10000,rng)
        x1=ns['wrap'](np.array(target['angle_grid'])[rng.log[0][1]]+rng.log[1][1])
        assert np.all((x>=-math.pi)&(x<math.pi)) and t.min()<.001
        if method=='flow':
            x0=rng.log[3][1];v=np.arctan2(np.sin(x1-x0),np.cos(x1-x0))
            assert np.max(abs(v-label))<1e-12
            assert np.max(abs(ns['wrap'](x0+t[:,None]*v)-x))<1e-12
        else:
            tau=.03+1.97*t;sigma=np.sqrt(2*tau)
            assert np.max(abs(label+rng.log[3][1]/sigma[:,None]))<1e-12
            assert np.max(abs(x-ns['wrap'](x1+sigma[:,None]*rng.log[3][1])))<1e-12
            assert np.max(abs(w-2*tau))<1e-12
        batches.append(dict(method=method,training_batch_equations=True,minimum_sampled_t=float(t.min())))
    # Exact wrapped-mixture score, including winding responsibilities.
    centers=np.array(target['angle_grid'])[:,0];weights=np.array(target['probability'])
    def density_score(x,tau):
        var=.05**2+2*tau;d=x-centers[:,None]+2*np.pi*np.arange(-8,9)[None,:]
        terms=weights[:,None]*np.exp(-d*d/(2*var))/np.sqrt(2*np.pi*var)
        return terms.sum(),float((-d/var*terms).sum()/terms.sum())
    errors=[]
    for tau in [.03,.2,2.]:
        for x in [-3.13,-.17,2.98]:
            rho,score=density_score(x,tau);h=1e-5
            fd=(math.log(density_score(x+h,tau)[0])-math.log(density_score(x-h,tau)[0]))/(2*h)
            errors.append(abs(fd-score));assert abs(fd-score)<1e-7
            assert abs(density_score(x+2*np.pi,tau)[1]-score)<1e-12
    # Verify the eight readout formulas against literal two-qubit Pauli matrices.
    rng=np.random.default_rng(20261104);psi=rng.normal(size=4)+1j*rng.normal(size=4);psi/=np.linalg.norm(psi)
    prob=abs(psi)**2;a=psi[0].conj()*psi[2]+psi[1].conj()*psi[3];b=psi[0].conj()*psi[1]+psi[2].conj()*psi[3]
    formula=np.array([prob[0]+prob[1]-prob[2]-prob[3],prob[0]-prob[1]+prob[2]-prob[3],2*a.real,2*b.real,2*a.imag,2*b.imag,prob[0]-prob[1]-prob[2]+prob[3],2*(psi[0].conj()*psi[3]+psi[1].conj()*psi[2]).real])
    I=np.eye(2);X=np.array([[0,1],[1,0]]);Y=np.array([[0,-1j],[1j,0]]);Z=np.diag([1,-1])
    ops=[np.kron(A,B) for A,B in [(Z,I),(I,Z),(X,I),(I,X),(Y,I),(I,Y),(Z,Z),(X,X)]]
    pauli_error=float(abs(formula-np.array([np.vdot(psi,P@psi).real for P in ops])).max());assert pauli_error<1e-14
    result=dict(passed=True,source_batch_checks=batches,wrapped_score_finite_difference_max_error=max(errors),
        Pauli_readout_max_error=pauli_error,score_endpoint_total_wrapped_variance=.05**2+2*.03,
        scope='AST-selected batch math and independent NumPy score/readout formulas; no Torch/RDKit/training execution')
    out=ROOT/'outputs/checks/2026-11-04-synthetic-training/review';out.mkdir(parents=True,exist_ok=True)
    (out/'torsion-math-review.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
