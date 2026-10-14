import { readFileSync } from 'node:fs';
import { pathToFileURL } from 'node:url';

export function payloadFor(config, paths) {
  if (!paths.length) throw new Error('Pass the changed canonical page paths. Use --submit only after release.');
  const origin = `https://${config.host}`;
  const urlList = [...new Set(paths)].map(path => {
    if (!config.paths.includes(path)) throw new Error(`Not an approved public page path: ${path}`);
    return new URL(path, origin).href;
  });
  return { host: config.host, key: config.key, keyLocation: `${origin}/${config.key}.txt`, urlList };
}

export async function submit(payload, fetcher = fetch) {
  const options = () => ({ redirect: 'error', signal: AbortSignal.timeout(15000) });
  const key = await fetcher(payload.keyLocation, options());
  if (key.status !== 200 || (await key.text()).trim() !== payload.key) throw new Error('The ownership file is not live. Release and verify the site before submitting.');
  for (const url of payload.urlList) {
    const response = await fetcher(url, options());
    if (response.status !== 200 || !response.headers.get('content-type')?.includes('text/html')) throw new Error(`Public HTML page unavailable: ${url}`);
    const html = await response.text();
    const robots = [...html.matchAll(/<meta\b[^>]*name=["'](?:robots|googlebot|bingbot)["'][^>]*>/gi)].map(match => match[0]).join(' ');
    if (/noindex|\bnone\b/i.test(robots + ' ' + (response.headers.get('x-robots-tag') ?? ''))) throw new Error(`Page is not indexable: ${url}`);
    const canonical = html.match(/<link\b[^>]*rel=["']canonical["'][^>]*href=["']([^"']+)["']/i)?.[1];
    if (canonical !== url) throw new Error(`Canonical does not match: ${url}`);
  }
  const response = await fetcher('https://api.indexnow.org/indexnow', {
    ...options(), method: 'POST', headers: { 'Content-Type': 'application/json; charset=utf-8' }, body: JSON.stringify(payload),
  });
  if (![200, 202].includes(response.status)) throw new Error(`IndexNow returned HTTP ${response.status}. Inspect the issue before retrying.`);
  return response.status === 200 ? 'URLs received. Indexing is not confirmed.' : 'URLs received. Ownership validation is pending.';
}

if (process.argv[1] && import.meta.url === pathToFileURL(process.argv[1]).href) {
  const args = process.argv.slice(2);
  const config = JSON.parse(readFileSync(new URL('./indexnow.json', import.meta.url), 'utf8'));
  const payload = payloadFor(config, args.filter(arg => arg !== '--submit'));
  if (args.includes('--submit')) console.log(await submit(payload));
  else console.log(JSON.stringify({ mode: 'dry-run', host: payload.host, urls: payload.urlList }, null, 2));
}
