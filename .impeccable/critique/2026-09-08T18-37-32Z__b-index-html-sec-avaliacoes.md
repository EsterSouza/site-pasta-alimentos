---
target: b/index.html — .sec-avaliacoes + reveal.js
total_score: 23
max_score: 32
na_heuristics: 7,10
p0_count: 0
p1_count: 3
timestamp: 2026-09-08T18-37-32Z
slug: b-index-html-sec-avaliacoes
---
⚠️ DEGRADED: single-context (subagentes não usados por instrução permanente da sessão; além disso a saída do detector já havia sido vista antes do Assessment A, então o julgamento estava ancorado)

## Design Health Score

| # | Heurística | Nota | Questão principal |
|---|-----------|-------|-----------|
| 1 | Visibilidade do status | 2 | A seção afirma "avaliações públicas no Google" e não oferece nenhum caminho para verificar |
| 2 | Correspondência com o mundo real | 4 | O card reproduz o do Google, resposta do proprietário inclusive; "há 1 mês" em linguagem natural |
| 3 | Controle e liberdade | 2 | Não há saída para a fonte nem para ver as demais avaliações |
| 4 | Consistência e padrões | 3 | Estrelas em lilás contradizem a própria justificativa de "cromo emprestado" |
| 5 | Prevenção de erro | 2 | A resposta truncada segue marcada `data-conferir` e pode subir sem conferência |
| 6 | Reconhecer em vez de lembrar | 4 | Formato reconhecível à primeira vista |
| 7 | Flexibilidade e eficiência | n/a | Superfície Persuade, sem fluxo a acelerar |
| 8 | Estético e minimalista | 3 | Limpo; só 1 dos 4 cards tem resposta, o que deixa o conjunto assimétrico |
| 9 | Recuperação de erro | 3 | Reveal é fail-open e tem prazo de segurança; sobra a janela "armou e quebrou" |
| 10 | Ajuda e documentação | n/a | Superfície Persuade |
| **Total** | | **23/32** | **Precisa de trabalho** |

## Veredito de especificidade

**Avaliação sem âncora:** o widget é específico deste produto por um motivo que não é decorativo — ele adota o formato de citação do Google pela mesma lógica que a página já usa duas vezes (a janela de arquivos do macOS no hero, o recorte da nota oficial). Isso é coerência de sistema, não cópia.

Mas há uma **contradição interna**: eu justifiquei o card dizendo "copiar o cromo para que a fonte seja reconhecível" e, em seguida, troquei as estrelas de amarelo para lilás — que é justamente o elemento mais reconhecível de uma avaliação. Ou o argumento vale e as estrelas são amarelas, ou o argumento não vale e o card inteiro precisa de outra defesa. Do jeito que está, o sistema ganhou e a citação perdeu, sem que a decisão fosse tomada de propósito.

**Varredura determinística:** 1 achado no markup (`b/index.html:56`, `overused-font: inter`) — decisão pendente e conhecida, não regressão. No CSS: 3 achados, sendo `side-tab` já registrado como exceção sancionada em `.impeccable/config.json` e 2 do mesmo Inter.

**Overlays visuais:** não executados. A mutação de DOM funciona, mas o painel do navegador não compõe quadros neste ambiente (screenshot expira em 5s, `visibilityState: hidden`, rAF em 0 quadros), então um overlay injetado seria invisível para o usuário — subir o live-server para isso não produziria sinal.

## Impressão geral

O widget resolve o problema que motivou o pedido: a seção tinha 568px de lista magra e agora tem 805px com substância por item. A resposta da consultoria é o melhor achado da referência e foi trazida.

A maior oportunidade é uma só e conserta três coisas ao mesmo tempo: **os cards não levam a lugar nenhum.**

## O que está funcionando

- **A resposta aninhada.** É o que faz o bloco ler como print do Google em vez de peça de marketing. Nenhum concorrente que fabrica depoimento tem isso.
- **O fail-open do reveal.** A referência esconde 24 elementos e devolve por JS; se o script falha, some o H1 e o botão de compra. Aqui nada nasce invisível: verificado nos três cenários, incluindo "JS nunca rodou".
- **A sombra é a do sistema.** `Flutuante`, tingida de navy, caindo reta para baixo — em vez de importar o `shadow-lg` preto do Tailwind da referência.

## Questões prioritárias

**[P1] Os cards afirmam uma fonte verificável e não linkam para ela**
- *Por que importa:* a página inteira se sustenta em citação conferível — o recorte da nota tem "Ver a nota oficial da Prefeitura". Aqui a nota diz "avaliações públicas no Google, reproduzidas na íntegra" e o visitante não tem como checar. É a única afirmação da página que pede confiança cega.
- *Correção:* transformar cada card em link para a avaliação no Google, ou no mínimo um "Ver no Google" ao pé da seção.
- *Comando:* `/impeccable clarify`

**[P1] Falsa affordance: os cards parecem clicáveis e não são**
- *Por que importa:* card branco elevado com sombra é vocabulário de coisa clicável. Zero elementos focáveis na seção. Quem tenta clicar não recebe resposta.
- *Correção:* a mesma do P1 acima — linkar resolve os dois. Se a decisão for não linkar, achatar a affordance (tirar a sombra, usar borda).
- *Comando:* `/impeccable polish`

**[P1] As estrelas lilás desmentem o argumento do cromo emprestado**
- *Por que importa:* não é questão de gosto, é de coerência. A regra que autoriza o card é a mesma que manda manter a cor da fonte reconhecível.
- *Correção:* decidir explicitamente. Amarelo = citação honesta e fonte reconhecível; lilás = a página fala com a própria voz e o card precisa de outra justificativa no DESIGN.md.
- *Comando:* `/impeccable colorize`

**[P2] A resposta truncada pode subir sem conferência**
- *Por que importa:* o texto veio cortado numa captura. `data-conferir` é um lembrete, não um bloqueio.
- *Correção:* confirmar o texto no Google antes de publicar, ou remover a resposta.
- *Comando:* `/impeccable harden`

**[P2] Uma resposta em quatro cards**
- *Por que importa:* a resposta é o elemento mais forte do widget e aparece em 25% dele.
- *Correção:* buscar as respostas das outras três; se não existirem, tudo bem — assimetria real é melhor que simetria fabricada.

## Bandeiras de persona

**Jordan (primeira vez):** chega na seção 3 sem saber quem é a consultoria. A nota explica, mas vem *depois* dos cards — ele lê quatro elogios a uma empresa que ainda não foi apresentada. Tenta clicar num card para ver de onde veio; nada acontece.

**Alex (cético / avaliador):** procura imediatamente a fonte. Não acha link, não acha nota média, não acha contagem total ("4 avaliações de quantas?"). Para ele, quatro depoimentos sem caminho de verificação são indistinguíveis de depoimentos fabricados — que é exatamente o oposto do que a página quis dizer.

**Dona de restaurante com multa na mão (persona do PRODUCT.md):** os quatro relatos falam de *consultoria* e *conteúdo*; nenhum fala do kit nem de vistoria. A nota admite isso honestamente, mas na posição 3 ela ainda não sabe que existe um kit. A prova chega antes do produto.

## Observações menores

- Sem estado de `:hover` nos cards — consistente com "não é clicável", inconsistente com a aparência.
- Avatares com `aria-hidden="true"` e estrelas com `role="img"` e rótulo: acessibilidade do conteúdo está correta.
- `<ul>`/`<li>` semânticos, nome acessível na seção via `aria-labelledby`. Hierarquia de títulos sem salto.
- 8 dos 12 keyframes da referência são código morto. Não trouxemos nenhum: só um `fade-in-up`, que é o que de fato carrega a página lá.

## Perguntas a considerar

- Se a prova social é sobre a consultoria e não sobre o kit, ela ganha mais na posição 3 (antes do produto existir para o leitor) ou logo depois do preço, onde a objeção é "posso confiar em quem vende isso"?
- O que uma versão confiante faria: quatro cards, ou um só, grande, com a resposta da consultoria e um link para o perfil inteiro?
- A nota de rodapé ("não se referem a este kit") protege a página ou enfraquece a prova que ela acabou de apresentar?
