"""Compare the actual raw and prepared mathematical trees, excluding outer tails."""
from pathlib import Path
import re,html,copy,json,hashlib,xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[3]
s=(ROOT/'outputs/html-work/main.html').read_text()
s=re.sub(r'(<img\b.*?\balt=")(.*?)("\s*/>)',lambda m:m[1]+html.escape(html.unescape(m[2]),quote=True)+m[3],s,flags=re.S)
a=ET.fromstring(s);b=ET.fromstring((ROOT/'web/book/main.html').read_text())
def signatures(tree,tag):
 out=[]
 for e in tree.iter(tag):
  e=copy.deepcopy(e);e.tail=None
  out.append(hashlib.sha256(ET.tostring(e)).hexdigest())
 return out
mtag=next(e.tag for e in a.iter() if e.tag.endswith('}math') or e.tag=='math')
assert signatures(a,'table')==signatures(b,'table')
assert signatures(a,mtag)==signatures(b,mtag)
wrappers=[e for e in b.iter() if e.attrib.get('class')=='reader-table-scroll']
assert all(len(e)==1 and e[0].tag=='table' for e in wrappers)
r=dict(passed=True,tables=len(signatures(a,'table')),native_mathml=len(signatures(a,mtag)),table_subtrees_unchanged=True,all_mathml_subtrees_unchanged=True,wrappers=len(wrappers),scope='Original native MathML and mathematical table trees unchanged, ignoring outer tails relocated after scroll wrappers. Viewport separately browser checked.')
(ROOT/'outputs/checks/2026-11-03-hecke-type-i/math-preservation.json').write_text(json.dumps(r,indent=2)+'\n');print(r)
