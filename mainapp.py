import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="內部系統總覽", page_icon="🧭", layout="wide")

ICON_OPTIONS = [
    "◆", "✦", "◈", "◉", "●", "★", "▶", "⬟", "⬡", "⬢",
    "📋", "📦", "📝", "💰", "🔧", "📊", "🗂", "🔔", "🧭", "🏠"
]

DEFAULT_SYSTEMS = [
    {"name": "新系統", "icon": "✦", "url": "https://new-system.streamlit.app"},
    {"name": "訂單系統", "icon": "◈", "url": "https://orders-system.streamlit.app"},
    {"name": "備忘系統", "icon": "◉", "url": "https://memo-system.streamlit.app"},
]

if "systems" not in st.session_state:
    st.session_state.systems = [s.copy() for s in DEFAULT_SYSTEMS]

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@400;500;600;700&family=DM+Sans:wght@400;500;600;700&display=swap');

#MainMenu, footer { visibility: hidden; }
header[data-testid="stHeader"] { background: transparent; }

.block-container {
    padding: 1.8rem 2.5rem 0 2.5rem !important;
    max-width: 100% !important;
}

[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #f6fbff 0%, #eef7f3 100%);
}

html, body, [class*="css"] {
    font-family: 'DM Sans', 'Noto Sans TC', sans-serif;
    color: #18324a;
}

.dash-header {
    display: flex;
    align-items: center;
    gap: 14px;
    margin-bottom: 20px;
}

.dash-logo {
    width: 42px;
    height: 42px;
    background: linear-gradient(135deg, #8fd3f4 0%, #84fab0 100%);
    border-radius: 14px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 21px;
    flex-shrink: 0;
    box-shadow: 0 8px 22px rgba(80, 160, 180, 0.25);
}

.dash-title {
    font-size: 22px;
    font-weight: 700;
    color: #16324f;
    letter-spacing: 0.02em;
}

.dash-sub {
    font-size: 12px;
    color: #7b8da3;
    letter-spacing: 0.14em;
    margin-left: auto;
    text-transform: uppercase;
    font-weight: 700;
}

[data-testid="stTabs"] > div:first-child {
    border-bottom: 1px solid #dbe8f3 !important;
    gap: 0 !important;
}

button[data-baseweb="tab"] {
    font-family: 'DM Sans', 'Noto Sans TC', sans-serif !important;
    font-size: 16px !important;
    font-weight: 700 !important;
    color: #6d7f91 !important;
    padding: 12px 24px !important;
    background: transparent !important;
    border: none !important;
    border-bottom: 3px solid transparent !important;
    transition: all 0.2s !important;
}

button[data-baseweb="tab"]:hover {
    color: #2f80ed !important;
    background: rgba(47, 128, 237, 0.06) !important;
}

button[aria-selected="true"][data-baseweb="tab"] {
    color: #2f80ed !important;
    border-bottom: 3px solid #2f80ed !important;
    background: transparent !important;
}

[data-testid="stTabPanel"] {
    padding: 0 !important;
}

[data-testid="stTabs"] [data-baseweb="tab-highlight"],
[data-testid="stTabs"] [data-baseweb="tab-border"] {
    display: none !important;
}

/* 右上角設定按鈕 */
[data-testid="stColumn"]:last-child [data-testid="stPopover"] button {
    background: #ffffff !important;
    border: 1px solid #d7e5f0 !important;
    color: #2f80ed !important;
    font-size: 19px !important;
    padding: 8px 11px !important;
    margin-top: 2px;
    border-radius: 12px !important;
    box-shadow: 0 6px 18px rgba(80, 120, 160, 0.12) !important;
}

[data-testid="stColumn"]:last-child [data-testid="stPopover"] button:hover {
    background: #eaf4ff !important;
    border-color: #b8d8ff !important;
}

[data-testid="stPopoverBody"] {
    background: #ffffff !important;
    border: 1px solid #d7e5f0 !important;
    border-radius: 18px !important;
    padding: 18px !important;
    min-width: 660px !important;
    box-shadow: 0 18px 45px rgba(70, 100, 130, 0.18) !important;
}

[data-testid="stPopoverBody"] h5 {
    color: #16324f !important;
    font-size: 22px !important;
    font-weight: 800 !important;
}

[data-testid="stPopoverBody"] [data-testid="stTextInput"] input {
    background: #f7fbff !important;
    border: 1px solid #cfddea !important;
    border-radius: 10px !important;
    color: #18324a !important;
    font-size: 16px !important;
    font-weight: 600 !important;
}

[data-testid="stPopoverBody"] [data-testid="stSelectbox"] > div > div {
    background: #f7fbff !important;
    border: 1px solid #cfddea !important;
    border-radius: 10px !important;
    color: #18324a !important;
    font-size: 16px !important;
    font-weight: 600 !important;
}

[data-testid="stButton"] button {
    background: #eaf4ff !important;
    border: 1px solid #b8d8ff !important;
    color: #1f6fd1 !important;
    border-radius: 10px !important;
    font-size: 15px !important;
    font-weight: 800 !important;
    font-family: 'DM Sans', 'Noto Sans TC', sans-serif !important;
    transition: all 0.18s !important;
}

[data-testid="stButton"] button:hover {
    background: #d8ecff !important;
    border-color: #5aa9ff !important;
}

hr {
    border-color: #dbe8f3 !important;
    margin: 12px 0 !important;
}
</style>
""", unsafe_allow_html=True)

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
                new_icon = st.selectbox(
                    "圖示",
                    ICON_OPTIONS,
                    index=icon_idx,
                    key=f"icon_{i}",
                    label_visibility="collapsed"
                )

            with c2:
                new_name = st.text_input(
                    "名稱",
                    value=sys["name"],
                    key=f"name_{i}",
                    label_visibility="collapsed"
                )

            with c3:
                new_url = st.text_input(
                    "網址",
                    value=sys["url"],
                    key=f"url_{i}",
                    label_visibility="collapsed"
                )

            with c4:
                st.markdown("<div style='height:4px'></div>", unsafe_allow_html=True)
                if st.button("✕", key=f"del_{i}", help="刪除"):
                    to_delete = i

            temp_systems.append({
                "name": new_name.strip(),
                "icon": new_icon,
                "url": new_url.strip()
            })

        if to_delete is not None:
            temp_systems.pop(to_delete)
            st.session_state.systems = temp_systems
            st.rerun()

        st.markdown("<hr>", unsafe_allow_html=True)

        c1, c2, c3, c4 = st.columns([1.2, 2.5, 5, 1])

        with c1:
            add_icon = st.selectbox(
                "新增圖示",
                ICON_OPTIONS,
                index=0,
                key="add_icon",
                label_visibility="collapsed"
            )

        with c2:
            add_name = st.text_input(
                "新增名稱",
                placeholder="系統名稱",
                key="add_name",
                label_visibility="collapsed"
            )

        with c3:
            add_url = st.text_input(
                "新增網址",
                placeholder="https://xxx.streamlit.app",
                key="add_url",
                label_visibility="collapsed"
            )

        with c4:
            st.markdown("<div style='height:4px'></div>", unsafe_allow_html=True)
            if st.button("＋", key="add_btn", help="新增"):
               if add_name.strip() and add_url.strip():
                   temp_systems.append({
                       "name": add_name.strip(),
                       "icon": add_icon,
                       "url": add_url.strip()
                   })
                   st.session_state.systems = temp_systems
                   st.rerun()
               else:
                   st.warning("請填入名稱和網址")

        st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True)

        if st.button("💾  儲存修改", key="save_btn"):
           if add_name.strip() and add_url.strip():
               temp_systems.append({
                   "name": add_name.strip(),
                   "icon": add_icon,
                   "url": add_url.strip()
               })

           st.session_state.systems = temp_systems
           st.success("✅ 已儲存！")
           st.rerun()

if tab_labels:
    for tab, sys in zip(tabs, systems):
        with tab:
            url = sys["url"].rstrip("/") + "/?embed=true"
            components.iframe(url, height=860, scrolling=True)
