// Janela de arquivos do hero — componente-assinatura da página.
// Carregada pelas duas variantes (a/index.html e b/index.html): não duplicar este bloco nelas.
//
// Ela não ilustra o produto, ela é o argumento dele: as 55 linhas são os nomes reais dos arquivos,
// e o comprador que tem a lista do fiscal na mão consegue conferir uma a uma.
//
// O componente é uma GRAVAÇÃO DE TELA, não um widget: um vídeo de alguém mexendo no computador,
// embutido na página. Por isso roda em laço, tem cursor de mouse e não é interativo — no desktop e
// no celular igualmente, porque é a mesma tela sendo retratada.
//
// Detalhe que sustenta tudo: `overflow: hidden` na lista bloqueia a rolagem do USUÁRIO mas não a
// programática. Sem isso, o dedo do visitante fica preso na lista ao rolar a página no celular.
(function () {
  var filelist = document.getElementById('finder-filelist');
  var cursor = document.getElementById('finder-cursor');
  var clickTarget = document.getElementById('finder-click-target');
  if (!filelist || !cursor || !clickTarget) return;

  // Quem pede menos movimento recebe a janela parada, mostrando o topo da lista.
  // O inventário completo continua acessível e navegável na seção #conteudo.
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;

  var SCROLL_SPEED = 1.3;         // px por frame — a lista é o assunto, tem de correr
  var PAUSE_BEFORE_SCROLL = 1200; // ms entre o "clique" e o início da rolagem
  var SCROLL_DURATION = 7000;     // ms de rolagem
  var RESET_PAUSE = 1000;         // ms antes de voltar ao topo
  var LOOP_PAUSE = 1200;          // ms antes de recomeçar o ciclo

  var scrollRAF = null;
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

  function rolar() {
    function tick(ts) {
      if (!scrollStart) scrollStart = ts;
      var elapsed = ts - scrollStart;

      var novoTopo = Math.min(filelist.scrollTop + SCROLL_SPEED, totalContentHeight);
      filelist.scrollTop = novoTopo;

      var y = parseFloat(cursor.style.top) || 0;
      cursor.style.top = Math.min(y + 0.2, filelist.clientHeight - 30) + 'px';
      cursor.style.transition = 'none';

      if (elapsed >= SCROLL_DURATION || novoTopo >= totalContentHeight) {
        setTimeout(reiniciar, RESET_PAUSE);
        return;
      }
      scrollRAF = requestAnimationFrame(tick);
    }
    scrollRAF = requestAnimationFrame(tick);
  }

  function reiniciar() {
    filelist.scrollTo({ top: 0, behavior: 'smooth' });
    clickTarget.classList.remove('finder-file--highlight');
    cursor.style.transition = 'top 0.5s ease, left 0.5s ease';
    cursor.style.top = '30px';
    cursor.style.left = '60px';
    setTimeout(demonstrar, LOOP_PAUSE);
  }

  function demonstrar() {
    var pos = posRelativa(clickTarget);
    // O alvo do clique é a 23ª linha, bem abaixo das que cabem na janela: mirar nele fazia o cursor
    // deslizar para fora da área visível e só reaparecer na fase de rolagem.
    cursor.style.left = pos.x + 'px';
    cursor.style.top = Math.min(pos.y, filelist.clientHeight - 40) + 'px';
    cursor.style.transition = 'top 0.9s cubic-bezier(0.4,0,0.2,1), left 0.9s cubic-bezier(0.4,0,0.2,1)';

    setTimeout(function () {
      cursor.style.transform = 'scale(0.8)';
      clickTarget.classList.add('finder-file--highlight');
      setTimeout(function () { cursor.style.transform = 'scale(1)'; }, 150);

      setTimeout(function () {
        totalContentHeight = filelist.scrollHeight - filelist.clientHeight;
        scrollStart = null;
        rolar();
      }, PAUSE_BEFORE_SCROLL);
    }, 950);
  }

  setTimeout(demonstrar, 800);
})();
