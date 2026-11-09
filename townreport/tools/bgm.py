"""동네성적표 오리지널 배경음악: python3 bgm.py out.wav 길이초 [seed]
밝고 가벼운 마림바+우쿨렐레풍. 시드마다 조성, 빠르기, 코드, 멜로디가 달라진다."""
import numpy as np, wave, sys
SR = 44100; out = sys.argv[1]; dur = float(sys.argv[2]) if len(sys.argv) > 2 else 30
rng = np.random.default_rng(int(sys.argv[3]) if len(sys.argv) > 3 else 7)
n = int(SR * dur); mix = np.zeros(n)
bpm = int(rng.choice([100, 104, 108, 112])); beat = 60 / bpm; bar = 4 * beat
root = 60 + int(rng.choice([-3, -1, 0, 2, 5]))
PROGS = [[0, 7, 9, 5], [0, 5, 7, 5], [9, 5, 0, 7], [0, 9, 5, 7]]
prog = PROGS[int(rng.integers(len(PROGS)))]
PENTA = [0, 2, 4, 7, 9]
hz = lambda k: 440 * 2 ** ((k - 69) / 12)

def add(sig, t0, amp):
    i = int(t0 * SR)
    if i >= n: return
    L = min(len(sig), n - i); mix[i:i + L] += sig[:L] * amp

def marimba(f, d=0.5):
    t = np.arange(int(d * SR)) / SR
    return (np.sin(2 * np.pi * f * t) + 0.35 * np.sin(2 * np.pi * f * 4 * t) * np.exp(-t * 30)) * np.exp(-t * 9) * np.minimum(1, t / 0.003)

def uke(f, d=0.35):
    t = np.arange(int(d * SR)) / SR
    return sum(np.sin(2 * np.pi * f * h * t) * a for h, a in [(1, 1), (2, .5), (3, .25)]) * np.exp(-t * 11) * np.minimum(1, t / 0.004)

def bass(f, d):
    t = np.arange(int(d * SR)) / SR
    return np.sin(2 * np.pi * f * t) * np.minimum(1, t / 0.01) * np.minimum(1, (d - t) / 0.05)

def chord_notes(deg):
    q = 3 if deg in (9, 2, 4) else 4
    return [root + deg, root + deg + q, root + deg + 7]

# 2마디 멜로디 동기를 만들어 곡 전체에서 되풀이한다(반복되어야 귀에 남는다)
RHY = [[0, 1, 1.5, 2.5, 3], [0, .5, 1.5, 2, 3.5], [0, 1.5, 2, 3, 3.5]]
rhythm = RHY[int(rng.integers(len(RHY)))]
motif = [(b, int(rng.integers(5))) for b in rhythm] + [(4 + b, int(rng.integers(5))) for b in rhythm[:4]]

t = 0; b = 0
while t < dur:
    deg = prog[b % 4]; ch = chord_notes(deg)
    add(bass(hz(root + deg - 24), beat * 1.6), t, .20)
    add(bass(hz(root + deg - 24 + 7), beat * .9), t + beat * 2.5, .15)
    for s, a in zip((.5, 1.5, 2.5, 3.5), (.9, 1, .9, 1)):        # 뒷박 우쿨렐레
        for j, k in enumerate(ch): add(uke(hz(k + 12)), t + s * beat + j * .012, .035 * a)
    for s in (1, 3):                                              # 박수
        L = int(.09 * SR); add(rng.standard_normal(L) * np.exp(-np.arange(L) / SR * 45), t + s * beat, .07)
    for s in (0, 2):                                              # 킥
        tt = np.arange(int(.2 * SR)) / SR
        add(np.sin(2 * np.pi * (48 + 70 * np.exp(-tt * 35)) * tt) * np.exp(-tt * 14), t + s * beat, .24)
    if b >= 2:                                                    # 두 마디 깔아 준 뒤 멜로디 시작
        for pos, idx in motif:
            if int(pos // 4) == (b % 2):
                add(marimba(hz(root + 12 + PENTA[idx])), t + (pos % 4) * beat, .16)
    t += bar; b += 1

mix = np.convolve(mix, np.ones(3) / 3, 'same')
mix *= np.minimum(1, np.arange(n) / SR / .3)
mix /= np.abs(mix).max() * 1.12
st = np.stack([mix, np.roll(mix, int(.010 * SR))], 1)
w = wave.open(out, 'wb'); w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
w.writeframes((st * 32767).astype(np.int16).tobytes()); w.close()
