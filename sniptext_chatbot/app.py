import time
import streamlit as st
from dotenv import load_dotenv

from config.settings import APP_NAME, SUGGESTED_QUESTIONS
from core.chain import generate_answer
from core.vectorstore import rebuild_vectorstore
from ui.layout import check_admin_password, render_admin_panel
from ui.styles import inject_custom_css

load_dotenv()

st.set_page_config(
    page_title=APP_NAME,
    page_icon="🤖",
    layout="wide"
)

st.markdown(inject_custom_css(), unsafe_allow_html=True)

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "pending_question" not in st.session_state:
    st.session_state.pending_question = None
if "admin_authenticated" not in st.session_state:
    st.session_state.admin_authenticated = False
if "active_tab" not in st.session_state:
    st.session_state.active_tab = "chat"


def render_user_message(text):
    """Question on RIGHT side, sky blue bubble, with avatar"""
    safe_text = text.replace('<', '&lt;').replace('>', '&gt;')
    _, right_col = st.columns([0.2, 0.8])
    with right_col:
        st.markdown(
            f"""
            <div style="display:flex;align-items:flex-start;gap:8px;
                        justify-content:flex-end;margin:0.5rem 0;">
                <div style="background:#3B82F6;color:#fff;
                            border-radius:18px 4px 18px 18px;
                            padding:0.7rem 1.1rem;font-size:0.93rem;
                            line-height:1.65;
                            box-shadow:0 4px 14px rgba(59,130,246,0.22);
                            word-wrap:break-word;">
                    {safe_text}
                </div>
                <div style="width:32px;height:32px;border-radius:50%;
                            background:#1D4ED8;display:flex;align-items:center;
                            justify-content:center;font-size:1rem;flex-shrink:0;
                            box-shadow:0 2px 8px rgba(29,78,216,0.3);">👤</div>
            </div>
            """,
            unsafe_allow_html=True
        )

def render_assistant_message(text, related_link=None):
    """Answer on LEFT side, white card, with 🤖 avatar to the left"""
    try:
        import markdown as mdlib
        html_text = mdlib.markdown(text, extensions=["nl2br"])
    except ImportError:
        html_text = text.replace('\n\n', '<br><br>').replace('\n', '<br>')

    link_html = ""
    if related_link:
        link_html = (
            f'<div class="related-link-box">'
            f'🔗&nbsp;<a class="related-link" href="{related_link}" '
            f'target="_blank">{related_link}</a></div>'
        )

    avatar_col, answer_col, _ = st.columns([0.06, 0.74, 0.20])

    with avatar_col:
        st.markdown(
            '<div style="width:34px;height:34px;border-radius:50%;'
            'background:linear-gradient(135deg,#1D4ED8,#3B82F6);'
            'display:flex;align-items:center;justify-content:center;'
            'font-size:1.1rem;margin-top:0.5rem;'
            'box-shadow:0 2px 8px rgba(29,78,216,0.25);">🤖</div>',
            unsafe_allow_html=True
        )

    with answer_col:
        st.markdown(
            f'<div style="background:#FFFFFF;border:1px solid #E5E7EB;'
            f'border-radius:4px 18px 18px 18px;padding:0.9rem 1.15rem;'
            f'box-shadow:0 4px 18px rgba(0,0,0,0.07);margin:0.5rem 0;'
            f'font-size:0.93rem;line-height:1.72;color:#1F2937;">'
            f'{html_text}{link_html}</div>',
            unsafe_allow_html=True
        )

# ── Sidebar ────────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown(
        f"""
        <div class="brand-header">
            <div class="brand-logo">🤖</div>
            <div class="brand-title">{APP_NAME}</div>
            <div class="brand-subtitle">Ask anything about the website</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown('<div class="section-header">Navigation</div>', unsafe_allow_html=True)

    if st.button("💬  Chat", use_container_width=True, key="nav_chat"):
        st.session_state.active_tab = "chat"
        st.rerun()

    if st.button("⚙️  Admin Panel", use_container_width=True, key="nav_admin"):
        st.session_state.active_tab = "admin"
        st.rerun()

    st.markdown("---")

    if st.button("🗑️  Clear conversation", use_container_width=True, key="clear_chat_btn"):
        st.session_state.chat_history = []
        st.session_state.pending_question = None
        st.rerun()

    st.markdown(
        '<div style="margin-top:1.5rem;font-size:0.7rem;'
        'color:rgba(255,255,255,0.4);text-align:center;">Powered by CheckAI</div>',
        unsafe_allow_html=True
    )


# ── Chat page ──────────────────────────────────────────────────────────────────
if st.session_state.active_tab == "chat":

    if not st.session_state.chat_history:
        st.markdown(
            """
            <div class="empty-state">
                <div class="empty-state-icon">🤖</div>
                <div class="empty-state-title">Ask anything about the website</div>
                <div class="empty-state-subtitle">
                    This assistant answers questions based on indexed website pages.
                    Try asking about features, pricing, free tools, contact info, or anything else.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    # Suggestions always visible
    if SUGGESTED_QUESTIONS:
        st.markdown(
            '<div style="font-size:0.72rem;font-weight:700;color:#6B7280;'
            'letter-spacing:0.09em;text-transform:uppercase;text-align:center;'
            'margin-bottom:0.3rem;">Try asking</div>',
            unsafe_allow_html=True
        )
        cols = st.columns(len(SUGGESTED_QUESTIONS))
        for i, question in enumerate(SUGGESTED_QUESTIONS):
            with cols[i]:
                if st.button(f"💬 {question}", use_container_width=True, key=f"suggestion_{i}"):
                    st.session_state.pending_question = question
                    st.rerun()

    # Render chat history
    for msg in st.session_state.chat_history:
        if msg["role"] == "user":
            render_user_message(msg["content"])
        else:
            render_assistant_message(msg["content"], msg.get("related_link"))

    # Chat input
    user_question = st.chat_input("Ask something about the website...")

    if st.session_state.pending_question and not user_question:
        user_question = st.session_state.pending_question
        st.session_state.pending_question = None

    if user_question:
        st.session_state.chat_history.append({"role": "user", "content": user_question})
        render_user_message(user_question)

        # Generate — hide internal tool messages
        gen_container = st.empty()
        with gen_container.container():
            with st.spinner("Thinking..."):
                answer, related_link = generate_answer(
                    user_question=user_question,
                    chat_history=st.session_state.chat_history[:-1]
                )
        gen_container.empty()

        # Stream word by word in the left column, then show final answer
        left_col, _ = st.columns([0.8, 0.2])
        with left_col:
            stream_placeholder = st.empty()
            words = answer.split()
            displayed = ""
            for i, word in enumerate(words):
                displayed += ("" if i == 0 else " ") + word
                stream_placeholder.markdown(
                    f'<div style="background:#FFFFFF;border:1px solid #E5E7EB;'
                    f'border-radius:4px 18px 18px 18px;padding:0.9rem 1.15rem;'
                    f'box-shadow:0 4px 18px rgba(0,0,0,0.07);margin:0.5rem 0;'
                    f'font-size:0.93rem;line-height:1.72;color:#1F2937;">'
                    f'{displayed} <span style="color:#3B82F6;font-weight:700;">▌</span></div>',
                    unsafe_allow_html=True
                )
                time.sleep(0.022)
            stream_placeholder.empty()

        render_assistant_message(answer, related_link)

        st.session_state.chat_history.append({
            "role": "assistant",
            "content": answer,
            "related_link": related_link
        })


# ── Admin page ─────────────────────────────────────────────────────────────────
elif st.session_state.active_tab == "admin":
    st.markdown(
        '<h2 style="color:#1F2937;font-weight:800;margin-bottom:1.4rem;">⚙️ Admin Panel</h2>',
        unsafe_allow_html=True
    )

    if not st.session_state.admin_authenticated:
        st.markdown(
            '<div class="admin-section">'
            '<div class="admin-section-title">Authentication Required</div>',
            unsafe_allow_html=True
        )
        password = st.text_input(
            "Password",
            type="password",
            placeholder="Enter admin password...",
            key="admin_password_input",
            label_visibility="collapsed"
        )
        if st.button("🔓  Unlock Admin Panel", key="admin_login_btn"):
            if check_admin_password(password):
                st.success("Access granted.")
                st.rerun()
            else:
                st.error("Incorrect password.")
        st.markdown("</div>", unsafe_allow_html=True)

    else:
        col_status, col_logout = st.columns([5, 1])
        with col_status:
            st.markdown(
                '<div style="color:#166534;background:#F0FDF4;border:1px solid #BBF7D0;'
                'border-radius:10px;padding:0.5rem 0.9rem;font-size:0.87rem;font-weight:500;'
                'margin-bottom:1rem;display:inline-block;">✅ Authenticated as admin</div>',
                unsafe_allow_html=True
            )
        with col_logout:
            if st.button("🔒 Logout", key="logout_btn"):
                st.session_state.admin_authenticated = False
                st.rerun()

        rebuild_clicked = render_admin_panel()

        if rebuild_clicked:
            with st.spinner("Rebuilding knowledge base from website..."):
                rebuild_vectorstore()
            st.success("Index rebuilt successfully.")
            st.rerun()
