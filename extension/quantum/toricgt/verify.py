"""Focused independent checks of circuit, gradients, masking and exact outputs."""
from __future__ import annotations
import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import platform
import time

import numpy as np

from data import (batch_arrays, build_dataset, enumerate_paths, learned_proposal,
                  path_certificate, solve_dag, vocabulary_lp_example)
from reference import simulate, parameter_shift


def verify_lp(record):
    c=record["certificate"]
    y=list(map(Fraction,c["equality_multipliers"]))
    z=list(map(Fraction,c["inequality_multipliers"]))
    u=list(map(Fraction,c["upper_bound_multipliers"]))
    assert all(v<=0 for v in z+u)
    for j,cost in enumerate(c["objective"]):
        lhs=sum(y[i]*row[j] for i,row in enumerate(c["Aeq"]))
        lhs+=sum(z[i]*row[j] for i,row in enumerate(c["Aub"]))+u[j]
        assert lhs<=cost
    bound=sum(a*b for a,b in zip(c["beq"],y))+sum(a*b for a,b in zip(c["bub"],z))+sum(u)
    assert bound==Fraction(record["exact_dual_lower_bound"])
    assert bound<=record["exact_enumerated_integer_optimum"]
    return {"rational_dual_feasible":True,"lower_bound":str(bound),
            "integer_optimum":record["exact_enumerated_integer_optimum"]}


def run_checks(device="cpu",numpy_only=False):
    start=time.perf_counter();rng=np.random.default_rng(303)
    dataset=build_dataset(sizes=(24,8,8,8))
    rows=sum(dataset["splits"].values(),[])
    for record in rows:
        distance,path=solve_dag(record)
        assert distance[0]==min(cost for cost,_ in enumerate_paths(record))
        assert path_certificate(record,path,distance)["optimality_certified"]
        proposal=learned_proposal(record,rng.normal(size=len(distance)))
        assert proposal["proposal_regret_units"]>=0
        assert proposal["final_certificate"]["optimality_certified"]
    lp=vocabulary_lp_example();lp_check=verify_lp(lp)
    u=np.diag(np.exp(2j*np.pi*np.arange(8)/8));v=np.zeros((8,8),complex)
    for j in range(8):v[(j-1)%8,j]=1
    weyl=float(np.max(abs(v@u-np.exp(2j*np.pi/8)*u@v)))
    assert weyl<2e-15
    fixtures=[];fd_error=0.0
    for _ in range(12):
        a=rng.uniform(-2,2,6);t=rng.normal(scale=.4,size=(2,3,2))
        f,s,_=simulate(a,t);jac=parameter_shift(a,t)
        assert abs(np.vdot(s,s)-1)<3e-15 and np.max(abs(f))<=1+1e-15
        for j in range(12):
            p=t.copy().reshape(-1);m=t.copy().reshape(-1);p[j]+=1e-5;m[j]-=1e-5
            fd=(simulate(a,p.reshape(t.shape))[0]-simulate(a,m.reshape(t.shape))[0])/2e-5
            fd_error=max(fd_error,float(np.max(abs(fd-jac[:,j]))))
        fixtures.append({"angles":a.tolist(),"theta":t.tolist(),"features":f.tolist(),
                         "state":{"real":s.real.tolist(),"imag":s.imag.tolist()},
                         "jacobian":jac.tolist()})
    assert fd_error<2e-10
    result={"schema":"quantum-toricgt-verification-v1","device_requested":device,
            "numpy_version":np.__version__,"python":platform.python_version(),
            "exact_path_enumerations":len(rows),"weyl_max_error":weyl,
            "parameter_shift_finite_difference_max_error":fd_error,
            "exact_lp_check":lp_check,"lp_example":lp,"reference_cases":fixtures}
    if not numpy_only:
        import torch
        from model import QuantumToricGT,node_mse,quantum_features,torch_batch
        torch.set_num_threads(2)
        if device.startswith("cuda"):
            torch.cuda.set_per_process_memory_fraction(.1)
        state_error=feature_error=jac_error=0.0
        for fixture in fixtures:
            a=torch.tensor(fixture["angles"],device=device,dtype=torch.float64)
            t=torch.tensor(fixture["theta"],device=device,dtype=torch.float64,requires_grad=True)
            f,s=quantum_features(a,t,True)
            ref=np.array(fixture["state"]["real"])+1j*np.array(fixture["state"]["imag"])
            state_error=max(state_error,float(np.max(abs(s.detach().cpu().numpy()-ref))))
            feature_error=max(feature_error,float(np.max(abs(f.detach().cpu().numpy()-fixture["features"]))))
            jac=torch.autograd.functional.jacobian(lambda theta:quantum_features(a,theta),t)
            jac_error=max(jac_error,float(np.max(abs(jac.detach().cpu().numpy().reshape(6,12)-fixture["jacobian"]))))
        assert max(state_error,feature_error,jac_error)<2e-12
        torch.manual_seed(79)
        model=QuantumToricGT(width=12,layers=1).to(device).double().eval()
        one=dataset["splits"]["test"][0]
        batch=torch_batch(batch_arrays([one]),device,torch.float64)
        prediction,detail=model(batch,True)
        loss=node_mse(prediction,batch)
        direct=torch.autograd.grad(loss,model.theta)[0].detach().cpu().numpy().reshape(12)
        override=detail["features"].detach().requires_grad_()
        second=node_mse(model(batch,feature_override=override),batch)
        adjoint=torch.autograd.grad(second,override)[0].detach().cpu().numpy()[0]
        angles=detail["angles"].detach().cpu().numpy()[0]
        theta=model.theta.detach().cpu().numpy()
        chain=sum(adjoint[j]@parameter_shift(a,theta) for j,a in enumerate(angles))
        chain_error=float(np.max(abs(chain-direct)))
        assert chain_error<2e-10
        permutation=torch.randperm(prediction.shape[1],device=device)
        permuted={k:(value[:,permutation][:,:,permutation] if k=="incidence" else value[:,permutation])
                  for k,value in batch.items()}
        equivariance=float((model(permuted)-prediction[:,permutation]).abs().max().detach().cpu())
        assert equivariance<2e-10
        pad=3;t=prediction.shape[1]
        padded={}
        for k,value in batch.items():
            if k=="incidence":
                extra=torch.randn((1,t+pad,t+pad),device=device,dtype=torch.float64);extra[:,:t,:t]=value
            else:
                shape=(1,pad)+tuple(value.shape[2:])
                tail=torch.zeros(shape,device=device,dtype=value.dtype)
                if k=="features":tail.normal_()
                extra=torch.cat([value,tail],dim=1)
            padded[k]=extra
        padded_prediction=model(padded)
        padding_error=float((padded_prediction[:,:t]-prediction).abs().max().detach().cpu())
        assert padding_error<2e-10 and not bool(padded_prediction[:,t:].any())
        route=detail["blocks"][0]["routing"]
        dispatch_error=float((route["dispatch"].sum(dim=1)-1).abs().max().detach().cpu())
        combine_error=float((route["combine"].sum(dim=-1)-1).abs().max().detach().cpu())
        assert max(dispatch_error,combine_error)<2e-12
        counts={}
        for mode in ("quantum","classical","frozen"):
            torch.manual_seed(17);counts[mode]=QuantumToricGT(mode).configuration()
        assert counts["quantum"]["trainable_parameters"]==counts["classical"]["trainable_parameters"]
        result.update({"torch_version":torch.__version__,"cuda_version":torch.version.cuda,
                       "actual_device":str(next(model.parameters()).device),
                       "torch_numpy_state_max_error":state_error,"torch_numpy_features_max_error":feature_error,
                       "autograd_parameter_shift_jacobian_max_error":jac_error,
                       "full_loss_chain_rule_max_error":chain_error,"full_loss_gradient_norm":float(np.linalg.norm(direct)),
                       "token_permutation_max_error":equivariance,"padding_max_error":padding_error,
                       "dispatch_sum_error":dispatch_error,"combine_sum_error":combine_error,
                       "parameter_counts":counts})
        if device.startswith("cuda"):
            result["gpu"]={"name":torch.cuda.get_device_name(),
                           "peak_allocated_bytes":torch.cuda.max_memory_allocated(),
                           "peak_reserved_bytes":torch.cuda.max_memory_reserved()}
    result["wall_seconds"]=time.perf_counter()-start
    result["passed"]=True
    result["source_sha256"]={p.name:hashlib.sha256(p.read_bytes()).hexdigest()
                              for p in Path(__file__).parent.glob("*.py")}
    return result


if __name__=="__main__":
    parser=argparse.ArgumentParser();parser.add_argument("--device",default="cpu")
    parser.add_argument("--numpy-only",action="store_true");parser.add_argument("--output",type=Path,required=True)
    args=parser.parse_args();result=run_checks(args.device,args.numpy_only)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps({k:v for k,v in result.items() if k not in {"reference_cases","lp_example","source_sha256"}},indent=2))
