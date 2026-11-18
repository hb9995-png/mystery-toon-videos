import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from extra import *

TOTAL = 9
QS = [  # (질문, A, B, 신부 선택, 신랑 선택, 해설)
    ('거실 벽은?', '하얀 벽\n깔끔하게', '포인트 벽\n하나 칠하기', 'B', 'A', '나는 포인트 벽 파.\n오빠는 하얀 벽 파.'),
    ('거실 한가운데엔?', '커다란\nTV 놓기', '넓은 식탁\n놓기', 'B', 'A', '오빠는 벌써\nTV 크기를 재고 있다.'),
    ('밤 조명은?', '밝은\n하얀 불', '은은한\n노란 불', 'B', 'B', '이건 둘 다 B.\n밤엔 무조건 노란 불.'),
    ('침대 자리는?', '벽에\n붙이기', '방\n가운데', 'A', 'A', '침대는 둘 다 A.\n방이 넓어 보여야 해.'),
    ('소파 색은?', '밝은\n아이보리', '때 안 타는\n회색', 'A', 'B', '나는 아이보리 파.\n오빠는 현실 회색 파.'),
    ('부엌 조리도구는?', '다 꺼내서\n걸어 두기', '서랍에\n싹 숨기기', 'B', 'B', '이건 또 둘 다 B.\n보이는 덴 깔끔하게.'),
]
A_BG, B_BG = '#FFE1E6', '#D9F2EA'

pages = {}
# 1 표지
pages[1] = (page_bg('#FFE9EC') + hearts(20, (40, 40, 1040, 1310), '#FFD3DA', 161)
    + f'<rect x="80" y="70" width="280" height="84" rx="42" fill="{ROSE}"/>' + T(220, 128, '밸런스 게임', 50, 'j', '#fff')
    + T(80, 265, '신혼집 꾸미기', 100, 'j', INK, 'start') + T(80, 390, '둘 중 하나만 골라!', 100, 'j', ROSE, 'start')
    + panel(f'<rect x="70" y="440" width="470" height="680" fill="{A_BG}"/><rect x="540" y="440" width="470" height="680" fill="{B_BG}"/>'
            + T(305, 540, 'A', 110, 'j', ROSE) + T(775, 540, 'B', 110, 'j', '#3E9C83')
            + char('bride', 305, 790, 1.0, 'smug', (10, -40)) + char('groom', 775, 790, 1.0, 'nervous', (40, -10), flip=True)
            + vs_badge(540, 760) + plant(950, 1100, .6), '#FFF7EE', 440, 1110)
    + f'<rect x="70" y="1150" width="940" height="130" rx="65" fill="#fff" stroke="{ROSE}" stroke-width="6"/>' + T(540, 1235, '+ 마지막에 우리 둘의 결과', 58, 'j', INK))

# 2~7 질문
for i, (q, a, b, bride, groom, cap) in enumerate(QS):
    no = i + 2
    inner = f'<rect x="70" y="130" width="470" height="930" fill="{A_BG}"/><rect x="540" y="130" width="470" height="930" fill="{B_BG}"/>'
    inner += f'<rect x="100" y="160" width="880" height="130" rx="40" fill="#fff" stroke="{INK}" stroke-width="5"/>'
    inner += f'<rect x="124" y="190" width="120" height="70" rx="35" fill="{ROSE}"/>' + T(184, 241, f'Q{i + 1}', 48, 'j', '#fff')
    inner += T(610, 246, q, 54, 'j', INK)
    for side, txt, cx, col in (('A', a, 305, ROSE), ('B', b, 775, '#3E9C83')):
        inner += f'<rect x="{cx - 200}" y="330" width="400" height="230" rx="36" fill="#fff" stroke="{col}" stroke-width="6"/>'
        inner += T(cx - 172, 382, side, 44, 'j', col, 'start') + T(cx, 455, txt, 56, 'j', INK)
    if bride == groom:
        cx = 305 if bride == 'A' else 775
        sh = 30 if cx == 305 else -15
        inner += char('bride', cx - 105 + sh, 820, .78, 'joy', (6, -50)) + char('groom', cx + 105 + sh, 815, .78, 'joy', (50, -6))
        inner += hearts(6, (cx - 200, 600, cx + 200, 680), '#FF9FB0', no + 160)
        other = 775 if cx == 305 else 305
        inner += T(other, 820, '(아무도 없음)', 50, 'g', '#9A9090')
    else:
        bx = 305 if bride == 'A' else 775; gx = 775 if bx == 305 else 305
        inner += char('bride', bx, 800, .95, 'smug' if i % 2 == 0 else 'happy', (8, -45), flip=bx > 540)
        inner += char('groom', gx, 800, .95, 'nervous' if i == 3 else 'happy', (45, -8), flip=gx > 540)
        inner += vs_badge(540, 760, 64)
    pages[no] = page_bg() + header(no, TOTAL) + panel(inner, '#FFF7EE') + caption(cap)

# 8 결과
res = page_bg('#FFF5D8') + speed(540, 900, '#FFE9B8', 40, 300) + header(8, TOTAL) + T(540, 240, '우리 둘의 결과', 80, 'j', INK)
res += f'<rect x="120" y="300" width="840" height="190" rx="60" fill="#fff" stroke="{INK}" stroke-width="6"/>'
res += T(540, 380, '6개 중 같은 답은', 58, 'g', '#7A6262') + T(540, 460, '딱 절반, 3개', 84, 'j', ROSE)
res += char('bride', 400, 820, 1.05, 'joy', (6, -40)) + char('groom', 680, 810, 1.05, 'joy', (40, -6)) + hearts(8, (300, 560, 780, 700), '#FF9FB0', 168)
res += f'<rect x="70" y="1150" width="940" height="140" rx="60" fill="#fff" stroke="{INK}" stroke-width="6"/>'
res += T(540, 1240, '다른 건 방 하나씩 맡아 꾸미기로 했다', 52, 'j', INK)
pages[8] = res

# 9 마무리
pages[9] = (page_bg('#FFE4E4') + header(9, TOTAL) + hearts(18, (40, 120, 1040, 700), '#FFD0D6', 169)
    + char('bride', 400, 470, 1.15, 'happy', (6, -40)) + char('groom', 690, 460, 1.15, 'smug', (40, -8))
    + f'<rect x="110" y="820" width="860" height="420" rx="60" fill="#fff" stroke="{INK}" stroke-width="6"/>'
    + T(540, 925, '댓글로 1A 2B 3A …', 74, 'j') + T(540, 1035, '같이 꾸밀 사람 태그하기', 76, 'j', ROSE)
    + T(540, 1145, '취향이 몇 개나 맞는지 확인해 보세요', 50, 'g', '#7A6262')
    + T(540, 1310, '@yebibubu.toon', 40, 'j', '#C49A9A'))

if __name__ == '__main__':
    render(pages, sys.argv[1] if len(sys.argv) > 1 else 'out/ep16')
