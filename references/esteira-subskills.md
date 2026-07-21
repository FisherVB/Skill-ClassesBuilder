# A esteira — sub-skills (ss1 → ss6)

Pipeline de produção de um curso, do material cru até a experiência final. Cada etapa consome a saída da
anterior. **A pessoa (professor) é a unidade**: tudo vive em `pessoas/<nome>/`.

| ss | De → Para | Saída | Ref |
|:--:|---|---|---|
| **ss1** | conteúdo cru (transcrições, decks, CV) → **temas de curso** | PDF: tabela de cursos + matriz de peças + **Mapa de Caminhos** | `SKILL.md` (Fases 1–4), `mapa-caminhos.md` |
| **ss2** | tema escolhido → **10 perguntas de entrevista** | roteiro de 10 perguntas (30–50 min) com probes | `ss2-perguntas-entrevista.md` |
| **ss3** | transcrição da entrevista → **esqueleto dos slides** | `.md` slide-a-slide, com nota do professor (verbatim) | `ss3-esqueleto-slides.md` |
| **ss4** | esqueleto → **slides de verdade** | deck na identidade snaq | `ss4-slides-design.md` |
| **ss5** | foto + voz → **professor-avatar** | experiência conversacional em tempo real | _anotado, não executar_ |
| **ss6** | material da aula → **outros formatos** | workshop / gravado / programa / peças | _a especificar_ |

## ss4 — slides de verdade (a especificar)
Consome o esqueleto da ss3 e produz o deck. **A identidade visual da snaq é fixa e já está extraída** —
reusar `references/design-system.md` (verde `#1EFD8A`, fundo `#16171A`, ink `#0B2E19`, Montserrat +
Space Mono, glow verde no canto, sem sombras, bordas retas). Pode agregar skills/libs de design
(ex.: a skill `pptx` para gerar `.pptx` nativo, ou HTML→PDF via Chrome headless, que já é o pipeline das
peças). Decisão em aberto: **formato de saída** (PPTX editável × PDF/HTML renderizado).

## ss5 — professor-avatar (anotado, não executar)
Ideia: a partir da **foto do professor** (já temos) + **amostras de áudio** dele (a pedir), clonar voz e
gerar uma experiência **o mais básica possível** onde o aluno **conversa em tempo real** com o "bonequinho"
do professor. Fica registrado como direção futura — **não implementar agora**.

## ss6 — outros formatos (a especificar)
Consome o material da aula e desdobra nos formatos de produto (workshop ao vivo / gravado / programa
4×2h) e nas peças. Aproveita o **formato recomendado para começar** já definido na ss1
(`criterios-comerciais.md`) e as **frases de efeito** extraídas na ss3.

## Princípios da esteira
1. **Cada etapa é auditável** — a saída de uma é a entrada legível da próxima (markdown, não caixa-preta).
2. **A voz do professor atravessa a esteira inteira** — verbatim entra na ss3 e sobrevive até a ss5/ss6.
3. **Lacuna é entregável** — cada etapa lista o que ficou faltando para a anterior resolver.
4. **Nada se inventa** — o que não veio do professor é marcado como complemento.
