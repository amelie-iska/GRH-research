"""Measured speech and gravitational-wave controls with exact codec replay.

This bounded study is deliberately not a LibriSpeech ASR benchmark or an
independent gravitational-wave discovery. Fitting excludes the cataloged event
window; speech is split by speaker. The native model interface and all outcomes
are retained, including negative transfer and lossy-representation metadata.
"""
from __future__ import annotations
import argparse,gzip,hashlib,json,lzma,math,sys,time,zlib
from pathlib import Path
from datetime import datetime,timezone
import numpy as np
from scipy.signal import butter,sosfiltfilt
import soundfile as sf
from exact_codec import fit as codec_fit,encode,decode
from run_realdata import load_native,train_native,count_model,summarize,code_lengths,LAG

SPEAKERS={'train':'6930','validation':'1320','test':'5639'}


def sha(b):return hashlib.sha256(b).hexdigest()
def dump(path,data):path.parent.mkdir(parents=True,exist_ok=True);path.write_text(json.dumps(data,indent=2,allow_nan=False)+'\n')


def prepare_segments(parts,cap=2400):
    training=np.concatenate([np.diff(x.astype(np.int64))for x in parts['train']])
    edges=np.unique(np.quantile(training,np.arange(1,8)/8,method='nearest')).astype(np.int64);K=len(edges)+1;labels=np.searchsorted(edges,training,side='right')
    reps=np.array([int(np.median(training[labels==k]))if np.any(labels==k)else 0 for k in range(K)],dtype=np.int64)
    mean=float(training.mean());scale=max(1.,float(training.std()));groups={};support={}
    for split,segments in parts.items():
        candidates=[];offset=0
        for j,x in enumerate(segments):
            d=np.diff(x.astype(np.int64));start=2*LAG+1
            for t in range(start,len(x),max(1,len(x)//(cap//max(1,len(segments))+1))):candidates.append((j,t,offset+t,d[t-LAG-1:t-1].copy(),int(d[t-1]),int(x[t])))
            offset+=len(x)+4*LAG
        if len(candidates)>cap:candidates=[candidates[i]for i in np.linspace(0,len(candidates)-1,cap,dtype=int)]
        ctx=np.stack([r[3]for r in candidates]);target=np.array([r[4]for r in candidates]);groups[split]=dict(index=np.array([r[2]for r in candidates]),context=ctx,normalized=((ctx-mean)/scale).astype(np.float32),target=target,y=np.searchsorted(edges,target,side='right'),raw_value=np.array([r[5]for r in candidates]),segment=np.array([r[0]for r in candidates]),local_index=np.array([r[1]for r in candidates]))
        support[split]=[(int(r[0]),int(r[1]-LAG-1),int(r[1]))for r in candidates]
    return dict(groups=groups,K=K,edges=edges,reps=reps,mean=mean,scale=scale,boundaries='source-group partition',support=support)


def exact_compression(parts,d,dtype,out):
    symbols=[np.searchsorted(d['edges'],np.diff(x.astype(np.int64)),side='right')for x in parts['train']]
    model=codec_fit(symbols,d['K'],order=2)
    packet,r=encode(parts['test'],d['edges'].tolist(),d['reps'].tolist(),model,dtype)
    decoded=decode(packet)
    for original,recovered in zip(parts['test'],decoded):
        if not np.array_equal(original,recovered):raise ValueError('Lossless decoder replay failed')
    raw=b''.join(x.astype(dtype).tobytes()for x in parts['test']);out.write_bytes(packet)
    r.update(sha256=sha(packet),raw_sha256=sha(raw),roundtrip_exact=True,zlib_bpb=8*len(zlib.compress(raw))/len(raw),lzma_bpb=8*len(lzma.compress(raw))/len(raw),model_fit='All eligible training differences; fixed order two; test-independent half-count smoothing. This whole-stream codec has a distinct training/exposure contract from the sampled-window native pilot.')
    return r


def speech(root):
    parts={};sources=[]
    for split,speaker in SPEAKERS.items():
        files=sorted((root/'speech'/speaker).glob('*.flac'))
        if len(files)!=6:raise ValueError('Exactly six acquired utterances per speaker required')
        parts[split]=[]
        for f in files:
            x,rate=sf.read(f,dtype='int16',always_2d=False)
            if rate!=16000 or x.ndim!=1 or len(x)<1000:raise ValueError('Unexpected speech axes/rate')
            parts[split].append(x.astype(np.int64));sources.append(dict(split=split,speaker=speaker,file=f.name,samples=len(x),flac_sha256=sha(f.read_bytes()),pcm_sha256=sha(x.astype('<i2').tobytes()),sample_rate=rate))
    return parts,dict(source='LibriSpeech SLR12 test-clean',url='https://www.openslr.org/12',license='CC-BY-4.0',files=sources,split_policy='Three distinct speakers, six utterances each, re-split for this local experiment; not the official ASR training/test benchmark.',semantics='Known human read speech established by aligned source provenance. Acoustic compressibility alone is not a test of linguistic meaning.',native_integer_representation='Exact decoded signed 16-bit PCM, original 16 kHz; no resampling.',test_population='One held-out speaker; no population-level claim.')


def gravitational(root):
    arrays={};sources=[]
    for name in ['H-H1','L-L1']:
        f=root/(name+'.txt.gz');b=f.read_bytes();x=np.loadtxt(gzip.decompress(b).decode().splitlines())
        if x.shape!=(131072,)or not np.all(np.isfinite(x)):raise ValueError('Expected finite 32 seconds at 4096 Hz')
        arrays[name]=x;sources.append(dict(file=f.name,sha256=sha(b),samples=len(x),sample_rate=4096,gps_start=1126259446))
    unit=1e-24;parts={};quantization={}
    for split,key,start,end in [('train','H-H1',0,8),('validation','H-H1',8,12),('test','L-L1',24,28)]:
        x=arrays[key][start*4096:end*4096];integers=np.rint(x/unit).astype(np.int64)
        if np.max(abs(integers))>=2**31:raise ValueError('Chosen fixed-point representation overflows')
        parts[split]=[integers];quantization[split]=dict(detector=key,start_seconds=start,end_seconds=end,max_absolute_strain_error=float(np.max(abs(x-integers*unit))))
    return parts,dict(source='GWOSC GW150914 public v2 4 kHz strain',url='https://gwosc.org/events/GW150914/',license='CC-BY-4.0',files=sources,split_policy='H1 0–8 s training; H1 8–12 s validation; L1 24–28 s test, relative to GPS 1126259446. Catalog event near 16.44 s excluded from all fitting.',fixed_point_unit_strain=unit,quantization=quantization,representation='Chosen int32 fixed-point view; exact codec is lossless for this view, not for original float64/ASCII strain.',test_population='One detector-transfer interval; instrument distribution shift is retained.'),arrays


def waveform_control(arrays):
    # Retrospective diagnostic of a known event; all filter and lag choices fixed.
    fs=4096;sos=butter(4,[35,350],btype='bandpass',fs=fs,output='sos')
    filtered={k:sosfiltfilt(sos,v)for k,v in arrays.items()}
    lags=np.arange(-41,42)
    def maxcorr(center):
        t=int(center*fs);half=512;a=filtered['H-H1'][t-half:t+half]
        values=[]
        for lag in lags:
            b=filtered['L-L1'][t-half+lag:t+half+lag]
            aa=a-a.mean();bb=b-b.mean();den=np.linalg.norm(aa)*np.linalg.norm(bb)
            values.append(float(np.dot(aa,bb)/den)if den else 0.)
        j=int(np.argmax(np.abs(values)));return dict(center_seconds=center,max_abs_correlation=abs(values[j]),signed_correlation=values[j],lag_seconds=float(lags[j]/fs),lag_samples=int(lags[j]))
    event=maxcorr(16.44);controls=[maxcorr(float(t))for t in np.arange(1.,31.,.5)if abs(t-16.44)>2]
    return dict(event=event,offsource=controls,filter='Fixed fourth-order Butterworth 35–350 Hz; acausal forward/backward filtering for retrospective visualization only; never a predictor feature.',search_lag_seconds=[-41/fs,41/fs],window_seconds=.25,scope='Known-event descriptive cross-detector waveform control. No false-alarm probability, causal direction, message discovery or independent event detection is inferred. Whole-record filtering is excluded from all learned predictive inputs.')


def learned(data,native,outdir,steps=80):
    train,val,test=(data['groups'][x]for x in ('train','validation','test'));choices=[]
    for order in [0,1,2,4]:
        for alpha in [.1,.5,1.]:
            pred,size,wire=count_model(train,data['K'],data['edges'],order,alpha);score=float(code_lengths(pred(val),val,data['reps'])[0].mean());choices.append((score,order,alpha,pred,size,wire))
    best=min(choices,key=lambda x:(x[0],x[1],x[2]));bp=best[3](test)
    metadata=dict(edges=data['edges'].tolist(),representatives=data['reps'].tolist(),mean=data['mean'],scale=data['scale'],lag=LAG)
    size=len(json.dumps(metadata).encode());rows=[]
    for variant in ['vanilla','tropical-code']:
        for seed in [17,29]:
            try:
                r,p,mix=train_native(data,native,variant,seed,steps,outdir)
                r['test']=summarize(p,test,data['reps'],r['parameter_bytes'],size)
                r['retrieval_test']=summarize(mix,test,data['reps'],r['parameter_bytes']+r['retrieval_bank_bytes'],size)
                np.savez_compressed(outdir/f'{variant}-{seed}-predictions.npz',labels=test['y'],probability=p,retrieval_probability=mix,baseline=bp,segment=test['segment'],local_index=test['local_index'])
                r['retrieval_scope']='Train-only learned embedding adapter; source groups are disjoint; fixed directed lag-chain semantics. This is not the full forest analogy head.'
                rows.append(r);print(outdir.name,variant,seed,r['test']['bits_per_symbol'],flush=True)
            except Exception as e:rows.append(dict(variant=variant,seed=seed,error=type(e).__name__+': '+str(e)))
    return dict(metadata=metadata,splits={k:len(g['y'])for k,g in data['groups'].items()},count_model=dict(order=best[1],alpha=best[2],validation_bits=best[0],test=summarize(bp,test,data['reps'],best[4],size)),native=rows,scope='Fresh bounded CPU native encoder component fits, 16 width, one layer, 80 updates, two seeds. Sampled-window ideal int32 BPB is distinct from whole-stream emitted PCM/fixed-point code. Each disconnected context is charged its seed in two-part BPB.')


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--data',type=Path,required=True);p.add_argument('--output',type=Path,required=True);p.add_argument('--native',type=Path,required=True);a=p.parse_args();a.output.mkdir(parents=True,exist_ok=True)
    native,hashes=load_native(a.native);report=dict(schema='grh.physical-controls.v1',created_at_utc=datetime.now(timezone.utc).isoformat(),script_sha256=sha(Path(__file__).read_bytes()),native_module_sha256=hashes,experiments=[],failures=[])
    for name in ['speech','gravitational']:
        folder=a.output/name;folder.mkdir(exist_ok=True)
        try:
            if name=='speech':parts,meta=speech(a.data)
            else:parts,meta,arrays=gravitational(a.data)
            data=prepare_segments(parts);codec=exact_compression(parts,data,'<i2'if name=='speech'else'<i4',folder/'test-stream.grhc')
            record=dict(name=name,source=meta,exact_codec=codec,raw_sample_counts={k:sum(len(x)for x in v)for k,v in parts.items()})
            if name=='gravitational':record['waveform_control']=waveform_control(arrays)
            record['learned']=learned(data,native,folder);report['experiments'].append(record);dump(a.output/'results.json',report)
        except Exception as e:report['failures'].append(dict(experiment=name,error=type(e).__name__+': '+str(e)));dump(a.output/'results.json',report)
    dump(a.output/'results.json',report);print(json.dumps({'experiments':len(report['experiments']),'failures':report['failures']},indent=2))

if __name__=='__main__':main()
