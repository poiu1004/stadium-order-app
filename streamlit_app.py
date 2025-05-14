import streamlit as st

# ————————————————
# 1) 페이지 설정
st.set_page_config(
    page_title="배달앱 메인",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ——————————————————
# 2) CSS 주입 (반드시 가장 위에!)
st.markdown("""
<style>
/* 1) Streamlit 전체 앱(main) 고정: 페이지 스크롤 완전 차단 */
main {
  position: fixed !important;
  top: 0; left: 0; right: 0; bottom: 0;
  overflow: hidden !important;
}

/* 2) 헤더/푸터 고정 */
.header, .footer {
  position: fixed; left: 0; right: 0; height: 60px;
  background-color: #FE4949; z-index: 1000;
}
.header { top: 0; }
.footer { bottom: 0; }

/* 3) 콘텐츠 영역 (헤더·푸터 사이) */
.content {
  position: absolute; top: 60px; bottom: 60px; width: 100%;
  display: flex; flex-direction: column;
  overflow: hidden;    /* 자식 컨테이너 외에는 스크롤 금지 */
}

/* 4) 지도 영역: 고정 높이(전체 높이 – 리스트 높이) */
.map-container {
  flex: none;
  height: calc(100% - 360px);
  overflow: hidden;
}

/* 5) 리스트 영역: 고정 360px, 이 안에서만 스크롤 */
.list-container {
  flex: none;
  height: 360px;
  overflow-y: auto;
  padding: 0 1rem;
  box-sizing: border-box;
}

/* 6) 카드 스타일 (딱 3개 보이도록 높이 120px) */
.list-item {
  display: flex; align-items: center;
  height: 120px;          /* 360px ÷ 3 = 120px */
  margin-bottom: 8px;
  padding: 8px;
  border: 1px solid #eee;
  border-radius: 8px;
  font-size: 0.9rem;      /* 살짝 작게 */
}
.list-item img {
  width: 72px; height: 72px;
  border-radius: 8px;
  margin-right: 12px;
}
.list-item .info {
  display: flex; flex-direction: column;
}
.list-item .name { font-weight: bold; margin-bottom: 4px; }
.list-item .desc { color: #666; margin-bottom: 4px; }
.list-item .fee  { color: #999; font-size: 0.8rem; }
</style>
""", unsafe_allow_html=True)

# ————————————————
# 3) 헤더, 콘텐츠, 푸터 구조

# 고정 헤더
st.markdown('<div class="header"></div>', unsafe_allow_html=True)

# 콘텐츠 영역 시작
st.markdown('<div class="content">', unsafe_allow_html=True)

# 3-1) 지도 (위쪽)
st.markdown('<div class="map-container">', unsafe_allow_html=True)
st.image("https://via.placeholder.com/800x400?text=Map+Here", use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)

# 3-2) 검색 + 리스트 (아래쪽, 360px 고정)
st.markdown('<div class="list-container">', unsafe_allow_html=True)
query = st.text_input("🔍 음식 또는 가게 검색", placeholder="예) 치킨, 피자")

restaurants = [
    {"name":"치킨나라",   "desc":"바삭한 후라이드 치킨",    "fee":2500},
    {"name":"피자팩토리", "desc":"치즈 듬뿍 수제 피자",    "fee":3000},
    {"name":"버거하우스", "desc":"육즙 가득 수제 버거",    "fee":2000},
    {"name":"초밥천국",   "desc":"신선한 모둠 초밥",       "fee":3500},
    {"name":"떡볶이로드", "desc":"매콤달콤 떡볶이",        "fee":1500},
    {"name":"분식왕국",   "desc":"튀김 & 순대 세트 메뉴",   "fee":1800},
    {"name":"샐러드바이", "desc":"건강한 샐러드 & 스무디","fee":2200},
]

for r in restaurants:
    st.markdown(f'''
      <div class="list-item">
        <img src="https://via.placeholder.com/80" alt="food"/>
        <div class="info">
          <div class="name">{r["name"]}</div>
          <div class="desc">{r["desc"]}</div>
          <div class="fee">배달비: ₩{r["fee"]:,}</div>
        </div>
      </div>
    ''', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)  # .list-container닫기
st.markdown('</div>', unsafe_allow_html=True)  # .content닫기

# 고정 푸터
st.markdown('<div class="footer"></div>', unsafe_allow_html=True)





