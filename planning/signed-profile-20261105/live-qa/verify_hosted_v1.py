"""Read-only verification of this release's published commits and Pages bytes."""
from pathlib import Path
from urllib.request import Request,urlopen
from urllib.parse import quote
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime,timezone
import argparse,hashlib,json
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[2]
PREP=Path('/home/iska/Documents/LaTeX-projects/GRH-publication-20261105-profile/outputs/publication/20261105-profile/release-preparation-v1')
OUT=ROOT/'outputs/checks/2026-11-05-signed-profile/live-qa'
sha=lambda b:hashlib.sha256(b).hexdigest()
blob=lambda b:hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
p=argparse.ArgumentParser();p.add_argument('--manifest',type=Path,required=True);p.add_argument('--main-receipt',type=Path,required=True);p.add_argument('--pages-receipt',type=Path,required=True);p.add_argument('--main-commit',required=True);p.add_argument('--pages-commit',required=True);a=p.parse_args()
for f in [a.manifest,a.main_receipt,a.pages_receipt]:assert f.resolve().is_relative_to(PREP) and f.is_file()
inputs={str(f):sha(f.read_bytes()) for f in [a.manifest,a.main_receipt,a.pages_receipt]}
manifest=json.loads(a.manifest.read_text());receipts={'main':json.loads(a.main_receipt.read_text()),'pages':json.loads(a.pages_receipt.read_text())}
assert manifest['main']['repository_worktree']=='/home/iska/Documents/LaTeX-projects/GRH-publication-20261105-profile'
for target,expected_commit in [('main',a.main_commit),('pages',a.pages_commit)]:
 r=receipts[target];assert r['published'] is True and r['target']==target and r['commit']==expected_commit and r['commit']!=r['base_commit']
 assert r['base_commit']==manifest[target]['base_commit'] and r['force'] is False
assert 'profile-uniformity.html' in receipts['pages']['changed_paths']
assert 'papers/profile-uniformity-details.tex' in receipts['main']['changed_paths']
run=OUT/('hosted-'+datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ'));run.mkdir(parents=True,exist_ok=False)
for label,f in [('api-manifest',a.manifest),('main-publication',a.main_receipt),('pages-publication',a.pages_receipt)]: (run/(label+'.json')).write_bytes(f.read_bytes())
headers={'User-Agent':'GRH-profile-reviewed-release-verification','Cache-Control':'no-cache','Accept':'application/vnd.github+json'}
def get(url):
 with urlopen(Request(url,headers=headers),timeout=45) as r:return r.status,r.read(),dict(r.headers)
tree_checks=[]
for target in ['main','pages']:
 r=receipts[target]
 try:
  status,data,_=get('https://api.github.com/repos/amelie-iska/GRH-research/git/commits/'+r['commit']);c=json.loads(data);(run/(target+'-public-commit.json')).write_bytes(data)
  assert status==200 and c['sha']==r['commit'] and c['tree']['sha']==r['tree'] and [x['sha'] for x in c['parents']]==[r['base_commit']]
  status,data,_=get('https://api.github.com/repos/amelie-iska/GRH-research/git/trees/'+r['tree']+'?recursive=1');t=json.loads(data);(run/(target+'-public-tree.json')).write_bytes(data)
  assert status==200 and t['sha']==r['tree'] and not t['truncated']
  leaves={x['path']:x for x in t['tree'] if x['type']=='blob'};checks=[]
  for e in manifest[target]['entries']:
   x=leaves.get(e['path']);checks.append({'path':e['path'],'expected_git_blob_sha1':e['git_blob_sha1'],'public_git_blob_sha1':None if x is None else x['sha'],'passed':x is not None and x['sha']==e['git_blob_sha1'] and x['mode']==e['mode'] and x.get('size')==e['bytes']})
  tree_checks.append(dict(target=target,passed=all(x['passed'] for x in checks),commit=r['commit'],tree=r['tree'],checks=checks))
 except Exception as e:tree_checks.append(dict(target=target,passed=False,error=str(e)))
(run/'public-git-tree-checks.json').write_text(json.dumps(tree_checks,indent=2)+'\n')
page_entries={e['path']:e for e in manifest['pages']['entries']};r=receipts['pages'];assert set(r['changed_paths'])==set(r['changed_file_sha256'])
def hosted(name):
 expected=r['changed_file_sha256'][name];entry=page_entries[name];assert entry['sha256']==expected
 url='https://amelie-iska.github.io/GRH-research/'+quote(name,safe='/')+'?release='+r['commit']
 try:
  status,data,h=get(url);s=sha(data);g=blob(data);return dict(path=name,HTTP=status,bytes=len(data),sha256=s,expected_sha256=expected,git_blob_sha1=g,expected_git_blob_sha1=entry['git_blob_sha1'],passed=status==200 and s==expected and g==entry['git_blob_sha1'] and len(data)==entry['bytes'],cache_headers={k:v for k,v in h.items() if k.lower() in ['age','last-modified','etag','cache-control']})
 except Exception as e:return dict(path=name,passed=False,error=str(e))
with ThreadPoolExecutor(max_workers=4) as pool:checks=list(pool.map(hosted,sorted(r['changed_paths'])))
unchanged=all(sha(Path(f).read_bytes())==h for f,h in inputs.items());passed=unchanged and all(t['passed'] for t in tree_checks) and all(c['passed'] for c in checks)
record={'passed':passed,'utc':datetime.now(timezone.utc).isoformat(),'main_commit':a.main_commit,'pages_commit':a.pages_commit,'all_changed_hosted_files':len(checks),'public_git_tree_targets':tree_checks,'hosted_checks':checks,'input_sha256':inputs,'inputs_unchanged':unchanged,'verifier_sha256':sha(Path(__file__).read_bytes()),'scope':'Every changed Pages file exact HTTP bytes/SHA256/Git blob; every selected main/Pages public Git-tree blob and mode/size. No token/auth/write/publication; mathematical claims reviewed separately.'}
f=run/'receipt.json';f.write_text(json.dumps(record,indent=2)+'\n');print(json.dumps({'passed':passed,'receipt':str(f),'receipt_sha256':sha(f.read_bytes()),'changed_hosted_files':len(checks),'errors':[c for c in checks if not c['passed']]}))
if not passed:raise SystemExit(1)
