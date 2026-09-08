// Tracking do Kit Pasta Sanitária (Alimentos) — ÚNICO ponto de link de checkout e de eventos.
// Carregado pelas duas variantes (a/index.html e b/index.html): não duplicar este bloco nelas.
//
// Atribuição Hotmart:
//   sck  = e2|<variante>  → aba SCK do Dashboard de Origem de Vendas; chega no webhook em
//          purchase.origin.sck. Limite de 30 chars, e `_` é reservado pela Hotmart — daí o pipe.
//   utm_* = origem paga repassada ao checkout → alimenta o Hotmart Analytics, mas a Hotmart NÃO
//          envia UTM no webhook.
//   xcod = e2|<variante>|<campaign.id>|<ad.id> → é o que chega no webhook com os IDs do
//          anúncio. Repete slug e variante de propósito: a Hotmart às vezes sobrescreve o sck com
//          valor próprio (HOTMART_*, NEW_CLUB_*), e nesse caso o xcod preserva a atribuição.
(function () {
  // Duas identidades distintas, e confundi-las quebra um dos dois relatórios:
  //   LP_PAGE     — qual PÁGINA é esta. Vai para o Clarity, cujo projeto é compartilhado por nove
  //                 repos da casa; ali um código de experimento não significaria nada.
  //   EXPERIMENTO — qual TESTE está rodando. É o código emitido pelo ERP, e é ele que a venda casa
  //                 em `experimento.codigo || '|' || variante`. Sem ele, a tag fica órfã.
  var LP_PAGE = 'alimentos';
  var EXPERIMENTO = 'e2';
  // Cookie por experimento: teste novo re-sorteia todo mundo. Reaproveitar o cookie faria o
  // visitante recorrente carregar a atribuição do teste anterior e nascer enviesado.
  var COOKIE = 'ab-' + EXPERIMENTO;
  var CHECKOUT_BASE = 'https://pay.hotmart.com/H104875140X?checkoutMode=10';
  var UTM_KEYS = ['utm_source', 'utm_medium', 'utm_campaign', 'utm_term', 'utm_content'];
  var UTM_STORE = 'lp_utm'; // mesma chave da frota (lp-vistoria/lib/tracking.ts)

  // A variante vem do próprio HTML servido (data-variant). O cookie é fallback: com cookies
  // bloqueados a página /b/ se reportava como 'a'.
  function getVariant() {
    var attr = document.documentElement.getAttribute('data-variant');
    if (attr) return attr;
    var m = document.cookie.match(new RegExp('(?:^|; )' + COOKIE + '=([^;]+)'));
    return m ? m[1] : 'a';
  }

  // Guarda os UTMs da primeira visita: o visitante pode ir até a política de privacidade e voltar
  // sem os parâmetros na URL, e o link de checkout precisa continuar completo.
  function captureUtms() {
    var stored = {};
    try {
      stored = JSON.parse(sessionStorage.getItem(UTM_STORE) || '{}');
    } catch (e) {
      stored = {};
    }
    var url = new URLSearchParams(location.search);
    for (var i = 0; i < UTM_KEYS.length; i++) {
      var v = url.get(UTM_KEYS[i]);
      if (v) stored[UTM_KEYS[i]] = v;
    }
    try {
      sessionStorage.setItem(UTM_STORE, JSON.stringify(stored));
    } catch (e) {
      /* modo privado / storage cheio — segue com o que veio na URL */
    }
    return stored;
  }

  var variant = getVariant();
  var sck = EXPERIMENTO + '|' + variant;
  var utms = captureUtms();

  var params = new URLSearchParams();
  params.set('sck', sck);
  Object.keys(utms).forEach(function (k) {
    if (utms[k]) params.set(k, utms[k]);
  });
  // Só emite xcod quando há de fato campanha ou anúncio — tráfego direto não ganha parâmetro vazio.
  if (utms.utm_campaign || utms.utm_content) {
    params.set(
      'xcod',
      [EXPERIMENTO, variant, utms.utm_campaign || '', utms.utm_content || ''].join('|')
    );
  }
  var href = CHECKOUT_BASE + '&' + params.toString();

  var links = document.querySelectorAll('a[href*="pay.hotmart.com"]');
  for (var j = 0; j < links.length; j++) links[j].href = href;

  // Clarity: o projeto y109t0glph é compartilhado por nove repos, e o rewrite de `/` deixa a URL
  // idêntica em A e B — sem estas tags não há como filtrar página nem variante no painel.
  if (window.clarity) {
    window.clarity('set', 'lp_page', LP_PAGE);
    window.clarity('set', 'ab_variant', variant);
  }

  document.addEventListener('click', function (e) {
    var a = e.target.closest('a[href*="pay.hotmart.com"]');
    if (!a) return;
    if (window.fbq) fbq('track','InitiateCheckout',{value:47.99,currency:'BRL',content_name:variant});
    if (window.gtag) {
      gtag('event','conversion',{'send_to':'AW-18030262622/9GECCKmJpo4cEN7yv5VD','value':1.0,'currency':'BRL'});
      gtag('event','conversion',{'send_to':'AW-18030262622/2sXFCLaXzpIcEN7yv5VD'});
    }
  });
})();
