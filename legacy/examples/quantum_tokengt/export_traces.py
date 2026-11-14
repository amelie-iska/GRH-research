"""Export trained passes into the existing read-only DAG schema."""
import argparse,hashlib,json,sys
import numpy as np
from model import ROOT,OBS,attention,circuit_features,graph_tokens,classical_features,teacher,qml
from train import predict,serial
sys.path.insert(0,str(ROOT/'examples/architecture'))
from trace_schema import Trace,source

def apply_gate(psi,U,wires):
    order=list(wires)+[i for i in range(3) if i not in wires];a=psi.reshape([2]*3).transpose(order).reshape(2**len(wires),-1)
    return (U@a).reshape([2]*3).transpose(np.argsort(order)).ravel()
def build(record,name,checkpoint):
    w=[np.array(v) for v in record['weights'][name]];mode=record['models'][name]['mode'];params=np.array(record['trace']['parameters'])
    angles,mask,ids=graph_tokens(params);features,psi=circuit_features(angles,True)
    if name.startswith('classical'):features=classical_features(angles)
    z,details=attention(features,w,mask,mode,True);prediction=np.asarray(predict(w,features,mask,mode))*record['normalization']['scale']+record['normalization']['mean'];target=teacher(params)[:32]
    identity='quantum-tokengt-rg-'+name.replace('quantum-','')
    t=Trace(identity,'Physical RG / '+name,'quantum-tokengt-rg',dict(kind='trained-checkpoint-replay',seed=record['seed'],checkpoint=source(checkpoint),
        implementation=source(__file__),training_source=source('examples/quantum_tokengt/train.py'),backend='PennyLane 0.40.0 exact CPU quantum features; Autograd classical learned attention',
        split='same saved heldout sample; 120train40test40OOD',scope='7physicalspin sites10incidenceedges; 3auxiliary featurequbits pertoken; no faithful orderrep, upstream training or quantumadvantage'),
        dict(wires='Auxiliary qubits0,1,2; qubit0 mostsignificant, not physicalsite indexing',attention='Single head6channels; hybrid=.5(softmax context+maxplus context); maskedpadding',feature_circuit='Fixed circuit; classicalQKV/readouttrained',linear='XW+b',shots=None))
    t.data['input']=dict(surface_m=5,parameters=params.tolist(),physical_sites=7,incidence_edges=10,feature_qubits=3,token_count=18,valid_tokens=17)
    t.add('physical_parameters',params,'Dimensionless physical Jplus,Jminus,b',axes=['parameter'])
    t.add('token_identifiers',np.array([[0 if v['kind']=='physical-node' else 1 if v['kind']=='physical-edge' else -1,*v['endpoints']] for v in ids]),'Kind and transported endpoint identifiers',axes=['token','metadata'])
    t.add('token_mask',mask,'17 valid tokens plus one masked pad',axes=['token'])
    t.add('token_angles',angles,'Explicit globalcontrols+localcoupling/field+endpoint metadata', ['physical_parameters','token_identifiers'],['batch','token','qubit'])
    if not name.startswith('classical'):
        state=np.zeros(8,complex);state[0]=1;last=t.add('token0.input',state,'Auxiliary |000> state',axes=['basis']);gates=[]
        for q in range(3):gates.extend([('RY',[q],float(angles[0,0,q])),('RZ',[q],.23*(q+1))])
        gates.extend([('CNOT',[0,1],None),('CNOT',[1,2],None)])
        for q in range(3):gates.append(('RX',[q],.19*(q+1)))
        for i,(gate,wires,angle) in enumerate(gates):
            op=getattr(qml,gate)(wires=wires) if angle is None else getattr(qml,gate)(angle,wires=wires)
            state=apply_gate(state,np.array(qml.matrix(op)),wires)
            last=t.add(f'token0.gate{i}',state,f'{gate} on auxiliaryqubitwires {wires}',[last,'token_angles'],['basis'],gate=gate,wires=wires,angle=angle)
        t.check('gate_replay_vs_pennylane_state',np.max(abs(state-psi[0,0])),1e-12)
        t.add('all_token_states',psi,'18 independent threequbit carrierstates; padstatecomputed butmasked',['token_angles'],['batch','token','basis'])
    t.add('token_features',features,'Six measurable ZandZZ expectations' if not name.startswith('classical') else 'Matched six local sincos features',['token_angles'],['batch','token','feature'])
    for i,a in enumerate(w):t.add(f'weight.{i}',a,'Saved trained classical parameter',axes=[f'axis{j}' for j in range(a.ndim)])
    for key in ['query','key','value']:
        j=['query','key','value'].index(key);t.add(key,details[key],f'features @ W{key[0].upper()}',['token_features',f'weight.{j}'],['batch','token','channel'])
    t.add('scores',details['scores'],'QK^T/sqrt(6)',['query','key'],['batch','query_token','key_token'])
    t.add('legal',details['legal'],'valid(query) and valid(key)',['token_mask'],['batch','query_token','key_token'])
    t.add('weights',details['weights'],'softmax overlegalkeys; emptyrowzero',['scores','legal'],['batch','query_token','key_token'])
    t.add('winners',details['winners'],'All exact floatingpoint coordinatewisemaxplus winners',['scores','value','legal'],['batch','query_token','key_token','channel'])
    t.add('context',details['context'],mode+' aggregation',['scores','value','weights','legal'],['batch','token','channel'])
    t.add('pooled',z,'maskedmean tanh(context+features)',['context','token_features','token_mask'],['batch','channel'])
    hidden=np.tanh(z@w[3]+w[4]);t.add('hidden',hidden,'tanh(zW1+b1)',['pooled','weight.3','weight.4'],['batch','hidden'])
    t.add('standardized_prediction',hidden@w[5]+w[6],'hiddenW2+b2',['hidden','weight.5','weight.6'],['batch','white_spin_configuration'])
    t.add('prediction',prediction,'Invert training-only target normalization',['standardized_prediction'],['batch','white_spin_configuration'])
    t.add('exact_target',target,'Exact blackspin decimation with constantretained',['physical_parameters'],['white_spin_configuration'])
    t.add('prediction_error',prediction-target,'Predicted minus exact32coarse logweights',['prediction','exact_target'],['batch','white_spin_configuration'])
    # Independent scalar aggregation witness checks.
    for i in range(18):
        if not mask[i]:continue
        score=np.array([np.dot(details['query'][0,i],details['key'][0,j])/np.sqrt(6) for j in range(17)])
        soft=np.exp(score-max(score));soft/=sum(soft);v=details['value'][0,:17]
        c=soft@v if mode=='softmax' else np.max(score[:,None]+v,axis=0) if mode=='tropical' else .5*(soft@v+np.max(score[:,None]+v,axis=0))
        t.check(f'context_scalar_row{i}',np.max(abs(c-details['context'][0,i])),1e-12)
    t.check('padded_context',np.max(abs(details['context'][:,17])),1e-12)
    t.check('feature_bounds',max(0.,float(np.max(abs(features))-1)),1e-12)
    return t.finish()

def main():
    folder=ROOT/'web/data/quantum-tokengt';manifest=json.loads((folder/'manifest.json').read_text());recordpath=folder/manifest['file'];record=json.loads(recordpath.read_text());assert hashlib.sha256(recordpath.read_bytes()).hexdigest()==manifest['sha256']
    checkpoint=ROOT/manifest['run']/'record.json';records=folder/'records';records.mkdir(exist_ok=True);traces=[]
    for name in record['models']:
        data=build(record,name,checkpoint);raw=json.dumps(serial(data),separators=(',',':'),allow_nan=False).encode();h=hashlib.sha256(raw).hexdigest();filename=f"{data['id']}-{h[:16]}.json";(records/filename).write_bytes(raw)
        traces.append(dict(id=data['id'],title=data['title'],category=data['category'],kind='trained-checkpoint-replay',file='records/'+filename,sha256=h,nodes=len(data['nodes']),checks=len(data['checks'])))
    manifest['schema_version']=1;manifest['traces']=traces;(folder/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n');print(json.dumps(traces))
if __name__=='__main__':main()
