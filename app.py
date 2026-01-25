
#For running this app write streamlit run app.py
import streamlit as st
import subprocess
from prompt import SYSTEM_PROMPT

st.set_page_config(page_title="Offline Coding Assistant",layout="wide")
st.title("Offline Coding ChatGPT")
st.caption("Private • Offline • Coding-Only AI Assistant")

user_input = st.text_area(
    "Enter your coding question or paste code:",
    height=250,
    placeholder="Example: Explain and optimize this C++ solution for LeetCode..."
)

if st.button("Ask DeepSeek"):
    if user_input.strip() == "":
        st.warning("Please enter a coding-related query.")
    else:
        full_prompt = SYSTEM_PROMPT + "\n\nUSER QUERY:\n" + user_input

        with st.spinner("Thinking... (running locally)"):
            result = subprocess.run(
                ["ollama", "run", "deepseek-coder"],
                input=full_prompt,
                text=True,
                capture_output=True
            )

        st.subheader("🧠 DeepSeek Response")
        st.code(result.stdout, language="markdown")

    
