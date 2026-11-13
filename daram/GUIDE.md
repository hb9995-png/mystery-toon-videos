# 꿀팁다람 (@daram.tip) 제작 가이드

중고등학생(14~19세)에게 귀여운 다람쥐 캐릭터 '다람이'가 생활·공부·진로·용돈·알바 같은 유익한 정보를 알려주는 25초 안팎 세로 릴스.

## 도구
- `python3 daram/tools/reel.py <episode.json> <out.mp4> <seed>` (seed = EP 번호 × 101). 오리지널 배경음악이 자동으로 들어간다.
- 캐릭터: `daram/assets/daram.png` (바꾸지 않는다).
- 한글 글꼴: /usr/share/fonts/opentype/noto/NotoSansCJK-*.ttc (없으면 `apt-get install -y fonts-noto-cjk`). 필요한 파이썬 패키지: pillow numpy.

## episode.json 형식 (예: daram/tools/episodes/ep02.json)
- slides 7장: 1장 훅(`"hook": true`, tag=주제, title=질문형 2줄), 2~6장 꿀팁 1~5(tag="꿀팁 N", title 2줄, body 3줄, bubble=짧은 말 6자 이하), 7장 끝(`"end": true`, tag="꿀팁다람", 저장·공유 유도).
- title 한 줄 10자 안팎, body 한 줄 14자 안팎. 줄바꿈은 \n.

## 내용 규칙
- 분야를 돌려 가며: 공부법, 시험, 수행평가, 진로·학과, 학교생활, 용돈·금융 상식, 알바·노동 권리, 디지털(폰·SNS 안전), 건강 습관(수면·자세 등 일반 상식), 과학·역사 상식.
- 숫자·법·제도는 그날 WebSearch/WebFetch 로 공식 자료(고용노동부, 교육부 등)에서 확인한 것만 쓴다. 확인 못 하면 숫자 없는 주제로 바꾼다.
- 다이어트·체중·외모 평가, 연애·성, 자해, 위험한 챌린지, 특정 브랜드 광고, 정치는 다루지 않는다. 말투는 친구처럼 반말, 상냥하게.
- used.txt 와 주제가 겹치지 않게.

## 캡션
- 첫 줄: 사람이 검색할 말이 자연스럽게 들어간 훅 + 🐿️. 둘째 줄: 저장·공유 유도.
- 해시태그 최대 5개(파이썬으로 # 개수 검사). #꿀팁다람 은 항상 1개. #릴스 #reels #fyp #좋아요 #팔로우 같은 범용 태그 금지.
