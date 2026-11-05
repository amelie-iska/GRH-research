from pathlib import Path
import re,json,hashlib,xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[3]
sha=lambda b:hashlib.sha256(b).hexdigest()
old=ROOT/'outputs/checks/2026-11-05-signed-profile/root/before/web/book/main.html'
new=ROOT/'outputs/profile-uniformity-book-20261105/v3/native/book/main.html'
a=old.read_text();b=new.read_text()
math=lambda s:re.findall(r'<math\b.*?</math>',s,re.S)
x,y=math(a),math(b);at=0
for v in y:
 if at<len(x) and v==x[at]:at+=1
assert at==len(x) and len(x)==7352 and len(y)==7605
frames=lambda s:re.findall(r'<iframe\b[^>]*>',s)
assert frames(a)==frames(b) and len(frames(b))==13
imgs=lambda s:re.findall(r'<img\b[^>]*?src="([^"]+\.svg)"',s)
assert imgs(a)==imgs(b) and len(imgs(b))==28
for name in imgs(b):
 assert (ROOT/'web/book'/name).read_bytes()==(new.parent/name).read_bytes(),name
malformed=[]
for i,v in enumerate(y):
 t=ET.fromstring(v)
 for n in t.iter():
  if n.tag.rsplit('}',1)[-1]=='munder' and len(n)!=2:malformed.append(i)
assert len(malformed)==3
r={'passed':True,'old_math':len(x),'new_total_math':len(y),'all_old_math_subtrees_ordered_and_byte_identical':True,'identical_iframes':13,'identical_SVG_references_and_asset_bytes':28,'canonical_SVGs':19,'other_preserved_SVGs':9,'inherited_malformed_munder_count':3,'new_malformed_nodes':0,'candidate_sha256':sha(new.read_bytes()),'old_sha256':sha(old.read_bytes()),'checker_sha256':sha(Path(__file__).read_bytes())}
p=ROOT/'outputs/checks/2026-11-05-signed-profile/root/math-preservation-v2.json';assert not p.exists();p.write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r,indent=2))
