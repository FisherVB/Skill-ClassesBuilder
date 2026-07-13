# CLAUDE.md — Workspace Classes Builder (snaq)

Este repositório é **duas coisas ao mesmo tempo**:
1. O **skill** portável `classes-builder` (`SKILL.md` + `references/`) — o método.
2. Um **workspace vivo** onde os casos de cada pessoa se acumulam (`pessoas/`) — os exemplos e o histórico.

Quando você (Claude) roda dentro deste repo, siga as regras abaixo **além** do `SKILL.md`.

## O que é este projeto

Descobrir e desenhar oportunidades de curso para a edtech da **snaq** (foco em construção e
crescimento de empresas), a partir de entrevistas em profundidade com especialistas. O método
completo está em [SKILL.md](SKILL.md). Este arquivo cuida de **como o workspace opera**.

## Estrutura de `pessoas/`

Cada especialista tem uma subpasta própria:

```
pessoas/
├── _template/                  # modelo — copie para começar uma pessoa nova
│   ├── transcricoes/           # inputs crus (qualquer formato: txt, md, vtt, pdf, colado)
│   └── resumo/
│       ├── dossie.md           # perfil com evidência (Fase 1)
│       └── decisao.md          # long-list + scoring + decisão final (Fases 2–4)
└── <nome-da-pessoa>/           # uma por especialista
    ├── transcricoes/
    └── resumo/
```

## Regras operacionais

### Ao receber conteúdo de uma pessoa nova
1. Crie `pessoas/<nome-da-pessoa>/` copiando o `_template/` (nome em kebab-case, ex.: `maria-silva`).
2. Salve a(s) transcrição(ões) / material bruto em `transcricoes/` (mesmo que tenha vindo colado no chat).
3. Rode o pipeline do skill (dossiê → long-list → scoring → saída).

### Consultar decisões anteriores (calibração, NÃO cópia)
Antes de finalizar o scoring de uma pessoa, **leia os `resumo/decisao.md` das pessoas anteriores**.
Use-os para:
- **Calibrar** estimativas de sizing e preço (o que já foi estimado antes, com que confiança).
- **Evitar duplicação** de tema no catálogo da snaq (não proponha um curso praticamente igual a um já decidido para outra pessoa, a menos que o ângulo/autoridade seja claramente diferente).
- **Manter consistência** de formato e critério entre casos.

> ⚠️ **Não copie o resultado anterior.** Casos passados são referência de método e mercado, não
> molde a repetir. Cada pessoa gera as suas sugestões a partir da própria evidência.

### Registrar o processo enquanto ele acontece
Trate `resumo/dossie.md` e `resumo/decisao.md` como **artefatos vivos**: escreva-os durante o
processo, não só no fim.
- `dossie.md` — vai sendo preenchido na Fase 1.
- `decisao.md` — registre a long-list (Fase 2), a tabela de scoring com fontes (Fase 3) e a decisão
  final com a justificativa do corte (Fase 4). É o **log de decisão** daquela pessoa: por que esses
  cursos, e não outros.

## Calibração dos pesos do scoring (aprendizado)

O **Score final** (ver `references/criterios-comerciais.md`) é `wA·Autoridade + wD·Demanda +
wM·Monetização + wE·Escala`. Os pesos abaixo são a **fonte da verdade** e **evoluem** conforme rodamos
professores — é assim que o skill aprende **onde o usuário quer cair**, sem heurísticas ad-hoc.

### Pesos atuais
| wA (Autoridade) | wD (Demanda) | wM (Monetização) | wE (Escala) |
|:--:|:--:|:--:|:--:|
| **0,30** | **0,30** | **0,20** | **0,20** |
_(default inicial — soma 1,00)_

### Loop de calibração (rodar ao fechar cada professor)
0. Considere a **ênfase declarada no Briefing (Passo 0, A4)** deste caso como **sinal** — não como
   override. Ela afina a leitura dos eixos; os pesos só mudam pelo padrão acumulado (passos 1–4).
1. Compare o **ranking do score** com a **escolha final** que o usuário validou.
2. Se houver **divergência sistemática** (ex.: o usuário repetidamente prefere temas de mais autoridade/
   alinhamento sobre temas de mais demanda/mercado, ou vice-versa), **proponha um ajuste pequeno** nos
   pesos (passos de ~0,05, mantendo a soma = 1,00) que teria reproduzido a escolha dele.
3. **Confirme com o usuário** antes de gravar. Ao gravar, **atualize a tabela acima** e registre no log.
4. Não mude peso por causa de **um** caso isolado — só quando o padrão se repete (≥ 2–3 casos).

### Log de calibração
| Data | De → Para (wA/wD/wM/wE) | Motivo (que padrão de escolha) |
|---|---|---|
| 2026-07-10 | — (default 0,30/0,30/0,20/0,20) | pesos iniciais |
| 2026-07-10 | mantido | 1º caso (Ricardo Catto): usuário escolheu mercado-primeiro → coincidiu com o default; sem ajuste |
| 2026-07-13 | mantido | Vinicius Catto: Briefing A4 = **Escala via mídia paga**. 1 caso isolado → não muda peso; **sinal anotado** (se ênfase em Escala recorrer em ≥2–3 casos, avaliar wE +0,05). Efeito neste caso ficou na leitura do eixo Escala e no go-to-market, não nos pesos |

> Enquanto houver poucos casos, os pesos ficam no default. A cada professor, o skill **anota** se a
> escolha do usuário bateu com o score; quando o padrão ficar claro, ajusta. Alinhamento de
> posicionamento entra pela **Autoridade** (real + atual), não por flag.

## Privacidade / versionamento

- `pessoas/` contém material real de pessoas reais e **não é versionado** por padrão (ver `.gitignore`).
  Só o `pessoas/_template/` entra no git.
- Se em algum caso específico você **quiser** versionar uma pessoa (com consentimento), force o add
  explícito daquela subpasta — mas confirme com o usuário antes.
- Nunca commite transcrições sem o usuário pedir explicitamente.

## Convenções

- Tudo em **português do Brasil**.
- Nomes de pasta de pessoa em **kebab-case**.
- O skill funciona **standalone** também: se não houver workspace `pessoas/` (ex.: transcrição colada
  num chat avulso), rode o pipeline e apresente os artefatos no chat, sem exigir a estrutura de pastas.
