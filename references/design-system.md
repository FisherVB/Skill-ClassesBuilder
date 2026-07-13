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

## 6. Anatomia de composição — **medida dos ref-assets** (não dos nossos templates)

⚠️ Correção: esta seção descreve a composição **dos 3 arquivos reais** em `../assets/ref-assets/`,
medida por pixel. Os **tamanhos de fonte são estimados** de cap-height (marcados `~`); os **caracteres**
são contados do texto real dos refs; **posições/alturas de blocos são medidas** (px e %H do canvas).
Nota: os 3 refs são **dois feeds de layouts diferentes + um story** — nossa taxonomia (feed/story/
one-pager) mapeia: nosso feed ≈ ref3, nosso story ≈ ref2; **ref1 (feed-hero) ainda não replicamos**;
o **one-pager é formato nosso** (documento do deliverable, sem ref snaq).

### 6.1 ref-asset1 — FEED "HERO" (1080×1350) · foto grande do professor
Foco: **foto recortada grande do professor** + título gigante + CTA alto.

| Zona (medida) | y (%H) | Elemento | ~fonte / peso | chars reais |
|---|---|---|---|---|
| Topo | 4% | Pill de URL (borda verde) + logo (dir.) | ~20 mono / ~34 (logo) | url "www.snaq.co/curso-ia-builder" (28) |
| ~10% | — | Kicker "CURSO SNAQ" | ~40 / 700 MAIÚSC | 10 |
| ~15–28% | pico branco 21% | **Título gigante** "AI Builder" | **~180 / 800** branco | 2 palavras (~10) |
| ~34–42% | verde @38% | Subhead 3 linhas; **última expr. verde** ("segundo cérebro de IA.") | ~64 / 700 | ~18–22/linha |
| ~45–90% | — | **FOTO do professor: recorte grande** (esq., ~40–50% da largura, ancorada na base) | — | — |
| ~50% | — | Nome do professor (dir.) + cargo | ~64 / 800 · ~40 | "RAFAEL GIROLINETO" (17) |
| **73–88%** | **h≈204px** | **Botão CTA verde** (x0–808) "RESERVE SUA VAGA AGORA!" | ~72 / 800 `--ink` | ~11/linha × 2 |
| ~95% | — | Rodapé "VAGAS LIMITADAS → GARANTA A SUA!" | ~30 / 700 | ~32 |

### 6.2 ref-asset2 — STORY (1080×1920) · sem foto, grafismo domina
| Zona (medida) | y (%H) | Elemento | ~fonte / peso | chars reais |
|---|---|---|---|---|
| Topo | ~6% | **Logo grande centralizado** | ~64 / 700 | — |
| ~22–42% | verde @27–34% | **Headline gigante 4 linhas**; **2 palavras verdes** ("agente pessoal") | **~120 / 800** | ~8–11/linha × 4 |
| ~48–62% | pico branco 55% | Promessa (branco, trecho em bold) | ~52 / 400–700 | **~135 total** (~6 linhas) |
| dir. | — | **Grafismo 3D** (asterisco laranja = **Claude — NÃO usar**) | — | — |
| ~66% | — | Cupom-ticket (dark, perfuração) | mono | "IA30" |
| **72–87%** | **h≈292px** | **Bloco CTA verde** (w≈856) com pill "INSCRIÇÕES ABERTAS · INÍCIO 07/07" + "Curso AI Builder" + cursor | ~90 / 800 `--ink` | título ~16 |

### 6.3 ref-asset3 — FEED "GRID" (1080×1350) · 2×2 cards com bullets (DENSO)
| Zona (medida) | y (%H) | Elemento | ~fonte / peso | chars reais |
|---|---|---|---|---|
| ~5–13% | verde @9% | Header: **"AS 4 COISAS" verde** + "QUE VOCÊ VAI APRENDER NO CURSO DE IA" branco + **"do jeito Snaq" verde itálico + swoosh** | ~56 / 800 MAIÚSC | "AS 4 COISAS"(11) + ~35 + "do jeito Snaq"(13) |
| ~5–14% | — | **Selo do professor verde** (topo-dir., x628–1076) — foto recortada saindo pelo topo | nome ~30 / cargo ~16 | — |
| ~18–82% | branco @49% | **2×2 cards**: nº verde (01–04) + **título MAIÚSC** + **3–5 bullets** | título ~34 / 700 · bullet ~26 / 400 | título ~20–30; cada bullet ~50–90 (2 linhas) |
| **87%** | **h≈100px** | **Cupom (dark, esq.) + CTA verde (dir., x244–1076) lado a lado** | CTA ~40 | "LANCAMENTO40" · "Garanta sua vaga" |

**Diferenças-chave dos meus templates (a corrigir se quisermos fidelidade total):**
- Feed real (ref3) tem **3–5 bullets por card** (denso). Meu feed usa só título + 1 linha (mais limpo) — foi **escolha minha**, não do ref.
- Feed real posiciona **cupom e CTA lado a lado**; o meu empilha (cupom em cima, CTA embaixo).
- Existe um **feed-hero (ref1)** com foto grande recortada — layout que eu **não tenho**.
- Story real (ref2) **não tem foto** (usa grafismo); coloquei foto no badge por decisão nossa.
- Título gigante: refs usam fontes bem maiores (~120–180px) do que as minhas (60–106px).

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
