import streamlit as st
from config.settings import APP_NAME, APP_TAGLINE, SUGGESTED_QUESTIONS
from ui.components import render_suggestions, render_index_meta
from core.utils import load_urls, load_index_meta, add_url, remove_url


def render_header():
    st.markdown(
        f"""
        <div class="brand-header">
            <div class="brand-title">🤖 {APP_NAME}</div>
            <div class="brand-subtitle">{APP_TAGLINE}</div>
        </div>
        """,
        unsafe_allow_html=True
    )


def render_sidebar():
    with st.sidebar:
        st.title("Assistant Panel")

        st.markdown("### About")
        st.write("This chatbot answers using only the indexed website content.")

        meta = load_index_meta()
        render_index_meta(meta)

        st.markdown("### Manage URLs")
        urls = load_urls()

        new_url = st.text_input("Add a new URL")
        add_clicked = st.button("Add URL", use_container_width=True)

        if add_clicked and new_url.strip():
            add_url(new_url.strip())
            st.success("URL added. Rebuild index now.")
            st.rerun()

        if urls:
            st.markdown("### Current URLs")
            for idx, url in enumerate(urls):
                col1, col2 = st.columns([4, 1])
                with col1:
                    st.markdown(f'<div class="url-item">{url}</div>', unsafe_allow_html=True)
                with col2:
                    if st.button("❌", key=f"remove_{idx}"):
                        remove_url(url)
                        st.success("URL removed. Rebuild index now.")
                        st.rerun()

        st.markdown("### Actions")
        clear = st.button("🗑️ Clear chat", use_container_width=True)
        rebuild = st.button("🔄 Rebuild index", use_container_width=True)

        st.markdown("### Good Questions")
        for q in SUGGESTED_QUESTIONS:
            st.markdown(f"- {q}")

        return clear, rebuild


def render_home_suggestions():
    return render_suggestions(SUGGESTED_QUESTIONS)