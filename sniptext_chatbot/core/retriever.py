from config.settings import TOP_K
from core.vectorstore import get_vectorstore
from core.utils import deduplicate_docs, rank_docs


def retrieve_documents(user_question: str):
    vectorstore = get_vectorstore()

    retriever = vectorstore.as_retriever(
        search_type="mmr",
        search_kwargs={"k": TOP_K, "fetch_k": 25}
    )

    docs = retriever.invoke(user_question)
    docs = deduplicate_docs(docs)
    docs = rank_docs(docs, user_question)

    return docs