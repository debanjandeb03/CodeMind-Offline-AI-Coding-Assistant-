```
# CodeMind – Offline AI Coding Assistant

CodeMind is a privacy-first, offline AI coding assistant built using Ollama and DeepSeek-R1, designed specifically for programming, DSA, and debugging workflows.

Unlike typical AI tools, CodeMind runs entirely on our local machine, ensuring:
- Zero data leakage.
- No API costs.
- Full control over inference.

---

## Key Features

- Fully offline & privacy-focused
- Strictly supports coding-related queries.
- Powered by DeepSeek-R1 (7B) for strong reasoning.
- Structured output:
  - Approach
  - Code
  - Explanation
  - Complexity Analysis
- Local inference via Ollama.
- Clean and minimal Streamlit UI.
- Dockerized for portability and reproducibility.

---

## Architecture

User (Browser)
↓
Streamlit Interface
↓
Prompt Engineering Layer
↓
Ollama Runtime
↓
DeepSeek-R1 (Local LLM)

---

## Model Details

- Model: DeepSeek-R1 (7B)
- Inference: Fully local via Ollama
- Execution Mode: Offline (no internet required after setup)

>NOTE: Model weights are not included in this repository and must be downloaded locally using Ollama.

---

## Project Structure

CodeMind/
│
├── app.py # Streamlit application
├── prompt.py # System prompt (coding-only constraint)
├── requirements.txt # Dependencies
├── Dockerfile # Containerization setup
├── README.md
└── .gitignore
---

## Setup & Usage

1️⃣ Install Ollama
Download from: https://ollama.com/download
Verify installation:
```bash
ollama --version

2️⃣ Pull Model
ollama run deepseek-r1

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run Application
streamlit run app.py

🐳 Run with Docker (Recommended)
docker build -t codemind .
docker run -p 8501:8501 codemind

Open in browser:
http://localhost:8501

---

## Supported Use Cases

- Explain and optimize DSA problems.
- Debug code (logical + runtime errors).
- Analyze time & space complexity.
- Improve algorithm design.
- Practice offline coding interviews.

❌ Non-technical queries are intentionally restricted.

---

## Design Decisions

🔹 Local Inference over Cloud APIs
Ensures:
- Data privacy.
- Zero dependency on external services.
- No recurring costs.

🔹 Coding-Only Prompt Constraint
- Improves response quality.
- Prevents misuse.
- Keeps system focused on technical tasks.

🔹 Streamlit UI
- Fast prototyping.
- Minimal frontend overhead.
- Easy local deployment.

🔹 Dockerization
- Environment consistency.
- Easy portability across systems.
- Simplified setup for recruiters and users.

---

## Limitations & Trade-offs

- Requires moderate hardware (recommended: 16 GB RAM).
- Performance depends on CPU/GPU availability.
- Higher latency compared to cloud APIs.
- No persistent memory (intentional for privacy).

---

## Performance Insights

- Avg latency: 2–10 seconds (hardware dependent).
- Handles large code inputs reliably.
- Optimized for offline usage, not real-time cloud speed.

---

## Tech Stack

- Python
- Streamlit
- Ollama
- DeepSeek-R1 LLM
- Docker

---

## Future Improvements

- Streaming responses (real-time token output).
- Chat history support.
- Hybrid mode (local + cloud fallback).
- Model selection (fast vs accurate).

---

📌 Author

Debanjan Deb
B.Tech (ECS), KIIT University
```
