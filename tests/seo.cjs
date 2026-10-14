const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
for (const [file, url] of [['docs/index.html','https://vibegraph.md/'], ['docs/what-is-a-vibegraph/index.html','https://vibegraph.md/what-is-a-vibegraph/']]) {
  test(`${file} has canonical, initial HTML schema, and a single primary heading`, () => {
    const html = fs.readFileSync(file,'utf8');
    assert.ok(html.includes(`<link rel="canonical" href="${url}"`));
    assert.equal((html.match(/<h1[ >]/g)||[]).length,1);
    const script = html.match(/<script type="application\/ld\+json">([\s\S]*?)<\/script>/);
    assert.ok(script);
    const graph = JSON.parse(script[1])['@graph'];
    assert.ok(graph.some(node => node.url === url));
    assert.ok(graph.some(node => node['@id'] === 'https://vibegraph.ai/#organization'));
  });
}
test('sitemap and homepage discover the definition article', () => {
  assert.ok(fs.readFileSync('docs/sitemap.xml','utf8').includes('https://vibegraph.md/what-is-a-vibegraph/'));
  assert.ok(fs.readFileSync('docs/index.html','utf8').includes('href="/what-is-a-vibegraph/"'));
});
