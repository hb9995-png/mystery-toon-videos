"""동네성적표 릴스 렌더러: python3 render.py episodes/xxx.json out/xxx.mp4 [--bgm bgm.wav] [--still t]"""
import json, math, sys, subprocess, os
from PIL import Image, ImageDraw, ImageFont, ImageFilter
sys.path.insert(0, os.path.dirname(__file__))
import basemap

W, H, FPS = 1080, 1920, 30
MAP_Y, MAP_H = 280, 1240
PAPER = (250, 246, 238); INK = (31, 42, 68); RED = (214, 64, 43); MUTED = (120, 124, 138); LINE = (226, 219, 204)
FB = '/usr/share/fonts/opentype/noto/NotoSansCJK-Black.ttc'
FBo = '/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc'
FM = '/usr/share/fonts/opentype/noto/NotoSansCJK-Medium.ttc'
_fc = {}
def F(path, size):
    k = (path, size)
    if k not in _fc: _fc[k] = ImageFont.truetype(path, size, index=1)
    return _fc[k]

def ease(t): t = max(0, min(1, t)); return 1 - (1 - t) ** 3
def clamp(t): return max(0, min(1, t))

def text_c(d, cx, y, s, font, fill):
    w = d.textlength(s, font=font); d.text((cx - w / 2, y), s, font=font, fill=fill)

def stamp(grade, size=230):
    im = Image.new('RGBA', (size, size), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.ellipse((8, 8, size - 8, size - 8), outline=RED + (255,), width=10)
    d.ellipse((26, 26, size - 26, size - 26), outline=RED + (255,), width=3)
    f = F(FB, int(size * (0.46 if len(grade) < 2 else 0.38)))
    bb = d.textbbox((0, 0), grade, font=f)
    d.text(((size - (bb[2] - bb[0])) / 2 - bb[0], (size - (bb[3] - bb[1])) / 2 - bb[1]), grade, font=f, fill=RED + (255,))
    im = im.rotate(-12, resample=Image.BICUBIC)
    a = im.split()[3].point(lambda v: int(v * 0.92)); im.putalpha(a)
    return im

def paste_stamp(fr, st, cx, cy, t):
    """t: 0..1 stamp-in animation (big->normal)."""
    if t <= 0: return
    k = 1.0 + 0.9 * (1 - ease(t * 1.4))
    s = st.resize((int(st.width * k), int(st.height * k)), Image.BICUBIC)
    if t < 0.3:
        s.putalpha(s.split()[3].point(lambda v: int(v * t / 0.3)))
    fr.alpha_composite(s, (int(cx - s.width / 2), int(cy - s.height / 2)))

class Ep:
    def __init__(s, spec):
        s.sp = spec
        prefix = f"build/ep{spec['ep']:02d}"
        if not os.path.exists(prefix + '_map.png'):
            basemap.build(spec['adm_nm'], prefix, W=W, H=MAP_H)
        s.map = Image.open(prefix + '_map.png').convert('RGBA')
        s.geo = json.load(open(prefix + '_geo.json'))
        # outside dim mask
        mask = Image.new('L', (W, MAP_H), 0); md = ImageDraw.Draw(mask)
        for r in s.geo['rings']: md.polygon([tuple(p) for p in r], fill=255)
        dim = Image.new('RGBA', (W, MAP_H), (31, 42, 68, 70)); inv = mask.point(lambda v: 255 - v)
        s.dimlayer = Image.new('RGBA', (W, MAP_H), (0, 0, 0, 0)); s.dimlayer.paste(dim, (0, 0), inv)
        s.fill = Image.new('RGBA', (W, MAP_H), (0, 0, 0, 0)); s.fill.paste(Image.new('RGBA', (W, MAP_H), RED + (34,)), (0, 0), mask)
        # ring perimeter for progressive stroke
        s.segs = []
        for r in s.geo['rings']:
            pts = [tuple(p) for p in r] + [tuple(r[0])]
            for a, b in zip(pts, pts[1:]): s.segs.append((a, b, math.dist(a, b)))
        s.perim = sum(x[2] for x in s.segs)
        s.pins = []
        for p in spec.get('pins', []):
            z, L, T = s.geo['z'], s.geo['L'], s.geo['T']
            x, y = basemap.ll2px(p['lon'], p['lat'], z); s.pins.append((p['name'], x - L, y - T))
        s.stamps = {g: stamp(g) for g in {x['grade'] for x in spec['subjects']}}
        s.bigstamp = stamp(spec['total'], 330)
        s.minis = {g: stamp(g, 120) for g in {x['grade'] for x in spec['subjects']}}
        # timeline
        s.t_sub0, s.t_sub = 5.0, 6.0
        n = len(spec['subjects'])
        s.t_minus = s.t_sub0 + n * s.t_sub
        s.t_total = s.t_minus + 5.0
        s.t_cta = s.t_total + 8.0
        s.dur = s.t_cta + 4.5
        s.header = s.make_header()

    def make_header(s):
        im = Image.new('RGBA', (W, H), PAPER + (255,)); d = ImageDraw.Draw(im)
        for y in range(MAP_Y + MAP_H + 70, H, 64): d.line((60, y, W - 60, y), fill=LINE, width=2)
        sp = s.sp
        tag = f"{sp['brand']}  ·  EP.{sp['ep']:02d}"
        d.rounded_rectangle((60, 46, 60 + d.textlength(tag, font=F(FBo, 34)) + 44, 104), 29, fill=INK)
        d.text((82, 50), tag, font=F(FBo, 34), fill=PAPER)
        d.text((60, 120), sp['title'], font=F(FB, 100), fill=INK)
        d.text((W - 60 - d.textlength(sp['sido'], font=F(FM, 34)), 62), sp['sido'], font=F(FM, 34), fill=MUTED)
        d.line((60, 262, W - 60, 262), fill=INK, width=4)
        foot = '지도 © OpenStreetMap contributors  ·  정보 제공 목적, 투자 권유 아님'
        text_c(d, W / 2, H - 58, foot, F(FM, 24), MUTED)
        return im

    def map_frame(s, t):
        m = s.map.copy()
        m.alpha_composite(s.dimlayer)
        prog = ease(clamp((t - 0.4) / 2.4))
        if prog >= 1: m.alpha_composite(s.fill)
        d = ImageDraw.Draw(m)
        left = prog * s.perim
        for a, b, l in s.segs:
            if left <= 0: break
            if l > left:
                k = left / l; b = (a[0] + (b[0] - a[0]) * k, a[1] + (b[1] - a[1]) * k)
            d.line((a, b), fill=RED, width=9); left -= l
        # pins
        pa = ease(clamp((t - 3.0) / 0.6))
        if pa > 0:
            for name, x, y in s.pins:
                r = 16 * pa
                d.ellipse((x - r - 6, y - r - 6, x + r + 6, y + r + 6), fill=(255, 255, 255))
                d.ellipse((x - r, y - r, x + r, y + r), fill=INK)
                f = F(FBo, 34); tw = d.textlength(name, font=f)
                d.rounded_rectangle((x + 30, y - 30, x + 30 + tw + 36, y + 28), 14, fill=INK)
                d.text((x + 48, y - 26), name, font=f, fill=PAPER)
        # slow zoom
        z = 1.0 + 0.05 * (t / s.dur)
        if z > 1.001:
            mw, mh = int(W * z), int(MAP_H * z)
            m = m.resize((mw, mh), Image.BILINEAR).crop(((mw - W) // 2, (mh - MAP_H) // 2, (mw - W) // 2 + W, (mh - MAP_H) // 2 + MAP_H))
        return m

    def subject_card(s, sub, i, lt):
        """lt: local time within the subject slot."""
        cw, ch = 960, 420
        card = Image.new('RGBA', (cw + 40, ch + 40), (0, 0, 0, 0))
        sh = Image.new('RGBA', card.size, (0, 0, 0, 0)); ImageDraw.Draw(sh).rounded_rectangle((20, 28, cw + 20, ch + 28), 36, fill=(0, 0, 0, 70))
        card.alpha_composite(sh.filter(ImageFilter.GaussianBlur(12)))
        d = ImageDraw.Draw(card)
        d.rounded_rectangle((20, 20, cw + 20, ch + 20), 36, fill=(255, 253, 248), outline=LINE, width=2)
        d.ellipse((60, 60, 160, 160), fill=INK); text_c(d, 110, 72, sub['key'], F(FB, 56), PAPER)
        d.text((186, 58), sub['name'], font=F(FB, 72), fill=INK)
        d.text((188, 146), f"{i + 1}교시 / {len(s.sp['subjects'])}", font=F(FM, 28), fill=MUTED)
        for j, ln in enumerate(sub['lines']):
            a = ease(clamp((lt - 0.6 - j * 0.35) / 0.4))
            if a <= 0: continue
            y = 216 + j * 64
            col = tuple(int(PAPER[k] + (INK[k] - PAPER[k]) * a) for k in range(3))
            d.ellipse((66, y + 18, 80, y + 32), fill=RED if j == 2 and '단' in ln[:2] else col)
            d.text((100, y), ln, font=F(FBo, 40), fill=col)
        paste_stamp(card, s.stamps[sub['grade']], cw - 120, 150, clamp((lt - 2.1) / 0.6))
        return card

    def total_card(s, lt):
        cw, ch = 940, 1080
        card = Image.new('RGBA', (cw, ch), (0, 0, 0, 0)); d = ImageDraw.Draw(card)
        d.rounded_rectangle((0, 0, cw, ch), 40, fill=(255, 253, 248), outline=INK, width=4)
        text_c(d, cw / 2, 40, '성   적   표', F(FB, 64), INK)
        text_c(d, cw / 2, 130, s.sp['title'], F(FBo, 38), MUTED)
        d.line((60, 200, cw - 60, 200), fill=INK, width=3)
        for j, sub in enumerate(s.sp['subjects']):
            y = 220 + j * 112
            a = ease(clamp((lt - 0.3 - j * 0.25) / 0.35))
            if a <= 0: continue
            d.text((80, y + 18), sub['name'], font=F(FB, 54), fill=INK)
            d.text((260, y + 34), sub['sub'], font=F(FM, 28), fill=MUTED)
            mini = s.minis[sub['grade']]
            card.alpha_composite(mini, (cw - 80 - mini.width, y - 4))
            d.line((60, y + 106, cw - 60, y + 106), fill=LINE, width=2)
        if lt > 2.0:
            text_c(d, 250, 830, '종합', F(FB, 64), INK)
            for k, v in enumerate(s.sp['verdict']):
                text_c(d, 250, 930 + k * 48, v, F(FBo, 32), MUTED)
        paste_stamp(card, s.bigstamp, cw - 240, 880, clamp((lt - 2.3) / 0.7))
        return card

    def frame(s, t):
        fr = s.header.copy(); sp = s.sp
        fr.alpha_composite(s.map_frame(t), (0, MAP_Y))
        d = ImageDraw.Draw(fr)
        cap_y = MAP_Y + MAP_H + 60
        def caption(lines, a=1.0):
            col = tuple(int(PAPER[k] + (INK[k] - PAPER[k]) * a) for k in range(3))
            for k, ln in enumerate(lines): text_c(d, W / 2, cap_y + k * 76, ln, F(FB, 56), col)
        if t < s.t_sub0:
            caption(sp['hook'], ease(clamp((t - 0.3) / 0.5)))
        elif t < s.t_minus:
            i = int((t - s.t_sub0) // s.t_sub); lt = t - s.t_sub0 - i * s.t_sub
            sub = sp['subjects'][i]
            y = 1720 - ease(clamp(lt / 0.5)) * 640 if lt < 5.6 else 1080 + ease((lt - 5.6) / 0.4) * 640
            fr.alpha_composite(s.subject_card(sub, i, lt), (20, int(y) - 20))
            fr.paste(s.header.crop((0, MAP_Y + MAP_H, W, H)), (0, MAP_Y + MAP_H))
            caption([sub['sub']], ease(clamp((lt - 0.4) / 0.4)))
        elif t < s.t_total:
            lt = t - s.t_minus
            cw, ch = 960, 330
            y = 1720 - ease(clamp(lt / 0.5)) * 600 if lt < 4.6 else 1120 + ease((lt - 4.6) / 0.4) * 600
            card = Image.new('RGBA', (cw, ch), (0, 0, 0, 0)); cd = ImageDraw.Draw(card)
            cd.rounded_rectangle((0, 0, cw, ch), 36, fill=(255, 253, 248), outline=RED, width=4)
            cd.text((50, 36), '감점 요인', font=F(FB, 60), fill=RED)
            for j, ln in enumerate(sp['minus']):
                a = ease(clamp((lt - 0.6 - j * 0.4) / 0.4))
                if a > 0: cd.text((60, 140 + j * 80), '-  ' + ln, font=F(FBo, 42), fill=INK)
            fr.alpha_composite(card, (60, int(y)))
            fr.paste(s.header.crop((0, MAP_Y + MAP_H, W, H)), (0, MAP_Y + MAP_H))
            caption(['완벽한 동네는 없죠'], ease(clamp((lt - 0.4) / 0.4)))
        elif t < s.t_cta:
            lt = t - s.t_total
            a = ease(clamp(lt / 0.5))
            card = s.total_card(lt)
            fr.alpha_composite(card, ((W - card.width) // 2, int(MAP_Y + 80 + (1 - a) * 300)))
            caption(['최종 성적은?'] if lt < 2.4 else ['종합 ' + sp['total'] + ' 받았습니다'], 1.0)
        else:
            lt = t - s.t_cta
            ov = Image.new('RGBA', (W, MAP_H), INK + (int(215 * ease(clamp(lt / 0.5))),))
            fr.alpha_composite(ov, (0, MAP_Y))
            a = ease(clamp((lt - 0.3) / 0.5))
            col = tuple(int(INK[k] + (PAPER[k] - INK[k]) * a) for k in range(3))
            for k, ln in enumerate(sp['cta']): text_c(d, W / 2, 760 + k * 100, ln, F(FB, 64), col)
            text_c(d, W / 2, 1010, '다음 시간에 채점할 동네는 댓글에서 뽑아요', F(FM, 36), col)
            caption([f"{sp['brand']} 팔로우하고 다음 성적표 받기"], a)
        return fr.convert('RGB')

def main():
    spec = json.load(open(sys.argv[1])); out = sys.argv[2]
    bgm = sys.argv[sys.argv.index('--bgm') + 1] if '--bgm' in sys.argv else None
    ep = Ep(spec)
    if '--still' in sys.argv:
        for tt in sys.argv[sys.argv.index('--still') + 1].split(','):
            ep.frame(float(tt)).save(f'build/still_{tt}.png')
        print('dur', ep.dur); return
    cmd = ['ffmpeg', '-y', '-loglevel', 'error', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-']
    if bgm: cmd += ['-i', bgm, '-shortest', '-c:a', 'aac', '-b:a', '160k', '-af', f'afade=t=out:st={ep.dur - 1.5}:d=1.5']
    cmd += ['-c:v', 'libx264', '-preset', 'veryfast', '-crf', '20', '-pix_fmt', 'yuv420p', '-movflags', '+faststart', out]
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    n = int(ep.dur * FPS)
    for k in range(n): p.stdin.write(ep.frame(k / FPS).tobytes())
    p.stdin.close(); p.wait(); print('done', out, ep.dur)

if __name__ == '__main__': main()
