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
  // Like a real select, an unset control reads as ''; the page treats that as "all".
  const make = id => nodes[id] ??= { id, innerHTML: '', textContent: '', value: '', dataset: {},
    classList: { toggle() {} }, addEventListener() {} };
  make('data').textContent = JSON.stringify(data);
  const ctx = vm.createContext({ document: { getElementById: make, querySelectorAll: () => [], addEventListener() {} },
    location: { hash }, history: { replaceState() {} }, console });
  vm.runInContext(code, ctx);
  return {nodes, run: code => vm.runInContext(code, ctx)};
}
const {nodes, run} = setup(payload);
const items = payload.backlog, total = items.length;
const count = () => Number(nodes.resultcount.textContent.split(' of ')[0]);

// One Library: a single view; every item has the same form, whatever its source.
assert(!html.includes('data-view='), 'no tabs: the Library is the only view');
assert(!/<nav\b/.test(html.split('<script')[0]), 'no navigation bar');
assert(!('episodes' in payload) && !('roadmap' in payload), 'the page carries no review notes or study path');
assert(!/transcript|<h3>Mathematical anatomy|not yet reviewed|\breviewed\b|viewing plan/i.test(html.split('<script id="data"')[0] + code), 'no review wording in the page');
assert.equal(run('items.length'), total);
assert(nodes.resultcount.textContent.startsWith(`${total} of ${total} items shown`));
assert(nodes.stats.innerHTML.includes(`<strong>${total}</strong><span>items in the library</span>`));
const sources = new Set(items.map(i => i.source_id));
assert(sources.has('mlst') && sources.size > 1, 'MLST and the other sources share the list');
assert.equal(new Set(items.map(i => i.key)).size, total, 'unique keys');

// Every item opens the same kind of entry: why it is here and what to settle.
for (const b of items) {
  run(`pick(${JSON.stringify(b.key)})`);
  const h = nodes.detail.innerHTML;
  assert(h.includes('Why it is here') && h.includes('Open original'), b.key);
  assert(!h.includes('[object Object]') && !h.includes('undefined'), b.key);
}

// Source filter.
for (const id of ['mlst', [...sources].find(s => s !== 'mlst')]) {
  nodes.source.value = id; run('drawList()');
  assert.equal(count(), items.filter(i => i.source_id === id).length, id);
}
nodes.source.value = 'all'; run('drawList()');

// Core ideas: every item carries its links; picking an idea shows its sources and narrows the list.
assert.equal(payload.core.length, 67);
assert(items.every(i => Array.isArray(i.core)));
const ids = new Set(payload.core.map(c => c.id));
assert(items.every(i => i.core.every(c => ids.has(c.id))));
assert(items.some(i => i.source_id === 'mlst' && i.core.length) && items.some(i => i.source_id !== 'mlst' && i.core.length), 'both are tied to core ideas');
for (const c of payload.core) {
  run(`pickIdea(${JSON.stringify(c.id)})`);
  assert.equal(count(), items.filter(i => i.core.some(x => x.id === c.id)).length, c.id);
  assert(nodes.ideabox.innerHTML.includes(`${c.id} · `) && nodes.ideabox.innerHTML.includes('Root text:'), c.id);
  assert(!nodes.ideabox.innerHTML.includes('undefined') && !nodes.ideabox.innerHTML.includes('[object Object]'), c.id);
}
// Within an idea, root and teaching sources come before material that goes deeper.
const busy = payload.core.map(c => c.id).find(id => new Set(items.flatMap(i => i.core.filter(x => x.id === id).map(x => x.relation))).size > 1);
if (busy) {
  run(`pickIdea(${JSON.stringify(busy)})`);
  const order = [...nodes.list.innerHTML.matchAll(/data-id="([^"]+)"/g)].map(m => m[1].replaceAll('&amp;', '&'));
  const rank = {ROOT: 0, ORIGINATOR: 1, TEACHING: 2, EXTENSION: 3};
  const ranks = order.map(k => rank[items.find(i => i.key === k).core.find(x => x.id === busy).relation]);
  assert.deepEqual(ranks, [...ranks].sort((a, b) => a - b), 'best sources first');
}
nodes.idea.value = 'none'; run('drawIdea();drawList()');
assert.equal(count(), items.filter(i => !i.core.length).length);
assert.equal(nodes.ideabox.innerHTML, '');
run("pickIdea('all')"); assert.equal(count(), total);
// An item outside the current filters is still reachable: the filters reset.
const other = items.find(i => i.source_id !== 'mlst'), mlst = items.find(i => i.source_id === 'mlst');
nodes.source.value = other.source_id; run('drawList()'); run(`pick(${JSON.stringify(mlst.key)})`);
assert.equal(nodes.source.value, 'all'); assert.equal(run('selected'), mlst.key);

// Search and sort work across the whole library.
nodes.search.value = 'sentinel-no-such-item'; run('drawList()');
assert(nodes.list.innerHTML.includes('No matching items'));
assert.equal(nodes.detail.innerHTML, '');
nodes.search.value = ''; nodes.order.value = 'newest'; run('drawList()'); assert.equal(count(), total);
assert.equal(run("esc('<script>bad()</script>')"), '&lt;script&gt;bad()&lt;/script&gt;');
assert(nodes.coverage.innerHTML.includes('In the Library'));

// Deep links: an item key, the old unqualified MLST id, and a core idea.
assert.equal(setup(payload, '#' + mlst.key.split(':')[1]).run('selected'), mlst.key);
assert.equal(setup(payload, '#' + encodeURIComponent(other.key)).run('selected'), other.key);
const deep = setup(payload, '#idea=l1'); assert.equal(deep.nodes.idea.value, 'L1'); assert(deep.nodes.ideabox.innerHTML.includes('L1 · '));
// Two sources can reuse an item ID; keys and deep links stay distinct.
const multi = structuredClone(payload), extra = structuredClone(mlst);
extra.key = 'test-lectures:' + mlst.key.split(':')[1]; extra.source_id = 'test-lectures'; extra.source = 'Test lecture series';
multi.backlog.push(extra);
multi.collections.push({...multi.collections[0], id: 'test-lectures', name: 'Test lecture series'});
const second = setup(multi);
second.nodes.source.value = 'test-lectures'; second.run('drawList()');
assert(second.nodes.resultcount.textContent.startsWith('1 of '));
assert(second.nodes.list.innerHTML.includes('Test lecture series'));
assert.equal(second.run('selected'), extra.key);
assert.equal(setup(multi, '#' + encodeURIComponent(extra.key)).run('selected'), extra.key);
assert.equal(setup(multi, '#' + mlst.key.split(':')[1]).run('initial'), null, 'an ambiguous bare id preselects nothing');
console.log(`Passed: one Library of ${total} items from ${sources.size} sources in one form, source filter, ${payload.core.length} core ideas with sources and ordering, deep links, cross-source ID collisions and text escaping.`);
