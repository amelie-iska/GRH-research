from pathlib import Path
import argparse
import hashlib
import json
import re
import shutil

ROOT=Path(__file__).resolve().parents[2]
SOURCE=ROOT/"outputs/checks/2026-11-08-cutoff-appendix"
NEW=ROOT/"outputs/checks/2026-11-08-cutoff-release"
NOTES=Path(__file__).resolve().parent

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def write(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("xb") as handle:
        handle.write(value.encode() if isinstance(value,str) else value)

def replace_once(text, before, after):
    assert text.count(before)==1,before
    return text.replace(before,after,1)

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--attempt",required=True)
    p.add_argument("--wide-core-sha",required=True)
    p.add_argument("--wide-details-sha",required=True)
    a=p.parse_args()
    assert re.fullmatch(r"stage-v[1-9][0-9]*",a.attempt)
    accept=SOURCE/"STAGE_ACCEPTED-v1.json"
    assert sha(accept)=="2afc788f3b599a580d2b159bbd4996be9537e93d9c24f387c71ec7116261459c"
    old_accept=json.loads(accept.read_text())
    manifest=ROOT/old_accept["source_stage"]["path"]
    assert sha(manifest)==old_accept["source_stage"]["sha256"]
    old=json.loads(manifest.read_text())
    base=manifest.parent/"inputs"
    wide={"core":a.wide_core_sha,"details":a.wide_details_sha}
    for kind,digest in wide.items():
        assert sha(NOTES/f"wide-cutoff-{kind}.tex")==digest
    for rel, digest in old["source_input_sha256"].items():
        assert sha(ROOT/rel)==digest,(rel,"Concurrent source change")
    for name in ("PDF-MARKER-stdout-v1.txt","CLAIM-v1.json"):
        assert (NEW/name).is_file()
    run=NEW/a.attempt
    run.mkdir()
    stage=run/"inputs"
    old_files={rel:next((row["stage_sha256"] for row in old["wrappers"] if row["path"]==rel),digest)
               for rel,digest in old["source_input_sha256"].items()}
    old_files.update({rel:row["sha256"] for rel,row in old["additions"].items()})
    old_files.update({name:sha(base/name) for name in (
        "native-baseline.json","figure-gate.json","scripts/build_cutoff_book.py","scripts/render_cutoff_native.py")})
    assert len(old_files)==528
    for rel,digest in old_files.items():
        assert sha(base/rel)==digest,(rel,"Accepted staging changed")
        write(stage/rel,(base/rel).read_bytes())
    for rel in ("papers","book/chapters"):
        for kind in wide:
            file=f"wide-cutoff-{kind}.tex"
            write(stage/rel/file,(NOTES/file).read_bytes())
    wrappers=[row["path"] for row in old["wrappers"]]
    for rel in wrappers:
        file=stage/rel
        content=file.read_text()
        if rel.startswith("book/"):
            marker=r"\input{chapters/paired-cutoff-details}"+"\n"
            add=r"\input{chapters/wide-cutoff-core}"+"\n"+r"\input{chapters/wide-cutoff-details}"+"\n"
        elif rel.endswith("-extended.tex"):
            marker=r"\input{paired-cutoff-details}"+"\n"
            add=r"\input{wide-cutoff-core}"+"\n"+r"\input{wide-cutoff-details}"+"\n"
        else:
            marker=r"\input{paired-cutoff-core}"+"\n"
            add=r"\input{wide-cutoff-core}"+"\n"
        file.write_text(replace_once(content,marker,marker+add))
    name="scripts/render_cutoff_native.py"
    renderer=(stage/name).read_text()
    renderer=replace_once(renderer,'names=["book/chapters/paired-cutoff-core.tex","book/chapters/paired-cutoff-figure.tex","book/chapters/paired-cutoff-details.tex"]',
        'names=["book/chapters/paired-cutoff-core.tex","book/chapters/paired-cutoff-figure.tex","book/chapters/paired-cutoff-details.tex","book/chapters/wide-cutoff-core.tex","book/chapters/wide-cutoff-details.tex"]')
    renderer=replace_once(renderer,'The dashed curve depends on fixed residual labels.',
        'The dotted curve depends on fixed residual labels.')
    renderer=replace_once(renderer,' · <a href="#pca:details">Complete proofs</a>',
        ' · <a href="#pca:details">Complete proofs</a> · <a href="#pca:wide-core">Wide correction</a>')
    assert "output only" in renderer
    (stage/name).write_text(renderer)
    path="scripts/build_cutoff_book.py"
    book=(stage/path).read_text()
    (stage/path).write_text(replace_once(book,"new_reviewed_sections=(2 if args.consume_book else 0)","new_reviewed_sections=(4 if args.consume_book else 0)"))
    allowed=set(wrappers)|{name,path}
    assert all(sha(stage/rel)==digest for rel,digest in old_files.items() if rel not in allowed)
    record={
        "passed":True,"previous_stage_acceptance_sha256":sha(accept),
        "old_source_inventory_sha256":sha(manifest),"previous_stage_input_sha256":old_files,
        "staged_input_sha256":{str(f.relative_to(stage)):sha(f) for f in sorted(stage.rglob("*")) if f.is_file()},
        "wrappers":wrappers,"wide_sha256":wide,"producer_sha256":sha(Path(__file__)),
        "new_native_alt":"Conditional fixed-label curve described as dotted",
        "isolated":True,"canonical_promoted":False,
    }
    write(run/"source-stage-v1.json",json.dumps(record,indent=2)+"\n")
    print(stage)

if __name__=="__main__":
    main()
