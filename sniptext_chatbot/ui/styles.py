def inject_custom_css():
    return """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

        * { font-family: 'Inter', sans-serif !important; }

        .stApp { background: #F3F4F6; }

        @keyframes slideInLeft {
            from { transform: translateX(-110%); opacity: 0; }
            to   { transform: translateX(0);     opacity: 1; }
        }

        section[data-testid="stSidebar"] {
            background: linear-gradient(160deg, #1D4ED8 0%, #2563EB 55%, #e85d27 140%);
            border-right: none;
            animation: slideInLeft 0.45s cubic-bezier(0.22, 1, 0.36, 1);
            box-shadow: 4px 0 24px rgba(29, 78, 216, 0.18);
        }

        section[data-testid="stSidebar"] h1,
        section[data-testid="stSidebar"] h2,
        section[data-testid="stSidebar"] h3,
        section[data-testid="stSidebar"] label,
        section[data-testid="stSidebar"] p,
        section[data-testid="stSidebar"] span,
        section[data-testid="stSidebar"] div { color: #EFF6FF !important; }

        section[data-testid="stSidebar"] hr { border-color: rgba(255,255,255,0.18) !important; }

        section[data-testid="stSidebar"] .stTextInput input {
            background: rgba(255,255,255,0.12) !important;
            color: #FFFFFF !important;
            border: 1px solid rgba(255,255,255,0.25) !important;
            border-radius: 10px !important;
        }

        .brand-header {
            padding: 1.3rem 1.1rem 1.1rem;
            border-radius: 16px;
            margin-bottom: 0.5rem;
            background: rgba(255,255,255,0.10);
            border: 1px solid rgba(255,255,255,0.18);
            backdrop-filter: blur(8px);
            position: relative;
            overflow: hidden;
        }
        .brand-header::after {
            content: "";
            position: absolute;
            top: -40px; right: -40px;
            width: 130px; height: 130px;
            background: rgba(255,255,255,0.06);
            border-radius: 50%;
        }
        .brand-logo  { font-size: 2rem; margin-bottom: 0.3rem; }
        .brand-title { font-size: 1.3rem; font-weight: 800; color: #fff; letter-spacing: -0.3px; }
        .brand-subtitle { font-size: 0.82rem; color: rgba(255,255,255,0.78); margin-top: 0.2rem; }

        .section-header {
            font-size: 0.68rem;
            font-weight: 700;
            color: rgba(255,255,255,0.55) !important;
            letter-spacing: 0.1em;
            text-transform: uppercase;
            margin: 0.9rem 0 0.45rem;
        }

        section[data-testid="stSidebar"] .stButton > button {
            background: rgba(255,255,255,0.10) !important;
            border: 1px solid rgba(255,255,255,0.22) !important;
            color: #EFF6FF !important;
            border-radius: 10px !important;
            font-weight: 600 !important;
            font-size: 0.88rem !important;
            min-height: 42px !important;
            transition: background 0.18s ease, transform 0.12s ease, border-color 0.18s !important;
        }
        section[data-testid="stSidebar"] .stButton > button:hover {
            background: rgba(255,255,255,0.22) !important;
            border-color: rgba(255,255,255,0.45) !important;
            transform: translateX(3px) !important;
        }

        /* Main area suggestion buttons */
        .stButton > button {
            background: #FFFFFF !important;
            border: 1.5px solid #E5E7EB !important;
            color: #1F2937 !important;
            border-radius: 999px !important;
            font-weight: 500 !important;
            font-size: 0.84rem !important;
            padding: 0.45rem 0.9rem !important;
            min-height: 38px !important;
            transition: all 0.15s ease !important;
            box-shadow: 0 1px 3px rgba(0,0,0,0.06) !important;
        }
        .stButton > button:hover {
            background: #EFF6FF !important;
            border-color: #3B82F6 !important;
            color: #1D4ED8 !important;
            box-shadow: 0 3px 10px rgba(29,78,216,0.12) !important;
            transform: translateY(-1px) !important;
        }

        /* ── USER MESSAGE BUBBLE (LEFT, SKY BLUE) ── */
        .user-message-row {
            display: flex;
            align-items: flex-start;
            gap: 10px;
            margin: 0.65rem 0;
            justify-content: flex-start;
        }
        .user-avatar {
            width: 34px;
            height: 34px;
            border-radius: 50%;
            background: #1D4ED8;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1rem;
            flex-shrink: 0;
            box-shadow: 0 2px 8px rgba(29,78,216,0.3);
        }
        .user-bubble {
            background: #3B82F6;
            color: #FFFFFF;
            border-radius: 4px 18px 18px 18px;
            padding: 0.7rem 1.1rem;
            max-width: 70%;
            font-size: 0.93rem;
            line-height: 1.65;
            box-shadow: 0 4px 14px rgba(59,130,246,0.22);
            word-wrap: break-word;
        }

        /* ── ASSISTANT MESSAGE (RIGHT, WHITE) ── */
        .assistant-message-row {
            display: flex;
            align-items: flex-start;
            gap: 10px;
            margin: 0.65rem 0;
            justify-content: flex-end;
        }
        .assistant-avatar {
            width: 34px;
            height: 34px;
            border-radius: 50%;
            background: linear-gradient(135deg, #1D4ED8, #3B82F6);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1rem;
            flex-shrink: 0;
            box-shadow: 0 2px 8px rgba(29,78,216,0.25);
        }
        .assistant-bubble {
            background: #FFFFFF;
            border: 1px solid #E5E7EB;
            border-radius: 18px 4px 18px 18px;
            padding: 0.9rem 1.15rem;
            max-width: 75%;
            font-size: 0.93rem;
            line-height: 1.72;
            color: #1F2937;
            box-shadow: 0 4px 18px rgba(0,0,0,0.07);
            word-wrap: break-word;
        }

        .streaming-text {
            color: #1F2937;
            font-size: 0.93rem;
            line-height: 1.72;
        }

        /* ── RELATED LINK ── */
        .related-link-box {
            margin-top: 0.75rem;
            padding: 0.55rem 0.85rem;
            background: #EFF6FF;
            border: 1px solid #BFDBFE;
            border-radius: 10px;
            display: flex;
            align-items: center;
            gap: 0.4rem;
        }
        .related-link {
            color: #1D4ED8 !important;
            text-decoration: none;
            font-weight: 600;
            font-size: 0.84rem;
            word-break: break-word;
            transition: color 0.15s;
        }
        .related-link:hover { color: #e85d27 !important; text-decoration: underline; }

        /* ── EMPTY STATE ── */
        .empty-state { text-align: center; padding: 2rem 1rem 1rem; }
        .empty-state-icon  { font-size: 2.4rem; margin-bottom: 0.6rem; }
        .empty-state-title { font-size: 1.05rem; font-weight: 700; color: #1F2937; margin-bottom: 0.4rem; }
        .empty-state-subtitle {
            font-size: 0.85rem; color: #6B7280; line-height: 1.65;
            max-width: 420px; margin: 0 auto;
        }

        /* ── CHAT INPUT ── */
        div[data-testid="stChatInput"] textarea {
            background: #FFFFFF !important;
            border: 1.5px solid #E5E7EB !important;
            border-radius: 16px !important;
            color: #1F2937 !important;
            font-size: 0.93rem !important;
            padding: 0.85rem 1rem !important;
            min-height: 50px !important;
            box-shadow: 0 2px 8px rgba(0,0,0,0.05) !important;
            transition: border-color 0.18s, box-shadow 0.18s !important;
        }
        div[data-testid="stChatInput"] textarea:focus {
            border-color: #3B82F6 !important;
            box-shadow: 0 0 0 3px rgba(59,130,246,0.12) !important;
        }
        button[data-testid="stChatInputSubmitButton"] {
            background: #1D4ED8 !important;
            border-radius: 10px !important;
            color: white !important;
        }
        button[data-testid="stChatInputSubmitButton"]:hover {
            background: #2563EB !important;
        }

        /* ── TEXT INPUT ── */
        .stTextInput > div > div > input {
            background: #FFFFFF !important;
            border: 1.5px solid #E5E7EB !important;
            border-radius: 10px !important;
            color: #1F2937 !important;
            transition: border-color 0.18s, box-shadow 0.18s !important;
        }
        .stTextInput > div > div > input:focus {
            border-color: #3B82F6 !important;
            box-shadow: 0 0 0 3px rgba(59,130,246,0.10) !important;
        }

        /* ── ADMIN CARDS ── */
        .meta-card {
            background: #FFFFFF; border: 1px solid #E5E7EB;
            border-radius: 14px; padding: 1rem 1.2rem; margin-bottom: 0.75rem;
        }
        .meta-card * { color: #1F2937 !important; }
        .meta-card strong { color: #1D4ED8 !important; }

        .admin-section {
            background: #FFFFFF; border: 1px solid #E5E7EB;
            border-radius: 14px; padding: 1.1rem 1.3rem;
            margin-bottom: 0.9rem; box-shadow: 0 2px 8px rgba(0,0,0,0.04);
        }
        .admin-section-title {
            font-size: 0.72rem; font-weight: 700; color: #6B7280;
            letter-spacing: 0.08em; text-transform: uppercase; margin-bottom: 0.65rem;
        }

        .url-item {
            background: #F3F4F6; border: 1px solid #E5E7EB;
            border-radius: 10px; padding: 0.55rem 0.8rem; margin-bottom: 0.35rem;
            transition: border-color 0.15s;
        }
        .url-item:hover { border-color: #3B82F6; }
        .url-text { color: #1D4ED8 !important; font-size: 0.83rem; font-weight: 500; word-break: break-word; }
        .removed-url { opacity: 0.55; }

        .stSuccess { background: #F0FDF4 !important; border: 1px solid #BBF7D0 !important; border-radius: 10px !important; color: #166534 !important; }
        .stError   { background: #FEF2F2 !important; border: 1px solid #FECACA !important; border-radius: 10px !important; color: #991B1B !important; }
        .stInfo, .stAlert { background: #EFF6FF !important; border: 1px solid #BFDBFE !important; border-radius: 10px !important; color: #1E40AF !important; }

        hr { border-color: #E5E7EB !important; margin: 0.8rem 0 !important; }
        .stMarkdown p, .stMarkdown li { color: #1F2937; }
        .stMarkdown h1,.stMarkdown h2,.stMarkdown h3 { color: #111827; }

        ::-webkit-scrollbar { width: 5px; }
        ::-webkit-scrollbar-track { background: #F3F4F6; }
        ::-webkit-scrollbar-thumb { background: #D1D5DB; border-radius: 99px; }
        ::-webkit-scrollbar-thumb:hover { background: #9CA3AF; }
    </style>
    """