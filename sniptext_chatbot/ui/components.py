import streamlit as st


def render_suggestions(questions):
    st.markdown("### Try asking")
    cols = st.columns(2)
    clicked_question = None

    for i, question in enumerate(questions):
        with cols[i % 2]:
            if st.button(question, use_container_width=True, key=f"suggestion_{i}"):
                clicked_question = question

    return clicked_question


def render_answer_card(answer, related_link=None):
    st.markdown(
        """
        <div class="answer-card">
            <div class="answer-card-header">
                <div class="answer-title">Response</div>
                <div class="trust-badge">Website-grounded</div>
            </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(answer)

    if related_link:
        st.markdown(
            f"""
            <div class="related-link-box">
                <a class="related-link" href="{related_link}" target="_blank">
                    Click here to explore more
                </a>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("</div>", unsafe_allow_html=True)


def render_empty_state():
    st.info(
        "This assistant answers questions from the indexed website pages. "
        "Ask about features, free tools, contact info, or company details."
    )


def render_index_meta(meta):
    st.markdown("### Knowledge Base Status")
    st.markdown(
        f"""
        <div class="meta-card">
            <div><strong>Last updated:</strong> {meta.get('last_updated', 'Not available')}</div>
            <div><strong>Total chunks:</strong> {meta.get('chunk_count', 0)}</div>
            <div><strong>Total URLs:</strong> {meta.get('url_count', 0)}</div>
        </div>
        """,
        unsafe_allow_html=True
    )