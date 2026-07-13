# Design System snaq (extraído dos refs)

Contrato visual para as peças de marketing. **Fonte da verdade = as imagens em
[../assets/ref-assets/](../assets/ref-assets/)** (`ref-asset1` feed hero · `ref-asset2` story ·
`ref-asset3` feed "4 coisas"). Tokens abaixo foram **amostrados por pixel** desses arquivos — use-os
literalmente, não de memória.

## 1. Cores (tokens — hex amostrado)

| Token | Hex | Uso |
|---|---|---|
| `--green` | **#1EFD8A** | Verde primário (neon/mint). Realces, cupom, CTA, bullets, números. **É este, não #37E27C.** |
| `--green-deep` | **#16C46F** | Verde escuro (gradiente/pressionado, sombra do botão) |
| `--ink` | **#0B2E19** | Verde quase-preto — **texto sobre botões verdes** |
| `--bg-hero` | **#2D2E2B** | Fundo do feed-hero (charcoal quente, com glow verde) |
| `--bg` | **#171919** | Fundo padrão (feed/cards) |
| `--bg-story` | **#131314** | Fundo do story (quase-preto) |
| `--white` | **#F1F1F0** | Texto branco (levemente off-white) |
| `--gray` | **#9DA0A0** | Texto secundário |
| `--card-line` | **#3D3F40 / rgba(255,255,255,.08)** | Bordas/hairlines dos cards |
| ~~laranja~~ | #F97A46 | **É o asterisco do Claude — NÃO usar** (a menos que o curso seja sobre Claude) |

Glow: há um **brilho verde radial** difuso no fundo (canto/atrás do conteúdo) — `radial-gradient`
com `--green` em alpha ~8–14%.

## 2. Tipografia

- **Família:** **Montserrat** (confirmado pela marca). Geométrica; usar o arquivo variável
  `Montserrat.ttf` (pesos 100–900). Baixe de google/fonts (`ofl/montserrat`).
- **Pesos:** títulos em ExtraBold/Bold (800/700); corpo em Regular/Medium.
- **Mono:** cupom, códigos e labels em **Space Mono** (confere com os refs).
- **Caixa:** títulos de peça às vezes em CAIXA ALTA (feed "AS 4 COISAS…"); hero em Title Case.

## 3. Componentes (anatomia)

- **Logo:** `snaq` (branco) + `I` (verde `--green`) + `A` (branco), lowercase pesado. No story vem
  **grande e centralizado** no topo; no feed vem menor (canto). ⚠️ **É aproximação — precisamos do
  logo oficial (SVG/PNG)** (§5).
- **Realce no título:** título branco com **uma expressão-chave em verde** (ref: "AS 4 COISAS" verde;
  "agente pessoal" verde; "segundo cérebro de IA" verde). No feed "4 coisas" há também **"do jeito
  snaq" em verde itálico** com **swoosh** (risco à mão) verde por baixo.
- **Selo do professor:** badge **verde** arredondado com "ministrado por / NOME / cargo" (texto
  `--ink`) e **foto recortada** (redonda ou meia-sangria saindo pelo topo).
- **Cards (feed):** retângulos `--bg`+borda, número mono verde (01–04), título bold branco, **e
  bullets** (o ref tem bullets — não só título).
- **Cupom (ticket):** faixa escura com **perfuração tracejada** vertical; "USE O CUPOM" + código mono
  verde; à direita preço riscado (gray) → preço grande (branco) → "% OFF" verde.
- **Botão CTA:** retângulo **verde vibrante**, texto `--ink` bold, com **cantinho dobrado (estilo
  adesivo/sticker)** e às vezes um **pill interno** ("INSCRIÇÕES ABERTAS · INÍCIO 07/07"). Ícone de
  **cursor (mãozinha)** no canto.
- **Pill/tag:** cápsula com borda verde ou fundo `--ink`, texto pequeno.

## 4. Fundos por formato
- **Feed hero** (`ref1`): `--bg-hero` #2D2E2B + glow verde + grafismo (cérebro de código) — opcional.
- **Feed "4 coisas"** (`ref3`): `--bg` #171919 + fumaça/glow verde no canto.
- **Story** (`ref2`): `--bg-story` #131314, mais limpo, logo grande centralizado.

## 6. Anatomia de composição por asset

Especificação de layout de cada peça: escala tipográfica, **orçamento de caracteres** por elemento
(quantos cabem sem estourar/quebrar feio — escreva o conteúdo para caber), imagem e ritmo. Valores em
px salvo indicação. "chars" = limite prático por linha (Montserrat) × nº de linhas.

### 6.1 FEED — 1080×1350 (densidade média)
Margem segura: 58px lados / 56–58 topo-base → **área útil ~956px** de largura.

| Elemento | px / peso | Caixa | Cor | Linhas | ~chars (orçamento) |
|---|---|---|---|---|---|
| Logo | 36 / 700 | — | branco+verde | 1 | fixo |
| Selo professor — nome | 23 / 700 | — | `--ink` | 1 | ~22 |
| Selo professor — cargo | 12 / 500 | — | `--ink` | 1 | ~34 |
| **H1** (título) | **60 / 700** | MAIÚSCULA | branco (1ª expressão **verde**) | **2 fixas** | **~24–26/linha** |
| H1 — nome do curso | 40–58 / 700 itálico | Title | **verde** + swoosh | 1 (ideal) | **≤~28 a 58px; nome longo → cair p/ 40px (~40)** |
| Sub (promessa) | 21 / 400 | frase | `--gray` | 2 | **~130–150 total** |
| Card — número | 28 / 700 mono | — | verde | 1 | 2 (01–04) |
| Card — título (H3) | 26 / 700 | Title | branco | 1–2 | **~28 (1 linha) / ~56 (2)** |
| Card — apoio (P) | 16 / 400 | frase | `--gray` | 2 | **~90–100** |
| Cupom — código | 34 / 700 mono | MAIÚSC | verde | 1 | ~12 |
| Cupom — preço novo | 40 / 700 | — | branco | 1 | ~9 |
| CTA — URL | 29 / 700 itálico | — | `--ink` | 1 | ~34 |

- **Imagem:** foto do professor **92×92px, círculo**, anel `--ink` 3px, dentro do selo verde (topo-direita). Sem outra imagem (fundo é charcoal + glow).
- **Grid:** 2×2 cards, gap 16, card ~470px (padding 24×28 → conteúdo ~414px).
- **Ritmo (topo→base):** logo+selo → H1 (3 linhas) → sub → grid 2×2 → cupom → CTA. CTA sempre encostado no rodapé.

### 6.2 STORY — 1080×1920 (densidade limpa)
Margem segura: 76px lados / 96 topo, 84 base → **área útil ~928px**.

| Elemento | px / peso | Caixa | Cor | Linhas | ~chars |
|---|---|---|---|---|---|
| Logo | **56 / 700, centralizado** | — | branco+verde | 1 | fixo |
| Kicker | 20 / 400 mono | MAIÚSC | verde | 1 | ~34 |
| **Gancho (hook)** | **106 / 700** | Title | branco (**1 palavra/expr. verde**) | **3** | **~14–15/linha (~40 total) — tem que ser curtíssimo** |
| Nome do curso | 44 / 700 | Title | verde | 1 | ~36 |
| Subtítulo | 26 / 400 | — | `--gray` | 1 | ~46 |
| Selo — nome | 36 / 700 | — | branco | 1 | ~26 |
| CTA — URL | 36 / 700 itálico | — | `--ink` | 1 | ~28 |
| Cupom (linha) | 24 / 400 mono | — | gray+verde | 1 | ~50 |

- **Imagem:** foto **132×132px, círculo**, anel verde 3px (badge horizontal com nome/cargo). Sem grafismo (o ref usa um asterisco 3D laranja = **Claude**, que não usamos).
- **Composição:** o gancho **domina** o terço superior; muito **respiro** (espaço vazio proposital) no meio; foto+cupom+CTA no rodapé. É a peça mais "arejada".

### 6.3 ONE-PAGER — A4 210×297mm (densidade carregada / documento)
Margem: 15mm. **Não é social** — é o único que "enche".

| Elemento | px / peso | Cor | ~chars |
|---|---|---|---|
| H1 (nome do curso) | 35 / 800 | branco | ~34/linha (≤2 linhas) |
| Subtítulo | 18 / 600 | verde | ~60 |
| Promessa | 13,5 / 400 | claro | ~230–260 (3 linhas) |
| Data strip — número (×3) | 18 / 700 mono | verde | 2–6 (ex.: "53,6%") |
| Data strip — texto (×3) | 10,5 / 400 | gray | ~60 |
| Learn card — título (×4) | 14,5 / 700 | branco | ~26 |
| Learn card — apoio (×4) | 11,5 / 400 | gray | ~80 |
| Formato — preço (×3) | 18 / 700 | verde | ~14 |
| Para quem é | 12 / 400 | gray | ~180 |

- **Imagem:** foto **38×38px** (mini, no crédito "com [nome]"). Documento, foto é opcional/discreta.
- **Estrutura:** hero → data strip (3 provas) → "o que vai aprender" (2×2) → formatos (3) → para quem → CTA. Tudo tem que caber em **1 página A4** (se estourar, reduzir fontes/margens — ver `saida-pdf.md`).

## 7. Princípios de composição (o "não-mapeável")
- **Um foco por peça social:** feed = a lista "4 coisas"; story = o gancho. Não competir dois focos.
- **Verde é acento, não preenchimento:** ~1 expressão realçada no título + números + cupom + CTA. O
  resto é branco/cinza sobre escuro. Verde demais quebra a marca.
- **Contraste de peso:** título ExtraBold/Bold gigante vs. corpo Regular pequeno — hierarquia forte.
- **CTA sempre no rodapé**, verde cheio, texto `--ink`, largura total; **cupom colado** acima/ao lado.
- **Foto sempre circular**, com anel (`--ink` no feed, verde no story).
- **Respiro proporcional à densidade:** story arejado, feed médio, one-pager cheio.
- **Alinhamento:** social alinhado à esquerda (menos o logo do story, centralizado); rótulos em mono.
- **Orçamento de texto é lei:** se o conteúdo não cabe no orçamento de chars da tabela, **encurte o
  texto** — não diminua a fonte (a escala é da marca). Nomes de curso longos são a exceção (cair 1 nível).
- **Glow verde** sempre no mesmo canto (topo-direita) — coerência entre peças.

## 8. O que precisamos da marca para chegar a 100%
Cor, espaçamento, componentes e layout dá para replicar dos refs; a **fonte é Montserrat** (✔ resolvido).
Falta uma coisa que não dá para reverter por pixel:
1. **O logo oficial** (SVG ou PNG transparente) — hoje o `snaqIA` é desenhado no CSS (aproximação).
Com o logo, fecha 100%.
