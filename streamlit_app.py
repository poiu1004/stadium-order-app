import streamlit as st

# 1) 무조건 최상단에 한 번만!
st.set_page_config(layout="wide", initial_sidebar_state="collapsed")

# 2) 메타태그 + CSS (헤더/푸터, 모바일 풀스크린, flex)
st.markdown("""
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
  /* 전체 화면 flex 배치 */
  html, body, .block-container {
    width:100vw!important; height:100vh!important;
    margin:0; padding:0; overflow:hidden;
    display:flex!important; flex-direction:column!important;
  }
  /* 헤더 높이 만큼 메인 위쪽 여백 */
  div[role="main"] {
    flex:1 1 auto!important;
    padding-top:60px!important;    /* 헤더 높이 */
    padding-bottom:60px!important; /* 푸터 높이 */
    overflow-y:auto!important;
  }
  /* 헤더 스타일 */
  .app-header {
    position:fixed; top:0; left:0;
    width:100%; height:60px;
    background:#FE4949;
    display:flex; align-items:center;
    padding:0 16px; box-sizing:border-box;
    z-index:1000;
  }
  .app-header select {
    flex:1;
    padding:8px 12px;
    border:none; border-radius:8px;
    font-size:16px;
  }
  .app-header img {
    width:32px; height:32px;
    margin-left:12px;
  }
  /* 푸터 스타일 */
  .app-footer {
    position:fixed; bottom:0; left:0;
    width:100%; height:60px;
    background:#FE4949;
    display:flex; align-items:center; justify-content:space-around;
    padding:0 16px; box-sizing:border-box;
    z-index:1000;
  }
  .app-footer .nav-btn {
    width:40px; height:40px;
    background:white; border-radius:8px;
  }
</style>

<!-- 3) 헤더 마크업 -->
<div class="app-header">
  <select>
    <option>잠실 야구장</option>
    <option>SSG 야구장</option>
    <option>고척돔</option>
  </select>
  <img src="https://via.placeholder.com/32" alt="logo">
</div>
""", unsafe_allow_html=True)

# --- 이 아래가 div[role="main"] 영역 ---

# 4) 맵 플레이스홀더
st.image("https://via.placeholder.com/350x180?text=Map+Placeholder", use_column_width=True)

# 5) 검색창
st.text_input("", placeholder="검색어를 입력하세요...", key="search")

# 6) 더미 메뉴
menus = [
    {"name":"라지 크림 새우","price":12000,"stand":"D05","time":20},
    {"name":"불고기 핫도그","price":6000, "stand":"D08","time":5},
    {"name":"치즈버킷","price":15000,"stand":"D07","time":60},
]
for m in menus:
    color = "#8BC34A" if m["time"]<=10 else "#FFEB3B" if m["time"]<=30 else "#F44336"
    with st.container():
        c1, c2, c3 = st.columns([1,4,2])
        c1.image("https://via.placeholder.com/60", width=60)
        c2.markdown(f"**{m['name']}** ({m['price']:,}원)\n1층 - {m['stand']}")
        c3.markdown(f"""
<div style="
  background:#F0F0F0; border-radius:8px;
  padding:4px 8px; text-align:center;
">
  {m['time']}분 
  <span style="
    display:inline-block; width:12px; height:12px;
    background:{color}; border-radius:50%; margin-left:4px;
  "></span>
</div>
""", unsafe_allow_html=True)
        st.markdown("---")

# 7) 푸터 마크업
st.markdown("""
<div class="app-footer">
  <div class="nav-btn"></div>
  <div class="nav-btn"></div>
  <div class="nav-btn" style="width:56px;height:56px;margin-top:-8px;border-radius:28px;"></div>
  <div class="nav-btn"></div>
  <div class="nav-btn"></div>
</div>
""", unsafe_allow_html=True)
