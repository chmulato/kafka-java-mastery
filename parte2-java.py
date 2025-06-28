"""
parte2-java.py

Script auxiliar para converter parte2-java.md em HTML responsivo e moderno usando o format-html.py.

Uso:
    python parte2-java.py

Gera o arquivo parte2-java.html pronto para publicação ou visualização local.
Requer format-html.py e o pacote markdown instalado.
"""

import subprocess
import re
from pathlib import Path
import sys

def main():
    python_exe = sys.executable
    # Gera HTML temporário
    result = subprocess.run([
        python_exe, 'format-html.py', 'parte2-java.md', 'parte2-java.html.tmp'
    ], capture_output=True, text=True)
    if result.returncode != 0:
        print('Erro ao gerar HTML temporário:')
        print(result.stdout)
        print(result.stderr)
        sys.exit(result.returncode)

    # Corrige links de navegação no HTML
    html_path = Path('parte2-java.html.tmp')
    final_path = Path('parte2-java.html')
    with html_path.open(encoding='utf-8') as f:
        html = f.read()
    # Substitui o link de navegação para a parte final (md para html)
    html = re.sub(r'(Avance para a Parte Final:[^<\[]*)\(parte-final-avancado\\?\.md\)', r'\1(parte-final-avancado.html)', html)
    # Substitui o link de navegação para a primeira parte (md para html)
    html = re.sub(r'(Voltar para a Parte I:[^<\[]*)\(parte1-fundamentos\\?\.md\)', r'\1(parte1-fundamentos.html)', html)
    with final_path.open('w', encoding='utf-8') as f:
        f.write(html)
    html_path.unlink()  # Remove temporário
    print(f'Arquivo HTML gerado em: {final_path.resolve()}')

if __name__ == '__main__':
    main()
