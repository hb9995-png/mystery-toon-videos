import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from extra import *

TOTAL = 9


def cafe(y0=130, y1=1060):
    """카페: 벽 + 창문 + 펜던트 조명."""
    s = f'<rect x="70" y="{y0}" width="940" height="{y1 - y0}" fill="#FCEBD8"/>'
    s += f'<rect x="640" y="{y0 + 60}" width="300" height="240" rx="16" fill="#CFE8F5" stroke="{INK}" stroke-width="5"/><path d="M790 {y0 + 60} V {y0 + 300} M 640 {y0 + 180} H 940" stroke="{INK}" stroke-width="4"/>'
    s += (f'<g stroke="{INK}" stroke-width="5"><path d="M300 {y0} V {y0 + 80}"/>'
          f'<path d="M240 {y0 + 140} Q 300 {y0 + 50} 360 {y0 + 140} Z" fill="#F5B860"/></g>')
    return s


def room(y0=130, y1=1060, wall='#EAF0FB'):
    return (f'<rect x="70" y="{y0}" width="940" height="{y1 - y0}" fill="{wall}"/>'
            f'<rect x="70" y="{y1 - 160}" width="940" height="160" fill="#C9C3D9"/>')


def hall(y0=130, y1=1060):
    """예식장: 분홍 벽 + 샹들리에 + 꽃길."""
    s = f'<rect x="70" y="{y0}" width="940" height="{y1 - y0}" fill="#FFF0F3"/>'
    s += chandelier(780, y0 + 230, .8)
    s += f'<path d="M420 {y1} L 500 {y0 + 520} H 580 L 660 {y1} Z" fill="#FFD6DE"/>'
    return s


def stand(x, y):
    """사회자 단상."""
    return (f'<g stroke="{INK}" stroke-width="5" stroke-linejoin="round"><path d="M{x - 110} {y} H {x + 110} L {x + 80} {y + 260} H {x - 80} Z" fill="#E9C9A4"/>'
            f'<rect x="{x - 125}" y="{y - 24}" width="250" height="30" rx="10" fill="#C9A07A"/></g>')


pages = {}
# 1 표지
pages[1] = (page_bg('#FFE4E4') + hearts(22, (40, 40, 1040, 1310), '#FFD0D6', 311)
    + f'<rect x="80" y="70" width="230" height="84" rx="42" fill="{ROSE}"/>' + T(195, 128, '썰툰', 50, 'j', '#fff')
    + T(80, 265, '사회 부탁했더니', 104, 'j', INK, 'start') + T(80, 390, '친구가 변했다', 104, 'j', ROSE, 'start')
    + panel(room(440, 1110) + receipt(760, 560, 230, 480)
            + friend('f1', 420, 720, .95, 'smug', (8, 100)) + mic(575, 700, .85), '#EAF0FB', 440, 1110)
    + f'<rect x="70" y="1150" width="940" height="130" rx="65" fill="#fff" stroke="{ROSE}" stroke-width="6"/>' + T(540, 1235, '+ 마지막에 사회 부탁 팁 5가지', 56, 'j', INK))
# 2 부탁
pages[2] = (page_bg() + header(2, TOTAL)
    + panel(cafe() + friend('f1', 230, 660, .78, 'blank', (8, -8))
            + char('bride', 600, 660, .78, 'happy', (8, 60), flip=True) + char('groom', 840, 654, .8, 'nervous', (8, -8), flip=True)
            + cafe_table(900) + bubble(330, 160, 520, '우리 결혼식\n사회 봐 줄래?', 52, (590, 470)), '#FCEBD8')
    + caption('식순표를 보다가\n사회자 칸이 비어 있었다.'))
# 3 감동
pages[3] = (page_bg() + header(3, TOTAL)
    + panel(speed(540, 620, '#FFE3C4', 40, 280) + hearts(10, (120, 160, 960, 330), '#FFB8C4', 313)
            + friend('f1', 540, 660, 1.1, 'joy', (110, 110)) + tears(540, 660, 1.1)
            + bubble(130, 170, 420, '내가?\n영광이야!!', 56, (430, 480)), '#FFF5E6')
    + caption('친구는 그 자리에서 울었다.\n여기까진 좋았다.'))
# 4 수정본
p4_screen = (f'<rect x="392" y="330" width="296" height="80" rx="20" fill="#fff"/>' + T(540, 383, '대본 1차 보낼게', 34, 'g')
             + f'<rect x="392" y="430" width="296" height="80" rx="20" fill="#fff"/>' + T(540, 483, '2차 수정본!', 34, 'g')
             + f'<rect x="392" y="530" width="296" height="80" rx="20" fill="#fff"/>' + T(540, 583, '3차… 이게 진짜', 34, 'g')
             + f'<rect x="392" y="630" width="296" height="80" rx="20" fill="#FFE1E6"/>' + T(540, 683, '아니 4차가 진짜', 34, 'g', ROSE))
pages[4] = (page_bg() + header(4, TOTAL)
    + panel(room(wall='#2F3550') + f'<circle cx="880" cy="230" r="60" fill="#FFF2B8"/>'
            + phone(370, 260, 340, 560, inner=p4_screen)
            + char('bride', 200, 700, .72, 'blank', (8, -8)) + char('groom', 880, 700, .72, 'shock', (8, -8), flip=True), '#2F3550')
    + caption('그날부터 매일 밤\n대본 수정본이 왔다.'))
# 5 긴 대본
pages[5] = (page_bg() + header(5, TOTAL)
    + panel(room() + receipt(780, 150, 260, 900)
            + friend('f1', 360, 680, .95, 'smug', (8, 100)) + mic(515, 660, .85)
            + bubble(100, 170, 560, '두 사람의 첫 만남부터\n말씀드리면…', 46, (360, 450)), '#EAF0FB')
    + caption('대본에는 우리 연애가\n처음부터 다 들어 있었다.'))
# 6 제발
pages[6] = (page_bg() + header(6, TOTAL)
    + panel(cafe() + char('bride', 330, 680, .95, 'shock', (120, 120)) + char('groom', 720, 680, .95, 'shock', (120, 120), flip=True)
            + sweat(440, 520) + sweat(830, 520)
            + bubble(250, 165, 580, '첫 데이트 이야기는\n제발 빼 줘!!', 52, (520, 450)), '#FCEBD8')
    + caption('첫 데이트 실수담만은\n빼 달라고 빌었다.'))
# 7 본식
pages[7] = (page_bg() + header(7, TOTAL)
    + panel(hall() + hearts(12, (110, 150, 980, 360), '#FFB8C4', 317)
            + char('bride', 470, 720, .7, 'joy', (8, -8)) + char('groom', 640, 714, .72, 'joy', (8, -8))
            + friend('f1', 860, 700, .66, 'happy', (8, 100)) + mic(965, 680, .55) + stand(860, 830)
            + bubble(100, 170, 470, '두 사람 앞날에\n큰 박수 부탁드립니다!', 44, (800, 520)), '#FFF0F3')
    + caption('본식 날 친구는\n떨지 않고 해냈다.'))
# 8 정리
items = [('일찍 부탁하기', '친구가 일정을 비워 둘 수 있게'), ('식순표 같이 보기', '순서와 시간을 미리 나누기'),
         ('이름 발음 확인', '양가 부모님 성함까지 꼭'), ('대본 같이 읽기', '빼고 싶은 이야기는 미리 말하기'),
         ('고마움 전하기', '작은 선물이나 손편지로')]
p8 = page_bg() + header(8, TOTAL) + T(540, 230, '사회 부탁 팁 5가지', 70, 'j')
cols = [ROSE, '#8FD3C1', '#F5B860', '#96B4EE', '#C59BE6']
for i, (a, b) in enumerate(items):
    y = 290 + i * 180
    p8 += f'<rect x="80" y="{y}" width="920" height="156" rx="50" fill="#fff" stroke="{INK}" stroke-width="5"/><circle cx="160" cy="{y+78}" r="46" fill="{cols[i]}"/>'
    p8 += T(160, y + 98, str(i + 1), 56, 'j', '#fff') + T(240, y + 66, a, 52, 'j', INK, 'start') + T(240, y + 126, b, 44, 'g', '#7A6262', 'start')
p8 += T(540, 1250, '대본은 짧게, 마음은 길게!', 46, 'g', ROSE)
pages[8] = p8
# 9 마무리
pages[9] = (page_bg('#FFE4E4') + header(9, TOTAL) + hearts(18, (40, 120, 1040, 700), '#FFD0D6', 319)
    + char('bride', 400, 470, 1.15, 'joy', (6, -40)) + char('groom', 690, 460, 1.15, 'happy', (40, -8))
    + f'<rect x="110" y="820" width="860" height="420" rx="60" fill="#fff" stroke="{INK}" stroke-width="6"/>'
    + T(540, 930, '저장해 두고', 76, 'j') + T(540, 1040, '사회 부탁할 친구에게 공유', 72, 'j', ROSE) + T(540, 1150, '사회 봐 준 친구, 기억나는 멘트는?', 46, 'g', '#7A6262')
    + T(540, 1310, '@yebibubu.toon', 40, 'j', '#C49A9A'))

if __name__ == '__main__':
    render(pages, sys.argv[1] if len(sys.argv) > 1 else 'out/ep31')
