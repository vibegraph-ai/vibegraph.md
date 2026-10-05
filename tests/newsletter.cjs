const { test } = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const vm = require('node:vm');
const code = fs.readFileSync('docs/assets/newsletter.js', 'utf8');
function mount(origin, fetch) {
  const events = {};
  const input = { value: 'test@example.com', validity: { valid: true }, setAttribute() {}, focus() {} };
  const button = {};
  const status = {};
  const form = { dataset: {}, setAttribute() {}, removeAttribute() {}, addEventListener(type, handler) { events[type] = handler; },
    querySelector(selector) { return selector === '[type="email"]' ? input : selector === 'button' ? button : selector === '[role="status"]' ? status : { value: '' }; } };
  vm.runInNewContext(code, { document: { querySelector: () => form }, location: new URL(origin), fetch, AbortSignal, URL });
  return { input, button, status, form, submit: () => events.submit({ preventDefault() {} }) };
}
test('preview and invalid addresses never contact the subscription service', async () => {
  let calls = 0;
  const fetch = async () => { calls++; throw Error('Unexpected request'); };
  const preview = mount('https://review.example.com', fetch);
  await preview.submit();
  assert.equal(preview.form.dataset.state, 'preview');
  const live = mount('https://vibegraph.md', fetch);
  live.input.validity.valid = false;
  await live.submit();
  assert.equal(live.form.dataset.state, 'error');
  assert.equal(calls, 0);
});
test('production sends one request, reports receipt and restores controls', async () => {
  let calls = 0, sent;
  let resolve;
  const pending = new Promise(r => { resolve = r; });
  const ui = mount('https://www.vibegraph.md', async (url, options) => {
    calls++; sent = { url, options }; await pending;
    return { ok: true, json: async () => ({ code: 'received' }) };
  });
  const first = ui.submit();
  assert.equal(ui.button.disabled, true);
  await ui.submit();
  assert.equal(calls, 1);
  resolve(); await first;
  assert.equal(sent.url, 'https://vibegraph.ai/api/subscribe/');
  assert.deepEqual(JSON.parse(sent.options.body), { email: 'test@example.com', website: '' });
  assert.equal(ui.form.dataset.state, 'success');
  assert.equal(ui.input.value, '');
  assert.equal(ui.button.disabled, false);
});
test('service errors preserve the address for a retry', async () => {
  const ui = mount('https://vibegraph.md', async () => ({ ok: false, json: async () => ({ code: 'unavailable' }) }));
  await ui.submit();
  assert.equal(ui.form.dataset.state, 'error');
  assert.equal(ui.input.value, 'test@example.com');
  assert.equal(ui.button.disabled, false);
});
