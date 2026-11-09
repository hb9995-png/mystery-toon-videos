# 동네성적표(townreport) 매일 제작 가이드

인스타 계정 동네성적표(@townreport): 서울·경기 행정동 하나를 골라 교통·학군·생활·자연·개발 5과목 성적표를 사진 8장 캐러셀로 만든다.

## 준비
1. 이 저장소의 `townreport/tools/*` 를 `/home/claude/dongne/` 에 복사하고 `mkdir -p /home/claude/dongne/{data,build,out,episodes}`.
2. 행정동 경계: `curl -sSL -o /home/claude/dongne/data/dong.json https://raw.githubusercontent.com/vuski/admdongkor/master/ver20230701/HangJeongDong_ver20230701.geojson` (약 35MB).
3. 한글 폰트는 `/usr/share/fonts/opentype/noto/NotoSansCJK-*.ttc` (없으면 `apt-get install -y fonts-noto-cjk`). Python 패키지: Pillow, numpy.
4. 지도는 OpenStreetMap 타일(tile.openstreetmap.org)을 basemap.py 가 받아 캐시한다. 역 좌표는 `python3 geocode.py 역이름` (Nominatim). 결과의 display_name 에 해당 동/구가 들어 있는지 확인한다.

## 동네 고르기
- `townreport/used.txt` 에 있는 동은 다시 하지 않는다. 다음 EP 번호 = used.txt 줄 수 + 1.
- 서울·경기 행정동 중에서 고른다. 사람들이 많이 검색하는 동네(역세권, 신도시, 재개발, 학군지)를 우선하고, 서울과 경기를 번갈아 다룬다. 이름은 dong.json 의 adm_nm 과 정확히 같아야 한다(예: "서울특별시 동작구 흑석동", "경기도 구리시 갈매동").
- 경계가 너무 넓거나(수 km) 산·하천만 있는 동은 피한다.

## 리서치 규칙
- WebSearch/WebFetch 로 6~10번 찾아본다(교통, 학교, 생활시설, 공원, 개발계획, 단점). 실제로 연 자료에 있는 사실만 쓰고, 출처를 기록한다.
- 아파트 시세, 가격, "오른다/사라" 같은 투자 권유 표현은 쓰지 않는다. 개발 호재는 확정/추진/검토 단계를 정확히 구분하고, 미확정이면 "단, 아직 확정 아님"을 넣는다.
- 행정동 경계 밖 시설은 "인근"으로 쓴다. 확실하지 않으면 빼거나 일반 표현으로 쓴다.
- 등급: A+ A A- B+ B B- C 중에서. 매번 다 높게 주지 말고 단점이 있으면 깎는다. 감점 요인 2개는 꼭 쓴다.

## 에피소드 파일
`tools/episodes/ep01_gongdeok.json` 형식을 그대로 따른다. 각 과목 lines 3줄(한 줄 22자 안팎, 세 번째 줄은 아쉬운 점이면 "단, " 으로 시작), sub 한 줄 평 18자 안팎. pins 에 대표 역 1개.

## 렌더링과 확인
- `cd /home/claude/dongne && python3 carousel.py episodes/epNN_이름.json out/epNN` → 01~08.jpg (1080x1350).
- 8장을 축소 합본으로 만들어 직접 보고 글자 넘침, 지도 경계 잘림, 핀 위치를 확인하고 고친다.

## 캡션
`tools/episodes/ep01_gongdeok_caption.txt` 형식. 해시태그 8개: #동네이름 #구/시 #동네성적표 #입지분석 + 그 동네에 맞는 4개(편마다 다르게). 끝에 "※ 공개 자료 기반 정보 제공 목적이며 투자 권유가 아닙니다." 와 "※ 지도 © OpenStreetMap contributors" 를 넣는다. 2,200자 이하.

## 대기열
- `townreport/queue/<YYYY-MM-DD>/01.jpg ~ 08.jpg`, `caption.txt`, `meta.json` ({"ep":N,"adm_nm":"...","title":"...","posted":false,"media_id":null}).
- 에피소드 json 과 캡션을 `townreport/tools/episodes/` 에도 보관하고, used.txt 에 `EP.NN <adm_nm> <날짜>` 를 추가한다.
- 7일보다 오래된 queue 날짜 폴더는 git rm 한다. 저장소의 다른 폴더(videos/ 등 미스테리툰 파일)는 건드리지 않는다.
