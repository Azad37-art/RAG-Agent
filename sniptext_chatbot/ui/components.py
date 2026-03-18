import streamlit as st


def render_suggestions(questions):
    st.markdown("### Try asking")
    cols = st.columns(2)
    clicked_question = None

    for i, question in enumerate(questions):
        with cols[i % 2]:
            if st.button(question, use_container_width=True):
                clicked_question = question

    return clicked_question


def render_top_sources(source_urls):
    if not source_urls:
        return

    st.markdown('<div class="section-label">Top Sources</div>', unsafe_allow_html=True)

    cards_html = '<div class="sources-row">'
    for url in source_urls[:3]:
        cards_html += f'<a class="source-card" href="{url}" target="_blank">{url}</a>'
    cards_html += "</div>"

    st.markdown(cards_html, unsafe_allow_html=True)


def render_answer_card(answer, source_urls):
    st.markdown(
        """
        <div class="answer-card">
            <div class="answer-card-header">
                <div class="answer-title">Answer</div>
                <div class="trust-badge">Website-grounded</div>
            </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(answer)
    render_top_sources(source_urls)

    st.markdown("</div>", unsafe_allow_html=True)


def render_empty_state():
    st.info(
        "This assistant answers questions only from the indexed website pages. "
        "Ask about features, free tools, contact info, blog, or company details."
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