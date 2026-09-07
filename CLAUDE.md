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
`<script defer src="../tracking.js?v=1">`. **Não duplicar o bloco dentro dos HTMLs** — era assim
antes, e a duplicação literal é o que produz drift.

- `sck=alimentos|<variante>` — pipe, sem `_` (a Hotmart reserva `_` para o sistema), ≤30 chars.
  Chega no webhook em `purchase.origin.sck`.
- `utm_*` de origem paga repassados ao checkout → alimentam o Hotmart Analytics. A Hotmart **não**
  envia UTM no webhook.
- `xcod=alimentos|<variante>|<campaign.id>|<ad.id>` → é o que leva os IDs do anúncio até o webhook.
  Emitido só quando há campanha ou anúncio.
- A variante sai do `data-variant` do `<html>`, com o cookie `ab-alimentos` como fallback.
- Clarity recebe `lp_page` e `ab_variant` — o rewrite de `/` deixa a URL idêntica em A e B, então
  sem essas tags não há como separar as variantes no painel.

## Pendências conhecidas
- **Atribuição de venda no ERP está órfã.** O ERP casa a venda por `site.codigo == sck` ou por
  `experimento.codigo || '|' || variante`. Não há experimento cadastrado para este produto
  (`experimentos_ativos: []`), então `alimentos|a` não casa com nada. O `xcod` faz o dado *chegar*,
  mas o relatório por página/variante depende desse cadastro. Há também **dois registros de site**
  para o mesmo host (`lp7` e `lp4`, um com `www.` e outro sem) — conferir qual é o bom.
- **`xcod` não foi confirmado em payload real.** Documentado na ajuda da Hotmart como o caminho que
  chega no webhook, mas ainda não verificado aqui. Conferir o `payload_bruto` de uma transação de
  teste antes de confiar no dado — foi o que se fez com o `sck` (confirmado em prod 2026-07-30).
- **Imagens:** 22 rasters grandes soltos na raiz.

## Deploy Vercel
O commit **precisa** ser autorado como `EsterSouza <esterposte@hotmail.com>` — a identidade Git tem
que bater com a conta conectada, senão a Vercel bloqueia o deploy (aprendido na `lp-vistoria`).
Push via alias SSH `github.com-github2`. `input/` e `*.md` ficam fora do bundle via `.vercelignore`.
