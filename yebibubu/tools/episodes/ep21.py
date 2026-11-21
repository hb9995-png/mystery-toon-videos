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


def sun(x, y, r=70):
    rays = ''.join(f'<path d="M{x} {y} m 0 {-r - 20} v -40" transform="rotate({a} {x} {y})"/>' for a in range(0, 360, 45))
    return f'<g stroke="{INK}" stroke-width="5">{rays}<circle cx="{x}" cy="{y}" r="{r}" fill="#FFD84D"/></g>'


def sea(y0=760):
    return (f'<rect x="70" y="{y0}" width="940" height="400" fill="#8FD3E8"/>'
            f'<path d="M70 {y0} q 60 -30 120 0 t 120 0 t 120 0 t 120 0 t 120 0 t 120 0 t 120 0 t 120 0" fill="none" stroke="{INK}" stroke-width="5"/>'
            f'<rect x="70" y="{y0 + 170}" width="940" height="300" fill="#F6E2B3"/><path d="M70 {y0 + 170} H 1010" stroke="{INK}" stroke-width="5"/>')


def think(x, y, w, h, inner, col='#fff'):
    return (f'<g stroke="{INK}" stroke-width="5"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="60" fill="{col}"/>'
            f'<circle cx="{x + w / 2}" cy="{y + h + 40}" r="20" fill="{col}"/><circle cx="{x + w / 2 + 10}" cy="{y + h + 90}" r="12" fill="{col}"/></g>' + inner)


pages = {}
# 1 표지
pages[1] = (page_bg('#FFE4E4') + hearts(22, (40, 40, 1040, 1310), '#FFD0D6', 211)
    + f'<rect x="80" y="70" width="230" height="84" rx="42" fill="{ROSE}"/>' + T(195, 128, '카톡 썰', 50, 'j', '#fff')
    + T(80, 265, '신혼여행 정하다', 108, 'j', INK, 'start') + T(80, 395, '받은 일정표', 108, 'j', ROSE, 'start')
    + panel(paper(100, 520, 330, 400, '일정표', [('06:00', '기상', None), ('07:00', '시장', None), ('09:00', '등산', None), ('11:00', '박물관', '#C0392B')], 40, -6)
            + char('bride', 610, 810, .95, 'shock', (60, 120)) + char('groom', 860, 810, .8, 'smug', (8, -8), flip=True) + sweat(760, 620), '#FFF7EE', 440, 1110)
    + f'<rect x="70" y="1150" width="940" height="130" rx="65" fill="#fff" stroke="{ROSE}" stroke-width="6"/>' + T(540, 1235, '+ 신혼여행 고를 때 맞춰 볼 5가지', 54, 'j', INK))
# 2
pages[2] = (page_bg() + header(2, TOTAL)
    + panel(char('bride', 540, 720, 1.2, 'happy') + phone(700, 560, 150, 250)
            + T(540, 250, '(신혼여행 어디 가지~)', 54, 'g', '#7A8090'), '#E8ECF6')
    + caption('신혼여행을 정하던 밤.\n오빠가 계획을 짰다고 했다.'))
# 3 카톡 1
pages[3] = (page_bg() + header(3, TOTAL)
    + panel(chat_screen([('l', '신혼여행 계획\n다 짰어!'), ('l', '(일정표.파일)'), ('l', '완벽해 ㅎㅎ'), ('r', '오 기대돼!\n열어 볼게')]), '#4E4A5A')
    + caption('오빠, 엄청 뿌듯해 보였다.'))
# 4 일정표
pages[4] = (page_bg() + header(4, TOTAL)
    + panel(paper(150, 200, 440, 620, '첫째 날', [('06:00', '기상', '#C0392B'), ('07:00', '시장 구경', None), ('09:00', '등산', None), ('12:00', '맛집 줄서기', None), ('14:00', '박물관', None), ('17:00', '야경 투어', None)], 42, -4)
            + char('bride', 800, 770, .95, 'shock', (60, 120), flip=True) + sweat(900, 640) + sweat(680, 660, .8), '#FFF5D8')
    + caption('아침 6시 기상부터\n하루가 꽉 차 있었다.'))
# 5 카톡 2
pages[5] = (page_bg() + header(5, TOTAL)
    + panel(chat_screen([('r', '이거 여행이야?\n훈련이야? ㅋㅋ'), ('r', '나는 바다 보면서\n누워 있고 싶어'), ('l', '...누워만 있어?'), ('l', '(시무룩)')]), '#4E4A5A')
    + caption('나는 쉬고 싶었고\n오빠는 다 보고 싶었다.'))
# 6 상상 비교
pages[6] = (page_bg() + header(6, TOTAL)
    + panel(think(100, 170, 400, 300, sun(220, 280, 50) + f'<path d="M110 400 q 50 -24 100 0 t 100 0 t 100 0 t 90 0" fill="none" stroke="{INK}" stroke-width="5"/>' + T(380, 330, '쉬기', 56, 'j'), '#E4F4FA')
            + think(580, 170, 400, 300, paper(620, 200, 150, 230, '', [], 30, 6) + ''.join(f'<path d="M650 {250+k*40} h 90" stroke="#C9B6B6" stroke-width="6"/>' for k in range(4)) + T(870, 340, '다니기', 56, 'j'), '#FFF1D6')
            + char('bride', 300, 840, 1.0, 'happy', (6, -6)) + char('groom', 780, 840, 1.0, 'joy', (8, -8), flip=True), '#F4ECFA')
    + caption('같은 여행인데\n머릿속 그림이 달랐다.'))
# 7 카톡 3
pages[7] = (page_bg() + header(7, TOTAL)
    + panel(chat_screen([('l', '그럼 오전엔\n내 일정 가고'), ('l', '오후엔 바다?'), ('r', '콜! 대신\n6시 기상은 빼'), ('l', '...7시? ㅎㅎ')]), '#4E4A5A')
    + caption('결국 반반 여행으로\n합의했다.'))
# 8 정리
items = [('쉬는 여행 vs 다니는 여행', '둘이 원하는 쪽 먼저 말하기'), ('꼭 하고 싶은 것 하나씩', '서로 하나는 양보 없이'), ('이동 시간 감당 되나', '식 끝나고 피곤한 걸 생각하기'),
         ('예산 범위 미리', '숙소·식비 어디에 쓸지'), ('여권·서류 확인', '기한과 필요한 서류 미리')]
p8 = page_bg() + header(8, TOTAL) + T(540, 230, '신혼여행 고를 때 맞춰 볼 5가지', 64, 'j')
cols = [ROSE, '#8FD3C1', '#F5B860', '#96B4EE', '#C59BE6']
for i, (a, b) in enumerate(items):
    y = 290 + i * 180
    p8 += f'<rect x="80" y="{y}" width="920" height="156" rx="50" fill="#fff" stroke="{INK}" stroke-width="5"/><circle cx="160" cy="{y+78}" r="46" fill="{cols[i]}"/>'
    p8 += T(160, y + 98, str(i + 1), 56, 'j', '#fff') + T(240, y + 66, a, 50, 'j', INK, 'start') + T(240, y + 126, b, 44, 'g', '#7A6262', 'start')
p8 += T(540, 1250, '어디로 가든 둘 다 즐거운 게 먼저', 46, 'g', ROSE)
pages[8] = p8
# 9 마무리
pages[9] = (page_bg('#FFE4E4') + header(9, TOTAL) + hearts(18, (40, 120, 1040, 700), '#FFD0D6', 219)
    + char('bride', 400, 470, 1.15, 'joy', (6, -40)) + char('groom', 690, 460, 1.15, 'happy', (40, -8))
    + f'<rect x="110" y="820" width="860" height="420" rx="60" fill="#fff" stroke="{INK}" stroke-width="6"/>'
    + T(540, 930, '쉬는 여행 vs', 76, 'j') + T(540, 1040, '다니는 여행?', 76, 'j', ROSE) + T(540, 1150, '댓글로 고르고 예비 배우자 태그하기', 48, 'g', '#7A6262')
    + T(540, 1310, '@yebibubu.toon', 40, 'j', '#C49A9A'))

if __name__ == '__main__':
    render(pages, sys.argv[1] if len(sys.argv) > 1 else 'out/ep21')
