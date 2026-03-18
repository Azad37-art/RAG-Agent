def inject_custom_css():
    return """
    <style>
        .main {
            padding-top: 1rem;
        }

        .block-container {
            padding-top: 1.2rem;
            padding-bottom: 2rem;
            max-width: 1100px;
        }

        .brand-header {
            padding: 1.25rem 1.25rem;
            border-radius: 18px;
            background: linear-gradient(135deg, #0f172a, #1e293b);
            color: white;
            margin-bottom: 1rem;
            box-shadow: 0 10px 30px rgba(0,0,0,0.18);
        }

        .brand-title {
            font-size: 2rem;
            font-weight: 800;
            margin-bottom: 0.2rem;
        }

        .brand-subtitle {
            font-size: 1rem;
            opacity: 0.92;
        }

        .answer-card {
            border: 1px solid rgba(255,255,255,0.10);
            border-radius: 18px;
            padding: 1rem 1rem 0.7rem 1rem;
            margin-top: 0.4rem;
            background: linear-gradient(180deg, rgba(255,255,255,0.03), rgba(255,255,255,0.015));
            box-shadow: 0 8px 24px rgba(0,0,0,0.10);
        }

        .answer-card-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 0.7rem;
            gap: 0.75rem;
            flex-wrap: wrap;
        }

        .answer-title {
            font-size: 1.05rem;
            font-weight: 700;
        }

        .trust-badge {
            font-size: 0.78rem;
            padding: 0.35rem 0.65rem;
            border-radius: 999px;
            background: rgba(59,130,246,0.12);
            border: 1px solid rgba(59,130,246,0.25);
        }

        .sources-row {
            display: flex;
            flex-wrap: wrap;
            gap: 0.6rem;
            margin-top: 0.7rem;
            margin-bottom: 0.2rem;
        }

        .source-card {
            display: inline-block;
            padding: 0.65rem 0.8rem;
            border-radius: 14px;
            border: 1px solid rgba(255,255,255,0.10);
            background: rgba(255,255,255,0.03);
            font-size: 0.88rem;
            text-decoration: none;
        }

        .section-label {
            font-size: 0.9rem;
            font-weight: 700;
            margin-top: 0.8rem;
            margin-bottom: 0.45rem;
        }

        .meta-card {
            border: 1px solid rgba(255,255,255,0.08);
            border-radius: 14px;
            padding: 0.8rem;
            margin-top: 0.5rem;
            background: rgba(255,255,255,0.02);
        }

        .small-muted {
            font-size: 0.85rem;
            opacity: 0.85;
        }

        .url-item {
            padding: 0.45rem 0.55rem;
            border-radius: 10px;
            background: rgba(255,255,255,0.02);
            margin-bottom: 0.35rem;
            border: 1px solid rgba(255,255,255,0.05);
        }
    </style>
    """