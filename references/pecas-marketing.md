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

## Identidade visual snaq (fixa)

- **Fundo:** `#0E0F11` (quase preto). **Cards:** `#17181B`, borda `rgba(255,255,255,.08)`.
- **Verde snaq:** `#37E27C` (principal) / `#4BEA8A` (botão CTA). Texto branco; cinza `#9AA1A8`.
- **Fontes:** **Space Grotesk** (títulos/corpo, bold e geométrica) + **Space Mono** (cupom, números,
  labels, cursor). Baixe de google/fonts (`ofl/spacegrotesk`, `ofl/spacemono`) e instale/coloque ao
  lado do HTML — mesma lógica da Montserrat em [saida-pdf.md](saida-pdf.md).
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

## Montagem no PDF final (matriz 3×3)

O PDF de saída da pessoa é **multipágina** e junta a tabela + os assets como imagens:

- **Página 1** — a tabela comparativa de cursos (paisagem; ver [saida-pdf.md](saida-pdf.md)).
- **Depois, para CADA curso do portfólio, 3 páginas de asset** com **rótulo fixo** (a "taxonomia de
  assets" é a mesma para toda pessoa/curso):
  - **Asset 1 — Feed** (rede social, 1080×1350, com foto da pessoa)
  - **Asset 2 — Story** (rede social, 1080×1920, com foto da pessoa)
  - **Asset 3 — One-pager** (documento A4)

Com 3 cursos → 1 (tabela) + 9 (assets) = **10 páginas**. Ordem: Curso 1 (Asset 1/2/3) → Curso 2
(Asset 1/2/3) → Curso 3 (Asset 1/2/3). Cada página de asset leva um **rótulo** no topo, ex.:
`ASSET 1 · FEED — <Nome do curso>`.

**Como montar** (páginas de tamanhos diferentes convivem no merge):
1. Renderize a **tabela** → `tabela.pdf` (paisagem).
2. Para cada curso × formato, renderize o asset (Chrome `--screenshot` p/ feed/story PNG;
   `--print-to-pdf` p/ one-pager). Envolva cada imagem numa **página com o rótulo** (HTML simples:
   fundo, label no topo, imagem centralizada) e gere o PDF da página.
3. **Merge** tudo em ordem com pypdf:
   ```python
   from pypdf import PdfWriter
   w = PdfWriter()
   for pdf in ["tabela.pdf", "c1-asset1.pdf", "c1-asset2.pdf", "c1-asset3.pdf",
               "c2-asset1.pdf", ...]:
       w.append(pdf)
   w.write("Cursos_<pessoa>_completo.pdf")
   ```
Salve o PDF combinado em `pessoas/<pessoa>/resumo/` e ofereça cópia em `~/Downloads/`.

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

## Como gerar (cada asset)
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
