import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from extra import *

TOTAL = 10
pages = {}
# 1 표지
pages[1] = (page_bg('#FFE4E4') + hearts(22, (40, 40, 1040, 1310), '#FFD0D6', 61)
    + f'<rect x="80" y="70" width="230" height="84" rx="42" fill="{ROSE}"/>' + T(195, 128, '명절 썰', 50, 'j', '#fff')
    + T(80, 265, '결혼하고 첫 명절,', 108, 'j', INK, 'start') + T(80, 395, '어느 집부터 가?', 108, 'j', ROSE, 'start')
    + panel(phone(110, 520, 220, 380) + phone(750, 520, 220, 380)
            + char('bride', 430, 800, .95, 'shock', (110, -6)) + char('groom', 650, 790, .95, 'shock', (6, 110), flip=True)
            + sweat(520, 640) + sweat(760, 630), '#FFF7EE', 440, 1110)
    + f'<rect x="70" y="1150" width="940" height="130" rx="65" fill="#fff" stroke="{ROSE}" stroke-width="6"/>' + T(540, 1235, '+ 마지막에 첫 명절 전 정할 5가지', 58, 'j', INK))
# 2
pages[2] = (page_bg() + header(2, TOTAL)
    + panel(calendar(130, 330, 360, mark=(9, 10, 11), title='명절') + char('bride', 760, 760, 1.05, 'happy', (8, 120))
            + bubble(520, 170, 440, '오빠, 이번 명절\n어디부터 가?', 54, (720, 470)), '#EAF3F7')
    + caption('결혼하고 첫 명절이 다가왔다.\n문제는 순서였다.'))
# 3
pages[3] = (page_bg() + header(3, TOTAL)
    + panel(hearts(10, (90, 160, 990, 1040), '#FFE0CC', 63) + char('momB', 540, 660, 1.45, 'happy', (8, 130))
            + bubble(140, 170, 800, '아가~ 명절엔\n아침 일찍 오렴~', 64, (600, 430)), '#FFF3E6')
    + caption('시어머님 전화가 먼저 왔다.'))
# 4
pages[4] = (page_bg() + header(4, TOTAL)
    + panel(hearts(10, (90, 160, 990, 1040), '#E9E1FA', 64) + char('momG', 540, 660, 1.45, 'joy', (130, 8))
            + bubble(140, 170, 800, '우리 딸~ 명절 첫날\n점심은 엄마랑 먹자!', 62, (480, 430)), '#F1ECFB')
    + caption('5분 뒤, 우리 엄마 전화도 왔다.'))
# 5
pages[5] = (page_bg() + header(5, TOTAL)
    + panel(speed(540, 640, '#FFE9E9', 50, 320) + char('bride', 360, 680, 1.15, 'shock') + char('groom', 720, 670, 1.15, 'shock', flip=True)
            + sweat(470, 520) + sweat(850, 510) + T(540, 260, '(정적)', 70, 'g', '#8A90A0'), '#FFF5F5')
    + caption('둘이 동시에 전화를 끊고\n서로 쳐다봤다.'))
# 6
pages[6] = (page_bg() + header(6, TOTAL)
    + panel(notebook(140, 640, 330, 240, '명절 규칙', -5) + char('groom', 720, 730, 1.15, 'smug', (8, 140))
            + bubble(110, 170, 860, '이번엔 우리 집 아침,\n너희 집 점심부터!\n다음 명절엔 반대로 하자', 56, (700, 520)), '#FFF5D8')
    + caption('오빠가 갑자기 노트를 꺼냈다.'))
# 7
pages[7] = (page_bg() + header(7, TOTAL)
    + panel(char('bride', 380, 720, 1.15, 'smug', (8, 130)) + char('groom', 730, 730, 1.0, 'nervous', (8, -8), flip=True) + sweat(840, 580)
            + bubble(90, 170, 640, '그럼 설날엔\n우리 집이 먼저다?', 58, (360, 470)) + bubble(640, 440, 340, '...응!', 58, (740, 560)), '#EAF4EE')
    + caption('그렇게 우리 집\n첫 번째 규칙이 생겼다.'))
# 8
pages[8] = (page_bg() + header(8, TOTAL)
    + panel(hearts(12, (90, 160, 990, 1040), '#FFD6DD', 68)
            + phone(150, 360, 200, 340) + phone(730, 360, 200, 340)
            + char('bride', 400, 820, .95, 'joy', (6, 110)) + char('groom', 680, 810, .95, 'joy', (110, 6), flip=True)
            + bubble(120, 170, 840, '엄마, 우리 둘이 정했어!', 56, (400, 330)), '#FFF0F2')
    + caption('각자 자기 부모님께는\n자기가 직접 전화로 말씀드렸다.'))
# 9 정리
items = [('순서', '번갈아 갈지, 가까운 집부터 갈지'), ('머무는 시간', '집마다 하루씩? 반나절씩?'), ('선물·용돈', '양가에 같은 기준으로, 예산 먼저'),
         ('내 부모님은 내가', '말씀은 각자 자기 부모님께'), ('쉬는 신호', '힘들 때 쓸 둘만의 신호 정하기')]
p9 = page_bg() + header(9, TOTAL) + T(540, 230, '첫 명절 전, 둘이 정할 5가지', 72, 'j')
cols = [ROSE, '#8FD3C1', '#F5B860', '#96B4EE', '#C59BE6']
for i, (a, b) in enumerate(items):
    y = 290 + i * 180
    p9 += f'<rect x="80" y="{y}" width="920" height="156" rx="50" fill="#fff" stroke="{INK}" stroke-width="5"/><circle cx="160" cy="{y+78}" r="46" fill="{cols[i]}"/>'
    p9 += T(160, y + 98, str(i + 1), 56, 'j', '#fff') + T(240, y + 66, a, 54, 'j', INK, 'start') + T(240, y + 126, b, 46, 'g', '#7A6262', 'start')
p9 += T(540, 1250, '미리 정해 두면 명절 전날 싸울 일이 줄어요', 48, 'g', ROSE)
pages[9] = p9
# 10 마무리
pages[10] = (page_bg('#FFE4E4') + header(10, TOTAL) + hearts(18, (40, 120, 1040, 700), '#FFD0D6', 70)
    + char('bride', 400, 470, 1.15, 'joy', (6, -40)) + char('groom', 690, 460, 1.15, 'joy', (40, -8))
    + f'<rect x="110" y="820" width="860" height="420" rx="60" fill="#fff" stroke="{INK}" stroke-width="6"/>'
    + T(540, 930, '저장해 두고', 76, 'j') + T(540, 1040, '예비 배우자에게 공유하기', 76, 'j', ROSE) + T(540, 1150, '여러분은 어느 집부터 가세요?', 50, 'g', '#7A6262')
    + T(540, 1310, '@yebibubu.toon', 40, 'j', '#C49A9A'))

if __name__ == '__main__':
    render(pages, sys.argv[1] if len(sys.argv) > 1 else 'out/ep06')
