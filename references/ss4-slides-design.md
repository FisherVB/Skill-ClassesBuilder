# SS4 — Esqueleto → Slides de verdade (identidade snaq)

Quarta etapa da esteira. Consome o **esqueleto da ss3** (`ss3-slides-transformai.md` e equivalentes) e
produz o **deck da aula**, na identidade visual da snaq.

## Saída: PPTX (+ PDF)
- **PPTX é o entregável principal.** A **"nota do professor"** de cada slide da ss3 vira **speaker note**
  nativa (o professor apresenta lendo dali), e o time consegue editar.
- **PDF** é gerado junto, só para distribuição.
- Ferramenta: **pptxgenjs** (via a skill `pptx`). 16:9 — `LAYOUT_WIDE` (13.3in × 7.5in).

## Tokens (fixos — não perguntar, hard-coded)
Herdados de `design-system.md`, sem `#` (regra do pptxgenjs):

| Token | Hex | Uso |
|---|---|---|
| `BG` | `16171A` | fundo de tudo |
| `PANEL` | `1C1D21` | cards e blocos |
| `GREEN` | `1EFD8A` | acento único, números, destaques |
| `INK` | `0B2E19` | texto sobre verde |
| `WHITE` | `F1F1F0` | títulos e corpo |
| `GRAY` | `9DA0A0` | legendas e apoio |
| `LINE` | `2A2C31` | bordas sutis |

**Tipografia:** **Montserrat** (títulos e corpo) · **Space Mono** (kickers, números, rótulos, códigos).
**Regras visuais:** sem sombras · sem barras/faixas decorativas · glow verde radial no canto (entra como
**imagem de fundo**, porque pptxgenjs não faz gradiente) · um acento só (verde) · respiro generoso.

## Arquétipos de slide (o gerador implementa; a ss3 escolhe pelo campo `Visual`)
| # | Arquétipo | Quando usar |
|---|---|---|
| `capa` | título + subtítulo + assinatura | abertura |
| `impacto` | **uma frase gigante**, nada mais | viradas de raciocínio |
| `numero` | stat gigante + legenda curta | 10-15%, 48 meses, 15% dos dados |
| `cards` | 2–4 blocos lado a lado (título + texto) | modos, camadas, armadilhas, bio |
| `espectro` | régua horizontal de 5 estágios | os 5 modos (slide-mãe) |
| `timeline` | marcos em linha | desde 2018 |
| `comparacao` | dois lados com divisor | antes × depois, dois caminhos |
| `enquete` | pergunta + código, tela limpa | dinâmicas ao vivo |
| `ficha` | campos numerados preenchíveis | exercício/compromisso |
| `cta` | fecho + convite | último slide |

## Processo
1. **Ler o esqueleto** da ss3; cada slide já traz `Conteúdo`, `Visual`, `Nota do professor`, `Origem`.
2. **Mapear `Visual` → arquétipo.** Se o campo estiver vago, escolher pelo conteúdo (frase solta →
   `impacto`; um número → `numero`; 2-4 itens → `cards`).
3. **Gerar** com pptxgenjs; **a nota do professor vira `slide.addNotes()`** — verbatim, com timestamp.
4. **Validar**: `python scripts/office/validate.py deck.pptx`.
5. **QA visual**: converter para imagens e inspecionar **todos** os slides — procurar overflow de texto
   (o defeito nº1), sobreposição e contraste.
6. **Exportar PDF** e entregar os dois na pasta do professor.

## Regras de ouro
1. **Uma ideia por slide.** Se não cabe, quebra em dois — nunca encolher a fonte até caber.
2. **O texto do slide é curto; o texto longo é speaker note.** A ss3 já separou — respeitar.
3. **Nunca inventar conteúdo** no design. Se faltou, o slide fica com a lacuna visível.
4. **Créditos de terceiros** (frameworks adaptados) aparecem em rodapé pequeno no slide de origem.
5. **QA de overflow é obrigatório** — Montserrat pode ser substituída no render de QA; deixar ~10% de
   folga nos blocos de texto.
