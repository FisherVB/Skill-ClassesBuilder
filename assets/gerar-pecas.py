# -*- coding: utf-8 -*-
import subprocess, os, shutil
from pypdf import PdfWriter

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
D = os.path.dirname(os.path.abspath(__file__)); os.chdir(D)
OUT = os.path.join(D, "out"); shutil.rmtree(OUT, ignore_errors=True); os.makedirs(OUT)
ROLE = "Conselheiro e mentor de líderes"

def sh(args): subprocess.run(args, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
def shot(html, png, w, h, sf=2):
    sh([CHROME,"--headless=new","--disable-gpu","--hide-scrollbars",
        "--force-device-scale-factor=%s"%sf,"--window-size=%d,%d"%(w,h),
        "--allow-file-access-from-files","--screenshot="+png,"file://"+os.path.join(D,html)])
def pdf(html, out):
    sh([CHROME,"--headless=new","--disable-gpu","--no-pdf-header-footer",
        "--allow-file-access-from-files","--print-to-pdf="+out,"file://"+os.path.join(D,html)])

FONTS = """
  @font-face{ font-family:'Grotesk'; src:local('Space Grotesk'),url('SpaceGrotesk.ttf') format('truetype'); font-weight:300 700; }
  @font-face{ font-family:'Mono'; src:local('Space Mono'),url('SpaceMono-Regular.ttf') format('truetype'); font-weight:400; }
  @font-face{ font-family:'Mono'; src:local('Space Mono'),url('SpaceMono-Bold.ttf') format('truetype'); font-weight:700; }
  :root{ --bg:#0E0F11; --card:#17181B; --line:rgba(255,255,255,.07); --green:#37E27C; --green2:#4BEA8A; --gray:#9AA1A8; --ink:#0B2C18; }
  *{ box-sizing:border-box; margin:0; padding:0; }
"""

def fill(t, c):
    for k,v in c.items(): t = t.replace("@@%s@@"%k, str(v))
    return t

# ---------------- FEED 1080x1350 ----------------
FEED = """<!doctype html><html lang=pt-BR><head><meta charset=utf-8><style>"""+FONTS+"""
 body{ width:1080px; height:1350px; background:var(--bg); font-family:'Grotesk',sans-serif; color:#fff; overflow:hidden; }
 .wrap{ padding:56px 60px 52px; height:100%; display:flex; flex-direction:column; }
 .top{ display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:28px; }
 .logo{ font-weight:700; font-size:34px; letter-spacing:-.5px; padding-top:8px; } .logo .i{ color:var(--green); }
 .prof{ display:flex; align-items:center; gap:16px; background:var(--green); border-radius:20px; padding:12px 14px 12px 22px; }
 .prof .pinfo{ text-align:right; color:var(--ink); }
 .prof .by{ display:block; font-size:13px; font-weight:500; letter-spacing:.04em; }
 .prof .pname{ display:block; font-size:23px; font-weight:700; letter-spacing:-.4px; line-height:1.05; }
 .prof .prole{ display:block; font-size:12px; font-weight:500; margin-top:2px; }
 .prof img{ width:92px; height:92px; border-radius:50%; object-fit:cover; border:3px solid var(--ink); }
 h1{ font-weight:700; font-size:54px; line-height:1.03; letter-spacing:-1px; text-transform:uppercase; }
 .hi{ position:relative; display:inline-block; margin-top:8px; }
 .hi .txt{ font-style:italic; text-transform:none; font-weight:700; font-size:@@GSIZE@@px; color:var(--green); letter-spacing:-1px; line-height:1.02; }
 .sub{ margin-top:26px; color:var(--gray); font-size:20px; font-weight:400; line-height:1.4; max-width:840px; }
 .grid{ margin-top:32px; display:grid; grid-template-columns:1fr 1fr; gap:18px; }
 .c{ background:var(--card); border:1px solid var(--line); border-radius:22px; padding:24px 26px; }
 .n{ font-family:'Mono'; font-weight:700; font-size:24px; color:var(--green); letter-spacing:1px; }
 .c h3{ font-weight:700; font-size:24px; margin:6px 0 9px; letter-spacing:-.3px; }
 .c p{ color:var(--gray); font-size:17px; line-height:1.38; }
 .foot{ margin-top:auto; padding-top:28px; }
 .coupon{ display:flex; background:var(--card); border:1px solid var(--line); border-radius:18px; overflow:hidden; }
 .coupon .l{ padding:20px 26px; flex:1; } .coupon .k{ font-family:'Mono'; font-size:15px; color:var(--gray); letter-spacing:.12em; }
 .coupon .code{ font-family:'Mono'; font-weight:700; font-size:32px; color:var(--green); letter-spacing:2px; margin:2px 0 4px; }
 .coupon .val{ font-family:'Mono'; font-size:14px; color:var(--gray); }
 .coupon .r{ border-left:2px dashed rgba(255,255,255,.14); padding:20px 30px; text-align:right; display:flex; flex-direction:column; justify-content:center; }
 .coupon .old{ color:var(--gray); text-decoration:line-through; font-size:20px; font-family:'Mono'; }
 .coupon .new{ font-weight:700; font-size:38px; letter-spacing:-1px; } .coupon .off{ color:var(--green); font-weight:700; font-size:19px; }
 .cta{ margin-top:20px; background:var(--green2); border-radius:18px; padding:24px 34px; display:flex; align-items:center; justify-content:space-between; }
 .cta .t{ color:var(--ink); } .cta .t b{ display:block; font-size:19px; font-weight:600; } .cta .t .u{ font-size:27px; font-weight:700; letter-spacing:-.5px; font-style:italic; }
 .cta svg{ width:50px; height:50px; }
</style></head><body><div class=wrap>
 <div class=top><div class=logo>snaq<span class=i>I</span>A</div>
  <div class=prof><div class=pinfo><span class=by>ministrado por</span><span class=pname>Ricardo Catto</span><span class=prole>@@ROLE@@</span></div><img src=foto-ricardo.jpeg></div></div>
 <h1>As 4 coisas que você<br>vai aprender no curso<br><div class=hi><span class=txt>@@NAME@@</span></div></h1>
 <p class=sub>@@PROMISE@@</p>
 <div class=grid>
  <div class=c><div class=n>01</div><h3>@@P1T@@</h3><p>@@P1D@@</p></div>
  <div class=c><div class=n>02</div><h3>@@P2T@@</h3><p>@@P2D@@</p></div>
  <div class=c><div class=n>03</div><h3>@@P3T@@</h3><p>@@P3D@@</p></div>
  <div class=c><div class=n>04</div><h3>@@P4T@@</h3><p>@@P4D@@</p></div></div>
 <div class=foot><div class=coupon><div class=l><div class=k>USE O CUPOM</div><div class=code>@@CODE@@</div><div class=val>válido até @@VALID@@</div></div>
   <div class=r><div class=old>@@OLD@@</div><div class=new>@@NEW@@</div><div class=off>@@OFF@@ OFF</div></div></div>
  <div class=cta><div class=t><b>Garanta sua vaga:</b><span class=u>@@URL@@</span></div>
   <svg viewBox="0 0 32 32" fill=none><path d="M9 3 L9 22 L14 18 L17 25 L20 24 L17 17 L23 17 Z" fill=#0B2C18 stroke=#0B2C18 stroke-width=1.5 stroke-linejoin=round/></svg></div></div>
</div></body></html>"""

# ---------------- STORY 1080x1920 ----------------
STORY = """<!doctype html><html lang=pt-BR><head><meta charset=utf-8><style>"""+FONTS+"""
 body{ width:1080px; height:1920px; background:var(--bg); font-family:'Grotesk',sans-serif; color:#fff; overflow:hidden; }
 .wrap{ padding:76px 66px 70px; height:100%; display:flex; flex-direction:column; }
 .logo{ font-weight:700; font-size:38px; letter-spacing:-.5px; } .logo .i{ color:var(--green); }
 .kick{ font-family:'Mono'; font-size:18px; color:var(--green); letter-spacing:.12em; text-transform:uppercase; margin-top:36px; }
 h1{ font-weight:700; font-size:@@H1SIZE@@px; line-height:.98; letter-spacing:-1.5px; margin-top:14px; }
 .subt{ color:var(--green); font-size:30px; font-weight:600; margin-top:14px; letter-spacing:-.3px; }
 .promise{ color:#D7DBDF; font-size:25px; line-height:1.45; margin-top:20px; }
 .prof{ display:flex; align-items:center; gap:22px; margin-top:30px; background:var(--card); border:1px solid var(--line); border-radius:22px; padding:18px 24px; }
 .prof img{ width:108px; height:108px; border-radius:50%; object-fit:cover; border:3px solid var(--green); }
 .prof .by{ color:var(--gray); font-size:18px; } .prof .nm{ font-size:29px; font-weight:700; letter-spacing:-.3px; margin-top:1px; } .prof .rl{ color:var(--gray); font-size:19px; margin-top:2px; }
 .lbl{ font-family:'Mono'; font-size:19px; color:var(--gray); text-transform:uppercase; letter-spacing:.1em; margin:36px 0 18px; }
 .list{ display:flex; flex-direction:column; gap:16px; }
 .it{ display:flex; gap:20px; align-items:flex-start; }
 .it .n{ font-family:'Mono'; font-weight:700; font-size:29px; color:var(--green); min-width:44px; }
 .it .tx b{ display:block; font-size:28px; font-weight:700; letter-spacing:-.2px; } .it .tx span{ display:block; color:var(--gray); font-size:21px; line-height:1.34; margin-top:3px; }
 .foot{ margin-top:auto; }
 .coupon{ display:flex; background:var(--card); border:1px solid var(--line); border-radius:20px; overflow:hidden; margin-top:30px; }
 .coupon .l{ padding:24px 30px; flex:1; } .coupon .k2{ font-family:'Mono'; font-size:18px; color:var(--gray); letter-spacing:.12em; }
 .coupon .code{ font-family:'Mono'; font-weight:700; font-size:40px; color:var(--green); letter-spacing:2px; margin:3px 0 5px; } .coupon .val{ font-family:'Mono'; font-size:17px; color:var(--gray); }
 .coupon .r{ border-left:2px dashed rgba(255,255,255,.14); padding:24px 34px; text-align:right; display:flex; flex-direction:column; justify-content:center; }
 .coupon .old{ color:var(--gray); text-decoration:line-through; font-size:24px; font-family:'Mono'; } .coupon .new{ font-weight:700; font-size:48px; letter-spacing:-1px; } .coupon .off{ color:var(--green); font-weight:700; font-size:23px; }
 .cta{ margin-top:22px; background:var(--green2); border-radius:22px; padding:32px 40px; display:flex; align-items:center; justify-content:space-between; }
 .cta .t{ color:var(--ink); } .cta .t b{ display:block; font-size:23px; font-weight:600; } .cta .t .u{ font-size:31px; font-weight:700; font-style:italic; letter-spacing:-.5px; margin-top:2px; } .cta svg{ width:58px; height:58px; }
</style></head><body><div class=wrap>
 <div class=logo>snaq<span class=i>I</span>A</div>
 <div class=kick>Curso snaq · Programa ao vivo · 4×2h</div>
 <h1>@@NAMEBR@@</h1><div class=subt>@@SUB@@</div>
 <p class=promise>@@PROMISE@@</p>
 <div class=prof><img src=foto-ricardo.jpeg><div><span class=by>com</span><div class=nm>Ricardo Catto</div><div class=rl>@@ROLE@@</div></div></div>
 <div class=lbl>O que você vai aprender</div>
 <div class=list>
  <div class=it><div class=n>01</div><div class=tx><b>@@P1T@@</b><span>@@P1D@@</span></div></div>
  <div class=it><div class=n>02</div><div class=tx><b>@@P2T@@</b><span>@@P2D@@</span></div></div>
  <div class=it><div class=n>03</div><div class=tx><b>@@P3T@@</b><span>@@P3D@@</span></div></div>
  <div class=it><div class=n>04</div><div class=tx><b>@@P4T@@</b><span>@@P4D@@</span></div></div></div>
 <div class=foot><div class=coupon><div class=l><div class=k2>USE O CUPOM</div><div class=code>@@CODE@@</div><div class=val>válido até @@VALID@@</div></div>
   <div class=r><div class=old>@@OLD@@</div><div class=new>@@NEW@@</div><div class=off>@@OFF@@ OFF</div></div></div>
  <div class=cta><div class=t><b>Garanta sua vaga:</b><span class=u>@@URL@@</span></div>
   <svg viewBox="0 0 32 32" fill=none><path d="M9 3 L9 22 L14 18 L17 25 L20 24 L17 17 L23 17 Z" fill=#0B2C18 stroke=#0B2C18 stroke-width=1.5 stroke-linejoin=round/></svg></div></div>
</div></body></html>"""

# ---------------- ONE-PAGER A4 ----------------
ONEP = """<!doctype html><html lang=pt-BR><head><meta charset=utf-8><style>"""+FONTS+"""
 @page{ size:210mm 297mm; margin:0; }
 body{ width:210mm; height:297mm; background:var(--bg); font-family:'Grotesk',sans-serif; color:#fff; overflow:hidden; }
 .wrap{ padding:15mm 15mm 13mm; height:100%; display:flex; flex-direction:column; }
 .top{ display:flex; justify-content:space-between; align-items:center; }
 .logo{ font-weight:700; font-size:22px; letter-spacing:-.4px; } .logo .i{ color:var(--green); }
 .kick{ font-family:'Mono'; font-size:11px; color:var(--gray); letter-spacing:.14em; text-transform:uppercase; }
 h1{ font-weight:700; font-size:42px; line-height:1.0; letter-spacing:-1px; margin-top:18px; }
 .subt{ color:var(--green); font-size:19px; font-weight:600; margin-top:8px; }
 .prof{ display:flex; align-items:center; gap:10px; margin-top:12px; }
 .prof img{ width:40px; height:40px; border-radius:50%; object-fit:cover; border:2px solid var(--green); }
 .prof span{ font-size:13px; color:#D7DBDF; } .prof b{ color:#fff; }
 .promise{ color:#D7DBDF; font-size:14.5px; line-height:1.5; margin-top:12px; max-width:170mm; }
 .datastrip{ margin-top:15px; background:var(--card); border:1px solid var(--line); border-left:3px solid var(--green); border-radius:12px; padding:14px 18px; display:flex; gap:20px; }
 .datastrip .d b{ color:var(--green); font-family:'Mono'; font-weight:700; font-size:19px; display:block; } .datastrip .d span{ color:var(--gray); font-size:11px; line-height:1.3; display:block; margin-top:2px; }
 .h2{ font-weight:700; font-size:13px; text-transform:uppercase; letter-spacing:.14em; color:var(--gray); margin:20px 0 11px; }
 .learn{ display:grid; grid-template-columns:1fr 1fr; gap:11px; }
 .learn .it{ background:var(--card); border:1px solid var(--line); border-radius:14px; padding:15px 17px; }
 .learn .n{ font-family:'Mono'; font-weight:700; color:var(--green); font-size:15px; } .learn .t{ font-weight:700; font-size:15.5px; margin:4px 0 5px; } .learn .p{ color:var(--gray); font-size:12px; line-height:1.4; }
 .formats{ display:grid; grid-template-columns:1fr 1fr 1fr; gap:11px; }
 .fmt{ background:var(--card); border:1px solid var(--line); border-radius:14px; padding:15px; }
 .fmt .l{ font-family:'Mono'; font-size:10px; color:var(--gray); text-transform:uppercase; letter-spacing:.1em; } .fmt .n{ font-weight:700; font-size:14px; margin:4px 0 8px; } .fmt .pr{ color:var(--green); font-weight:700; font-size:19px; letter-spacing:-.5px; } .fmt .d{ color:var(--gray); font-size:11px; line-height:1.4; margin-top:6px; }
 .who{ margin-top:18px; background:var(--card); border:1px solid var(--line); border-radius:14px; padding:15px 17px; } .who b{ font-size:13px; } .who p{ color:var(--gray); font-size:12.5px; line-height:1.5; margin-top:4px; }
 .cta{ margin-top:auto; background:var(--green2); border-radius:16px; padding:19px 26px; display:flex; align-items:center; justify-content:space-between; }
 .cta .t{ color:var(--ink); } .cta .t b{ display:block; font-size:15px; font-weight:600; } .cta .t .u{ font-size:23px; font-weight:700; font-style:italic; letter-spacing:-.5px; } .cta svg{ width:38px; height:38px; }
</style></head><body><div class=wrap>
 <div class=top><div class=logo>snaq<span class=i>I</span>A</div><div class=kick>Curso snaq · Programa ao vivo</div></div>
 <h1>@@NAME@@</h1><div class=subt>@@SUB@@</div>
 <div class=prof><img src=foto-ricardo.jpeg><span>com <b>Ricardo Catto</b> · @@ROLE@@</span></div>
 <p class=promise>@@PROMISE@@</p>
 <div class=datastrip>
  <div class=d><b>@@D1N@@</b><span>@@D1T@@</span></div>
  <div class=d><b>@@D2N@@</b><span>@@D2T@@</span></div>
  <div class=d><b>@@D3N@@</b><span>@@D3T@@</span></div></div>
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

COURSES = [
 dict(slug="soberania-cognitiva", NAME="Soberania Cognitiva", NAMEBR="Soberania<br>Cognitiva",
   SUB="Liderança e Decisão na Era da IA", GSIZE=56, H1SIZE=88, ROLE=ROLE,
   PROMISE="Para líderes e founders que usam IA todo dia e não querem terceirizar o próprio julgamento.",
   P1T="Mapa da dependência", P1D="Onde você já delega atenção e decisão para a IA — sem perceber.",
   P2T="Recuperar a autoria", P2D="Discernimento como prática: decidir antes da pergunta fechar.",
   P3T="IA × julgamento no time", P3D="Sustentar a polaridade sem abrir mão do critério humano.",
   P4T="Arquitetura de decisão", P4D="Seu protocolo de decisão soberana, pronto para usar.",
   CODE="SOBERANIA40", VALID="31/07", OLD="R$ 4.980", NEW="R$ 2.988", OFF="40%",
   URL="www.snaq.co/soberania-cognitiva",
   D1N="53,6%", D1T="dos profissionais dependem de IA mais do que gostariam (GoTo, 2026)",
   D2N="95%", D2T="das empresas no Brasil já usam IA (EY, 2026)",
   D3N="MIT", D3T="cunhou “dívida cognitiva”: o custo de delegar o pensar",
   FW="R$ 497–997", FG="R$ 297", FP="R$ 4.000–8.000",
   QUEM="C-level, fundadores e conselheiros que usam IA intensamente e querem preservar julgamento e autoria. Não é para quem busca atalho — é para quem quer decidir melhor."),
 dict(slug="formacao-conselheiros-mentores", NAME="Formação de Conselheiros-Mentores", NAMEBR="Conselheiros<br>-Mentores",
   SUB="Formação de conselheiros e mentores de travessia", GSIZE=40, H1SIZE=76, ROLE=ROLE,
   PROMISE="Para quem quer atuar como conselheiro consultivo e mentor de líderes — com método, não improviso.",
   P1T="O novo mandato", P1D="O conselheiro que não vende resposta: sustentar a leitura, não dar a direção.",
   P2T="As 4 portas", P2D="A bússola de intervenção: interior e exterior, individual e coletivo.",
   P3T="Orquestração de lentes", P3D="Integral, Teoria U, Polaridades e Eneagrama iEQ9 — sem método único.",
   P4T="Conduzir a jornada", P4D="A jornada de 8–10 sessões na prática, do diagnóstico ao encerramento.",
   CODE="CONSELHEIRO30", VALID="31/07", OLD="R$ 12.000", NEW="R$ 8.400", OFF="30%",
   URL="www.snaq.co/conselheiros-mentores",
   D1N="R$ 17k+", D1T="ticket de formação de conselheiro no Brasil (ref. IBGC)",
   D2N="8–10", D2T="sessões: método documentado (Kegan, Wilber, Teoria U)",
   D3N="25 anos", D3T="entre execução estratégica e desenvolvimento humano",
   FW="R$ 497", FG="R$ 297", FP="R$ 8.000–30.000",
   QUEM="Executivos sêniores, ex-C-level e coaches que querem atuar como conselheiros consultivos e mentores de líderes."),
 dict(slug="sucessao-sem-ruptura", NAME="Sucessão sem Ruptura", NAMEBR="Sucessão<br>sem Ruptura",
   SUB="Governança para Empresas Familiares", GSIZE=52, H1SIZE=82, ROLE=ROLE,
   PROMISE="Para donos e herdeiros que querem preparar a sucessão sem quebrar a família nem a empresa.",
   P1T="Os 3 patrimônios", P1D="Separar família, sociedade e gestão antes que se confundam.",
   P2T="A governança na prática", P2D="Conselho de família, acordo de sócios e matérias reservadas.",
   P3T="A conversa difícil", P3D="Negociar sucessão e entrada/saída de sócios sem litígio.",
   P4T="Plano de transição", P4D="Do herdeiro ao executivo: o plano que se apresenta à família.",
   CODE="SUCESSAO30", VALID="31/07", OLD="R$ 5.000", NEW="R$ 3.500", OFF="30%",
   URL="www.snaq.co/sucessao-sem-ruptura",
   D1N="90%", D1T="das empresas no Brasil são familiares (IBGE)",
   D2N="54%", D2T="não têm plano de sucessão estruturado",
   D3N="36%", D3T="só sobrevivem à 2ª geração — a transição é o risco",
   FW="R$ 297–497", FG="R$ 97–297", FP="R$ 3.500–6.000",
   QUEM="Donos e herdeiros de empresa familiar de médio/grande porte e family offices que vão passar por sucessão."),
]

# label page wrapper (embeds a PNG + label header)
LABEL = """<!doctype html><html><head><meta charset=utf-8><style>"""+FONTS+"""
 @page{ size:@@PW@@px @@PH@@px; margin:0; }
 body{ width:@@PW@@px; height:@@PH@@px; background:#0E0F11; font-family:'Grotesk',sans-serif; }
 .hd{ padding:22px 34px; display:flex; align-items:baseline; gap:14px; border-bottom:1px solid rgba(255,255,255,.08); }
 .hd .a{ font-family:'Mono'; font-weight:700; color:#37E27C; font-size:22px; letter-spacing:1px; }
 .hd .t{ color:#fff; font-weight:700; font-size:22px; letter-spacing:-.3px; } .hd .f{ color:#9AA1A8; font-size:16px; }
 .img{ display:block; width:@@IW@@px; margin:26px auto; border-radius:14px; border:1px solid rgba(255,255,255,.08); }
</style></head><body>
 <div class=hd><span class=a>ASSET @@AN@@</span><span class=t>@@ATYPE@@</span><span class=f>— @@CNAME@@</span></div>
 <img class=img src="@@IMG@@"></body></html>"""

def label_page(n, atype, cname, png, iw, ih, out):
    PW = iw + 120; header = 88; PH = ih + header + 52
    html = fill(LABEL, dict(PW=PW, PH=PH, IW=iw, AN=n, ATYPE=atype, CNAME=cname, IMG=png))
    hf = "lbl_%s.html"%out; open(hf,"w").write(html); pdf(hf, out+".pdf")

writer = PdfWriter(); writer.append("Cursos_RicardoCatto_Teste2_final.pdf")  # page 1 = tabela
os.makedirs(OUT, exist_ok=True)
for i,c in enumerate(COURSES,1):
    cdir = os.path.join(OUT, "%02d_%s"%(i,c["slug"])); os.makedirs(cdir, exist_ok=True)
    # FEED
    fh="feed_%s.html"%c["slug"]; open(fh,"w").write(fill(FEED,c)); shot(fh, cdir+"/asset-1-feed.png", 1080,1350,2)
    # STORY
    sh_="story_%s.html"%c["slug"]; open(sh_,"w").write(fill(STORY,c)); shot(sh_, cdir+"/asset-2-story.png", 1080,1920,1.5)
    # ONE-PAGER (pdf p/ zip + png p/ review)
    oh="onep_%s.html"%c["slug"]; open(oh,"w").write(fill(ONEP,c)); pdf(oh, cdir+"/asset-3-onepager.pdf"); shot(oh, "onep_%s.png"%c["slug"], 794,1123,2)
    # label pages -> merge
    label_page(1,"FEED (1080×1350)", c["NAME"], cdir+"/asset-1-feed.png", 1080,1350, "p_%d_1"%i)
    label_page(2,"STORY (1080×1920)", c["NAME"], cdir+"/asset-2-story.png", 900,1600, "p_%d_2"%i)
    label_page(3,"ONE-PAGER (A4)", c["NAME"], "onep_%s.png"%c["slug"], 794,1123, "p_%d_3"%i)
    for k in (1,2,3): writer.append("p_%d_%d.pdf"%(i,k))

final = "Cursos_RicardoCatto_completo.pdf"; writer.write(final)
print("PDF paginas:", len(PdfWriter(clone_from=final).pages) if False else "ok")
from pypdf import PdfReader; print("paginas:", len(PdfReader(final).pages))
# ZIP
zroot="Assets_ricardo-catto"; shutil.rmtree(zroot, ignore_errors=True); shutil.copytree(OUT, zroot)
sh(["zip","-rq","Assets_ricardo-catto.zip", zroot])
print("zip pronto:", os.path.exists("Assets_ricardo-catto.zip"))
