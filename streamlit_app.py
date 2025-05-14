import streamlit as st

# 1) 페이지 설정
st.set_page_config(
    page_title="배달앱 메인",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2) CSS 주입 (반드시 가장 위에!)
st.markdown("""
<style>
/* 고정 헤더 (필요 시 유지) */
.header {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  height: 60px;
  background-color: #FE4949;
  z-index: 1000;
}

/* 맵 영역: 헤더 아래, bottom-box 위 */
.map-container {
  position: absolute;
  top: 60px;
  left: 0;
  right: 0;
  bottom: 260px; /* bottom-box 높이 */
  overflow: hidden;
}
.map-container img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

/* 하단 박스: 검색 + 리스트 */
.bottom-box {
  position: fixed;
  left: 0;
  right: 0;
  bottom: 0;
  height: 260px; /* search(40px) + 2 items * 110px + margins */
  background-color: #fff;
  border-top: 1px solid #ddd;
  box-shadow: 0 -2px 5px rgba(0,0,0,0.1);
  padding: 10px;
  box-sizing: border-box;
  z-index: 1000;
}

/* 검색창 영역 */
.bottom-box .search-box {
  height: 40px;
  margin-bottom: 10px;
}

/* 리스트 영역: 내부 스크롤 */
.bottom-box .list-container {
  height: calc(100% - 50px); /* search-box + margin 제외 */
  overflow-y: auto;
}

/* 카드 스타일 (2개만 보이도록 고정 높이 조정) */
.list-item {
  display: flex;
  align-items: center;
  height: 110px; /* 2개 = 220px + margin */
  margin-bottom: 10px;
  padding: 8px;
  border: 1px solid #eee;
  border-radius: 8px;
  font-size: 0.9rem;
}
.list-item img {
  width: 80px;
  height: 80px;
  border-radius: 8px;
  margin-right: 12px;
}
.list-item .info {
  display: flex;
  flex-direction: column;
}
.list-item .name { font-weight: bold; margin-bottom: 4px; }
.list-item .desc { color: #666; margin-bottom: 4px; }
.list-item .fee  { color: #999; font-size: 0.8rem; }
</style>
""", unsafe_allow_html=True)

# 3) 헤더 (필요 시)
st.markdown('<div class="header"></div>', unsafe_allow_html=True)

# 4) 맵 영역
st.markdown('<div class="map-container">', unsafe_allow_html=True)
st.image("https://via.placeholder.com/800x400?text=Map+Here", use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)

# 5) 하단 박스 시작
st.markdown('<div class="bottom-box">', unsafe_allow_html=True)

# 5-1) 검색창
st.markdown('<div class="search-box">', unsafe_allow_html=True)
query = st.text_input("🔍 음식 또는 가게 검색", placeholder="예) 치킨, 피자")
st.markdown('</div>', unsafe_allow_html=True)

# 5-2) 리스트 영역
st.markdown('<div class="list-container">', unsafe_allow_html=True)

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

st.markdown('</div>', unsafe_allow_html=True)  # .list-container 닫기

st.markdown('</div>', unsafe_allow_html=True)  # .bottom-box 닫기

# 6) (필요 시) 푸터
# st.markdown('<div class="footer"></div>', unsafe_allow_html=True)






