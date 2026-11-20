import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from extra import *

TOTAL = 9


def room(y0=130, y1=1060, night=True, win=True):
    """밤 거실 벽과 바닥, 창문."""
    wall = '#E9E4F2' if night else '#FFF1E4'
    s = (f'<rect x="70" y="{y0}" width="940" height="{y1 - y0}" fill="{wall}"/>'
         f'<rect x="70" y="{y1 - 160}" width="940" height="160" fill="#D9C3AE"/>')
    if night and win:
        s += (f'<rect x="760" y="{y0 + 50}" width="190" height="190" rx="14" fill="#3E4A72" stroke="{INK}" stroke-width="5"/>'
              f'<circle cx="900" cy="{y0 + 100}" r="26" fill="#FFF3B0"/>'
              f'<path d="M855 {y0 + 50} V {y0 + 240} M 760 {y0 + 145} H 950" stroke="{INK}" stroke-width="4"/>')
    return s


def cloud(x, y, s=1.0, col='#9C93A8'):
    """머리 위 먹구름."""
    return (f'<g transform="translate({x} {y}) scale({s})" stroke="{INK}" stroke-width="4" fill="{col}">'
            '<path d="M-70 20 a 40 40 0 0 1 20 -60 a 50 50 0 0 1 90 -6 a 36 36 0 0 1 30 66 z"/></g>')


def hall_card(x, y, name, memo, col):
    return (f'<rect x="{x}" y="{y}" width="260" height="300" rx="24" fill="#fff" stroke="{INK}" stroke-width="5"/>'
            f'<rect x="{x + 20}" y="{y + 20}" width="220" height="130" rx="14" fill="{col}"/>'
            + T(x + 130, y + 210, name, 46, 'j', INK) + T(x + 130, y + 265, memo, 38, 'g', '#7A6262'))


pages = {}
# 1 표지
pages[1] = (page_bg('#FFE4E4') + hearts(22, (40, 40, 1040, 1310), '#FFD0D6', 191)
    + f'<rect x="80" y="70" width="270" height="84" rx="42" fill="{ROSE}"/>' + T(215, 128, '싸움 썰', 50, 'j', '#fff')
    + T(80, 265, '결혼 준비하다', 100, 'j', INK, 'start') + T(80, 390, '처음 크게 싸운 날', 100, 'j', ROSE, 'start')
    + panel(room(440, 1110) + char('bride', 320, 800, .95, 'blank', (-10, -10))
            + char('groom', 760, 800, .95, 'blank', (10, -10), flip=True)
            + cloud(320, 520, .9) + cloud(760, 520, .9) + vs_badge(540, 760, 64), '#E9E4F2', 440, 1110)
    + f'<rect x="70" y="1150" width="940" height="130" rx="65" fill="#fff" stroke="{ROSE}" stroke-width="6"/>' + T(540, 1235, '+ 준비 싸움 줄이는 5가지', 58, 'j', INK))
# 2
pages[2] = (page_bg() + header(2, TOTAL)
    + panel(room(night=False) + hall_card(110, 330, '1번 홀', '밝고 넓음', '#FFE1E6')
            + hall_card(410, 330, '2번 홀', '역에서 가까움', '#D9F2EA') + hall_card(710, 330, '3번 홀', '분위기 좋음', '#E3E8F2')
            + char('bride', 300, 820, .75, 'happy', (6, -30)) + char('groom', 780, 820, .75, 'happy', (30, -6), flip=True)
            + T(540, 240, '(하루에 세 군데 투어)', 56, 'g', '#7A6262'), '#FFF1E4')
    + caption('하루에 웨딩홀\n세 군데를 보고 왔다.'))
# 3
pages[3] = (page_bg() + header(3, TOTAL)
    + panel(room() + sofa(540, 700, 640) + char('bride', 380, 650, .95, 'nervous', (10, 20))
            + char('groom', 700, 650, .95, 'blank', (20, 10), flip=True)
            + T(540, 250, '밤 11시', 80, 'j', '#5A5470') + sweat(500, 480, .8), '#E9E4F2')
    + caption('밤 11시, 둘 다\n발이 퉁퉁 부어 있었다.'))
# 4
pages[4] = (page_bg() + header(4, TOTAL)
    + panel(room(win=False) + char('bride', 300, 720, 1.05, 'nervous', (60, 40))
            + char('groom', 780, 720, 1.05, 'blank', (8, -8), flip=True)
            + bubble(110, 180, 420, '그래서\n어디로 할 건데?', 50, (300, 500))
            + bubble(560, 190, 400, '아무 데나\n괜찮아', 50, (760, 500)), '#E9E4F2')
    + caption('"아무 데나"라는 말에\n뭔가 툭 끊어졌다.'))
# 5
pages[5] = (page_bg() + header(5, TOTAL)
    + panel(speed(540, 620, '#D9D2E6', 44, 320) + char('bride', 330, 700, 1.15, 'shock', (130, 120))
            + char('groom', 760, 700, 1.05, 'shock', (8, -8), flip=True)
            + bubble(90, 150, 520, '나 혼자 결혼해?', 58, (360, 420)), '#E9E4F2')
    + caption('나는 소리를 질렀고\n오빠는 말없이 나갔다.'))
# 6
pages[6] = (page_bg() + header(6, TOTAL)
    + panel(room(win=False) + door(720, 380, 220, 520) + char('bride', 360, 700, 1.1, 'blank', (-20, -20))
            + tears(360, 700, .9) + T(540, 260, '(30분째...)', 60, 'g', '#5A5470'), '#E9E4F2')
    + caption('30분이 지났다.\n괜히 소리 질렀나...'))
# 7
pages[7] = (page_bg() + header(7, TOTAL)
    + panel(room(night=False) + hearts(10, (100, 160, 980, 520), '#FFD0D6', 197)
            + char('groom', 720, 690, 1.1, 'nervous', (60, 40), flip=True)
            + char('bride', 300, 690, 1.0, 'shock', (8, -8)) + tears(300, 690, .8) + chicken_box(560, 800, 280)
            + bubble(470, 160, 500, '오늘은 결혼 얘기\n금지. 치킨 먹자', 50, (700, 440)), '#FFF5D8')
    + caption('오빠가 치킨을\n안고 돌아왔다.'))
# 8 정리
items = [('쉬는 날 정하기', '준비 얘기 안 하는 날 만들기'), ('피곤하면 미루기', '지친 밤엔 중요한 결정 금지'),
         ('한 번에 하나씩', '오늘 정할 것 하나만 고르기'), ('기준 먼저 맞추기', '둘에게 중요한 것부터 말하기'),
         ('고마운 것 말하기', '하루 하나씩 고맙다고 하기')]
p8 = page_bg() + header(8, TOTAL) + T(540, 230, '준비 싸움 줄이는 5가지', 70, 'j')
cols = [ROSE, '#8FD3C1', '#F5B860', '#96B4EE', '#C59BE6']
for i, (a, b) in enumerate(items):
    y = 290 + i * 180
    p8 += f'<rect x="80" y="{y}" width="920" height="156" rx="50" fill="#fff" stroke="{INK}" stroke-width="5"/><circle cx="160" cy="{y+78}" r="46" fill="{cols[i]}"/>'
    p8 += T(160, y + 98, str(i + 1), 56, 'j', '#fff') + T(240, y + 66, a, 52, 'j', INK, 'start') + T(240, y + 126, b, 44, 'g', '#7A6262', 'start')
p8 += T(540, 1250, '"아무 데나"보다 "나는 2번이 좋아"!', 48, 'g', ROSE)
pages[8] = p8
# 9 마무리
pages[9] = (page_bg('#FFE4E4') + header(9, TOTAL) + hearts(18, (40, 120, 1040, 700), '#FFD0D6', 199)
    + char('bride', 400, 470, 1.15, 'joy', (6, -40)) + char('groom', 690, 460, 1.15, 'happy', (40, -8))
    + f'<rect x="110" y="820" width="860" height="420" rx="60" fill="#fff" stroke="{INK}" stroke-width="6"/>'
    + T(540, 930, '저장해 두고', 76, 'j') + T(540, 1040, '예비 배우자에게 공유하기', 76, 'j', ROSE) + T(540, 1150, '여러분 첫 싸움은 어떻게 풀었어요?', 50, 'g', '#7A6262')
    + T(540, 1310, '@yebibubu.toon', 40, 'j', '#C49A9A'))

if __name__ == '__main__':
    render(pages, sys.argv[1] if len(sys.argv) > 1 else 'out/ep19')
