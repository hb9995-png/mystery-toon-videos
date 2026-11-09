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
