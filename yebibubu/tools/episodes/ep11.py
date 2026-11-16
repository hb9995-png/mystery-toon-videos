import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from extra import *

TOTAL = 10


def wall(y0=130, y1=1060):
    """오빠네 거실 벽: 액자 두 개."""
    return (f'<rect x="70" y="{y0}" width="940" height="{y1 - y0}" fill="#FFF0DC"/>'
            f'<rect x="150" y="{y0 + 60}" width="170" height="130" rx="10" fill="#CFE6D8" stroke="{INK}" stroke-width="5"/>'
            f'<rect x="760" y="{y0 + 50}" width="150" height="150" rx="10" fill="#F6D9E0" stroke="{INK}" stroke-width="5"/>')


pages = {}
# 1 표지
pages[1] = (page_bg('#FFE4E4') + hearts(22, (40, 40, 1040, 1310), '#FFD0D6', 111)
    + f'<rect x="80" y="70" width="250" height="84" rx="42" fill="{ROSE}"/>' + T(205, 128, '첫 인사 썰', 50, 'j', '#fff')
    + T(80, 265, '오빠 부모님께', 110, 'j', INK, 'start') + T(80, 395, '"엄마"라고 한 썰', 110, 'j', ROSE, 'start')
    + panel(door(110, 560, 220, 500) + char('momB', 800, 790, 1.0, 'shock', (100, -8)) + char('bride', 480, 800, 1.0, 'shock', (6, -6))
            + box(405, 900, 150, 110, '선물') + sweat(590, 650) + T(950, 600, '!?', 90, 'j', ROSE), '#FFF7EE', 440, 1110)
    + f'<rect x="70" y="1150" width="940" height="130" rx="65" fill="#fff" stroke="{ROSE}" stroke-width="6"/>' + T(540, 1235, '+ 첫 인사 갈 때 챙길 5가지', 58, 'j', INK))
# 2
pages[2] = (page_bg() + header(2, TOTAL)
    + panel(hearts(10, (100, 160, 980, 560), '#FFD0D6', 112) + notebook(600, 250, 330, 230, '호칭 연습', 6)
            + char('bride', 360, 700, 1.25, 'nervous', (6, 110)) + T(360, 250, '어머님... 아버님...', 58, 'g', '#7A6262') + sweat(520, 560), '#FFF5D8')
    + caption('오빠 부모님께 처음 인사 가는 날.\n호칭만 백 번 연습했다.'))
# 3
pages[3] = (page_bg() + header(3, TOTAL)
    + panel(char('groom', 700, 700, 1.15, 'smug', (110, -8)) + char('bride', 330, 720, 1.05, 'nervous') + sweat(450, 580)
            + bubble(440, 170, 520, '그냥 편하게 해~\n우리 엄마 안 무서워', 52, (690, 440)), '#EAF3F7')
    + caption('오빠는 편하게 하라는데\n그게 제일 어렵다.'))
# 4
pages[4] = (page_bg() + header(4, TOTAL)
    + panel(door(110, 330, 240, 730) + char('momB', 560, 720, 1.05, 'joy', (110, -8)) + char('dadB', 830, 730, 1.0, 'happy')
            + bubble(380, 170, 560, '어서 와요~\n먼 길 오느라 고생했지', 50, (580, 440)), '#FFF0DC')
    + caption('현관문이 열리고\n두 분이 반겨 주셨다.'))
# 5
pages[5] = (page_bg() + header(5, TOTAL)
    + panel(wall() + char('momB', 330, 560, 1.0, 'joy', (8, 120)) + char('bride', 720, 570, 1.0, 'happy') + table(790)
            + bubble(130, 170, 520, '많이 먹어~\n이것도 먹어 봐', 54, (330, 400)), '#FFF0DC')
    + caption('어머님은 계속\n반찬을 내 앞으로 밀어 주셨다.'))
# 6
pages[6] = (page_bg() + header(6, TOTAL)
    + panel(speed(540, 660, '#FFE6D2', 44, 330) + char('bride', 540, 700, 1.4, 'joy', (6, -40))
            + bubble(170, 170, 740, '너무 맛있어요, 엄마!', 64, (540, 400)), '#FFF3E6')
    + caption('긴장이 풀린 순간\n그 말이 튀어나왔다.'))
# 7
pages[7] = (page_bg() + header(7, TOTAL)
    + panel(wall() + char('momB', 200, 600, .8, 'blank') + char('dadB', 420, 600, .8, 'blank') + char('bride', 660, 610, .8, 'shock')
            + char('groom', 880, 600, .8, 'shock') + table(800) + sweat(760, 500) + sweat(980, 490, .8) + T(540, 330, '(...정적...)', 68, 'g', '#8A90A0'), '#E7EEF3')
    + caption('식탁에 3초 동안\n아무 소리도 안 났다.'))
# 8
pages[8] = (page_bg() + header(8, TOTAL)
    + panel(hearts(14, (100, 160, 980, 600), '#FFD0D6', 118) + char('momB', 360, 690, 1.15, 'joy', (130, 120)) + char('dadB', 720, 700, 1.05, 'joy', (110, -8))
            + bubble(120, 170, 840, '어머 좋다! 그래,\n앞으로 엄마라고 해~', 58, (360, 440)), '#FFF5D8')
    + caption('어머님이 먼저 활짝 웃으셨다.\n오빠는 옆에서 몰래 울컥했다.'))
# 9 정리
items = [('호칭 미리 묻기', '어떻게 불러 드릴지 짝꿍에게 확인'), ('작은 선물', '부모님 취향은 짝꿍이 잘 알아요'),
         ('깔끔한 옷차림', '너무 꾸미기보다 편하고 단정하게'), ('대화 소재', '짝꿍 어릴 적 이야기면 성공'), ('다녀와서 인사', '감사 연락은 짝꿍과 같이 드리기')]
p9 = page_bg() + header(9, TOTAL) + T(540, 230, '첫 인사 갈 때 챙길 5가지', 68, 'j')
cols = [ROSE, '#8FD3C1', '#F5B860', '#96B4EE', '#C59BE6']
for i, (a, b) in enumerate(items):
    y = 290 + i * 180
    p9 += f'<rect x="80" y="{y}" width="920" height="156" rx="50" fill="#fff" stroke="{INK}" stroke-width="5"/><circle cx="160" cy="{y+78}" r="46" fill="{cols[i]}"/>'
    p9 += T(160, y + 98, str(i + 1), 56, 'j', '#fff') + T(240, y + 66, a, 52, 'j', INK, 'start') + T(240, y + 126, b, 44, 'g', '#7A6262', 'start')
p9 += T(540, 1250, '실수해도 괜찮아요, 웃으면 돼요!', 48, 'g', ROSE)
pages[9] = p9
# 10 마무리
pages[10] = (page_bg('#FFE4E4') + header(10, TOTAL) + hearts(18, (40, 120, 1040, 700), '#FFD0D6', 120)
    + char('bride', 400, 470, 1.15, 'joy', (6, -40)) + char('groom', 690, 460, 1.15, 'joy', (40, -8))
    + f'<rect x="110" y="820" width="860" height="420" rx="60" fill="#fff" stroke="{INK}" stroke-width="6"/>'
    + T(540, 930, '저장해 두고', 76, 'j') + T(540, 1040, '예비 배우자에게 공유하기', 76, 'j', ROSE) + T(540, 1150, '여러분 첫 인사 썰도 댓글로!', 50, 'g', '#7A6262')
    + T(540, 1310, '@yebibubu.toon', 40, 'j', '#C49A9A'))

if __name__ == '__main__':
    render(pages, sys.argv[1] if len(sys.argv) > 1 else 'out/ep11')
