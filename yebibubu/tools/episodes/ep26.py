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



def moon(x, y, r=70):
    return (f'<circle cx="{x}" cy="{y}" r="{r}" fill="#FFF2B8" stroke="{INK}" stroke-width="5"/>'
            f'<circle cx="{x + r * .45}" cy="{y - r * .25}" r="{r * .85}" fill="#3E4170"/>')


def bowl(x, y, w=240):
    """라면 그릇. (x, y) 는 그릇 윗면 가운데."""
    st = ''.join(f'<path d="M{x + k * 50} {y - 30} q 20 -30 0 -60 t 0 -60" fill="none" stroke="#B9B2C4" stroke-width="6"/>' for k in (-1, 0, 1))
    noodles = ''.join(f'<path d="M{x - w / 2 + 30 + k * 30} {y + 6} q 15 -18 30 0" fill="none" stroke="#E8B04B" stroke-width="6"/>' for k in range(int((w - 60) / 30)))
    return (st + f'<g stroke="{INK}" stroke-width="5"><path d="M{x - w / 2} {y} H {x + w / 2} Q {x + w / 2} {y + w * .5} {x} {y + w * .5} Q {x - w / 2} {y + w * .5} {x - w / 2} {y} z" fill="#F07B5A"/>'
            f'<ellipse cx="{x}" cy="{y}" rx="{w / 2}" ry="{w * .1}" fill="#FFE1A6"/></g>' + noodles)


def hall(y=860):
    return (f'<rect x="70" y="{y}" width="940" height="300" fill="#F3E3EE"/><path d="M70 {y} H 1010" stroke="{INK}" stroke-width="5"/>'
            f'<rect x="430" y="{y}" width="220" height="300" fill="#fff" stroke="{INK}" stroke-width="4"/>')


pages = {}
# 1 표지
pages[1] = (page_bg('#FFE4E4') + hearts(22, (40, 40, 1040, 1310), '#FFD0D6', 261)
    + f'<rect x="80" y="70" width="240" height="84" rx="42" fill="{ROSE}"/>' + T(200, 128, '공감 주의', 50, 'j', '#fff')
    + T(80, 265, '결혼식 당일', 108, 'j', INK, 'start') + T(80, 395, '생기는 일 7가지', 108, 'j', ROSE, 'start')
    + panel(hall(960) + chandelier(540, 640, .8)
            + char('bride', 400, 800, .85, 'joy', (6, -6)) + char('groom', 680, 800, .85, 'nervous', (8, -8), flip=True) + sweat(790, 650), '#FFF7EE', 440, 1110)
    + f'<rect x="70" y="1150" width="940" height="130" rx="65" fill="#fff" stroke="{ROSE}" stroke-width="6"/>' + T(540, 1235, '+ 몇 개 공감했는지 댓글로', 58, 'j', INK))

# 2 새벽 기상
pages[2] = scene(2, 1, '해 뜨기 전 기상', '#3E4170',
    moon(840, 340) + f'<rect x="70" y="820" width="940" height="400" fill="#5A5C8C"/>'
    + char('bride', 480, 700, 1.15, 'blank', (8, -8)) + T(220, 480, 'Zzz', 80, 'j', '#C9C3E0'),
    '식 날 아침은\n해 뜨기 전에 시작.')

# 3 배고픔
pages[3] = scene(3, 2, '꼬르륵', '#FFF1D6',
    floor(900, '#F2D9C4') + char('groom', 520, 680, 1.15, 'shock', (60, 60)) + sweat(680, 540)
    + T(830, 820, '꼬르륵', 70, 'j', '#C0392B') + T(230, 820, '꼬르륵', 56, 'j', '#C0392B'),
    '정작 신랑 신부는\n밥을 못 먹는다.')

# 4 드레스
pages[4] = scene(4, 3, '한 걸음이 어려워', '#F4ECFA',
    floor(920, '#E5DAF0') + char('bride', 440, 660, 1.15, 'nervous', (40, 40)) + sweat(600, 520) + sweat(300, 540, .8)
    + bubble(640, 300, 330, '한 발짝만…', 52, (620, 520)),
    '드레스 입고 걷기,\n생각보다 힘들다.')

# 5 인사
pages[5] = scene(5, 4, '인사 무한 반복', '#FFEFF2',
    hall(900) + char('bride', 360, 700, 1.0, 'joy', (6, -6)) + char('groom', 700, 700, 1.0, 'joy', (8, -8), flip=True)
    + bubble(120, 290, 380, '와 줘서 고마워!', 44, (300, 520)) + bubble(580, 330, 380, '와 줘서 고마워!', 44, (720, 540)),
    '같은 인사를\n백 번쯤 한다.')

# 6 부모님 눈물
pages[6] = scene(6, 5, '눈물 참기 실패', '#EAF4F8',
    hall(900) + char('momG', 330, 660, 1.0, 'nervous', (8, -8)) + tears(330, 660, 1.0)
    + char('bride', 720, 680, 1.0, 'nervous', (8, -8), flip=True) + tears(720, 680, 1.0),
    '엄마 얼굴 보는 순간\n눈물이 터진다.')

# 7 기억 없음
pages[7] = scene(7, 6, '기억이 안 나', '#EEF1F7',
    camera(840, 470, .8) + char('bride', 330, 700, 1.0, 'blank', (6, -6)) + char('groom', 600, 700, 1.0, 'blank', (8, -8), flip=True)
    + T(190, 420, '?', 90, 'j', '#9A8FB5') + T(470, 380, '?', 90, 'j', '#9A8FB5') + T(720, 420, '?', 80, 'j', '#9A8FB5'),
    '식이 어떻게 갔는지\n하나도 기억 안 난다.')

# 8 라면
pages[8] = scene(8, 7, '최고의 한 끼', '#FFF5E6',
    f'<rect x="70" y="840" width="940" height="400" fill="#E9D6BE"/>'
    + char('bride', 300, 640, 1.0, 'joy', (60, 6)) + char('groom', 780, 640, 1.0, 'joy', (6, 60), flip=True)
    + bowl(540, 860, 280) + T(540, 300, '(집에 와서)', 54, 'g', '#7A8090'),
    '집에 와서 먹는 라면이\n제일 맛있다.')

# 9 마무리
pages[9] = (page_bg('#FFE4E4') + header(9, TOTAL) + hearts(18, (40, 120, 1040, 700), '#FFD0D6', 269)
    + char('bride', 400, 470, 1.15, 'joy', (6, -40)) + char('groom', 690, 460, 1.15, 'happy', (40, -8))
    + f'<rect x="110" y="820" width="860" height="420" rx="60" fill="#fff" stroke="{INK}" stroke-width="6"/>'
    + T(540, 925, '몇 개 공감했어요?', 76, 'j') + T(540, 1035, '댓글로 번호 남기기', 76, 'j', ROSE)
    + T(540, 1145, '곧 식 올리는 예비부부에게 공유!', 48, 'g', '#7A6262')
    + T(540, 1310, '@yebibubu.toon', 40, 'j', '#C49A9A'))

if __name__ == '__main__':
    render(pages, sys.argv[1] if len(sys.argv) > 1 else 'out/ep26')
