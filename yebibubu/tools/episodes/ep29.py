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


def notes(pts, col='#E06C7A'):
    return ''.join(note(x, y, s, col) for x, y, s in pts)


pages = {}
# 1 표지
pages[1] = (page_bg('#FFE4E4') + hearts(22, (40, 40, 1040, 1310), '#FFD0D6', 291)
    + f'<rect x="80" y="70" width="230" height="84" rx="42" fill="{ROSE}"/>' + T(195, 128, '카톡 썰', 50, 'j', '#fff')
    + T(80, 265, '"축가는 내가 할게"', 100, 'j', INK, 'start') + T(80, 395, '오빠가 선언했다', 108, 'j', ROSE, 'start')
    + panel(char('groom', 600, 790, .9, 'smug', (8, -8)) + mic(692, 872, .7)
            + char('bride', 300, 800, .85, 'shock', (60, -6)) + sweat(400, 640)
            + notes([(860, 600, 1.0), (920, 700, .8), (180, 600, .8)]), '#FFF7EE', 440, 1110)
    + f'<rect x="70" y="1150" width="940" height="130" rx="65" fill="#fff" stroke="{ROSE}" stroke-width="6"/>' + T(540, 1235, '+ 축가 부탁 전 정리 5가지', 58, 'j', INK))
# 2 고민
pages[2] = (page_bg() + header(2, TOTAL)
    + panel(f'<rect x="70" y="760" width="940" height="400" fill="#C9C3E0"/>' + f'<circle cx="860" cy="260" r="60" fill="#FFF2B8" stroke="{INK}" stroke-width="5"/>'
            + char('bride', 450, 700, 1.15, 'nervous', (100, -6)) + phone(680, 560, 130, 220)
            + T(300, 280, '(축가… 누구한테?)', 56, 'g', '#7A8090'), '#E4E8F4')
    + caption('축가를 누구한테\n부탁할지 고민하던 밤.'))
# 3 카톡 1
pages[3] = (page_bg() + header(3, TOTAL)
    + panel(chat_screen([('r', '축가 누구한테\n부탁하지?'), ('l', '그거 내가 할게'), ('l', '진심임'), ('r', '오빠가??')]), '#4E4A5A')
    + caption('오빠가 갑자기\n축가를 하겠단다.'))
# 4 연습
pages[4] = (page_bg() + header(4, TOTAL)
    + panel(f'<rect x="70" y="820" width="940" height="400" fill="#D9CDBE"/>'
            + char('groom', 480, 690, 1.15, 'joy', (8, -8)) + mic(592, 812, .9) + sweat(330, 540)
            + notes([(780, 300, 1.1), (880, 420, .9), (220, 330, .9), (300, 220, .7)], '#9A8FB5')
            + T(800, 640, '삑사리', 56, 'j', '#C0392B'), '#EFE6DA')
    + caption('그날부터 오빠는\n매일 밤 연습했다.'))
# 5 카톡 2 음성 메시지
pages[5] = (page_bg() + header(5, TOTAL)
    + panel(chat_screen([('l', '(음성 메시지)\n▶ ▬▬▬▬'), ('l', '들어 봐 ㅎㅎ'), ('r', '......'), ('r', '음이 좀\n올라가네?')]), '#4E4A5A')
    + caption('연습한 노래를\n녹음해서 보내왔다.'))
# 6 듣는 신부
pages[6] = (page_bg() + header(6, TOTAL)
    + panel(f'<rect x="70" y="800" width="940" height="400" fill="#F2D9C4"/>'
            + char('bride', 480, 680, 1.15, 'shock', (100, -6)) + phone(700, 520, 130, 220) + sweat(330, 520) + sweat(620, 480, .8)
            + f'<g transform="rotate(25 820 300)">{note(820, 300, 1.0, "#9A8FB5")}</g>'
            + f'<g transform="rotate(-35 220 330)">{note(220, 330, 1.0, "#9A8FB5")}</g>'
            + f'<g transform="rotate(60 900 440)">{note(900, 440, .8, "#9A8FB5")}</g>', '#FFF1E2')
    + caption('솔직히…\n음이 많이 흔들렸다.'))
# 7 카톡 3
pages[7] = (page_bg() + header(7, TOTAL)
    + panel(chat_screen([('l', '역시 별로지..'), ('l', '그냥 친구한테\n부탁할까'), ('r', '아니!'), ('r', '오빠 목소리라서\n좋은 거야')]), '#4E4A5A')
    + caption('잘 부르는 노래보다\n오빠 노래가 좋았다.'))
# 8 카톡 4
pages[8] = (page_bg() + header(8, TOTAL)
    + panel(chat_screen([('r', '대신 같이\n연습하자'), ('l', '둘이 듀엣?!'), ('r', '틀리면 같이\n틀리기 ㅋㅋ'), ('l', '최고다 진짜')]), '#4E4A5A')
    + caption('그래서 축가는\n둘이 같이 하기로 했다.'))
# 9 정리
items = [('일찍 부탁하기', '준비할 시간 넉넉히 주기'), ('곡은 같이 정하기', '둘의 이야기 담긴 노래로'), ('리허설 시간 알리기', '식장 동선도 미리 공유'),
         ('반주·마이크 확인', '식장에 미리 물어보기'), ('고마움 꼭 전하기', '식사나 작은 선물로 마음 표현')]
p9 = page_bg() + header(9, TOTAL) + T(540, 230, '축가 부탁 전 정리 5가지', 64, 'j')
cols = [ROSE, '#8FD3C1', '#F5B860', '#96B4EE', '#C59BE6']
for i, (a, b) in enumerate(items):
    y = 290 + i * 180
    p9 += f'<rect x="80" y="{y}" width="920" height="156" rx="50" fill="#fff" stroke="{INK}" stroke-width="5"/><circle cx="160" cy="{y+78}" r="46" fill="{cols[i]}"/>'
    p9 += T(160, y + 98, str(i + 1), 56, 'j', '#fff') + T(240, y + 66, a, 50, 'j', INK, 'start') + T(240, y + 126, b, 44, 'g', '#7A6262', 'start')
p9 += T(540, 1250, '부탁받은 사람도 편하게!', 46, 'g', ROSE)
pages[9] = p9
# 10 마무리
pages[10] = (page_bg('#FFE4E4') + header(10, TOTAL) + hearts(18, (40, 120, 1040, 700), '#FFD0D6', 299)
    + char('bride', 400, 470, 1.15, 'joy', (6, 120)) + char('groom', 690, 460, 1.15, 'joy', (120, -8))
    + notes([(160, 260, 1.0), (930, 280, 1.0), (540, 200, .8)])
    + f'<rect x="110" y="820" width="860" height="420" rx="60" fill="#fff" stroke="{INK}" stroke-width="6"/>'
    + T(540, 930, '우리 축가는 누가?', 76, 'j') + T(540, 1040, '댓글로 들려주세요', 76, 'j', ROSE) + T(540, 1150, '축가 고민 중인 커플에게 공유!', 48, 'g', '#7A6262')
    + T(540, 1310, '@yebibubu.toon', 40, 'j', '#C49A9A'))

if __name__ == '__main__':
    render(pages, sys.argv[1] if len(sys.argv) > 1 else 'out/ep29')
