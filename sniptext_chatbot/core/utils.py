import json
import shutil
from datetime import datetime
from collections import OrderedDict

from config.settings import (
    URLS_FILE,
    REMOVED_URLS_FILE,
    DEFAULT_URLS,
    VECTOR_DIR,
    INDEX_META_FILE,
)


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


def _load_json_list(file_path, default=None):
    file_path.parent.mkdir(parents=True, exist_ok=True)

    if not file_path.exists():
        return default[:] if default else []

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data if isinstance(data, list) else (default[:] if default else [])
    except Exception:
        return default[:] if default else []


def _save_json_list(file_path, items):
    file_path.parent.mkdir(parents=True, exist_ok=True)

    clean_items = []
    seen = set()
    for item in items:
        item = item.strip()
        if item and item not in seen:
            clean_items.append(item)
            seen.add(item)

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(clean_items, f, indent=2)


def load_urls():
    if not URLS_FILE.exists():
        save_urls(DEFAULT_URLS)
        return DEFAULT_URLS[:]
    return _load_json_list(URLS_FILE, DEFAULT_URLS)


def save_urls(urls):
    _save_json_list(URLS_FILE, urls)


def load_removed_urls():
    return _load_json_list(REMOVED_URLS_FILE, [])


def save_removed_urls(urls):
    _save_json_list(REMOVED_URLS_FILE, urls)


def add_url(new_url: str):
    new_url = new_url.strip()
    if not new_url:
        return

    active_urls = load_urls()
    removed_urls = load_removed_urls()

    if new_url not in active_urls:
        active_urls.append(new_url)
        save_urls(active_urls)

    if new_url in removed_urls:
        removed_urls.remove(new_url)
        save_removed_urls(removed_urls)


def remove_url(url_to_remove: str):
    active_urls = load_urls()
    removed_urls = load_removed_urls()

    active_urls = [u for u in active_urls if u != url_to_remove]

    if url_to_remove not in removed_urls:
        removed_urls.append(url_to_remove)

    save_urls(active_urls)
    save_removed_urls(removed_urls)


def restore_removed_url(url_to_restore: str):
    active_urls = load_urls()
    removed_urls = load_removed_urls()

    if url_to_restore not in active_urls:
        active_urls.append(url_to_restore)

    removed_urls = [u for u in removed_urls if u != url_to_restore]

    save_urls(active_urls)
    save_removed_urls(removed_urls)


def restore_default_urls():
    active_urls = load_urls()
    removed_urls = load_removed_urls()

    for url in DEFAULT_URLS:
        if url not in active_urls:
            active_urls.append(url)
        if url in removed_urls:
            removed_urls.remove(url)

    save_urls(active_urls)
    save_removed_urls(removed_urls)


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