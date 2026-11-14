"""Port exact source statements/proofs without promoting them to verified facts.

Only pinned, user-specified public repositories are fetched. Upstream Git blob
hashes and local SHA-256 bind the original documents. Run --download once, then
replay offline against the saved trees/documents. This is not a TeX theorem prover.
"""
from __future__ import annotations
import argparse, hashlib, json, re, urllib.request
from pathlib import Path
from datetime import datetime, timezone

PINS={
 'TropicalGT':'f8ffc7150afdd83bace8078c86fde7c8eeb0e08e',
 'ToricGT':'a5199bc989a6fb170e21220e5e87bf95bc2fc0b4',
 'ToricGT-Program':'f91ba1811b5a4f70d53c7120acf8ca2a0049f85b',
 'Mora-3':'75ac2d696f42da0a673fc43a20d84686a2ceed40',
 'Tropical_Quivers_of_Archs':'2b6ab79a685e2c6233fb8892e59589951feeddad',
}
MAX_BYTES=2_000_000


def sha(data:bytes)->str:return hashlib.sha256(data).hexdigest()
def git_blob(data:bytes)->str:return hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
def dump(path:Path,value)->None:
 path.parent.mkdir(parents=True,exist_ok=True)
 path.write_text(json.dumps(value,indent=2,ensure_ascii=False,allow_nan=False)+'\n')


def uncomment(text:str)->str:
 """Blank TeX line comments, preserving offsets; escaped percent stays literal."""
 out=list(text)
 for match in re.finditer('%',text):
  i=match.start();j=i-1
  while j>=0 and text[j]=='\\':j-=1
  if (i-1-j)%2:continue
  end=text.find('\n',i)
  if end<0:end=len(text)
  out[i:end]=' '*(end-i)
 return ''.join(out)


def extract(text:str)->list[dict]:
 code=uncomment(text)
 aliases={'theorem','lemma','proposition','corollary','claim','thm','lem','prop','cor'}
 # Preserve custom theorem environments; assumptions/definitions are separate data.
 for a,label in re.findall(r'\\newtheorem\*?\{([^}]+)\}(?:\[[^]]*\])?\{([^}]+)\}',code):
  if re.search(r'theorem|lemma|proposition|corollary|claim',label,re.I):aliases.add(a)
 pat=re.compile(r'\\begin\{('+ '|'.join(re.escape(a)for a in sorted(aliases))+r')\}(?:\[([^\n]*?)\])?')
 begins=list(pat.finditer(code));records=[]
 for ix,m in enumerate(begins):
  env=m[1];endmark='\\end{'+env+'}';end=code.find(endmark,m.end())
  if end<0:raise ValueError('Unclosed theorem environment '+env)
  end+=len(endmark);next_start=begins[ix+1].start()if ix+1<len(begins)else len(code)
  pm=re.search(r'\\begin\{proof\}(?:\[[^\n]*?\])?',code[end:next_start])
  proof=None;proof_start=None;proof_end=None
  if pm:
   proof_start=end+pm.start();proof_end=code.find('\\end{proof}',end+pm.end())
   if proof_end<0:raise ValueError('Unclosed proof')
   proof_end+=len('\\end{proof}');proof=text[proof_start:proof_end]
  statement=text[m.start():end]
  labels=re.findall(r'\\label\{([^}]+)\}',code[m.start():end])
  records.append({'kind':env,'title':m[2]or '', 'labels':labels,
   'statement_lines':[text.count('\n',0,m.start())+1,text.count('\n',0,end)+1],
   'proof_lines':None if proof is None else [text.count('\n',0,proof_start)+1,text.count('\n',0,proof_end)+1],
   'statement_latex':statement,'proof_latex':proof,
   'statement_sha256':sha(statement.encode()),'proof_sha256':None if proof is None else sha(proof.encode()),
   'status':'source_port_only','proof_attachment':'following proof before next named claim'if proof else 'no adjacent proof located',
   'limitations':'Extraction preserves text; citations, omitted proofs and mathematical validity need separate review.'})
 return records


def selected(repo:str,path:str)->bool:
 return path.endswith('.tex') or (repo=='Mora-3' and path.startswith('paper/') and path.endswith('.md'))


def fetch(url:str)->bytes:
 req=urllib.request.Request(url,headers={'User-Agent':'GRH-research source-proof audit'})
 with urllib.request.urlopen(req,timeout=45)as r:data=r.read(MAX_BYTES+1)
 if len(data)>MAX_BYTES:raise ValueError('Source exceeds bound')
 return data


def inventory(root:Path,out:Path,download:bool=False)->dict:
 out.mkdir(parents=True,exist_ok=True);docs=[];claims=[]
 for repo,pin in PINS.items():
  base=root/repo;base.mkdir(parents=True,exist_ok=True);treefile=base/'tree.json'
  if download:treefile.write_bytes(fetch(f'https://api.github.com/repos/amelie-iska/{repo}/git/trees/{pin}?recursive=1'))
  tree=json.loads(treefile.read_text())
  if tree.get('sha')!=pin or tree.get('truncated'):raise ValueError('Unpinned or incomplete tree: '+repo)
  for item in tree['tree']:
   path=item['path']
   if item['type']!='blob' or not selected(repo,path):continue
   dest=(base/path).resolve()
   if not dest.is_relative_to(base.resolve()):raise ValueError('Unsafe source path')
   if download:
    dest.parent.mkdir(parents=True,exist_ok=True)
    dest.write_bytes(fetch(f'https://raw.githubusercontent.com/amelie-iska/{repo}/{pin}/{path}'))
   data=dest.read_bytes()
   if git_blob(data)!=item['sha']:raise ValueError('Git blob mismatch: '+path)
   text=data.decode('utf8');entries=extract(text)if path.endswith('.tex')else []
   identity={'repository':repo,'commit':pin,'path':path,'git_blob':item['sha'],'sha256':sha(data),
    'url':f'https://github.com/amelie-iska/{repo}/blob/{pin}/{path}'}
   docs.append(dict(identity,bytes=len(data),claim_count=len(entries),full_text_preserved=True))
   # Original research sources are separate from the audited/repaired exposition.
   target=out/'originals'/repo/path;target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(data)
   for j,c in enumerate(entries):claims.append(dict(identity,ordinal=j+1,**c))
 with (out/'claims.jsonl').open('w')as f:
  for c in claims:f.write(json.dumps(c,ensure_ascii=False)+'\n')
 report={'schema':'grh.source-proof-port.v1','created_at_utc':datetime.now(timezone.utc).isoformat(),
  'documents':docs,'document_count':len(docs),'claim_occurrences':len(claims),
  'unique_statement_hashes':len({c['statement_sha256']for c in claims}),
  'adjacent_proof_occurrences':sum(c['proof_latex']is not None for c in claims),
  'claims_sha256':sha((out/'claims.jsonl').read_bytes()),
  'not_accessible':[{'repository':'amelie-iska/TropicalGT-Program','status':'404 from public API and selected connector on 2026-11-14','replacement_assumed':False}],
  'coverage':'Every .tex in the five pinned accessible trees plus every Mora-3 paper/*.md. PDF-only external references are not claimed ported or fully reviewed.',
  'validation':'Git blob and SHA-256 source integrity. Mathematical and Lean review is per-claim, never inferred from extraction.'}
 dump(out/'manifest.json',report);return report

if __name__=='__main__':
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--snapshots',type=Path,required=True);p.add_argument('--output',type=Path,required=True);p.add_argument('--download',action='store_true');a=p.parse_args()
 r=inventory(a.snapshots,a.output,a.download);print(json.dumps({k:v for k,v in r.items()if k!='documents'},indent=2))
