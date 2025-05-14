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
  margin: 0;
  padding: 0;
  height: 100vh;
  overflow: hidden;                /* 전체 페이지 스크롤 차단 */
}
.header, .footer {
  background-color: #FE4949;
  width: 100%;
  height: 60px;
}
.content {
  height: calc(100vh - 120px);
  display: flex;
  flex-direction: column;
}
.map-container {
  flex: 1;
  overflow: hidden;
}
.list-container {
  overflow-y: auto;
  max-height: 200px;               /* 하단 리스트 높이 고정 (약 3개 분량) */
  padding: 0 1rem;
}
/* 항목 크기 0.6배 축소 */
.list-item {
  transform: scale(0.6);
  transform-origin: top left;
  margin-bottom: 0.5rem;
}
</style>
<div class="header"></div>
""", unsafe_allow_html=True)

# 3) 본문 영역
st.markdown('<div class="content">', unsafe_allow_html=True)

# 3-1) 지도 (위쪽 절반)
st.markdown('<div class="map-container">', unsafe_allow_html=True)
st.image(
    "https://via.placeholder.com/800x400?text=Map+Here",
    use_container_width=True
)
st.markdown('</div>', unsafe_allow_html=True)

# 3-2) 검색 + 리스트 (아래쪽 절반, 스크롤)
st.markdown('<div class="list-container">', unsafe_allow_html=True)
query = st.text_input("🔍 음식 또는 가게 검색", placeholder="예) 치킨, 피자")

# 예시 음식점 7개
restaurants = [
    {"name": "치킨나라",     "desc": "바삭한 후라이드 치킨",    "fee": 2500},
    {"name": "피자 팩토리", "desc": "치즈 듬뿍 수제 피자",    "fee": 3000},
    {"name": "버거 하우스", "desc": "육즙 가득 수제 버거",    "fee": 2000},
    {"name": "초밥천국",   "desc": "신선한 모둠 초밥",       "fee": 3500},
    {"name": "떡볶이로드", "desc": "매콤달콤 떡볶이",        "fee": 1500},
    {"name": "분식왕국",   "desc": "튀김 & 순대 세트 메뉴",   "fee": 1800},
    {"name": "샐러드바이", "desc": "건강한 샐러드 & 스무디",  "fee": 2200},
]

for r in restaurants:
    # 0.6배 축소를 위해 wrapper
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

# 4) Footer
st.markdown('<div class="footer"></div>', unsafe_allow_html=True)



