import { test } from 'node:test';
import assert from 'node:assert/strict';
import { payloadFor, submit } from './indexnow.mjs';

const config = { host: 'example.com', key: '0123456789abcdef', paths: ['/', '/about/'] };
const payload = payloadFor(config, ['/about/']);
test('only explicitly listed public canonical paths can be submitted', () => {
  for (const path of ['https://elsewhere.example/', '/account/', '/about/?email=a', '/about/#fragment', '//elsewhere.example/']) {
    assert.throws(() => payloadFor(config, [path]));
  }
  assert.throws(() => payloadFor(config, []));
  assert.equal(payloadFor(config, ['/', '/']).urlList.length, 1);
});
test('missing ownership prevents any page request or submission', async () => {
  let calls = 0;
  await assert.rejects(submit(payload, async () => { calls++; return new Response('missing', { status: 404 }); }), /ownership file/);
  assert.equal(calls, 1);
});
test('unavailable, noindex, and wrong-canonical pages prevent submission', async () => {
  for (const response of [
    () => new Response('failed', { status: 503 }),
    () => new Response('<meta name="robots" content="noindex">', { headers: { 'content-type': 'text/html' } }),
    () => new Response('<link rel="canonical" href="https://example.com/">', { headers: { 'content-type': 'text/html' } }),
  ]) {
    let calls = 0;
    await assert.rejects(submit(payload, async () => ++calls === 1 ? new Response(config.key) : response()));
    assert.equal(calls, 2);
  }
});
test('a verified page is submitted once and pending validation is reported accurately', async () => {
  let calls = 0;
  const result = await submit(payload, async (url, options) => {
    calls++;
    if (calls === 1) return new Response(config.key);
    if (calls === 2) return new Response('<link rel="canonical" href="https://example.com/about/">', { headers: { 'content-type': 'text/html' } });
    assert.equal(url, 'https://api.indexnow.org/indexnow');
    assert.equal(options.method, 'POST');
    assert.deepEqual(JSON.parse(options.body), payload);
    return new Response('', { status: 202 });
  });
  assert.match(result, /validation is pending/);
  assert.equal(calls, 3);
});
