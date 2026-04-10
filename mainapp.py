import streamlit as st
import streamlit.components.v1 as components
import json, os

st.set_page_config(page_title="內部系統總覽", page_icon="🧭", layout="wide")

SYSTEMS_FILE = "systems.json"
DEFAULT_SYSTEMS = [
    {"name": "新系統",   "icon": "✦", "url": "https://new-system.streamlit.app"},
    {"name": "訂單系統", "icon": "◈", "url": "https://orders-system.streamlit.app"},
    {"name": "備忘系統", "icon": "◉", "url": "https://memo-system.streamlit.app"},
]

def load_systems():
    if os.path.exists(SYSTEMS_FILE):
        with open(SYSTEMS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return DEFAULT_SYSTEMS

def save_systems(systems):
    with open(SYSTEMS_FILE, "w", encoding="utf-8") as f:
        json.dump(systems, f, ensure_ascii=False, indent=2)

if "systems" not in st.session_state:
    st.session_state.systems = load_systems()

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@300;400;500;600&family=DM+Sans:opsz,wght@9..40,300;9..40,400;9..40,500;9..40,600&display=swap');

#MainMenu, footer { visibility: hidden; }
header[data-testid="stHeader"] { background: transparent; }
.block-container { padding: 1.8rem 2.5rem 0 2.5rem !important; max-width: 100% !important; }

/* 整體背景：深藍灰，不要純黑 */
[data-testid="stAppViewContainer"] { background: #1b1f2e; }
html, body, [class*="css"] {
    font-family: 'DM Sans', 'Noto Sans TC', sans-serif;
    color: #dde1ee;
}

/* Header */
.dash-header { display: flex; align-items: center; gap: 12px; margin-bottom: 22px; }
.dash-logo {
    width: 36px; height: 36px;
    background: linear-gradient(135deg, #6c8fff 0%, #a78bfa 100%);
    border-radius: 9px; display: flex; align-items: center; justify-content: center;
    font-size: 18px; flex-shrink: 0; box-shadow: 0 4px 14px rgba(108,143,255,0.3);
}
.dash-title { font-size: 18px; font-weight: 600; color: #eef0f8; letter-spacing: 0.02em; }
.dash-sub { font-size: 11px; color: #4e5470; letter-spacing: 0.1em; margin-left: auto; text-transform: uppercase; }

/* Tabs */
[data-testid="stTabs"] > div:first-child {
    border-bottom: 1px solid rgba(255,255,255,0.1) !important;
    gap: 0 !important;
}
button[data-baseweb="tab"] {
    font-family: 'DM Sans', 'Noto Sans TC', sans-serif !important;
    font-size: 13.5px !important; font-weight: 400 !important;
    color: #6b7290 !important; padding: 10px 22px !important;
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

/* Expander */
[data-testid="stExpander"] {
    background: #222638 !important;
    border: 1px solid rgba(255,255,255,0.09) !important;
    border-radius: 10px !important; margin-bottom: 18px;
}
[data-testid="stExpander"] summary {
    color: #8892b0 !important; font-size: 13px !important;
}
[data-testid="stExpander"] summary:hover { color: #b0b8d4 !important; }

/* Input 欄位 - 關鍵修正 */
[data-testid="stTextInput"] input {
    background: #2a2f45 !important;
    border: 1px solid rgba(255,255,255,0.12) !important;
    border-radius: 7px !important;
    color: #eef0f8 !important;          /* 白色文字 */
    font-size: 13.5px !important;
    font-family: 'DM Sans', 'Noto Sans TC', sans-serif !important;
    caret-color: #8ba4ff !important;
}
[data-testid="stTextInput"] input::placeholder {
    color: #4a5070 !important;          /* placeholder 明顯一點 */
}
[data-testid="stTextInput"] input:focus {
    border-color: #6c8fff !important;
    box-shadow: 0 0 0 2px rgba(108,143,255,0.2) !important;
}
[data-testid="stTextInput"] label { color: #6b7290 !important; font-size: 11.5px !important; }

/* 按鈕 */
[data-testid="stButton"] button {
    background: #2a2f45 !important;
    border: 1px solid rgba(255,255,255,0.11) !important;
    color: #8ba4ff !important; border-radius: 7px !important;
    font-size: 13px !important;
    font-family: 'DM Sans', 'Noto Sans TC', sans-serif !important;
    transition: all 0.18s !important;
}
[data-testid="stButton"] button:hover {
    background: #313759 !important; border-color: #6c8fff !important;
    color: #adc0ff !important;
}

/* Success / warning */
[data-testid="stAlert"] { border-radius: 8px !important; font-size: 13px !important; }

hr { border-color: rgba(255,255,255,0.08) !important; margin: 12px 0 !important; }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="dash-header">
    <div class="dash-logo">🧭</div>
    <span class="dash-title">內部系統總覽</span>
    <span class="dash-sub">Internal Dashboard</span>
</div>
""", unsafe_allow_html=True)

# ── 系統管理 ──────────────────────────────────────────────
with st.expander("⚙️  管理系統清單", expanded=False):
    systems = st.session_state.systems
    st.markdown("<div style='height:4px'></div>", unsafe_allow_html=True)

    for i, sys in enumerate(systems):
        col1, col2, col3, col4 = st.columns([1, 3, 6, 1])
        with col1:
            new_icon = st.text_input("圖示", value=sys["icon"], key=f"icon_{i}", label_visibility="collapsed")
        with col2:
            new_name = st.text_input("名稱", value=sys["name"], key=f"name_{i}", label_visibility="collapsed")
        with col3:
            new_url  = st.text_input("網址", value=sys["url"],  key=f"url_{i}",  label_visibility="collapsed")
        with col4:
            st.markdown("<div style='height:4px'></div>", unsafe_allow_html=True)
            if st.button("✕", key=f"del_{i}", help="刪除此系統"):
                systems.pop(i)
                save_systems(systems)
                st.rerun()
        systems[i] = {"name": new_name, "icon": new_icon, "url": new_url}

    st.markdown("<hr>", unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns([1, 3, 6, 1])
    with c1:
        add_icon = st.text_input("圖示", value="◆", key="add_icon", label_visibility="collapsed")
    with c2:
        add_name = st.text_input("名稱", placeholder="系統名稱", key="add_name", label_visibility="collapsed")
    with c3:
        add_url  = st.text_input("網址", placeholder="https://xxx.streamlit.app", key="add_url", label_visibility="collapsed")
    with c4:
        st.markdown("<div style='height:4px'></div>", unsafe_allow_html=True)
        if st.button("＋", key="add_btn", help="新增系統"):
            if add_name and add_url:
                systems.append({"name": add_name, "icon": add_icon, "url": add_url})
                save_systems(systems)
                st.rerun()
            else:
                st.warning("請填入名稱和網址")

    if st.button("💾  儲存修改", key="save_btn"):
        save_systems(systems)
        st.session_state.systems = systems
        st.success("已儲存！")
        st.rerun()

# ── Tabs + iframe ─────────────────────────────────────────
systems = st.session_state.systems

if not systems:
    st.info("尚未設定任何系統，請展開上方「管理系統清單」新增。")
else:
    tab_labels = [f"{s['icon']}  {s['name']}" for s in systems]
    tabs = st.tabs(tab_labels)
    for tab, sys in zip(tabs, systems):
        with tab:
            iframe_url = sys["url"].rstrip("/") + "/?embed=true"
            components.iframe(iframe_url, height=860, scrolling=True)
