# Mapa de Caminhos — rankings por cruzamento (página 3 do PDF)

Além da tabela final (3 cursos escolhidos) e da matriz de peças, o entregável ganha uma **página de
"Mapa de Caminhos"**: para **cada caminho do motor combinatório** (Competência × Ferramenta,
Competência × Setor, Competência × Dor, Framework próprio × Competência, Paixão/Case × Competência,
Setor × Ferramenta…), um **ranking top-3** de ideias de curso **com score**, lado a lado.

## Por que existe
A tabela mostra **o que foi escolhido**; o Mapa de Caminhos mostra **de onde veio e o que perdeu no
corte**. É o "benchmark de cursos possíveis" da pessoa: torna o espaço de busca da Fase 2 visível e
auditável, expõe **buracos** (caminho sem candidato forte) e **quase-escolhidos** (ideia alta que não
entrou), e deixa o critério transparente.

## O que entra
- **Uma coluna por caminho** (5–6 colunas). Título = o cruzamento.
- Em cada coluna, **top-3** (ou top-5) ideias, ordenadas pelo **Score final** (mesma rubrica da Fase 3:
  `0,30·Aut + 0,30·Dem + 0,20·Mon + 0,20·Esc`).
- Cada card: posição, nome do curso, **score** (cor por banda: Forte ≥4,3 / Bom 3,5–4,2 / Fraco <3,5),
  e uma linha de nota (âncora, risco, ⚠ duplicação/teto).
- **Selecionados** (os que foram para a tabela) marcados com **★ + borda verde**.
- Caminho sem candidato viável aparece **explicitamente vazio** (hachurado) com o motivo (ex.: "duplicaria
  outro professor do time") — silêncio não; o buraco é informação.

## Regras
1. **Mesma rubrica e pesos** da Fase 3 — o Mapa não é um scoring paralelo; é a long-list inteira pontuada
   e agrupada por caminho. Um curso pode aparecer em mais de um caminho se dois cruzamentos o geram;
   marque-o no caminho que melhor o explica e evite repetir na mesma página.
2. **Cobertura**: tente preencher todos os caminhos aplicáveis ao dossiê; onde não houver lastro, mostre
   vazio com o motivo (não invente candidato sem evidência).
3. **Consistência com a tabela**: os ★ da página têm que ser exatamente os cursos da tabela, com o mesmo
   score.
4. **Honestidade de confiança**: quando o score for estimativa rápida (sem pesquisa web dedicada por
   candidato), sinalize na legenda ("notas refináveis com o briefing"). O **briefing** (Passo 0) é o que
   permite preencher os rankings com assertividade — ver [briefing-inicial.md](briefing-inicial.md).

## Layout (identidade snaq)
Landscape, fundo escuro snaq (`#16171A`), glow verde no canto. Cabeçalho com título "Mapa de Caminhos —
<Pessoa>" + logo `snaqIA` + uma linha explicando ★ e as bandas. Grid de colunas; cards em painel
`#1C1D21` com borda-esquerda na cor da banda; score em Space Mono grande no canto superior direito
(dê `padding-right` ao nome para não colidir). Rodapé com legenda das bandas + a fórmula do score.
Renderize via Chrome headless (`--print-to-pdf`) e **anexe como página final** do
`Cursos_<Pessoa>_completo.pdf` (tabela · matriz · **mapa de caminhos**).
