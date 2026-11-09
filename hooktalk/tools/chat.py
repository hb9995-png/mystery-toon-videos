"""톡잘못보냄(hook.talk) 메신저 대화 썰 릴스 렌더러
python3 chat.py episode.json out.mp4
episode.json:
{"ep":1, "hook":"첫 2초 훅 문장(상단 띠, 2줄 이내)", "room":"대화방 이름", "seed":1,
 "msgs":[{"who":"me"|"them"|"sys", "text":"...", "name":"(them 일 때 선택, 단톡방용)", "hold":초(선택)}, ...],
 "end":"마지막 자막 한 줄(선택)"}
- me: 오른쪽 민트 말풍선, them: 왼쪽 흰 말풍선, sys: 가운데 회색 안내(예: "메시지를 삭제했습니다", "오후 11:42")
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
TOP = 330            # 훅 띠 높이
HEAD = 130           # 대화방 머리줄
BG = (198, 214, 228); MINT = (164, 232, 196); WHITE = (255, 255, 255)
TXT = (25, 25, 25); GRAY = (110, 120, 130)
FM = f(FR, 44); FN = f(FR, 30); FS = f(FR, 30); FH = f(FK, 70); FT = f(FB, 42); FE = f(FB, 52)
MAXW = 640

def wrap(d, text, font, maxw):
    lines = []
    for para in text.split('\n'):
        cur = ''
        for ch in para:
            if d.textlength(cur + ch, font=font) > maxw and cur:
                lines.append(cur); cur = ch
            else: cur += ch
        lines.append(cur)
    return lines

def bubble_size(d, m):
    if m['who'] == 'sys':
        return 70, None
    lines = wrap(d, m['text'], FM, MAXW)
    w = max(d.textlength(l, font=FM) for l in lines) + 56
    h = len(lines) * 60 + 36
    extra = 40 if (m['who'] == 'them' and m.get('name')) else 0
    return h + extra + 22, (lines, w, h, extra)

def draw_hook(d, hook):
    d.rectangle([0, 0, W, TOP], fill=(12, 12, 14))
    lines = wrap(d, hook, FH, W - 120)[:3]
    y = (TOP - len(lines) * 92) // 2 + 6
    for l in lines:
        tw = d.textlength(l, font=FH); x = (W - tw) / 2
        d.text((x + 3, y + 3), l, font=FH, fill=(0, 0, 0))
        d.text((x, y), l, font=FH, fill=(255, 226, 92)); y += 92

def draw_head(d, room):
    y0 = TOP
    d.rectangle([0, y0, W, y0 + HEAD], fill=(186, 203, 219))
    d.line([(46, y0 + 65), (70, y0 + 42)], fill=TXT, width=6); d.line([(46, y0 + 65), (70, y0 + 88)], fill=TXT, width=6)
    tw = d.textlength(room, font=FT); d.text(((W - tw) / 2, y0 + 38), room, font=FT, fill=TXT)
    for i in range(3): d.ellipse([W - 80, y0 + 40 + i * 20, W - 68, y0 + 52 + i * 20], fill=TXT)

def render_state(ep, shown, typing, end_text=None):
    im = Image.new('RGB', (W, H), BG); d = ImageDraw.Draw(im)
    msgs = ep['msgs'][:shown]
    sizes = [bubble_size(d, m) for m in msgs]
    total = sum(s[0] for s in sizes) + (110 if typing else 0)
    area_top = TOP + HEAD + 20; area_bot = H - 170
    y = max(area_top, area_bot - total) if total > area_bot - area_top else area_top
    if total > area_bot - area_top: y = area_bot - total
    for m, (h, info) in zip(msgs, sizes):
        if y + h < area_top - 200: y += h; continue
        if m['who'] == 'sys':
            tw = d.textlength(m['text'], font=FS); x = (W - tw) / 2
            d.rounded_rectangle([x - 24, y + 8, x + tw + 24, y + 56], 24, fill=(172, 188, 204))
            d.text((x, y + 13), m['text'], font=FS, fill=(70, 80, 90))
        else:
            lines, bw, bh, extra = info
            if m['who'] == 'me':
                x1 = W - 40; x0 = x1 - bw; col = MINT
            else:
                d.rounded_rectangle([34, y, 114, y + 80], 30, fill=(150, 170, 190))
                d.ellipse([56, y + 14, 92, y + 50], fill=(230, 236, 242)); d.pieslice([46, y + 46, 102, y + 100], 180, 360, fill=(230, 236, 242))
                if extra: d.text((134, y), m['name'], font=FN, fill=(60, 70, 80))
                x0 = 134; x1 = x0 + bw; col = WHITE
            by = y + extra
            d.rounded_rectangle([x0, by, x1, by + bh], 28, fill=col)
            ty = by + 18
            for l in lines: d.text((x0 + 28, ty), l, font=FM, fill=TXT); ty += 60
        y += h
    if typing:
        d.rounded_rectangle([34, y, 114, y + 80], 30, fill=(150, 170, 190))
        d.rounded_rectangle([134, y, 274, y + 84], 28, fill=WHITE)
        for i in range(3): d.ellipse([164 + i * 34, y + 34, 182 + i * 34, y + 52], fill=(150, 150, 150))
    # 화면 위를 가리는 겹침 정리: 훅 띠와 머리줄을 마지막에 다시 그린다
    draw_hook(d, ep['hook']); draw_head(d, ep['room'])
    d.rectangle([0, H - 150, W, H], fill=(236, 240, 244))
    d.rounded_rectangle([40, H - 125, W - 160, H - 45], 40, fill=WHITE)
    d.text((80, H - 108), '메시지 입력', font=FN, fill=(170, 170, 170))
    d.ellipse([W - 135, H - 125, W - 55, H - 45], fill=MINT)
    if end_text:
        im = Image.blend(im, Image.new('RGB', (W, H), (0, 0, 0)), 0.45); d = ImageDraw.Draw(im)
        lines = wrap(d, end_text, FE, W - 160)
        bh = len(lines) * 72 + 60; y0 = (H - bh) // 2 + 120
        d.rounded_rectangle([50, y0, W - 50, y0 + bh], 30, fill=(12, 12, 14))
        yy = y0 + 30
        for l in lines:
            tw = d.textlength(l, font=FE); d.text(((W - tw) / 2, yy), l, font=FE, fill=WHITE); yy += 72
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
