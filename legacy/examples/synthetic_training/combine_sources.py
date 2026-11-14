"""Add separately labelled planned-source anchors; preserve frozen input data."""
import argparse,json,shutil
from collections import Counter,defaultdict
from pathlib import Path
from common import fresh,sha,write_json

def quarantine_conflicts(source,anchors,out):
    """Never move frozen default heldouts: exclude conflicting anchor parents."""
    import numpy as np
    import pyarrow as pa
    import pyarrow.parquet as pq
    from rdkit import Chem,DataStructs
    from rdkit.Chem import rdFingerprintGenerator
    from rdkit.Chem.Scaffolds import MurckoScaffold
    path=out/'source_anchors'/'train-00000-of-00001.parquet'
    table=pq.read_table(path);rows=table.to_pylist();fpgen=rdFingerprintGenerator.GetMorganGenerator(radius=2,fpSize=2048,includeChirality=False)
    def features(smiles):
        m=Chem.MolFromSmiles(smiles)
        return (Chem.MolToSmiles(m,isomericSmiles=False),MurckoScaffold.MurckoScaffoldSmiles(mol=m,includeChirality=False),fpgen.GetFingerprint(m))
    held=[];chem={};geometry=defaultdict(list)
    for shard in sorted((source/'data').glob('*.parquet')):
        for r in pq.read_table(shard).to_pylist():
            if r['split']=='train':continue
            p=json.loads(r['payload_json']);s=p.get('canonical_smiles')
            if not s:continue
            chem.setdefault(s,features(s));c=p['conditions'];z=np.array(c['atomic_numbers']);x=np.array(c['coordinates_angstrom'])[z>1]
            d=np.linalg.norm(x[:,None]-x[None,:],axis=-1);sig=tuple(sorted(z[z>1].tolist()))
            geometry[sig].append((r['record_id'],np.sort(d[np.triu_indices(len(x),1)])))
            held.append((r['record_id'],s))
    rejected={};checked=0;nearest=0.;minimum=float('inf')
    for r in rows:
        p=json.loads(r['payload_json']);c=p['conditions'];s=c.get('canonical_smiles')
        if not s:continue # PDB coarse residue graphs and MP20 crystals are separate tasks.
        checked+=1;constitution,scaffold,fp=features(s);group=r['group_id']
        for hs,(hc,hsc,hfp) in chem.items():
            similarity=DataStructs.TanimotoSimilarity(fp,hfp);nearest=max(nearest,similarity)
            reason='same_constitution' if constitution==hc else ('same_nonempty_scaffold' if scaffold and scaffold==hsc else ('Morgan>=0.65' if similarity>=.65 else None))
            if reason:rejected.setdefault(group,dict(anchor=r['record_id'],heldout_smiles=hs,reason=reason,tanimoto=similarity))
        z=np.array(c['atomic_numbers']);x=np.array(c['coordinates_angstrom'])[z>1];d=np.linalg.norm(x[:,None]-x[None,:],axis=-1);v=np.sort(d[np.triu_indices(len(x),1)])
        for hid,w in geometry[tuple(sorted(z[z>1].tolist()))]:
            distance=float(np.sqrt(np.mean((v-w)**2)));minimum=min(minimum,distance)
            if distance<=.10:rejected.setdefault(group,dict(anchor=r['record_id'],heldout_record=hid,reason='all_conformer_heavy_distance_descriptor<=0.10angstrom',distance_angstrom=distance))
    retained=[r for r in rows if r['group_id'] not in rejected]
    assert retained
    # Excluded rows remain immutable in the parent packet, never in upload shards.
    pq.write_table(pa.Table.from_pylist(retained,schema=table.schema),path,compression='zstd')
    audit=dict(passed=True,policy='Quarantine complete source parent if any variant conflicts with frozen default validation/test; no heldout moved',
        input_anchor_rows=len(rows),retained_anchor_rows=len(retained),excluded_rows=len(rows)-len(retained),excluded_parents=len(rejected),
        exclusion_witnesses=rejected,checked_molecular_anchor_rows=checked,default_heldout_rows=len(held),
        source_chemistry_threshold=.65,source_geometry_threshold_angstrom=.10,
        pre_quarantine_max_Tanimoto=nearest,pre_quarantine_min_geometry_angstrom=minimum if np.isfinite(minimum) else None,
        retained_direct_threshold_crossings=0,
        scope='All emitted molecular anchor geometries vs all default heldouts. PDB residue contact models/MP20 effective crystals are distinct tasks, train only; no fold-blind/global corpus claim.')
    write_json(out/'source-cross-configuration-audit.json',audit)
    quality=json.loads((out/'source-anchor-quality.json').read_text());quality.update(records=len(retained),origin_counts=dict(Counter(r['origin_class'] for r in retained)),retained_parent_groups=len({r['group_id'] for r in retained}),quarantined_rows=audit['excluded_rows'])
    write_json(out/'source-anchor-quality.json',quality)
    return audit

def combine(source,anchors,out):
    source=Path(source);anchors=Path(anchors);out=fresh(out)
    for root in [source,anchors]:
        m=json.loads((root/'manifest.json').read_text())
        for name,entry in m['files'].items():assert sha(root/name)==entry['sha256'],name
    for p in source.iterdir():
        if p.is_dir():shutil.copytree(p,out/p.name)
        elif p.name!='manifest.json':shutil.copyfile(p,out/p.name)
    write_json(out/'simulated-parent-manifest.json',json.loads((source/'manifest.json').read_text()))
    for p in anchors.iterdir():
        if p.name=='manifest.json':write_json(out/'anchor-parent-manifest.json',json.loads(p.read_text()))
        elif p.is_dir():shutil.copytree(p,out/p.name)
        else:shutil.copyfile(p,out/p.name)
    code=out/'anchor_source';code.mkdir();shutil.copyfile(Path(__file__).with_name('source_anchors.py'),code/'source_anchors.py');shutil.copyfile(__file__,code/'combine_sources.py')
    quarantine_conflicts(source,anchors,out)
    card=(out/'README.md').read_text();needle='''  - split: test
    path: data/test-*.parquet'''
    card=card.replace(needle,needle+'''
- config_name: source_anchors
  data_files:
  - split: train
    path: source_anchors/train-*.parquet''')
    quality=json.loads((out/'quality.json').read_text());anchor=json.loads((out/'source-anchor-quality.json').read_text())
    assert quality['records']>=10000
    card+=f'''\n## Size and explicit data origin\n\nThe default configuration contains **{quality['records']:,} static response/conformer
rows** before any time frames are counted. Separate source-anchor rows: {anchor['records']}.
Dynamics configurations count trajectories as rows, not each time step as an
independent system. Distinct parents and similarity components are reported.

`origin_class`, `planned_source_dataset`, `planned_source_record_id` and
`label_origin` distinguish reused planned-source identity/geometry, new public
structure anchors and newly computed/synthetic labels. The default source is
new simulations; novelty of chemical identity against all existing corpora is
not asserted. Source-linked variants are additional computed data, not newly
measured experimental or ab-initio labels.

`source_anchors` is **train only**. Existing Aster MP20 and Mora PubChem source
training assignments are respected. Public PDB coordinate anchors retain
CC0/DOI/hash and a qualified relation to the planned structural source family;
no PDBbind affinity or measured CISS label is copied. Quantum-transfer models
constructed on their graphs are uncalibrated effective models. Source structures
are not proofs of those quantum properties. A molecular source parent and all
its variants are excluded if they conflict with any frozen default validation/test
identity, scaffold, Morgan>=0.65 or applicable all-conformer heavy-distance
descriptor<=0.10angstrom. The source-cross-configuration audit records witnesses;
excluded data remain preserved in the parent packet, outside release shards.
Retained parent derivatives remain together. These anchors cannot establish blind model performance when their
parents may already have been seen. Global cross-corpus exposure and broader
chemical/protein similarity admission remain the owning model's evaluation
gates, separate from the within-release component audit.
'''
    (out/'README.md').write_text(card)
    origin=dict(default_new_simulation_rows=quality['records'],source_anchor_rows=anchor['records'],source_origin_counts=anchor['origin_counts'],
        static_frame_counting='One response/conformer record per row; no inflation by time frames',
        active_model_changes=False,private_release=True,minimum_10000_default_rows=True)
    write_json(out/'origin-summary.json',origin)
    old=json.loads((source/'manifest.json').read_text())
    files={str(p.relative_to(out)):{'sha256':sha(p),'bytes':p.stat().st_size} for p in out.rglob('*') if p.is_file() and p.name!='README.md'}
    write_json(out/'manifest.json',dict(**{k:v for k,v in old.items() if k!='files'},files=files,minimum_10000_default_rows=True,
        origin_summary=origin,source_anchor_manifest_sha256=sha(anchors/'manifest.json')))
    print(origin)
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--source',type=Path,required=True);p.add_argument('--anchors',type=Path,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args();combine(a.source,a.anchors,a.output)
