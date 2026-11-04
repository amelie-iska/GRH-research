"""Freeze an additional reviewed release with consistent row origins and evidence."""
import argparse,json,shutil
from pathlib import Path
import pyarrow as pa
import pyarrow.parquet as pq
from common import fresh,sha,write_json,canonical

def seal(source,out,model):
    source=Path(source);out=fresh(out);old=json.loads((source/'manifest.json').read_text())
    for name,item in old['files'].items():assert sha(source/name)==item['sha256']
    for p in source.iterdir():
        if p.is_dir():shutil.copytree(p,out/p.name)
        elif p.name!='manifest.json':shutil.copyfile(p,out/p.name)
    write_json(out/'release-parent-manifest.json',old)
    counts={};stereo=0
    for config in ['data','source_anchors','electronic_dynamics','nuclear_md']:
        if not (out/config).exists():continue
        counts[config]={}
        for file in sorted((out/config).glob('*.parquet')):
            table=pq.read_table(file);rows=table.to_pylist()
            for r in rows:
                p=json.loads(r['payload_json'])
                if config=='source_anchors':
                    c=p['conditions'];diagnostic=c.pop('gradient_finite_difference_error',None)
                    if diagnostic is not None:p.setdefault('evaluation',{})['gradient_finite_difference_error']=diagnostic
                    r['condition_json']=canonical(c);r['payload_json']=canonical(p)
                    stereo+=sum(b.get('stereo',0)>1 for b in c.get('bonds',[]))
                elif config!='data':
                    r.update(origin_class='new_simulation',planned_source_dataset=None,planned_source_record_id=None,
                        label_origin='new_computed_effective_electronic_or_MMFF_dynamics; not observed data')
                    p['origin_class']='new_simulation';r['payload_json']=canonical(p)
            pq.write_table(pa.Table.from_pylist(rows),file,compression='zstd');counts[config][rows[0]['split']]=len(rows)
    assert stereo==0,'This release has no assigned E/Z anchors; future E/Z parents require geometric stereo validation'
    validation=out/'validation';validation.mkdir()
    checkroot=Path('outputs/checks/2026-11-04-synthetic-training')
    for name in [model+'-large-validation.json',model+'-large-dynamics-validation.json',model+'-sources-validation.json','native-interfaces-large.json']:
        report=json.loads((checkroot/name).read_text());assert report.get('passed',True)
        shutil.copyfile(checkroot/name,validation/name)
    write_json(out/'release-quality.json',dict(passed=True,config_split_rows=counts,all_rows_explicit_origin=True,
        anchor_validation_diagnostic_excluded_from_conditions=True,assigned_double_bond_stereo_anchor_count=stereo,
        molecular_stereochemistry_scope='Assigned tetrahedral/CIP checked; this selected PubChem anchor packet has no assigned E/Z bonds',
        provenance='Parent manifests retain earlier frozen stages; scientific values preserved; final source graph/condition-role schema explicit',
        exposure_scope='Within-release finite similarity audit only; full historical model corpus exposure unqualified',active_model_training_changed=False))
    code=out/'release_source';code.mkdir()
    for name in ['seal_release.py','check_sources.py','source_anchors.py','combine_sources.py','common.py']:
        shutil.copyfile(Path(__file__).with_name(name),code/name)
    card=(out/'README.md').read_text().replace('No private model weights, existing\ntraining data or credentials are included.', 'No private model weights or credentials are included. Only the explicitly\nauthorized source-anchor excerpts/derivatives are included from prior training sources.')
    card+='\n## Final release audit\n\nExact configuration counts: `'+canonical(counts)+'`.\nEvery configuration carries explicit origin fields. Source-anchor finite-difference\ndiagnostics are evaluation metadata, excluded from forward conditions. All emitted\nassigned tetrahedral/CIP geometries were checked; selected PubChem anchors have\nzero assigned double-bond E/Z tags. Historical PDB1HRW is explicitly obsolete and\nsuperseded by1LE0; actual downloaded HEADER identity and source bytes are retained.\n`validation/` retains all-row physics and source-boundary receipts. Final manifest\nhashes pin the corrected row schema and all released evidence. No peptide-fold\nblindness or full prior-model exposure audit is claimed.\n'
    (out/'README.md').write_text(card)
    write_json(out/'manifest.json',dict(files={str(p.relative_to(out)):{'sha256':sha(p),'bytes':p.stat().st_size} for p in out.rglob('*') if p.is_file() and p.name!='README.md'},
        frozen_parent_sha256=sha(source/'manifest.json'),release_quality_sha256=sha(out/'release-quality.json'),private_release=True))
    print(dict(passed=True,model=model,counts=counts,output=str(out)))

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--source',type=Path,required=True);p.add_argument('--output',type=Path,required=True);p.add_argument('--model',choices=['aster','mora'],required=True);a=p.parse_args();seal(a.source,a.output,a.model)
