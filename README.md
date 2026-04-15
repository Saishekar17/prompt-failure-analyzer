# 🧠 Prompt Failure Analyzer (Local AI System)

A FAANG-level AI system that detects, analyzes, and improves failed LLM outputs using **Ollama + FAISS + RAG + Streamlit** — fully local, no API cost.

---

## 📸 Results

### 🔍 Prompt & Bad output
![img](https://github.com/Saishekar17/prompt-failure-analyzer/blob/951eea845749036e00d87a378bfb2e590230355d/my2.png)

### 🛠 Failure Analysis & Improved Prompt
![img](https://github.com/Saishekar17/prompt-failure-analyzer/blob/a532ebc73b720e6c0744ba8d2c5aa831fe4525d7/my1.png)

### 📊 Scores & 📈 Improvement Trend
![img](assets/screenshot.png)

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
