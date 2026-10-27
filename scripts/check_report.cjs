// Exercise the real inline report code with a small DOM substitute; no packages required.
const fs = require('node:fs'), path = require('node:path');
const vm = require('node:vm'), assert = require('node:assert/strict');
const root = path.resolve(__dirname, '..');
const html = fs.readFileSync(path.join(root, 'index.html'), 'utf8');
const scripts = [...html.matchAll(/<script([^>]*)>([\s\S]*?)<\/script>/g)];
const payload = JSON.parse(scripts.find(s => s[1].includes('application/json'))[2]);
const code = scripts.filter(s => !s[1].includes('application/json')).map(s => s[2]).join('\n');
function setup(data, hash = '') {
  const nodes = {};
  const make = id => nodes[id] ??= { id, innerHTML: '', textContent: '', value: '', dataset: {},
    classList: { toggle() {} }, addEventListener() {} };
  make('data').textContent = JSON.stringify(data);
  make('decision').value = make('source').value = 'all';
  make('order').value = 'priority';
  const ctx = vm.createContext({ document: { getElementById: make, querySelectorAll: () => [], addEventListener() {} },
    location: { hash }, history: { replaceState() {} }, console });
  vm.runInContext(code, ctx);
  return {nodes, run: code => vm.runInContext(code, ctx)};
}
const {nodes, run} = setup(payload);
assert(nodes.resultcount.textContent.startsWith(`${payload.episodes.length} of ${payload.episodes.length}`));
for (const e of payload.episodes) {
  run(`pick(${JSON.stringify(e.key)})`);
  assert(nodes.detail.innerHTML.includes('Mathematical anatomy'));
  assert(nodes.detail.innerHTML.includes(e.publisher.name));
  assert(nodes.detail.innerHTML.includes(e.review_link));
  assert(!nodes.detail.innerHTML.includes('[object Object]'));
}
for (const [decision, count] of Object.entries(payload.summary.decisions)) {
  nodes.decision.value = decision; run('drawList()');
  assert(nodes.resultcount.textContent.startsWith(`${count} of `));
}
nodes.decision.value = 'all'; nodes.search.value = 'sentinel-no-such-episode'; run('drawList()');
assert(nodes.list.innerHTML.includes('No matching episodes'));
assert.equal(nodes.detail.innerHTML, '');
nodes.search.value = ''; nodes.order.value = 'newest'; run('drawList()');
assert.equal(run("render('<script>bad()</script>')"), '&lt;script&gt;bad()&lt;/script&gt;');
assert(!nodes.coverage.innerHTML.includes('What I wanted from each episode'));
assert(nodes.coverage.innerHTML.includes('README.md#methodology'));
// The old, unqualified MLST hash remains usable while IDs are unambiguous.
assert.equal(setup(payload, '#' + payload.episodes[0].id).run('selected'), payload.episodes[0].key);
// A second source can reuse an episode ID; filtering and deep links remain distinct.
const multi = structuredClone(payload), extra = structuredClone(multi.episodes[0]);
extra.key = 'test-lectures:' + extra.id;
extra.publisher = {id: 'test-lectures', name: 'Test lecture series', short_name: 'Test', format: 'Lecture', url: 'https://example.org'};
multi.episodes.push(extra);
multi.collections.push({...multi.collections[0], ...extra.publisher, reviewed: 1});
const second = setup(multi);
second.nodes.source.value = 'test-lectures'; second.run('drawList()');
assert(second.nodes.resultcount.textContent.startsWith('1 of '));
assert(second.nodes.list.innerHTML.includes('Test lecture series'));
assert(second.nodes.detail.innerHTML.includes('Test lecture series'));
assert.equal(second.run('selected'), extra.key);
second.run(`pick(${JSON.stringify(extra.key)})`);
assert.equal(second.nodes.source.value, 'test-lectures');
second.run(`pick(${JSON.stringify(multi.episodes[1].key)})`);
assert.equal(second.nodes.source.value, 'all');
assert.equal(setup(multi, '#' + encodeURIComponent(extra.key)).run('selected'), extra.key);
console.log(`Passed: ${payload.episodes.length} reviews, source attribution, filters, cross-source ID collisions, deep links and text escaping.`);
