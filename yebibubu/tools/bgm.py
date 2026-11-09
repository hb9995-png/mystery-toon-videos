"""예비부부툰 오리지널 배경음악: python3 bgm.py out.wav 길이초 seed
밝고 귀여운 장조 (우쿨렐레 느낌 스트럼 + 글로켄 멜로디 + 가벼운 리듬). 시드마다 조성, 빠르기, 진행, 멜로디가 달라진다. 외부 음원 없음."""
import numpy as np, wave, sys
SR = 44100
out = sys.argv[1]; dur = float(sys.argv[2]); seed = int(sys.argv[3])
rng = np.random.default_rng(seed); n = int(SR * dur); mix = np.zeros(n)
hz = lambda k: 440 * 2 ** ((k - 69) / 12)
def add(sig, t0, amp):
    i = int(t0 * SR)
    if i >= n: return
    L = min(len(sig), n - i); mix[i:i + L] += sig[:L] * amp
def ks(f, d=.6):  # 카플러스-스트롱 현 (우쿨렐레 느낌)
    N = int(SR / f); buf = rng.uniform(-1, 1, N); L = int(d * SR); o = np.zeros(L)
    for i in range(L):
        o[i] = buf[i % N]; buf[i % N] = .5 * (buf[i % N] + buf[(i + 1) % N]) * .994
    return o
def glock(f, d=1.0):
    t = np.arange(int(d * SR)) / SR
    return (np.sin(2 * np.pi * f * t) + .35 * np.sin(2 * np.pi * f * 2.76 * t) * np.exp(-t * 6)) * np.exp(-t * 3.2) * np.minimum(1, t / .002)
def bass(f, d):
    t = np.arange(int(d * SR)) / SR
    return np.sin(2 * np.pi * f * t) * np.minimum(1, t / .01) * np.exp(-t * 2.5)
bpm = int(rng.choice([100, 104, 108, 112, 116])); root = 60 + int(rng.choice([-3, -1, 0, 2, 5]))
PROGS = [[0, 7, 9, 5], [0, 5, 7, 5], [0, 9, 5, 7], [5, 7, 0, 0], [0, 4, 5, 7]]
prog = PROGS[int(rng.integers(len(PROGS)))]; SCALE = [0, 2, 4, 7, 9, 12]
beat = 60 / bpm; bar = 4 * beat
def triad(d):
    m = d in (9, 4, 2)
    return [root + d, root + d + (3 if m else 4), root + d + 7]
STRUM = [[0, 1, 1.5, 2.5, 3], [0, .5, 1.5, 2, 3], [0, 1.5, 2, 3, 3.5]][int(rng.integers(3))]
motif = [(p, int(rng.integers(6))) for p in sorted(rng.choice(np.arange(0, 8, .5), 7, replace=False))]
cache = {}
t = 0; b = 0
while t < dur:
    ch = triad(prog[b % 4])
    add(bass(hz(ch[0] - 24), beat * 1.6), t, .2); add(bass(hz(ch[0] - 24), beat * 1.2), t + 2 * beat, .16)
    for s in STRUM:
        for j, k in enumerate(ch + [ch[0] + 12]):
            key = k
            if key not in cache: cache[key] = ks(hz(k), .5)
            add(cache[key], t + s * beat + j * .012, .05)
    for s in range(4):
        tt = np.arange(int(.15 * SR)) / SR
        if s in (0, 2): add(np.sin(2 * np.pi * (55 + 60 * np.exp(-tt * 40)) * tt) * np.exp(-tt * 18), t + s * beat, .18)
        L = int(.04 * SR); add(rng.standard_normal(L) * np.exp(-np.arange(L) / SR * 90), t + (s + .5) * beat, .035)
    if b >= 1:
        for pos, idx in motif:
            if int(pos // 4) == b % 2: add(glock(hz(root + 12 + SCALE[idx])), t + (pos % 4) * beat, .1)
    t += bar; b += 1
mix = np.convolve(mix, np.ones(3) / 3, 'same'); mix *= np.minimum(1, np.arange(n) / SR / .2)
mix /= np.abs(mix).max() * 1.2
w = wave.open(out, 'wb'); w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
w.writeframes((mix * 32767).astype(np.int16).tobytes()); w.close()
