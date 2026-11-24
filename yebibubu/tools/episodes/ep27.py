import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from extra import *

TOTAL = 9


def room(y0=130, y1=1060, wall='#FFF1E4'):
    return (f'<rect x="70" y="{y0}" width="940" height="{y1 - y0}" fill="{wall}"/>'
            f'<rect x="70" y="{y1 - 160}" width="940" height="160" fill="#D9C3AE"/>')


def restaurant(y0=130, y1=1060):
    """식당: 벽 + 펜던트 조명 둘."""
    s = f'<rect x="70" y="{y0}" width="940" height="{y1 - y0}" fill="#FCEBD8"/>'
    for lx in (300, 780):
        s += (f'<g stroke="{INK}" stroke-width="5"><path d="M{lx} {y0} V {y0 + 90}"/>'
              f'<path d="M{lx - 60} {y0 + 150} Q {lx} {y0 + 60} {lx + 60} {y0 + 150} Z" fill="#F5B860"/></g>')
    return s


def four(m1='happy', m2='happy', mb='happy', mg='happy', ab=(8, -8), ag=(8, -8), a1=(8, -8), a2=(8, -8), y=640):
    """탁자 앞 네 명: 왼쪽 친구 둘, 오른쪽 신부·신랑(왼쪽을 봄)."""
    return (friend('f1', 190, y, .68, m1, a1) + friend('f2', 425, y, .68, m2, a2)
            + char('bride', 665, y, .68, mb, ab, flip=True) + char('groom', 892, y - 6, .7, mg, ag, flip=True)
            + cafe_table(880))


pages = {}
# 1 표지
pages[1] = (page_bg('#FFE4E4') + hearts(22, (40, 40, 1040, 1310), '#FFD0D6', 271)
    + f'<rect x="80" y="70" width="230" height="84" rx="42" fill="{ROSE}"/>' + T(195, 128, '썰툰', 50, 'j', '#fff')
    + T(80, 265, '오빠가 내 친구들', 104, 'j', INK, 'start') + T(80, 390, '처음 만난 날', 104, 'j', ROSE, 'start')
    + panel(restaurant(440, 1110) + friend('f1', 220, 720, .8, 'smug', (8, -8)) + friend('f2', 430, 720, .8, 'smug', (8, -8))
            + char('groom', 790, 730, .95, 'nervous', (8, -8), flip=True) + sweat(900, 590) + cafe_table(950, 90, 990), '#FCEBD8', 440, 1110)
    + f'<rect x="70" y="1150" width="940" height="130" rx="65" fill="#fff" stroke="{ROSE}" stroke-width="6"/>' + T(540, 1235, '+ 마지막에 청첩장 모임 팁 5가지', 54, 'j', INK))
# 2 연습
pages[2] = (page_bg() + header(2, TOTAL)
    + panel(room() + mirror(700, 380, 240, 480) + char('groom', 400, 660, 1.0, 'nervous', (8, 70))
            + memo_card(470, 640, 240, 150, ('1. 인사', '2. 이름', '3. 웃기'), 8)
            + bubble(110, 170, 520, '안녕하세요!\n저는 신랑…', 52, (360, 470)), '#FFF1E4')
    + caption('청첩장 모임 날 아침.\n오빠가 자기소개를 외웠다.'))
# 3 정적
pages[3] = (page_bg() + header(3, TOTAL)
    + panel(restaurant() + four('blank', 'blank', 'happy', 'nervous', y=670) + sweat(965, 540)
            + invite_card(120, 790, 150, -6) + invite_card(350, 795, 150, 5)
            + T(540, 330, '. . .', 90, 'j', '#9A8F8F'), '#FCEBD8')
    + caption('청첩장을 건네자\n친구들 눈빛이 면접관이 됐다.'))
# 4 꼬임
pages[4] = (page_bg() + header(4, TOTAL)
    + panel(restaurant() + friend('f1', 200, 710, .75, 'shock', (8, -8)) + friend('f2', 430, 710, .75, 'shock', (8, -8))
            + char('groom', 820, 690, .95, 'nervous', (8, 80), flip=True) + sweat(950, 540) + sweat(700, 560)
            + memo_card(560, 800, 200, 130, ('1. 인사', '2. 이…'), -10)
            + bubble(460, 160, 520, '저는 신부의\n신랑의… 신랑입니다!', 46, (760, 470)) + cafe_table(900), '#FCEBD8')
    + caption('외워 온 자기소개는\n첫 줄에서 꼬였다.'))
# 5 질문
pages[5] = (page_bg() + header(5, TOTAL)
    + panel(speed(540, 600, '#FFE3C4', 40, 280) + friend('f2', 360, 640, 1.05, 'smug', (8, -60))
            + bubble(500, 190, 460, '그래서\n얘 어디가 좋아요?', 50, (520, 470)), '#FFF5E6')
    + caption('그때 날아온 질문.\n오빠 쪽지에는 없는 문제였다.'))
# 6 대답
pages[6] = (page_bg() + header(6, TOTAL)
    + panel(restaurant() + hearts(8, (520, 160, 980, 330), '#FFD0D6', 276)
            + char('groom', 720, 690, 1.05, 'happy', (8, -8), flip=True)
            + char('bride', 300, 720, .85, 'nervous', (8, -8)) + sweat(410, 570)
            + bubble(100, 160, 560, '힘든 날이면 제가 말하기\n전에 먼저 알아채요.\n그게 제일 좋아요.', 44, (640, 470))
            + cafe_table(920), '#FCEBD8')
    + caption('쪽지는 접혀 있었다.\n대답은 바로 나왔다.'))
# 7 합격
pages[7] = (page_bg() + header(7, TOTAL)
    + panel(restaurant() + hearts(14, (90, 150, 990, 420), '#FFB8C4', 277)
            + four('joy', 'joy', 'nervous', 'happy', a1=(8, -70), a2=(70, -8), y=670)
            + tears(190, 670, .68) + tears(425, 670, .68)
            + f'<ellipse cx="618" cy="692" rx="20" ry="11" fill="#FF8FA0"/><ellipse cx="712" cy="692" rx="20" ry="11" fill="#FF8FA0"/>'
            + bubble(130, 170, 360, '합격!!\n잘 부탁해요!', 50, (300, 460)), '#FCEBD8')
    + caption('면접은 그 자리에서 끝났다.\n내 얼굴만 빨개졌다.'))
# 8 정리
items = [('날짜는 미리 묻기', '친구들 일정 먼저 확인하기'), ('편한 자리 고르기', '이야기 나누기 좋은 곳으로'),
         ('청첩장은 손으로', '직접 건네며 고마움 전하기'), ('모바일도 함께', '오시는 길 링크 같이 보내기'),
         ('식 끝나고 인사', '와 준 친구에게 꼭 연락하기')]
p8 = page_bg() + header(8, TOTAL) + T(540, 230, '청첩장 모임 팁 5가지', 70, 'j')
cols = [ROSE, '#8FD3C1', '#F5B860', '#96B4EE', '#C59BE6']
for i, (a, b) in enumerate(items):
    y = 290 + i * 180
    p8 += f'<rect x="80" y="{y}" width="920" height="156" rx="50" fill="#fff" stroke="{INK}" stroke-width="5"/><circle cx="160" cy="{y+78}" r="46" fill="{cols[i]}"/>'
    p8 += T(160, y + 98, str(i + 1), 56, 'j', '#fff') + T(240, y + 66, a, 52, 'j', INK, 'start') + T(240, y + 126, b, 44, 'g', '#7A6262', 'start')
p8 += T(540, 1250, '자기소개는 외우기보다 진심으로!', 46, 'g', ROSE)
pages[8] = p8
# 9 마무리
pages[9] = (page_bg('#FFE4E4') + header(9, TOTAL) + hearts(18, (40, 120, 1040, 700), '#FFD0D6', 279)
    + char('bride', 400, 470, 1.15, 'joy', (6, -40)) + char('groom', 690, 460, 1.15, 'happy', (40, -8))
    + f'<rect x="110" y="820" width="860" height="420" rx="60" fill="#fff" stroke="{INK}" stroke-width="6"/>'
    + T(540, 930, '저장해 두고', 76, 'j') + T(540, 1040, '예비 배우자에게 공유하기', 76, 'j', ROSE) + T(540, 1150, '친구들에게 처음 소개한 날 어땠어요?', 46, 'g', '#7A6262')
    + T(540, 1310, '@yebibubu.toon', 40, 'j', '#C49A9A'))

if __name__ == '__main__':
    render(pages, sys.argv[1] if len(sys.argv) > 1 else 'out/ep27')
