import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from extra import *

TOTAL = 9


def chat_screen(msgs, title='단짝 친구', size=42):
    """카톡 화면. msgs: [('r'|'l', 글)] r=나(신부), l=친구"""
    out = ''
    y = 300
    for side, t in msgs:
        lines = t.split('\n'); bh = len(lines) * size * 1.25 + 34; bw = 320
        bx = 712 - bw if side == 'r' else 368
        out += (f'<rect x="{bx}" y="{y}" width="{bw}" height="{bh}" rx="28" fill="{"#FFE36A" if side == "r" else "#fff"}" stroke="{INK}" stroke-width="3"/>'
                + T(bx + bw / 2, y + size + 8, lines, size, lh=1.25))
        y += bh + 30
    return (f'<rect x="330" y="170" width="420" height="860" rx="50" fill="#3A3542" stroke="{INK}" stroke-width="6"/>'
            f'<rect x="352" y="210" width="376" height="790" rx="26" fill="#DCE9F6"/>' + T(540, 262, title, 44, 'j') + out)


pages = {}
# 1 표지
pages[1] = (page_bg('#FFE4E4') + hearts(22, (40, 40, 1040, 1310), '#FFD0D6', 131)
    + f'<rect x="80" y="70" width="230" height="84" rx="42" fill="{ROSE}"/>' + T(195, 128, '카톡 썰', 50, 'j', '#fff')
    + T(80, 265, '축가 부탁했더니', 108, 'j', INK, 'start') + T(80, 395, '돌아온 답장', 108, 'j', ROSE, 'start')
    + panel(char('bride', 370, 800, 1.05, 'smug', (6, 120)) + phone(110, 840, 110, 190)
            + char('groom', 720, 790, 1.05, 'shock', (8, -8), flip=True) + sweat(850, 640) + sweat(600, 660, .8)
            + note(880, 560, 1.0) + note(960, 680, .8, '#96B4EE'), '#FFF7EE', 440, 1110)
    + f'<rect x="70" y="1150" width="940" height="130" rx="65" fill="#fff" stroke="{ROSE}" stroke-width="6"/>' + T(540, 1235, '+ 축가·사회 부탁 매너 5가지', 58, 'j', INK))
# 2
pages[2] = (page_bg() + header(2, TOTAL)
    + panel(char('bride', 540, 720, 1.35, 'happy') + phone(700, 560, 150, 250)
            + bubble(120, 180, 520, '단짝한테\n큰맘 먹고 연락', 58, (440, 420)), '#FFF0DC')
    + caption('날짜 잡고 제일 먼저\n떠오른 사람.'))
# 3 카톡 1
pages[3] = (page_bg() + header(3, TOTAL)
    + panel(chat_screen([('r', '나 결혼해!!'), ('l', '헐 축하해ㅠㅠ'), ('r', '그래서 말인데\n축가 해 줄래?'), ('l', '...')]), '#4E4A5A')
    + caption('...왜 말이 없지?'))
# 4
pages[4] = (page_bg() + header(4, TOTAL)
    + panel(char('bride', 540, 700, 1.4, 'nervous', (120, 120)) + sweat(730, 500) + sweat(350, 520, .8)
            + T(540, 250, '(읽음 표시 뜨고 한참째)', 56, 'g', '#7A8090'), '#EEF1F7')
    + caption('읽고 답이 없다.\n괜히 부탁했나?'))
# 5 카톡 2
pages[5] = (page_bg() + header(5, TOTAL)
    + panel(chat_screen([('l', '나 음치인 거\n알잖아'), ('l', '근데 너니까\n할게!'), ('l', '대신 신랑이랑\n듀엣으로'), ('r', '...오빠???')]), '#4E4A5A')
    + caption('조건이 붙었다.'))
# 6
pages[6] = (page_bg() + header(6, TOTAL)
    + panel(speed(540, 660, '#E3E9F8', 44, 330) + char('groom', 540, 690, 1.45, 'shock', (8, -8)) + sweat(740, 480) + sweat(340, 500, .8)
            + T(540, 250, '(노래방 탬버린 담당)', 58, 'g', '#7A8090'), '#F4F6FB')
    + caption('그렇게 오빠는\n축가에 끌려 들어갔다.'))
# 7 카톡 3
pages[7] = (page_bg() + header(7, TOTAL)
    + panel(chat_screen([('l', '오늘 연습한 거\n녹음 보냄'), ('r', '오빠 음이탈\n또 났네 ㅋㅋ'), ('l', '근데 진짜\n열심히 해'), ('r', '알아...\n나 벌써 울컥해')]), '#4E4A5A')
    + caption('매일 밤 둘의\n연습 녹음이 왔다.'))
# 8 본식
pages[8] = (page_bg() + header(8, TOTAL)
    + panel(hearts(10, (100, 170, 980, 420), '#FFC2CC', 138)
            + char('groom', 330, 720, 1.1, 'nervous', (8, 120)) + mic(505, 700, .75) + note(150, 320) + note(560, 260, .8, '#96B4EE')
            + char('bride', 760, 740, 1.1, 'joy', (6, -6), flip=True) + tears(760, 740, 1.1), '#FFF0F3')
    + caption('본식 날 음이탈 한 번에\n다 같이 웃고 울었다.'))
# 9 정리 + 마무리
items = [('일찍, 직접 부탁', '날짜 잡히면 말로 먼저'), ('곡은 같이 고르기', '부르기 편한 곡이 최고'), ('리허설 일정 공유', '도착 시간과 순서 미리'),
         ('장비는 식장에 확인', '마이크·반주 준비 여부'), ('고마움은 꼭 표현', '식사 대접이나 작은 선물')]
p9 = page_bg() + header(9, TOTAL) + T(540, 230, '축가·사회 부탁 매너 5가지', 72, 'j')
cols = [ROSE, '#8FD3C1', '#F5B860', '#96B4EE', '#C59BE6']
for i, (a, b) in enumerate(items):
    y = 290 + i * 172
    p9 += f'<rect x="80" y="{y}" width="920" height="150" rx="50" fill="#fff" stroke="{INK}" stroke-width="5"/><circle cx="160" cy="{y+75}" r="46" fill="{cols[i]}"/>'
    p9 += T(160, y + 95, str(i + 1), 56, 'j', '#fff') + T(240, y + 64, a, 52, 'j', INK, 'start') + T(240, y + 122, b, 44, 'g', '#7A6262', 'start')
p9 += T(540, 1185, '축가 해 준 친구, 태그해서 고맙다 하기', 46, 'g', ROSE)
p9 += T(540, 1250, '여러분 축가 썰도 댓글로 들려주세요', 42, 'g', '#7A6262')
p9 += T(540, 1315, '@yebibubu.toon', 40, 'j', '#C49A9A')
pages[9] = p9

if __name__ == '__main__':
    render(pages, sys.argv[1] if len(sys.argv) > 1 else 'out/ep13')
