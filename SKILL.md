---
name: classes-builder
description: >
  Descoberta e desenho de oportunidades de curso a partir de entrevistas em profundidade
  com um especialista, para uma edtech focada em construção e crescimento de empresas.
  Lê transcrições (ou conteúdo colado no chat), monta um dossiê do entrevistado com
  competências e diferenciais ancorados em evidência, gera uma long-list de temas via
  brainstorm combinatório (competência × setor × ferramenta × framework), pontua cada
  candidato numa rubrica comercial (autoridade, demanda, monetização, escala) validada
  com pesquisa web, e entrega as melhores sugestões de curso com ICP, tamanho de mercado
  (Brasil), faixa de preço e ementas nos formatos da edtech (workshop ao vivo, curso
  gravado, programa ao vivo). Use este skill sempre que o usuário fornecer transcrições
  de entrevista, currículo ou trajetória de um profissional e pedir para descobrir,
  brainstormar, avaliar ou desenhar cursos que essa pessoa poderia ministrar; quando
  mencionar "temas de curso", "que curso essa pessoa daria", "oportunidade de curso",
  "ementa", "descoberta de cursos", "edtech", "snaq", ou pedir análise de autoridade e
  potencial comercial de um especialista para produto educacional. Também acione para
  registrar/consultar o histórico de decisões de cursos por pessoa dentro do workspace.
---

# Classes Builder — Descoberta de Cursos a partir de Entrevistas

Skill para transformar o conhecimento tácito de um especialista — capturado em entrevistas
em profundidade — em **oportunidades de curso comercialmente fortes** para a edtech da snaq,
focada no ecossistema de construção e crescimento de empresas.

O skill não busca apenas "o que a pessoa sabe ensinar". Busca a interseção entre **alta
autoridade do professor** e **alta demanda de mercado**, produzindo sugestões que uma
edtech de verdade lançaria e conseguiria escalar com mídia paga.

## Quando Ativar

Ative quando o usuário:
- Fornecer transcrições de entrevista (arquivo, pasta, ou texto colado no chat) e pedir
  para descobrir/brainstormar/avaliar cursos que a pessoa poderia dar
- Pedir análise de autoridade e potencial comercial de um especialista para curso
- Pedir ementas, ICP, tamanho de mercado ou pricing de um tema de curso
- Mencionar snaq, edtech, "temas de curso", "oportunidade de curso", "descoberta de cursos"
- Pedir para registrar ou consultar o histórico de decisões de curso de uma pessoa

## Princípio Central (leia sempre)

> **Autoridade real × Demanda comercial clara.** Um tema só entra se o entrevistado tiver
> repertório acima da média comprovável nas entrevistas **E** existir gente disposta a pagar
> para aprender aquilo. Faltando qualquer um dos dois, o tema cai.

Duas disciplinas inegociáveis:

1. **Evidência, não invenção.** Toda competência atribuída ao entrevistado deve ancorar num
   trecho concreto da entrevista (o que ele fez, decidiu, o nível de detalhe, a
   responsabilidade assumida). Você pode **inferir** competência a partir de como a pessoa
   conta os cases — mas a inferência precisa apontar para a evidência que a sustenta. Nunca
   atribua domínio sem lastro. Ver [references/metodologia-analise.md](references/metodologia-analise.md).

2. **Demanda validada, não achismo.** Tamanho de mercado, faixa de preço e concorrência são
   ancorados em **pesquisa web real** (você DEVE pesquisar) e marcados com nível de confiança.
   Ver [references/criterios-comerciais.md](references/criterios-comerciais.md).

## Pipeline (4 fases)

Execute nesta ordem. Cada fase produz um artefato; não pule para as sugestões antes de
completar o dossiê e o scoring.

### Fase 1 — Dossiê do entrevistado
Leia **todas** as transcrições com profundidade e monte um perfil consolidado com evidência
citada: competências técnicas, competências de gestão/liderança, padrões recorrentes nos
cases, ferramentas dominadas, setores conhecidos a fundo, metodologias/frameworks próprios,
e experiências raras ou difíceis de achar no mercado. Separe **explícito** (a pessoa afirma)
de **inferido** (você deduz do relato) e marque a força de cada evidência.
→ Formato e método em [references/metodologia-analise.md](references/metodologia-analise.md).

### Fase 2 — Long-list de temas (brainstorm combinatório)
A partir do dossiê, gere uma lista ampla (~10–20) de temas candidatos usando o motor
combinatório — Competência × Competência, Competência × Setor, Competência × Ferramenta,
Setor × Ferramenta, Framework Próprio × Competência. Cada candidato deve nascer amarrado a
uma competência real do dossiê. Prefira o específico e memorável ao genérico.
→ Motor, taxonomia e exemplos em [references/catalogo-temas.md](references/catalogo-temas.md).

### Fase 3 — Scoring comercial
Pontue cada candidato numa rubrica 0–5 em quatro eixos — **Autoridade**, **Demanda**,
**Monetização**, **Escala** — e calcule um score composto. Faça a pesquisa web aqui: valide
demanda, mapeie concorrência, ancore sizing e preço. Marque nível de confiança.
→ Rubrica, pesos e protocolo de pesquisa em [references/criterios-comerciais.md](references/criterios-comerciais.md).

### Fase 4 — Seleção e saída
A quantidade de sugestões é **decidida pelo score, não fixa**. Padrão: 3. Mas se a
distribuição pedir, mostre 2 (quando o top-2 abre gap claro sobre o 3º) ou até 4 (empate
forte). Para as escolhidas, entregue a tabela final com Tema · ICP · Tamanho de mercado (BR) ·
Faixa de preço · 3 ementas (workshop 2h / gravado 2h / programa 4×2h). As sugestões finais
devem ser **diferentes entre si** e coerentes como portfólio (independentes, ou
básico→intermediário→avançado, ou dois complementares + um integrador — escolha a estrutura
que melhor servir o entrevistado).
→ Formatos de produto e templates de ementa em [references/formatos-produto.md](references/formatos-produto.md).
→ Formato exato da saída (tabela única) em [references/template-saida.md](references/template-saida.md).
→ Além da tabela em markdown, **gere sempre o PDF** da tabela (Montserrat, uma página, bem espaçado) —
  ver [references/saida-pdf.md](references/saida-pdf.md) e o template [assets/tabela-template.html](assets/tabela-template.html).

## Workspace e histórico

Quando estiver rodando dentro do repositório do workspace (com pasta `pessoas/`), siga as
regras do `CLAUDE.md` da raiz: onde guardar transcrições novas, como consultar decisões
anteriores como **calibração** (nunca como molde a copiar), e como registrar o processo de
decisão em `pessoas/<nome>/resumo/`. Quando rodar standalone (ex.: transcrição colada no
chat, sem workspace), execute o pipeline normalmente e apresente os artefatos no chat.

## Regras de Ouro

1. Nunca atribua competência sem evidência na entrevista.
2. Sempre pesquise a web para validar demanda, concorrência, sizing e preço — e marque a confiança.
3. Autoridade sem demanda não vira curso. Demanda sem autoridade também não.
4. Número de sugestões é função do score, não um número fixo.
5. Prefira temas específicos e vendáveis a temas genéricos ("IA para X vertical" > "Introdução à IA").
6. As sugestões finais têm que ser distintas entre si e parecer algo que uma grande edtech lançaria.
7. Mantenha o dossiê e o log de decisão como artefatos escritos — eles são o produto tanto quanto a tabela.
8. Toda a saída em português do Brasil.
