"""Reproducible matched learning experiments; explicit CLI, no import-time work."""
from __future__ import annotations
import os
os.environ.setdefault("CUBLAS_WORKSPACE_CONFIG",":4096:8")
import argparse
import copy
import hashlib
import json
from pathlib import Path
import platform
import time

import numpy as np
import torch

from data import batch_arrays, learned_proposal, tensor_record, COST_SCALE
from model import QuantumToricGT,node_mse,torch_batch
from reference import simulate


def source_hashes():
    return {p.name:hashlib.sha256(p.read_bytes()).hexdigest()
            for p in Path(__file__).parent.glob("*.py")}


def serial(value):
    if isinstance(value,torch.Tensor):return value.detach().cpu().tolist()
    if isinstance(value,dict):return {k:serial(v) for k,v in value.items()}
    if isinstance(value,(tuple,list)):return [serial(v) for v in value]
    return value


def save_json(path,value):
    path.write_text(json.dumps(value,indent=2,allow_nan=False)+"\n")


def subset(batch,indices):
    return {k:v[indices] for k,v in batch.items()}


def evaluate(model,records,batch):
    model.eval()
    with torch.no_grad():
        prediction=model(batch)
        mse=float(node_mse(prediction,batch).cpu())
    values=prediction.cpu().numpy()
    source_error=[];regret=[];certified=[];examples=[]
    for j,record in enumerate(records):
        n=len(record["text"])+1
        proposed=learned_proposal(record,values[j,:n])
        source_error.append((float(values[j,0])*COST_SCALE-record["optimal_cost_units"])/16)
        regret.append(proposed["proposal_regret_units"]/16)
        certified.append(proposed["proposal_certificate"]["optimality_certified"])
        examples.append({"id":record["id"],"predicted_distance_units":(values[j,:n]*COST_SCALE).tolist(),
                         "true_distance_units":record["distance_units"],**proposed})
    return {"node_rmse_cost":float(COST_SCALE/16*np.sqrt(mse)),
            "source_cost_rmse":float(np.sqrt(np.mean(np.square(source_error)))),
            "mean_proposal_regret_cost":float(np.mean(regret)),
            "max_proposal_regret_cost":float(np.max(regret)),
            "optimal_proposal_fraction":float(np.mean(np.asarray(regret)==0)),
            "initial_certificate_fraction":float(np.mean(certified)),
            "final_certified_fraction":float(np.mean([e["final_certificate"]["optimality_certified"] for e in examples])),
            "examples":examples}


def export_trace(model,record,batch,path):
    model.eval()
    with torch.no_grad():prediction,detail=model(batch,True)
    theta=model.theta.detach().cpu().numpy()
    angles=detail["angles"][0].cpu().numpy()
    features=detail["features"][0].cpu().numpy()
    max_error=0.0
    for a,actual in zip(angles,features):
        ref,_,_=simulate(a,theta)
        max_error=max(max_error,float(np.max(abs(actual-ref))))
    assert max_error<3e-6
    state=detail.pop("state")[0].cpu().numpy()
    trace={"schema":"quantum-toricgt-trained-trace-v1","graph":record,
           "configuration":model.configuration(),"theta":theta.tolist(),
           "token_info":tensor_record(record)[4],"angles":angles.tolist(),"features":features.tolist(),
           "state":{"real":state.real.tolist(),"imag":state.imag.tolist()},
           "predicted_values_normalized":prediction[0].cpu().tolist(),
           "path_result":learned_proposal(record,prediction[0,:len(record["text"])+1].cpu().numpy()),
           "blocks":serial(detail["blocks"]),"independent_numpy_features_max_error":max_error,
           "browser_scope":"Live circuit controls recompute token features; stored graph predictions are checkpoint results."}
    save_json(path,trace)


def main(args):
    if args.output.exists():raise FileExistsError(args.output)
    args.output.mkdir(parents=True)
    torch.set_num_threads(2)
    torch.use_deterministic_algorithms(True)
    torch.backends.cuda.matmul.allow_tf32=False
    torch.backends.cudnn.allow_tf32=False
    if args.device.startswith("cuda"):
        if not torch.cuda.is_available():raise RuntimeError("CUDA requested but unavailable")
        torch.cuda.set_per_process_memory_fraction(.1)
    raw=args.dataset.read_bytes();dataset=json.loads(raw)
    train_strings={r["text"] for r in dataset["splits"]["train"]}
    for key in ("validation","test","ood"):
        assert not train_strings.intersection(r["text"] for r in dataset["splits"][key])
    tensors={key:torch_batch(batch_arrays(rows),args.device) for key,rows in dataset["splits"].items()}
    seeds=[int(v) for v in args.seeds.split(",")]
    modes=args.modes.split(",")
    manifest={"schema":"quantum-toricgt-benchmark-v1","dataset_sha256":hashlib.sha256(raw).hexdigest(),
              "source_sha256":source_hashes(),"seeds":seeds,"modes":modes,"epochs":args.epochs,
              "batch_size":args.batch_size,"learning_rate":args.lr,"weight_decay":1e-4,
              "selection":"Lowest validation node MSE within each predeclared run; test and OOD are scored once after selection.",
              "backend":"PyTorch CUDA exact statevector/autograd simulation" if args.device.startswith("cuda") else "PyTorch CPU exact statevector/autograd simulation",
              "quantum_hardware":False,"quantum_advantage_established":False,
              "python":platform.python_version(),"torch":torch.__version__,"numpy":np.__version__,
              "cuda_runtime":torch.version.cuda,"device":args.device,"runs":[]}
    if args.device.startswith("cuda"):manifest["gpu_name"]=torch.cuda.get_device_name()
    save_json(args.output/"protocol.json",manifest)
    for seed in seeds:
        for mode in modes:
            name=f"{mode}-seed{seed}";run_dir=args.output/name;run_dir.mkdir()
            torch.manual_seed(seed);np.random.seed(seed)
            if args.device.startswith("cuda"):torch.cuda.manual_seed_all(seed)
            model=QuantumToricGT(mode,width=args.width,layers=args.layers).to(args.device)
            initial_theta=model.theta.detach().cpu().numpy().copy()
            optimizer=torch.optim.AdamW([p for p in model.parameters() if p.requires_grad],lr=args.lr,weight_decay=1e-4)
            scheduler=torch.optim.lr_scheduler.CosineAnnealingLR(optimizer,T_max=args.epochs,eta_min=args.lr*.1)
            order_rng=np.random.default_rng(seed+10000)
            best_value=float("inf");best_state=None;best_epoch=None;history=[];steps=[];first_gradient=None
            if args.device.startswith("cuda"):
                torch.cuda.synchronize();torch.cuda.reset_peak_memory_stats()
            start=time.perf_counter()
            for epoch in range(args.epochs):
                model.train();total=0.;count=0
                for indices in np.array_split(order_rng.permutation(len(dataset["splits"]["train"])),
                                              int(np.ceil(len(dataset["splits"]["train"])/args.batch_size))):
                    batch=subset(tensors["train"],torch.as_tensor(indices,device=args.device))
                    optimizer.zero_grad(set_to_none=True)
                    loss=node_mse(model(batch),batch)
                    if not bool(torch.isfinite(loss)):raise FloatingPointError(name)
                    loss.backward()
                    if first_gradient is None:
                        first_gradient={"circuit":None if model.theta.grad is None else serial(model.theta.grad),
                                        "angle_encoder_norm":None if model.angle_map.weight.grad is None else float(model.angle_map.weight.grad.norm().detach().cpu())}
                    torch.nn.utils.clip_grad_norm_(model.parameters(),5.0)
                    optimizer.step()
                    value=float(loss.detach().cpu());steps.append(value);total+=value;count+=1
                scheduler.step();model.eval()
                with torch.no_grad():val=float(node_mse(model(tensors["validation"]),tensors["validation"]).cpu())
                if val<best_value:
                    best_value=val;best_epoch=epoch+1
                    best_state={k:v.detach().cpu().clone() for k,v in model.state_dict().items()}
                history.append({"epoch":epoch+1,"train_batch_mean_mse":total/count,"validation_node_mse":val,
                                "learning_rate":optimizer.param_groups[0]["lr"]})
                if epoch==0 or (epoch+1)%10==0:
                    print(json.dumps({"run":name,"epoch":epoch+1,"train":total/count,"validation":val}),flush=True)
            if args.device.startswith("cuda"):torch.cuda.synchronize()
            training_seconds=time.perf_counter()-start
            model.load_state_dict(best_state)
            np.savez_compressed(run_dir/"weights.npz",**{k:v.numpy() for k,v in best_state.items()})
            final_theta=model.theta.detach().cpu().numpy()
            metrics={key:evaluate(model,dataset["splits"][key],tensors[key])
                     for key in ("train","validation","test","ood")}
            sample=subset(tensors["test"],slice(0,min(32,len(dataset["splits"]["test"]))))
            model.eval()
            with torch.no_grad():
                for _ in range(3):model(sample)
                if args.device.startswith("cuda"):torch.cuda.synchronize()
                then=time.perf_counter()
                for _ in range(20):model(sample)
                if args.device.startswith("cuda"):torch.cuda.synchronize()
            inference_ms=1000*(time.perf_counter()-then)/20
            run={"name":name,"seed":seed,**model.configuration(),"selected_epoch":best_epoch,
                 "best_validation_mse":best_value,"training_wall_seconds":training_seconds,
                 "inference_batch_graphs":int(sample["features"].shape[0]),"inference_batch_ms":inference_ms,
                 "initial_theta":initial_theta.tolist(),"trained_theta":final_theta.tolist(),
                 "theta_change_norm":float(np.linalg.norm(final_theta-initial_theta)),
                 "first_gradient":first_gradient,"history":history,"step_losses":steps,"metrics":metrics}
            if args.device.startswith("cuda"):
                run["cuda_peak_allocated_bytes"]=torch.cuda.max_memory_allocated()
                run["cuda_peak_reserved_bytes"]=torch.cuda.max_memory_reserved()
            if mode=="quantum":
                # Encode only this graph so padding is absent in the browser trace.
                one=torch_batch(batch_arrays([dataset["splits"]["test"][0]]),args.device)
                export_trace(model,dataset["splits"]["test"][0],one,run_dir/"trace.json")
            save_json(run_dir/"run.json",run)
            summary={k:v for k,v in run.items() if k not in {"history","step_losses","metrics","first_gradient","initial_theta","trained_theta"}}
            summary["metrics"]={split:{k:v for k,v in m.items() if k!="examples"} for split,m in metrics.items()}
            summary["record"]=f"{name}/run.json"
            summary["record_sha256"]=hashlib.sha256((run_dir/"run.json").read_bytes()).hexdigest()
            summary["weights_sha256"]=hashlib.sha256((run_dir/"weights.npz").read_bytes()).hexdigest()
            manifest["runs"].append(summary)
            save_json(args.output/"benchmark.json",manifest)
            print(json.dumps({"completed":name,"test":summary["metrics"]["test"],"seconds":training_seconds}),flush=True)
            del model,optimizer,best_state
            if args.device.startswith("cuda"):torch.cuda.empty_cache()
    quantum=[r for r in manifest["runs"] if r["mode"]=="quantum"]
    if quantum:
        representative=min(quantum,key=lambda r:r["best_validation_mse"])
        manifest["representative_trace"]=f"{representative['name']}/trace.json"
    manifest["aggregate"]={}
    for mode in modes:
        runs=[r for r in manifest["runs"] if r["mode"]==mode]
        manifest["aggregate"][mode]={}
        for split in ("test","ood"):
            manifest["aggregate"][mode][split]={}
            for metric in ("node_rmse_cost","source_cost_rmse","mean_proposal_regret_cost","optimal_proposal_fraction","initial_certificate_fraction"):
                values=[r["metrics"][split][metric] for r in runs]
                manifest["aggregate"][mode][split][metric]={"mean":float(np.mean(values)),
                    "sample_std":float(np.std(values,ddof=1)) if len(values)>1 else None,"values":values}
    save_json(args.output/"benchmark.json",manifest)
    print(json.dumps({"complete":True,"output":str(args.output),"runs":len(manifest["runs"])}),flush=True)


if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--dataset",type=Path,required=True);parser.add_argument("--output",type=Path,required=True)
    parser.add_argument("--device",default="cuda");parser.add_argument("--seeds",default="17,29,43")
    parser.add_argument("--modes",default="quantum,classical,frozen");parser.add_argument("--epochs",type=int,default=80)
    parser.add_argument("--batch-size",type=int,default=32);parser.add_argument("--width",type=int,default=24)
    parser.add_argument("--layers",type=int,default=2);parser.add_argument("--lr",type=float,default=.0015)
    main(parser.parse_args())
