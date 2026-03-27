from config.settings import MIN_CONTEXT_LENGTH
from core.llm import get_llm
from core.prompt import SYSTEM_PROMPT
from core.retriever import retrieve_documents
from core.utils import build_context, extract_sources


def build_messages(chat_history, prompt, user_question):
    messages = [("system", prompt)]

    history_window = chat_history[-6:]
    for msg in history_window:
        role = "human" if msg["role"] == "user" else "assistant"
        messages.append((role, msg["content"]))

    messages.append(("human", user_question))
    return messages

def generate_answer(user_question: str, chat_history: list):
    docs = retrieve_documents(user_question)

    context = build_context(docs)
    source_urls = extract_sources(docs)

    # Default: no link
    related_link = None

    # Check context length first (irrelevant / not found)
    if len(context) < MIN_CONTEXT_LENGTH:
        answer = (
            "I'm sorry, I couldn’t find this information on the website.\n\n"
            "📞 WhatsApp: +92 341 8378430\n"
            "📧 Email: support@sniptext.com\n\n"
            "Feel free to contact us — we’ll help you!"
        )
        return answer, None   # ❌ NO LINK

    # 🔥 SMART LINK FILTERING
    if source_urls:
        top_doc = docs[0]
        content = top_doc.page_content.lower()
        question_words = user_question.lower().split()

        # Count matching words
        match_count = sum(1 for w in question_words if w in content)

        # Only allow link if strong match
        if match_count >= 3:
            related_link = source_urls[0]
        else:
            related_link = None  # ❌ remove wrong link

    # Build prompt
    prompt = SYSTEM_PROMPT.format(
        context=context
    )

    llm = get_llm()
    messages = build_messages(chat_history, prompt, user_question)
    response = llm.invoke(messages)

    answer = response.content if hasattr(response, "content") else str(response)

    return answer, related_link

def rebuild_index(urls: list):
    """
    Call your actual index rebuilding logic here.
    Replace the body of this function with your real implementation.
    For example: from core.indexer import build_index; build_index(urls)
    """
    pass
