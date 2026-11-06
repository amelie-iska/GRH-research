#!/usr/bin/env python3
"""Append verified local milestone to ledgers; preserve prefixes and every before byte."""
from pathlib import Path
import csv,io,json,hashlib,os,subprocess
R=Path('/home/iska/Documents/LaTeX-projects/GRH-from-Mac-20261104')
C=R/'outputs/checks/2026-11-06-gauss-book'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def main():
 promotion=C/'promotion-v1/promotion-v1.json';pr=json.loads(promotion.read_text());assert pr['passed']
 out=C/'metadata-v1';assert out.exists() and not (out/'receipt.json').exists()
 note="""

## 6 November 2026 — reviewed local Gauss-tail book milestone

The Linux working book is333pages/40chapters/10299nativeMathML; all9810previous literal math subtrees are ordered and byte-identical. All389tables/14canonical iframes/30oldSVG references and85non-HTML book assets remain unchanged. One original short-divisor partition/cubic-matrix diagram raises SVG references to31. Focused articles are81/228pages; analytic notes39/118pages. Sources papers/gauss-tail-{core,details}.tex and matching generated book copies retain85shared labels plus the book-only figure label, with full proofs and exact PDF-aux numbering.

The prior accepted actual pure Gauss-weighted large-short-divisor tail is now fully cited/explained in the book: the two disjoint cutoff boxes give TU+TY before the physical cubic matrix norm. The only deep input is the previously pinned external deFaveri2610.04045v1 Theorem1.1/Example2.2 n3; no new sieve or reproof is claimed. The original finiteK, all primitive roots/S values/source/ray/class/rawzero/full-union/common-complexW data and explicit Mellin seminorm remain.

NEW independently accepted direct reduction retains the ACTUAL discrete sixth-part s and EVERY original rho: P_X[AU,AU] reduces to its original-finiteK small-AY j0 model. It does not introduce the separate principal-density/counting-mean split. At A1~H=D3/4,X=D3/8,Y=min(U,D1/8), errors have powers-1/16,3/4,31/48 (the coefficient tail is exactly0 ifY=U). There is NO k/s or w/s coprimality mask; overlapping frequencies and all w<64/nonunit S modes remain. The old separate37/48 counting-error certificate is neither improved nor set tozero; its effects stay in the exact-discrete small model. That model is still unestimated at target size. The full signed13/12 and global unsigned9/8 are unchanged.

Separate RESEARCH-ONLY work OUTSIDE these book fragments uses the exact J5 finite ideal HB identity and the same physical cubic norm on balanced residual blocks. The linear TypeII column costs M(W)D^epsilon D^(1/3)Y^(1/3); the stated pure principal leading component has critical power11/16. This is a scoped signed-component estimate, not an energy lower bound or a full target theorem. Exhaustive one-long-unrestricted-factor classification explicitly assumesD>=2^64. BOTH-TypeI, including long prime residuals, remains open. See planning/gauss-book-20261106/lane-a/BALANCED_RESIDUAL_HEATH_BROWN_CUBIC-v2.md and independently reviewed research aggregate outputs/checks/2026-11-06-gauss-book/RESEARCH_ACCEPTED-v1.json.

Focused checks: all5source-bound final PDFs pass; current book and detailed editions are buildsv3, unchanged concise editions are source-bound v2 reuse. Final nativev3 adds489MathML with zero new malformed nodes/rawTeX/conversion warnings. Independent mathematical/source/artifact reviews and representative five-PDF/native visuals pass. The SAME focused browser harness passes40checks at desktop1440/mobile320, both palettes and keyboard horizontal scrolling; all86labels/63equations/65references and source/PDF/figure hashes pass. It records105global protocol events+1initial marker, zero actual parent departures, fetch/HTTP/newpageerrors/pending/timeouts0, with750msquiet/30sidle guards. This is focused local QA, not a rerun of the220group public release audit. Three inherited munder warnings and oldamsmath/hyperref/underfull diagnostics remain, with no new overfull/unresolved reference or Lean declaration. Source-matched cached PDF searchability and public-SVG reproduction limits remain disclosed.

Fresh synthetic formal algebra checks cover2304 coefficient equalities/847 target coefficients and2184 dyadic scale boxes, with exact integer powers, distinct equal-norm formal ideals and seed2026110609. A deliberately incorrect J4/same-fifth-root truncation fails at norm544825 (true+1,wrong-23,remainder+24). These support the new HB algebra/grouping; they are not actual character/Gauss/family data, interval arithmetic or Lean. No old scientific tables/traces/control suites were rerun. Every failed source guard, overfull/Pandoc candidate and night palette diagnostic is preserved. The night filter was readable but altered the new source palette; only the new diagram now keeps that palette on a white canvas, with old theme/assets unchanged.

This is LOCAL promotion only. No new public release: Main87f89878f470ab98b84055fe72f28766d89202c6/Pagesf6773684b6ea4d5ee067409c62c88c80d1529080 and the hosted319page/9810MathML edition remain current. Existing Macworkspace/old8765 preview and all13HEAD/indexstates/12releaseworktrees are preserved. No dependency/toolchain installation, authentication, token access/transfer, external MCP activation, Claude/global config or Git/index/publication action occurred.

NEXT implementation: prepare a separately reviewed substantive release from this milestone with all5PDF exports and the exact new source-only research closure; do not publish a status-only update. NEXT arithmetic: bound the actual residual long TypeI Gauss moment or the full exact-discrete small-AY kernel before losing r/k/w/s/root/column coupling. Retain fixedW/explicit seminorms, exactAU, allclass/rho/nonunitS/full-union/commonprime/rawzero/ray/SF/conductor/capacity hypotheses, and return to neighboring pure/mixed blocks and signed full assembly separately. Do not rebrand the finished balanced block, cutoff tail, scalar-count, density, free-Euler or norm routes as the full target.

P4/P7/priorP9 and both completion gates remain unfinished; one existing heartbeat stays ACTIVE. Independent positive arithmetic determinant/zero-location comparisons remain separate for Dirichlet/Hecke/Dedekind/elliptic/generalArtin; no Artinholomorphy/GRH/desiredpositivity/zero assumption. Actual analytic/categoryLean is unfinished. Linux4.24approval remains unanswered: no install/download/substitute/reinventory/repeated question.
"""
 names=['planning/MASTER_IMPLEMENTATION_PLAN.md','planning/PROGRESS.md','planning/CONTINUATION.md','planning/OPEN_OBLIGATIONS.md','book/SOURCE_COVERAGE.md','book/VERIFICATION.md']
 append={n:note for n in names}
 append['README.md']="""

## Reviewed local Gauss-tail edition — 6 November 2026

The verified Linux working book is333pages/10299MathML, preserving every prior formula, table and all14labs; focused articles are81/228pages and notes39/118pages. [Shared statements](papers/gauss-tail-core.tex) and full proofs explain the actual signed short-divisor tail and a new exact-discrete top-prefix reduction retaining every ray, finite cutoff and raw mask. An original partition/cubic-matrix diagram supports the exposition. All5PDFs, native structure, independent reviews and40focused browser checks pass. The remaining small-cutoff moment and long TypeI terms remain open; whole signed13/12/global unsigned9/8, determinant/zero-location, comprehensive Lean and GRH are unchanged. Public Main87f89878/Pagesf6773684 still serve319pages/9810MathML. See planning/gauss-book-20261106/HANDOFF-v1.md and the local milestone receipt under outputs/checks/2026-11-06-gauss-book/. Both completion gates are false; the existing heartbeat continues.
"""
 records={}
 for n,t in append.items():
  p=R/n;backup=out/'before'/n;assert backup.is_file();old=backup.read_bytes()
  assert p.read_bytes()==old+t.encode(),('Concurrent ledger change',n)
  records[n]=dict(before=hashlib.sha256(old).hexdigest(),after=sha(p),old_bytes_preserved=True,already_appended_once_in_preserved_v1=True)
 p=R/'planning/CLAIMS.csv';old=p.read_bytes();rows=list(csv.reader(io.StringIO(old.decode())));ids={x[0] for x in rows[1:]};assert not ids&{'GTB01','GTDIRECT01','HBRES01'}
 backup=out/'before/planning/CLAIMS.csv';backup.parent.mkdir(parents=True,exist_ok=True);backup.write_bytes(old)
 s=io.StringIO(newline='');w=csv.writer(s,lineterminator='\r\n')
 w.writerow(['GTB01','papers/gauss-tail-core.tex;papers/gauss-tail-details.tex','Actual pure finite-K Gauss-weighted large-short-divisor tail integrated with full proof and unique diagram','External pinned physical cubic input;all masks/fixedW/Mellin seminorm;small model/full bound open','outputs/checks/2026-11-06-gauss-book/promotion-v1/promotion-v1.json','Bound actual long residual TypeI/coupled small model'])
 w.writerow(['GTDIRECT01','planning/gauss-book-20261106/lane-b/DIRECT_DISCRETE_TOP_CUTOFF-v2.md','Original exact-discrete all-rho pure top-prefix reduces to finite-K smallAY j0 model with target-sized errors','Every original s/w endpoint/rawzero retained;no density split or new whole exponent','outputs/checks/2026-11-06-gauss-book/review-a-direct/acceptance-v1.json','Bound remaining exact-discrete smallAY kernel before triangles'])
 w.writerow(['HBRES01','planning/gauss-book-20261106/lane-a/BALANCED_RESIDUAL_HEATH_BROWN_CUBIC-v2.md','Research-only exact J5 residual identity and balanced TypeII principal leading component11/16','Outsidebook;D>=2^64 TypeI classification;both-TypeI/full target open;formal controls syntheticonly','outputs/checks/2026-11-06-gauss-book/review-b-hb/acceptance-v1.json','Bound actual long unrestricted TypeI Gauss sums with growing coupled masks'])
 assert old.endswith(b'\n');p.write_bytes(old+s.getvalue().encode());records['planning/CLAIMS.csv']=dict(before=hashlib.sha256(old).hexdigest(),after=sha(p),old_bytes_preserved=True)
 p=R/'web/index.html';old=p.read_bytes();backup=out/'before/web/index.html';backup.parent.mkdir(parents=True,exist_ok=True);backup.write_bytes(old)
 t=old.decode();a='319 pages · 40 chapters · 9,810 MathML expressions</strong>; focused articles 76/215 pages and notes 34/105 pages.';b='333 pages · 40 chapters · 10,299 MathML expressions</strong>; focused articles 81/228 pages and notes 39/118 pages.'
 assert t.count(a)==1;t=t.replace(a,b)
 key='<section id="reading">';assert t.count(key)==1
 t=t.replace(key,key+'<p class="small">New: <a href="/book/main.html#gtl:core">actual Gauss-weighted cutoff tail and exact discrete-prefix reduction</a>. The small-cutoff kernel and full signed target remain open.</p>')
 p.write_text(t);records['web/index.html']=dict(before=hashlib.sha256(old).hexdigest(),after=sha(p))
 for n in ['web/verification.html','web/implementation-plan.html']:
  p=R/n;backup=out/'before'/n;backup.parent.mkdir(parents=True,exist_ok=True);backup.write_bytes(p.read_bytes())
 env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1'}
 for script in ['scripts/build_verification_page.py','scripts/build_implementation_page.py']:
  x=subprocess.run(['python3',script],cwd=R,env=env,capture_output=True,text=True,check=True)
  (out/(Path(script).stem+'.stdout.txt')).write_text(x.stdout+x.stderr)
 rec=dict(passed=True,promotion_sha256=sha(promotion),append_records=records,generated_pages={n:sha(R/n) for n in ['web/verification.html','web/implementation-plan.html']},producer_sha256=sha(Path(__file__)),public_release_performed=False,project_complete=False,research_complete=False)
 (out/'receipt.json').write_text(json.dumps(rec,indent=2)+'\n');print(json.dumps(dict(passed=True,sha256=sha(out/'receipt.json'))))
if __name__=='__main__':main()
