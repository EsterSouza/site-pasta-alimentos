// Janela de arquivos do hero — componente-assinatura da página.
// Carregada pelas duas variantes (a/index.html e b/index.html): não duplicar este bloco nelas.
//
// Ela não ilustra o produto, ela é o argumento dele: as 54 linhas são os nomes reais dos arquivos,
// e o comprador que tem a lista do fiscal na mão consegue conferir uma a uma.
//
// É uma GRAVAÇÃO DE TELA, não um widget: a lista percorre o conteúdo em laço contínuo, volta ao
// topo e recomeça. Sem cursor e sem interação — quem assiste está vendo um vídeo da pasta aberta.
//
// Detalhe que sustenta tudo: `overflow: hidden` na lista bloqueia a rolagem do USUÁRIO mas não a
// programática. Sem isso, o dedo do visitante fica preso na lista ao rolar a página no celular.
(function () {
  var lista = document.getElementById('finder-filelist');
  if (!lista) return;

  // Quem pede menos movimento recebe a janela parada, mostrando o topo da lista.
  // O inventário completo continua acessível e navegável na seção #conteudo.
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;

  var VELOCIDADE = 100;   // px por segundo — ~2,7 linhas/s, ainda dá para ler os nomes
  var PAUSA_INICIO = 900; // ms parado no topo antes de começar
  var PAUSA_FIM = 1400;   // ms parado no fim antes de rebobinar

  var raf = null;
  var ultimoFrame = null;

  function alturaRolavel() {
    return lista.scrollHeight - lista.clientHeight;
  }

  function correr() {
    ultimoFrame = null;
    var limite = alturaRolavel();

    function passo(ts) {
      // Baseado em tempo, não em frames: a 120Hz um passo por frame correria ao dobro.
      if (ultimoFrame === null) ultimoFrame = ts;
      var dt = (ts - ultimoFrame) / 1000;
      ultimoFrame = ts;

      var proximo = lista.scrollTop + VELOCIDADE * dt;
      if (proximo >= limite) {
        lista.scrollTop = limite;
        setTimeout(rebobinar, PAUSA_FIM);
        return;
      }
      lista.scrollTop = proximo;
      raf = requestAnimationFrame(passo);
    }
    raf = requestAnimationFrame(passo);
  }

  function rebobinar() {
    lista.scrollTo({ top: 0, behavior: 'smooth' });
    setTimeout(correr, PAUSA_INICIO);
  }

  setTimeout(correr, PAUSA_INICIO);
})();
