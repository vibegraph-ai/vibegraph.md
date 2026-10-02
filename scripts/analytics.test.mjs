import assert from 'node:assert/strict';
import { readFileSync, existsSync } from 'node:fs';
import { runInNewContext } from 'node:vm';
import { test } from 'node:test';

const path = new URL('../docs/assets/analytics.js', import.meta.url);
const source = existsSync(path) ? readFileSync(path, 'utf8') : '';
function load(hostname, protocol = 'https:') {
  const inserted = [];
  const listeners = {};
  const context = {
    window: {}, URL,
    location: { hostname, protocol, href: `${protocol}//${hostname}/` },
    document: {
      createElement: () => ({}),
      getElementsByTagName: () => [{ parentNode: { insertBefore: script => inserted.push(script) } }],
      addEventListener: (name, handler) => { listeners[name] = handler; },
    },
  };
  runInNewContext(source, context);
  return { context, inserted, listeners };
}

test('loads the analytics SDK exactly once on the production domains', () => {
  for (const host of ['vibegraph.md', 'www.vibegraph.md']) {
    const { context, inserted } = load(host);
    assert.equal(inserted.length, 1, `SDK not loaded on ${host}`);
    assert.equal(inserted[0].src, 'https://us-assets.i.posthog.com/static/array.js');
    assert.equal(context.window.posthog._i[0][1].capture_pageview, true);
    assert.equal(context.window.posthog._i[0][1].capture_pageleave, true);
    runInNewContext(source, context);
    assert.equal(inserted.length, 1);
  }
});

test('never loads analytics on local, preview, lookalike or insecure hosts', () => {
  for (const host of ['localhost', '127.0.0.1', 'preview.vercel.app', 'vibegraph-ai.github.io', 'vibegraph.md.evil.test']) {
    assert.equal(load(host).inserted.length, 0, host);
  }
  assert.equal(load('vibegraph.md', 'http:').inserted.length, 0);
});

test('tracks outbound links and downloads without query strings or form values', () => {
  const { context, listeners } = load('vibegraph.md');
  assert.equal(typeof listeners.click, 'function');
  const click = (href, download = false) => listeners.click({ target: { closest: () => ({ href, hasAttribute: name => name === 'download' && download }) } });
  click('https://example.com/start?email=private@example.com#secret');
  click('https://vibegraph.md/files/guide.pdf?token=private');
  click('https://vibegraph.md/pricing/');
  click('mailto:private@example.com');
  const events = context.window.posthog.filter(item => item[0] === 'capture');
  assert.equal(events.length, 2);
  assert.equal(events[0][1], 'outbound_link_clicked');
  assert.equal(events[1][1], 'file_download_clicked');
  assert.ok(!JSON.stringify(events).includes('private'));
});
