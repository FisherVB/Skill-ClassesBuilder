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

## 5. O que precisamos da marca para chegar a 100%
Cor, espaçamento, componentes e layout dá para replicar dos refs; a **fonte é Montserrat** (✔ resolvido).
Falta uma coisa que não dá para reverter por pixel:
1. **O logo oficial** (SVG ou PNG transparente) — hoje o `snaqIA` é desenhado no CSS (aproximação).
Com o logo, fecha 100%.
