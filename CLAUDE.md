# site-pasta-alimentos — repo-rascunho estático (linha da Ana)

> Doc de orientação. Convenções completas em [`../CONVENTIONS.md`](../CONVENTIONS.md) e
> [`../TRACKING.md`](../TRACKING.md).

## Status: **A APOSENTAR** ⚠️
- **Não é Next.js** — é HTML estático (`a/index.html`, `b/index.html`, split via `api/ab.js`).
  Sem `package.json` de app, sem `next.config`.
- Provável **sucessor:** `lp-pasta-personalizada-alimentos` (mesmo produto/linha, já em Next).
- **Decisão pendente do dono:** privatizar / arquivar / aposentar. Está **fora do escopo** da
  arquitetura A/B e do starter (que são para os apps Next).

## Grupo de tracking: **ANA**
- Meta Pixel `1429926872242671` · Google Ads `AW-18030262622` · GA4 `G-L1SR8V2ECY`. Slug: `alimentos`.

## Se for mantido temporariamente (não vale reescrever)
- **Deploy Vercel (aprendido na `lp-vistoria`):** se ainda publicar na Vercel, o commit tem que ser
  autorado como `EsterSouza <esterposte@hotmail.com>` — senão a Vercel **bloqueia o deploy**. Mas a
  prioridade aqui é **aposentar**, não manter.
- Hoje a variante vai em `utm_content=variante-a/b` (a Hotmart **ignora** no relatório de origem) e
  os UTMs são fixos. O correto seria **`sck=alimentos|<variante>`** (pipe, sem `_`) no link
  `pay.hotmart.com` — mas, dado que o repo será aposentado, **priorizar a decisão de descontinuar**
  em vez de refatorar.
- Produto Hotmart aqui: `H104875140X` (diverge do catálogo do app sucessor).
- Imagens: 22 rasters gigantes soltos na raiz (compartilhados com o `lp-pasta-personalizada-alimentos`).
