# site-pasta-alimentos — LP do Kit (linha da Ana)

> Doc de orientação. As convenções da frota são citadas como `../CONVENTIONS.md` e `../TRACKING.md`
> em todos os repos, mas **esses arquivos não existem** em lugar nenhum — a referência viva é o
> `lib/tracking.ts` das LPs Next (`lp-vistoria` é a mais completa).

## O que este repo é
- **LP do Kit Pasta Sanitária** — produto Hotmart `H104875140X`, R$ 47,99, 54 documentos prontos.
  Domínio: `lp-pasta-alimentos.consultorasanitaria.com.br`.
- **HTML estático**, não Next.js: `a/index.html`, `b/index.html`, split 50/50 via `api/ab.js`
  (edge function, rewrite de `/`). Sem `package.json` de app, sem `next.config`.

### Não confundir com `lp-pasta-personalizada-alimentos`
São **produtos diferentes**, não um o sucessor do outro. Aquele repo vende a **Pasta Personalizada**
(`A106157606C` / `A106162381P` / `Q106162166E`, R$ 497–857) em
`pasta-personalizada-alimentos.consultorasanitaria.com.br`. Produtos, preços e domínios distintos.
Uma versão anterior deste doc afirmava que ele era o sucessor "com mesmo produto/linha" — era falso,
e daí saiu um status "A APOSENTAR" sem fundamento. A confusão provavelmente veio de um
`b/index.html` legado naquele repo que vendia `H104875140X` e já não existe mais.

## Grupo de tracking: **ANA**
- Meta Pixel `1429926872242671` · Google Ads `AW-18030262622` · GA4 `G-L1SR8V2ECY`.
- Microsoft Clarity `y109t0glph` — **compartilhado com outros oito repos** da casa. Sem tags
  customizadas é impossível saber de qual LP é uma gravação.
- Slug: `alimentos`.

## Tracking — tudo em `tracking.js` (raiz)
Ponto único de link de checkout e de eventos, carregado pelas duas variantes com
`<script defer src="../tracking.js?v=2">`. **Não duplicar o bloco dentro dos HTMLs** — era assim
antes, e a duplicação literal é o que produz drift.

- `sck=e2|<variante>` — `e2` é o código do experimento emitido pelo ERP, e é o que faz a venda
  casar. Pipe, sem `_` (a Hotmart reserva `_` para o sistema), ≤30 chars.
  Chega no webhook em `purchase.origin.sck`.
- `utm_*` de origem paga repassados ao checkout → alimentam o Hotmart Analytics. A Hotmart **não**
  envia UTM no webhook.
- `xcod=e2|<variante>|<campaign.id>|<ad.id>` → é o que leva os IDs do anúncio até o webhook.
  Emitido só quando há campanha ou anúncio.
- A variante sai do `data-variant` do `<html>`, com o cookie `ab-e2` como fallback. **O cookie leva
  o código do experimento**: teste novo re-sorteia todo mundo, em vez de herdar a atribuição do
  anterior — que nasceria enviesado.
- Clarity recebe `lp_page` e `ab_variant` — o rewrite de `/` deixa a URL idêntica em A e B, então
  sem essas tags não há como separar as variantes no painel.

## Pendências conhecidas
- **Atribuição de venda: resolvida.** O ERP casa a venda por `site.codigo == sck` ou por
  `experimento.codigo || '|' || variante`. Com o experimento `e2` cadastrado, `e2|a` e `e2|b` casam
  pelo segundo caminho. Antes a tag era `alimentos|<variante>` e não casava com nada.
  Segue em aberto: há **dois registros de site** para o mesmo host (`lp7` e `lp4`, um com `www.` e
  outro sem) — conferir qual é o bom.
- **`xcod` não foi confirmado em payload real.** Documentado na ajuda da Hotmart como o caminho que
  chega no webhook, mas ainda não verificado aqui. Conferir o `payload_bruto` de uma transação de
  teste antes de confiar no dado — foi o que se fez com o `sck` (confirmado em prod 2026-07-30).
- **Imagens:** 22 rasters grandes soltos na raiz.

## Rodar localmente COM o A/B
`python3 -m http.server` serve os arquivos mas **não executa a edge function** — com ele só dá para
abrir `/a/index.html` na mão, o que nunca testa o rewrite de `/`, o sorteio, o cookie nem o `?v=`.

```bash
node scripts/dev-server.mjs 3000
```

O `scripts/dev-server.mjs` **importa o `api/ab.js` real** e aplica os rewrites e headers do
`vercel.json`: o que se vê ali é o mesmo código que a Vercel executa. Sem dependências — Node 18+
já tem `Request`/`Response`/`fetch`.

Descartável, sem instalar Node e sem construir imagem:
```bash
docker run --rm -v "$PWD":/app -w /app -p 3000:3000 node:22-alpine node scripts/dev-server.mjs
```

## Deploy Vercel
O commit **precisa** ser autorado como `EsterSouza <esterposte@hotmail.com>` — a identidade Git tem
que bater com a conta conectada, senão a Vercel bloqueia o deploy (aprendido na `lp-vistoria`).
Push via alias SSH `github.com-github2`. `input/` e `*.md` ficam fora do bundle via `.vercelignore`.
