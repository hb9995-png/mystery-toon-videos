import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from extra import *

TOTAL = 10


def chat_screen(msgs, title='오빠♥', size=46):
    """카톡 화면. msgs: [('r'|'l', 글)] r=나(신부), l=상대"""
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
pages[1] = (page_bg('#FFE4E4') + hearts(22, (40, 40, 1040, 1310), '#FFD0D6', 331)
    + f'<rect x="80" y="70" width="230" height="84" rx="42" fill="{ROSE}"/>' + T(195, 128, '카톡 썰', 50, 'j', '#fff')
    + T(80, 265, '우리 아빠랑 오빠,', 100, 'j', INK, 'start') + T(80, 395, '단둘이 낚시 간 날', 100, 'j', ROSE, 'start')
    + panel(lake(860) + dock(70, 1010, 840)
            + rod(250, 800, -150, -260, 360) + rod(800, 800, 150, -260, 360)
            + char('dadG', 330, 640, .8, 'blank', (8, -8)) + char('groom', 720, 640, .8, 'nervous', (8, -8)) + sweat(810, 520)
            + T(540, 560, '……', 70, 'j', '#7A8090'), '#E4F1F8', 440, 1110)
    + f'<rect x="70" y="1150" width="940" height="130" rx="65" fill="#fff" stroke="{ROSE}" stroke-width="6"/>' + T(540, 1235, '+ 예비 부모님과 친해지는 법', 58, 'j', INK))
# 2 아빠의 제안
pages[2] = (page_bg() + header(2, TOTAL)
    + panel(f'<rect x="70" y="820" width="940" height="300" fill="#E9D6BE"/>'
            + char('dadG', 300, 600, 1.0, 'smug', (8, -8)) + char('groom', 780, 600, 1.0, 'shock', (8, -8), flip=True) + sweat(890, 450)
            + bubble(110, 180, 420, '이번 주말에\n낚시 가겠나?', 50, (300, 420)), '#FFF5E6')
    + caption('아빠가 갑자기\n오빠한테 낚시를 권했다.'))
# 3 카톡 1
pages[3] = (page_bg() + header(3, TOTAL)
    + panel(chat_screen([('l', '아버님이랑\n둘이 낚시래'), ('l', '무슨 얘기 하지?'), ('r', '아빠 원래\n말씀 별로 없어'), ('r', '그냥 같이 있어 ㅋㅋ')]), '#4E4A5A')
    + caption('오빠는 전날 밤부터\n긴장하기 시작했다.'))
# 4 침묵
pages[4] = (page_bg() + header(4, TOTAL)
    + panel(lake(760) + dock(70, 1010, 740)
            + rod(220, 700, -110, -300, 420) + rod(840, 700, 120, -300, 420)
            + char('dadG', 300, 540, .9, 'blank', (8, -8)) + char('groom', 760, 540, .9, 'nervous', (8, -8)) + sweat(860, 410) + sweat(650, 380, .8)
            + T(540, 300, '……', 90, 'j', '#7A8090'), '#E4F1F8')
    + caption('물가에 앉자\n정적이 흘렀다.'))
# 5 카톡 2
pages[5] = (page_bg() + header(5, TOTAL)
    + panel(chat_screen([('l', '30분째\n아무 말 없으셔'), ('l', '물고기도 안 잡혀'), ('r', '아빠 지금\n제일 편하신 거야'), ('r', '진짜로 ㅋㅋ')]), '#4E4A5A')
    + caption('오빠는 몰래\n실시간 중계를 했다.'))
# 6 입질
pages[6] = (page_bg() + header(6, TOTAL)
    + panel(lake(760) + dock(70, 1010, 740)
            + rod(780, 700, 170, -440, 150) + fish(950, 450, .65, '#F2A65A', -80)
            + ''.join(f'<path d="M{x} {y} l 30 0" stroke="#fff" stroke-width="8" stroke-linecap="round"/>' for x, y in ((850, 380), (850, 450), (860, 520)))
            + char('dadG', 280, 540, .9, 'joy', (100, 100)) + char('groom', 640, 520, .9, 'shock', (8, -8))
            + T(300, 290, '당겨!!', 80, 'j', '#C0392B'), '#E4F1F8')
    + caption('그때 오빠 낚싯대에\n입질이 왔다.'))
# 7 카톡 3
pages[7] = (page_bg() + header(7, TOTAL)
    + panel(chat_screen([('l', '잡았어!!'), ('l', '아버님이 처음\n크게 웃으셨어'), ('l', '사진도 찍어\n주셨다 ㅠㅠ'), ('r', '거봐 ㅋㅋㅋ')]), '#4E4A5A')
    + caption('물고기 한 마리에\n둘 다 신이 났다.'))
# 8 아빠 카톡
pages[8] = (page_bg() + header(8, TOTAL)
    + panel(chat_screen([('l', '(사진)\n물고기 든 사위'), ('l', '그 친구\n괜찮더라'), ('l', '다음 달에\n또 간다'), ('r', '아빠 ㅋㅋ ♥')], title='아빠'), '#4E4A5A')
    + caption('그날 저녁,\n아빠한테도 카톡이 왔다.'))
# 9 정리
items = [('먼저 짧게 안부 묻기', '부담 없이 자주, 가볍게'), ('좋아하시는 것 묻기', '취미 하나면 대화가 열려요'), ('침묵을 겁내지 않기', '같이 있는 시간도 대화예요'),
         ('배우자가 다리 놓기', '말투·취향 미리 알려 주기'), ('고마움은 말로 전하기', '작은 인사가 오래 남아요')]
p9 = page_bg() + header(9, TOTAL) + T(540, 230, '예비 부모님과 친해지는 법', 62, 'j')
cols = [ROSE, '#8FD3C1', '#F5B860', '#96B4EE', '#C59BE6']
for i, (a, b) in enumerate(items):
    y = 290 + i * 180
    p9 += f'<rect x="80" y="{y}" width="920" height="156" rx="50" fill="#fff" stroke="{INK}" stroke-width="5"/><circle cx="160" cy="{y+78}" r="46" fill="{cols[i]}"/>'
    p9 += T(160, y + 98, str(i + 1), 56, 'j', '#fff') + T(240, y + 66, a, 50, 'j', INK, 'start') + T(240, y + 126, b, 44, 'g', '#7A6262', 'start')
p9 += T(540, 1250, '서두르지 말고 천천히!', 46, 'g', ROSE)
pages[9] = p9
# 10 마무리
pages[10] = (page_bg('#FFE4E4') + header(10, TOTAL) + hearts(18, (40, 120, 1040, 700), '#FFD0D6', 339)
    + char('bride', 400, 470, 1.15, 'joy', (6, 120)) + char('groom', 690, 460, 1.15, 'joy', (120, -8))
    + fish(880, 260, .6, '#F2A65A', 15)
    + f'<rect x="110" y="820" width="860" height="420" rx="60" fill="#fff" stroke="{INK}" stroke-width="6"/>'
    + T(540, 930, '예비 부모님과 첫 외출?', 70, 'j') + T(540, 1040, '댓글로 들려주세요', 76, 'j', ROSE) + T(540, 1150, '긴장 중인 예비 배우자에게 공유!', 48, 'g', '#7A6262')
    + T(540, 1310, '@yebibubu.toon', 40, 'j', '#C49A9A'))

if __name__ == '__main__':
    render(pages, sys.argv[1] if len(sys.argv) > 1 else 'out/ep33')
