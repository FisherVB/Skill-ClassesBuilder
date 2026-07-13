# Saída em PDF — Tabela de Cursos

Referência da **Fase 4**. Além da tabela em markdown no chat, a entrega final padrão inclui um **PDF
da tabela** — bem espaçado, uma página, **na identidade snaq** (fundo escuro, Poppins, acentos verdes).
É a página 1 do PDF combinado (ver [pecas-marketing.md](pecas-marketing.md) para a página 2, a matriz
de assets). Sempre gere o PDF ao fechar as sugestões.

## Especificação de design (fixa — identidade snaq)

- **Fonte:** **Poppins** (títulos/corpo) + **Space Mono** (labels: TAM/SAM/SOM, formatos, score, header).
- **Fundo escuro** (`#0E0F11`); células em painel `#17181B`; texto claro; hairlines translúcidas.
- **Verde snaq** `#37E27C` nos rótulos do cabeçalho, preços e bullets do 1º curso.
- **Formato:** tabela única, 9 colunas (Tema · ICP · Público Meta Ads · Tamanho TAM/SAM/SOM · Faixa de
  preço · 3 ementas · Score final), uma linha por curso (2 a 4 cursos).
- **Uma página**, largura ~520mm, altura **ajustada ao conteúdo**.
- **Cabeçalho** preto com linha verde embaixo; rótulo do formato em Space Mono verde.
- **Código de cor por curso:** faixa lateral + acento (verde `--c1` / azul `--c2` / âmbar `--c3`) nos
  bullets e no Score — ajuda a comparar linha a linha.
- **Espaçamento generoso** (padding ~18px/célula). Nunca deixar apertado.
- **Só o conteúdo da tabela** — sem título ou texto extra (a menos que o usuário peça).

O template pronto (CSS + estrutura + linha de exemplo) está em
[../assets/tabela-template.html](../assets/tabela-template.html). Copie, preencha o `<tbody>` com uma
`<tr class="rN">` por curso, e renderize.

## Procedimento

### 1. Garantir as fontes (Poppins + Space Mono)
Instalar em `~/Library/Fonts` (macOS) **ou** deixar os `.ttf` ao lado do HTML:
```bash
for w in Regular SemiBold Bold ExtraBold; do curl -sL -o Poppins-$w.ttf "https://github.com/google/fonts/raw/main/ofl/poppins/Poppins-$w.ttf"; done
curl -sL -o SpaceMono-Regular.ttf "https://github.com/google/fonts/raw/main/ofl/spacemono/SpaceMono-Regular.ttf"
cp Poppins-*.ttf SpaceMono-*.ttf ~/Library/Fonts/   # ajuda o Chrome a achar
```

### 2. Preencher o template
Copie `assets/tabela-template.html` para o diretório de trabalho, preencha `<tbody>`. Uma `<tr>` por
curso; classes `r1..r3` definem o acento (verde/azul/âmbar). Use `<em>` para itálico, `li.bonus` para o
bônus, `.enc` (E1/E2) nos encontros do programa.

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
