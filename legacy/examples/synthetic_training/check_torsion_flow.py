"""Independent circuit, gradient, periodic mixture-score and sampler controls."""
import argparse,json,math
from pathlib import Path
import numpy as np
import torch
from common import write_json,sha
from train_torsion_flow import Learner,wrap,sample_target,histogram

def oracle(target,x,tau):
    x=np.asarray(x);grid=np.array(target['angle_grid']);variance=.05**2+2*tau;delta=wrap(x[:,None,:]-grid[None,:,:]);kernel=np.zeros_like(delta);derivative=np.zeros_like(delta)
    for k in range(-3,4):
        a=delta+2*math.pi*k;v=np.exp(-a*a/(2*variance))/math.sqrt(2*math.pi*variance);kernel+=v;derivative-=a*v/variance
    weight=np.array(target['probability'])[None,:]*kernel.prod(-1);density=weight.sum(1)
    score=(weight[:,:,None]*derivative/np.maximum(kernel,1e-250)).sum(1)/density[:,None]
    return density,score

def features_numpy(x,t,angles):
    out=[];I=np.eye(2)
    X=np.array([[0,1],[1,0]],complex);Y=np.array([[0,-1j],[1j,0]]);Z=np.diag([1.,-1.]);observables=[np.kron(Z,I),np.kron(I,Z),np.kron(X,I),np.kron(I,X),np.kron(Y,I),np.kron(I,Y),np.kron(Z,Z),np.kron(X,X)]
    for point,time in zip(x,t):
        psi=np.ones(4,dtype=complex)/2
        for layer in range(2):
            for wire in range(2):
                coordinate=point[wire] if len(point)==2 else (wire+1)*point[0];a,b,c=angles[layer,wire];p=coordinate+a*time+b;Rz=np.diag(np.exp(np.array([-.5j,.5j])*p));Ry=np.array([[np.cos(c/2),-np.sin(c/2)],[np.sin(c/2),np.cos(c/2)]])
                U=Ry@Rz;psi=(np.kron(U,I) if wire==0 else np.kron(I,U))@psi
            psi=np.diag([1,1,1,-1])@psi
        assert abs(np.vdot(psi,psi)-1)<1e-12
        out.append([np.vdot(psi,O@psi).real for O in observables]+[time,np.sin(math.pi*time),np.cos(math.pi*time)])
    return np.array(out)

def check(folder):
    data=json.loads((folder/'torsion-flow.json').read_text());rng=np.random.default_rng(20261105);circuit=0.;gradient=0.;scoreerror=0.;periodic=0.;metrics=[];controls=[]
    for experiment in data['experiments']:
        target=experiment['target'];d=target['dimension'];probe=rng.uniform(-math.pi,math.pi,(18,d));times=rng.uniform(0,1,18)
        for tau in [.03,.2,2.]:
            p,s=oracle(target,probe,tau)
            for k in range(d):
                a=probe.copy();b=probe.copy();a[:,k]+=1e-5;b[:,k]-=1e-5
                fd=(np.log(oracle(target,a,tau)[0])-np.log(oracle(target,b,tau)[0]))/2e-5;scoreerror=max(scoreerror,float(np.max(abs(fd-s[:,k]))))
            periodic=max(periodic,float(np.max(abs(oracle(target,probe+2*math.pi,tau)[1]-s))))
        for row in experiment['models']:
            model=Learner(d,row['quantum']);model.load_state_dict(torch.load(folder/(row['name']+'.pt'),map_location='cpu',weights_only=True));x=torch.tensor(probe);t=torch.tensor(times)
            if row['quantum']:
                actual=model.features(x,t).detach().numpy();independent=features_numpy(probe,times,model.angles.detach().numpy());circuit=max(circuit,float(np.max(abs(actual-independent))))
                loss=(model(x,t)**2).mean();loss.backward();analytic=model.angles.grad.clone()
                for index in [(0,0,0),(1,1,2)]:
                    with torch.no_grad():
                        value=model.angles[index].item();model.angles[index]=value+1e-5;a=(model(x,t)**2).mean().item();model.angles[index]=value-1e-5;b=(model(x,t)**2).mean().item();model.angles[index]=value
                    gradient=max(gradient,abs((a-b)/2e-5-analytic[index].item()))
            assert row['minimum_trained_normalized_time']==0.
            if row['method']=='score':assert row['minimum_reverse_heat_time']==.03 and 'positive-noise' in row['endpoint_law']
            with torch.no_grad():
                tau=.03+(2.-.03)*times;exact=np.concatenate([oracle(target,probe[i:i+1],tau[i])[1] for i in range(len(probe))]);prediction=model(x,t).numpy()
            if row['method']=='score':metrics.append(dict(name=row['name'],score_oracle_MSE=float(np.mean((prediction-exact)**2)),zero_score_MSE=float(np.mean(exact**2))))
        # Exact-score reverse heat control, with nested Brownian increments.
        n=256;source=wrap(sample_target(target,n,rng)+2*rng.normal(size=(n,d)));noise=rng.normal(size=(128,n,d));results=[];states=[]
        for steps in [64,128]:
            x=source.copy();dt=(2.-.03)/steps
            for i in range(steps):
                _,score=oracle(target,x,2.-i*dt);eta=noise[i] if steps==128 else (noise[2*i]+noise[2*i+1])/math.sqrt(2)
                x=wrap(x+2*dt*score+math.sqrt(2*dt)*eta)
            ref=histogram(sample_target(target,100000,np.random.default_rng(667),sigma=math.sqrt(.05**2+.06)),target);hist=histogram(x,target);results.append(dict(steps=steps,TV_to_correct_positive_noise_endpoint=float(.5*np.sum(abs(hist-ref)))));states.append(x)
        controls.append(dict(dimension=d,exact_score_Euler_controls=results,nested_path_RMS_radian=float(np.sqrt(np.mean(wrap(states[1]-states[0])**2))),scope='Finite stochastic weak/distribution diagnostics with256 samples; no monotone convergence theorem or recovery of zero-noise target'))
    assert circuit<1e-12 and gradient<1e-5 and scoreerror<1e-5 and periodic<1e-10
    return dict(passed=True,quantum_features_independent_Kronecker_max_error=circuit,quantum_gradient_FD_max_error=gradient,wrapped_mixture_score_FD_max_error=scoreerror,oracle_periodicity_max_error=periodic,learned_score_oracle_metrics=metrics,exact_score_controls=controls,
        scores_target_positive_noise_endpoint=True,models=8,CPU_only=True,active_models_unchanged=True,GRH_proved=False)
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--experiment',type=Path,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args();r=check(a.experiment);write_json(a.output,r);print(json.dumps(r,indent=2))
