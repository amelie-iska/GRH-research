#!/usr/bin/env python3
"""Check a built Pages bundle: local URL closure, hashes, and adapter behavior.

This is a static plus isolated JavaScript contract check, not a rendered-browser
or scientific correctness test. Downloadable example scripts are not mistaken
for page entrypoints: only scripts referenced by HTML and their imports run
through the runtime dependency closure.
"""
from __future__ import annotations

import argparse
from collections import deque
import hashlib
import html
from html.parser import HTMLParser
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
from urllib.parse import unquote, urljoin, urlsplit

from build_github_pages import javascript_references, rewrite_javascript_modules

ORIGIN = "https://pages.invalid"
LINK_ATTRIBUTES = {"href", "src", "poster", "data-source", "action"}
CSS_URLS = re.compile(r'''url\(\s*["']?([^\s)"']+)["']?\s*\)''', re.I)


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


class Document(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.links, self.scripts, self.ids, self.inline = [], [], set(), []
        self.inside_script = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        for key, value in attrs.items():
            if key in LINK_ATTRIBUTES and value:
                self.links.append((tag, key, value))
            if key == "id" and value:
                self.ids.add(value)
        if tag == "a" and attrs.get("name"):
            self.ids.add(attrs["name"])
        if tag == "script":
            self.inside_script = not attrs.get("src") and attrs.get("type", "").lower() in {"", "module", "text/javascript", "application/javascript"}
            if attrs.get("src"):
                self.scripts.append(attrs["src"])

    def handle_endtag(self, tag):
        if tag == "script":
            self.inside_script = False

    def handle_data(self, data):
        if self.inside_script:
            self.inline.append(data)


def legacy_map(value: str, base: str) -> str:
    # Resolve recorded manifest URLs for the checker. The JavaScript adapter is
    # tested independently below, including the already-prefixed regression.
    loopback = "http://127.0.0.1:8765"
    if value == loopback:
        value = "/"
    elif value.startswith(loopback + "/"):
        value = value[len(loopback):]
    elif value.startswith(loopback + "?") or value.startswith(loopback + "#"):
        value = "/" + value[len(loopback):]
    if value.startswith(ORIGIN + "/"):
        value = value[len(ORIGIN):]
    if not value.startswith("/") or value.startswith("//") or value.startswith(base) or urlsplit(value).path == base.rstrip("/"):
        return value
    path = urlsplit(value).path
    return base + ("" if path == "/legacy" or path.startswith("/legacy/") else "legacy/") + value.lstrip("/")


def dependency_lexer_check() -> dict:
    """Regression contract for real dependencies versus strings and comments."""
    source = r'''
import {name as alias} from '/module.mjs?version=1#part';
import '/side-effect.mjs';
export {name} from '/exports.mjs';
export * as all from './all.mjs';
const module = import('/dynamic.mjs');
// import '/comment.mjs'; fetch('/comment.json');
/* export * from '/block-comment.mjs'; */
const prose = "import '/string.mjs' and from '/also-string.mjs'";
const field = state[name === 'source' ? 'from' : 'to'];
const object = {from: '/property.json'};
const template = `from '/template.mjs' ${`nested ${'from'}`}`;
const pattern = /import 'decoy.mjs' from 'another.mjs'/;
if (flag) /from 'regexp.mjs'/.test(prose);
fetch('/data.json?mode=small#record');
fetch('/data/' + name);
fetch(item.path);
new Worker(new URL('/worker.js', import.meta.url));
new SharedWorker('./shared.js');
importScripts('/one.js', '/two.js');
const computed = import('./parts/' + name);
'''
    expected = [
        ("import", "/module.mjs?version=1#part"), ("import", "/side-effect.mjs"),
        ("import", "/exports.mjs"), ("import", "./all.mjs"), ("import", "/dynamic.mjs"),
        ("fetch", "/data.json?mode=small#record"), ("fetch_dynamic_prefix", "/data/"),
        ("fetch_dynamic_argument", "item"), ("worker", "/worker.js"),
        ("worker", "./shared.js"), ("worker", "/one.js"), ("worker", "/two.js"),
        ("import_dynamic_prefix", "./parts/"),
    ]
    actual = [(context, token.value) for context, token in javascript_references(source)]
    if actual != expected:
        return {"status": "failed", "expected": expected, "actual": actual}
    rewritten = rewrite_javascript_modules(source, "/GRH-research/", True)
    for old, new in [("/module.mjs?version=1#part", "/GRH-research/legacy/module.mjs?version=1#part"), ("/worker.js", "/GRH-research/legacy/worker.js")]:
        if new not in rewritten:
            return {"status": "failed", "reason": "literal_rewrite_missing", "url": old}
    for decoy in ["/string.mjs", "/also-string.mjs", "/comment.mjs", "/template.mjs", "/property.json"]:
        if "/GRH-research/legacy" + decoy in rewritten:
            return {"status": "failed", "reason": "noncode_literal_rewritten", "url": decoy}
    return {"status": "passed", "literal_references": sum("dynamic" not in k for k, _ in actual), "dynamic_calls_explicitly_reported": sum("dynamic" in k for k, _ in actual), "string_comment_template_regexp_decoys_ignored": True, "query_fragment_retained": True}


def adapter_check(bundle: Path, base: str) -> dict:
    node = os.environ.get("CODEX_PRIMARY_RUNTIME_NODE") or shutil.which("node")
    if not node:
        return {"status": "failed", "error": "Node unavailable; adapter behavior was not checked"}
    harness = r'''
const fs=require('node:fs'),vm=require('node:vm'),assert=require('node:assert/strict');
const [adapter,base]=process.argv.slice(1),legacy=base+'legacy/',origin='https://pages.invalid';
class Element { constructor(){this.attrs={};this.nodeType=1;} setAttribute(k,v){this.attrs[k]=v;} getAttribute(k){return this.attrs[k]??null;} querySelectorAll(){return [];} }
const ctx={URL,Request,location:{origin},document:{documentElement:new Element()},Element,
  MutationObserver:class {observe(){}},fetch:(input,init)=>Promise.resolve({input,init})};
for(const name of ['HTMLAnchorElement','HTMLImageElement','HTMLIFrameElement','HTMLMediaElement','HTMLSourceElement','HTMLVideoElement','HTMLLinkElement','HTMLScriptElement']){
  const C=class extends Element{};
  for(const key of ['href','src','poster'])Object.defineProperty(C.prototype,key,{configurable:true,get(){return this.attrs[key];},set(v){this.attrs[key]=v;}});
  ctx[name]=C;
}
ctx.window=ctx;vm.createContext(ctx);vm.runInContext(fs.readFileSync(adapter,'utf8'),ctx);
const cases=[
 ['/legacy/data/rg/lab.json',legacy+'data/rg/lab.json'],
 ['/data/rg/lab.json',legacy+'data/rg/lab.json'],
 [legacy+'data/rg/lab.json',legacy+'data/rg/lab.json'],
 [origin+legacy+'data/rg/lab.json',legacy+'data/rg/lab.json'],
 ['http://127.0.0.1:8765/data/rg/lab.json',legacy+'data/rg/lab.json'],
 ['/legacy/architecture.html?collection=qtoken#tensor',legacy+'architecture.html?collection=qtoken#tensor'],
 ['data/training.json','data/training.json'],
 ['https://other.example/data/file.json','https://other.example/data/file.json'],
 ['//other.example/data/file.json','//other.example/data/file.json'],
 [base+'fluids.html',base+'fluids.html'],
 ['#reading','#reading'],['/legacy',base+'legacy'],
 ['/legacy?tab=proof#reading',base+'legacy?tab=proof#reading'],
 ['/architecture.html?collection=qtoken#tensor',legacy+'architecture.html?collection=qtoken#tensor'],
 [base+'downloads/paper.pdf#page=2',base+'downloads/paper.pdf#page=2'],
 [base.slice(0,-1)+'?mode=review#reading',base.slice(0,-1)+'?mode=review#reading'],
 ['http://127.0.0.1:8765?mode=review#reading',legacy+'?mode=review#reading']
];
(async()=>{
 for(const [input,want]of cases){assert.equal(ctx.__grhLegacyURLMap(input),want,input);assert.equal(ctx.__grhLegacyURLMap(want),want,'idempotence: '+input);}
 const response=await ctx.fetch(new URL(origin+'/data/rg/lab.json'));assert.equal(response.input.href,origin+legacy+'data/rg/lab.json');
 const request=new Request(origin+'/data/rg/lab.json',{method:'POST',headers:{'X-Research':'check'},body:'payload'});
 const wrapped=await ctx.fetch(request);assert.equal(wrapped.input.url,origin+legacy+'data/rg/lab.json');assert.equal(wrapped.input.method,'POST');assert.equal(wrapped.input.headers.get('X-Research'),'check');assert.equal(await wrapped.input.text(),'payload');
 const anchor=new ctx.HTMLAnchorElement();anchor.href='/legacy/architecture.html';assert.equal(anchor.href,legacy+'architecture.html');
 anchor.setAttribute('href','/data/rg/lab.json');assert.equal(anchor.getAttribute('href'),legacy+'data/rg/lab.json');
 process.stdout.write(JSON.stringify({status:'passed',mapping_cases:cases.length,idempotence_cases:cases.length,fetch_url_request_and_dom_contracts:4}));
})().catch(e=>{console.error(e);process.exitCode=1;});
'''
    result = subprocess.run([node, "-e", harness, str(bundle / "legacy/legacy-base.js"), base], text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=30)
    if result.returncode:
        return {"status": "failed", "exit_code": result.returncode, "error": result.stderr[-6000:]}
    return json.loads(result.stdout)


def check(bundle: Path) -> dict:
    bundle = bundle.resolve()
    manifest = json.loads((bundle / "publication.json").read_text())
    base = manifest["base_path"]
    errors, warnings, checked, external = [], [], set(), set()
    documents = {}
    for p in bundle.rglob("*.html"):
        d = Document()
        d.feed(p.read_text(encoding="utf-8"))
        documents[p.relative_to(bundle).as_posix()] = d
    aliases = {x["path"] for x in manifest["compatibility"]}

    def resolve(value: str, owner: str, context: str, legacy_runtime: bool = False, fragments: bool = True):
        value = html.unescape(value.strip())
        if not value or value.startswith(("data:", "blob:", "mailto:", "tel:", "javascript:")):
            return None
        if "${" in value or "\\" in value:
            warnings.append({"owner": owner, "url": value, "context": context, "reason": "dynamic_or_escaped_literal_not_statically_resolved"})
            return None
        if legacy_runtime:
            value = legacy_map(value, base)
        parsed = urlsplit(urljoin(ORIGIN + base + owner, value))
        if parsed.netloc != "pages.invalid":
            external.add(parsed.scheme + "://" + parsed.netloc)
            return None
        if not parsed.path.startswith(base):
            errors.append({"owner": owner, "url": value, "context": context, "reason": "escapes_project_prefix"})
            return None
        rel = unquote(parsed.path[len(base):])
        target = (bundle / rel).resolve()
        if target != bundle and bundle not in target.parents:
            errors.append({"owner": owner, "url": value, "context": context, "reason": "escapes_publication_directory"})
            return None
        if target.is_dir():
            if context == "fetch" and value.endswith("/"):
                checked.add((owner, value, context));return rel
            target = target / "index.html"
            rel = target.relative_to(bundle).as_posix()
        if not target.is_file():
            errors.append({"owner": owner, "url": value, "context": context, "reason": "missing_local_target", "target": rel})
            return None
        checked.add((owner, value, context))
        if fragments and parsed.fragment and rel in documents and rel not in aliases:
            fragment = unquote(parsed.fragment)
            if fragment not in documents[rel].ids:
                errors.append({"owner": owner, "url": value, "context": context, "reason": "missing_html_fragment", "target": rel, "fragment": fragment})
        return rel

    queue = deque()

    def inspect_javascript(text: str, rel: str) -> None:
        try:
            references = javascript_references(text)
        except ValueError as exc:
            errors.append({"owner": rel, "reason": "javascript_dependency_lexing_failed", "detail": str(exc)})
            return
        for context, token in references:
            if "_dynamic_" in context:
                warnings.append({"owner": rel, "url": token.value, "context": context, "reason": "computed_resource_requires_runtime_or_manifest_validation"})
                continue
            if token.value.startswith("node:"):
                continue
            target = resolve(token.value, rel, context, legacy_runtime=context == "fetch" and rel.startswith("legacy/"))
            if target and context != "fetch":
                queue.append(target)

    for rel, d in documents.items():
        for tag, attr, value in d.links:
            target = resolve(value, rel, f"{tag}.{attr}")
            if tag == "script" and attr == "src" and target:
                queue.append(target)
        for text in d.inline:
            inspect_javascript(text, rel)
    for p in bundle.rglob("*.css"):
        rel = p.relative_to(bundle).as_posix()
        for m in CSS_URLS.finditer(p.read_text()):
            resolve(m[1], rel, "css.url")
    visited = set()
    while queue:
        rel = queue.popleft()
        if rel in visited:
            continue
        visited.add(rel)
        text = (bundle / rel).read_text(encoding="utf-8")
        inspect_javascript(text, rel)
    hash_checks = 0
    for entry in manifest["source_files"]:
        p = bundle / entry["path"]
        if not p.is_file() or digest(p) != entry["published_sha256"]:
            errors.append({"owner": "publication.json", "target": entry["path"], "reason": "published_hash_mismatch"})
        elif p.suffix == ".json":
            hash_checks += 1
            if entry["source_sha256"] != entry["published_sha256"]:
                errors.append({"target": entry["path"], "reason": "numerical_json_changed"})
    for entry in manifest["compatibility"]:
        p = bundle / entry["path"]
        if entry["kind"] == "byte_identical_asset_alias" and digest(p) != digest(bundle / entry["target"]):
            errors.append({"target": entry["path"], "reason": "legacy_asset_alias_hash_mismatch"})
        elif entry["kind"].startswith("html_redirect"):
            text = p.read_text()
            if "location.search + location.hash" not in text or entry["target"] not in text:
                errors.append({"target": entry["path"], "reason": "legacy_redirect_loses_state"})
            resolve(entry["target"], entry["path"], "compatibility_redirect")
    adapter = adapter_check(bundle, base)
    if adapter["status"] != "passed":
        errors.append({"reason": "runtime_adapter_contract_failed", "details": adapter})
    lexer = dependency_lexer_check()
    if lexer["status"] != "passed":
        errors.append({"reason": "dependency_lexer_contract_failed", "details": lexer})
    return {"schema_version": 2, "status": "passed" if not errors else "failed", "base_path": base, "html_documents": len(documents), "runtime_script_closure": sorted(visited), "checked_local_references": len(checked), "byte_identical_json_files_checked": hash_checks, "compatibility_entries_checked": len(manifest["compatibility"]), "external_origins_not_network_checked": sorted(external), "adapter_contract": adapter, "dependency_lexer_contract": lexer, "errors": errors, "warnings": warnings, "publication_manifest_sha256": digest(bundle / "publication.json"), "scope": "Static local link/fragment and literal executable-script dependency closure, source-record and alias hashes, and isolated JavaScript adapter contracts. Computed resources are reported separately; expressions inside template interpolation are not dependency-parsed. No rendered-browser interaction, external URL availability, mathematical proof, or numerical algorithm accuracy is implied."}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--site", type=Path, required=True)
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()
    report = check(args.site)
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({k: report[k] for k in ["status", "base_path", "html_documents", "checked_local_references", "byte_identical_json_files_checked", "compatibility_entries_checked", "adapter_contract"]}, indent=2))
    if report["errors"]:
        print(json.dumps(report["errors"][:30], indent=2))
    return 0 if report["status"] == "passed" else 1


if __name__ == "__main__":
    raise SystemExit(main())
