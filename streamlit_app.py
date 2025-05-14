# app.py 또는 pages/1_Home.py
import streamlit as st

# 1) 페이지 설정
st.set_page_config(
    page_title="배달앱 메인",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# 2) 전역 CSS (Header/Footer, 스크롤 영역)
st.markdown("""
<style>
/* 상단·하단 바 */
.header, .footer {
  background-color: #FE4949;
  width: 100%;
  height: 60px;
}
/* 콘텐츠 전체 높이 = 뷰포트 높이 – (헤더+푸터 높이) */
.content {
  height: calc(100vh - 120px);
  overflow: hidden;
  display: flex;
  flex-direction: column;
}
/* 지도 영역: 전체 콘텐츠 높이의 50% */
.map-container {
  flex: 1;
  overflow: hidden;
}
/* 리스트 영역: 나머지 50% + 세로 스크롤 */
.list-container {
  flex: 1;
  overflow-y: auto;
  padding: 0 1rem;
}
</style>
<div class="header"></div>
""", unsafe_allow_html=True)

# 3) 본문 영역
st.markdown('<div class="content">', unsafe_allow_html=True)

# 3-1) 지도 (위쪽 절반)
with st.container():
    st.markdown('<div class="map-container">', unsafe_allow_html=True)
    # 실제 서비스: 구글맵·카카오맵 iframe 또는 Static map 이미지
    st.image("https://via.placeholder.com/800x400?text=Map+Here", use_column_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# 3-2) 검색 + 리스트 (아래쪽 절반, 스크롤)
with st.container():
    st.markdown('<div class="list-container">', unsafe_allow_html=True)
    # 검색창
    query = st.text_input("🔍 음식 또는 가게 검색", placeholder="예) 치킨, 피자")
    # 예시 데이터
    restaurants = [
        {"name": "치킨 나라", "desc": "바삭한 후라이드 치킨", "fee": 2500},
        {"name": "피자 팩토리", "desc": "치즈 듬뿍 피자",   "fee": 3000},
        # … 더 많은 항목 …
    ]
    # 리스트 렌더링
    for r in restaurants:
        col1, col2 = st.columns([1, 3])
        with col1:
            st.image("https://via.placeholder.com/80", width=80)
        with col2:
            st.subheader(r["name"])
            st.write(r["desc"])
            st.caption(f"배달비: ₩{r['fee']:,}")
        st.markdown("---")
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# 4) Footer
st.markdown('<div class="footer"></div>', unsafe_allow_html=True)

