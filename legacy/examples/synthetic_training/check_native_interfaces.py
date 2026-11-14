"""Read-only native reader checks; never enroll data, fit vocabularies or train."""
import argparse,hashlib,json,sys
from pathlib import Path
sys.dont_write_bytecode=True
import pyarrow.parquet as pq
from common import canonical,write_json

def main():
    p=argparse.ArgumentParser();p.add_argument('--materials',type=Path,required=True);p.add_argument('--bio',type=Path,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args()
    root=Path('/home/iska/Documents/amelie');h=root/'quantum-mat/holonforge';m=root/'bio/Mora-3'
    watched=[h/'src/holonforge/aster/tokenization.py',h/'src/holonforge/aster/data.py',m/'src/mora3/data/schema.py',m/'src/mora3/data/tasks.py',m/'src/mora3/data/array_tasks.py']
    before={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in watched}
    sys.path[:0]=[str(h/'src'),str(m/'src')]
    from holonforge.aster.tokenization import GraphTokenizer,Vocabulary
    from holonforge.aster.data import validate_record
    from mora3.data.schema import GraphRecord,Node,Edge,Measurement
    from mora3.data.provenance import Provenance,LeakageKey
    from mora3.data.tasks import ConditionalTask
    from mora3.data.array_tasks import OrderedArray,ArrayTask
    materials=[r for f in sorted((a.materials/'data').glob('*.parquet')) for r in pq.read_table(f).to_pylist()]
    tok=GraphTokenizer(Vocabulary(size=4096),max_length=32768);cases=[]
    for family in sorted({r['family'] for r in materials}):
        r=next(r for r in materials if r['family']==family);c=json.loads(r['condition_json'])
        def project(r):return dict(hamiltonian=json.loads(r['condition_json']),instruction='Predict the requested effective-model observables from these conditions.',requested_modalities=['observables'])
        native=project(r);assert validate_record(dict(native,id='read-only-check'))['valid']
        encoded=tok.encode(native);mutant=dict(r,target_json='{"poison":123456789}',payload_json='{"hidden_target":987654321}')
        assert tok.encode(project(mutant))['token_ids']==encoded['token_ids']
        cases.append(dict(family=family,tokens=len(encoded['token_ids']),target_poison_invariance=True))
    bio=[r for f in sorted((a.bio/'data').glob('*.parquet')) for r in pq.read_table(f).to_pylist()];checked=0;gated=0;scalar_available=[]
    for r in bio[::max(1,len(bio)//16)]:
        payload=json.loads(r['payload_json']);c=payload['conditions'];t=payload['targets'];nodes=[];roles=[]
        for i,(z,xyz,force) in enumerate(zip(c['atomic_numbers'],c['coordinates_angstrom'],t['forces_kcal_per_mol_angstrom'])):
            measures=[Measurement('atomic_number',z,'dimensionless','predicted',True)]
            measures +=[Measurement('position_'+axis,v,'angstrom','predicted',True) for axis,v in zip('xyz',xyz)]
            measures +=[Measurement('force_'+axis,v,'kcal/(mol angstrom)','predicted',True) for axis,v in zip('xyz',force)]
            nodes.append(Node('chemical_atom',tuple(measures)))
            roles +=[(('node',i,v.name),'target' if v.name.startswith('force_') else 'condition') for v in measures]
        edges=[]
        for b in c['bonds']:
            for s,d in [(b['source'],b['target']),(b['target'],b['source'])]:
                j=len(edges);edges.append(Edge(s,d,'covalent_bond_reciprocal',True,(Measurement('bond_order',b['order'],'dimensionless','predicted',True),)));roles.append((('edge',j,'bond_order'),'condition'))
        digest=hashlib.sha256(r['payload_json'].encode()).hexdigest()
        record=GraphRecord(r['record_id'],tuple(nodes),tuple(edges),(Provenance('GRH complementary simulated conformers','release-v1',r['record_id'],digest,'owner-controlled private research'),),(LeakageKey('grh-complementary-v1-similarity',r['group_id']),))
        task=ConditionalTask(tuple(roles),topology_known=True);inputs=task.input_fields(record)
        assert not any(ref[2].startswith('force_') for ref in inputs)
        assert GraphRecord.from_bytes(record.canonical_bytes())==record
        try:scalar_available.append(len(task.available_targets(record)))
        except ValueError:scalar_available.append('computed_target_rejected')
        xyz=tuple(v for point in c['coordinates_angstrom'] for v in point);force=tuple(v for point in t['forces_kcal_per_mol_angstrom'] for v in point)
        axis=tuple(f'atom{i}:{a}' for i in range(len(c['atomic_numbers'])) for a in 'xyz')
        array=ArrayTask((OrderedArray('coordinates',axis,xyz,'explicit atom order and Cartesian axes','angstrom','source_predicted'),OrderedArray('forces',axis,force,'same explicit atom order and Cartesian axes','kcal/(mol angstrom)','source_predicted')),(('coordinates','condition'),('forces','target')),digest)
        assert set(x['name'] for x in array.input_metadata()['arrays'])=={'coordinates'}
        try:array.project(device='cpu')
        except ValueError:gated+=1
        else:raise AssertionError('Computed targets unexpectedly bypassed observed-only ArrayTask gate')
        checked+=1
    after={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in watched}
    report=dict(passed=True,Aster_condition_only_tokenization=cases,Mora_scalar_graph_checks=checked,Mora_available_computed_scalar_targets=scalar_available,
        Mora_computed_array_target_rejections=gated,source_labels_preserved=True,native_model_admission=False,neural_updates=0,
        no_model_repo_writes_by_this_program=True,inspected_source_hashes_unchanged=(before==after),source_hashes_before=before,source_hashes_after=after,
        boundary='Reader compatibility and target exclusion only; array supervised admission requires owning model policy review. No observed relabel, source enrollment, model or vocabulary changes.')
    write_json(a.output,report);print(json.dumps(report,indent=2))
if __name__=='__main__':main()
