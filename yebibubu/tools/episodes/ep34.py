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


def bowls(y=900):
    """바닥에 놓인 그릇 두 개 + 젓가락."""
    s = f'<g stroke="{INK}" stroke-width="5">'
    for cx in (440, 640):
        s += (f'<path d="M{cx - 70} {y - 10} H {cx + 70} Q {cx + 70} {y + 50} {cx} {y + 50} Q {cx - 70} {y + 50} {cx - 70} {y - 10} z" fill="#F07B5A"/>'
              f'<path d="M{cx - 40} {y - 30} l 90 -70 M {cx - 20} {y - 20} l 90 -70" stroke="#C9A07A" stroke-width="7"/>')
    s += '</g>'
    return s + ''.join(f'<path d="M{x} {y - 60} q 16 -24 0 -48 t 0 -48" fill="none" stroke="#B9B2C4" stroke-width="6"/>' for x in (440, 640))


def socks(x, y):
    return (f'<g stroke="{INK}" stroke-width="4" stroke-linejoin="round">'
            f'<path d="M{x} {y} v 70 q 0 30 40 30 h 40 v -36 h -40 v -64 z" fill="#96B4EE"/>'
            f'<path d="M{x + 110} {y - 10} v 70 q 0 30 40 30 h 40 v -36 h -40 v -64 z" fill="#FFB3C1"/></g>')


pages = {}
# 1 표지
pages[1] = (page_bg('#FFE4E4') + hearts(22, (40, 40, 1040, 1310), '#FFD0D6', 341)
    + f'<rect x="80" y="70" width="240" height="84" rx="42" fill="{ROSE}"/>' + T(200, 128, '공감 주의', 50, 'j', '#fff')
    + T(80, 265, '신혼집 이삿날', 108, 'j', INK, 'start') + T(80, 395, '생기는 일 7가지', 108, 'j', ROSE, 'start')
    + panel(floor(980, '#F3E6D6') + box(80, 830, 170, 150, '주방') + box(95, 700, 140, 130) + box(820, 830, 180, 150, '옷')
            + char('bride', 410, 760, .8, 'joy', (6, -6)) + char('groom', 660, 760, .8, 'nervous', (8, -8)) + sweat(750, 630), '#FFF7EE', 440, 1110)
    + f'<rect x="70" y="1150" width="940" height="130" rx="65" fill="#fff" stroke="{ROSE}" stroke-width="6"/>' + T(540, 1235, '+ 몇 개 공감했는지 댓글로', 58, 'j', INK))
# 2 상자 산
pages[2] = scene(2, 1, '상자가 끝이 없다', '#FFF5E6',
    floor(880) + box(560, 730, 240, 150) + box(590, 590, 200, 140) + box(610, 470, 160, 120) + box(800, 760, 190, 120) + box(820, 650, 150, 110)
    + char('bride', 300, 640, 1.0, 'shock', (8, -8)) + sweat(420, 500),
    '분명 짐 별로 없었는데\n상자가 끝이 없다.')
# 3 가위
pages[3] = scene(3, 2, '가위 어디 있어?', '#EAF4F8',
    floor(880, '#D6E6EE') + box(430, 760, 220, 150)
    + char('bride', 250, 620, .95, 'nervous', (8, -8)) + char('groom', 830, 620, .95, 'nervous', (8, -8), flip=True)
    + bubble(360, 300, 360, '가위는…\n저 상자 안에', 48, (540, 560)),
    '상자 뜯을 가위가\n상자 안에 있다.')
# 4 라벨과 다른 내용물
pages[4] = scene(4, 3, '주방 상자의 비밀', '#F4ECFA',
    floor(900, '#E5DAF0') + box(400, 720, 280, 190, '주방') + socks(440, 610)
    + char('bride', 220, 640, .9, 'blank', (8, -8)) + char('groom', 860, 640, .9, 'smug', (8, -8), flip=True) + sweat(960, 500),
    '"주방" 상자를 열었더니\n양말이 나왔다.')
# 5 커튼 없음
pages[5] = scene(5, 4, '커튼이 없다', '#FFFBEA',
    window(560, 300, 380, 420) + floor(900, '#F2E2C4')
    + char('groom', 330, 640, 1.0, 'blank', (130, -8)) + T(330, 330, '눈부셔…', 56, 'g', '#7A8090'),
    '첫 아침, 커튼이 없어서\n해랑 같이 일어났다.')
# 6 바닥 첫 끼
pages[6] = scene(6, 5, '첫 끼는 바닥에서', '#FFF5E6',
    floor(880) + box(460, 760, 160, 120) + bowls(960)
    + char('bride', 230, 640, .95, 'joy', (8, -8)) + char('groom', 850, 640, .95, 'joy', (8, -8), flip=True),
    '식탁이 아직 없어서\n상자 옆 바닥에서 먹었다.')
# 7 택배
pages[7] = scene(7, 6, '택배가 매일 온다', '#EEF1F7',
    floor(880, '#D9DEE8') + door(700, 360, 220, 520) + box(560, 780, 160, 100) + box(590, 690, 120, 90)
    + char('groom', 330, 620, 1.0, 'shock', (8, -8)) + sweat(450, 480),
    '이사 끝났는데\n택배는 매일 온다.')
# 8 첫날 밤
pages[8] = scene(8, 7, '우리 집이다', '#FFF0E0',
    lamp(540, 330) + floor(900, '#E9D6BE') + box(820, 760, 170, 140)
    + char('bride', 400, 650, 1.0, 'happy', (8, -8)) + char('groom', 680, 650, 1.0, 'happy', (8, -8), flip=True)
    + hearts(5, (420, 280, 660, 420), '#FFB3C1', 8),
    '그래도 불 끄고 누우면\n"우리 집이다" 싶다.')
# 9 마무리
pages[9] = (page_bg('#FFE4E4') + header(9, TOTAL) + hearts(18, (40, 120, 1040, 700), '#FFD0D6', 349)
    + char('bride', 400, 470, 1.15, 'joy', (6, -40)) + char('groom', 690, 460, 1.15, 'happy', (40, -8))
    + f'<rect x="110" y="820" width="860" height="420" rx="60" fill="#fff" stroke="{INK}" stroke-width="6"/>'
    + T(540, 925, '몇 개 공감했어요?', 76, 'j') + T(540, 1035, '댓글로 번호 남기기', 76, 'j', ROSE)
    + T(540, 1145, '이사 앞둔 예비 배우자에게 공유!', 48, 'g', '#7A6262')
    + T(540, 1310, '@yebibubu.toon', 40, 'j', '#C49A9A'))

if __name__ == '__main__':
    render(pages, sys.argv[1] if len(sys.argv) > 1 else 'out/ep34')
