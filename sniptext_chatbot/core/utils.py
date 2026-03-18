import json
import shutil
from collections import OrderedDict
from datetime import datetime

from config.settings import URLS_FILE, DEFAULT_URLS, VECTOR_DIR, INDEX_META_FILE


def normalize_text(text: str) -> str:
    return " ".join(text.split()).strip().lower()


def deduplicate_docs(docs):
    seen = set()
    unique_docs = []

    for doc in docs:
        key = (
            normalize_text(doc.page_content[:500]),
            doc.metadata.get("source", "")
        )
        if key not in seen:
            seen.add(key)
            unique_docs.append(doc)

    return unique_docs


def rank_docs(docs, query: str):
    query_terms = set(query.lower().split())
    scored = []

    for doc in docs:
        content = doc.page_content.lower()
        overlap = sum(1 for term in query_terms if term in content)
        source_bonus = 1 if doc.metadata.get("source") else 0
        score = overlap + source_bonus
        scored.append((score, doc))

    scored.sort(key=lambda x: x[0], reverse=True)
    return [doc for _, doc in scored]


def extract_sources(docs):
    ordered = OrderedDict()
    for doc in docs:
        src = doc.metadata.get("source", "").strip()
        if src and src not in ordered:
            ordered[src] = True
    return list(ordered.keys())


def build_context(docs):
    return "\n\n".join(doc.page_content.strip() for doc in docs if doc.page_content.strip())


def load_urls():
    URLS_FILE.parent.mkdir(parents=True, exist_ok=True)

    if not URLS_FILE.exists():
        save_urls(DEFAULT_URLS)
        return DEFAULT_URLS.copy()

    try:
        with open(URLS_FILE, "r", encoding="utf-8") as f:
            urls = json.load(f)
        if not isinstance(urls, list):
            return DEFAULT_URLS.copy()
        return urls
    except Exception:
        return DEFAULT_URLS.copy()


def save_urls(urls):
    URLS_FILE.parent.mkdir(parents=True, exist_ok=True)
    clean_urls = []
    seen = set()

    for url in urls:
        url = url.strip()
        if url and url not in seen:
            clean_urls.append(url)
            seen.add(url)

    with open(URLS_FILE, "w", encoding="utf-8") as f:
        json.dump(clean_urls, f, indent=2)


def add_url(new_url: str):
    urls = load_urls()
    new_url = new_url.strip()

    if new_url and new_url not in urls:
        urls.append(new_url)
        save_urls(urls)


def remove_url(url_to_remove: str):
    urls = load_urls()
    urls = [u for u in urls if u != url_to_remove]
    save_urls(urls)


def delete_vectorstore():
    if VECTOR_DIR.exists():
        shutil.rmtree(VECTOR_DIR)


def save_index_meta(chunk_count: int, url_count: int):
    INDEX_META_FILE.parent.mkdir(parents=True, exist_ok=True)
    data = {
        "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "chunk_count": chunk_count,
        "url_count": url_count,
    }
    with open(INDEX_META_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def load_index_meta():
    if not INDEX_META_FILE.exists():
        return {
            "last_updated": "Not available",
            "chunk_count": 0,
            "url_count": 0,
        }

    try:
        with open(INDEX_META_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {
            "last_updated": "Not available",
            "chunk_count": 0,
            "url_count": 0,
        }