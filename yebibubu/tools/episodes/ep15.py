import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from extra import *

TOTAL = 9


def shop(y0=130, y1=1060):
    """드레스샵 벽과 바닥."""
    return (f'<rect x="70" y="{y0}" width="940" height="{y1 - y0}" fill="#FBEFF2"/>'
            f'<rect x="70" y="{y1 - 170}" width="940" height="170" fill="#EBD9CF"/>'
            + chandelier(540, y0 + 10, .8))


pages = {}
# 1 표지
pages[1] = (page_bg('#FFE4E4') + hearts(22, (40, 40, 1040, 1310), '#FFD0D6', 151)
    + f'<rect x="80" y="70" width="270" height="84" rx="42" fill="{ROSE}"/>' + T(215, 128, '드레스 썰', 50, 'j', '#fff')
    + T(80, 265, '드레스 투어 갔다가', 100, 'j', INK, 'start') + T(80, 390, '오빠가 먼저 운 썰', 106, 'j', ROSE, 'start')
    + panel(shop(440, 1110) + curtain(160, 540, 360, 520, True) + char('bride', 340, 790, .95, 'happy', (6, -40))
            + char('groom', 780, 800, 1.0, 'shock', (60, 20), flip=True) + tears(780, 800, .85), '#FBEFF2', 440, 1110)
    + f'<rect x="70" y="1150" width="940" height="130" rx="65" fill="#fff" stroke="{ROSE}" stroke-width="6"/>' + T(540, 1235, '+ 드레스 투어 전 챙길 5가지', 58, 'j', INK))
# 2
pages[2] = (page_bg() + header(2, TOTAL)
    + panel(shop() + dress_rack(110, 360, 360, 4) + char('bride', 330, 700, 1.05, 'joy', (6, -40))
            + char('groom', 760, 700, 1.05, 'blank', (8, -8), flip=True)
            + bubble(520, 180, 460, '다 똑같은\n흰색 아니야?', 54, (740, 470)), '#FBEFF2')
    + caption('드디어 드레스 투어 날.\n오빠는 시큰둥했다.'))
# 3
pages[3] = (page_bg() + header(3, TOTAL)
    + panel(shop() + sofa(520, 640, 380) + char('groom', 710, 600, 1.0, 'blank', (100, 90), flip=True)
            + phone(560, 770, 90, 140) + char('bride', 290, 660, 1.0, 'smug', (8, -8))
            + bubble(470, 190, 480, '응 예뻐~\n(폰 보는 중)', 54, (700, 440)), '#FBEFF2')
    + caption('첫 번째 드레스.\n오빠는 폰만 보고 있었다.'))
# 4
pages[4] = (page_bg() + header(4, TOTAL)
    + panel(shop() + mirror(640, 300, 260, 540) + char('bride', 380, 680, 1.25, 'nervous', (-20, 20))
            + sweat(560, 470) + sweat(220, 500, .8) + T(380, 260, '(숨 참는 중...)', 62, 'g', '#7A6262'), '#FBEFF2')
    + caption('두 번째 드레스는\n숨쉬기가 조금 힘들었다.'))
# 5
pages[5] = (page_bg() + header(5, TOTAL)
    + panel(speed(540, 600, '#FFE3EA', 44, 320) + curtain(250, 210, 580, 760, True)
            + hearts(10, (120, 160, 960, 420), '#FFB3C1', 155) + char('bride', 540, 640, 1.35, 'happy', (6, -40)), '#FFF5F7')
    + caption('세 번째 드레스.\n커튼이 천천히 열렸다.'))
# 6
pages[6] = (page_bg() + header(6, TOTAL)
    + panel(speed(540, 640, '#E3E8F2', 44, 330) + char('groom', 540, 650, 1.45, 'shock', (30, -30))
            + phone(160, 860, 110, 170) + T(220, 820, '(툭)', 70, 'j', '#7A8090') + sweat(740, 460), '#EEF1F7')
    + caption('오빠 손에서\n폰이 툭 떨어졌다.'))
# 7
pages[7] = (page_bg() + header(7, TOTAL)
    + panel(hearts(12, (100, 160, 980, 600), '#FFD0D6', 157) + char('bride', 360, 710, 1.15, 'joy', (-40, 120))
            + char('groom', 710, 700, 1.15, 'nervous', (120, -10)) + tears(710, 700, 1.0)
            + bubble(140, 170, 800, '...이거다.\n이거 입고 결혼하자', 58, (640, 470)), '#FFF5D8')
    + caption('다 똑같은 흰색이라던\n사람, 맞나요?'))
# 8 정리
items = [('원하는 스타일 사진', '마음에 드는 라인 사진 모아 가기'), ('사진 촬영 가능 여부', '찍어도 되는지 샵에 미리 묻기'),
         ('피팅 준비물', '필요한 게 있는지 미리 확인하기'), ('함께 갈 사람', '동행 인원 정해서 미리 알리기'),
         ('바로 메모', '입어 본 드레스 특징 적어 두기')]
p8 = page_bg() + header(8, TOTAL) + T(540, 230, '드레스 투어 전 챙길 5가지', 70, 'j')
cols = [ROSE, '#8FD3C1', '#F5B860', '#96B4EE', '#C59BE6']
for i, (a, b) in enumerate(items):
    y = 290 + i * 180
    p8 += f'<rect x="80" y="{y}" width="920" height="156" rx="50" fill="#fff" stroke="{INK}" stroke-width="5"/><circle cx="160" cy="{y+78}" r="46" fill="{cols[i]}"/>'
    p8 += T(160, y + 98, str(i + 1), 56, 'j', '#fff') + T(240, y + 66, a, 52, 'j', INK, 'start') + T(240, y + 126, b, 44, 'g', '#7A6262', 'start')
p8 += T(540, 1250, '예비 신랑도 폰은 잠깐 넣어 두기!', 48, 'g', ROSE)
pages[8] = p8
# 9 마무리
pages[9] = (page_bg('#FFE4E4') + header(9, TOTAL) + hearts(18, (40, 120, 1040, 700), '#FFD0D6', 159)
    + char('bride', 400, 470, 1.15, 'joy', (6, -40)) + char('groom', 690, 460, 1.15, 'happy', (40, -8))
    + f'<rect x="110" y="820" width="860" height="420" rx="60" fill="#fff" stroke="{INK}" stroke-width="6"/>'
    + T(540, 930, '저장해 두고', 76, 'j') + T(540, 1040, '예비 배우자에게 공유하기', 76, 'j', ROSE) + T(540, 1150, '여러분 드레스 투어 썰도 댓글로!', 50, 'g', '#7A6262')
    + T(540, 1310, '@yebibubu.toon', 40, 'j', '#C49A9A'))

if __name__ == '__main__':
    render(pages, sys.argv[1] if len(sys.argv) > 1 else 'out/ep15')
