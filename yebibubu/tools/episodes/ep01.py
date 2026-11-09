import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from kit import *

pages = {}
# 1 표지
pages[1] = (f'<rect width="1080" height="1350" fill="#FFE4E4"/>' + hearts(22, (40, 40, 1040, 1310), '#FFD0D6', 3)
    + f'<rect x="80" y="70" width="230" height="84" rx="42" fill="{ROSE}"/>' + T(195, 128, '상견례 썰', 50, 'j', '#fff')
    + T(80, 260, '상견례 10분 만에', 110, 'j', INK, 'start') + T(80, 390, '분위기 싸해진 썰', 110, 'j', ROSE, 'start')
    + panel(lattice(120, 470, 300, 330) + lattice(660, 470, 300, 330) + char('bride', 380, 760, 1.05, 'shock', (6, -6)) + char('groom', 700, 750, 1.05, 'shock', (10, -8)) + table(990) + sweat(500, 600) + sweat(840, 590), '#FFF7EE', 440, 1110)
    + f'<rect x="70" y="1150" width="940" height="130" rx="65" fill="#fff" stroke="{ROSE}" stroke-width="6"/>' + T(540, 1235, '+ 상견례 전 둘이 맞춰둘 5가지', 58, 'j', INK))
# 2
pages[2] = (f'<rect width="1080" height="1350" fill="{BG}"/>' + header(2)
    + panel(lattice(120, 170, 260, 300) + lattice(700, 170, 260, 300) + char('bride', 360, 600, 1.1, 'happy') + char('groom', 720, 590, 1.1, 'joy') + table(820)
            + bubble(560, 170, 380, '잘 될 거야!', 60, (690, 380)), '#FFF0DC')
    + caption('드디어 상견례 날.\n분위기는 좋았다. 처음 10분은.'))
# 3
pages[3] = (f'<rect width="1080" height="1350" fill="{BG}"/>' + header(3)
    + panel(hearts(10, (90, 160, 990, 1040), '#E9E1FA', 5) + char('momG', 540, 640, 1.55, 'happy')
            + bubble(130, 170, 820, '그래서 예단은\n어느 정도 생각하세요?', 64, (520, 420)), '#F1ECFB')
    + caption('어머님이 웃으면서 물으셨다.'))
# 4
pages[4] = (f'<rect width="1080" height="1350" fill="{BG}"/>' + header(4)
    + panel(speed(330, 640, '#FFE6D2') + char('momB', 330, 620, 1.35, 'smug') + char('momG', 790, 690, 1.1, 'shock') + sweat(930, 560)
            + bubble(100, 170, 700, '예단이요~?\n요즘 누가 예단을 해요~', 62, (320, 430)), '#FFF3E6')
    + caption('우리 엄마도 지지 않았다.'))
# 5
pages[5] = (f'<rect width="1080" height="1350" fill="{BG}"/>' + header(5)
    + panel(char('dadB', 320, 560, 1.15, 'blank') + char('dadG', 760, 560, 1.15, 'blank') + table(780) + sweat(470, 430) + sweat(910, 430)
            + T(540, 250, '(오물오물)', 64, 'g', '#8A90A0'), '#E7EEF3')
    + caption('양가 아버지는 갑자기\n반찬에만 집중하셨다.'))
# 6 카톡
chat = ''
y = 300
for side, t in [('r', '오빠 어머님한테\n예단 얘기 안 했어??'), ('l', '했는데...\n까먹으셨나 봐'), ('r', '지금 우리 엄마\n표정 봐 ㅠㅠ'), ('l', '내가 수습할게\n3초만')]:
    lines = t.split('\n'); bh = len(lines) * 62 + 36; bw = 380
    bx = 690 - bw if side == 'r' else 390
    chat += f'<rect x="{bx}" y="{y}" width="{bw}" height="{bh}" rx="28" fill="{"#FFE36A" if side == "r" else "#fff"}" stroke="{INK}" stroke-width="3"/>' + T(bx + bw / 2, y + 62, lines, 50)
    y += bh + 40
pages[6] = (f'<rect width="1080" height="1350" fill="{BG}"/>' + header(6)
    + panel(f'<rect x="340" y="170" width="400" height="860" rx="50" fill="#3A3542" stroke="{INK}" stroke-width="6"/><rect x="362" y="210" width="356" height="790" rx="26" fill="#DCE9F6"/>' + T(540, 262, '오빠♥', 44, 'j') + chat, '#4E4A5A')
    + caption('식탁 밑에서 급하게 카톡을 보냈다.'))
# 7
pages[7] = (f'<rect width="1080" height="1350" fill="{BG}"/>' + header(7)
    + panel(speed(540, 700, '#FFE9B8', 50, 340) + char('groom', 540, 700, 1.45, 'joy', (-150, 150)) + sweat(720, 520)
            + bubble(110, 165, 860, '예단, 예물 다 생략하고\n그 돈으로 신혼집 대출 갚기로\n저희 둘이 정했어요!', 58, (470, 520)), '#FFF5D8')
    + caption('그날 우리는 상견례에서\n처음으로 같은 편이 됐다.'))
# 8 정리
items = [('예단, 예물', '할지 말지, 한다면 어느 정도까지'), ('결혼식', '규모와 비용을 어떻게 나눌지'), ('신혼집', '지역, 전세인지 매매인지, 대출 계획'),
         ('부모님께 미리 전달', '내 부모님께는 내가 먼저 말하기'), ('곤란한 질문 담당', '돈 얘기가 나오면 누가 대답할지')]
p8 = f'<rect width="1080" height="1350" fill="{BG}"/>' + header(8) + T(540, 230, '상견례 전, 둘이 맞춰둘 5가지', 72, 'j')
cols = [ROSE, '#8FD3C1', '#F5B860', '#96B4EE', '#C59BE6']
for i, (a, b) in enumerate(items):
    y = 290 + i * 180
    p8 += f'<rect x="80" y="{y}" width="920" height="156" rx="50" fill="#fff" stroke="{INK}" stroke-width="5"/><circle cx="160" cy="{y+78}" r="46" fill="{cols[i]}"/>'
    p8 += T(160, y + 98, str(i + 1), 56, 'j', '#fff') + T(240, y + 66, a, 54, 'j', INK, 'start') + T(240, y + 126, b, 48, 'g', '#7A6262', 'start')
p8 += T(540, 1250, '둘이 먼저 정해 두면, 부모님 앞에서 같은 편이 될 수 있어요', 46, 'g', ROSE)
pages[8] = p8
# 9 마무리
pages[9] = (f'<rect width="1080" height="1350" fill="#FFE4E4"/>' + header(9) + hearts(18, (40, 120, 1040, 700), '#FFD0D6', 9)
    + char('bride', 400, 470, 1.15, 'joy', (6, -40)) + char('groom', 690, 460, 1.15, 'joy', (40, -8))
    + f'<rect x="110" y="820" width="860" height="420" rx="60" fill="#fff" stroke="{INK}" stroke-width="6"/>'
    + T(540, 930, '저장해 두고', 76, 'j') + T(540, 1040, '예비 배우자에게 공유하기', 76, 'j', ROSE) + T(540, 1150, '여러분 상견례 썰도 댓글로 들려주세요', 50, 'g', '#7A6262')
    + T(540, 1310, '@yebibubu.toon', 40, 'j', '#C49A9A'))

if __name__ == '__main__':
    render(pages, sys.argv[1] if len(sys.argv) > 1 else 'out/ep01')
