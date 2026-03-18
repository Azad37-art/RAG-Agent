import os
from langchain_community.document_loaders import WebBaseLoader
from core.utils import load_urls


def load_website_docs():
    os.environ["USER_AGENT"] = os.getenv("USER_AGENT", "Mozilla/5.0")

    urls = load_urls()
    loader = WebBaseLoader(urls)
    docs = loader.load()

    for d in docs:
        d.metadata.setdefault("source", d.metadata.get("url", ""))
        d.metadata.setdefault("title", d.metadata.get("source", ""))

    return docs