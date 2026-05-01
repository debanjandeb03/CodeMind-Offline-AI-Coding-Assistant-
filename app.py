# For running this app write: streamlit run app.py

import streamlit as st
import requests
import re
from prompt import SYSTEM_PROMPT


# ------------------ Utility Function ------------------
def clean_output(text):
    """
    Remove ANSI escape sequences from model output
    """
    ansi_escape = re.compile(r'\x1B\[[0-?]*[ -/]*[@-~]')
    return ansi_escape.sub('', text)


# ------------------ LLM Function ------------------
def query_llm(full_prompt):
    try:
        response = requests.post(
            "http://host.docker.internal:11434/api/generate",
            json={
                "model": "deepseek-coder",
                "prompt": full_prompt,
                "stream": False
            },
        )
        return response.json().get("response", "No response")
    except Exception as e:
        return f"Error: {str(e)}"


# ------------------ UI ------------------
st.set_page_config(page_title="CodeMind-Offline Coding Assistant", layout="wide")

st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
    background-color: #0f172a;
    color: white;
}

[data-testid="stSidebar"] {
    background-color: #111827;
}

[data-testid="stChatMessage"] {
    border-radius: 12px;
    padding: 10px;
    margin-bottom: 10px;
}

[data-testid="stChatMessage"][data-testid="user"] {
    background-color: #1e293b;
}

[data-testid="stChatMessage"][data-testid="assistant"] {
    background-color: #020617;
}

.stButton button {
    background-color: #2563eb;
    color: white;
    border-radius: 8px;
    padding: 8px 16px;
}

textarea {
    background-color: #020617 !important;
    color: white !important;
}

#loader {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: linear-gradient(135deg, #f8fafc, #eef2ff);
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 9999;
    flex-direction: column;
}

.spinner {
    width: 50px;
    height: 50px;
    border: 5px solid #c7d2fe;
    border-top: 5px solid #6366f1;
    border-radius: 50%;
    animation: spin 1s linear infinite;
    margin-bottom: 15px;
}

@keyframes spin {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
}

.loader-text {
    font-size: 18px;
    color: #4f46e5;
    font-weight: 600;
}
</style>
""", unsafe_allow_html=True)

st.title("CodeMind-Offline Coding Assistant")
st.caption("Private • Offline • Coding-Only AI Assistant")

user_input = st.text_area(
    "Enter your coding question or paste code:",
    height=250,
    placeholder="Example: Explain and optimize this C++ solution for LeetCode..."
)


# ------------------ Button Logic ------------------
if st.button("Ask CodeMind"):
    if user_input.strip() == "":
        st.warning("Please enter a coding-related query.")
    else:
        full_prompt = SYSTEM_PROMPT + "\n\nUSER QUERY:\n" + user_input

        st.subheader("🧠 DeepSeek Response")

        with st.spinner("Thinking..."):
            output = query_llm(full_prompt)

        cleaned_output = clean_output(output)
        st.markdown(cleaned_output, unsafe_allow_html=True)

    
