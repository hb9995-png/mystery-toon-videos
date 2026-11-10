import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from extra import *

TOTAL = 9


def tag(n, label):
    return (f'<rect x="100" y="160" width="{110 + len(label) * 50}" height="80" rx="40" fill="#fff" stroke="{INK}" stroke-width="5"/>'
            + f'<circle cx="140" cy="200" r="28" fill="{ROSE}"/>' + T(140, 215, str(n), 40, 'j', '#fff')
            + T(184, 218, label, 46, 'j', INK, 'start'))


def card(no, n, label, bg, inner, cap):
    return page_bg() + header(no, TOTAL) + panel(inner + tag(n, label), bg) + caption(cap)


pages = {}
# 1 표지
cover_in = (fridge(130, 540, 230, 400) + washer(760, 640, 200)
            + char('bride', 450, 800, .95, 'joy', (6, 100)) + char('groom', 640, 790, .95, 'nervous', (8, -8)) + sweat(740, 640))
pages[1] = (page_bg('#FFE4E4') + hearts(22, (40, 40, 1040, 1310), '#FFD0D6', 51)
    + f'<rect x="80" y="70" width="270" height="84" rx="42" fill="{ROSE}"/>' + T(215, 128, '체크리스트', 50, 'j', '#fff')
    + T(80, 265, '혼수 가전 사기 전', 110, 'j', INK, 'start') + T(80, 395, '꼭 볼 5가지', 110, 'j', ROSE, 'start')
    + panel(cover_in, '#FFF7EE', 440, 1110)
    + f'<rect x="70" y="1150" width="940" height="130" rx="65" fill="#fff" stroke="{ROSE}" stroke-width="6"/>' + T(540, 1235, '+ 저장해 두고 매장 가기 전에 보기', 58, 'j', INK))
# 2 상황 1
pages[2] = (page_bg() + header(2, TOTAL)
    + panel(fridge(110, 380, 250, 520, '#F6E7EC') + fridge(780, 380, 250, 520) + char('bride', 500, 720, 1.1, 'joy', (-30, 140))
            + bubble(380, 175, 520, '이거 예쁘다!\n이것도 예쁘다!', 58, (520, 470)), '#EAF3F7')
    + caption('가전 매장에 가니\n전부 우리 집에 있어야 할 것 같았다.'))
# 3 상황 2
pages[3] = (page_bg() + header(3, TOTAL)
    + panel(door(140, 330, 230, 640) + fridge(420, 300, 300, 680) + char('groom', 850, 760, 1.0, 'shock', (120, 120)) + sweat(960, 600)
            + bubble(560, 170, 400, '근데 이거\n문은 통과해?', 54, (860, 420)), '#FFF3E6')
    + caption('계약서에 사인하려는 순간\n오빠가 물었다.'))
# 4~8 항목
pages[4] = card(4, 1, '치수부터 재기', '#FFF5D8',
    tape(250, 560, 600) + fridge(400, 620, 180, 320) + char('bride', 790, 820, .9, 'smug', (100, -8)),
    '놓을 자리는 물론\n현관·엘리베이터 폭까지')
pages[5] = card(5, 2, '배송일은 입주일 뒤로', '#EAF4EE',
    calendar(150, 330, 420, mark=(17,), title='입주') + box(640, 620, 260, 190, '배송') + char('groom', 780, 820, .75, 'happy'),
    '집에 들어가기 전에 오면\n둘 곳이 없어요.')
pages[6] = card(6, 3, '지금 vs 나중', '#F1ECFB',
    paper(120, 300, 400, 560, '지금', [('냉장고', '✔', None), ('세탁기', '✔', None), ('침대', '✔', None)], 46, -3)
    + paper(560, 300, 400, 560, '나중에', [('건조기', '', '#7A6262'), ('식기세척기', '', '#7A6262'), ('큰 TV', '', '#7A6262')], 46, 3),
    '처음부터 다 살 필요 없어요.\n살아 보고 사도 늦지 않아요.')
pages[7] = card(7, 4, '추가 비용 확인', '#FFF0DC',
    paper(140, 300, 520, 620, '견적서', [('제품', '포함', None), ('설치비', '?', ROSE), ('기존 제품 수거', '?', ROSE), ('추가 자재', '?', ROSE)], 44, -3)
    + char('bride', 820, 760, .95, 'nervous', (8, 100)) + sweat(930, 600),
    '설치·수거·자재비가\n견적에 들어 있는지 물어보기')
pages[8] = card(8, 5, '예산 상한은 둘이 같이', '#FFE9EE',
    hearts(10, (100, 300, 980, 700), '#FFD0D6', 88) + notebook(380, 330, 320, 230, '가전 예산', -4)
    + char('bride', 360, 800, 1.0, 'happy', (8, 110)) + char('groom', 720, 790, 1.0, 'happy', (110, -8)),
    '매장 가기 전에 정해 두면\n그 자리에서 안 흔들려요.')
# 9 마무리
pages[9] = (page_bg('#FFE4E4') + header(9, TOTAL) + hearts(18, (40, 120, 1040, 700), '#FFD0D6', 59)
    + char('bride', 400, 470, 1.15, 'joy', (6, -40)) + char('groom', 690, 460, 1.15, 'joy', (40, -8))
    + f'<rect x="110" y="820" width="860" height="420" rx="60" fill="#fff" stroke="{INK}" stroke-width="6"/>'
    + T(540, 930, '저장해 두고', 76, 'j') + T(540, 1040, '같이 매장 갈 사람에게 공유', 72, 'j', ROSE) + T(540, 1150, '여러분 혼수 1순위 가전은 뭐였나요?', 50, 'g', '#7A6262')
    + T(540, 1310, '@yebibubu.toon', 40, 'j', '#C49A9A'))

if __name__ == '__main__':
    render(pages, sys.argv[1] if len(sys.argv) > 1 else 'out/ep05')
