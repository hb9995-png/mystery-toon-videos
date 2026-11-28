import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from extra import *

TOTAL = 9


def shop(y0=130, y1=1060):
    """반지 매장: 연보라 벽 + 조명 + 진열장."""
    s = f'<rect x="70" y="{y0}" width="940" height="{y1 - y0}" fill="#F6EEFB"/>'
    for cx in (260, 540, 820):
        s += (f'<g stroke="{INK}" stroke-width="5"><path d="M{cx} {y0} V {y0 + 60}"/>'
              f'<path d="M{cx - 50} {y0 + 110} Q {cx} {y0 + 30} {cx + 50} {y0 + 110} Z" fill="#FFE7A8"/></g>')
    return s


def room(y0=130, y1=1060, wall='#EAF0FB'):
    return (f'<rect x="70" y="{y0}" width="940" height="{y1 - y0}" fill="{wall}"/>'
            f'<rect x="70" y="{y1 - 160}" width="940" height="160" fill="#C9C3D9"/>')


pages = {}
# 1 표지
pages[1] = (page_bg('#FFE4E4') + hearts(22, (40, 40, 1040, 1310), '#FFD0D6', 351)
    + f'<rect x="80" y="70" width="230" height="84" rx="42" fill="{ROSE}"/>' + T(195, 128, '썰툰', 50, 'j', '#fff')
    + T(80, 265, '결혼반지 고르던 날', 98, 'j', INK, 'start') + T(80, 390, '오빠가 숨긴 것', 104, 'j', ROSE, 'start')
    + panel(shop(440, 1110) + showcase(1000, 70, 1010)
            + char('bride', 330, 700, .82, 'happy', (8, -8)) + char('groom', 720, 700, .82, 'nervous', (8, -8), flip=True)
            + sweat(820, 560), '#F6EEFB', 440, 1110)
    + f'<rect x="70" y="1150" width="940" height="130" rx="65" fill="#fff" stroke="{ROSE}" stroke-width="6"/>' + T(540, 1235, '+ 마지막에 반지 고르는 팁 5가지', 54, 'j', INK))
# 2 매장
pages[2] = (page_bg() + header(2, TOTAL)
    + panel(shop() + hearts(10, (120, 300, 960, 460), '#FFC2CD', 352)
            + char('bride', 330, 560, .8, 'joy', (110, 110)) + char('groom', 730, 560, .8, 'happy', (8, -8), flip=True)
            + showcase(860)
            + bubble(130, 160, 440, '다 예뻐!!', 60, (330, 360)), '#F6EEFB')
    + caption('결혼반지 보러 간 날.\n반짝반짝 끝이 없었다.'))
# 3 많이 껴 보기
p3 = shop() + showcase(860) + char('bride', 330, 560, .8, 'smug', (110, -8)) + char('groom', 730, 560, .8, 'blank', (8, -8), flip=True)
for i, (rx, ry) in enumerate(((180, 300), (250, 230), (430, 260), (480, 340))):
    p3 += ring(rx, ry, .5, i % 2 == 0, rot=-15 + i * 10)
p3 += bubble(600, 160, 360, '이것도?\n저것도?', 54, (520, 380))
pages[3] = (page_bg() + header(3, TOTAL) + panel(p3, '#F6EEFB')
    + caption('나는 열 개쯤 껴 봤다.\n오빠는 하나만 계속 봤다.'))
# 4 속삭임
pages[4] = (page_bg() + header(4, TOTAL)
    + panel(shop() + showcase(900, 400, 1010)
            + clerk(870, 600, .74, 'happy', (8, -8), flip=True) + char('groom', 580, 600, .74, 'nervous', (8, -8))
            + char('bride', 200, 640, .7, 'shock', (8, -8)) + sweat(300, 500)
            + bubble(400, 160, 520, '이건 비밀로\n해 주세요…', 50, (580, 420)), '#F6EEFB')
    + caption('그런데 오빠가 직원분께\n뭔가 속삭였다.'))
# 5 밤에 궁금
p5_screen = (f'<rect x="392" y="330" width="296" height="80" rx="20" fill="#fff"/>' + T(540, 383, '반지 비밀', 34, 'g')
             + f'<rect x="392" y="430" width="296" height="80" rx="20" fill="#fff"/>' + T(540, 483, '남친 속삭임 뜻', 34, 'g')
             + f'<rect x="392" y="530" width="296" height="80" rx="20" fill="#FFE1E6"/>' + T(540, 583, '설마…?', 34, 'g', ROSE))
pages[5] = (page_bg() + header(5, TOTAL)
    + panel(room(wall='#2F3550') + f'<circle cx="880" cy="230" r="60" fill="#FFF2B8"/>'
            + phone(370, 260, 340, 560, inner=p5_screen)
            + char('bride', 200, 700, .72, 'nervous', (8, -8)), '#2F3550')
    + caption('집에 와서도\n계속 그 생각만 났다.'))
# 6 시치미
pages[6] = (page_bg() + header(6, TOTAL)
    + panel(room() + char('bride', 300, 680, .9, 'smug', (8, 100)) + char('groom', 740, 680, .9, 'nervous', (120, 120), flip=True)
            + sweat(850, 520) + sweat(620, 560)
            + bubble(520, 160, 440, '아무것도\n아니야!!', 56, (720, 420)), '#EAF0FB')
    + caption('물어봐도 오빠는\n시치미만 뗐다.'))
# 7 각인
p7 = speed(540, 520, '#FFE3C4', 40, 260) + hearts(12, (110, 150, 980, 330), '#FFB8C4', 357)
p7 += (f'<g stroke="{INK}" stroke-width="6"><ellipse cx="540" cy="480" rx="300" ry="190" fill="none" stroke="#E8C46A" stroke-width="60"/>'
       f'<ellipse cx="540" cy="480" rx="330" ry="220" fill="none" stroke-width="5"/><ellipse cx="540" cy="480" rx="270" ry="160" fill="none" stroke-width="5"/></g>')
p7 += f'<rect x="330" y="430" width="420" height="100" rx="30" fill="#fff" stroke="{INK}" stroke-width="5"/>' + T(540, 500, '평생 네 편', 64, 'j', ROSE)
p7 += char('bride', 330, 820, .62, 'joy', (110, 110)) + tears(330, 820, .62) + char('groom', 750, 820, .62, 'smug', (8, -8), flip=True)
pages[7] = (page_bg() + header(7, TOTAL) + panel(p7, '#FFF5E6')
    + caption('반지 받는 날 보니\n안쪽에 글자가 있었다.'))
# 8 정리
items = [('매일 낄지 생각하기', '걸리지 않는 편한 디자인으로'), ('손이 덜 부은 때 재기', '손 굵기는 하루에도 달라져요'),
         ('둘이 같이 껴 보기', '나란히 놓고 사진도 찍어 보기'), ('각인 문구 미리 정하기', '짧고 둘만 아는 말로'),
         ('관리 방법 물어보기', '세척·수리는 어떻게 하는지')]
p8 = page_bg() + header(8, TOTAL) + T(540, 230, '반지 고르는 팁 5가지', 70, 'j')
cols = [ROSE, '#8FD3C1', '#F5B860', '#96B4EE', '#C59BE6']
for i, (a, b) in enumerate(items):
    y = 290 + i * 180
    p8 += f'<rect x="80" y="{y}" width="920" height="156" rx="50" fill="#fff" stroke="{INK}" stroke-width="5"/><circle cx="160" cy="{y+78}" r="46" fill="{cols[i]}"/>'
    p8 += T(160, y + 98, str(i + 1), 56, 'j', '#fff') + T(240, y + 66, a, 52, 'j', INK, 'start') + T(240, y + 126, b, 44, 'g', '#7A6262', 'start')
p8 += T(540, 1250, '반짝임보다 편안함 먼저!', 46, 'g', ROSE)
pages[8] = p8
# 9 마무리
pages[9] = (page_bg('#FFE4E4') + header(9, TOTAL) + hearts(18, (40, 120, 1040, 700), '#FFD0D6', 359)
    + char('bride', 400, 470, 1.15, 'joy', (6, -40)) + char('groom', 690, 460, 1.15, 'happy', (40, -8))
    + f'<rect x="110" y="820" width="860" height="420" rx="60" fill="#fff" stroke="{INK}" stroke-width="6"/>'
    + T(540, 930, '저장해 두고', 76, 'j') + T(540, 1040, '반지 보러 갈 짝꿍에게 공유', 70, 'j', ROSE) + T(540, 1150, '반지 안쪽에 새기고 싶은 말은?', 48, 'g', '#7A6262')
    + T(540, 1310, '@yebibubu.toon', 40, 'j', '#C49A9A'))

if __name__ == '__main__':
    render(pages, sys.argv[1] if len(sys.argv) > 1 else 'out/ep35')
