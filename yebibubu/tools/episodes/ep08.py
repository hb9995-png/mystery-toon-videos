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


def night(y0=130, y1=1060):
    s = f'<rect x="70" y="{y0}" width="940" height="{y1 - y0}" fill="#2E3557"/>'
    import random; r = random.Random(8)
    for _ in range(40):
        s += f'<circle cx="{r.uniform(90, 990)}" cy="{r.uniform(y0 + 20, y0 + 500)}" r="{r.uniform(2, 5)}" fill="#FFF6C8"/>'
    return s + f'<circle cx="860" cy="260" r="60" fill="#FFF1A8"/><circle cx="885" cy="245" r="54" fill="#2E3557"/>'


def bench(y):
    return (f'<g stroke="{INK}" stroke-width="5" stroke-linejoin="round"><rect x="200" y="{y}" width="680" height="40" rx="12" fill="#C99561"/>'
            f'<rect x="230" y="{y + 40}" width="24" height="120" fill="#8C6A4E"/><rect x="826" y="{y + 40}" width="24" height="120" fill="#8C6A4E"/></g>')


pages = {}
# 1 표지
pages[1] = (page_bg('#FFE4E4') + hearts(22, (40, 40, 1040, 1310), '#FFD0D6', 81)
    + f'<rect x="80" y="70" width="230" height="84" rx="42" fill="{ROSE}"/>' + T(195, 128, '본식 썰', 50, 'j', '#fff')
    + T(80, 265, '본식 전날 밤', 110, 'j', INK, 'start') + T(80, 395, '오빠가 사라진 썰', 110, 'j', ROSE, 'start')
    + panel(night(440, 1110) + bench(880) + char('groom', 540, 820, 1.1, 'nervous', (100, -10)) + notebook(735, 760, 210, 160, '서약서', -8)
            + sweat(690, 620) + T(250, 560, '???', 90, 'j', '#FFF1A8'), '#2E3557', 440, 1110)
    + f'<rect x="70" y="1150" width="940" height="130" rx="65" fill="#fff" stroke="{ROSE}" stroke-width="6"/>' + T(540, 1235, '+ 본식 전날 챙길 5가지', 58, 'j', INK))
# 2
pages[2] = (page_bg() + header(2, TOTAL)
    + panel(hearts(12, (100, 160, 980, 600), '#FFD0D6', 82) + calendar(620, 200, 300, (17,), '내일 본식')
            + char('bride', 360, 700, 1.25, 'joy', (6, -40)), '#FFF0DC')
    + caption('드디어 내일이 본식.\n설레서 잠이 안 왔다.'))
# 3
pages[3] = (page_bg() + header(3, TOTAL)
    + panel(chat_screen([('r', '오빠 자?'), ('r', '나 너무 떨려 ㅠㅠ'), ('r', '오빠?'), ('r', '1 안 없어짐...')]), '#4E4A5A')
    + caption('밤 11시.\n오빠가 카톡을 안 읽는다.'))
# 4
pages[4] = (page_bg() + header(4, TOTAL)
    + panel(speed(540, 660, '#E3E8F2', 44, 330) + char('bride', 540, 680, 1.45, 'shock') + sweat(730, 480) + sweat(360, 500, .8)
            + T(540, 250, '(뚜르르르... 뚜르르르...)', 58, 'g', '#7A8090'), '#EEF1F7')
    + caption('전화도 안 받는다.\n심장이 쿵 내려앉았다.'))
# 5
pages[5] = (page_bg() + header(5, TOTAL)
    + panel(night() + bench(820) + char('groom', 540, 760, 1.2, 'nervous', (100, -10)) + notebook(740, 680, 220, 170, '서약서', -8)
            + sweat(720, 560) + T(330, 330, '(중얼중얼...)', 62, 'g', '#FFF6C8'), '#2E3557')
    + caption('같은 시각, 오빠는\n동네 놀이터 벤치에 있었다.'))
# 6 카톡
pages[6] = (page_bg() + header(6, TOTAL)
    + panel(chat_screen([('l', '헉 미안 ㅠㅠ\n폰 무음이었어'), ('l', '혼인 서약\n외우는 중이었어'), ('l', '세 줄 넘어가면\n자꾸 울컥해서...'), ('r', '...바보야 ㅠㅠ')]), '#4E4A5A')
    + caption('한참 뒤에야\n답장이 왔다.'))
# 7
pages[7] = (page_bg() + header(7, TOTAL)
    + panel(hearts(12, (100, 160, 980, 600), '#FFD0D6', 87) + char('bride', 380, 700, 1.2, 'joy', (-40, 120)) + char('groom', 700, 690, 1.2, 'joy', (120, -40))
            + tears(700, 690, 1.0) + bubble(120, 170, 840, '그럼 반은 내가 읽을게.\n같이 하면 덜 떨리잖아', 56, (400, 430)), '#FFF5D8')
    + caption('다음 날 서약은 반씩 나눠 읽었다.\n물론 둘 다 울었다.'))
# 8 정리
items = [('서약서·편지', '미리 출력해서 가방에 넣어 두기'), ('반지·소품', '누가 들고 갈지 한 사람 정하기'), ('축의금 받을 사람', '양가에서 한 명씩 미리 부탁'),
         ('당일 연락 담당', '헬퍼·플래너 번호를 친구에게 공유'), ('일찍 자기', '휴대폰은 소리 켜 두고 충전기 꽂기')]
p8 = page_bg() + header(8, TOTAL) + T(540, 230, '본식 전날 챙길 5가지', 72, 'j')
cols = [ROSE, '#8FD3C1', '#F5B860', '#96B4EE', '#C59BE6']
for i, (a, b) in enumerate(items):
    y = 290 + i * 180
    p8 += f'<rect x="80" y="{y}" width="920" height="156" rx="50" fill="#fff" stroke="{INK}" stroke-width="5"/><circle cx="160" cy="{y+78}" r="46" fill="{cols[i]}"/>'
    p8 += T(160, y + 98, str(i + 1), 56, 'j', '#fff') + T(240, y + 66, a, 52, 'j', INK, 'start') + T(240, y + 126, b, 44, 'g', '#7A6262', 'start')
p8 += T(540, 1250, '전날 밤엔 서로 연락 잘 되게 해 두기!', 48, 'g', ROSE)
pages[8] = p8
# 9 마무리
pages[9] = (page_bg('#FFE4E4') + header(9, TOTAL) + hearts(18, (40, 120, 1040, 700), '#FFD0D6', 89)
    + char('bride', 400, 470, 1.15, 'joy', (6, -40)) + char('groom', 690, 460, 1.15, 'joy', (40, -8))
    + f'<rect x="110" y="820" width="860" height="420" rx="60" fill="#fff" stroke="{INK}" stroke-width="6"/>'
    + T(540, 930, '저장해 두고', 76, 'j') + T(540, 1040, '예비 배우자에게 공유하기', 76, 'j', ROSE) + T(540, 1150, '여러분 본식 전날 썰도 댓글로!', 50, 'g', '#7A6262')
    + T(540, 1310, '@yebibubu.toon', 40, 'j', '#C49A9A'))

if __name__ == '__main__':
    render(pages, sys.argv[1] if len(sys.argv) > 1 else 'out/ep08')
