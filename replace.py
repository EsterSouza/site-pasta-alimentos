import re

# Read files
with open('c:/Users/miche/OneDrive - MSFT/TreinaVISA/site/site-pasta-sanitaria/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

with open('c:/Users/miche/OneDrive - MSFT/TreinaVISA/site/site-pasta-sanitaria/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# CSS adjustments
css = css.replace('--section-pad-v:96px;', '--section-pad-v:80px;')
css = css.replace('--section-pad-v-mob:56px;', '--section-pad-v-mob:48px;')
css = css.replace('max-width:1120px', 'max-width:1200px')

# Typography - Desktop h2
css = re.sub(r'h2\{font-family:\'Playfair Display\',serif;font-size:clamp\([^)]+\)', r'h2{font-family:\'Playfair Display\',serif;font-size:36px', css)
# Ensure h2 class in CSS affects all sections, the existing CSS has specific classes like .problem-text h2, .sec-solution h2.
# We will just replace all font-size:clamp(...) with font-size:36px for h2, and set mobile query.
css = re.sub(r'clamp\([^)]+\)', '36px', css) # replace all clamps for h2 sizes

# Hero
css = css.replace('.hero__tag{margin-bottom:20px}', '.hero__tag{background:transparent;border:1.5px solid #C9B8E8;color:#C9B8E8;font-size:12px;font-weight:700;letter-spacing:3px;text-transform:uppercase;margin-bottom:16px;padding:5px 16px;border-radius:20px;display:inline-block}')
css = css.replace('font-size:36px;font-weight:700;color:var(--off-white)', 'font-size:72px;font-weight:700;color:var(--off-white)') # fixed the clamp replace above
css = css.replace('.hero__sub{font-size:1.05rem', '.hero__sub{font-size:20px')
css = css.replace('.btn-cta.large{font-size:1.1rem;padding:19px 42px}', '.btn-cta.large{font-size:16px;padding:16px 40px}')

# Subtitles
css = css.replace('.sec-solution .subtitle{color:rgba(240,245,241,.7);margin-bottom:36px;max-width:620px;font-size:1rem}', '.sec-solution .subtitle{color:rgba(240,245,241,.7);margin-bottom:36px;max-width:620px;font-size:22px}')
css = css.replace('.sec-cta-final .subtitle{color:rgba(240,245,241,.65);font-size:1.05rem', '.sec-cta-final .subtitle{color:rgba(240,245,241,.65);font-size:22px')

# Problem block (vistoria)
css = css.replace('.problem-grid{display:grid;grid-template-columns:1fr;gap:40px;align-items:center}', '.problem-grid{display:grid;grid-template-columns:1fr;gap:40px;align-items:center}') # mobile
css = css.replace('.problem-img{border-radius:12px;overflow:hidden;box-shadow:0 8px 32px rgba(10,31,68,.15)}', '.problem-img{border-radius:12px;overflow:hidden;box-shadow:0 8px 32px rgba(10,31,68,.15);height:100%}')
css = css.replace('.problem-img img{width:100%;height:340px;object-fit:cover;display:block}', '.problem-img img{width:100%;height:100%;object-fit:cover;display:block}')

# Solution block (Kit resolve)
css = css.replace('.solution-grid{display:grid;grid-template-columns:1fr;gap:48px;align-items:center}', '.solution-grid{display:grid;grid-template-columns:1fr;gap:48px;align-items:center}')
css = css.replace('.solution-img{border-radius:12px;overflow:hidden;box-shadow:0 12px 40px rgba(0,0,0,.4)}', '.solution-img{border-radius:12px;overflow:hidden;box-shadow:0 12px 40px rgba(0,0,0,.4);height:100%}')
css = css.replace('.solution-img img{width:100%;height:380px;object-fit:cover;display:block}', '.solution-img img{width:100%;height:100%;object-fit:cover;display:block}')

# Feature pills
css = css.replace('.pills-grid{display:grid;grid-template-columns:1fr;gap:10px;margin-bottom:36px}', '.pills-grid{display:grid;grid-template-columns:1fr;gap:10px;margin-bottom:36px}')
css = css.replace('.pill{display:flex;align-items:flex-start;gap:10px;background:rgba(201,184,232,.1);border:1px solid rgba(201,184,232,.3);border-radius:8px;padding:10px 14px;font-size:.9rem;color:var(--off-white);line-height:1.5}', '.pill{display:flex;align-items:center;gap:10px;background:rgba(201,184,232,.12);border:1px solid #C9B8E8;border-radius:8px;padding:10px 16px;font-size:15px;color:#F0F5F1;line-height:1.5}')
css = css.replace('.pill::before{content:"\u2713";color:var(--lilac-light);font-weight:700;flex-shrink:0;margin-top:1px}', '.pill::before{content:"\u2713";color:#C9B8E8;font-weight:700;flex-shrink:0;font-size:16px}')

# Desktop media query modifications
# We need to add mobile h2 and hero font sizes to the mobile media query, and desktop ones to desktop
desktop_mq_addition = """
  .hero__headline{font-size:72px;}
  h2, .problem-text h2, .sec-solution h2, .sec-detail h2, .sec-whom h2, .authority-text h2, .sec-testimonials h2, .sec-price h2, .sec-faq h2, .sec-cta-final h2 {font-size:36px !important;}
  .problem-grid{grid-template-columns:55fr 45fr;gap:56px}
  .solution-grid{grid-template-columns:42fr 58fr;gap:56px}
  .pills-grid{grid-template-columns:1fr 1fr}
"""
css = css.replace('.problem-grid{grid-template-columns:60fr 40fr;gap:56px}', '')
css = css.replace('.solution-grid{grid-template-columns:40fr 60fr;gap:56px}', '')
css = css.replace('.pills-grid{grid-template-columns:1fr 1fr}', '')
css = css.replace('@media(min-width:768px){', '@media(min-width:768px){' + desktop_mq_addition)

mobile_mq_addition = """
  body{font-size:17px}
  .hero__headline{font-size:44px;}
  .hero__text{order:2}
  .hero__mockup{order:1; margin-bottom: 24px;}
  h2, .problem-text h2, .sec-solution h2, .sec-detail h2, .sec-whom h2, .authority-text h2, .sec-testimonials h2, .sec-price h2, .sec-faq h2, .sec-cta-final h2 {font-size:28px !important;}
  .problem-img img{height:260px;width:100%}
  .solution-img{order:1}
  .solution-content{order:2}
  .solution-grid{display:flex;flex-direction:column}
  .solution-img img{height:240px;width:100%}
  .authority-wrap{display:flex;flex-direction:column}
  .authority-img-wrap{order:1}
  .authority-text{order:2}
"""
css = css.replace('@media(max-width:767px){', '@media(max-width:767px){' + mobile_mq_addition)
css = css.replace('body{font-size:16px}', '')
css = css.replace('.hero__mockup img{height:260px}', '')
css = css.replace('.problem-img img{height:240px}', '')
css = css.replace('.solution-img img{height:260px}', '')

# Cards
css = css.replace('.card__body{padding:24px}', '.card__body{padding:0}')
css = css.replace('.card__title{font-family:\'Playfair Display\',serif;font-size:1.1rem;color:var(--navy);margin-bottom:10px;font-weight:700}', '.card__title{font-family:\'Inter\',sans-serif;font-size:18px;font-weight:700;padding:20px 20px 8px;margin:0;color:var(--navy)}')
css = css.replace('.card__desc{font-size:.9rem;color:#444;line-height:1.7;margin-bottom:14px}', '.card__desc{font-size:14px;color:#1A1A1A;padding:0 20px 20px;margin:0;line-height:1.7}')
css = css.replace('.card__list{display:flex;flex-direction:column;gap:6px}', '.card__list{display:flex;flex-direction:column;gap:6px;padding:0 20px 20px}')
css = css.replace('.card{background:#fff;border:1px solid var(--lilac-light);border-radius:16px;overflow:hidden;box-shadow:0 4px 20px rgba(10,31,68,.08);transition:transform .25s,box-shadow .25s}', '.card{background:#fff;border:1px solid #C9B8E8;border-radius:12px;overflow:hidden;box-shadow:none;transition:transform .25s}')
css = css.replace('.card__img{width:100%;height:200px;object-fit:cover;display:block}', '.card__img{width:100%;height:200px;object-fit:cover;display:block;border-radius:12px 12px 0 0}')

# Avatar
css = css.replace('.persona-card__img{width:88px;height:88px;border-radius:50%;object-fit:cover;border:3px solid rgba(201,184,232,.5);box-shadow:0 4px 16px rgba(0,0,0,.3)}', '.persona-card__img{width:100px;height:100px;border-radius:50%;object-fit:cover;object-position:center top;border:3px solid #C9B8E8;box-shadow:none}')
css = css.replace('.persona-card__label{font-size:.78rem;color:var(--lilac-light);font-weight:600;text-align:center;max-width:100px;line-height:1.35}', '.persona-card__label{font-size:13px;color:#F0F5F1;font-weight:600;text-align:center;max-width:100px;line-height:1.35;margin-top:8px;}')

# Authority Foto da ana
css = css.replace('.authority-img{width:100%;max-height:480px;object-fit:cover;object-position:top center;border-radius:16px;box-shadow:0 12px 40px rgba(10,31,68,.2);display:block}', '.authority-img{width:100%;min-width:380px;height:auto;object-fit:cover;border-radius:12px;display:block}')
css = css.replace('.authority-img{max-height:320px}', '.authority-img{min-width:100%;height:320px;object-fit:cover;object-position:top center}')

# Price block
css = css.replace('.price-anchor-old{font-size:1rem;color:rgba(240,245,241,.4);text-decoration:line-through;display:block;margin-bottom:4px}', '.price-anchor-old{font-size:1rem;color:gray;text-decoration:line-through;display:block;margin-bottom:4px}')
css = css.replace('.price-anchor-new{font-size:3rem;font-weight:700;color:var(--lilac-light);font-family:\'Playfair Display\',serif;display:block;line-height:1}', '.price-anchor-new{font-size:56px;font-weight:700;color:#C9B8E8;font-family:\'Inter\',sans-serif;display:block;line-height:1}')
css = css.replace('.price-installment{font-size:.85rem;color:rgba(240,245,241,.55);display:block;margin-top:6px;margin-bottom:26px}', '.price-installment{font-size:16px;color:rgba(240,245,241,.65);display:block;margin-top:6px;margin-bottom:26px}')
css = css.replace('.btn-cta.full{width:100%;font-size:1.1rem;padding:19px 24px}', '.btn-cta.full{width:100%;min-width:320px;font-size:18px;padding:18px 48px}')

# WhatsApp Floating CTA
wa_css = """
.wa-float{position:fixed;bottom:24px;right:24px;width:60px;height:60px;border-radius:50%;background-color:#25D366;display:flex;align-items:center;justify-content:center;box-shadow:0 4px 12px rgba(0,0,0,0.25);cursor:pointer;transition:transform 0.2s ease, box-shadow 0.2s ease;z-index:9999;}
.wa-float:hover{transform:scale(1.08);box-shadow:0 6px 20px rgba(37,211,102,0.4);}
.wa-tooltip{position:absolute;right:72px;top:50%;transform:translateY(-50%);background:#1A1A1A;color:#fff;font-size:12px;border-radius:4px;padding:6px 12px;white-space:nowrap;opacity:0;pointer-events:none;transition:opacity 0.2s;}
.wa-float:hover .wa-tooltip{opacity:1;}
@media(max-width:767px){ .wa-float{bottom:80px;} .wa-tooltip{display:none;} }
"""
css += "\n" + wa_css


# HTML adjustments
html = html.replace('<div class="section-tag hero__tag">Serviço de Alimentação</div>', '<div class="section-tag hero__tag">PARA SERVIÇOS DE ALIMENTAÇÃO</div>')
html = html.replace('img-hero-mockup.webp', 'hero.png')
html = html.replace('img-problem.webp', 'img 1.png')
html = html.replace('img-solution.webp', 'BLOCO A SOLUÇÃO.png')

html = html.replace('img-card-pop.webp', 'IMAGEM 4 \u2014 CARD 1 (POPs).png')
html = html.replace('img-card-planilha.webp', 'card 2 planilhas.png')
html = html.replace('img-card-manual.webp', 'card 3 manual.png')

html = html.replace('src="img-personas.webp"\n             alt="Dono de restaurante"', 'src="restaurante.jpg"\n             alt="Dono de restaurante"')
html = html.replace('src="img-personas.webp"\n             alt="Gerente de padaria"', 'src="padaria.jpg"\n             alt="Gerente de padaria"')
html = html.replace('src="img-personas.webp"\n             alt="Responsável por cozinha industrial"', 'src="buffet.jpg"\n             alt="Responsável por cozinha industrial"') # Wait, user said buffet.png in prompt, but we see buffet.jpg in dir. Also restaurante.jpg, padaria.jpg. Let's use the actual extensions.
html = html.replace('src="img-personas.webp"\n             alt="Chef de buffet"', 'src="ifood.webp"\n             alt="Chef de buffet"') # Using ifood.webp

html = html.replace('<span class="persona-card__label">Dono de Restaurante</span>', '<span class="persona-card__label">Restaurante</span>')
html = html.replace('<span class="persona-card__label">Gerente de Padaria</span>', '<span class="persona-card__label">Padaria</span>')
html = html.replace('<span class="persona-card__label">Cozinha Industrial</span>', '<span class="persona-card__label">Buffet</span>')
html = html.replace('<span class="persona-card__label">Chef de Buffet</span>', '<span class="persona-card__label">Delivery</span>')

# Reorder sections
# We need to move <section class="sec-price" id="preco"> BEfore <section class="sec-authority" id="sobre">
# Delete depoimentos
html = re.sub(r'<!-- ============================================================\n     BLOCO 7 \u2014 DEPOIMENTOS(.*?)</section>', '', html, flags=re.DOTALL)

# Extract sec-price block
price_match = re.search(r'<!-- ============================================================\n     BLOCO 8 \u2014 PREÇO E GARANTIA.*?</section>', html, re.DOTALL)
if price_match:
    price_html = price_match.group(0)
    html = html.replace(price_html, '') # remove from original place
    
    # insert before authority
    authority_match = re.search(r'<!-- ============================================================\n     BLOCO 6 \u2014 AUTORIDADE', html)
    if authority_match:
        html = html.replace(authority_match.group(0), price_html + '\n\n' + authority_match.group(0))

# Ana photo
html = html.replace('img-authority.webp', 'foto da ana.jpeg') # its foto da ana.jpeg
html = html.replace('style="object-position:0% center"', '')
html = html.replace('style="object-position:33% center"', '')
html = html.replace('style="object-position:66% center"', '')
html = html.replace('style="object-position:100% center"', '')

# Instagram secondary btn
html = html.replace('<a href="https://instagram.com/aconsultora.nutri" target="_blank" rel="noopener" class="btn-secondary">\n            Ver Instagram \u2192\n          </a>', '<a href="https://instagram.com/aconsultora.nutri" target="_blank" rel="noopener" class="btn-secondary" style="background:transparent;border:1.5px solid #C9B8E8;color:#C9B8E8;padding:10px 24px;border-radius:4px;">\n            Ver no Instagram \u2192\n          </a>')

# Guarantee Shield SVG
guarantee_svg = '<svg viewBox="0 0 24 24" fill="none" stroke="#C9B8E8" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" width="32" height="32"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path></svg>'
html = html.replace('<div class="guarantee__icon">\ud83d\udee1\ufe0f</div>', f'<div class="guarantee__icon">{guarantee_svg}</div>')
html = html.replace('<strong style="color:var(--off-white)">Garantia de 7 dias.</strong>', '<strong style="color:var(--off-white)">Garantia de 7 dias \u2014 reembolso 100% via Hotmart.</strong>')

# Links cleanup
html = html.replace('<a href="https://instagram.com/aconsultora.nutri" target="_blank" rel="noopener" style="color:var(--lilac-mid)">@aconsultora.nutri</a>', '@aconsultora.nutri')
html = html.replace('<a href="https://instagram.com/aconsultora.nutri" target="_blank" rel="noopener">@aconsultora.nutri</a>', '@aconsultora.nutri')
html = html.replace('<a href="mailto:alimentos@consultorasanitaria.com.br">alimentos@consultorasanitaria.com.br</a>', 'alimentos@consultorasanitaria.com.br')

# WhatsApp button
wa_html = """
<a href="https://wa.me/5521990313823?text=Ol%C3%A1!%20Tenho%20interesse%20no%20Kit%20Pasta%20Sanit%C3%A1ria" target="_blank" rel="noopener" class="wa-float">
  <span class="wa-tooltip">Fale comigo no WhatsApp</span>
  <svg viewBox="0 0 24 24" fill="white" width="32" height="32">
    <path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347z"/>
    <path d="M12 0C5.373 0 0 5.373 0 12c0 2.123.554 4.118 1.525 5.847L.057 23.882l6.198-1.448A11.934 11.934 0 0012 24c6.627 0 12-5.373 12-12S18.627 0 12 0zm0 21.818a9.818 9.818 0 01-5.006-1.371l-.36-.213-3.68.859.875-3.593-.234-.371A9.818 9.818 0 1112 21.818z"/>
  </svg>
</a>
</body>
"""
html = html.replace('</body>', wa_html)


with open('c:/Users/miche/OneDrive - MSFT/TreinaVISA/site/site-pasta-sanitaria/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

with open('c:/Users/miche/OneDrive - MSFT/TreinaVISA/site/site-pasta-sanitaria/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Done")
