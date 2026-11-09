"""오리지널 배경음악 생성: python3 bgm2.py out.wav 길이초 seed style
style: hook(통통 튀는 신스 플럭, 장난스러운 긴장감) / law(잔잔한 피아노, 정보 전달용)
시드마다 조성, 빠르기, 코드 진행, 멜로디가 달라진다. 외부 음원은 쓰지 않는다."""
import numpy as np, wave, sys
SR = 44100
out = sys.argv[1]; dur = float(sys.argv[2]); seed = int(sys.argv[3]); style = sys.argv[4] if len(sys.argv) > 4 else 'hook'
rng = np.random.default_rng(seed); n = int(SR * dur); mix = np.zeros(n)
hz = lambda k: 440 * 2 ** ((k - 69) / 12)
def add(sig, t0, amp):
    i = int(t0 * SR)
    if i >= n: return
    L = min(len(sig), n - i); mix[i:i + L] += sig[:L] * amp
def env(t, a, d): return np.minimum(1, t / a) * np.exp(-t * d)
def pluck(f, d=.3):
    t = np.arange(int(d * SR)) / SR
    s = np.sign(np.sin(2 * np.pi * f * t)) * .35 + np.sin(2 * np.pi * f * t) * .65
    return s * env(t, .002, 14)
def piano(f, d=1.2):
    t = np.arange(int(d * SR)) / SR
    return sum(np.sin(2 * np.pi * f * h * t) * a * np.exp(-t * (2.5 + h)) for h, a in [(1, 1), (2, .4), (3, .15), (4, .08)]) * np.minimum(1, t / .004)
def pad(f, d):
    t = np.arange(int(d * SR)) / SR
    return (np.sin(2 * np.pi * f * t) + .5 * np.sin(2 * np.pi * f * 1.003 * t)) * np.minimum(1, t / .4) * np.minimum(1, (d - t) / .4)
def bass(f, d):
    t = np.arange(int(d * SR)) / SR
    return np.sin(2 * np.pi * f * t) * np.minimum(1, t / .01) * np.minimum(1, (d - t) / .05)
if style == 'hook':
    bpm = int(rng.choice([96, 100, 104, 110])); root = 57 + int(rng.choice([0, 2, 3, 5]))
    PROGS = [[0, 8, 3, 10], [0, 5, 8, 7], [0, 10, 8, 7], [0, 3, 8, 10]]; SCALE = [0, 3, 5, 7, 10]
else:
    bpm = int(rng.choice([72, 76, 80, 84])); root = 60 + int(rng.choice([-5, -3, 0, 2]))
    PROGS = [[0, 9, 5, 7], [0, 7, 9, 5], [5, 7, 0, 9], [0, 4, 9, 5]]; SCALE = [0, 2, 4, 7, 9]
beat = 60 / bpm; bar = 4 * beat; prog = PROGS[int(rng.integers(len(PROGS)))]
def triad(deg):
    minor = (style == 'hook' and deg in (0, 5, 7)) or (style == 'law' and deg in (9, 2, 4))
    return [root + deg, root + deg + (3 if minor else 4), root + deg + 7]
RHY = [[0, .75, 1.5, 2.5, 3], [0, .5, 1.5, 2, 3.5], [0, 1, 1.75, 2.5, 3.25]]
rhythm = RHY[int(rng.integers(3))]
motif = [(b, int(rng.integers(5))) for b in rhythm] + [(4 + b, int(rng.integers(5))) for b in rhythm[:4]]
t = 0; b = 0
while t < dur:
    deg = prog[b % 4]; ch = triad(deg)
    if style == 'hook':
        add(bass(hz(root + deg - 24), beat * .45), t, .22); add(bass(hz(root + deg - 24), beat * .45), t + beat * 1.5, .18)
        add(bass(hz(root + deg - 12), beat * .45), t + beat * 2.5, .14)
        for s in (0, 1, 2, 3):
            tt = np.arange(int(.18 * SR)) / SR
            if s in (0, 2): add(np.sin(2 * np.pi * (50 + 80 * np.exp(-tt * 40)) * tt) * np.exp(-tt * 16), t + s * beat, .26)
            else:
                L = int(.08 * SR); add(rng.standard_normal(L) * np.exp(-np.arange(L) / SR * 50), t + s * beat, .09)
            L = int(.03 * SR); add(rng.standard_normal(L) * np.exp(-np.arange(L) / SR * 160), t + (s + .5) * beat, .04)
        for s in (.5, 1.5, 2.5, 3.5):
            for j, k in enumerate(ch): add(pluck(hz(k + 12), .18), t + s * beat + j * .008, .03)
        if b >= 2:
            for pos, idx in motif:
                if int(pos // 4) == b % 2: add(pluck(hz(root + 12 + SCALE[idx]), .25), t + (pos % 4) * beat, .11)
    else:
        for k in ch: add(pad(hz(k), bar), t, .025)
        add(bass(hz(root + deg - 24), bar * .9), t, .13)
        for s, k in zip((0, 1, 2, 3), (ch[0], ch[1], ch[2], ch[1])): add(piano(hz(k)), t + s * beat, .07)
        if b >= 2:
            for pos, idx in motif[::2]:
                if int(pos // 4) == b % 2: add(piano(hz(root + 12 + SCALE[idx]), 1.6), t + (pos % 4) * beat, .12)
    t += bar; b += 1
mix = np.convolve(mix, np.ones(3) / 3, 'same'); mix *= np.minimum(1, np.arange(n) / SR / .3)
mix /= np.abs(mix).max() * 1.15
w = wave.open(out, 'wb'); w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
w.writeframes((mix * 32767).astype(np.int16).tobytes()); w.close()
