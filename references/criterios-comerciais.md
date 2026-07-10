# Critérios Comerciais — Scoring, Sizing e Pesquisa

Referência carregada na **Fase 3**. Define a rubrica de pontuação, o protocolo de pesquisa web
(obrigatória) e o método de estimativa de mercado e preço para o Brasil.

## Rubrica de scoring (0–5 por eixo)

Pontue cada tema candidato da long-list em quatro eixos. Some com pesos para o score composto.

### 1. Autoridade (peso 30%)
Quão forte é o lastro do entrevistado neste tema específico?
- **5** — experiência rara, executada, com resultado e método próprio; poucos no país ensinariam melhor
- **3** — domínio sólido e comprovado, mas não excepcional/único
- **1** — sabe o suficiente, mas evidência rasa (competência 🟡/⚪ no dossiê)
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

**Score final = 0,30·Autoridade + 0,30·Demanda + 0,20·Monetização + 0,20·Escala** (escala 0–5, cada
eixo pontuado pela rubrica acima). É o número que ordena os candidatos e aparece na **coluna "Score
final"** da tabela. Bandas de leitura: **≥ 4,3 Forte · 3,5–4,2 Bom · < 3,5 Fraco**.

**Ajuste de alinhamento de posicionamento (flag, não recálculo).** Depois de calcular o score bruto,
verifique se o tema está **dentro do posicionamento/autoridade central atual** da pessoa (o que os
materiais mais recentes mostram que ela quer/está fazendo). Se um tema de **score alto** estiver
**fora** desse foco, **não o rebaixe no número** — mas marque-o com **⚑ fora de posicionamento** e
trate-o como **opção/swap**, não como recomendação automática do portfólio. A seleção final (Fase 4)
pondera score **e** alinhamento; explique sempre o trade-off. (Ex.: Ricardo — Governança Familiar
score 4,5 porém ⚑ fora de posicionamento → swap, não top-3.)

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
