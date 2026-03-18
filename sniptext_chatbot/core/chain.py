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
    related_link = source_urls[0] if source_urls else ""

    if len(context) < MIN_CONTEXT_LENGTH:
        answer = (
            "I couldn’t find that information on the indexed website pages.\n\n"
            "You can try asking about features, free tools, contact information, or company details."
        )
        return answer, related_link

    prompt = SYSTEM_PROMPT.format(
        context=context,
        source=related_link if related_link else "Not available"
    )

    llm = get_llm()
    messages = build_messages(chat_history, prompt, user_question)
    response = llm.invoke(messages)

    answer = response.content if hasattr(response, "content") else str(response)
    return answer, related_link