from pathlib import Path
from hashlib import sha256
from html import escape
import csv
import io
import json
import re
import shutil
import subprocess

ROOT=Path(__file__).resolve().parents[3]
OUT=ROOT/"outputs/checks/2026-11-09-mid-divisor"
OLD=ROOT/"outputs/checks/2026-11-09-joint-unit-pair"
STAGE=OUT/"metadata-stage-v1"
BUNDLE=OUT/"bundle-v3"

def sha(p):
    return sha256(p.read_bytes()).hexdigest()

def read(p):
    return json.loads(p.read_text())

def ref(p):
    return {"path":str(p.relative_to(ROOT)),"bytes":p.stat().st_size,"sha256":sha(p)}

def write(p,data):
    p.parent.mkdir(exist_ok=True,parents=True)
    with p.open("xb") as h: h.write(data.encode() if isinstance(data,str) else data)

def adapt(value):
    marker='<script src="/GRH-research/public-base.js"></script>'
    assert value.count("<head>")==1 and marker not in value
    value=value.replace("http://127.0.0.1:8765/","/GRH-research/")
    value=re.sub(r"""((?:href|src|poster|data-source)=["'])/(?!/|GRH-research/)""",
        lambda m:m[1]+"/GRH-research/",value)
    return value.replace("<head>","<head>"+marker,1)

def main():
    evidence=OUT/"RESEARCH_ACCEPTED-v2.json"
    accepted=OUT/"INTEGRATION_ACCEPTED-v1.json"
    checkpoint=OUT/"CHECKPOINT-v1.json"
    a=read(accepted)
    assert a["passed"] and read(evidence)["integration"]==ref(accepted)
    c=read(checkpoint)
    assert c["task"]["status"]=="in_progress" and c["task"]["owner"]=="grh-research-loop"
    queue="planning/IMPLEMENTATION_QUEUE.json"
    current=read(ROOT/queue)
    prior=read(OUT/"QUEUE-BEFORE-v1.json")
    assert [y["id"] for x,y in zip(prior["tasks"],current["tasks"],strict=True) if x!=y]==["P7-low-gcd"]
    assert c["task"]==next(x for x in current["tasks"] if x["id"]=="P7-low-gcd")
    assert not current["project_complete"] and not current["research_complete"]
    previous=read(OLD/"metadata-validation-v1.json")["local_postimages"]
    notes=["README.md","planning/MASTER_IMPLEMENTATION_PLAN.md","planning/PROGRESS.md",
       "planning/OPEN_OBLIGATIONS.md","planning/CONTINUATION.md","book/SOURCE_COVERAGE.md","book/VERIFICATION.md"]
    claims="planning/CLAIMS.csv"
    pages=["web/implementation-plan.html","web/verification.html","web/index.html"]
    paths=[*notes,claims,*pages,queue]
    assert all(sha(ROOT/x)==previous[x] for x in [*notes,claims,*pages[:2]])
    candidate=read(OUT/"bundle-v2/CANDIDATE-v1.json")
    assert a["candidate"]==ref(OUT/"bundle-v2/CANDIDATE-v1.json")
    edition=a["edition"]
    assert edition["pages"]==370 and edition["mathml"]==12011
    s=f"""

## 9 November 2026 UTC — joint cutoff edition and middle-divisor research

The 370-page edition has 40 chapters and 12,011 native MathML expressions. The joint cutoff appendix keeps all 11,657 earlier literal expressions and all 14 canonical tools. Focused articles have 90 and 263 pages and the notes have 47 and 152 pages. The reviewed low-divisor pure full-frequency unit-pair estimate reaches target at Nd up to order D^(1/6). The actual selected frequency prefix is D^(15/32) over all d, and all frequency lengths are covered for Nd at least of order D^(27/56), with the actual selected middle subtraction. The equality-wide proof has its separate support thresholds and selected comparable prefix 111/476. Source, builds and browser evidence are bound by {accepted.relative_to(ROOT)}.

Separate new research in {evidence.relative_to(ROOT)} covers selected middle-divisor cross-conjugate overlap, smooth main frequency bands including a good sixth-free selection, and a thin equality product strip. Signed summation over the large common ideal gives explicit subpower cancellation; the fixed 1/16 gap of that upper comparison at the core remains. Low-overlap mid-divisors, sharp main-frequency selections, the whole signed form, determinant/zero-location bridges and analytic/category Lean remain open. P7 checkpoint {c['id']}.
"""
    for name in notes:
        t=(ROOT/name).read_text()
        if name=="README.md":
            old="**Latest verified public edition:** 348 pages and 10,858 native MathML expressions"
            assert t.count(old)==1
            t=t.replace(old,"**Latest verified public edition:** 370 pages and 12,011 native MathML expressions",1)
            t=t.replace("book/main.html#rg:core) or [download","book/main.html#pca:joint-core) or [download",1)
            t=t.replace("The original pure finite TOP prefix has normalized power101/144 under its full stated fixed-data/profile hypotheses. Whole signed13/12/global9/8, the frequency complement, analytic/category Lean and GRH remain open.",
                "The joint cutoff appendix gives scoped full-frequency, selected-mode and equality-wide estimates. The unrestricted signed form, determinant bridge, analytic/category Lean and GRH remain open.",1)
            t=t.replace("Current edition: **303 pages,40 chapters,9,172 MathML expressions and thirteen unique in-book laboratories**.","The physical-sieve edition had **303 pages, 40 chapters, 9,172 MathML expressions and thirteen unique in-book laboratories**.",1)
        write(STAGE/name,t+s)
    text=io.StringIO(newline="")
    csv.writer(text).writerow(["MID_DIVISOR_SELECTED_AND_JOINT_EDITION01",
      "planning/mid-divisor-20261109/lane-c/CROSS_CONJUGATE_CUTOFF-v1.md",
      "Selected middle-divisor, smooth main-frequency and equality-wide estimates",
      "Independently reviewed scoped arithmetic with exact masks and compensation",
      str(evidence.relative_to(ROOT)),
      "Bound the remaining low-overlap, sharp frequency and small-support cells before the absolute divisor comparison"])
    old=(ROOT/claims).read_bytes()
    assert old.endswith(b"\r\n")
    write(STAGE/claims,old+text.getvalue().encode())
    write(STAGE/queue,(ROOT/queue).read_bytes())
    write(STAGE/"web/index.html",(OUT/"bundle-v2/canonical-index.html").read_bytes())
    for f in ("build_implementation_page.py","build_verification_page.py","theme_assets.py"):
        write(STAGE/"scripts"/f,(ROOT/"scripts"/f).read_bytes())
    for f in ("build_implementation_page.py","build_verification_page.py"):
        subprocess.run(["python3","-B",str(STAGE/"scripts"/f)],check=True)
    for page,note in zip(pages[:2],(notes[1],notes[6]),strict=True):
        body=(STAGE/page).read_text().split("<pre>",1)[1].split("</pre>",1)[0]
        assert body==escape((STAGE/note).read_text())
    assert escape(c["task"]["last_result"]) in (STAGE/pages[0]).read_text()
    m={"passed":True,"checkpoint":c["id"],"integration":ref(accepted),"research":ref(evidence),
      "preimages":{x:sha(ROOT/x) for x in paths},"artifacts":{x:ref(STAGE/x) for x in paths}}
    write(STAGE/"receipt-v1.json",json.dumps(m,indent=2)+"\n")
    old_site=OUT/"bundle-v2/site"
    new_site=BUNDLE/"site"
    overlays={name.removeprefix("web/"):adapt((STAGE/name).read_text()).encode() for name in pages[:2]}
    pub=read(old_site/"publication.json")
    assert pub["files"]==648
    pub["files"]=650
    overlays["publication.json"]=(json.dumps(pub,indent=2)+"\n").encode()
    for f in sorted(old_site.rglob("*")):
        if not f.is_file():continue
        name=f.relative_to(old_site).as_posix()
        if name in overlays:continue
        p=new_site/name
        p.parent.mkdir(exist_ok=True,parents=True)
        shutil.copyfile(f,p)
        assert sha(f)==sha(p)
    for name,data in overlays.items():write(new_site/name,data)
    prior_site=ROOT/"outputs/checks/2026-11-08-cutoff-release/bundle/bundle-v1/site"
    prior_hash={p.relative_to(prior_site).as_posix():sha(p) for p in prior_site.rglob("*") if p.is_file()}
    now={p.relative_to(new_site).as_posix():sha(p) for p in new_site.rglob("*") if p.is_file()}
    assert len(prior_hash)==649 and len(now)==651 and set(prior_hash)<=set(now)
    delta={name:ref(new_site/name) for name,digest in now.items() if digest!=prior_hash.get(name)}
    assert set(delta)==set(candidate["overlays"])|set(overlays)
    assert all(delta[name]["sha256"]==item["sha256"] for name,item in candidate["overlays"].items())
    record={"passed":True,"site":str(new_site.relative_to(ROOT)),"metadata":ref(STAGE/"receipt-v1.json"),
      "candidate":ref(OUT/"bundle-v2/CANDIDATE-v1.json"),"overlays":delta,
      "all_files":len(now),"prior_byte_identical":len(set(prior_hash)-set(delta)),"inventory":now}
    write(BUNDLE/"bundle-receipt-v1.json",json.dumps(record,indent=2)+"\n")
    print(json.dumps({"delta":len(delta),"retained":record["prior_byte_identical"],"site":len(now)}))

if __name__=="__main__":main()
