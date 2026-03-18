def inject_custom_css():
    return """
    <style>
        .stApp {
            background: #F3F4F6;
        }

        section[data-testid="stSidebar"] {
            background: linear-gradient(180deg, #1D4ED8 0%, #3B82F6 100%);
            border-right: 1px solid rgba(255,255,255,0.18);
        }

        section[data-testid="stSidebar"] .stTextInput input {
            background: #FFFFFF !important;
            color: #1F2937 !important;
            border: 1px solid #E5E7EB !important;
            border-radius: 12px !important;
        }

        .brand-header {
            padding: 1.2rem;
            border-radius: 20px;
            color: white;
            margin-bottom: 1rem;
            background: linear-gradient(135deg, #1D4ED8 0%, #3B82F6 70%, #e85d27 100%);
            box-shadow: 0 10px 24px rgba(29, 78, 216, 0.18);
            border: 1px solid rgba(255,255,255,0.15);
        }

        .brand-title {
            font-size: 2rem;
            font-weight: 800;
            margin-bottom: 0.2rem;
            color: #FFFFFF;
        }

        .brand-subtitle {
            font-size: 1rem;
            color: rgba(255,255,255,0.92);
        }

        .answer-card {
            background: #FFFFFF;
            border: 1px solid #E5E7EB;
            border-radius: 18px;
            box-shadow: 0 6px 18px rgba(31, 41, 55, 0.06);
            padding: 1rem;
            margin-top: 0.4rem;
        }

        .meta-card {
            background: #FFFFFF;
            border: 1px solid #BFDBFE;
            border-radius: 16px;
            padding: 0.8rem;
            color: #1D4ED8 !important;
        }

        .url-item {
            background: #FFFFFF;
            border: 1px solid #93C5FD;
            border-radius: 14px;
            padding: 0.75rem 0.8rem;
            margin-bottom: 0.4rem;
        }

        .url-text {
            color: #1D4ED8 !important;
            font-size: 0.9rem;
            word-break: break-word;
            font-weight: 600;
        }

        .removed-url {
            background: #EFF6FF;
            border: 1px solid #BFDBFE;
        }

        .answer-card-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 0.75rem;
            gap: 0.75rem;
            flex-wrap: wrap;
        }

        .answer-title {
            color: #1F2937;
            font-weight: 700;
            font-size: 1.05rem;
        }

        .trust-badge {
            background: #EFF6FF;
            border: 1px solid #BFDBFE;
            color: #1D4ED8;
            border-radius: 999px;
            padding: 0.35rem 0.7rem;
            font-size: 0.78rem;
            font-weight: 600;
        }

        .related-link-box {
            margin-top: 0.9rem;
            padding: 0.75rem 0.85rem;
            background: #EFF6FF;
            border: 1px solid #BFDBFE;
            border-radius: 14px;
        }

        .related-link {
            color: #1D4ED8 !important;
            text-decoration: none;
            word-break: break-word;
            font-weight: 700;
        }

        .related-link:hover {
            text-decoration: underline;
        }

        .stButton > button {
            border-radius: 12px !important;
            border: none !important;
            color: white !important;
            font-weight: 600 !important;
            min-height: 46px !important;
            background: linear-gradient(135deg, #1D4ED8 0%, #3B82F6 80%, #e85d27 100%) !important;
            box-shadow: 0 8px 18px rgba(29, 78, 216, 0.18) !important;
        }

        .stButton > button:hover {
            filter: brightness(1.04);
        }

        .stTextInput > div > div > input,
        div[data-testid="stChatInput"] textarea {
            background: #FFFFFF !important;
            border: 1px solid #D1D5DB !important;
            border-radius: 16px !important;
            color: #1F2937 !important;
        }

        div[data-testid="stChatInput"] textarea {
            min-height: 64px !important;
            padding: 0.95rem 1rem !important;
            font-size: 1rem !important;
        }

        div[data-testid="stChatMessage"] {
            background: transparent;
            border: none;
        }

        .stInfo {
            background: #FFFFFF !important;
            border: 1px solid #E5E7EB !important;
            border-radius: 16px !important;
            color: #1F2937 !important;
        }

        /* BLUE TEXT FOR SIDEBAR SECTIONS */
        section[data-testid="stSidebar"] h1,
        section[data-testid="stSidebar"] h2,
        section[data-testid="stSidebar"] h3,
        section[data-testid="stSidebar"] label,
        section[data-testid="stSidebar"] p,
        section[data-testid="stSidebar"] span,
        section[data-testid="stSidebar"] div {
            color: #EAF2FF !important;
        }

        section[data-testid="stSidebar"] .meta-card,
        section[data-testid="stSidebar"] .meta-card strong,
        section[data-testid="stSidebar"] .url-item,
        section[data-testid="stSidebar"] .url-text {
            color: #1D4ED8 !important;
        }

        label, .stMarkdown, .stText, .stWrite, p, li, span {
            color: #1F2937;
        }

        small, .caption {
            color: #6B7280;
        }
    </style>
    """