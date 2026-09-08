// Janela de arquivos do hero — componente-assinatura da página.
// Carregada pelas duas variantes (a/index.html e b/index.html): não duplicar este bloco nelas.
//
// Ela não ilustra o produto, ela é o argumento dele: as 55 linhas são os nomes reais dos arquivos,
// e o comprador que tem a lista do fiscal na mão consegue conferir uma a uma. Por isso a lista é
// rolável de verdade — interação vale mais que simulação.
//
// Dois modos, decididos pela largura e não pelo dispositivo:
//   desktop (>=1025px) — o cursor falso do macOS demonstra UMA vez e para, deixando a lista livre;
//   mobile             — sem cursor (não existe mouse no toque). Um auto-scroll curto sinaliza
//                        "isto rola" e morre no primeiro toque, para nunca disputar o dedo.
(function () {
  var filelist = document.getElementById('finder-filelist');
  var cursor = document.getElementById('finder-cursor');
  var clickTarget = document.getElementById('finder-click-target');
  if (!filelist || !cursor || !clickTarget) return;

  var semMovimento = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var ehDesktop = window.matchMedia('(min-width: 1025px)').matches;

  // Quem pede menos movimento recebe a janela parada — mas ainda rolável à mão.
  if (semMovimento) return;

  // --------------------------------------------------------------------------
  // Interrupção: qualquer gesto do visitante encerra a demonstração para sempre.
  // --------------------------------------------------------------------------
  var interrompido = false;
  var scrollRAF = null;

  function interromper() {
    if (interrompido) return;
    interrompido = true;
    if (scrollRAF) cancelAnimationFrame(scrollRAF);
    cursor.style.display = 'none';
  }

  ['touchstart', 'wheel', 'pointerdown'].forEach(function (evt) {
    filelist.addEventListener(evt, interromper, { passive: true, once: true });
  });

  // --------------------------------------------------------------------------
  // Mobile: só o empurrãozinho que revela que a lista rola.
  // --------------------------------------------------------------------------
  if (!ehDesktop) {
    cursor.style.display = 'none';
    setTimeout(function () {
      if (interrompido) return;
      var alvo = Math.min(220, filelist.scrollHeight - filelist.clientHeight);
      var inicio = null;
      (function passo(ts) {
        if (interrompido) return;
        if (!inicio) inicio = ts;
        var t = Math.min((ts - inicio) / 2200, 1);
        // ease-out-quart: começa decidido e assenta sem freada brusca
        filelist.scrollTop = alvo * (1 - Math.pow(1 - t, 4));
        if (t < 1) scrollRAF = requestAnimationFrame(passo);
      })(performance.now());
    }, 1200);
    return;
  }

  // --------------------------------------------------------------------------
  // Desktop: a demonstração do cursor, uma única vez.
  // --------------------------------------------------------------------------
  var SCROLL_SPEED = 0.7;        // px por frame
  var PAUSE_BEFORE_SCROLL = 1200; // ms entre o "clique" e o início da rolagem
  var SCROLL_DURATION = 7000;     // ms de rolagem
  var scrollStart = null;
  var totalContentHeight = 0;

  cursor.style.display = 'block';
  cursor.style.left = '60px';
  cursor.style.top = '30px';

  function posRelativa(el) {
    var pai = filelist.getBoundingClientRect();
    var r = el.getBoundingClientRect();
    return { x: r.left - pai.left + r.width / 2, y: r.top - pai.top + r.height / 2 };
  }

  function encerrar() {
    // A demonstração acabou: o cursor sai de cena e a lista fica para o visitante.
    cursor.style.transition = 'opacity 0.4s ease';
    cursor.style.opacity = '0';
    setTimeout(function () { cursor.style.display = 'none'; }, 400);
  }

  function rolar() {
    function tick(ts) {
      if (interrompido) return;
      if (!scrollStart) scrollStart = ts;
      var elapsed = ts - scrollStart;

      var novoTopo = Math.min(filelist.scrollTop + SCROLL_SPEED, totalContentHeight);
      filelist.scrollTop = novoTopo;

      var y = parseFloat(cursor.style.top) || 0;
      cursor.style.top = Math.min(y + 0.2, filelist.clientHeight - 30) + 'px';
      cursor.style.transition = 'none';

      if (elapsed >= SCROLL_DURATION || novoTopo >= totalContentHeight) {
        encerrar();
        return;
      }
      scrollRAF = requestAnimationFrame(tick);
    }
    scrollRAF = requestAnimationFrame(tick);
  }

  function demonstrar() {
    if (interrompido) return;
    var pos = posRelativa(clickTarget);
    // O alvo do clique é a 23ª linha, bem abaixo das ~14 que cabem na janela: mirar nele
    // fazia o cursor deslizar para fora da área visível e só reaparecer na fase de rolagem.
    // Manter o ponteiro dentro da faixa visível preserva a demonstração.
    cursor.style.left = pos.x + 'px';
    cursor.style.top = Math.min(pos.y, filelist.clientHeight - 40) + 'px';
    cursor.style.transition = 'top 0.9s cubic-bezier(0.4,0,0.2,1), left 0.9s cubic-bezier(0.4,0,0.2,1)';

    setTimeout(function () {
      if (interrompido) return;
      cursor.style.transform = 'rotate(-45deg) scale(0.75)';
      clickTarget.classList.add('finder-file--highlight');
      setTimeout(function () { cursor.style.transform = 'rotate(-45deg) scale(1)'; }, 150);

      setTimeout(function () {
        if (interrompido) return;
        totalContentHeight = filelist.scrollHeight - filelist.clientHeight;
        scrollStart = null;
        rolar();
      }, PAUSE_BEFORE_SCROLL);
    }, 950);
  }

  setTimeout(demonstrar, 800);
})();
