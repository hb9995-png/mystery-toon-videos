"""동네성적표 캐러셀(사진) 렌더러: python3 carousel.py episodes/xxx.json out/폴더"""
import json, sys, os
from PIL import Image, ImageDraw, ImageFilter, ImageEnhance
sys.path.insert(0, os.path.dirname(__file__))
import basemap
from render import F, FB, FBo, FM, PAPER, INK, RED, MUTED, LINE, stamp, text_c

W, H = 1080, 1350
CARD = (255, 253, 248)

def base(sp, page, total):
    im = Image.new('RGBA', (W, H), PAPER + (255,)); d = ImageDraw.Draw(im)
    tag = f"{sp['brand']}  ·  EP.{sp['ep']:02d}"
    d.rounded_rectangle((56, 44, 56 + d.textlength(tag, font=F(FBo, 30)) + 40, 96), 26, fill=INK)
    d.text((76, 47), tag, font=F(FBo, 30), fill=PAPER)
    pg = f"{page} / {total}"
    d.text((W - 56 - d.textlength(pg, font=F(FM, 30)), 52), pg, font=F(FM, 30), fill=MUTED)
    text_c(d, W / 2, H - 52, '지도 © OpenStreetMap contributors  ·  정보 제공 목적, 투자 권유 아님', F(FM, 22), MUTED)
    return im, d

def map_img(sp, w, h, pins=True, focus=False):
    prefix = f"build/ep{sp['ep']:02d}_wide" if 'mapkey' not in sp else f"build/m_{sp['mapkey']}_wide"
    if not os.path.exists(prefix + '_raw.png'):
        basemap.build(sp['adm_nm'], prefix, W=2600, H=2600)
    m = Image.open(prefix + '_raw.png').convert('RGBA'); geo = json.load(open(prefix + '_geo.json'))
    m = ImageEnhance.Color(m.convert('RGB')).enhance(0.85).convert('RGBA')
    mask = Image.new('L', m.size, 0); md = ImageDraw.Draw(mask)
    for r in geo['rings']: md.polygon([tuple(p) for p in r], fill=255)
    dim = Image.new('RGBA', m.size, (31, 42, 68, 55)); out = Image.new('RGBA', m.size, (0, 0, 0, 0))
    out.paste(dim, (0, 0), mask.point(lambda v: 255 - v)); m.alpha_composite(out)
    fill = Image.new('RGBA', m.size, (0, 0, 0, 0)); fill.paste(Image.new('RGBA', m.size, RED + (30,)), (0, 0), mask); m.alpha_composite(fill)
    d = ImageDraw.Draw(m)
    for r in geo['rings']: d.line([tuple(p) for p in r] + [tuple(r[0])], fill=RED, width=9, joint='curve')
    # crop to target aspect around polygon center
    xs = [p[0] for r in geo['rings'] for p in r]; ys = [p[1] for r in geo['rings'] for p in r]
    cx, cy = (min(xs) + max(xs)) / 2, (min(ys) + max(ys)) / 2
    if focus and sp.get('pins'):
        px, py = basemap.ll2px(sp['pins'][0]['lon'], sp['pins'][0]['lat'], geo['z'])
        cx, cy = (cx + px - geo['L']) / 2, (cy + py - geo['T']) / 2
    sc = max(w / m.width, h / m.height)
    if (max(ys) - min(ys)) * sc > h * 0.92: sc = h * 0.92 / (max(ys) - min(ys))
    if (max(xs) - min(xs)) * sc > w * 0.92: sc = min(sc, w * 0.92 / (max(xs) - min(xs)))
    sc = max(sc, w / m.width, h / m.height)
    mm = m.resize((int(m.width * sc), int(m.height * sc)), Image.LANCZOS)
    l = int(min(max(cx * sc - w / 2, 0), mm.width - w)); t = int(min(max(cy * sc - h / 2, 0), mm.height - h))
    m = mm.crop((l, t, l + w, t + h)); d = ImageDraw.Draw(m)
    if pins:
        for p in sp.get('pins', []):
            x, y = basemap.ll2px(p['lon'], p['lat'], geo['z']); x = (x - geo['L']) * sc - l; y = (y - geo['T']) * sc - t
            d.ellipse((x - 20, y - 20, x + 20, y + 20), fill=(255, 255, 255)); d.ellipse((x - 13, y - 13, x + 13, y + 13), fill=INK)
            f = F(FBo, 34); tw = d.textlength(p['name'], font=f)
            bx = x + 28 if not p.get('left') else x - 28 - tw - 36
            d.rounded_rectangle((bx, y - 30, bx + tw + 36, y + 28), 16, fill=INK)
            d.text((bx + 18, y - 26), p['name'], font=f, fill=PAPER)
    return m

def rounded(im, r):
    m = Image.new('L', im.size, 0); ImageDraw.Draw(m).rounded_rectangle((0, 0, im.width, im.height), r, fill=255)
    o = Image.new('RGBA', im.size, (0, 0, 0, 0)); o.paste(im, (0, 0), m); return o

def shadow_card(im, box, r=36, outline=LINE, ow=2):
    x0, y0, x1, y1 = box
    sh = Image.new('RGBA', im.size, (0, 0, 0, 0)); ImageDraw.Draw(sh).rounded_rectangle((x0, y0 + 10, x1, y1 + 10), r, fill=(0, 0, 0, 45))
    im.alpha_composite(sh.filter(ImageFilter.GaussianBlur(14)))
    ImageDraw.Draw(im).rounded_rectangle(box, r, fill=CARD, outline=outline, width=ow)

def cover(sp, n):
    im, d = base(sp, 1, n)
    d.text((56, 118), sp['title'], font=F(FB, 104), fill=INK)
    d.text((60, 250), sp['sido'], font=F(FM, 34), fill=MUTED)
    mp = rounded(map_img(sp, 968, 820), 32)
    im.alpha_composite(mp, (56, 316))
    shadow_card(im, (56, 1000, 1024, 1250), r=32, outline=INK, ow=3); d = ImageDraw.Draw(im)
    for k, ln in enumerate(sp['hook']): d.text((100, 1036 + k * 74), ln, font=F(FB, 54), fill=INK)
    d.text((100, 1190), '넘겨서 과목별 점수 확인 →', font=F(FBo, 30), fill=RED)
    st = stamp('?', 190); im.alpha_composite(st, (1024 - 230, 1030))
    return im

def subject(sp, i, n):
    sub = sp['subjects'][i]; im, d = base(sp, i + 2, n)
    d.text((56, 124), f"{i + 1}교시", font=F(FBo, 36), fill=RED)
    d.text((56, 166), sub['name'], font=F(FB, 120), fill=INK)
    st = stamp(sub['grade'], 300); im.alpha_composite(st, (W - 56 - 300, 96))
    mp = rounded(map_img(sp, 968, 470, focus=True), 28); im.alpha_composite(mp, (56, 350))
    shadow_card(im, (56, 860, 1024, 1250)); d = ImageDraw.Draw(im)
    for j, ln in enumerate(sub['lines']):
        y = 900 + j * 76
        d.ellipse((96, y + 20, 112, y + 36), fill=RED if ln.startswith('단') or '아쉬움' in ln else INK)
        d.text((136, y), ln, font=F(FBo, 44), fill=INK)
    d.line((96, 1140, 984, 1140), fill=LINE, width=2)
    d.text((96, 1162), '한 줄 평  ' + sub['sub'], font=F(FBo, 36), fill=MUTED)
    return im

def minus(sp, n):
    im, d = base(sp, len(sp['subjects']) + 2, n)
    d.text((56, 124), '감점 요인', font=F(FB, 120), fill=RED)
    d.text((60, 290), '완벽한 동네는 없죠', font=F(FBo, 44), fill=MUTED)
    nm = len(sp['minus']); bottom = 400 + 80 + nm * 150
    shadow_card(im, (56, 400, 1024, bottom), outline=RED, ow=4); d = ImageDraw.Draw(im)
    mp = rounded(map_img(sp, 968, 1240 - bottom - 40), 28); im.alpha_composite(mp, (56, bottom + 40)); d = ImageDraw.Draw(im)
    for j, ln in enumerate(sp['minus']):
        y = 450 + j * 150
        d.text((106, y), f"0{j + 1}", font=F(FB, 64), fill=RED)
        d.text((230, y + 6), ln, font=F(FBo, 48), fill=INK)
        if j < len(sp['minus']) - 1: d.line((106, y + 115, 974, y + 115), fill=LINE, width=2)
    return im

def report(sp, n):
    im, d = base(sp, n, n)
    shadow_card(im, (56, 120, 1024, 1140), outline=INK, ow=4); d = ImageDraw.Draw(im)
    text_c(d, W / 2, 150, '성   적   표', F(FB, 72), INK)
    text_c(d, W / 2, 248, f"{sp['sido']} {sp['title']}", F(FBo, 34), MUTED)
    d.line((106, 310, 974, 310), fill=INK, width=3)
    for j, sub in enumerate(sp['subjects']):
        y = 326 + j * 108
        d.text((116, y + 16), sub['name'], font=F(FB, 54), fill=INK)
        d.text((290, y + 34), sub['sub'], font=F(FM, 30), fill=MUTED)
        mini = stamp(sub['grade'], 104); im.alpha_composite(mini, (974 - 104, y - 2)); d = ImageDraw.Draw(im)
        d.line((106, y + 104, 974, y + 104), fill=LINE, width=2)
    d.text((116, 900), '종합', font=F(FB, 72), fill=INK)
    for k, v in enumerate(sp['verdict']): d.text((118, 1000 + k * 50), v, font=F(FBo, 36), fill=MUTED)
    im.alpha_composite(stamp(sp['total'], 330), (974 - 330, 800))
    d = ImageDraw.Draw(im)
    d.rounded_rectangle((56, 1170, 1024, 1270), 30, fill=INK)
    text_c(d, W / 2, 1192, sp['cta'][0] + '  ·  댓글에 동네 이름!', F(FB, 42), PAPER)
    return im


# ---------- 랭킹형·비교형 (2026-11-23 사용자 요청: 랭킹·비교·논쟁형) ----------
def head(sp, page, total, label=None):
    """EP 번호 없는 머리줄(랭킹·비교형)."""
    im = Image.new('RGBA', (W, H), PAPER + (255,)); d = ImageDraw.Draw(im)
    if label:
        f = F(FBo, 30); d.rounded_rectangle((56, 44, 56 + d.textlength(label, font=f) + 40, 96), 26, fill=INK)
        d.text((76, 47), label, font=f, fill=PAPER)
    pg = f"{page} / {total}"
    d.text((W - 56 - d.textlength(pg, font=F(FM, 30)), 52), pg, font=F(FM, 30), fill=MUTED)
    text_c(d, W / 2, H - 52, sp.get('foot', '지도 © OpenStreetMap contributors  ·  정보 제공 목적, 투자 권유 아님'), F(FM, 22), MUTED)
    return im, d

def fit(d, s, path, size, maxw):
    while d.textlength(s, font=F(path, size)) > maxw and size > 20: size -= 2
    return F(path, size)

def qcover(sp, n):
    """첫 장: 질문 한 줄 큰 글씨 + 미리보기."""
    im, d = head(sp, 1, n)
    y = 300
    for k, ln in enumerate(sp['question']):
        f = fit(d, ln, FB, 150, 968); text_c(d, W / 2, y, ln, f, INK if k == 0 else RED); y += f.size + 60
    d.line((300, y + 30, 780, y + 30), fill=INK, width=6)
    for k, ln in enumerate(sp['teaser']):
        text_c(d, W / 2, y + 80 + k * 70, ln, F(FBo, 48), MUTED)
    shadow_card(im, (190, 1080, 890, 1200), r=60, outline=INK, ow=3); d = ImageDraw.Draw(im)
    text_c(d, W / 2, 1100, sp['cover_cta'], F(FB, 52), RED)
    return im

def criteria(sp, n):
    im, d = head(sp, 2, n, '기준')
    d.text((56, 130), sp['crit_title'], font=fit(d, sp['crit_title'], FB, 100, 968), fill=INK)
    hh = sum(92 if l.startswith('#') else 82 for l in sp['crit_lines'])
    shadow_card(im, (56, 330, 1024, 330 + hh + 100), outline=INK, ow=3); d = ImageDraw.Draw(im)
    y = 380
    for ln in sp['crit_lines']:
        if ln.startswith('#'):
            d.text((100, y), ln[1:], font=F(FB, 54), fill=RED); y += 92
        else:
            d.ellipse((104, y + 22, 120, y + 38), fill=INK)
            d.text((144, y), ln, font=fit(d, ln, FBo, 44, 840), fill=INK); y += 82
    y = 330 + hh + 180
    for k, ln in enumerate(sp.get('crit_extra', [])):
        text_c(d, W / 2, y + k * 120, ln, fit(d, ln, FB, 88, 968), RED if k else INK)
    return im

def rank_slide(sp, it, page, n):
    im, d = head(sp, page, n, sp['tag'])
    d.text((56, 120), f"{it['rank']}위", font=F(FB, 170), fill=RED)
    x = 56 + d.textlength(f"{it['rank']}위", font=F(FB, 170)) + 36
    d.text((x, 150), it['city'], font=F(FBo, 44), fill=MUTED)
    d.text((x, 200), it['name'], font=fit(d, it['name'], FB, 92, 1024 - x), fill=INK)
    m = {'ep': sp['ep'], 'adm_nm': it['adm_nm'], 'mapkey': it['key'], 'pins': it.get('pins', [])}
    mp = rounded(map_img(m, 968, 640), 28); im.alpha_composite(mp, (56, 360))
    shadow_card(im, (56, 1030, 1024, 1250)); d = ImageDraw.Draw(im)
    d.text((96, 1050), it['stat_label'], font=F(FBo, 36), fill=MUTED)
    d.text((96, 1100), it['stat'], font=F(FB, 96), fill=INK)
    if it.get('note'):
        f = F(FBo, 40); tw = d.textlength(it['note'], font=f)
        d.rounded_rectangle((984 - tw - 40, 1140, 984, 1210), 30, fill=RED)
        d.text((984 - tw - 20, 1146), it['note'], font=f, fill=PAPER)
    if it['rank'] == 1:
        im.alpha_composite(stamp('1위', 240), (W - 56 - 240, 100))
    return im

def rank_summary(sp, n):
    im, d = head(sp, n, n, sp['tag'])
    d.text((56, 120), sp['sum_title'], font=fit(d, sp['sum_title'], FB, 96, 968), fill=INK)
    shadow_card(im, (56, 290, 1024, 1000), outline=INK, ow=4); d = ImageDraw.Draw(im)
    for j, it in enumerate(sorted(sp['items'], key=lambda x: x['rank'])):
        y = 320 + j * 134
        d.text((100, y + 10), f"{it['rank']}", font=F(FB, 80), fill=RED if it['rank'] == 1 else INK)
        d.text((200, y + 14), it['name'], font=F(FB, 56), fill=INK)
        d.text((200, y + 86), it['city'], font=F(FM, 28), fill=MUTED)
        tw = d.textlength(it['stat'], font=F(FBo, 48)); d.text((984 - tw, y + 30), it['stat'], font=F(FBo, 48), fill=INK)
        if j < 4: d.line((100, y + 128, 984, y + 128), fill=LINE, width=2)
    for k, ln in enumerate(sp['sum_note']): d.text((60, 1030 + k * 46), ln, font=F(FM, 32), fill=MUTED)
    d.rounded_rectangle((56, 1150, 1024, 1250), 30, fill=INK)
    text_c(d, W / 2, 1170, sp['cta'], fit(d, sp['cta'], FB, 46, 900), PAPER)
    return im

def vs_intro(sp, n):
    im, d = head(sp, 2, n, 'VS')
    A, B = sp['sides']
    for k, side in enumerate((A, B)):
        x0 = 56 + k * 500
        m = {'ep': sp['ep'], 'adm_nm': side['adm_nm'], 'mapkey': side['key'], 'pins': side.get('pins', [])}
        mp = rounded(map_img(m, 468, 760), 28); im.alpha_composite(mp, (x0, 330)); d = ImageDraw.Draw(im)
        col = side['color']
        text_c(d, x0 + 234 + (-40 if k == 0 else 40), 130, side['name'], fit(d, side['name'], FB, 110, 360), col)
        text_c(d, x0 + 234, 265, side['area'], fit(d, side['area'], FBo, 34, 460), MUTED)
        for j, ln in enumerate(side['intro']):
            text_c(d, x0 + 234, 1110 + j * 56, ln, fit(d, ln, FBo, 38, 460), INK)
    st = Image.new('RGBA', (150, 150), (0, 0, 0, 0)); sd = ImageDraw.Draw(st)
    sd.ellipse((0, 0, 149, 149), fill=INK); text_c(sd, 75, 34, 'VS', F(FB, 64), PAPER)
    im.alpha_composite(st, (W // 2 - 75, 150))
    return im

def vs_round(sp, r, k, page, n):
    im, d = head(sp, page, n, f"{k}라운드")
    d.text((56, 120), r['title'], font=fit(d, r['title'], FB, 120, 968), fill=INK)
    d.text((60, 280), '기준: ' + r['crit'], font=fit(d, '기준: ' + r['crit'], FBo, 36, 960), fill=MUTED)
    A, B = sp['sides']
    for j, side in enumerate((A, B)):
        x0 = 56 + j * 500; win = r['win'] == j
        shadow_card(im, (x0, 360, x0 + 468, 1060), outline=side['color'] if win else LINE, ow=8 if win else 2); d = ImageDraw.Draw(im)
        text_c(d, x0 + 234, 395, side['name'], F(FB, 64), side['color'])
        d.line((x0 + 40, 490, x0 + 428, 490), fill=LINE, width=2)
        text_c(d, x0 + 234, 520, r['vals'][j][0], fit(d, r['vals'][j][0], FB, 84, 420), INK)
        for q, ln in enumerate(r['vals'][j][1:]):
            text_c(d, x0 + 234, 660 + q * 60, ln, fit(d, ln, FBo, 38, 420), MUTED)
        if win: im.alpha_composite(stamp('승', 200), (x0 + 134, 850))
    d = ImageDraw.Draw(im)
    res = r.get('result') or (f"{sp['sides'][r['win']]['name']} 승" if r['win'] in (0, 1) else '무승부')
    d.rounded_rectangle((56, 1100, 1024, 1240), 36, fill=INK)
    text_c(d, W / 2, 1118, res, fit(d, res, FB, 64, 900), PAPER)
    return im

def vs_score(sp, n):
    im, d = head(sp, n - 1, n, '최종 결과')
    A, B = sp['sides']
    wa = sum(1 for r in sp['rounds'] if r['win'] == 0); wb = sum(1 for r in sp['rounds'] if r['win'] == 1)
    text_c(d, W / 2, 130, '최종 스코어', F(FB, 90), INK)
    text_c(d, 290, 280, A['name'], F(FB, 80), A['color']); text_c(d, 790, 280, B['name'], F(FB, 80), B['color'])
    text_c(d, 290, 380, str(wa), F(FB, 260), A['color']); text_c(d, 790, 380, str(wb), F(FB, 260), B['color'])
    shadow_card(im, (56, 720, 1024, 1240), outline=INK, ow=3); d = ImageDraw.Draw(im)
    for j, r in enumerate(sp['rounds']):
        y = 750 + j * 92
        d.text((100, y), r['title'], font=F(FBo, 44), fill=INK)
        res = A['name'] if r['win'] == 0 else B['name'] if r['win'] == 1 else '무'
        col = A['color'] if r['win'] == 0 else B['color'] if r['win'] == 1 else MUTED
        tw = d.textlength(res, font=F(FB, 48)); d.text((984 - tw, y - 2), res, font=F(FB, 48), fill=col)
    d = ImageDraw.Draw(im)
    win = A if wa > wb else B if wb > wa else None
    im.alpha_composite(stamp(win.get('stamp', win['name'][:2]) if win else '무', 230), (W // 2 - 115, 470))
    return im

def vs_end(sp, n):
    im, d = head(sp, n, n, '결론')
    y = 150
    for ln in sp['verdict']:
        d.text((56, y), ln, font=fit(d, ln, FB, 76, 968), fill=INK); y += 110
    shadow_card(im, (56, y + 30, 1024, y + 30 + 70 * len(sp['notes']) + 60)); d = ImageDraw.Draw(im)
    for k, ln in enumerate(sp['notes']):
        d.text((96, y + 60 + k * 70), ln, font=fit(d, ln, FBo, 36, 880), fill=MUTED)
    d.rounded_rectangle((56, 1110, 1024, 1240), 36, fill=RED)
    text_c(d, W / 2, 1135, sp['cta'], fit(d, sp['cta'], FB, 52, 900), PAPER)
    return im

def build_rank(sp):
    items = sorted(sp['items'], key=lambda x: -x['rank']); n = 3 + len(items)
    return [qcover(sp, n), criteria(sp, n)] + [rank_slide(sp, it, 3 + k, n) for k, it in enumerate(items)] + [rank_summary(sp, n)]

def build_vs(sp):
    for sd in sp['sides']: sd['color'] = tuple(sd['color'])
    n = 4 + len(sp['rounds'])
    return [qcover(sp, n), vs_intro(sp, n)] + [vs_round(sp, r, k + 1, 3 + k, n) for k, r in enumerate(sp['rounds'])] + [vs_score(sp, n), vs_end(sp, n)]

def main():
    sp = json.load(open(sys.argv[1])); od = sys.argv[2]; os.makedirs(od, exist_ok=True)
    if sp.get('type') == 'rank': slides = build_rank(sp)
    elif sp.get('type') == 'vs': slides = build_vs(sp)
    else:
      n = len(sp['subjects']) + 3
      slides = [cover(sp, n)] + [subject(sp, i, n) for i in range(len(sp['subjects']))] + [minus(sp, n), report(sp, n)]
    for k, s in enumerate(slides, 1): s.convert('RGB').save(f"{od}/{k:02d}.jpg", quality=92)
    print('slides', len(slides))

if __name__ == '__main__': main()
