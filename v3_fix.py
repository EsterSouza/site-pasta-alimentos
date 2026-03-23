import re

html_path = 'c:/Users/miche/OneDrive - MSFT/TreinaVISA/site/site-pasta-sanitaria/index.html'

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

changes = 0

new_hero = """<!-- ============================================================
     BLOCO 1 . HERO
============================================================ -->
<section class="hero" id="hero">
  <!-- Fundo escuro -->
  <div class="hero__bg_solid"></div>
  
  <!-- Decorações -->
  <div class="hero__deco">+50</div>
  <svg class="hero-svg pot" viewBox="0 0 24 24" stroke="#C9B8E8" fill="none" stroke-width="1" stroke-linecap="round" stroke-linejoin="round">
    <path d="M5 8h14v10a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V8z"></path>
    <path d="M9 8V6a3 3 0 0 1 6 0v2"></path>
    <path d="M2 10h3"></path>
    <path d="M19 10h3"></path>
  </svg>
  <svg class="hero-svg spoon" viewBox="0 0 24 24" stroke="#C9B8E8" fill="none" stroke-width="1" stroke-linecap="round" stroke-linejoin="round">
    <path d="M16 4a4 4 0 0 0-4 4v2l-5 5-3-3l-2 2a2 2 0 0 0 2.83 2.83l2-2l-3-3l5-5h2a4 4 0 1 0-2.83-6.83l-1.42 1.42"></path>
  </svg>
  <svg class="hero-svg thermometer" viewBox="0 0 24 24" stroke="#C9B8E8" fill="none" stroke-width="1" stroke-linecap="round" stroke-linejoin="round">
    <path d="M14 14.5a3 3 0 1 1-4 0V5a2 2 0 1 1 4 0v9.5z"></path>
    <path d="M12 9v3"></path>
  </svg>
  <svg class="hero-svg gloves" viewBox="0 0 24 24" stroke="#C9B8E8" fill="none" stroke-width="1" stroke-linecap="round" stroke-linejoin="round">
    <path d="M5 10c0-1.8 1.4-3.2 3.2-3.2s3.2 1.4 3.2 3.2v6.8c0 .8.6 1.4 1.4 1.4s1.4-.6 1.4-1.4v-4.5c0-.8.6-1.4 1.4-1.4s1.4.6 1.4 1.4v2.5c0 .8.6 1.4 1.4 1.4s1.4-.6 1.4-1.4V4c0-.8.6-1.4 1.4-1.4s1.4.6 1.4 1.4v14.5c0 2.5-2 4.5-4.5 4.5h-5C6.4 23 4 20.6 4 17.6V10c0-.8.6-1.4 1.4-1.4S6.8 9.2 6.8 10v4"></path>
  </svg>

  <div class="container hero__inner">
    <div class="hero__text">
      <div class="hero__badge">
        <span class="dot"></span> PARA SERVIÇOS DE ALIMENTAÇÃO
      </div>
      <h1 class="hero__headline">
        SUA PASTA<br>SANITÁRIA<br><span>PRONTA.</span>
      </h1>
      <p class="hero__sub">
        Mais de 50 documentos editáveis em Word: POPs, planilhas, checklists e treinamentos exigidos pela Vigilância Sanitária.
      </p>
      <div class="hero__divider"></div>
      
      <a href="https://pay.hotmart.com/H104875140X?checkoutMode=10&utm_source=landing&utm_medium=organico&utm_campaign=kit-pasta-sanitaria"
         target="_blank" rel="noopener" class="btn-cta hero-btn" id="cta-hero"
         onclick="fbq('track','InitiateCheckout')">
        QUERO MEU KIT AGORA
      </a>
      <span class="hero__micro">Acesso imediato. Mais de 50 arquivos em Word.</span>
    </div>

    <!-- Coluna Direita com a Imagem -->
    <div class="hero__mockup-cols">
      <div class="hero__gradient-overlay"></div>
      <img src="hero.png" alt="Kit Pasta Sanitária Mockup" loading="eager" />
    </div>
  </div>
</section>
"""

new_problem = """<!-- ============================================================
     BLOCO 2 . O PROBLEMA
============================================================ -->
<section class="sec-problem" id="problema">
  <div class="container">
    <div class="problem-grid">
      <div class="problem-img-col">
        <img src="img 1.png" alt="Fiscalizando restaurante" loading="lazy" />
      </div>
      <div class="problem-text">
        <h2>A vistoria da VISA não avisa quando chega.</h2>
        <p>Restaurantes, lanchonetes, padarias e buffets estão sujeitos à fiscalização sem agendamento. O fiscal chega, pede os documentos e registra cada ausência.</p>
        <p>A RDC ANVISA 216/2004 exige POPs, Manual de Boas Práticas, planilhas de controle e registros de capacitação. Não ter esses documentos gera notificação.</p>
        <a href="https://pay.hotmart.com/H104875140X?checkoutMode=10&utm_source=landing&utm_medium=organico&utm_campaign=kit-pasta-sanitaria" target="_blank" rel="noopener" class="btn-cta btn-small-cta" style="margin-top:24px;">VER O KIT COMPLETO</a>
      </div>
    </div>
  </div>
</section>
"""

new_tabs = """<!-- ============================================================
     BLOCO 3 e 4 .  A SOLUÇÃO + CONTEÚDO (ABAS)
============================================================ -->
<section class="sec-tabs" id="conteudo">
  <div class="container">
    <div class="tabs-header">
      <h2>O que você recebe no kit</h2>
      <p class="subtitle">Mais de 50 documentos organizados por categoria</p>
    </div>
    
    <div class="tabs-nav">
      <button class="tab-btn active" data-target="tab1">POPs (11)</button>
      <button class="tab-btn" data-target="tab2">Planilhas (14)</button>
      <button class="tab-btn" data-target="tab3">Checklists (7)</button>
      <button class="tab-btn" data-target="tab4">Treinamentos e Modelos</button>
    </div>

    <div class="tabs-content">
      <!-- ABA 1 -->
      <div class="tab-pane active" id="tab1">
        <ul class="tab-list scrollable">
          <li><svg viewBox="0 0 24 24" fill="none" stroke="#7B61C4" stroke-width="2" width="16"><path d="M20 6L9 17l-5-5"></path></svg> POP 01 Armazenamento de Alimentos na Refrigeração</li>
          <li><svg viewBox="0 0 24 24" fill="none" stroke="#7B61C4" stroke-width="2" width="16"><path d="M20 6L9 17l-5-5"></path></svg> POP 02 Controle de Amostras</li>
          <li><svg viewBox="0 0 24 24" fill="none" stroke="#7B61C4" stroke-width="2" width="16"><path d="M20 6L9 17l-5-5"></path></svg> POP 03 Controle de Vetores e Pragas Urbanas</li>
          <li><svg viewBox="0 0 24 24" fill="none" stroke="#7B61C4" stroke-width="2" width="16"><path d="M20 6L9 17l-5-5"></path></svg> POP 04 Descongelamento</li>
          <li><svg viewBox="0 0 24 24" fill="none" stroke="#7B61C4" stroke-width="2" width="16"><path d="M20 6L9 17l-5-5"></path></svg> POP 05 Lavagem de Mãos</li>
          <li><svg viewBox="0 0 24 24" fill="none" stroke="#7B61C4" stroke-width="2" width="16"><path d="M20 6L9 17l-5-5"></path></svg> POP 06 Descarte de Óleo de Cozinha</li>
          <li><svg viewBox="0 0 24 24" fill="none" stroke="#7B61C4" stroke-width="2" width="16"><path d="M20 6L9 17l-5-5"></path></svg> POP 07 Higiene e Saúde dos Manipuladores</li>
          <li><svg viewBox="0 0 24 24" fill="none" stroke="#7B61C4" stroke-width="2" width="16"><path d="M20 6L9 17l-5-5"></path></svg> POP 08 Higienização de Hortifrutigranjeiros</li>
          <li><svg viewBox="0 0 24 24" fill="none" stroke="#7B61C4" stroke-width="2" width="16"><path d="M20 6L9 17l-5-5"></path></svg> POP 09 Higienização de Instalações, Móveis e Utensílios</li>
          <li><svg viewBox="0 0 24 24" fill="none" stroke="#7B61C4" stroke-width="2" width="16"><path d="M20 6L9 17l-5-5"></path></svg> POP 10 Higienização do Reservatório de Água</li>
          <li><svg viewBox="0 0 24 24" fill="none" stroke="#7B61C4" stroke-width="2" width="16"><path d="M20 6L9 17l-5-5"></path></svg> POP 11 Separação e Descarte de Resíduos</li>
        </ul>
      </div>

      <!-- ABA 2 -->
      <div class="tab-pane" id="tab2">
        <ul class="tab-list scrollable">
          <li><svg viewBox="0 0 24 24" fill="none" stroke="#7B61C4" stroke-width="2" width="16"><path d="M20 6L9 17l-5-5"></path></svg> Planilha Avaliação de Insumos</li>
          <li><svg viewBox="0 0 24 24" fill="none" stroke="#7B61C4" stroke-width="2" width="16"><path d="M20 6L9 17l-5-5"></path></svg> Planilha Controle de Limpeza de Instalações e Móveis</li>
          <li><svg viewBox="0 0 24 24" fill="none" stroke="#7B61C4" stroke-width="2" width="16"><path d="M20 6L9 17l-5-5"></path></svg> Planilha Controle de Limpeza de Utensílios</li>
          <li><svg viewBox="0 0 24 24" fill="none" stroke="#7B61C4" stroke-width="2" width="16"><path d="M20 6L9 17l-5-5"></path></svg> Planilha Controle de Validade de Matéria-Prima</li>
          <li><svg viewBox="0 0 24 24" fill="none" stroke="#7B61C4" stroke-width="2" width="16"><path d="M20 6L9 17l-5-5"></path></svg> Planilha de Controle da Ocorrência de Pragas e Vetores</li>
          <li><svg viewBox="0 0 24 24" fill="none" stroke="#7B61C4" stroke-width="2" width="16"><path d="M20 6L9 17l-5-5"></path></svg> Planilha de Controle da Qualidade do Óleo</li>
          <li><svg viewBox="0 0 24 24" fill="none" stroke="#7B61C4" stroke-width="2" width="16"><path d="M20 6L9 17l-5-5"></path></svg> Planilha de Controle da Temperatura de Resfriamento</li>
          <li><svg viewBox="0 0 24 24" fill="none" stroke="#7B61C4" stroke-width="2" width="16"><path d="M20 6L9 17l-5-5"></path></svg> Planilha de Controle de Amostras</li>
          <li><svg viewBox="0 0 24 24" fill="none" stroke="#7B61C4" stroke-width="2" width="16"><path d="M20 6L9 17l-5-5"></path></svg> Planilha de Controle de Coleta de Amostras</li>
          <li><svg viewBox="0 0 24 24" fill="none" stroke="#7B61C4" stroke-width="2" width="16"><path d="M20 6L9 17l-5-5"></path></svg> Planilha de Controle de Descongelamento</li>
          <li><svg viewBox="0 0 24 24" fill="none" stroke="#7B61C4" stroke-width="2" width="16"><path d="M20 6L9 17l-5-5"></path></svg> Planilha de Controle de Dosagem de Cloro</li>
          <li><svg viewBox="0 0 24 24" fill="none" stroke="#7B61C4" stroke-width="2" width="16"><path d="M20 6L9 17l-5-5"></path></svg> Planilha de Controle de Temperatura de Equipamentos</li>
          <li><svg viewBox="0 0 24 24" fill="none" stroke="#7B61C4" stroke-width="2" width="16"><path d="M20 6L9 17l-5-5"></path></svg> Planilha de Controle de Validade de ASOs</li>
          <li><svg viewBox="0 0 24 24" fill="none" stroke="#7B61C4" stroke-width="2" width="16"><path d="M20 6L9 17l-5-5"></path></svg> Planilha de Controle no Transporte de Mercadorias</li>
          <li><svg viewBox="0 0 24 24" fill="none" stroke="#7B61C4" stroke-width="2" width="16"><path d="M20 6L9 17l-5-5"></path></svg> Planilha de Limpeza Diária</li>
          <li><svg viewBox="0 0 24 24" fill="none" stroke="#7B61C4" stroke-width="2" width="16"><path d="M20 6L9 17l-5-5"></path></svg> Planilha de Recebimento</li>
          <li><svg viewBox="0 0 24 24" fill="none" stroke="#7B61C4" stroke-width="2" width="16"><path d="M20 6L9 17l-5-5"></path></svg> Planilha de Temperatura dos Alimentos na Distribuição</li>
          <li><svg viewBox="0 0 24 24" fill="none" stroke="#7B61C4" stroke-width="2" width="16"><path d="M20 6L9 17l-5-5"></path></svg> Planilha de Temperatura dos Equipamentos</li>
          <li><svg viewBox="0 0 24 24" fill="none" stroke="#7B61C4" stroke-width="2" width="16"><path d="M20 6L9 17l-5-5"></path></svg> Planilha de Troca de Esponja</li>
          <li><svg viewBox="0 0 24 24" fill="none" stroke="#7B61C4" stroke-width="2" width="16"><path d="M20 6L9 17l-5-5"></path></svg> Planilha de Verificação de Temperatura da Geladeira</li>
          <li><svg viewBox="0 0 24 24" fill="none" stroke="#7B61C4" stroke-width="2" width="16"><path d="M20 6L9 17l-5-5"></path></svg> Planilha de Visita Técnica por Área</li>
          <li><svg viewBox="0 0 24 24" fill="none" stroke="#7B61C4" stroke-width="2" width="16"><path d="M20 6L9 17l-5-5"></path></svg> Planilha Higiene Pessoal</li>
          <li><svg viewBox="0 0 24 24" fill="none" stroke="#7B61C4" stroke-width="2" width="16"><path d="M20 6L9 17l-5-5"></path></svg> Planilhas de Controle de Higienização</li>
        </ul>
      </div>

      <!-- ABA 3 -->
      <div class="tab-pane" id="tab3">
        <ul class="tab-list scrollable">
          <li><svg viewBox="0 0 24 24" fill="none" stroke="#7B61C4" stroke-width="2" width="16"><path d="M20 6L9 17l-5-5"></path></svg> Checklist de Documentos e Segurança Alvará dos Bombeiros</li>
          <li><svg viewBox="0 0 24 24" fill="none" stroke="#7B61C4" stroke-width="2" width="16"><path d="M20 6L9 17l-5-5"></path></svg> Checklist Armazenamento</li>
          <li><svg viewBox="0 0 24 24" fill="none" stroke="#7B61C4" stroke-width="2" width="16"><path d="M20 6L9 17l-5-5"></path></svg> Checklist Auditoria</li>
          <li><svg viewBox="0 0 24 24" fill="none" stroke="#7B61C4" stroke-width="2" width="16"><path d="M20 6L9 17l-5-5"></path></svg> Checklist Controle da Potabilidade da Água</li>
          <li><svg viewBox="0 0 24 24" fill="none" stroke="#7B61C4" stroke-width="2" width="16"><path d="M20 6L9 17l-5-5"></path></svg> Checklist Controle de Saúde de Manipuladores</li>
          <li><svg viewBox="0 0 24 24" fill="none" stroke="#7B61C4" stroke-width="2" width="16"><path d="M20 6L9 17l-5-5"></path></svg> Checklist Controle Manutenção Preventiva e Calibração</li>
          <li><svg viewBox="0 0 24 24" fill="none" stroke="#7B61C4" stroke-width="2" width="16"><path d="M20 6L9 17l-5-5"></path></svg> Checklist de Controle de Vetores e Pragas</li>
        </ul>
      </div>

      <!-- ABA 4 -->
      <div class="tab-pane" id="tab4">
        <ul class="tab-list scrollable">
          <li><svg viewBox="0 0 24 24" fill="none" stroke="#7B61C4" stroke-width="2" width="16"><path d="M20 6L9 17l-5-5"></path></svg> Manual de Boas Práticas</li>
          <li><svg viewBox="0 0 24 24" fill="none" stroke="#7B61C4" stroke-width="2" width="16"><path d="M20 6L9 17l-5-5"></path></svg> Modelo Contrato</li>
          <li><svg viewBox="0 0 24 24" fill="none" stroke="#7B61C4" stroke-width="2" width="16"><path d="M20 6L9 17l-5-5"></path></svg> Modelo Proposta</li>
          <li><svg viewBox="0 0 24 24" fill="none" stroke="#7B61C4" stroke-width="2" width="16"><path d="M20 6L9 17l-5-5"></path></svg> Registro de Capacitação de Manipuladores</li>
          <li><svg viewBox="0 0 24 24" fill="none" stroke="#7B61C4" stroke-width="2" width="16"><path d="M20 6L9 17l-5-5"></path></svg> Registro de Manutenção e Trocas de Filtros</li>
          <li><svg viewBox="0 0 24 24" fill="none" stroke="#7B61C4" stroke-width="2" width="16"><path d="M20 6L9 17l-5-5"></path></svg> Registro de Manutenção Preventiva e Corretiva</li>
          <li><svg viewBox="0 0 24 24" fill="none" stroke="#7B61C4" stroke-width="2" width="16"><path d="M20 6L9 17l-5-5"></path></svg> Relação de Documentos Pasta Sanitária em UAN</li>
          <li><svg viewBox="0 0 24 24" fill="none" stroke="#7B61C4" stroke-width="2" width="16"><path d="M20 6L9 17l-5-5"></path></svg> Tábuas para Cada Tipo de Alimento</li>
          <li><svg viewBox="0 0 24 24" fill="none" stroke="#7B61C4" stroke-width="2" width="16"><path d="M20 6L9 17l-5-5"></path></svg> Treinamento de Controle de Temperatura</li>
          <li><svg viewBox="0 0 24 24" fill="none" stroke="#7B61C4" stroke-width="2" width="16"><path d="M20 6L9 17l-5-5"></path></svg> Treinamento de Emergências e Prevenção de Incêndios</li>
          <li><svg viewBox="0 0 24 24" fill="none" stroke="#7B61C4" stroke-width="2" width="16"><path d="M20 6L9 17l-5-5"></path></svg> Treinamento de Higiene Pessoal</li>
          <li><svg viewBox="0 0 24 24" fill="none" stroke="#7B61C4" stroke-width="2" width="16"><path d="M20 6L9 17l-5-5"></path></svg> Treinamento de Manejo de Resíduos e Desperdício Zero</li>
        </ul>
      </div>
    </div>
    
    <p class="tab-anchor-phrase">Todos os arquivos em Word. Você edita, coloca o nome do estabelecimento e está pronto para a vistoria.</p>
    <div class="center-btn">
      <a href="https://pay.hotmart.com/H104875140X?checkoutMode=10&utm_source=landing&utm_medium=organico&utm_campaign=kit-pasta-sanitaria" class="btn-cta btn-dark-cta" target="_blank" rel="noopener" style="margin-top:32px; display:inline-block;">QUERO TODO ESSE CONTEÚDO AGORA</a>
    </div>
    
  </div>
</section>
"""

new_whom = """<!-- ============================================================
     BLOCO 5 . PARA QUEM É
============================================================ -->
<section class="sec-whom-netflix" id="para-quem">
  <div class="container">
    <h2 class="ntf-title">Para quem é este kit?</h2>
    
    <div class="ntf-grid">
      <div class="ntf-card">
        <img class="ntf-img" src="restaurante.jpg" alt="Restaurantes" loading="lazy" />
        <div class="ntf-overlay"></div>
        <div class="ntf-content">
          <h3>Restaurantes</h3>
          <p>Do fast food ao fine dining</p>
        </div>
      </div>
      <div class="ntf-card">
        <img class="ntf-img" src="padaria.jpg" alt="Padarias e Confeitarias" loading="lazy" />
        <div class="ntf-overlay"></div>
        <div class="ntf-content">
          <h3>Padarias e Confeitarias</h3>
          <p>Produção, atendimento e vendas</p>
        </div>
      </div>
      <div class="ntf-card">
        <img class="ntf-img" src="buffet.jpg" alt="Buffets e Eventos" loading="lazy" />
        <div class="ntf-overlay"></div>
        <div class="ntf-content">
          <h3>Buffets e Eventos</h3>
          <p>Produção em escala com conformidade</p>
        </div>
      </div>
      <div class="ntf-card">
        <img class="ntf-img" src="ifood.webp" alt="Cozinhas e Delivery" loading="lazy" />
        <div class="ntf-overlay"></div>
        <div class="ntf-content">
          <h3>Cozinhas e Delivery</h3>
          <p>Dark kitchens e food service</p>
        </div>
      </div>
    </div>
    
    <p class="ntf-bottom">Se você prepara ou serve alimentos para terceiros, a Vigilância Sanitária pode chegar ao seu estabelecimento.</p>
    <div class="center-btn" style="margin-top:24px;">
      <a href="https://pay.hotmart.com/H104875140X?checkoutMode=10&utm_source=landing&utm_medium=organico&utm_campaign=kit-pasta-sanitaria" class="btn-cta hero-btn" target="_blank" rel="noopener">GARANTIR MEU KIT AGORA</a>
    </div>
  </div>
</section>
"""

# Let's perform replacements safely
# HERO:
html = re.sub(r'<!-- =+\s*BLOCO 1[^<]*<section class="hero[^>]*>.*?</section>', new_hero, html, flags=re.DOTALL)
if new_hero in html: changes += 1

# PROBLEMA:
html = re.sub(r'<!-- =+\s*BLOCO 2[^<]*<section class="sec-problem[^>]*>.*?</section>', new_problem, html, flags=re.DOTALL)
if new_problem in html: changes += 1

# SOLUÇÃO & CONTEÚDO (Blocos 3 e 4):
html = re.sub(r'<!-- =+\s*BLOCO 3[^<]*<section class="sec-solution[^>]*>.*?</section>', '', html, flags=re.DOTALL)
html = re.sub(r'<!-- =+\s*BLOCO 4[^<]*<section class="sec-detail[^>]*>.*?</section>', new_tabs, html, flags=re.DOTALL)
if new_tabs in html: changes += 1

# PARA QUEM É:
html = re.sub(r'<!-- =+\s*BLOCO 5[^<]*<section class="sec-whom[^>]*>.*?</section>', new_whom, html, flags=re.DOTALL)
if new_whom in html: changes += 1

# Write back HTML if changes applied
with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
print(f'Done rewriting! Changes applied logic executed. Modifications verified: {changes}')
