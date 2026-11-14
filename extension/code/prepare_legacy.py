#!/usr/bin/env python3
"""Reproduce the inherited public companion under /legacy/ without editing web/.

The publication recipe in scripts/build_public_site.py supplies PDF aliases,
examples, original Lean sources, and a TeX download in addition to web/. Saved
scientific records remain byte-identical. One oversized JSON is delivered as a
lossless gzip with its specific loader patched. All served files are <=25 MiB.
"""
from __future__ import annotations

import gzip
import hashlib
from html.parser import HTMLParser
import json
from pathlib import Path
import posixpath
import re
import subprocess
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / 'web'
DEST = ROOT / 'extension/site/legacy'
REVIEW = ROOT / 'extension/review'
LIMIT = 25 * 1024 * 1024
UPSTREAM = 'dbd954eede479a5129831e4e7c30537389ae973d'
EXAMPLE_SUFFIXES = {'.py', '.sage', '.md', '.json', '.mjs', '.sv', '.v'}
ALIASES = {
    'book.pdf': 'outputs/book/surface-orders-book.pdf',
    'concise.pdf': 'outputs/papers/resolutions-concise.pdf',
    'extended.pdf': 'outputs/papers/resolutions-extended.pdf',
    'validated-oracle-concise.pdf': 'outputs/papers/validated-oracle-20261104/validated-oracle-concise.pdf',
    'validated-oracle-extended.pdf': 'outputs/papers/validated-oracle-20261104/validated-oracle-extended.pdf',
    'papers/dessin-core.tex': 'papers/dessin-core.tex',
}
OVERSIZED_JSON = 'data/synthetic-training/orbital-v1/wavepackets.json'

# Same-origin dynamic record URLs need the same namespace as static markup.
# In particular this preserves JSON bytes and their embedded SHA256 contracts.
BASE_ADAPTER = r'''// Scope: inherited companion pages only. Recorded data stays unchanged.
(() => {
  'use strict';
  if (window.__integralLegacyBase) return;
  window.__integralLegacyBase = true;
  const base = '/legacy/';
  const map = value => {
    if (typeof value !== 'string') return value;
    const loopback = 'http://127.0.0.1:8765';
    if (value === loopback) value = '/';
    else if (value.startsWith(loopback + '/')) value = value.slice(loopback.length);
    else if (value.startsWith(loopback + '?') || value.startsWith(loopback + '#')) value = '/' + value.slice(loopback.length);
    else if (value.startsWith(location.origin + '/')) value = value.slice(location.origin.length);
    if (value.startsWith('/') && !value.startsWith('//') && !value.startsWith(base)) return base + value.slice(1);
    return value;
  };
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
  const setAttribute = Element.prototype.setAttribute;
  Element.prototype.setAttribute = function (key, value) {
    return setAttribute.call(this, key, attributes.includes(key.toLowerCase()) ? map(value) : value);
  };
  const patch = node => {
    if (node.nodeType !== 1) return;
    for (const element of [node, ...node.querySelectorAll('[href],[src],[poster],[data-source]')]) {
      for (const key of attributes) {
        const value = element.getAttribute(key), mapped = map(value);
        if (value && mapped !== value) setAttribute.call(element, key, mapped);
      }
    }
  };
  new MutationObserver(records => records.forEach(record => record.type === 'attributes'
    ? patch(record.target) : record.addedNodes.forEach(patch)))
    .observe(document.documentElement, { subtree: true, childList: true,
      attributes: true, attributeFilter: attributes });
})();
'''


def sha(data):
    return hashlib.sha256(data).hexdigest()


def original_sources():
    return {str(p.relative_to(SOURCE)): sha(p.read_bytes())
            for p in sorted(SOURCE.rglob('*')) if p.is_file()}


def publication_sources():
    """Match the existing public-site whitelist; do not run mutating preparation."""
    tracked = subprocess.check_output(
        ['git', 'ls-files', '-z', 'examples', 'lean-analytic'], cwd=ROOT
    ).decode().split('\0')
    assets = dict(ALIASES)
    for name in filter(None, tracked):
        p = Path(name)
        if p.parts[0] == 'examples' and p.suffix in EXAMPLE_SUFFIXES:
            target = name
        elif p.parts[0] == 'lean-analytic' and p.suffix == '.lean':
            target = 'lean/' + p.name
        else:
            continue
        if target in assets and assets[target] != name:
            raise RuntimeError(f'Publication target collision: {target}')
        assets[target] = name
    return assets


class Links(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.links = []

    def handle_starttag(self, tag, attrs):
        for key, value in attrs:
            if value and key in {'href', 'src', 'poster', 'data-source'}:
                self.links.append((value, 'html:' + key))
            if value and key == 'srcset':
                self.links.extend((item.strip().split()[0], 'html:srcset')
                                  for item in value.split(',') if item.strip())


def static_audit():
    """Check actual markup and literal URLs; record dynamic paths separately."""
    references, dynamic, external, seen = [], [], set(), set()
    download_sources = []
    for p in sorted(DEST.rglob('*')):
        if not p.is_file() or p.suffix not in {'.html', '.css', '.js', '.mjs'}:
            continue
        source = str(p.relative_to(DEST))
        if source.startswith(('examples/', 'lean/', 'papers/')):
            # These are original repository downloads, not loaded browser modules.
            # Their filesystem imports must remain faithful to the cloned repo.
            download_sources.append(source)
            continue
        if source == 'legacy-base.js':
            continue
        text = p.read_text()
        found = []
        if p.suffix == '.html':
            parser = Links()
            parser.feed(text)
            found.extend(parser.links)
        # Static module imports and fetch/import/URL constructors with literal arguments.
        for match in re.finditer(
                r'''(?:\bfetch|\bimport|\bURL|\bWorker)\s*\(\s*(['"`])([^'"`]+)\1''', text):
            kind = 'js:request'
            if text[match.end():].lstrip().startswith('+'):
                kind = 'js:dynamic-prefix'
            elif match[0].split('(')[0].strip() == 'URL':
                kind = 'js:base-url'
            found.append((match[2], kind))
        found.extend((m[2], 'js:import') for m in re.finditer(
            r'''(?:\bfrom\s+|\bimport\s+)(['"])([^'"]+)\1''', text))
        # Includes data base paths used to construct filenames dynamically.
        found.extend((m[2], 'literal:legacy') for m in re.finditer(
            r'''(['"`])(/legacy/[^\s'"`<>]*)\1''', text))
        if p.suffix in {'.css', '.html'}:
            found.extend((m[1].strip().strip('\'"'), 'css:url') for m in re.finditer(
                r'url\(\s*([^)]*?)\s*\)', text))
        for url, kind in found:
            identity = (source, url, kind)
            if identity in seen:
                continue
            seen.add(identity)
            if not url or url.startswith(('#', 'data:', 'mailto:', 'javascript:', 'tel:')):
                continue
            if '${' in url:
                dynamic.append({'source': source, 'url': url, 'kind': kind})
                continue
            parsed = urlsplit(url)
            if parsed.hostname in {'127.0.0.1', 'localhost'}:
                references.append({'source': source, 'url': url, 'kind': kind,
                                   'status': 'unrebased_loopback_url'})
                continue
            if parsed.scheme or parsed.netloc:
                external.add(url)
                continue
            path = unquote(parsed.path)
            if not path:
                continue
            if path.startswith('/legacy/'):
                rel = posixpath.normpath(path[len('/legacy/'):])
            elif path.startswith('/'):
                # Remaining real root URLs would escape the inherited namespace.
                references.append({'source': source, 'url': url, 'kind': kind,
                                   'status': 'outside_legacy_namespace'})
                continue
            else:
                rel = posixpath.normpath(posixpath.join(posixpath.dirname(source), path))
            if rel.startswith('../'):
                references.append({'source': source, 'url': url, 'kind': kind,
                                   'status': 'outside_legacy_namespace'})
                continue
            target = DEST / rel
            if target.is_dir() and kind in {'literal:legacy', 'js:dynamic-prefix', 'js:base-url'}:
                dynamic.append({'source': source, 'url': url, 'kind': 'existing_directory_prefix'})
                continue
            exists = target.is_file() or (target / 'index.html').is_file()
            references.append({'source': source, 'url': url, 'kind': kind,
                               'target': rel, 'status': 'resolved' if exists else 'missing'})
    missing = [record for record in references if record['status'] != 'resolved']
    return {'scope': 'Browser markup, CSS, static imports, literal requests and namespace paths. Downloaded example sources retain repository-relative filesystem imports. Templated runtime paths require browser QA.',
            'checked_references': len(references), 'unresolved_references': missing,
            'dynamic_references': dynamic, 'external_url_count': len(external),
            'download_sources_not_browser_entrypoints': download_sources}


def main():
    DEST.mkdir(parents=True, exist_ok=True)
    REVIEW.mkdir(parents=True, exist_ok=True)
    before = original_sources()
    aliases = publication_sources()
    names = {p.name for p in SOURCE.iterdir()} | {Path(name).parts[0] for name in aliases}
    names |= {'legacy-base.js', 'availability.json'}
    alternatives = '|'.join(re.escape(name) for name in sorted(names, key=len, reverse=True))
    prefix = re.compile(r"(['\"\x60])/(?=(?:" + alternatives + r")(?:[/#?'\"\x60\s]|$)|[?#]|['\"\x60])")
    css_prefix = re.compile(r'url\(\s*/(?=(?:' + alternatives + r')(?:[/#?)]|$))')
    loopback_prefix = re.compile(r'''(['"`])http://127\.0\.0\.1:8765(?=/|[?#'"`])/?''')
    changes, ledger, missing_originals, generated = [], [], [], set()

    def write(rel, out, source=None, action='copy'):
        target = DEST / rel
        if len(out) > LIMIT:
            raise RuntimeError(f'Served file exceeds 25 MiB: {rel} ({len(out)} bytes)')
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(out)
        generated.add(str(rel))
        record = {'path': str(rel), 'served_bytes': len(out), 'served_sha256': sha(out), 'action': action}
        if source:
            record['source'] = str(source.relative_to(ROOT))
            record['source_sha256'] = sha(source.read_bytes())
        ledger.append(record)
        return target

    for p in sorted(SOURCE.rglob('*')):
        if not p.is_file():
            continue
        rel = p.relative_to(SOURCE)
        raw = p.read_bytes()
        out = raw
        # Never rewrite recorded scientific JSON or binary assets.
        if p.suffix in {'.html', '.css', '.js', '.mjs'}:
            text = raw.decode('utf-8')
            text = prefix.sub(lambda match: match[1] + '/legacy/', text)
            text = loopback_prefix.sub(lambda match: match[1] + '/legacy/', text)
            text = css_prefix.sub('url(/legacy/', text)
            if p.suffix == '.html':
                text = re.sub(r'(<head\b[^>]*>)',
                              r'\1<script src="/legacy/legacy-base.js"></script>', text, count=1, flags=re.I)
            out = text.encode('utf-8')
        if len(out) > LIMIT:
            if str(rel) != OVERSIZED_JSON or out != raw:
                raise RuntimeError(f'Review a lossless delivery method for {rel}')
            packed = gzip.compress(raw, compresslevel=9, mtime=0)
            assert gzip.decompress(packed) == raw
            write(str(rel) + '.gz', packed, p, 'lossless gzip')
            changes.append({'path': str(rel), 'action': 'lossless gzip',
                            'source_sha256': sha(raw), 'source_bytes': len(raw),
                            'served_bytes': len(packed), 'served_sha256': sha(packed)})
        else:
            write(str(rel), out, p, 'namespace and adapter' if out != raw else 'copy')
            if out != raw:
                changes.append({'path': str(rel), 'action': 'namespace and adapter',
                                'source_sha256': sha(raw), 'served_sha256': sha(out)})

    for destination, source_name in sorted(aliases.items()):
        source = ROOT / source_name
        if source.is_file():
            write(destination, source.read_bytes(), source, 'publication dependency')
        else:
            missing_originals.append({'destination': destination, 'source': source_name,
                                      'reason': 'Original publication asset is absent from the repository'})

    loader = DEST / 'orbital-lab.mjs'
    text = loader.read_text()
    old = "const r=await fetch('/legacy/data/synthetic-training/orbital-v1/wavepackets.json');if(!r.ok)throw Error('Wave packets unavailable');cases=(await r.json()).cases;"
    new = ("const r=await fetch('/legacy/data/synthetic-training/orbital-v1/wavepackets.json.gz');"
           "if(!r.ok)throw Error('Wave packets unavailable');"
           "const raw=await r.arrayBuffer(),bytes=new Uint8Array(raw);"
           "const payload=bytes[0]===31&&bytes[1]===139?"
           "await new Response(new Blob([raw]).stream().pipeThrough(new DecompressionStream('gzip'))).json():"
           "JSON.parse(new TextDecoder().decode(raw));cases=payload.cases;")
    if old not in text:
        raise RuntimeError('The known orbital loader changed; inspect before patching')
    loader.write_text(text.replace(old, new))
    for record in ledger:
        if record['path'] == 'orbital-lab.mjs':
            record.update(served_bytes=loader.stat().st_size, served_sha256=sha(loader.read_bytes()),
                          action='namespace and lossless gzip reader')
    changes.append({'path': 'orbital-lab.mjs', 'action': 'lossless gzip reader',
                    'served_sha256': sha(loader.read_bytes())})
    write('legacy-base.js', BASE_ADAPTER.encode(), action='dynamic URL namespace adapter')

    # Remove only stale files from this generated destination, never from web/.
    for p in sorted(DEST.rglob('*'), reverse=True):
        if p.is_file() and str(p.relative_to(DEST)) not in generated:
            p.unlink()
        elif p.is_dir() and not any(p.iterdir()):
            p.rmdir()
    audit = static_audit()
    availability = {'upstream_commit': UPSTREAM, 'source_tree': 'web/',
                    'source_files': len(before), 'namespace': '/legacy/',
                    'publication_aliases': ALIASES, 'publication_dependencies': len(aliases),
                    'missing_originals': missing_originals,
                    'unresolved_static_references': audit['unresolved_references'],
                    'per_file_limit_bytes': LIMIT,
                    'scientific_json_bytes_preserved': True,
                    'compressed_exception': {'path': OVERSIZED_JSON,
                                            'method': 'lossless gzip; original decompressed bytes retained'}}
    write('availability.json', (json.dumps(availability, indent=2) + '\n').encode(), action='availability manifest')
    assert original_sources() == before, 'Original web/ bytes changed during the build'
    for p in SOURCE.rglob('*.json'):
        rel = str(p.relative_to(SOURCE))
        actual = gzip.decompress((DEST / (rel + '.gz')).read_bytes()) if rel == OVERSIZED_JSON else (DEST / rel).read_bytes()
        assert actual == p.read_bytes(), f'Scientific JSON changed: {rel}'
    served = [p for p in DEST.rglob('*') if p.is_file()]
    largest = max(p.stat().st_size for p in served)
    assert largest <= LIMIT
    manifest = {'upstream_commit': UPSTREAM, 'source': 'web/',
                'destination': 'extension/site/legacy/', 'source_files': len(before),
                'files': len(served), 'original_tree_modified': False,
                'publication_dependencies': len(aliases), 'missing_originals': missing_originals,
                'scientific_json_bytes_preserved': True, 'per_file_limit_bytes': LIMIT,
                'largest_served_file': largest, 'transformations': changes,
                'assets': ledger, 'static_audit': audit}
    (REVIEW / 'legacy-build.json').write_text(json.dumps(manifest, indent=2) + '\n')
    (REVIEW / 'legacy-missing-originals.json').write_text(json.dumps({
        'missing_originals': missing_originals,
        'unresolved_static_references': audit['unresolved_references']}, indent=2) + '\n')
    print(json.dumps({'source_files': len(before), 'served_files': len(served),
                      'publication_dependencies': len(aliases), 'missing_originals': len(missing_originals),
                      'checked_static_references': audit['checked_references'],
                      'unresolved_static_references': len(audit['unresolved_references']),
                      'largest_served_file': largest}))
    if missing_originals or audit['unresolved_references']:
        raise RuntimeError('Inspect extension/review/legacy-missing-originals.json before publication')


if __name__ == '__main__':
    main()
