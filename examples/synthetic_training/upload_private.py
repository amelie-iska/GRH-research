"""Explicit private HF release; authorized credential copy never enters artifacts.

Use only after reviewing dataset files/cards and passing validation. No login,
global credential store, destructive operation or implicit whole-folder upload.
"""
import argparse,hashlib,json,os,re,shutil,sys
from pathlib import Path
STAGE='arguments'

def main():
    global STAGE
    p=argparse.ArgumentParser();p.add_argument('--dataset',required=True,type=Path);p.add_argument('--slug',required=True)
    p.add_argument('--credential-source',required=True,type=Path);p.add_argument('--credential-copy',required=True,type=Path)
    p.add_argument('--receipt',required=True,type=Path);p.add_argument('--credential-check-only',action='store_true')
    p.add_argument('--http-transfer',action='store_true');p.add_argument('--resume-empty-repository',action='store_true');a=p.parse_args()
    authorized=Path('/home/iska/Documents/amelie/quantum-mat/holonforge/keys.txt')
    if a.credential_source!=authorized:raise ValueError('Only the exact user-authorized credential source is supported')
    if '.private-credentials' not in a.credential_copy.parts:raise ValueError('Protected ignored credential-copy directory required')
    import subprocess
    root=Path(__file__).resolve().parents[2]
    subprocess.run(['git','check-ignore','-q',str(a.credential_copy)],cwd=root,check=True)
    a.credential_copy.parent.mkdir(parents=True,exist_ok=True);os.chmod(a.credential_copy.parent,0o700)
    if not a.credential_copy.exists():
        fd=os.open(a.credential_copy,os.O_WRONLY|os.O_CREAT|os.O_EXCL,0o600)
        with os.fdopen(fd,'wb') as out,authorized.open('rb') as source:shutil.copyfileobj(source,out)
    os.chmod(a.credential_copy,0o600)
    tokens=set(re.findall(r'hf_[A-Za-z0-9]{20,}',a.credential_copy.read_text()))
    if len(tokens)!=1:raise ValueError('Credential copy does not contain one unambiguous Hugging Face token; no credential was displayed')
    token=tokens.pop()
    os.environ['HF_HOME']=str(a.credential_copy.parent/'hf-home');os.environ['HF_HUB_DISABLE_IMPLICIT_TOKEN']='1';os.environ['HF_HUB_DISABLE_TELEMETRY']='1'
    if a.http_transfer:os.environ['HF_HUB_DISABLE_XET']='1'
    from huggingface_hub import HfApi,CommitOperationAdd
    api=HfApi(endpoint='https://huggingface.co',token=token)
    STAGE='identity';identity=api.whoami();owner=identity['name'];repo=owner+'/'+a.slug
    if a.credential_check_only:
        print(json.dumps(dict(account=owner,role=identity.get('auth',{}).get('accessToken',{}).get('role'),credential_copy_protected=True,no_repository_created=True)));return
    STAGE='manifest_scan';card=a.dataset/'README.md'
    card.write_text(card.read_text().replace('REPO_ID',repo))
    manifest=json.loads((a.dataset/'manifest.json').read_text());files=list(manifest['files'])+['manifest.json','README.md']
    assert (a.dataset/'README.md').is_file()
    for name in files:
        path=a.dataset/name
        STAGE='member_safety:'+name
        if not path.is_file() or path.is_symlink() or '..' in Path(name).parts:raise ValueError('Unsafe upload member')
        content=path.read_bytes()
        STAGE='credential_pattern_scan:'+name
        if re.search(rb'hf_[A-Za-z0-9]{20,}|gh[pousr]_[A-Za-z0-9]{30,}|-----BEGIN (?:RSA |EC |OPENSSH |DSA |ENCRYPTED )?PRIVATE KEY-----',content):raise ValueError('Credential pattern in upload member')
        STAGE='member_hash:'+name
        if name in manifest['files']:assert hashlib.sha256(content).hexdigest()==manifest['files'][name]['sha256']
    # Refuse existing repository collisions; no unrelated data is overwritten.
    STAGE='create_private_repo'
    if a.resume_empty_repository:
        existing=api.repo_info(repo,repo_type='dataset',files_metadata=True)
        assert existing.private is True
        assert {s.rfilename for s in existing.siblings}<={'.gitattributes'},'Refuse any existing data overwrite'
    else:api.create_repo(repo_id=repo,repo_type='dataset',private=True,exist_ok=False)
    assert api.repo_info(repo,repo_type='dataset').private is True
    STAGE='commit_reviewed_files';commit=api.create_commit(repo_id=repo,repo_type='dataset',operations=[CommitOperationAdd(path_in_repo=name,path_or_fileobj=str(a.dataset/name)) for name in files],commit_message='Add reviewed complementary synthetic physics dataset with Parquet splits')
    STAGE='verify_remote_files'
    info=api.repo_info(repo,repo_type='dataset',revision=commit.oid,files_metadata=True)
    assert info.private is True and info.sha==commit.oid
    remote={s.rfilename:s for s in info.siblings}
    for name in files:assert name in remote and remote[name].size==(a.dataset/name).stat().st_size
    # Verify exact remote Git blob hashes for ordinary files and SHA256 for LFS.
    for name in files:
        s=remote[name];content=(a.dataset/name).read_bytes()
        if s.lfs:assert s.lfs.sha256==hashlib.sha256(content).hexdigest()
        else:assert s.blob_id==hashlib.sha1(b'blob '+str(len(content)).encode()+b'\0'+content).hexdigest()
    receipt=dict(passed=True,private=True,repo_id=repo,url='https://huggingface.co/datasets/'+repo,commit=commit.oid,
        files_verified=len(files),parquet_files=[x for x in files if x.endswith('.parquet')],manifest_sha256=hashlib.sha256((a.dataset/'manifest.json').read_bytes()).hexdigest(),
        credential_handling='Exact authorized source copied to ignored0700/0600 path; never logged, committed or uploaded; explicit file allowlist')
    a.receipt.parent.mkdir(parents=True,exist_ok=True);a.receipt.write_text(json.dumps(receipt,indent=2)+'\n');print(json.dumps(receipt,indent=2))
if __name__=='__main__':
    try:main()
    except Exception as exc:
        # API exception representations may include headers or credential-bearing context.
        print(json.dumps(dict(passed=False,stage=STAGE,error_type=type(exc).__name__,status_code=getattr(getattr(exc,'response',None),'status_code',None))),file=sys.stderr)
        raise SystemExit(1)
