"""톡잘못보냄(hook.talk) 메신저 대화 썰 릴스 렌더러
python3 chat.py episode.json out.mp4
episode.json:
{"ep":1, "hook":"첫 2초 훅 문장(상단 띠, 2줄 이내)", "room":"대화방 이름", "seed":1,
 "msgs":[{"who":"me"|"them"|"sys", "text":"...", "name":"(them 일 때 선택, 단톡방용)", "hold":초(선택)}, ...],
 "end":"마지막 자막 한 줄(선택)"}
- me: 오른쪽 파란 말풍선, them: 왼쪽 회색 말풍선, "hl":true 면 빨강(핵심 실수 톡 1개), sys: 가운데 회색 안내(예: "메시지를 삭제했습니다", "오후 11:42")
- 1080x1920, H.264 + AAC, 음성 없음, 오리지널 배경음악(bgm2.py hook)
"""
import json, sys, os, subprocess
from PIL import Image, ImageDraw, ImageFont
HERE = os.path.dirname(os.path.abspath(__file__))
FB = '/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc'
FR = '/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
FK = '/usr/share/fonts/opentype/noto/NotoSansCJK-Black.ttc'
f = lambda p, s: ImageFont.truetype(p, s, index=1)  # index 1 = KR
W, H = 1080, 1920
# 디자인 C(2026-11-10 사용자 선택): 밝은 미니멀, 위 검은 훅 카드(마지막 줄 빨강), 파란 내 말풍선, 핵심 실수 톡("hl":true)만 빨강
BG = (247, 247, 250); BLUE = (40, 120, 255); RED = (255, 90, 90); GRAYB = (228, 228, 234)
TXT = (20, 20, 20); GRAY = (140, 140, 150)
FM = f('/usr/share/fonts/opentype/noto/NotoSansCJK-Medium.ttc', 48); FN = f(FR, 30); FS = f(FR, 30)
FH = f(FK, 74); FT = f(FB, 44); FE = f(FB, 52)
MAXW = 760; LH = 64; PAD = 28
CARD = (50, 90, W - 50, 380)

def wrap(d, text, font, maxw):
    # 띄어쓰기 단위로 줄바꿈(한 글자만 다음 줄로 넘어가는 것 방지), 너무 긴 낱말만 글자 단위
    lines = []
    for para in text.split('\n'):
        cur = ''
        for word in para.split(' '):
            cand = (cur + ' ' + word) if cur else word
            if d.textlength(cand, font=font) <= maxw: cur = cand; continue
            if cur: lines.append(cur); cur = ''
            for ch in word:
                if d.textlength(cur + ch, font=font) > maxw and cur: lines.append(cur); cur = ch
                else: cur += ch
        lines.append(cur)
    return lines

def bubble_size(d, m):
    if m['who'] == 'sys':
        return 70, None
    lines = wrap(d, m['text'], FM, MAXW)
    w = max(d.textlength(l, font=FM) for l in lines) + PAD * 2
    h = len(lines) * LH + 34
    extra = 40 if (m['who'] == 'them' and m.get('name')) else 0
    return h + extra + 18, (lines, w, h, extra)

def draw_hook(d, hook):
    d.rectangle([0, 0, W, CARD[3] + 30], fill=BG)
    d.rounded_rectangle(CARD, 40, fill=(20, 20, 20))
    lines = wrap(d, hook, FH, CARD[2] - CARD[0] - 80)[:3]
    y = CARD[1] + (CARD[3] - CARD[1] - len(lines) * 95) // 2
    for i, l in enumerate(lines):
        tw = d.textlength(l, font=FH)
        d.text(((W - tw) / 2, y), l, font=FH, fill=RED if (i == len(lines) - 1 and len(lines) > 1) else (255, 255, 255)); y += 95

def draw_head(d, room):
    y0 = CARD[3] + 30
    d.rectangle([0, y0, W, y0 + 115], fill=BG)
    tw = d.textlength(room, font=FT); d.text(((W - tw) / 2, y0 + 20), room, font=FT, fill=(30, 30, 30))
    d.line([(W / 2 - 40, y0 + 92), (W / 2 + 40, y0 + 92)], fill=(220, 220, 228), width=3)

def render_state(ep, shown, typing, end_text=None):
    im = Image.new('RGB', (W, H), BG); d = ImageDraw.Draw(im)
    msgs = ep['msgs'][:shown]
    sizes = [bubble_size(d, m) for m in msgs]
    total = sum(s[0] for s in sizes) + (110 if typing else 0) + (50 if msgs and msgs[-1]['who'] == 'me' else 0)
    area_top = CARD[3] + 150; area_bot = H - 110
    y = area_bot - total if total > area_bot - area_top else area_top
    last_me = None
    for m, (h, info) in zip(msgs, sizes):
        if y < area_top - 10: y += h; continue  # 위로 밀려난 말풍선은 통째로 숨김
        if m['who'] == 'sys':
            tw = d.textlength(m['text'], font=FS); d.text(((W - tw) / 2, y + 16), m['text'], font=FS, fill=GRAY)
        else:
            lines, bw, bh, extra = info
            if m['who'] == 'me':
                x1 = W - 50; x0 = x1 - bw; col = RED if m.get('hl') else BLUE; tc = (255, 255, 255)
            else:
                if extra: d.text((60, y), m['name'], font=FN, fill=(90, 90, 100))
                x0 = 50; x1 = x0 + bw; col = RED if m.get('hl') else GRAYB; tc = (255, 255, 255) if m.get('hl') else TXT
            by = y + extra
            d.rounded_rectangle([x0, by, x1, by + bh], 44, fill=col)
            ty = by + 14
            for l in lines: d.text((x0 + PAD, ty), l, font=FM, fill=tc); ty += LH
            last_me = by + bh if m['who'] == 'me' else None
        y += h
    if typing:
        d.rounded_rectangle([50, y, 210, y + 90], 44, fill=GRAYB)
        for i in range(3): d.ellipse([86 + i * 34, y + 36, 104 + i * 34, y + 54], fill=(150, 150, 158))
    elif last_me is not None:
        t = '읽음'; d.text((W - 50 - d.textlength(t, font=FN), last_me + 6), t, font=FN, fill=GRAY)
    draw_hook(d, ep['hook']); draw_head(d, ep['room'])
    if end_text:
        im = Image.blend(im, Image.new('RGB', (W, H), (0, 0, 0)), 0.45); d = ImageDraw.Draw(im)
        lines = wrap(d, end_text, FE, W - 160)
        bh = len(lines) * 72 + 60; y0 = (H - bh) // 2 + 120
        d.rounded_rectangle([50, y0, W - 50, y0 + bh], 30, fill=(20, 20, 20))
        yy = y0 + 30
        for l in lines:
            tw = d.textlength(l, font=FE); d.text(((W - tw) / 2, yy), l, font=FE, fill=(255, 255, 255)); yy += 72
    return im

def main(epf, out):
    ep = json.load(open(epf, encoding='utf-8'))
    tmp = f"/tmp/hook_{ep['ep']}"; os.makedirs(tmp, exist_ok=True)
    states = [(0, False, None, 1.6)]
    for i, m in enumerate(ep['msgs']):
        if m['who'] == 'them': states.append((i, True, None, 0.7))
        hold = m.get('hold') or min(3.0, 1.0 + len(m['text']) * 0.055)
        states.append((i + 1, False, None, hold))
    if ep.get('end'): states.append((len(ep['msgs']), False, ep['end'], 3.0))
    else: states[-1] = states[-1][:3] + (states[-1][3] + 1.5,)
    lst = ''
    for k, (shown, typing, endt, dur) in enumerate(states):
        p = f'{tmp}/{k:03d}.png'; render_state(ep, shown, typing, endt).save(p)
        lst += f"file '{p}'\nduration {dur:.2f}\n"
    lst += f"file '{tmp}/{len(states)-1:03d}.png'\n"
    open(f'{tmp}/list.txt', 'w').write(lst)
    total = sum(s[3] for s in states)
    subprocess.run(['python3', os.path.join(HERE, 'bgm2.py'), f'{tmp}/bgm.wav', str(total + 1), str(ep.get('seed', ep['ep'])), 'hook'], check=True)
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'concat', '-safe', '0', '-i', f'{tmp}/list.txt', '-i', f'{tmp}/bgm.wav',
        '-vf', 'fps=30,format=yuv420p', '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '21', '-c:a', 'aac', '-b:a', '160k',
        '-af', f'afade=t=out:st={max(0,total-1.5):.2f}:d=1.5', '-t', f'{total:.2f}', '-movflags', '+faststart', out], check=True)
    print(out, round(total, 1), 's')

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
