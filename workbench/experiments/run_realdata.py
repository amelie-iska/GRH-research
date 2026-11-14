"""Bounded real-data study: frozen temporal splits, native graph encoders and retrieval.

This is a small component experiment, not training the full Mora-3 model.
CPU only. Quantized symbol likelihood is reported separately from exact integer
residual costs. No result implies language, intent, causal discovery or CCC.
"""
from __future__ import annotations
import argparse, copy, csv, hashlib, importlib.util, io, json, lzma, math, os
from pathlib import Path
import re, sys, time, types, urllib.request, zlib
from datetime import datetime, timezone
from decimal import Decimal
import numpy as np

PIN='75ac2d696f42da0a673fc43a20d84686a2ceed40'
LAG=8
SOURCES={
 'co2':('noaa_co2','https://gml.noaa.gov/webdata/ccgg/trends/co2/co2_mm_mlo.csv','ppm, source precision 0.01','https://gml.noaa.gov/ccgg/trends/','CC0-1.0; NOAA citation requested'),
 'sunspots':('silso_sunspot','https://www.sidc.be/SILSO/DATA/SN_m_tot_V2.0.csv','international sunspot number, source precision 0.1','https://www.sidc.be/SILSO/datafiles','CC-BY-NC-4.0; source-linked, not redistributed'),
 'enso':('noaa_enso','https://psl.noaa.gov/data/correlation/nina34.anom.data','degrees C anomaly, source precision 0.01','https://psl.noaa.gov/data/timeseries/month/','NOAA public data; preserve product citation'),
 'ecg':('physionet_ecg','https://physionet.org/files/mitdb/1.0.0/100.dat','ADC counts, 200 counts/mV, 360 Hz','https://physionet.org/content/mitdb/1.0.0/','ODC-By-1.0; MIT-BIH record 100 attribution required'),
}

def sha(b):return hashlib.sha256(b).hexdigest()
def dump(p,d):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(d,indent=2,allow_nan=False)+'\n')
def fixed(s,scale):
 v=Decimal(s)*scale
 if v!=v.to_integral_value():raise ValueError('Unexpected source precision')
 return int(v)

def acquire(name,root):
 filename,url,unit,landing,license_=SOURCES[name];p=root/filename
 if not p.exists():
  req=urllib.request.Request(url,headers={'User-Agent':'GRH-research reproducible bounded study'})
  with urllib.request.urlopen(req,timeout=45) as r:b=r.read(10000001)
  if len(b)>10000000:raise ValueError('Download exceeds 10 MB')
  p.write_bytes(b)
 b=p.read_bytes();meta=dict(name=name,url=url,landing_page=landing,license=license_,bytes=len(b),sha256=sha(b),units=unit,read_at_utc=datetime.now(timezone.utc).isoformat())
 if name=='co2':
  rows=list(csv.DictReader(io.StringIO('\n'.join(x for x in b.decode().splitlines() if not x.startswith('#')))))
  rows=[r for r in rows if 1958<=int(r['year'])<=2025 and Decimal(r['average'])>=0]
  vals=[fixed(r['average'],100) for r in rows];ids=[int(r['year'])*12+int(r['month'])-1 for r in rows]
  meta['scale']=100;meta['caveat']='Monthly background measurements; Maunakea site substitution in 2022-2023; retrospective revised source, not historical real-time vintage.'
 elif name=='sunspots':
  rows=[x.split(';') for x in b.decode().splitlines() if x.strip()]
  rows=[r for r in rows if 1850<=int(r[0])<=2025 and Decimal(r[3])>=0]
  vals=[fixed(r[3],10) for r in rows];ids=[int(r[0])*12+int(r[1])-1 for r in rows];meta['scale']=10
  meta['caveat']='Monthly observational index, version 2; no smoothed future-centered series; raw data not redistributed.'
 elif name=='enso':
  vals=[];ids=[]
  for line in b.decode().splitlines():
   r=line.split()
   if len(r)!=13 or not re.fullmatch(r'\d{4}',r[0]):continue
   year=int(r[0])
   if not 1948<=year<=2025:continue
   for month,s in enumerate(r[1:]):
    if Decimal(s)>-90:vals.append(fixed(s,100));ids.append(year*12+month)
  meta['scale']=100;meta['caveat']='ERSST-based reconstructed observational index; not raw sensor output or a prospective forecasting vintage.'
 else:
  a=np.frombuffer(b,dtype=np.uint8).reshape(-1,3).astype(np.int32)
  both=np.column_stack((a[:,0]+((a[:,1]&15)<<8),a[:,2]+((a[:,1]>>4)<<8)))
  both=np.where(both>=2048,both-4096,both)
  if both.shape!=(650000,2) or both[0].tolist()!=[995,1011]:raise ValueError('WFDB212/header check failed')
  vals=both[:24000,0].tolist();ids=list(range(len(vals)));meta['scale']=1
  meta['caveat']='First 24000 samples of MLII in one public recording; within-record temporal test, no patient-generalization or diagnostic result.'
 return np.array(vals,dtype=np.int64),np.array(ids,dtype=np.int64),meta

def prepare(values,ids):
 n=len(values);a=int(.6*n);b=int(.8*n)
 if n<200:raise ValueError('Too few observations')
 # The train quantizer sees only first differences wholly inside the training span.
 delta=np.diff(values);good=np.diff(ids)==1
 train_delta=delta[:a-1][good[:a-1]]
 edges=np.unique(np.quantile(train_delta,np.arange(1,8)/8,method='nearest')).astype(np.int64)
 K=len(edges)+1;bins=np.searchsorted(edges,delta,side='right')
 reps=np.array([int(np.median(train_delta[np.searchsorted(edges,train_delta,side='right')==k])) if np.any(np.searchsorted(edges,train_delta,side='right')==k) else 0 for k in range(K)],dtype=np.int64)
 mean=float(train_delta.mean());scale=max(1.,float(train_delta.std()))
 groups={}
 for label,start,end in [('train',0,a),('validation',a,b),('test',b,n)]:
  # Every context and its target remains in one span. Extra lag gap prevents overlap.
  targets=[t for t in range(start+2*LAG+1,end) if np.all(good[t-LAG-1:t])]
  if len(targets)<20:raise ValueError('Insufficient split size')
  idx=np.array(targets);ctx=np.stack([delta[t-LAG-1:t-1] for t in idx]);y=bins[idx-1]
  groups[label]=dict(index=idx,context=ctx,normalized=((ctx-mean)/scale).astype(np.float32),y=y,target=delta[idx-1],raw_value=values[idx])
 return dict(groups=groups,K=K,edges=edges,reps=reps,mean=mean,scale=scale,boundaries=[a,b,n])

def code_lengths(probs,group,reps):
 if probs.ndim!=2 or len(probs)!=len(group['y']) or np.any(probs<=0) or not np.allclose(probs.sum(1),1,atol=1e-6):raise ValueError('Invalid probability table')
 symbol=-np.log2(probs[np.arange(len(probs)),group['y']])
 residual=group['target']-reps[group['y']]
 zig=np.where(residual>=0,2*residual,-2*residual-1)
 gamma=2*np.floor(np.log2(zig+1))+1
 # Previous observed values reconstruct differences; starts need an explicit seed.
 return symbol,gamma

def summarize(probs,group,reps,model_bytes=0,metadata_bytes=0):
 symbol,gamma=code_lengths(probs,group,reps);n=len(symbol);bits=float(symbol.sum());r=float(gamma.sum())
 seed_bits=32*(LAG+1)*(1+int(np.count_nonzero(np.diff(group['index'])!=1)))
 return dict(n=n,symbol_bits=bits,bits_per_symbol=bits/n,residual_bits=r,
  ideal_integer_bpb=(bits+r)/(4*n),canonical_target_bytes=4*n,
  two_part_bpb=(bits+r+8*(model_bytes+metadata_bytes)+seed_bits)/(4*n),
  parameter_bytes=model_bytes,metadata_bytes=metadata_bytes,initial_context_bits=seed_bits,
  graph_side_bits=0,graph_convention='Public deterministic directed 8-lag chain; no target-derived edges; no graph topology bits per observation.',
  residual_convention='Signed zigzag residual + Elias gamma(z+1); exact for fixed-point integer values, not source CSV formatting.',
  coding_scope='Ideal conditional likelihood codelength, not an emitted arithmetic-coded bitstream. Includes exact integer residual; two-part cost also charges state/metadata and explicit lag-context seeds.')

def count_model(train,K,edges,order,alpha):
 table={};global_count=np.bincount(train['y'],minlength=K).astype(float)
 ctx=np.searchsorted(edges,train['context'],side='right')
 for row,y in zip(ctx,train['y']):
  key=tuple(int(v) for v in row[-order:]) if order else ()
  if key not in table:table[key]=np.zeros(K)
  table[key][y]+=1
 def predict(g):
  c=np.searchsorted(edges,g['context'],side='right');out=[]
  for row in c:
   key=tuple(int(v) for v in row[-order:]) if order else ();v=table.get(key,global_count)
   out.append((v+alpha)/(v.sum()+alpha*K))
  return np.array(out)
 wire={'order':order,'alpha':alpha,'rows':[[list(k),v.astype(int).tolist()] for k,v in sorted(table.items())],'fallback':global_count.astype(int).tolist()}
 return predict,len(json.dumps(wire,separators=(',',':')).encode()),wire

def block_interval(values,block,seed=2718):
 rng=np.random.default_rng(seed);blocks=[values[i:i+block] for i in range(0,len(values),block)]
 if len(blocks)<3:return dict(available=False,reason='Fewer than three blocks')
 draws=[float(np.concatenate([blocks[i] for i in rng.integers(len(blocks),size=len(blocks))]).mean()) for _ in range(499)]
 return dict(available=True,mean=float(np.mean(values)),lower=float(np.quantile(draws,.025)),upper=float(np.quantile(draws,.975)),blocks=len(blocks),block_length=block,scope='Exploratory percentile block bootstrap; stationarity not established; no multiplicity-adjusted discovery claim.')

def load_native(native):
 import torch
 pkg=types.ModuleType('_grh_native');pkg.__path__=[str(native)];sys.modules[pkg.__name__]=pkg
 for name in ['tropical','tokengt']:
  p=native/(name+'.py');spec=importlib.util.spec_from_file_location('_grh_native.'+name,p);m=importlib.util.module_from_spec(spec);sys.modules[spec.name]=m;spec.loader.exec_module(m)
 return sys.modules['_grh_native.tokengt'],{p.name:sha(p.read_bytes()) for p in [native/'tokengt.py',native/'tropical.py']}

def train_native(data,native,variant,seed,steps,outdir):
 import torch
 from torch import nn
 torch.set_num_threads(2);torch.manual_seed(seed);rng=np.random.default_rng(seed)
 K=data['K'];model=native.TokenGT(3,LAG,width=16,heads=2,layers=1,ffn_width=32,attention=variant)
 head=nn.Linear(16,K);parameters=list(model.parameters())+list(head.parameters())
 opt=torch.optim.AdamW(parameters,lr=.003,weight_decay=.0001)
 endpoints=torch.tensor([[i,i] for i in range(LAG)]+[[i,i+1] for i in range(LAG-1)],dtype=torch.long)
 roles=torch.tensor([0]*LAG+[1]*(LAG-1),dtype=torch.long);identifiers=torch.eye(LAG)
 def graphs(x):
  result=[]
  for row in x:
   features=torch.zeros(2*LAG-1,3);features[:LAG,0]=torch.from_numpy(row.copy());features[:LAG,1]=torch.arange(LAG)/LAG;features[LAG:,2]=1
   result.append(dict(features=features,endpoints=endpoints,roles=roles,identifiers=identifiers))
  return result
 train=data['groups']['train'];val=data['groups']['validation'];test=data['groups']['test']
 cache={k:graphs(g['normalized']) for k,g in data['groups'].items()}
 def predict(label,embedding=False):
  model.eval();head.eval();parts=[];emb=[]
  with torch.no_grad():
   for i in range(0,len(cache[label]),64):
    h=model(cache[label][i:i+64])[0][:,0];p=head(h).softmax(-1)
    # A fixed uniform floor gives a normalized positive coding distribution.
    parts.append((.999*p+.001/K).cpu().numpy());emb.append(torch.nn.functional.normalize(h,dim=-1).cpu().numpy())
  return np.concatenate(parts),np.concatenate(emb)
 best=None;best_loss=float('inf');history=[];started=time.monotonic()
 for step in range(1,steps+1):
  model.train();head.train();ix=rng.integers(len(cache['train']),size=32)
  h=model([cache['train'][i] for i in ix])[0][:,0]
  loss=nn.functional.cross_entropy(head(h),torch.tensor(train['y'][ix],dtype=torch.long))
  if not torch.isfinite(loss):raise ValueError('Nonfinite training loss')
  opt.zero_grad();loss.backward();nn.utils.clip_grad_norm_(parameters,1.);opt.step()
  if step%20==0 or step==steps:
   p,_=predict('validation');bits=code_lengths(p,val,data['reps'])[0].mean();history.append(dict(step=step,train_loss=float(loss.detach()),validation_bits_per_symbol=float(bits)))
   if bits<best_loss:best_loss=float(bits);best=(copy.deepcopy(model.state_dict()),copy.deepcopy(head.state_dict()),step)
 model.load_state_dict(best[0]);head.load_state_dict(best[1]);trp,trz=predict('train');vp,vz=predict('validation');tp,tz=predict('test')
 # Trained embedding retrieval uses only the disjoint training span and the same
 # directed chain relation. It is a reference adapter, not NativeForestAnalogyHead.
 bank=np.linspace(0,len(trz)-1,min(2048,len(trz)),dtype=int);bz=trz[bank];by=train['y'][bank]
 def retrieval(z):
  answer=[]
  for a in range(0,len(z),256):
   sim=z[a:a+256]@bz.T;ii=np.argpartition(-sim,min(16,len(bz))-1,axis=1)[:,:min(16,len(bz))]
   counts=np.stack([np.bincount(by[j],minlength=K) for j in ii]);answer.append((counts+.5)/(counts.sum(1,keepdims=True)+.5*K))
  return np.concatenate(answer)
 vr=retrieval(vz);tt=retrieval(tz);choices=[0.,.25,.5]
 chosen=min(choices,key=lambda w:code_lengths((1-w)*vp+w*vr,val,data['reps'])[0].mean())
 mixed=(1-chosen)*tp+chosen*tt
 path=outdir/f'{variant}-{seed}.pt';torch.save({'encoder':best[0],'readout':best[1],'variant':variant,'seed':seed,'step':best[2]},path)
 result=dict(variant=variant,seed=seed,steps_attempted=steps,best_step=best[2],parameter_count=sum(x.numel() for x in parameters),parameter_bytes=sum(x.numel()*x.element_size() for x in parameters),checkpoint_bytes=path.stat().st_size,checkpoint_sha256=sha(path.read_bytes()),history=history,elapsed_seconds=time.monotonic()-started,trained_embedding_retrieval_weight=chosen,retrieval_bank_size=len(bank),retrieval_neighbors=min(16,len(bank)),retrieval_bank_bytes=int(bz.nbytes+by.nbytes),retrieval_scope='Train-only learned native graph-token embeddings; exact dot-product shortlist for a fixed directed lag graph; not full native forest analogy, not a transferred physical law.')
 return result,tp,mixed

def run(args):
 root=Path(args.data);root.mkdir(parents=True,exist_ok=True);out=Path(args.output);out.mkdir(parents=True,exist_ok=True)
 native,hashes=load_native(Path(args.native));report=dict(schema='grh.realdata-study.v1',created_at_utc=datetime.now(timezone.utc).isoformat(),native_revision=PIN,native_sha256=hashes,protocol=dict(lag=LAG,train_fraction=.6,validation_fraction=.2,test_fraction=.2,steps=args.steps,seeds=[17,29],variants=['vanilla','tropical-code'],max_identifier_nodes=LAG,device='cpu',source_year_end=2025,selection='Validation only; no failed run dropped',target='Next fixed-point first difference; no target/future in graph input'),datasets=[],failures=[])
 import torch
 report['runtime']=dict(python=sys.version,torch=torch.__version__,numpy=np.__version__)
 for name in args.datasets.split(','):
  start=time.monotonic()
  try:
   values,ids,meta=acquire(name,root);d=prepare(values,ids);groups=d['groups'];folder=out/name;folder.mkdir(exist_ok=True)
   metadata={'edges':d['edges'].tolist(),'representatives':d['reps'].tolist(),'mean':d['mean'],'scale':d['scale'],'source':meta,'splits':d['boundaries'],'lag':LAG}
   mb=len(json.dumps(metadata).encode());candidates=[]
   for order in [0,1,2,4]:
    for alpha in [.1,.5,1.]:
     predict,size,wire=count_model(groups['train'],d['K'],d['edges'],order,alpha)
     v=float(code_lengths(predict(groups['validation']),groups['validation'],d['reps'])[0].mean());candidates.append((v,order,alpha,size,wire,predict))
   best=min(candidates,key=lambda x:(x[0],x[1],x[2]));bp=best[5](groups['test']);basebits=code_lengths(bp,groups['test'],d['reps'])[0]
   uni=next(c for c in candidates if c[1]==0 and c[2]==.5);up=uni[5](groups['test'])
   block=360 if name=='ecg' else 24
   record=dict(name=name,source=meta,observations=len(values),K=d['K'],split_counts={k:len(v['y']) for k,v in groups.items()},metadata=metadata,baseline=dict(order=best[1],alpha=best[2],validation_bits=best[0],**summarize(bp,groups['test'],d['reps'],best[3],mb)),unigram=summarize(up,groups['test'],d['reps'],uni[3],mb),neural=[])
   raw=groups['test']['raw_value'].astype('<i4').tobytes();record['byte_compressors']={key:8*len(f(raw))/len(raw) for key,f in [('zlib_bpb',zlib.compress),('lzma_bpb',lzma.compress)]}
   record['byte_compressors']['scope']='Actual compressor bytes on heldout canonical int32 values; distinct from model conditional coding; decoder overhead not included; not Kolmogorov complexity.'
   for variant in ['vanilla','tropical-code']:
    for seed in [17,29]:
     try:
      r,p,pm=train_native(d,native,variant,seed,args.steps,folder)
      r['test']=summarize(p,groups['test'],d['reps'],r['parameter_bytes'],mb)
      r['retrieval_test']=summarize(pm,groups['test'],d['reps'],r['parameter_bytes']+r['retrieval_bank_bytes'],mb)
      delta=basebits-code_lengths(p,groups['test'],d['reps'])[0];r['gain_over_selected_count_bits_per_symbol']=block_interval(delta,block)
      r['retrieval_gain_bits_per_symbol']=float((code_lengths(p,groups['test'],d['reps'])[0]-code_lengths(pm,groups['test'],d['reps'])[0]).mean())
      np.savez_compressed(folder/f'{variant}-{seed}-predictions.npz',index=groups['test']['index'],labels=groups['test']['y'],probability=p,retrieval_probability=pm,baseline=bp)
      record['neural'].append(r);print(name,variant,seed,r['test']['bits_per_symbol'],r['retrieval_gain_bits_per_symbol'],flush=True)
     except Exception as e:record['neural'].append({'variant':variant,'seed':seed,'error':type(e).__name__+': '+str(e)})
   # A circular offset diagnostic is NOT a calibrated test for these nonstationary series.
   rng=np.random.default_rng(881);scores=[];n=len(bp)
   for offset in rng.integers(LAG+1,n-LAG,size=31):
    y=np.roll(groups['test']['y'],int(offset));scores.append(float((-np.log2(bp[np.arange(n),y])).mean()))
   record['shift_diagnostic']=dict(actual_bits=float(basebits.mean()),shifted_bits=scores,scope='Descriptive label-context offset comparison only; exchangeability and stationarity not assumed; no significance p-value.')
   record['elapsed_seconds']=time.monotonic()-start;report['datasets'].append(record);dump(out/'results.json',report)
  except Exception as e:report['failures'].append(dict(dataset=name,error=type(e).__name__+': '+str(e)));dump(out/'results.json',report)
 dump(out/'results.json',report)
 return report

if __name__=='__main__':
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--data',required=True);p.add_argument('--output',required=True);p.add_argument('--native',required=True);p.add_argument('--steps',type=int,default=80);p.add_argument('--datasets',default='co2,sunspots,enso,ecg');a=p.parse_args()
 if not 20<=a.steps<=200:raise ValueError('Bounded 20-200 optimizer steps only')
 run(a)
