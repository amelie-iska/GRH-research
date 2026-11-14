#!/usr/bin/env python3
"""Actual gate-by-gate replay of the trained coherent purification checkpoint."""
from pathlib import Path
import sys,json,hashlib,math,argparse
import torch,numpy as np
from generative import ROOT,apply_gate,cnot_permutation,physical_teacher
from state_flow import PurificationFlow
sys.path.insert(0,str(ROOT/'examples/architecture'))
from trace_schema import Trace,source


@torch.no_grad()
def main():
    parser=argparse.ArgumentParser();parser.add_argument('--run',type=Path,required=True);parser.add_argument('--output',type=Path,required=True);args=parser.parse_args()
    saved=json.loads((args.run/'record.json').read_text());path=args.run/'state-flow.pt';assert hashlib.sha256(path.read_bytes()).hexdigest()==saved['checkpoint_sha256'];checkpoint=torch.load(path,weights_only=True,map_location='cpu');model=PurificationFlow(checkpoint['depth']);model.load_state_dict(checkpoint['state_dict']);model.eval();time=.5
    trace=Trace('quantum-purification-flow','Learned coherent purification flow','quantum-state-flow-rg',dict(kind='trained-checkpoint-replay',seed=saved['seed'],checkpoint=source(path),training_source=source('examples/learned_frontier/state_flow.py'),implementation=source(__file__),backend='TorchCUDA training and exact CPU gate replay',scope='Known finite target purification, full state supervision; physical system2qubits+ancilla2; no universal channel inverse or GRH'),dict(wires='q0,q1 retained physical blackspins; q2,q3 ancilla; q0mostsignificant',angle='t theta+t² omega',metric='Euclidean complex Hilbert state inner product'))
    trace.data['input']=dict(surface_m=5,physical_sites=7,retained_sites=[0,1],system_qubits=2,ancilla_qubits=2)
    trace.add('time',np.array([time]),'Control time',axes=['time']);trace.add('weight.theta',model.theta.numpy(),'Trained linear time coefficient',axes=['layer','qubit']);trace.add('weight.omega',model.omega.numpy(),'Trained quadratic time coefficient',axes=['layer','qubit'])
    state=torch.zeros(1,16,dtype=torch.complex64);state[:,0]=1;last=trace.add('flow.input',state[0].numpy(),'|0000>',axes=['basis']);counter=0
    def cn(a,b):
        nonlocal state,last,counter
        state=state[:,cnot_permutation(4,a,b,'cpu')];last=trace.add(f'flow.gate{counter}',state[0].numpy(),'CNOT on recorded physical/ancilla wires',[last],['basis'],gate='CNOT',wires=[a,b],angle=None);counter+=1
    def ry(q,angle):
        nonlocal state,last,counter
        c=math.cos(angle/2);s=math.sin(angle/2);state=apply_gate(state,torch.tensor([[[c,-s],[s,c]]],dtype=torch.complex64),q,4);last=trace.add(f'flow.gate{counter}',state[0].numpy(),'RY on recorded physical/ancilla wire',[last,'time','weight.theta','weight.omega'],['basis'],gate='RY',wires=[q],angle=angle);counter+=1
    ry(0,math.pi/2);ry(1,math.pi/2);cn(0,2);cn(1,3)
    for layer in range(model.depth):
        pairs=[(q,(q+1+layer%3)%4) for q in range(4)]
        for a,b in pairs:cn(a,b)
        for q in range(4):ry(q,float(time*model.theta[layer,q]+time*time*model.omega[layer,q]))
        for a,b in reversed(pairs):cn(a,b)
    trace.check('state_replay',float(abs(state-model(torch.tensor([time]))).max()),2e-6)
    psi=state.reshape(4,4);rho=psi@psi.T.conj();trace.add('reduced_density',rho.numpy(),'Trace ancilla2qubits of final pure state',[last],['row','column']);trace.add('exact_reduced_target',(torch.eye(4)*(1-time)/4+time*torch.tensor(physical_teacher()['reduced_density'])).numpy(),'Known target density interpolation',axes=['row','column'])
    payload=json.dumps(trace.finish(),indent=2)+'\n';sha=hashlib.sha256(payload.encode()).hexdigest();file=args.output/'records'/('quantum-purification-flow-'+sha[:16]+'.json');file.parent.mkdir(parents=True,exist_ok=True)
    if file.exists():assert file.read_text()==payload
    else:file.write_text(payload)
    p=args.output/'manifest.json';manifest=json.loads(p.read_text());entry=dict(id=trace.data['id'],title=trace.data['title'],category=trace.data['category'],kind='trained-checkpoint-replay',file=str(file.relative_to(args.output)),sha256=sha);manifest['traces']=[x for x in manifest['traces'] if x['id']!=entry['id']]+[entry];p.write_text(json.dumps(manifest,indent=2)+'\n');print('Coherent checkpoint exported:76gates and actual reduced density')


if __name__=='__main__':main()
