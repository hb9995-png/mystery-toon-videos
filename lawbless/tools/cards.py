"""법블레스유(law.bless.you) 생활법률 카드뉴스 릴스 렌더러
python3 cards.py episode.json out.mp4
episode.json:
{"ep":1, "seed":11, "tag":"알바", "cover":{"q":"표지 질문(훅, 2~3줄)", "sub":"작은 부제"},
 "cards":[{"title":"소제목", "body":["짧은 문장", "..."], "law":"근거: 법 조문(선택)"}, ... 4~6장],
 "summary":["한 줄 정리", ...]}
- 1080x1920 세로, 장마다 정해진 시간 노출, 음성 없음, 오리지널 배경음악(bgm2.py law)
- 마지막 장에 '일반 정보이며 법률 자문이 아님 + 대한법률구조공단 132' 안내가 자동으로 들어간다
"""
import json, sys, os, subprocess
from PIL import Image, ImageDraw, ImageFont
HERE = os.path.dirname(os.path.abspath(__file__))
FB = '/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc'
FR = '/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
FK = '/usr/share/fonts/opentype/noto/NotoSansCJK-Black.ttc'
f = lambda p, s: ImageFont.truetype(p, s, index=1)
W, H = 1080, 1920
NAVY = (22, 34, 62); GOLD = (232, 190, 92); CREAM = (250, 246, 236); INK = (28, 30, 38); MUTE = (120, 120, 130)
DISC = '※ 일반적인 법률 정보이며 개별 사안에 대한 법률 자문이 아닙니다. 구체적인 사안은 변호사 또는 대한법률구조공단(국번 없이 132)에 상담하세요.'

def wrap(d, text, font, maxw):
    out = []
    for para in text.split('\n'):
        cur = ''
        for word in para.split(' '):
            t = (cur + ' ' + word).strip()
            if d.textlength(t, font=font) <= maxw: cur = t; continue
            if cur: out.append(cur)
            cur = ''
            for ch in word:
                if d.textlength(cur + ch, font=font) > maxw and cur: out.append(cur); cur = ch
                else: cur += ch
        out.append(cur)
    return out

def frame(page, total, tag):
    im = Image.new('RGB', (W, H), CREAM); d = ImageDraw.Draw(im)
    d.rectangle([0, 0, W, 170], fill=NAVY)
    d.text((60, 52), '법블레스유', font=f(FK, 54), fill=GOLD)
    t = f'#{tag}'; tw = d.textlength(t, font=f(FB, 36)); d.text((W - 60 - tw, 64), t, font=f(FB, 36), fill=(200, 208, 225))
    d.rectangle([0, H - 120, W, H], fill=NAVY)
    for i in range(total):
        x = W / 2 - (total - 1) * 22 + i * 44
        d.ellipse([x - 9, H - 69, x + 9, H - 51], fill=GOLD if i == page else (80, 92, 120))
    return im, d

def cover(ep, total):
    im, d = frame(0, total, ep['tag'])
    d.rectangle([60, 330, 80, 1100], fill=GOLD)
    y = 360
    for l in wrap(d, ep['cover']['q'], f(FK, 96), W - 200)[:5]:
        d.text((120, y), l, font=f(FK, 96), fill=INK); y += 132
    y += 40
    for l in wrap(d, ep['cover']['sub'], f(FB, 48), W - 200):
        d.text((120, y), l, font=f(FB, 48), fill=MUTE); y += 68
    d.text((120, 1560), '끝까지 보면 대처법까지 →', font=f(FB, 44), fill=NAVY)
    return im

def card(ep, c, page, total):
    im, d = frame(page, total, ep['tag'])
    lay = Image.new('RGB', (W, 1700), CREAM); g = ImageDraw.Draw(lay)
    g.text((70, 0), f'{page:02d}', font=f(FK, 64), fill=GOLD)
    y = 100
    for l in wrap(g, c['title'], f(FK, 78), W - 140):
        g.text((70, y), l, font=f(FK, 78), fill=INK); y += 104
    g.rectangle([70, y + 20, 230, y + 30], fill=GOLD); y += 90
    for para in c['body']:
        g.ellipse([74, y + 28, 90, y + 44], fill=NAVY)
        for l in wrap(g, para, f(FR, 56), W - 180): g.text((110, y), l, font=f(FR, 56), fill=INK); y += 80
        y += 36
    if c.get('law'):
        ls = wrap(g, c['law'], f(FB, 40), W - 200); bh = len(ls) * 58 + 50; y += 30
        g.rounded_rectangle([70, y, W - 70, y + bh], 24, fill=(234, 228, 212)); yy = y + 25
        for l in ls: g.text((100, yy), l, font=f(FB, 40), fill=(90, 80, 60)); yy += 58
        y += bh
    top = 170 + max(60, (H - 120 - 170 - y) // 2 - 40)
    im.paste(lay.crop((0, 0, W, y)), (0, top))
    return im, y

def summary(ep, page, total):
    im, d = frame(page, total, ep['tag'])
    d.text((70, 280), '3줄 요약', font=f(FK, 80), fill=INK)
    y = 440
    for i, s in enumerate(ep['summary']):
        d.rounded_rectangle([70, y, 150, y + 80], 18, fill=NAVY); d.text((96, y + 6), str(i + 1), font=f(FK, 56), fill=GOLD)
        for l in wrap(d, s, f(FB, 52), W - 260): d.text((180, y + 6), l, font=f(FB, 52), fill=INK); y += 76
        y += 50
    y = max(y + 40, 1240)
    d.text((70, y), '저장해두고 필요할 때 꺼내 보세요', font=f(FB, 44), fill=NAVY); y += 110
    for l in wrap(d, DISC, f(FR, 34), W - 140): d.text((70, y), l, font=f(FR, 34), fill=MUTE); y += 50
    return im

def main(epf, out):
    ep = json.load(open(epf, encoding='utf-8'))
    tmp = f"/tmp/law_{ep['ep']}"; os.makedirs(tmp, exist_ok=True)
    total = len(ep['cards']) + 2
    pages = [(cover(ep, total), 3.2)]
    for i, c in enumerate(ep['cards']):
        im, _ = card(ep, c, i + 1, total)
        chars = len(c['title']) + sum(len(b) for b in c['body']) + len(c.get('law', ''))
        pages.append((im, min(6.5, max(3.8, 2.0 + chars * 0.035))))
    pages.append((summary(ep, total - 1, total), 5.5))
    lst = ''
    for k, (im, dur) in enumerate(pages):
        p = f'{tmp}/{k:02d}.png'; im.save(p); lst += f"file '{p}'\nduration {dur:.2f}\n"
    lst += f"file '{tmp}/{len(pages)-1:02d}.png'\n"; open(f'{tmp}/list.txt', 'w').write(lst)
    T = sum(p[1] for p in pages)
    subprocess.run(['python3', os.path.join(HERE, 'bgm2.py'), f'{tmp}/bgm.wav', str(T + 1), str(ep.get('seed', ep['ep'])), 'law'], check=True)
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'concat', '-safe', '0', '-i', f'{tmp}/list.txt', '-i', f'{tmp}/bgm.wav',
        '-vf', 'fps=30,format=yuv420p', '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '21', '-c:a', 'aac', '-b:a', '160k',
        '-af', f'afade=t=out:st={T-1.5:.2f}:d=1.5', '-t', f'{T:.2f}', '-movflags', '+faststart', out], check=True)
    print(out, round(T, 1), 's')

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
