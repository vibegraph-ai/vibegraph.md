/**
 * Render cover.html and body.html to PDF with puppeteer-core driving the
 * installed Chrome. Two passes on purpose: the cover carries no footer
 * (matching v1.0), and the body's page numbering starts at 1 on the
 * Introduction page, exactly as v1.0 numbered it. build.py merges the two.
 */
const puppeteer = require("puppeteer-core");
const path = require("path");

const CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome";
const MARGIN = { top: "20mm", bottom: "24mm", left: "24mm", right: "24mm" };

const FOOTER = `
  <div style="width:100%; margin: 0 24mm; font-family: Georgia, serif; font-size: 7.6pt; color: #71717a;">
    <div style="border-top: 0.6px solid #d4d4d8; padding-top: 5px; display: flex; justify-content: space-between;">
      <span>The Vibegraph&trade; &nbsp;&middot;&nbsp; Your Vibes, Codified. &nbsp;&middot;&nbsp; v1.5 &nbsp;&middot;&nbsp; August 2026</span>
      <span>Page <span class="pageNumber"></span></span>
    </div>
  </div>`;

async function render(page, file, out, withFooter) {
  await page.goto("file://" + path.resolve(__dirname, file), {
    waitUntil: "networkidle0",
  });
  await page.pdf({
    path: path.resolve(__dirname, out),
    format: "Letter",
    printBackground: true,
    margin: MARGIN,
    displayHeaderFooter: withFooter,
    headerTemplate: "<span></span>",
    footerTemplate: withFooter ? FOOTER : "<span></span>",
  });
}

(async () => {
  const browser = await puppeteer.launch({ executablePath: CHROME });
  const page = await browser.newPage();
  await render(page, "cover.html", "cover.pdf", false);
  await render(page, "body.html", "body.pdf", true);
  await browser.close();
  console.log("rendered cover.pdf + body.pdf");
})();
