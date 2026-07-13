# Briefing inicial (Passo 0) — limites factuais do professor

Antes da Fase 1, quando a skill roda **interativamente no chat**, faça um **briefing obrigatório**.
O foco são **fatos sobre o professor** que a transcrição não fixa com certeza e que **bounded a Autoridade**
e a **viabilidade dos formatos** — "até onde essa pessoa vai como professor". Nada de adivinhar a
estratégia da snaq: perguntas **objetivas**, que quem entrevistou/conhece a pessoa responde de imediato.

> **Regra:** no chat, o briefing é **obrigatório** e vem **antes** do dossiê. Em modo batch, não trave:
> use os defaults conservadores do fim e registre no `dossie.md` que rodou sem briefing.

## Bloco A — capacidade e limites (perguntas estruturadas, factuais)

Use uma pergunta interativa (ex.: `AskUserQuestion`). Se o usuário não souber uma, aplique o default.

**A1. Teto técnico — até que nível ele ensina com autoridade real?**
- **Iniciante** — introduz o tema, dá o mapa, mas não aprofunda
- **Intermediário** — põe a mão na massa junto com o aluno
- **Avançado** — constrói coisas não-triviais e responde dúvidas difíceis _(default se incerto)_
- **Ponta / referência** — dos melhores no tema; não é encurralado nem por especialista

**A2. Prova ao vivo — o que ele consegue fazer na frente do aluno?**
- **Constrói / coda ao vivo do zero** — demonstração real, sem rede
- **Demonstra em ferramentas prontas** — mostra funcionando, não constrói do zero _(default)_
- **Conceito + framework** — explica/slides, pouca demo prática

**A3. Track record de ensino — ele já ensinou/expôs isso?**
- **Recorrente** — dá aula/mentoria/palestra sobre o tema com frequência
- **Pontual** — já fez algumas vezes _(default)_
- **Nunca formalmente, mas explica muito bem** — cru em formato, forte no conteúdo
- **Cru em público** — pouca desenvoltura de palco; risco de execução

**A4. Case comprovável — a autoridade ancora em quê?**
- **Público e verificável** — produto no ar, números, portfólio que dá pra citar
- **Interno / sob NDA** — real, mas **não pode ser exposto** em marketing _(default: tratar como não-citável)_
- **Só o relato da entrevista** — sem prova externa

## Bloco B — abertas (mesmo turno, texto livre; todas opcionais)

1. **Onde ele é teto de mercado** vs. só "acima da média"? (destaque os temas em que é referência)
2. **Formatos/disponibilidade** que ele topa e consegue entregar: workshop ao vivo · gravado · programa
   ao vivo (4×2h) · mentoria em grupo/cohort · 1:1.
3. **Vetos / temas sensíveis / NDA** — o que não pode virar curso nem aparecer em peça.
4. **Materiais** além da transcrição (CV, métricas, decks) e a **foto** para as peças.
5. _(Opcional)_ Se você **já tem** uma intenção de posicionamento/objetivo pra esse professor, diga;
   senão, sigo pelo score.

## Como cada resposta entra no scoring

| Resposta | O que calibra |
|---|---|
| **A1 Teto técnico** | **Teto da Autoridade por tema:** tema acima do teto dele é **capado** (ou cai); define o nível de aluno que a ementa pode mirar (não prometer "avançado" se o teto é intermediário) |
| **A2 Prova ao vivo** | **Viabilidade de formato:** construir ao vivo habilita **programa premium ao vivo** (↑ Monetização) e molda a ementa (demo real × teoria); se é conceitual, peso no **gravado** |
| **A3 Track record** | **Autoridade "atual"** + **risco de execução** → move a **confiança** do scoring. "Cru em público" ⇒ recomendar primeiro o formato de menor risco (gravado/workshop) antes do programa ao vivo |
| **A4 Case comprovável** | **Força da evidência** da Autoridade: público+verificável ⇒ confiança alta e material p/ peças; interno/NDA ⇒ **não citar** número/claim nas peças (restrição de asset); só-relato ⇒ confiança menor, marcar como estimativa |
| **B1 Teto de mercado** | separa **Autoridade 5** (referência) de **4** (acima da média) por tema |
| **B2 Formatos** | quais **SKUs** são de fato ofertáveis (não montar programa ao vivo se ele só topa gravado) |
| **B3 Vetos/NDA** | remove temas/claims da long-list e das peças; registra o corte em `decisao.md` |
| **B4 Materiais/foto** | profundidade/confiança do dossiê + peças |
| **B5 Intenção (opcional)** | se houver, entra como contexto; **não** sobrescreve o score |

## Registro

Grave as respostas no topo do `pessoas/<nome>/resumo/dossie.md` (bloco "Briefing"), com data. Elas
explicam **por que a Autoridade e a confiança ficaram onde ficaram** — fazem parte do log de decisão.

## Defaults quando o briefing é pulado (batch ou "não sei")

Teto = **avançado** (conservador, sem prometer ponta) · Prova = **demonstra em ferramentas prontas** ·
Track record = **pontual** · Evidência = **interno/NDA ⇒ não citável** (marcar números como estimativa) ·
sem vetos · formatos = os três padrão · sem foto. Rebaixe **1 banda de confiança** de qualquer eixo que
dependia de um fato não coletado e registre no dossiê.
