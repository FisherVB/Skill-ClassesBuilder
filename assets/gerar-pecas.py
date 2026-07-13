# -*- coding: utf-8 -*-
import subprocess, os, shutil
from pypdf import PdfWriter, PdfReader
from PIL import Image

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
D = os.path.dirname(os.path.abspath(__file__)); os.chdir(D)
OUT = os.path.join(D, "out"); shutil.rmtree(OUT, ignore_errors=True); os.makedirs(OUT)
ROLE = "Conselheiro e mentor de líderes"

def sh(a): subprocess.run(a, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
def shot(html,png,w,h,sf=2): sh([CHROME,"--headless=new","--disable-gpu","--hide-scrollbars","--force-device-scale-factor=%s"%sf,"--window-size=%d,%d"%(w,h),"--allow-file-access-from-files","--screenshot="+png,"file://"+os.path.join(D,html)])
def pdf(html,out): sh([CHROME,"--headless=new","--disable-gpu","--no-pdf-header-footer","--allow-file-access-from-files","--print-to-pdf="+out,"file://"+os.path.join(D,html)])
def fill(t,c):
    for k,v in c.items(): t=t.replace("@@%s@@"%k,str(v))
    return t

FONTS = """
 @font-face{ font-family:'Grotesk'; src:local('Montserrat'),url('Montserrat.ttf') format('truetype'); font-weight:100 900; }
 @font-face{ font-family:'Mono'; src:local('Space Mono'),url('SpaceMono-Regular.ttf') format('truetype'); font-weight:400; }
 @font-face{ font-family:'Mono'; src:local('Space Mono'),url('SpaceMono-Bold.ttf') format('truetype'); font-weight:700; }
 :root{ --bg:#16171A; --card:#1F201F; --line:rgba(255,255,255,.08); --green:#1EFD8A; --green2:#1EFD8A; --gray:#9DA0A0; --ink:#0B2E19; }
 *{ box-sizing:border-box; margin:0; padding:0; }
"""

# ---------- FEED 1080x1350 — densidade MÉDIA (as 4 coisas) ----------
FEED = """<!doctype html><html lang=pt-BR><head><meta charset=utf-8><style>"""+FONTS+"""
 body{ width:1080px; height:1350px; background:radial-gradient(130% 90% at 85% 8%, rgba(30,253,138,.13), transparent 55%), var(--bg); font-family:'Grotesk',sans-serif; color:#fff; overflow:hidden; }
 .wrap{ padding:58px 62px 56px; height:100%; display:flex; flex-direction:column; }
 .top{ display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:30px; }
 .logo{ font-weight:700; font-size:36px; letter-spacing:-.5px; padding-top:8px; } .logo .i{ color:var(--green); }
 .prof{ display:flex; align-items:center; gap:16px; background:var(--green); border-radius:20px; padding:12px 14px 12px 22px; }
 .prof .pinfo{ text-align:right; color:var(--ink); } .prof .by{ display:block; font-size:13px; font-weight:500; }
 .prof .pname{ display:block; font-size:23px; font-weight:700; letter-spacing:-.4px; } .prof .prole{ display:block; font-size:12px; font-weight:500; margin-top:2px; }
 .prof img{ width:92px; height:92px; border-radius:50%; object-fit:cover; border:3px solid var(--ink); }
 h1{ font-weight:700; font-size:60px; line-height:1.02; letter-spacing:-1px; text-transform:uppercase; }
 .hi{ position:relative; display:inline-block; }
 .hi .txt{ font-style:italic; text-transform:none; font-weight:700; font-size:@@GSIZE@@px; color:var(--green); letter-spacing:-1px; line-height:1.02; }
 .hi svg{ position:absolute; left:-2px; bottom:-16px; height:26px; }
 .sub{ margin-top:30px; color:var(--gray); font-size:23px; line-height:1.4; max-width:860px; }
 .grid{ margin-top:38px; display:grid; grid-template-columns:1fr 1fr; gap:20px; }
 .c{ background:var(--card); border:1px solid var(--line); border-radius:22px; padding:28px 30px; }
 .n{ font-family:'Mono'; font-weight:700; font-size:28px; color:var(--green); letter-spacing:1px; }
 .c h3{ font-weight:700; font-size:30px; margin:8px 0 0; letter-spacing:-.4px; line-height:1.08; }
 .foot{ margin-top:auto; padding-top:30px; }
 .coupon{ display:flex; background:var(--card); border:1px solid var(--line); border-radius:18px; overflow:hidden; }
 .coupon .l{ padding:20px 26px; flex:1; } .coupon .k{ font-family:'Mono'; font-size:15px; color:var(--gray); letter-spacing:.12em; }
 .coupon .code{ font-family:'Mono'; font-weight:700; font-size:34px; color:var(--green); letter-spacing:2px; margin:2px 0 4px; } .coupon .val{ font-family:'Mono'; font-size:14px; color:var(--gray); }
 .coupon .r{ border-left:2px dashed rgba(255,255,255,.14); padding:20px 30px; text-align:right; display:flex; flex-direction:column; justify-content:center; }
 .coupon .old{ color:var(--gray); text-decoration:line-through; font-size:20px; font-family:'Mono'; } .coupon .new{ font-weight:700; font-size:40px; letter-spacing:-1px; } .coupon .off{ color:var(--green); font-weight:700; font-size:20px; }
 .cta{ margin-top:20px; background:var(--green2); border-radius:18px; padding:26px 34px; display:flex; align-items:center; justify-content:space-between; }
 .cta .t{ color:var(--ink); } .cta .t b{ display:block; font-size:20px; font-weight:600; } .cta .t .u{ font-size:29px; font-weight:700; font-style:italic; letter-spacing:-.5px; } .cta svg{ width:52px; height:52px; }
</style></head><body><div class=wrap>
 <div class=top><div class=logo>snaq<span class=i>I</span>A</div>
  <div class=prof><div class=pinfo><span class=by>ministrado por</span><span class=pname>Ricardo Catto</span><span class=prole>@@ROLE@@</span></div><img src=foto-ricardo.jpeg></div></div>
 <h1>As 4 coisas que você<br>vai aprender no curso<br><div class=hi><span class=txt>@@NAME@@</span>@@SWOOSH@@</div></h1>
 <p class=sub>@@PROMISE@@</p>
 <div class=grid>
  <div class=c><div class=n>01</div><h3>@@P1T@@</h3></div>
  <div class=c><div class=n>02</div><h3>@@P2T@@</h3></div>
  <div class=c><div class=n>03</div><h3>@@P3T@@</h3></div>
  <div class=c><div class=n>04</div><h3>@@P4T@@</h3></div></div>
 <div class=foot><div class=coupon><div class=l><div class=k>USE O CUPOM</div><div class=code>@@CODE@@</div><div class=val>válido até @@VALID@@</div></div>
   <div class=r><div class=old>@@OLD@@</div><div class=new>@@NEW@@</div><div class=off>@@OFF@@ OFF</div></div></div>
  <div class=cta><div class=t><b>Garanta sua vaga:</b><span class=u>@@URL@@</span></div>
   <svg viewBox="0 0 32 32" fill=none><path d="M9 3 L9 22 L14 18 L17 25 L20 24 L17 17 L23 17 Z" fill=#0B2C18 stroke=#0B2C18 stroke-width=1.5 stroke-linejoin=round/></svg></div></div>
</div></body></html>"""

# ---------- STORY 1080x1920 — densidade LIMPA (um gancho grande) ----------
STORY = """<!doctype html><html lang=pt-BR><head><meta charset=utf-8><style>"""+FONTS+"""
 body{ width:1080px; height:1920px; background:radial-gradient(120% 70% at 88% 6%, rgba(30,253,138,.12), transparent 55%), var(--bg); font-family:'Grotesk',sans-serif; color:#fff; overflow:hidden; }
 .wrap{ padding:96px 76px 84px; height:100%; display:flex; flex-direction:column; }
 .logo{ font-weight:700; font-size:42px; letter-spacing:-.5px; } .logo .i{ color:var(--green); }
 .kick{ font-family:'Mono'; font-size:20px; color:var(--green); letter-spacing:.12em; text-transform:uppercase; margin-top:52px; }
 .hook{ font-weight:700; font-size:106px; line-height:.98; letter-spacing:-2px; margin-top:26px; }
 .cn{ color:var(--green); font-weight:700; font-size:44px; letter-spacing:-.6px; margin-top:40px; }
 .cs{ color:var(--gray); font-size:26px; margin-top:8px; }
 .prof{ display:flex; align-items:center; gap:24px; margin-top:52px; }
 .prof img{ width:132px; height:132px; border-radius:50%; object-fit:cover; border:3px solid var(--green); }
 .prof .by{ color:var(--gray); font-size:20px; } .prof .nm{ font-size:36px; font-weight:700; letter-spacing:-.3px; } .prof .rl{ color:var(--gray); font-size:22px; margin-top:2px; }
 .foot{ margin-top:auto; }
 .cta{ background:var(--green2); border-radius:24px; padding:40px 46px; display:flex; align-items:center; justify-content:space-between; }
 .cta .t{ color:var(--ink); } .cta .t b{ display:block; font-size:26px; font-weight:600; } .cta .t .u{ font-size:36px; font-weight:700; font-style:italic; letter-spacing:-.5px; margin-top:3px; } .cta svg{ width:64px; height:64px; }
 .cpn{ font-family:'Mono'; color:var(--gray); font-size:24px; margin-top:26px; text-align:center; }
 .cpn b{ color:var(--green); } .cpn .p{ color:#fff; font-weight:700; }
</style></head><body><div class=wrap>
 <div class=logo>snaq<span class=i>I</span>A</div>
 <div class=kick>Curso snaq · Programa ao vivo</div>
 <div class=hook>@@HOOK@@</div>
 <div class=cn>@@NAME@@</div><div class=cs>@@SUB@@</div>
 <div class=prof><img src=foto-ricardo.jpeg><div><span class=by>com</span><div class=nm>Ricardo Catto</div><div class=rl>@@ROLE@@</div></div></div>
 <div class=foot>
   <div class=cta><div class=t><b>Garanta sua vaga:</b><span class=u>@@URL@@</span></div>
     <svg viewBox="0 0 32 32" fill=none><path d="M9 3 L9 22 L14 18 L17 25 L20 24 L17 17 L23 17 Z" fill=#0B2C18 stroke=#0B2C18 stroke-width=1.5 stroke-linejoin=round/></svg></div>
   <div class=cpn>cupom <b>@@CODE@@</b> · <span class=p>@@NEW@@</span> (@@OFF@@ OFF) · até @@VALID@@</div>
 </div>
</div></body></html>"""

# ---------- ONE-PAGER A4 — densidade CARREGADA (doc) ----------
ONEP = """<!doctype html><html lang=pt-BR><head><meta charset=utf-8><style>"""+FONTS+"""
 @page{ size:210mm 297mm; margin:0; }
 body{ width:210mm; height:297mm; background:var(--bg); font-family:'Grotesk',sans-serif; color:#fff; overflow:hidden; }
 .wrap{ padding:15mm 15mm 13mm; height:100%; display:flex; flex-direction:column; }
 .top{ display:flex; justify-content:space-between; align-items:center; }
 .logo{ font-weight:700; font-size:22px; letter-spacing:-.4px; } .logo .i{ color:var(--green); } .kick{ font-family:'Mono'; font-size:11px; color:var(--gray); letter-spacing:.14em; text-transform:uppercase; }
 h1{ font-weight:800; font-size:35px; line-height:1.02; letter-spacing:-1px; margin-top:12px; } .subt{ color:var(--green); font-size:18px; font-weight:600; margin-top:6px; }
 .prof{ display:flex; align-items:center; gap:10px; margin-top:9px; } .prof img{ width:38px; height:38px; border-radius:50%; object-fit:cover; border:2px solid var(--green); } .prof span{ font-size:12.5px; color:#D7DBDF; } .prof b{ color:#fff; }
 .promise{ color:#D7DBDF; font-size:13.5px; line-height:1.45; margin-top:9px; max-width:170mm; }
 .datastrip{ margin-top:11px; background:var(--card); border:1px solid var(--line); border-left:3px solid var(--green); border-radius:12px; padding:11px 16px; display:flex; gap:18px; }
 .datastrip .d b{ color:var(--green); font-family:'Mono'; font-weight:700; font-size:18px; display:block; } .datastrip .d span{ color:var(--gray); font-size:10.5px; line-height:1.3; display:block; margin-top:2px; }
 .h2{ font-weight:700; font-size:12.5px; text-transform:uppercase; letter-spacing:.14em; color:var(--gray); margin:14px 0 8px; }
 .learn{ display:grid; grid-template-columns:1fr 1fr; gap:9px; }
 .learn .it{ background:var(--card); border:1px solid var(--line); border-radius:14px; padding:12px 15px; } .learn .n{ font-family:'Mono'; font-weight:700; color:var(--green); font-size:14px; } .learn .t{ font-weight:700; font-size:14.5px; margin:3px 0 4px; } .learn .p{ color:var(--gray); font-size:11.5px; line-height:1.38; }
 .formats{ display:grid; grid-template-columns:1fr 1fr 1fr; gap:9px; }
 .fmt{ background:var(--card); border:1px solid var(--line); border-radius:14px; padding:12px; } .fmt .l{ font-family:'Mono'; font-size:9.5px; color:var(--gray); text-transform:uppercase; letter-spacing:.1em; } .fmt .n{ font-weight:700; font-size:13.5px; margin:4px 0 7px; } .fmt .pr{ color:var(--green); font-weight:700; font-size:18px; letter-spacing:-.5px; } .fmt .d{ color:var(--gray); font-size:10.5px; line-height:1.38; margin-top:5px; }
 .who{ margin-top:12px; background:var(--card); border:1px solid var(--line); border-radius:14px; padding:12px 15px; } .who b{ font-size:12.5px; } .who p{ color:var(--gray); font-size:12px; line-height:1.45; margin-top:4px; }
 .cta{ margin-top:auto; background:var(--green2); border-radius:16px; padding:15px 24px; display:flex; align-items:center; justify-content:space-between; } .cta .t{ color:var(--ink); } .cta .t b{ display:block; font-size:14.5px; font-weight:600; } .cta .t .u{ font-size:22px; font-weight:700; font-style:italic; letter-spacing:-.5px; } .cta svg{ width:36px; height:36px; }
</style></head><body><div class=wrap>
 <div class=top><div class=logo>snaq<span class=i>I</span>A</div><div class=kick>Curso snaq · Programa ao vivo</div></div>
 <h1>@@NAME@@</h1><div class=subt>@@SUB@@</div>
 <div class=prof><img src=foto-ricardo.jpeg><span>com <b>Ricardo Catto</b> · @@ROLE@@</span></div>
 <p class=promise>@@PROMISE@@</p>
 <div class=datastrip><div class=d><b>@@D1N@@</b><span>@@D1T@@</span></div><div class=d><b>@@D2N@@</b><span>@@D2T@@</span></div><div class=d><b>@@D3N@@</b><span>@@D3T@@</span></div></div>
 <div class=h2>O que você vai aprender</div>
 <div class=learn>
  <div class=it><div class=n>01</div><div class=t>@@P1T@@</div><div class=p>@@P1D@@</div></div>
  <div class=it><div class=n>02</div><div class=t>@@P2T@@</div><div class=p>@@P2D@@</div></div>
  <div class=it><div class=n>03</div><div class=t>@@P3T@@</div><div class=p>@@P3D@@</div></div>
  <div class=it><div class=n>04</div><div class=t>@@P4T@@</div><div class=p>@@P4D@@</div></div></div>
 <div class=h2>Formatos e investimento</div>
 <div class=formats>
  <div class=fmt><div class=l>Workshop ao vivo · 2h</div><div class=n>Vitória rápida</div><div class=pr>@@FW@@</div><div class=d>Uma sessão. Diagnóstico e primeiro passo.</div></div>
  <div class=fmt><div class=l>Curso gravado · 2h</div><div class=n>No seu ritmo</div><div class=pr>@@FG@@</div><div class=d>On-demand, com material baixável.</div></div>
  <div class=fmt><div class=l>Programa ao vivo · 4×2h</div><div class=n>Transformação</div><div class=pr>@@FP@@</div><div class=d>Cohort. In-company sob consulta.</div></div></div>
 <div class=who><b>Para quem é:</b><p>@@QUEM@@</p></div>
 <div class=cta><div class=t><b>Garanta sua vaga:</b><span class=u>@@URL@@</span></div>
  <svg viewBox="0 0 32 32" fill=none><path d="M9 3 L9 22 L14 18 L17 25 L20 24 L17 17 L23 17 Z" fill=#0B2C18 stroke=#0B2C18 stroke-width=1.5 stroke-linejoin=round/></svg></div>
</div></body></html>"""

SW = '<svg viewBox="0 0 540 26" fill=none style="width:%dpx"><path d="M6 17 C 150 4, 410 4, 534 12" stroke=#37E27C stroke-width=7 stroke-linecap=round/></svg>'

COURSES = [
 dict(slug="soberania-cognitiva", short="Soberania", NAME="Soberania Cognitiva", SUB="Liderança e Decisão na Era da IA",
   GSIZE=58, SWOOSH=SW%540, HOOK="Não deixe a IA<br>decidir por<br>você.", ROLE=ROLE,
   PROMISE="Para líderes e founders que usam IA todo dia e não querem terceirizar o próprio julgamento.",
   P1T="Mapa da dependência", P1D="Onde você já delega atenção e decisão para a IA — sem perceber.",
   P2T="Recuperar a autoria", P2D="Discernimento como prática: decidir antes da pergunta fechar.",
   P3T="IA × julgamento no time", P3D="Sustentar a polaridade sem abrir mão do critério humano.",
   P4T="Arquitetura de decisão", P4D="Seu protocolo de decisão soberana, pronto para usar.",
   CODE="SOBERANIA40", VALID="31/07", OLD="R$ 4.980", NEW="R$ 2.988", OFF="40%", URL="www.snaq.co/soberania-cognitiva",
   D1N="53,6%", D1T="dos profissionais dependem de IA mais do que gostariam (GoTo, 2026)",
   D2N="95%", D2T="das empresas no Brasil já usam IA (EY, 2026)", D3N="MIT", D3T="cunhou “dívida cognitiva”: o custo de delegar o pensar",
   FW="R$ 497–997", FG="R$ 297", FP="R$ 4.000–8.000",
   QUEM="C-level, fundadores e conselheiros que usam IA intensamente e querem preservar julgamento e autoria."),
 dict(slug="formacao-conselheiros-mentores", short="Conselheiros", NAME="Formação de Conselheiros-Mentores", SUB="Formação de conselheiros e mentores de travessia",
   GSIZE=40, SWOOSH="", HOOK="O conselheiro<br>que o líder<br>procura.", ROLE=ROLE,
   PROMISE="Para quem quer atuar como conselheiro consultivo e mentor de líderes — com método, não improviso.",
   P1T="O novo mandato", P1D="O conselheiro que não vende resposta: sustentar a leitura, não dar a direção.",
   P2T="As 4 portas", P2D="A bússola de intervenção: interior e exterior, individual e coletivo.",
   P3T="Orquestração de lentes", P3D="Integral, Teoria U, Polaridades e Eneagrama iEQ9 — sem método único.",
   P4T="Conduzir a jornada", P4D="A jornada de 8–10 sessões na prática, do diagnóstico ao encerramento.",
   CODE="CONSELHEIRO30", VALID="31/07", OLD="R$ 12.000", NEW="R$ 8.400", OFF="30%", URL="www.snaq.co/conselheiros-mentores",
   D1N="R$ 17k+", D1T="ticket de formação de conselheiro no Brasil (ref. IBGC)",
   D2N="8–10", D2T="sessões: método documentado (Kegan, Wilber, Teoria U)", D3N="25 anos", D3T="entre execução estratégica e desenvolvimento humano",
   FW="R$ 497", FG="R$ 297", FP="R$ 8.000–30.000",
   QUEM="Executivos sêniores, ex-C-level e coaches que querem atuar como conselheiros consultivos e mentores de líderes."),
 dict(slug="sucessao-sem-ruptura", short="Sucessão", NAME="Sucessão sem Ruptura", SUB="Governança para Empresas Familiares",
   GSIZE=52, SWOOSH=SW%560, HOOK="A sucessão não<br>precisa quebrar<br>a família.", ROLE=ROLE,
   PROMISE="Para donos e herdeiros que querem preparar a sucessão sem quebrar a família nem a empresa.",
   P1T="Os 3 patrimônios", P1D="Separar família, sociedade e gestão antes que se confundam.",
   P2T="A governança na prática", P2D="Conselho de família, acordo de sócios e matérias reservadas.",
   P3T="A conversa difícil", P3D="Negociar sucessão e entrada/saída de sócios sem litígio.",
   P4T="Plano de transição", P4D="Do herdeiro ao executivo: o plano que se apresenta à família.",
   CODE="SUCESSAO30", VALID="31/07", OLD="R$ 5.000", NEW="R$ 3.500", OFF="30%", URL="www.snaq.co/sucessao-sem-ruptura",
   D1N="90%", D1T="das empresas no Brasil são familiares (IBGE)",
   D2N="54%", D2T="não têm plano de sucessão estruturado", D3N="36%", D3T="só sobrevivem à 2ª geração — a transição é o risco",
   FW="R$ 297–497", FG="R$ 97–297", FP="R$ 3.500–6.000",
   QUEM="Donos e herdeiros de empresa familiar de médio/grande porte e family offices que vão passar por sucessão."),
]

# render individual assets (para o ZIP) + guarda os PNGs p/ a matriz
thumbs=[]  # (course_short, [ (label,png), (label,png), (label,png) ])
for i,c in enumerate(COURSES,1):
    cdir=os.path.join(OUT,"%02d_%s"%(i,c["slug"])); os.makedirs(cdir,exist_ok=True)
    fh="feed_%s.html"%c["slug"]; open(fh,"w").write(fill(FEED,c)); shot(fh,cdir+"/asset-1-feed.png",1080,1350,2)
    sh_="story_%s.html"%c["slug"]; open(sh_,"w").write(fill(STORY,c)); shot(sh_,cdir+"/asset-2-story.png",1080,1920,1.5)
    oh="onep_%s.html"%c["slug"]; open(oh,"w").write(fill(ONEP,c)); pdf(oh,cdir+"/asset-3-onepager.pdf"); shot(oh,"onep_%s.png"%c["slug"],794,1123,2)
    thumbs.append((c["short"], [
        ("Asset 1 · Feed", cdir+"/asset-1-feed.png"),
        ("Asset 2 · Story", cdir+"/asset-2-story.png"),
        ("Asset 3 · One-pager", "onep_%s.png"%c["slug"]),
    ]))

# ---------- MATRIZ 3x3 (uma pagina) ----------
H=520; GAP=34; MX=64; CAP=44; HEAD=64
def wof(png): im=Image.open(png); return int(H*im.size[0]/im.size[1])
colw=[max(wof(t[1][k][1]) for t in thumbs) for k in range(3)]  # largura por coluna (formato)
PW=MX*2+sum(colw)+GAP*2
PH=2*MX+HEAD+3*(CAP+H)+GAP*2+16
cells=""
for short,row in thumbs:
    rowhtml="<div class=row>"
    for k,(lbl,png) in enumerate(row):
        rowhtml+='<div class=cell style="width:%dpx"><div class=cap><b>%s</b> · %s</div><img style="height:%dpx" src="%s"></div>'%(colw[k],short,lbl,H,png)
    cells+=rowhtml+"</div>"
MATRIX="""<!doctype html><html><head><meta charset=utf-8><style>"""+FONTS+"""
 @page{ size:@@PW@@px @@PH@@px; margin:0; }
 body{ width:@@PW@@px; height:@@PH@@px; background:#FFFFFF; font-family:'Grotesk',sans-serif; color:#14243B; }
 .wrap{ padding:@@MX@@px; }
 .hd{ font-weight:700; font-size:26px; letter-spacing:-.4px; margin-bottom:26px; } .hd .i{ color:#1DB863; } .hd .s{ color:#71808C; font-weight:500; font-size:20px; margin-left:8px; }
 .row{ display:flex; gap:@@GAP@@px; margin-bottom:@@GAP@@px; align-items:flex-start; } .row:last-child{ margin-bottom:0; }
 .cell{ display:flex; flex-direction:column; }
 .cap{ font-family:'Mono'; font-size:16px; color:#71808C; margin-bottom:12px; letter-spacing:.02em; } .cap b{ color:#14243B; }
 .cell img{ width:100%; border:1px solid #E4E8EC; display:block; }
</style></head><body><div class=wrap>
 <div class=hd>snaq<span class=i>I</span>A <span class=s>· Ricardo Catto — peças de divulgação (feed · story · one-pager, por curso)</span></div>
 @@CELLS@@
</div></body></html>"""
open("matrix.html","w").write(fill(MATRIX,dict(PW=PW,PH=PH,MX=MX,GAP=GAP,CELLS=cells)))
pdf("matrix.html","matrix.pdf")

# ---------- PDF final: pagina 1 = tabela, pagina 2 = matriz ----------
w=PdfWriter(); w.append("Cursos_RicardoCatto_Teste2_final.pdf"); w.append("matrix.pdf")
w.write("Cursos_RicardoCatto_completo.pdf")
print("paginas:", len(PdfReader("Cursos_RicardoCatto_completo.pdf").pages))
# ZIP
zr="Assets_ricardo-catto"; shutil.rmtree(zr,ignore_errors=True); shutil.copytree(OUT,zr)
sh(["zip","-rq","Assets_ricardo-catto.zip",zr]); print("zip:", os.path.exists("Assets_ricardo-catto.zip"))
