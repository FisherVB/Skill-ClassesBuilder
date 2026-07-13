# Briefing inicial (Passo 0) — calibração antes do pipeline

Antes da Fase 1, quando a skill roda **interativamente no chat**, faça um **briefing obrigatório**
com o usuário. O objetivo é coletar o contexto que a transcrição **não** entrega — intenção da snaq,
público-alvo, modelo de monetização, vetos e posicionamento atual — para que o **scoring** (Autoridade,
Demanda, Monetização, Escala) seja calibrado com dados, não com achismo.

> **Regra:** no chat, o briefing é **obrigatório** e vem **antes** de montar o dossiê. Em modo batch
> (não-interativo), não trave: use os defaults abaixo e registre no `dossie.md` que o briefing não foi
> coletado.

## Bloco A — perguntas estruturadas (pergunte no chat)

Use uma pergunta interativa (ex.: `AskUserQuestion`) com as 4 questões abaixo. Se o usuário responder
"tanto faz" a qualquer uma, aplique o default e siga.

**A1. Objetivo da snaq com este professor agora?**
- **Carro-chefe / lançamento grande** — buscar volume, topo de funil
- **Expandir catálogo** — curso complementar ao que já existe _(default)_
- **Testar um tema/ângulo novo** — aposta exploratória
- **Curso premium de nicho** — alto ticket, público restrito

**A2. Que público a snaq quer priorizar para ele?**
- **B2C de massa** — profissionais e empreendedores individuais
- **Times / empresas (B2B)** — gestores, áreas, in-company
- **Nicho técnico avançado** — builders, devs, especialistas
- **O que o tema pedir** — sem preferência fixa _(default)_

**A3. Que modelo de monetização priorizar?**
- **Volume com ticket baixo** — workshop/gravado acessível, escala por mídia
- **Premium com ticket alto** — programa ao vivo, mentoria, cohort
- **Escada de produtos** — do acessível ao premium _(default)_
- **Sem preferência**

**A4. No corte final deste caso, o que deve pesar mais?** _(múltipla escolha)_
- **Autoridade / alinhamento** do professor
- **Demanda de mercado** (tema quente)
- **Monetização** (ticket / LTV)
- **Escala** via mídia paga (volume)

_Default de A4: nenhum realce — usa os pesos calibrados do `CLAUDE.md`._

## Bloco B — perguntas abertas (mesmo turno, texto livre)

No mesmo turno, em texto, peça (todas opcionais — o que o usuário tiver):
1. **Posicionamento / foco atual** da pessoa: como ela quer ser vista **hoje**? (alimenta a Autoridade "atual")
2. **Vetos ou temas sensíveis** a evitar (ex.: temas pessoais, compliance, exposição de terceiros).
3. **Materiais** além da transcrição (CV, métricas, decks, docs) — e onde estão.
4. **Foto da pessoa** para as peças de marketing — peça o arquivo/pasta (é também o Passo 0 das peças).

## Como cada resposta entra no scoring

| Resposta | O que calibra |
|---|---|
| **A1 Objetivo** | Ênfase entre Escala × Monetização × Demanda; e o **nº de sugestões** (ex.: premium de nicho tende a menos SKUs) |
| **A2 Público** | **ICP**, **Público Meta Ads**, o recorte de **SAM/SOM** e a faixa de ticket plausível |
| **A3 Monetização** | **Faixa de preço**, eixo **Monetização** e quais **formatos** priorizar (gravado barato × programa premium) |
| **A4 Ênfase** | Afina a leitura dos 4 eixos **e vira sinal para o loop de calibração dos pesos** no `CLAUDE.md`. **Não** sobrescreve os pesos ad-hoc — se o padrão se repetir em ≥2–3 casos, aí sim os pesos mudam pelo loop. |
| **B1 Posicionamento** | Autoridade **"real + atual"** (alinhamento entra por aqui, não por flag) |
| **B2 Vetos** | Remove temas da long-list; registra o corte em `decisao.md` |
| **B3 Materiais** | Profundidade e confiança do dossiê |
| **B4 Foto** | Peças de marketing (heros e sociais) |

## Registro

Grave as respostas do briefing no topo do `pessoas/<nome>/resumo/dossie.md` (bloco "Briefing"), com data.
Elas fazem parte do **log de decisão**: explicam por que o scoring pendeu de um jeito e não de outro.
Se A4 destoar sistematicamente dos pesos atuais, anote no **Log de calibração** do `CLAUDE.md` (não mude
peso por um caso isolado).

## Defaults quando o briefing é pulado (batch ou "tanto faz")

Objetivo = expandir catálogo · Público = o que o tema pedir · Monetização = escada de produtos ·
Ênfase = pesos vigentes do `CLAUDE.md` (sem realce) · sem vetos · só a transcrição · sem foto (peças
saem sem retrato ou com placeholder). Registre no dossiê que rodou com defaults.
