# Critérios Comerciais — Scoring, Sizing e Pesquisa

Referência carregada na **Fase 3**. Define a rubrica de pontuação, o protocolo de pesquisa web
(obrigatória) e o método de estimativa de mercado e preço para o Brasil.

## Rubrica de scoring (0–5 por eixo)

Pontue cada tema candidato da long-list em quatro eixos. Some com pesos para o score composto.

### 1. Autoridade (peso: ver CLAUDE.md)
Quão forte é o lastro do entrevistado **e quão alinhado ao que ele realmente é/quer ser hoje**?
Autoridade aqui é **real + atual**: não basta ter feito no passado — pesa se é onde o posicionamento
e a identidade atual da pessoa estão (o que os materiais mais recentes mostram que ela quer levar ao
mercado). É por aqui que o "alinhamento de posicionamento" entra no **score** — sem flag paralela.
- **5** — experiência rara, executada, com método próprio **e** é o centro do posicionamento atual dela
- **3** — domínio sólido e comprovado, mas **adjacente** ao foco atual (sabe fazer, não é onde ela quer atuar)
- **1** — evidência rasa (🟡/⚪) ou claramente fora da identidade atual
- **0** — sem lastro real (não deveria ter chegado até aqui)

### 2. Demanda (peso 30%)
Existe gente procurando aprender isso? Vende bem online? Cresce?
- Ancore em pesquisa (ver protocolo abaixo). Considere: volume de busca/interesse, número de
  profissionais no ICP, tendência (crescendo/estável/caindo), quantidade de lançamentos recentes.
- **5** — demanda alta e em crescimento, tema quente; **3** — demanda estável e real;
  **1** — nicho pequeno ou em queda; **0** — sem demanda perceptível.

### 3. Monetização (peso 20%)
Dá para cobrar bem? Empresa compra (B2B) ou só B2C?
- Ticket sustentável, disposição a pagar, possibilidade de venda corporativa/turmas in-company.
- **5** — ticket alto + B2B viável; **3** — ticket médio B2C saudável; **1** — só ticket baixo.

### 4. Escala (peso 20%)
Escala com mídia paga? ICP é buscável/segmentável? Mensagem clara para anúncio?
- **5** — ICP grande e segmentável, promessa clara e "anunciável"; **3** — escala moderada;
  **1** — nicho difícil de atingir por ads.

### Score composto
`Score = 0.30·Autoridade + 0.30·Demanda + 0.20·Monetização + 0.20·Escala` (0–5).

Registre a nota **e a justificativa de cada eixo** com o link/evidência de pesquisa. Sem
justificativa, a nota não vale.

## Quantas sugestões mostrar (regra de corte)

O número **não é fixo**. A partir dos scores ordenados:
- **Padrão: top 3.**
- **Mostre 2** se houver *gap* claro: os 2 primeiros bem acima e o 3º cai (ex.: queda ≥ ~1,0 ponto
  entre o 2º e o 3º, ou o 3º < 3,0).
- **Mostre 4** se houver empate forte no topo (4 candidatos praticamente colados e todos ≥ ~4,0).
- Nunca force um tema fraco só para fechar 3. Melhor 2 fortes que 3 com um fraco.
- Explique em uma linha por que parou naquele número (com base na distribuição dos scores).

## Formato recomendado para começar (por curso)

Para **cada curso** escolhido, indique **qual dos 3 formatos (workshop ao vivo · gravado · programa ao
vivo) é o melhor para *começar***. Não é o mais lucrativo no papel — é o de maior **aderência ao contexto**
(a pessoa, a dinâmica dela, a demanda e o risco). Heurística:

- **Workshop ao vivo (2h) — validar / de-riscar / esquentar.** Comece por aqui quando: o professor é
  ótimo comunicador mas **nunca deu curso formal** (testar execução com baixo custo); a promessa é uma
  **vitória rápida** ou um gancho quente; você quer **sinal de demanda** antes de investir produção; ou o
  tema é conceitual/visão (bom ao vivo, com Q&A). É o começo mais comum quando a confiança de execução é média.
- **Gravado (2h) — escalar / evergreen / massa.** Comece por aqui quando: a demanda é **ampla e escalável
  por mídia paga** (topo de funil), o conteúdo é **estável/evergreen**, a autoridade já é sólida, e o
  objetivo é **volume com custo marginal baixo**. Bom para cursos de massa e ticket menor.
- **Programa ao vivo (4×2h) — premium / profundidade / nicho.** Comece por aqui quando: o tema é
  **transformacional/profundo**, o público é **B2B/líderes** disposto a pagar por cohort/mentoria, o
  professor **sustenta profundidade ao vivo**, e a jogada é **margem por aluno**, não volume. Evite começar
  aqui se a execução ao vivo do professor é incerta (de-risque antes com workshop).

Cruze com o briefing (Passo 0): **prova ao vivo** e **track record de ensino** puxam para começar no
workshop (de-risco); **demanda de massa + escala** puxa para o gravado; **ticket alto + nicho B2B +
profundidade** puxa para o programa. Registre o formato recomendado **e a justificativa de contexto** na
tabela de saída (uma coluna/marcador "começar por").

## Protocolo de pesquisa web (OBRIGATÓRIO)

Você **deve** pesquisar. Não estime demanda/mercado/preço de memória. Para cada tema finalista
(e para os candidatos em dúvida no corte), rode:

1. **Demanda / tendência** — busque o tema + "curso", "treinamento", "bootcamp"; veja se há muitos
   players oferecendo (sinal de demanda) e se o interesse cresce. Termos em PT e EN.
2. **Concorrência** — quem já vende isso no Brasil? (G4, PM3, Tera, Alura, Rocketseat, Growth
   Machine, Conquer, StartSe, Descola, e escolas de nicho). Como posicionam, que formato, que preço.
   Cross-referencie com [catalogo-temas.md](catalogo-temas.md).
3. **Preço de referência** — colete faixas reais praticadas por concorrentes no formato equivalente.
4. **Sizing** — colete proxies para dimensionar o ICP (ver método abaixo).

Sempre cite as URLs. Marque **nível de confiança** (Alto / Médio / Baixo) em cada número que
depender de estimativa. Se não achar dado, diga que não achou e use um proxy explícito — nunca
invente número.

## Método de sizing — TAM / SAM / SOM (metodologia fixa)

Estime **sempre** em três níveis, cada um com o **número final em negrito**. É uma metodologia básica
mas **consistente entre casos** — o objetivo é comparabilidade, não precisão de consultoria. Cada
nível é um funil sobre o anterior, com os multiplicadores **declarados explicitamente**.

**Passo 0 — ICP em uma frase:** cargo + senioridade + tipo/porte de empresa + setor.

**TAM — universo total do ICP no Brasil.** Proxy de população do ICP inteiro. Fontes/proxies:
- Conselhos de classe (exato p/ verticais regulados): OAB 1,3 mi advogados, CFM ~635 mil médicos, CFC ~539 mil contadores.
- LinkedIn Campaign Manager / Sales Navigator (censo funcional por cargo+senioridade+localização).
- IBGE CEMPRE/RAIS (nº de empresas por porte/CNAE) quando o comprador é B2B/empresa.
- Associações setoriais (nº de fintechs, corretoras, agtechs, clínicas...).
→ Reporte o **TAM em negrito** (faixa) + fonte + confiança. Ex.: **~50–120 mil** líderes C-level.

**SAM — mercado endereçável.** TAM × filtros de realismo, **cada corte nomeado**: geografia atendida,
senioridade/renda que compra o preço-alvo, setores-alvo, e **propensão a se capacitar** (proxy:
penetração de players como PM3/Alura/IBGC na função). Ex.: TAM 120k × 60% sêniores × 50% em setores-alvo
= **SAM ~36 mil**.

**SOM — obtível em 12–18 meses.** SAM × taxa de captura realista de um curso novo (tipicamente
**0,5%–3%**). Ex.: SAM 36k × 1,5% = **SOM ~540 alunos/ciclo**. Cross-check bottom-up: alcance de canais
(orgânico + mídia paga) × conversão × ticket deve bater na mesma ordem de grandeza.

**Regras de saída (para a célula "Tamanho de mercado"):**
- Três linhas: **TAM**, **SAM**, **SOM** — número final de cada em **negrito**, com o multiplicador ao lado.
- Marque a **confiança** de cada nível (o SOM quase sempre é o mais incerto).
- **Triangule com o Público Meta Ads** (abaixo): o tamanho de audiência estimado da Meta é um
  segundo caminho para validar TAM/SAM — se divergir muito do proxy, sinalize.
- Complemente com qualitativo (crescimento? urgência? gatilho de mercado?).

## Público Meta Ads (derivar do ICP)

Logo depois do ICP, liste **interesses/segmentações da Meta (Facebook/Instagram Ads)** que alcançariam
esse público — serve para (a) operacionalizar a mídia paga e (b) **validar o sizing** (o estimador de
audiência do Gerenciador de Anúncios é um proxy independente de TAM/SAM).

Como derivar:
- A Meta **não** segmenta por cargo de forma confiável no Brasil → mire em **interesses, páginas,
  comportamentos e formação** correlacionados ao ICP.
- Traduza cada traço do ICP em 1–2 interesses concretos e **acionáveis na plataforma** (nomes que
  existem no Gerenciador). Ex.: fundador → "Empreendedorismo", "Pequenas e médias empresas",
  "Startup company"; líder de IA → "Inteligência artificial", "ChatGPT", "Automação"; executivo →
  "Liderança", "Harvard Business Review", "Endeavor", "StartSe".
- Combine **interesse + comportamento** (ex.: "administradores de página de empresa", "donos de
  pequenas empresas") para afunilar.
- Liste **5–8 segmentações** na célula, priorizando as mais específicas. Anote o **tamanho de
  audiência estimado** quando puder consultar, e use-o para cruzar com o SAM.

## Score final (metodologia)

**Score final = wA·Autoridade + wD·Demanda + wM·Monetização + wE·Escala** (escala 0–5). Os **pesos
`wA/wD/wM/wE` vivem no [CLAUDE.md](../CLAUDE.md)** e **não são fixos**: começam num default e vão
sendo **calibrados** conforme rodamos vários professores, para refletir onde o usuário quer chegar.
Use sempre os pesos atuais do CLAUDE.md. É o número que ordena os candidatos e aparece na **coluna
"Score final"**. Bandas: **≥ 4,3 Forte · 3,5–4,2 Bom · < 3,5 Fraco** (recalibre as bandas se os pesos mudarem).

**Alinhamento resolve-se no próprio score, não com flag.** Um tema de alta demanda mas fora do
posicionamento atual da pessoa **já cai** porque a **Autoridade** (real + atual) o penaliza. Não use
regra/flag paralela: se o usuário sistematicamente prefere/rejeita certos perfis de tema, isso é sinal
para **ajustar os pesos** (loop de calibração no CLAUDE.md) — não para criar exceções ad-hoc.

## Mapa de concorrência e whitespace (por tema)

Para cada finalista, monte um mini-mapa: **quem já vende isso no Brasil, a que preço, e como posiciona**.
O objetivo é achar **whitespace** — ângulo com demanda mas sem oferta direta (foi o que destravou o
melhor tema do caso Ricardo: todos vendem "use +IA", ninguém vende "preserve seu julgamento").
- Liste 3–6 concorrentes (nome, formato, preço, ângulo).
- Classifique o tema: **saturado** (muitos players no mesmo ângulo) / **disputado** / **whitespace**.
- Whitespace real **sobe a nota de Escala/Demanda**; saturação sem diferencial **desce**.
- Registre no `decisao.md` e alimente a [base-mercado.md](base-mercado.md).

## Faixas de preço (Brasil) por formato

Use como ponto de partida e **ajuste com a pesquisa de concorrência** de cada tema. Estas faixas
são preenchidas/atualizadas com os dados da pesquisa de mercado em
[catalogo-temas.md](catalogo-temas.md).

Faixas trianguladas por benchmarking (jul/2026) — ver detalhamento e fontes em
[catalogo-temas.md](catalogo-temas.md). Confiança: média (mercado fragmentado).

| Formato | Faixa plausível (BRL) | Sweet spot | Observações |
|---|---|---|---|
| Workshop ao vivo (~2h) | R$ 47 – 497 | R$ 97–297 | Ticket de entrada; topo de funil e captação de lista |
| Curso gravado (~2h) | R$ 27 – 297 | R$ 47–97 (ou incluso em assinatura) | Escalável, margem alta, sem custo marginal |
| Programa ao vivo (4×2h) | R$ 1.500 – 6.000 | ~R$ 2–4k | Cohort/turma; high-ticket de nicho pode passar de R$ 10k; ideal p/ B2B/in-company |

Âncoras de infoproduto BR: low ticket < R$ 97 · mid ~R$ 297–2.000 · high > R$ 2.000. Imersão
executiva presencial R$ 10–25k+ (StartSe R$ 18.500; ticket G4 Learning ~R$ 25k).

> Sempre prefira o preço real de um concorrente direto do tema (via pesquisa) a estas faixas
> genéricas. **B2B/in-company multiplica o ticket** — sinalize quando o tema permitir venda corporativa.

### Proxies rápidos de sizing (Brasil, jul/2026)
Âncoras iniciais de universo por vertical/função (refine com LinkedIn audience + IBGE CEMPRE/RAIS):
advogados **1,3 mi** (OAB) · médicos **~635 mil** (CFM) · contadores **~539 mil** (CFC) · fintechs
**~1,7–2,1 mil** · corretoras de seguros **~65 mil** (Susep) · agtechs **~2 mil** · demanda TIC
**~159 mil/ano** (Brasscom). Para função (PM, growth, vendas): use LinkedIn Campaign Manager /
Sales Navigator como censo funcional. Sempre triangule por dois caminhos e reporte faixa + confiança.

## Saída da fase

Tabela de scoring com os quatro eixos, score composto, justificativa + fontes por candidato, e a
decisão de corte (quantos e por quê). Isso vira a base do `resumo/decisao.md` no workspace e
alimenta a Fase 4 (saída final) — ver [template-saida.md](template-saida.md).
