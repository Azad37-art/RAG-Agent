import os
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI

def get_llm():
    api_key = (
        st.secrets.get("GOOGLE_API_KEY")
        or st.secrets.get("GEMINI_API_KEY")
        or os.getenv("GOOGLE_API_KEY")
        or os.getenv("GEMINI_API_KEY")
    )

    if not api_key:
        raise ValueError(
            "Gemini API key not found. Add GOOGLE_API_KEY or GEMINI_API_KEY in Streamlit secrets."
        )

    return ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        google_api_key=api_key,
        temperature=0.2,
    )
