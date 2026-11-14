"""Small trainable Weyl-feature graph transformer; no training at import.

This original implementation follows the documented ToricGT ingredients
(node/edge tokens, endpoint structure, max-plus attention, four Soft-MoE
experts), with a new jointly trained finite quantum feature encoder.
"""
from __future__ import annotations
import math
import torch
from torch import nn
from torch.nn import functional as F

FEATURE_DIM = 8


def quantum_features(angles, theta, return_state=False):
    """angles:[...,6], theta:[2,3,2]; qubit0 is the most-significant bit.

    Each parameter occurs in one Pauli rotation per token. U is the q=8
    clock, V the backward cyclic shift. All six returned features are real.
    """
    if angles.shape[-1] != 6 or theta.shape != (2,3,2):
        raise ValueError("Expected angles[...,6] and theta[2,3,2]")
    cdtype = torch.complex128 if angles.dtype == torch.float64 else torch.complex64
    index = torch.arange(8, device=angles.device)
    state = F.one_hot(torch.zeros(angles.shape[:-1],dtype=torch.long,device=angles.device),8).to(cdtype)
    for layer in range(2):
        for q in range(3):
            bit = ((index >> (2-q)) & 1).to(angles.dtype)
            angle = angles[...,q] + theta[layer,q,0]
            c, s = torch.cos(angle/2)[...,None], torch.sin(angle/2)[...,None]
            flipped = state.index_select(-1,index ^ (1 << (2-q)))
            state = c*state + (2*bit-1)*s*flipped
            angle = angles[...,q+3] + theta[layer,q,1]
            state = state * torch.exp(.5j*(2*bit-1)*angle[...,None])
        for control,target in ((0,1),(1,2)):
            perm = index ^ (((index >> (2-control)) & 1) << (2-target))
            state = state.index_select(-1,perm)
    clock = torch.exp((2j*torch.pi/8)*index.to(angles.dtype))
    shifted = state.index_select(-1,(index+1)%8)
    ev_u = (state.conj()*clock*state).sum(-1)
    ev_v = (state.conj()*shifted).sum(-1)
    ev_uv = (state.conj()*clock*shifted).sum(-1)
    values = torch.stack([part for z in (ev_u,ev_v,ev_uv) for part in (z.real,z.imag)],dim=-1)
    return (values,state) if return_state else values


def classical_features(angles,theta):
    """Six bounded trigonometric features with exactly12 learned phase parameters."""
    p=theta.reshape(12)
    return .5*(torch.sin(angles+p[:6])+torch.cos(torch.roll(angles,1,dims=-1)+p[6:]))


def normalized_exp(logits, mask, axis):
    masked=logits.masked_fill(~mask,-1e9)
    numerator=torch.exp(masked-masked.amax(dim=axis,keepdim=True))*mask.to(logits.dtype)
    return numerator/numerator.sum(dim=axis,keepdim=True).clamp_min(1e-12)


class SoftExperts(nn.Module):
    """Four experts, two slots each: dispatch over tokens, combine over slots."""
    def __init__(self,width):
        super().__init__()
        self.keys=nn.Parameter(torch.randn(8,width)/math.sqrt(width))
        self.scale=nn.Parameter(torch.tensor(0.0))
        self.residual=nn.Parameter(torch.tensor(.1))
        self.experts=nn.ModuleList([nn.Sequential(nn.Linear(width,2*width),nn.GELU(),
                                                 nn.Linear(2*width,width)) for _ in range(4)])

    def forward(self,x,valid,details=False):
        logits=self.scale.exp()*torch.einsum("btd,sd->bts",F.normalize(x,dim=-1,eps=1e-6),
                                            F.normalize(self.keys,dim=-1,eps=1e-6))
        mask=valid[...,None].expand_as(logits)
        dispatch=normalized_exp(logits,mask,axis=1)
        slots=torch.einsum("bts,btd->bsd",dispatch,x).reshape(x.shape[0],4,2,x.shape[-1])
        processed=torch.stack([expert(slots[:,j]) for j,expert in enumerate(self.experts)],dim=1)
        processed=processed.reshape(x.shape[0],8,x.shape[-1])
        combine=torch.softmax(logits,dim=-1)*valid[...,None]
        out=self.residual*torch.einsum("bts,bsd->btd",combine,processed)
        diagnostic={"dispatch":dispatch,"combine":combine,"slots":slots} if details else None
        return out,diagnostic


class GraphBlock(nn.Module):
    def __init__(self,width=24,heads=2):
        super().__init__()
        self.width,self.heads=width,heads
        self.norm1,self.norm2=nn.LayerNorm(width),nn.LayerNorm(width)
        self.qkv=nn.Linear(width,3*width)
        self.output=nn.Linear(width,width)
        self.mix=nn.Parameter(torch.tensor(0.0))
        self.incidence_scale=nn.Parameter(torch.tensor(-1.0))
        self.experts=SoftExperts(width)

    def forward(self,x,incidence,valid,details=False):
        b,t,d=x.shape
        split=lambda z:z.reshape(b,t,self.heads,d//self.heads).transpose(1,2)
        q,k,v=[split(z) for z in self.qkv(self.norm1(x)).chunk(3,dim=-1)]
        q=F.normalize(q-q.amax(dim=-1,keepdim=True),dim=-1,eps=1e-6)
        k=F.normalize(k-k.amax(dim=-1,keepdim=True),dim=-1,eps=1e-6)
        scores=torch.matmul(q,k.transpose(-1,-2))/math.sqrt(d//self.heads)
        scores=scores+F.softplus(self.incidence_scale)*incidence[:,None,:,:]
        legal=valid[:,None,:,None]&valid[:,None,None,:]
        weights=normalized_exp(scores,legal.expand_as(scores),axis=-1)
        soft=torch.matmul(weights,v)
        candidates=scores[...,None]+v[:,:,None,:,:]
        tropical=candidates.masked_fill(~legal[...,None],-1e9).amax(dim=-2)
        tropical=tropical*valid[:,None,:,None]
        gate=torch.sigmoid(self.mix)
        context=gate*soft+(1-gate)*tropical
        merged=context.transpose(1,2).reshape(b,t,d)
        x=(x+self.output(merged))*valid[...,None]
        moe,route=self.experts(self.norm2(x),valid,details)
        x=(x+moe)*valid[...,None]
        diagnostic=None
        if details:
            diagnostic={"scores":scores,"softmax_weights":weights,"tropical_context":tropical,
                        "softmax_mix":gate,"routing":route}
        return x,diagnostic


class QuantumToricGT(nn.Module):
    def __init__(self,mode="quantum",width=24,layers=2):
        super().__init__()
        if mode not in {"quantum","classical","frozen"}:
            raise ValueError(mode)
        self.mode,self.width,self.layers=mode,width,layers
        self.angle_map=nn.Linear(FEATURE_DIM,6)
        self.theta=nn.Parameter(torch.randn(2,3,2)*.15,requires_grad=mode!="frozen")
        if mode=="frozen":
            for parameter in self.angle_map.parameters():
                parameter.requires_grad_(False)
        self.input_map=nn.Linear(FEATURE_DIM,width)
        self.feature_map=nn.Linear(6,width)
        self.blocks=nn.ModuleList([GraphBlock(width) for _ in range(layers)])
        self.norm=nn.LayerNorm(width)
        self.readout=nn.Sequential(nn.Linear(width,width),nn.GELU(),nn.Linear(width,1))

    def forward(self,batch,details=False,feature_override=None):
        raw,valid,incidence=batch["features"],batch["valid"],batch["incidence"]
        angles=torch.pi*torch.tanh(self.angle_map(raw))
        state=None
        if feature_override is not None:
            values=feature_override
        elif self.mode=="classical":
            values=classical_features(angles,self.theta)
        else:
            values,state=quantum_features(angles,self.theta,True)
        values=values*valid[...,None]
        x=(self.input_map(raw)+self.feature_map(values))*valid[...,None]
        diagnostics=[]
        for block in self.blocks:
            x,detail=block(x,incidence,valid,details)
            if details:diagnostics.append(detail)
        out=self.readout(self.norm(x)).squeeze(-1)*valid
        if details:
            return out,{"angles":angles,"features":values,"state":state,
                        "blocks":diagnostics,"hidden":x}
        return out

    def configuration(self):
        return {"mode":self.mode,"width":self.width,"layers":self.layers,
                "qubits_per_quantum_token":3 if self.mode!="classical" else 0,
                "circuit_parameter_count":12 if self.mode!="classical" else 0,
                "feature_phase_parameters":12,"total_parameters":sum(p.numel() for p in self.parameters()),
                "trainable_parameters":sum(p.numel() for p in self.parameters() if p.requires_grad)}


def torch_batch(arrays,device,dtype=torch.float32):
    return {key:torch.as_tensor(value,device=device,dtype=torch.bool if key in {"valid","nodes"} else dtype)
            for key,value in arrays.items()}


def node_mse(prediction,batch):
    return ((prediction-batch["targets"])**2*batch["nodes"]).sum()/batch["nodes"].sum()
