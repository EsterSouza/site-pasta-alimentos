# Guia: Teste A/B com Vercel Edge Functions + Rastreamento de Conversões

Documentação do que foi implementado neste projeto para replicar em outros.

## Arquitetura

```
Visitante acessa /
       ↓
Edge Function (api/ab.js)
       ↓
Sorteia variante (50/50) ou lê cookie "ab-variant"
       ↓
Redirect 302 → /a/ ou /b/
       ↓
Cookie gravado por 30 dias
```

### Arquivos envolvidos

| Arquivo | Função |
|---|---|
| `vercel.json` | Rewrite de `/` para `/api/ab` |
| `api/ab.js` | Edge function que sorteia e redireciona |
| `a/index.html` | Variante A |
| `b/index.html` | Variante B |

---

## 1. vercel.json

```json
{
  "rewrites": [
    { "source": "/", "destination": "/api/ab" }
  ]
}
```

## 2. Edge Function (api/ab.js)

```js
export const config = { runtime: 'edge' };

const COOKIE = 'ab-variant';

export default async function handler(request) {
  const url = new URL(request.url);
  const cookies = request.headers.get('cookie') || '';
  const match = cookies.match(new RegExp(`${COOKIE}=([ab])`));
  let variant = match ? match[1] : null;

  if (!variant) {
    variant = Math.random() < 0.5 ? 'a' : 'b';
  }

  const target = variant === 'b' ? '/b/' : '/a/';
  const headers = new Headers({ Location: new URL(target, url.origin).toString() });

  if (!match) {
    headers.append(
      'Set-Cookie',
      `${COOKIE}=${variant}; Path=/; Max-Age=${30 * 24 * 60 * 60}; SameSite=Lax`
    );
  }

  return new Response(null, { status: 302, headers });
}
```

> **IMPORTANTE:** Usar redirect 302 (não proxy/rewrite) para que o browser mude a URL. Caso contrário, o analytics só enxerga `/` e não distingue as variantes.

---

## 3. Caminhos relativos nas variantes

Como as páginas ficam em subpastas (`/a/`, `/b/`), todos os assets que estão na raiz precisam de `../`:

```html
<!-- ERRADO (quebra o CSS e imagens) -->
<link rel="stylesheet" href="style.css" />
<img src="hero.webp" />

<!-- CORRETO -->
<link rel="stylesheet" href="../style.css" />
<img src="../hero.webp" />
```

Isso vale para: CSS, imagens, links do footer (política de privacidade, termos de uso), etc.

---

## 4. Rastreamento por plataforma

### Google Analytics (GA4)

Adicionar user property `ab_variant` no gtag de cada variante:

```html
<!-- Variante A -->
gtag('set', 'user_properties', { 'ab_variant': 'a' });

<!-- Variante B -->
gtag('set', 'user_properties', { 'ab_variant': 'b' });
```

No GA4, segmentar relatórios por essa propriedade. O path `/a/` vs `/b/` também aparece automaticamente.

### Hotmart

Adicionar `utm_content` diferente nos links de checkout de cada variante:

```
Variante A: ...&utm_content=variante-a
Variante B: ...&utm_content=variante-b
```

No relatório de vendas da Hotmart, filtrar por `utm_content`.

### Meta Pixel

Adicionar `content_name` no evento `InitiateCheckout`:

```js
// Variante A
fbq('track','InitiateCheckout',{value:47.99,currency:'BRL',content_name:'variante-a'})

// Variante B
fbq('track','InitiateCheckout',{value:47.99,currency:'BRL',content_name:'variante-b'})
```

### Google Ads

Conversões já são rastreadas via `gtag('event','conversion',{...})` nos cliques do CTA. O GA4 user property permite cruzar com a variante.

---

## 5. Como testar

```bash
# Ver o redirect no terminal
curl -I https://seu-dominio.com/

# Deve retornar HTTP 302 com Location: /a/ ou /b/
```

No browser: abrir aba anônima, acessar o site e verificar se a URL muda para `/a/` ou `/b/`.

---

## Checklist para novo projeto

- [ ] Criar pastas `/a/` e `/b/` com as variantes
- [ ] Corrigir todos os caminhos relativos nas variantes (`../`)
- [ ] Criar `api/ab.js` com edge function de redirect 302
- [ ] Configurar `vercel.json` com rewrite de `/` para `/api/ab`
- [ ] Adicionar `utm_content=variante-a` / `variante-b` nos links de checkout
- [ ] Adicionar `ab_variant` como user property no gtag
- [ ] Adicionar `content_name` no evento do Meta Pixel
- [ ] Testar ambas as variantes (CSS, imagens, links, analytics)
