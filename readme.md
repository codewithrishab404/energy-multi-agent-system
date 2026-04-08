# ⚡ Agentic Energy Assistant (RAG-Based Multi-Agent System)

## 📌 Overview

This project is a **multi-agent AI system** that analyzes unstructured power sector logs and answers user queries in natural language.

It uses a **Retrieval-Augmented Generation (RAG)** pipeline with local models to:

- Store and search logs semantically
- Retrieve relevant information
- Generate accurate answers

---

## 🧠 System Architecture

The system is divided into **3 agents**:

### 1️⃣ Data Agent

- Loads log files from directory
- Splits text into chunks
- Generates embeddings
- Stores data in vector database

### 2️⃣ Analysis Agent

- Converts user query into embedding
- Performs similarity search in vector DB
- Retrieves most relevant logs

### 3️⃣ Report Agent

- Takes retrieved logs as context
- Uses LLM to generate final answer

---

## 🔄 Workflow

User Query → Embedding → Vector Search → Context Retrieval → LLM → Final Answer

---

## 🛠️ Tech Stack

- Python
- Streamlit (UI)
- ChromaDB (Vector Database)
- Ollama (Local LLM + Embeddings)

---

## 🤖 Models Used

### 🔢 Embedding Model

- `nomic-embed-text-v2-moe`
- Purpose: Convert text → vectors for semantic search

### 💬 Chat Model

- `ministral-3:3b`
- Purpose: Generate final answers from retrieved logs

---

## 📂 Dataset

Unstructured log files (~1000 words each) representing:

- Transformer failure (North) - log1.txt
- Maintenance (South) - log2.txt
- Weather outage (West) - log3.txt
- Peak demand (East) - log4.txt
- Grid overload (Central) - log5.txt

---

## ▶️ How to Run the Project

### 1️⃣ Install Dependencies

```bash
pip install requirements.txt
```

---

### 2️⃣ Install & Run Ollama

Download from: https://ollama.com

Then pull models:

```bash
ollama pull nomic-embed-text-v2-moe
ollama pull ministral-3:3b
```

---

### 3️⃣ Run the App

```bash
streamlit run main.py
```

---

## ❓ Example Questions You Can Ask

### 🔍 Basic Queries

- Which region had the longest outage?
- What caused the power outage?
- Which region had maintenance?

### 📊 Analytical Queries

- Compare outage durations across regions
- Which outage was caused by weather?
- Which region had no outage?

### 🧠 Advanced Queries

- Summarize all power events
- Explain the major outage in the North region
- Which region handled peak demand successfully?

---

## ⚠️ Notes

- Embedding models (like `nomic-embed-text-v2-moe`) **cannot chat**
- Chat models (like `ministral-3:3b`) are used for answer generation
- Vector DB always returns closest match → filtering may be applied

---

## 🚀 Features

- Multi-agent architecture
- Semantic search using embeddings
- Local LLM (no API required)
- Handles unstructured data
- Context-aware responses

---

## 💬 Short Explanation

> “This project implements a multi-agent RAG system where data is embedded and stored in a vector database, retrieved via semantic search, and passed to an LLM for generating accurate responses.”

---

## 🏁 Conclusion

This system demonstrates how **AI + vector databases + LLMs** can be combined to build intelligent assistants for real-world data analysis.

---
