# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Users

Donos e responsáveis por serviços de alimentação: restaurantes, lanchonetes, bares, padarias,
confeitarias, buffets, cozinhas industriais, deliveries e food trucks.

**Não há gatilho dominante — os três convivem** (confirmado pelo dono):

1. **Reação** — já levou notificação ou multa, com prazo correndo.
2. **Antecipação** — vai abrir o estabelecimento, renovar alvará ou tem vistoria marcada.
3. **Uso profissional** — nutricionistas e consultores que compram para aplicar nos próprios clientes.

Consequência para trabalho futuro: urgência, planejamento e uso profissional precisam ser atendidos
na mesma página. Nenhum dos três pode ser tratado como caso secundário nem otimizado às custas dos
outros dois.

**Fora do público:** indústria de alimentos — legislação distinta da RDC 216/2004.

## Product Purpose

Entregar por download imediato a documentação sanitária que um serviço de alimentação precisa ter
organizada quando a Vigilância Sanitária aparece.

São 54 documentos editáveis em Word e Excel, conforme RDC ANVISA 216/2004: 1 Manual de Boas Práticas,
11 POPs, 7 checklists de auditoria, 24 planilhas de controle diário, 4 treinamentos de equipe, modelo
de contrato, modelo de proposta comercial e a relação de documentos.

Sucesso é o comprador abrir os arquivos, substituir os campos com os dados do próprio estabelecimento
e ter a pasta pronta no mesmo dia — sem conhecimento técnico e sem contratar ninguém.

## Positioning

**Construído por quem esteve do lado da fiscalização.** Ana Roberta Ribeiro é nutricionista com
especialização em Vigilância Sanitária e experiência em fiscalização, auditoria e gestão sanitária de
estabelecimentos. O kit reúne os documentos que o fiscal efetivamente exige e verifica numa vistoria —
não uma lista genérica de conformidade montada de fora. É a afirmação que um concorrente vendendo
modelos de documento não conseguiria copiar de forma verdadeira.

A alternativa real do comprador não é outro kit: é contratar consultoria ou não ter documentação
nenhuma. O preço (R$ 47,99) existe dentro dessa comparação.

## Operating Context

- A pasta é um objeto **físico e conferível**: o fiscal pede, folheia e verifica se os controles
  diários estão preenchidos. O produto é digital, mas o uso final é impresso e manuseado.
- O preenchimento é recorrente — 24 planilhas de controle **diário** implicam rotina de equipe, não
  um documento que se arquiva depois de pronto.
- A compra é frequentemente feita fora do horário comercial e do computador, por quem está tocando o
  estabelecimento.
- Entrega e cobrança são inteiramente da Hotmart; não há área de membros própria.

## Capabilities and Constraints

**Produto e oferta**
- Hotmart `H104875140X` — R$ 47,99 à vista ou 6x de R$ 9,00. Oferta base `off=1pu3fait`.
- Entrega por e-mail com link de download após confirmação do pagamento. Word e Excel, editáveis.
- Garantia de 7 dias, reembolso direto pela Hotmart.
- Licença de uso pessoal, para estabelecimentos sob responsabilidade do comprador. Uso em CNPJ de
  terceiros exige contato.

**Escopo legal**
- Base: RDC ANVISA nº 216/2004, norma **federal**. Exigências municipais e estaduais variam e não são
  cobertas pelo material.
- Não indicado para indústria de alimentos. Essa exclusão é afirmada hoje no site e no `llms.txt` e
  deve ser preservada.

**Técnicas**
- HTML estático (`a/index.html`, `b/index.html`) — sem framework, sem build de app. Split A/B 50/50
  por edge function (`api/ab.js`) com rewrite de `/`, então **a URL é idêntica nas duas variantes**.
- Deploy na Vercel: o commit precisa sair como `EsterSouza <esterposte@hotmail.com>`, senão a Vercel
  bloqueia. Push via alias SSH `github.com-github2`.
- Imagens somente `.webp` (`scripts/to-webp.mjs`, sharp).
- Tracking centralizado em `tracking.js` — grupo ANA: Meta Pixel `1429926872242671`, Google Ads
  `AW-18030262622`, GA4 `G-L1SR8V2ECY`, Clarity `y109t0glph` (compartilhado com outros oito repos da
  casa). Slug de página `alimentos` (usado na tag `lp_page` do Clarity); atribuição de venda por
  `sck=e2|<variante>`, onde `e2` é o código do experimento emitido pelo ERP.

**Experimento em curso**
- Experimento `e2` cadastrado no ERP. A tag `e2|<variante>` casa em
  `experimento.codigo || '|' || variante`, então a venda passa a ser atribuível por variante.
- O cookie de sorteio leva o código do experimento (`ab-e2`): teste novo re-sorteia todo mundo, em
  vez de herdar a atribuição do anterior.

## Brand Commitments

- **Nome:** Kit Pasta Sanitária para Serviço de Alimentação. Marca guarda-chuva: Consultora Sanitária.
- **Rosto e assinatura:** Ana Roberta Ribeiro — "Nutricionista | Especialista em Vigilância Sanitária".
  Instagram `@aconsultora.nutri`. A autoridade dela é o eixo da página, não um bloco de rodapé.
- **Empresa:** HUB TREINAVISA SERVIÇOS LTDA, CNPJ 53.297.694/0001-37 — Av. Embaixador Abelardo Bueno,
  1, Sala 153-D, Ed. Lagoa, Barra da Tijuca, Rio de Janeiro – RJ, 22775-022.
- **Contato:** alimentos@consultorasanitaria.com.br · WhatsApp +55 21 99031-3823.
- **Domínio:** `lp-pasta-alimentos.consultorasanitaria.com.br`.
- **Limite de comunicação confirmado:** nunca prometer **aprovação garantida na vistoria**. O kit
  organiza a documentação; a aprovação é decisão do fiscal. Vale para headline, CTA, prova e microcópia.

## Evidence on Hand

- **"+100 estabelecimentos aprovados"** — confirmado pelo dono como **número real e sustentável**.
  Já usado no hero e na meta description; pode ser trabalhado e ampliado.
- **Foto real da autora:** `foto-ana.webp`.
- **Imagens de contexto de uso:** `restaurante.webp`, `padaria.webp`, `buffet.webp`, `ifood.webp`,
  `hero-v3.webp`, `img-problema.webp`.
- **Inventário conferido:** 54 arquivos exatos, verificado no OneDrive (registro do catálogo interno).
- **Não existe hoje e não pode ser inventado:** depoimento de cliente, estudo de caso, print de
  aprovação, nota ou avaliação, selo de terceiro, menção de imprensa, número de alunos.

## Product Principles

1. **Os três gatilhos convivem.** Quem chega com multa na mão, quem está abrindo e o consultor
   comprando para clientes veem a mesma página. Otimizar só para o pânico perde os outros dois.
2. **A promessa para no fiscal.** O kit garante documentação organizada, nunca o resultado da
   vistoria. Toda copy futura respeita essa fronteira.
3. **Autoridade vem de dentro da fiscalização.** O diferencial é a origem do material — quem já
   auditou sabe o que é pedido. Isso é conteúdo, não selo decorativo.
4. **Zero conhecimento técnico.** O comprador abre no Word e preenche. Qualquer coisa que sugira
   trabalho de especialista contradiz o produto.
5. **A pasta é usada, não arquivada.** Controles diários implicam rotina de equipe — o material vive
   impresso, preenchido à mão e conferido por terceiro.
