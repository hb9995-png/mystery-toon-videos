import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from extra import *

TOTAL = 9


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


def tie(x, y, col, s=1.0):
    return (f'<g transform="translate({x} {y}) scale({s})" stroke="{INK}" stroke-width="5" stroke-linejoin="round">'
            f'<path d="M-24 0 H 24 L 14 34 L 30 200 L 0 240 L -30 200 L -14 34 Z" fill="{col}"/><path d="M-14 34 H 14"/></g>')


pages = {}
# 1 표지
pages[1] = (page_bg('#FFE4E4') + hearts(22, (40, 40, 1040, 1310), '#FFD0D6', 171)
    + f'<rect x="80" y="70" width="230" height="84" rx="42" fill="{ROSE}"/>' + T(195, 128, '카톡 썰', 50, 'j', '#fff')
    + T(80, 265, '상견례 전날 밤', 108, 'j', INK, 'start') + T(80, 395, '오빠가 보낸 카톡', 108, 'j', ROSE, 'start')
    + panel(char('bride', 360, 800, 1.05, 'smug', (6, 120)) + char('groom', 720, 790, 1.05, 'nervous', (8, -8), flip=True)
            + phone(130, 820, 120, 200) + sweat(850, 640) + sweat(890, 740, .8), '#FFF7EE', 440, 1110)
    + f'<rect x="70" y="1150" width="940" height="130" rx="65" fill="#fff" stroke="{ROSE}" stroke-width="6"/>' + T(540, 1235, '+ 상견례 전 맞춰 둘 5가지', 58, 'j', INK))
# 2
pages[2] = (page_bg() + header(2, TOTAL)
    + panel(char('bride', 540, 720, 1.35, 'blank') + phone(700, 560, 150, 250)
            + T(540, 250, '(밤 11시, 불 끄기 직전)', 54, 'g', '#7A8090'), '#E8ECF6')
    + caption('상견례 전날 밤.\n자려는데 폰이 울렸다.'))
# 3 카톡 1
pages[3] = (page_bg() + header(3, TOTAL)
    + panel(chat_screen([('l', '자?'), ('l', '내일 아버님이\n뭐 물어보시면'), ('l', '뭐라고 해야 돼?'), ('r', '오빠 그냥\n오빠답게 해 ㅋㅋ')]), '#4E4A5A')
    + caption('오빠, 완전 긴장했다.'))
# 4 거울 연습
pages[4] = (page_bg() + header(4, TOTAL)
    + panel(mirror(640, 260, 260, 620) + char('groom', 380, 760, 1.25, 'nervous', (90, 90)) + sweat(540, 560) + sweat(250, 580, .8)
            + bubble(110, 180, 460, '처음 뵙겠습니다!\n(꾸벅)', 52, (360, 440)), '#EEF1F7')
    + caption('알고 보니 거울 앞에서\n인사 연습 중이었다.'))
# 5 카톡 2
pages[5] = (page_bg() + header(5, TOTAL)
    + panel(chat_screen([('l', '인사 연습\n계속 하는 중'), ('l', '넥타이 세 개 중에\n골라 줘'), ('l', '(사진 3장)'), ('r', '파란 거!\n그리고 이제 자 ㅋㅋ')]), '#4E4A5A')
    + caption('넥타이 사진까지\n보내왔다.'))
# 6 신부도 긴장
pages[6] = (page_bg() + header(6, TOTAL)
    + panel(tie(220, 300, '#E06C7A', .9) + tie(860, 300, '#7FA9D9', .9) + tie(540, 220, '#7FC58F', .7)
            + char('bride', 540, 760, 1.35, 'nervous', (100, 100)) + sweat(720, 560) + sweat(360, 580, .8), '#FFF5D8')
    + caption('사실 나도 떨려서\n잠이 안 오고 있었다.'))
# 7 카톡 3
pages[7] = (page_bg() + header(7, TOTAL)
    + panel(chat_screen([('r', '우리 엄마\n오빠 좋아해'), ('r', '내일 나도\n옆에 있을게'), ('l', '...고마워'), ('l', '내일 우리\n같은 편 하자')]), '#4E4A5A')
    + caption('그래서 내가\n먼저 마음을 보냈다.'))
# 8 정리
items = [('호칭 맞추기', '서로 부모님을 어떻게 부를지'), ('부모님 취향 공유', '좋아하는 음식·싫어하는 것'), ('피할 화제 정하기', '민감한 이야기는 미리 둘이'),
         ('장소·계산 미리', '누가 예약하고 계산할지'), ('끝나고 연락', '각자 부모님께 감사 인사')]
p8 = page_bg() + header(8, TOTAL) + T(540, 230, '상견례 전 맞춰 둘 5가지', 72, 'j')
cols = [ROSE, '#8FD3C1', '#F5B860', '#96B4EE', '#C59BE6']
for i, (a, b) in enumerate(items):
    y = 290 + i * 180
    p8 += f'<rect x="80" y="{y}" width="920" height="156" rx="50" fill="#fff" stroke="{INK}" stroke-width="5"/><circle cx="160" cy="{y+78}" r="46" fill="{cols[i]}"/>'
    p8 += T(160, y + 98, str(i + 1), 56, 'j', '#fff') + T(240, y + 66, a, 52, 'j', INK, 'start') + T(240, y + 126, b, 44, 'g', '#7A6262', 'start')
p8 += T(540, 1250, '완벽한 인사보다 둘이 같은 편인 게 먼저', 46, 'g', ROSE)
pages[8] = p8
# 9 마무리
pages[9] = (page_bg('#FFE4E4') + header(9, TOTAL) + hearts(18, (40, 120, 1040, 700), '#FFD0D6', 179)
    + char('bride', 400, 470, 1.15, 'joy', (6, -40)) + char('groom', 690, 460, 1.15, 'happy', (40, -8))
    + f'<rect x="110" y="820" width="860" height="420" rx="60" fill="#fff" stroke="{INK}" stroke-width="6"/>'
    + T(540, 930, '상견례 때 제일', 76, 'j') + T(540, 1040, '떨렸던 순간은?', 76, 'j', ROSE) + T(540, 1150, '댓글로 남기고 예비 배우자 태그하기', 48, 'g', '#7A6262')
    + T(540, 1310, '@yebibubu.toon', 40, 'j', '#C49A9A'))

if __name__ == '__main__':
    render(pages, sys.argv[1] if len(sys.argv) > 1 else 'out/ep17')
