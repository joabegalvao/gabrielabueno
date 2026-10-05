#!/usr/bin/env node
/* Monta a imagem de compartilhamento (1200x630) com o Chromium, usando as
   fontes do site e as imagens geradas por tools/optimize-images.py (os
   ícones também saem de lá, a partir do monograma).

   Uso (na raiz do projeto), com o Playwright instalado:
     node tools/render-compartilhamento.js

   Variáveis opcionais: PLAYWRIGHT_MODULE (caminho do módulo playwright) e
   CHROMIUM_PATH (executável do Chromium). */
const path = require('path');
const fs = require('fs');
const os = require('os');

const playwrightModule = process.env.PLAYWRIGHT_MODULE || 'playwright';
const { chromium } = require(playwrightModule);

const root = path.resolve(__dirname, '..');
const out = path.join(root, 'assets/img');

const fontFace = (family, file, style = 'normal') => `@font-face { font-family: "${family}"; src: url("file://${path.join(root, 'assets/fonts', file)}") format("woff2"); font-style: ${style}; font-weight: 300 700; }`;
const fonts = [
  fontFace('Bodoni Moda', 'bodoni-moda-normal-latin.woff2'),
  fontFace('Bodoni Moda', 'bodoni-moda-italic-latin.woff2', 'italic'),
  fontFace('Jost', 'jost-normal-latin.woff2'),
].join('\n');

const BROWN = '#2b2420', GOLD = '#a07127', GOLD2 = '#ecd6b0', IVORY = '#f7f3ed';
const frame = (file, w, h, extra = '') => `<div style="position:relative;padding:8px;border:1px solid ${GOLD};${extra}"><img src="file://${path.join(out, file)}" style="width:${w}px;height:${h}px;object-fit:cover;object-position:50% 12%;display:block" alt=""></div>`;

const html = `<div style="width:1200px;height:630px;display:grid;grid-template-columns:620px 580px;background:${IVORY};color:#241f1b;font-family:Jost,sans-serif;overflow:hidden">
  <div style="display:flex;flex-direction:column;justify-content:center;padding:0 64px">
    <div style="display:flex;align-items:center;gap:16px">
      <img src="file://${path.join(out, 'monograma-160.png')}" style="width:56px;height:auto" alt="">
      <div style="line-height:1.1"><div style="font-family:'Bodoni Moda',serif;font-size:24px;letter-spacing:.04em">Gabriela Bueno</div><div style="margin-top:4px;font-size:11px;font-weight:500;letter-spacing:.28em;text-transform:uppercase;color:#7a5416">Hair Colorist</div></div>
    </div>
    <div style="margin-top:44px;font-family:'Bodoni Moda',serif;font-size:56px;line-height:1.04;letter-spacing:-.01em">Cor que parece sua,<br><em style="color:#7a5416">com menos manutenção.</em></div>
    <div style="margin-top:26px;font-size:20px;font-weight:300;line-height:1.45;color:#625649">Mechas, mega hair e correção de cor em Maringá.<br>Há 8 anos na beleza. Agende pelo WhatsApp.</div>
    <div style="margin-top:28px;display:flex;align-items:center;gap:12px;font-size:12px;font-weight:500;letter-spacing:.24em;text-transform:uppercase;color:#7a5416"><span style="display:inline-block;width:24px;height:1px;background:${GOLD}"></span> Nota 5 no Google</div>
  </div>
  <div style="position:relative;background:${BROWN};display:flex;align-items:center;justify-content:center;gap:20px;padding:0 40px">
    ${frame('loiro-ondulado-665.jpg', 230, 400, 'margin-top:-48px')}
    ${frame('loiro-mel-665.jpg', 230, 400, 'margin-top:48px')}
  </div>
</div>`;

(async () => {
  const browser = await chromium.launch(
    process.env.CHROMIUM_PATH ? { executablePath: process.env.CHROMIUM_PATH } : {}
  );
  const page = await browser.newPage({ viewport: { width: 1200, height: 630 }, deviceScaleFactor: 1 });
  // a página é aberta por file:// para o Chromium aceitar as fontes e as fotos locais
  const tmp = path.join(os.tmpdir(), 'gabriela-render.html');
  fs.writeFileSync(tmp, `<!doctype html><html><head><meta charset="utf-8"><style>${fonts} body{margin:0;background:transparent}</style></head><body>${html}</body></html>`);
  await page.goto('file://' + tmp, { waitUntil: 'load' });
  await page.evaluate(() => document.fonts.ready);
  await page.screenshot({ path: path.join(out, 'compartilhamento.jpg'), type: 'jpeg', quality: 86 });
  fs.unlinkSync(tmp);
  await browser.close();
  console.log('assets/img/compartilhamento.jpg');
})();
