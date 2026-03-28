from config.settings import MIN_CONTEXT_LENGTH
from core.llm import get_llm
from core.prompt import SYSTEM_PROMPT
from core.retriever import retrieve_documents
from core.utils import build_context

def build_messages(chat_history, prompt, user_question):
    messages = [("system", prompt)]

    history_window = chat_history[-6:]
    for msg in history_window:
        role = "human" if msg["role"] == "user" else "assistant"
        messages.append((role, msg["content"]))

    messages.append(("human", user_question))
    return messages


def _pick_best_link(docs, user_question):
    """
    Score each retrieved document against the question and return
    the source URL of the highest-scoring one.
    Scoring: count how many unique question words appear in the doc content.
    """
    if not docs:
        return None

    question_words = set(
        w.lower() for w in user_question.split()
        if len(w) > 3  # skip short stop-words
    )

    best_score = -1
    best_url = None

    for doc in docs:
        source = doc.metadata.get("source") or doc.metadata.get("url", "")
        if not source:
            continue

        content_lower = doc.page_content.lower()
        score = sum(1 for w in question_words if w in content_lower)

        if score > best_score:
            best_score = score
            best_url = source

    # Only return a link if there is at least some meaningful match
    return best_url if best_score >= 1 else None


def generate_answer(user_question: str, chat_history: list):
    docs = retrieve_documents(user_question)

    context = build_context(docs)

    # Not enough relevant content found
    if len(context) < MIN_CONTEXT_LENGTH:
        answer = (
            "I'm sorry, I couldn't find this information on the website.\n\n"
            "📞 WhatsApp: +92 341 8378430\n"
            "📧 Email: support@sniptext.com\n\n"
            "Feel free to contact us — we'll help you!"
        )
        return answer, None

    # Pick the most relevant link for THIS specific question
    related_link = _pick_best_link(docs, user_question)

    # Build and run LLM
    prompt = SYSTEM_PROMPT.format(context=context)
    llm = get_llm()
    messages = build_messages(chat_history, prompt, user_question)
    response = llm.invoke(messages)

    answer = response.content if hasattr(response, "content") else str(response)

    return answer, related_link


def rebuild_index(urls: list):
    pass
