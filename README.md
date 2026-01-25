```
# 🧠 CodeMind – Offline AI Coding Assistant

**CodeMind** is a **privacy-first, offline AI coding assistant** built using **Ollama** and **DeepSeek-R1**, designed exclusively for **programming, DSA, and debugging tasks**.

The application runs entirely on the local machine, ensuring **zero cloud dependency**, **no API costs**, and **complete data privacy**.

---

## 🚀 Key Highlights

- 🔒 Fully **offline & private**
- 💻 Restricted to **coding-only queries**
- 🧠 Powered by **DeepSeek-R1 (7B)** for strong reasoning
- 📊 Provides approach, optimized code, and complexity analysis
- ⚡ Fast local inference using Ollama
- 🧩 Minimal and clean **Streamlit UI**

---

## 🏗️ Architecture Overview
User (Browser)
↓
Streamlit Interface
↓
Prompt Engineering Layer
↓
Ollama (Local Runtime)
↓
DeepSeek-R1 LLM (Offline)


---

## 🧠 Model Information

- **Model:** DeepSeek-R1 (7B)
- **Inference Mode:** Local (via Ollama)

> Model weights are intentionally excluded from the repository and must be pulled locally.

---

## 📁 Project Structure
CodeMind/
│
├── app.py # Streamlit application
├── prompt.py # Coding-only system prompt
├── requirements.txt # Python dependencies
├── README.md
└── .gitignore


---

## ⚙️ Setup & Usage
### 1️⃣ Install Ollama
https://ollama.com/download
Verify installation:
```bash
ollama --version

🧪 Supported Use Cases
Explain and optimize DSA solutions
Debug logical and runtime errors
Analyze time & space complexity
Improve algorithmic approaches
Offline coding interview preparation
Non-technical queries are intentionally rejected.

🧠 Design Decisions 
Local Inference over Cloud APIs
Chosen to ensure data privacy and eliminate dependency on paid services.
Coding-Only Prompt Constraint
Prevents misuse and improves answer relevance for technical tasks.
Streamlit for UI
Enables rapid prototyping and easy local interaction without frontend complexity.
Ollama Runtime
Provides standardized local model management and reproducibility.

⚖️ Limitations & Trade-offs
Requires moderate system RAM (recommended: 16 GB)
Performance depends on local hardware
No persistent conversation memory (by design for privacy)
These trade-offs were accepted to prioritize security, simplicity, and offline capability.

📊 Performance Notes
Average response latency: 1–3 seconds on mid-range laptops
Handles multi-hundred-line code inputs reliably
Stable for extended DSA and debugging sessions

🛠️ Tech Stack
Python
Streamlit
Ollama
DeepSeek-R1 LLM
```
