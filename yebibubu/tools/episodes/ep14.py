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


def floor(y=880):
    return f'<rect x="70" y="{y}" width="940" height="300" fill="#E9D6BE"/><path d="M70 {y} H 1010" stroke="{INK}" stroke-width="5"/>'


def noti(x, y, w, text):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="70" rx="18" fill="#fff" stroke="{INK}" stroke-width="3"/>'
            f'<circle cx="{x + 36}" cy="{y + 35}" r="16" fill="{ROSE}"/>' + T(x + 64, y + 46, text, 32, 'j', INK, 'start'))


def coin(x, y, r=40):
    return (f'<circle cx="{x}" cy="{y}" r="{r}" fill="#FFD36A" stroke="{INK}" stroke-width="5"/>'
            f'<circle cx="{x}" cy="{y}" r="{r * .62}" fill="none" stroke="#E0A93A" stroke-width="4"/>')


pages = {}
# 1 표지
pages[1] = (page_bg('#FFE4E4') + hearts(22, (40, 40, 1040, 1310), '#FFD0D6', 141)
    + f'<rect x="80" y="70" width="240" height="84" rx="42" fill="{ROSE}"/>' + T(200, 128, '공감 주의', 50, 'j', '#fff')
    + T(80, 265, '통장 합치면', 108, 'j', INK, 'start') + T(80, 395, '생기는 일 7가지', 108, 'j', ROSE, 'start')
    + panel(floor(960) + notebook(120, 500, 300, 220, '우리 가계부', -8) + coin(820, 560) + coin(900, 640, 32)
            + char('bride', 400, 860, .95, 'smug', (6, -6)) + char('groom', 700, 850, .95, 'nervous', (8, -8)) + sweat(820, 700), '#FFF7EE', 440, 1110)
    + f'<rect x="70" y="1150" width="940" height="130" rx="65" fill="#fff" stroke="{ROSE}" stroke-width="6"/>' + T(540, 1235, '+ 몇 개 공감했는지 댓글로', 58, 'j', INK))

# 2 가계부 의욕
pages[2] = scene(2, 1, '의욕 폭발', '#FFF7E6',
    floor() + notebook(560, 320, 360, 260, '우리 가계부', 6)
    + char('groom', 330, 800, 1.1, 'smug', (120, -10)) + bubble(560, 640, 380, '영수증도\n다 찍자!', 54, (470, 560)),
    '가계부 앱 깔고 첫날엔\n영수증까지 찍는다.')

# 3 알림
ph_in = (noti(440, 360, 290, '결제 알림') + noti(440, 450, 290, '결제 알림') + noti(440, 540, 290, '결제 알림'))
pages[3] = scene(3, 2, '알림 폭탄', '#E4F0F7',
    phone(420, 300, 330, 560, '#DCE9F6', ph_in)
    + char('bride', 230, 820, .95, 'shock', (60, -10)) + char('groom', 860, 820, .95, 'shock', (8, 60), flip=True) + sweat(320, 640) + sweat(960, 640),
    '서로의 결제 알림이\n실시간으로 날아온다.')

# 4 택배
pages[4] = scene(4, 3, '이거 누구 거?', '#F4ECFA',
    floor() + box(400, 760, 280, 200, '택배')
    + char('bride', 230, 800, 1.0, 'smug', (120, -10)) + char('groom', 850, 800, 1.0, 'nervous', (8, -8), flip=True) + sweat(950, 620)
    + bubble(300, 290, 360, '이건\n누구 거?', 54, (260, 520)),
    '택배 상자 하나에\n조용한 수사가 시작된다.')

# 5 비상금 고백
pages[5] = scene(5, 4, '비상금 고백', '#EEF1F7',
    char('groom', 300, 800, 1.05, 'nervous', (8, 100)) + sweat(420, 620)
    + char('bride', 780, 810, 1.05, 'nervous', (100, -8), flip=True) + sweat(660, 620)
    + bubble(110, 300, 380, '사실 나\n비상금 있어', 50, (300, 560)) + bubble(590, 300, 380, '...나도', 54, (780, 560)),
    '털어놓다 보니\n둘 다 비상금이 있었다.')

# 6 통장 이름
ph_in6 = (T(585, 430, '통장 이름', 40, 'j', '#7A8090') + f'<rect x="440" y="470" width="290" height="110" rx="20" fill="#fff" stroke="{INK}" stroke-width="3"/>'
          + T(585, 540, '신혼여행 가자', 40, 'j', ROSE))
pages[6] = scene(6, 5, '이름 짓기', '#FFF3D9',
    phone(420, 300, 330, 560, '#DCE9F6', ph_in6) + hearts(6, (110, 300, 380, 560), '#FF9FB0', 146)
    + char('bride', 230, 820, .95, 'joy', (60, -10)) + char('groom', 860, 820, .95, 'joy', (8, 60), flip=True),
    '통장 이름 짓는 데만\n한참 걸렸다.')

# 7 월급날
pages[7] = scene(7, 6, '월급날', '#FFEFF2',
    calendar(640, 290, 300, (17,), '이번 달') + coin(160, 360) + coin(240, 300, 30) + coin(560, 360, 34)
    + char('bride', 320, 740, .95, 'joy', (130, 130)) + char('groom', 720, 750, .95, 'joy', (130, 130)),
    '월급날엔 둘이\n같이 환호한다.')

# 8 용돈 협상
rows = [('커피', '협상 중', ROSE), ('취미', '협상 중', ROSE), ('간식', '합의 완료', '#4E9A7E')]
pages[8] = scene(8, 7, '용돈 협상', '#E9F5EE',
    paper(330, 280, 420, 400, '용돈 협상안', rows, 40, -3)
    + char('bride', 230, 800, .9, 'smug', (60, -10)) + char('groom', 850, 800, .9, 'smug', (8, 60), flip=True),
    '결국 용돈제를 두고\n진지한 협상 테이블.')

# 9 마무리
pages[9] = (page_bg('#FFE4E4') + header(9, TOTAL) + hearts(18, (40, 120, 1040, 700), '#FFD0D6', 149)
    + char('bride', 400, 470, 1.15, 'joy', (6, -40)) + char('groom', 690, 460, 1.15, 'happy', (40, -8))
    + f'<rect x="110" y="820" width="860" height="420" rx="60" fill="#fff" stroke="{INK}" stroke-width="6"/>'
    + T(540, 925, '몇 개 공감했어요?', 76, 'j') + T(540, 1035, '댓글로 번호 남기기', 76, 'j', ROSE)
    + T(540, 1145, '통장 합칠 사람한테 공유!', 48, 'g', '#7A6262')
    + T(540, 1310, '@yebibubu.toon', 40, 'j', '#C49A9A'))

if __name__ == '__main__':
    render(pages, sys.argv[1] if len(sys.argv) > 1 else 'out/ep14')
