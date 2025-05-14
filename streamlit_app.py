import streamlit as st
from streamlit.components.v1 import html as st_html

# 1) 페이지 설정
st.set_page_config(
    page_title="배달앱 메인",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2) CSS 주입
st.markdown("""
<style>
/* 전체 페이지 스크롤 제거 */
html, body, .main, .main > div { overflow: hidden; height: 100%; }
/* 맵 영역 */
.map-container { position: absolute; top: 0; left: 0; right: 0; bottom: 260px; overflow: hidden; }
.map-container img { width: 100%; height: 100%; object-fit: cover; }
/* 하단 박스 */
.bottom-box { position: absolute; left: 0; right: 0; bottom: 0; height: 260px; background: #fff; box-shadow: 0 -2px 5px rgba(0,0,0,0.1); }
.bottom-box .search-box { height: 40px; padding: 5px; }
.bottom-box .search-box input { width: 100%; height: 100%; box-sizing: border-box; padding: 0 8px; }
.bottom-box .list-container { height: calc(260px - 50px); overflow-y: auto; padding: 5px; box-sizing: border-box; }
.bottom-box .list-item { display: flex; align-items: center; height: 110px; margin-bottom: 8px; border: 1px solid #eee; border-radius: 8px; padding: 8px; }
.bottom-box .list-item img { width: 80px; height: 80px; border-radius: 8px; margin-right: 12px; }
.bottom-box .list-item .info { display: flex; flex-direction: column; }
.bottom-box .list-item .name { font-weight: bold; margin-bottom: 4px; }
.bottom-box .list-item .desc { color: #666; margin-bottom: 4px; }
.bottom-box .list-item .fee { color: #999; font-size: 0.8rem; }
</style>
""", unsafe_allow_html=True)

# 3) 맵 영역 렌더링
st.markdown('<div class="map-container">', unsafe_allow_html=True)
st.image("https://via.placeholder.com/800x400?text=Map+Here")
st.markdown('</div>', unsafe_allow_html=True)

# 4) 하단 박스 전체를 HTML 컴포넌트로 렌더
restaurants = [
    {"name":"치킨나라",   "desc":"바삭한 후라이드 치킨","fee":2500},
    {"name":"피자팩토리", "desc":"치즈 듬뿍 수제 피자","fee":3000},
    {"name":"버거하우스", "desc":"육즙 가득 수제 버거","fee":2000},
    {"name":"초밥천국",   "desc":"신선한 모둠 초밥","fee":3500},
    {"name":"떡볶이로드", "desc":"매콤달콤 떡볶이","fee":1500},
    {"name":"분식왕국",   "desc":"튀김 & 순대 세트","fee":1800},
    {"name":"샐러드바이", "desc":"건강한 샐러드 & 스무디","fee":2200},
]

items_html = "".join([
    f'''<div class="list-item">
          <img src="https://via.placeholder.com/80" alt="food"/>
          <div class="info">
            <div class="name">{r['name']}</div>
            <div class="desc">{r['desc']}</div>
            <div class="fee">배달비: ₩{r['fee']:,}</div>
          </div>
        </div>''' for r in restaurants
])

st_html(f"""
<div class="bottom-box">
  <div class="search-box">
    <input type="text" placeholder="🔍 음식 또는 가게 검색" />
  </div>
  <div class="list-container">
    {items_html}
  </div>
</div>
""", height=260)






