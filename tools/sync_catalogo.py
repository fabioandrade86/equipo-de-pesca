"""Copia catalogo.json para dentro do index.html (bloco <script id="catalogo-embutido">).

O site publicado busca catalogo.json direto; a cópia embutida serve para quem abre
o arquivo HTML sem internet ou fora do GitHub Pages.

Uso: python3 tools/sync_catalogo.py   (rodar na raiz do repositório)
"""
import json, re, sys, pathlib

root = pathlib.Path(__file__).resolve().parent.parent
cat = json.loads((root / "catalogo.json").read_text(encoding="utf-8"))
for k in ("atualizado", "tiers", "items"):
    if k not in cat:
        sys.exit(f"catalogo.json sem a chave obrigatória: {k}")
payload = json.dumps(cat, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
html_path = root / "index.html"
html = html_path.read_text(encoding="utf-8")
pat = re.compile(r'(<script type="application/json" id="catalogo-embutido">)(.*?)(</script>)', re.S)
if not pat.search(html):
    sys.exit("Bloco catalogo-embutido não encontrado no index.html")
html = pat.sub(lambda m: m.group(1) + payload + m.group(3), html, count=1)
html_path.write_text(html, encoding="utf-8")
print(f"OK: {len(cat['items'])} itens, {len(cat['tiers'])} itens com marcas, atualizado em {cat['atualizado']}")
