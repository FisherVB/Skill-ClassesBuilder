# SS3 — Transcrição → Esqueleto dos Slides (.md)

Terceira etapa da esteira (ver `esteira-subskills.md`). Consome a **transcrição da entrevista da ss2** e
produz o **esqueleto slide-a-slide da aula**, em markdown, pronto para a ss4 transformar em deck.

> **A ss3 não desenha nada.** Ela decide **quantos slides, em que ordem, com que conteúdo** — e carrega,
> em cada slide, a **fala do professor** que sustenta aquele slide. É roteiro e material ao mesmo tempo.

## Por que verbatim em cada slide
Um esqueleto só com títulos e bullets **perde o ativo principal**: a voz do professor. É ela que
diferencia a aula dele de conteúdo genérico, e é dela que a ss4 (fala do slide) e a ss5 (peças, gravado)
vão precisar. Por isso **cada slide carrega uma "nota do professor"** — verbatim limpo + timestamp.

## Processo (6 passos)

1. **Higienizar.** Descobrir quem realmente fala (rótulos de ASR mentem — confira pela 1ª pessoa e pelo
   conteúdo), cortar preâmbulo/off-topic, delimitar o trecho útil por timestamp.
2. **Glossário de ASR.** Termo técnico degradado vira erro de aula. Liste as correções antes de destilar
   (ex.: "Herval evalde" → *evals/avaliação*).
3. **Mapear resposta ↔ pergunta (ss2)** e medir **cobertura**: respondida / parcial / **não respondida**.
4. **Montar o arco.** Módulos na **ordem pedagógica** (≠ ordem da entrevista): abre por "por que agora",
   fecha por "o que fazer segunda". Estime o tempo por módulo.
5. **Quebrar em slides.** ~1 ideia por slide. Inclua as **dinâmicas** que o professor já usa (enquetes,
   exercícios) como slides próprios.
6. **Fechar com lacunas e fidelidade.**

## Formato de cada slide (fixo)

```markdown
### Slide N — <título do slide>
**Conteúdo:** bullets do que aparece no slide (curto — é slide, não parágrafo)
**Visual:** o que a ss4 deve desenhar (diagrama, tabela, número gigante, foto…)
**Nota do professor:** > "verbatim limpo da fala dele" _(mm:ss)_
**Origem:** transcrição mm:ss · deck X pág. Y · [complemento]
```

Regras:
- **Conteúdo é slide, não texto corrido.** Se precisa de parágrafo, vira nota do professor.
- **Visual sempre preenchido** — mesmo que seja "só o número, gigante". A ss4 não deve adivinhar.
- **Marque `[complemento]`** quando o conteúdo veio de deck/pesquisa e não da boca dele.
- **Slides de dinâmica** (enquete, exercício) entram numerados como qualquer outro.

## Seções do arquivo de saída
1. **Ficha da aula** — professor, tema, público, promessa, formato/duração, objetivo estratégico interno
2. **Tese central** — a frase que o aluno leva (verbatim quando possível)
3. **Mapa dos módulos** — tabela: módulo · slides · tempo
4. **Os slides** — no formato acima, em ordem
5. **Frases de efeito** — as que viram slide de impacto, abertura e peça (ss5)
6. **Armadilhas & objeções** — o que ele desmente e como responde (serve à aula e ao comercial)
7. **Lacunas & follow-up** — o que ficou sem resposta + a pergunta para fechar
8. **Fidelidade & glossário** — verbatim × complemento; correções de ASR; erros de rotulagem

## Regras de ouro
1. **Preserve a voz** — limpe vício e repetição, **não reescreva o pensamento**.
2. **Nada entra sem lastro** — ou está na transcrição, ou é marcado como complemento.
3. **Lacuna é entregável** — liste e proponha o follow-up.
4. **A ordem pedagógica manda** — a entrevista é insumo, não roteiro.
5. **Credite terceiros que o professor credita** (frameworks adaptados) — fortalece a autoridade.
