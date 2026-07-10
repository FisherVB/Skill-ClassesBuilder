# Saída em PDF — Tabela de Cursos

Referência da **Fase 4**. Além da tabela em markdown no chat, a entrega final padrão inclui um **PDF
da tabela** — bem espaçado, em Montserrat, uma página. É o formato que o usuário usa para comparar os
cursos lado a lado (markdown em tela fica apertado). Sempre gere o PDF ao fechar as sugestões.

## Especificação de design (fixa)

- **Fonte:** Montserrat em tudo (pesos 500/600/700).
- **Formato:** tabela única, 7 colunas (Tema · ICP · Tamanho de mercado · Faixa de preço · 3 ementas),
  uma linha por curso (2 a 4 cursos).
- **Uma página**, largura ~390mm, altura **ajustada ao conteúdo** (sem espaço branco sobrando).
- **Cabeçalho** em ink escuro (#14243B), rótulo do formato de cada ementa em dourado (#B98A44).
- **Código de cor por curso:** faixa lateral + tint suave na 1ª célula (teal / roxo / terracota / azul)
  — ajuda a bater o olho e comparar linha a linha.
- **Espaçamento generoso** (padding ~20px/célula; bullets com respiro). Nunca deixar apertado.
- **Preço** em blocos empilhados (Workshop / Gravado / Programa) com rótulo pequeno em maiúsculas.
- **Só o conteúdo da tabela** — sem título, cabeçalho de página ou texto extra (a menos que o usuário peça).

O template pronto (CSS + estrutura + linha de exemplo) está em
[../assets/tabela-template.html](../assets/tabela-template.html). Copie, preencha o `<tbody>` com uma
`<tr class="rN">` por curso, e renderize.

## Procedimento

### 1. Garantir a fonte Montserrat
Instalar em `~/Library/Fonts` (macOS) **ou** deixar `Montserrat.ttf` ao lado do HTML:
```bash
curl -sL -o Montserrat.ttf "https://github.com/google/fonts/raw/main/ofl/montserrat/Montserrat%5Bwght%5D.ttf"
cp Montserrat.ttf ~/Library/Fonts/Montserrat-Variable.ttf   # opcional, mas ajuda o Chrome a achar
```

### 2. Preencher o template
Copie `assets/tabela-template.html` para o diretório de trabalho, preencha `<tbody>`. Uma `<tr>` por
curso; classes `r1..r4` definem a cor. Use `<em>` para itálico, `li.bonus` para o bônus, `.enc` (E1/E2)
nos encontros do programa.

### 3. Ajustar a altura da página (para caber em 1 página, sem sobra)
A largura de conteúdo do PDF = largura da página − 2× margem (ex.: 390 − 32 = 358mm ≈ 1353px @96dpi).
Meça a altura real do conteúdo nessa largura e defina `@page size` = altura do conteúdo + margens:
```bash
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
"$CHROME" --headless=new --disable-gpu --hide-scrollbars --force-device-scale-factor=1 \
  --window-size=1353,2400 --screenshot="measure.png" "file://$PWD/tabela.html"
python3 - <<'PY'
from PIL import Image
im=Image.open("measure.png").convert("RGB"); w,h=im.size; px=im.load()
def blank(y):
    return all(px[x,y][0]>=245 and px[x,y][1]>=245 and px[x,y][2]>=245 for x in range(0,w,7))
bottom=next(y for y in range(h-1,-1,-1) if not blank(y))
mm=bottom/96*25.4
print("altura conteudo ~", round(mm,1),"mm | page height sugerida:", round(mm+32+4),"mm (margens 32 + folga 4)")
PY
```
Edite a linha `@page{ size:390mm <ALTURA>mm; margin:16mm; }` com a altura sugerida.

### 4. Renderizar o PDF
```bash
"$CHROME" --headless=new --disable-gpu --no-pdf-header-footer \
  --print-to-pdf="cursos-<pessoa>.pdf" "file://$PWD/tabela.html"
# conferir que ficou em 1 página:
python3 -c "from pypdf import PdfReader as R; p=R('cursos-<pessoa>.pdf').pages; print('paginas:',len(p))"
```
Se der 2 páginas, aumente a altura do `@page`. O Chrome embute o subset da Montserrat no PDF → abre
igual em qualquer máquina.

### 5. Onde salvar
No workspace: `pessoas/<pessoa>/resumo/cursos-<pessoa>.pdf`. Ofereça também copiar para `~/Downloads/`.

## Fallbacks
- **Sem Chrome/Chromium:** entregue o `tabela.html` pronto (o usuário abre no navegador e faz
  "Imprimir → Salvar como PDF") e avise que o PDF automático não pôde ser gerado aqui.
- **Sem internet para a fonte:** se Montserrat não estiver disponível, use o fallback do `@font-face`
  (`local(...)`), avise que a fonte pode cair para a padrão do sistema, e ofereça reprocessar depois.
- **Para impressão física:** ofereça uma versão A3 paisagem ou A4 em múltiplas páginas (o padrão é um
  canvas único grande, otimizado para tela).
