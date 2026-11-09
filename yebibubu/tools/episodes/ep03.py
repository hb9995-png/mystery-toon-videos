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


pages = {}
# 1 표지
cover_in = (chandelier(540, 530, .8) + char('bride', 380, 800, 1.0, 'blank', (6, -6)) + char('groom', 700, 790, 1.0, 'blank', (8, -8))
            + paper(150, 930, 260, 200, '견적서', [], 34, -8) + paper(680, 935, 260, 200, '하객 명단', [], 34, 7) + sweat(500, 700) + sweat(830, 690))
pages[1] = (page_bg('#FFE4E4') + hearts(22, (40, 40, 1040, 1310), '#FFD0D6', 31)
    + f'<rect x="80" y="70" width="240" height="84" rx="42" fill="{ROSE}"/>' + T(200, 128, '공감 주의', 50, 'j', '#fff')
    + T(80, 265, '결혼 준비하면', 110, 'j', INK, 'start') + T(80, 395, '생기는 일 7가지', 110, 'j', ROSE, 'start')
    + panel(cover_in, '#FFF7EE', 440, 1110)
    + f'<rect x="70" y="1150" width="940" height="130" rx="65" fill="#fff" stroke="{ROSE}" stroke-width="6"/>' + T(540, 1235, '+ 몇 개 공감했는지 세어 보기', 58, 'j', INK))

# 2 웨딩홀 투어
pages[2] = scene(2, 1, '웨딩홀 투어', '#F4ECFA',
    chandelier(220, 470, .8) + chandelier(540, 450, .8) + chandelier(860, 470, .8)
    + char('bride', 360, 760, 1.0, 'blank', (6, -6)) + char('groom', 720, 750, 1.0, 'blank', (8, -8))
    + bubble(560, 290, 420, '여기 아까\n거기 아니야?', 54, (700, 560)),
    '세 번째 홀부터는\n다 똑같아 보인다.')

# 3 견적서
rows = [('드레스 피팅', '추가', ROSE), ('원본 사진', '추가', ROSE), ('헬퍼 이모님', '추가', ROSE), ('얼리 스타트', '추가', ROSE), ('부케', '추가', ROSE)]
pages[3] = scene(3, 2, '스드메 견적', '#FFF0DC',
    paper(120, 290, 480, 600, '견적서', rows, 44, -4)
    + char('bride', 790, 700, 1.0, 'shock', (60, -10)) + sweat(920, 560) + sweat(660, 600, .8),
    '견적서에서 제일 많이\n보이는 글자: 추가')

# 4 연락 끊긴 친구
ph_in = (f'<rect x="580" y="390" width="250" height="110" rx="24" fill="#FFE36A" stroke="{INK}" stroke-width="3"/>' + T(705, 438, '잘 지냈어?', 42)
         + T(705, 484, '사실 나...', 42)
         + f'<rect x="580" y="530" width="250" height="70" rx="24" fill="#fff" stroke="{INK}" stroke-width="3"/>' + T(705, 577, '...?', 42))
pages[4] = scene(4, 3, '하객 명단', '#E4F0F7',
    phone(555, 300, 300, 560, '#DCE9F6', ph_in)
    + char('groom', 330, 700, 1.05, 'nervous', (100, -10)) + sweat(470, 560) + sweat(200, 590, .8),
    '청첩장 주려고 연락하니\n5년 만의 안부 인사.')

# 5 엄마 장부
pages[5] = scene(5, 4, '전설의 장부', '#F1ECFB',
    hearts(8, (90, 300, 990, 1040), '#E3DAF7', 5)
    + char('momG', 360, 700, 1.15, 'smug', (110, -10)) + notebook(560, 660, 340, 240, '축의금 장부', -8)
    + bubble(150, 290, 780, '그 집 딸 결혼할 때\n우리가 얼마 했더라~', 58, (380, 540)),
    '엄마 서랍에서\n전설의 장부가 나왔다.')

# 6 청첩장 모임 달력
cal = f'<rect x="130" y="290" width="520" height="560" rx="24" fill="#fff" stroke="{INK}" stroke-width="5"/>'
cal += f'<rect x="130" y="290" width="520" height="90" rx="24" fill="{ROSE}" stroke="{INK}" stroke-width="5"/>' + T(390, 352, '이번 달', 48, 'j', '#fff')
for r in range(5):
    for c in range(7):
        x = 150 + c * 70; y = 400 + r * 88
        cal += f'<rect x="{x}" y="{y}" width="60" height="76" rx="10" fill="#FFF3EA" stroke="#E3CFC5" stroke-width="3"/>'
        if (r * 7 + c) % 6 != 5:
            cal += f'<path transform="translate({x + 30} {y + 44}) scale(.75)" d="M0 10 C -30 -16 -16 -36 0 -20 C 16 -36 30 -16 0 10 Z" fill="#FF9FB0"/>'
pages[6] = scene(6, 5, '청첩장 모임', '#FFEFF2',
    cal + char('groom', 820, 720, .95, 'blank', (8, -50)) + sweat(940, 600),
    '이번 달 저녁 약속\n빈칸이 없다.')

# 7 드레스
pages[7] = scene(7, 6, '드레스 투어', '#FFF7E6',
    speed(330, 700, '#FFEFC4', 44, 300) + hearts(10, (100, 300, 560, 700), '#FFD0D6', 7)
    + char('bride', 330, 690, 1.2, 'happy', (8, -8)) + char('groom', 780, 730, 1.0, 'joy', (90, 70)) + tears(780, 730, 1.0)
    + bubble(640, 290, 330, '예쁘다...', 56, (760, 560)),
    '드레스 처음 입은 날\n오빠가 먼저 울었다.')

# 8 치킨 휴전
pages[8] = scene(8, 7, '싸우다가도', '#FFF3D9',
    char('bride', 300, 680, 1.0, 'joy', (70, -10)) + char('groom', 780, 670, 1.0, 'joy', (10, -70)) + hearts(6, (380, 320, 700, 520), '#FF9FB0', 8)
    + chicken_box(360, 870, 360),
    '청첩장 문구로 싸우다가도\n치킨 오면 휴전.')

# 9 마무리
pages[9] = (page_bg('#FFE4E4') + header(9, TOTAL) + hearts(18, (40, 120, 1040, 700), '#FFD0D6', 39)
    + char('bride', 400, 470, 1.15, 'joy', (6, -40)) + char('groom', 690, 460, 1.15, 'happy', (40, -8))
    + f'<rect x="110" y="820" width="860" height="420" rx="60" fill="#fff" stroke="{INK}" stroke-width="6"/>'
    + T(540, 925, '몇 개 공감했어요?', 76, 'j') + T(540, 1035, '댓글로 번호 남기기', 76, 'j', ROSE)
    + T(540, 1145, '같이 준비하는 사람한테 공유해 주세요', 48, 'g', '#7A6262')
    + T(540, 1310, '@yebibubu.toon', 40, 'j', '#C49A9A'))

if __name__ == '__main__':
    render(pages, sys.argv[1] if len(sys.argv) > 1 else 'out/ep03')
