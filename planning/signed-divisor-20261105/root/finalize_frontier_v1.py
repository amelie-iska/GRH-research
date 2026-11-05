from pathlib import Path
import json,hashlib
R=Path('/home/iska/Documents/LaTeX-projects/GRH-from-Mac-20261104')
prom=R/'outputs/checks/2026-11-05-signed-divisor/promotion-v1/promotion-v1.json';d=json.loads(prom.read_text());assert d['passed']
O=R/'outputs/checks/2026-11-05-signed-divisor/root/frontier-final-v1';O.mkdir(parents=True,exist_ok=False)
text='''

Final signed-divisor promotion: outputs/checks/2026-11-05-signed-divisor/promotion-v1/promotion-v1.json binds the accepted bookPDFv1/nativev3 and four article/notev1 builds. Current delivered edition279pages/40chapters/8176MathML, preserving ALL7891 prior literal math subtrees in order,385oldtables/13canonical iframes/28oldSVG refs. One new source-matched workflow SVG/PDF/TeX gives29totalSVGrefs. Focused64/175pages; notes23/66pages. Independent source/proof/data/UI/build preservation reviews and finalnative-qa-v3 pass. The failed narrow-table320px candidate and measured local-scroll probe are preserved; finaltable/math bytes and fonts remain unchanged. Root visually inspected workflow and new PDF proof pages. Three inherited malformed munder nodes and old amsmath/hyperref/underfull diagnostics remain disclosed; no new malformednode,overfullbox,unresolvedreference or Lean declaration. This is not a new signed exponent, determinant or zero-location bridge. Publication is separately gated. Protected sourceHEAD/index and all previous worktrees/evidence remain unchanged.
'''
changed=[]
for name in ['planning/MASTER_IMPLEMENTATION_PLAN.md','planning/PROGRESS.md','planning/CONTINUATION.md','planning/OPEN_OBLIGATIONS.md','book/SOURCE_COVERAGE.md','book/VERIFICATION.md']:
 p=R/name;(O/name.replace('/','__')).write_bytes(p.read_bytes());p.write_text(p.read_text()+text);changed.append(name)
p=R/'README.md';(O/'README.md').write_bytes(p.read_bytes());p.write_text(p.read_text()+'\nCurrent delivered edition:279pages/40chapters/8176MathML; focused64/175pages and notes23/66pages. All7891 prior literal math subtrees remain ordered and byte-identical. The signed-divisor exact finite reference and new workflow add no asymptotic power saving or Lean theorem.\n');changed.append('README.md')
p=R/'web/index.html';before=p.read_bytes();(O/'web__index.html').write_bytes(before);s=before.decode()
old='272 pages · 40 chapters · 7,891 MathML expressions';assert s.count(old)==1;s=s.replace(old,'279 pages · 40 chapters · 8,176 MathML expressions')
old='focused articles62/168pages and notes20/59pages';assert s.count(old)==1;s=s.replace(old,'focused articles64/175pages and notes23/66pages')
needle='<section id="learning">';assert s.count(needle)==1;s=s.replace(needle,needle+'<p><a class="button" href="/signed-divisor.html">Complete-column laboratory: step through ideal incidence, actual row states and signed divisor sums ↗</a></p>')
needle='The signed asymptotic estimate and GRH bridge remain open.';assert s.count(needle)==1;s=s.replace(needle,'A new exact divisor lift and nine-zeta/eight-state expansion retain the actual coherent signed sum; the complete-column reference exposes every raw mask. The signed asymptotic estimate and GRH bridge remain open. <a href="/book/main.html#sd:core">Read the signed-divisor proof ↗</a>')
p.write_text(s);changed.append('web/index.html')
record={'passed':True,'promotion_sha256':hashlib.sha256(prom.read_bytes()).hexdigest(),'changed':changed,'sha256':{n:hashlib.sha256((R/n).read_bytes()).hexdigest() for n in changed},'scope':'Add final accepted counts and user-facing laboratory/proof links, without altering historical math or gates; publication not yet claimed'}
(O/'record.json').write_text(json.dumps(record,indent=2)+'\n');print(json.dumps({'passed':True,'documents':len(changed)}))
