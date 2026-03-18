import streamlit as st
from dotenv import load_dotenv

from config.settings import APP_NAME, APP_ICON
from core.chain import generate_answer
from core.vectorstore import rebuild_vectorstore
from ui.layout import render_header, render_sidebar, render_home_suggestions
from ui.components import render_empty_state, render_answer_card
from ui.styles import inject_custom_css

load_dotenv()

st.set_page_config(
    page_title=APP_NAME,
    page_icon=APP_ICON,
    layout="wide"
)

st.markdown(inject_custom_css(), unsafe_allow_html=True)

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "pending_question" not in st.session_state:
    st.session_state.pending_question = None

clear_clicked, rebuild_clicked = render_sidebar()

if clear_clicked:
    st.session_state.chat_history = []
    st.session_state.pending_question = None
    st.rerun()

if rebuild_clicked:
    with st.spinner("Rebuilding vector index..."):
        rebuild_vectorstore()
    st.success("Index rebuilt successfully.")
    st.rerun()

render_header()

if not st.session_state.chat_history:
    render_empty_state()
    selected_prompt = render_home_suggestions()
    if selected_prompt:
        st.session_state.pending_question = selected_prompt
        st.rerun()

for msg in st.session_state.chat_history:
    with st.chat_message(msg["role"]):
        if msg["role"] == "assistant":
            render_answer_card(msg["content"], msg.get("sources", []))
        else:
            st.markdown(msg["content"])

user_question = st.chat_input("Ask something about the website...")

if st.session_state.pending_question and not user_question:
    user_question = st.session_state.pending_question
    st.session_state.pending_question = None

if user_question:
    st.session_state.chat_history.append({"role": "user", "content": user_question})

    with st.chat_message("user"):
        st.markdown(user_question)

    with st.chat_message("assistant"):
        with st.spinner("Searching website content..."):
            answer, source_urls = generate_answer(
                user_question=user_question,
                chat_history=st.session_state.chat_history[:-1]
            )

        render_answer_card(answer, source_urls)

    st.session_state.chat_history.append({
        "role": "assistant",
        "content": answer,
        "sources": source_urls
    })