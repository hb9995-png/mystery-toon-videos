"""예비부부툰 강아지 캐릭터 (SVG 문자열)"""
import math
OL = '#3A2E2E'; LW = 6

def scallop(cx, cy, rx, ry, n, amp, start=0, end=360):
    pts = []
    for i in range(n + 1):
        a = math.radians(start + (end - start) * i / n)
        pts.append((cx + math.cos(a) * rx, cy + math.sin(a) * ry))
    d = f'M{pts[0][0]:.1f} {pts[0][1]:.1f} '
    for i in range(n):
        (x0, y0), (x1, y1) = pts[i], pts[i + 1]
        mx, my = (x0 + x1) / 2, (y0 + y1) / 2
        nx, ny = mx - cx, my - cy; L = math.hypot(nx, ny) or 1
        d += f'Q{mx + nx / L * amp:.1f} {my + ny / L * amp:.1f} {x1:.1f} {y1:.1f} '
    return d + 'Z'

def face(cx, cy, mood='happy', blush=True, gender=None):
    s = ''
    for k in (-1, 1):
        ex = cx + k * 40
        if mood == 'smug':
            s += f'<ellipse cx="{ex}" cy="{cy+4}" rx="14" ry="12" fill="{OL}"/><circle cx="{ex-4}" cy="{cy+2}" r="4" fill="#fff"/>'
            s += f'<path d="M{ex-20} {cy-6} H {ex+20}" stroke="{OL}" stroke-width="6" stroke-linecap="round"/>'
        elif mood == 'shock':
            s += f'<circle cx="{ex}" cy="{cy}" r="17" fill="#fff" stroke="{OL}" stroke-width="5"/><circle cx="{ex}" cy="{cy+2}" r="6" fill="{OL}"/>'
        elif mood == 'joy':
            s += f'<path d="M{ex-16} {cy+6} Q {ex} {cy-14} {ex+16} {cy+6}" stroke="{OL}" stroke-width="6" fill="none" stroke-linecap="round"/>'
        elif mood == 'blank':
            s += f'<circle cx="{ex}" cy="{cy}" r="7" fill="{OL}"/>'
        else:
            s += f'<ellipse cx="{ex}" cy="{cy}" rx="15" ry="18" fill="{OL}"/>'
            s += f'<ellipse cx="{ex}" cy="{cy+5}" rx="10" ry="10" fill="#6B4A3A" opacity=".55"/>'
            s += f'<circle cx="{ex-5}" cy="{cy-7}" r="6.5" fill="#fff"/><circle cx="{ex+6}" cy="{cy+7}" r="3" fill="#fff"/>'
    s += f'<ellipse cx="{cx}" cy="{cy+26}" rx="11" ry="7.5" fill="{OL}"/>'
    if mood in ('happy', 'joy', 'smug'):
        s += f'<path d="M{cx} {cy+33} v6 M{cx-14} {cy+40} q7 7 14 0 q7 7 14 0" stroke="{OL}" stroke-width="4" fill="none" stroke-linecap="round"/>'
    elif mood == 'shock':
        s += f'<ellipse cx="{cx}" cy="{cy+50}" rx="10" ry="13" fill="#7A3A3E" stroke="{OL}" stroke-width="4"/>'
    elif mood == 'blank':
        s += f'<path d="M{cx-10} {cy+44} H {cx+10}" stroke="{OL}" stroke-width="4" stroke-linecap="round"/>'
    else:  # nervous
        s += f'<path d="M{cx} {cy+33} v5 M{cx-12} {cy+46} q6 -7 12 0 q6 7 12 0" stroke="{OL}" stroke-width="4" fill="none" stroke-linecap="round"/>'
    if mood == 'nervous':
        s += f'<path d="M{cx-58} {cy-32} l 20 -8 M{cx+58} {cy-32} l -20 -8" stroke="{OL}" stroke-width="4" stroke-linecap="round"/>'
    if gender == 'f' and mood in ('happy', 'nervous', 'shock', 'smug', 'blank'):
        for k in (-1, 1):
            ex = cx + k * 40
            s += f'<path d="M{ex+k*13} {cy-12} l {k*12} -8 M {ex+k*17} {cy-2} l {k*14} -2" stroke="{OL}" stroke-width="3.5" stroke-linecap="round"/>'
    if gender == 'm' and mood != 'nervous':
        s += f'<path d="M{cx-58} {cy-34} q 18 -10 34 -2 M {cx+58} {cy-34} q -18 -10 -34 -2" stroke="{OL}" stroke-width="7" fill="none" stroke-linecap="round"/>'
    if mood in ('happy', 'joy'):
        s += f'<path d="M{cx-7} {cy+44} q 7 14 14 0 Z" fill="#FF8FA0" stroke="{OL}" stroke-width="2.5"/>'
    if blush:
        s += f'<ellipse cx="{cx-64}" cy="{cy+24}" rx="17" ry="10" fill="#FFA9B4" opacity=".85"/><ellipse cx="{cx+64}" cy="{cy+24}" rx="17" ry="10" fill="#FFA9B4" opacity=".85"/>'
        s += f'<circle cx="{cx-70}" cy="{cy+20}" r="3" fill="#fff" opacity=".9"/><circle cx="{cx+58}" cy="{cy+20}" r="3" fill="#fff" opacity=".9"/>'
    return s

def g(content, x, y, s):
    return f'<g transform="translate({x} {y}) scale({s})">{content}</g>'

def body(w, h, col, belly=None, legcol=None, arm_l=0, arm_r=0, under='', over='', armcol=None, paw=None):
    legcol = legcol or col; armcol = armcol or col
    s = f'<g stroke="{OL}" stroke-width="{LW}" stroke-linejoin="round" stroke-linecap="round">'
    for dx in (-w * .24, w * .24):
        s += f'<rect x="{dx - 29}" y="{h - 26}" width="58" height="52" rx="22" fill="{legcol}"/>'
    s += under
    s += f'<rect x="{-w / 2}" y="0" width="{w}" height="{h}" rx="{w * .32}" fill="{col}"/>'
    if belly: s += f'<ellipse cx="0" cy="{h * .55}" rx="{w * .26}" ry="{h * .3}" fill="{belly}" stroke="none"/>'
    s += over
    for sgn, ang in ((-1, arm_l), (1, arm_r)):
        ax = -w / 2 - 22 if sgn < 0 else w / 2 - 24
        s += f'<g transform="rotate({ang} {sgn*(w / 2 - 10)} 30)"><rect x="{ax}" y="20" width="46" height="{h * .55}" rx="23" fill="{armcol}"/>'
        if paw:
            s += f'<ellipse cx="{ax+23}" cy="{20 + h*.55 - 12}" rx="25" ry="20" fill="{paw}"/><path d="M{ax+15} {20 + h*.55 - 8} v -10 M {ax+31} {20 + h*.55 - 8} v -10" stroke-width="3"/>'
        s += '</g>'
    if paw:
        for dx in (-w * .24, w * .24):
            s += f'<path d="M{dx-29} {h+12} q 29 22 58 0 v 14 q -29 10 -58 0 Z" fill="{paw}" stroke-width="4"/><path d="M{dx-8} {h+18} v 8 M {dx+8} {h+18} v 8" stroke-width="3"/>'
    return s + '</g>'

def suit_body(arm_l=10, arm_r=-8, col='#3E4C7A', fur='#E9A35E'):
    over = (f'<path d="M-34 2 L 0 70 L 34 2 Z" fill="#fff"/>'
            f'<path d="M-30 14 L -4 26 L -30 38 Z M 30 14 L 4 26 L 30 38 Z" fill="#C94A5A"/><circle cx="0" cy="26" r="8" fill="#C94A5A"/>'
            f'<path d="M-34 2 L -52 60 L 0 110 M 34 2 L 52 60 L 0 110" fill="none" stroke-width="4"/>'
            f'<circle cx="0" cy="130" r="5" fill="#fff" stroke-width="3"/>')
    return body(180, 160, col, None, legcol='#2E3A60', arm_l=arm_l, arm_r=arm_r, over=over, armcol=col, paw=fur)

def dress_body(arm_l=6, arm_r=-6):
    under = scallop_skirt()
    over = (f'<path d="M-70 60 Q 0 84 70 60" fill="none" stroke="#F3A8B8" stroke-width="12"/>'
            f'<circle cx="0" cy="72" r="10" fill="#F3A8B8" stroke-width="3"/>')
    return body(170, 150, '#FFFFFF', None, legcol='#FFF8EE', arm_l=arm_l, arm_r=arm_r, under=under, over=over, armcol='#FFF8EE', paw='#FFF8EE')

def scallop_skirt():
    # 넓게 퍼지는 드레스 자락
    pts = 'M-90 70 C -120 130 -140 170 -150 190 '
    n = 8
    for i in range(n):
        x0 = -150 + i * 300 / n; x1 = x0 + 300 / n
        pts += f'Q {(x0 + x1) / 2} {214} {x1} 190 '
    pts += 'C 140 170 120 130 90 70 Z'
    return f'<path d="{pts}" fill="#FFFFFF"/>' + ''.join(f'<circle cx="{-120 + i * 40}" cy="170" r="5" fill="#F7E3EA" stroke="none"/>' for i in range(7))

def dress_parent(col, arm_l=8, arm_r=-8, pearl=True):
    over = ''
    if pearl:
        over += ''.join(f'<circle cx="{-46 + i * 13}" cy="{14 + abs(i - 3.5) * -2 + 10}" r="6" fill="#FFF8F0" stroke-width="2.5"/>' for i in range(8))
    return body(180, 160, col, None, legcol=col, arm_l=arm_l, arm_r=arm_r, over=over)

def dad_suit(col='#6B6F7E', fur=None, arm_l=8, arm_r=-8):
    over = (f'<path d="M-30 2 L 0 60 L 30 2 Z" fill="#fff"/><path d="M-8 8 h16 l 6 60 l -14 16 l -14 -16 Z" fill="#4E6A9A"/>')
    return body(186, 160, col, None, legcol='#4A4E5C', arm_l=arm_l, arm_r=arm_r, over=over)

# ---------- 머리 ----------
def blouse_mom(arm_l=8, arm_r=-8, col='#F7B9C8', paw='#B9774A'):
    over = (f'<path d="M-60 2 Q -30 40 0 8 Q 30 40 60 2 Z" fill="#FFFFFF" stroke-width="4"/>'
            + ''.join(f'<circle cx="{-44 + i * 12.5}" cy="{30 + abs(i - 3.5) * -3 + 10}" r="5.5" fill="#FFF8F0" stroke-width="2"/>' for i in range(8))
            + ''.join(f'<circle cx="0" cy="{70 + i*30}" r="5" fill="#fff" stroke-width="2.5"/>' for i in range(3))
            + ''.join(f'<circle cx="{x}" cy="{y}" r="5" fill="#fff" stroke="none" opacity=".7"/>' for x, y in [(-60, 80), (55, 70), (-45, 130), (60, 125), (-20, 110), (30, 100)]))
    return body(180, 160, col, None, legcol='#E9A0B4', arm_l=arm_l, arm_r=arm_r, over=over, paw=paw)

def cardigan_mom(arm_l=8, arm_r=-8, col='#B9A6E0', paw='#E8964E'):
    over = (f'<path d="M-40 2 L 0 60 L 40 2 Z" fill="#FFFFFF" stroke-width="4"/>'
            f'<path d="M-40 2 L -10 160 M 40 2 L 10 160" stroke-width="4"/>'
            + ''.join(f'<circle cx="-24" cy="{70 + i*30}" r="5" fill="#FFF3C4" stroke-width="2.5"/>' for i in range(3))
            + f'<path d="M-70 120 h 40 v 30 h -40 Z" fill="#A894D6" stroke-width="3"/>')
    return body(180, 160, col, None, legcol='#8A80A8', arm_l=arm_l, arm_r=arm_r, over=over, paw=paw)

def vest_dad(arm_l=8, arm_r=-8, paw='#D9A06A'):
    over = (f'<path d="M-44 0 L -20 24 L 0 4 L 20 24 L 44 0 Z" fill="#fff" stroke-width="4"/>'
            f'<path d="M-90 30 C -60 20 -40 20 -20 30 L 0 110 L 20 30 C 40 20 60 20 90 30 L 90 160 L -90 160 Z" fill="#2F4A7A" stroke-width="4"/>'
            + ''.join(f'<path d="M{-80 + i*20} 140 l 8 -8 l 8 8" stroke="#4A6AA0" stroke-width="3" fill="none"/>' for i in range(9)))
    return body(186, 160, '#BFD8F2', None, legcol='#5A5A66', arm_l=arm_l, arm_r=arm_r, over=over, armcol='#BFD8F2', paw=paw)

def sweater_dad(arm_l=8, arm_r=-8, paw='#FFFFFF'):
    over = (f'<path d="M-40 0 L -14 22 L 0 6 L 14 22 L 40 0 Z" fill="#fff" stroke-width="4"/>'
            f'<path d="M-60 40 H 60 M -60 54 H 60" stroke="#8FA48A" stroke-width="5"/>')
    return body(186, 160, '#6F8A6A', None, legcol='#4A4E5C', arm_l=arm_l, arm_r=arm_r, over=over, paw=paw)

def tuft(y=-112, col='#000'):
    return f'<path d="M-16 {y+4} q 6 -30 26 -14 M 2 {y} q 14 -26 30 -6" stroke="{OL}" stroke-width="5" fill="none" stroke-linecap="round"/>'

def shiba_head(mood='happy'):
    s = f'<g stroke="{OL}" stroke-width="{LW}" stroke-linejoin="round">'
    s += '<path d="M-118 -30 C -126 -110 -110 -150 -92 -158 C -70 -140 -50 -112 -40 -92 Z" fill="#E9A35E"/>'
    s += '<path d="M118 -30 C 126 -110 110 -150 92 -158 C 70 -140 50 -112 40 -92 Z" fill="#E9A35E"/>'
    s += '<path d="M-136 10 C -136 -80 -70 -110 0 -110 C 70 -110 136 -80 136 10 C 136 90 80 128 0 128 C -80 128 -136 90 -136 10 Z" fill="#E9A35E"/></g>'
    s += '<path d="M-104 -104 C -100 -128 -92 -140 -88 -142 C -76 -128 -66 -114 -60 -104 Z M104 -104 C 100 -128 92 -140 88 -142 C 76 -128 66 -114 60 -104 Z" fill="#F9C4B4"/>'
    s += '<path d="M-124 40 C -100 4 -50 10 0 30 C 50 10 100 4 124 40 C 110 100 60 122 0 122 C -60 122 -110 100 -124 40 Z" fill="#FFF6EA"/>'
    s += '<ellipse cx="-40" cy="-32" rx="13" ry="8" fill="#FFF6EA"/><ellipse cx="40" cy="-32" rx="13" ry="8" fill="#FFF6EA"/>'
    return s + face(0, 0, mood)

def bride_head(mood='happy', veil=True):
    s = ''
    if veil:
        s += f'<path d="M-40 -110 C -200 -60 -210 120 -180 260 L -110 250 C -130 120 -70 -30 10 -100 Z" fill="#FFFFFF" fill-opacity=".8" stroke="{OL}" stroke-width="4" stroke-linejoin="round"/>'
    s += f'<path d="{scallop(-118, 40, 48, 92, 14, 9)}" fill="#F2D3B0" stroke="{OL}" stroke-width="{LW}" stroke-linejoin="round"/>'
    s += f'<path d="{scallop(118, 40, 48, 92, 14, 9)}" fill="#F2D3B0" stroke="{OL}" stroke-width="{LW}" stroke-linejoin="round"/>'
    s += f'<path d="{scallop(0, 0, 128, 120, 22, 10)}" fill="#FFF8EE" stroke="{OL}" stroke-width="{LW}" stroke-linejoin="round"/>'
    if veil:  # 티아라
        s += f'<path d="M-50 -104 L -36 -136 L -18 -112 L 0 -146 L 18 -112 L 36 -136 L 50 -104 Z" fill="#FFE08A" stroke="{OL}" stroke-width="4" stroke-linejoin="round"/>'
        s += f'<circle cx="0" cy="-122" r="6" fill="#9ED8FF" stroke="{OL}" stroke-width="2.5"/>'
    return s + face(0, 6, mood, gender='f')

def poodle_head(mood='happy', col='#B9774A', ear='#9E6038'):
    """신부 엄마: 갈색 곱슬"""
    s = f'<path d="{scallop(-116, 50, 46, 80, 12, 9)}" fill="{ear}" stroke="{OL}" stroke-width="{LW}"/>'
    s += f'<path d="{scallop(116, 50, 46, 80, 12, 9)}" fill="{ear}" stroke="{OL}" stroke-width="{LW}"/>'
    s += f'<path d="{scallop(0, 0, 124, 116, 20, 10)}" fill="{col}" stroke="{OL}" stroke-width="{LW}"/>'
    s += f'<path d="{scallop(0, -96, 70, 40, 12, 9, 180, 360)}" fill="{col}" stroke="none"/>'
    s += f'<ellipse cx="0" cy="40" rx="66" ry="50" fill="#E2B08A"/>'
    s += face(0, 6, mood, gender='f')
    s += f'<g stroke="{OL}" stroke-width="3">' + ''.join(f'<circle cx="{78+math.cos(math.radians(a))*14:.1f}" cy="{-70+math.sin(math.radians(a))*14:.1f}" r="11" fill="#FFD1DC"/>' for a in range(0,360,72)) + '<circle cx="78" cy="-70" r="8" fill="#FFE07A"/></g>'
    return s

def corgi_head(mood='happy', glasses=True):
    """신랑 엄마: 웰시코기"""
    s = f'<g stroke="{OL}" stroke-width="{LW}" stroke-linejoin="round">'
    s += '<path d="M-110 -10 C -140 -100 -120 -170 -90 -176 C -60 -150 -46 -110 -40 -86 Z" fill="#E8964E"/>'
    s += '<path d="M110 -10 C 140 -100 120 -170 90 -176 C 60 -150 46 -110 40 -86 Z" fill="#E8964E"/>'
    s += '<path d="M-130 20 C -130 -80 -70 -106 0 -106 C 70 -106 130 -80 130 20 C 130 96 76 126 0 126 C -76 126 -130 96 -130 20 Z" fill="#E8964E"/></g>'
    s += '<path d="M-96 -112 C -94 -140 -88 -154 -86 -156 C -72 -138 -62 -120 -56 -106 Z M96 -112 C 94 -140 88 -154 86 -156 C 72 -138 62 -120 56 -106 Z" fill="#F9C4B4"/>'
    s += '<path d="M-12 -106 C -10 -40 -60 0 -110 40 C -90 100 -40 120 0 120 C 40 120 90 100 110 40 C 60 0 10 -40 12 -106 Z" fill="#FFF8EE"/>'
    s += face(0, 4, mood, gender='f')
    s += f'<path d="M60 -80 L 30 -104 L 34 -60 Z M 60 -80 L 92 -108 L 92 -62 Z" fill="#C9A6F0" stroke="{OL}" stroke-width="3.5" stroke-linejoin="round"/><circle cx="60" cy="-82" r="8" fill="#FFE07A" stroke="{OL}" stroke-width="3"/>'
    if glasses:
        s += f'<circle cx="-40" cy="4" r="28" fill="none" stroke="#7A5644" stroke-width="5"/><circle cx="40" cy="4" r="28" fill="none" stroke="#7A5644" stroke-width="5"/><path d="M-12 4 H 12" stroke="#7A5644" stroke-width="5"/>'
    return s

def beagle_head(mood='blank'):
    """신부 아빠"""
    s = f'<path d="M-110 -40 C -170 -20 -170 120 -120 140 C -100 120 -96 40 -96 0 Z" fill="#8A5A38" stroke="{OL}" stroke-width="{LW}" stroke-linejoin="round"/>'
    s += f'<path d="M110 -40 C 170 -20 170 120 120 140 C 100 120 96 40 96 0 Z" fill="#8A5A38" stroke="{OL}" stroke-width="{LW}" stroke-linejoin="round"/>'
    s += f'<path d="M-124 10 C -124 -84 -66 -112 0 -112 C 66 -112 124 -84 124 10 C 124 92 72 124 0 124 C -72 124 -124 92 -124 10 Z" fill="#D9A06A" stroke="{OL}" stroke-width="{LW}"/>'
    s += '<path d="M-14 -112 C -16 -40 -50 10 -70 50 C -50 110 50 110 70 50 C 50 10 16 -40 14 -112 Z" fill="#FFF8EE"/>'
    return s + face(0, 6, mood, blush=False, gender='m') + tuft(-112)

def bw_head(mood='blank'):
    """신랑 아빠: 흑백 강아지"""
    s = f'<path d="{scallop(-112, 50, 44, 86, 12, 7)}" fill="#3B3A40" stroke="{OL}" stroke-width="{LW}"/>'
    s += f'<path d="{scallop(112, 50, 44, 86, 12, 7)}" fill="#3B3A40" stroke="{OL}" stroke-width="{LW}"/>'
    s += f'<path d="M-122 10 C -122 -84 -66 -112 0 -112 C 66 -112 122 -84 122 10 C 122 92 72 124 0 124 C -72 124 -122 92 -122 10 Z" fill="#FFFFFF" stroke="{OL}" stroke-width="{LW}"/>'
    s += f'<path d="M-112 -40 C -90 -100 -40 -112 -8 -112 C -20 -70 -60 -40 -112 -20 Z M112 -40 C 90 -100 40 -112 8 -112 C 20 -70 60 -40 112 -20 Z" fill="#3B3A40"/>'
    s += f'<path d="M-122 10 C -122 -84 -66 -112 0 -112 C 66 -112 122 -84 122 10 C 122 92 72 124 0 124 C -72 124 -122 92 -122 10 Z" fill="none" stroke="{OL}" stroke-width="{LW}"/>'
    s += face(0, 6, mood, blush=False, gender='m')
    s += f'<circle cx="-40" cy="6" r="28" fill="none" stroke="{OL}" stroke-width="5"/><circle cx="40" cy="6" r="28" fill="none" stroke="{OL}" stroke-width="5"/><path d="M-12 6 H 12" stroke="{OL}" stroke-width="5"/>'
    return s

def char(kind, x, y, s=1.0, mood='happy', arms=(8, -8), flip=False):
    fx = -s if flip else s
    if kind == 'groom': b, h = suit_body(*arms), shiba_head(mood); hy = -6
    elif kind == 'bride': b, h = dress_body(*arms), bride_head(mood); hy = 0
    elif kind == 'momB': b, h = blouse_mom(*arms), poodle_head(mood); hy = 0
    elif kind == 'momG': b, h = cardigan_mom(*arms), corgi_head(mood); hy = 0
    elif kind == 'dadB': b, h = vest_dad(*arms), beagle_head(mood); hy = 0
    elif kind == 'dadG': b, h = sweater_dad(*arms), bw_head(mood); hy = 0
    # 몸은 머리 아래 (머리 중심 기준 y+105), 머리 1.2배
    return (f'<g transform="translate({x} {y}) scale({fx} {s})">'
            f'<g transform="translate(0 105)">{b}</g><g transform="translate(0 {hy}) scale(1.2)">{h}</g></g>')
