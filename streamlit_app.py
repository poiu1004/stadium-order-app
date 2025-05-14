import streamlit as st

# 1) 페이지 설정: 반드시 최상단에!
st.set_page_config(
    page_title="Stadium Order",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2) 메타 태그 + CSS (모바일 전체화면, 상·하단 바, flex 레이아웃)
st.markdown("""
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
  /* 전체 화면을 100%로 채우고, flex column 배치 */
  html, body, .block-container {
    width: 100vw !important;
    height: 100vh !important;
    margin: 0; padding: 0;
    overflow: hidden;
    display: flex !important;
    flex-direction: column !important;
  }
  /* 실제 콘텐츠 영역: 상단/하단 바 높이(20px) 제외한 공간에서 스크롤 가능 */
  div[role="main"] {
    width: 100% !important;
    height: calc(100vh - 40px) !important;  /* 상단20 + 하단20 제외 */
    margin: 0 !important;
    padding: 0 !important;
    overflow-y: auto !important;
    display: flex;
    flex-direction: column;
  }
  /* 가로 스크롤 방지 */
  body, html { overflow-x: hidden !important; }

  /* 상단·하단 고정 바 */
  .top-bar, .bottom-bar {
    position: fixed;
    left: 0; width: 100%; height: 20px;
    background: #FE4949;
    z-index: 999;
  }
  .top-bar { top: 0; }
  .bottom-bar { bottom: 0; }
</style>

<!-- 상단·하단 바 엘리먼트 -->
<div class="top-bar"></div>
<div class="bottom-bar"></div>
""", unsafe_allow_html=True)

# --- 여기부터 실제 Streamlit UI ---

# 3) 헤더: 구장 선택 드롭다운 + 로고
st.markdown("""
<div style="
  display: flex; align-items: center;
  padding: 12px; background: #FE4949;
">
  <select style="
    flex: 1;
    padding: 8px 12px;
    font-size: 16px;
    border: 2px solid white;
    border-radius: 12px;
    background: white;
  ">
    <option>잠실 야구장</option>
    <option>SSG 야구장</option>
    <option>고척돔</option>
  </select>
  <div style="width: 12px;"></div>
  <img src="https://via.placeholder.com/32"
       style="width:32px; height:32px; border-radius:50%;" />
</div>
""", unsafe_allow_html=True)

# 4) 맵 플레이스홀더
st.image(
    "https://via.placeholder.com/350x180?text=Map+Placeholder",
    use_column_width=True
)

# 5) 검색창
_ = st.text_input("", placeholder="검색어를 입력하세요...", key="search")

# 6) 더미 메뉴 리스트
menus = [
    {"name": "라지 크림 새우", "price": 12000, "stand": "D05", "time": 20},
    {"name": "불고기 핫도그",   "price": 6000,  "stand": "D08", "time": 5},
    {"name": "치즈버킷",       "price": 15000, "stand": "D07", "time": 60},
]

for m in menus:
    # ETA 배지 색상
    badge_color = "#8BC34A" if m["time"] <= 10 else "#FFEB3B" if m["time"] <= 30 else "#F44336"

    with st.container():
        cols = st.columns([1, 4, 2])
        # 메뉴 이미지
        cols[0].image("https://via.placeholder.com/60", width=60)
        # 이름·가격·스탠드
        cols[1].markdown(f"**{m['name']}**  ({m['price']:,}원)\n1층 - {m['stand']}")
        # ETA 배지
        cols[2].markdown(f"""
<div style="
  background: #F0F0F0;
  border-radius: 8px;
  padding: 4px 8px;
  text-align: center;
  font-size: 14px;
">
  {m['time']}분
  <span style="
    display: inline-block;
    width: 12px; height: 12px;
    background: {badge_color};
    border-radius: 50%;
    margin-left: 4px;
  "></span>
</div>
""", unsafe_allow_html=True)
        st.markdown("---")

# 7) 하단 내비게이션 (바 아래, 높이 60px)
st.markdown("""
<div style="
  position: fixed;
  bottom: 20px;
  left: 50%;
  transform: translateX(-50%);
  width: 375px;
  height: 60px;
  background: #FE4949;
  display: flex;
  justify-content: space-around;
  align-items: center;
  border-radius: 12px 12px 0 0;
  z-index: 999;
">
  <div style="width:40px; height:40px; background:white; border-radius:8px;"></div>
  <div style="width:40px; height:40px; background:white; border-radius:8px;"></div>
  <div style="width:56px; height:56px; background:white; border-radius:28px; margin-top:-16px;"></div>
  <div style="width:40px; height:40px; background:white; border-radius:8px;"></div>
  <div style="width:40px; height:40px; background:white; border-radius:8px;"></div>
</div>
""", unsafe_allow_html=True)








