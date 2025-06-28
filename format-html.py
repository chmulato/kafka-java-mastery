"""
format-html.py

Script universal para converter arquivos Markdown (.md) em HTML responsivo e moderno.

Uso:
    python format-html.py <arquivo_markdown.md> [arquivo_saida.html]

- Gera um HTML com layout profissional, pronto para publicação ou visualização local.
- Suporta realce de código, tabelas, imagens e links responsivos.
- O título do HTML é gerado automaticamente a partir do nome do arquivo Markdown.
- Se o nome do arquivo de saída não for informado, será usado o mesmo nome do markdown com extensão .html.

Requisitos:
    pip install markdown

Exemplo:
    python format-html.py parte1-fundamentos.md
    python format-html.py parte2-java.md parte2-java.html
"""

import markdown
from pathlib import Path
import sys

# Uso: python format-html.py arquivo.md [arquivo.html]
if len(sys.argv) < 2:
    print('Uso: python format-html.py <arquivo_markdown.md> [arquivo_saida.html]')
    sys.exit(1)

md_path = Path(sys.argv[1])
if not md_path.exists():
    print(f'Arquivo markdown não encontrado: {md_path}')
    sys.exit(1)

if len(sys.argv) > 2:
    html_path = Path(sys.argv[2])
else:
    html_path = md_path.with_suffix('.html')

with md_path.open(encoding='utf-8') as f:
    md_content = f.read()

html_body = markdown.markdown(md_content, extensions=['extra', 'toc', 'codehilite'])

html_template = f"""
<!DOCTYPE html>
<html lang='pt-br'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>{md_path.stem.replace('-', ' ').title()}</title>
    <link rel='stylesheet' href='https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/styles/github-dark.min.css'>
    <style>
        body {{ font-family: 'Segoe UI', Arial, sans-serif; background: #f8f9fa; color: #222; margin: 0; }}
        .container {{ max-width: 900px; margin: 2rem auto; background: #fff; border-radius: 12px; box-shadow: 0 2px 16px rgba(0,0,0,0.07); padding: 2.5rem 2rem; }}
        h1, h2, h3, h4 {{ color: #0d47a1; }}
        pre, code {{ font-family: 'Fira Mono', 'Consolas', monospace; background: #23272e; color: #f8f8f2; border-radius: 6px; }}
        pre {{ padding: 1em; overflow-x: auto; }}
        a {{ color: #1976d2; text-decoration: none; }}
        a:hover {{ text-decoration: underline; }}
        table {{ border-collapse: collapse; width: 100%; margin: 1.5rem 0; }}
        th, td {{ border: 1px solid #ddd; padding: 10px; }}
        th {{ background: #f0f4fa; }}
        img {{ max-width: 100%; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.06); }}
        @media (max-width: 600px) {{
            .container {{ padding: 1rem; }}
            h1 {{ font-size: 1.6em; }}
        }}
    </style>
    <script src='https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/highlight.min.js'></script>
    <script>hljs.highlightAll();</script>
</head>
<body>
    <div class='container'>
        {html_body}
    </div>
</body>
</html>
"""

with html_path.open('w', encoding='utf-8') as f:
    f.write(html_template)

print(f'Arquivo HTML gerado em: {html_path.resolve()}')
