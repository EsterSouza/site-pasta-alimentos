import re
html_path = 'c:/Users/miche/OneDrive - MSFT/TreinaVISA/site/site-pasta-sanitaria/index.html'

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Remove the old sec-price block entirely
html = re.sub(r'<!-- ============================================================\n     BLOCO 8 \. PREÇO E GARANTIA.*?</section>', '', html, flags=re.DOTALL)

# Fix the sec-problem CTA that was missed
html = html.replace('<a href="#conteudo" class="btn-cta btn-small-cta" style="margin-top:24px;">VER O KIT COMPLETO</a>', '<a href="https://pay.hotmart.com/H104875140X?checkoutMode=10&utm_source=landing&utm_medium=organico&utm_campaign=kit-pasta-sanitaria" target="_blank" rel="noopener" class="btn-cta btn-small-cta" style="margin-top:24px;">VER O KIT COMPLETO</a>')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
print('Fixed missing CTA and removed old price block')
