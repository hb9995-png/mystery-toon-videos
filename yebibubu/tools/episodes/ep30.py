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


def floor(y=880, col='#E9D6BE'):
    return f'<rect x="70" y="{y}" width="940" height="300" fill="{col}"/><path d="M70 {y} H 1010" stroke="{INK}" stroke-width="5"/>'


def shelf(y=300, col='#F3E6D6'):
    """마트 진열대 배경."""
    s = f'<rect x="70" y="{y}" width="940" height="560" fill="{col}"/>'
    cols = ['#F08A6A', '#9CCB7E', '#F2C66B', '#96B4EE', '#C59BE6', '#FFB3C1']
    for r in range(3):
        yy = y + 40 + r * 180
        s += f'<rect x="70" y="{yy + 120}" width="940" height="20" fill="#C9A07A" stroke="{INK}" stroke-width="4"/>'
        for k in range(10):
            s += f'<rect x="{90 + k * 92}" y="{yy + 40}" width="70" height="80" rx="8" fill="{cols[(k + r) % 6]}" stroke="{INK}" stroke-width="3" opacity=".75"/>'
    return s


def toothpick(x, y):
    return (f'<path d="M{x} {y} l 70 -70" stroke="#C9A07A" stroke-width="6" stroke-linecap="round"/>'
            f'<circle cx="{x + 70}" cy="{y - 70}" r="22" fill="#F08A6A" stroke="{INK}" stroke-width="4"/>')


def rice_table(y=880):
    """밥상: 밥 두 공기 + 국."""
    s = f'<g stroke="{INK}" stroke-width="5"><rect x="200" y="{y}" width="680" height="60" rx="20" fill="#E9C9A4"/>'
    for cx in (360, 720):
        s += (f'<path d="M{cx - 70} {y - 10} H {cx + 70} Q {cx + 70} {y + 40} {cx} {y + 40} Q {cx - 70} {y + 40} {cx - 70} {y - 10} z" fill="#fff"/>'
              f'<path d="M{cx - 66} {y - 10} Q {cx} {y - 70} {cx + 66} {y - 10} z" fill="#FFFDF5"/>')
    s += f'<path d="M470 {y - 10} H 610 Q 610 {y + 40} 540 {y + 40} Q 470 {y + 40} 470 {y - 10} z" fill="#F07B5A"/></g>'
    s += ''.join(f'<path d="M{x} {y - 50} q 16 -24 0 -48 t 0 -48" fill="none" stroke="#B9B2C4" stroke-width="6"/>' for x in (360, 540, 720))
    return s


pages = {}
# 1 표지
pages[1] = (page_bg('#FFE4E4') + hearts(22, (40, 40, 1040, 1310), '#FFD0D6', 301)
    + f'<rect x="80" y="70" width="240" height="84" rx="42" fill="{ROSE}"/>' + T(200, 128, '공감 주의', 50, 'j', '#fff')
    + T(80, 265, '첫 살림 장보기', 108, 'j', INK, 'start') + T(80, 395, '생기는 일 7가지', 108, 'j', ROSE, 'start')
    + panel(floor(960, '#F3E6D6') + cart(420, 820, .75)
            + char('bride', 280, 800, .85, 'joy', (6, -6)) + char('groom', 820, 800, .85, 'nervous', (8, -8), flip=True) + sweat(920, 650), '#FFF7EE', 440, 1110)
    + f'<rect x="70" y="1150" width="940" height="130" rx="65" fill="#fff" stroke="{ROSE}" stroke-width="6"/>' + T(540, 1235, '+ 몇 개 공감했는지 댓글로', 58, 'j', INK))

# 2 카트 가득
pages[2] = scene(2, 1, '카트가 넘친다', '#FFF5E6',
    shelf(280) + floor(860) + char('bride', 250, 680, 1.0, 'shock', (8, -8)) + sweat(370, 540)
    + cart(520, 770, .95),
    '필요한 것만 사려 했는데\n카트가 넘친다.')

# 3 수건 색
pages[3] = scene(3, 2, '수건 색 고르기', '#F4ECFA',
    floor(900, '#E5DAF0') + towels(420, 900)
    + char('bride', 250, 680, .95, 'smug', (8, -8)) + char('groom', 830, 680, .95, 'smug', (8, -8), flip=True)
    + bubble(110, 300, 300, '분홍색!', 52, (240, 500)) + bubble(670, 300, 300, '하늘색!', 52, (830, 500)),
    '수건 색 하나 고르는데\n한참 걸린다.')

# 4 시식 코너
pages[4] = scene(4, 3, '시식 코너 정복', '#FFEFF2',
    shelf(280, '#FBE3E8') + floor(880, '#F2D9C4')
    + char('groom', 520, 680, 1.15, 'joy', (8, -8)) + toothpick(650, 900) + bubble(640, 290, 330, '하나만 더…', 50, (640, 540)),
    '오빠는 시식 코너에서\n떠나지 않는다.')

# 5 같은 물건
pages[5] = scene(5, 4, '이거 아까 담았는데', '#EAF4F8',
    floor(900, '#D6E6EE')
    + char('bride', 330, 640, 1.0, 'blank', (8, -8)) + char('groom', 750, 640, 1.0, 'blank', (8, -8), flip=True)
    + pan(470, 760, .6, 120) + pan(610, 760, .6, 60)
    + T(540, 400, '…?', 90, 'j', '#9A8FB5'),
    '둘이 같은 걸\n하나씩 담아 왔다.')

# 6 계산대
pages[6] = scene(6, 5, '계산대 앞 정적', '#EEF1F7',
    receipt(540, 250, 220, 620) + floor(880, '#D9DEE8')
    + char('bride', 250, 680, 1.0, 'shock', (8, -8)) + char('groom', 830, 680, 1.0, 'shock', (8, -8), flip=True)
    + sweat(370, 520) + sweat(710, 520),
    '영수증이 끝없이 나오고\n둘 다 말이 없어진다.')

# 7 둘 곳 없음
pages[7] = scene(7, 6, '넣을 자리가 없다', '#F6EFE6',
    floor(880) + door(780, 360, 200, 520)
    + box(120, 730, 220, 160) + box(150, 580, 180, 150) + box(560, 760, 200, 130) + box(590, 640, 150, 120)
    + char('groom', 470, 620, .95, 'nervous', (8, -8)) + sweat(580, 480),
    '집에 오니\n넣을 자리가 없다.')

# 8 첫 집밥
pages[8] = scene(8, 7, '첫 집밥', '#FFF5E6',
    f'<rect x="70" y="900" width="940" height="300" fill="#E9D6BE"/>'
    + char('bride', 260, 640, 1.0, 'joy', (8, -8)) + char('groom', 820, 640, 1.0, 'joy', (8, -8), flip=True)
    + rice_table(900) + hearts(6, (380, 320, 700, 500), '#FFB3C1', 7),
    '그래도 둘이 차린\n첫 밥은 최고다.')

# 9 마무리
pages[9] = (page_bg('#FFE4E4') + header(9, TOTAL) + hearts(18, (40, 120, 1040, 700), '#FFD0D6', 309)
    + char('bride', 400, 470, 1.15, 'joy', (6, -40)) + char('groom', 690, 460, 1.15, 'happy', (40, -8))
    + f'<rect x="110" y="820" width="860" height="420" rx="60" fill="#fff" stroke="{INK}" stroke-width="6"/>'
    + T(540, 925, '몇 개 공감했어요?', 76, 'j') + T(540, 1035, '댓글로 번호 남기기', 76, 'j', ROSE)
    + T(540, 1145, '같이 장 볼 예비 배우자에게 공유!', 48, 'g', '#7A6262')
    + T(540, 1310, '@yebibubu.toon', 40, 'j', '#C49A9A'))

if __name__ == '__main__':
    render(pages, sys.argv[1] if len(sys.argv) > 1 else 'out/ep30')
