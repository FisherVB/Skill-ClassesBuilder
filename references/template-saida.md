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

## 2. Tabela final de sugestões

Uma linha por curso, exatamente estas colunas:

```markdown
| Tema do curso | ICP | Tamanho de mercado (Brasil) | Faixa de preço | Ementa — Workshop ao vivo (2h) | Ementa — Curso gravado (2h) | Ementa — Programa ao vivo (4×2h) |
|---|---|---|---|---|---|---|
```

Como as tabelas markdown ficam apertadas com 3 ementas longas dentro, o padrão preferido é:
**tabela-resumo** (Tema · ICP · Tamanho · Preço) **seguida de uma seção por curso** com as três
ementas em blocos legíveis (usando os templates de [formatos-produto.md](formatos-produto.md)).

```markdown
### Sugestão 1 — <Tema do curso>
- **ICP:** <perfil específico de comprador>
- **Tamanho de mercado (Brasil):** <faixa + proxy + confiança>
- **Faixa de preço:** <workshop / gravado / programa, em BRL>

**Workshop ao vivo (2h)** … (blocos)
**Curso gravado (~2h)** … (módulos)
**Programa ao vivo (4×2h)** … (encontros)
```

### Orientações por coluna
- **Tema do curso** — nome comercial forte, específico e vendável. Nada genérico.
- **ICP** — perfil específico de comprador (cargo + senioridade + tipo/porte de empresa + setor).
- **Tamanho de mercado (Brasil)** — quantitativo (faixa + proxy) **e** qualitativo (crescimento/urgência),
  com nível de confiança. Método em [criterios-comerciais.md](criterios-comerciais.md).
- **Faixa de preço** — plausível para o mercado brasileiro, por formato; ancorada na concorrência.
- **Ementas** — seguindo os templates de [formatos-produto.md](formatos-produto.md); específicas,
  puxando os métodos e casos raros do dossiê.

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
