# Peças de Marketing por Curso (identidade snaq)

Referência para o entregável **#11**: para cada curso escolhido (Fase 4), o skill gera peças na
identidade visual da **snaq**. Há **dois tipos** — não confundir:

**A) Peças de rede social** (levam a **foto da pessoa**, como nas referências):
1. **Feed** — 1080×1350 (4:5), PNG — template [../assets/peca-divulgacao-template.html](../assets/peca-divulgacao-template.html).
2. **Story** — 1080×1920 (9:16), PNG — mesma identidade, layout vertical.

**B) Documento** (não é rede social):
3. **One-pager de venda** — A4 PDF — template [../assets/one-pager-template.html](../assets/one-pager-template.html).

Os templates estão preenchidos com um exemplo (curso "Soberania Cognitiva") — **adapte** por curso.
Salve em `pessoas/<pessoa>/resumo/`.

## Passo 0 (obrigatório em chat) — pedir a foto da pessoa
Ao acionar o skill num chat, **peça ao usuário a foto da pessoa** (retrato, boa resolução) para
ilustrar os criativos sociais — como as peças de referência da snaq trazem o professor. Ao receber:
- **Salve** em `pessoas/<pessoa>/foto-<pessoa>.<ext>` (precisa ser **arquivo**; se vier só colada
  inline, peça o caminho/anexo).
- Use nas peças **de rede social** (feed + story) com recorte/posicionamento da pessoa.
- O **one-pager** pode ou não usar a foto (é documento; foto é opcional ali).
- Sem foto disponível, gere as peças sem ela e sinalize que ficam melhores com o retrato.

## Referência visual (fonte da verdade)

As peças reais da snaq estão em [../assets/ref-assets/](../assets/ref-assets/) (`ref-asset1/2/3.png` —
feed, story, feed). **Estude-as antes de gerar** e siga a identidade delas. O que elas confirmam:
verde vibrante `#37E27C`; logo `snaq` (branco) + `I` (verde) + `A` (branco); título branco com **uma
palavra-chave realçada em verde**; selo verde "ministrado por [nome] + foto"; cupom em fonte
**monoespaçada**; botão CTA verde com ícone de cursor; fundo escuro (do quase-preto ao carvão) com
leve brilho verde. **Fonte da marca: geométrica arredondada (tipo Poppins/Sofia)** — não usar fonte
angular/técnica para os títulos.

## Design system (contrato — ler primeiro)

Os **tokens exatos** (cores amostradas por pixel dos refs, tipografia, anatomia de cada componente)
estão em **[design-system.md](design-system.md)**. É o contrato — siga-o literalmente. Destaques:
verde **#1EFD8A** (neon, não #37E27C); fundos charcoal com **glow verde**; cupom/labels em Space Mono.

## Identidade visual snaq (fixa)

- **Fundo:** `#0E0F11` (quase preto). **Cards:** `#17181B`, borda `rgba(255,255,255,.08)`.
- **Verde snaq:** `#37E27C` (principal) / `#4BEA8A` (botão CTA). Texto branco; cinza `#9AA1A8`.
- **Fontes:** **Poppins** (títulos/corpo — geométrica arredondada, a cara da snaq; use pesos 600/700/800
  nos títulos) + **Space Mono** (cupom, números, labels, cursor). Baixe de google/fonts (`ofl/poppins`,
  `ofl/spacemono`) e instale/coloque ao lado do HTML — mesma lógica da Montserrat em [saida-pdf.md](saida-pdf.md).
- **Logo:** aproximação `snaq` (branco) + `I` (verde) + `A` (branco). ⚑ **Trocar pelo SVG/logo oficial
  da snaq quando disponível** — o atual é aproximação.
- **Regras de conteúdo (importantes):**
  - **INCLUIR a foto da pessoa** nas peças de rede social (pedir no Passo 0) — como as referências da snaq.
  - **NÃO** usar o logo/asterisco do Claude — **exceto** se o curso for especificamente sobre Claude.
  - Preços e cupons são **ilustrativos** — confirmar com o time antes de publicar.

## Estrutura — Peça de divulgação (1080×1350)
Baseada nas peças reais da snaq (não copiar rígido; seguir a ideia):
- Topo: logo snaq + pill do formato ("Programa ao vivo · 4×2h").
- Headline: **"As N coisas que você vai aprender no curso"** + nome do curso em **verde itálico** com
  **swoosh** verde por baixo (SVG). N = nº de pilares (mapeia os encontros/módulos).
- Subtítulo curto (promessa / para quem é).
- **Grid 2×2** de cards: número mono verde (01–04), título bold, 1 linha de descrição.
- Rodapé: **cupom** (ticket com perfuração tracejada, código em Space Mono verde, preço riscado →
  preço com desconto → "% OFF" verde) + **CTA** verde (URL) com ícone de cursor.

## Estrutura — One-pager de venda (A4)
- Topo: logo + kicker ("Curso snaq · Programa ao vivo").
- Hero: **nome do curso** (grande) + subtítulo verde + parágrafo de promessa.
- **Data strip** (prova social): 2–3 números com fonte datada (ex.: GoTo 53,6%, EY 95%, MIT "dívida
  cognitiva"). Puxe da [base-mercado.md](base-mercado.md).
- **"O que você vai aprender"**: grid 2×2 dos pilares.
- **"Formatos e investimento"**: 3 cards (Workshop / Gravado / Programa) com preço em verde.
- **"Para quem é"** + CTA verde com cursor.

## Montagem no PDF final (2 páginas)

O PDF de saída da pessoa tem **2 páginas**:
- **Página 1** — a tabela comparativa de cursos (paisagem; ver [saida-pdf.md](saida-pdf.md)).
- **Página 2** — uma **matriz 3×3 ("jogo da velha")** com os 9 assets numa **única página**: linhas =
  cursos, colunas = formatos (Feed · Story · One-pager). **Cada asset leva uma legenda em cima**
  (ex.: `Soberania · Asset 1 · Feed`). As larguras das colunas seguem o aspecto de cada formato
  (story mais estreito, feed médio, one-pager mais largo); altura da miniatura fixa por linha.
  **Fundo da página branco** (os assets são escuros — no fundo preto sumiam; no branco ficam
  emoldurados, com sombra sutil e legenda em texto escuro).

O **ZIP** continua com os 9 arquivos soltos (não muda) — a matriz é só para revisão de bater o olho.

**Densidade por formato (peças sociais = texto maior, menos texto):**
- **Story = limpa** — um **gancho grande** (frase curta e forte) + nome do curso + foto + CTA. Pouco texto.
- **Feed = média** — "As 4 coisas que você vai aprender" (só os 4 títulos, grandes) + cupom + CTA.
- **One-pager = carregada** — o documento detalhado (prova social, ementa, formatos, preços).

**Como montar** (Chrome render + pypdf merge): renderize feed/story (PNG) e one-pager (PDF+PNG),
monte a página-matriz embutindo as miniaturas, e faça `w.append("tabela.pdf"); w.append("matrix.pdf")`.
O [gerador](../assets/gerar-pecas.py) já faz tudo isso. Salve em `pessoas/<pessoa>/resumo/` + `~/Downloads/`.

### Entregáveis: PDF + ZIP (sempre os dois)
- **PDF combinado** (`Cursos_<pessoa>_completo.pdf`) — para revisar/comparar (tabela + matriz de assets).
- **ZIP com os assets soltos** (`Assets_<pessoa>.zip`) — os arquivos individuais, prontos para uso
  (postar/subir). Estrutura por curso, com nomes pela taxonomia fixa:
  ```
  Assets_<pessoa>/
  ├── 01_<curso-slug>/
  │   ├── asset-1-feed.png        (1080×1350)
  │   ├── asset-2-story.png       (1080×1920)
  │   └── asset-3-onepager.pdf    (A4)
  ├── 02_<curso-slug>/ ...
  └── 03_<curso-slug>/ ...
  ```
  Gere com `zip -r Assets_<pessoa>.zip Assets_<pessoa>/` e ofereça cópia em `~/Downloads/`.

## Gerador em lote (recomendado)

Para produzir os 9 assets + PDF combinado + ZIP de uma vez, use o script de referência
[../assets/gerar-pecas.py](../assets/gerar-pecas.py) — parametrizado por uma lista `COURSES`
(nome, subtítulo, promessa, 4 pilares, cupom, preços, público, data strip), a foto da pessoa
(`foto-<pessoa>.jpeg`) e o PDF da tabela (página 1). Ele renderiza feed/story/one-pager via Chrome,
monta as páginas rotuladas, faz o merge com pypdf e gera o `Assets_<pessoa>.zip`. Rode dentro de uma
pasta que tenha as fontes (SpaceGrotesk/SpaceMono), a foto e o PDF da tabela. Adapte os dados de
`COURSES` por pessoa (o script vem preenchido com um exemplo — Ricardo Catto).

## Como gerar (cada asset, manual)
```bash
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
# Peça social (PNG 2x, 1080x1350):
"$CHROME" --headless=new --disable-gpu --hide-scrollbars --force-device-scale-factor=2 \
  --window-size=1080,1350 --screenshot="peca-<curso>.png" "file://$PWD/peca.html"
# One-pager (PDF A4):
"$CHROME" --headless=new --disable-gpu --no-pdf-header-footer \
  --print-to-pdf="onepager-<curso>.pdf" "file://$PWD/onepager.html"
```
Confira o PNG/PDF antes de entregar (fonte carregou? cabe em 1 página? verde certo?).
