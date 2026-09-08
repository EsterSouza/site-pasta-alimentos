/**
 * reveal.js — entrada suave das avaliações quando entram na tela.
 *
 * Fail-OPEN, de propósito. A página de referência da casa faz o contrário: o CSS
 * declara `opacity: 0` e só o JS devolve a visibilidade. Se o script falhar, se
 * o observer não disparar ou se o navegador for antigo, o conteúdo some — lá são
 * 24 elementos nesse regime, incluindo o H1 e o botão de compra.
 *
 * Aqui nada nasce invisível. O JS só ESCONDE depois de confirmar que sabe
 * revelar: precisa de IntersectionObserver, e ainda assim há um prazo de
 * segurança que mostra tudo se o observer não tiver entregue nada.
 */
(function () {
  var alvos = document.querySelectorAll('[data-revelar]');
  if (!alvos.length) return;

  // Quem pediu menos movimento não recebe nenhum: sai antes de armar.
  var quieto = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)');
  if (quieto && quieto.matches) return;

  if (typeof IntersectionObserver !== 'function') return;   // sem observer, fica visível

  var PRAZO = 1200;   // se o observer não entregar nada até aqui, revela tudo
  var revelado = false;

  function revelarTudo() {
    if (revelado) return;
    revelado = true;
    for (var i = 0; i < alvos.length; i++) alvos[i].classList.add('e-visivel');
  }

  // Só agora esconde — a partir daqui o JS é responsável por devolver.
  document.documentElement.classList.add('revelar-armado');
  var prazo = setTimeout(revelarTudo, PRAZO);

  // O que já está na tela neste instante não tem por que animar entrando: ele
  // não "entrou". Revelar de imediato mata o piscar de quem abre a página já
  // com a seção visível, e encolhe a janela em que o conteúdo depende do JS.
  for (var j = 0; j < alvos.length; j++) {
    var caixa = alvos[j].getBoundingClientRect();
    if (caixa.top < window.innerHeight && caixa.bottom > 0) alvos[j].classList.add('e-visivel');
  }

  var observer = new IntersectionObserver(function (entradas) {
    for (var i = 0; i < entradas.length; i++) {
      if (!entradas[i].isIntersecting) continue;
      entradas[i].target.classList.add('e-visivel');
      observer.unobserve(entradas[i].target);
    }
    if (!document.querySelectorAll('[data-revelar]:not(.e-visivel)').length) {
      clearTimeout(prazo);
      observer.disconnect();
    }
  }, { rootMargin: '0px 0px -10% 0px', threshold: 0.05 });

  for (var i = 0; i < alvos.length; i++) observer.observe(alvos[i]);
})();
