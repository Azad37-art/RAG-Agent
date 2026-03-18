from pathlib import Path

APP_NAME = "CheckAI Website Assistant"
APP_TAGLINE = "Ask anything about the website"
APP_ICON = "🤖"

DATA_DIR = Path("data")
VECTOR_DIR = DATA_DIR / "faiss_index"
URLS_FILE = DATA_DIR / "urls.json"
REMOVED_URLS_FILE = DATA_DIR / "removed_urls.json"
INDEX_META_FILE = DATA_DIR / "index_meta.json"

DEFAULT_URLS = [
    "https://www.checkai.pro/",
    "https://www.checkai.pro/tools/free-tools",
    "https://www.checkai.pro/features",
    "https://www.checkai.pro/about",
    "https://www.checkai.pro/blog/blog",
    "https://www.checkai.pro/contact",
]

EMBEDDING_MODEL = "sentence-transformers/all-mpnet-base-v2"
LLM_MODEL = "gemini-2.5-flash"

CHUNK_SIZE = 800
CHUNK_OVERLAP = 120

TOP_K = 6
MIN_CONTEXT_LENGTH = 180

SUGGESTED_QUESTIONS = [
    "What free tools are available?",
    "What features does CheckAI offer?",
    "How can I contact support?",
    "Tell me about the company.",
]