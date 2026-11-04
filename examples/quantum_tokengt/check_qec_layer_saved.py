"""Audit the separate layer artifact and its complete physical predictions."""
import hashlib,json
from pathlib import Path
import numpy as np
from scipy.special import logsumexp
from model import ROOT,spins,teacher,graph_tokens,circuit_features,OBS
from train import predict
from qec_layer import effective_error,density_mixture

def main():
    web=ROOT/'web/data/quantum-tokengt';manifest=json.loads((web/'manifest.json').read_text());pointer=manifest['qec_layer'];raw=(web/pointer['file']).read_bytes();assert hashlib.sha256(raw).hexdigest()==pointer['sha256'];layer=json.loads(raw)
    recordraw=(web/manifest['file']).read_bytes();assert hashlib.sha256(recordraw).hexdigest()==manifest['sha256']==layer['source_record']['sha256'];record=json.loads(recordraw)
    assert (ROOT/manifest['run']/'record.json').read_bytes()==recordraw
    assert len(layer['heldout_indices'])==40 and layer['heldout_indices']==record['dataset']['test']
    target=np.stack([teacher(p)[:32] for p in layer['heldout_parameters']]);np.testing.assert_allclose(target,layer['target_logweights'],atol=1e-12)
    checks=0
    for name,m in layer['models'].items():
        for case in m['cases']:
            for v in case['variants']:
                a=np.array(v['prediction_logweights']);lza=logsumexp(a,axis=1);lzt=logsumexp(target,axis=1);pa=np.exp(a-lza[:,None]);pt=np.exp(target-lzt[:,None])
                measured=dict(logweight_rmse=np.sqrt(np.mean((a-target)**2)),logZ_rmse=np.sqrt(np.mean((lza-lzt)**2)),
                    retained_magnetization_rmse=np.sqrt(np.mean(((pa-pt)@spins(5))**2)),mean_TV=.5*np.abs(pa-pt).sum(1).mean(),
                    identity_coefficient_rmse=np.sqrt(np.mean((a.mean(1)-target.mean(1))**2)))
                for k,value in measured.items():np.testing.assert_allclose(value,v['metrics'][k],atol=1e-12)
                np.testing.assert_allclose(v['effective_logical_X_error'],effective_error(case['p'],v['levels']),atol=1e-15);checks+=1
    # Use density mixtures rather than attenuation to replay a complete saved head.
    angles,mask,_=graph_tokens(np.array(layer['heldout_parameters'])[:2]);features,states=circuit_features(angles,True);noisy=np.zeros_like(features);p=.1
    for i in range(2):
        for t in range(18):noisy[i,t]=np.diag(density_mixture(states[i,t],effective_error(p,1))).real@OBS
    w=[np.array(v) for v in record['weights']['quantum-hybrid']];prediction=np.asarray(predict(w,noisy,mask,'hybrid'))*np.array(record['normalization']['scale'])+np.array(record['normalization']['mean'])
    saved=next(c for c in layer['models']['quantum-hybrid']['cases'] if c['p']==p)['variants'][1]['prediction_logweights'];err=float(np.max(abs(prediction-np.array(saved)[:2])));assert err<2e-12
    report=dict(passed=True,layer_sha256=pointer['sha256'],trained_record_sha256=manifest['sha256'],trained_record_unchanged=True,
        complete_metric_cases=checks,independent_density_cases=len(layer['independent_density_checks']),density_replayed_prediction_error=err,
        scope='Ideal independent-X feature-memory recovery; no noisy recovery, phase protection or fault-tolerance proof')
    out=ROOT/'outputs/checks/2026-11-03-actual-rg/quantum-tokengt';(out/'qec-layer.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
if __name__=='__main__':main()
