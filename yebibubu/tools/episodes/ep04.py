import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from extra import *

TOTAL = 9


def chat_screen(msgs, title='오빠♥', size=48):
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


def sofa(y):
    return (f'<g stroke="{INK}" stroke-width="5" stroke-linejoin="round"><rect x="90" y="{y}" width="900" height="260" rx="60" fill="#9FC7B8"/>'
            f'<rect x="130" y="{y + 90}" width="820" height="150" rx="40" fill="#B7D9CC"/></g>')


pages = {}
# 1 표지
pages[1] = (page_bg('#FFE4E4') + hearts(22, (40, 40, 1040, 1310), '#FFD0D6', 41)
    + f'<rect x="80" y="70" width="230" height="84" rx="42" fill="{ROSE}"/>' + T(195, 128, '카톡 썰', 50, 'j', '#fff')
    + T(80, 265, '신혼여행지 정하다', 104, 'j', INK, 'start') + T(80, 392, '카톡으로 싸운 썰', 104, 'j', ROSE, 'start')
    + panel(sofa(800) + char('bride', 360, 760, 1.0, 'nervous', (6, -6)) + char('groom', 720, 750, 1.0, 'smug', (8, -8), flip=True)
            + phone(110, 820, 120, 200) + phone(860, 820, 120, 200) + sweat(500, 640) + sweat(860, 620), '#FFF7EE', 440, 1110)
    + f'<rect x="70" y="1150" width="940" height="130" rx="65" fill="#fff" stroke="{ROSE}" stroke-width="6"/>' + T(540, 1235, '+ 신혼여행지 정할 때 맞춰볼 5가지', 56, 'j', INK))
# 2
pages[2] = (page_bg() + header(2, TOTAL)
    + panel(sofa(760) + char('bride', 360, 690, 1.1, 'happy') + char('groom', 720, 680, 1.1, 'joy', (8, 120))
            + bubble(470, 180, 480, '우리 신혼여행\n어디 갈래?', 58, (700, 420)), '#FFF0DC')
    + caption('식장도 정했으니\n이제 신나는 것만 남았다.'))
# 3 카톡 1
pages[3] = (page_bg() + header(3, TOTAL)
    + panel(chat_screen([('r', '난 바다!\n누워만 있을래 🏝'), ('l', '난 유럽!\n하루에 3도시 🏰'), ('r', '3도시...?'), ('l', '최소 3도시')]), '#4E4A5A')
    + caption('각자 폰으로 찾아보다가\n카톡으로 의견을 냈다.'))
# 4 카톡 2
pages[4] = (page_bg() + header(4, TOTAL)
    + panel(chat_screen([('l', '누워만 있으면\n비행기값 아깝잖아'), ('r', '돌아다니면\n쉬는 게 아니잖아'), ('l', '그럼 왜 가?'), ('r', '쉬러 가지!!')]), '#4E4A5A')
    + caption('바로 옆에 앉아 있는데\n말투가 점점 짧아졌다.'))
# 5
pages[5] = (page_bg() + header(5, TOTAL)
    + panel(speed(540, 640, '#E3E8F2', 44, 330) + char('bride', 540, 660, 1.45, 'blank') + sweat(720, 470)
            + T(540, 260, '(오빠 입력 중...)', 64, 'g', '#7A8090'), '#EEF1F7')
    + caption('그리고 오빠가\n한참 동안 뭔가를 쓰기 시작했다.'))
# 6 카톡 3
pages[6] = (page_bg() + header(6, TOTAL)
    + panel(chat_screen([('l', '그럼 반반 어때?\n앞 3일은 바다에서\n누워만 있고'), ('l', '뒤 3일은\n도시 하나만 천천히'), ('r', '...오빠 천재야?')]), '#4E4A5A')
    + caption('긴 장문이 올 줄 알았는데\n타협안이 왔다.'))
# 7
pages[7] = (page_bg() + header(7, TOTAL)
    + panel(hearts(12, (100, 160, 980, 600), '#FFD0D6', 77) + char('bride', 380, 700, 1.2, 'joy', (-40, 120)) + char('groom', 700, 690, 1.2, 'joy', (120, -40))
            + bubble(130, 170, 820, '근데 비행기 표는\n누가 알아볼 거야?', 58, (540, 420)), '#FFF5D8')
    + caption('우리는 다시 한 팀이 됐다.\n아직 할 일은 많지만.'))
# 8 정리
items = [('쉬는 여행 vs 보는 여행', '둘 중 어떤 여행을 원하는지'), ('일정 길이', '둘 다 쓸 수 있는 휴가 기간'), ('예산 상한', '항공·숙소·경비를 합쳐서 얼마까지'),
         ('꼭 하고 싶은 것 하나씩', '각자 양보 못 하는 한 가지'), ('계절과 이동 시간', '가는 때 날씨, 비행 시간 확인')]
p8 = page_bg() + header(8, TOTAL) + T(540, 230, '신혼여행지 정할 때 맞춰볼 5가지', 68, 'j')
cols = [ROSE, '#8FD3C1', '#F5B860', '#96B4EE', '#C59BE6']
for i, (a, b) in enumerate(items):
    y = 290 + i * 180
    p8 += f'<rect x="80" y="{y}" width="920" height="156" rx="50" fill="#fff" stroke="{INK}" stroke-width="5"/><circle cx="160" cy="{y+78}" r="46" fill="{cols[i]}"/>'
    p8 += T(160, y + 98, str(i + 1), 56, 'j', '#fff') + T(240, y + 66, a, 52, 'j', INK, 'start') + T(240, y + 126, b, 46, 'g', '#7A6262', 'start')
p8 += T(540, 1250, '먼저 이걸 맞추면, 장소는 금방 좁혀져요', 48, 'g', ROSE)
pages[8] = p8
# 9 마무리
pages[9] = (page_bg('#FFE4E4') + header(9, TOTAL) + hearts(18, (40, 120, 1040, 700), '#FFD0D6', 49)
    + char('bride', 400, 470, 1.15, 'joy', (6, -40)) + char('groom', 690, 460, 1.15, 'joy', (40, -8))
    + f'<rect x="110" y="820" width="860" height="420" rx="60" fill="#fff" stroke="{INK}" stroke-width="6"/>'
    + T(540, 930, '휴양파 vs 관광파', 76, 'j') + T(540, 1040, '여러분은 어느 쪽?', 76, 'j', ROSE) + T(540, 1150, '댓글로 남기고 예비 배우자 태그하기', 50, 'g', '#7A6262')
    + T(540, 1310, '@yebibubu.toon', 40, 'j', '#C49A9A'))

if __name__ == '__main__':
    render(pages, sys.argv[1] if len(sys.argv) > 1 else 'out/ep04')
