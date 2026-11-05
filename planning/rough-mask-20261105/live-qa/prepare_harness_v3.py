"""Prepare additive strict QA from the exact141-group predecessor; no browser execution."""
from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parents[3];HERE=Path(__file__).resolve().parent
sha=lambda b:hashlib.sha256(b).hexdigest()
OLD=ROOT/'planning/signed-divisor-20261105/live-qa/check_browser_v1.mjs'
assert sha(OLD.read_bytes())=='cf3c42ecfddf2121e1fa40ecfd4beca9666440246156b51207905aca4117660d'
s=OLD.read_text();changes=[]
def replace(old,new,minimum=1):
 global s
 n=s.count(old);assert n>=minimum,(old,n)
 s=s.replace(old,new);changes.append(dict(old=old,new=new,occurrences=n))
replace("assert(base&&out&&expected.book_pages===279&&expected.math_nodes===8176);", "assert(base&&out&&expected.schema==='rough-mask-release-expectations-v1'&&Number.isInteger(expected.book_pages)&&Number.isInteger(expected.math_nodes)&&expected.old_math_nodes===8176&&expected.rma_anchors.length===40);")
replace("document.querySelectorAll('math').length===8176", "document.querySelectorAll('math').length===${expected.math_nodes}")
for v in ['book.math','book.visible','bm.visible','sdBook.math','sdBook.visible']:replace(v+'===8176',v+'===expected.math_nodes')
replace("landing.includes('279 pages')", "landing.includes(String(expected.book_pages)+' pages')")
replace("/focused articles\\s*64\\/175\\s*pages/.test(landing)", "new RegExp(String.raw`focused articles\\s*${expected.focused_pages.join('/')}\\s*pages`).test(landing)")
replace("/notes\\s*23\\/66\\s*pages/.test(landing)", "new RegExp(String.raw`notes\\s*${expected.notes_pages.join('/')}\\s*pages`).test(landing)")
replace("landing.includes('8,176')", "landing.includes(expected.math_nodes.toLocaleString('en-US'))")
replace("'new-book-all8176-visible-and-proof-source-PDF-navigation'", "'book-all-current-MathML-visible-and-proof-source-PDF-navigation'")
replace("'new-book-320-focusable-table-source-figure-and-all8176-visible'", "'book-320-focusable-table-source-figure-and-all-currentMathML-visible'")
anchor=" for(const page of['implementation-plan.html','verification.html'])"
replace(anchor,(HERE/'rough-mask-block-v3.js.txt').read_text()+'\n'+anchor)
replace("check(/signed[ -]divisor/i.test(text),'new-signed-divisor-synchronized-'+page);", "check(/signed[ -]divisor/i.test(text),'new-signed-divisor-synchronized-'+page);check(/rough[ -](?:prime[ -])?mask/i.test(text),'new-rough-mask-synchronized-'+page);")
replace("check(links.signed&&links.signedProof&&links.profile&&links.proof&&links.cover,'landing-profile-proof-cover-links',links);", "check(links.signed&&links.signedProof&&links.profile&&links.proof&&links.cover,'landing-profile-proof-cover-links',links);check(await b.evaluate(`!!document.querySelector('a[href$=\"book/main.html#rma:core\"]')&&!!document.querySelector('a[href$=\"data/rough-mask-controls.json\"]')`),'landing-new-rma-proof-and-summary-links');")
replace("const paths=['/book/sources/signed-divisor-core.tex'", "const paths=['/book/sources/rough-mask-core.tex','/book/sources/rough-mask-details.tex','/data/rough-mask-controls.json','/book/sources/signed-divisor-core.tex'")
replace("const assetHashes={", "const assetHashes={'/data/rough-mask-controls.json':expected.summary.sha256,'/book/sources/rough-mask-core.tex':expected.assets['/book/sources/rough-mask-core.tex'],'/book/sources/rough-mask-details.tex':expected.assets['/book/sources/rough-mask-details.tex'],")
replace("report.strict_integration_groups=report.integration.length;", "report.bound_expectations={book_pages:expected.book_pages,math_nodes:expected.math_nodes,tables:expected.tables,focused_pages:expected.focused_pages,notes_pages:expected.notes_pages,rma_anchors:expected.rma_anchors.length,summary_sha256:expected.summary.sha256};report.strict_integration_groups=report.integration.length;")
replace("report.scope='NEW signed-divisor:", "report.scope='NEW rough-mask adds40rma labels,exact3case tables/summary,S-only mask and restrictedcoefficient/zeroedge/PIT-M1-U7 scopes; rootbound newbook counts preserve old8176MathML/29SVGrefs/13labs and all141predecessor groups. Retained signed-divisor:")
# Global WS/idle protocol and existing error classifications are copied byte for byte.
old=OLD.read_text();start=old.index('const collectedErrors=');end=old.index('const check=')
assert old[start:end]==s[s.index('const collectedErrors='):s.index('const check=')]
for token in ["const inherited=", "const unexpected=errors.filter(x=>!inherited.includes(x))", "networkErrors.length===0", "timingEvents.filter(x=>x.event==='network.fetchError').length===0"]:
 # The predecessor names inherited inside a comma declaration, so compare its substantive filter separately.
 if token=='const inherited=':continue
 assert token in old and token in s
assert 'NS_BINDING'not in s
with (HERE/'check_browser_v3.mjs').open('x') as f:f.write(s)
record=dict(passed=True,prepared_only=True,browser_executed=False,prior_harness_sha256=sha(OLD.read_bytes()),new_harness_sha256=sha(s.encode()),global_WS_block_byte_identical=True,error_filters_unchanged=True,legacy_groups_retained=141,expected_new_count_source='Explicit root-supplied candidate counts in expectations-v1.json, SHA bound by runner',exact_adaptations=changes)
with (HERE/'harness-adaptation-v3.json').open('x') as f:json.dump(record,f,sort_keys=True,indent=2);f.write('\n')
print(record['new_harness_sha256'])
