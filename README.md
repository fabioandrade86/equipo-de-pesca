# Equipo de Pesca

Lista de equipamentos de pesca para os peixes mais comuns no Paraná, Santa Catarina, São Paulo e Mato Grosso do Sul.

- Filtro por peixe, por local (barranco ou barco) e por situação (falta, já pedi, já tenho, não preciso)
- Marcas por faixa de preço (barata, média e alta) e links de busca nas lojas
- Clima no local da pescaria: chuva, vento, sol, temperatura, pressão, lua e nota de pesca do dia (Open-Meteo)
- Modo fácil com letra grande, alto contraste e leitura em voz alta
- Cores vermelho e preto ou verde e branco, e layout para celular, tablet e computador

Site: https://fabioandrade86.github.io/equipo-de-pesca/

Modo fácil direto: https://fabioandrade86.github.io/equipo-de-pesca/#facil

Modo fácil já em verde e branco: https://fabioandrade86.github.io/equipo-de-pesca/#facil-verde

As marcações ficam salvas só no navegador de cada pessoa.

## Como os preços e produtos são atualizados

Produtos, marcas e preços de referência ficam em `catalogo.json`. O site sempre carrega a versão mais nova desse arquivo.

- **Automático:** uma tarefa agendada pesquisa os preços toda semana, atualiza `catalogo.json` e publica.
- **Manual:** edite `catalogo.json` direto no GitHub (botão de lápis) e salve. Para o arquivo HTML que roda sem internet também ficar atualizado, rode `python3 tools/sync_catalogo.py`.

Estrutura de cada faixa de marcas em `tiers`: `"b"` barata, `"m"` média, `"a"` alta; cada entrada é `["Marca e modelo", "≈R$ 123"]` ou `"consulte"` quando não há preço confirmado.
