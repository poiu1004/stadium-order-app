import streamlit as st

# 1) 페이지 설정
st.set_page_config(
    page_title="배달앱 메인",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# 2) 전역 CSS
st.markdown("""
<style>
html, body {
  margin: 0; padding: 0;
  height: 100%; overflow: hidden;
}
/* Header/Footer 고정 */
.header, .footer {
  position: fixed;
  left: 0; right: 0;
  height: 60px;
  background-color: #FE4949;
  z-index: 1000;
}
.header { top: 0; }
.footer { bottom: 0; }

/* 콘텐츠 (지도 + 리스트) */
.content {
  position: absolute;
  top: 60px;       /* header 아래 */
  bottom: 60px;    /* footer 위 */
  width: 100%;
  display: flex;
  flex-direction: column;
}

/* 지도: 리스트 높이(360px)를 제외한 나머지 공간 차지 */
.map-container {
  flex: none;
  height: calc(100% - 360px);
  overflow: hidden;
}

/* 리스트: 고정 높이 360px (약 3개 항목 분량), 내부 스크롤 */
.list-container {
  flex: none;
  height: 360px;
  overflow-y: auto;
  padding: 0 1rem;
  box-sizing: border-box;
}

/* 리스트 아이템 0.6배 축소 */
.list-item {
  transform: scale(0.6);
  transform-origin: top left;
  margin-bottom: 1rem;
}
</style>

<div class="header"></div>
<div class="footer"></div>
""", unsafe_allow_html=True)

# 3) 본문 영역
st.markdown('<div class="content">', unsafe_allow_html=True)

# 3-1) 지도
st.markdown('<div class="map-container">', unsafe_allow_html=True)
st.image(
    "https://via.placeholder.com/800x400?text=Map+Here",
    use_container_width=True
)
st.markdown('</div>', unsafe_allow_html=True)

# 3-2) 검색 + 리스트
st.markdown('<div class="list-container">', unsafe_allow_html=True)
query = st.text_input("🔍 음식 또는 가게 검색", placeholder="예) 치킨, 피자")

restaurants = [
    {"name": "치킨나라",   "desc": "바삭한 후라이드 치킨",   "fee": 2500},
    {"name": "피자팩토리", "desc": "치즈 듬뿍 수제 피자",   "fee": 3000},
    {"name": "버거하우스", "desc": "육즙 가득 수제 버거",   "fee": 2000},
    {"name": "초밥천국",   "desc": "신선한 모둠 초밥",      "fee": 3500},
    {"name": "떡볶이로드", "desc": "매콤달콤 떡볶이",       "fee": 1500},
    {"name": "분식왕국",   "desc": "튀김 & 순대 세트 메뉴",  "fee": 1800},
    {"name": "샐러드바이", "desc": "건강한 샐러드 & 스무디","fee": 2200},
]

for r in restaurants:
    st.markdown('<div class="list-item">', unsafe_allow_html=True)
    col1, col2 = st.columns([1, 3])
    with col1:
        st.image(
            "https://via.placeholder.com/80",
            width=80,
            use_container_width=False
        )
    with col2:
        st.subheader(r["name"])
        st.write(r["desc"])
        st.caption(f"배달비: ₩{r['fee']:,}")
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)  # .list-container 닫기
st.markdown('</div>', unsafe_allow_html=True)  # .content 닫기




