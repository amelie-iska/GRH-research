#!/usr/bin/env python3
"""Build the integrated research companion for a GitHub project Pages prefix.

Only the fresh output directory is written. Scientific records are copied
byte-for-byte; HTML/CSS URL references and module specifiers are adapted in the
output. The inherited runtime adapter is replaced in that output so old root
URLs in immutable JSON records resolve inside the preserved legacy companion.
"""
from __future__ import annotations

import argparse
from dataclasses import dataclass
import hashlib
import html
import json
from pathlib import Path
import re
import shutil
import subprocess
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[2]
TEXT_EXTENSIONS = {".html", ".css", ".js", ".mjs"}
ATTRIBUTE_URL = re.compile(r"(?P<lead>\b(?:href|src|poster|data-source|action)\s*=\s*)(?P<q>[\"'])(?P<url>.*?)(?P=q)", re.I | re.S)
CSS_URL = re.compile(r"(?P<lead>url\(\s*)(?P<q>[\"']?)(?P<url>[^\s)\"']+)(?P=q)(?P<tail>\s*\))", re.I)
SCRIPT_BLOCK = re.compile(r"(<script\b[^>]*>)(.*?)(</script\s*>)", re.I | re.S)
LOOPBACK = "http://127.0.0.1:8765"


@dataclass(frozen=True)
class JSToken:
    kind: str
    value: str
    start: int
    end: int


def javascript_tokens(text: str) -> list[JSToken]:
    """Lex executable tokens without interpreting prose inside strings.

    This is a dependency lexer, not an ECMAScript syntax validator. Strings,
    comments, regexp literals, and complete template literals are atomic. URL
    expressions inside template interpolations remain a rendered-check concern.
    Positions retain the original spelling so rewriting changes only a URL.
    """
    tokens: list[JSToken] = []
    size, index = len(text), 0
    prefix_words = {"return", "throw", "case", "delete", "void", "typeof", "new", "in", "of", "yield", "await", "else", "do"}
    control_words = {"if", "while", "for", "with", "switch", "catch"}
    parens: list[bool] = []
    regex_allowed = True

    def quoted(start: int) -> int:
        quote, i = text[start], start + 1
        while i < size:
            if text[i] == "\\":
                i += 2
            elif text[i] == quote:
                return i + 1
            else:
                i += 1
        raise ValueError(f"Unterminated JavaScript string at character {start}")

    def template(start: int) -> int:
        i = start + 1
        while i < size:
            if text[i] == "\\":
                i += 2
            elif text[i] == "`":
                return i + 1
            elif text.startswith("${", i):
                depth, i = 1, i + 2
                while i < size and depth:
                    if text[i] in "\"'":
                        i = quoted(i)
                    elif text[i] == "`":
                        i = template(i)
                    elif text.startswith("//", i):
                        end = text.find("\n", i + 2)
                        i = size if end < 0 else end
                    elif text.startswith("/*", i):
                        end = text.find("*/", i + 2)
                        if end < 0:
                            raise ValueError("Unterminated JavaScript comment")
                        i = end + 2
                    else:
                        depth += (text[i] == "{") - (text[i] == "}")
                        i += 1
            else:
                i += 1
        raise ValueError(f"Unterminated JavaScript template at character {start}")

    while index < size:
        char = text[index]
        if char.isspace():
            index += 1
            continue
        if text.startswith("//", index):
            end = text.find("\n", index + 2)
            index = size if end < 0 else end
            continue
        if text.startswith("/*", index):
            end = text.find("*/", index + 2)
            if end < 0:
                raise ValueError("Unterminated JavaScript comment")
            index = end + 2
            continue
        start = index
        if char in "\"'":
            index = quoted(start)
            token = JSToken("string", text[start + 1:index - 1], start, index)
        elif char == "`":
            index = template(start)
            token = JSToken("template", text[start + 1:index - 1], start, index)
        elif char.isalpha() or char in "_$":
            index += 1
            while index < size and (text[index].isalnum() or text[index] in "_$"):
                index += 1
            token = JSToken("identifier", text[start:index], start, index)
        elif char.isdigit():
            index += 1
            while index < size and (text[index].isalnum() or text[index] in "._"):
                index += 1
            token = JSToken("number", text[start:index], start, index)
        elif char == "/" and regex_allowed:
            index, in_class = index + 1, False
            while index < size and text[index] not in "\r\n":
                if text[index] == "\\":
                    index += 2
                    continue
                if text[index] == "[":
                    in_class = True
                elif text[index] == "]":
                    in_class = False
                elif text[index] == "/" and not in_class:
                    index += 1
                    while index < size and text[index].isalpha():
                        index += 1
                    break
                index += 1
            token = JSToken("regexp", text[start:index], start, index)
        else:
            index += 1
            if text[start:index + 1] in {"=>", "++", "--", "?."}:
                index += 1
            token = JSToken("punctuation", text[start:index], start, index)
        previous = tokens[-1] if tokens else None
        tokens.append(token)
        if token.value == "(":
            parens.append(bool(previous and previous.kind == "identifier" and previous.value in control_words))
        if token.value == ")":
            regex_allowed = parens.pop() if parens else False
        elif token.kind == "identifier":
            regex_allowed = token.value in prefix_words
        else:
            regex_allowed = token.kind == "punctuation" and token.value not in {"]", "}", "++", "--", ".", "?."}
    return tokens


def javascript_references(text: str) -> list[tuple[str, JSToken]]:
    """Find module specifiers and literal fetch/worker arguments in code tokens.

    An isolated identifier ``from`` is never an import. Only actual import or
    export clauses may contain a from-specifier. A literal prefix of a computed
    argument is tagged dynamic rather than certified as the complete resource.
    """
    tokens, found = javascript_tokens(text), []

    def value(i: int) -> str:
        return tokens[i].value if 0 <= i < len(tokens) else ""

    def literal(i: int, context: str) -> None:
        if i >= len(tokens):
            return
        token = tokens[i]
        if token.kind == "string" or (token.kind == "template" and "${" not in token.value):
            exact = value(i + 1) in {",", ")"} if context != "import" else True
            found.append((context if exact else context + "_dynamic_prefix", token))
        else:
            found.append((context + "_dynamic_argument", token))

    for i, token in enumerate(tokens):
        if token.kind != "identifier":
            continue
        word = token.value
        if word in {"import", "export"} and value(i - 1) not in {".", "?."}:
            if word == "import" and value(i + 1) == "(":
                # Computed import expressions cannot be rewritten as literals.
                before = len(found)
                literal(i + 2, "import")
                if len(found) > before and found[-1][0] == "import" and value(i + 3) not in {",", ")"}:
                    found[-1] = ("import_dynamic_prefix", found[-1][1])
            elif word == "import" and i + 1 < len(tokens) and tokens[i + 1].kind == "string":
                found.append(("import", tokens[i + 1]))
            elif value(i + 1) in {"*", "{"} or (word == "import" and i + 1 < len(tokens) and tokens[i + 1].kind == "identifier"):
                depth, j = 0, i + 1
                while j < len(tokens):
                    current = tokens[j]
                    if current.value in {"{", "[", "("}:
                        depth += 1
                    elif current.value in {"}", "]", ")"}:
                        depth -= 1
                    if depth == 0 and current.kind == "identifier" and current.value == "from":
                        if j + 1 < len(tokens) and tokens[j + 1].kind == "string":
                            found.append(("import", tokens[j + 1]))
                        break
                    if depth < 0 or (depth == 0 and current.value in {";", "="}):
                        break
                    j += 1
        elif word == "fetch" and value(i + 1) == "(" and value(i - 1) not in {".", "?.", "function"}:
            literal(i + 2, "fetch")
        elif word == "importScripts" and value(i + 1) == "(" and value(i - 1) not in {".", "?.", "function"}:
            j = i + 2
            while j < len(tokens) and tokens[j].kind in {"string", "template"}:
                literal(j, "worker")
                if value(j + 1) != ",":
                    break
                j += 2
        elif word in {"Worker", "SharedWorker"} and value(i - 1) == "new" and value(i + 1) == "(":
            j = i + 2
            if value(j) == "new" and value(j + 1) == "URL" and value(j + 2) == "(":
                j += 3
            literal(j, "worker")
    return found


def rewrite_javascript_modules(text: str, base: str, legacy: bool) -> str:
    replacements = []
    for context, token in javascript_references(text):
        if context in {"import", "worker"}:
            mapped = map_url(token.value, base, legacy)
            if mapped != token.value:
                replacements.append((token.start + 1, token.end - 1, mapped))
    for start, end, mapped in reversed(replacements):
        text = text[:start] + mapped + text[end:]
    return text


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def normalize_base(value: str) -> str:
    if not value.startswith("/") or value.startswith("//"):
        raise ValueError("Base path must be an absolute URL path, e.g. /GRH-research/")
    if any(part in {".", ".."} for part in value.split("/")) or re.search(r"[^A-Za-z0-9_./-]", value):
        raise ValueError("Base path contains an unsupported or unsafe character")
    return value.rstrip("/") + "/"


def map_url(value: str, base: str, legacy: bool) -> str:
    """Adapt only known local URLs; external links and relative paths survive."""
    if value == LOOPBACK:
        value = "/"
    elif value.startswith(LOOPBACK + "/"):
        value = value[len(LOOPBACK):]
    elif value.startswith(LOOPBACK + "?") or value.startswith(LOOPBACK + "#"):
        value = "/" + value[len(LOOPBACK):]
    if not value.startswith("/") or value.startswith("//"):
        return value
    path = urlsplit(value).path
    if value.startswith(base) or (base != "/" and path == base.rstrip("/")):
        return value
    if path == "/legacy" or value.startswith("/legacy/"):
        return base + value.lstrip("/")
    return base + ("legacy/" if legacy else "") + value.lstrip("/")


def legacy_runtime(base: str) -> str:
    # Keep one adapter. Stacking the old adapter would corrupt already-prefixed
    # URLs, so this replaces only the output copy of legacy/legacy-base.js.
    template = r'''// Generated project-prefix adapter. Recorded scientific data is unchanged.
(() => {
  'use strict';
  if (window.__grhLegacyBase) return;
  window.__grhLegacyBase = true;
  const projectBase = __BASE__;
  const legacyBase = projectBase + 'legacy/';
  const loopback = 'http://127.0.0.1:8765';
  const map = value => {
    if (typeof value !== 'string') return value;
    if (value === loopback) value = '/';
    else if (value.startsWith(loopback + '/')) value = value.slice(loopback.length);
    else if (value.startsWith(loopback + '?') || value.startsWith(loopback + '#')) value = '/' + value.slice(loopback.length);
    else if (value.startsWith(location.origin + '/')) value = value.slice(location.origin.length);
    if (!value.startsWith('/') || value.startsWith('//')) return value;
    if (value.startsWith(projectBase)) return value;
    if (value === projectBase.slice(0, -1) || value.startsWith(projectBase.slice(0, -1) + '?') || value.startsWith(projectBase.slice(0, -1) + '#')) return value;
    if (value === '/legacy' || value.startsWith('/legacy?') || value.startsWith('/legacy#') || value.startsWith('/legacy/')) return projectBase + value.slice(1);
    return legacyBase + value.slice(1);
  };
  Object.defineProperty(window, '__grhLegacyURLMap', { value: map });
  const nativeFetch = window.fetch.bind(window);
  window.fetch = (input, init) => nativeFetch(
    typeof input === 'string' ? map(input) :
    input instanceof URL ? new URL(map(input.href), location.origin) :
    input instanceof Request ? new Request(new URL(map(input.url), location.origin), input) : input, init);
  const properties = [[HTMLAnchorElement, 'href'], [HTMLImageElement, 'src'],
    [HTMLIFrameElement, 'src'], [HTMLMediaElement, 'src'], [HTMLSourceElement, 'src'],
    [HTMLVideoElement, 'poster'], [HTMLLinkElement, 'href'], [HTMLScriptElement, 'src']];
  for (const [type, key] of properties) {
    const descriptor = Object.getOwnPropertyDescriptor(type.prototype, key);
    if (descriptor && descriptor.set) Object.defineProperty(type.prototype, key,
      { ...descriptor, set(value) { descriptor.set.call(this, map(value)); } });
  }
  const attributes = ['href', 'src', 'poster', 'data-source'];
  const nativeSetAttribute = Element.prototype.setAttribute;
  Element.prototype.setAttribute = function (key, value) {
    return nativeSetAttribute.call(this, key, attributes.includes(key.toLowerCase()) ? map(value) : value);
  };
  const patch = node => {
    if (node.nodeType !== 1) return;
    for (const element of [node, ...node.querySelectorAll('[href],[src],[poster],[data-source]')]) {
      for (const key of attributes) {
        const value = element.getAttribute(key), mapped = map(value);
        if (value && mapped !== value) nativeSetAttribute.call(element, key, mapped);
      }
    }
  };
  new MutationObserver(records => records.forEach(record => record.type === 'attributes'
    ? patch(record.target) : record.addedNodes.forEach(patch)))
    .observe(document.documentElement, { subtree: true, childList: true,
      attributes: true, attributeFilter: attributes });
})();
'''
    return template.replace("__BASE__", json.dumps(base))


def redirect_document(target: str) -> str:
    escaped = html.escape(target, quote=True)
    return ("<!doctype html>\n<html lang=\"en\"><head><meta charset=\"utf-8\">"
            "<meta name=\"viewport\" content=\"width=device-width,initial-scale=1\">"
            "<title>Research page moved</title>"
            f'<link rel="canonical" href="{escaped}">'
            f'<meta http-equiv="refresh" content="0;url={escaped}">'
            "</head><body>"
            f'<p>This research page is preserved at <a href="{escaped}">{escaped}</a>.</p>'
            f'<script>location.replace({json.dumps(target)} + location.search + location.hash);</script>'
            "</body></html>\n")


def git_metadata(source: Path) -> dict:
    try:
        revision = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=source, text=True, stderr=subprocess.DEVNULL).strip()
        dirty = bool(subprocess.check_output(["git", "status", "--porcelain"], cwd=source, text=True, stderr=subprocess.DEVNULL).strip())
        return {"revision": revision, "working_tree_dirty_at_build": dirty}
    except (subprocess.CalledProcessError, FileNotFoundError):
        return {"revision": None, "working_tree_dirty_at_build": None}


def build(source: Path, output: Path, base: str, aliases: bool = True) -> dict:
    source, output = source.resolve(), output.resolve()
    base = normalize_base(base)
    if not source.is_dir() or not (source / "index.html").is_file():
        raise ValueError("Source must be the prepared extension/site directory")
    if output == source or source in output.parents:
        raise ValueError("Output must be outside the source site")
    if output.exists():
        raise FileExistsError("Use a fresh output directory; existing bundles are never overwritten")
    source_paths = sorted(p for p in source.rglob("*") if p.is_file())
    if any(p.is_symlink() or source not in p.resolve().parents for p in source_paths):
        raise ValueError("Symlinks and paths escaping the source are not published")
    before = {p.relative_to(source).as_posix(): digest(p) for p in source_paths}
    output.mkdir(parents=True)
    records, transformed = [], []
    for p in source_paths:
        rel = p.relative_to(source)
        target = output / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(p, target)
        legacy = rel.parts[0] == "legacy"
        if rel.as_posix() == "legacy/legacy-base.js":
            target.write_text(legacy_runtime(base), encoding="utf-8")
        elif p.suffix in TEXT_EXTENSIONS:
            text = p.read_text(encoding="utf-8")
            if p.suffix == ".html":
                text = ATTRIBUTE_URL.sub(lambda m: m["lead"] + m["q"] + html.escape(map_url(html.unescape(m["url"]), base, legacy), quote=True).replace("&#x27;", "'" if m["q"] == '"' else "&#x27;") + m["q"], text)
            if p.suffix in {".html", ".css"}:
                text = CSS_URL.sub(lambda m: m["lead"] + m["q"] + map_url(m["url"], base, legacy) + m["q"] + m["tail"], text)
            if p.suffix in {".js", ".mjs"}:
                text = rewrite_javascript_modules(text, base, legacy)
            elif p.suffix == ".html":
                text = SCRIPT_BLOCK.sub(lambda m: m[1] + rewrite_javascript_modules(m[2], base, legacy) + m[3], text)
            target.write_text(text, encoding="utf-8")
        out_hash = digest(target)
        changed = out_hash != before[rel.as_posix()]
        if changed:
            transformed.append(rel.as_posix())
        if p.suffix not in TEXT_EXTENSIONS and changed:
            raise RuntimeError(f"Scientific/download asset changed: {rel}")
        records.append({"path": rel.as_posix(), "source_sha256": before[rel.as_posix()], "published_sha256": out_hash, "bytes": target.stat().st_size, "transformed": changed})
    compatibility, collisions = [], []
    if aliases:
        for p in sorted((output / "legacy").rglob("*")):
            if not p.is_file():
                continue
            rel = p.relative_to(output / "legacy")
            target = output / rel
            if target.exists():
                collisions.append(rel.as_posix())
                continue
            target.parent.mkdir(parents=True, exist_ok=True)
            if p.suffix == ".html":
                destination = base + "legacy/" + rel.as_posix()
                target.write_text(redirect_document(destination), encoding="utf-8")
                compatibility.append({"path": rel.as_posix(), "target": destination, "kind": "html_redirect_query_hash_preserved"})
            else:
                shutil.copyfile(p, target)
                compatibility.append({"path": rel.as_posix(), "target": "legacy/" + rel.as_posix(), "kind": "byte_identical_asset_alias", "sha256": digest(target)})
    (output / ".nojekyll").touch()
    if before != {p.relative_to(source).as_posix(): digest(p) for p in source_paths}:
        raise RuntimeError("Source changed during build; inspect this bundle and rerun into a fresh directory")
    if sorted(before) != sorted(p.relative_to(source).as_posix() for p in source.rglob("*") if p.is_file()):
        raise RuntimeError("Source file inventory changed during build; rerun after editing completes")
    manifest = {"schema_version": 1, "base_path": base, "source": git_metadata(source), "source_files": records, "transformed_text_files": transformed, "unchanged_source_files": sum(not x["transformed"] for x in records), "byte_identical_json_files": sum(x["path"].endswith(".json") and not x["transformed"] for x in records), "source_unchanged": True, "compatibility": compatibility, "compatibility_collisions_kept_new": collisions, "scope": "Project-prefix transport adaptation only. Data hashes and numerical content are unchanged. Original root index and any conflicting new assets take precedence; legacy originals remain under legacy/."}
    (output / "publication.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    return manifest


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=ROOT / "extension/site")
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--base", default="/GRH-research/")
    parser.add_argument("--no-compatibility-aliases", action="store_true")
    args = parser.parse_args()
    result = build(args.source, args.output, args.base, not args.no_compatibility_aliases)
    print(json.dumps({"output": str(args.output.resolve()), "base_path": result["base_path"], "source_files": len(result["source_files"]), "byte_identical_json_files": result["byte_identical_json_files"], "compatibility_entries": len(result["compatibility"]), "collisions": result["compatibility_collisions_kept_new"]}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
