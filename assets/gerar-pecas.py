# -*- coding: utf-8 -*-
import subprocess, os, shutil
from pypdf import PdfWriter, PdfReader
from PIL import Image

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
D = os.path.dirname(os.path.abspath(__file__)); os.chdir(D)
OUT = os.path.join(D, "out"); shutil.rmtree(OUT, ignore_errors=True); os.makedirs(OUT)
ROLE = "Conselheiro e mentor de líderes"

def sh(a):
    for attempt in range(2):
        try: subprocess.run(a, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True, timeout=90); return
        except subprocess.TimeoutExpired:
            subprocess.run(["pkill","-f","headless=new"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    subprocess.run(a, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True, timeout=120)
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
 .g{ color:var(--green); }
 .cursor{ width:52px; height:52px; }
"""
CURSOR = '<svg class=cursor viewBox="0 0 32 32" fill=none><path d="M9 3 L9 22 L14 18 L17 25 L20 24 L17 17 L23 17 Z" fill=#0B2E19 stroke=#0B2E19 stroke-width=1.5 stroke-linejoin=round/></svg>'
SW = '<svg viewBox="0 0 540 26" fill=none style="width:%dpx"><path d="M6 17 C 150 4, 410 4, 534 12" stroke=#1EFD8A stroke-width=7 stroke-linecap=round/></svg>'

# ---------- FEED GRID (ref3) — cards com bullets + cupom/CTA lado a lado ----------
FEED = """<!doctype html><html lang=pt-BR><head><meta charset=utf-8><style>"""+FONTS+"""
 body{ width:1080px; height:1350px; background:radial-gradient(130% 90% at 85% 8%, rgba(30,253,138,.13), transparent 55%), var(--bg); font-family:'Grotesk',sans-serif; color:#fff; overflow:hidden; }
 .wrap{ padding:54px 58px 52px; height:100%; display:flex; flex-direction:column; }
 .top{ display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:24px; }
 .logo{ font-weight:800; font-size:36px; letter-spacing:-.5px; padding-top:8px; } .logo .i{ color:var(--green); }
 .prof{ display:flex; align-items:center; gap:14px; background:var(--green); border-radius:20px; padding:11px 14px 11px 20px; }
 .prof .pinfo{ text-align:right; color:var(--ink); } .prof .by{ display:block; font-size:12px; font-weight:600; }
 .prof .pname{ display:block; font-size:21px; font-weight:800; letter-spacing:-.3px; } .prof .prole{ display:block; font-size:11px; font-weight:600; }
 .prof img{ width:82px; height:82px; border-radius:50%; object-fit:cover; border:3px solid var(--ink); }
 h1{ font-weight:800; font-size:52px; line-height:1.03; letter-spacing:-1px; text-transform:uppercase; }
 .hi{ position:relative; display:inline-block; }
 .hi .txt{ font-style:italic; text-transform:none; font-weight:800; font-size:@@GSIZE@@px; color:var(--green); letter-spacing:-1px; line-height:1.02; }
 .hi svg{ position:absolute; left:-2px; bottom:-14px; height:24px; }
 .grid{ margin-top:32px; display:grid; grid-template-columns:1fr 1fr; gap:16px; }
 .c{ background:var(--card); border:1px solid var(--line); border-radius:20px; padding:22px 26px; }
 .n{ font-family:'Mono'; font-weight:700; font-size:24px; color:var(--green); }
 .c h3{ font-weight:800; font-size:23px; margin:6px 0 12px; letter-spacing:-.3px; line-height:1.08; }
 .c ul{ list-style:none; } .c li{ position:relative; padding-left:16px; margin-bottom:8px; color:#C9CDD1; font-size:16px; line-height:1.32; }
 .c li:last-child{ margin-bottom:0; } .c li::before{ content:''; position:absolute; left:2px; top:8px; width:5px; height:5px; border-radius:50%; background:var(--green); }
 .foot{ margin-top:auto; padding-top:26px; display:flex; gap:16px; align-items:stretch; }
 .coupon{ display:flex; background:var(--card); border:1px solid var(--line); border-radius:18px; overflow:hidden; flex:1; }
 .coupon .l{ padding:18px 24px; flex:1; } .coupon .k{ font-family:'Mono'; font-size:14px; color:var(--gray); letter-spacing:.1em; }
 .coupon .code{ font-family:'Mono'; font-weight:700; font-size:30px; color:var(--green); letter-spacing:1px; margin:2px 0 3px; } .coupon .val{ font-family:'Mono'; font-size:13px; color:var(--gray); }
 .coupon .r{ border-left:2px dashed rgba(255,255,255,.14); padding:18px 24px; text-align:right; display:flex; flex-direction:column; justify-content:center; }
 .coupon .old{ color:var(--gray); text-decoration:line-through; font-size:17px; font-family:'Mono'; } .coupon .new{ font-weight:800; font-size:32px; letter-spacing:-1px; } .coupon .off{ color:var(--green); font-weight:700; font-size:17px; }
 .cta{ background:var(--green2); border-radius:18px; padding:20px 24px; width:392px; display:flex; align-items:center; justify-content:space-between; gap:12px; }
 .cta .t{ color:var(--ink); } .cta .t b{ display:block; font-size:17px; font-weight:700; } .cta .t .u{ font-size:20px; font-weight:800; font-style:italic; letter-spacing:-.4px; word-break:break-all; }
</style></head><body><div class=wrap>
 <div class=top><div class=logo>snaq<span class=i>I</span>A</div>
  <div class=prof><div class=pinfo><span class=by>ministrado por</span><span class=pname>Ricardo Catto</span><span class=prole>@@ROLE@@</span></div><img src=foto-ricardo.jpeg></div></div>
 <h1><span class=g>As 4 coisas</span> que você<br>vai aprender no curso<br><div class=hi><span class=txt>@@NAME@@</span>@@SWOOSH@@</div></h1>
 <div class=grid>
  <div class=c><div class=n>01</div><h3>@@P1T@@</h3><ul>@@B1@@</ul></div>
  <div class=c><div class=n>02</div><h3>@@P2T@@</h3><ul>@@B2@@</ul></div>
  <div class=c><div class=n>03</div><h3>@@P3T@@</h3><ul>@@B3@@</ul></div>
  <div class=c><div class=n>04</div><h3>@@P4T@@</h3><ul>@@B4@@</ul></div></div>
 <div class=foot>
  <div class=coupon><div class=l><div class=k>USE O CUPOM</div><div class=code>@@CODE@@</div><div class=val>válido até @@VALID@@</div></div>
   <div class=r><div class=old>@@OLD@@</div><div class=new>@@NEW@@</div><div class=off>@@OFF@@ OFF</div></div></div>
  <div class=cta><div class=t><b>Garanta sua vaga:</b><span class=u>@@URL@@</span></div>"""+CURSOR+"""</div></div>
</div></body></html>"""

# ---------- FEED HERO (ref1) — foto grande + titulo gigante + CTA alto ----------
HERO = """<!doctype html><html lang=pt-BR><head><meta charset=utf-8><style>"""+FONTS+"""
 body{ width:1080px; height:1350px; background:radial-gradient(120% 80% at 15% 85%, rgba(30,253,138,.16), transparent 55%), var(--bg); font-family:'Grotesk',sans-serif; color:#fff; overflow:hidden; }
 .wrap{ padding:56px 58px 52px; height:100%; display:flex; flex-direction:column; position:relative; }
 .top{ display:flex; justify-content:space-between; align-items:center; }
 .pill{ border:2px solid var(--green); color:var(--green); font-family:'Mono'; font-size:17px; padding:9px 18px; border-radius:40px; }
 .logo{ font-weight:800; font-size:34px; letter-spacing:-.5px; } .logo .i{ color:var(--green); }
 .kick{ font-family:'Mono'; font-size:22px; color:#fff; letter-spacing:.14em; text-transform:uppercase; margin-top:44px; }
 h1{ font-weight:800; font-size:@@HGSIZE@@px; line-height:.96; letter-spacing:-2px; margin-top:8px; max-width:640px; }
 .sub{ margin-top:26px; font-size:32px; font-weight:600; line-height:1.25; max-width:600px; color:#EDEFF0; }
 .photo{ position:absolute; right:44px; top:360px; width:470px; height:470px; border-radius:50%; object-fit:cover; border:5px solid var(--green); }
 .who{ margin-top:auto; margin-bottom:20px; } .who .c{ color:var(--gray); font-size:22px; } .who .nm{ font-weight:800; font-size:44px; letter-spacing:-.5px; line-height:1.05; } .who .rl{ color:#EDEFF0; font-size:24px; margin-top:4px; }
 .cta{ background:var(--green2); border-radius:22px; padding:34px 40px; display:flex; align-items:center; justify-content:space-between; }
 .cta b{ color:var(--ink); font-size:46px; font-weight:800; letter-spacing:-1px; text-transform:uppercase; line-height:1; }
</style></head><body><div class=wrap>
 <div class=top><div class=pill>@@URL@@</div><div class=logo>snaq<span class=i>I</span>A</div></div>
 <div class=kick>Curso snaq · ao vivo</div>
 <h1>@@NAME@@</h1>
 <p class=sub>@@HEROSUB@@</p>
 <img class=photo src=foto-ricardo.jpeg>
 <div class=who><div class=c>com</div><div class=nm>Ricardo Catto</div><div class=rl>@@ROLE@@</div></div>
 <div class=cta><b>Reserve sua<br>vaga agora!</b>"""+CURSOR+"""</div>
</div></body></html>"""

# ---------- STORY (ref2) — gancho gigante, sem grafismo ----------
STORY = """<!doctype html><html lang=pt-BR><head><meta charset=utf-8><style>"""+FONTS+"""
 body{ width:1080px; height:1920px; background:radial-gradient(120% 70% at 88% 6%, rgba(30,253,138,.12), transparent 55%), var(--bg); font-family:'Grotesk',sans-serif; color:#fff; overflow:hidden; }
 .wrap{ padding:96px 76px 84px; height:100%; display:flex; flex-direction:column; }
 .logo{ font-weight:800; font-size:58px; letter-spacing:-.6px; text-align:center; } .logo .i{ color:var(--green); }
 .kick{ font-family:'Mono'; font-size:20px; color:var(--green); letter-spacing:.12em; text-transform:uppercase; margin-top:50px; }
 .hook{ font-weight:800; font-size:118px; line-height:.96; letter-spacing:-3px; margin-top:24px; }
 .cn{ color:var(--green); font-weight:800; font-size:46px; letter-spacing:-.6px; margin-top:40px; }
 .cs{ color:var(--gray); font-size:26px; margin-top:8px; }
 .prof{ display:flex; align-items:center; gap:24px; margin-top:48px; }
 .prof img{ width:128px; height:128px; border-radius:50%; object-fit:cover; border:3px solid var(--green); }
 .prof .by{ color:var(--gray); font-size:20px; } .prof .nm{ font-size:36px; font-weight:800; letter-spacing:-.3px; } .prof .rl{ color:var(--gray); font-size:22px; margin-top:2px; }
 .foot{ margin-top:auto; }
 .cta{ background:var(--green2); border-radius:24px; padding:38px 44px; display:flex; align-items:center; justify-content:space-between; }
 .cta .t{ color:var(--ink); } .cta .t b{ display:block; font-size:24px; font-weight:700; } .cta .t .u{ font-size:34px; font-weight:800; font-style:italic; letter-spacing:-.5px; margin-top:2px; }
 .cpn{ font-family:'Mono'; color:var(--gray); font-size:24px; margin-top:24px; text-align:center; } .cpn b{ color:var(--green); } .cpn .p{ color:#fff; font-weight:700; }
</style></head><body><div class=wrap>
 <div class=logo>snaq<span class=i>I</span>A</div>
 <div class=kick>Curso snaq · Programa ao vivo</div>
 <div class=hook>@@HOOK@@</div>
 <div class=cn>@@NAME@@</div><div class=cs>@@SUB@@</div>
 <div class=prof><img src=foto-ricardo.jpeg><div><span class=by>com</span><div class=nm>Ricardo Catto</div><div class=rl>@@ROLE@@</div></div></div>
 <div class=foot>
   <div class=cta><div class=t><b>Garanta sua vaga:</b><span class=u>@@URL@@</span></div>"""+CURSOR+"""</div>
   <div class=cpn>cupom <b>@@CODE@@</b> · <span class=p>@@NEW@@</span> (@@OFF@@ OFF) · até @@VALID@@</div>
 </div>
</div></body></html>"""

# ---------- ONE-PAGER A4 (documento nosso) ----------
ONEP = """<!doctype html><html lang=pt-BR><head><meta charset=utf-8><style>"""+FONTS+"""
 @page{ size:210mm 297mm; margin:0; }
 body{ width:210mm; height:297mm; background:var(--bg); font-family:'Grotesk',sans-serif; color:#fff; overflow:hidden; }
 .wrap{ padding:15mm 15mm 13mm; height:100%; display:flex; flex-direction:column; }
 .top{ display:flex; justify-content:space-between; align-items:center; } .logo{ font-weight:800; font-size:22px; } .logo .i{ color:var(--green); } .kick{ font-family:'Mono'; font-size:11px; color:var(--gray); letter-spacing:.14em; text-transform:uppercase; }
 h1{ font-weight:800; font-size:35px; line-height:1.02; letter-spacing:-1px; margin-top:12px; } .subt{ color:var(--green); font-size:18px; font-weight:600; margin-top:6px; }
 .prof{ display:flex; align-items:center; gap:10px; margin-top:9px; } .prof img{ width:38px; height:38px; border-radius:50%; object-fit:cover; border:2px solid var(--green); } .prof span{ font-size:12.5px; color:#D7DBDF; } .prof b{ color:#fff; }
 .promise{ color:#D7DBDF; font-size:13.5px; line-height:1.45; margin-top:9px; max-width:170mm; }
 .datastrip{ margin-top:11px; background:var(--card); border:1px solid var(--line); border-left:3px solid var(--green); border-radius:12px; padding:11px 16px; display:flex; gap:18px; }
 .datastrip .d b{ color:var(--green); font-family:'Mono'; font-weight:700; font-size:18px; display:block; } .datastrip .d span{ color:var(--gray); font-size:10.5px; line-height:1.3; display:block; margin-top:2px; }
 .h2{ font-weight:700; font-size:12.5px; text-transform:uppercase; letter-spacing:.14em; color:var(--gray); margin:14px 0 8px; }
 .learn{ display:grid; grid-template-columns:1fr 1fr; gap:9px; } .learn .it{ background:var(--card); border:1px solid var(--line); border-radius:14px; padding:12px 15px; } .learn .n{ font-family:'Mono'; font-weight:700; color:var(--green); font-size:14px; } .learn .t{ font-weight:700; font-size:14.5px; margin:3px 0 4px; } .learn .p{ color:var(--gray); font-size:11.5px; line-height:1.38; }
 .formats{ display:grid; grid-template-columns:1fr 1fr 1fr; gap:9px; } .fmt{ background:var(--card); border:1px solid var(--line); border-radius:14px; padding:12px; } .fmt .l{ font-family:'Mono'; font-size:9.5px; color:var(--gray); text-transform:uppercase; letter-spacing:.1em; } .fmt .n{ font-weight:700; font-size:13.5px; margin:4px 0 7px; } .fmt .pr{ color:var(--green); font-weight:700; font-size:18px; letter-spacing:-.5px; } .fmt .d{ color:var(--gray); font-size:10.5px; line-height:1.38; margin-top:5px; }
 .who{ margin-top:12px; background:var(--card); border:1px solid var(--line); border-radius:14px; padding:12px 15px; } .who b{ font-size:12.5px; } .who p{ color:var(--gray); font-size:12px; line-height:1.45; margin-top:4px; }
 .cta{ margin-top:auto; background:var(--green2); border-radius:16px; padding:15px 24px; display:flex; align-items:center; justify-content:space-between; } .cta .t{ color:var(--ink); } .cta .t b{ display:block; font-size:14.5px; font-weight:700; } .cta .t .u{ font-size:22px; font-weight:800; font-style:italic; letter-spacing:-.5px; } .cta .cursor{ width:36px; height:36px; }
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
 <div class=cta><div class=t><b>Garanta sua vaga:</b><span class=u>@@URL@@</span></div>"""+CURSOR+"""</div>
</div></body></html>"""

def ul(items): return "".join("<li>%s</li>"%x for x in items)

COURSES = [
 dict(slug="soberania-cognitiva", short="Soberania", NAME="Soberania Cognitiva", SUB="Liderança e Decisão na Era da IA",
   GSIZE=56, HGSIZE=104, SWOOSH=SW%540, HOOK="Não deixe a IA<br>decidir <span class=g>por<br>você.</span>", ROLE=ROLE,
   HEROSUB="Decida na era da IA sem <span class=g>terceirizar o seu julgamento.</span>",
   PROMISE="Para líderes e founders que usam IA todo dia e não querem terceirizar o próprio julgamento.",
   P1T="Mapa da dependência", B1=ul(["Onde a IA já decide por você","Diagnóstico dos seus pontos cegos"]),
   P2T="Recuperar a autoria", B2=ul(["Decidir antes da pergunta fechar","Repertório próprio vs. roteiro herdado"]),
   P3T="IA × julgamento no time", B3=ul(["Sustentar a polaridade sem terceirizar","Critério humano como vantagem"]),
   P4T="Arquitetura de decisão", B4=ul(["Seu protocolo de decisão soberana","Pronto para aplicar amanhã"]),
   P1D="Onde você já delega atenção e decisão para a IA.", P2D="Discernimento como prática: decidir antes da pergunta fechar.",
   P3D="Sustentar a polaridade sem abrir mão do critério humano.", P4D="Seu protocolo de decisão soberana, pronto para usar.",
   CODE="SOBERANIA40", VALID="31/07", OLD="R$ 4.980", NEW="R$ 2.988", OFF="40%", URL="www.snaq.co/soberania-cognitiva",
   D1N="53,6%", D1T="dos profissionais dependem de IA mais do que gostariam (GoTo, 2026)",
   D2N="95%", D2T="das empresas no Brasil já usam IA (EY, 2026)", D3N="MIT", D3T="cunhou “dívida cognitiva”: o custo de delegar o pensar",
   FW="R$ 497–997", FG="R$ 297", FP="R$ 4.000–8.000",
   QUEM="C-level, fundadores e conselheiros que usam IA intensamente e querem preservar julgamento e autoria."),
 dict(slug="formacao-conselheiros-mentores", short="Conselheiros", NAME="Formação de Conselheiros-Mentores", SUB="Formação de conselheiros e mentores de travessia",
   GSIZE=40, HGSIZE=78, SWOOSH="", HOOK="O conselheiro<br>que o líder<br><span class=g>procura.</span>", ROLE=ROLE,
   HEROSUB="Torne-se o conselheiro que os líderes procuram <span class=g>na hora difícil.</span>",
   PROMISE="Para quem quer atuar como conselheiro consultivo e mentor de líderes — com método, não improviso.",
   P1T="O novo mandato", B1=ul(["O conselheiro que não vende resposta","Sustentar a leitura, não dar a direção"]),
   P2T="As 4 portas", B2=ul(["Interior e exterior, indivíduo e coletivo","Por onde a virada pede entrada"]),
   P3T="Orquestração de lentes", B3=ul(["Integral, Teoria U, Polaridades","Eneagrama iEQ9 — sem método único"]),
   P4T="Conduzir a jornada", B4=ul(["A jornada de 8–10 sessões","Do diagnóstico ao encerramento"]),
   P1D="O conselheiro que não vende resposta: sustentar a leitura.", P2D="A bússola de intervenção: interior e exterior, individual e coletivo.",
   P3D="Integral, Teoria U, Polaridades e Eneagrama iEQ9 — sem método único.", P4D="A jornada de 8–10 sessões, do diagnóstico ao encerramento.",
   CODE="CONSELHEIRO30", VALID="31/07", OLD="R$ 12.000", NEW="R$ 8.400", OFF="30%", URL="www.snaq.co/conselheiros-mentores",
   D1N="R$ 17k+", D1T="ticket de formação de conselheiro no Brasil (ref. IBGC)",
   D2N="8–10", D2T="sessões: método documentado (Kegan, Wilber, Teoria U)", D3N="25 anos", D3T="entre execução estratégica e desenvolvimento humano",
   FW="R$ 497", FG="R$ 297", FP="R$ 8.000–30.000",
   QUEM="Executivos sêniores, ex-C-level e coaches que querem atuar como conselheiros consultivos e mentores de líderes."),
 dict(slug="sucessao-sem-ruptura", short="Sucessão", NAME="Sucessão sem Ruptura", SUB="Governança para Empresas Familiares",
   GSIZE=52, HGSIZE=92, SWOOSH=SW%560, HOOK="A sucessão não<br>precisa <span class=g>quebrar<br>a família.</span>", ROLE=ROLE,
   HEROSUB="Prepare a sucessão sem <span class=g>quebrar a família nem a empresa.</span>",
   PROMISE="Para donos e herdeiros que querem preparar a sucessão sem quebrar a família nem a empresa.",
   P1T="Os 3 patrimônios", B1=ul(["Família, sociedade e gestão","Separar antes que se confundam"]),
   P2T="A governança na prática", B2=ul(["Conselho de família e acordo de sócios","Matérias reservadas e vetos"]),
   P3T="A conversa difícil", B3=ul(["Negociar sucessão sem litígio","Entrada e saída de sócios"]),
   P4T="Plano de transição", B4=ul(["Do herdeiro ao executivo","O plano que se apresenta à família"]),
   P1D="Separar família, sociedade e gestão antes que se confundam.", P2D="Conselho de família, acordo de sócios e matérias reservadas.",
   P3D="Negociar sucessão e entrada/saída de sócios sem litígio.", P4D="Do herdeiro ao executivo: o plano que se apresenta à família.",
   CODE="SUCESSAO30", VALID="31/07", OLD="R$ 5.000", NEW="R$ 3.500", OFF="30%", URL="www.snaq.co/sucessao-sem-ruptura",
   D1N="90%", D1T="das empresas no Brasil são familiares (IBGE)",
   D2N="54%", D2T="não têm plano de sucessão estruturado", D3N="36%", D3T="só sobrevivem à 2ª geração — a transição é o risco",
   FW="R$ 297–497", FG="R$ 97–297", FP="R$ 3.500–6.000",
   QUEM="Donos e herdeiros de empresa familiar de médio/grande porte e family offices que vão passar por sucessão."),
]

thumbs=[]
for i,c in enumerate(COURSES,1):
    cdir=os.path.join(OUT,"%02d_%s"%(i,c["slug"])); os.makedirs(cdir,exist_ok=True)
    for name,tpl,png,w,h,sf in [
        ("feed",FEED,cdir+"/asset-1-feed.png",1080,1350,2),
        ("story",STORY,cdir+"/asset-2-story.png",1080,1920,1.5),
        ("hero",HERO,cdir+"/asset-4-hero.png",1080,1350,2)]:
        hf="%s_%s.html"%(name,c["slug"]); open(hf,"w").write(fill(tpl,c)); shot(hf,png,w,h,sf)
    oh="onep_%s.html"%c["slug"]; open(oh,"w").write(fill(ONEP,c)); pdf(oh,cdir+"/asset-3-onepager.pdf"); shot(oh,"onep_%s.png"%c["slug"],794,1123,2)
    thumbs.append((c["short"],[
        ("Asset 1 · Feed", cdir+"/asset-1-feed.png"),
        ("Asset 4 · Feed-Hero", cdir+"/asset-4-hero.png"),
        ("Asset 2 · Story", cdir+"/asset-2-story.png"),
        ("Asset 3 · One-pager", "onep_%s.png"%c["slug"]),
    ]))

# ---------- MATRIZ (fundo branco) ----------
H=470; GAP=30; MX=60; CAP=44; HEAD=64
def wof(png): im=Image.open(png); return int(H*im.size[0]/im.size[1])
ncol=len(thumbs[0][1])
colw=[max(wof(t[1][k][1]) for t in thumbs) for k in range(ncol)]
PW=MX*2+sum(colw)+GAP*(ncol-1); PH=2*MX+HEAD+3*(CAP+H)+GAP*2+16
cells=""
for short,row in thumbs:
    cells+="<div class=row>"
    for k,(lbl,png) in enumerate(row):
        cells+='<div class=cell style="width:%dpx"><div class=cap><b>%s</b> · %s</div><img style="height:%dpx" src="%s"></div>'%(colw[k],short,lbl,H,png)
    cells+="</div>"
MATRIX="""<!doctype html><html><head><meta charset=utf-8><style>"""+FONTS+"""
 @page{ size:@@PW@@px @@PH@@px; margin:0; } body{ width:@@PW@@px; height:@@PH@@px; background:#FFF; font-family:'Grotesk',sans-serif; color:#14243B; }
 .wrap{ padding:@@MX@@px; } .hd{ font-weight:800; font-size:26px; margin-bottom:26px; } .hd .i{ color:#1DB863; } .hd .s{ color:#71808C; font-weight:500; font-size:20px; margin-left:8px; }
 .row{ display:flex; gap:@@GAP@@px; margin-bottom:@@GAP@@px; align-items:flex-start; } .row:last-child{ margin-bottom:0; }
 .cell{ display:flex; flex-direction:column; } .cap{ font-family:'Mono'; font-size:15px; color:#71808C; margin-bottom:11px; } .cap b{ color:#14243B; }
 .cell img{ width:100%; border:1px solid #E4E8EC; display:block; }
</style></head><body><div class=wrap>
 <div class=hd>snaq<span class=i>I</span>A <span class=s>· Ricardo Catto — peças de divulgação (feed · hero · story · one-pager, por curso)</span></div>
 @@CELLS@@
</div></body></html>"""
open("matrix.html","w").write(fill(MATRIX,dict(PW=PW,PH=PH,MX=MX,GAP=GAP,CELLS=cells)))
pdf("matrix.html","matrix.pdf")
print("matriz:", len(PdfReader("matrix.pdf").pages),"pag")

# ZIP
zr="Assets_ricardo-catto"; shutil.rmtree(zr,ignore_errors=True); shutil.copytree(OUT,zr)
sh(["zip","-rq","Assets_ricardo-catto.zip",zr]); print("zip ok")
