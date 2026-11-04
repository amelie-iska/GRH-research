"""Offline structural and cross-artifact integrity check; no network access."""
import hashlib
import json
from pathlib import Path
import re


def require(value, message):
    if not value:
        raise ValueError(message)


def run():
    here = Path(__file__).resolve().parent
    root = here.parents[2]
    source = json.loads((here / "sources-2026-11-04.json").read_text())
    papers = json.loads((here / "papers-2026-11-04.json").read_text())
    repos = source["sources"]
    require(len(repos) == 20, "expected twenty resolved repository records")
    require(len({r["repository"] for r in repos}) == len(repos), "duplicate repository")
    count = 0
    for repo in repos:
        require(re.fullmatch(r"[0-9a-f]{40}", repo["commit"]), "invalid commit pin")
        require(repo["documents"], "missing reviewed document")
        require(repo["retrieved_at_utc"], "missing retrieval time")
        for doc in repo["documents"]:
            require(repo["commit"] in doc["url"] and repo["commit"] in doc["raw_url"],
                    "mutable document URL")
            require(re.fullmatch(r"[0-9a-f]{64}", doc["sha256"]), "invalid digest")
            first, last = doc["reviewed_lines"]
            require(1 <= first <= last <= doc["total_lines"], "invalid review range")
            count += 1
    require(len(papers["papers"]) == 13, "expected thirteen primary paper records")
    for paper in papers["papers"]:
        require(paper["title"] and paper["retrieved_at_utc"] and
                paper["version_url"].endswith("v" + str(paper["version"])),
                "missing versioned paper metadata")
    evidence = root / "examples/learned_frontier/hardware/evidence-2026-11-04.json"
    saved = json.loads(evidence.read_text())
    require(saved["status"] == "pass", "reference evidence did not pass")
    require(all(saved["negative_controls_detected"].values()), "undetected negative control")
    for name, digest in saved["source_sha256"].items():
        actual = hashlib.sha256((evidence.parent / name).read_bytes()).hexdigest()
        require(actual == digest, "saved evidence source mismatch: " + name)
    local_links = 0
    for doc in list(here.glob("*.md")) + [evidence.parent / "README.md"]:
        for link in re.findall(r"\]\(([^)]+)\)", doc.read_text()):
            if "://" not in link and not link.startswith("#"):
                require((doc.parent / link.split("#", 1)[0]).exists(), "broken local link: " + link)
                local_links += 1
    return {"status": "pass", "repositories": len(repos), "documents": count,
            "primary_papers": len(papers["papers"]), "local_links": local_links,
            "reference_source_hashes_match": True,
            "scope": "offline artifact integrity; upstream claims not reproduced"}


if __name__ == "__main__":
    print(json.dumps(run(), indent=2))
