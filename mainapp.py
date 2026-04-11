import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="內部系統總覽", page_icon="🧭", layout="wide")

# ── 圖示選項 ──────────────────────────────────────────────
ICON_OPTIONS = ["◆", "✦", "◈", "◉", "●", "★", "▶", "⬟", "⬡", "⬢",
                "📋", "📦", "📝", "💰", "🔧", "📊", "🗂", "🔔", "🧭", "🏠"]

# ── 預設系統清單（永久保存靠這裡，不依賴檔案系統）─────────
DEFAULT_SYSTEMS = [
    {"name": "新系統",   "icon": "✦", "url": "https://new-system.streamlit.app"},
    {"name": "訂單系統", "icon": "◈", "url": "https://orders-system.streamlit.app"},
    {"name": "備忘系統", "icon": "◉", "url": "https://memo-system.streamlit.app"},
]

if "systems" not in st.session_state:
    st.session_state.systems = [s.copy() for s in DEFAULT_SYSTEMS]

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@300;400;500;600&family=DM+Sans:opsz,wght@9..40,300;9..40,400;9..40,500;9..40,600&display=swap');

#MainMenu, footer { visibility: hidden; }
header[data-testid="stHeader"] { background: transparent; }
.block-container { padding: 1.8rem 2.5rem 0 2.5rem !important; max-width: 100% !important; }
[data-testid="stAppViewContainer"] { background: #1b1f2e; }
html, body, [class*="css"] { font-family: 'DM Sans', 'Noto Sans TC', sans-serif; }

.dash-header { display: flex; align-items: center; gap: 12px; margin-bottom: 18px; }
.dash-logo {
    width: 34px; height: 34px;
    background: linear-gradient(135deg, #6c8fff 0%, #a78bfa 100%);
    border-radius: 9px; display: flex; align-items: center; justify-content: center;
    font-size: 17px; flex-shrink: 0; box-shadow: 0 4px 12px rgba(108,143,255,0.3);
}
.dash-title { font-size: 17px; font-weight: 600; color: #eef0f8; letter-spacing: 0.02em; }
.dash-sub { font-size: 11px; color: #4e5470; letter-spacing: 0.1em; margin-left: auto; text-transform: uppercase; }

[data-testid="stTabs"] > div:first-child {
    border-bottom: 1px solid rgba(255,255,255,0.1) !important; gap: 0 !important;
}
button[data-baseweb="tab"] {
    font-family: 'DM Sans', 'Noto Sans TC', sans-serif !important;
    font-size: 13.5px !important; font-weight: 400 !important;
    color: #6b7290 !important; padding: 10px 20px !important;
    background: transparent !important; border: none !important;
    border-bottom: 2px solid transparent !important; transition: all 0.2s !important;
}
button[data-baseweb="tab"]:hover { color: #b0b8d4 !important; background: rgba(255,255,255,0.04) !important; }
button[aria-selected="true"][data-baseweb="tab"] {
    color: #8ba4ff !important; font-weight: 500 !important;
    border-bottom: 2px solid #8ba4ff !important; background: transparent !important;
}
[data-testid="stTabPanel"] { padding: 0 !important; }
[data-testid="stTabs"] [data-baseweb="tab-highlight"],
[data-testid="stTabs"] [data-baseweb="tab-border"] { display: none !important; }

/* Popover 按鈕 */
[data-testid="stColumn"]:last-child [data-testid="stPopover"] button {
    background: transparent !important; border: none !important;
    color: #4e5470 !important; font-size: 17px !important;
    padding: 8px 10px !important; margin-top: 4px;
    transition: color 0.2s !important;
}
[data-testid="stColumn"]:last-child [data-testid="stPopover"] button:hover {
    color: #8ba4ff !important;
    background: rgba(139,164,255,0.08) !important;
    border-radius: 7px !important;
}
[data-testid="stPopoverBody"] {
    background: #222638 !important;
    border: 1px solid rgba(255,255,255,0.1) !important;
    border-radius: 12px !important;
    padding: 16px !important;
    min-width: 600px !important;
}

/* Input & select 在 popover 裡 */
[data-testid="stPopoverBody"] [data-testid="stTextInput"] input {
    background: #2a2f45 !important;
    border: 1px solid rgba(255,255,255,0.12) !important;
    border-radius: 6px !important;
    color: #eef0f8 !important;
    font-size: 13px !important;
}
[data-testid="stPopoverBody"] [data-testid="stSelectbox"] > div > div {
    background: #2a2f45 !important;
    border: 1px solid rgba(255,255,255,0.12) !important;
    border-radius: 6px !important;
    color: #eef0f8 !important;
    font-size: 15px !important;
}

[data-testid="stButton"] button {
    background: #2a2f45 !important; border: 1px solid rgba(255,255,255,0.11) !important;
    color: #8ba4ff !important; border-radius: 7px !important; font-size: 13px !important;
    font-family: 'DM Sans', 'Noto Sans TC', sans-serif !important; transition: all 0.18s !important;
}
[data-testid="stButton"] button:hover { background: #313759 !important; border-color: #6c8fff !important; }

hr { border-color: rgba(255,255,255,0.08) !important; margin: 10px 0 !important; }
</style>
""", unsafe_allow_html=True)

# ── Header ────────────────────────────────────────────────
st.markdown("""
<div class="dash-header">
    <div class="dash-logo">🧭</div>
    <span class="dash-title">內部系統總覽</span>
    <span class="dash-sub">Internal Dashboard</span>
</div>
""", unsafe_allow_html=True)

systems = st.session_state.systems
tab_labels = [f"{s['icon']}  {s['name']}" for s in systems] if systems else []

col_tabs, col_gear = st.columns([11, 1])

with col_tabs:
    if tab_labels:
        tabs = st.tabs(tab_labels)
    else:
        st.info("尚未設定任何系統，請點右側 ⚙️ 新增。")

with col_gear:
    with st.popover("⚙️", help="管理系統清單"):
        st.markdown("##### 系統清單")

        to_delete = None
        temp_systems = []

        for i, sys in enumerate(systems):
            c1, c2, c3, c4 = st.columns([1.2, 2.5, 5, 1])
            with c1:
                icon_idx = ICON_OPTIONS.index(sys["icon"]) if sys["icon"] in ICON_OPTIONS else 0
                new_icon = st.selectbox("圖示", ICON_OPTIONS, index=icon_idx,
                                        key=f"icon_{i}", label_visibility="collapsed")
            with c2:
                new_name = st.text_input("名稱", value=sys["name"],
                                         key=f"name_{i}", label_visibility="collapsed")
            with c3:
                new_url = st.text_input("網址", value=sys["url"],
                                        key=f"url_{i}", label_visibility="collapsed")
            with c4:
                st.markdown("<div style='height:4px'></div>", unsafe_allow_html=True)
                if st.button("✕", key=f"del_{i}", help="刪除"):
                    to_delete = i

            temp_systems.append({"name": new_name, "icon": new_icon, "url": new_url})

        if to_delete is not None:
            temp_systems.pop(to_delete)
            st.session_state.systems = temp_systems
            st.rerun()

        st.markdown("<hr>", unsafe_allow_html=True)

        # 新增列
        c1, c2, c3, c4 = st.columns([1.2, 2.5, 5, 1])
        with c1:
            add_icon = st.selectbox("圖示", ICON_OPTIONS, index=0,
                                    key="add_icon", label_visibility="collapsed")
        with c2:
            add_name = st.text_input("", placeholder="系統名稱",
                                     key="add_name", label_visibility="collapsed")
        with c3:
            add_url = st.text_input("", placeholder="https://xxx.streamlit.app",
                                    key="add_url", label_visibility="collapsed")
        with c4:
            st.markdown("<div style='height:4px'></div>", unsafe_allow_html=True)
            if st.button("＋", key="add_btn"):
                if add_name and add_url:
                    temp_systems.append({"name": add_name, "icon": add_icon, "url": add_url})
                    st.session_state.systems = temp_systems
                    st.rerun()
                else:
                    st.warning("請填入名稱和網址")

        st.markdown("<div style='height:6px'></div>", unsafe_allow_html=True)
        if st.button("💾  儲存修改", key="save_btn"):
            st.session_state.systems = temp_systems
            st.success("✅ 已儲存！")
            st.rerun()

# ── iframe ────────────────────────────────────────────────
if tab_labels:
    for tab, sys in zip(tabs, systems):
        with tab:
            url = sys["url"].rstrip("/") + "/?embed=true"
            components.iframe(url, height=860, scrolling=True)
