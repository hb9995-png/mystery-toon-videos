import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from extra import *

TOTAL = 9
QS = [  # (질문, A, B, 신부 선택, 신랑 선택, 해설)
    ('저녁 먹고 설거지는?', '먹자마자\n바로 한다', '모아 뒀다가\n한 번에', 'A', 'B', '나는 바로 파.\n오빠는 내일의 오빠 믿는 파.'),
    ('잘 때 이불은?', '큰 이불 하나\n같이 덮기', '각자 이불\n따로 덮기', 'B', 'B', '이건 둘 다 B.\n이불 뺏기 전쟁 끝.'),
    ('쉬는 주말엔?', '집에서\n하루 종일 뒹굴', '밖에 나가서\n맛집 탐방', 'B', 'A', '나는 나가고 싶고\n오빠는 소파랑 한 몸.'),
    ('방 온도는?', '조금 춥게\n시원하게', '조금 덥게\n따뜻하게', 'B', 'A', '리모컨 쟁탈전은\n오늘도 계속된다.'),
    ('퇴근 후 저녁은?', '간단하게\n집밥 해 먹기', '오늘만은\n배달 시키기', 'B', 'B', '이건 또 둘 다 B.\n메뉴 고르다 30분.'),
    ('택배 상자는?', '뜯자마자\n바로 버리기', '모아 뒀다가\n분리수거 날', 'A', 'B', '현관에 상자 탑이\n점점 높아지는 중.'),
]
A_BG, B_BG = '#FFE1E6', '#D9F2EA'

pages = {}
# 1 표지
pages[1] = (page_bg('#FFE9EC') + hearts(20, (40, 40, 1040, 1310), '#FFD3DA', 71)
    + f'<rect x="80" y="70" width="280" height="84" rx="42" fill="{ROSE}"/>' + T(220, 128, '밸런스 게임', 50, 'j', '#fff')
    + T(80, 265, '신혼 살림 밸런스 게임', 92, 'j', INK, 'start') + T(80, 385, '우리 집은 어느 쪽?', 100, 'j', ROSE, 'start')
    + panel(f'<rect x="70" y="440" width="470" height="680" fill="{A_BG}"/><rect x="540" y="440" width="470" height="680" fill="{B_BG}"/>'
            + T(305, 540, 'A', 110, 'j', ROSE) + T(775, 540, 'B', 110, 'j', '#3E9C83')
            + char('bride', 305, 790, 1.0, 'smug', (10, -40)) + char('groom', 775, 790, 1.0, 'nervous', (40, -10), flip=True)
            + vs_badge(540, 760), '#FFF7EE', 440, 1110)
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
        inner += char('bride', cx - 105, 820, .78, 'joy', (6, -50)) + char('groom', cx + 105, 815, .78, 'joy', (50, -6))
        inner += hearts(6, (cx - 200, 600, cx + 200, 680), '#FF9FB0', no + 70)
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
res += T(540, 380, '6개 중 같은 답은', 58, 'g', '#7A6262') + T(540, 460, '딱 2개', 84, 'j', ROSE)
res += char('bride', 400, 820, 1.05, 'joy', (6, -40)) + char('groom', 680, 810, 1.05, 'joy', (40, -6)) + hearts(8, (300, 560, 780, 700), '#FF9FB0', 78)
res += f'<rect x="70" y="1150" width="940" height="140" rx="60" fill="#fff" stroke="{INK}" stroke-width="6"/>'
res += T(540, 1240, '다른 건 정하면 되고, 같은 건 즐기면 된다', 52, 'j', INK)
pages[8] = res

# 9 마무리
pages[9] = (page_bg('#FFE4E4') + header(9, TOTAL) + hearts(18, (40, 120, 1040, 700), '#FFD0D6', 79)
    + char('bride', 400, 470, 1.15, 'happy', (6, -40)) + char('groom', 690, 460, 1.15, 'smug', (40, -8))
    + f'<rect x="110" y="820" width="860" height="420" rx="60" fill="#fff" stroke="{INK}" stroke-width="6"/>'
    + T(540, 925, '댓글로 1A 2B 3A …', 74, 'j') + T(540, 1035, '같이 살 사람 태그하기', 76, 'j', ROSE)
    + T(540, 1145, '둘이 몇 개나 같은지 맞춰 보세요', 50, 'g', '#7A6262')
    + T(540, 1310, '@yebibubu.toon', 40, 'j', '#C49A9A'))

if __name__ == '__main__':
    render(pages, sys.argv[1] if len(sys.argv) > 1 else 'out/ep07')
