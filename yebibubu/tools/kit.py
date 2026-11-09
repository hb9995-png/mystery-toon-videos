"""예비부부툰 공용 도구: SVG 도우미 + 렌더링. 에피소드 파일에서 from kit import * 로 쓴다."""
import sys, os, subprocess, html as H
TOOLS = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, TOOLS)
from dogs import *
INK = OL; ROSE = '#E06C7A'; BG = '#FFF3EA'
HEAD = f'''<!DOCTYPE html><html lang="ko"><head><meta charset="utf-8">
<style>@font-face{{font-family:'Gamja Flower';src:url(file://{TOOLS}/fonts/GamjaFlower.ttf)}} @font-face{{font-family:'Jua';src:url(file://{TOOLS}/fonts/Jua.ttf)}}
html,body{{margin:0;width:1080px;height:1350px;overflow:hidden}} .g{{font-family:'Gamja Flower'}} .j{{font-family:'Jua'}}</style></head><body>
<svg width="1080" height="1350" viewBox="0 0 1080 1350" xmlns="http://www.w3.org/2000/svg">'''

def T(x, y, lines, size, cls='g', fill=INK, anchor='middle', lh=1.32):
    if isinstance(lines, str): lines = lines.split('\n')
    return ''.join(f'<text class="{cls}" x="{x}" y="{y + i * size * lh}" font-size="{size}" fill="{fill}" text-anchor="{anchor}">{H.escape(l)}</text>' for i, l in enumerate(lines))

def bubble(x, y, w, text, size=58, tail=None, fill='#fff'):
    lines = text.split('\n'); h = len(lines) * size * 1.32 + 44
    s = f'<g stroke="{INK}" stroke-width="5" stroke-linejoin="round">'
    if tail:
        tx, ty = tail; bx = min(max(tx, x + 60), x + w - 60); by = y + h if ty > y + h else y
        s += f'<path d="M{bx-24} {by} L {tx} {ty} L {bx+24} {by}" fill="{fill}"/>'
    s += f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{min(46, h/2)}" fill="{fill}"/>'
    if tail: s += f'<path d="M{bx-20} {by} H {bx+20}" stroke="{fill}" stroke-width="8"/>'
    s += '</g>'
    return s + T(x + w / 2, y + 22 + size * .95, lines, size)

def header(no, total=9):
    return T(80, 90, '예비부부툰', 52, 'j', ROSE, 'start') + T(1000, 90, f'{no}/{total}', 44, 'j', '#C9A9A9', 'end')

def panel(inner, bg, y0=130, y1=1060):
    cid = f'p{abs(hash(inner)) % 99999}'
    return (f'<clipPath id="{cid}"><rect x="70" y="{y0}" width="940" height="{y1-y0}" rx="48"/></clipPath>'
            f'<g clip-path="url(#{cid})"><rect x="70" y="{y0}" width="940" height="{y1-y0}" fill="{bg}"/>{inner}</g>'
            f'<rect x="70" y="{y0}" width="940" height="{y1-y0}" rx="48" fill="none" stroke="{INK}" stroke-width="6"/>')

def caption(text, y0=1100):
    lines = text.split('\n'); size = 60
    return (f'<rect x="70" y="{y0}" width="940" height="{1290-y0}" rx="48" fill="#fff" stroke="{INK}" stroke-width="6"/>'
            + T(540, (y0 + 1290) / 2 - (len(lines) - 1) * size * .66 + size * .35, lines, size))

def table(y, x0=40, x1=1040):
    s = f'<g stroke="{INK}" stroke-width="5" stroke-linejoin="round"><rect x="{x0}" y="{y}" width="{x1-x0}" height="400" rx="30" fill="#D7A877"/>'
    n = 5
    for i in range(n):
        cx = x0 + 120 + i * (x1 - x0 - 240) / (n - 1)
        s += f'<ellipse cx="{cx}" cy="{y+70}" rx="80" ry="34" fill="#fff"/><ellipse cx="{cx}" cy="{y+66}" rx="50" ry="18" fill="{["#F08A6A","#9CCB7E","#F2C66B"][i%3]}" stroke="none"/>'
    return s + '</g>'

def lattice(x, y, w, h):
    s = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="#FBF3E4" stroke="#C7A47A" stroke-width="8"/>'
    for i in range(1, 4): s += f'<path d="M{x + w * i / 4} {y} V {y + h} M {x} {y + h * i / 4} H {x + w}" stroke="#D9BE96" stroke-width="5"/>'
    return s

def hearts(n, area, col='#FFD1D8', seed=1):
    import random; r = random.Random(seed); x0, y0, x1, y1 = area; s = ''
    for _ in range(n):
        x, y, k = r.uniform(x0, x1), r.uniform(y0, y1), r.uniform(.6, 1.3)
        s += f'<path transform="translate({x} {y}) scale({k})" d="M0 10 C -30 -16 -16 -36 0 -20 C 16 -36 30 -16 0 10 Z" fill="{col}"/>'
    return s

def sweat(x, y, s=1):
    return f'<path transform="translate({x} {y}) scale({s})" d="M0 -26 c 16 24 16 40 0 44 c -16 -4 -16 -20 0 -44 z" fill="#A9DEFF" stroke="{INK}" stroke-width="4"/>'

def speed(cx, cy, col, n=44, r0=300):
    import math; s = ''
    for i in range(n):
        a = i / n * 2 * math.pi
        s += f'<path d="M{cx + math.cos(a) * r0} {cy + math.sin(a) * r0} L {cx + math.cos(a + .04) * 1400} {cy + math.sin(a + .04) * 1400} L {cx + math.cos(a - .04) * 1400} {cy + math.sin(a - .04) * 1400} Z" fill="{col}"/>'
    return s


def render(pages, out_dir):
    """pages: {번호: svg 본문}. out_dir 에 01.png.. 와 01.jpg.. 를 만든다."""
    from PIL import Image
    os.makedirs(out_dir, exist_ok=True)
    for no, body_ in sorted(pages.items()):
        p = os.path.join(out_dir, f'{no:02d}')
        open(p + '.html', 'w').write(HEAD + body_ + '</svg></body></html>')
        subprocess.run(['google-chrome', '--headless=new', '--no-sandbox', '--disable-gpu', '--hide-scrollbars',
                        '--force-device-scale-factor=1', '--window-size=1080,1350', '--virtual-time-budget=3000',
                        f'--screenshot={p}.png', f'file://{p}.html'], check=True, capture_output=True)
        Image.open(p + '.png').convert('RGB').save(p + '.jpg', quality=92)
        os.remove(p + '.html')
    print('rendered', len(pages), 'pages ->', out_dir)
