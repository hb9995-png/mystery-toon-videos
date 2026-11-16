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


def invite(x, y, w=300, rot=0):
    """청첩장 한 장: 봉투 위에 카드."""
    h = w * .7
    return (f'<g transform="rotate({rot} {x + w / 2} {y + h / 2})" stroke="{INK}" stroke-width="5" stroke-linejoin="round">'
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="#FFF8F0"/>'
            f'<path d="M{x} {y} L {x + w / 2} {y + h * .55} L {x + w} {y}" fill="#F6E3E6"/>'
            f'<circle cx="{x + w / 2}" cy="{y + h * .55}" r="{w * .07}" fill="{ROSE}"/></g>')


pages = {}
# 1 표지
pages[1] = (page_bg('#FFE4E4') + hearts(22, (40, 40, 1040, 1310), '#FFD0D6', 121)
    + f'<rect x="80" y="70" width="270" height="84" rx="42" fill="{ROSE}"/>' + T(215, 128, '체크리스트', 50, 'j', '#fff')
    + T(80, 265, '청첩장 돌리기 전', 110, 'j', INK, 'start') + T(80, 395, '꼭 볼 5가지', 110, 'j', ROSE, 'start')
    + panel(invite(120, 560, 260, -8) + invite(700, 540, 240, 7) + invite(150, 880, 220, 5)
            + char('bride', 450, 800, .95, 'joy', (6, 100)) + char('groom', 650, 790, .95, 'nervous', (8, -8)) + sweat(760, 640), '#FFF7EE', 440, 1110)
    + f'<rect x="70" y="1150" width="940" height="130" rx="65" fill="#fff" stroke="{ROSE}" stroke-width="6"/>' + T(540, 1235, '+ 저장해 두고 인쇄 전에 보기', 58, 'j', INK))
# 2 상황 1
pages[2] = (page_bg() + header(2, TOTAL)
    + panel(hearts(12, (100, 160, 980, 600), '#FFD0D6', 122) + box(620, 640, 300, 220, '청첩장')
            + char('bride', 380, 700, 1.2, 'joy', (-30, 140)) + bubble(110, 170, 560, '드디어 왔다!\n너무 예쁘다~', 58, (380, 430)), '#FFF5D8')
    + caption('청첩장이 도착했다.\n이제 돌리기만 하면 된다.'))
# 3 상황 2
pages[3] = (page_bg() + header(3, TOTAL)
    + panel(paper(130, 320, 440, 560, '청첩장', [('신랑', '오빠', None), ('신부', '나', None), ('예식', '오후 1시', None), ('장소', '○○홀', None)], 46, -3)
            + char('groom', 780, 760, 1.05, 'shock', (120, 120)) + sweat(900, 600)
            + bubble(560, 170, 400, '근데 우리\n2시 아니었어?', 54, (790, 440)), '#FFF3E6')
    + caption('봉투에 넣으려는 순간\n오빠가 물었다.'))
# 4~8 항목
pages[4] = card(4, 1, '소리 내서 읽기', '#FFF5D8',
    paper(140, 300, 460, 600, '확인', [('이름', '✔', None), ('날짜·요일', '✔', None), ('시간', '✔', None), ('장소·층', '✔', None)], 46, -3)
    + char('bride', 800, 780, .95, 'smug', (100, -8)),
    '이름·날짜·시간·장소를\n한 글자씩 읽어 보기')
pages[5] = card(5, 2, '양가 부모님 확인', '#F1ECFB',
    char('momB', 270, 700, .9, 'happy') + char('momG', 800, 700, .9, 'happy') + invite(400, 560, 280, 0)
    + bubble(230, 280, 620, '이름 표기 이렇게 할게요!', 46, (540, 540)),
    '부모님 성함과 표기 방식은\n인쇄 전에 양가 모두 확인')
pages[6] = card(6, 3, '오시는 길 안내', '#EAF4EE',
    f'<rect x="150" y="300" width="460" height="560" rx="20" fill="#fff" stroke="{INK}" stroke-width="5"/>'
    f'<path d="M190 420 H 570 M 300 330 V 830 M 190 650 Q 380 600 570 720" stroke="#BFD9C8" stroke-width="22" fill="none"/>'
    f'<path d="M430 520 c -40 -60 -60 -90 -60 -110 a 60 60 0 0 1 120 0 c 0 20 -20 50 -60 110 z" fill="{ROSE}" stroke="{INK}" stroke-width="5"/>'
    + char('groom', 800, 780, .9, 'happy', (100, -8)),
    '주차·대중교통 안내가\n맞는지 한 번 더 확인')
pages[7] = card(7, 4, '모바일 청첩장도', '#EAF3F7',
    phone(160, 290, 340, 640, inner=invite(200, 420, 260) + T(330, 700, '지도 열기', 42, 'j', ROSE) + T(330, 790, '연락하기', 42, 'j', ROSE))
    + char('bride', 770, 780, .95, 'happy', (8, 110)),
    '보내기 전에 링크를 눌러\n지도·연락처까지 직접 확인')
pages[8] = card(8, 5, '명단은 둘이 같이', '#FFE9EE',
    hearts(10, (100, 300, 980, 700), '#FFD0D6', 128)
    + paper(330, 280, 420, 360, '전달 명단', [('직접 만나서', '', None), ('우편으로', '', None), ('모바일로', '', None)], 40, -3)
    + char('bride', 330, 820, .9, 'happy', (8, 110)) + char('groom', 750, 810, .9, 'happy', (110, -8)),
    '누구에게 어떻게 전할지\n함께 나눠 적어 두기')
# 9 마무리
pages[9] = (page_bg('#FFE4E4') + header(9, TOTAL) + hearts(18, (40, 120, 1040, 700), '#FFD0D6', 129)
    + char('bride', 400, 470, 1.15, 'joy', (6, -40)) + char('groom', 690, 460, 1.15, 'joy', (40, -8))
    + f'<rect x="110" y="820" width="860" height="420" rx="60" fill="#fff" stroke="{INK}" stroke-width="6"/>'
    + T(540, 930, '저장해 두고', 76, 'j') + T(540, 1040, '예비 배우자에게 공유하기', 76, 'j', ROSE) + T(540, 1150, '청첩장 오타 썰 있으면 댓글로!', 50, 'g', '#7A6262')
    + T(540, 1310, '@yebibubu.toon', 40, 'j', '#C49A9A'))

if __name__ == '__main__':
    render(pages, sys.argv[1] if len(sys.argv) > 1 else 'out/ep12')
