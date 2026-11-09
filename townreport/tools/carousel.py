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
    prefix = f"build/ep{sp['ep']:02d}_wide"
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
            d.rounded_rectangle((x + 28, y - 30, x + 28 + tw + 36, y + 28), 16, fill=INK)
            d.text((x + 46, y - 26), p['name'], font=f, fill=PAPER)
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

def main():
    sp = json.load(open(sys.argv[1])); od = sys.argv[2]; os.makedirs(od, exist_ok=True)
    n = len(sp['subjects']) + 3
    slides = [cover(sp, n)] + [subject(sp, i, n) for i in range(len(sp['subjects']))] + [minus(sp, n), report(sp, n)]
    for k, s in enumerate(slides, 1): s.convert('RGB').save(f"{od}/{k:02d}.jpg", quality=92)
    print('slides', len(slides))

if __name__ == '__main__': main()
