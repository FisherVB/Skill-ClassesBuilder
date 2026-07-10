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

## Método de sizing de mercado (Brasil)

Estime de forma **defensável**, combinando quantitativo + qualitativo. Lógica ICP → TAM/SAM:

1. **Defina o ICP** com precisão (cargo + senioridade + tipo/porte de empresa + setor).
2. **Ache um proxy de população** do ICP no Brasil. Fontes/proxies úteis:
   - LinkedIn (nº de profissionais por cargo/localização — usar busca com filtros como proxy)
   - Dados setoriais e de associações (ex.: nº de clínicas, corretoras, fintechs, agências)
   - Nº de empresas por porte/CNAE (IBGE, dados de mercado)
   - Volume de comunidades/eventos do nicho
3. **Aplique funil realista:** TAM (todos do ICP) → SAM (os que buscam se capacitar/têm budget) →
   fatia capturável num lançamento. Seja explícito nas taxas de conversão assumidas.
4. **Complemente com qualitativo:** o tema está crescendo? é urgente/dor real? tem gatilho de
   mercado (nova tecnologia, regulação, hype)?
5. **Entregue como faixa + nota de confiança**, não como número cravado. Ex.: "~15–40 mil PMs em
   empresas de tech no Brasil (proxy LinkedIn, confiança Média); SAM plausível de alguns milhares
   com disposição a pagar por formação em IA aplicada a produto."

## Faixas de preço (Brasil) por formato

Use como ponto de partida e **ajuste com a pesquisa de concorrência** de cada tema. Estas faixas
são preenchidas/atualizadas com os dados da pesquisa de mercado em
[catalogo-temas.md](catalogo-temas.md).

| Formato | Faixa típica (BRL) | Observações |
|---|---|---|
| Workshop ao vivo (~2h) | (validar por pesquisa) | Ticket de entrada; ótimo para topo de funil e lista |
| Curso gravado (~2h) | (validar por pesquisa) | Escalável, ticket baixo/médio, margem alta |
| Programa ao vivo (4×2h) | (validar por pesquisa) | Ticket mais alto; cohort/turma; permite B2B/in-company |

> Sempre que a pesquisa trouxer números concretos de concorrentes, prefira-os a estas faixas
> genéricas. B2B/in-company costuma multiplicar o ticket — sinalize quando aplicável.

## Saída da fase

Tabela de scoring com os quatro eixos, score composto, justificativa + fontes por candidato, e a
decisão de corte (quantos e por quê). Isso vira a base do `resumo/decisao.md` no workspace e
alimenta a Fase 4 (saída final) — ver [template-saida.md](template-saida.md).
