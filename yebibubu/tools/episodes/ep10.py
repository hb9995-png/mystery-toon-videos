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


def ring(x, y, s=1.0):
    return (f'<g transform="translate({x} {y}) scale({s})" stroke="{INK}" stroke-width="5">'
            f'<rect x="-90" y="-10" width="180" height="120" rx="20" fill="#C0445A"/><path d="M-90 30 H 90" />'
            f'<circle cx="0" cy="-40" r="44" fill="none" stroke="#F2C66B" stroke-width="14"/><circle cx="0" cy="-40" r="44" fill="none" stroke-width="3"/>'
            f'<path d="M-18 -96 L 0 -118 L 18 -96 L 0 -78 Z" fill="#DFF4FF"/></g>')


pages = {}
# 1 표지
pages[1] = (page_bg('#FFE4E4') + hearts(22, (40, 40, 1040, 1310), '#FFD0D6', 101)
    + f'<rect x="80" y="70" width="230" height="84" rx="42" fill="{ROSE}"/>' + T(195, 128, '카톡 썰', 50, 'j', '#fff')
    + T(80, 265, '프로포즈 계획을', 108, 'j', INK, 'start') + T(80, 395, '나한테 보낸 오빠', 108, 'j', ROSE, 'start')
    + panel(char('bride', 360, 800, 1.05, 'smug', (6, 120)) + char('groom', 720, 790, 1.05, 'shock', (8, -8), flip=True)
            + phone(130, 820, 120, 200) + ring(910, 1000, .7) + sweat(850, 640) + sweat(600, 660, .8), '#FFF7EE', 440, 1110)
    + f'<rect x="70" y="1150" width="940" height="130" rx="65" fill="#fff" stroke="{ROSE}" stroke-width="6"/>' + T(540, 1235, '+ 프로포즈 준비 체크 5가지', 58, 'j', INK))
# 2
pages[2] = (page_bg() + header(2, TOTAL)
    + panel(char('bride', 540, 720, 1.35, 'happy') + phone(700, 560, 150, 250)
            + bubble(120, 180, 520, '오빠한테서\n카톡이 왔다', 58, (440, 420)), '#FFF0DC')
    + caption('평범한 화요일 밤.\n오빠한테 카톡이 왔다.'))
# 3 카톡 1
pages[3] = (page_bg() + header(3, TOTAL)
    + panel(chat_screen([('l', '반지는 금요일에\n찾으러 가고'), ('l', '토요일 저녁에\n한강 공원'), ('l', '노래 나오면\n무릎 꿇기'), ('r', '...?')]), '#4E4A5A')
    + caption('...이게 뭐지?'))
# 4
pages[4] = (page_bg() + header(4, TOTAL)
    + panel(speed(540, 660, '#FFE9B8', 44, 330) + char('bride', 540, 680, 1.45, 'shock') + sweat(730, 480)
            + T(540, 250, '(오빠 입력 중...)', 62, 'g', '#7A8090'), '#FFF5D8')
    + caption('친구한테 보낼 걸\n나한테 보낸 거다.'))
# 5 카톡 2
pages[5] = (page_bg() + header(5, TOTAL)
    + panel(chat_screen([('l', '아 잠깐'), ('l', '방금 거\n못 본 걸로 해 줘'), ('l', '제발'), ('r', '이미 다 봤는데\nㅋㅋㅋㅋㅋ')]), '#4E4A5A')
    + caption('1초 만에 정신 차린 오빠.'))
# 6
pages[6] = (page_bg() + header(6, TOTAL)
    + panel(char('groom', 540, 720, 1.4, 'nervous', (120, 120)) + sweat(720, 520) + sweat(360, 540, .8) + sweat(780, 640, .7)
            + T(540, 250, '(현관 앞에서 3분째 서성이는 중)', 52, 'g', '#7A8090'), '#EEF1F7')
    + caption('그날 밤 오빠는\n잠을 못 잤다고 한다.'))
# 7 카톡 3
pages[7] = (page_bg() + header(7, TOTAL)
    + panel(chat_screen([('r', '토요일 저녁\n한강 좋아 :)'), ('r', '나 모르는 척\n제대로 할게'), ('l', '...진짜?'), ('r', '대신 노래는\n내가 고를래 ㅋㅋ')]), '#4E4A5A')
    + caption('그래서 내가 먼저 답장했다.'))
# 8 정리
items = [('좋아하는 분위기', '둘만 조용히 vs 깜짝 이벤트'), ('날씨 플랜 B', '비 오면 갈 실내 장소 하나'), ('사진 남길 방법', '부탁할 친구나 삼각대 준비'),
         ('반지 치수', '평소 끼는 반지로 몰래 확인'), ('보내기 전 확인', '계획 카톡은 받는 사람 두 번 보기')]
p8 = page_bg() + header(8, TOTAL) + T(540, 230, '프로포즈 준비 체크 5가지', 72, 'j')
cols = [ROSE, '#8FD3C1', '#F5B860', '#96B4EE', '#C59BE6']
for i, (a, b) in enumerate(items):
    y = 290 + i * 180
    p8 += f'<rect x="80" y="{y}" width="920" height="156" rx="50" fill="#fff" stroke="{INK}" stroke-width="5"/><circle cx="160" cy="{y+78}" r="46" fill="{cols[i]}"/>'
    p8 += T(160, y + 98, str(i + 1), 56, 'j', '#fff') + T(240, y + 66, a, 52, 'j', INK, 'start') + T(240, y + 126, b, 44, 'g', '#7A6262', 'start')
p8 += T(540, 1250, '들켜도 괜찮아요, 진심이면 감동은 그대로', 46, 'g', ROSE)
pages[8] = p8
# 9 마무리
pages[9] = (page_bg('#FFE4E4') + header(9, TOTAL) + hearts(18, (40, 120, 1040, 700), '#FFD0D6', 109)
    + char('bride', 400, 470, 1.15, 'joy', (6, -40)) + char('groom', 690, 460, 1.15, 'joy', (40, -8)) + tears(690, 460, 1.0)
    + f'<rect x="110" y="820" width="860" height="420" rx="60" fill="#fff" stroke="{INK}" stroke-width="6"/>'
    + T(540, 930, '프로포즈 들킨 적', 76, 'j') + T(540, 1040, '있다 vs 없다?', 76, 'j', ROSE) + T(540, 1150, '댓글로 남기고 그 사람 태그하기', 50, 'g', '#7A6262')
    + T(540, 1310, '@yebibubu.toon', 40, 'j', '#C49A9A'))

if __name__ == '__main__':
    render(pages, sys.argv[1] if len(sys.argv) > 1 else 'out/ep10')
