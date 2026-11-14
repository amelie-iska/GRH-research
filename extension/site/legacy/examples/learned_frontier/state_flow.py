#!/usr/bin/env python3
"""Learned coherent purification flow for the actual two-spin RG density.
Finite known-teacher control benchmark, not universal inversion of a channel.
"""
from pathlib import Path
import argparse,json,math,time,hashlib
import numpy as np
import torch
from torch import nn
from generative import physical_teacher,apply_gate,cnot_permutation


class PurificationFlow(nn.Module):
    def __init__(self,depth=6):
        super().__init__();self.depth=depth;self.theta=nn.Parameter(.01*torch.randn(depth,4));self.omega=nn.Parameter(.01*torch.randn(depth,4))
        for layer in range(depth):
            # Conjugate each rotation block by a different reversible CNOT circuit.
            pairs=[(q,(q+1+layer%3)%4) for q in range(4)]
            for j,(a,b) in enumerate(pairs):self.register_buffer(f'p{layer}_{j}',cnot_permutation(4,a,b,'cpu'))

    def forward(self,t,trace=False):
        t=t.flatten();state=torch.zeros(len(t),16,dtype=torch.complex64,device=t.device);state[:,[0,5,10,15]]=.5;steps=[]
        for layer in range(self.depth):
            for j in range(4):state=state[:,getattr(self,f'p{layer}_{j}')]
            for q in range(4):
                angle=t*self.theta[layer,q]+t.square()*self.omega[layer,q];c=torch.cos(angle/2);s=torch.sin(angle/2)
                gate=torch.stack([c,-s,s,c],1).reshape(-1,2,2).to(torch.complex64);state=apply_gate(state,gate,q,4)
            for j in reversed(range(4)):state=state[:,getattr(self,f'p{layer}_{j}')]
            if trace:steps.append(state.detach().cpu().numpy())
        return (state,steps) if trace else state


def target_states(t,rho):
    value,U=torch.linalg.eigh(rho)
    diagonal=((1-t[:,None])/4+t[:,None]*value[None]).sqrt()
    root=torch.einsum('ai,bi,ci->bac',U,diagonal,U)
    return root.reshape(-1,16).to(torch.complex64)


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--output',required=True,type=Path);parser.add_argument('--device',default='cuda');parser.add_argument('--steps',type=int,default=2000);args=parser.parse_args()
    if args.output.exists():raise SystemExit('New output directory required')
    args.output.mkdir(parents=True);torch.manual_seed(20261104);start=time.perf_counter();device=torch.device(args.device)
    teacher=physical_teacher(device);rho=torch.tensor(teacher['reduced_density'],device=device,dtype=torch.float32);net=PurificationFlow().to(device);opt=torch.optim.Adam(net.parameters(),lr=.025);history=[]
    for step in range(args.steps):
        t=torch.cat([torch.zeros(1,device=device),torch.ones(1,device=device),torch.rand(62,device=device)])
        desired=target_states(t,rho);actual=net(t);fidelity=abs((desired.conj()*actual).sum(1)).square();loss=(1-fidelity).mean()
        opt.zero_grad(set_to_none=True);loss.backward();opt.step()
        if step%100==0 or step==args.steps-1:history.append(dict(step=step,loss=float(loss.detach())))
    with torch.no_grad():
        times=torch.linspace(0,1,33,device=device);ideal=target_states(times,rho);actual=net(times);fidelity=abs((ideal.conj()*actual).sum(1)).square()
        psi=actual.reshape(-1,4,4);reduced=psi@psi.transpose(1,2).conj();wanted=(1-times[:,None,None])*torch.eye(4,device=device)/4+times[:,None,None]*rho
        errors=torch.linalg.matrix_norm(reduced-wanted);norms=actual.abs().square().sum(1)
        assert float(abs(norms-1).max())<2e-5
        assert float(torch.linalg.eigvalsh(reduced).min())>-1e-6
        assert float(abs(actual[0]-ideal[0]).max())<1e-6
        rows=[dict(t=float(t),fidelity=float(f),density_error=float(e),density_real=r.real.cpu().tolist(),density_imag=r.imag.cpu().tolist()) for t,f,e,r in zip(times,fidelity,errors,reduced)]
    path=args.output/'state-flow.pt';torch.save(dict(state_dict=net.state_dict(),depth=net.depth,seed=20261104),path)
    result=dict(seed=20261104,device=args.device,gpu=torch.cuda.get_device_name(0) if args.device=='cuda' else None,steps=args.steps,batch=64,depth=net.depth,feature_qubits=4,system_qubits=2,ancilla_qubits=2,nominal_parameters=sum(p.numel() for p in net.parameters()),wall_seconds=time.perf_counter()-start,history=history,min_grid_fidelity=float(fidelity.min()),max_grid_density_error=float(errors.max()),rows=rows,theta=net.theta.detach().cpu().tolist(),omega=net.omega.detach().cpu().tolist(),checkpoint_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),scope='Trained coherent4qubit variational state-preparation flow on a known finite Gibbs-RG density family. It fits full target purifications with ideal state access, not measured-only supervision or universal CPTP denoising; finite-grid accuracy is not uniform certification or GRH.')
    (args.output/'record.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:result[k] for k in ['steps','min_grid_fidelity','max_grid_density_error','wall_seconds']}))


if __name__=='__main__':main()
