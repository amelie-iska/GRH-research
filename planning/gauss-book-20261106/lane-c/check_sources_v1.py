#!/usr/bin/env python3
"""Focused source-only guard for the two new shared Gauss-tail fragments."""
from pathlib import Path
from datetime import datetime, timezone
from collections import Counter
import argparse, hashlib, json, re

ROOT = Path(__file__).resolve().parents[3]
FILES = ("papers/gauss-tail-core.tex", "papers/gauss-tail-details.tex")
def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()
def body(text):
    return "\n".join(re.split(r"(?<!\\)%", line, maxsplit=1)[0] for line in text.splitlines())
def balanced(s):
    level = 0
    for i, c in enumerate(s):
        if c not in "{}":
            continue
        nslash = 0
        j = i - 1
        while j >= 0 and s[j] == "\\":
            nslash += 1
            j -= 1
        if nslash % 2:
            continue
        level += 1 if c == "{" else -1
        if level < 0:
            return False
    return level == 0
parser = argparse.ArgumentParser()
parser.add_argument("--output", required=True)
args = parser.parse_args()
texts = {f: body((ROOT/f).read_text()) for f in FILES}
labels = {}
all_labels = Counter()
for p in sorted((ROOT/"papers").glob("*.tex")):
    all_labels.update(re.findall(r"\\label\{([^}]+)\}", body(p.read_text())))
old_core = set()
for p in sorted((ROOT/"papers").glob("*-core.tex")):
    if p.name != "gauss-tail-core.tex":
        old_core.update(re.findall(r"\\label\{([^}]+)\}", body(p.read_text())))
checks = []
def check(name, ok, detail=None):
    checks.append({"name": name, "passed": bool(ok), "detail": detail})
for rel, s in texts.items():
    own = re.findall(r"\\label\{([^}]+)\}", s)
    labels[rel] = own
    check(rel+":balanced-braces", balanced(s))
    check(rel+":namespace", bool(own) and all(x.startswith("gtl:") for x in own))
    check(rel+":no-new-macros-or-wrapper", not re.search(
        r"\\(?:newcommand|renewcommand|providecommand|def|documentclass|usepackage|chapter|input)\b", s))
    check(rel+":only-supported-statement-environments", not re.search(r"\\begin\{(?:lemma|definition|corollary)\}", s))
    check(rel+":all-displays-labelled", "\\[" not in s and "$$" not in s and
          all(re.match(r"\s*\\label\{gtl:[^}]+\}", s[m.end():]) for m in re.finditer(r"\\begin\{equation\}",s)))
    begins = Counter(re.findall(r"\\begin\{([^}]+)\}",s))
    ends = Counter(re.findall(r"\\end\{([^}]+)\}",s))
    check(rel+":balanced-environments", begins == ends, dict(begins))
    heads = list(re.finditer(r"\\(?:section|subsection|subsubsection|paragraph)\*?\{", s))
    for i, m in enumerate(heads):
        stop = heads[i+1].start() if i+1<len(heads) else len(s)
        check(rel+":heading-label-"+str(i+1), bool(re.search(r"\\label\{gtl:[^}]+\}", s[m.end():min(stop,m.end()+250)])))
    for i,m in enumerate(re.finditer(r"\\begin\{(?:theorem|proposition)\}",s)):
        check(rel+":statement-label-"+str(i+1), bool(re.search(r"\\label\{gtl:[^}]+\}",s[m.end():m.end()+180])))
new = [v for vs in labels.values() for v in vs]
check("new-labels-unique-across-project", len(set(new))==len(new) and all(all_labels[x]==1 for x in new), len(new))
available = set(all_labels)
for rel,s in texts.items():
    refs = re.findall(r"\\(?:eqref|ref)\{([^}]+)\}",s)
    check(rel+":all-references-resolve", all(x in available for x in refs), refs)
core_refs = re.findall(r"\\(?:eqref|ref)\{([^}]+)\}",texts[FILES[0]])
check("concise-core-has-no-details-only-reference", all(x in old_core or x in labels[FILES[0]] for x in core_refs))
check("no-book-only-figure-reference", not any("gtl:workflow" in s for s in texts.values()))
report = {
 "schema":"gauss-tail-shared-source-structural-v1",
 "created_utc":datetime.now(timezone.utc).isoformat(),
 "passed":all(x["passed"] for x in checks),
 "files":{rel:{"sha256":digest(ROOT/rel),"bytes":(ROOT/rel).stat().st_size,"labels":labels[rel]} for rel in FILES},
 "checker_sha256":digest(Path(__file__)),
 "checks":checks,
 "mathematical_proof_checker":False,
 "builds_or_old_controls_run":False
}
out = Path(args.output)
out.parent.mkdir(parents=True,exist_ok=True)
with out.open("x") as f:
    json.dump(report,f,indent=2,sort_keys=True);f.write("\n")
print(json.dumps({"passed":report["passed"],"checks":len(checks),"labels":len(new),
                  "report":str(out),"sha256":digest(out),
                  "failures":[x for x in checks if not x["passed"]]},indent=2))
raise SystemExit(0 if report["passed"] else 1)
