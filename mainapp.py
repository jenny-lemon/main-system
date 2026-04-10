import streamlit as st
import streamlit.components.v1 as components

# ── 頁面基本設定 ──────────────────────────────────────────
st.set_page_config(
    page_title="內部系統總覽",
    page_icon="🧭",
    layout="wide",
)

# ── 系統清單（之後新增系統只要在這裡加一行）──────────────────
SYSTEMS = [
    {"name": "新系統",  "icon": "✦", "url": "https://new-system.streamlit.app"},
    {"name": "訂單系統", "icon": "◈", "url": "https://orders-system.streamlit.app"},
    {"name": "備忘系統", "icon": "◉", "url": "https://memo-system.streamlit.app"},
]

# ── 自訂 CSS ─────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@300;400;500;600&family=DM+Sans:wght@300;400;500&display=swap');

/* 隱藏 Streamlit 預設元素 */
#MainMenu, header, footer { visibility: hidden; }
.block-container { padding: 0 !important; max-width: 100% !important; }
[data-testid="stAppViewContainer"] { background: #0f1117; }

/* 整體字體 */
html, body, [class*="css"] {
    font-family: 'DM Sans', 'Noto Sans TC', sans-serif;
}

/* 頂部 Header 區塊 */
.top-header {
    background: linear-gradient(135deg, #0f1117 0%, #1a1d2e 100%);
    border-bottom: 1px solid rgba(255,255,255,0.07);
    padding: 18px 36px 0 36px;
    display: flex;
    flex-direction: column;
    gap: 0;
}

.header-title-row {
    display: flex;
    align-items: center;
    gap: 12px;
    margin-bottom: 16px;
}

.header-logo {
    width: 32px;
    height: 32px;
    background: linear-gradient(135deg, #6c8fff, #a78bfa);
    border-radius: 8px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 16px;
    flex-shrink: 0;
}

.header-title {
    font-size: 17px;
    font-weight: 600;
    color: #e8eaf0;
    letter-spacing: 0.02em;
}

.header-subtitle {
    font-size: 12px;
    color: #5a6070;
    font-weight: 300;
    margin-left: auto;
    letter-spacing: 0.05em;
}

/* Tab 導覽列 */
.tab-nav {
    display: flex;
    gap: 0;
    align-items: flex-end;
}

.tab-btn {
    padding: 10px 22px;
    font-size: 13.5px;
    font-weight: 400;
    color: #636878;
    background: transparent;
    border: none;
    border-bottom: 2px solid transparent;
    cursor: pointer;
    transition: all 0.2s ease;
    font-family: 'DM Sans', 'Noto Sans TC', sans-serif;
    letter-spacing: 0.01em;
    white-space: nowrap;
}

.tab-btn:hover {
    color: #a8afc0;
    background: rgba(255,255,255,0.03);
}

.tab-btn.active {
    color: #8ba4ff;
    border-bottom: 2px solid #8ba4ff;
    font-weight: 500;
}

.tab-icon {
    margin-right: 7px;
    font-size: 12px;
    opacity: 0.8;
}

/* iframe 容器 */
.iframe-container {
    width: 100%;
    background: #0f1117;
}

/* 隱藏 streamlit 元件的多餘 padding */
[data-testid="stHorizontalBlock"] { gap: 0 !important; }
div[data-testid="column"] { padding: 0 !important; }
</style>
""", unsafe_allow_html=True)

# ── Session state：記住目前選的 tab ─────────────────────
if "active_tab" not in st.session_state:
    st.session_state.active_tab = 0

# ── Header + Tab HTML ─────────────────────────────────
tabs_html = ""
for i, s in enumerate(SYSTEMS):
    active_class = "active" if i == st.session_state.active_tab else ""
    tabs_html += f"""
        <button class="tab-btn {active_class}" onclick="selectTab({i})">
            <span class="tab-icon">{s['icon']}</span>{s['name']}
        </button>
    """

st.markdown(f"""
<div class="top-header">
    <div class="header-title-row">
        <div class="header-logo">🧭</div>
        <span class="header-title">內部系統總覽</span>
        <span class="header-subtitle">INTERNAL DASHBOARD</span>
    </div>
    <div class="tab-nav">
        {tabs_html}
    </div>
</div>

<script>
function selectTab(index) {{
    const input = window.parent.document.querySelectorAll('input[type="radio"]');
    if (input[index]) input[index].click();
}}
</script>
""", unsafe_allow_html=True)

# ── 用隱藏的 radio 控制 active tab ───────────────────────
selected = st.radio(
    "tab_selector",
    options=[s["name"] for s in SYSTEMS],
    index=st.session_state.active_tab,
    horizontal=True,
    label_visibility="collapsed",
)

# 更新 session state
for i, s in enumerate(SYSTEMS):
    if selected == s["name"]:
        st.session_state.active_tab = i
        current = s
        break

# ── 取得視窗高度並顯示 iframe ─────────────────────────────
iframe_url = current["url"] + "/?embed=true"
IFRAME_HEIGHT = 880  # 可視需求調整

components.iframe(iframe_url, height=IFRAME_HEIGHT, scrolling=True)
