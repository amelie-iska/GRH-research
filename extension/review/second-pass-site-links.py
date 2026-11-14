#!/usr/bin/env python3
"""Check authored static HTML references without contacting external sites.

Uses HTMLParser for element attributes and target IDs. It checks href/src/
poster/data/action and srcset references, resolves directory index documents,
and checks HTML fragments. It does not execute scripts or claim to validate
computed fetch URLs, browser behavior, or external HTTP links.
"""
from datetime import datetime, timezone
from html.parser import HTMLParser
import hashlib
import json
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[2]
SITE = ROOT / "extension/site"


class Page(HTMLParser):
    def __init__(self, path):
        super().__init__(convert_charrefs=True)
        self.ids = set()
        self.refs = []
        self.base = None
        self.feed(path.read_text())

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if attrs.get("id"):
            self.ids.add(attrs["id"])
        if tag == "a" and attrs.get("name"):
            self.ids.add(attrs["name"])
        if tag == "base":
            self.base = attrs.get("href")
            return
        for key in ("href", "src", "poster", "data", "action"):
            if key in attrs and attrs[key] is not None:
                self.refs.append((tag, key, attrs[key], self.getpos()[0]))
        if attrs.get("srcset") and not attrs["srcset"].lstrip().startswith("data:"):
            for item in attrs["srcset"].split(","):
                if item.strip():
                    self.refs.append((tag, "srcset", item.strip().split()[0], self.getpos()[0]))


def main():
    pages = sorted(p for p in SITE.rglob("*.html")
                   if "legacy" not in p.relative_to(SITE).parts
                   and "downloads" not in p.relative_to(SITE).parts)
    parsed = {p: Page(p) for p in pages}
    checks, broken, external = [], [], 0
    for page in pages:
        source = parsed[page]
        if source.base:
            raise ValueError(f"Review base href before checking {page}: {source.base}")
        for tag, attr, raw, line in source.refs:
            parts = urlsplit(raw)
            if parts.scheme or parts.netloc:
                external += 1
                continue
            target_path = unquote(parts.path)
            target = ((SITE / target_path.lstrip("/")) if target_path.startswith("/")
                      else page.parent / target_path).resolve() if target_path else page
            issue = None
            if not target.is_relative_to(SITE.resolve()):
                issue = "target escapes the published site root"
            else:
                if target.is_dir():
                    target = target / "index.html"
                if not target.is_file():
                    issue = "target file does not exist"
                elif parts.fragment and target.suffix.lower() in (".html", ".htm"):
                    if target not in parsed:
                        parsed[target] = Page(target)
                    if unquote(parts.fragment) not in parsed[target].ids:
                        issue = "HTML fragment ID/name does not exist"
            record = {"source": str(page.relative_to(SITE)), "line": line,
                      "element": tag, "attribute": attr, "url": raw,
                      "target": str(target.relative_to(SITE)) if target.is_relative_to(SITE) else str(target),
                      "status": "broken" if issue else "exists"}
            if issue:
                record["issue"] = issue
                broken.append(record)
            checks.append(record)
    output = {
        "checked_at_utc": datetime.now(timezone.utc).isoformat(),
        "method": "HTMLParser attribute/fragment check; no browser or network execution",
        "scope": "All authored HTML pages under extension/site; preserved legacy HTML is excluded as a source, but authored links into it are checked.",
        "limitations": ["No claim about external HTTP availability", "Dynamic JavaScript fetch/import/Worker URLs and CSS url() are outside this HTML-attribute check", "Target existence is not an assertion that a download contains the latest release bytes"],
        "pages": [{"path": str(p.relative_to(SITE)), "sha256": hashlib.sha256(p.read_bytes()).hexdigest()} for p in pages],
        "local_reference_count": len(checks), "external_references_skipped": external,
        "broken_target_count": len(broken), "broken_targets": broken, "checks": checks,
    }
    path = ROOT / "extension/review/second-pass-site-links.json"
    path.write_text(json.dumps(output, indent=2) + "\n")
    print(json.dumps({k: output[k] for k in ("local_reference_count", "external_references_skipped", "broken_target_count", "broken_targets")}, indent=2))
    print("HTML pages:", ", ".join(p.name for p in pages))


if __name__ == "__main__":
    main()
