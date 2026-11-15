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


def window(x, y, w=260, h=260, sun=False):
    s = f'<g stroke="{INK}" stroke-width="5"><rect x="{x}" y="{y}" width="{w}" height="{h}" fill="#CFE9F7"/><path d="M{x + w / 2} {y} V {y + h} M {x} {y + h / 2} H {x + w}"/></g>'
    if sun: s += f'<circle cx="{x + w * .75}" cy="{y + h * .25}" r="34" fill="#FFD36A" stroke="{INK}" stroke-width="4"/>'
    return s


def floor(y=880):
    return f'<rect x="70" y="{y}" width="940" height="300" fill="#E9D6BE"/><path d="M70 {y} H 1010" stroke="{INK}" stroke-width="5"/>'


pages = {}
# 1 표지
pages[1] = (page_bg('#FFE4E4') + hearts(22, (40, 40, 1040, 1310), '#FFD0D6', 91)
    + f'<rect x="80" y="70" width="240" height="84" rx="42" fill="{ROSE}"/>' + T(200, 128, '공감 주의', 50, 'j', '#fff')
    + T(80, 265, '신혼집 보러 가면', 108, 'j', INK, 'start') + T(80, 395, '생기는 일 7가지', 108, 'j', ROSE, 'start')
    + panel(floor(960) + door(130, 500, 200, 460) + window(700, 520, 230, 230, True)
            + char('bride', 450, 860, .95, 'blank', (6, -6)) + char('groom', 640, 850, .95, 'nervous', (8, -8)) + sweat(760, 700), '#FFF7EE', 440, 1110)
    + f'<rect x="70" y="1150" width="940" height="130" rx="65" fill="#fff" stroke="{ROSE}" stroke-width="6"/>' + T(540, 1235, '+ 몇 개 공감했는지 세어 보기', 58, 'j', INK))

# 2 사진이랑 다름
pages[2] = scene(2, 1, '사진이랑 달라', '#F4ECFA',
    floor() + paper(110, 300, 360, 430, '매물 사진', [], 40, -6)
    + T(290, 560, '넓음!', 64, 'j', ROSE)
    + char('bride', 590, 820, 1.0, 'shock', (60, -10)) + char('groom', 820, 820, 1.0, 'shock', (8, 60)) + sweat(680, 610) + sweat(910, 600),
    '사진에선 넓었는데\n둘이 서니까 꽉 찼다.')

# 3 줄자
pages[3] = scene(3, 2, '줄자는 필수', '#E4F0F7',
    floor() + fridge(740, 420, 220, 440) + tape(440, 930, 300)
    + char('groom', 230, 780, 1.0, 'smug', (120, -10)) + bubble(480, 290, 430, '냉장고 자리\n90 맞지?', 54, (560, 520)),
    '집 구경은 뒷전,\n냉장고 자리부터 잰다.')

# 4 해 드는 방향
pages[4] = scene(4, 3, '아는 척', '#FFF7E6',
    floor() + window(620, 300, 300, 300, True)
    + char('bride', 360, 800, 1.15, 'smug', (150, -10)) + bubble(130, 290, 420, '여기 남향\n맞죠? (모름)', 54, (330, 520)),
    '해 드는 방향 묻는 척\n사실 잘 모른다.')

# 5 부모님 영상통화
ph_in = (f'<rect x="595" y="400" width="220" height="200" rx="24" fill="#FFF3EA" stroke="{INK}" stroke-width="3"/>' + T(705, 520, '엄마', 50, 'j', ROSE)
         + f'<rect x="580" y="630" width="250" height="110" rx="24" fill="#fff" stroke="{INK}" stroke-width="3"/>' + T(705, 676, '화장실 다시', 38) + T(705, 722, '보여줘 봐~', 38))
pages[5] = scene(5, 4, '영상통화', '#F1ECFB',
    phone(555, 300, 300, 560, '#DCE9F6', ph_in)
    + char('groom', 330, 760, 1.05, 'nervous', (100, -10)) + sweat(470, 600) + sweat(200, 620, .8),
    '부모님께 영상통화로\n집 한 바퀴 투어 시켜 드림.')

# 6 동네 한 바퀴
pages[6] = scene(6, 5, '동네 탐방', '#FFF3D9',
    char('bride', 300, 700, 1.0, 'joy', (70, -10)) + char('groom', 780, 690, 1.0, 'joy', (10, -70)) + hearts(6, (380, 320, 700, 520), '#FF9FB0', 96)
    + chicken_box(360, 880, 360) + bubble(560, 270, 400, '치킨집\n가까워!', 56, (720, 470)),
    '역까지 거리보다\n치킨집 거리를 먼저 본다.')

# 7 예산
rows = [('마음에 든 집', '예산 초과', ROSE), ('예산 맞는 집', '마음이...', '#7A8090'), ('둘 다 맞는 집', '이미 나감', ROSE)]
pages[7] = scene(7, 6, '예산의 벽', '#EEF1F7',
    paper(110, 300, 520, 520, '오늘 본 집', rows, 42, -4)
    + char('bride', 790, 780, 1.0, 'blank', (60, -10)) + sweat(910, 620),
    '마음에 들면 예산 초과,\n예산 맞으면 마음이...')

# 8 결국 첫 집
pages[8] = scene(8, 7, '결국 그 집', '#FFEFF2',
    floor() + door(150, 340, 220, 520) + hearts(10, (420, 280, 980, 600), '#FF9FB0', 98)
    + char('bride', 560, 820, 1.05, 'joy', (6, 130)) + char('groom', 820, 810, 1.05, 'joy', (130, -10)),
    '열 군데를 보고\n첫 번째 집으로 갔다.')

# 9 마무리
pages[9] = (page_bg('#FFE4E4') + header(9, TOTAL) + hearts(18, (40, 120, 1040, 700), '#FFD0D6', 99)
    + char('bride', 400, 470, 1.15, 'joy', (6, -40)) + char('groom', 690, 460, 1.15, 'happy', (40, -8))
    + f'<rect x="110" y="820" width="860" height="420" rx="60" fill="#fff" stroke="{INK}" stroke-width="6"/>'
    + T(540, 925, '몇 개 공감했어요?', 76, 'j') + T(540, 1035, '댓글로 번호 남기기', 76, 'j', ROSE)
    + T(540, 1145, '같이 집 보러 다니는 사람한테 공유!', 48, 'g', '#7A6262')
    + T(540, 1310, '@yebibubu.toon', 40, 'j', '#C49A9A'))

if __name__ == '__main__':
    render(pages, sys.argv[1] if len(sys.argv) > 1 else 'out/ep09')
