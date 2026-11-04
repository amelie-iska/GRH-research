"""Read a verified private release with its pinned commit and official loader."""
import argparse,json,os,re,faulthandler
from pathlib import Path

def main():
    p=argparse.ArgumentParser();p.add_argument('--receipt',type=Path,required=True);p.add_argument('--dataset',type=Path,required=True);p.add_argument('--credential-copy',type=Path,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args()
    assert '.private-credentials' in a.credential_copy.parts
    tokens=set(re.findall(r'hf_[A-Za-z0-9]{20,}',a.credential_copy.read_text()));assert len(tokens)==1;token=tokens.pop()
    os.environ['HF_HUB_DISABLE_IMPLICIT_TOKEN']='1';os.environ['HF_HUB_DISABLE_TELEMETRY']='1'
    # Match the successful standard-HTTP release path; local process setting only.
    os.environ['HF_HUB_DISABLE_XET']='1'
    os.environ['HF_HOME']=str(a.credential_copy.parent/'hf-home')
    from datasets import load_dataset
    receipt=json.loads(a.receipt.read_text());assert receipt['passed'] and receipt['private']
    quality=json.loads((a.dataset/'release-quality.json').read_text());results={}
    for directory,counts in quality['config_split_rows'].items():
        config='default' if directory=='data' else directory
        print(json.dumps(dict(stage='load_configuration',configuration=config)),flush=True)
        # No locals, arguments, tokens or headers in these bounded diagnostic stacks.
        faulthandler.dump_traceback_later(90,repeat=False)
        data=load_dataset(receipt['repo_id'],config,revision=receipt['commit'],token=token,cache_dir=str(a.dataset.parent/'hf-verified-loader-cache'))
        faulthandler.cancel_dump_traceback_later()
        actual={s:len(v) for s,v in data.items()};assert actual==counts,(config,actual,counts)
        for split,table in data.items():
            assert 'origin_class' in table.column_names and 'planned_source_dataset' in table.column_names
            row=table[0];assert row['split']==split and row['origin_class']
        results[config]=actual
    report=dict(passed=True,repo_id=receipt['repo_id'],commit=receipt['commit'],official_datasets_loader=True,all_config_rows=results,origin_columns_every_configuration=True)
    a.output.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
if __name__=='__main__':
    try:main()
    except Exception as exc:
        print(json.dumps(dict(passed=False,error_type=type(exc).__name__)));raise SystemExit(1)
