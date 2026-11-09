import numpy as np, wave, sys
SR=44100; dur=float(sys.argv[2]) if len(sys.argv)>2 else 60; out=sys.argv[1]
rng=np.random.default_rng(int(sys.argv[3]) if len(sys.argv)>3 else 7)
bpm=88; beat=60/bpm; n=int(SR*dur); mix=np.zeros(n)
def note(f,t0,d,amp,kind='pad'):
    i0=int(t0*SR); L=int(d*SR)
    if i0>=n: return
    L=min(L,n-i0); t=np.arange(L)/SR
    if kind=='pad':
        w=sum(np.sin(2*np.pi*f*h*t+rng.random())*a for h,a in [(1,1),(2,.3),(3,.12)])
        env=np.minimum(1,t/0.4)*np.minimum(1,(d-t)/0.6)
    else:
        w=np.sin(2*np.pi*f*t)*(1+0.3*np.sin(2*np.pi*f*2*t)); env=np.exp(-t*5)*np.minimum(1,t/0.005)
    mix[i0:i0+L]+=w*env*amp
m=lambda k:440*2**((k-69)/12)
prog=[[60,64,67,71],[57,60,64,67],[53,57,60,64],[55,59,62,65]]  # Cmaj7 Am7 Fmaj7 G7
mel=[76,74,72,71,72,74,76,79]
bar=4*beat; t=0; b=0
while t<dur:
    ch=prog[b%4]
    for k in ch: note(m(k),t,bar+0.3,0.05)
    note(m(ch[0]-24),t,bar,0.10)
    for s in range(8):
        if rng.random()<0.55: note(m(rng.choice(ch)+12),t+s*beat/2,0.6,0.045,'pluck')
    for s in range(4):  # kick + hat
        i0=int((t+s*beat)*SR)
        if s in (0,2) and i0<n:
            L=min(int(0.25*SR),n-i0); tt=np.arange(L)/SR
            mix[i0:i0+L]+=np.sin(2*np.pi*(50+60*np.exp(-tt*30))*tt)*np.exp(-tt*12)*0.22
        for h in (0,0.5):
            i1=int((t+(s+h)*beat)*SR)
            if i1<n:
                L=min(int(0.05*SR),n-i1); mix[i1:i1+L]+=rng.standard_normal(L)*np.exp(-np.arange(L)/SR*80)*0.025
    t+=bar; b+=1
crack=(rng.random(n)<0.0004)*rng.standard_normal(n)*0.08
mix+=crack+rng.standard_normal(n)*0.002
# simple lowpass for warmth
k=np.ones(6)/6; mix=np.convolve(mix,k,'same')
mix*=np.minimum(1,np.arange(n)/SR/1.0); mix/=np.abs(mix).max()*1.25
st=np.stack([mix,np.roll(mix,int(0.012*SR))],1)
w=wave.open(out,'wb'); w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes((st*32767).astype(np.int16).tobytes()); w.close()
