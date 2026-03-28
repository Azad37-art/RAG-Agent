import streamlit as st


def render_answer_card(answer, related_link=None):
    st.markdown(
        """
        <div class="answer-card">
        """,
        unsafe_allow_html=True
    )
    st.markdown(answer)
    if related_link:
        st.markdown(
            f"""
            <div class="related-link-box">
                <span>🔗</span>
                <a class="related-link" href="{related_link}" target="_blank">{related_link}</a>
            </div>
            """,
            unsafe_allow_html=True
        )
    st.markdown("</div>", unsafe_allow_html=True)


def render_empty_state():
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


def render_index_meta(meta):
    st.markdown(
        f"""
        <div class="meta-card">
            <div style="display:flex; gap:2rem; flex-wrap:wrap;">
                <div>
                    <div style="font-size:0.7rem;color:#6B7280;text-transform:uppercase;
                                letter-spacing:0.06em;margin-bottom:2px;">Last updated</div>
                    <div style="font-size:0.95rem;font-weight:600;color:#1F2937;">
                        {meta.get('last_updated', 'Not available')}</div>
                </div>
                <div>
                    <div style="font-size:0.7rem;color:#6B7280;text-transform:uppercase;
                                letter-spacing:0.06em;margin-bottom:2px;">Total chunks</div>
                    <div style="font-size:0.95rem;font-weight:600;color:#1F2937;">
                        {meta.get('chunk_count', 0)}</div>
                </div>
                <div>
                    <div style="font-size:0.7rem;color:#6B7280;text-transform:uppercase;
                                letter-spacing:0.06em;margin-bottom:2px;">Indexed URLs</div>
                    <div style="font-size:0.95rem;font-weight:600;color:#1F2937;">
                        {meta.get('url_count', 0)}</div>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


def render_url_item(url, removed=False):
    extra = "removed-url" if removed else ""
    icon = "🚫" if removed else "🌐"
    st.markdown(
        f"""
        <div class="url-item {extra}">
            <span style="font-size:0.8rem;">{icon}</span>
            <span class="url-text"> {url}</span>
        </div>
        """,
        unsafe_allow_html=True
    )


def render_brand_block(app_name, app_icon, tagline="Ask anything about the website"):
    st.markdown(
        f"""
        <div class="brand-header">
            <div class="brand-logo">{app_icon}</div>
            <div class="brand-title">{app_name}</div>
            <div class="brand-subtitle">{tagline}</div>
        </div>
        """,
        unsafe_allow_html=True
    )