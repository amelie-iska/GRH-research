#!/usr/bin/env python3
"""Publish computed RG cases and immutable numerical forward traces locally."""
from pathlib import Path
import sys,json,hashlib
import numpy as np
from scipy.special import logsumexp
from rg_math import dessin,classical_flow,quantum_example,walsh,spins
from train_rg import features,encode
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'examples/architecture'));sys.path.insert(0,str(ROOT/'examples/quantum'))
from trace_schema import Trace,source
from quantum_traces import apply_gate,CZ
from surface_models import ry,rz

def make_trace(model,k):
    e=model['examples'][k];x=np.array(e['parameters']);theta=np.array(model['theta']).reshape(2,3,2)
    t=Trace(f'actual-rg-{k}','Full-action RG quantum feature learner','quantum-full-action-rg',
        dict(kind='trained-checkpoint-replay',split='saved held-out actual7-to5 spin RG example',seed=model['seed'],training_source=source('examples/rg/train_rg.py'),checkpoint=source('outputs/experiments/actual-rg/training.json')),
        dict(basis='qubit0 most significant',target='All32 unnormalized logweights; not a state-compression score',feature_wires='coupling registers J+,J-,b; not physical spin sites'))
    t.data['input']=dict(parameters=x.tolist(),surface_m=5,physical_sites=7,retained_sites=5)
    t.add('couplings',x,'Tied physical J+,J-,b parameters',axes=['parameter'])
    t.add('parameters',theta,'Saved12 circuit angles',axes=['layer','wire','rotation'])
    t.add('head',model['head'],'Saved8-by32 affine readout, last row bias',axes=['feature_bias','boundary_configuration'])
    state=np.zeros(8,complex);state[0]=1;previous=t.add('circuit.input',state,'|000> feature registers',axes=['basis'])
    for q,a in enumerate(encode(x)):
        state=apply_gate(state,ry(a),[q],3)
        previous=t.add(f'circuit.encode{q}',state,f'RY({a:.8g}) input encoding',[previous,'couplings'],['basis'],gate='RY',wires=[q],angle=float(a))
    for l in range(2):
        for q in range(3):
            for r,(name,gate) in enumerate([('RY',ry),('RZ',rz)]):
                a=theta[l,q,r];state=apply_gate(state,gate(a),[q],3)
                previous=t.add(f'circuit.layer{l}.{name.lower()}{q}',state,f'{name} saved angle',[previous,'parameters'],['basis'],gate=name,wires=[q],angle=float(a))
        for a,b in [(0,1),(1,2),(2,0)]:
            state=apply_gate(state,CZ,[a,b],3)
            previous=t.add(f'circuit.layer{l}.cz{a}_{b}',state,'CZ entangler',[previous],['basis'],gate='CZ',wires=[a,b])
    probability=abs(state)**2
    zs=np.array([np.sum(probability*np.array([(-1)**((i&mask).bit_count()) for i in range(8)])) for mask in range(1,8)])
    t.check('PennyLane_feature_equivalence',np.max(abs(zs-features(theta.ravel(),x[None])[0])))
    f=t.add('pauli_features',zs,'Seven nonempty Z-product expectations',[previous],['feature'])
    head=np.array(model['head']);pred=np.r_[zs,1]@head*model['target_scale']+model['target_mean']
    out=t.add('full_coarse_action',pred,'Affine full logweights, de-standardized',[f,'head'],['boundary_configuration'])
    t.add('generated_interactions',walsh(pred),'Walsh transform; mask0 is the constant',[out],['spin_subset'])
    t.add('exact_target',e['exact_logweights'],'Exact sum over both black spins',['couplings'],['boundary_configuration'])
    t.add('logZ',logsumexp(pred),'logsumexp of full coarse action',[out])
    t.check('saved_action_replay',np.max(abs(pred-e['predicted_logweights'])))
    t.check('feature_state_norm',abs(np.vdot(state,state)-1))
    return t.finish()

def main():
    folder=ROOT/'web/data/rg';records=folder/'records';records.mkdir(parents=True,exist_ok=True)
    model=json.loads((ROOT/'outputs/experiments/actual-rg/training.json').read_text())
    manifest=dict(schema_version=1,traces=[],scope='New actual finite full-action RG; original22 architecture records preserved')
    for k in range(len(model['examples'])):
        trace=make_trace(model,k);raw=(json.dumps(trace,indent=2)+'\n').encode();h=hashlib.sha256(raw).hexdigest()
        name=f"{trace['id']}-{h[:16]}.json";(records/name).write_bytes(raw)
        manifest['traces'].append(dict(id=trace['id'],title=trace['title'],category=trace['category'],kind=trace['provenance']['kind'],file='records/'+name,sha256=h))
    (folder/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
    classical=[dict(m=m,parameters=p,dessin=dessin(m),flow=classical_flow(m,p)) for m,p in [(5,[.57,.83,-.24]),(9,[.57,.83,-.24])]]
    quantum=[quantum_example(m,p,beta=b,transverse=g) for m,p,b,g in [(5,[.52,.66,.21],.73,.47),(5,[.8,.43,-.32],.95,.65),(3,[.65,.8,.1],.8,.42)]]
    lab=dict(classical=classical,quantum=quantum,training=model,evaluation=json.loads((ROOT/'outputs/experiments/actual-rg/evaluation.json').read_text()),sampling=json.loads((ROOT/'outputs/experiments/actual-rg/sampling.json').read_text()),
        convention='V=log unnormalized classical Boltzmann weight; quantum H_eff=-log Wprime/beta',
        physical_scope='Finite exact decimation, all constants and interactions; no thermodynamic fixed-point or arithmetic result')
    (folder/'lab.json').write_text(json.dumps(lab,indent=2)+'\n')
    print(json.dumps(dict(traces=len(manifest['traces']),classical_cases=len(classical),quantum_cases=len(quantum),teacher='actualK2,5 dessin graph spin decimation'),indent=2))
if __name__=='__main__':main()
