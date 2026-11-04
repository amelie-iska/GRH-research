"""Read-only reachable-history credential check; never echo matched content."""
from pathlib import Path
import subprocess,re,json,argparse
ROOT=Path(__file__).resolve().parents[1]
PATTERNS=[rb'hf_[A-Za-z0-9]{20,}',rb'gh[pousr]_[A-Za-z0-9]{30,}',rb'github_pat_[A-Za-z0-9_]{30,}',rb'-----BEGIN (?:RSA |EC |OPENSSH |DSA |ENCRYPTED )?PRIVATE KEY-----']
def main(output):
    raw=subprocess.check_output(['git','rev-list','--objects','--all'],cwd=ROOT).decode().splitlines()
    names={row.split(' ',1)[0]:(row.split(' ',1)[1] if ' ' in row else '') for row in raw}
    process=subprocess.Popen(['git','cat-file','--batch'],cwd=ROOT,stdin=subprocess.PIPE,stdout=subprocess.PIPE)
    blobs=0;size=0;hits=[]
    for oid in names:
        process.stdin.write((oid+'\n').encode());process.stdin.flush()
        header=process.stdout.readline().decode().strip().split();assert len(header)==3
        data=process.stdout.read(int(header[2]));assert process.stdout.read(1)==b'\n'
        if header[1]!='blob':continue
        blobs+=1;size+=len(data)
        if any(re.search(p,data) for p in PATTERNS):hits.append({'object':oid,'path':names[oid],'content_suppressed':True})
    process.stdin.close();assert process.wait()==0
    staged=subprocess.check_output(['git','diff','--cached','--name-only','-z'],cwd=ROOT).decode().split('\0')
    for name in filter(None,staged):
        data=subprocess.check_output(['git','show',':'+name],cwd=ROOT)
        if any(re.search(p,data) for p in PATTERNS):hits.append({'path':name,'staged':True,'content_suppressed':True})
        assert '.private-credentials' not in name and not name.startswith('outputs/datasets/'), 'Protected payload staged'
    result={'passed':not hits,'reachable_blobs':blobs,'reachable_bytes_scanned':size,'staged_files':len(list(filter(None,staged))),'credential_matches':hits,'scope':'Configured credential patterns over all reachable Git blobs and current index; not an arbitrary private-file publication'}
    output.parent.mkdir(parents=True,exist_ok=True);output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='credential_matches'}));assert not hits,'Credential patterns found; matched contents suppressed'
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output',type=Path,required=True);main(p.parse_args().output)
