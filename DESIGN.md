---
name: Kit Pasta Sanitária — Alimentos
description: Navy institucional e lilás sereno em torno de uma janela de arquivos que mostra o produto antes da compra.
colors:
  navy: "#0A1F44"
  navy-deep: "#060F24"   # token no CSS desde a amplificação da faixa; antes era literal no rodapé
  lilac: "#7B61C4"
  lilac-deep: "#6449B0"
  lilac-pale: "#C9B8E8"
  lilac-mist: "#F5F3FA"
  off-white: "#F0F5F1"
  near-black: "#1A1A1A"
  ink-soft: "#333333"
  white: "#FFFFFF"
  alert-red: "#D4321F"
  ink-muted: "#555555"
  whatsapp-green: "#25D366"
  chrome-window: "rgba(28, 28, 36, 0.97)"
  chrome-titlebar: "rgba(55, 55, 65, 0.95)"
  chrome-surface: "#EBEBEB"
  chrome-panel: "#F8F9FA"
  chrome-divider: "#EEEEEE"
  chrome-border: "#DDDDDD"
  chrome-border-alt: "#CCCCCC"
  chrome-shadow: "rgba(0,0,0,0.1)"
  chrome-mac-red: "#FF5F57"
  chrome-mac-yellow: "#FFBD2E"
  chrome-mac-green: "#28C840"
  chrome-mac-green-alt: "#27C93F"
  chrome-word: "#2B5EBF"
  chrome-excel: "#1E7E45"
  chrome-pdf: "#D93025"
  # chrome-g1 removido: a faixa não cita mais o g1 (fonte agora é a nota da Prefeitura)
typography:
  display:
    fontFamily: "Playfair Display, Georgia, serif"
    fontSize: "80px"
    fontWeight: 700
    lineHeight: 1
  display-mobile:
    fontFamily: "Playfair Display, Georgia, serif"
    fontSize: "60px"
    fontWeight: 700
    lineHeight: 1
  headline:
    fontFamily: "Inter, sans-serif"
    fontSize: "clamp(40px, 6vw, 76px)"
    fontWeight: 900
    lineHeight: 1.1
    letterSpacing: "-2px"
  headline-mobile:
    fontFamily: "Inter, sans-serif"
    fontSize: "42px"
    fontWeight: 900
    lineHeight: 1.1
    letterSpacing: "-1px"
  headline-sub:
    fontFamily: "Inter, sans-serif"
    fontSize: "clamp(28px, 4vw, 48px)"
    fontWeight: 900
    lineHeight: 1.1
    letterSpacing: "-0.5px"
  headline-sub-mobile:
    fontFamily: "Inter, sans-serif"
    fontSize: "32px"
    fontWeight: 900
    lineHeight: 1.1
  title:
    fontFamily: "Inter, sans-serif"
    fontSize: "44px"
    fontWeight: 800
    lineHeight: 1.2
  title-lg:
    fontFamily: "Inter, sans-serif"
    fontSize: "48px"
    fontWeight: 900
    lineHeight: 1.2
  title-sm:
    fontFamily: "Inter, sans-serif"
    fontSize: "40px"
    fontWeight: 800
    lineHeight: 1.2
  title-mobile:
    fontFamily: "Inter, sans-serif"
    fontSize: "36px"
    fontWeight: 900
    lineHeight: 1.2
  subtitle:
    fontFamily: "Inter, sans-serif"
    fontSize: "20px"
    fontWeight: 500
    lineHeight: 1.6
  card-title:
    fontFamily: "Inter, sans-serif"
    fontSize: "22px"
    fontWeight: 700
    lineHeight: 1.3
  body:
    fontFamily: "Inter, sans-serif"
    fontSize: "1.1rem"
    fontWeight: 400
    lineHeight: 1.6
  body-base:
    fontFamily: "Inter, sans-serif"
    fontSize: "18px"
    fontWeight: 400
    lineHeight: 1.6
  body-alt:
    fontFamily: "Inter, sans-serif"
    fontSize: "1rem"
    fontWeight: 400
    lineHeight: 1.6
  list:
    fontFamily: "Inter, sans-serif"
    fontSize: "16px"
    fontWeight: 400
    lineHeight: 1.6
  label:
    fontFamily: "Inter, sans-serif"
    fontSize: "14px"
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: "0.01em"
  label-alt:
    fontFamily: "Inter, sans-serif"
    fontSize: "13px"
    fontWeight: 600
    lineHeight: 1.4
  label-sm:
    fontFamily: "Inter, sans-serif"
    fontSize: "12px"
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: "1.5px"
  micro:
    fontFamily: "Inter, sans-serif"
    fontSize: "10px"
    fontWeight: 400
    lineHeight: 1.2
rounded:
  xs: "2px"
  sm: "4px"
  md: "6px"
  lg: "8px"
  xl: "12px"
  xxl: "20px"
  full: "50%"
  chip: "3px"
  none: "0"
spacing:
  xs: "8px"
  sm: "12px"
  md: "16px"
  lg: "24px"
  xl: "32px"
  xxl: "48px"
  section: "80px"
  section-mobile: "56px"
components:
  button-primary:
    backgroundColor: "{colors.lilac}"
    textColor: "{colors.white}"
    rounded: "{rounded.md}"
    padding: "18px 36px"
  button-primary-hover:
    backgroundColor: "{colors.lilac-deep}"
  button-hero:
    backgroundColor: "{colors.lilac}"
    textColor: "{colors.white}"
    rounded: "{rounded.md}"
    padding: "20px 48px"
  button-price:
    backgroundColor: "{colors.lilac}"
    textColor: "{colors.white}"
    rounded: "{rounded.lg}"
    padding: "22px"
    width: "100%"
  chip-tab:
    backgroundColor: "{colors.lilac-mist}"
    textColor: "{colors.navy}"
    rounded: "{rounded.md}"
    padding: "12px 24px"
  chip-tab-active:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.off-white}"
  pill-trust:
    backgroundColor: "rgba(201,184,232,0.08)"
    textColor: "{colors.lilac-pale}"
    rounded: "{rounded.sm}"
    padding: "8px 18px"
  badge-quiet:
    backgroundColor: "rgba(201,184,232,0.08)"
    textColor: "{colors.lilac-pale}"
    rounded: "{rounded.sm}"
    padding: "8px 20px"
  card-price:
    backgroundColor: "rgba(255,255,255,0.04)"
    textColor: "{colors.white}"
    rounded: "{rounded.xxl}"
    padding: "48px"
---

# Design System: Kit Pasta Sanitária — Alimentos

## Overview

**Creative North Star: "O Arquivo Aberto"**

O sistema existe para resolver uma desconfiança específica: ninguém compra 54 documentos que não pode
ver. Por isso a peça central não é uma promessa — é uma **janela de arquivos**, inclinada em 3D no
hero, rolando os nomes reais dos POPs e das planilhas. O navy é o arquivo fechado; o lilás é a linha
selecionada dentro dele. Todo o resto do sistema se organiza em torno desse gesto: mostrar o conteúdo
antes de pedir a decisão.

O caráter é **técnico, mas acolhedor**. O rigor vem do navy dominante, da hierarquia firme e do
vocabulário de janela de sistema operacional — pontos de semáforo, ícones de extensão, linhas de
arquivo. O acolhimento vem do lilás e do serif Playfair, que entram justamente onde o comprador
precisa sentir que há uma pessoa do outro lado: o nome da Ana, o título das perguntas, o número do
preço. O sistema nunca intimida quem não é técnico, porque o produto se vende exatamente por não
exigir conhecimento técnico.

A superfície alterna deliberadamente entre escuro e claro, e essa alternância é estrutural, não
decorativa: navy onde o sistema afirma (hero, para-quem, preço), claro onde ele explica (problema,
conteúdo, autoridade, FAQ). O vermelho é o único elemento de urgência e aparece contado.

**Key Characteristics:**
- Janela de arquivos como prova de conteúdo, não como ilustração
- Alternância escuro/claro marcando afirmação versus explicação
- Lilás como única cor interativa do sistema
- Serif pontual sobre sans pesado — três aparições por página, no máximo
- Base tipográfica de 18px: `1rem` vale 18px, não 16px
- Interação tátil: sobe, brilha na própria cor, respira

## Colors

Uma paleta fria e institucional aquecida por uma única família de lilás, com vermelho reservado
exclusivamente à urgência.

### Primary
- **Lilás Confiança** (`#7B61C4`): a única cor interativa do sistema. Todo CTA, todo link de rodapé,
  o divisor do hero e o rótulo de função da Ana. Se algo é clicável, é lilás.
- **Lilás Profundo** (`#6449B0`): exclusivamente o estado `:hover` do lilás. Nunca aparece em repouso.
- **Lilás Sereno** (`#C9B8E8`): o lilás sobre fundo escuro — bordas de badge, texto de pílula de
  prova, o número grande do preço, a palavra que digita no hero. É o lilás legível no navy.
- **Névoa Lilás** (`#F5F3FA`): fundo das seções claras de explicação (problema, autoridade). Um
  cinza que puxa para o roxo, e não para o azul.

### Secondary
- **Vermelho de Alerta** (`#D4321F`): urgência real, e só ela — hoje reduzido a **uma** aparição, o
  marca-texto da palavra "multa" na seção do problema. Nunca é fundo, nunca compete com o lilás por
  clique. O valor foi escurecido do `#E63B2E` original porque branco sobre ele media 4,18:1 e falhava
  o WCAG AA; em `#D4321F` mede 4,91:1.

### Neutral
- **Navy Arquivo** (`#0A1F44`): o chão dominante. Fundo do hero, da grade de segmentos e do bloco de
  preço; cor de todos os `h2` sobre fundo claro; fundo do chip de aba ativo.
- **Navy Fundo de Gaveta** (`#060F24`): apenas o rodapé — um degrau abaixo do navy, fechando a página.
- **Off-White Sereno** (`#F0F5F1`): texto sobre navy. Tem um leve viés verde que o separa do branco
  puro e evita o contraste duro de `#FFF` sobre azul escuro.
- **Preto Suave** (`#1A1A1A`): corpo de texto sobre fundo claro.
- **Tinta Branda** (`#333333`): parágrafos secundários nas seções de explicação.
- **Branco** (`#FFFFFF`): fundo das seções de conteúdo e FAQ, e texto dentro de botões.

### Paleta de cromo (componente, não marca)

Estas cores não pertencem à identidade — elas **imitam um sistema operacional e
aplicativos reais**, e é justamente esse realismo que faz a janela de arquivos funcionar como prova.
Existem só dentro do componente:

- **Semáforo do macOS** (`#FF5F57`, `#FFBD2E`, `#28C840`): os três pontos da barra de título.
- **Cores de aplicativo** — Word (`#2B5EBF`), Excel (`#1E7E45`), PDF (`#D93025`): os ícones de tipo
  de arquivo. São as cores dos programas de verdade; alterá-las quebra o reconhecimento.
- **Superfícies da janela** (`rgba(28,28,36,0.97)`, `rgba(55,55,65,0.95)` na encarnação escura;
  `#EBEBEB`, `#F8F9FA`, `#EEEEEE` na clara).
- ~~**Vermelho do g1** (`#C4170C`)~~: **removido.** A faixa de notícia deixou de citar o g1 quando a
  fonte passou a ser a nota oficial da Prefeitura do Rio. A etiqueta da fonte hoje usa o Navy da
  própria página: reproduzir o azul institucional de um órgão numa página de venda puxa para o lado
  de parecer peça oficial, o contrário do que o aviso da seção afirma. Ela nomeia a fonte sem imitar
  a marca dela — e por isso o vermelho aparece uma vez só na página, no selo.

**A Regra do Cromo Emprestado.** Nenhuma cor desta lista pode migrar para fora da janela de arquivos.
O vermelho do PDF não é um vermelho de marca; o verde do Excel não é um verde de sucesso. Elas são
citações de outro software, e perdem o sentido — e ganham ruído — fora do componente que as cita.

### Named Rules

**A Regra da Voz Única.** O lilás é a única cor interativa. Nada mais no sistema pode sinalizar
"clique aqui" — nem o vermelho, nem o verde do WhatsApp, nem o navy. Um segundo tom clicável divide a
atenção e a página tem um só objetivo.

**A Regra do Vermelho Contado.** O vermelho aparece no máximo duas vezes por página, sempre como
estado (selo, verificação), nunca como superfície. No momento em que virar fundo de botão, deixa de
significar urgência e passa a significar "infoproduto".

## Typography

**Display Font:** Playfair Display (com Georgia, serif)
**Body Font:** Inter (com sans-serif)

**Character:** Inter carrega o peso institucional em `900` e `800` — headlines apertadas, com
`letter-spacing` negativo, que soam firmes sem gritar. Playfair entra em três momentos exatos e
funciona como pontuação humana: o nome da autora, o título das perguntas e o número do preço. É o
serif que impede o sistema de virar um painel administrativo.

A base é **18px**, declarada em `html`, então `1rem` vale 18px e `1.1rem` vale 19,8px. Qualquer
cálculo futuro em `rem` precisa partir daí, não dos 16px habituais.

### Hierarchy
- **Display** (Playfair 700, 80px, line-height 1): apenas o número da parcela no card de preço. Em
  mobile cai para 60px.
- **Headline** (Inter 900, `clamp(40px, 6vw, 76px)`, line-height 1.1, tracking -2px): a primeira
  linha do hero — a que anima. As linhas de apoio ficam em `clamp(28px, 4vw, 48px)` com tracking
  -0,5px, deliberadamente menores.
- **Title** (Inter 800, 40–48px): os `h2` de seção, sempre em navy sobre claro ou off-white sobre
  navy.
- **Body** (Inter 400/500, 1.1rem, line-height 1.6): parágrafos e itens de lista.
- **Label** (Inter 600, 14px, tracking 0,01em, caixa e acentuação normais): o degrau dominante —
  rodapé, selos, badge do hero, rótulo de função, `.ntf-content`.
- **Label-sm** (Inter 700, 12px, tracking 1,5px, caixa alta): reservado a etiquetas de até quatro
  palavras — selo do preço, cromo da janela de arquivos.

### Named Rules

**A Regra do Playfair Contado.** O serif aparece no máximo três vezes por página. Ele marca o humano
e o preço; espalhado, vira enfeite e o contraste com o Inter se dissolve.

**A Regra da Caixa Alta Curta.** Caixa alta só em rótulos de até quatro palavras, sempre com
`letter-spacing` de 1,5px ou mais. Frase inteira em caixa alta é o registro de LP agressiva que este
sistema recusa.

### A escala real, e o que nela é débito

Os degraus acima **descrevem o CSS como ele é hoje**, não como deveria ser. São 21 tamanhos distintos
numa única página, e vários são redundantes:

| Redundância | Situação |
|---|---|
| `18px` e `1rem` | **O mesmo valor.** A base é 18px, então `1rem` = 18px. Dois nomes, um degrau. |
| `1.1rem` (19,8px) e `20px` | Separados por 0,2px — diferença invisível, decisão sem intenção. |
| `40px` · `42px` · `44px` · `48px` | Quatro degraus de título em oito pixels de intervalo. |
| `32px` e `36px` | Aglomerado de título em mobile, mesma função. |
| `13px` e `14px` | Dois rótulos pequenos onde um bastaria. |

**A grafia dupla das cores foi resolvida.** O CSS escrevia o mesmo branco de dois jeitos (`#FFF` e
`#FFFFFF`) e a mesma tinta de dois jeitos (`#333` e `#333333`). Hoje `ink-soft`, `ink-muted`,
`chrome-border` e `chrome-border-alt` são tokens de verdade no `:root`, e nenhum literal de cor com
token equivalente sobrou fora dele. Verificado por comparação das cores computadas de 671 elementos
antes e depois: **zero divergências**.

**O que ainda é dívida de cor:** 38 declarações `rgba()` repetem à mão um token com opacidade —
`rgba(240,245,241,0.8)` é o off-white a 80%. A técnica já está decidida para quando isso for feito:
canais RGB (`--off-white-rgb: 240, 245, 241`), pela compatibilidade com navegadores antigos.

**Isto é dívida, não sistema.** Uma escala com propósito teria cerca de oito degraus com saltos
perceptíveis. Consolidar exige refatorar o CSS e revalidar a página inteira — trabalho de
`/impeccable typeset`, não de documentação. Até lá, este documento diz a verdade sobre o código em
vez de fingir uma escala que não existe.

**A Regra do Degrau Perceptível.** Tamanho novo só entra se a diferença for visível a olho nu contra
o degrau vizinho. `1.1rem` ao lado de `20px` é a prova do que acontece quando essa regra não vale.

## Layout

Contêiner único de **1200px** com respiro lateral de 24px, centralizado. As seções respiram
verticalmente por um token só — `--section-pad-v`, 80px no desktop e 56px abaixo de 768px.

As grades são deliberadamente assimétricas e cada uma tem uma proporção própria, que carrega
significado: o hero divide **55/45** (texto ganha do visual); o problema divide **60/40** (o texto
domina, a imagem ilustra); a autoridade inverte para **40/60** (a foto da Ana ganha presença antes do
texto). A grade de segmentos é o único módulo simétrico — quatro colunas iguais, porque os quatro
públicos têm o mesmo peso.

**Responsivo em três degraus.** Em **1024px** todas as grades assimétricas colapsam para uma coluna,
o hero centraliza o texto e a janela do Finder **desaparece** — ela é uma peça de desktop e não tenta
se espremer. A grade de segmentos vai a duas colunas. Em **768px** o padding de seção cai para 56px,
a headline afrouxa o tracking para -1px e os botões passam a ocupar a largura toda. Em **480px** os
segmentos viram coluna única.

Um CTA fixo aparece no rodapé da viewport ao rolar, e o botão do WhatsApp flutua acima dele — por
isso o rodapé reserva 120px de padding inferior, para que nada fique sob os elementos fixos.

## Elevation & Depth

O sistema é **quase plano no claro e dramático no escuro** — mas hoje isso acontece por acaso, não
por escala. Os valores em produção divergem entre si (tinta navy num lugar, preto puro noutro,
sombra direcional só na janela do Finder). A escala abaixo é a normalização a adotar; a lista de
divergências no fim é débito a corrigir.

A profundidade sobre fundo claro é tingida de **navy**, nunca de preto puro: sombra preta sobre
`#F5F3FA` suja o roxo e cria um cinza morto.

### Shadow Vocabulary
- **Repouso** (`box-shadow: 0 10px 30px rgba(10,31,68,0.05)`): cartões e listas em repouso sobre
  fundo claro. Quase imperceptível — a borda faz mais trabalho que a sombra.
- **Flutuante** (`box-shadow: 0 16px 40px rgba(10,31,68,0.10)`): a janela de documentos e qualquer
  superfície que precise se destacar do fundo claro.
- **Elevado** (`box-shadow: 0 24px 48px rgba(10,31,68,0.16)`): o degrau mais forte sobre claro.
  Reservado a elemento único por seção.
- **Sobre Navy** (`box-shadow: 0 32px 64px rgba(0,0,0,0.5)`): a única sombra que usa preto puro,
  porque tinta navy sobre navy é invisível. Vale para o card de preço e equivalentes.
- **Brilho Interativo** (`box-shadow: 0 8px 24px rgba(123,97,196,0.4)`): resposta de hover em
  elementos primários. Escala para `0 16px 40px rgba(123,97,196,0.35)` no botão do hero.

### Named Rules

**A Regra da Luz de Cima.** A sombra cai reta para baixo, sem deslocamento horizontal.

**A Regra do Brilho Colorido.** Interação nunca escurece: ela ilumina na própria cor do elemento.
Hover em botão lilás produz brilho lilás, jamais uma sombra preta mais forte. E o brilho tem
deslocamento e desfoque — halo de raio zero (`0 0 0 15px`) é decoração, não profundidade, e foi por
isso que os pulsos infinitos saíram.

**A Regra do Momento Único.** A página tem **um** movimento autoral: a entrada escalonada do hero e a
palavra que digita no `h1`. Fora isso, **nada anima em repouso** — os quatro halos pulsantes saíram
por isso. A janela de arquivos é a exceção **declarada**, e a razão é de natureza, não de licença:
ela não é um elemento animado, é uma **gravação de tela** embutida na página, e gravação roda em
laço. Quem pede `prefers-reduced-motion` recebe a página parada, com a headline já escrita e a janela
imóvel no topo da lista.

**Estado:** as três divergências registradas na primeira versão deste documento foram pagas — a
janela de documentos e o botão do WhatsApp passaram a tinta navy, e o `drop-shadow` do hero perdeu o
deslocamento horizontal.

## Shapes

O raio cresce com a importância da superfície, e essa progressão é legível: **2px** nas etiquetas de
extensão, **4px** em badges e pílulas, **6px** em botões e chips, **8px** no botão de preço, **12px**
em cartões, imagens e itens de FAQ, **20px** no card de preço — o mais arredondado do sistema,
porque é o único que precisa parecer um objeto e não um bloco. Círculo pleno só em pontos de status e
no botão flutuante.

Bordas são finas e coloridas, quase sempre em lilás com transparência (`1.5px solid` em itens de FAQ
e no card de preço, `1px` em listas). Sobre navy, a borda vira lilás translúcido a 25–50% — ela
delimita sem cortar.

A silhueta recorrente do sistema é a **janela**: barra de título, três pontos de semáforo, corpo
rolável. Ela aparece duas vezes, em dois climas — escura e inclinada no hero, clara e reta na seção
de conteúdo.

## Components

### Buttons
- **Shape:** cantos suaves de 6px (`--rounded-md`); o botão de preço abre para 8px por ocupar a
  largura toda.
- **Primary:** fundo Lilás Confiança, texto branco, peso 800, `18px 36px`, tracking 0,02em. A
  variante do hero cresce para 20px de fonte e `20px 48px`.
- **Hover:** fundo escurece para Lilás Profundo, o elemento sobe 2px e ganha brilho lilás
  (`0 8px 24px rgba(123,97,196,0.4)`), em `0.3s cubic-bezier(0.25,0.46,0.45,0.94)`. Todos sobem os
  mesmos 2px — nenhum escala.
- **Focus:** anel de 3px em Lilás Sereno com `outline-offset: 3px`, via `:focus-visible`. Dentro das
  abas e do FAQ, sobre fundo claro, o anel vira Lilás Confiança.
- **Mobile:** abaixo de 768px todo botão ocupa 100% da largura, com padding 16px e fonte 1rem.
- **Débito conhecido:** a classe `.btn-dark-cta`, usada no CTA da seção da autoridade, **não existe
  no CSS** — aquele botão renderiza como primário lilás. Ou a variante escura é implementada, ou a
  classe sai do HTML.

### Badges e selos
- **Style:** fundo `rgba(201,184,232,0.08)`, texto Lilás Sereno, borda 1px em lilás a 35%, raio 4px.
  Uma linguagem só para o badge do hero, a pílula de prova e o selo do card de preço — nenhum deles é
  bloco de cor sólida.

### Chips (abas de conteúdo)
- **Style:** fundo Névoa Lilás, texto navy, borda 1px em Lilás Sereno, raio 6px, `12px 24px`, peso 700.
- **State:** ativo inverte para fundo navy com texto off-white e borda navy. Dentro da janela clara
  de documentos, o repouso vira fundo branco com borda `#ccc` e texto `#555`.

### Cards / Containers
- **Corner Style:** 12px para cartões de segmento, imagens e itens de FAQ; 20px no card de preço.
- **Background:** branco ou Névoa Lilás no claro; `rgba(255,255,255,0.04)` sobre navy — vidro, não
  bloco sólido.
- **Shadow Strategy:** ver Elevation. Repouso no claro, Sobre Navy no escuro.
- **Border:** `1.5px` em Lilás Sereno nos elementos que precisam de contorno próprio (FAQ, preço).
- **Internal Padding:** 48px no card de preço (32px 24px em mobile), 24px em itens de FAQ.

### Navigation
Não há navegação persistente — a página é uma coluna única de rolagem, com âncoras internas. O
substituto é o **CTA fixo**: aparece ao rolar, fundo navy a 98% com `backdrop-filter: blur(10px)`,
borda superior de 2px em lilás, entrando por `translateY` em 0.4s.

### Signature Component — A Janela de Arquivos
A peça que define o sistema, em duas encarnações:

**Escura (hero).** Janela `rgba(28,28,36,0.97)`, raio 12px, borda branca a 13%, com a sombra em
`box-shadow` na própria janela — nunca `filter` no pai, que achata o 3D e apaga o elemento no Firefox. Barra de título com os três pontos do macOS (`#FF5F57`, `#FFBD2E`, `#28C840`); a linha
destacada usa lilás a 30%. Ícones de tipo de arquivo carregam as cores dos aplicativos reais — Word
`#2B5EBF`, PDF `#D93025`, Excel `#1E7E45`.

**É uma gravação de tela, não um widget.** A lista percorre o conteúdo a **100px/s** — cerca de 2,7
linhas por segundo, ritmo em que ainda se leem os nomes —, pausa no fim, rebobina e recomeça. Ciclo
de ~29s, igual em qualquer largura, porque o que está sendo retratado é a mesma tela.

**Sem cursor e sem encenação.** O componente já teve um ponteiro que caminhava até um arquivo e
clicava antes de a lista rolar. Foi removido: a encenação atrasava o que interessa e o ponteiro
competia com o conteúdo pela atenção. **O assunto da gravação é a lista de arquivos correndo** — é
ela que prova o que o comprador está levando. Uma linha permanece destacada, como um arquivo
selecionado numa pasta aberta de verdade.

**Só documentos, nada de contêiner.** A janela lista exatamente **54 linhas — os 54 documentos**, um
para um com o número anunciado na página. A linha da pasta que os continha foi removida: ela não é
um item do kit, inflava a contagem de quem confere, e seu ícone era o emoji `📁` fazendo as vezes de
ícone. Toda linha da janela tem de ser um arquivo que o comprador recebe.

O laço é **baseado em tempo**, não em quadros: um passo fixo por frame correria ao dobro num monitor
de 120Hz.

Só a moldura muda com a largura: no desktop ela ganha a inclinação
`perspective(1000px) rotateY(-4deg) rotateX(2deg)` e lista de 480px; abaixo de 1024px fica reta, com
lista de 260px, abaixo do CTA porque não há espaço acima da dobra.

**A Regra da Vitrine Fechada.** A lista **nunca** é rolável pelo usuário: `overflow: hidden`
obrigatório. A janela fica no caminho do scroll da página, e um contêiner rolável ali captura o dedo
do visitante por ~2.500px de conteúdo antes de a página voltar a andar — foi exatamente o defeito que
`overflow-y: auto` com `overscroll-behavior: contain` produziu em produção. Rolagem programática
segue funcionando com `overflow: hidden`; é ela que anima a gravação.

**Clara (conteúdo).** A mesma silhueta, sem inclinação: barra `#EBEBEB`, corpo branco, abas no topo
e rodapé `#F8F9FA`. Aqui a janela é navegável de verdade, com as abas trocando o conteúdo.

O realismo é o argumento — os nomes de arquivo são reais. Falsificar o conteúdo dessa janela quebra a
única prova que a página oferece.

### Faixa de Notícia (variante B)

Prova social do **problema**, não do produto: uma fiscalização real, citada.

**O título mede uma linha, não um degrau da escala.** "Num único dia, na Zona Sul do Rio." tem oito
palavras; a 44px ela quebrava e deixava "do Rio." sozinho numa segunda linha a 25% da largura da
coluna. A 36px cabe inteira (576px de 603px). O tamanho saiu da medição da frase real, não do topo
da escala — e `text-wrap: balance` cobre as larguras onde a coluna estreita e a quebra volta.

**Ela afirma, então vive no escuro.** O chão é Navy Fundo de Gaveta (`#060F24`), um degrau abaixo do
hero. O bloco continua o mesmo compasso — "a fiscalização não avisa" seguido da prova disso — e só
depois a página quebra para o claro, onde explica a exigência legal. Duas seções claras coladas se
borravam numa só; duas escuras em degraus diferentes leem como uma passagem contínua.

**São dois painéis, não um cartão e um texto.** A leitura tem chão próprio: Navy (`#0A1F44`), o
mesmo do hero, um degrau acima do Navy Fundo de Gaveta da seção. Sem ele o texto encostava direto no
fundo enquanto o recorte ao lado era um objeto com superfície, e a dupla lia torta. Sendo dois
painéis, eles dividem a aresta de cima (`align-items: start`) — a mesma escolha da seção da
especialista, onde a coluna de texto também é bem mais alta que o objeto ao lado.

**A colagem: a foto é o chão, o recorte pousa sobre ela.** Foto e título vêm da mesma nota oficial da
Prefeitura do Rio (SEOP / IVISA-Rio), e o crédito ao lado diz isso. A fonte é o poder público, não um
veículo de imprensa — o que muda tanto o que a página pode afirmar quanto o que ela precisa negar.

**A foto é recorte da fotografia, nunca o card inteiro.** O material de origem vem como um card
completo, com título e resumo já tipografados. Usá-lo como imagem transformaria o texto da seção em
pixel: não escala, não é lido por leitor de tela, não entra em busca. O card é remontado em HTML e
só a fotografia vira imagem, no mesmo `aspect-ratio` do slot para o `cover` não cortar de novo.

**Os números ficam na leitura, não no recorte.** A nota oficial traz 11 fiscalizados, 10 multados e
~R$ 4 mil por multa já no próprio resumo. Repeti-los dentro do recorte e de novo ao lado faria a
seção dizer a mesma coisa duas vezes, em duas vozes. O recorte cita o título; a leitura conta os
números. A composição existe porque o recorte sozinho media 309px contra 607px da
coluna de texto e ficava pequeno demais; empilhado sobre a foto, a diferença cai para 72px.

**O selo `Interditado` é grafismo editorial, e a página admite isso na legenda.** Ele é
deliberadamente tipográfico — sem brasão, sem nome de órgão — porque ler como lacre oficial
sugeriria envolvimento da Vigilância Sanitária, que é o que o aviso da seção nega. A chapa branca
sob o vermelho não é decoração: sobre foto o contraste é incontrolável, e só ela garante a
legibilidade mesmo que a imagem por baixo seja preta (4,20:1, contra os 3:1 exigidos).

**As avaliações são seção própria, na posição 3.** Antes viviam dentro do texto da especialista, e o
bloco lia como uma coisa só. Como seção, elas ganham chão branco — a seção seguinte já é Névoa
Lilás, e duas iguais coladas se borrariam numa só, então o ritmo fica navy-deep → branco → névoa.

A coluna é contida em 760px e centrada: o container serve a duas colunas, e uma citação atravessando
1150px estoura a linha de leitura. A 19,8px isso dá 77 caracteres por linha, dentro da faixa
confortável. O título fica a 32px, um degrau abaixo do problema (40px) e das abas (44px) — a seção
credencia, não faz o pitch, e não deve competir com eles.

**A nota de origem saiu por decisão do dono.** Com ela foi embora a única menção de que as avaliações
vêm do Google. O que segura a honestidade agora é só o título — "O que dizem sobre a **consultoria**"
—, que continua dizendo que os relatos não são sobre o kit. Se o título mudar, a ressalva precisa
voltar em algum lugar, senão quatro cinco-estrelas numa página de venda passam a ler como prova do
produto.

**A Regra da Citação Intocada.** Texto de avaliação real nunca é editado para caber na página. Uma
das avaliações citava "Ester" — sócia da Treinavisa, mas não a profissional que a página apresenta.
Trocar o nome resolveria a estranheza e produziria um depoimento falso, ainda por cima checável
contra o original, que segue público no Google. **A avaliação foi removida, não reescrita.** Quando
um relato verdadeiro não serve à página, ele sai; o que não acontece é ele mudar de texto para
servir. Restam duas avaliações, e a seção ficou menor — esse é o preço, e é o preço certo.

**A Regra da Foto Creditada.** Imagem de terceiro nesta página só entra com origem declarada ao lado
dela, e qualquer marcação nossa sobre ela é identificada como nossa.

**O recorte é um documento claro sobre o escuro** — o mesmo papel que a janela de arquivos cumpre no
hero, e a mesma sombra `Sobre Navy`. Etiqueta do veículo, filete navy sob o cabeçalho, manchete entre
aspas a 28px. Não é screenshot: é a citação tipografada na voz da página.

**O vermelho vive dentro do recorte, nunca sobre o navy.** Sobre o escuro ele mede 3,31:1 e reprova
no AA; sobre o branco do recorte, 4,91:1 e passa. Os números da leitura seguem o precedente do valor
da parcela: Lilás Sereno sobre escuro, a 36px.

- **Os números vivem dentro da frase, nunca em caixas.** "11 estabelecimentos fiscalizados. 10 saíram
  multados. Cerca de R$ 4 mil cada multa." O craft-floor recusa o template de métrica — número grande,
  rótulo pequeno, fileira de caixas iguais —, e foi exatamente nele que a primeira versão caiu. O
  bloco de preço depois retoma esses R$ 4 mil como âncora.
- **A ressalva não é rodapé, é parte do componente.** "Não é endosso ao produto — nem o veículo nem
  a Vigilância Sanitária têm qualquer relação com este kit." Sem ela, citar jornalismo ao lado de um
  botão de compra sugere um aval que não existe.
- **A fonte é clicável e verificável.** Veículo, data e manchete literal. Um número sem link de
  volta à matéria é uma estatística inventada do ponto de vista de quem lê.

**A Regra da Notícia Emprestada.** A página pode citar um fato externo, nunca vesti-lo de aval.
Manchete entre aspas, veículo nomeado, link para a origem e a ressalva no mesmo bloco — os quatro,
sempre juntos. Retirar qualquer um transforma reportagem em endosso.

## Do's and Don'ts

### Do:
- **Do** usar o lilás (`#7B61C4`) como única cor de ação. Se um elemento novo é clicável, ele é lilás.
- **Do** tingir sombras de navy sobre fundo claro (`rgba(10,31,68,…)`) e reservar preto puro para
  superfícies sobre navy.
- **Do** responder à interação subindo 2px e iluminando na própria cor do elemento.
- **Do** alternar escuro e claro por função: navy onde a página afirma, claro onde ela explica.
- **Do** calcular medidas em `rem` a partir de **18px**, não de 16px.
- **Do** manter os nomes de arquivo da janela reais e verificáveis.
- **Do** deixar a janela do Finder sumir abaixo de 1024px em vez de comprimi-la.
- **Do** vestir as superfícies do navegador com a paleta: `::selection` em Lilás Sereno sobre navy e
  um `:focus-visible` visível. `outline: none` sem substituto é proibido.

### Don't:
- **Don't** adotar o registro de LP de lançamento agressiva: contador regressivo, setas amarelas,
  frase inteira em caixa alta, "últimas vagas". O produto é documentação séria e a autoridade da
  autora é o ativo — esse registro a destrói.
- **Don't** transformar o vermelho em fundo de botão ou em segunda cor de ação.
- **Don't** espalhar o Playfair além de três aparições por página.
- **Don't** aplicar sombra com deslocamento horizontal; a luz vem de cima.
- **Don't** usar `#FFFFFF` puro para texto corrido sobre navy — o off-white (`#F0F5F1`) existe para
  amaciar esse contraste.
- **Don't** usar animação infinita. Nenhuma. O sistema é tátil no toque, parado em repouso.
- **Don't** usar sombra de raio zero (`0 0 0 Npx`) como realce — é halo decorativo, não profundidade.
- **Don't** dar `cursor: pointer` ou hover de escala a algo que não navega para lugar nenhum.
- **Don't** introduzir uma cor de ação nova sem aposentar o lilás — o sistema tem uma voz só.
