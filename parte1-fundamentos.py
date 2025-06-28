"""
parte1-fundamentos.py

Script auxiliar para converter parte1-fundamentos.md em HTML responsivo e moderno usando o format-html.py.

Uso:
    python parte1-fundamentos.py

Gera o arquivo parte1-fundamentos.html pronto para publicação ou visualização local.
Requer format-html.py e o pacote markdown instalado.
"""

import subprocess
import re
from pathlib import Path

# Executa o conversor universal format-html.py para gerar parte1-fundamentos.html
def main():
    # Gera HTML temporário
    subprocess.run([
        'python', 'format-html.py', 'parte1-fundamentos.md', 'parte1-fundamentos.html.tmp'
    ], check=True)

    # Corrige links de navegação no HTML
    html_path = Path('parte1-fundamentos.html.tmp')
    final_path = Path('parte1-fundamentos.html')
    with html_path.open(encoding='utf-8') as f:
        html = f.read()
    # Substitui apenas o link de navegação para a parte II (md para html)
    html = re.sub(r'(Avance para a Parte II:[^<\[]*)\(parte2-java\\?\.md\)', r'\1(parte2-java.html)', html)
    # Substitui o link de navegação para o início, se houver (md para html)
    html = re.sub(r'(Voltar ao Guia Principal[^<\[]*)\(README\\?\.md\)', r'\1(README.html)', html)
    # Substitui todos os links .md por .html, exceto links externos
    html = re.sub(r'\((parte[\w\-]+)\\?\.md\)', r'(\1.html)', html)
    html = re.sub(r'\((README)\\?\.md\)', r'(README.html)', html)
    with final_path.open('w', encoding='utf-8') as f:
        f.write(html)
    html_path.unlink()  # Remove temporário
    print(f'Arquivo HTML gerado em: {final_path.resolve()}')

if __name__ == '__main__':
    main()
