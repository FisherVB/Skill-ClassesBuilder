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
