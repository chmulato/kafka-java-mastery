"""
parte-final-avancado.py

Script auxiliar para converter parte-final-avancado.md em HTML responsivo e moderno usando o format-html.py.

Uso:
    python parte-final-avancado.py

Gera o arquivo parte-final-avancado.html pronto para publicação ou visualização local.
Requer format-html.py e o pacote markdown instalado.
"""

import subprocess
import re
from pathlib import Path
import sys


def main():
    # Usa o mesmo interpretador Python do ambiente atual
    python_exe = sys.executable
    # Gera HTML temporário
    result = subprocess.run([
        python_exe, 'format-html.py', 'parte-final-avancado.md', 'parte-final-avancado.html.tmp'
    ], capture_output=True, text=True)
    if result.returncode != 0:
        print('Erro ao gerar HTML temporário:')
        print(result.stdout)
        print(result.stderr)
        sys.exit(result.returncode)

    # Corrige links de navegação no HTML
    html_path = Path('parte-final-avancado.html.tmp')
    final_path = Path('parte-final-avancado.html')
    with html_path.open(encoding='utf-8') as f:
        html = f.read()
    # Substitui apenas o link de navegação para o README
    html = re.sub(r'(Voltar ao Guia Principal[^<\[]*)\(README\\?\.md\)', r'\1(README.html)', html)
    with final_path.open('w', encoding='utf-8') as f:
        f.write(html)
    html_path.unlink()  # Remove temporário
    print(f'Arquivo HTML gerado em: {final_path.resolve()}')

if __name__ == '__main__':
    main()
