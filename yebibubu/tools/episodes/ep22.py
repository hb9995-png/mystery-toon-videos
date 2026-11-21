import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from extra import *

TOTAL = 9


def tag(n, label):
    return (f'<rect x="100" y="160" width="{110 + len(label) * 50}" height="80" rx="40" fill="#fff" stroke="{INK}" stroke-width="5"/>'
            + f'<circle cx="140" cy="200" r="28" fill="{ROSE}"/>' + T(140, 215, str(n), 40, 'j', '#fff')
            + T(184, 218, label, 46, 'j', INK, 'start'))


def scene(no, n, label, bg, inner, cap):
    return page_bg() + header(no, TOTAL) + panel(inner + tag(n, label), bg) + caption(cap)


def floor(y=880, col='#E9D6BE'):
    return f'<rect x="70" y="{y}" width="940" height="300" fill="{col}"/><path d="M70 {y} H 1010" stroke="{INK}" stroke-width="5"/>'


def open_fridge(x, y, w=300, h=500):
    """문 열린 냉장고: 안에 선반과 빈 칸."""
    s = f'<g stroke="{INK}" stroke-width="5" stroke-linejoin="round"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="20" fill="#E8EEF3"/>'
    s += f'<rect x="{x + 18}" y="{y + 18}" width="{w - 36}" height="{h - 36}" rx="10" fill="#F7FBFF"/>'
    for k in range(1, 4):
        s += f'<path d="M{x + 18} {y + h * k / 4} H {x + w - 18}" stroke-width="4"/>'
    s += f'<path d="M{x} {y + 10} l -90 40 v {h - 60} l 90 30 z" fill="#DDE5EC"/></g>'
    return s


def tv(x, y, w=360, h=220):
    return (f'<g stroke="{INK}" stroke-width="6"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="14" fill="#3A3542"/>'
            f'<rect x="{x + 16}" y="{y + 16}" width="{w - 32}" height="{h - 32}" rx="6" fill="#9FD2F0"/>'
            f'<path d="M{x + w / 2} {y + h} v 40 M{x + w / 2 - 70} {y + h + 40} h 140"/></g>')


def price_tag(x, y, text='?'):
    return (f'<g stroke="{INK}" stroke-width="4"><path d="M{x} {y} h 110 l 30 34 l -30 34 h -110 z" fill="#FFE36A"/></g>'
            + T(x + 56, y + 48, text, 40, 'j', INK))


pages = {}
# 1 표지
pages[1] = (page_bg('#FFE4E4') + hearts(22, (40, 40, 1040, 1310), '#FFD0D6', 221)
    + f'<rect x="80" y="70" width="240" height="84" rx="42" fill="{ROSE}"/>' + T(200, 128, '공감 주의', 50, 'j', '#fff')
    + T(80, 265, '혼수 보러 가면', 108, 'j', INK, 'start') + T(80, 395, '생기는 일 7가지', 108, 'j', ROSE, 'start')
    + panel(floor(980, '#EDE6F0') + fridge(110, 560, 200, 400) + washer(820, 720, 160)
            + char('bride', 460, 870, .85, 'joy', (6, -6)) + char('groom', 700, 860, .8, 'nervous', (8, -8)) + sweat(800, 700), '#FFF7EE', 440, 1110)
    + f'<rect x="70" y="1150" width="940" height="130" rx="65" fill="#fff" stroke="{ROSE}" stroke-width="6"/>' + T(540, 1235, '+ 몇 개 공감했는지 댓글로', 58, 'j', INK))

# 2 냉장고 문 열기
pages[2] = scene(2, 1, '문 다 열어 보기', '#EAF4F8',
    floor(900, '#DCE6EE') + open_fridge(620, 330)
    + char('bride', 360, 820, 1.05, 'joy', (100, -6)) + hearts(5, (420, 300, 600, 460), '#FFB3C0', 7),
    '매장 냉장고 문을\n괜히 다 열어 본다.')

# 3 세탁기
pages[3] = scene(3, 2, '안까지 구경', '#F1F5F9',
    floor(900, '#DCE6EE') + washer(560, 470, 320)
    + char('groom', 340, 820, 1.05, 'shock', (60, 60)) + sweat(500, 600)
    + bubble(560, 270, 360, '안 넓다!', 54, (700, 460)),
    '세탁기 안을\n한참 들여다보는 오빠.')

# 4 소파
pages[4] = scene(4, 3, '일어나기 싫어', '#F4ECFA',
    sofa(170, 560, 740)
    + char('bride', 340, 760, .9, 'happy', (6, -6)) + char('groom', 740, 760, .9, 'happy', (8, -8), flip=True)
    + T(840, 420, 'Zzz', 80, 'j', '#9A8FB5'),
    '전시 소파에 앉으면\n둘 다 일어나기 싫다.')

# 5 색깔
pages[5] = scene(5, 4, '색깔 고민', '#FFF5E6',
    fridge(130, 320, 200, 380, '#F7F7F7') + fridge(360, 320, 200, 380, '#F4C6D0') + fridge(590, 320, 200, 380, '#C9DCC9') + fridge(820, 320, 160, 380, '#D9D3E8')
    + char('bride', 360, 940, .8, 'nervous', (60, -6)) + char('groom', 700, 940, .8, 'blank', (8, 60), flip=True) + sweat(470, 790),
    '색 하나 고르는 데\n한참이 걸린다.')

# 6 설명 듣다 멍
pages[6] = scene(6, 5, '머리가 하얘짐', '#EEF1F7',
    tv(560, 300) + bubble(110, 300, 400, '이 기능은요~\n저 기능은요~', 46, (180, 600))
    + char('bride', 380, 830, .95, 'blank', (6, -6)) + char('groom', 700, 830, .95, 'blank', (8, -8), flip=True)
    + T(200, 700, '?', 90, 'j', '#9A8FB5') + T(900, 700, '?', 90, 'j', '#9A8FB5'),
    '기능 설명을 듣다 보면\n둘 다 멍해진다.')

# 7 견적서
pages[7] = scene(7, 6, '잠깐 조용', '#FFEFF2',
    paper(560, 290, 380, 480, '견적서', [('냉장고', '?', None), ('세탁기', '?', None), ('TV', '?', None), ('합계', '!!!', '#C0392B')], 44)
    + char('bride', 280, 830, .95, 'shock', (60, 60)) + sweat(400, 620) + sweat(150, 640, .8),
    '견적서를 받으면\n둘 다 말이 없어진다.')

# 8 집에 와서 또 검색
pages[8] = scene(8, 7, '밤새 비교', '#E4E8F4',
    f'<rect x="70" y="760" width="940" height="400" fill="#C9C3E0"/>'
    + char('bride', 320, 780, .95, 'smug', (100, -6)) + char('groom', 760, 780, .95, 'nervous', (8, 100), flip=True)
    + phone(410, 340, 110, 190) + phone(560, 340, 110, 190) + T(800, 300, '(새벽 2시)', 54, 'g', '#7A8090'),
    '집에 와서도\n밤새 비교 검색 중.')

# 9 마무리
pages[9] = (page_bg('#FFE4E4') + header(9, TOTAL) + hearts(18, (40, 120, 1040, 700), '#FFD0D6', 229)
    + char('bride', 400, 470, 1.15, 'joy', (6, -40)) + char('groom', 690, 460, 1.15, 'happy', (40, -8))
    + f'<rect x="110" y="820" width="860" height="420" rx="60" fill="#fff" stroke="{INK}" stroke-width="6"/>'
    + T(540, 925, '몇 개 공감했어요?', 76, 'j') + T(540, 1035, '댓글로 번호 남기기', 76, 'j', ROSE)
    + T(540, 1145, '혼수 보러 갈 예비부부에게 공유!', 48, 'g', '#7A6262')
    + T(540, 1310, '@yebibubu.toon', 40, 'j', '#C49A9A'))

if __name__ == '__main__':
    render(pages, sys.argv[1] if len(sys.argv) > 1 else 'out/ep22')
