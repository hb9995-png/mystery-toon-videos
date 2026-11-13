"""꿀팁다람 릴스 렌더러: python3 reel.py episode.json out.mp4 [seed]
episode.json: {"slides":[{"tag":"..","title":"..\\n..","body":"..\\n..","bubble":"..", "hook":true|"end":true, "dur":3.6}]}"""
import json, math, os, sys, subprocess, tempfile, wave, random
import numpy as np
from PIL import Image, ImageDraw, ImageFont
HERE=os.path.dirname(os.path.abspath(__file__))
W,H,FPS=1080,1920,30
def font(bold,s):
    p="/usr/share/fonts/opentype/noto/NotoSansCJK-Black.ttc" if bold else "/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc"
    if not os.path.exists(p): p="/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc"
    return ImageFont.truetype(p,s,index=1)
CREAM=(255,246,229); BROWN=(92,58,33); ORANGE=(255,159,67); NAVY=(38,52,94)
def ease(t): return 1-(1-min(max(t,0),1))**3
def text_c(d,y,txt,f,fill,gap=14):
    for line in txt.split("\n"):
        w=d.textlength(line,font=f); d.text(((W-w)/2,y),line,font=f,fill=fill); y+=f.size+gap
    return y
def fit(d,txt,bold,size,maxw):
    while size>40:
        f=font(bold,size)
        if max(d.textlength(l,font=f) for l in txt.split("\n"))<=maxw: return f
        size-=4
    return font(bold,size)
def render(ep,outdir):
    char=Image.open(os.path.join(HERE,"..","assets","daram.png"))
    slides=ep["slides"]; n=0
    for si,s in enumerate(slides):
        N=int(s.get("dur",3.2 if s.get("hook") else 3.6)*FPS)
        for i in range(N):
            t=i/FPS; img=Image.new("RGB",(W,H),CREAM); d=ImageDraw.Draw(img)
            for yy in range(0,H,90):
                for xx in range((yy//90%2)*45,W,90): d.ellipse([xx-5,yy-5,xx+5,yy+5],fill=(250,232,200))
            d.rounded_rectangle([60,110,W-60,200],45,fill=BROWN)
            bf=font(True,44); lab="꿀팁다람 | 중고딩 생활 꿀팁"
            d.text(((W-d.textlength(lab,font=bf))/2,128),lab,font=bf,fill=(255,236,200))
            for k in range(len(slides)):
                cx=W/2+(k-(len(slides)-1)/2)*40
                d.ellipse([cx-9,235,cx+9,253],fill=ORANGE if k<=si else (230,210,180))
            p=ease(t/0.35); tf=font(True,50); tw=d.textlength(s["tag"],font=tf); ty=300+(1-p)*40
            d.rounded_rectangle([(W-tw)/2-40,ty,(W+tw)/2+40,ty+90],45,fill=ORANGE); d.text(((W-tw)/2,ty+12),s["tag"],font=tf,fill="white")
            base=128 if s.get("hook") else 112
            f=fit(d,s["title"],True,int(base*(0.85+0.15*p)),W-120)
            y=text_c(d,450,s["title"],f,NAVY,18)
            p2=ease((t-0.35)/0.35)
            if p2>0 and s.get("body"):
                bfnt=fit(d,s["body"],False,60,W-260); lines=s["body"].split("\n")
                lh=bfnt.size+20; ch=len(lines)*lh+80; top=y+50+(1-p2)*30
                card=Image.new("RGBA",(W,H),(0,0,0,0)); cd=ImageDraw.Draw(card)
                cd.rounded_rectangle([90,top,W-90,top+ch],40,fill=(255,255,255,int(255*p2)),outline=(240,215,175,int(255*p2)),width=5)
                img.paste(card,(0,0),card); d=ImageDraw.Draw(img); yy=top+40
                for line in lines:
                    w=d.textlength(line,font=bfnt); d.text(((W-w)/2,yy),line,font=bfnt,fill=BROWN); yy+=lh
            big=s.get("hook") or s.get("end"); cs=640 if s.get("end") else 560
            c=char.resize((cs,int(cs*char.height/char.width)))
            c=c.rotate(4*math.sin(2*math.pi*t*0.8),resample=Image.BICUBIC,expand=True)
            cx=(W-c.width)//2 if big else W-c.width-30
            img.paste(c,(cx,H-c.height-90+int(14*math.sin(2*math.pi*t*1.6))),c)
            if not big and s.get("bubble"):
                d=ImageDraw.Draw(img); sb=font(True,46); txt=s["bubble"]; sw=d.textlength(txt,font=sb); bx,by=70,H-520
                d.rounded_rectangle([bx,by,bx+sw+60,by+90],45,fill="white",outline=BROWN,width=5)
                d.polygon([(bx+sw+40,by+60),(bx+sw+110,by+120),(bx+sw+20,by+85)],fill="white")
                d.text((bx+30,by+14),txt,font=sb,fill=BROWN)
            img.save(f"{outdir}/{n:05d}.png"); n+=1
    return n/FPS
NOTES={'C3':130.81,'D3':146.83,'E3':164.81,'F3':174.61,'G3':196.0,'A3':220.0,'B3':246.94,'C4':261.63,'D4':293.66,'E4':329.63,'F4':349.23,'G4':392.0,'A4':440.0,'B4':493.88,'C5':523.25,'D5':587.33,'E5':659.25,'F5':698.46,'G5':783.99}
PROGS=[[['C4','E4','G4','C3'],['G3','B3','D4','G3'],['A3','C4','E4','A3'],['F3','A3','C4','F3']],
       [['F3','A3','C4','F3'],['G3','B3','D4','G3'],['E3','G3','B3','E3'],['A3','C4','E4','A3']],
       [['C4','E4','G4','C3'],['A3','C4','E4','A3'],['F3','A3','C4','F3'],['G3','B3','D4','G3']]]
SCALE=['C5','D5','E5','G5','A4','G4','E5','C5','D5']
def music(path,dur,seed):
    rng=random.Random(seed); np.random.seed(seed%2**32)
    SR=44100; bpm=rng.choice([104,110,116,122]); beat=60/bpm; out=np.zeros(int(SR*(dur+0.5)))
    prog=rng.choice(PROGS); mel=[rng.choice(SCALE) for _ in range(16)]; cache={}
    def pluck(n,l,a):
        k=(n,l,a)
        if k in cache: return cache[k]
        fr=NOTES[n]; N=int(SR/fr); buf=np.random.uniform(-1,1,N); m=int(SR*l); y=np.zeros(m)
        for i in range(m): y[i]=buf[i%N]; buf[i%N]=0.996*0.5*(buf[i%N]+buf[(i+1)%N])
        cache[k]=y*a; return cache[k]
    def add(y,t):
        s=int(t*SR); e=min(len(out),s+len(y))
        if s<len(out): out[s:e]+=y[:e-s]
    t=0; bar=0
    while t<dur:
        ch=prog[bar%4]
        for b in range(4):
            tt=t+b*beat
            if b in (0,2): add(pluck(ch[3],beat*2,0.3),tt)
            for k,nn in enumerate(ch[:3]): add(pluck(nn,beat*1.2,0.12),tt+0.015*k+beat*0.5)
            for h in range(2):
                if (b*2+h)%3!=2: add(pluck(mel[(bar*8+b*2+h)%16],beat*0.9,0.16),tt+h*beat/2)
            kl=int(0.12*SR); kt=np.arange(kl)/SR
            if b in (0,2): add(np.sin(2*np.pi*(60+80*np.exp(-kt*30))*kt)*np.exp(-kt*25)*0.35,tt)
            sl=int(0.04*SR); add(np.random.randn(sl)*np.exp(-np.arange(sl)/400)*0.04,tt+beat/2)
        t+=4*beat; bar+=1
    out=out[:int(SR*dur)]; f=int(SR*1.5); out[-f:]*=np.linspace(1,0,f); out[:int(SR*.05)]*=np.linspace(0,1,int(SR*.05))
    out=out/np.max(np.abs(out))*0.8
    with wave.open(path,"w") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes((out*32767).astype(np.int16).tobytes())
if __name__=="__main__":
    ep=json.load(open(sys.argv[1])); out=sys.argv[2]; seed=int(sys.argv[3]) if len(sys.argv)>3 else 1
    tmp=tempfile.mkdtemp(); fr=os.path.join(tmp,"f"); os.makedirs(fr)
    dur=render(ep,fr); wav=os.path.join(tmp,"m.wav"); music(wav,dur,seed)
    subprocess.run(["ffmpeg","-y","-loglevel","error","-framerate",str(FPS),"-i",f"{fr}/%05d.png","-i",wav,"-c:v","libx264","-preset","veryfast","-crf","21","-pix_fmt","yuv420p","-c:a","aac","-b:a","160k","-shortest","-movflags","+faststart",out],check=True)
    print("ok",out,round(dur,1))
