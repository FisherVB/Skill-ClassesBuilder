# 🎓 Classes Builder — Claude Code Skill (snaq)

**Descoberta e desenho de oportunidades de curso a partir de entrevistas em profundidade com especialistas.**

Skill da suíte de edtech da **snaq** (ecossistema de construção e crescimento de empresas). Recebe
transcrições de entrevista com um profissional e descobre **quais cursos ele poderia ministrar** —
priorizando a interseção entre **autoridade real do professor** e **demanda comercial clara**.
Entrega dossiê do entrevistado, scoring dos temas e sugestões prontas com ICP, tamanho de mercado
(Brasil), faixa de preço e ementas nos três formatos da edtech.

> Não é um gerador de ideias soltas. É um funil: evidência da entrevista → temas candidatos →
> pontuação comercial validada com pesquisa → as melhores sugestões, com ementas.

---

## O que ele faz

1. **Dossiê do entrevistado** — lê todas as transcrições e monta um perfil com competências,
   ferramentas, setores, métodos próprios e experiências raras — **cada uma ancorada em evidência**.
2. **Long-list de temas** — brainstorm combinatório (competência × setor × ferramenta × framework).
3. **Scoring comercial** — pontua cada tema em Autoridade, Demanda, Monetização e Escala, **com
   pesquisa web obrigatória** para validar mercado, concorrência e preço.
4. **Sugestões finais** — número decidido pelo score (padrão 3, mas 2 ou 4 conforme a distribuição),
   com ICP, tamanho de mercado (BR), faixa de preço e as 3 ementas (workshop 2h / gravado 2h / programa 4×2h).

## Instalação

### Claude Code (Terminal)

```bash
# Copiar a pasta do skill para o diretório global de skills
cp -r Skill-ClassesBuilder ~/.claude/skills/classes-builder

# ou clonar e criar symlink
ln -s "$(pwd)/Skill-ClassesBuilder" ~/.claude/skills/classes-builder

# verificar
ls ~/.claude/skills/classes-builder/SKILL.md
```

O skill ativa automaticamente quando você fornece transcrições/trajetória de um profissional e pede
para descobrir cursos. Você também pode chamá-lo explicitamente.

### Claude.ai / Desktop
Suba a pasta como skill (Settings → Capabilities/Skills → Add). O `SKILL.md` é o ponto de entrada;
as `references/` são carregadas sob demanda.

## Uso

### Modo standalone (transcrição no chat)
Cole a transcrição (ou aponte para um arquivo/pasta) e peça:
```
Analise esta entrevista e me diga quais cursos essa pessoa poderia dar na snaq.
```

### Modo workspace (este repositório)
Rodando dentro do repo, o `CLAUDE.md` governa o acúmulo de casos:
```
pessoas/
└── <nome-da-pessoa>/
    ├── transcricoes/     # material bruto (qualquer formato)
    └── resumo/
        ├── dossie.md     # perfil com evidência
        └── decisao.md    # long-list + scoring + decisão final
```
Ao receber material de alguém novo, o Claude cria a pasta a partir de `pessoas/_template/`, roda o
pipeline, e registra o processo de decisão em `resumo/`. Decisões anteriores são consultadas como
**calibração** (sizing, preço, anti-duplicação) — nunca como molde a copiar.

## Estrutura

```
Skill-ClassesBuilder/
├── SKILL.md                          # método portável (pipeline em 4 fases)
├── CLAUDE.md                         # regras do workspace + loop de aprendizado
├── README.md
├── references/                       # carregadas sob demanda
│   ├── metodologia-analise.md        # Fase 1 — ler transcrição, inferir com evidência, dossiê
│   ├── catalogo-temas.md             # Fase 2 — motor combinatório + taxonomia + benchmarking
│   ├── criterios-comerciais.md       # Fase 3 — scoring, TAM/SAM/SOM, Público Meta Ads, Score final
│   ├── base-mercado.md               # Fase 3 — base de mercado viva (datada; calibra entre casos)
│   ├── formatos-produto.md           # Fase 4 — os 3 formatos fixos + templates de ementa
│   ├── template-saida.md             # Fase 4 — formato exato da saída (tabela única, 9 colunas)
│   ├── saida-pdf.md                  # Fase 4 — gerar o PDF da tabela (Montserrat, 1 página)
│   └── pecas-marketing.md            # Fase 4 — peça de divulgação + one-pager (identidade snaq)
├── assets/                           # templates HTML → PDF/PNG
│   ├── tabela-template.html          # tabela final de cursos
│   ├── peca-divulgacao-template.html # peça social 1080×1350
│   └── one-pager-template.html       # one-pager de venda A4
└── pessoas/
    └── _template/                    # modelo de caso (único versionado; casos reais no .gitignore)
```

## Princípios

- **Autoridade × Demanda.** Um tema só entra se a pessoa tiver lastro real **e** houver mercado pagante.
- **Evidência, não invenção.** Nenhuma competência sem trecho da entrevista que a sustente.
- **Demanda validada.** Mercado, concorrência e preço vêm de pesquisa web, com nível de confiança.
- **Específico vence genérico.** "IA para Corretores" > "Introdução à IA".

## Privacidade

`pessoas/` guarda material real de pessoas reais e **não é versionado** (só `pessoas/_template/`).
Transcrições nunca são commitadas sem pedido explícito.

## Compatibilidade

| Ferramenta | Suporte |
|---|---|
| Claude Code | ✅ Nativo |
| Claude.ai (Pro/Max/Team/Enterprise) | ✅ Via upload |
| Claude Desktop | ✅ Via import |

---

_Parte da suíte de skills de edtech da snaq._
