import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from extra import *

TOTAL = 10


def chat_screen(msgs, title='오빠♥', size=46):
    """카톡 화면. msgs: [('r'|'l', 글)] r=나(신부), l=오빠"""
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


def think(x, y, w, h, inner, col='#fff'):
    return (f'<g stroke="{INK}" stroke-width="5"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="60" fill="{col}"/>'
            f'<circle cx="{x + w / 2}" cy="{y + h + 40}" r="20" fill="{col}"/><circle cx="{x + w / 2 + 10}" cy="{y + h + 90}" r="12" fill="{col}"/></g>' + inner)



def pot(x, y, s=1.0):
    """죽 냄비. (x, y) 는 냄비 가운데."""
    st = ''.join(f'<path d="M{x + k * 40 * s} {y - 70 * s} q 20 -30 0 -60 t 0 -60" fill="none" stroke="#B9B2C4" stroke-width="6"/>' for k in (-1, 0, 1))
    return (st + f'<g stroke="{INK}" stroke-width="5"><rect x="{x - 110 * s}" y="{y - 60 * s}" width="{220 * s}" height="{130 * s}" rx="{30 * s}" fill="#E8B04B"/>'
            f'<ellipse cx="{x}" cy="{y - 60 * s}" rx="{110 * s}" ry="{24 * s}" fill="#FFF6DA"/>'
            f'<path d="M{x - 110 * s} {y - 30 * s} h -40 M{x + 110 * s} {y - 30 * s} h 40" stroke-width="10"/></g>')


def umbrella(x, y, w=520, col='#96B4EE'):
    return (f'<g stroke="{INK}" stroke-width="5" stroke-linejoin="round">'
            f'<path d="M{x - w / 2} {y} Q {x} {y - w * .55} {x + w / 2} {y} q -{w / 8} -30 -{w / 4} 0 q -{w / 8} -30 -{w / 4} 0 q -{w / 8} -30 -{w / 4} 0 q -{w / 8} -30 -{w / 4} 0 z" fill="{col}"/>'
            f'<path d="M{x} {y - w * .28} V {y + 330}" stroke-width="7" fill="none"/></g>')


def rain(seed=3, area=(80, 140, 1000, 1050), n=40):
    import random
    r = random.Random(seed); x0, y0, x1, y1 = area
    return ''.join(f'<path d="M{(x := r.uniform(x0, x1))} {(y := r.uniform(y0, y1))} l -10 40" stroke="#7FA9D9" stroke-width="5" stroke-linecap="round"/>' for _ in range(n))


pages = {}
# 1 표지
pages[1] = (page_bg('#FFE4E4') + hearts(22, (40, 40, 1040, 1310), '#FFD0D6', 251)
    + f'<rect x="80" y="70" width="230" height="84" rx="42" fill="{ROSE}"/>' + T(195, 128, '카톡 썰', 50, 'j', '#fff')
    + T(80, 265, '결혼 결심한 순간', 108, 'j', INK, 'start') + T(80, 395, '물어봤더니', 108, 'j', ROSE, 'start')
    + panel(phone(150, 560, 190, 330, inner=T(245, 760, '?', 120, 'j', ROSE))
            + char('bride', 560, 790, .9, 'smug', (60, -6)) + char('groom', 830, 800, .85, 'nervous', (8, -8), flip=True) + sweat(930, 640), '#FFF7EE', 440, 1110)
    + f'<rect x="70" y="1150" width="940" height="130" rx="65" fill="#fff" stroke="{ROSE}" stroke-width="6"/>' + T(540, 1235, '+ 서로 물어볼 질문 5가지', 58, 'j', INK))
# 2
pages[2] = (page_bg() + header(2, TOTAL)
    + panel(f'<rect x="70" y="760" width="940" height="400" fill="#C9C3E0"/>' + f'<circle cx="860" cy="260" r="60" fill="#FFF2B8" stroke="{INK}" stroke-width="5"/>'
            + char('bride', 450, 700, 1.15, 'happy', (100, -6)) + phone(680, 560, 130, 220)
            + T(300, 280, '(문득…)', 60, 'g', '#7A8090'), '#E4E8F4')
    + caption('자려고 누웠다가\n갑자기 궁금해졌다.'))
# 3 카톡 1
pages[3] = (page_bg() + header(3, TOTAL)
    + panel(chat_screen([('r', '오빠는 언제\n결혼 결심했어?'), ('l', '갑자기? ㅋㅋ'), ('l', '음...'), ('r', '빨리 말해!')]), '#4E4A5A')
    + caption('오빠는 답장이\n바로 안 왔다.'))
# 4 오빠 입력 중
pages[4] = (page_bg() + header(4, TOTAL)
    + panel(f'<rect x="70" y="800" width="940" height="400" fill="#D9CDBE"/>'
            + char('groom', 440, 700, 1.15, 'nervous', (100, -6)) + phone(670, 580, 130, 220) + sweat(300, 560) + sweat(580, 520, .8)
            + bubble(640, 220, 300, '. . .', 60, (720, 560)) + T(250, 280, '(입력 중)', 56, 'g', '#7A8090'), '#EFE6DA')
    + caption('오빠는 한참이나\n입력 중이었다.'))
# 5 카톡 2
pages[5] = (page_bg() + header(5, TOTAL)
    + panel(chat_screen([('l', '나 감기 걸렸던\n날 기억나?'), ('l', '네가 죽을\n끓여 왔잖아'), ('l', '"짜면 말해"\n하면서'), ('r', '...그게 다야?')]), '#4E4A5A')
    + caption('작년 겨울,\n오빠가 크게 아팠던 날.'))
# 6 회상
pages[6] = (page_bg() + header(6, TOTAL)
    + panel(f'<rect x="70" y="820" width="940" height="400" fill="#F2D9C4"/>'
            + char('groom', 700, 620, 1.0, 'blank', (8, -8), flip=True)
            + f'<rect x="520" y="760" width="420" height="320" rx="60" fill="#B7C4D9" stroke="{INK}" stroke-width="5"/>'
            + char('bride', 300, 640, 1.0, 'happy', (70, 70)) + pot(300, 960, .8)
            + T(880, 300, '콜록', 56, 'j', '#9A8FB5') + T(160, 260, '(회상)', 52, 'g', '#7A8090'), '#FFF1E2')
    + caption('사실 그 죽,\n엄청 짰다.'))
# 7 카톡 3
pages[7] = (page_bg() + header(7, TOTAL)
    + panel(chat_screen([('l', '짠 죽 먹다가\n생각했어'), ('l', '아파도 이 사람\n옆이면 되겠다'), ('r', 'ㅠㅠㅠ\n감동이야'), ('l', '근데 너는?')]), '#4E4A5A')
    + caption('짠 죽 한 그릇에\n결심을 했단다.'))
# 8 내 답
pages[8] = (page_bg() + header(8, TOTAL)
    + panel(chat_screen([('r', '우산 하나로\n같이 쓴 날'), ('r', '오빠 어깨만\n다 젖었잖아'), ('r', '그때였어'), ('l', '일부러 그런\n건데 ㅎㅎ')]), '#4E4A5A')
    + caption('우리 둘 다\n작은 순간이었다.'))
# 9 정리
items = [('언제 결혼을 결심했어?', '처음 마음 꺼내 보기'), ('내 어떤 점이 좋아?', '작은 습관까지 말해 주기'), ('서운했던 적 있어?', '그때 못 한 말 풀기'),
         ('힘들 때 뭐가 필요해?', '위로받는 방식 알아 두기'), ('우리 집은 어떤 모습?', '같이 사는 하루 그려 보기')]
p9 = page_bg() + header(9, TOTAL) + T(540, 230, '서로 물어볼 질문 5가지', 64, 'j')
cols = [ROSE, '#8FD3C1', '#F5B860', '#96B4EE', '#C59BE6']
for i, (a, b) in enumerate(items):
    y = 290 + i * 180
    p9 += f'<rect x="80" y="{y}" width="920" height="156" rx="50" fill="#fff" stroke="{INK}" stroke-width="5"/><circle cx="160" cy="{y+78}" r="46" fill="{cols[i]}"/>'
    p9 += T(160, y + 98, str(i + 1), 56, 'j', '#fff') + T(240, y + 66, a, 50, 'j', INK, 'start') + T(240, y + 126, b, 44, 'g', '#7A6262', 'start')
p9 += T(540, 1250, '자기 전에 하나씩 물어보기', 46, 'g', ROSE)
pages[9] = p9
# 10 마무리
pages[10] = (page_bg('#FFE4E4') + header(10, TOTAL) + hearts(18, (40, 120, 1040, 700), '#FFD0D6', 259)
    + char('bride', 400, 470, 1.15, 'joy', (6, -40)) + char('groom', 690, 460, 1.15, 'happy', (40, -8))
    + f'<rect x="110" y="820" width="860" height="420" rx="60" fill="#fff" stroke="{INK}" stroke-width="6"/>'
    + T(540, 930, '결혼 결심한 순간', 76, 'j') + T(540, 1040, '댓글로 들려주세요', 76, 'j', ROSE) + T(540, 1150, '예비 배우자에게 이 질문 보내기', 48, 'g', '#7A6262')
    + T(540, 1310, '@yebibubu.toon', 40, 'j', '#C49A9A'))

if __name__ == '__main__':
    render(pages, sys.argv[1] if len(sys.argv) > 1 else 'out/ep25')
