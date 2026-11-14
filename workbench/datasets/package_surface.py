"""Build the version-two release from verified sources; publishing is separate.

This builder does not read credentials. It preserves the prior scientific packet,
adds the exact proof port, measured speech/strain graph windows, native results,
actual lossless packets, and current reproduction sources. Every new graph row
is checked against raw context/target support before publication.
"""
from __future__ import annotations
import argparse,hashlib,json,shutil,subprocess,sys,zipfile
from pathlib import Path
from datetime import datetime,timezone
import numpy as np

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'experiments'))
from physical_controls import speech,gravitational,prepare_segments,SPEAKERS
from exact_codec import decode
from run_realdata import summarize

PREVIOUS='84aa1e7241e67c9b85e31d2e45400d3f285c001d'

def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def dump(path,value):path.parent.mkdir(parents=True,exist_ok=True);path.write_text(json.dumps(value,indent=2,ensure_ascii=False,allow_nan=False)+'\n')
def copy(source,destination):destination.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(source,destination)


def graph_records(name,parts,meta,data,acquisition,out):
    identities=set();supports={};counts={};raw_files={r['path']:r for r in acquisition['files']}
    for split,g in data['groups'].items():
        path=out/'data'/('speech_graphs'if name=='speech'else'gw_graphs')/(split+'.jsonl');path.parent.mkdir(parents=True,exist_ok=True);counts[split]=0
        with path.open('w')as f:
            for row,(segment,t,ctx,target,label)in enumerate(zip(g['segment'],g['local_index'],g['context'],g['target'],g['y'])):
                segment,t=int(segment),int(t);values=parts[split][segment]
                if not np.array_equal(np.diff(values.astype(np.int64))[t-9:t-1],ctx)or int(values[t]-values[t-1])!=int(target):raise ValueError('Context or target mismatch')
                if name=='speech':
                    info=[r for r in meta['files']if r['split']==split][segment];source_hash=info['flac_sha256'];source_id=info['file'];group='speaker:'+info['speaker'];rate=16000;origin=0;unit='signed PCM16 count'
                else:
                    info=meta['quantization'][split];short=info['detector'];source=next(r for r in acquisition['files']if r.get('path')==short+'.txt.gz');source_hash=source['sha256'];source_id=short+'.txt.gz';group=short+':'+str(info['start_seconds'])+'-'+str(info['end_seconds']);rate=4096;origin=info['start_seconds']*rate;unit='strain / 1e-24, rounded int32'
                identity=f'{name}:{source_hash}:{origin+t}'
                if identity in identities:raise ValueError('Duplicate target identity')
                identities.add(identity);support=supports.setdefault(split,set());support.update((source_hash,origin+j)for j in range(t-9,t+1))
                graph={'nodes':[{'id':i,'role':'observed_past_difference','value':int(v),'relative_target_index':i-8}for i,v in enumerate(ctx)],'edges':[{'source':i,'target':i+1,'relation':'next_observed_sample'}for i in range(7)]}
                record=dict(id=identity,source=name,source_file=source_id,source_sha256=source_hash,source_url=meta['url'],split=split,group_id=group,segment=segment,time_index=origin+t,sample_rate_hz=rate,units=unit,input_differences=[int(v)for v in ctx],target_difference=int(target),target_value=int(values[t]),previous_value_for_reconstruction=int(values[t-1]),quantized_target=int(label),graph_json=json.dumps(graph,separators=(',',':')),target_in_input=False,provenance='measured_physical_signal',representation='PCM16'if name=='speech'else'fixed_point_int32',quantization='Native decoded PCM16'if name=='speech'else'round(strain/1e-24); representation error in source report',training_admission='Explicit split only; overlapping windows remain within their declared group')
                f.write(json.dumps(record,separators=(',',':'))+'\n');counts[split]+=1
    for i,a in enumerate(supports):
        for b in list(supports)[i+1:]:
            if supports[a]&supports[b]:raise ValueError('Cross-split raw-support overlap')
    return dict(counts=counts,duplicate_ids=0,cross_split_raw_support_overlap=0,groups='Distinct speakers'if name=='speech'else'Disjoint source detector/time intervals; one-event local control, not independent-event generalization')


def build(a):
    if a.output.exists():raise ValueError('Use a new output directory')
    baseline=json.loads((a.baseline/'manifest.json').read_text())
    for name,info in baseline['files'].items():
        path=a.baseline/name
        if not path.is_file()or path.stat().st_size!=info['bytes']or sha(path)!=info['sha256']:raise ValueError('Baseline manifest mismatch '+name)
    shutil.copytree(a.baseline,a.output)
    history=a.output/'history/84aa1e7';history.mkdir(parents=True,exist_ok=True)
    for name in ['README.md','manifest.json','source-catalog.json','LICENSES.md']:copy(a.baseline/name,history/name)
    record=json.loads((a.results/'results.json').read_text());acq=json.loads((a.raw/'acquisition-verified.json').read_text())
    if acq['transcript_coverage']['missing']!=0 or acq['transcript_coverage']['matched_transcripts']!=18:raise ValueError('Incomplete communication provenance')
    for r in acq['files']:
        source=a.raw/r['path']
        if sha(source)!=r['sha256']or source.stat().st_size!=r['bytes']:raise ValueError('Acquisition hash mismatch')
        copy(source,a.output/'sources/physical-controls'/r['path'])
    for name in ['acquisition-verified.json','selected-transcripts.json']:copy(a.raw/name,a.output/'sources/physical-controls'/name)
    # The old unscoped transcripts.txt files are intentionally not admitted.
    new_counts={};replay=[]
    for result in record['experiments']:
        name=result['name'];parts,meta=(speech(a.raw)if name=='speech'else gravitational(a.raw)[:2]);data=prepare_segments(parts)
        new_counts[name]=graph_records(name,parts,meta,data,acq,a.output)
        decoded=decode((a.results/name/'test-stream.grhc').read_bytes())
        if len(decoded)!=len(parts['test'])or any(not np.array_equal(x,y)for x,y in zip(decoded,parts['test'])):raise ValueError('Codec replay mismatch')
        if sha(a.results/name/'test-stream.grhc')!=result['exact_codec']['sha256']:raise ValueError('Codec hash drift')
        for run in result['learned']['native']:
            if 'error'in run:raise ValueError('Unresolved native run failure')
            p=a.results/name/f"{run['variant']}-{run['seed']}-predictions.npz";arrays=np.load(p)
            group=data['groups']['test']
            if not np.array_equal(arrays['labels'],group['y'])or not np.array_equal(arrays['local_index'],group['local_index'])or not np.array_equal(arrays['segment'],group['segment']):raise ValueError('Prediction target alignment failed')
            for key,stored in [('probability','test'),('retrieval_probability','retrieval_test')]:
                expected=run[stored];actual=summarize(arrays[key],group,data['reps'],expected['parameter_bytes'],expected['metadata_bytes'])
                for metric in ['symbol_bits','bits_per_symbol','residual_bits','ideal_integer_bpb','two_part_bpb','canonical_target_bytes','initial_context_bits']:
                    if not np.isclose(actual[metric],expected[metric],rtol=1e-10,atol=1e-8):raise ValueError('Codelength replay mismatch '+metric)
            checkpoint=a.results/name/f"{run['variant']}-{run['seed']}.pt"
            if sha(checkpoint)!=run['checkpoint_sha256']:raise ValueError('Checkpoint mismatch')
            replay.append(dict(source=name,variant=run['variant'],seed=run['seed'],targets=len(group['y']),score_residual_denominator_and_checkpoint_match=True))
        for p in (a.results/name).iterdir():
            if p.suffix in ('.pt','.npz','.grhc'):copy(p,a.output/'evidence/physical-controls'/name/p.name)
    copy(a.results/'results.json',a.output/'evidence/physical-controls/results.json')
    # Current source is distinct from the immutable older source revision.
    for p in ROOT.rglob('*'):
        if p.is_file()and p.suffix in {'.py','.js','.html','.css','.tex','.md','.lean'}and not any(x in p.parts for x in ['.local','.generated','__pycache__','.lake','.venv']):copy(p,a.output/'reproduction'/p.relative_to(ROOT))
    # Include the exact assets needed by the otherwise standalone reproduction.
    repo=ROOT.parent
    for name in ['extension/site/quantum-core.js','extension/site/data/torus3x3.json','extension/quantum/gpu_experiments.py','extension/lean/verify_all.py','extension/quantum/requirements-gpu.lock']:
        copy(repo/name,a.output/'reproduction-project-dependencies'/name)
    copy(a.paper,a.output/'documents/certified-surface-computation.pdf')
    proofdir=a.output/'proof-port';shutil.copytree(a.proofs,proofdir)
    with zipfile.ZipFile(a.output/'documents/source-proof-port.zip','w',zipfile.ZIP_DEFLATED)as z:
        for p in sorted(a.proofs.rglob('*')):
            if p.is_file():z.write(p,str(p.relative_to(a.proofs)))
    destination=a.output/'evidence/surface-release';destination.mkdir(parents=True,exist_ok=True)
    allowed=['expressivity-witnesses.json','quantum-cpu.json','quantum-gpu.json','realizations.json','half-density-cpu.json','half-density-gpu.json','provenance-repair.json','pdf-pass-3.log','browser-check.py','final-audit.py']
    for name in allowed:
        if (a.evidence/name).is_file():copy(a.evidence/name,destination/name)
    for name in ['final','browser']:
        shutil.copytree(a.evidence/name,destination/name)
    for p in (a.evidence/'pdf-qa').glob('contact-*.png'):copy(p,destination/'pdf-qa'/p.name)
    audit=dict(schema='grh.surface-package-audit.v1',baseline_members_verified=len(baseline['files']),new_graphs=new_counts,model_prediction_replays=replay,lossless_packet_replays=2,transcript_coverage=acq['transcript_coverage'],scientific_results_sha256=sha(a.results/'results.json'),old_results_preserved=sha(a.output/'evidence/results.json')==baseline['experiment_sha256'],old_pdf_preserved=sha(a.output/'documents/graph-computation-category-o.pdf')==baseline['files']['documents/graph-computation-category-o.pdf']['sha256'])
    if not audit['old_results_preserved']or not audit['old_pdf_preserved']:raise ValueError('Historical artifact changed')
    dump(destination/'package-audit.json',audit)
    # A release editor writes the current card/catalog/terms before manifest sealing.
    dump(a.output/'version2-build.json',dict(schema='grh.surface-package-build.v1',created_at_utc=datetime.now(timezone.utc).isoformat(),source_commit=subprocess.check_output(['git','rev-parse','HEAD'],cwd=repo,text=True).strip(),previous_revision=PREVIOUS,new_record_counts=new_counts,package_audit='evidence/surface-release/package-audit.json'))
    return audit

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    for name in ['baseline','raw','results','proofs','evidence','paper','output']:p.add_argument('--'+name,type=Path,required=True)
    args=p.parse_args();print(json.dumps(build(args),indent=2))
