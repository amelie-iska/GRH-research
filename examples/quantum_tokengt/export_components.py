"""Saved learned concept/critic and continuous GFN DAGs; no training at import.

Component axes are classical latent coordinates, never surface vertices or
quantum wires. A main trained record is read byte-for-byte and left intact.
"""
import hashlib,json,sys
import numpy as np
from scipy.special import logsumexp
from model import ROOT,SEED,attention,circuit_features,graph_tokens,teacher
from train import gfn_mu,gfn_tb,gfn_reward,gaussian_log,serial
sys.path.insert(0,str(ROOT/'examples/architecture'))
from trace_schema import Trace,source

def component(identity,title,record,checkpoint,kind):
    t=Trace(identity,title,'quantum-tokengt-rg',dict(kind='trained-checkpoint-replay',seed=record['seed'],checkpoint=source(checkpoint),
        implementation=source(__file__),training_source=source('examples/quantum_tokengt/train.py'),saved_training_sources=record['source_hashes'],
        backend='NumPy/SciPy replay of saved classical learned network; no new optimizer steps',component=kind,
        scope='m5 physical teacher context only; latent feature/control coordinates are not dessin/quiver vertices. No fabricated quantum gates, faithful order representation or quantum advantage.'),
        dict(component=kind,linear='row input x W + b',axes='Classical latent coordinates; no physical spin or qubit identification',
            replay='Saved final parameters; final post-update losses need not equal last pre-update minibatch history loss'))
    t.data['input']=dict(surface_m=5,component=kind,geometry_context_only=True,
        indexing_boundary='Latent coordinates and hidden units are not the five quiver vertices or seven physical spin sites')
    return t

def concept_trace(record,checkpoint):
    c=record['concepts'];normal=record['normalization'];t=component('quantum-tokengt-rg-concept-critic','Learned concept directions / intervention critic',record,checkpoint,'concept-critic')
    B0=np.array(c['basis']);B=B0/np.linalg.norm(B0,axis=1,keepdims=True);C=np.array(c['critic']);z=(np.array(record['trace']['pooled'])[0]-normal['zmean'])/normal['zscale']
    code=int(np.random.default_rng(SEED+401).integers(0,6));direction=code//2;sign=2*(code%2)-1
    t.data['input'].update(case=int(record['trace']['sample_index']),code_seed=SEED+401,code_distribution='Uniform over six direction/sign codes; this trace fixes one sampled code',latent_dimension=6)
    t.add('input.pooled_embedding',np.array(record['trace']['pooled'])[0],'Saved quantum-hybrid heldout pooled embedding',axes=['latent_coordinate'])
    t.add('normalization.mean',normal['zmean'],'Training-only pooled mean',axes=['latent_coordinate']);t.add('normalization.scale',normal['zscale'],'Training-only pooled scale',axes=['latent_coordinate'])
    t.add('input.z',z,'(pooled-mean)/scale',['input.pooled_embedding','normalization.mean','normalization.scale'],['latent_coordinate'])
    t.add('input.code',code,'Explicit fixed sample C ~ Uniform({0,...,5}); seed stored in trace input',axes=[])
    t.add('direction_index',direction,'floor(C/2)',['input.code'],[]);t.add('direction_sign',sign,'2(C mod 2)-1',['input.code'],[])
    t.add('weight.basis',B0,'Saved trained normalized basis parameter',axes=['direction','latent_coordinate'])
    t.add('basis.row_norms',np.linalg.norm(B0,axis=1,keepdims=True),'Euclidean row norms',['weight.basis'],['direction','singleton'])
    t.add('basis.normalized',B,'Normalize rows (saved rows already unit to floating precision)',['weight.basis','basis.row_norms'],['direction','latent_coordinate'])
    intervention=.7*sign*B[direction];base=np.tanh(.3*z);steered=np.tanh(.3*z+intervention);delta=steered-base
    t.add('intervention',intervention,'.7 sign(C) B_direction',['basis.normalized','direction_index','direction_sign'],['latent_coordinate'])
    t.add('base.tanh',base,'tanh(.3z)',['input.z'],['latent_coordinate'])
    t.add('steered.tanh',steered,'tanh(.3z+intervention)',['input.z','intervention'],['latent_coordinate'])
    t.add('delta',delta,'steered.tanh-base.tanh',['base.tanh','steered.tanh'],['latent_coordinate'])
    t.add('weight.critic',C,'Saved trained linear critic; no bias',axes=['latent_coordinate','code_class'])
    raw=delta@C;logits=raw/.2;logprob=logits-logsumexp(logits);prob=np.exp(logprob);ce=-logprob[code];gram=B@B.T;penalty=.08*np.sum((gram-np.eye(3))**2)
    t.add('critic.linear',raw,'Delta @ trained critic',['delta','weight.critic'],['code_class'])
    t.add('critic.logits',logits,'critic.linear / temperature(.2)',['critic.linear'],['code_class'])
    t.add('critic.log_probabilities',logprob,'logits-logsumexp(logits)',['critic.logits'],['code_class'])
    t.add('critic.softmax',prob,'exp(log probabilities)',['critic.log_probabilities'],['code_class'])
    t.add('code_cross_entropy',ce,'-log q(C | Delta) for the explicit sampled code',['critic.log_probabilities','input.code'],[])
    t.add('basis.gram',gram,'B B^T',['basis.normalized'],['direction_row','direction_column'])
    t.add('orthogonality_penalty',penalty,'.08 ||B B^T-I||_F^2',['basis.gram'],[])
    t.add('single_code_objective',ce+penalty,'Code CE + orthogonality penalty; replay diagnostic, not saved final minibatch loss',['code_cross_entropy','orthogonality_penalty'],[])
    # Reproduce the actual saved heldout code/change distribution, all40 x6 codes.
    dataset_raw=(ROOT/record['dataset']['path']).read_bytes();assert hashlib.sha256(dataset_raw).hexdigest()==record['dataset']['sha256'];dataset=json.loads(dataset_raw);params=np.array(dataset['parameters'])[dataset['test']];angles,mask,_=graph_tokens(params)
    w=[np.array(a) for a in record['weights']['quantum-hybrid']];emb=(np.asarray(attention(circuit_features(angles),w,mask,'hybrid'))-normal['zmean'])/normal['zscale']
    labels=np.tile(np.arange(6),len(emb));bases=np.repeat(emb,6,axis=0);changes=np.tanh(.3*bases+.7*B[labels//2]*(2*(labels%2)-1)[:,None])-np.tanh(.3*bases)
    scores=changes@C/.2;losses=logsumexp(scores,axis=1)-scores[np.arange(len(labels)),labels];heldout=float(losses.mean());mi=float(np.log(6)-heldout)
    t.add('heldout.embeddings',emb,'Replayed normalized embeddings for40 heldout physical inputs',['normalization.mean','normalization.scale'],['heldout_example','latent_coordinate'])
    t.add('heldout.codes',labels,'All six uniform code values for each heldout base',axes=['example_code_pair'])
    t.add('heldout.delta',changes,'Actual heldout intervention-change distribution',['heldout.embeddings','heldout.codes','basis.normalized'],['example_code_pair','latent_coordinate'])
    t.add('heldout.logits',scores,'heldout.Delta @ critic / .2',['heldout.delta','weight.critic'],['example_code_pair','code_class'])
    t.add('heldout.code_CE',losses,'logsumexp(logits)-selected-code logit',['heldout.logits','heldout.codes'],['example_code_pair'])
    t.add('heldout_CE',heldout,'Mean of240 heldout code cross entropies',['heldout.code_CE'],[])
    t.add('empirical_MI_functional',mi,'log6-empirical heldout CE; estimate of variational-bound functional, not certified population MI',['heldout_CE'],[])
    scalar=np.array([sum(delta[j]*C[j,k] for j in range(6))/.2 for k in range(6)])
    t.check('critic_scalar_replay',np.max(abs(scalar-logits)),1e-12);t.check('probability_sum',abs(prob.sum()-1),1e-12)
    t.check('saved_heldout_CE',abs(heldout-c['heldout_cross_entropy']),1e-11)
    t.check('saved_empirical_MI',abs(mi-c['heldout_InfoNCE_lower_bound_nats']),1e-11)
    t.check('basis_unit_rows',np.max(abs(np.linalg.norm(B,axis=1)-1)),1e-12)
    return t.finish()

def gfn_trace(record,checkpoint):
    g=record['gfn'];w=[np.array(a) for a in g['weights']];path=np.array(g['paths'][0]);t=component('quantum-tokengt-rg-continuous-gfn','Continuous GFlowNet / Gaussian MLP and trajectory balance',record,checkpoint,'continuous-gfn')
    t.data['input'].update(saved_path_index=0,horizon=3,latent_dimension=2,root_measure=g['root_measure'],backward_kernel=g['backward'])
    axes=[['mlp_input','hidden_unit'],['hidden_unit'],['hidden_unit','latent_coordinate'],['latent_coordinate'],['time_step','latent_coordinate'],['scalar_parameter']]
    for i,a in enumerate(w):t.add(f'weight.{i}',a,'Saved trained Gaussian-policy parameter' if i<5 else 'Saved learned log normalization',axes=axes[i])
    t.add('saved.path',path,'Actual saved continuous on-policy trajectory, first of30 displayed paths',axes=['time','latent_coordinate'])
    t.add('root.x',path[0],'Fixed root x0=(0,0)',['saved.path'],['latent_coordinate'])
    t.add('root.mass',1.,'Unit point mass at root, not a Lebesgue density',axes=[])
    t.add('root.log_mass',0.,'log1 for delta root; no Gaussian density at root',['root.mass'],[])
    previous='root.x';log_forward=[];log_backward=[];forward_nodes=[];backward_nodes=[]
    for step in range(1,4):
        prefix=f'step{step}';inp=np.r_[path[step-1],step/3];linear=inp@w[0]+w[1];hidden=np.tanh(linear);drift=hidden@w[2]+w[3];mu=path[step-1]+drift;logs=w[4][step-1];sigma=np.exp(logs)
        innovation=(path[step]-mu)/sigma;per_coordinate=-.5*(innovation**2+2*logs+np.log(2*np.pi));logpf=float(per_coordinate.sum())
        t.add(prefix+'.mlp_input',inp,'Concat(previous x, t/3)',[previous],['mlp_input'])
        t.add(prefix+'.linear1',linear,'input W0+b0',[prefix+'.mlp_input','weight.0','weight.1'],['hidden_unit'])
        t.add(prefix+'.hidden',hidden,'tanh(linear1)',[prefix+'.linear1'],['hidden_unit'])
        t.add(prefix+'.drift',drift,'hidden W1+b1',[prefix+'.hidden','weight.2','weight.3'],['latent_coordinate'])
        t.add(prefix+'.forward_mean',mu,'previous x + learned drift',[previous,prefix+'.drift'],['latent_coordinate'])
        t.add(prefix+'.log_sigma',logs,'Saved learned diagonal log-standard-deviation at this time',['weight.4'],['latent_coordinate'])
        t.add(prefix+'.sigma',sigma,'exp(log_sigma)',[prefix+'.log_sigma'],['latent_coordinate'])
        t.add(prefix+'.x',path[step],'Actual saved next continuous state',['saved.path'],['latent_coordinate'])
        t.add(prefix+'.innovation',innovation,'(saved x_t - forward mean)/sigma; recovered innovation, not a new RNG draw',[prefix+'.x',prefix+'.forward_mean',prefix+'.sigma'],['latent_coordinate'])
        t.add(prefix+'.log_density_coordinates',per_coordinate,'-.5(innovation²+2log_sigma+log(2pi))',[prefix+'.innovation',prefix+'.log_sigma'],['latent_coordinate'])
        pfnode=t.add(prefix+'.forward_log_density',logpf,'Sum coordinate log densities w.r.t. 2D Lebesgue measure',[prefix+'.log_density_coordinates'],[])
        t.add(prefix+'.forward_density',np.exp(logpf),'exp(forward log density); a continuous density may exceed1',[pfnode],[])
        forward_nodes.append(pfnode);log_forward.append(logpf)
        if step==1:
            pbnode=t.add(prefix+'.backward_log_mass',0.,'Unit backward point mass on root; no Lebesgue Gaussian for this step',['root.log_mass'],[]);logpb=0.
        else:
            bmu=path[step]*(step-1)/step;variance=(step-1)/(3*step);bcoordinate=-.5*((path[step-1]-bmu)**2/variance+np.log(variance)+np.log(2*np.pi));logpb=float(bcoordinate.sum())
            t.add(prefix+'.backward_mean',bmu,'((t-1)/t)x_t',[prefix+'.x'],['latent_coordinate'])
            t.add(prefix+'.backward_variance',np.full(2,variance),'((t-1)/(3t)) I diagonal',axes=['latent_coordinate'])
            t.add(prefix+'.backward_log_coordinates',bcoordinate,'Gaussian log p_B coordinate terms',[previous,prefix+'.backward_mean',prefix+'.backward_variance'],['latent_coordinate'])
            pbnode=t.add(prefix+'.backward_log_density',logpb,'Sum backward coordinate log densities',[prefix+'.backward_log_coordinates'],[])
            t.add(prefix+'.backward_density',np.exp(logpb),'Normalized Gaussian backward density, not discrete probability',[pbnode],[])
        backward_nodes.append(pbnode);log_backward.append(logpb);previous=prefix+'.x'
        t.check(prefix+'.mean_replay',np.max(abs(mu-np.asarray(gfn_mu(w,path[step-1:step],step))[0])),1e-12)
        t.check(prefix+'.forward_density_replay',abs(logpf-float(gaussian_log(path[step],mu,logs))),1e-12)
    params=np.array([.62+.35*np.tanh(path[-1,0]),.58+.34*np.tanh(path[-1,1]),.12]);target=teacher(params);physical_logz=target[32];confinement=-.5*np.sum(path[-1]**2);logreward=float(confinement+.35*(physical_logz-7))
    t.add('terminal.physical_parameters',params,'(.62+.35 tanh x0,.58+.34 tanh x1,.12)',[previous],['physical_control'])
    t.add('terminal.coarse_logweights',target[:32],'Exact black-spin decimation on K2,5; all32 weights and constant retained',['terminal.physical_parameters'],['white_spin_configuration'])
    t.add('terminal.physical_logZ',physical_logz,'logsumexp of exact coarse action',['terminal.coarse_logweights'],[])
    t.add('terminal.confining_log_factor',confinement,'-||x_T||²/2',[previous],[])
    t.add('terminal.log_reward',logreward,'confining factor + .35(physical logZ-7)',['terminal.physical_logZ','terminal.confining_log_factor'],[])
    t.add('trajectory.sum_log_forward',sum(log_forward),'Sum continuous forward log densities',forward_nodes,[])
    t.add('trajectory.sum_log_backward',sum(log_backward),'Sum backward log densities plus unit root log mass',backward_nodes,[])
    parents=['weight.5','trajectory.sum_log_forward','trajectory.sum_log_backward','terminal.log_reward'];residual=float(w[5][0]+sum(log_forward)-sum(log_backward)-logreward)
    t.add('squared_TB_loss',residual**2,'Square of logZ_parameter+sum logPF-sum logPB-logR; one saved trajectory',parents,[])
    t.add('TB_residual',residual,'logZ_parameter+sum logPF-sum logPB-logR; finite density-balance residual',parents,[])
    t.check('saved_path_root',np.max(abs(path[0])),1e-15)
    t.check('reward_exact_teacher_replay',abs(logreward-float(gfn_reward(path[-1:])[0])),1e-12)
    t.check('TB_vectorized_replay',abs(residual-float(gfn_tb(w,path[None])[0])),1e-12)
    return t.finish()

def entries(record,checkpoint):return [concept_trace(record,checkpoint),gfn_trace(record,checkpoint)]

def main():
    folder=ROOT/'web/data/quantum-tokengt';manifest=json.loads((folder/'manifest.json').read_text());raw=(folder/manifest['file']).read_bytes();assert hashlib.sha256(raw).hexdigest()==manifest['sha256'];record=json.loads(raw);checkpoint=ROOT/manifest['run']/'record.json';assert checkpoint.read_bytes()==raw
    keep=[item for item in manifest['traces'] if item['id'] not in ['quantum-tokengt-rg-concept-critic','quantum-tokengt-rg-continuous-gfn']];added=[]
    for data in entries(record,checkpoint):
        payload=json.dumps(serial(data),separators=(',',':'),allow_nan=False).encode();digest=hashlib.sha256(payload).hexdigest();name=f"{data['id']}-{digest[:16]}.json";(folder/'records'/name).write_bytes(payload)
        added.append(dict(id=data['id'],title=data['title'],category=data['category'],kind='trained-checkpoint-replay',file='records/'+name,sha256=digest,nodes=len(data['nodes']),checks=len(data['checks'])))
    manifest['traces']=keep+added;(folder/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n');assert (folder/manifest['file']).read_bytes()==raw
    print(json.dumps(added))
if __name__=='__main__':main()
