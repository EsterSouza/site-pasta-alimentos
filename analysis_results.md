# Análise da Landing Page — Kit Pasta Sanitária
## vs. Skill `landing-page-generator` + Skills Complementares

---

## 1. Checklist da Skill `landing-page-generator`

| Critério | Status | Detalhe |
|----------|--------|---------|
| **Copy Framework (PAS/AIDA/BAB)** | ⚠️ Parcial | A LP usa parcialmente o PAS (Problema → Agitação → Solução), mas falta uma seção de *agitação* mais clara entre o Problema e a Solução. O hero não aponta a dor diretamente no H1 como a skill recomenda. |
| **Hero — variante correta** | ⚠️ Parcial | Usa o layout **Split** (texto + imagem), que é um dos 5 da skill. Porém falta: (a) gradiente de fundo com blur/glow decorativo, (b) micro-texto de prova social ("Mais de X profissionais…"), (c) botão secundário (ex: "Ver conteúdo completo →"). |
| **Feature Section** | ✅ OK | As abas (tabs) funcionam como feature section organizada por categorias. |
| **Pricing Table** | ⚠️ Ausente na LP atual | Existe no CSS (`sec-price-v3`) mas não está renderizado no HTML. A skill recomenda ter pricing visível com trust signals próximas. |
| **FAQ com Schema Markup** | ❌ Faltando | O FAQ existe e funciona, mas **não tem `FAQPage` JSON-LD**. A skill exige schema markup no FAQ. |
| **Testimonials** | ❌ Ausente | Seção de depoimentos/testemunhos não existe na LP atual. Existe CSS (`sec-testimonials`) mas sem HTML. |
| **CTA Banner/Final** | ✅ OK | Seção final com headline + CTA + preço. Bem feita. |
| **Footer** | ✅ OK | Simples com contato, links legais e disclaimer. |
| **SEO: `<title>` (50-60 chars)** | ✅ OK | "Kit Pasta Sanitária · 50+ documentos editáveis para a Vigilância Sanitária" — 74 chars ⚠️ (levemente acima, idealmente encurtar) |
| **SEO: Meta description (150-160)** | ✅ OK | 156 chars — dentro do ideal. |
| **SEO: OG Image** | ❌ Faltando | Não há meta `og:image`, `og:title`, `og:description` ou `twitter:card`. |
| **SEO: H1 único** | ✅ OK | Apenas 1 `<h1>`: "SUA PASTA SANITÁRIA PRONTA." |
| **SEO: Structured Data** | ❌ Faltando | Sem JSON-LD (Product, FAQPage ou Organization). |
| **SEO: Canonical URL** | ❌ Faltando | Sem `<link rel="canonical">`. |
| **SEO: Alt text em imagens** | ✅ OK | Todas as imagens têm `alt` text. |
| **SEO: robots.txt / sitemap** | ❌ Faltando | Não há `robots.txt` nem `sitemap.xml` no diretório. |
| **Performance: LCP < 1s** | ⚠️ Risco | [hero.png](file:///c:/Users/miche/OneDrive%20-%20MSFT/TreinaVISA/site/site-pasta-sanitaria/hero.png) (5.9 MB!) carregada como `eager` no mockup. Pesadíssima. Usar WebP otimizado. |
| **Performance: CLS < 0.1** | ⚠️ Risco | Imagens sem `width`/`height` explícitos em vários locais (mockup, cards Netflix). |
| **Mobile viewport** | ✅ OK | Meta viewport presente. |
| **Design Style definido** | ✅ OK | Usa um estilo "Dark SaaS" adaptado (navy + lilac), coerente. |
| **CTA above-the-fold mobile** | ✅ OK | Sticky CTA no mobile + botão no hero. |

---

## 2. Problemas Críticos do Hero Atual

### 2.1. Performance das Imagens
- [hero.png](file:///c:/Users/miche/OneDrive%20-%20MSFT/TreinaVISA/site/site-pasta-sanitaria/hero.png) tem **5.9 MB** (!). Já existe [hero.webp](file:///c:/Users/miche/OneDrive%20-%20MSFT/TreinaVISA/site/site-pasta-sanitaria/hero.webp) (55 KB) mas não está sendo usada no `<img>`.
- O CSS referencia [hero.webp](file:///c:/Users/miche/OneDrive%20-%20MSFT/TreinaVISA/site/site-pasta-sanitaria/hero.webp) no fundo (`.hero__bg`), mas esse elemento (`hero__bg`) nem existe no HTML — existe `hero__bg_solid` (fundo sólido).

### 2.2. Design do Hero — Oportunidades
O hero atual é funcional mas **não impressiona visualmente**:

| Aspecto | Situação Atual | Recomendação |
|---------|---------------|--------------|
| **Fundo** | Sólido navy `#0A1F44` sem profundidade | Adicionar gradiente sutil ou glow atrás do mockup |
| **Elementos decorativos** | SVGs de ícones (panela, colher, termômetro, luva) com 6% opacidade | Pouco visíveis; considerar partículas flutuantes ou padrão geométrico sutil |
| **Mockup** | Imagem crua sem efeito | Adicionar sombra profunda, brilho de borda, reflexo sutil |
| **Gradiente sobre mockup** | Linear simples da esquerda | Melhorar para dar mais atmosfera e profundidade |
| **Badge/Tag** | Borda lilac simples | OK mas poderia ter animação de pulso no dot |
| **Micro-prova social** | Não existe | Falta um elemento como "✓ 380+ profissionais já baixaram" |
| **Tipografia** | Playfair Display 80px — boa | OK, manter |

### 2.3. Copy do Hero
- O H1 "SUA PASTA SANITÁRIA PRONTA." é bom mas não segue o framework PAS.
- Pela PAS, o H1 deveria apontar a **dor**: ex. "A Vigilância pode chegar a qualquer momento. Você está pronto?"
- O subtítulo é informativo mas não cria **urgência**.

---

## 3. Skills Recomendadas para Melhorar a LP

### 🔥 Prioridade Alta — Impacto Direto no Hero

#### 3.1. `design-spells`
**Para quê:** Adicionar micro-interações "mágicas" ao hero.
- Animação de entrada suave no H1 (stagger letter-by-letter ou word-by-word)
- Efeito de pulso no badge "PARA SERVIÇOS DE ALIMENTAÇÃO"
- Hover magnético no botão CTA
- Parallax sutil nos ícones SVG decorativos ao mover o mouse
- Efeito de glow pulsante atrás do mockup

#### 3.2. `antigravity-design-expert`  
**Para quê:** Dar profundidade visual ao hero com técnicas de "weightlessness".
- Sombras diffusas no mockup para parecer "flutuar"
- Glassmorphism no badge ou em elementos decorativos
- Parallax leve entre layers (fundo → ícones → texto → mockup)
- Animação de scroll-triggered nas seções seguintes

#### 3.3. `image-studio`
**Para quê:** Gerar/melhorar o mockup do hero.
- Criar novo mockup profissional com o produto (pasta/documentos)
- Gerar imagem realista estilo "mesa de trabalho com documentos organizados"
- Upscale criativo das imagens existentes
- Converter imagens pesadas (5.9 MB PNG → WebP otimizado)

---

### ⚡ Prioridade Média — Melhoria Geral da LP

#### 3.4. `seo` (Audit Completo)
**Para quê:** Corrigir todas as lacunas de SEO identificadas:
- Adicionar Open Graph tags (`og:image`, `og:title`, etc.)
- Gerar JSON-LD: `Product`, `FAQPage`, `Organization`
- Criar `canonical URL`
- Criar `robots.txt` e `sitemap.xml`
- Otimizar `<title>` (74 → ≤60 chars)

#### 3.5. `seo-meta-optimizer`
**Para quê:** Otimizar meta tags com variações A/B.
- Gerar 3-5 variações de `<title>` e `meta description`
- Incluir power words e emotional triggers
- Adequar para display mobile (truncation)

#### 3.6. `ad-creative`
**Para quê:** Melhorar os textos de CTA e copy dos botões.
- Gerar variações do copy de CTA: "QUERO MEU KIT AGORA" vs alternativas
- Aplicar ângulos diferentes (urgência, prova social, dor, identidade)
- Melhorar micro-copy do sticky CTA mobile

---

### 💡 Prioridade Baixa — Polimento Premium

#### 3.7. `brainstorming`
**Para quê:** Facilitar decisões de design antes de implementar.
- Estruturar a discussão sobre direção do hero (qual variante?)
- Definir tom de voz (PAS vs BAB vs AIDA)
- Validar suposições sobre o público-alvo

#### 3.8. `canvas-design`
**Para quê:** Se desejar criar assets visuais premium (banners OG, thumbnails).
- Criar OG image profissional (1200×630px)
- Criar assets visuais para compartilhamento social

---

## 4. Elementos Faltantes na LP (vs. Skill)

| Seção | Status | Ação |
|-------|--------|------|
| **Pricing (Preço visível)** | ❌ HTML ausente | Reativar a seção de preço que existe no CSS (`sec-price-v3`) |
| **Testimonials** | ❌ HTML ausente | Adicionar depoimentos (mesmo placeholder marcados) |
| **Prova Social** | ❌ Sem | Adicionar número de compradores ou depoimentos |
| **Trust Signals próx. CTA** | ⚠️ Parcial | Selos de garantia e Hotmart existem no CSS mas não no HTML |
| **Garantia visível** | ⚠️ Parcial | Mencionada no FAQ mas sem destaque visual |

---

## 5. Resumo de Ações Prioritárias

1. **URGENTE — Performance:** Trocar [hero.png](file:///c:/Users/miche/OneDrive%20-%20MSFT/TreinaVISA/site/site-pasta-sanitaria/hero.png) (5.9 MB) por [hero.webp](file:///c:/Users/miche/OneDrive%20-%20MSFT/TreinaVISA/site/site-pasta-sanitaria/hero.webp) (55 KB) no HTML
2. **URGENTE — SEO:** Adicionar OG tags, JSON-LD (FAQPage + Product), canonical URL
3. **HERO — Design:** Ativar skills `design-spells` + `antigravity-design-expert` para micro-animações e profundidade visual
4. **HERO — Copy:** Reescrever H1 seguindo o framework PAS (dor → agitação → solução)
5. **LP — Seções faltantes:** Reativar Pricing e Testimonials que existem no CSS mas não no HTML
6. **Assets — `image-studio`:** Criar mockup profissional e OG image
7. **Meta — `seo-meta-optimizer`:** Otimizar title tag (encurtar para 60 chars) e gerar variações
