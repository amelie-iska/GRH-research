"""User-authorized public visibility for exactly two reviewed project releases.

Preserves immutable data; only a new dataset-card commit and visibility change.
Uses the already-authorized protected credential copy, never a global login.
"""
from pathlib import Path
import argparse,json,re,os,hashlib
REPOS={'aster':('AmelieSchreiber/GRH-Aster-TopoResponse-20261104','2b8ce36571298a3517b8c88bb23269341d9b8908'),
       'mora':('AmelieSchreiber/GRH-Mora-ConformerResponse-20261104','53a6b66acaa69ef79584648f3f6dc068363c4837')}
def main(root):
    protected=root/'.private-credentials/authorized-upload-keys.txt'
    assert protected.is_file() and protected.stat().st_mode&0o077==0
    tokens=set(re.findall(r'hf_[A-Za-z0-9]{20,}',protected.read_text()));assert len(tokens)==1
    os.environ['HF_HUB_DISABLE_IMPLICIT_TOKEN']='1';os.environ['HF_HUB_DISABLE_TELEMETRY']='1'
    from huggingface_hub import HfApi,CommitOperationAdd
    api=HfApi(token=tokens.pop());assert api.whoami()['name']=='AmelieSchreiber'
    out=root/'outputs/publication/2026-11-04';out.mkdir(parents=True,exist_ok=True);receipts=[]
    for model,(repo,frozen) in REPOS.items():
        old=json.loads((root/f'outputs/checks/2026-11-04-synthetic-training/{model}-hf-release.json').read_text())
        assert old['repo_id']==repo and old['commit']==frozen and old['passed']
        before=api.repo_info(repo,repo_type='dataset',files_metadata=True);assert before.sha==frozen,'Unexpected external dataset revision; refuse overwrite'
        card=out/f'{model}-PUBLIC-README.md';assert card.is_file()
        assert not re.search(r'hf_[A-Za-z0-9]{20,}|gh[pousr]_[A-Za-z0-9]{30,}',card.read_text())
        commit=api.create_commit(repo,repo_type='dataset',parent_commit=frozen,operations=[CommitOperationAdd(path_in_repo='README.md',path_or_fileobj=card)],commit_message='Publish reviewed complementary dataset card at owner request')
        after=api.repo_info(repo,repo_type='dataset',revision=commit.oid,files_metadata=True)
        b={s.rfilename:s for s in before.siblings};a={s.rfilename:s for s in after.siblings};assert set(a)==set(b)
        for name in b:
            if name!='README.md':assert a[name].blob_id==b[name].blob_id and a[name].size==b[name].size and a[name].lfs==b[name].lfs
        api.update_repo_settings(repo,repo_type='dataset',private=False)
        final=api.repo_info(repo,repo_type='dataset');assert final.private is False and final.sha==commit.oid
        receipt=dict(passed=True,repo_id=repo,url='https://huggingface.co/datasets/'+repo,private=False,frozen_data_commit=frozen,published_card_commit=commit.oid,data_files_unchanged=True,card_sha256=hashlib.sha256(card.read_bytes()).hexdigest())
        receipts.append(receipt);(out/f'{model}-public-receipt.json').write_text(json.dumps(receipt,indent=2)+'\n');print(json.dumps(receipt),flush=True)
    (out/'datasets-publication.json').write_text(json.dumps(receipts,indent=2)+'\n')
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--root',type=Path,required=True)
    try:main(p.parse_args().root)
    except Exception as e:print(json.dumps({'failed':type(e).__name__,'detail_suppressed_to_protect_credentials':True}));raise SystemExit(1)
