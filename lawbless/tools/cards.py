"""법블레스유(law.bless.you) 생활법률 카드뉴스 릴스 렌더러
python3 cards.py episode.json out.mp4
episode.json:
{"ep":1, "seed":11, "tag":"알바", "cover":{"q":"표지 질문(훅, 2~3줄)", "sub":"작은 부제"},
 "cards":[{"title":"소제목", "body":["짧은 문장", "..."], "law":"근거: 법 조문(선택)"}, ... 4~6장],
 "summary":["한 줄 정리", ...]}
- 1080x1920 세로, 장마다 정해진 시간 노출, 음성 없음, 오리지널 배경음악(bgm2.py law)
- 마지막 장에 '일반 정보이며 법률 자문이 아님 + 대한법률구조공단 132' 안내가 자동으로 들어간다

[사연 → 판결 형식, 2026-11-24~] episode.json 에 "pages" 가 있으면 이 형식으로 그린다.
{"ep":32, "seed":352, "tag":"중고거래", "pages":[
  {"type":"chat", "head":"첫 장 큰 글씨(15자 안팎 한 줄)", "who":"대화 상대 이름", "app":"문자|채팅",
   "msgs":[{"from":"them","text":"상대가 한 말"}, {"from":"me","text":"내가 한 말"}], "note":"(선택) 상황 설명 한 줄", "dur":3.0},
  {"type":"question", "q":"이거 법적으로\n누가 이길까?", "a":"보기 A", "b":"보기 B"},
  {"type":"verdict", "title":"판결 소제목", "body":["..."], "law":"근거 조문"},
  {"type":"todo", "title":"이럴 땐 이렇게", "items":["할 일 1", "할 일 2", "할 일 3"]},
  {"type":"cta", "lines":["한 줄 결론", "..."]}]}
- dur 를 안 쓰면 글 양에 따라 3~5초. 첫 장은 최소 2.8초.
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
    g.text((70, 0), c.get('label', f'{page:02d}'), font=f(FK, 64), fill=GOLD)
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

CHATBG = (186, 206, 224); ME = (255, 236, 130); THEM = (255, 255, 255)

def bubble(d, x_right, y, text, mine, font, maxw=640):
    ls = wrap(d, text, font, maxw); lh = int(font.size * 1.32)
    tw = max(d.textlength(l, font=font) for l in ls); bw = tw + 72; bh = len(ls) * lh + 48
    x0 = x_right - bw if mine else 150
    d.rounded_rectangle([x0, y, x0 + bw, y + bh], 34, fill=ME if mine else THEM)
    yy = y + 20
    for l in ls: d.text((x0 + 32, yy), l, font=font, fill=INK); yy += lh
    return y + bh

def chat_page(ep, p, page, total):
    im = Image.new('RGB', (W, H), CHATBG); d = ImageDraw.Draw(im)
    # 큰 글씨 한 줄(첫 장 훅)
    d.rectangle([0, 0, W, 330], fill=(20, 22, 30))
    hf = f(FK, 84)
    while d.textlength(p['head'], font=hf) > W - 100 and hf.size > 56: hf = f(FK, hf.size - 4)
    hw = d.textlength(p['head'], font=hf); d.text(((W - hw) / 2, 165 - hf.size * 0.62), p['head'], font=hf, fill=(255, 255, 255))
    # 메신저 상단 바
    d.rectangle([0, 330, W, 450], fill=(160, 184, 206))
    d.text((50, 352), '‹', font=f(FB, 64), fill=INK)
    d.text((110, 362), p['who'], font=f(FB, 50), fill=INK)
    app = p.get('app', '채팅'); aw = d.textlength(app, font=f(FR, 34)); d.text((W - 60 - aw, 374), app, font=f(FR, 34), fill=(70, 80, 95))
    lay = Image.new('RGB', (W, 1500), CHATBG); g = ImageDraw.Draw(lay)
    y = 0; mf = f(FR, 60)
    if p.get('note'):
        nf = f(FB, 46); nl = wrap(g, p['note'], nf, W - 220); nh = len(nl) * 64 + 44
        g.rounded_rectangle([70, y, W - 70, y + nh], 30, fill=(110, 130, 155)); yy = y + 22
        for l in nl: tw = g.textlength(l, font=nf); g.text(((W - tw) / 2, yy), l, font=nf, fill=(255, 255, 255)); yy += 64
        y += nh + 56
    prev = None
    for m in p['msgs']:
        mine = m['from'] == 'me'
        if not mine and prev != 'them':
            g.ellipse([40, y, 130, y + 90], fill=(140, 150, 165))
            g.text((150, y - 4), p['who'], font=f(FR, 38), fill=(60, 70, 85)); y += 54
        y = bubble(g, W - 50, y, m['text'], mine, mf, 680) + 34; prev = m['from']
    top = 450 + max(70, (H - 120 - 450 - y) // 2 - 60)
    im.paste(lay.crop((0, 0, W, y)), (0, top))
    d.text((60, H - 90), '법블레스유', font=f(FB, 34), fill=(90, 104, 125))
    for i in range(total):
        x = W / 2 - (total - 1) * 22 + i * 44
        d.ellipse([x - 9, H - 69, x + 9, H - 51], fill=NAVY if i == page else (140, 156, 178))
    return im, y

def question_page(ep, p, page, total):
    im = Image.new('RGB', (W, H), NAVY); d = ImageDraw.Draw(im)
    y = 520
    for l in p['q'].split('\n'):
        tw = d.textlength(l, font=f(FK, 110)); d.text(((W - tw) / 2, y), l, font=f(FK, 110), fill=GOLD); y += 150
    y += 80
    for k, key in enumerate(['a', 'b']):
        d.rounded_rectangle([110, y, W - 110, y + 130], 30, fill=(40, 56, 92))
        d.text((150, y + 30), 'AB'[k], font=f(FK, 60), fill=GOLD)
        d.text((240, y + 34), p[key], font=f(FB, 54), fill=CREAM); y += 170
    t = '댓글로 먼저 골라 보세요 ↓'; tw = d.textlength(t, font=f(FB, 46)); d.text(((W - tw) / 2, y + 60), t, font=f(FB, 46), fill=(200, 208, 225))
    for i in range(total):
        x = W / 2 - (total - 1) * 22 + i * 44
        d.ellipse([x - 9, H - 69, x + 9, H - 51], fill=GOLD if i == page else (80, 92, 120))
    return im

def cta_page(ep, p, page, total):
    im, d = frame(page, total, ep['tag'])
    d.text((70, 300), '정리하면', font=f(FK, 80), fill=INK)
    y = 450
    for i, s in enumerate(p['lines']):
        d.rounded_rectangle([70, y, 150, y + 80], 18, fill=NAVY); d.text((96, y + 6), str(i + 1), font=f(FK, 56), fill=GOLD)
        for l in wrap(d, s, f(FB, 52), W - 260): d.text((180, y + 6), l, font=f(FB, 52), fill=INK); y += 76
        y += 50
    y = max(y + 30, 1150)
    d.text((70, y), '당신이라면 어떻게 하겠어요? 댓글로', font=f(FB, 46), fill=NAVY); y += 90
    d.text((70, y), '비슷한 일 겪는 친구에게 보내 주세요', font=f(FB, 42), fill=NAVY); y += 110
    d.text((70, y), '※ 이해를 돕기 위한 가상 사례입니다.', font=f(FR, 34), fill=MUTE); y += 54
    for l in wrap(d, DISC, f(FR, 34), W - 140): d.text((70, y), l, font=f(FR, 34), fill=MUTE); y += 50
    return im

def story(ep, tmp):
    P = ep['pages']; total = len(P); pages = []
    for i, p in enumerate(P):
        t = p['type']
        if t == 'chat':
            im, _ = chat_page(ep, p, i, total)
            chars = len(p.get('note', '')) + sum(len(m['text']) for m in p['msgs'])
        elif t == 'question':
            im = question_page(ep, p, i, total); chars = 0
        elif t in ('verdict', 'todo'):
            c = {'title': p['title'], 'body': p.get('body') or p['items'], 'law': p.get('law', ''), 'label': p.get('label', '판결' if t == 'verdict' else '이렇게')}
            im, _ = card(ep, c, i, total)
            chars = len(c['title']) + sum(len(b) for b in c['body']) + len(c['law'])
        else:
            im = cta_page(ep, p, i, total); chars = sum(len(x) for x in p['lines']) + 40
        dur = p.get('dur') or min(5.0, max(3.0, 1.8 + chars * 0.03))
        if i == 0: dur = max(dur, 2.8)
        if t == 'question': dur = p.get('dur', 2.6)
        pages.append((im, dur))
    return pages

def main(epf, out):
    ep = json.load(open(epf, encoding='utf-8'))
    tmp = f"/tmp/law_{ep['ep']}"; os.makedirs(tmp, exist_ok=True)
    if 'pages' in ep:
        return render(ep, story(ep, tmp), tmp, out)
    total = len(ep['cards']) + 2
    pages = [(cover(ep, total), 3.2)]
    for i, c in enumerate(ep['cards']):
        im, _ = card(ep, c, i + 1, total)
        chars = len(c['title']) + sum(len(b) for b in c['body']) + len(c.get('law', ''))
        pages.append((im, min(6.5, max(3.8, 2.0 + chars * 0.035))))
    pages.append((summary(ep, total - 1, total), 5.5))
    return render(ep, pages, tmp, out)

def render(ep, pages, tmp, out):
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
