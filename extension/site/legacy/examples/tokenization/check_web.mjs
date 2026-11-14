import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import {fileURLToPath} from 'node:url';
import {segment,tokenCount,fraction} from '../../web/convextok.mjs';
const data=JSON.parse(readFileSync(fileURLToPath(new URL('../../web/data/convextok.json',import.meta.url)),'utf8'));
let replays=0;
for(const c of data.cases)for(const r of c.results)for(const scheme of Object.values(r.lp.rounded)){
  assert.equal(tokenCount(c.words,scheme.vocabulary),scheme.dp_count);
  assert.equal(tokenCount(c.words,scheme.vocabulary,true),scheme.greedy_count);
  assert.ok(scheme.dp_count>=fraction(r.lp.value));
  for(const w of c.words)assert.deepEqual(segment(w,scheme.vocabulary).flat(),w);
  replays++;
}
assert.equal(tokenCount([Array.from('abcd')],[Array.from('ab'),Array.from('bcd')]),2);
assert.equal(tokenCount([Array.from('abcd')],[Array.from('ab'),Array.from('bcd')],true),3);
console.log(JSON.stringify({corpora:data.cases.length,rounded_vocabulary_replays:replays,shortest_and_greedy_counts:'pass',roundtrip:'pass'}));
