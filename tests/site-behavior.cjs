const assert = require('node:assert/strict');
const fs = require('node:fs');
const vm = require('node:vm');
const code = fs.readFileSync('docs/assets/site.js', 'utf8');
const html = fs.readFileSync('docs/index.html', 'utf8');
function element() {
  return { dataset: {}, attrs: {}, events: {}, hidden: true,
    classList: { add() {}, remove() {} },
    setAttribute(k, v) { this.attrs[k] = v; },
    addEventListener(k, v) { this.events[k] = v; },
    querySelector() { return {}; }, querySelectorAll() { return []; },
    contains() { return false; }, focus() {} };
}
async function run(saved, reduced = false) {
  const root = element();
  const button = element();
  const target = element();
  const themes = [element(), element()];
  const nodes = { '.net-toggle': button, '#net-background': target };
  const document = { documentElement: root, hidden: false,
    querySelector: s => nodes[s] || element(), querySelectorAll: () => themes,
    addEventListener() {}, head: { append() {} } };
  const storage = { getItem: () => saved, setItem(k, v) { saved = v; } };
  const context = { document, localStorage: storage,
    matchMedia: q => ({ matches: q.includes('reduced-motion') ? reduced : q.includes('color-scheme'), addEventListener() {} }),
    addEventListener() {}, IntersectionObserver: class { observe() {} },
    window: { THREE: {}, VANTA: { NET: () => ({ renderer: {}, destroy() {} }) } } };
  vm.runInNewContext(html.match(/<script>([\s\S]*?)<\/script>/)[1], context);
  assert.equal(root.dataset.theme, saved === 'dark' ? 'dark' : 'light');
  vm.runInNewContext(code, context);
  await Promise.resolve(); await Promise.resolve();
  assert.equal(root.dataset.theme, saved === 'dark' ? 'dark' : 'light');
  assert.equal(root.dataset.net, reduced ? 'static' : 'running');
  assert.equal(button.disabled, reduced);
  if (!reduced) {
    button.events.click();
    assert.equal(root.dataset.net, 'static');
    assert.equal(button.attrs['aria-label'], 'Play motion');
    assert.equal(button.attrs['aria-pressed'], 'true');
    button.events.click();
    await Promise.resolve(); await Promise.resolve();
    assert.equal(root.dataset.net, 'running');
    assert.equal(button.attrs['aria-label'], 'Pause motion');
    themes[0].events.click();
    assert.equal(root.dataset.theme, saved);
  }
}
(async () => {
  await run(null); await run('invalid'); await run('dark'); await run(null, true);
  assert(!html.includes('Preview NET background'));
  assert(!html.includes('vibegraph &amp; vibeclone'));
  assert(html.includes('© 2026 Raizen Labs, LLC | Built and maintained by <a href="https://ryancharleston.com">Ryan Charleston</a>'));
  console.log('PASS: light default, saved theme, autoplay, pause/play, reduced motion, footer');
})();
