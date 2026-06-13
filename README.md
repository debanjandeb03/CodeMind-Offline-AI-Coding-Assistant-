```
# CodeMind – Offline AI Coding Assistant

## Overview

CodeMind is a privacy-first AI coding assistant designed for programming, DSA, debugging, and technical interview preparation.

Unlike traditional cloud-based AI tools, CodeMind runs entirely on local infrastructure using Ollama and DeepSeek-Coder, ensuring complete data privacy, zero API costs, and full control over inference.

The project has evolved from a simple Streamlit application into a production-style AI system featuring a FastAPI backend, service-oriented architecture, Docker containerization, and Docker Compose orchestration.

---

## What's New in the Latest Version

### FastAPI Backend Integration

* Introduced a dedicated FastAPI backend layer.
* Clean REST API endpoints for AI interactions.
* Separation between frontend and backend responsibilities.

### Layered Architecture

Implemented a scalable architecture with:

* API Routes Layer
* Service Layer
* Provider Layer
* Schema Layer
* Configuration Layer

This improves maintainability, testability, and extensibility.

### Pydantic Schema Validation

Added request and response validation using Pydantic schemas to ensure reliable API communication.

### Health Monitoring Endpoints

Added production-ready endpoints:

```http
GET /health
GET /model-info
```

Used for monitoring, debugging, deployment verification, and cloud readiness.

### Docker Multi-Container Setup

Migrated from a single Docker container to:

* Frontend Container (Streamlit)
* Backend Container (FastAPI)

Managed through Docker Compose.

### Configuration Management

Introduced environment-based configuration using:

```env
MODEL_NAME
MODEL_VERSION
OLLAMA_URL
SERVICE_NAME
```

---

## Key Features

* Fully Offline AI Assistant
* Privacy-Focused Architecture
* Coding-Only AI Responses
* DeepSeek-Coder Integration
* FastAPI Backend
* Streamlit Frontend
* Dockerized Deployment
* Docker Compose Support
* Health Monitoring APIs
* Model Metadata APIs
* Structured Response Format

---

## Architecture

```text
User (Browser)
        │
        ▼
Streamlit Frontend
        │
        ▼
FastAPI Backend
        │
        ▼
Service Layer
        │
        ▼
Provider Layer
        │
        ▼
Ollama Runtime
        │
        ▼
DeepSeek-Coder
```

---

## Project Structure

```text
CodeMind-Offline-AI-Coding-Assistant
│
├── api/
│   └── routes/
│       └── chat.py
│
├── core/
│   └── config.py
│
├── prompts/
│   └── prompt.py
│
├── providers/
│   └── ollama_provider.py
│
├── schemas/
│   └── chat_schema.py
│
├── services/
│   └── llm_service.py
│
├── app.py
├── main.py
│
├── Dockerfile.backend
├── Dockerfile.frontend
├── docker-compose.yml
│
├── requirements.txt
├── .env.example
└── README.md
```

---

## API Endpoints

### Chat Endpoint

```http
POST /chat
```

Request:

```json
{
  "prompt": "Write Binary Search in Python"
}
```

Response:

```json
{
  "response": "Generated AI response"
}
```

---

### Health Check

```http
GET /health
```

Response:

```json
{
  "status": "healthy"
}
```

---

### Model Information

```http
GET /model-info
```

Response:

```json
{
  "model_name": "DeepSeek-Coder",
  "model_version": "1.0.0",
  "provider": "ollama",
  "status": "loaded"
}
```

---

## Setup

### Install Ollama

```bash
ollama --version
```

### Download Model

```bash
ollama run deepseek-coder
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Backend

```bash
uvicorn main:app --reload
```

### Run Frontend

```bash
streamlit run app.py
```

---

## Docker Deployment

### Build and Run

```bash
docker compose up --build
```

### Access Application

Frontend:

```text
http://localhost:8501
```

Backend Swagger Docs:

```text
http://localhost:8000/docs
```

---

## Tech Stack

* Python
* FastAPI
* Streamlit
* Ollama
* DeepSeek-Coder
* Docker
* Docker Compose
* Pydantic

---

## Future Improvements

* Streaming Token Responses
* Conversation History
* User Authentication
* Multiple Model Support
* Cloud Deployment on AWS EC2
* CI/CD Pipeline
* Monitoring & Logging

---

## Author

**Debanjan Deb**

B.Tech (Electronics and Computer Science Engineering)

KIIT University

```
