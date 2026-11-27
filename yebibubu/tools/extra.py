"""예비부부툰 추가 소품 (dogs.py 는 고치지 않는다). from extra import * 로 쓴다."""
from kit import *


def tears(x, y, s=1.0):
    """char(x, y, s) 의 눈 아래로 흐르는 눈물. x, y 는 char 에 넣은 값 그대로."""
    out = ''
    for k in (-1, 1):
        ex = x + k * 48 * s; ey = y + 26 * s
        out += (f'<path d="M{ex - 12 * s} {ey} q {-6 * s} {60 * s} {4 * s} {120 * s} h {16 * s} q {-4 * s} {-60 * s} {8 * s} {-120 * s} z" '
                f'fill="#A9DEFF" stroke="{INK}" stroke-width="3.5" opacity=".95"/>')
    return out


def phone(x, y, w=300, h=520, screen='#DCE9F6', inner=''):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{w * .12}" fill="#3A3542" stroke="{INK}" stroke-width="6"/>'
            f'<rect x="{x + 16}" y="{y + 40}" width="{w - 32}" height="{h - 80}" rx="18" fill="{screen}"/>' + inner)


def paper(x, y, w, h, title='', rows=(), size=40, rot=0, title_col=None):
    """견적서·명단 같은 종이. rows: [(왼쪽 글, 오른쪽 글, 색)]"""
    s = f'<g transform="rotate({rot} {x + w / 2} {y + h / 2})">'
    s += f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="14" fill="#fff" stroke="{INK}" stroke-width="5"/>'
    if title:
        s += T(x + w / 2, y + 66, title, size + 8, 'j', title_col or INK)
        s += f'<path d="M{x + 30} {y + 92} H {x + w - 30}" stroke="#E3D6D6" stroke-width="4"/>'
    for i, (a, b, c) in enumerate(rows):
        yy = y + 150 + i * size * 1.45
        s += T(x + 36, yy, a, size, 'g', c or INK, 'start') + T(x + w - 36, yy, b, size, 'g', c or INK, 'end')
    return s + '</g>'


def chandelier(x, y, s=1.0):
    out = f'<g transform="translate({x} {y}) scale({s})" stroke="{INK}" stroke-width="4">'
    out += '<path d="M0 -200 V -40" />'
    out += '<path d="M-120 0 Q 0 60 120 0" fill="none"/><path d="M-70 -30 Q 0 10 70 -30" fill="none"/>'
    for dx in (-120, -60, 0, 60, 120):
        dy = 0 if abs(dx) == 120 else 22 - abs(dx) * .1
        out += f'<rect x="{dx - 9}" y="{dy - 30}" width="18" height="30" fill="#FFF8DA"/><path d="M{dx} {dy - 30} q -9 -16 0 -30 q 9 14 0 30" fill="#FFD36A"/>'
        out += f'<path d="M{dx} {dy} v 26" /><circle cx="{dx}" cy="{dy + 34}" r="8" fill="#CFE9FF"/>'
    return out + '</g>'


def notebook(x, y, w=300, h=220, title='', rot=-6):
    s = f'<g transform="rotate({rot} {x + w / 2} {y + h / 2})">'
    s += f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="#F6E3A8" stroke="{INK}" stroke-width="5"/>'
    s += f'<rect x="{x + 22}" y="{y + 22}" width="{w - 44}" height="{h - 44}" rx="8" fill="#FFFBEA" stroke="{INK}" stroke-width="3"/>'
    if title: s += T(x + w / 2, y + h / 2 + 18, title, 46, 'j', '#8A5A3A')
    return s + '</g>'


def chicken_box(x, y, w=360):
    h = w * .5
    s = f'<g stroke="{INK}" stroke-width="5" stroke-linejoin="round">'
    s += f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="16" fill="#F2C66B"/>'
    for i in range(4):
        cx = x + w * (.2 + .2 * i); cy = y + 10
        s += f'<ellipse cx="{cx}" cy="{cy}" rx="{w * .12}" ry="{w * .09}" fill="#C9772E" transform="rotate({(-1) ** i * 18} {cx} {cy})"/>'
        s += f'<path d="M{cx + w * .08} {cy - w * .03} l {w * .07} {-w * .07}" stroke-width="10" stroke="#FFF3D9"/>'
    s += '</g>'
    return s + T(x + w / 2, y + h * .72, '치킨', w * .16, 'j', '#8A4A1E')


def vs_badge(x, y, r=78):
    return (f'<circle cx="{x}" cy="{y}" r="{r}" fill="{ROSE}" stroke="{INK}" stroke-width="6"/>'
            + T(x, y + r * .36, 'VS', r * .95, 'j', '#fff'))


def page_bg(col=BG):
    return f'<rect width="1080" height="1350" fill="{col}"/>'


def fridge(x, y, w=260, h=460, col='#E8EEF3'):
    """양문형 냉장고."""
    return (f'<g stroke="{INK}" stroke-width="5" stroke-linejoin="round"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="22" fill="{col}"/>'
            f'<path d="M{x + w / 2} {y + 10} V {y + h - 10}" /><rect x="{x + w / 2 - 26}" y="{y + h * .3}" width="10" height="{h * .25}" rx="5" fill="#B9C3CC"/>'
            f'<rect x="{x + w / 2 + 16}" y="{y + h * .3}" width="10" height="{h * .25}" rx="5" fill="#B9C3CC"/></g>')


def washer(x, y, w=240, col='#F3F5F7'):
    """드럼 세탁기."""
    return (f'<g stroke="{INK}" stroke-width="5"><rect x="{x}" y="{y}" width="{w}" height="{w * 1.15}" rx="20" fill="{col}"/>'
            f'<path d="M{x} {y + w * .22} H {x + w}"/><circle cx="{x + w / 2}" cy="{y + w * .7}" r="{w * .3}" fill="#BFE3F5"/>'
            f'<circle cx="{x + w * .8}" cy="{y + w * .11}" r="{w * .05}" fill="{ROSE}"/></g>')


def tape(x, y, length=420):
    """줄자: (x, y) 에 몸통, 오른쪽으로 길이만큼 테이프."""
    s = f'<g stroke="{INK}" stroke-width="5"><rect x="{x}" y="{y - 14}" width="{length}" height="28" fill="#FFD84D"/>'
    for i in range(1, int(length / 30)):
        s += f'<path d="M{x + i * 30} {y - 14} v {14 if i % 2 else 22}" stroke-width="3"/>'
    return s + f'<rect x="{x - 90}" y="{y - 60}" width="110" height="120" rx="26" fill="{ROSE}"/><circle cx="{x - 35}" cy="{y}" r="22" fill="#fff"/></g>'


def calendar(x, y, w=300, mark=(), title=''):
    """달력 한 장. mark: 동그라미 칠 칸 번호(0~27)."""
    s = f'<g stroke="{INK}" stroke-width="5"><rect x="{x}" y="{y}" width="{w}" height="{w}" rx="18" fill="#fff"/><path d="M{x} {y + w * .22} H {x + w}"/>'
    s += f'<rect x="{x}" y="{y}" width="{w}" height="{w * .22}" rx="18" fill="{ROSE}"/></g>' + T(x + w / 2, y + w * .16, title, w * .12, 'j', '#fff')
    cw = w / 7
    for i in range(28):
        cx = x + cw * (i % 7) + cw / 2; cy = y + w * .22 + cw * .7 + (i // 7) * cw * .95
        s += f'<circle cx="{cx}" cy="{cy}" r="{cw * .12}" fill="#D9CCCC"/>'
        if i in mark: s += f'<circle cx="{cx}" cy="{cy}" r="{cw * .38}" fill="none" stroke="{ROSE}" stroke-width="5"/>'
    return s


def box(x, y, w=200, h=150, label=''):
    """택배 상자."""
    return (f'<g stroke="{INK}" stroke-width="5" stroke-linejoin="round"><rect x="{x}" y="{y}" width="{w}" height="{h}" fill="#D9A86C"/>'
            f'<path d="M{x + w / 2 - 20} {y} v {h * .35} h 40 v {-h * .35}" fill="#C8955A"/></g>' + (T(x + w / 2, y + h * .78, label, h * .2, 'j', '#6A4A2A') if label else ''))


def door(x, y, w=230, h=520):
    """현관문."""
    return (f'<g stroke="{INK}" stroke-width="6"><rect x="{x - 20}" y="{y - 20}" width="{w + 40}" height="{h + 20}" fill="#C7A47A"/>'
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="#8C6A4E"/><circle cx="{x + w - 30}" cy="{y + h * .55}" r="12" fill="#FFD36A"/></g>')


def mic(x, y, s=1.0):
    """손 마이크. (x, y) 가 머리 중심."""
    return (f'<g transform="translate({x} {y}) scale({s}) rotate(-20)" stroke="{INK}" stroke-width="5">'
            f'<rect x="-14" y="20" width="28" height="120" rx="12" fill="#3A3542"/>'
            f'<circle cx="0" cy="0" r="34" fill="#C9CED6"/><path d="M-24 -10 H 24 M -28 6 H 28" stroke-width="3"/></g>')


def note(x, y, s=1.0, col='#E06C7A'):
    """음표 하나."""
    return (f'<g transform="translate({x} {y}) scale({s})" stroke="{INK}" stroke-width="4">'
            f'<ellipse cx="0" cy="0" rx="22" ry="16" fill="{col}" transform="rotate(-20)"/>'
            f'<path d="M18 -6 V -80 q 26 10 30 36" fill="none" stroke-width="6"/></g>')


def curtain(x, y, w=420, h=640, opened=False, col='#F4C6D0'):
    """피팅룸 커튼. opened=True 면 양옆으로 젖혀진 모양."""
    s = f'<g stroke="{INK}" stroke-width="5" stroke-linejoin="round"><rect x="{x - 20}" y="{y - 24}" width="{w + 40}" height="24" rx="10" fill="#C9A26A"/>'
    if opened:
        for sx, d in ((x, 1), (x + w, -1)):
            s += f'<path d="M{sx} {y} q {d * 90} {h * .45} {d * 30} {h} h {d * 60} q {d * 10} {-h * .6} {d * 50} {-h} z" fill="{col}"/>'
    else:
        n = 6; cw = w / n
        for i in range(n):
            s += f'<path d="M{x + i * cw} {y} q {cw * .5} {h * .5} 0 {h} h {cw} q {-cw * .5} {-h * .5} 0 {-h} z" fill="{col}"/>'
    return s + '</g>'


def mirror(x, y, w=260, h=520):
    """전신 거울."""
    return (f'<g stroke="{INK}" stroke-width="6"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{w / 2}" fill="#E7C98A"/>'
            f'<rect x="{x + 18}" y="{y + 18}" width="{w - 36}" height="{h - 36}" rx="{w / 2 - 18}" fill="#DDEFF7"/></g>'
            f'<path d="M{x + w * .3} {y + h * .2} l {w * .25} {-w * .12} M {x + w * .3} {y + h * .3} l {w * .35} {-w * .17}" stroke="#fff" stroke-width="8" stroke-linecap="round"/>')


def dress_rack(x, y, w=520, n=5):
    """드레스 걸린 행거."""
    s = f'<g stroke="{INK}" stroke-width="5" stroke-linejoin="round"><path d="M{x} {y} H {x + w}" stroke-width="8"/>'
    s += f'<path d="M{x + 10} {y} V {y + 420} M {x + w - 10} {y} V {y + 420}" stroke-width="7"/>'
    gap = (w - 60) / max(1, n - 1)
    for i in range(n):
        cx = x + 30 + i * gap
        s += f'<path d="M{cx} {y} v 18"/><path d="M{cx - 22} {y + 20} h 44 l 34 260 h -112 z" fill="#FFFFFF"/>'
        s += f'<path d="M{cx - 22} {y + 70} h 44" stroke="#E7D7DA" stroke-width="4"/>'
    return s + '</g>'


def sofa(x, y, w=520, col='#B7C4D9'):
    """2인용 소파. (x, y) 는 등받이 왼쪽 위."""
    return (f'<g stroke="{INK}" stroke-width="6" stroke-linejoin="round"><rect x="{x}" y="{y}" width="{w}" height="170" rx="40" fill="{col}"/>'
            f'<rect x="{x - 30}" y="{y + 90}" width="{w + 60}" height="140" rx="40" fill="{col}"/>'
            f'<rect x="{x + 30}" y="{y + 110}" width="{w / 2 - 40}" height="70" rx="24" fill="#fff" fill-opacity=".35"/>'
            f'<rect x="{x + w / 2 + 10}" y="{y + 110}" width="{w / 2 - 40}" height="70" rx="24" fill="#fff" fill-opacity=".35"/>'
            f'<rect x="{x}" y="{y + 230}" width="26" height="40" fill="#8C6A4E"/><rect x="{x + w - 26}" y="{y + 230}" width="26" height="40" fill="#8C6A4E"/></g>')


def plant(x, y, s=1.0):
    """화분. (x, y) 는 화분 아래 가운데."""
    return (f'<g transform="translate({x} {y}) scale({s})" stroke="{INK}" stroke-width="5" stroke-linejoin="round">'
            f'<path d="M0 -120 q -70 -40 -60 -130 q 50 30 60 130 z M0 -120 q 70 -50 70 -150 q -60 20 -70 150 z M0 -120 q -10 -80 10 -170 q 30 80 -10 170 z" fill="#7FC58F"/>'
            f'<path d="M-60 -120 h 120 l -20 120 h -80 z" fill="#E59A6B"/></g>')


def lamp(x, y, warm=True):
    """천장 펜던트 조명. (x, y) 는 갓 위 가운데."""
    glow = '#FFE6A3' if warm else '#F4FAFF'
    return (f'<circle cx="{x}" cy="{y + 110}" r="170" fill="{glow}" fill-opacity=".55"/>'
            f'<g stroke="{INK}" stroke-width="5"><path d="M{x} {y - 200} V {y}"/><path d="M{x - 80} {y + 80} L {x - 30} {y} H {x + 30} L {x + 80} {y + 80} Z" fill="{"#F5B860" if warm else "#DCE6F2"}"/>'
            f'<circle cx="{x}" cy="{y + 92}" r="18" fill="{glow}"/></g>')


def camera(x, y, s=1.0, tripod=True):
    """삼각대 위 카메라. (x, y) 는 카메라 몸체 가운데."""
    t = ''
    if tripod:
        t = (f'<path d="M0 60 L -90 380 M0 60 L 90 380 M0 60 L 0 380" stroke-width="8" fill="none"/>')
    return (f'<g transform="translate({x} {y}) scale({s})" stroke="{INK}" stroke-width="5" stroke-linejoin="round">' + t +
            f'<rect x="-110" y="-70" width="220" height="140" rx="22" fill="#4A4652"/>'
            f'<rect x="-60" y="-96" width="70" height="30" rx="8" fill="#4A4652"/>'
            f'<circle cx="0" cy="0" r="52" fill="#2E2B35"/><circle cx="0" cy="0" r="32" fill="#7FA9D9"/>'
            f'<circle cx="-10" cy="-10" r="9" fill="#fff" stroke="none"/><circle cx="78" cy="-44" r="10" fill="#FFD36A"/></g>')


def frame(x, y, w=260, h=200, inner='', col='#C99A6B'):
    """벽 액자. inner 는 액자 안 그림."""
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{col}" stroke="{INK}" stroke-width="6"/>'
            f'<rect x="{x + 18}" y="{y + 18}" width="{w - 36}" height="{h - 36}" fill="#FFF8EE" stroke="{INK}" stroke-width="3"/>' + inner)


def friend(kind, x, y, s=1.0, mood='happy', arms=(8, -8), flip=False):
    """신부 친구들(조연). kind: 'f1' 크림 푸들·민트 니트, 'f2' 회색 푸들·노란 티. char() 와 같은 좌표계."""
    if kind == 'f1':
        h = poodle_head(mood, col='#F4E3C3', ear='#E2C99C')
        b = body(180, 160, '#9ED9C6', None, legcol='#7FBFAB', arm_l=arms[0], arm_r=arms[1], paw='#F4E3C3',
                 over=f'<path d="M-50 2 Q 0 40 50 2" fill="none" stroke-width="4"/>')
    else:
        h = poodle_head(mood, col='#A7A3AE', ear='#8A8592')
        b = body(180, 160, '#FFD86A', None, legcol='#E9BE4A', arm_l=arms[0], arm_r=arms[1], paw='#A7A3AE',
                 over=f'<circle cx="0" cy="80" r="22" fill="#FF9FB0" stroke-width="3"/>')
    fx = -s if flip else s
    return (f'<g transform="translate({x} {y}) scale({fx} {s})">'
            f'<g transform="translate(0 105)">{b}</g><g transform="scale(1.2)">{h}</g></g>')


def invite_card(x, y, w=300, rot=0):
    """청첩장 한 장: 봉투 위 카드 (x, y 는 왼쪽 위)."""
    h = w * .7
    return (f'<g transform="rotate({rot} {x + w / 2} {y + h / 2})" stroke="{INK}" stroke-width="5" stroke-linejoin="round">'
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="#FFF8F0"/>'
            f'<path d="M{x} {y} L {x + w / 2} {y + h * .55} L {x + w} {y}" fill="#F6E3E6"/>'
            f'<circle cx="{x + w / 2}" cy="{y + h * .55}" r="{w * .07}" fill="{ROSE}"/></g>')


def cafe_table(y=880, x0=110, x1=970):
    """식당 긴 탁자 + 접시·컵."""
    s = (f'<g stroke="{INK}" stroke-width="5" stroke-linejoin="round">'
         f'<rect x="{x0}" y="{y}" width="{x1 - x0}" height="56" rx="18" fill="#E9C9A4"/>'
         f'<rect x="{x0 + 50}" y="{y + 56}" width="28" height="120" fill="#C9A07A"/><rect x="{x1 - 78}" y="{y + 56}" width="28" height="120" fill="#C9A07A"/>')
    for cx in range(x0 + 120, x1 - 60, 230):
        s += f'<ellipse cx="{cx}" cy="{y + 6}" rx="70" ry="18" fill="#fff"/>'
        s += f'<rect x="{cx + 80}" y="{y - 56}" width="40" height="58" rx="8" fill="#CDEBF7"/>'
    return s + '</g>'


def memo_card(x, y, w=260, h=180, lines=(), rot=-4):
    """작은 메모 쪽지(줄글)."""
    s = f'<g transform="rotate({rot} {x + w / 2} {y + h / 2})"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="#FFF7B8" stroke="{INK}" stroke-width="5"/>'
    for i, t in enumerate(lines):
        s += T(x + 24, y + 54 + i * 46, t, 36, 'g', INK, 'start')
    return s + '</g>'


def cart(x, y, s=1.0, full=True):
    """장보기 카트. (x, y) 는 바구니 왼쪽 위. full=True 면 물건이 쌓여 있다."""
    w, h = 360 * s, 220 * s
    st = ''
    if full:
        cols = ['#F08A6A', '#9CCB7E', '#F2C66B', '#96B4EE', '#C59BE6', '#FFB3C1']
        for i in range(6):
            bx = x + 20 * s + (i % 3) * 110 * s; by = y - 70 * s - (i // 3) * 80 * s
            st += f'<rect x="{bx}" y="{by}" width="{100 * s}" height="{90 * s}" rx="{10 * s}" fill="{cols[i]}" stroke="{INK}" stroke-width="4"/>'
    return (st + f'<g stroke="{INK}" stroke-width="5" stroke-linejoin="round" fill="none">'
            f'<path d="M{x} {y} H {x + w} L {x + w - 30 * s} {y + h} H {x + 30 * s} Z" fill="#DDE6EE"/>'
            + ''.join(f'<path d="M{x + w * k / 5} {y} L {x + 30 * s + (w - 60 * s) * k / 5} {y + h}" stroke-width="3"/>' for k in range(1, 5))
            + f'<path d="M{x + w} {y} l {50 * s} {-60 * s} h {40 * s}" stroke-width="8"/>'
            f'<path d="M{x + 40 * s} {y + h} V {y + h + 60 * s} H {x + w - 40 * s} V {y + h}" stroke-width="6"/></g>'
            f'<circle cx="{x + 60 * s}" cy="{y + h + 80 * s}" r="{20 * s}" fill="#3A3542"/><circle cx="{x + w - 60 * s}" cy="{y + h + 80 * s}" r="{20 * s}" fill="#3A3542"/>')


def towels(x, y, cols=('#FFB3C1', '#96B4EE', '#9CCB7E', '#F2C66B', '#C59BE6'), w=240):
    """개어 놓은 수건 더미. (x, y) 는 맨 아래 수건 왼쪽 아래."""
    s = ''
    for i, c in enumerate(cols):
        yy = y - (i + 1) * 54
        s += f'<rect x="{x + (i % 2) * 10}" y="{yy}" width="{w}" height="54" rx="20" fill="{c}" stroke="{INK}" stroke-width="4"/>'
    return s


def pan(x, y, s=1.0, rot=0):
    """프라이팬. (x, y) 는 팬 가운데."""
    return (f'<g transform="translate({x} {y}) rotate({rot}) scale({s})" stroke="{INK}" stroke-width="5">'
            f'<rect x="80" y="-14" width="170" height="28" rx="14" fill="#6B4A3A"/>'
            f'<circle cx="0" cy="0" r="95" fill="#4A4552"/><circle cx="0" cy="0" r="70" fill="#5E5868" stroke-width="3"/></g>')


def receipt(x, y, w=200, h=600):
    """길게 늘어진 영수증. (x, y) 는 위 가운데."""
    s = f'<path d="M{x - w / 2} {y} H {x + w / 2} V {y + h} ' + ''.join(f'l {-w / 10} 20 l {-w / 10} -20 ' for _ in range(5)) + f'Z" fill="#fff" stroke="{INK}" stroke-width="5"/>'
    for i in range(int((h - 60) / 46)):
        yy = y + 50 + i * 46
        s += f'<path d="M{x - w / 2 + 24} {yy} h {w * .45}" stroke="#C9BDBD" stroke-width="6" stroke-linecap="round"/><path d="M{x + w / 2 - 24} {yy} h {-w * .2}" stroke="#C9BDBD" stroke-width="6" stroke-linecap="round"/>'
    return s


def lake(y=760, col='#9CCBE8'):
    """호수 물결 배경. y 는 수면."""
    s = f'<rect x="70" y="{y}" width="940" height="600" fill="{col}"/>'
    for i in range(5):
        yy = y + 50 + i * 70
        for k in range(4):
            xx = 120 + k * 240 + (i % 2) * 110
            s += f'<path d="M{xx} {yy} q 30 -18 60 0 t 60 0" fill="none" stroke="#fff" stroke-width="5" opacity=".7"/>'
    return s


def dock(x0, x1, y):
    """나무 선착장(물가 데크)."""
    s = f'<g stroke="{INK}" stroke-width="5"><rect x="{x0}" y="{y}" width="{x1 - x0}" height="60" fill="#C9A07A"/>'
    for xx in range(int(x0) + 80, int(x1), 160):
        s += f'<rect x="{xx}" y="{y + 60}" width="26" height="200" fill="#A9825E"/>'
    return s + '</g>'


def rod(x, y, dx=300, dy=-260, line=380):
    """낚싯대: (x, y) 손잡이에서 (x+dx, y+dy) 끝, 거기서 줄이 line 만큼 아래로."""
    ex, ey = x + dx, y + dy
    return (f'<path d="M{x} {y} L {ex} {ey}" stroke="#6A4A2A" stroke-width="9" stroke-linecap="round"/>'
            f'<path d="M{ex} {ey} V {ey + line}" stroke="#555" stroke-width="2.5"/>'
            f'<circle cx="{ex}" cy="{ey + line}" r="12" fill="{ROSE}" stroke="{INK}" stroke-width="3"/>')


def fish(x, y, s=1.0, col='#F2A65A', rot=0):
    """물고기 한 마리. (x, y) 가운데."""
    return (f'<g transform="translate({x} {y}) rotate({rot}) scale({s})" stroke="{INK}" stroke-width="5" stroke-linejoin="round">'
            f'<path d="M70 0 L 120 -40 L 120 40 Z" fill="{col}"/><ellipse cx="0" cy="0" rx="85" ry="48" fill="{col}"/>'
            f'<circle cx="-45" cy="-10" r="9" fill="{INK}"/><path d="M-10 -40 q 20 40 0 80" fill="none" stroke-width="3"/></g>')


def window(x, y, w=380, h=420, curtain_=False, sun=True):
    """창문. 햇빛 들어오는 창 (커튼 없이)."""
    s = ''
    if sun:
        s += f'<path d="M{x} {y + h} L {x - 120} {y + h + 500} L {x + w + 260} {y + h + 500} L {x + w} {y + h} Z" fill="#FFF2B8" opacity=".55"/>'
    s += (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="#CFE9FF" stroke="{INK}" stroke-width="6"/>'
          f'<path d="M{x + w / 2} {y} V {y + h} M {x} {y + h / 2} H {x + w}" stroke="{INK}" stroke-width="5"/>')
    if sun:
        s += f'<circle cx="{x + w * .72}" cy="{y + h * .28}" r="48" fill="#FFD36A" stroke="{INK}" stroke-width="4"/>'
    return s
