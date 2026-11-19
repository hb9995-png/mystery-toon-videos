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


def flash(x, y, r=120):
    pts = ' '.join(f'{x + (r if i % 2 == 0 else r * .45) * __import__("math").cos(i * 3.14159 / 6)},{y + (r if i % 2 == 0 else r * .45) * __import__("math").sin(i * 3.14159 / 6)}' for i in range(12))
    return f'<polygon points="{pts}" fill="#FFF2A8" stroke="{INK}" stroke-width="4"/>'


def thumbs(x, y, cols=4, rows=3, w=90, h=70):
    s = ''
    for r in range(rows):
        for c in range(cols):
            s += f'<rect x="{x + c * (w + 14)}" y="{y + r * (h + 14)}" width="{w}" height="{h}" rx="8" fill="#F7D9DE" stroke="{INK}" stroke-width="3"/>'
            s += f'<circle cx="{x + c * (w + 14) + w * .38}" cy="{y + r * (h + 14) + h * .5}" r="14" fill="#fff" stroke="{INK}" stroke-width="2"/><circle cx="{x + c * (w + 14) + w * .64}" cy="{y + r * (h + 14) + h * .5}" r="14" fill="#E9A15B" stroke="{INK}" stroke-width="2"/>'
    return s


def snack(x, y):
    return (f'<g stroke="{INK}" stroke-width="5" stroke-linejoin="round"><path d="M{x} {y} l 60 -110 l 60 110 z" fill="#FFE1A6"/>'
            f'<path d="M{x} {y} h 120 v 24 h -120 z" fill="#8FD3C1"/></g>')


pages = {}
# 1 표지
pages[1] = (page_bg('#FFE4E4') + hearts(22, (40, 40, 1040, 1310), '#FFD0D6', 181)
    + f'<rect x="80" y="70" width="240" height="84" rx="42" fill="{ROSE}"/>' + T(200, 128, '공감 주의', 50, 'j', '#fff')
    + T(80, 265, '웨딩촬영 하면', 108, 'j', INK, 'start') + T(80, 395, '생기는 일 7가지', 108, 'j', ROSE, 'start')
    + panel(floor(980, '#F3E3D3') + camera(170, 640, .7) + flash(170, 560, 70)
            + char('bride', 520, 860, .95, 'joy', (6, -6)) + char('groom', 800, 850, .95, 'nervous', (8, -8)) + sweat(920, 700), '#FFF7EE', 440, 1110)
    + f'<rect x="70" y="1150" width="940" height="130" rx="65" fill="#fff" stroke="{ROSE}" stroke-width="6"/>' + T(540, 1235, '+ 몇 개 공감했는지 댓글로', 58, 'j', INK))

# 2 미소 경련
pages[2] = scene(2, 1, '광대 경련', '#FFF7E6',
    camera(820, 420, .9) + flash(820, 330, 80)
    + char('bride', 330, 800, 1.15, 'joy', (6, -6)) + sweat(500, 560) + sweat(170, 580, .8)
    + bubble(120, 290, 380, '볼이\n떨려...', 54, (300, 520)),
    '계속 웃다 보면\n광대가 바들바들 떨린다.')

# 3 자연스럽게
pages[3] = scene(3, 2, '자연스럽게요~', '#E4F0F7',
    camera(860, 560, .8)
    + char('bride', 300, 820, 1.0, 'nervous', (8, -6)) + char('groom', 560, 820, 1.0, 'nervous', (-6, 8)) + sweat(420, 620) + sweat(680, 620)
    + bubble(500, 270, 420, '"자연스럽게\n웃어 주세요~"', 46, (820, 460)),
    '자연스럽게 하라니까\n더 어색해진다.')

# 4 로봇 포즈
pages[4] = scene(4, 3, '얼음 포즈', '#F4ECFA',
    char('groom', 360, 800, 1.15, 'blank', (150, 150)) + sweat(520, 580)
    + char('bride', 780, 820, .95, 'joy', (6, 120), flip=True)
    + bubble(560, 290, 400, '오빠 숨 쉬어\nㅋㅋㅋ', 50, (760, 540)),
    '카메라 앞에만 서면\n오빠는 얼음이 된다.')

# 5 드레스 갈아입기
pages[5] = scene(5, 4, '또 갈아입기', '#FFEFF2',
    dress_rack(520, 300, 440, 4) + curtain(110, 280, 360, 620, True)
    + char('bride', 300, 830, 1.0, 'nervous', (8, 100)) + sweat(420, 640),
    '드레스 갈아입고, 머리 바꾸고\n또 갈아입고...')

# 6 배고픔
pages[6] = scene(6, 5, '배꼽시계', '#FFF3D9',
    snack(450, 640) + snack(560, 660)
    + char('bride', 250, 820, .95, 'shock', (60, -10)) + char('groom', 830, 820, .95, 'shock', (8, 60), flip=True)
    + T(540, 360, '꼬르륵~', 80, 'j', '#C9886A'),
    '드레스 때문에 못 먹고\n간식만 바라본다.')

# 7 사진 고르기
pages[7] = scene(7, 6, '다 똑같은데?', '#E9F5EE',
    phone(380, 280, 320, 560, '#DCE9F6', thumbs(410, 360, 3, 5, 76, 64))
    + char('bride', 230, 790, .85, 'smug', (60, -10)) + char('groom', 850, 790, .85, 'blank', (8, 60), flip=True) + sweat(940, 630),
    '원본 고르는 날,\n다 같은 사진 같다는 오빠.')

# 8 액자 자리
pages[8] = scene(8, 7, '액자 자리 회의', '#EEF1F7',
    frame(380, 290, 320, 240, char('bride', 500, 390, .28, 'joy') + char('groom', 580, 386, .28, 'happy'))
    + sofa(280, 760, 520)
    + char('bride', 230, 820, .8, 'smug', (120, -10)) + char('groom', 850, 820, .8, 'nervous', (8, 120), flip=True),
    '액자 하나 거는 데\n가족회의가 열린다.')

# 9 마무리
pages[9] = (page_bg('#FFE4E4') + header(9, TOTAL) + hearts(18, (40, 120, 1040, 700), '#FFD0D6', 189)
    + char('bride', 400, 470, 1.15, 'joy', (6, -40)) + char('groom', 690, 460, 1.15, 'happy', (40, -8))
    + f'<rect x="110" y="820" width="860" height="420" rx="60" fill="#fff" stroke="{INK}" stroke-width="6"/>'
    + T(540, 925, '몇 개 공감했어요?', 76, 'j') + T(540, 1035, '댓글로 번호 남기기', 76, 'j', ROSE)
    + T(540, 1145, '촬영 앞둔 예비부부에게 공유!', 48, 'g', '#7A6262')
    + T(540, 1310, '@yebibubu.toon', 40, 'j', '#C49A9A'))

if __name__ == '__main__':
    render(pages, sys.argv[1] if len(sys.argv) > 1 else 'out/ep18')
