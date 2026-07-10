# Peças de Marketing por Curso (identidade snaq)

Referência para o entregável **#11**: para cada curso escolhido (Fase 4), o skill pode gerar duas
peças na identidade visual da **snaq**:
1. **Peça de divulgação** (social, 1080×1350 PNG) — template [../assets/peca-divulgacao-template.html](../assets/peca-divulgacao-template.html).
2. **One-pager de venda** (A4 PDF) — template [../assets/one-pager-template.html](../assets/one-pager-template.html).

Os templates estão preenchidos com um exemplo (curso "Soberania Cognitiva") — **adapte** o conteúdo
por curso. Gere sob demanda ou junto da tabela final. Salve em `pessoas/<pessoa>/resumo/`.

## Identidade visual snaq (fixa)

- **Fundo:** `#0E0F11` (quase preto). **Cards:** `#17181B`, borda `rgba(255,255,255,.08)`.
- **Verde snaq:** `#37E27C` (principal) / `#4BEA8A` (botão CTA). Texto branco; cinza `#9AA1A8`.
- **Fontes:** **Space Grotesk** (títulos/corpo, bold e geométrica) + **Space Mono** (cupom, números,
  labels, cursor). Baixe de google/fonts (`ofl/spacegrotesk`, `ofl/spacemono`) e instale/coloque ao
  lado do HTML — mesma lógica da Montserrat em [saida-pdf.md](saida-pdf.md).
- **Logo:** aproximação `snaq` (branco) + `I` (verde) + `A` (branco). ⚑ **Trocar pelo SVG/logo oficial
  da snaq quando disponível** — o atual é aproximação.
- **Regras de conteúdo (importantes):**
  - **NÃO** incluir foto de professor.
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

## Como gerar
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
