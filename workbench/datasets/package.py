"""Build an allowlisted, rights-aware HF artifact from the executed study.

No credentials are read by this builder. Publishing is a separate explicit step.
Measured NOAA records, test-only mathematical fixtures and experiment summaries
are separate configurations. Restricted external raw data are not copied.
"""
from __future__ import annotations
import argparse,hashlib,json,shutil,sys
from pathlib import Path
from datetime import datetime,timezone

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT));sys.path.insert(0,str(ROOT/'experiments'))
from contracts import certificate,canonical
from run_realdata import acquire,prepare,LAG,SOURCES

def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def dump(p,value):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(value,indent=2,allow_nan=False)+'\n')

def build(raw:Path,results:Path,out:Path,paper:Path|None=None):
 if out.exists() and any(out.iterdir()):raise ValueError('Use a fresh output directory')
 out.mkdir(parents=True,exist_ok=True);(out/'data').mkdir();(out/'evidence').mkdir()
 record=json.loads((results/'results.json').read_text());counts={k:0 for k in ('train','validation','test')};ids=set();supports={};sources=[]
 for split in counts:(out/'data'/f'{split}.jsonl').write_text('')
 for name in ('co2','enso'):
  values,times,meta=acquire(name,raw);expected=next(x['source']['sha256'] for x in record['datasets'] if x['name']==name)
  if meta['sha256']!=expected:raise ValueError('Raw source hash differs from the executed study')
  d=prepare(values,times);sources.append(meta)
  for split,g in d['groups'].items():
   support=set()
   with (out/'data'/f'{split}.jsonl').open('a') as f:
    for t,ctx,label in zip(g['index'],g['context'],g['y']):
     t=int(t);identity=f'{name}:{expected}:{t}'
     if identity in ids:raise ValueError('Duplicate record identity')
     ids.add(identity);support.update(range(t-LAG-1,t+1))
     graph={'nodes':[{'id':i,'role':'observed_past_difference','value':int(v)}for i,v in enumerate(ctx)],'edges':[{'source':i,'target':i+1,'relation':'next_observed_month'}for i in range(LAG-1)]}
     row={'id':identity,'source':name,'source_sha256':expected,'source_url':meta['url'],'split':split,'group_id':name+':'+split,'time_index':int(times[t]),'units':meta['units'],'fixed_point_scale':meta['scale'],'input_differences':[int(v)for v in ctx],'target_difference':int(g['target'][counts[split]-counts[split]]) if False else int(values[t]-values[t-1]),'target_value':int(values[t]),'previous_value_for_reconstruction':int(values[t-1]),'quantized_target':int(label),'graph_json':json.dumps(graph,separators=(',',':')),'target_in_input':False,'provenance':'measured_or_observation_derived','uncertainty':'Source-native uncertainty is not replaced by neural confidence; see original product.'}
     f.write(json.dumps(row,separators=(',',':'))+'\n');counts[split]+=1
   supports[name,split]=support
  for i,a in enumerate(counts):
   for b in list(counts)[i+1:]:
    if supports[name,a]&supports[name,b]:raise ValueError('Raw temporal support leakage')
 examples=[certificate('heat',{'r':r})for r in ('0','1/8','1/4')]
 examples.extend([certificate('rank',{'draws':4095,'exceedances':0}),certificate('risk',{'tests':288,'per_test':'1/10000','drift':'1/100','alpha':'1/20'}),certificate('gain',{'matrix':[['1/4','3/2'],['3/32','1/4']],'weights':['4','1'],'rate':'5/8'}),certificate('mutation',{'matrix':[[0,1],[-1,0]],'seed':['2','5'],'vertex':0})])
 with (out/'data/reference.jsonl').open('w')as f:
  for i,c in enumerate(examples):f.write(json.dumps({'id':f'finite-reference-{i}','kind':c['kind'],'certificate_json':canonical(c),'provenance':'constructed_exact_mathematical_fixture','training_admission':False})+'\n')
 for name in ('results.json','text-control.json','initial-failure.json','adapter-failure.json'):
  p=results/name
  if p.exists():shutil.copy2(p,out/'evidence'/name)
 # Only NOAA-derived per-record predictions/checkpoints are redistributed here.
 for source in ('co2','enso'):
  for p in (results/source).glob('*'):
   if p.suffix in ('.npz','.pt'):
    dest=out/'evidence'/source/p.name;dest.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,dest)
 allowed={'.py','.js','.html','.css','.tex','.md','.lean'}
 for p in ROOT.rglob('*'):
  if p.is_file() and p.suffix in allowed and not any(v in p.parts for v in ('.local','.generated','.venv','.lake','__pycache__')):
   dest=out/'reproduction'/p.relative_to(ROOT);dest.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,dest)
 if paper:
  (out/'documents').mkdir();shutil.copy2(paper,out/'documents/graph-computation-category-o.pdf')
 catalog=[]
 for name,(filename,url,units,landing,terms)in SOURCES.items():
  catalog.append({'id':name,'landing':landing,'download':url,'units':units,'terms':terms,'status':'executed','included_records':name in ('co2','enso'),'reason':None if name in ('co2','enso') else 'Only aggregate experimental results redistributed; raw records and per-record predictions remain source-linked.'})
 for name,url in [('Gutenberg English','https://www.gutenberg.org/ebooks/11'),('Planck CMB','https://pla.esac.esa.int/'),('GWOSC strain','https://gwosc.org/'),('JHTDB turbulence','https://turbulence.pha.jhu.edu/'),('PDEBench simulations','https://github.com/pdebench/PDEBench'),('UCI human activity','https://archive.ics.uci.edu/dataset/240/human+activity+recognition+using+smartphones')]:
  catalog.append({'id':name,'landing':url,'status':'executed_text_control' if name=='Gutenberg English' else 'proposed_not_acquired','included_records':False,'terms':'Consult the source-specific release before any redistribution; no rights inferred from a public URL.'})
 dump(out/'source-catalog.json',catalog)
 (out/'LICENSES.md').write_text('''# Component-specific rights and provenance

This collection does not relicense third-party sources. NOAA GML data carry the
source CC0 designation and citation request; NOAA PSL federal data retain their
source attribution and product qualifications. The included measured graph views
are derived only from those NOAA sources. Consult the catalog and original
products for authoritative terms. Original project code and documentation retain
the terms of the associated GRH-research repository; public visibility alone is
not a grant of additional third-party rights.

SILSO states CC BY-NC 4.0. Its raw data, per-record predictions and checkpoints are
not redistributed here. PhysioNet MIT-BIH uses ODC Attribution 1.0; this release
links its raw data rather than copying them. The aggregate comparison is not a
clinical result. The Gutenberg positive control is source-linked; its raw book
is not included. No third-party paper PDF, private dataset, token or credential
is included. Constructed exact fixtures are expressly distinguished from
measurements and are test-only, not admitted neural training examples.
''')
 lines=['---','license: other','license_name: component-specific-source-terms','license_link: LICENSES.md','task_categories:','- time-series-forecasting','configs:','- config_name: measured_noaa_graphs','  data_files:']
 for split in counts:lines.extend([f'  - split: {split}',f'    path: data/{split}.jsonl'])
 lines.extend(['- config_name: exact_reference_fixtures','  data_files:','  - split: test','    path: data/reference.jsonl','---','', '# GRH Physical Graph Workbench','', 'Associated project: https://github.com/amelie-iska/GRH-research','', '## What is included','',f'This release includes {sum(counts.values())} actual NOAA-derived directed lag-graph records ({counts}), {len(examples)} separate exact test fixtures, code, source hashes, aggregate results from sixteen freshly trained small native Mora-3 encoder runs, and a known human-English control. It is not a full Mora-3 checkpoint, a general physical-language corpus or evidence of a hidden message.','', 'The four executed process sources are CO2, sunspots, Niño-3.4 and one public ECG recording. Only the two NOAA sources are redistributed at record level. Other sources remain linked with aggregate results. Planned CMB, gravitational-wave, fluid and sensor studies are not labeled executed.','', '## Protocol and limitations','', 'Chronological train/validation/test spans have disjoint raw context/target support; group IDs are temporal span identities within one physical series, not independent systems. Repeated genuine values are not deleted as duplicate observations: deduplication uses source revision and original observation index. Target columns are explicit and never part of input graph_json. Scaling, bins, memory and fitting use training only; validation selects the checkpoint/baseline/mixture.','', 'Reported symbol likelihood is separate from exact integer residual cost and model-inclusive BPB. The native pilot uses one 16-wide layer, two heads, seeds 17/29 and 80 optimizer steps. It is not the 80M model, the original training campaign, trained GFlowNet/quantum extension or full native forest analogy head. Retrieval is a trained-embedding temporal adapter.','', 'Compression and dependence do not establish semantics, intent, causal effects or CCC. Kolmogorov complexity is not measured; actual compressors and ideal codelengths are explicitly labeled proxies. Two-part storage costs can overwhelm predictive gains on short samples.','', '## Evidence','', '`evidence/results.json` contains all successful final runs, per-seed histories, source hashes and qualified bootstrap/offset diagnostics. Failed preflight records are retained separately. NOAA-only probability arrays and component checkpoints support replay. The human-language control uses actual Gutenberg text with no raw text redistribution. `reproduction/` contains the exact source; `source-catalog.json` distinguishes executed and proposed sources.','', '## Source attribution','', 'NOAA Global Monitoring Laboratory: Lan, Tans and Thoning, Trends in Atmospheric Carbon Dioxide. NOAA Physical Sciences Laboratory: ERSST Niño-3.4 anomaly. SILSO, Royal Observatory of Belgium, International Sunspot Number version 2, DOI 10.24414/qnza-ac80. Moody and Mark, MIT-BIH Arrhythmia Database 1.0.0, PhysioNet, DOI 10.13026/C2F305. Lewis Carroll, Alice’s Adventures in Wonderland, Project Gutenberg ebook 11.',''])
 (out/'README.md').write_text('\n'.join(lines))
 manifest={'schema':'grh.dataset-package.v1','created_at_utc':datetime.now(timezone.utc).isoformat(),'record_counts':counts,'reference_records':len(examples),'duplicate_record_ids':0,'cross_split_raw_support_overlap':0,'experiment_sha256':digest(results/'results.json'),'files':{str(p.relative_to(out)):{'bytes':p.stat().st_size,'sha256':digest(p)}for p in out.rglob('*')if p.is_file()}}
 dump(out/'manifest.json',manifest);return manifest

if __name__=='__main__':
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--raw',type=Path,required=True);p.add_argument('--results',type=Path,required=True);p.add_argument('--output',type=Path,required=True);p.add_argument('--paper',type=Path);a=p.parse_args();m=build(a.raw,a.results,a.output,a.paper);print(json.dumps({k:v for k,v in m.items()if k!='files'},indent=2))
