#!/usr/bin/env python3
"""Read-only348 source selection/preflight with actual API roundtrips and in-memory Pages projection. No copy/stage/build/publish."""
from pathlib import Path
from collections import defaultdict, deque
from datetime import datetime, timezone
import argparse, ast, base64, hashlib, json, os, re, stat, subprocess

ROOT=Path("/home/iska/Documents/LaTeX-projects/GRH-from-Mac-20261104")
TARGET=Path("/home/iska/Documents/LaTeX-projects/GRH-publication-20261106-ramified")
BASE="1f346d1a825aa6eff1479197aef45d293a878902"
PAGES="de2614bf439e1c6ab8af09f3242af5a163f16f79"
ENV={**os.environ,"GIT_OPTIONAL_LOCKS":"0","PYTHONDONTWRITEBYTECODE":"1"}
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def blob(b):return hashlib.sha1(b"blob "+str(len(b)).encode()+b"\0"+b).hexdigest()
def load(n):return json.loads((ROOT/n).read_text())
def block(n):
    parts=Path(n).parts
    if any(x in n for x in ["protected-baseline","protected-final","canonical-preservation","metadata-stage-","FIGURE_ACCEPTED-v1.json","static-source-v1.json","RUN_CLOSED-v1.json"]):return True
    return ((n.startswith("planning/") and n.endswith(".pdf"))
      or any(x in {"primary","primary-private","primary-cache","private","adversarial-sources","build-admin","release-preparation-v1","protected-snapshot-v1"} for x in parts)
      or any(x in n.lower() for x in ["publisher-cache","private-pins","source-index","index-refreshed","index-preserved","automation"])
      or n.endswith((".bin",".env",".pt",".pth",".ckpt",".safetensors"))
      or n.startswith(("outputs/experiments/","outputs/datasets/","planning/ramified-release-20261106/root/public-overlay-v1/"))
      or n.startswith(("planning/ramified-release-20261106/lane-a/","planning/ramified-release-20261106/lane-a-held/",
                       "outputs/checks/2026-11-06-ramified-release/lane-a/","outputs/checks/2026-11-06-ramified-release/lane-a-held/")))
def normalize(s):
    if s.startswith(str(ROOT)+"/"):s=s[len(str(ROOT))+1:]
    if "\n" in s or "\\" in s or "\0" in s or Path(s).is_absolute() or ".." in Path(s).parts:return None
    if s != Path(s).as_posix():return None
    if s=="README.md":return s
    if not s.startswith(("planning/","outputs/","book/","papers/","scripts/","web/","research/","examples/")):return None
    return s
ap=argparse.ArgumentParser();ap.add_argument("--output",required=True,type=Path);args=ap.parse_args()
out=args.output.resolve();assert out.is_relative_to(ROOT/"outputs/checks/2026-11-06-ramified-release/lane-b") and not out.exists()
assert not TARGET.exists(),"Root reviews proposal before fresh worktree creation"
out.mkdir(parents=True)
index=ROOT/".git/index";index_before=sha(index)
assert index_before=="0ef1af515b143ef68fed1d9a42aef7c00d5d1d7c3ef6832d2926d48e0925214c"
treebytes=subprocess.check_output(["git","ls-tree","-rz","--full-tree",BASE],cwd=ROOT,env=ENV)
base={}
for row in treebytes.split(b"\0"):
    if not row:continue
    left,name=row.split(b"\t",1);mode,kind,oid=left.decode().split()
    base[name.decode()]={"mode":mode,"type":kind,"sha":oid}
groups=defaultdict(set);excluded=[];historical=[];aliases={};alias_rows={};missing=[];opened=set();queue=deque()
promotion="outputs/checks/2026-11-06-ramified-book/lane-b/promotion-v1/promotion-v1.json"
p=load(promotion);assert p["passed"]
for row in p["changed_artifacts"]:
    src,dest=row["source"],row["target"]
    assert (ROOT/src).read_bytes()==(ROOT/dest).read_bytes()
    aliases[src]=dest
# Exact copied producers are represented once at their canonical source paths.
canonical_code=[
 "planning/ramified-book-20261106/root/build_book_pdf_v1.py",
 "scripts/build_remote_articles.py","planning/physical-sieve-20261105/builds/build_notes_v1.py",
 "planning/ramified-book-20261106/root/render_native_v1.py",
]
byhash={sha(ROOT/n):n for n in canonical_code}
def add(n,group,pin=None,follow=True):
    n=normalize(n)
    if not n:return
    if block(n):
        excluded.append({"path":n,"reason":"Private/primary/build-admin/automation/raw-index or explicitly excluded NEW research","via":group});return
    if any(x in Path(n).parts for x in ["before","previous","prepromotion","draft-v1","draft-v2"]) or "/failed" in n:
        excluded.append({"path":n,"reason":"Historical before/draft/failure version retained locally; governing current proof and layout gates selected","via":group});return
    if n.endswith((".png",".jpg",".jpeg",".stdout",".stderr")):
        excluded.append({"path":n,"reason":"Local visual/diagnostic capture; public PDF/SVG and acceptance hashes retained","via":group});return
    if n.startswith("outputs/") and n not in aliases and Path(n).suffix in {".pdf",".log",".toc",".html",".tex",".js"} and not n.startswith(("outputs/book/","outputs/papers/")):
        excluded.append({"path":n,"reason":"Noncanonical generated/stale candidate output; approved promoted aliases and current PDF records selected instead","via":group});return
    path=ROOT/n
    if not path.is_file():
        missing.append({"path":n,"via":group});return
    assert not path.is_symlink() and path.resolve().is_relative_to(ROOT),n
    actual=sha(path)
    if pin and actual!=pin:
        historical.append({"path":n,"claimed_sha256":pin,"current_sha256":actual,"via":group,
                           "reason":"Historical/context binding, not silently treated as a current source pin"});return
    if n in aliases:
        dest=aliases[n];assert actual==sha(ROOT/dest)
        alias_rows[n]={"promoted_path":dest,"sha256":actual,"bytes":path.stat().st_size}
        n=dest;path=ROOT/n
    elif path.name in {"ramified-cusp-prefix.pdf","ramified-cusp-prefix.svg","ramified-cusp-prefix.tex"} and actual==sha(ROOT/("book/figures/"+path.name)):
        dest="book/figures/"+path.name;alias_rows[n]={"promoted_path":dest,"sha256":actual,"bytes":path.stat().st_size};n=dest
    elif path.name in {"builder.py","build_isolated.py","renderer.py"} and actual in byhash:
        dest=byhash[actual];alias_rows[n]={"promoted_path":dest,"sha256":actual,"bytes":path.stat().st_size};n=dest
    first=n not in groups;groups[n].add(group)
    mode="100755" if (ROOT/n).stat().st_mode&stat.S_IXUSR else "100644"
    in_base=base.get(n)=={"mode":mode,"type":"blob","sha":blob((ROOT/n).read_bytes())}
    if first and follow and n.endswith(".json") and not in_base:queue.append(n)
def seeds(text,group):
    for n in text.splitlines():
        n=n.strip()
        if n and not n.startswith("#"):add(n,group)
seeds('\npapers/ramified-gauss-core.tex\npapers/ramified-gauss-details.tex\nbook/chapters/ramified-gauss-core.tex\nbook/chapters/ramified-gauss-details.tex\nbook/chapters/ramified-gauss-figure.tex\nbook/chapters/weighted-cutoff.tex\nbook/figures/ramified-cusp-prefix.tex\nbook/figures/ramified-cusp-prefix.pdf\nbook/figures/ramified-cusp-prefix.svg\npapers/resolutions-concise.tex\npapers/resolutions-extended.tex\npapers/validated-oracle-concise.tex\npapers/validated-oracle-extended.tex\nscripts/assemble_book.py\nscripts/build_public_site.py\nscripts/theme_assets.py\nscripts/build_implementation_page.py\nscripts/build_verification_page.py\nscripts/verify_project.py\nscripts/build_remote_articles.py\nplanning/physical-sieve-20261105/builds/build_notes_v1.py\nREADME.md\nbook/SOURCE_COVERAGE.md\nbook/VERIFICATION.md\nplanning/MASTER_IMPLEMENTATION_PLAN.md\nplanning/PROGRESS.md\nplanning/CONTINUATION.md\nplanning/OPEN_OBLIGATIONS.md\nplanning/CLAIMS.csv\nplanning/IMPLEMENTATION_QUEUE.json\nweb/index.html\nweb/implementation-plan.html\nweb/verification.html\nplanning/ramified-book-20261106/HANDOFF-v1.md\noutputs/checks/2026-11-06-ramified-book/root/MILESTONE_ACCEPTED-v1.json\noutputs/checks/2026-11-06-ramified-book/root/RUN_CLOSED-v1.json\noutputs/checks/2026-11-06-ramified-book/lane-b/promotion-v1/promotion-v1.json\noutputs/checks/2026-11-06-ramified-book/root/source-integration-v1.json\noutputs/checks/2026-11-06-ramified-book/lane-a/review-math-v1/acceptance-v1.json\noutputs/checks/2026-11-06-ramified-book/root/figure-acceptance-v1.json\noutputs/checks/2026-11-06-ramified-book/lane-a/FIGURE_ACCEPTED-v2.json\noutputs/checks/2026-11-06-ramified-book/lane-c/artifacts/figure-review-v1/acceptance-v1.json\noutputs/checks/2026-11-06-ramified-book/lane-b/build-aggregate-v1/aggregate-v1.json\noutputs/checks/2026-11-06-ramified-book/native/run-v1/native-build-record.json\noutputs/checks/2026-11-06-ramified-book/native/run-v1/supplement.ast.json\noutputs/checks/2026-11-06-ramified-book/lane-c/artifacts/candidate-review-v1/acceptance-v1.json\noutputs/checks/2026-11-06-ramified-book/lane-c/artifacts/candidate-review-v1/artifact-manifest-v1.json\noutputs/checks/2026-11-06-ramified-book/lane-a/browser-v1/acceptance-v1.json\noutputs/checks/2026-11-06-ramified-book/lane-a/browser-v1/run-v1/receipt.json\noutputs/checks/2026-11-06-ramified-book/lane-a/browser-v1/run-v1/browser.json\noutputs/checks/2026-11-06-ramified-book/lane-a/browser-v1/run-v1/network-navigation-timing.json\noutputs/checks/2026-11-06-ramified-book/root/pdf-visual-v1/acceptance-v1.json\noutputs/checks/2026-11-06-ramified-book/root/native-visual-v1.json\noutputs/checks/2026-11-06-ramified-book/metadata-final-v1/receipt-v1.json\noutputs/checks/2026-11-06-ramified-book/lane-b/independent-review-post-v1/acceptance-v1.json\nplanning/unit-gauss-20261106/HANDOFF-v1.md\noutputs/checks/2026-11-06-unit-gauss/RESEARCH_ACCEPTED-v1.json\nplanning/twisted-gauss-20261106/HANDOFF-v1.md\noutputs/checks/2026-11-06-twisted-gauss/RESEARCH_ACCEPTED-v1.json\nplanning/ramified-gauss-20261106/HANDOFF-v1.md\noutputs/checks/2026-11-06-ramified-gauss/RESEARCH_ACCEPTED-v1.json\noutputs/checks/2026-11-06-gauss-release/research-aggregate-v1/RESEARCH_ACCEPTED-v1.json\nplanning/ramified-book-20261106/lane-c/research/BOUNDED_GOOD_PART_COMPLEMENT-v2.md\noutputs/checks/2026-11-06-ramified-book/lane-c/research/fixed-family-match-addendum-v1.json\noutputs/checks/2026-11-06-ramified-book/lane-c/research/RESEARCH_ACCEPTED-v1.json\nplanning/ramified-book-20261106/lane-c/research/HANDOFF-v1.md\nplanning/ramified-book-20261106/lane-b/review-complement-v1/INDEPENDENT_REVIEW-v1.md\noutputs/checks/2026-11-06-ramified-book/lane-b/review-complement-v1/acceptance-v1.json\noutputs/checks/2026-11-06-ramified-book/root/review-complement-v1/acceptance-v1.json\nplanning/ramified-gauss-20261106/lane-a/PUBLIC-CITATION-v1.json\nplanning/twisted-gauss-20261106/lane-a/PUBLIC-CITATION-v1.json\nplanning/unit-gauss-20261106/lane-a/PUBLIC-CITATION-v2.json\nplanning/ramified-book-20261106/root/build_book_pdf_v1.py\nplanning/ramified-book-20261106/root/run_builds_v2.py\nplanning/ramified-book-20261106/root/render_native_v1.py\nplanning/ramified-book-20261106/lane-a/build_figure_v6.py\nplanning/ramified-book-20261106/lane-a/verify_figure_v6.py\nplanning/ramified-book-20261106/lane-a/check_native_v1.mjs\nplanning/ramified-book-20261106/lane-a/serve_candidate_v2.py\nplanning/ramified-book-20261106/lane-c/artifacts/check_candidates_v7.py\nplanning/ramified-book-20261106/lane-b/build-aggregate-v1/aggregate_existing_v1.py\nplanning/ramified-book-20261106/lane-b/review_metadata_v3.py\nplanning/ramified-book-20261106/lane-b/review_postpromotion_v2.py\nplanning/ramified-release-20261106/lane-b/SCIENCE_SELECTION_PLAN-v1.md\nplanning/ramified-release-20261106/lane-b/prepare_science_selection_v3.py\n',"Explicit reviewed348science/evidence/accepted parent closure")
# Exact canonical promoted artifacts, never duplicate candidate PDFs/native HTML.
for row in p["changed_artifacts"]:add(row["target"],"18 canonical promoted artifacts")
# Expand only exact named receipt pointers/hash maps, never a directory or Markdown history sweep.
SKIP_KEYS={"supersedes","historical_author_receipt","before","previous","parent","parent_aggregate","parent_note","parent_source_map","historical",
 "preserved_draft_snapshots","old_book_assets_sha256","source_and_live_before","promoted_artifacts_before",
 "target_before_sha256","independently_reviewed_artifact_sha256","before_sha256","checkpoint",
 "acceptance_records_sha256","source_HEAD","source_index_sha256"}
ALLOWED_START=("planning/","outputs/","book/","papers/","scripts/","web/","research/","examples/")
def walk(v,via,key=""):
    if key in SKIP_KEYS or key.startswith(("before_","old_","parent_","historical_","preserved_")):return
    if isinstance(v,dict):
        if v.get("exists") is False and isinstance(v.get("path"),str):
            n=normalize(v["path"])
            if n:
                assert not (ROOT/n).exists()
                excluded.append({"path":n,"reason":"Explicit inactive IfFileExists branch, absence confirmed; active figures remain SHA-guarded","via":via})
            return
        if isinstance(v.get("path"),str):
            n=normalize(v["path"])
            if n:add(n,via+" named pointer",v.get("sha256"),follow=True)
        for k,x in v.items():
            n=normalize(k) if isinstance(k,str) else None
            if n and isinstance(x,str) and re.fullmatch("[0-9a-f]{64}",x):add(n,via+" exact SHA binding",x)
            elif n and isinstance(x,dict) and "sha256" in x:add(n,via+" exact file row",x["sha256"])
            if k not in {"path","sha256"}:walk(x,via,k)
    elif isinstance(v,list):
        for x in v:walk(x,via,key)
    elif isinstance(v,str):
        n=normalize(v)
        if n and (ROOT/n).is_file():add(n,via+" named path")
while queue:
    n=queue.popleft()
    if n in opened:continue
    opened.add(n)
    obj=load(n)
    def private_reading_pin(v):
        if isinstance(v,dict):return any(private_reading_pin(k) or private_reading_pin(x) for k,x in v.items())
        if isinstance(v,list):return any(private_reading_pin(x) for x in v)
        if isinstance(v,str):
            path=normalize(v)
            return bool(path and any(x in {"primary","primary-private","primary-cache","adversarial-sources"} for x in Path(path).parts))
        return False
    if not Path(n).name.startswith("PUBLIC-CITATION") and private_reading_pin(obj):
        groups.pop(n)
        excluded.append({"path":n,"reason":"Private primary-reading pin metadata, not a public citation or scientific source; exact approved PUBLIC-CITATION selected","via":"current JSON boundary review"})
        continue
    # Administrative integrity/metadata summaries stay summaries; they are not public folder roots.
    if any(x in n for x in ["integrity-acceptance","focused-final-checks","metadata-v1/receipt",
                             "metadata-preparation-v1/receipt","native-visual","pdf-visual"]) or n=="planning/IMPLEMENTATION_QUEUE.json":continue
    if n=="outputs/checks/2026-11-06-gauss-book/builds/run-v2/aggregate.json":
        prior=load(n)
        walk({"results":{k:prior["results"][k] for k in ["focused-concise","notes-concise"]}},n+" ONLY the two actually reused concise rows")
        continue
    walk(obj,n)
# Five exact exports are explicit even if the old builder exports fewer by default.
exports=[]
for source,dest in [
 ("outputs/book/surface-orders-book.pdf","book.pdf"),
 ("outputs/papers/resolutions-concise.pdf","concise.pdf"),
 ("outputs/papers/resolutions-extended.pdf","extended.pdf"),
 ("outputs/papers/validated-oracle-20261104/validated-oracle-concise.pdf","validated-oracle-concise.pdf"),
 ("outputs/papers/validated-oracle-20261104/validated-oracle-extended.pdf","validated-oracle-extended.pdf")]:
    add(source,"Five reviewed PDF exports");exports.append({"source":source,"bundle_path":dest,"sha256":sha(ROOT/source)})
required=[
 "web/book/main.html","web/book/sources/ramified-gauss-core.tex","web/book/sources/ramified-gauss-details.tex",
 "web/book/sources/ramified-gauss-figure.tex","web/book/figures/ramified-cusp-prefix.svg",
 "web/book/figures/ramified-cusp-prefix.pdf","web/book/figures/ramified-cusp-prefix.tex",
 "web/coherent-band.html","web/data/coherent-band-schur-v1.json"]
for n in required:add(n,"Required public runtime/source preservation")
closure={};delta={}
for n,gs in sorted(groups.items()):
    raw=(ROOT/n).read_bytes();mode="100755" if (ROOT/n).stat().st_mode&stat.S_IXUSR else "100644"
    row={"bytes":len(raw),"sha256":hashlib.sha256(raw).hexdigest(),"git_blob_sha1":blob(raw),"mode":mode,
         "groups":sorted(gs),"change":"new" if n not in base else "unchanged" if base[n]=={"mode":mode,"type":"blob","sha":blob(raw)} else "modified"}
    closure[n]=row
    if row["change"]!="unchanged":delta[n]=row
assert sha(index)==index_before

# Only explicit old administrative/context pins may be historical; a changed
# mathematical source pin is an error, not silently excused by selection.
historical_context={"README.md","book/SOURCE_COVERAGE.md","book/VERIFICATION.md","planning/MASTER_IMPLEMENTATION_PLAN.md","planning/PROGRESS.md","planning/CONTINUATION.md","planning/OPEN_OBLIGATIONS.md","planning/CLAIMS.csv","planning/IMPLEMENTATION_QUEUE.json","web/index.html","web/implementation-plan.html","web/verification.html"}
assert all(x["path"] in historical_context for x in historical),("Unexpected stale mathematical pin",historical)
assert not missing,("Missing named source dependencies",missing)
# Strict release-only metadata alias: canonical science/context originals remain
# exact source guards, while only two explicitly reviewed current headlines use
# distinct candidate bytes. Never rewrite receipts or local historical ledgers.
overlay_path="outputs/checks/2026-11-06-ramified-release/root/public-overlay-proposal-v1.json"
overlay=load(overlay_path)
assert sha(ROOT/overlay_path)=="57248dbe2845ae74056c09fb01d4092e9da9dc201bfd79304b25f02f48bfddc5"
assert set(overlay["changes"])=={"README.md","web/index.html"}
overlay_rows={}
for name,rec in overlay["changes"].items():
    candidate=normalize(rec["candidate_source"]);assert candidate
    cp=ROOT/candidate;assert cp.is_file() and not cp.is_symlink()
    assert sha(ROOT/name)==rec["source_before_sha256"] and sha(cp)==rec["candidate_sha256"]
    original=(ROOT/name).read_text();new=cp.read_text()
    if name=="README.md":
        # Exactly the first status paragraph changes; all old remainder and
        # appended historical ledgers are byte-identical.
        before=original.split("\n\nA public research workspace",1)
        after=new.split("\n\nA public research workspace",1)
        assert len(before)==len(after)==2 and before[1]==after[1]
        assert "Current reviewed edition" in after[0] and "normalized upper power101/144" in after[0]
        assert "Whole signed13/12/global9/8" in after[0] and "GRH remain open" in after[0]
    else:
        old='New local proof:'
        assert original.count(old)==1
        expected=original.replace(old,'New:',1).replace(' Public release remains333pages until separately reviewed publication.','',1)
        assert new==expected,"Release index overlay must be exact bounded approved wording"
    raw=cp.read_bytes();row=dict(delta[name]);row.update(source_path=candidate,source_before_sha256=rec["source_before_sha256"],sha256=hashlib.sha256(raw).hexdigest(),git_blob_sha1=blob(raw),bytes=len(raw),release_only_metadata_alias=True)
    delta[name]=row;closure[name]=dict(row);overlay_rows[name]={"source_path":candidate,"sha256":sha(cp),"source_before_sha256":rec["source_before_sha256"]}
# Genuine API representation roundtrips, no API calls or content serialization.
def api_roundtrip(raw,mode):
    assert mode in {"100644","100755"},"Unsafe Git mode"
    try:content=raw.decode("utf-8");encoding="utf-8"
    except UnicodeDecodeError:content=base64.b64encode(raw).decode();encoding="base64"
    payload=json.loads(json.dumps({"encoding":encoding,"content":content},ensure_ascii=True))
    restored=payload["content"].encode() if encoding=="utf-8" else base64.b64decode(payload["content"],validate=True)
    assert restored==raw and blob(restored)==blob(raw)
    return encoding
refusal={"unsafe_path":0,"protected_path":0,"unsafe_mode":0,"synthetic_roundtrip":0}
for bad in ["web//x","../x","web/../x","/tmp/x","web/x\nx","web/x\\x",".git/config","outputs/x\0"]:
    assert normalize(bad) is None,bad;refusal["unsafe_path"]+=1
for bad in ["planning/a/primary/x.txt","planning/a/primary-private/x.txt","planning/a/primary-cache/x.json","outputs/a/private-pins-v1.json","planning/a/full.pdf"]:
    assert block(bad),bad;refusal["protected_path"]+=1
for mode in ["120000","160000","040000"]:
    try:api_roundtrip(b"formal",mode)
    except AssertionError:refusal["unsafe_mode"]+=1
    else:raise AssertionError(mode)
for raw in [b"",b"literal backslash\\n and dollar$()\n",b"\xff\0\x80","lambda λ literal".encode()]:
    api_roundtrip(raw,"100644");refusal["synthetic_roundtrip"]+=1
for name,row in closure.items():
    p=ROOT/row.get("source_path",name)
    assert not p.is_symlink() and p.resolve().is_relative_to(ROOT)
    assert not any(parent.is_symlink() for parent in p.parents if parent.is_relative_to(ROOT))
    row["type"]="blob";row["API_encoding"]=api_roundtrip(p.read_bytes(),row["mode"])
for name,row in delta.items():
    p=ROOT/row.get("source_path",name);row["type"]="blob";row["API_encoding"]=api_roundtrip(p.read_bytes(),row["mode"])
    if p.suffix in {".md",".tex",".py",".mjs"}:row["header_preview"]=[x[:180] for x in p.read_text().splitlines()[:3]]
# Exact in-memory future Pages comparison to the actual public commit tree.
pages={}
for row in subprocess.check_output(["git","ls-tree","-rz","--full-tree",PAGES],cwd=ROOT,env=ENV).split(b"\0"):
    if row:
        left,name=row.split(b"\t",1);mode,kind,oid=left.decode().split()
        pages[name.decode()]={"mode":mode,"type":kind,"sha":oid}
assert len(pages)==635 and all(x["type"]=="blob" for x in pages.values())
builder=ROOT/"scripts/build_public_site.py"
assert base["scripts/build_public_site.py"]["sha"]==blob(builder.read_bytes()),"Builder changed; separate adapter review needed"
runtime=None
for node in ast.walk(ast.parse(builder.read_text())):
    if isinstance(node,ast.Assign) and any(isinstance(t,ast.Name) and t.id=="runtime" for t in node.targets):
        assert isinstance(node.value,ast.Constant) and isinstance(node.value.value,str);runtime=node.value.value.encode()
assert runtime is not None and blob(runtime)==pages["public-base.js"]["sha"],"Favicon-safe adapter must remain exact"
future={n:dict(v) for n,v in pages.items()};projected={}
def transform(name,raw):
    prefix="/GRH-research/"
    if name.endswith(".html"):
        s=raw.decode().replace("http://127.0.0.1:8765/",prefix)
        s=re.sub(r'''((?:href|src|poster|data-source)=["'])/(?!/|GRH-research/)''',lambda m:m[1]+prefix,s)
        return s.replace("<head>",'<head><script src="'+prefix+'public-base.js"></script>',1).encode()
    if name.endswith(".css"):return re.sub(r'''url\((["']?)/(?!/)''',lambda m:"url("+m[1]+prefix,raw.decode()).encode()
    if name.endswith((".mjs",".js")) and Path(name).name!="public-base.js":return re.sub(r'''(from\s+["']|import\s*["'])/(?!/)''',lambda m:m[1]+prefix,raw.decode()).encode()
    return raw
def project(source,dest,mode="100644"):
    raw=transform(dest,(ROOT/source).read_bytes());obj={"mode":mode,"type":"blob","sha":blob(raw)}
    if future.get(dest)!=obj:
        future[dest]=obj;projected[dest]={"source_path":source,"mode":mode,"type":"blob","bytes":len(raw),"sha256":hashlib.sha256(raw).hexdigest(),"git_blob_sha1":blob(raw),"API_encoding":api_roundtrip(raw,mode),"before":pages.get(dest),"change":"new" if dest not in pages else "modified"}
for name,row in delta.items():
    src=row.get("source_path",name)
    if name.startswith("web/"):project(src,name[4:],row["mode"])
    elif name.startswith("examples/") and Path(name).suffix in {".py",".sage",".md",".json",".mjs",".sv",".v"}:project(src,name,row["mode"])
for rec in exports:project(rec["source"],rec["bundle_path"])
pub=json.loads(subprocess.check_output(["git","show",PAGES+":publication.json"],cwd=ROOT,env=ENV))
pub["byte_identical_data_assets"]+=sum(n not in pages and Path(n).suffix in {".json",".png",".npz",".npy"} for n in future)
pub["files"]=len(future)-1
raw=(json.dumps(pub,indent=2)+"\n").encode()
if blob(raw)!=pages["publication.json"]["sha"]:
    future["publication.json"]={"mode":"100644","type":"blob","sha":blob(raw)}
    projected["publication.json"]={"source_path":"existing builder deterministic manifest","mode":"100644","type":"blob","bytes":len(raw),"sha256":hashlib.sha256(raw).hexdigest(),"git_blob_sha1":blob(raw),"API_encoding":api_roundtrip(raw,"100644"),"before":pages["publication.json"],"change":"modified"}
assert set(pages)<=set(future) and all(future[n]==pages[n] for n in pages if n not in projected)
assert not any(n.startswith(("planning/","outputs/checks/")) for n in projected)
# A focused credential-pattern check covers only selected public bytes.
secret=re.compile(rb"(?:gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|sk-[A-Za-z0-9]{20,}|-----BEGIN (?:OPENSSH |RSA |EC )?PRIVATE KEY-----|https?://[^/\s:@]+:[^@\s/]+@)")
for name,row in delta.items():assert not secret.search((ROOT/row.get("source_path",name)).read_bytes()),("Credential-pattern refusal; content not emitted",name)
projection={"base_commit":PAGES,"baseline_files":len(pages),"future_files":len(future),"changed_count":len(projected),"new_count":sum(x["change"]=="new" for x in projected.values()),"changed_files":projected,"tree_entries":future,"no_deletions":True,"unselected_leaves_unchanged":True,"favicon_runtime_byte_exact":True,"projection_only_no_bundle_build":True}
assert sha(index)==index_before and not TARGET.exists()

report={
 "schema":"ramified-release-explicit-science-selection-v1","status":"PROPOSAL: independent root review BEFORE fresh worktree creation/copy/stage/bundle/API",
 "source":str(ROOT),"target":str(TARGET),"base_commit":BASE,"pages_base_commit":PAGES,
 "entries":delta,"all_named_input_closure":closure,"release_only_metadata_source_aliases":overlay_rows,"public_overlay_authority":{"path":overlay_path,"sha256":sha(ROOT/overlay_path)},"original_metadata_before_guards":{n:x["source_before_sha256"]for n,x in overlay_rows.items()},"projected_pages":projection,"focused_refusal_controls":refusal,"actual_API_roundtrips":{"selected":len(delta),"closure":len(closure)},"credential_pattern_scan":{"selected_files":len(delta),"matches":0},"changed_files":len(delta),"changed_bytes":sum(x["bytes"]for x in delta.values()),
 "new_files":sum(x["change"]=="new"for x in delta.values()),"modified_preexisting_files":sum(x["change"]=="modified"for x in delta.values()),
 "public_exports":exports,"required_public_paths":required,"accepted_staging_artifact_aliases":alias_rows,
 "promotion_receipt":{"path":promotion,"sha256":sha(ROOT/promotion)},
 "source_only_accepted_parent_and_cone_never_Pages":True,"no_recursive_folder_or_history_selection":True,
 "fresh_json_prefixes":[],"current_json_files":[],"excluded_references":excluded,
 "historical_not_current_bindings":historical,"missing_named_paths":missing,
 "held_pending":["Full release QA harness/expectations producer files, after preparation and independent static review"],
 "copied":False,"staged":False,"bundle_built":False,"auth_or_API_actions":False,
 "source_index_bytes_preserved":sha(index)==index_before,"all_git_reads_optional_locks_zero":True,
 "selector_sha256":sha(Path(__file__)),"created_utc":datetime.now(timezone.utc).isoformat(),
}
for name,obj in [("selection-proposal-v1.json",report),
 ("selection-summary-v1.json",{"changed_files":len(delta),"new":report["new_files"],"modified":report["modified_preexisting_files"],
 "changed_bytes":report["changed_bytes"],"closure_files":len(closure),"base_unchanged_dependencies":len(closure)-len(delta),
 "groups":{g:sum(g in x["groups"]for x in closure.values())for g in sorted({g for x in closure.values()for g in x["groups"]})},
 "alias_count":len(alias_rows),"excluded":len(excluded),"historical_bindings":len(historical),"missing":missing,
 "largest_delta":[{"path":n,"bytes":row["bytes"]}for n,row in sorted(delta.items(),key=lambda x:-x[1]["bytes"])[:12]]})]:
    with (out/name).open("x")as f:json.dump(obj,f,indent=2,sort_keys=True);f.write("\n")
print(json.dumps({"draft":str(out/"selection-proposal-v1.json"),"sha256":sha(out/"selection-proposal-v1.json"),
 "changed_files":len(delta),"closure_files":len(closure),"bytes":report["changed_bytes"],
 "excluded":len(excluded),"historical_bindings":len(historical),"missing":missing},indent=2))
