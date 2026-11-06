from pathlib import Path
import json,hashlib,re
R=Path('/home/iska/Documents/LaTeX-projects/GRH-from-Mac-20261104');p=R/'outputs/checks/2026-11-05-physical-sieve/promotion-v1/promotion-v1.json';d=json.loads(p.read_text());assert d['passed']and d['edition']['book_pages']==303 and d['edition']['MathML']==9172
O=R/'outputs/checks/2026-11-05-physical-sieve/root/frontier-final-v1';assert not O.exists()
text='''

Final physical-sieve promotion: outputs/checks/2026-11-05-physical-sieve/promotion-v1/promotion-v1.json binds valid bookPDF/nativev3, focused concisev1/extendedv2 and notes concisev1/extendedv2, plus inspected inspectorv3. Edition303pages/40chapters/9172MathML, focused71/200pages, notes29/89. ALL8552previous literal math subtrees remain ordered/byte-identical, all388oldtables remain in389,13canonical iframes/29SVGrefs/assets unchanged. Current external-preprint-based unsigned envelope has critical9/8 and original unweighted A6=1two-pivot signed comparison13/12; target3/4 is still open. Globalgap3/8/scopedsignedgap1/3 supersede former5/12. Newshortpositivecertificate19/24pure and min7/9mixed have only CONDITIONAL scalarinput/strictstrip diagnostics; no input or newzero-free strip is proved. Fixed0<theta<1 moving-profile supnorm sharpness is not fixed-W sharpness. Every original mask/commonprofile/mean/endpoint and arbitraryweightednorm qualification remains.

All6source-bound PDF/native builds, independent mathematical/application/integration reviews, focused exponent/model controls and UI/native desktop/mobile/night/keyboard/source/PDF/visual checks pass. No new malformedMathML/overfull/unresolvedreference/Lean declaration. Three inherited munder nodes and old amsmath/hyperref/underfull diagnostics remain; source-matched cachedPDF searchability/publicSVG limits unchanged. Failed hash-line/native-spacing/earlycapture candidates and all old outputs remain preserved. Both completiongatesFALSE; target signedassembly, independent determinant/zero-location and scope-specific GRH/analytic-categoryLean remainOPEN. Linux4.24approval stillunanswered; no newinstall/substitution/question. OriginalsourceHEAD/index, all releaseworktrees/indices/environments/caches/history/Macpreview/privateactive-data protected. Publication is separately gated; keepONEheartbeatACTIVE.
'''
planned={};original={}
for n in ['planning/MASTER_IMPLEMENTATION_PLAN.md','planning/PROGRESS.md','planning/CONTINUATION.md','planning/OPEN_OBLIGATIONS.md','book/SOURCE_COVERAGE.md','book/VERIFICATION.md','planning/COVERAGE.md']:
 original[n]=(R/n).read_bytes();planned[n]=original[n]+text.encode()
n='README.md';original[n]=(R/n).read_bytes();s=original[n].decode()
s,count=re.subn(r'^Current edition: \*\*[^\n]+\*\*\.', 'Current edition: **303 pages,40 chapters,9,172 MathML expressions and thirteen unique in-book laboratories**.',s,count=1,flags=re.M);assert count==1
planned[n]=(s+text).encode()
n='web/index.html';original[n]=(R/n).read_bytes();s=original[n].decode()
for before,after in [
('288 pages · 40 chapters · 8,552 MathML expressions','303 pages · 40 chapters · 9,172 MathML expressions'),
('focused articles67/183pages and notes25/74pages','focused articles71/200pages and notes29/89pages'),
('Arithmetic frontier: inspect the new conductor bound and remaining 7/6 envelope','Current arithmetic bounds: physical radicands9/8 and the sixth-free13/12 slice'),
('New: an ordinary-conductor refinement gives the unsigned7/6 envelope','Previously, an ordinary-conductor refinement gave the unsigned7/6 envelope'),
('retaining power7/6 and its unresolved5/12 excess.','with its former power7/6 and5/12 excess retained as history.'),
('Read the new bound and its proof ↗','Previous ordinary bound and proof ↗')]:
 assert s.count(before)==1,(before,s.count(before));s=s.replace(before,after)
marker='New: an ordinary-conductor' # No substitution relies on this historical marker.
needle='; focused articles71/200pages and notes29/89pages. ';assert s.count(needle)==1
new='Current: a pinned fixed-order preprint theorem applied to the physical sixth-power-free family gives global unsigned power9/8 and the original A₆=1two-pivot signed slice13/12. Every raw mask, common profile and coherent mean remains; the fixed-profile target3/4 and independent determinant/zero-location bridge are open. <a href="/book/main.html#phy:core">Read the current application proof ↗</a> · <a href="/book/main.html#cmr:core">Mean-retaining coherent reductions ↗</a> · <a href="/quadratic-pivot.html">Inspect current and historical powers ↗</a>. '
s=s.replace(needle,needle+new);planned[n]=s.encode()
for n,b in original.items():assert(R/n).read_bytes()==b,n
O.mkdir(parents=True)
for n,b in original.items():(O/n.replace('/','__')).write_bytes(b)
for n,b in planned.items():(R/n).write_bytes(b)
r={'passed':True,'promotion_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'changed':list(planned),'sha256':{n:hashlib.sha256((R/n).read_bytes()).hexdigest()for n in planned},'scope':'Final accepted edition/current-bound metadata, exact proof links and preserved history. No new publication assertion.'}
(O/'record.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps({'passed':True,'documents':len(planned)}))
