import json, sys, os
from PIL import Image, ImageDraw, ImageFont
W,H=1080,1350
FB="/usr/share/fonts/opentype/noto/NotoSansCJK-Black.ttc"; FR="/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc"
if not os.path.exists(FR): FR="/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc"
f=lambda p,s: ImageFont.truetype(p,s,index=1)
NAVY=(18,38,74); GOLD=(244,185,66); IVORY=(250,247,240); RED=(226,74,60); GRAY=(110,118,135); GREEN=(46,160,110)
BRAND="나랏돈사용설명서"
def wrap_center(d,y,txt,font,fill,gap=16):
    for line in txt.split("\n"):
        w=d.textlength(line,font=font); d.text(((W-w)/2,y),line,font=font,fill=fill); y+=font.size+gap
    return y
def left(d,x,y,txt,font,fill,gap=14):
    for line in txt.split("\n"): d.text((x,y),line,font=font,fill=fill); y+=font.size+gap
    return y
def footer(d,i,n,dark):
    c=(200,205,215) if dark else GRAY
    d.text((70,H-95),BRAND,font=f(FB,34),fill=GOLD if dark else NAVY)
    t=f"{i}/{n}"; ft=f(FB,34); d.text((W-70-d.textlength(t,font=ft),H-95),t,font=ft,fill=c)
def cover(s,i,n):
    im=Image.new("RGB",(W,H),NAVY); d=ImageDraw.Draw(im)
    d.rectangle([0,0,W,18],fill=GOLD)
    tag=s["tag"]; tf=f(FB,44); tw=d.textlength(tag,font=tf)
    d.rounded_rectangle([(W-tw)/2-36,200,(W+tw)/2+36,290],45,fill=GOLD); d.text(((W-tw)/2,212),tag,font=tf,fill=NAVY)
    y=wrap_center(d,370,s["title"],f(FB,104),"white",22)
    d.line([(W/2-80,y+40),(W/2+80,y+40)],fill=GOLD,width=8)
    wrap_center(d,y+90,s["sub"],f(FR,56),(220,226,238),16)
    d.text(((W-d.textlength("밀어서 확인 →",font=f(FB,40)))/2,H-230),"밀어서 확인 →",font=f(FB,40),fill=GOLD)
    footer(d,i,n,True); return im
def warn(s,i,n):
    im=Image.new("RGB",(W,H),IVORY); d=ImageDraw.Draw(im)
    d.rectangle([0,0,W,18],fill=NAVY)
    d.text((70,50),s["num"],font=f(FB,130),fill=GOLD)
    d.rounded_rectangle([70,300,W-70,560],36,fill="white",outline=RED,width=6)
    pf=f(FB,38); pw=d.textlength("이런 말 조심",font=pf)
    d.rounded_rectangle([110,272,110+pw+60,334],31,fill=RED); d.text((140,276),"이런 말 조심",font=pf,fill="white")
    qn=s["quote"].count("\n")+1; wrap_center(d,430-(qn*90-16)//2-12,s["quote"],f(FB,74),RED,16)
    d.text((70,620),"사실은",font=f(FB,46),fill=NAVY)
    d.line([(70,690),(W-70,690)],fill=(225,220,205),width=4)
    y=left(d,70,725,s["fact"],f(FR,54),NAVY,18)
    if s.get("note"):
        d.rounded_rectangle([70,H-300,W-70,H-150],28,fill=(236,232,220))
        left(d,105,H-275,s["note"],f(FR,38),GRAY,12)
    footer(d,i,n,False); return im
def todo(s,i,n):
    im=Image.new("RGB",(W,H),IVORY); d=ImageDraw.Draw(im); d.rectangle([0,0,W,18],fill=NAVY)
    wrap_center(d,110,s["title"],f(FB,82),NAVY,16)
    y=330
    for k,(h,b) in enumerate(s["items"]):
        d.rounded_rectangle([70,y,W-70,y+230],30,fill="white",outline=(225,220,205),width=4)
        d.ellipse([105,y+40,185,y+120],fill=GREEN); d.text((131,y+46),str(k+1),font=f(FB,52),fill="white")
        d.text((215,y+40),h,font=f(FB,54),fill=NAVY)
        left(d,215,y+115,b,f(FR,40),GRAY,10); y+=265
    footer(d,i,n,False); return im
def cta(s,i,n):
    im=Image.new("RGB",(W,H),NAVY); d=ImageDraw.Draw(im); d.rectangle([0,0,W,18],fill=GOLD)
    y=wrap_center(d,260,s["title"],f(FB,90),"white",20)
    y=wrap_center(d,y+50,s["sub"],f(FR,52),(220,226,238),14)
    bt=s["button"]; bf=f(FB,52); bw=d.textlength(bt,font=bf)
    d.rounded_rectangle([(W-bw)/2-60,y+80,(W+bw)/2+60,y+200],60,fill=GOLD); d.text(((W-bw)/2,y+108),bt,font=bf,fill=NAVY)
    wrap_center(d,y+290,s["foot"],f(FR,40),(170,180,200),12)
    footer(d,i,n,True); return im
def info(s,i,n):
    im=Image.new("RGB",(W,H),IVORY); d=ImageDraw.Draw(im); d.rectangle([0,0,W,18],fill=NAVY)
    d.text((70,50),s["num"],font=f(FB,130),fill=GOLD)
    y=left(d,70,240,s["title"],f(FB,76),NAVY,14)
    d.line([(70,y+20),(W-70,y+20)],fill=(225,220,205),width=4)
    y=left(d,70,y+60,s["body"],f(FR,52),NAVY,20)
    if s.get("note"):
        d.rounded_rectangle([70,H-300,W-70,H-150],28,fill=(236,232,220))
        left(d,105,H-275,s["note"],f(FR,38),GRAY,12)
    footer(d,i,n,False); return im
def todo4(s,i,n):
    im=Image.new("RGB",(W,H),IVORY); d=ImageDraw.Draw(im); d.rectangle([0,0,W,18],fill=NAVY)
    y=wrap_center(d,90,s["title"],f(FB,76),NAVY,14)
    items=s["items"]; k=len(items); top=max(y+40,300); avail=H-150-top; hh=avail//k-20
    for j,(h,b) in enumerate(items):
        yy=top+j*(hh+20)
        d.rounded_rectangle([70,yy,W-70,yy+hh],30,fill="white",outline=(225,220,205),width=4)
        d.ellipse([105,yy+30,175,yy+100],fill=GREEN); d.text((128,yy+33),str(j+1),font=f(FB,46),fill="white")
        d.text((205,yy+30),h,font=f(FB,50),fill=NAVY)
        left(d,205,yy+98,b,f(FR,38),GRAY,8)
    footer(d,i,n,False); return im
R=dict(cover=cover,warn=warn,todo=todo,cta=cta,info=info,list=todo4)
data=json.load(open(sys.argv[1])); out=sys.argv[2]; os.makedirs(out,exist_ok=True)
n=len(data)
for i,s in enumerate(data,1): R[s["type"]](s,i,n).convert("RGB").save(f"{out}/{i:02d}.jpg",quality=92)
print("done",n)
