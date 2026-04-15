# 🧠 Prompt Failure Analyzer (Local AI System)

A FAANG-level AI system that detects, analyzes, and improves failed LLM outputs using **Ollama + FAISS + RAG + Streamlit** — fully local, no API cost.

---

## 🚀 Features

- 🔍 Detects LLM failure types:
  - Hallucination
  - Missing Context
  - Bad Reasoning
  - Ambiguous Prompt

- 🛠 Automatically improves prompts
- 🤖 Generates better outputs
- 📊 Scores improvement (%)
- 🧠 Learns from past failures (FAISS Vector DB)
- 🎨 Interactive UI with Streamlit

---

## 🧱 Tech Stack

- Python
- Ollama (Local LLM)
- FAISS (Vector Database)
- Sentence Transformers
- FastAPI
- Streamlit

---

## ⚙️ System Architecture

User Input → Failure Analyzer → Prompt Improver → LLM (Ollama) → Evaluator → Memory (FAISS)

---

## 🖥️ Demo

### Input:
Prompt: `Explain AI`  
Bad Output: `AI is something`

### Output:
- Failure: Missing Context  
- Improved Prompt: Detailed version  
- Score Improvement: +65%

---

## ▶️ Run Locally

### 1. Install dependencies
```bash
pip install -r requirements.txt