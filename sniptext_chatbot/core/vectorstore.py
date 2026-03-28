import streamlit as st
from langchain_community.vectorstores import FAISS

from config.settings import VECTOR_DIR
from core.embeddings import get_embeddings
from core.loader import load_website_docs
from core.splitter import split_docs
from core.utils import save_index_meta


@st.cache_resource(show_spinner=True)
def get_vectorstore():
    embeddings = get_embeddings()

    if VECTOR_DIR.exists():
        return FAISS.load_local(
            str(VECTOR_DIR),
            embeddings,
            allow_dangerous_deserialization=True
        )

    docs = load_website_docs()
    chunks = split_docs(docs)

    vs = FAISS.from_documents(chunks, embeddings)
    VECTOR_DIR.parent.mkdir(parents=True, exist_ok=True)
    vs.save_local(str(VECTOR_DIR))

    save_index_meta(
        chunk_count=len(chunks),
        url_count=len({doc.metadata.get("source", "") for doc in docs})
    )

    return vs


def rebuild_vectorstore():
    from core.utils import delete_vectorstore
    delete_vectorstore()
    get_vectorstore.clear()
    return get_vectorstore()