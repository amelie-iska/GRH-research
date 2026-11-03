"""Small fixed-weight graph models matching the audited upstream core formulas.

These are original NumPy references, not loaded upstream trained checkpoints.
No PyTorch dependency is needed; dropout and optional polar compression are off.
"""
import math
import numpy as np
from scipy.special import erf
from trace_schema import ROOT, Trace, source

SEED = 20261106
PIN = "a5199bc989a6fb170e21220e5e87bf95bc2fc0b4"
SOURCE_FILES = ["graph_tokenizer.py", "tropical_attention.py", "soft_moe.py", "toric_algebra.py"]
D = 6
HEADS = 2


def normalize(x, eps=1e-12):
    return x / np.maximum(np.linalg.norm(x, axis=-1, keepdims=True), eps)


def softmax(x, mask, axis):
    mask = np.broadcast_to(mask, x.shape)
    m = np.max(np.where(mask, x, -np.inf), axis=axis, keepdims=True)
    m = np.where(np.isfinite(m), m, 0)
    exp = np.exp(np.where(mask, x-m, -np.inf))
    return exp / np.maximum(exp.sum(axis=axis, keepdims=True), 1e-12)


def layernorm(x):
    return (x-x.mean(axis=-1, keepdims=True)) / np.sqrt(x.var(axis=-1, keepdims=True)+1e-5)


def gelu(x):
    return x * (1 + erf(x / np.sqrt(2))) / 2


def fixture():
    """One three-edge graph with a fourth padded node; explicit absolute IDs."""
    rng = np.random.default_rng(SEED)
    shapes = dict(node_proj=(2,D), node_bias=(D,), edge_proj=(1,D), edge_bias=(D,),
        type_emb=(2,D), node_id=(4,D), edge_id=(3,D), toric_proj=(4,D), toric_bias=(D,),
        endpoint_proj=(2*D,D), endpoint_bias=(D,), qkv=(D,3*D), qkv_bias=(3*D,),
        attention_out=(D,D), attention_bias=(D,), ff1=(D,12), ff1_bias=(12,),
        ff2=(12,D), ff2_bias=(D,), slot_keys=(2,1,D),
        expert_w1=(2,D,12), expert_b1=(2,12), expert_w2=(2,12,D), expert_b2=(2,D),
        node_head=(D,2), edge_head=(D,2), graph_head=(D,2))
    w = {k: rng.normal(0, .35, size=shape) for k, shape in shapes.items()}
    x = np.array([[[.2,1.1],[-.8,.3],[.9,-.5],[0,0]]])
    e = np.array([[[.7],[1.2],[-.4]]])
    endpoints = np.array([[0,1],[1,2],[2,0]])
    mask = np.array([[True, True, True, False, True, True, True]])
    return w, x, e, endpoints, mask


def tokenizer(w, x, e, endpoints):
    theta = (np.sqrt(5)-1)/2
    angles = 2*np.pi*theta*np.arange(4)[:,None]*np.arange(1,3)[None,:]
    phase = np.concatenate([np.sin(angles),np.cos(angles)], axis=-1)
    nt = x@w["node_proj"]+w["node_bias"]+w["type_emb"][0]+w["node_id"]+phase@w["toric_proj"]+w["toric_bias"]
    end = np.concatenate([w["node_id"][endpoints[:,0]],w["node_id"][endpoints[:,1]]],axis=-1)
    et = e@w["edge_proj"]+w["edge_bias"]+w["type_emb"][1]+w["edge_id"]+end@w["endpoint_proj"]+w["endpoint_bias"]
    return np.concatenate([nt,et],axis=1), phase, end


def attention(x, mask, w, mode, ranks=None):
    b, length, d = x.shape
    projected = x@w["qkv"]+w["qkv_bias"]
    raw = [a.reshape(b,length,HEADS,d//HEADS).transpose(0,2,1,3) for a in np.split(projected,3,axis=-1)]
    q, k, v = raw
    q = normalize(q-q.max(axis=-1,keepdims=True)); k = normalize(k-k.max(axis=-1,keepdims=True))
    scores = q@k.swapaxes(-1,-2)/np.sqrt(d//HEADS)
    legal = mask[:,None,:,None]&mask[:,None,None,:]
    if ranks is not None:
        legal = legal & (ranks[:,None,None,:] <= ranks[:,None,:,None])
    legal = np.broadcast_to(legal, scores.shape)
    weights = softmax(scores,legal,-1)
    terms = scores[...,None]+v[:,:,None,:,:]
    masked = np.where(legal[...,None],terms,-np.inf)
    dense = np.max(masked,axis=-2)
    valid = legal.any(axis=-1,keepdims=True)
    dense = np.where(valid,dense,0)
    # Keep every maximizer per (batch,head,query,coordinate), including ties.
    winners = legal[...,None] & (terms == dense[...,None,:])
    block_values = [np.max(masked[:,:,:,start:start+2,:],axis=-2) for start in range(0,length,2)]
    ring = np.where(valid,np.max(block_values,axis=0),0)
    context = weights@v if mode == "softmax" else ring if mode == "tropical_ring" else dense
    gate = 1/(1+np.exp(2.2))
    merged = (context*gate).transpose(0,2,1,3).reshape(b,length,d)
    output = merged@w["attention_out"]+w["attention_bias"]
    return dict(projected=projected, q_raw=raw[0], k_raw=raw[1], value=v, query=q, key=k,
        scores=scores, legal=legal, weights=weights, winners=winners, context=context,
        block_contexts=np.where(np.isfinite(block_values),block_values,0),
        block_valid=np.stack([legal[:,:,:,s:s+2].any(axis=-1) for s in range(0,length,2)]),
        ring=ring,dense=dense, merged=merged, output=output)


def experts(slots,w):
    # Expert axis is penultimate before (slot,feature), for ordinary or causal slots.
    return np.stack([gelu(slots[...,e,:,:]@w["expert_w1"][e]+w["expert_b1"][e])@w["expert_w2"][e]+w["expert_b2"][e] for e in range(2)],axis=-3)


def moe(x, mask, w, causal=False):
    # Match F.normalize(...,eps=1e-6) used in the pinned Soft-MoE source.
    logits = np.einsum("bld,esd->bles",normalize(x,1e-6),normalize(w["slot_keys"],1e-6))
    combine = softmax(logits.reshape(*x.shape[:2],-1),np.ones((*x.shape[:2],2),bool),-1).reshape(logits.shape)*mask[:,:,None,None]
    if not causal:
        dispatch = softmax(logits,mask[:,:,None,None],axis=1)
        slots = np.einsum("bles,bld->besd",dispatch,x)
        out_slots = experts(slots,w)
        output = .1*np.einsum("bles,besd->bld",combine,out_slots)
        return dict(logits=logits,dispatch=dispatch,slots=slots,expert_outputs=out_slots,combine=combine,output=output)
    flat = logits.reshape(*x.shape[:2],-1)
    weights = np.exp(flat-flat.max(axis=-1,keepdims=True))*mask[:,:,None]
    # Rowwise centering before the prefix sum is part of the actual upstream rule.
    num = np.cumsum(weights[:,:,:,None]*x[:,:,None,:],axis=1)
    den = np.cumsum(weights,axis=1)
    strict_num = np.concatenate([np.zeros_like(num[:,:1]),num[:,:-1]],axis=1)
    strict_den = np.concatenate([np.zeros_like(den[:,:1]),den[:,:-1]],axis=1)
    slots = (strict_num/np.maximum(strict_den[:,:,:,None],1e-6)).reshape(*x.shape[:2],2,1,D)
    out_slots = experts(slots,w)
    output = np.einsum("bles,blesd->bld",combine,out_slots)
    return dict(logits=logits,prefix_weights=weights,strict_numerator=strict_num,
                strict_denominator=strict_den,slots=slots,expert_outputs=out_slots,combine=combine,output=output)


def build(identity, modes, feedforward="mlp", causal=False):
    w, x, e, endpoints, mask = fixture()
    t = Trace(identity, identity.replace("-"," ").title(), "classical-"+identity,
        dict(kind="fixed-weight-reference", seed=SEED, weights="Seeded didactic weights exported below; no upstream trained-checkpoint claim",
             implementation=source(__file__), upstream_commit=PIN,
             upstream_sources=[source("external/ToricGT/src/toricgt/"+f) for f in SOURCE_FILES],
             backend="NumPy/SciPy CPU; audited source formulas, upstream PyTorch model not executed",
             scope="Miniature finite graph reference; optional polarquant/dropout/GPU/distributed training disabled"),
        dict(linear="right multiplication X W + b; weights stored input-by-output",
             batch=1,tokens="4 node positions (one padded), then 3 edge positions",d_model=D,heads=HEADS,
             identifiers="Absolute ID/torus metadata; permutation claims require transporting this metadata",
             layernorm="identity affine parameters; population variance plus epsilon=1e-5",
             attention="max-shift and L2 normalize Q/K; ordinary dot scores, max-plus aggregation only in tropical modes"))
    for key,value in w.items():
        t.add("weight."+key,value,"Fixed seeded parameter (no training)")
    nx=t.add("node_features",x,"Input node features",axes=["batch","node","feature"])
    ex=t.add("edge_features",e,"Input edge features",axes=["batch","edge","feature"])
    t.add("endpoints",endpoints,"Ordered edge endpoints",axes=["edge","endpoint"])
    mn=t.add("token_mask",mask,"True means a valid token",axes=["batch","token"])
    state,phase,end = tokenizer(w,x,e,endpoints)
    t.add("torus_phase",phase,"concat(sin(2 pi theta i r),cos(...)), r=1,2",axes=["node","coordinate"])
    t.add("endpoint_ids",end,"Concatenated learned source/destination ID embeddings",["endpoints","weight.node_id"],["edge","feature"])
    last=t.add("tokens",state,"Concat node/edge projections + IDs + type + torus/endpoint projections",
        [nx,ex,"torus_phase","endpoint_ids"]+["weight."+k for k in ["node_proj","node_bias","edge_proj","edge_bias","type_emb","node_id","edge_id","toric_proj","toric_bias","endpoint_proj","endpoint_bias"]],
        ["batch","token","channel"])
    t.data["surface_context"]=dict(example="elliptic theta dessin",sigma=[[0,1,2],[3,4,5]],
        alpha=[[0,3],[1,4],[2,5]],genus=1,completed_order_rank_over_DVR=18,
        carrier="one permitted three-cycle; fourth position is padding, not another dessin edge",
        boundary="Finite token graph forgets the second branch and alpha-gluing; no faithful representation of the infinite surface algebra/order is asserted")
    ranks=np.array([[0,1,2,2**30,1,2,2]]) if causal else None
    if causal:t.add("causal_rank",ranks,"Endpoint maximum ranks for edge tokens; key rank <= query rank",axes=["batch","token"])
    for layer,mode in enumerate(modes):
        prefix=f"layer{layer}"
        norm=layernorm(state)
        ln=t.add(prefix+".norm",norm,"LayerNorm before attention",[last],["batch","token","channel"])
        a=attention(norm,mask,w,mode,ranks)
        node_ids={}
        for key in ["projected","q_raw","k_raw","value","query","key","scores","legal","weights","winners","context","block_contexts","block_valid","merged","output"]:
            formula={"query":"L2normalize(Q_raw-max_channel(Q_raw))", "key":"L2normalize(K_raw-max_channel(K_raw))",
                "scores":"Q K^T / sqrt(head_dim)","legal":"valid(query) and valid(key), with optional causal rank",
                "weights":"softmax over legal key tokens; empty rows zero (used by softmax mode)",
                "winners":"All legal key maximizers per output coordinate; ties retained (tropical diagnostic)",
                "context":"weights V" if mode=="softmax" else "max_legal_key(scores + V)",
                "block_contexts":"Key blocks of size 2; invalid block entries zero, interpreted with block_valid",
                "block_valid":"Whether a key block contains any legal key per query",
                "merged":"Concatenate heads after sigmoid(-2.2) gating", "output":"merged W_out + b_out"}.get(key,key)
            parent_names={"projected":[ln,"weight.qkv","weight.qkv_bias"],
                "q_raw":[prefix+".projected"],"k_raw":[prefix+".projected"],"value":[prefix+".projected"],
                "query":[prefix+".q_raw"],"key":[prefix+".k_raw"],
                "scores":[prefix+".query",prefix+".key"],
                "legal":[mn]+(["causal_rank"] if causal else []),
                "weights":[prefix+".scores",prefix+".legal"],
                "winners":[prefix+".scores",prefix+".value",prefix+".legal"],
                "context":[prefix+".weights",prefix+".value"] if mode=="softmax" else [prefix+".scores",prefix+".value",prefix+".legal"],
                "block_contexts":[prefix+".scores",prefix+".value",prefix+".legal"],
                "block_valid":[prefix+".legal"],"merged":[prefix+".context"],
                "output":[prefix+".merged","weight.attention_out","weight.attention_bias"]}
            axes={"projected":["batch","token","qkv_channel"],
                "scores":["batch","head","query_token","key_token"],"legal":["batch","head","query_token","key_token"],
                "weights":["batch","head","query_token","key_token"],"winners":["batch","head","query_token","key_token","head_channel"],
                "block_contexts":["block","batch","head","query_token","head_channel"],"block_valid":["block","batch","head","query_token"],
                "merged":["batch","token","channel"],"output":["batch","token","channel"]}.get(key,["batch","head","token","head_channel"])
            node_ids[key]=t.add(prefix+"."+key,a[key],formula,parent_names[key],axes,mode=mode)
        t.check(prefix+".ring_dense_agreement",np.max(abs(a["ring"]-a["dense"])))
        t.check(prefix+".attention_rows",np.max(abs(a["weights"].sum(axis=-1)-a["legal"].any(axis=-1))))
        t.check(prefix+".padded_query_zero_context",np.max(abs(a["context"][:,:,~mask[0],:])))
        state=state+a["output"]
        residual=t.add(prefix+".residual",state,"X + projected attention; bias can be nonzero on padding",[last,node_ids["output"]],["batch","token","channel"])
        norm=layernorm(state)
        fn=t.add(prefix+".ff_norm",norm,"LayerNorm before feed-forward",[residual],["batch","token","channel"])
        if feedforward=="mlp":
            hidden=gelu(norm@w["ff1"]+w["ff1_bias"])
            hn=t.add(prefix+".hidden",hidden,"GELU(LN(X) W1+b1)",[fn,"weight.ff1","weight.ff1_bias"],["batch","token","hidden"])
            update=hidden@w["ff2"]+w["ff2_bias"]
            un=t.add(prefix+".ff_output",update,"hidden W2+b2",[hn,"weight.ff2","weight.ff2_bias"],["batch","token","channel"])
        else:
            m=moe(norm,mask,w,causal=causal)
            mids={}
            for key,value in m.items():
                formula={"dispatch":"Softmax over valid TOKENS for each expert-slot", "combine":"Softmax over EXPERT-SLOTS for each valid token",
                    "slots":"Strict earlier-token weighted averages" if causal else "dispatch^T X",
                    "output":"Combine expert-slot outputs; scale=1" if causal else "0.1 * combine * expert-slot outputs"}.get(key,key)
                mp=prefix+".moe."
                parents={"logits":[fn,"weight.slot_keys"],"dispatch":[mp+"logits",mn],
                    "prefix_weights":[mp+"logits",mn],"strict_numerator":[mp+"prefix_weights",fn],
                    "strict_denominator":[mp+"prefix_weights"],
                    "slots":[mp+"strict_numerator",mp+"strict_denominator"] if causal else [mp+"dispatch",fn],
                    "expert_outputs":[mp+"slots","weight.expert_w1","weight.expert_b1","weight.expert_w2","weight.expert_b2"],
                    "combine":[mp+"logits",mn],"output":[mp+"combine",mp+"expert_outputs"]}
                axes={"logits":["batch","token","expert","slot"],"dispatch":["batch","token","expert","slot"],
                    "combine":["batch","token","expert","slot"],"prefix_weights":["batch","token","expert_slot"],
                    "strict_numerator":["batch","token","expert_slot","channel"],"strict_denominator":["batch","token","expert_slot"],
                    "slots":["batch","token","expert","slot","channel"] if causal else ["batch","expert","slot","channel"],
                    "expert_outputs":["batch","token","expert","slot","channel"] if causal else ["batch","expert","slot","channel"],
                    "output":["batch","token","channel"]}
                mids[key]=t.add(mp+key,value,formula,parents[key],axes[key])
            update=m["output"];un=mids["output"]
            t.check(prefix+".combine_axis",np.max(abs(m["combine"].sum(axis=(-2,-1))-mask)))
            t.check(prefix+".padding_update",np.max(abs(update[:,~mask[0],:])))
            empty=moe(norm,np.zeros_like(mask),w,causal)
            t.check(prefix+".all_pad_output",np.max(abs(empty["output"])))
            if causal:
                changed=norm.copy();changed[:,5:,:]+=30
                perturbed=moe(changed,mask,w,True)
                t.check(prefix+".future_invariance",np.max(abs(perturbed["output"][:,:5]-update[:,:5])))
                t.check(prefix+".empty_first_prefix",np.max(abs(m["slots"][:,0])))
            else:t.check(prefix+".dispatch_axis",np.max(abs(m["dispatch"].sum(axis=1)-1)))
        state=state+update
        last=t.add(prefix+".layer_output",state,"Residual + feed-forward update",[residual,un],["batch","token","channel"])
    t.add("node_logits",state[:,:4]@w["node_head"],"Node linear head; inspect only valid nodes",[last,"weight.node_head"],["batch","node","class"])
    t.add("edge_logits",state[:,4:]@w["edge_head"],"Edge linear head",[last,"weight.edge_head"],["batch","edge","class"])
    pooled=(state*mask[:,:,None]).sum(axis=1)/mask.sum(axis=1)[:,None]
    pool=t.add("graph_pool",pooled,"Masked mean over valid node and edge tokens",[last,mn],["batch","channel"])
    t.add("graph_logits",pooled@w["graph_head"],"Graph linear head; no training labels claimed",[pool,"weight.graph_head"],["batch","class"])
    t.data["architecture"]=dict(attention_modes=modes,feedforward=feedforward,causal=causal,layer_weights="Shared between layers in this miniature only; not an upstream default")
    return t.finish()


def all_traces():
    for args in [("tokengt-softmax",["softmax"],"mlp",False),
                 ("tropical-attention",["tropical"],"mlp",False),
                 ("tropical-ring",["tropical_ring"],"mlp",False),
                 ("attention-hybrid",["softmax","tropical_ring"],"mlp",False),
                 ("toricgt-soft-moe",["tropical_ring"],"moe",False),
                 ("causal-soft-moe",["softmax"],"moe",True)]:
        yield build(*args)
