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
const total = payload.episodes.length + payload.backlog.length;
const count = () => Number(nodes.resultcount.textContent.split(' of ')[0]);

// One Library: a single view, with reviewed episodes and unreviewed candidates in one list.
assert(!html.includes('data-view='), 'no tabs: the Library is the only view');
assert(!/<nav\b/.test(html.split('<script')[0]), 'no navigation bar');
assert.equal(run('items.length'), total);
assert(nodes.resultcount.textContent.startsWith(`${total} of ${total} items shown`));
assert(nodes.resultcount.textContent.includes(`${payload.episodes.length} with notes`));
assert(nodes.stats.innerHTML.includes(`<strong>${total}</strong><span>items in the library</span>`));

// Status filter separates them without separate tabs.
nodes.status.value = 'reviewed'; run('drawList()'); assert.equal(count(), payload.episodes.length);
nodes.status.value = 'unreviewed'; run('drawList()'); assert.equal(count(), payload.backlog.length);
nodes.status.value = 'all'; run('drawList()');

// Reviewed items open their notes; unreviewed items say why they are here.
for (const e of payload.episodes) {
  run(`pick(${JSON.stringify(e.key)})`);
  assert(nodes.detail.innerHTML.includes('Mathematical anatomy'));
  assert(nodes.detail.innerHTML.includes(e.publisher.name));
  assert(nodes.detail.innerHTML.includes(e.review_link));
  assert(!nodes.detail.innerHTML.includes('[object Object]'));
}
for (const b of payload.backlog) {
  run(`pick(${JSON.stringify(b.key)})`);
  assert(nodes.detail.innerHTML.includes('Not yet reviewed'), b.key);
  assert(nodes.detail.innerHTML.includes('Why it is here'));
  assert(!nodes.detail.innerHTML.includes('Mathematical anatomy'));
  assert(!nodes.detail.innerHTML.includes('[object Object]') && !nodes.detail.innerHTML.includes('undefined'), b.key);
}

// Core ideas: every item carries its links; picking an idea shows its sources and narrows the list.
assert.equal(payload.core.length, 67);
const linked = [...payload.episodes, ...payload.backlog];
assert(linked.every(i => Array.isArray(i.core)));
const ids = new Set(payload.core.map(c => c.id));
assert(linked.every(i => i.core.every(c => ids.has(c.id))));
assert(payload.episodes.some(e => e.core.length) && payload.backlog.some(b => b.core.length), 'both kinds are tied to core ideas');
for (const c of payload.core) {
  run(`pickIdea(${JSON.stringify(c.id)})`);
  assert.equal(count(), linked.filter(i => i.core.some(x => x.id === c.id)).length, c.id);
  assert(nodes.ideabox.innerHTML.includes(`${c.id} · `) && nodes.ideabox.innerHTML.includes('Root text:'), c.id);
  assert(!nodes.ideabox.innerHTML.includes('undefined') && !nodes.ideabox.innerHTML.includes('[object Object]'), c.id);
}
// Within an idea, root and teaching sources come before material that goes deeper.
const busy = payload.core.map(c => c.id).find(id => new Set(linked.flatMap(i => i.core.filter(x => x.id === id).map(x => x.relation))).size > 1);
if (busy) {
  run(`pickIdea(${JSON.stringify(busy)})`);
  const order = [...nodes.list.innerHTML.matchAll(/data-id="([^"]+)"/g)].map(m => m[1].replaceAll('&amp;', '&'));
  const rank = {ROOT: 0, ORIGINATOR: 1, TEACHING: 2, EXTENSION: 3};
  const ranks = order.map(k => rank[linked.find(i => i.key === k).core.find(x => x.id === busy).relation]);
  assert.deepEqual(ranks, [...ranks].sort((a, b) => a - b), 'best sources first');
}
nodes.idea.value = 'none'; run('drawIdea();drawList()');
assert.equal(count(), linked.filter(i => !i.core.length).length);
assert.equal(nodes.ideabox.innerHTML, '');
run("pickIdea('all')"); assert.equal(count(), total);
// An item outside the current filters is still reachable: the filters reset.
nodes.status.value = 'unreviewed'; run('drawList()'); run(`pick(${JSON.stringify(payload.episodes[0].key)})`);
assert.equal(nodes.status.value, 'all'); assert.equal(run('selected'), payload.episodes[0].key);

// Search and sort work across the whole library.
nodes.search.value = 'sentinel-no-such-item'; run('drawList()');
assert(nodes.list.innerHTML.includes('No matching items'));
assert.equal(nodes.detail.innerHTML, '');
nodes.search.value = ''; nodes.order.value = 'newest'; run('drawList()'); assert.equal(count(), total);
assert.equal(run("render('<script>bad()</script>')"), '&lt;script&gt;bad()&lt;/script&gt;');
assert(nodes.coverage.innerHTML.includes('README.md#methodology'));

// Deep links: an item key, the old unqualified MLST id, and a core idea.
assert.equal(setup(payload, '#' + payload.episodes[0].id).run('selected'), payload.episodes[0].key);
assert.equal(setup(payload, '#' + encodeURIComponent(payload.backlog[0].key)).run('selected'), payload.backlog[0].key);
const deep = setup(payload, '#idea=l1'); assert.equal(deep.nodes.idea.value, 'L1'); assert(deep.nodes.ideabox.innerHTML.includes('L1 · '));
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
console.log(`Passed: one Library of ${total} items (${payload.episodes.length} reviewed, ${payload.backlog.length} not yet), status and source filters, ${payload.core.length} core ideas with sources and ordering, deep links, cross-source ID collisions and text escaping.`);
