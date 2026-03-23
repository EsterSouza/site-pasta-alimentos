# V3 Build Script
import re
import os

css_path = 'style.css'
html_path = 'index.html'

with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# ====================
# 1. REMOVE TRAVESSÃO (—) AND (-) WHICH COULD BE CONFUSED
# We only replace typographic em-dash and en-dash
html = html.replace('—', '.')
html = html.replace('–', '.') 

# Optional check for " - " -> ". "
html = html.replace(' - ', '. ')

# Remove any multiple periods we might have created
html = html.replace('..', '.')

# ====================
# 2. V3 NEW HERO
# We will use Regex to rip out the old Hero and replace it
# ====================

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
# Replace old hero
html = re.sub(r'<!-- ===+ BLOCO 1.*?</section>', new_hero, html, flags=re.DOTALL)


# ====================
# 3. O PROBLEMA
# ====================
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
        <a href="#conteudo" class="btn-cta btn-small-cta" style="margin-top:24px;">VER O KIT COMPLETO</a>
      </div>
    </div>
  </div>
</section>
"""
html = re.sub(r'<!-- ===+ BLOCO 2.*?</section>', new_problem, html, flags=re.DOTALL)


# ====================
# 4. SOLUÇÃO E ABAS (Fundir)
# ====================
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
      <a href="https://pay.hotmart.com/H104875140X?checkoutMode=10&utm_source=landing&utm_medium=organico&utm_campaign=kit-pasta-sanitaria" class="btn-cta btn-dark-cta" target="_blank" rel="noopener">QUERO TODO ESSE CONTEÚDO AGORA</a>
    </div>
    
  </div>
</section>
"""
# Replace bloco 3 and 4
html = re.sub(r'<!-- ===+ BLOCO 3.*?</section>', '', html, flags=re.DOTALL)
html = re.sub(r'<!-- ===+ BLOCO 4.*?</section>', new_tabs, html, flags=re.DOTALL)


# ====================
# 5. PARA QUEM É (Netflix style)
# ====================
new_whom = """<!-- ============================================================
     BLOCO 5 . PARA QUEM É
============================================================ -->
<section class="sec-whom-netflix" id="para-quem">
  <div class="container">
    <h2 class="ntf-title">Para quem é este kit?</h2>
    
    <div class="ntf-grid">
      <!-- Card 1 -->
      <div class="ntf-card">
        <img class="ntf-img" src="restaurante.jpg" alt="Restaurantes" loading="lazy" />
        <div class="ntf-overlay"></div>
        <div class="ntf-content">
          <h3>Restaurantes</h3>
          <p>Do fast food ao fine dining</p>
        </div>
      </div>
      
      <!-- Card 2 -->
      <div class="ntf-card">
        <img class="ntf-img" src="padaria.jpg" alt="Padarias e Confeitarias" loading="lazy" />
        <div class="ntf-overlay"></div>
        <div class="ntf-content">
          <h3>Padarias e Confeitarias</h3>
          <p>Produção, atendimento e vendas</p>
        </div>
      </div>
      
      <!-- Card 3 -->
      <div class="ntf-card">
        <img class="ntf-img" src="buffet.jpg" alt="Buffets e Eventos" loading="lazy" />
        <div class="ntf-overlay"></div>
        <div class="ntf-content">
          <h3>Buffets e Eventos</h3>
          <p>Produção em escala com conformidade</p>
        </div>
      </div>
      
      <!-- Card 4 -->
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
html = re.sub(r'<!-- ===+ BLOCO 5.*?</section>', new_whom, html, flags=re.DOTALL)


# ====================
# 6. SEÇÃO DE PREÇO
# ====================
new_price = """<!-- ============================================================
     BLOCO 8 . PREÇO
============================================================ -->
<section class="sec-price-v3" id="preco">
  <div class="container">
    <h2 class="price-v3-title">Sua pasta sanitária pronta hoje.</h2>
    <p class="price-v3-subtitle">Acesso imediato. Mais de 50 documentos em Word.</p>
    
    <div class="price-v3-card">
      <div class="price-v3-badge">OFERTA ESPECIAL</div>
      <ul class="price-v3-list">
        <li><svg viewBox="0 0 24 24" fill="none" stroke="#C9B8E8" stroke-width="2" width="16"><path d="M20 6L9 17l-5-5"></path></svg> 50+ documentos editáveis em Word</li>
        <li><svg viewBox="0 0 24 24" fill="none" stroke="#C9B8E8" stroke-width="2" width="16"><path d="M20 6L9 17l-5-5"></path></svg> 11 POPs conforme a RDC 216/2004</li>
        <li><svg viewBox="0 0 24 24" fill="none" stroke="#C9B8E8" stroke-width="2" width="16"><path d="M20 6L9 17l-5-5"></path></svg> 14 planilhas de controle operacional</li>
        <li><svg viewBox="0 0 24 24" fill="none" stroke="#C9B8E8" stroke-width="2" width="16"><path d="M20 6L9 17l-5-5"></path></svg> 7 checklists de auditoria</li>
        <li><svg viewBox="0 0 24 24" fill="none" stroke="#C9B8E8" stroke-width="2" width="16"><path d="M20 6L9 17l-5-5"></path></svg> Acesso vitalício ao material</li>
      </ul>
      
      <div class="price-v3-block">
        <span class="p-prefix">6x de</span>
        <span class="p-big">R$ 9,00</span>
        <span class="p-or">ou</span>
        <span class="p-cash">R$ 47,99 à vista</span>
      </div>
      
      <a href="https://pay.hotmart.com/H104875140X?checkoutMode=10&utm_source=landing&utm_medium=organico&utm_campaign=kit-pasta-sanitaria"
         target="_blank" rel="noopener" class="btn-cta price-v3-btn"
         onclick="fbq('track','InitiateCheckout')">
        GARANTIR MEU KIT AGORA
      </a>
      
      <div class="price-v3-seals">
        <!-- SVG icons -->
        <span class="seal"><svg viewBox="0 0 24 24" fill="none" stroke="#C9B8E8" stroke-width="2" width="16"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path></svg> Checkout Seguro Hotmart</span>
        <span class="seal"><svg viewBox="0 0 24 24" fill="none" stroke="#C9B8E8" stroke-width="2" width="16"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg> Satisfação Garantida</span>
        <span class="seal"><svg viewBox="0 0 24 24" fill="none" stroke="#C9B8E8" stroke-width="2" width="16"><path d="M16 12a4 4 0 0 1-8 0a4 4 0 0 1 8 0z"></path><path d="M2 12c0-5.5 4-10 10-10s10 4.5 10 10-4.5 10-10 10-10-4.5-10-10z"></path></svg> Acesso Vitalício</span>
      </div>
    </div>
  </div>
</section>
"""
# Replace Bloco 8
html = re.sub(r'<!-- ===+ BLOCO 8.*?</section>', new_price, html, flags=re.DOTALL)


# ====================
# ADD CTA TO ANA ROBERTA
# ====================
ana_cta_html = """<a href="https://pay.hotmart.com/H104875140X?checkoutMode=10&utm_source=landing&utm_medium=organico&utm_campaign=kit-pasta-sanitaria" class="btn-cta btn-dark-cta" target="_blank" rel="noopener">GARANTIR MEU KIT AGORA</a>"""
html = html.replace('<div class="authority-btns">', '<div class="authority-btns">\n          ' + ana_cta_html)
# Actually, the authority block already had a CTA, but might have been replaced. Let's make sure it's the right color.
html = re.sub(r'id="cta-autoridade"[^>]*>.*?</a', 'id="cta-autoridade" class="btn-cta btn-dark-cta"\n             onclick="fbq(\'track\',\'InitiateCheckout\')">\n            GARANTIR MEU KIT AGORA</a', html, flags=re.DOTALL)


# Add the small script for tabs
tabs_script = """
<script>
document.querySelectorAll('.tab-btn').forEach(btn => {
  btn.addEventListener('click', () => {
    // remove active from all
    document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
    document.querySelectorAll('.tab-pane').forEach(p => p.classList.remove('active'));
    
    // add to current
    btn.classList.add('active');
    document.getElementById(btn.dataset.target).classList.add('active');
  });
});
</script>
"""
if "tab-pane" not in html and "tabs-script" not in html:
    html = html.replace('</body>', tabs_script + '\n</body>')


# Write back HTML
with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)


# ====================
# WRITE CSS
# ====================
new_css = """
/* V3 NEW CSS RULES */

.hero{position:relative;background:#0A1F44;overflow:hidden;min-height:500px;display:flex;align-items:center}
.hero__bg_solid{position:absolute;inset:0;background:#0A1F44;}
.hero-svg{position:absolute;stroke-width:1px;opacity:0.06;}
.hero-svg.pot{bottom:20px;left:24px;width:120px;transform:rotate(-15deg);}
.hero-svg.spoon{top:35%;right:5%;width:80px;transform:rotate(25deg);}
.hero-svg.thermometer{top:60%;left:8%;width:60px;transform:rotate(-10deg);}
.hero-svg.gloves{top:75%;right:15%;width:90px;transform:rotate(8deg);}

.hero__inner{position:relative;z-index:2;display:grid;grid-template-columns:55fr 45fr;align-items:center;padding:0 !important; max-width:1200px;}
.hero__text{padding:100px 24px; padding-right:48px;}
.hero__badge{display:inline-flex;align-items:center;gap:8px;border:1.5px solid #C9B8E8;border-radius:100px;padding:6px 20px;color:#C9B8E8;font-size:11px;font-weight:700;letter-spacing:3px;text-transform:uppercase;margin-bottom:28px;}
.hero__badge .dot{width:6px;height:6px;border-radius:50%;background:#C9B8E8;}
.hero__headline{font-family:'Playfair Display',serif;font-size:80px !important;font-weight:700;line-height:1.0;color:#F0F5F1;letter-spacing:-1px;margin-bottom:24px;}
.hero__headline span{color:#C9B8E8;}
.hero__sub{font-family:'Inter',sans-serif;font-size:18px;line-height:1.6;color:rgba(240,245,241,0.70);max-width:480px;margin-bottom:40px;}
.hero__divider{width:48px;height:2px;background:#C9B8E8;margin-bottom:32px;}
.hero-btn{background:#7B61C4;color:#FFFFFF;font-family:'Inter',sans-serif;font-weight:700;font-size:16px;letter-spacing:1.5px;padding:18px 40px;border-radius:4px;border:none;cursor:pointer;transition:background 0.2s ease;margin-bottom:16px;display:inline-block;}
.hero-btn:hover{background:#6449B0; transform:none;}
.hero__micro{display:block;font-size:13px;color:rgba(240,245,241,0.40);}

.hero__mockup-cols{position:relative;height:100%;min-height:500px;}
.hero__gradient-overlay{position:absolute;inset:0;background:linear-gradient(to right, #0A1F44 0%, transparent 15%);z-index:1;}
.hero__mockup-cols img{width:100%;height:100%;object-fit:cover;object-position:center;position:absolute;inset:0;}

/* Problem V3 */
.problem-img-col{border-radius:0 12px 12px 0;overflow:hidden;height:480px;}
.problem-img-col img{width:100%;height:100%;object-fit:cover;display:block;}
.problem-text{padding:48px; padding-left:0;}
.problem-grid{grid-template-columns:60fr 40fr;gap:40px;}

/* Tabs V3 */
.sec-tabs{background:#F5F3FA;padding:80px 0;}
.tabs-header{text-align:center;margin-bottom:48px;}
.tabs-header h2{font-family:'Playfair Display',serif;font-size:40px;color:#0A1F44;margin-bottom:8px;}
.tabs-header .subtitle{font-family:'Inter',sans-serif;font-size:18px;color:#666666;}
.tabs-nav{display:flex;gap:8px;justify-content:center;flex-wrap:wrap;margin-bottom:32px;}
.tab-btn{background:#F5F3FA;color:#0A1F44;border:1px solid #C9B8E8;border-radius:8px;padding:10px 24px;font-weight:600;font-size:14px;cursor:pointer;}
.tab-btn.active{background:#0A1F44;color:#F0F5F1;border:1px solid #0A1F44;}
.tab-pane{display:none;}
.tab-pane.active{display:block;}
.tab-list{max-height:400px;overflow-y:auto;background:#fff;border-radius:12px;border:1px solid rgba(201,184,232,0.4);}
.tab-list::-webkit-scrollbar{width:8px;}
.tab-list::-webkit-scrollbar-thumb{background:#C9B8E8;border-radius:8px;}
.tab-list li{display:flex;align-items:center;gap:12px;padding:12px 16px;border-bottom:0.5px solid rgba(201,184,232,0.20);font-size:15px;color:#1A1A1A;}
.tab-list li:hover{background:rgba(201,184,232,0.08);}
.tab-anchor-phrase{font-family:'Inter',sans-serif;font-style:italic;font-weight:500;font-size:17px;color:#0A1F44;text-align:center;margin-top:32px;}
.center-btn{text-align:center;}
.btn-dark-cta{background:#0A1F44; color:#fff;}
.btn-dark-cta:hover{background:#000;color:#fff;}

/* For Whom Netflix */
.sec-whom-netflix{background:#0A1F44;padding:80px 0;}
.ntf-title{font-family:'Playfair Display',serif;font-size:40px;color:#F0F5F1;text-align:center;margin-bottom:48px;}
.ntf-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:16px;}
.ntf-card{height:400px;border-radius:12px;overflow:hidden;position:relative;cursor:pointer;}
.ntf-card .ntf-img{width:100%;height:100%;object-fit:cover;object-position:center;transition:transform 0.4s ease; position:absolute; inset:0;}
.ntf-overlay{position:absolute;inset:0;background:linear-gradient(to top, rgba(10,31,68,0.92) 0%, rgba(10,31,68,0.40) 50%, transparent 100%); transition:background 0.4s ease;}
.ntf-card:hover .ntf-img{transform:scale(1.04);}
.ntf-card:hover .ntf-overlay{background:linear-gradient(to top, rgba(10,31,68,1.0) 0%, rgba(10,31,68,0.60) 50%, transparent 100%);}
.ntf-content{position:absolute;bottom:0;left:0;right:0;padding:24px;z-index:2;}
.ntf-content h3{font-family:'Playfair Display',serif;font-size:22px;color:#F0F5F1;margin-bottom:8px;}
.ntf-content p{font-family:'Inter',sans-serif;font-size:14px;color:rgba(240,245,241,0.75);}
.ntf-bottom{font-family:'Inter',sans-serif;font-size:17px;color:rgba(240,245,241,0.75);text-align:center;max-width:600px;margin:32px auto 0;}

/* Price V3 */
.sec-price-v3{background:#0A1F44;padding:80px 0; color:#fff;}
.price-v3-title{font-family:'Playfair Display',serif;font-size:40px;color:#F0F5F1;text-align:center;}
.price-v3-subtitle{font-family:'Inter',sans-serif;font-size:18px;color:rgba(240,245,241,0.65);text-align:center;margin-bottom:48px; border:none;}
.price-v3-card{max-width:480px;margin:0 auto;background:rgba(255,255,255,0.05);border:1.5px solid #C9B8E8;border-radius:16px;padding:40px;text-align:center;}
.price-v3-badge{background:#7B61C4;color:#fff;font-size:11px;letter-spacing:2px;padding:6px 20px;border-radius:100px;display:inline-block;margin-bottom:24px;}
.price-v3-list{text-align:left;display:flex;flex-direction:column;gap:12px;margin-bottom:32px;}
.price-v3-list li{display:flex;align-items:center;gap:10px;font-size:15px;color:#F0F5F1;}
.price-v3-block{margin-bottom:32px;}
.p-prefix{display:block;font-family:'Inter',sans-serif;font-size:18px;color:rgba(240,245,241,0.65);}
.p-big{display:block;font-family:'Playfair Display',serif;font-weight:700;font-size:80px;color:#C9B8E8;line-height:1.0;}
.p-or{display:block;font-family:'Inter',sans-serif;font-size:16px;color:rgba(240,245,241,0.40);margin:8px 0;}
.p-cash{display:block;font-family:'Inter',sans-serif;font-weight:500;font-size:20px;color:rgba(240,245,241,0.65);}
.price-v3-btn{width:100%;display:block;background:#7B61C4;color:#fff;padding:18px;font-family:'Inter',sans-serif;font-weight:700;font-size:16px;letter-spacing:1.5px;border-radius:6px;margin-bottom:24px;}
.price-v3-btn:hover{background:#6449B0;transform:none;box-shadow:none;}
.price-v3-seals{display:flex;justify-content:center;gap:24px;}
.price-v3-seals .seal{display:flex;align-items:center;gap:6px;font-size:12px;color:rgba(240,245,241,0.50);}

/* Mobile V3 Overrides */
@media(max-width:767px){
  .hero__inner{grid-template-columns:1fr; padding-block:0;}
  .hero__text{padding:60px 24px; order:2;}
  .hero__headline{font-size:48px !important;}
  .hero__mockup-cols {order:1; height:280px; min-height:auto; width:100%;}
  .hero__mockup-cols img{position:relative;}
  .hero__gradient-overlay{background:linear-gradient(to bottom, transparent 50%, #0A1F44 100%);}
  .hero-svg{opacity:0.04;}
  
  .problem-grid{grid-template-columns:1fr; gap:0;}
  .problem-img-col{border-radius:12px 12px 0 0; height:240px; order:1;}
  .problem-text{padding:32px 24px; order:2;}
  
  .tabs-nav{flex-wrap:nowrap; overflow-x:auto; padding-bottom:8px; justify-content:flex-start;}
  
  .ntf-grid{grid-template-columns:1fr 1fr;}
  .ntf-card{height:280px;}
  
  @media(max-width:400px){
    .ntf-grid{grid-template-columns:1fr;}
  }
}
"""

with open(css_path, 'a', encoding='utf-8') as f:
    f.write(new_css)

print('V3 Python build successfully executed!')
