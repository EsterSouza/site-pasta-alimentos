export const config = { runtime: 'edge' };

// Cookie por experimento — ver tracking.js. Trocar o código aqui e lá em conjunto.
const COOKIE = 'ab-e2';

const MARKDOWN = `# Kit Pasta Sanitária para Serviço de Alimentação

> Consultora Sanitária — linha de alimentos

## Produto

Kit digital com 54 documentos editáveis (Word e Excel) para regularização sanitária de serviços de alimentação conforme RDC ANVISA 216/2004.

- **Preço:** R$ 47,99 à vista ou 6x de R$ 9,00
- **Formato:** digital (download imediato)
- **Garantia:** 7 dias (reembolso via Hotmart)
- **Checkout:** https://pay.hotmart.com/H104875140X?checkoutMode=10

## O que inclui

- POPs (Procedimentos Operacionais Padronizados)
- Manual de Boas Práticas (MBP)
- Planilhas de controle (temperatura, higienização, pragas)
- Checklists de verificação
- Treinamentos para equipe

## Público-alvo

Restaurantes, lanchonetes, padarias, buffets, cozinhas industriais, deliveries e food trucks que precisam de documentação sanitária para vistoria da Vigilância Sanitária.

Não indicado para indústria de alimentos (legislação específica diferente).

## Autora

**Ana Roberta Ribeiro** — Consultora de Alimentos
- Instagram: @aconsultora.nutri
- E-mail: alimentos@consultorasanitaria.com.br
- WhatsApp: +55 21 99031-3823

## FAQ

1. **Como vou receber os documentos?**
   Após a confirmação do pagamento pela Hotmart, você recebe um e-mail com o link de acesso para download imediato em formato Word.

2. **Preciso ter algum conhecimento técnico?**
   Não. Os documentos já estão escritos e formatados. Basta abrir no Word e substituir os campos indicados com os dados do seu estabelecimento.

3. **Esses documentos atendem à legislação vigente?**
   Sim. Elaborados com base na RDC ANVISA nº 216/2004.

4. **Serve para qualquer tipo de serviço de alimentação?**
   Sim, para serviços em geral (restaurantes, padarias, buffets, etc.). Não indicado para indústria de alimentos.

5. **E se eu não gostar?**
   7 dias de garantia. Reembolso direto pela Hotmart, sem burocracia.

6. **Posso usar em mais de um estabelecimento?**
   Licença para uso pessoal em estabelecimentos sob sua responsabilidade.

## Contato

- **Empresa:** HUB TREINAVISA SERVIÇOS LTDA
- **CNPJ:** 53.297.694/0001-37
- **Endereço:** Av. Embaixador Abelardo Bueno, 1, Sala 153-D, Ed. Lagoa, Barra da Tijuca, Rio de Janeiro – RJ, 22775-022
- **E-mail:** alimentos@consultorasanitaria.com.br
- **WhatsApp:** +55 21 99031-3823`;

export default async function handler(request) {
  const accept = request.headers.get('accept') || '';
  if (accept.includes('text/markdown')) {
    return new Response(MARKDOWN, {
      headers: { 'Content-Type': 'text/markdown; charset=utf-8' },
    });
  }

  const url = new URL(request.url);
  const cookies = request.headers.get('cookie') || '';
  const match = cookies.match(new RegExp(`${COOKIE}=([ab])`));
  let variant = match ? match[1] : null;
  let isNew = false;

  const forced = url.searchParams.get('v');
  if (forced === 'a' || forced === 'b') {
    variant = forced;
    isNew = true;
  }

  if (!variant) {
    variant = Math.random() < 0.5 ? 'a' : 'b';
    isNew = true;
  }

  const target = new URL(`/${variant}/`, url.origin);
  // `no-store` é obrigatório aqui: sem ele o nó de borda pode devolver uma cópia
  // do HTML buscada ANTES do último deploy, e a página fica atualizada numa região
  // e velha noutra — sem nada no navegador do visitante explicar o motivo.
  const res = await fetch(target, { cache: 'no-store' });
  const body = await res.text();

  const headers = new Headers({ 'Content-Type': 'text/html; charset=utf-8' });
  if (isNew) {
    headers.append(
      'Set-Cookie',
      `${COOKIE}=${variant}; Path=/; Max-Age=${30 * 24 * 60 * 60}; SameSite=Lax`
    );
  }

  return new Response(body, { status: 200, headers });
}
