import os
import streamlit as st
from dotenv import load_dotenv

from ui.components import render_index_meta, render_url_item
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


def check_admin_password(entered_password=None):
    if entered_password is None:
        return st.session_state.get("admin_authenticated", False)
    real_password = os.getenv("ADMIN_PASSWORD", "")
    if entered_password == real_password and entered_password.strip():
        st.session_state.admin_authenticated = True
        return True
    return False


def render_public_sidebar():
    clear = False
    show_admin_login = False
    if st.session_state.get("active_tab") == "chat" and st.session_state.get("chat_history"):
        if st.button("🗑️  Clear conversation", use_container_width=True, key="clear_chat_btn"):
            clear = True
    return clear, show_admin_login


def render_admin_panel():
    meta = load_index_meta()
    render_index_meta(meta)

    st.markdown("---")

    # ---- Add new URL ----
    st.markdown(
        '<div class="admin-section">'
        '<div class="admin-section-title">Add New URL</div>',
        unsafe_allow_html=True
    )
    new_url = st.text_input(
        "URL",
        placeholder="https://example.com/page",
        key="admin_add_url",
        label_visibility="collapsed"
    )
    col_add, col_restore = st.columns([1, 1])
    with col_add:
        if st.button("➕  Add URL", use_container_width=True, key="add_url_btn"):
            if new_url.strip():
                add_url(new_url.strip())
                st.success("URL added. Rebuild the index to apply.")
                st.rerun()
            else:
                st.warning("Please enter a valid URL.")
    with col_restore:
        if st.button("↩️  Restore Defaults", use_container_width=True, key="restore_defaults_btn"):
            restore_default_urls()
            st.success("Default site URLs restored.")
            st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

    # ---- Active URLs ----
    urls = load_urls()
    removed_urls = load_removed_urls()

    st.markdown(
        '<div class="admin-section">'
        f'<div class="admin-section-title">Active URLs ({len(urls)})</div>',
        unsafe_allow_html=True
    )
    if urls:
        for idx, url in enumerate(urls):
            col1, col2 = st.columns([5, 1])
            with col1:
                render_url_item(url)
            with col2:
                st.markdown("<div style='padding-top:6px;'></div>", unsafe_allow_html=True)
                if st.button("❌", key=f"remove_{idx}", help="Remove URL"):
                    remove_url(url)
                    st.success("URL removed.")
                    st.rerun()
    else:
        st.markdown(
            '<p style="color:#6B7280;font-size:0.88rem;">No active URLs found.</p>',
            unsafe_allow_html=True
        )
    st.markdown("</div>", unsafe_allow_html=True)

    # ---- Removed URLs ----
    if removed_urls:
        st.markdown(
            f'<div class="admin-section">'
            f'<div class="admin-section-title">Removed URLs ({len(removed_urls)})</div>',
            unsafe_allow_html=True
        )
        for idx, url in enumerate(removed_urls):
            col1, col2 = st.columns([5, 1])
            with col1:
                render_url_item(url, removed=True)
            with col2:
                st.markdown("<div style='padding-top:6px;'></div>", unsafe_allow_html=True)
                if st.button("↩️", key=f"restore_{idx}", help="Restore URL"):
                    restore_removed_url(url)
                    st.success("URL restored.")
                    st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

    # ---- Rebuild index ----
    st.markdown("")
    rebuild = st.button(
        "🔄  Rebuild Knowledge Index",
        use_container_width=True,
        key="rebuild_btn"
    )

    return rebuild