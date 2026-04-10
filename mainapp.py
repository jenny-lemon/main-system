import streamlit as st
import streamlit.components.v1 as components
import json
import os

# ── 頁面設定 ──────────────────────────────────────────────
st.set_page_config(
    page_title="內部系統總覽",
    page_icon="🧭",
    layout="wide",
)

# ── 讀取 / 儲存系統清單 ────────────────────────────────────
SYSTEMS_FILE = "systems.json"

DEFAULT_SYSTEMS = [
    {"name": "新系統",  "icon": "✦", "url": "https://new-system.streamlit.app"},
    {"name": "訂單系統", "icon": "◈", "url": "https://orders-system.streamlit.app"},
    {"name": "備忘系統", "icon": "◉", "url": "https://memo-system.streamlit.app"},
]

def load_systems():
    if os.path.exists(SYSTEMS_FILE):
        with open(SYSTEMS_FILE, encoding="utf-8") as f:
            return json.load(f)
    return DEFAULT_SYSTEMS

def save_systems(systems):
    with open(SYSTEMS_FILE, "w", encoding="utf-8") as f:
        json.dump(systems, f, ensure_ascii=False, indent=2)

if "systems" not in st.session_state:
    st.session_state.systems = load_systems()

# ── 美化 CSS ──────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@300;400;500;600&family=DM+Sans:ital,opsz,wght@0,9..40,300;0,9..40,400;0,9..40,500&display=swap');

/* 隱藏 Streamlit 預設 UI */
#MainMenu, header, footer { visibility: hidden; }
[data-testid="stToolbar"] { display: none; }
.block-container {
    padding-top: 1.5rem !important;
    padding-left: 2rem !important;
    padding-right: 2rem !important;
    max-width: 100% !important;
}

/* 整體背景與字體 */
[data-testid="stAppViewContainer"] {
    background: #0e1118;
    font-family: 'DM Sans', 'Noto Sans TC', sans-serif;
}

/* 頁面頂部標題 */
.dashboard-header {
    display: flex;
    align-items: center;
    gap: 12px;
    margin-bottom: 20px;
    padding-bottom: 16px;
    border-bottom: 1px solid rgba(255,255,255,0.07);
}
.dashboard-logo {
    width: 36px; height: 36px;
    background: linear-gradient(135deg, #6c8fff 0%, #a78bfa 100%);
    border-radius: 9px;
    display: flex; align-items: center; justify-content: center;
    font-size: 18px;
}
.dashboard-title {
    font-size: 18px; font-weight: 600;
    color: #e2e5f0; letter-spacing: 0.02em;
}
.dashboard-badge {
    margin-left: auto;
    font-size: 11px; font-weight: 400;
    color: #3d4358;
    letter-spacing: 0.1em;
    text-transform: uppercase;
}

/* Tab 樣式 */
[data-testid="stTabs"] [role="tablist"] {
    gap: 0px;
    border-bottom: 1px solid rgba(255,255,255,0.07);
    background: transparent;
}
[data-testid="stTabs"] [role="tab"] {
    font-family: 'DM Sans', 'Noto Sans TC', sans-serif !important;
    font-size: 13.5px !important;
    font-weight: 400 !important;
    color: #5a6278 !important;
    padding: 10px 20px !important;
    border: none !important;
    border-bottom: 2px solid transparent !important;
    background: transparent !important;
    border-radius: 0 !important;
    transition: all 0.2s ease !important;
}
[data-testid="stTabs"] [role="tab"]:hover {
    color: #9aa3be !important;
    background: rgba(255,255,255,0.03) !important;
}
[data-testid="stTabs"] [role="tab"][aria-selected="true"] {
    color: #8ba4ff !important;
    border-bottom: 2px solid #8ba4ff !important;
    font-weight: 500 !important;
    background: transparent !important;
}
[data-testid="stTabs"] [data-testid="stTabPanel"] {
    padding: 0 !important;
}

/* Input 欄位 */
[data-testid="stTextInput"] input {
    background: rgba(255,255,255,0.05) !important;
    border: 1px solid rgba(255,255,255,0.1) !important;
    border-radius: 8px !important;
    color: #d0d4e0 !important;
    font-family: 'DM Sans', 'Noto Sans TC', sans-serif !important;
}
[data-testid="stTextInput"] input:focus {
    border-color: #8ba4ff !important;
    box-shadow: 0 0 0 2px rgba(139, 164, 255, 0.15) !important;
}

/* 按鈕 */
[data-testid="stButton"] button {
    border-radius: 8px !important;
    font-family: 'DM Sans', 'Noto Sans TC', sans-serif !important;
    font-size: 13px !important;
    transition: all 0.2s ease !important;
}
</style>
""", unsafe_allow_html=True)

# ── 頁面頂部 Header ───────────────────────────────────────
st.markdown("""
<div class="dashboard-header">
    <div class="dashboard-logo">🧭</div>
    <span class="dashboard-title">內部系統總覽</span>
    <span class="dashboard-badge">Internal Dashboard</span>
</div>
""", unsafe_allow_html=True)

# ── 組合 Tab 清單（系統 + 設定）────────────────────────────
systems = st.session_state.systems
tab_labels = [f"{s['icon']}  {s['name']}" for s in systems] + ["⚙️  設定"]
tabs = st.tabs(tab_labels)

# ── 各系統 iframe ─────────────────────────────────────────
for i, s in enumerate(systems):
    with tabs[i]:
        iframe_url = s["url"].rstrip("/") + "/?embed=true"
        components.iframe(iframe_url, height=860, scrolling=True)

# ── 設定頁面 ──────────────────────────────────────────────
with tabs[-1]:
    st.markdown("<div style='padding-top: 24px;'>", unsafe_allow_html=True)
    st.markdown("### ⚙️ 系統清單管理")

    # ── 顯示現有系統（可編輯 / 刪除）─────────────────────
    st.markdown("**現有系統**")
    delete_index = None

    for i, s in enumerate(list(st.session_state.systems)):
        col1, col2, col3, col4 = st.columns([1, 3, 5, 1])
        with col1:
            new_icon = st.text_input("圖示", value=s["icon"], key=f"icon_{i}", label_visibility="collapsed")
        with col2:
            new_name = st.text_input("名稱", value=s["name"], key=f"name_{i}", label_visibility="collapsed")
        with col3:
            new_url = st.text_input("網址", value=s["url"], key=f"url_{i}", label_visibility="collapsed")
        with col4:
            st.markdown("<div style='margin-top:28px'>", unsafe_allow_html=True)
            if st.button("🗑", key=f"del_{i}", help="刪除此系統"):
                delete_index = i
            st.markdown("</div>", unsafe_allow_html=True)

        st.session_state.systems[i]["icon"] = new_icon
        st.session_state.systems[i]["name"] = new_name
        st.session_state.systems[i]["url"]  = new_url

    if delete_index is not None:
        st.session_state.systems.pop(delete_index)
        save_systems(st.session_state.systems)
        st.rerun()

    st.divider()

    # ── 新增系統 ─────────────────────────────────────────
    st.markdown("**＋ 新增系統**")
    col1, col2, col3, col4 = st.columns([1, 3, 5, 1])
    with col1:
        add_icon = st.text_input("圖示", value="◆", key="add_icon")
    with col2:
        add_name = st.text_input("系統名稱", key="add_name", placeholder="例：報表系統")
    with col3:
        add_url  = st.text_input("Streamlit 網址", key="add_url", placeholder="https://xxx.streamlit.app")
    with col4:
        st.markdown("<div style='margin-top:28px'>", unsafe_allow_html=True)
        add_clicked = st.button("＋ 新增")
        st.markdown("</div>", unsafe_allow_html=True)

    if add_clicked:
        if add_name and add_url:
            st.session_state.systems.append({
                "icon": add_icon or "◆",
                "name": add_name,
                "url":  add_url,
            })
            save_systems(st.session_state.systems)
            st.success(f"✅ 已新增「{add_name}」，請重新整理頁面")
            st.rerun()
        else:
            st.warning("請填寫系統名稱與網址")

    st.markdown("<div style='margin-top: 12px;'>", unsafe_allow_html=True)
    if st.button("💾 儲存所有修改", type="primary"):
        save_systems(st.session_state.systems)
        st.success("✅ 已儲存，請重新整理頁面套用變更")
    st.markdown("</div></div>", unsafe_allow_html=True)
