#!/usr/bin/env node
/**
 * dev-server.mjs — roda a LP localmente COM a edge function do A/B.
 *
 * Por que existe: um servidor estático comum (`python3 -m http.server`) serve os arquivos mas
 * não executa `api/ab.js`. Com ele só dá para abrir `/a/index.html` e `/b/index.html` na mão —
 * o que nunca testa o que de fato roda em produção: o rewrite de `/`, o sorteio 50/50, o cookie
 * de variante e o forçador `?v=a`.
 *
 * Este servidor IMPORTA o `api/ab.js` real e aplica os rewrites e headers do `vercel.json`.
 * O que você vê aqui é o mesmo código que a Vercel executa.
 *
 * Uso:
 *   node scripts/dev-server.mjs [porta]
 *
 * Ou, descartável, sem instalar nada e sem deixar imagem:
 *   docker run --rm -v "$PWD":/app -w /app -p 3000:3000 node:22-alpine node scripts/dev-server.mjs
 */
import { createServer } from "node:http";
import { readFile, stat } from "node:fs/promises";
import { extname, join, normalize } from "node:path";
import { fileURLToPath } from "node:url";

const RAIZ = fileURLToPath(new URL("..", import.meta.url));
const PORTA = Number(process.argv[2] || process.env.PORT || 3000);

const vercel = JSON.parse(await readFile(join(RAIZ, "vercel.json"), "utf8"));
const { default: handlerAB } = await import(new URL("../api/ab.js", import.meta.url));

const TIPOS = {
  ".html": "text/html; charset=utf-8", ".css": "text/css; charset=utf-8",
  ".js": "text/javascript; charset=utf-8", ".mjs": "text/javascript; charset=utf-8",
  ".json": "application/json; charset=utf-8", ".webp": "image/webp",
  ".svg": "image/svg+xml", ".txt": "text/plain; charset=utf-8",
  ".xml": "application/xml; charset=utf-8", ".ico": "image/x-icon",
  ".woff2": "font/woff2",
};

/** Reproduz o bloco `headers` do vercel.json — inclusive o cache imutável de imagens e fontes. */
function headersDoVercel(caminho) {
  const extras = {};
  for (const regra of vercel.headers || []) {
    if (new RegExp("^" + regra.source + "$").test(caminho)) {
      for (const h of regra.headers) extras[h.key] = h.value;
    }
  }
  return extras;
}

/** Resolve uma URL para um arquivo em disco. `/a/` vira `a/index.html`, como na Vercel. */
async function resolverArquivo(caminho) {
  let rel = decodeURIComponent(caminho).replace(/^\/+/, "");
  if (rel === "" || rel.endsWith("/")) rel += "index.html";
  const abs = join(RAIZ, normalize(rel));
  if (!abs.startsWith(RAIZ)) return null;              // barra travessia de diretório
  try {
    if ((await stat(abs)).isDirectory()) return resolverArquivo(caminho + "/");
    return abs;
  } catch {
    try { const alt = abs + "/index.html"; await stat(alt); return alt; } catch { return null; }
  }
}

const servidor = createServer(async (req, res) => {
  const url = new URL(req.url, `http://localhost:${PORTA}`);
  const rewrite = (vercel.rewrites || []).find(r => r.source === url.pathname);

  try {
    // --- rota reescrita: executa a edge function DE VERDADE ---
    if (rewrite) {
      const pedido = new Request(url.href, {
        method: req.method,
        headers: Object.entries(req.headers).flatMap(([k, v]) =>
          Array.isArray(v) ? v.map(x => [k, x]) : [[k, v]]),
      });
      const resposta = await handlerAB(pedido);
      const cabecalhos = {};
      for (const [k, v] of resposta.headers) {
        // Set-Cookie pode vir múltiplo; o Headers do Node junta com vírgula.
        cabecalhos[k] = k.toLowerCase() === "set-cookie" ? v.split(/,\s*(?=[\w-]+=)/) : v;
      }
      res.writeHead(resposta.status, cabecalhos);
      res.end(Buffer.from(await resposta.arrayBuffer()));
      console.log(`  ${req.method} ${req.url} → api/ab.js (${resposta.status})`);
      return;
    }

    // --- estático ---
    const arquivo = await resolverArquivo(url.pathname);
    if (!arquivo) {
      res.writeHead(404, { "Content-Type": "text/plain; charset=utf-8" });
      res.end("404");
      console.log(`  ${req.method} ${req.url} → 404`);
      return;
    }
    const corpo = await readFile(arquivo);
    res.writeHead(200, {
      "Content-Type": TIPOS[extname(arquivo)] || "application/octet-stream",
      "Cache-Control": "public, max-age=0, must-revalidate",   // igual à Vercel para HTML/JS/CSS
      ...headersDoVercel(url.pathname),
    });
    res.end(corpo);
  } catch (erro) {
    res.writeHead(500, { "Content-Type": "text/plain; charset=utf-8" });
    res.end(String(erro && erro.stack ? erro.stack : erro));
    console.error(`  ERRO em ${req.url}:`, erro);
  }
});

servidor.listen(PORTA, () => {
  console.log(`
  LP no ar com a edge function do A/B  ·  http://localhost:${PORTA}

    /            sorteio 50/50, grava o cookie ab-e2 e serve a variante
    /?v=a        força a variante A (e fixa o cookie)
    /?v=b        força a variante B
    /a/  /b/     acesso direto, sem passar pelo sorteio

  Para trocar de variante, apague o cookie ab-e2 ou use ?v=.
  Ctrl+C encerra.
`);
});
