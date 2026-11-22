import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from extra import *

TOTAL = 9


def room(y0=130, y1=1060, night=False):
    wall = '#E9E4F2' if night else '#FFF1E4'
    return (f'<rect x="70" y="{y0}" width="940" height="{y1 - y0}" fill="{wall}"/>'
            f'<rect x="70" y="{y1 - 160}" width="940" height="160" fill="#D9C3AE"/>')


def desk(y=880):
    """거실 낮은 탁자."""
    return (f'<g stroke="{INK}" stroke-width="5" stroke-linejoin="round">'
            f'<rect x="150" y="{y}" width="780" height="60" rx="20" fill="#D7A877"/>'
            f'<rect x="190" y="{y + 60}" width="30" height="80" fill="#B88958"/><rect x="860" y="{y + 60}" width="30" height="80" fill="#B88958"/></g>')


def long_list(x, y, w, n, title, col=None, rot=0):
    """끝없이 길어지는 명단 종이(아래로 말림)."""
    s = f'<g transform="rotate({rot} {x + w / 2} {y})">'
    h = 120 + n * 52
    s += f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="#fff" stroke="{INK}" stroke-width="5"/>'
    s += T(x + w / 2, y + 62, title, 44, 'j', col or INK)
    for i in range(n):
        yy = y + 110 + i * 52
        s += f'<path d="M{x + 30} {yy} h {w * .55 - (i * 37) % 60}" stroke="#B9AFAF" stroke-width="10" stroke-linecap="round"/>'
        s += f'<circle cx="{x + w - 40}" cy="{yy}" r="9" fill="#E8DADA"/>'
    s += (f'<ellipse cx="{x + w / 2}" cy="{y + h}" rx="{w / 2 + 6}" ry="26" fill="#F3EDED" stroke="{INK}" stroke-width="5"/>')
    return s + '</g>'


def photo(x, y, w=220, h=170, rot=-5):
    """빛바랜 옛날 사진(두 친구 실루엣)."""
    return (f'<g transform="rotate({rot} {x + w / 2} {y + h / 2})" stroke="{INK}" stroke-width="5">'
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="#fff"/>'
            f'<rect x="{x + 16}" y="{y + 16}" width="{w - 32}" height="{h - 50}" fill="#F6E0C4"/>'
            f'<circle cx="{x + w * .38}" cy="{y + h * .42}" r="24" fill="#fff"/><circle cx="{x + w * .62}" cy="{y + h * .42}" r="24" fill="#D9B48A"/></g>')


def chat_screen(msgs, title='수아', size=46):
    out = ''
    y = 300
    for side, t in msgs:
        lines = t.split('\n'); bh = len(lines) * size * 1.25 + 34; bw = 420
        bx = 700 - bw if side == 'r' else 380
        out += (f'<rect x="{bx}" y="{y}" width="{bw}" height="{bh}" rx="28" fill="{"#FFE36A" if side == "r" else "#fff"}" stroke="{INK}" stroke-width="3"/>'
                + T(bx + bw / 2, y + size + 8, lines, size, lh=1.25))
        y += bh + 30
    return (f'<rect x="330" y="170" width="420" height="860" rx="50" fill="#3A3542" stroke="{INK}" stroke-width="6"/>'
            f'<rect x="352" y="210" width="376" height="790" rx="26" fill="#DCE9F6"/>' + T(540, 262, title, 44, 'j') + out)


pages = {}
# 1 표지
pages[1] = (page_bg('#FFE4E4') + hearts(22, (40, 40, 1040, 1310), '#FFD0D6', 231)
    + f'<rect x="80" y="70" width="230" height="84" rx="42" fill="{ROSE}"/>' + T(195, 128, '썰툰', 50, 'j', '#fff')
    + T(80, 265, '하객 명단 쓰다가', 104, 'j', INK, 'start') + T(80, 390, '생긴 일', 104, 'j', ROSE, 'start')
    + panel(room(440, 1110) + long_list(560, 500, 300, 9, '오빠 명단', '#3E4C7A', 4)
            + char('bride', 300, 800, .95, 'shock', (60, 110)) + sweat(420, 600), '#FFF1E4', 440, 1110)
    + f'<rect x="70" y="1150" width="940" height="130" rx="65" fill="#fff" stroke="{ROSE}" stroke-width="6"/>' + T(540, 1235, '+ 마지막에 하객 명단 정리 5가지', 54, 'j', INK))
# 2
pages[2] = (page_bg() + header(2, TOTAL)
    + panel(room(night=True) + char('bride', 330, 640, .95, 'happy', (40, 20)) + char('groom', 750, 640, .95, 'happy', (20, 40), flip=True)
            + desk(860) + paper(230, 760, 220, 120, '', (), 30, -6) + paper(630, 760, 220, 120, '', (), 30, 5)
            + T(540, 240, '(청첩장 몇 장 맞추지?)', 54, 'g', '#5A5470'), '#E9E4F2')
    + caption('청첩장 맞추기 전,\n둘이 하객 명단을 쓰기로 했다.'))
# 3
pages[3] = (page_bg() + header(3, TOTAL)
    + panel(room() + long_list(120, 180, 330, 13, '오빠 명단', '#3E4C7A', -3)
            + char('bride', 760, 720, 1.0, 'shock', (8, -8), flip=True) + sweat(860, 560)
            + bubble(560, 170, 400, '이 종이\n언제 끝나?', 50, (740, 470)), '#FFF1E4')
    + caption('오빠 명단은\n끝이 안 보였다.'))
# 4
pages[4] = (page_bg() + header(4, TOTAL)
    + panel(room() + char('groom', 330, 700, 1.05, 'smug', (60, -8))
            + bubble(500, 190, 460, '초등학교 때\n짝꿍도 써야지!', 50, (440, 520))
            + char('bride', 800, 760, .85, 'blank', (-10, -10), flip=True), '#FFF1E4')
    + caption('"연락 안 한 지 오래됐잖아?"\n"그래도 고마운 친구야."'))
# 5
pages[5] = (page_bg() + header(5, TOTAL)
    + panel(room(night=True) + paper(150, 230, 300, 360, '내 명단', [('가족', '', None), ('대학 친구', '', None), ('회사', '', None)], 42, -3)
            + photo(620, 230, 260, 200, 6) + char('bride', 680, 740, 1.0, 'blank', (-10, -10), flip=True)
            + tears(680, 740, .85), '#E9E4F2')
    + caption('그러다 나는 연락이 끊긴\n고등학교 단짝이 떠올랐다.'))
# 6
pages[6] = (page_bg() + header(6, TOTAL)
    + panel(room() + hearts(8, (100, 160, 980, 400), '#FFD0D6', 236)
            + char('bride', 330, 720, 1.0, 'nervous', (8, -8)) + tears(330, 720, .7)
            + char('groom', 750, 710, 1.05, 'happy', (100, -8), flip=True) + phone(600, 800, 86, 150)
            + bubble(430, 180, 520, '지금 연락해 봐.\n분명 반가워할걸?', 50, (700, 480)), '#FFF1E4')
    + caption('오빠가 내 휴대폰을\n살짝 건네줬다.'))
# 7 카톡
pages[7] = (page_bg() + header(7, TOTAL)
    + panel(chat_screen([('r', '수아야 오랜만이야..\n나 결혼해!'), ('l', '헐 진짜???'), ('l', '당연히 가지!!\n나 울어 ㅠㅠ'), ('r', '고마워 ㅠㅠ')]), '#4E4A5A')
    + caption('답장은 1분 만에 왔다.\n괜히 망설였네.'))
# 8 정리
items = [('각자 먼저 쓰기', '따로 쓰고 나중에 합치기'), ('묶어서 나누기', '가족·친구·회사처럼 칸 나누기'),
         ('연락처 같이 적기', '청첩장 보낼 때 덜 헤매요'), ('참석 표시하기', '확실·아마·모름 세 가지로'),
         ('식사 인원 확인', '보증 인원은 홀에 꼭 물어보기')]
p8 = page_bg() + header(8, TOTAL) + T(540, 230, '하객 명단 정리 5가지', 70, 'j')
cols = [ROSE, '#8FD3C1', '#F5B860', '#96B4EE', '#C59BE6']
for i, (a, b) in enumerate(items):
    y = 290 + i * 180
    p8 += f'<rect x="80" y="{y}" width="920" height="156" rx="50" fill="#fff" stroke="{INK}" stroke-width="5"/><circle cx="160" cy="{y+78}" r="46" fill="{cols[i]}"/>'
    p8 += T(160, y + 98, str(i + 1), 56, 'j', '#fff') + T(240, y + 66, a, 52, 'j', INK, 'start') + T(240, y + 126, b, 44, 'g', '#7A6262', 'start')
p8 += T(540, 1250, '고마운 사람이 먼저 떠오르면 그게 정답!', 46, 'g', ROSE)
pages[8] = p8
# 9 마무리
pages[9] = (page_bg('#FFE4E4') + header(9, TOTAL) + hearts(18, (40, 120, 1040, 700), '#FFD0D6', 239)
    + char('bride', 400, 470, 1.15, 'joy', (6, -40)) + char('groom', 690, 460, 1.15, 'happy', (40, -8))
    + f'<rect x="110" y="820" width="860" height="420" rx="60" fill="#fff" stroke="{INK}" stroke-width="6"/>'
    + T(540, 930, '저장해 두고', 76, 'j') + T(540, 1040, '예비 배우자에게 공유하기', 76, 'j', ROSE) + T(540, 1150, '명단 쓰다 떠오른 사람 있어요?', 50, 'g', '#7A6262')
    + T(540, 1310, '@yebibubu.toon', 40, 'j', '#C49A9A'))

if __name__ == '__main__':
    render(pages, sys.argv[1] if len(sys.argv) > 1 else 'out/ep23')
