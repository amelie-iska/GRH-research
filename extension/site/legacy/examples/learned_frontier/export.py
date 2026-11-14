#!/usr/bin/env python3
"""Read-only checkpoint/trajectory export into the existing architecture DAG schema."""
from pathlib import Path
import sys,json,hashlib,math,argparse
import numpy as np
import torch
from generative import ROOT,HybridField,apply_gate,schedule
sys.path.insert(0,str(ROOT/'examples/architecture'))
from trace_schema import Trace,source


def digest(path):return hashlib.sha256(path.read_bytes()).hexdigest()


@torch.no_grad()
def trace_checkpoint(run,record,output):
    checkpoint=run/record['checkpoint'];assert digest(checkpoint)==record['checkpoint_sha256']
    saved=torch.load(checkpoint,weights_only=True,map_location='cpu');model=HybridField(saved['dimension'],saved['entangle']);model.load_state_dict(saved['state_dict']);model.eval()
    identity='generative-'+record['objective']+('-entangled' if saved['entangle'] else '-product')
    trace=Trace(identity,record['objective'].title()+' / '+record['architecture'],'quantum-generative-rg',dict(kind='trained-checkpoint-replay',seed=record['seed'],checkpoint=source(checkpoint),implementation=source(__file__),training_source=source('examples/learned_frontier/generative.py'),backend='TorchCUDA training; exact four-qubit differentiable simulation; CPU checkpoint replay',scope='Classical learned sampler with quantum features of the actual reduced-Gibbs Z measurement marginal; not coherent quantum denoising or GRH'),dict(linear='xW^T+b',wires='Four auxiliary feature qubits;qubit0mostsignificant',Zmask='bit0 labels leastsignificant basis bit, hence qubit3',physical_model='Genus2 clean dessin K2,5 quantum matter; trace white spins and retain black0,black1',parameter_note='Final RZ phases are invisible to the final all-Z readout; nominal parameter budget is not effective capacity'))
    trace.data['input']=dict(surface_m=5,physical_sites=7,retained_sites=[0,1],feature_qubits=4)
    x=torch.tensor([[.2,-.4]]);t=torch.tensor([[.5]]);context=torch.cat([x,t,torch.sin(2*math.pi*t),torch.cos(2*math.pi*t),torch.sin(4*math.pi*t),torch.cos(4*math.pi*t)],1)
    trace.add('retained_coordinates',x.numpy(),'Retained black-spin noisy measurement coordinates',axes=['batch','retained_spin'])
    trace.add('time',t.numpy(),'Diffusion/flow interpolation time',axes=['batch','time'])
    trace.add('context',context.numpy(),'[x,t,sin2πt,cos2πt,sin4πt,cos4πt]',['retained_coordinates','time'],['batch','channel'])
    for name,parameter in model.named_parameters():trace.add('weight.'+name,parameter.numpy(),'Saved trained parameter',axes=[f'axis{i}' for i in range(parameter.ndim)])
    raw=model.encoder(context);angles=math.pi*torch.tanh(raw)
    trace.add('encoder',raw.numpy(),'context W_encoder^T+b_encoder',['context','weight.encoder.weight','weight.encoder.bias'],['batch','qubit'])
    trace.add('angles',angles.numpy(),'π tanh(encoder)',['encoder'],['batch','qubit'])
    state=torch.zeros(1,16,dtype=torch.complex64);state[:,0]=1;last=trace.add('feature.input',state[0].numpy(),'Auxiliary |0000>',axes=['basis'])
    step=0
    for layer in range(2):
        for q in range(4):
            a=angles[:,q]+model.quantum.theta[layer,q,0];c=torch.cos(a/2);s=torch.sin(a/2)
            gate=torch.stack([c,-s,s,c],1).reshape(1,2,2).to(torch.complex64);state=apply_gate(state,gate,q,4)
            last=trace.add(f'feature.gate{step}',state[0].numpy(),'RY on auxiliary feature qubit',[last,'angles','weight.quantum.theta'],['basis'],gate='RY',wires=[q],angle=float(a[0]));step+=1
            phase=angles[:,q]*.37+model.quantum.theta[layer,q,1];gate=torch.diag_embed(torch.stack([torch.exp(-.5j*phase),torch.exp(.5j*phase)],1));state=apply_gate(state,gate,q,4)
            last=trace.add(f'feature.gate{step}',state[0].numpy(),'RZ; final-layer diagonal phase invisible to all-Z expectations',[last,'angles','weight.quantum.theta'],['basis'],gate='RZ',wires=[q],angle=float(phase[0]));step+=1
        if saved['entangle']:
            for q in range(4):
                state=state[:,getattr(model.quantum,f'perm{q}')]
                last=trace.add(f'feature.gate{step}',state[0].numpy(),'CNOT ring on auxiliary feature qubits',[last],['basis'],gate='CNOT',wires=[q,(q+1)%4],angle=None);step+=1
    features=(state.real.square()+state.imag.square())@model.quantum.observables
    trace.check('gate_replay',float(abs(features-model.quantum(angles)).max()),1e-6)
    trace.add('Z_features',features.numpy(),'Fifteen commuting Z-string expectations',[last],['batch','feature'])
    joined=torch.cat([context,features],1);trace.add('joined',joined.numpy(),'Concatenate context and measured features',['context','Z_features'],['batch','channel'])
    hidden=joined;previous='joined'
    for i,layer in enumerate(model.head):
        hidden=layer(hidden)
        inputs=[previous]+([f'weight.head.{i}.weight',f'weight.head.{i}.bias'] if isinstance(layer,torch.nn.Linear) else [])
        previous=trace.add(f'head.{i}',hidden.numpy(),'xW^T+b' if isinstance(layer,torch.nn.Linear) else 'SiLU(x)',inputs,['batch','channel'])
    trace.check('head_replay',float(abs(hidden-model(x,t)).max()),1e-6)
    payload=json.dumps(trace.finish(),indent=2)+'\n';sha=hashlib.sha256(payload.encode()).hexdigest();path=output/'records'/(identity+'-'+sha[:16]+'.json');path.parent.mkdir(parents=True,exist_ok=True)
    if path.exists():assert path.read_text()==payload
    else:path.write_text(payload)
    # Actual learned paths: each row is one paired trajectory, including time.
    torch.manual_seed(20261104);position=torch.randn(128,2);paths=[dict(time=0.,points=position.tolist())]
    if record['objective']=='flow':
        for k in range(128):
            tt=torch.full((128,),(k/128));v=model(position,tt);nxt=position+v/128
            position+=(v+model(nxt,torch.full((128,),(k+1)/128)))/256
            if (k+1)%8==0:paths.append(dict(time=(k+1)/128,points=position.tolist()))
    else:
        beta,alpha,ab=schedule(64,'cpu')
        for k in range(64,0,-1):
            eps=model(position,torch.full((128,),k/64));mu=(position-beta[k-1]/(1-ab[k]).sqrt()*eps)/alpha[k-1].sqrt();var=beta[k-1]*(1-ab[k-1])/(1-ab[k])
            position=mu+(var.sqrt()*torch.randn_like(position) if k>1 else 0)
            if (64-k+1)%4==0:paths.append(dict(time=(64-k+1)/64,points=position.tolist()))
    return dict(id=identity,title=trace.data['title'],category=trace.data['category'],kind='trained-checkpoint-replay',file=str(path.relative_to(output)),sha256=sha),dict(id=identity,objective=record['objective'],architecture=record['architecture'],paths=paths,metrics=record['evaluation'])


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--run',type=Path,required=True);parser.add_argument('--output',type=Path,required=True);args=parser.parse_args();args.output.mkdir(parents=True,exist_ok=True)
    saved=json.loads((args.run/'record.json').read_text());entries=[];paths=[]
    for record in saved['records']:
        e,p=trace_checkpoint(args.run,record,args.output);entries.append(e);paths.append(p)
    (args.output/'manifest.json').write_text(json.dumps(dict(schema_version=1,traces=entries),indent=2)+'\n')
    (args.output/'lab.json').write_text(json.dumps(dict(seed=saved['seed'],hardware=saved['hardware'],teacher=saved['teacher'],probabilities=saved['probabilities'],gaussian_baseline=saved['gaussian_baseline'],target_control=saved['independent_target_control'],models=paths),indent=2)+'\n')
    print('Four checkpoint DAGs, gate/head replay checks and actual128paired trajectories exported')


if __name__=='__main__':main()
