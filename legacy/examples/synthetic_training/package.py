"""HF-native typed Parquet packaging of a frozen, curated supplementary corpus."""
import argparse,json,shutil
from pathlib import Path
import pyarrow as pa
import pyarrow.parquet as pq
from common import fresh,sha,write_json

def package(source,out):
    source=Path(source);out=fresh(out);m=json.loads((source/'manifest.json').read_text())
    for name,entry in m['files'].items():assert sha(source/name)==entry['sha256']
    rows=[r for p in sorted((source/'data').glob('*.parquet')) for r in pq.read_table(p).to_pylist()]
    bio='atomic_numbers' in json.loads(rows[0]['condition_json']);vec=pa.list_(pa.float64());matrix=pa.list_(vec)
    base=[(k,pa.string()) for k in rows[0]]+[(k,pa.string()) for k in ['origin_class','planned_source_dataset','planned_source_record_id','label_origin']]
    if bio:
        extra=[('condition_atomic_numbers',pa.list_(pa.int16())),('condition_bond_sources',pa.list_(pa.int32())),
            ('condition_bond_targets',pa.list_(pa.int32())),('condition_bond_orders',vec),('condition_coordinates_angstrom',matrix),
            ('target_forces_kcal_mol_angstrom',matrix),('target_energy_kcal_mol',pa.float64()),('target_partial_charges_e',vec),
            ('target_VR_H0_angstrom',matrix),('target_VR_H1_angstrom',matrix),('target_reference_coordinates_angstrom',matrix),
            ('evaluation_canonical_smiles',pa.string()),('evaluation_reference_energy_kcal_mol',pa.float64())]
    else:
        extra=[('condition_parameter_names',pa.list_(pa.string())),('condition_parameter_values',vec),('condition_intervention',pa.string()),
            ('target_open_spectrum',vec),('target_edge_weights',vec),('target_bulk_axis',vec),('target_bulk_bands',matrix),
            ('target_effective_action',vec),('target_retained_probability',vec),('target_invariant',pa.int32()),
            ('target_invariant_kind',pa.string()),('target_gap',pa.float64()),('evaluation_hamiltonian_real',matrix),('evaluation_hamiltonian_imag',matrix)]
    schema=pa.schema(base+extra,metadata={b'role_contract':b'condition_* only as forward inputs; target_* supervision; evaluation_* excluded. JSON payload/IDs/provenance are not automatic model inputs.',b'schema':b'grh-complementary-physics-hf-v1'})
    enriched=[]
    for r in rows:
        r=dict(r);p=json.loads(r['payload_json']);c=p['conditions'];t=p['targets']
        r.update(origin_class='new_simulation',planned_source_dataset=None,planned_source_record_id=None,
            label_origin='new_computed_physics; novelty of chemical identity against pre-existing corpora not asserted')
        if bio:
            r.update(condition_atomic_numbers=c['atomic_numbers'],condition_bond_sources=[b['source'] for b in c['bonds']],
                condition_bond_targets=[b['target'] for b in c['bonds']],condition_bond_orders=[b['order'] for b in c['bonds']],
                condition_coordinates_angstrom=c['coordinates_angstrom'],target_forces_kcal_mol_angstrom=t['forces_kcal_per_mol_angstrom'],
                target_energy_kcal_mol=t['energy_kcal_per_mol'],target_partial_charges_e=t['forcefield_partial_charges_e'],
                target_VR_H0_angstrom=t['heavy_atom_VR']['H0'],target_VR_H1_angstrom=t['heavy_atom_VR']['H1'],
                target_reference_coordinates_angstrom=p['inverse_task']['targets']['reference_coordinates_angstrom'],
                evaluation_canonical_smiles=p['canonical_smiles'],evaluation_reference_energy_kcal_mol=p['reference_energy_kcal_per_mol'])
        else:
            top=t['topology'];kind=next((k for k in ['chern','winding','z2','surface_genus'] if k in top),None);curve=t['bulk_curve']
            r.update(condition_parameter_names=list(c['parameters']),condition_parameter_values=[float(v) for v in c['parameters'].values()],
                condition_intervention=c['intervention'],target_open_spectrum=t.get('open_spectrum'),target_edge_weights=t.get('edge_weight'),
                target_bulk_axis=curve.get('axis'),target_bulk_bands=curve.get('bands'),target_effective_action=curve.get('effective_action'),
                target_retained_probability=curve.get('retained_probability'),target_invariant=top.get(kind),target_invariant_kind=kind,
                target_gap=top.get('gap'),evaluation_hamiltonian_real=p.get('hamiltonian_real'),evaluation_hamiltonian_imag=p.get('hamiltonian_imag'))
        enriched.append(r)
    (out/'data').mkdir()
    for split in ['train','validation','test']:
        subset=[r for r in enriched if r['split']==split];table=pa.Table.from_pylist(subset,schema=schema)
        target=out/'data'/f'{split}-00000-of-00001.parquet';pq.write_table(table,target,compression='zstd',version='2.6')
        assert pq.read_table(target).to_pylist()==subset
    for name in ['quality.json','split-audit.json','failures.json','examples.json']:
        if (source/name).exists():shutil.copyfile(source/name,out/name)
    for name in ['generation_source','parent_generation_source']:
        if (source/name).exists():shutil.copytree(source/name,out/name)
    write_json(out/'curation-manifest.json',m)
    summary=json.loads((out/'quality.json').read_text());audit=json.loads((out/'split-audit.json').read_text())
    title='Mora Complementary Conformer Response' if bio else 'Aster Complementary Topological Response'
    purpose=('Atom/bond graphs, explicit-H coordinates, MMFF94 energies/forces/charges, recorded-reference denoising pairs and complete heavy-atom VR H0/H1.' if bio else 'SSH, Kitaev, QWZ, Rice–Mele pumps, Harper photonic strips and genus1/2/4 clean-dessin classical RG; bulk/open-boundary/gauge/defect response pairs.')
    limitation=('MMFF94 is an empirical molecular-mechanics method, not ab-initio or experimental biology. No affinity, ADMET, catalyst, therapeutic or clinical labels. Neutral/formal-charge graph states do not infer physiological protonation. Optimization convergence is not a proof of a unique/global minimum. Absolute MMFF energies are not cross-molecule atomization energies. Geometric persistence is a finite distance-filtration descriptor, not an electronic phase invariant.' if bio else 'Dimensionless effective models, not generated validated crystals or synthesized quantum matter. Bulk invariant and finite boundary response are distinct. Bulk curves are ky=0; open strips are ky=.37. Mesh consistency and analytic/gap guards are numerical evidence, not interval-certified topology for every model. Dessin genus is not a quantum phase index. No GRH theorem or quantum advantage follows.')
    native=('Mora-3 scalar graphs can retain predicted/computed status. Its current ArrayTask rejects source_predicted targets for supervised projection. This is an explicit future admission-policy boundary; no label was changed to observed to bypass it.' if bio else 'Aster has nonchemical node and Hamiltonian/observable tracks. Tokenizer readability is not production corpus admission, scalar normalization or a trained capability.')
    card=f'''---
pretty_name: {title}
language: en
license: other
task_categories:
- other
tags:
- synthetic
- physics
- parquet
- complementary-dataset
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*.parquet
  - split: validation
    path: data/validation-*.parquet
  - split: test
    path: data/test-*.parquet
---
# {title}

## Additional complementary scope
{purpose}
This is an ADDITIONAL independent auxiliary corpus. It replaces no existing
training data, model, vocabulary or split. Both active model projects were
inspected read-only; no enrollment or neural optimizer update occurred.

## Data, format and intended tasks
{summary['records']} computed records; split counts: {summary['split_counts']}.
Three Zstandard-compressed typed Parquet shards include native scalar/list/matrix
columns. `condition_*` fields are forward inputs, `target_*` are supervision,
and `evaluation_*` are excluded. The three JSON columns preserve the complete
lossless schema and task/provenance details; do not feed complete payloads or
record/group IDs into a model as a shortcut. Inverse tasks need an explicit
role swap and desired-condition contract, never hidden target access.

```python
from datasets import load_dataset
from huggingface_hub import dataset_info
# Authenticate separately through your approved private-repository access.
revision = dataset_info("REPO_ID").sha
data = load_dataset("REPO_ID", revision=revision)
print(data["train"].column_names)
```

## Generation and evidence
Seed20261104; Python{summary['python']}; NumPy{summary['numpy']}.
Exact source snapshots, parameter/units/evidence fields, `quality.json`,
`split-audit.json`, retained failure records where applicable, and SHA256
manifests accompany the shards. Deterministic simulations are independent of
the target neural models. Refer to validation and native-interface receipts
in the GRH project for actual checks and limitations.

## Splits and leakage
{audit.get('policy',audit.get('final_component_allocation',{}).get('policy','Whole similarity components'))}.
All parent/conformer/gauge/intervention and task descendants remain together.
{'Morgan radius2/2048bit Tanimoto>=.65, same nonempty Murcko scaffold and stereo-agnostic constitution form chemical components. A second all-conformer geometric closure joins identical heavy-element multisets at sorted pair-distance RMS<=.10angstrom.' if bio else 'Same-family/discrete-size parameter proximity and relative finite-spectrum proximity form transitive components; thresholds and conservative SSH hopping-swap/Kitaev mu-sign folding are explicit in the audit.'}
Actual component-level family/topology (or size/VR) strata inform allocation.
Indivisible large components and rare strata prevent exact80/10/10 or complete
class coverage; distributions and cross-split nearest witnesses are reported.
These finite metric audits cannot prove all possible statistical independence
or prevent overfitting. Protein RMSD/TM-score or sequence-homology claims are
not made for these small-molecule/effective-model corpora.

## Limitations and native-model boundary
{limitation}
{native}
Use as a method-labelled auxiliary/pretraining/fine-tuning source only after
the owning model's explicit source contract, normalization, task/mask and
evaluation review. No learned quality improvement has been measured.

## Rights and privacy
Owner-controlled synthetic research release, stored privately. No public
redistribution license has been selected. No private model weights, existing
training data or credentials are included. Upstream software terms remain
separate from these computed outputs.

## References
- Fukui–Hatsugai–Suzuki, arXiv:cond-mat/0503172v2.
- RDKit MMFF94 and ETKDG documentation: https://www.rdkit.org/docs/
- Reproduction and contextual examples: GRH-research/examples/synthetic_training.
'''
    (out/'README.md').write_text(card)
    files={str(p.relative_to(out)):{'sha256':sha(p),'bytes':p.stat().st_size} for p in sorted(out.rglob('*')) if p.is_file() and p.name!='README.md'}
    write_json(out/'manifest.json',dict(schema='grh-complementary-physics-hf-v1',description=purpose,files=files,
        packaging_source_sha256=sha(__file__),curation_manifest_sha256=sha(source/'manifest.json'),typed_columns=[f.name for f in schema],
        source_code_sha256=m['source_code_sha256'],private_release=True,additional_complementary=True,native_model_admission=False))
    print(dict(output=str(out),rows=len(rows),typed_columns=len(schema)))
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--source',required=True,type=Path);p.add_argument('--output',required=True,type=Path);a=p.parse_args();package(a.source,a.output)
