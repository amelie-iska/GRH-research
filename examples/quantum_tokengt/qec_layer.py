"""Evaluate an ideal QEC memory layer inside the saved token-feature pipeline.

No optimizer, pretrained record or checkpoint is modified. Three logical
feature qubits are encoded separately after feature-state preparation and
before noise/measurement. The Bell-reference recovery identity supplies the
logical channel, even for entangled feature inputs. All gates and recovery
are ideal; only independent X memory errors are modeled.
"""
import argparse,hashlib,itertools,json
from pathlib import Path
import numpy as np
from model import ROOT,OBS,SEED,circuit_features,graph_tokens,teacher
from train import predict,metrics
WEIGHTS=np.array([1,1,1,2,2,2])

def effective_error(p,levels=1):
    value=float(p)
    if not 0<=value<=1 or levels not in [0,1,2]:raise ValueError('p in [0,1], levels in {0,1,2}')
    for _ in range(levels):value=3*value**2-2*value**3
    return value

def attenuate(features,p,levels=1):
    return np.asarray(features)*(1-2*effective_error(p,levels))**WEIGHTS

def density_mixture(psi,p):
    """Independent explicit density channel over all eight logical X patterns."""
    rho=np.zeros((8,8),complex)
    for errors in itertools.product([0,1],repeat=3):
        flip=sum(e<<(2-q) for q,e in enumerate(errors));prob=np.prod([p if e else 1-p for e in errors])
        shifted=np.asarray(psi)[np.arange(8)^flip];rho+=prob*np.outer(shifted,shifted.conj())
    return rho

def evaluate_record(record,manifest):
    dataset_path=ROOT/record['dataset']['path'];data=json.loads(dataset_path.read_text());assert hashlib.sha256(dataset_path.read_bytes()).hexdigest()==record['dataset']['sha256']
    indices=np.array(data['test']);parameters=np.array(data['parameters'])[indices];target=np.stack([teacher(p)[:32] for p in parameters]);angles,mask,ids=graph_tokens(parameters)
    features,states=circuit_features(angles,True);mean=np.array(record['normalization']['mean']);scale=np.array(record['normalization']['scale'])
    probabilities=[0,.02,.05,.1,.2];rows=[];models={};max_error=0.;checks=[]
    # Real saved entangled feature states; independent mixture also checks PSD/trace.
    for sample,token in [(0,0),(0,9),(7,3),(19,12),(39,16)]:
        psi=states[sample,token]
        for p in probabilities:
            for levels in [0,1,2]:
                q=effective_error(p,levels);rho=density_mixture(psi,q);expected=attenuate(features[sample,token],p,levels);actual=np.diag(rho).real@OBS
                error=float(np.max(abs(actual-expected)));max_error=max(max_error,error)
                assert error<2e-13 and abs(np.trace(rho)-1)<2e-13 and np.linalg.eigvalsh(rho).min()>-2e-13
                checks.append(dict(sample_index=int(indices[sample]),token=token,p=p,levels=levels,logical_error=q,max_abs_error=error))
    for name in ['quantum-softmax','quantum-tropical','quantum-hybrid']:
        w=[np.array(v) for v in record['weights'][name]];mode=record['models'][name]['mode'];clean=np.asarray(predict(w,features,mask,mode))*scale+mean
        clean_metrics=metrics(target,clean)
        for k,v in clean_metrics.items():np.testing.assert_allclose(v,record['models'][name]['heldout'][k],atol=2e-12)
        model_rows=[]
        for p in probabilities:
            variants=[]
            for levels in [0,1,2]:
                noisy=attenuate(features,p,levels);prediction=np.asarray(predict(w,noisy,mask,mode))*scale+mean
                variants.append(dict(levels=levels,physical_qubits_per_token=3**(levels+1),effective_logical_X_error=effective_error(p,levels),
                    attenuation=(1-2*effective_error(p,levels))**WEIGHTS,metrics=metrics(target,prediction),
                    prediction_logweights=prediction.tolist(),prediction_change_rmse_from_clean=float(np.sqrt(np.mean((prediction-clean)**2)))))
            model_rows.append(dict(p=p,variants=variants))
        models[name]=dict(clean_metrics=clean_metrics,mode=mode,cases=model_rows)
    return dict(schema=1,seed=SEED,source_record=dict(file=manifest['file'],sha256=manifest['sha256'],run=manifest['run']),
        source_hashes={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in [Path(__file__),Path(__file__).with_name('model.py'),Path(__file__).with_name('train.py')]},
        heldout_indices=indices.tolist(),heldout_parameters=parameters.tolist(),target_logweights=target.tolist(),probabilities=probabilities,
        feature_observables=['Z0','Z1','Z2','Z0Z1','Z1Z2','Z0Z2'],feature_weights=WEIGHTS.tolist(),models=models,
        channel=dict(location='After prepared 3-qubit token state, before measurement; separate repetition encoder/recovery per logical feature qubit',
            noise='Independent physical X errors with probability p during one memory interval; ideal encoding, syndrome, correction and decoding',
            levels='0:unencoded3qubits;1:3independent three-bit blocks,9physicalqubits/token;2:ideal concatenation,27physicalqubits/token',
            identity='Each Pauli-Z product of weight w attenuates by (1-2p_eff)^w, p_eff=f^levels(p), f(p)=3p²-2p³',
            assumptions='Recovered tensor-product logical X channel follows from single-block Bell-reference channel and disjoint independent error blocks, valid for entangled logical input',
            executed='Original3-qubit feature states, exact8-logical-error density mixtures and complete saved classical prediction heads; no9/27-qubit gate/noisy recovery simulation',
            limitation='Ideal memory layer only; no phase-error protection, noisy gates, noisy syndrome, correlated noise, threshold or fault-tolerance claim'),
        independent_density_checks=checks,max_density_attenuation_error=max_error)

def convert(v):
    if isinstance(v,np.ndarray):return v.tolist()
    if isinstance(v,np.generic):return v.item()
    if isinstance(v,dict):return {k:convert(a) for k,a in v.items()}
    if isinstance(v,list):return [convert(a) for a in v]
    return v

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--run',default='qec-memory-layer-20261103-v1');args=parser.parse_args()
    web=ROOT/'web/data/quantum-tokengt';manifest=json.loads((web/'manifest.json').read_text());record_path=web/manifest['file'];raw=record_path.read_bytes();assert hashlib.sha256(raw).hexdigest()==manifest['sha256'];record=json.loads(raw)
    result=evaluate_record(record,manifest);result=convert(result);payload=json.dumps(result,separators=(',',':'),allow_nan=False).encode();digest=hashlib.sha256(payload).hexdigest()
    out=ROOT/'outputs/experiments/quantum-tokengt'/args.run;out.mkdir(exist_ok=False);(out/'qec-layer.json').write_bytes(payload)
    filename=f'qec-layer-{digest[:16]}.json';(web/filename).write_bytes(payload);pointer=dict(file=filename,sha256=digest,run=str(out.relative_to(ROOT)))
    manifest['qec_layer']=pointer;(web/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n');(out/'manifest.json').write_text(json.dumps(pointer,indent=2)+'\n')
    assert record_path.read_bytes()==raw
    print(json.dumps(dict(pointer=pointer,checks=len(result['independent_density_checks']),max_error=result['max_density_attenuation_error'],models={name:[dict(p=case['p'],action_RMSE=[v['metrics']['logweight_rmse'] for v in case['variants']]) for case in model['cases']] for name,model in result['models'].items()})))
if __name__=='__main__':main()
