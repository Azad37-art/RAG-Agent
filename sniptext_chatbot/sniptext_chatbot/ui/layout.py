import os
import streamlit as st
from dotenv import load_dotenv

from ui.components import render_index_meta
from core.utils import (
    load_urls,
    load_removed_urls,
    load_index_meta,
    add_url,
    remove_url,
    restore_removed_url,
    restore_default_urls,
)

load_dotenv()


def check_admin_password():
    if "admin_authenticated" not in st.session_state:
        st.session_state.admin_authenticated = False

    entered_password = st.text_input(
        "Enter admin password",
        type="password",
        key="admin_password_input"
    )

    if st.button("Login to Admin Dashboard", use_container_width=True, key="admin_login_btn"):
        real_password = os.getenv("ADMIN_PASSWORD", "")
        if entered_password == real_password and entered_password.strip():
            st.session_state.admin_authenticated = True
            st.success("Admin access granted.")
            st.rerun()
        else:
            st.error("Incorrect password.")

    return st.session_state.admin_authenticated


def render_public_sidebar():
    with st.sidebar:
        st.title("Assistant Panel")
        st.write("Ask questions about the indexed website content.")

        clear = st.button("🗑️ Clear chat", use_container_width=True, key="clear_chat_btn")

        st.markdown("---")
        st.markdown("### Admin Access")
        show_admin_login = st.checkbox("Open Admin Dashboard")

        return clear, show_admin_login


def render_admin_panel():
    with st.sidebar:
        st.markdown("---")
        st.markdown("## Admin Dashboard")

        meta = load_index_meta()
        render_index_meta(meta)

        st.markdown("### Add New URL")
        new_url = st.text_input("Add a new URL", key="admin_add_url")
        add_clicked = st.button("Add URL", use_container_width=True, key="add_url_btn")

        if add_clicked and new_url.strip():
            add_url(new_url.strip())
            st.success("URL added. Rebuild index now.")
            st.rerun()

        restore_defaults_clicked = st.button(
            "Restore Default Site URLs",
            use_container_width=True,
            key="restore_defaults_btn"
        )
        if restore_defaults_clicked:
            restore_default_urls()
            st.success("Default site URLs restored.")
            st.rerun()

        urls = load_urls()
        removed_urls = load_removed_urls()

        st.markdown("### Current Active URLs")
        if urls:
            for idx, url in enumerate(urls):
                col1, col2 = st.columns([4, 1])
                with col1:
                    st.markdown(
                        f'<div class="url-item"><span class="url-text">{url}</span></div>',
                        unsafe_allow_html=True
                    )
                with col2:
                    if st.button("❌", key=f"remove_{idx}"):
                        remove_url(url)
                        st.success("URL moved to removed list.")
                        st.rerun()
        else:
            st.info("No active URLs found.")

        st.markdown("### Removed URLs")
        if removed_urls:
            for idx, url in enumerate(removed_urls):
                col1, col2 = st.columns([4, 1])
                with col1:
                    st.markdown(
                        f'<div class="url-item removed-url"><span class="url-text">{url}</span></div>',
                        unsafe_allow_html=True
                    )
                with col2:
                    if st.button("↩️", key=f"restore_{idx}"):
                        restore_removed_url(url)
                        st.success("URL restored to active list.")
                        st.rerun()
        else:
            st.info("No removed URLs.")

        rebuild = st.button("🔄 Rebuild index", use_container_width=True, key="rebuild_btn")
        logout = st.button("🚪 Logout Admin", use_container_width=True, key="logout_btn")

        if logout:
            st.session_state.admin_authenticated = False
            st.rerun()

        return rebuild