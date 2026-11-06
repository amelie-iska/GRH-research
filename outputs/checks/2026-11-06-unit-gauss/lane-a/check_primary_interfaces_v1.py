#!/usr/bin/env python3
"""Author source/interface controls; not a mathematical proof checker."""
from pathlib import Path
from fractions import Fraction
import hashlib, json, datetime
ROOT=Path(__file__).resolve().parents[4]
P=ROOT/'planning/unit-gauss-20261106/lane-a'
O=Path(__file__).resolve().parent
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
specs=[
 ('planning/unit-gauss-20261106/lane-a/primary-private/dunn-radziwill-2109.07463v3.pdf','df888f8527b3647a3428d6677a3e3070aab7439f79f737f3e894218fb64cfef0'),
 ('planning/unit-gauss-20261106/lane-a/primary-private/dunn-radziwill-2109.07463v3.txt','636da1119ebebdcab6756e9258554af06a42d67baf0c47026c73e960de2f4767'),
 ('planning/unit-gauss-20261106/lane-a/primary-private/openai-first-moment-4eaee8754825.pdf','0af3e675f8a6a5b3e47da9ea5ca7434a825f48f7186f79594b1ee5d54d443a37'),
 ('planning/unit-gauss-20261106/lane-a/primary-private/openai-first-moment-4eaee8754825.txt','4c231b89ade86e737a56874ebb025e983dc509fa66818d62ab64e1817321ac80'),
 ('planning/unit-gauss-20261106/lane-a/primary-private/yoshimoto-1987-vor.pdf','acdf6f3e72aac6054394dd613afab6c5d04740a8b67766a77fc94c731d3bf14f'),
 ('planning/unit-gauss-20261106/lane-a/primary-private/yoshimoto-1987-vor.txt','32f1429d7471c5d6d19bce669fdfe26fffe456b3f8a0fbabacadd6df57196b0d'),
 ('planning/prime-fibre-20261105/lane-b/primary/dunn-metaplectic-v5.pdf','12d75260bde7b5dff9b1b198b0d30eefaf34323e7e8594580bf7719bcf8f8701'),
 ('planning/prime-fibre-20261105/lane-b/primary/dunn-metaplectic-v5.txt','f9fd9ac6bea7427999bd052b1a46d4e70314ccc8221283c8bf1294fdcda018af'),
 ('planning/gauss-release-20261106/lane-a/TYPE_I_FREQUENCY_AND_DELETION_TRANSFER-v2.md','77660bde6a635d5de376e384f7570cee78a0f5dd981e01660ae22a948cbba48b'),
 ('planning/root-moment-20261106/lane-a/ALL_COMPONENT_COLUMN_PHASES-v1.md','011b68a07eda5489b6ea8d8b7fa565e52920423f0c954ef583ea143b64609df8'),
 ('planning/gauss-release-20261106/postpublication/lane-b/PAIRED_LONG_TYPE_I_AND_SHORT_FREQUENCIES-v2.md','99fe6c5a4aa85523bf239527747a33f2436e910a1882a44a8b5e57730d7ad340'),
]
checks=[]
for n,h in specs:
 got=sha(ROOT/n)
 assert got==h,(n,got,h)
 checks.append({'kind':'sha256','path':n,'sha256':got,'pass':True})
dr=(P/'primary-private/dunn-radziwill-2109.07463v3.txt').read_text()
oa=(P/'primary-private/openai-first-moment-4eaee8754825.txt').read_text()
yo=(P/'primary-private/yoshimoto-1987-vor.txt').read_text()
du=(ROOT/'planning/prime-fibre-20261105/lane-b/primary/dunn-metaplectic-v5.txt').read_text()
for name,body,tokens in [
 ('DR genuine primary interfaces',dr,['Proposition 5.1.','Proposition 5.2.','Proposition 5.3.','Lemma 5.4.','primitive cubic Dirichlet']),
 ('2026 fixed-angular and source interfaces',oa,['Proposition A.4','(A.5)','(A.8)','(A.9)','no uniformity in a growing angular','G(b)']),
 ('Yoshimoto separate prime/noncubic interface',yo,['THEOREM 2.','degree 1','α3','parity' if 'parity' in yo else 'α( —1)']),
 ('Dunn cuspidal scope',du,['METAPLECTIC CUSP FORMS','fixed cubic metaplectic cusp form','Lemma 1.4.']),
]:
 for token in tokens:
  assert token in body,(name,token)
 checks.append({'kind':'primary_anchor','name':name,'tokens':tokens,'pass':True})
expected=[
 Fraction(51,100)-Fraction(1,2),
 Fraction(51,100)*(1+Fraction(1,64))-(Fraction(1,2)+Fraction(1,64)),
 Fraction(51,100)*(1+Fraction(1,32))-(Fraction(1,2)+Fraction(1,32)),
 Fraction(1,100)/Fraction(49,100),
 Fraction(5,6)-Fraction(1,100)-Fraction(1,2),
 Fraction(1,2)+Fraction(3,4)*Fraction(1,2)+Fraction(1,2)*Fraction(1,12),
 Fraction(11,12)-Fraction(1,2),
 1-Fraction(1,12),
 Fraction(1,3)+Fraction(1,2)*Fraction(1,2),
]
receipt=json.loads((O/'parameter-controls-v1.json').read_text())
assert len(receipt['checks'])==len(expected)
for row,got in zip(receipt['checks'],expected):
 assert Fraction(row['value'])==got==Fraction(row['expected']),(row,got)
 checks.append({'kind':'exact_fraction','name':row['name'],'value':str(got),'pass':True})
citation=json.loads((P/'PUBLIC-CITATION-v1.json').read_text())
assert len(citation['items'])==4
assert 'private' not in json.dumps(citation['items']).lower()
checks.append({'kind':'citation_metadata','pass':True,'items':4,'private_cache_locator_in_public_items':False})
out=O/'AUTHOR_CHECKS-v1.json'
if out.exists():raise RuntimeError('Refuse overwriting '+str(out))
out.write_text(json.dumps({'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'scope':'Source integrity/anchor and new rational interface controls only; no numerical family, Lean, full-paper proof verification or actual signed estimate.',
 'pass':True,'checks':checks,
 'checked_note_sha256':sha(P/'PRIMARY_MATCH_AND_ANGULAR_GAUSS-v1.md'),
 'public_citation_sha256':sha(P/'PUBLIC-CITATION-v1.json')},indent=2)+'\n')
print(json.dumps({'pass':True,'checks':len(checks),'receipt':str(out),'sha256':sha(out)}))
