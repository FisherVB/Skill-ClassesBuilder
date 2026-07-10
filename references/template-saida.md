# Template de Saída

Referência carregada na **Fase 4**. Define o formato exato de apresentação: a tabela de scoring
(transparência da decisão) e a tabela final de sugestões.

## Ordem de apresentação

1. **Resumo do entrevistado** — 2–4 linhas puxadas do dossiê: quem é e onde mora a autoridade rara.
2. **Tabela de scoring** — mostra a long-list pontuada e justifica quantas sugestões serão exibidas.
3. **Sugestões finais** — tabela completa com ementas.
4. **Nota de estrutura do portfólio** — por que essas N sugestões, e que forma têm (independentes /
   básico→avançado / complementares + integrador).

## 1. Tabela de scoring (mostrar a decisão)

Liste os candidatos ordenados por score. Não precisa mostrar todos os ~20 — mostre pelo menos os
finalistas + os que ficaram no limite do corte.

```markdown
| # | Tema candidato | Autoridade | Demanda | Monetização | Escala | Score | Confiança | Notas / fontes |
|---|---|---|---|---|---|---|---|---|
| 1 | ... | 5 | 5 | 4 | 4 | 4,6 | Alta | link/evidência |
```

Feche com uma linha explicando o corte: _"Mostro 3 — top-3 todos ≥ 4,0 e distintos entre si"_ /
_"Mostro 2 — gap de 1,2 ponto para o 3º"_ / _"Mostro 4 — empate forte no topo"_.

## 2. Tabela final de sugestões (SEMPRE em tabela única)

> **Regra fixa:** a saída final é **uma única tabela**, uma linha por curso, com as três ementas
> dentro das células. Nada de "tabela-resumo + seções separadas" — o usuário quer comparar os cursos
> lado a lado, e isso só funciona com tudo na mesma tabela. Estas colunas, exatamente e nesta ordem:

```markdown
| Tema do curso | ICP | Público Meta Ads | Tamanho de mercado (TAM/SAM/SOM) | Faixa de preço | Ementa — Workshop (2h) | Ementa — Gravado (2h) | Ementa — Programa (4×2h) | Score final |
|---|---|---|---|---|---|---|---|---|
```

Para manter as ementas legíveis dentro da célula, use **`<br>`** entre os itens e um marcador curto
(`•` ou `E1/E2/...`). Cada item deve ser uma linha enxuta — título do bloco/módulo/encontro, não um
parágrafo. Exemplo de célula de workshop:
`• Os medos não-ditos do fundador<br>• Os 3 patrimônios: família, sociedade, gestão<br>• Caso real: reestruturação sem litígio<br>• Diagnóstico + Q&A`

A **tabela de scoring** (seção 1) também é tabela — então toda a entrega é comparável em formato de
tabela do começo ao fim.

**Entrega em PDF (padrão):** além da tabela em markdown no chat, gere sempre um **PDF** da tabela
final — Montserrat, uma página, colunas bem espaçadas, código de cor por curso. É o formato que o
usuário usa para comparar lado a lado. Procedimento e template em [saida-pdf.md](saida-pdf.md).

### Orientações por coluna
- **Tema do curso** — nome comercial forte, específico e vendável. Nada genérico.
- **ICP** — perfil específico de comprador (cargo + senioridade + tipo/porte de empresa + setor).
- **Público Meta Ads** — 5–8 interesses/comportamentos acionáveis no Gerenciador da Meta, derivados do
  ICP; também valida o sizing. Método em [criterios-comerciais.md](criterios-comerciais.md).
- **Tamanho de mercado (TAM/SAM/SOM)** — três níveis, **número final de cada em negrito**, com o
  multiplicador ao lado + confiança + uma linha qualitativa. Metodologia em [criterios-comerciais.md](criterios-comerciais.md).
- **Faixa de preço** — plausível para o mercado brasileiro, por formato; ancorada na concorrência.
- **Ementas** — seguindo os templates de [formatos-produto.md](formatos-produto.md); específicas,
  puxando os métodos e casos raros do dossiê.
- **Score final** — composto 0–5 (número + banda Forte/Bom/Fraco), com **⚑** se estiver fora do
  posicionamento atual da pessoa. Fórmula em [criterios-comerciais.md](criterios-comerciais.md).

## 3. Estrutura do portfólio

Escolha automaticamente a forma que melhor serve o entrevistado e explique em uma linha:
- **3 cursos independentes** — quando há 3 territórios fortes e distintos.
- **Básico → Intermediário → Avançado** — quando há um tema-mãe com profundidades.
- **2 complementares + 1 integrador** — quando dois temas conversam e um terceiro os une.

## Checklist de qualidade (antes de entregar)

- [ ] Toda competência usada tem evidência no dossiê (nada inventado).
- [ ] Todo número de mercado/preço tem fonte ou proxy explícito + nível de confiança.
- [ ] As sugestões são **distintas entre si**.
- [ ] Cada tema combina autoridade real **e** demanda validada.
- [ ] Nomes específicos e vendáveis, não genéricos.
- [ ] Número de sugestões justificado pelos scores.
- [ ] As três ementas de cada curso são coerentes (mesma promessa, três profundidades).
- [ ] Tudo em português do Brasil.
- [ ] (Workspace) dossiê e decisão salvos em `pessoas/<nome>/resumo/`.
